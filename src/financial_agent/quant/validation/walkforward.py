"""Rolling selection with embargo and a single cash-continuous OOS portfolio."""

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd  # type: ignore[import-untyped]

from ..backtest import BacktestConfig, BacktestResult, run_backtest
from ..data import MarketData
from ..strategies import Strategy

StrategyFactory = Callable[[Mapping[str, Any]], Strategy]
ParameterGrid = Sequence[Mapping[str, Any]]


def annual_sharpe(returns: np.ndarray) -> float:
    """Zero-rf sample Sharpe annualized at 252 sessions; NaN if undefined."""
    std = float(returns.std(ddof=1)) if len(returns) > 1 else 0.0
    return float(returns.mean() / std * np.sqrt(252)) if std > 0 else float("nan")


@dataclass(frozen=True)
class Fold:
    """Inclusive session bounds; IS/OOS Sharpe are annualized net returns."""

    train_start: pd.Timestamp
    train_end: pd.Timestamp
    test_start: pd.Timestamp
    test_end: pd.Timestamp
    chosen_params: dict[str, Any]
    is_sharpe: float
    oos_sharpe: float
    variant: int


@dataclass(frozen=True)
class WalkForwardResult:
    oos_returns: pd.Series
    folds: tuple[Fold, ...]
    variant_returns: pd.DataFrame
    selected_params: dict[str, Any]
    backtest: BacktestResult


@dataclass(frozen=True)
class _SwitchingStrategy:
    variants: tuple[Strategy, ...]
    windows: tuple[tuple[pd.Timestamp, pd.Timestamp, int], ...]
    name: str = "walk_forward"

    @property
    def warmup(self) -> int:
        return max(s.warmup for s in self.variants)

    def params(self) -> dict[str, Any]:
        return {"variants": [s.params() for s in self.variants]}

    def target_weights(self, data: MarketData) -> pd.Series:
        decision = data.sessions[-1]
        for start, end, variant in self.windows:
            if start <= decision <= end:
                return self.variants[variant].target_weights(data)
        return pd.Series(0.0, index=data.symbols)


def walk_forward(
    factory: StrategyFactory,
    grid: ParameterGrid,
    data: MarketData,
    config: BacktestConfig,
    *,
    train_sessions: int = 1260,
    test_sessions: int = 252,
    embargo_sessions: int = 5,
) -> WalkForwardResult:
    """Select on trailing train windows and trade complete, disjoint test windows.

    Variants are aligned strictly after their latest first decision. Each fold's
    training ends before its embargo; test windows advance by test_sessions.
    The switching portfolio is in cash outside tests and pays all transition
    costs. Final selected_params uses the latest complete trailing train window,
    including observations after the last historical fold, for the next trade.
    """
    for name, value, minimum in (
        ("train_sessions", train_sessions, 2),
        ("test_sessions", test_sessions, 1),
        ("embargo_sessions", embargo_sessions, 0),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
            raise ValueError(f"{name} must be an integer >= {minimum}")
    if not grid:
        raise ValueError("grid must contain at least one variant")
    variants = tuple(factory(dict(params)) for params in grid)
    results = [run_backtest(strategy, data, config) for strategy in variants]
    active = [result.active_start for result in results]
    variant_returns = pd.concat([r.returns for r in results], axis=1)
    variant_returns.columns = pd.RangeIndex(len(variants), name="variant")
    if any(start is None for start in active):
        variant_returns = variant_returns.iloc[:0]
    else:
        latest = max(start for start in active if start is not None)
        variant_returns = variant_returns.loc[variant_returns.index > latest]
    sessions = variant_returns.index

    def choose(training: pd.DataFrame) -> tuple[int, float]:
        scores = [annual_sharpe(training[i].to_numpy()) for i in range(len(variants))]
        usable = np.where(np.isfinite(scores), scores, -np.inf)
        winner = int(np.argmax(usable))
        return winner, scores[winner]

    windows: list[tuple[pd.Timestamp, pd.Timestamp, int]] = []
    records: list[tuple[pd.Timestamp, pd.Timestamp, int, float]] = []
    for train_end in range(
        train_sessions,
        len(sessions) - embargo_sessions - test_sessions + 1,
        test_sessions,
    ):
        training = variant_returns.iloc[train_end - train_sessions : train_end]
        winner, score = choose(training)
        test_start = train_end + embargo_sessions
        windows.append(
            (sessions[test_start], sessions[test_start + test_sessions - 1], winner)
        )
        records.append((training.index[0], training.index[-1], winner, score))
    selected = (
        dict(variants[choose(variant_returns.tail(train_sessions))[0]].params())
        if len(sessions) >= train_sessions
        else {}
    )
    switch_variants = tuple(factory(dict(params)) for params in grid)
    switched = run_backtest(
        _SwitchingStrategy(switch_variants, tuple(windows)), data, config
    )
    mask = np.zeros(len(switched.returns), dtype=bool)
    folds: list[Fold] = []
    for (start, end, winner), (train_start, train_end, _, score) in zip(
        windows, records
    ):
        included = (switched.returns.index >= start) & (switched.returns.index <= end)
        mask |= included
        folds.append(
            Fold(
                train_start,
                train_end,
                start,
                end,
                dict(variants[winner].params()),
                score,
                annual_sharpe(switched.returns.loc[included].to_numpy()),
                winner,
            )
        )
    return WalkForwardResult(
        switched.returns.loc[mask], tuple(folds), variant_returns, selected, switched
    )
