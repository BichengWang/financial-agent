"""Inspectable portfolio histories and net performance summaries."""

from dataclasses import dataclass, field
from typing import Any
import pandas as pd  # type: ignore[import-untyped]
from .config import BacktestConfig
from .metrics import performance_summary


@dataclass(frozen=True)
class BacktestResult:
    equity: pd.Series
    returns: pd.Series
    weights: pd.DataFrame
    trades: pd.DataFrame
    costs: pd.Series
    turnover: pd.Series
    strategy_name: str
    params: dict[str, Any]
    data_fingerprint: str
    config: BacktestConfig
    active_start: pd.Timestamp | None = None
    skipped_trades: pd.DataFrame = field(default_factory=pd.DataFrame)

    def summary(self) -> dict[str, float]:
        """Summarize sessions after the first decision; retain full raw histories.

        No decision (or no later session) yields undefined performance/turnover.
        Costs and trade count cover all executed trades, which occur in this period.
        """
        active_returns = (
            self.returns.loc[self.returns.index > self.active_start]
            if self.active_start is not None
            else self.returns.iloc[:0]
        )
        active_turnover = (
            self.turnover.loc[self.turnover.index > self.active_start]
            if self.active_start is not None
            else self.turnover.iloc[:0]
        )
        result = performance_summary(active_returns)
        result.update(
            total_costs=float(self.costs.sum()),
            average_annual_turnover=(
                float(active_turnover.mean() * 252)
                if len(active_turnover)
                else float("nan")
            ),
            trade_count=float(len(self.trades)),
        )
        return result
