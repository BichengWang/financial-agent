"""REST transport integration: paper settlement and an authorized live session."""

from dataclasses import replace
from datetime import date, datetime, time, timezone
from pathlib import Path
from typing import Any, Literal

import pytest

from financial_agent.quant.data import CsvProvider
from financial_agent.quant.execution import AlpacaBroker, Journal
from financial_agent.quant.execution.alpaca import LIVE_URL
from financial_agent.quant.runner import TradingConfig, authorize_live, run_session
from .conftest import ny_clock
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
        for symbol, position in self.positions.items():
            position["current_price"] = float(data.close.iloc[-1][symbol])


def test_alpaca_paper_round_trip_and_no_repeat_lookups(
    config: TradingConfig, first_day: date
) -> None:
    config = replace(config, broker_kind="alpaca")
    transport = Exchange()
    broker = AlpacaBroker("key", "secret", session=transport)
    first = run_session(config, today=first_day, broker=broker, now=ny_clock(first_day))
    assert first.status == "TRADED", first.reasons
    rerun = run_session(config, today=first_day, broker=broker, now=ny_clock(first_day))
    assert rerun.status == "NO_CHANGE"
    assert sum(method == "POST" for method, _ in transport.calls) == len(first.orders)
    transport.fill(config, first_day)
    day = date(2020, 6, 9)
    second = run_session(config, today=day, broker=broker, now=ny_clock(day))
    assert second.status != "HALTED", second.reasons
    assert second.fills
    assert all(abs(f.price / f.reference_price - 1) < 0.000501 for f in second.fills)
    before = sum(url.endswith("by_client_order_id") for _, url in transport.calls)
    again = run_session(config, today=day, broker=broker, now=ny_clock(day))
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
    report = run_session(
        live, today=first_day, broker=broker, environ=environ, now=ny_clock(first_day)
    )
    assert report.status == "TRADED", report.reasons
    assert any(method == "POST" for method, _ in transport.calls)
    assert all(url.startswith(LIVE_URL) for _, url in transport.calls)
    journal = Journal(config.state_dir / "journal.jsonl")
    assert journal.events(["live_authorized"])
    assert "secret" not in journal.path.read_text()


@pytest.mark.parametrize("observed", [False, True])
def test_alpaca_prior_intent_recovery(
    config: TradingConfig, first_day: date, observed: bool
) -> None:
    from financial_agent.quant.risk import Order
    from financial_agent.quant.runner.report import json_value

    config = replace(config, broker_kind="alpaca")
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    order = Order("SPY", "buy", 10, client_order_id="old-intent")
    journal = Journal(config.state_dir / "journal.jsonl")
    journal.append(
        "submission_intent",
        {"session": str(first_day), "order": json_value(order), "reference_price": 100},
    )
    if observed:
        broker.submit(order)
        exchange.fill(config, first_day)
    day = date(2020, 6, 9)
    report = run_session(config, today=day, broker=broker, now=ny_clock(day))
    assert report.status != "HALTED", report.reasons
    if observed:
        assert any(f.client_order_id == order.client_order_id for f in report.fills)
        assert not journal.events(["submission_abandoned"])
    else:
        assert (
            journal.events(["submission_abandoned"])[0].payload["client_order_id"]
            == "old-intent"
        )
        assert "old-intent" not in exchange.orders


def test_alpaca_lookup_failure_halts_then_recovers(
    config: TradingConfig, first_day: date
) -> None:
    from financial_agent.quant.execution import BrokerError
    from financial_agent.quant.risk import Order
    from financial_agent.quant.runner.report import json_value

    class BrokenLookup(Exchange):
        def request(self, method: str, url: str, **kwargs: Any) -> Response:
            if url.endswith("/v2/orders:by_client_order_id"):
                raise BrokerError("lookup interrupted")
            return super().request(method, url, **kwargs)

    config = replace(config, broker_kind="alpaca")
    journal = Journal(config.state_dir / "journal.jsonl")
    journal.append(
        "submission_intent",
        {
            "session": str(first_day),
            "order": json_value(Order("SPY", "buy", 10, client_order_id="old-intent")),
            "reference_price": 100,
        },
    )
    broken = AlpacaBroker("key", "secret", session=BrokenLookup())
    day = date(2020, 6, 9)
    report = run_session(config, today=day, broker=broken, now=ny_clock(day))
    assert report.status == "HALTED"
    assert not journal.events(["submission_abandoned", "submitted"])
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    report = run_session(config, today=day, broker=broker, now=ny_clock(day))
    assert report.status == "TRADED", report.reasons
    assert journal.events(["submission_abandoned"])


@pytest.mark.parametrize("kind", ["paper", "alpaca"])
def test_live_requires_twenty_broker_backed_paper_sessions(
    config: TradingConfig, tmp_path: Path, kind: Literal["paper", "alpaca"]
) -> None:
    from datetime import timedelta
    from financial_agent.harness.market_calendar import session
    from financial_agent.quant.execution import PaperBroker
    from financial_agent.quant.runner import PromotionError

    config = replace(
        config,
        broker_kind=kind,
        backtest=replace(config.backtest, cash_buffer=0.10, drift_threshold=0),
    )
    cert = certificate(config, tmp_path)
    exchange = Exchange()
    broker = (
        AlpacaBroker("key", "secret", session=exchange)
        if kind == "alpaca"
        else PaperBroker(
            config.state_dir / "paper.json",
            costs=config.backtest.costs,
            initial_cash=config.initial_cash,
        )
    )
    day = date(2020, 6, 8)
    previous: date | None = None
    completed = 0
    while completed < 20:
        if session(day).trading_day:
            if kind == "alpaca" and previous is not None:
                exchange.fill(config, previous)
            report = run_session(config, today=day, broker=broker, now=ny_clock(day))
            assert report.status in ("TRADED", "NO_CHANGE"), report.reasons
            previous = day
            completed += 1
        day += timedelta(days=1)
    journal = Journal(config.state_dir / "journal.jsonl")
    assert {e.payload["broker_kind"] for e in journal.events(["session_outcome"])} == {
        kind
    }
    if kind == "paper":
        with pytest.raises(PromotionError, match="paper sessions 0"):
            authorize_live(
                config,
                certificate_path=cert,
                paper_journal_path=journal.path,
                environ={"FA_QUANT_ALLOW_LIVE": "1"},
            )
    else:
        assert (
            authorize_live(
                config,
                certificate_path=cert,
                paper_journal_path=journal.path,
                environ={"FA_QUANT_ALLOW_LIVE": "1"},
            ).strategy
            == config.strategy_name
        )


@pytest.mark.parametrize(
    ("at", "status"),
    [
        (time(8, 45), "TRADED"),
        (time(9, 24, 59), "TRADED"),
        (time(9, 25), "HALTED"),
        (time(9, 26), "HALTED"),
    ],
)
def test_opening_auction_submission_window(
    config: TradingConfig, first_day: date, at: time, status: str
) -> None:
    config = replace(config, broker_kind="alpaca")
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    clock = ny_clock(first_day, at)
    report = run_session(config, today=first_day, broker=broker, now=clock)
    assert report.status == status, report.reasons
    journal = Journal(config.state_dir / "journal.jsonl")
    assert journal.events(["reconcile"])
    if status == "HALTED":
        assert report.reasons == [
            f"submission window closed: observed 2020-06-08 {at:%H:%M:%S} "
            "America/New_York; orders for 2020-06-08 must be submitted that day "
            "before 09:25"
        ]
        assert not journal.events(["submission_intent", "submitted"])
        assert not exchange.orders
    else:
        assert report.orders and len(exchange.orders) == len(report.orders)


def test_replayed_session_against_broker_halts(
    config: TradingConfig, first_day: date
) -> None:
    config = replace(config, broker_kind="alpaca")
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    # The default clock is the system clock, never 2020-06-08 in New York.
    report = run_session(config, today=first_day, broker=broker)
    assert report.status == "HALTED"
    assert report.reasons[0].startswith("submission window closed")
    assert not Journal(config.state_dir / "journal.jsonl").events(["submission_intent"])
    assert not exchange.orders


def test_naive_clock_fails_closed(config: TradingConfig, first_day: date) -> None:
    config = replace(config, broker_kind="alpaca")
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    naive = datetime.combine(first_day, time(8, 45))
    report = run_session(config, today=first_day, broker=broker, now=lambda: naive)
    assert report.status == "HALTED"
    assert report.reasons == ["session failed (ValueError)"]
    assert not exchange.orders


def test_cutoff_crossed_mid_plan_stops_before_next_submit(
    config: TradingConfig, first_day: date
) -> None:
    config = replace(config, broker_kind="alpaca")
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    early = ny_clock(first_day, time(9, 24, 59))()
    late = ny_clock(first_day, time(9, 25))()
    # One read before journaling intents, one before the first submission.
    reads = iter([early, early])
    report = run_session(
        config, today=first_day, broker=broker, now=lambda: next(reads, late)
    )
    assert report.status == "HALTED"
    assert "observed 2020-06-08 09:25:00" in report.reasons[0]
    assert len(report.orders) > 1
    journal = Journal(config.state_dir / "journal.jsonl")
    intents = journal.events(["submission_intent"])
    assert len(intents) == len(report.orders)
    assert len(journal.events(["submitted"])) == len(exchange.orders) == 1
    # A same-day retry after the cutoff cannot submit the remaining intents.
    retry = run_session(
        config, today=first_day, broker=broker, now=ny_clock(first_day, time(9, 40))
    )
    assert retry.status == "HALTED"
    assert retry.reasons[0].startswith("submission window closed")
    assert len(exchange.orders) == 1
    # The next session abandons them instead of sending them to a later auction.
    exchange.fill(config, first_day)
    day = date(2020, 6, 9)
    report = run_session(config, today=day, broker=broker, now=ny_clock(day))
    assert report.status != "HALTED", report.reasons
    abandoned = {
        e.payload["client_order_id"] for e in journal.events(["submission_abandoned"])
    }
    assert len(abandoned) == len(intents) - 1
    assert not abandoned & set(exchange.orders)


def test_late_run_on_off_cadence_day_is_no_change(config: TradingConfig) -> None:
    config = replace(
        config,
        broker_kind="alpaca",
        backtest=replace(config.backtest, rebalance="weekly"),
    )
    exchange = Exchange()
    broker = AlpacaBroker("key", "secret", session=exchange)
    day = date(2020, 6, 9)
    report = run_session(
        config, today=day, broker=broker, now=ny_clock(day, time(11, 45))
    )
    assert report.status == "NO_CHANGE"
    assert report.reasons == ["outside rebalance calendar"]
    assert not exchange.orders
