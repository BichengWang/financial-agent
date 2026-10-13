"""Point-in-time execution and accounting behavior on hand-built bars."""

from dataclasses import dataclass, field, replace
from typing import Any
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from financial_agent.quant.data import MarketData, synthetic_market
from financial_agent.quant.strategies import buy_and_hold, StrategyError
from financial_agent.quant.backtest import BacktestConfig, CostModel, run_backtest


def bars() -> MarketData:
    index = pd.bdate_range("2024-01-01", periods=5)
    close = pd.DataFrame(
        {"A": [10, 12, 14, 15, 16], "B": [20, 21, 22, 23, 24]}, index=index
    )
    opening = pd.DataFrame(
        {"A": [9, 11, 13, 14, 15], "B": [19, 20, 21, 22, 23]}, index=index
    )
    return MarketData(
        opening,
        close + 1,
        opening - 1,
        close,
        close * 100,
        adjusted=True,
        source="test",
    )


@dataclass
class Recording:
    name: str = "recording"
    warmup: int = 2
    seen: list[MarketData] = field(default_factory=list)

    def params(self) -> dict[str, Any]:
        return {}

    def target_weights(self, data: MarketData) -> pd.Series:
        self.seen.append(data)
        return pd.Series({"A": 0.5, "B": 0.5})


@pytest.mark.parametrize(
    "execution,delay,reference,fill_index",
    [("next_open", 0, 11, 1), ("next_close", 0, 12, 1), ("next_open", 1, 13, 2)],
)
def test_hand_computed_fill(
    execution: Any, delay: int, reference: float, fill_index: int
) -> None:
    data = bars()
    cost = CostModel(
        commission_per_share=0.1,
        commission_min=1,
        commission_bps=10,
        half_spread_bps=10,
        slippage_bps=10,
    )
    result = run_backtest(
        buy_and_hold({"A": 1}),
        data,
        BacktestConfig(
            initial_cash=100,
            rebalance="monthly",
            execution=execution,
            extra_delay=delay,
            costs=cost,
        ),
    )
    assert result.trades.empty  # Month-end decision is the final bar.
    result = run_backtest(
        buy_and_hold({"A": 1}),
        data,
        BacktestConfig(
            initial_cash=100,
            rebalance="daily",
            drift_threshold=1,
            execution=execution,
            extra_delay=delay,
            costs=cost,
        ),
    )
    first = result.trades.iloc[0]
    price = reference * 1.002
    quantity = np.floor((100 - 1) / price)
    commission = max(1, quantity * 0.1 + quantity * price * 0.001)
    cash = 100 - quantity * price - commission
    assert first.fill_session == data.sessions[fill_index]
    assert first.shares == quantity
    assert first.reference_price == reference
    assert first.fill_price == pytest.approx(price)
    assert first.commission == pytest.approx(commission)
    assert first.slippage_cost == pytest.approx(quantity * (price - reference))
    assert result.equity.iloc[fill_index] == pytest.approx(
        cash + quantity * data.close.iloc[fill_index]["A"]
    )
    assert (result.weights.sum(axis=1) <= 1 + 1e-12).all()


@pytest.mark.parametrize("cadence", ["daily", "weekly", "monthly"])
def test_exact_history_and_calendar(cadence: Any) -> None:
    data = synthetic_market(["A", "B"], 65, seed=7, start="2023-12-20")
    strategy = Recording(warmup=4)
    start = data.sessions[6]
    run_backtest(strategy, data, BacktestConfig(rebalance=cadence, start=start))
    sessions = data.sessions
    expected = []
    for i, session in enumerate(sessions):
        end = i == len(sessions) - 1
        if cadence == "weekly" and not end:
            end = session.isocalendar()[:2] != sessions[i + 1].isocalendar()[:2]
        if cadence == "monthly" and not end:
            end = (session.year, session.month) != (
                sessions[i + 1].year,
                sessions[i + 1].month,
            )
        if i >= 3 and session >= start and (cadence == "daily" or end):
            expected.append(session)
    assert [history.sessions[-1] for history in strategy.seen] == expected
    for history, decision in zip(strategy.seen, expected):
        for name in ("open", "high", "low", "close", "volume"):
            pd.testing.assert_frame_equal(
                getattr(history, name), getattr(data, name).loc[:decision]
            )
    strategy.seen[0].close.iloc[0, 0] = -999
    assert data.close.iloc[0, 0] != -999


def test_perturbation_no_future_leakage() -> None:
    data = synthetic_market(["A", "B"], 80, seed=3)
    k = 30
    fields = {
        name: getattr(data, name).copy()
        for name in ("open", "high", "low", "close", "volume")
    }
    for frame in fields.values():
        frame.iloc[k + 2 :] *= 10
    changed = MarketData(**fields, adjusted=True, source="perturbed")
    config = BacktestConfig(rebalance="daily")
    original = run_backtest(Recording(), data, config)
    perturbed = run_backtest(Recording(), changed, config)
    pd.testing.assert_series_equal(
        original.equity.iloc[: k + 2], perturbed.equity.iloc[: k + 2]
    )
    pd.testing.assert_frame_equal(
        original.trades[original.trades.fill_session <= data.sessions[k + 1]],
        perturbed.trades[perturbed.trades.fill_session <= data.sessions[k + 1]],
    )


def test_missing_fill_and_close_carry_forward() -> None:
    data = bars()
    opening = data.open.copy()
    opening.iloc[1, 0] = np.nan
    closing = data.close.copy()
    closing.iloc[3, 0] = np.nan
    changed = replace(data, open=opening, close=closing)
    result = run_backtest(
        buy_and_hold({"A": 1}),
        changed,
        BacktestConfig(initial_cash=100, rebalance="daily", costs=CostModel.zero()),
    )
    assert result.skipped_trades.iloc[0].fill_session == data.sessions[1]
    assert result.trades.iloc[0].fill_session == data.sessions[2]
    assert result.equity.iloc[3] == result.equity.iloc[2]
    assert np.isfinite(result.equity).all()


def test_sells_first_and_cash_constrained_portfolio() -> None:
    class Switch(Recording):
        def target_weights(self, data: MarketData) -> pd.Series:
            return pd.Series({"A": 1.0} if len(data.sessions) == 1 else {"B": 1.0})

    result = run_backtest(
        Switch(warmup=1),
        bars(),
        BacktestConfig(
            initial_cash=100, rebalance="daily", costs=CostModel(commission_min=1)
        ),
    )
    day = result.trades[result.trades.fill_session == bars().sessions[2]]
    assert list(day.side) == ["sell", "buy"]
    assert (result.weights.sum(axis=1) <= 1).all()
    assert (result.weights >= 0).all().all()
    assert result.costs.sum() > 0


def test_invalid_strategy_fails_with_name_and_values() -> None:
    class Invalid(Recording):
        def target_weights(self, data: MarketData) -> pd.Series:
            return pd.Series({"A": -1.0})

    with pytest.raises(StrategyError, match="recording.*-1"):
        run_backtest(Invalid(), bars(), BacktestConfig())


def test_zero_cost_and_scaling() -> None:
    cost = CostModel(0.01, 1, 2, 3, 4)
    scaled = cost.scaled(2)
    assert scaled.commission(10, 100) == pytest.approx(cost.commission(10, 100) * 2)
    assert scaled.fill_price("buy", 100) == pytest.approx(100.14)
    assert cost.commission(0, 100) == 0
    assert CostModel.zero().fill_price("sell", 100) == 100
    with pytest.raises(ValueError):
        cost.scaled(-1)


@pytest.mark.parametrize("fractional", [False, True])
def test_gap_and_minimum_commissions_never_overdraw(fractional: bool) -> None:
    data = bars()
    opening = data.open.copy()
    opening.iloc[1] *= 5
    data = replace(data, open=opening)
    costs = CostModel(commission_min=5, commission_bps=15)
    result = run_backtest(
        Recording(warmup=1),
        data,
        BacktestConfig(
            initial_cash=100,
            rebalance="daily",
            fractional_shares=fractional,
            costs=costs,
        ),
    )
    cash = 100.0
    held = {"A": 0.0, "B": 0.0}
    for trade in result.trades.itertuples():
        direction = 1 if trade.side == "buy" else -1
        cash -= direction * trade.notional + trade.commission
        held[trade.symbol] += direction * trade.shares
        assert cash >= 0
        assert held[trade.symbol] >= 0
        if not fractional:
            assert trade.shares == int(trade.shares)
    for session, nav in result.equity.items():
        assert nav > 0
        assert result.weights.loc[session].sum() <= 1 + 1e-12


def test_pending_delayed_exits_cannot_create_shorts() -> None:
    class Exit(Recording):
        def target_weights(self, data: MarketData) -> pd.Series:
            return pd.Series({"A": 1.0 if len(data.sessions) < 4 else 0.0})

    data = synthetic_market(["A"], 20, seed=1)
    result = run_backtest(
        Exit(warmup=1),
        data,
        BacktestConfig(rebalance="daily", extra_delay=2, costs=CostModel.zero()),
    )
    quantity = 0.0
    for trade in result.trades.itertuples():
        quantity += trade.shares if trade.side == "buy" else -trade.shares
        assert quantity >= 0
    assert quantity == 0
    assert result.weights.iloc[-1].sum() == 0


@pytest.mark.parametrize("delay", [1, 3])
def test_pending_fixed_weight_buys_do_not_duplicate(delay: int) -> None:
    data = bars()
    constant = data.close * 0 + 10.0
    data = replace(data, open=constant.copy(), close=constant.copy())
    result = run_backtest(
        buy_and_hold({"A": 0.5}),
        data,
        BacktestConfig(
            initial_cash=100,
            rebalance="daily",
            extra_delay=delay,
            drift_threshold=0,
            costs=CostModel.zero(),
        ),
    )
    assert len(result.trades) == 1
    trade = result.trades.iloc[0]
    assert trade.side == "buy"
    assert trade.shares == 5
    assert trade.fill_session == data.sessions[1 + delay]
    assert result.weights["A"].max() == 0.5
    assert result.weights["A"].iloc[-1] == 0.5


def test_summary_excludes_warmup_and_keeps_full_histories() -> None:
    data = synthetic_market(["A"], 30, seed=7)
    strategy = replace(buy_and_hold({"A": 0.5}), warmup=15)
    config = BacktestConfig(rebalance="daily", costs=CostModel.zero())
    long = run_backtest(strategy, data, config)
    short = run_backtest(
        buy_and_hold({"A": 0.5}), data.window(data.sessions[14], None), config
    )
    assert long.active_start == data.sessions[14]
    assert short.active_start == long.active_start
    assert len(long.returns) == 30
    assert (long.returns.iloc[:15] == 0).all()
    pd.testing.assert_series_equal(long.returns.iloc[15:], short.returns.iloc[1:])
    assert long.summary() == pytest.approx(short.summary(), nan_ok=True)
    assert long.summary()["average_annual_turnover"] == pytest.approx(
        long.turnover.iloc[15:].mean() * 252
    )


def test_summary_without_an_active_fill_period() -> None:
    result = run_backtest(
        replace(buy_and_hold({"A": 1}), warmup=20), bars(), BacktestConfig()
    )
    assert result.active_start is None
    assert np.isnan(result.summary()["cagr"])
    assert np.isnan(result.summary()["average_annual_turnover"])
    result = run_backtest(
        buy_and_hold({"A": 1}), bars(), BacktestConfig(rebalance="monthly")
    )
    assert result.active_start == bars().sessions[-1]
    assert np.isnan(result.summary()["cagr"])


@pytest.mark.parametrize("reference", [20.0, float("nan")])
def test_pending_exit_after_underfilled_or_skipped_buy(reference: float) -> None:
    class Exit(Recording):
        def target_weights(self, data: MarketData) -> pd.Series:
            return pd.Series({"A": 1.0 if len(data.sessions) == 1 else 0.0})

    data = bars()
    constant = data.close * 0 + 10.0
    opening = constant.copy()
    opening.iloc[2, 0] = reference
    data = replace(data, open=opening, close=constant)
    result = run_backtest(
        Exit(warmup=1),
        data,
        BacktestConfig(
            initial_cash=100, rebalance="daily", extra_delay=1, costs=CostModel.zero()
        ),
    )
    assert (result.weights >= 0).all().all()
    assert result.weights.iloc[-1].sum() == 0
    if np.isfinite(reference):
        assert result.trades.shares.tolist() == [5.0, 5.0]
        assert result.trades.side.tolist() == ["buy", "sell"]
    else:
        assert result.trades.empty
        assert len(result.skipped_trades) == 1


@pytest.mark.parametrize("fractional", [False, True])
@pytest.mark.parametrize("delay", [0, 2])
def test_cash_buffer_caps_decision_price_allocations(
    fractional: bool, delay: int
) -> None:
    data = bars()
    constant = data.close * 0 + 10.0
    data = replace(data, open=constant.copy(), close=constant.copy())
    config = BacktestConfig(
        initial_cash=1000,
        cash_buffer=0.02,
        rebalance="daily",
        extra_delay=delay,
        drift_threshold=0,
        fractional_shares=fractional,
        costs=CostModel.zero(),
    )
    result = run_backtest(Recording(warmup=1), data, config)
    assert (result.weights.sum(axis=1) <= 0.98 + 1e-12).all()
    assert result.weights.iloc[-1].sum() == pytest.approx(0.98)
    assert result.trades.shares.sum() == pytest.approx(98)


@pytest.mark.parametrize("buffer", [-0.01, 1, 1.01, float("nan"), float("inf"), True])
def test_invalid_cash_buffer_rejected(buffer: float) -> None:
    with pytest.raises(ValueError, match="cash_buffer"):
        BacktestConfig(cash_buffer=buffer)


def test_buffer_preserves_defensive_allocations_and_rejects_invalid_targets() -> None:
    config = BacktestConfig(cash_buffer=0.02)
    assert config.buffered_targets({"A": 0.2, "B": 0.3}) == {"A": 0.2, "B": 0.3}
    assert config.buffered_targets({"A": 0}) == {"A": 0}
    for targets in [{"A": 1.1}, {"A": -1}, {"A": float("nan")}]:
        with pytest.raises(ValueError):
            config.buffered_targets(targets)
