"""Execution sensitivity of the final selected variant, without re-selection."""

from dataclasses import dataclass, replace

import pandas as pd  # type: ignore[import-untyped]

from ..backtest import BacktestConfig, run_backtest
from ..data import MarketData
from ..strategies import Strategy
from .walkforward import annual_sharpe


@dataclass(frozen=True)
class StressResult:
    sharpe_2x_costs: float
    sharpe_delay_1: float


def stress_test(
    strategy: Strategy,
    data: MarketData,
    config: BacktestConfig,
    oos_sessions: pd.DatetimeIndex,
) -> StressResult:
    """Annualized net Sharpe on the same OOS sessions; delay is one extra session."""
    doubled = run_backtest(
        strategy, data, replace(config, costs=config.costs.scaled(2.0))
    )
    delayed = run_backtest(strategy, data, replace(config, extra_delay=1))
    return StressResult(
        annual_sharpe(doubled.returns.loc[oos_sessions].to_numpy()),
        annual_sharpe(delayed.returns.loc[oos_sessions].to_numpy()),
    )
