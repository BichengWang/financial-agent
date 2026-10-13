"""Public runner integration through an injected Client Portal transport."""

from dataclasses import replace
from datetime import date
from pathlib import Path

import pytest

from financial_agent.quant.data import CsvProvider
from financial_agent.quant.execution import IBKRBroker, Journal
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
