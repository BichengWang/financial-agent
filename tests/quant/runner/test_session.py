"""Whole session behavior: fills, retries, persistent stops, and crash recovery."""

from dataclasses import replace
from datetime import date, timedelta
import json
from pathlib import Path

import pytest

from financial_agent.quant.data import CsvProvider
from financial_agent.quant.execution import Journal, PaperBroker
from financial_agent.quant.risk import KillSwitch, RiskState
from financial_agent.quant.runner import TradingConfig, run_session
from financial_agent.quant.runner.session import session_lock


def csv(config: TradingConfig) -> CsvProvider:
    assert config.csv_dir is not None
    return CsvProvider(config.csv_dir)


def paper(config: TradingConfig) -> PaperBroker:
    return PaperBroker(
        config.state_dir / "paper.json",
        costs=config.backtest.costs,
        initial_cash=config.initial_cash,
    )


def test_multiple_sessions_settle_reconcile_and_retry(
    config: TradingConfig, first_day: date
) -> None:
    first = run_session(config, today=first_day)
    assert first.status == "TRADED", first.reasons
    assert first.decision_session == "2020-06-05"
    assert first.orders and not first.fills
    assert first.account and not first.account.positions
    first_path = config.state_dir / "reports/2020-06-08.json"
    first_bytes = first_path.read_bytes()
    broker = paper(config)
    count = len(broker.open_orders())
    again = run_session(config, today=first_day)
    assert again.status == "NO_CHANGE"
    assert first_path.read_bytes() == first_bytes
    rerun = json.loads((config.state_dir / "reports/2020-06-08.2.json").read_text())
    assert rerun["status"] == "NO_CHANGE"
    assert (config.state_dir / "reports/2020-06-08.2.md").exists()
    run_session(config, today=first_day)
    assert (config.state_dir / "reports/2020-06-08.3.json").exists()
    assert first_path.read_bytes() == first_bytes
    assert len(broker.open_orders()) == count
    second = run_session(config, today=first_day + timedelta(days=1))
    assert second.status in ("TRADED", "NO_CHANGE"), second.reasons
    assert second.fills and second.account and second.account.positions
    assert all(f.session[:10] == "2020-06-08" for f in second.fills)
    source = csv(config).fetch(config.symbols, config.data_start, date(2020, 6, 8))
    assert all(
        f.reference_price == source.open.loc["2020-06-08", f.symbol]
        for f in second.fills
    )
    assert Journal(config.state_dir / "journal.jsonl").verify().ok
    report = json.loads((config.state_dir / "reports/2020-06-09.json").read_text())
    assert report["actual_weights"]
    assert "drawdown_utilization" in report["risk"]


@pytest.mark.parametrize("today", [date(2020, 6, 6), date(2020, 7, 3)])
def test_nontrading_dates_do_not_initialize_broker(
    config: TradingConfig, today: date
) -> None:
    assert run_session(config, today=today).status == "NO_SESSION"
    assert not (config.state_dir / "paper.json").exists()


def test_preview_does_not_submit_or_overwrite_session_report(
    config: TradingConfig, first_day: date
) -> None:
    report = run_session(config, today=first_day, dry_run=True)
    assert report.orders and report.dry_run
    assert not paper(config).open_orders()
    assert not (config.state_dir / f"reports/{first_day}.json").exists()
    assert (config.state_dir / f"reports/{first_day}.preview.json").exists()
    assert run_session(config, today=first_day).status == "TRADED"


def test_stale_data_halts_without_submission(
    config: TradingConfig, first_day: date, tmp_path: Path
) -> None:
    source = csv(config).fetch(config.symbols, config.data_start, date(2020, 6, 4))
    from financial_agent.quant.data.providers import write_csv

    write_csv(source, tmp_path / "stale")
    report = run_session(
        config, today=first_day, provider=CsvProvider(tmp_path / "stale")
    )
    assert report.status == "HALTED"
    assert any("STALE" in r for r in report.reasons)
    assert not (config.state_dir / "paper.json").exists()


def test_drawdown_engages_persistent_kill(
    config: TradingConfig, first_day: date
) -> None:
    config.state_dir.mkdir()
    RiskState(200000, 100000, first_day.isoformat()).save(
        config.state_dir / "risk_state.json"
    )
    report = run_session(config, today=first_day)
    assert report.status == "HALTED"
    assert KillSwitch(config.state_dir).engaged()
    assert not paper(config).open_orders()
    assert run_session(config, today=first_day).reasons == ["kill switch engaged"]


def test_unexplained_position_halts(config: TradingConfig, first_day: date) -> None:
    broker = paper(config)
    state = json.loads(broker.state_path.read_text())
    state["positions"]["SPY"] = {
        "symbol": "SPY",
        "qty": 1,
        "avg_price": 100,
        "market_price": 100,
    }
    broker.state_path.write_text(json.dumps(state))
    report = run_session(config, today=first_day, broker=broker)
    assert report.status == "HALTED"
    assert report.reasons == ["reconciliation break"]
    assert not broker.open_orders()


def test_tamper_lock_and_stale_metadata(config: TradingConfig, first_day: date) -> None:
    with session_lock(config.state_dir):
        assert run_session(config, today=first_day).status == "HALTED"
    (config.state_dir / "session.lock").write_text("999999999")
    assert run_session(config, today=first_day).status == "TRADED"
    journal = config.state_dir / "journal.jsonl"
    journal.write_text(journal.read_text() + "{}\n")
    count = len(paper(config).open_orders())
    report = run_session(config, today=first_day + timedelta(days=1))
    assert report.status == "HALTED"
    assert report.reasons == ["journal verification failed"]
    assert len(paper(config).open_orders()) == count


def test_interrupted_settlement_recovers_authorized_fills(
    config: TradingConfig, first_day: date
) -> None:
    assert run_session(config, today=first_day).status == "TRADED"
    broker = paper(config)
    data = csv(config).fetch(config.symbols, config.data_start, first_day)
    assert broker.settle(data)
    report = run_session(config, today=first_day + timedelta(days=1), broker=broker)
    assert report.status != "HALTED", report.reasons
    assert report.fills and report.account and report.account.positions
    retry = run_session(config, today=first_day + timedelta(days=1), broker=broker)
    assert not retry.fills


def test_live_without_evidence_never_submits(
    config: TradingConfig, first_day: date
) -> None:
    live = replace(config, mode="live", broker_kind="alpaca")
    report = run_session(live, today=first_day, broker=paper(config), environ={})
    assert report.status == "HALTED"
    assert len(report.reasons) >= 4
    assert not paper(config).open_orders()


def test_daily_loss_breach(config: TradingConfig, first_day: date) -> None:
    config.state_dir.mkdir()
    RiskState(100000, 110000, first_day.isoformat()).save(
        config.state_dir / "risk_state.json"
    )
    report = run_session(config, today=first_day)
    assert report.status == "HALTED"
    assert any("max_daily_loss_pct" in r for r in report.reasons)
    assert KillSwitch(config.state_dir).engaged()


def test_bad_prices_halt_before_broker_sync(
    config: TradingConfig, first_day: date
) -> None:
    assert config.csv_dir is not None
    import pandas as pd  # type: ignore[import-untyped]

    source = config.csv_dir / "SPY.csv"
    frame = pd.read_csv(source)
    frame.loc[frame["date"] == "2020-06-05", "open"] = 0
    frame.to_csv(source, index=False)
    report = run_session(config, today=first_day)
    assert report.status == "HALTED"
    assert any("NONPOSITIVE" in r for r in report.reasons)
    assert not (config.state_dir / "paper.json").exists()


def test_external_error_is_redacted(config: TradingConfig, first_day: date) -> None:
    from collections.abc import Sequence
    from financial_agent.quant.data import MarketData

    class BrokenProvider:
        def fetch(self, symbols: Sequence[str], start: date, end: date) -> MarketData:
            raise ValueError("sensitive-credential-value")

    report = run_session(config, today=first_day, provider=BrokenProvider())
    assert report.status == "HALTED"
    assert "sensitive-credential-value" not in str(report)
    assert (
        "sensitive-credential-value"
        not in (config.state_dir / "journal.jsonl").read_text()
    )


def test_partial_submission_recovers_without_duplicate_orders(
    config: TradingConfig, first_day: date
) -> None:
    from financial_agent.quant.execution import BrokerError, OrderAck
    from financial_agent.quant.risk import Order

    class InterruptedPaper(PaperBroker):
        def submit(self, order: Order) -> OrderAck:
            if self.open_orders():
                raise BrokerError("interrupted")
            return super().submit(order)

    broker = InterruptedPaper(
        config.state_dir / "paper.json",
        costs=config.backtest.costs,
        initial_cash=config.initial_cash,
    )
    report = run_session(config, today=first_day, broker=broker)
    assert report.status == "HALTED"
    assert len(broker.open_orders()) == 1
    retry = run_session(config, today=first_day, broker=paper(config))
    assert retry.status == "TRADED", retry.reasons
    assert len(broker.open_orders()) == len(report.orders)
    assert run_session(config, today=first_day).status == "NO_CHANGE"


@pytest.mark.parametrize(
    "day,expected",
    [
        (date(2020, 6, 9), "NO_CHANGE"),
        (date(2020, 6, 8), "TRADED"),
        (date(2020, 5, 26), "TRADED"),
    ],
)
def test_weekly_calendar(config: TradingConfig, day: date, expected: str) -> None:
    weekly = replace(config, backtest=replace(config.backtest, rebalance="weekly"))
    assert run_session(weekly, today=day).status == expected


def test_first_observed_equity_initializes_risk_anchors(
    config: TradingConfig, first_day: date
) -> None:
    broker = PaperBroker(
        config.state_dir / "paper.json", costs=config.backtest.costs, initial_cash=10000
    )
    report = run_session(config, today=first_day, broker=broker)
    assert report.status == "TRADED", report.reasons
    assert report.risk["high_water_mark"] == 10000
    assert report.risk["drawdown"] == 0


def test_risk_anchors_cannot_be_reset_by_file_loss_or_rewrite(
    config: TradingConfig, first_day: date
) -> None:
    assert run_session(config, today=first_day).status == "TRADED"
    path = config.state_dir / "risk_state.json"
    original = RiskState.load(path)
    path.unlink()
    assert run_session(config, today=first_day).status == "NO_CHANGE"
    assert RiskState.load(path) == original
    RiskState(1000, 1000, first_day.isoformat()).save(path)
    report = run_session(config, today=first_day)
    assert report.status == "HALTED"
    assert report.reasons == ["risk state disagrees with journal"]


def test_off_cadence_skips_bad_price_band_but_preview_reports_it(
    config: TradingConfig, first_day: date
) -> None:
    from financial_agent.quant.risk import AccountSnapshot

    class MismarkedPaper(PaperBroker):
        def account(self) -> AccountSnapshot:
            observed = super().account()
            return replace(
                observed,
                positions={
                    symbol: replace(position, market_price=position.market_price * 1.1)
                    for symbol, position in observed.positions.items()
                },
            )

    weekly = replace(config, backtest=replace(config.backtest, rebalance="weekly"))
    first = run_session(weekly, today=first_day)
    assert first.status == "TRADED" and first.orders
    broker = MismarkedPaper(
        config.state_dir / "paper.json",
        costs=config.backtest.costs,
        initial_cash=config.initial_cash,
    )
    tuesday = date(2020, 6, 9)
    report = run_session(weekly, today=tuesday, broker=broker)
    assert report.status == "NO_CHANGE", report.reasons
    assert report.reasons == ["outside rebalance calendar"]
    assert report.targets == first.targets
    rendered = (config.state_dir / "reports/2020-06-09.md").read_text()
    assert "Target (last plan)" in rendered
    assert first.targets
    assert all(f"{weight:.2%}" in rendered for weight in first.targets.values())
    assert not report.orders and report.fills
    journal = Journal(config.state_dir / "journal.jsonl")
    assert not [
        e for e in journal.events(["plan"]) if e.payload["session"] == str(tuesday)
    ]
    preview = run_session(weekly, today=tuesday, dry_run=True, broker=broker)
    assert preview.status == "NO_CHANGE", preview.reasons
    assert preview.dry_run and not preview.risk["rebalance_due"]
    assert any("price_band_pct" in r for r in preview.reasons)
    assert not broker.open_orders()


@pytest.mark.parametrize("broker_observed", [False, True])
def test_crash_during_submission_recovers_same_day(
    config: TradingConfig, first_day: date, broker_observed: bool
) -> None:
    from financial_agent.quant.execution import BrokerError, OrderAck
    from financial_agent.quant.risk import Order

    class CrashedPaper(PaperBroker):
        def submit(self, order: Order) -> OrderAck:
            if broker_observed:
                super().submit(order)
            raise BrokerError("process interrupted before journal acknowledgement")

    broker = CrashedPaper(
        config.state_dir / "paper.json",
        costs=config.backtest.costs,
        initial_cash=config.initial_cash,
    )
    original = run_session(config, today=first_day, broker=broker)
    assert original.status == "HALTED" and original.orders
    assert len(broker.open_orders()) == int(broker_observed)
    preview = run_session(config, today=first_day, dry_run=True)
    assert preview.status == "NO_CHANGE" and preview.orders
    assert len(broker.open_orders()) == int(broker_observed)
    recovered = run_session(config, today=first_day)
    assert recovered.status == "TRADED", recovered.reasons
    assert {o.client_order_id for o in recovered.orders} == {
        o.client_order_id for o in original.orders
    }
    assert len(broker.open_orders()) == len(original.orders)
    assert run_session(config, today=first_day).status == "NO_CHANGE"


@pytest.mark.parametrize("observed", [False, True])
def test_prior_session_intent_is_observed_or_abandoned(
    config: TradingConfig, first_day: date, observed: bool
) -> None:
    from financial_agent.quant.risk import Order
    from financial_agent.quant.runner.report import json_value

    broker = paper(config)
    broker.settle(
        csv(config).fetch(config.symbols, config.data_start, date(2020, 6, 5))
    )
    order = Order("SPY", "buy", 10, client_order_id="interrupted-order")
    journal = Journal(config.state_dir / "journal.jsonl")
    journal.append(
        "submission_intent",
        {"session": str(first_day), "order": json_value(order), "reference_price": 100},
    )
    if observed:
        broker.submit(order)
    recovered = run_session(config, today=date(2020, 6, 9), broker=broker)
    assert recovered.status != "HALTED", recovered.reasons
    submitted = journal.events(["submitted"])
    abandoned = journal.events(["submission_abandoned"])
    if observed:
        assert any(
            e.payload["client_order_id"] == order.client_order_id for e in submitted
        )
        assert not abandoned
        assert any(f.client_order_id == order.client_order_id for f in recovered.fills)
    else:
        assert (
            len(abandoned) == 1
            and abandoned[0].payload["client_order_id"] == order.client_order_id
        )
        assert not any(
            e.payload["client_order_id"] == order.client_order_id for e in submitted
        )
        assert (
            order.client_order_id
            not in json.loads(broker.state_path.read_text())["orders"]
        )
    assert (
        run_session(config, today=date(2020, 6, 9), broker=broker).status == "NO_CHANGE"
    )
    assert journal.verify().ok


def test_off_cadence_still_checks_drawdown(config: TradingConfig) -> None:
    weekly = replace(config, backtest=replace(config.backtest, rebalance="weekly"))
    config.state_dir.mkdir()
    day = date(2020, 6, 9)
    RiskState(200000, 100000, str(day)).save(config.state_dir / "risk_state.json")
    report = run_session(weekly, today=day)
    assert report.status == "HALTED"
    assert any("max_drawdown_pct" in r for r in report.reasons)
    assert KillSwitch(config.state_dir).engaged()


def test_off_cadence_without_a_plan_has_unknown_targets(
    config: TradingConfig,
) -> None:
    from financial_agent.quant.risk import AccountSnapshot, Position
    from financial_agent.quant.runner.report import SessionReport, render_markdown
    from datetime import datetime, timezone

    weekly = replace(config, backtest=replace(config.backtest, rebalance="weekly"))
    report = run_session(weekly, today=date(2020, 6, 9))
    assert report.targets == {}
    held = AccountSnapshot(
        75000,
        100000,
        {"SPY": Position("SPY", 250, 100, 100)},
        datetime.now(timezone.utc),
    )
    rendered = render_markdown(
        SessionReport(
            "NO_CHANGE", "2020-06-09", [], [], [], held, {}, targets=report.targets
        )
    )
    assert "| SPY | — | 25.00% |" in rendered
