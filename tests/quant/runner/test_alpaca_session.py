"""REST transport integration: paper settlement and an authorized live session."""

from dataclasses import replace
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import pytest

from financial_agent.quant.data import CsvProvider
from financial_agent.quant.execution import AlpacaBroker, Journal
from financial_agent.quant.execution.alpaca import LIVE_URL
from financial_agent.quant.runner import TradingConfig, authorize_live, run_session
from .test_promotion import certificate, paper_evidence


class Response:
    def __init__(self, status: int, value: Any) -> None:
        self.status_code = status
        self.value = value

    def json(self) -> Any:
        return self.value


class Exchange:
    """Small fake REST exchange; actual AlpacaBroker owns request parsing."""

    def __init__(self) -> None:
        self.orders: dict[str, dict[str, Any]] = {}
        self.positions: dict[str, dict[str, Any]] = {}
        self.cash = 100000.0
        self.calls: list[tuple[str, str]] = []

    def request(self, method: str, url: str, **kwargs: Any) -> Response:
        self.calls.append((method, url))
        if method == "POST":
            body = kwargs["json"]
            client = body["client_order_id"]
            if client in self.orders:
                return Response(422, {})
            order = {
                **body,
                "id": client,
                "status": "new",
                "filled_qty": "0",
                "filled_avg_price": None,
                "submitted_at": datetime.now(timezone.utc).isoformat(),
            }
            self.orders[client] = order
            return Response(200, order)
        if url.endswith("/v2/orders:by_client_order_id"):
            found = self.orders.get(kwargs["params"]["client_order_id"])
            return Response(200, found) if found else Response(404, {})
        if url.endswith("/v2/account"):
            equity = self.cash + sum(
                float(p["qty"]) * float(p["current_price"])
                for p in self.positions.values()
            )
            return Response(200, {"cash": self.cash, "equity": equity})
        if url.endswith("/v2/positions"):
            return Response(200, list(self.positions.values()))
        if url.endswith("/v2/orders"):
            return Response(
                200, [o for o in self.orders.values() if o["status"] == "new"]
            )
        raise AssertionError(url)

    def fill(self, config: TradingConfig, day: date) -> None:
        assert config.csv_dir is not None
        data = CsvProvider(config.csv_dir).fetch(config.symbols, config.data_start, day)
        for order in self.orders.values():
            if order["status"] != "new":
                continue
            symbol = order["symbol"]
            reference = float(data.open.iloc[-1][symbol])
            price = config.backtest.costs.fill_price(order["side"], reference)
            qty = float(order["qty"])
            signed = qty if order["side"] == "buy" else -qty
            self.cash -= signed * price
            held = float(self.positions.get(symbol, {}).get("qty", 0))
            self.positions[symbol] = {
                "symbol": symbol,
                "qty": held + signed,
                "avg_entry_price": price,
                "current_price": float(data.close.iloc[-1][symbol]),
            }
            order.update(status="filled", filled_qty=qty, filled_avg_price=price)


def test_alpaca_paper_round_trip_and_no_repeat_lookups(
    config: TradingConfig, first_day: date
) -> None:
    config = replace(config, broker_kind="alpaca")
    transport = Exchange()
    broker = AlpacaBroker("key", "secret", session=transport)
    first = run_session(config, today=first_day, broker=broker)
    assert first.status == "TRADED", first.reasons
    assert run_session(config, today=first_day, broker=broker).status == "NO_CHANGE"
    assert sum(method == "POST" for method, _ in transport.calls) == len(first.orders)
    transport.fill(config, first_day)
    second = run_session(config, today=date(2020, 6, 9), broker=broker)
    assert second.status != "HALTED", second.reasons
    assert second.fills
    assert all(abs(f.price / f.reference_price - 1) < 0.000501 for f in second.fills)
    before = sum(url.endswith("by_client_order_id") for _, url in transport.calls)
    again = run_session(config, today=date(2020, 6, 9), broker=broker)
    assert again.status != "HALTED", again.reasons
    after = sum(url.endswith("by_client_order_id") for _, url in transport.calls)
    # Filled orders are not polled forever; only today's pending orders are read.
    assert after - before <= len(second.orders)


def test_live_authorization_with_real_gate_and_fake_transport(
    config: TradingConfig,
    first_day: date,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cert = certificate(config, tmp_path)
    evidence = paper_evidence(config, tmp_path / "evidence.jsonl")
    live = replace(
        config,
        mode="live",
        broker_kind="alpaca",
        certificate_path=cert,
        paper_journal_path=evidence.path,
    )
    environ = {"FA_QUANT_ALLOW_LIVE": "1"}
    monkeypatch.setenv("FA_QUANT_ALLOW_LIVE", "1")
    grant = authorize_live(live, environ=environ)
    transport = Exchange()
    broker = AlpacaBroker(
        "key", "secret", session=transport, base_url=LIVE_URL, live_authorization=grant
    )
    report = run_session(live, today=first_day, broker=broker, environ=environ)
    assert report.status == "TRADED", report.reasons
    assert any(method == "POST" for method, _ in transport.calls)
    assert all(url.startswith(LIVE_URL) for _, url in transport.calls)
    journal = Journal(config.state_dir / "journal.jsonl")
    assert journal.events(["live_authorized"])
    assert "secret" not in journal.path.read_text()
