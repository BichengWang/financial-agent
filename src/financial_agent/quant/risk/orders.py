"""Immutable execution contracts and deterministic backtest-parity order planning."""

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime
from hashlib import sha256
import math
from types import MappingProxyType
from typing import Literal
import pandas as pd  # type: ignore[import-untyped]

from financial_agent.quant.backtest import BacktestConfig
from financial_agent.quant.portfolio import rebalance_deltas


@dataclass(frozen=True)
class Order:
    """Positive share quantity; client ID identifies one session's planned trade."""

    symbol: str
    side: Literal["buy", "sell"]
    qty: float
    order_type: str = "market"
    time_in_force: str = "opg"
    limit_price: float | None = None
    client_order_id: str = field(kw_only=True)


@dataclass(frozen=True)
class Position:
    """Share quantity and per-share prices in account currency."""

    symbol: str
    qty: float
    avg_price: float
    market_price: float

    @property
    def market_value(self) -> float:
        return self.qty * self.market_price


@dataclass(frozen=True)
class AccountSnapshot:
    """Broker observation; positions are copied into an immutable mapping."""

    cash: float
    equity: float
    positions: Mapping[str, Position]
    as_of: datetime

    def __post_init__(self) -> None:
        object.__setattr__(self, "positions", MappingProxyType(dict(self.positions)))

    def weights(self) -> dict[str, float]:
        """Signed marked position values divided by positive account equity."""
        if not math.isfinite(self.equity) or self.equity <= 0:
            raise ValueError("equity must be positive")
        return {s: p.market_value / self.equity for s, p in self.positions.items()}


def plan_orders(
    targets: Mapping[str, float] | pd.Series,
    account: AccountSnapshot,
    prices: Mapping[str, float] | pd.Series,
    *,
    session: str,
    strategy: str,
    config: BacktestConfig,
) -> list[Order]:
    """Use shared drift, rounding and notional rules; sorted sells precede buys."""
    deltas = rebalance_deltas(
        targets,
        {s: p.qty for s, p in account.positions.items()},
        prices,
        account.equity,
        drift_threshold=config.drift_threshold,
        fractional=config.fractional_shares,
        min_trade_notional=config.min_trade_notional,
    )
    orders = []
    for symbol, delta in sorted(
        deltas.items(), key=lambda item: (item[1] > 0, item[0])
    ):
        side: Literal["buy", "sell"] = "buy" if delta > 0 else "sell"
        qty = abs(delta)
        digest = sha256(
            f"{strategy}|{session}|{symbol}|{side}|{qty}".encode()
        ).hexdigest()
        orders.append(Order(symbol, side, qty, client_order_id="fa-" + digest[:24]))
    return orders
