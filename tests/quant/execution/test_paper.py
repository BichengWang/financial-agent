"""Offline execution invariants across sessions and persisted broker instances."""

from pathlib import Path
from dataclasses import replace

import pytest

from financial_agent.quant.backtest import CostModel
from financial_agent.quant.data import synthetic_market
from financial_agent.quant.execution import BrokerError, PaperBroker
from financial_agent.quant.risk.orders import Order


def test_next_open_costs_restart_and_idempotency(tmp_path: Path) -> None:
    data = synthetic_market(["SPY"], 5, seed=7)
    costs = CostModel(commission_per_share=0.1, commission_min=1)
    path = tmp_path / "paper.json"
    broker = PaperBroker(path, costs=costs, initial_cash=1000)
    assert broker.settle(data.upto(data.sessions[0])) == []
    order = Order("SPY", "buy", 3, client_order_id="buy")
    ack = broker.submit(order)
    assert broker.submit(replace(order, qty=20)) == ack
    assert broker.settle(data.upto(data.sessions[0])) == []
    restarted = PaperBroker(path, costs=costs, initial_cash=0)
    (fill,) = restarted.settle(data.upto(data.sessions[1]))
    opening = float(data.open.iloc[1, 0])
    assert fill.session == data.sessions[1].isoformat()
    assert fill.reference_price == opening
    assert fill.price == pytest.approx(costs.fill_price("buy", opening))
    assert fill.commission == 1
    account = broker.account()
    assert account.cash == pytest.approx(1000 - 3 * fill.price - 1)
    assert account.positions["SPY"].avg_price == fill.price
    assert account.positions["SPY"].market_price == data.close.iloc[1, 0]
    assert account.equity == pytest.approx(account.cash + 3 * data.close.iloc[1, 0])
    assert broker.submit(order).filled_qty == 3
    assert restarted.settle(data.upto(data.sessions[1])) == []
    assert broker.open_orders() == []


def test_cash_partial_rejected_and_sells_before_buys(tmp_path: Path) -> None:
    data = synthetic_market(["SPY", "QQQ"], 5, seed=9, annual_vol=0, annual_drift=0)
    broker = PaperBroker(
        tmp_path / "state", costs=CostModel(commission_min=1), initial_cash=251
    )
    broker.settle(data.upto(data.sessions[0]))
    first = Order("SPY", "buy", 5, client_order_id="one")
    second = Order("QQQ", "buy", 1, client_order_id="two")
    broker.submit(first)
    fills = broker.settle(data.upto(data.sessions[1]))
    assert fills[0].qty == 2
    assert broker.submit(first).status == "partially_filled"
    assert broker.account().cash >= 0
    broker.submit(second)
    assert broker.settle(data.upto(data.sessions[2])) == []
    assert broker.submit(second).status == "rejected"
    assert broker.submit(second).reason == "insufficient cash"
    buy = Order("QQQ", "buy", 2, client_order_id="three")
    sell = Order("SPY", "sell", 100, client_order_id="four")
    broker.submit(buy)
    broker.submit(sell)
    fills = broker.settle(data.upto(data.sessions[3]))
    assert [(f.side, f.qty) for f in fills] == [("sell", 2), ("buy", 2)]
    assert broker.submit(sell).status == "partially_filled"
    assert "SPY" not in broker.account().positions
    empty = Order("SPY", "sell", 1, client_order_id="five")
    broker.submit(empty)
    assert broker.settle(data.upto(data.sessions[4])) == []
    assert broker.submit(empty).status == "rejected"


def test_cancel_and_failed_settlement_leave_state_unchanged(tmp_path: Path) -> None:
    data = synthetic_market(["SPY"], 3, seed=1)
    broker = PaperBroker(tmp_path / "state", costs=CostModel.zero(), initial_cash=1000)
    broker.settle(data.upto(data.sessions[0]))
    broker.submit(Order("QQQ", "buy", 1, client_order_id="missing"))
    before = broker.state_path.read_bytes()
    with pytest.raises(BrokerError, match="missing"):
        broker.settle(data)
    assert broker.state_path.read_bytes() == before
    assert broker.cancel_all() == 1
    assert broker.cancel_all() == 0
    broker.settle(data)
    assert broker.account().cash == 1000
    for order in [
        Order("SPY", "buy", 0.5, client_order_id="fraction"),
        Order("SPY", "buy", 1, "limit", client_order_id="limit"),
        Order("SPY", "buy", 1, time_in_force="day", client_order_id="day"),
    ]:
        with pytest.raises(BrokerError):
            broker.submit(order)


def test_batched_data_fills_first_new_open_and_marks_last_close(tmp_path: Path) -> None:
    data = synthetic_market(["SPY"], 5, seed=2)
    broker = PaperBroker(tmp_path / "state", costs=CostModel.zero(), initial_cash=1000)
    broker.settle(data.upto(data.sessions[0]))
    broker.submit(Order("SPY", "buy", 1, client_order_id="batch"))
    (fill,) = broker.settle(data)
    assert fill.reference_price == data.open.iloc[1, 0]
    assert broker.account().positions["SPY"].market_price == data.close.iloc[-1, 0]
    assert broker.settle(data.upto(data.sessions[2])) == []
