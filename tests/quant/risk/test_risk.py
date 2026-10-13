"""Consumer-visible boundaries, persistence and execution parity."""

from dataclasses import replace
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, Literal

import pytest

from financial_agent.quant.backtest import BacktestConfig
from financial_agent.quant.portfolio import rebalance_deltas
from financial_agent.quant.risk import (
    AccountSnapshot,
    KillSwitch,
    Order,
    Position,
    RiskConfigError,
    RiskLimits,
    RiskState,
    check_orders,
    plan_orders,
    update_risk_state,
)


def account(cash: float = 1000, **quantities: float) -> AccountSnapshot:
    return AccountSnapshot(
        cash,
        1000,
        {s: Position(s, q, 1, 1) for s, q in quantities.items()},
        datetime(2026, 10, 12),
    )


def order(qty: float, side: Literal["buy", "sell"] = "buy", symbol: str = "A") -> Order:
    assert side in {"buy", "sell"}
    return Order(symbol, side, qty, client_order_id=f"{symbol}-{side}-{qty}")


def permissive(**overrides: Any) -> RiskLimits:
    return replace(
        RiskLimits(
            max_weight=1,
            max_gross=3,
            max_turnover_pct=3,
            min_cash_pct=0,
            max_order_notional_pct=1,
        ),
        **overrides,
    )


@pytest.mark.parametrize(
    "name,threshold,qty",
    [
        ("max_weight", 0.3, 300),
        ("max_gross", 0.3, 300),
        ("max_order_notional_pct", 0.35, 350),
        ("max_turnover_pct", 0.4, 400),
        ("min_cash_pct", 0.1, 900),
    ],
)
def test_numeric_boundaries(
    tmp_path: Path, name: str, threshold: float, qty: float
) -> None:
    limits = permissive(**{name: threshold})
    switch = KillSwitch(tmp_path)
    for quantity in (qty - 0.001, qty):
        decision = check_orders(
            [order(quantity)], account(), {"A": 1}, limits, kill_switch=switch
        )
        assert not decision.halt and len(decision.approved) == 1
    decision = check_orders(
        [order(qty + 0.001)], account(), {"A": 1}, limits, kill_switch=switch
    )
    assert decision.halt and not decision.approved and decision.rejected
    assert any(
        name in r and "value=" in r and "threshold=" in r for r in decision.reasons
    )


def test_turnover_full_flip_and_plan_atomicity(tmp_path: Path) -> None:
    switch = KillSwitch(tmp_path)
    orders = [order(500, "sell"), order(500, symbol="B")]
    acc = account(500, A=500)
    limits = permissive(max_turnover_pct=1)
    assert not check_orders(
        orders, acc, {"A": 1, "B": 1}, limits, kill_switch=switch
    ).halt
    bad = [orders[0], order(500.01, symbol="B")]
    result = check_orders(bad, acc, {"A": 1, "B": 1}, limits, kill_switch=switch)
    assert result.halt and result.approved == [] and len(result.rejected) == 2


def test_short_symbol_count_and_price_band(tmp_path: Path) -> None:
    switch = KillSwitch(tmp_path)
    acc = account(900, A=100)
    for qty, halt in [(100, False), (100.01, True)]:
        result = check_orders(
            [order(qty, "sell")], acc, {"A": 1}, permissive(), kill_switch=switch
        )
        assert result.halt == halt
    result = check_orders(
        [order(60, "sell"), order(60, "sell")],
        acc,
        {"A": 1},
        permissive(),
        kill_switch=switch,
    )
    assert result.halt
    assert not check_orders(
        [order(101, "sell")],
        acc,
        {"A": 1},
        permissive(allow_short=True),
        kill_switch=switch,
    ).halt
    limits = permissive(allowed_symbols=("A",), max_orders=1)
    assert not check_orders([order(1)], acc, {"A": 1}, limits, kill_switch=switch).halt
    for orders, name in [
        ([order(1, symbol="B")], "allowed_symbols"),
        ([order(1), order(1)], "max_orders"),
    ]:
        result = check_orders(orders, acc, {"A": 1, "B": 1}, limits, kill_switch=switch)
        assert (
            result.halt
            and not result.approved
            and any(name in r for r in result.reasons)
        )
    for price, halt in [
        (1.0499, False),
        (1.05, False),
        (1.05001, True),
        (0.95, False),
        (0.94999, True),
    ]:
        result = check_orders(
            [order(1)], acc, {"A": price}, permissive(), kill_switch=switch
        )
        assert result.halt == halt


@pytest.mark.parametrize("price", [None, 0, -1, float("nan"), float("inf")])
def test_invalid_price_fails_closed(tmp_path: Path, price: float | None) -> None:
    prices = {} if price is None else {"A": price}
    result = check_orders(
        [order(1)], account(), prices, permissive(), kill_switch=KillSwitch(tmp_path)
    )
    assert result.halt and not result.approved
    assert any("reference_price" in r for r in result.reasons)


@pytest.mark.parametrize("qty", [0, -1, float("nan"), float("inf")])
def test_invalid_orders_fail_closed(tmp_path: Path, qty: float) -> None:
    result = check_orders(
        [order(qty)],
        account(),
        {"A": 1},
        permissive(),
        kill_switch=KillSwitch(tmp_path),
    )
    assert result.halt and not result.approved


def test_invalid_account_and_unchanged_holdings(tmp_path: Path) -> None:
    switch = KillSwitch(tmp_path)
    for equity in [0, -1, float("nan"), float("inf")]:
        result = check_orders(
            [order(1)],
            replace(account(), equity=equity),
            {"A": 1},
            permissive(),
            kill_switch=switch,
        )
        assert result.halt and not result.approved
    assert check_orders(
        [], account(500, A=500), {"A": 1}, RiskLimits(), kill_switch=switch
    ).halt
    assert check_orders(
        [], account(500, A=500), {}, permissive(), kill_switch=switch
    ).halt


@pytest.mark.parametrize(
    "key,value",
    [
        ("max_weight", 0.31),
        ("max_gross", 1.01),
        ("max_order_notional_pct", 0.36),
        ("max_turnover_pct", 1.01),
        ("max_daily_loss_pct", 0.031),
        ("max_drawdown_pct", 0.21),
        ("max_orders", 51),
        ("price_band_pct", 0.051),
        ("min_cash_pct", 0.009),
        ("allow_short", True),
        ("allowed_symbols", ("A", "B")),
        ("allowed_symbols", ()),
    ],
)
def test_every_loosening_rejected(key: str, value: Any) -> None:
    with pytest.raises(RiskConfigError):
        RiskLimits(allowed_symbols=("A",)).tighten({key: value})


def test_tighten_and_loading_errors(tmp_path: Path) -> None:
    base = RiskLimits(allow_short=True)
    overrides = {
        "max_weight": 0.2,
        "max_gross": 0.8,
        "max_order_notional_pct": 0.2,
        "max_turnover_pct": 0.8,
        "max_daily_loss_pct": 0.02,
        "max_drawdown_pct": 0.1,
        "min_cash_pct": 0.1,
        "price_band_pct": 0.02,
        "max_orders": 10,
        "allow_short": False,
        "allowed_symbols": ["A", "B"],
    }
    tight = base.tighten(overrides)
    assert tight.allowed_symbols == ("A", "B")
    assert tight.tighten({"allowed_symbols": ["A"]}).allowed_symbols == ("A",)
    assert tight.tighten({}) == tight
    for content in [
        "[risk]\nunknown = 1",
        "[risk]\nmax_weight = -1",
        "[risk]\nmax_weight = nan",
        "[risk]\nmax_orders = 1.5",
        "[risk]\nallow_short = 1",
        "[risk]\nmin_cash_pct = 2",
        '[risk]\nallowed_symbols = "A"',
        '[risk]\nallowed_symbols = [""]',
        "[promotion]\nfoo = 1",
    ]:
        path = tmp_path / "policy.toml"
        path.write_text(content)
        with pytest.raises(ValueError):
            RiskLimits.load(path)
    path.write_text("[risk]\nmax_weight = 0.15\n[promotion]\nfoo = 1")
    assert RiskLimits.load(path).max_weight == 0.15
    with pytest.raises(ValueError):
        base.tighten({"unknown": 0})


@pytest.mark.parametrize(
    "fractional,drift,minimum", [(False, 0, 0), (True, 0.02, 100), (False, 0.1, 10)]
)
def test_order_planning_exact_parity(
    fractional: bool, drift: float, minimum: float
) -> None:
    acc = account(600, A=150.5, C=249.5)
    prices = {"A": 1.7, "B": 2.3, "C": 0.8}
    targets = {"A": 0.2, "B": 0.3}
    config = BacktestConfig(
        fractional_shares=fractional, drift_threshold=drift, min_trade_notional=minimum
    )
    orders = plan_orders(
        targets, acc, prices, session="2026-10-12", strategy="test", config=config
    )
    expected = rebalance_deltas(
        targets,
        {s: p.qty for s, p in acc.positions.items()},
        prices,
        acc.equity,
        fractional=fractional,
        drift_threshold=drift,
        min_trade_notional=minimum,
    )
    assert {
        o.symbol: o.qty * (1 if o.side == "buy" else -1) for o in orders
    } == expected
    assert [o.side for o in orders] == sorted([o.side for o in orders], reverse=True)
    assert orders == plan_orders(
        targets, acc, prices, session="2026-10-12", strategy="test", config=config
    )
    later = plan_orders(
        targets, acc, prices, session="2026-10-13", strategy="test", config=config
    )
    assert all(a.client_order_id != b.client_order_id for a, b in zip(orders, later))
    for o in orders:
        payload = f"test|2026-10-12|{o.symbol}|{o.side}|{o.qty}"
        assert o.client_order_id == "fa-" + sha256(payload.encode()).hexdigest()[:24]
    changed = plan_orders(
        {"B": 0.4},
        account(),
        prices,
        session="2026-10-12",
        strategy="test",
        config=config,
    )
    original = plan_orders(
        {"B": 0.3},
        account(),
        prices,
        session="2026-10-12",
        strategy="test",
        config=config,
    )
    assert changed[0].client_order_id != original[0].client_order_id


def test_state_rollover_boundaries_and_roundtrip(tmp_path: Path) -> None:
    state = RiskState(1000, 1000, "day1")
    limits = RiskLimits()
    for equity, names in [
        (970, []),
        (969.99, ["max_daily_loss_pct"]),
        (800, ["max_daily_loss_pct"]),
        (799.99, ["max_drawdown_pct", "max_daily_loss_pct"]),
    ]:
        updated, reasons = update_risk_state(
            state, replace(account(), equity=equity), limits, session="day1"
        )
        assert [r.split()[0] for r in reasons] == names
        assert updated.high_water_mark == 1000
    rolled, reasons = update_risk_state(
        state, replace(account(), equity=900), limits, session="day2"
    )
    assert rolled.day_start_equity == 900 and not reasons
    risen, reasons = update_risk_state(
        rolled, replace(account(), equity=1100), limits, session="day2"
    )
    assert (
        risen.high_water_mark == 1100 and risen.day_start_equity == 900 and not reasons
    )
    path = tmp_path / "nested" / "risk.json"
    risen.save(path)
    assert RiskState.load(path) == risen
    rolled.save(path)
    assert RiskState.load(path) == rolled
    assert update_risk_state(
        state, replace(account(), equity=float("nan")), limits, session="day1"
    )[1]


def test_kill_switch_manual_persistence_and_release(tmp_path: Path) -> None:
    switch = KillSwitch(tmp_path)
    assert not switch.engaged() and switch.reason() is None
    (tmp_path / "KILL").touch()
    assert KillSwitch(tmp_path).engaged() and switch.reason() == "manual emergency stop"
    decision = check_orders(
        [order(1)], account(), {"A": 1}, permissive(), kill_switch=switch
    )
    assert (
        decision.halt and not decision.approved and "kill_switch" in decision.reasons[0]
    )
    switch.engage("daily loss", source="risk")
    other = KillSwitch(tmp_path)
    assert other.reason() == "daily loss"
    for reason, operator in [("", "owner"), ("reviewed", ""), ("  ", "owner")]:
        with pytest.raises(ValueError):
            other.release(reason, operator=operator)
        assert switch.engaged()
    record = other.release("reviewed", operator="owner")
    assert (
        record["released"]["reason"] == "daily loss"
        and record["released"]["source"] == "risk"
    )
    assert not switch.engaged()
    (tmp_path / "KILL").write_text("broken JSON")
    assert switch.engaged() and switch.reason() == "manual emergency stop"
    assert (
        switch.release("manual reset", operator="owner")["released"]["reason"]
        == "manual emergency stop"
    )


def test_out_of_range_loosening_and_account_weights() -> None:
    with pytest.raises(RiskConfigError):
        RiskLimits().tighten({"max_weight": 2})
    assert account(900, A=100).weights() == {"A": 0.1}
    with pytest.raises(ValueError):
        replace(account(), equity=float("nan")).weights()


def test_invalid_mark_and_position_fail_closed(tmp_path: Path) -> None:
    switch = KillSwitch(tmp_path)
    for position in [Position("A", 100, 1, 0), Position("A", float("nan"), 1, 1)]:
        acc = replace(account(), positions={"A": position})
        result = check_orders(
            [order(1)], acc, {"A": 1}, permissive(), kill_switch=switch
        )
        assert result.halt and not result.approved
    for cash in [float("nan"), float("inf")]:
        assert check_orders(
            [order(1)],
            replace(account(), cash=cash),
            {"A": 1},
            permissive(),
            kill_switch=switch,
        ).halt
