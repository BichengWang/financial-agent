"""Persistent long-only paper execution at the next observed session open."""

from contextlib import contextmanager
from collections.abc import Iterator
from dataclasses import asdict, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import fcntl
import json
import math
import os
import tempfile

from financial_agent.quant.backtest import CostModel
from financial_agent.quant.data import MarketData
from financial_agent.quant.risk.orders import AccountSnapshot, Order, Position
from .broker import BrokerError, Fill, OrderAck, validate_order


class PaperBroker:
    """Whole-share market OPG orders; partial fills terminate at the auction."""

    name = "paper"
    is_live = False

    def __init__(
        self, state_path: str | Path, *, costs: CostModel, initial_cash: float
    ) -> None:
        if not math.isfinite(initial_cash) or initial_cash < 0:
            raise ValueError("initial_cash must be finite and nonnegative")
        self.state_path = Path(state_path)
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.costs = costs
        self._state: dict[str, Any] = dict(
            cash=initial_cash, positions={}, orders={}, fills=[], last_session=None
        )
        with self._locked():
            if not self.state_path.exists():
                self._save()

    @contextmanager
    def _locked(self) -> Iterator[None]:
        with self.state_path.with_name(self.state_path.name + ".lock").open(
            "a"
        ) as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            if self.state_path.exists():
                try:
                    self._state = json.loads(self.state_path.read_text())
                except (ValueError, OSError):
                    raise BrokerError("cannot read paper state") from None
            yield

    def _save(self) -> None:
        fd, temporary = tempfile.mkstemp(dir=self.state_path.parent)
        try:
            with os.fdopen(fd, "w") as handle:
                json.dump(self._state, handle, sort_keys=True, allow_nan=False)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.state_path)
            directory = os.open(self.state_path.parent, os.O_RDONLY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    @staticmethod
    def _ack(record: dict[str, Any]) -> OrderAck:
        fields = dict(record)
        fields["submitted_at"] = datetime.fromisoformat(fields["submitted_at"])
        return OrderAck(**fields)

    def _store(self, ack: OrderAck) -> None:
        record = asdict(ack)
        record["submitted_at"] = ack.submitted_at.isoformat()
        self._state["orders"][ack.client_order_id] = record

    def submit(self, order: Order) -> OrderAck:
        """Persist once per client ID; only market OPG whole-share orders qualify."""
        with self._locked():
            existing = self._state["orders"].get(order.client_order_id)
            if existing is not None:
                return self._ack(existing)
            validate_order(order)
            if (
                order.order_type != "market"
                or order.time_in_force != "opg"
                or not float(order.qty).is_integer()
            ):
                raise BrokerError(
                    "paper execution requires whole-share market OPG orders"
                )
            ack = OrderAck(
                order.client_order_id,
                "paper-" + order.client_order_id,
                order.symbol,
                order.side,
                order.qty,
                "pending",
                0.0,
                None,
                datetime.now(timezone.utc),
            )
            self._store(ack)
            self._save()
            return ack

    def open_orders(self) -> list[OrderAck]:
        with self._locked():
            return self._pending()

    def _pending(self) -> list[OrderAck]:
        return [
            self._ack(v)
            for v in self._state["orders"].values()
            if v["status"] == "pending"
        ]

    def cancel_all(self) -> int:
        with self._locked():
            pending = self._pending()
            for ack in pending:
                self._store(replace(ack, status="canceled"))
            self._save()
            return len(pending)

    def account(self) -> AccountSnapshot:
        """Equity uses the most recently settled close, not order reference prices."""
        with self._locked():
            positions = {s: Position(**p) for s, p in self._state["positions"].items()}
            last = self._state["last_session"]
            return AccountSnapshot(
                self._state["cash"],
                self._state["cash"] + sum(p.market_value for p in positions.values()),
                positions,
                (
                    datetime.fromisoformat(last).replace(tzinfo=timezone.utc)
                    if last
                    else datetime.now(timezone.utc)
                ),
            )

    def settle(self, data: MarketData) -> list[Fill]:
        """Fill at first session strictly after last_session; mark at latest close."""
        with self._locked():
            last = self._state["last_session"]
            sessions = [
                s for s in data.sessions if last is None or s.isoformat() > last
            ]
            if not sessions:
                return []
            pending = sorted(self._pending(), key=lambda a: (a.side == "buy", a.symbol))
            required = set(self._state["positions"]) | {a.symbol for a in pending}
            if not required.issubset(data.symbols):
                raise BrokerError("market data is missing execution or held symbols")
            opening, closing = sessions[0], data.sessions[-1]
            # Validate every required price before mutating any account state.
            for symbol in required:
                for price in (
                    data.open.loc[opening, symbol],
                    data.close.loc[closing, symbol],
                ):
                    if not math.isfinite(float(price)) or float(price) <= 0:
                        raise BrokerError("market prices must be finite and positive")
            fills = []
            for ack in pending:
                reference = float(data.open.loc[opening, ack.symbol])
                price = self.costs.fill_price(ack.side, reference)
                position = self._state["positions"].get(ack.symbol)
                held = position["qty"] if position else 0.0
                qty = min(ack.qty, held) if ack.side == "sell" else ack.qty
                if ack.side == "buy":
                    low, high = 0, int(qty)
                    while low < high:
                        mid = (low + high + 1) // 2
                        if (
                            mid * price + self.costs.commission(mid, price)
                            <= self._state["cash"]
                        ):
                            low = mid
                        else:
                            high = mid - 1
                    qty = float(low)
                fee = self.costs.commission(qty, price)
                if qty:
                    self._state["cash"] += (
                        1 if ack.side == "sell" else -1
                    ) * qty * price - fee
                    remaining = held + (qty if ack.side == "buy" else -qty)
                    if remaining:
                        average = (
                            (
                                (held * position["avg_price"] if position else 0.0)
                                + qty * price
                            )
                            / remaining
                            if ack.side == "buy"
                            else position["avg_price"]
                        )
                        self._state["positions"][ack.symbol] = asdict(
                            Position(ack.symbol, remaining, average, price)
                        )
                    else:
                        self._state["positions"].pop(ack.symbol, None)
                    fill = Fill(
                        ack.client_order_id,
                        ack.symbol,
                        ack.side,
                        qty,
                        price,
                        reference,
                        fee,
                        opening.isoformat(),
                    )
                    fills.append(fill)
                    self._state["fills"].append(asdict(fill))
                reason = (
                    None
                    if qty == ack.qty
                    else (
                        "insufficient cash"
                        if ack.side == "buy"
                        else "insufficient holdings"
                    )
                )
                self._store(
                    replace(
                        ack,
                        status=(
                            "filled"
                            if qty == ack.qty
                            else ("partially_filled" if qty else "rejected")
                        ),
                        filled_qty=qty,
                        filled_avg_price=price if qty else None,
                        reason=reason,
                    )
                )
            for symbol, position in self._state["positions"].items():
                position["market_price"] = float(data.close.loc[closing, symbol])
            self._state["last_session"] = closing.isoformat()
            self._save()
            return fills
