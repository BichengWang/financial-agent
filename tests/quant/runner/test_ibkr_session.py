"""Public runner integration through an injected Client Portal transport."""

from dataclasses import replace
from datetime import date
from pathlib import Path
from typing import Any

import pytest

from financial_agent.quant.data import CsvProvider
from financial_agent.quant.execution import Broker, IBKRBroker, Journal
from financial_agent.quant.runner import (
    TradingConfig,
    authorize_live,
    run_session,
    PromotionError,
)
from ..execution.test_ibkr import Gateway
from .test_promotion import certificate, paper_evidence


@pytest.fixture(autouse=True)
def no_transport_pacing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(IBKRBroker, "_pace", lambda self, path: None)


def fill(transport: Gateway, config: TradingConfig, day: date) -> None:
    """Apply opening-auction fills, then expose trades from an earlier session."""
    assert config.csv_dir is not None
    data = CsvProvider(config.csv_dir).fetch(config.symbols, config.data_start, day)
    for o in transport.orders:
        symbol = next(s for s, c in config.conids.items() if c == o["conid"])
        price = config.backtest.costs.fill_price(
            "buy", float(data.open.iloc[-1][symbol])
        )
        qty = o["totalSize"]
        transport.cash -= qty * price
        transport.positions.append(
            {
                "acctId": transport.account_id,
                "conid": o["conid"],
                "position": qty,
                "avgPrice": price,
                "mktPrice": float(data.close.iloc[-1][symbol]),
                "currency": "USD",
                "assetClass": "STK",
            }
        )
        transport.trades.append(
            {
                "account": transport.account_id,
                "order_ref": o["local_order_id"],
                "order_id": o["orderId"],
                "execution_id": str(o["orderId"]),
                "conid": o["conid"],
                "symbol": symbol,
                "side": "B",
                "size": qty,
                "price": price,
                "trade_time_r": 1591623000000,
            }
        )
    transport.orders = []


def ibkr_config(config: TradingConfig) -> TradingConfig:
    return replace(
        config,
        broker_kind="ibkr",
        account_id="DU123456",
        conids={s: i + 1 for i, s in enumerate(config.symbols)},
    )


def test_ibkr_paper_round_trip(config: TradingConfig, first_day: date) -> None:
    config = ibkr_config(config)
    transport = Gateway()
    broker = IBKRBroker(
        config.account_id or "", session=transport, conids=config.conids
    )
    first = run_session(config, today=first_day, broker=broker)
    assert first.status == "TRADED", first.reasons
    assert run_session(config, today=first_day, broker=broker).status == "NO_CHANGE"
    fill(transport, config, first_day)
    # A fresh adapter has no in-memory original order quantities; the journal does.
    broker = IBKRBroker(
        config.account_id or "", session=transport, conids=config.conids
    )
    second = run_session(config, today=date(2020, 6, 9), broker=broker)
    assert second.status != "HALTED", second.reasons
    assert len(second.fills) == len(first.orders)
    assert second.account is not None
    assert {s: p.qty for s, p in second.account.positions.items()} == {
        o.symbol: o.qty for o in first.orders
    }
    journal = Journal(config.state_dir / "journal.jsonl")
    assert journal.verify().ok
    assert all(e.payload["broker_kind"] == "ibkr" for e in journal.events(["fill"]))


def test_question_halts_without_double_submission(
    config: TradingConfig, first_day: date
) -> None:
    config = ibkr_config(config)
    transport = Gateway()
    transport.questions = [["o354"]]
    broker = IBKRBroker(
        config.account_id or "", session=transport, conids=config.conids
    )
    report = run_session(config, today=first_day, broker=broker)
    assert report.status == "HALTED" and "o354" in str(report.reasons)
    assert not transport.orders
    assert (
        sum(m == "POST" and p.endswith("/orders") for m, p, _ in transport.calls) == 1
    )
    again = run_session(config, today=first_day, broker=broker)
    assert again.status == "HALTED" and "o354" in str(again.reasons)
    assert (
        sum(m == "POST" and p.endswith("/orders") for m, p, _ in transport.calls) == 1
    )


@pytest.mark.parametrize("kind", ["alpaca", "paper", "ibkr"])
def test_live_evidence_is_same_broker(
    config: TradingConfig, tmp_path: Path, kind: str
) -> None:
    live = replace(ibkr_config(config), mode="live", account_id="U123456")
    cert = certificate(live, tmp_path)
    source = paper_evidence(live, tmp_path / "source.jsonl")
    journal = Journal(tmp_path / "evidence.jsonl")
    for event in source.events():
        journal.append(event.type, {**event.payload, "broker_kind": kind})
    if kind == "ibkr":
        assert (
            authorize_live(
                live,
                certificate=cert,
                journal=journal,
                environ={"FA_QUANT_ALLOW_LIVE": "1"},
            ).strategy
            == live.strategy_name
        )
    else:
        with pytest.raises(PromotionError, match="paper sessions 0"):
            authorize_live(
                live,
                certificate=cert,
                journal=journal,
                environ={"FA_QUANT_ALLOW_LIVE": "1"},
            )


def test_ibkr_config_parsing_and_refusals(config_path: Path) -> None:
    text = (
        config_path.read_text()
        .replace("initial_cash = 100000.0\n", "")
        .replace(
            'kind = "paper"',
            'kind = "ibkr"\naccount_id = "DU123456"\n'
            'base_url = "https://localhost:5001/v1/api"\nverify = false\n'
            'confirm_message_ids = ["o354"]\n[broker.conids]\nSPY = 123',
        )
    )
    config_path.write_text(text)
    loaded = TradingConfig.load(config_path)
    assert loaded.conids == {"SPY": 123}
    assert loaded.verify is False
    for replacement in ['account_id = "U123456"', 'account_id = ""']:
        config_path.write_text(text.replace('account_id = "DU123456"', replacement))
        with pytest.raises(ValueError):
            TradingConfig.load(config_path)


@pytest.mark.parametrize("kind", ["ibkr", "alpaca"])
@pytest.mark.parametrize("execution", ["none", "partial", "unreported"])
def test_opening_auction_is_final(
    config: TradingConfig, first_day: date, kind: str, execution: str
) -> None:
    from financial_agent.quant.execution import AlpacaBroker
    from .test_alpaca_session import Exchange

    config = replace(
        ibkr_config(config), backtest=replace(config.backtest, rebalance="weekly")
    )
    transport: Any
    broker: Broker
    if kind == "ibkr":
        transport = Gateway()
        broker = IBKRBroker(
            config.account_id or "", session=transport, conids=config.conids
        )
    else:
        config = replace(config, broker_kind="alpaca")
        transport = Exchange()
        broker = AlpacaBroker("key", "secret", session=transport)
    first = run_session(config, today=first_day, broker=broker)
    assert first.status == "TRADED", first.reasons
    initial = {o.client_order_id: o.qty for o in first.orders}
    if execution != "none":
        if kind == "ibkr":
            if execution == "partial":
                for order in transport.orders:
                    order["totalSize"] = order["totalSize"] / 2
            fill(transport, config, first_day)
            if execution == "unreported":
                transport.trades = []
        else:
            if execution == "partial":
                for order in transport.orders.values():
                    order["qty"] = float(order["qty"]) / 2
            transport.fill(config, first_day)
            if execution == "partial":
                for client, order in transport.orders.items():
                    order.update(qty=initial[client], status="canceled")
    if execution != "partial" or kind == "ibkr":
        transport.orders = [] if kind == "ibkr" else {}
    if execution == "partial":
        # Simulate a crash after journaling only the first share of each fill.
        journal = Journal(config.state_dir / "journal.jsonl")
        for intended in first.orders:
            price = (
                next(
                    t["price"]
                    for t in transport.trades
                    if t["order_ref"] == intended.client_order_id
                )
                if kind == "ibkr"
                else transport.orders[intended.client_order_id]["filled_avg_price"]
            )
            journal.append(
                "fill",
                {
                    "client_order_id": intended.client_order_id,
                    "symbol": intended.symbol,
                    "side": intended.side,
                    "qty": 1,
                    "price": price,
                    "reference_price": price,
                    "commission": 0,
                    "session": str(first_day),
                    "broker_kind": kind,
                },
            )
    next_day = run_session(config, today=date(2020, 6, 9), broker=broker)
    journal = Journal(config.state_dir / "journal.jsonl")
    finals = journal.events(["order_final"])
    assert len(finals) == len(first.orders)
    assert all(e.payload["status"] == "canceled" for e in finals)
    if execution == "partial":
        assert {
            e.payload["client_order_id"]: e.payload["filled_qty"] for e in finals
        } == {c: q / 2 for c, q in initial.items()}
        assert len(next_day.fills) == len(first.orders)
        assert {f.client_order_id: f.qty for f in next_day.fills} == {
            c: q / 2 - 1 for c, q in initial.items()
        }
        # Incremental fills must be durable before finality stops future lookups.
        assert max(e.seq for e in journal.events(["fill"])) < min(e.seq for e in finals)
    else:
        assert not next_day.fills
        assert all(
            e.payload["filled_qty"] == 0
            and e.payload["reason"]
            == "not reported by broker after the opening auction"
            for e in finals
        )
    if execution == "unreported":
        assert next_day.status == "HALTED" and next_day.reasons == [
            "reconciliation break"
        ]
    else:
        assert next_day.status == "NO_CHANGE", next_day.reasons
        before = len(transport.calls)
        if kind == "ibkr":
            transport.trades = []  # History disappears after seven days.
        later = run_session(config, today=date(2020, 6, 18), broker=broker)
        assert later.status == "NO_CHANGE", later.reasons
        calls = transport.calls[before:]
        assert not any(
            "/account/orders" in c[1]
            or "/account/trades" in c[1]
            or "by_client_order_id" in c[1]
            for c in calls
        )
        assert len(journal.events(["order_final"])) == len(finals)


def test_missing_order_before_auction_still_halts(
    config: TradingConfig, first_day: date
) -> None:
    config = ibkr_config(config)
    transport = Gateway()
    broker = IBKRBroker(
        config.account_id or "", session=transport, conids=config.conids
    )
    assert run_session(config, today=first_day, broker=broker).status == "TRADED"
    transport.orders = []
    assert run_session(config, today=first_day, broker=broker).status == "HALTED"
    assert not Journal(config.state_dir / "journal.jsonl").events(["order_final"])


def test_eleven_order_session_validates_account_once(tmp_path: Path) -> None:
    from financial_agent.quant.data import synthetic_market
    from financial_agent.quant.data.providers import write_csv

    symbols = tuple(f"ETF{i}" for i in range(11))
    write_csv(
        synthetic_market(
            symbols,
            420,
            seed=42,
            start="2019-01-02",
            annual_drift=0.30,
            annual_vol=0.03,
            correlation=0.1,
        ),
        tmp_path / "csv",
    )
    path = tmp_path / "ibkr.toml"
    path.write_text(
        'mode = "paper"\nstate_dir = "state"\n[strategy]\n'
        'name = "buy_and_hold"\n[strategy.params.weights]\n'
        + "\n".join(f"{s} = 0.08" for s in symbols)
        + "\n[universe]\nsymbols = "
        + str(list(symbols)).replace("'", '"')
        + '\n[data]\nprovider = "csv"\ncsv_dir = "csv"\nstart = "2019-01-02"\n'
        '[backtest]\ncash_buffer = 0.02\n[broker]\nkind = "ibkr"\n'
        'account_id = "DU123456"\n[broker.conids]\n'
        + "\n".join(f"{s} = {i + 1}" for i, s in enumerate(symbols))
    )
    config = TradingConfig.load(path)
    transport = Gateway()
    broker = IBKRBroker(
        config.account_id or "", session=transport, conids=config.conids
    )
    report = run_session(config, today=date(2020, 6, 8), broker=broker)
    assert report.status == "TRADED", report.reasons
    assert len(report.orders) == 11
    assert sum(p == "/portfolio/accounts" for _, p, _ in transport.calls) == 1
    assert sum(p == "/iserver/auth/status" for _, p, _ in transport.calls) == 1
