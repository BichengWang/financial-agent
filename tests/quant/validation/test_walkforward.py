"""Rolling selection is causal and portfolio transitions incur real costs."""

from collections.abc import Mapping
from dataclasses import replace
from typing import Any

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest

from financial_agent.quant.backtest import BacktestConfig, CostModel, run_backtest
from financial_agent.quant.data import MarketData, synthetic_market
from financial_agent.quant.strategies import Strategy, build_strategy
from financial_agent.quant.validation import stress_test, walk_forward
from financial_agent.quant.validation.walkforward import annual_sharpe


def factory(params: Mapping[str, Any]) -> Strategy:
    return build_strategy("buy_and_hold", params)


def regime_market() -> MarketData:
    data = synthetic_market(["A", "B"], 105, seed=12)
    rng = np.random.default_rng(13)
    returns = rng.normal(0, 0.002, (105, 2))
    returns[:45, 0] += 0.015
    returns[:45, 1] -= 0.005
    returns[45:, 0] -= 0.005
    returns[45:, 1] += 0.015
    close = pd.DataFrame(
        100 * np.cumprod(1 + returns, axis=0), index=data.sessions, columns=data.symbols
    )
    opening = close.shift(1).fillna(100)
    return replace(
        data,
        close=close,
        open=opening,
        high=np.maximum(close, opening),
        low=np.minimum(close, opening),
    )


def test_folds_embargo_selection_oos_membership_and_switching_costs() -> None:
    data = regime_market()
    grid = [{"weights": {"A": 1.0}}, {"weights": {"B": 1.0}}]
    config = BacktestConfig(
        rebalance="daily",
        drift_threshold=0.5,
        costs=CostModel(commission_bps=10),
        fractional_shares=True,
    )
    result = walk_forward(
        factory,
        grid,
        data,
        config,
        train_sessions=20,
        test_sessions=15,
        embargo_sessions=3,
    )
    assert len(result.folds) == 5
    expected_sessions = []
    for i, fold in enumerate(result.folds):
        train_end = data.sessions.get_loc(fold.train_end)
        test_start = data.sessions.get_loc(fold.test_start)
        assert test_start - train_end - 1 == 3
        training = result.variant_returns.loc[fold.train_start : fold.train_end]
        scores = [annual_sharpe(training[j].to_numpy()) for j in range(2)]
        assert fold.variant == int(np.argmax(scores))
        assert fold.is_sharpe == pytest.approx(max(scores))
        assert fold.chosen_params == grid[fold.variant]
        assert fold.oos_sharpe == pytest.approx(
            annual_sharpe(
                result.oos_returns.loc[fold.test_start : fold.test_end].to_numpy()
            )
        )
        if i:
            assert result.folds[i - 1].test_end < fold.test_start
        expected_sessions.extend(
            data.sessions[
                (data.sessions >= fold.test_start) & (data.sessions <= fold.test_end)
            ]
        )
    assert result.oos_returns.index.equals(pd.DatetimeIndex(expected_sessions))
    assert result.folds[0].chosen_params != result.folds[-1].chosen_params
    assert result.selected_params == {"weights": {"B": 1.0}}
    trades = result.backtest.trades
    transition = next(
        f
        for i, f in enumerate(result.folds)
        if i and f.variant != result.folds[i - 1].variant
    )
    fills = trades.loc[trades.decision_session == transition.test_start]
    assert set(fills.side) == {"buy", "sell"}
    assert fills.commission.sum() > 0
    assert (
        result.backtest.costs.loc[transition.test_start : transition.test_end].sum() > 0
    )
    assert result.oos_returns.equals(result.backtest.returns.loc[expected_sessions])
    independently_stitched = pd.concat(
        [
            result.variant_returns[fold.variant].loc[fold.test_start : fold.test_end]
            for fold in result.folds
        ]
    )
    assert not np.allclose(result.oos_returns, independently_stitched)


def test_future_data_does_not_change_earlier_choices() -> None:
    data = regime_market()
    grid = [{"weights": {"A": 1.0}}, {"weights": {"B": 1.0}}]
    config = BacktestConfig(rebalance="weekly")
    full = walk_forward(
        factory,
        grid,
        data,
        config,
        train_sessions=15,
        test_sessions=10,
        embargo_sessions=2,
    )
    early = walk_forward(
        factory,
        grid,
        data.window(None, data.sessions[50]),
        config,
        train_sessions=15,
        test_sessions=10,
        embargo_sessions=2,
    )
    for a, b in zip(full.folds, early.folds):
        assert a == b
    assert np.allclose(full.oos_returns.loc[early.oos_returns.index], early.oos_returns)


def test_stress_uses_exact_oos_sessions_and_preserves_configuration() -> None:
    data = regime_market()
    config = BacktestConfig(rebalance="weekly", extra_delay=2)
    strategy = factory({"weights": {"A": 0.8}})
    sessions = data.sessions[30:70]
    result = stress_test(strategy, data, config, sessions)
    doubled = run_backtest(
        strategy, data, replace(config, costs=config.costs.scaled(2))
    )
    delayed = run_backtest(strategy, data, replace(config, extra_delay=1))
    assert result.sharpe_2x_costs == pytest.approx(
        annual_sharpe(doubled.returns.loc[sessions].to_numpy())
    )
    assert result.sharpe_delay_1 == pytest.approx(
        annual_sharpe(delayed.returns.loc[sessions].to_numpy())
    )
    assert config.extra_delay == 2


def test_insufficient_history_yields_empty_oos_and_no_selection() -> None:
    data = synthetic_market(["SPY"], 10, seed=0)
    result = walk_forward(
        factory, [{"weights": {"SPY": 1.0}}], data, BacktestConfig(), train_sessions=20
    )
    assert result.oos_returns.empty
    assert not result.folds
    assert not result.selected_params


@pytest.mark.parametrize("train,test,embargo", [(1, 2, 0), (2, 0, 0), (2, 2, -1)])
def test_walk_forward_rejects_invalid_windows(
    train: int, test: int, embargo: int
) -> None:
    with pytest.raises(ValueError):
        walk_forward(
            factory,
            [{}],
            synthetic_market(["SPY"], 10, seed=0),
            BacktestConfig(),
            train_sessions=train,
            test_sessions=test,
            embargo_sessions=embargo,
        )


def test_switching_uses_fresh_strategy_instances_without_full_run_state() -> None:
    class ChronologicalStrategy:
        name = "chronological"
        warmup = 1

        def __init__(self) -> None:
            self.last_session: pd.Timestamp | None = None

        def params(self) -> dict[str, Any]:
            return {"weights": {"SPY": 0.5}}

        def target_weights(self, data: MarketData) -> pd.Series:
            session = data.sessions[-1]
            if self.last_session is not None and session <= self.last_session:
                raise ValueError("strategy state from a future decision")
            self.last_session = session
            return pd.Series({"SPY": 0.5})

    result = walk_forward(
        lambda params: ChronologicalStrategy(),
        [{}],
        synthetic_market(["SPY"], 60, seed=1),
        BacktestConfig(rebalance="daily"),
        train_sessions=20,
        test_sessions=10,
        embargo_sessions=2,
    )
    assert len(result.oos_returns) == 30
