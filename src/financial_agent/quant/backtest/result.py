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
    skipped_trades: pd.DataFrame = field(default_factory=pd.DataFrame)

    def summary(self) -> dict[str, float]:
        """Net metrics plus currency costs, annual notional turnover and trade count."""
        result = performance_summary(self.returns)
        result.update(
            total_costs=float(self.costs.sum()),
            average_annual_turnover=(
                float(self.turnover.mean() * 252)
                if len(self.turnover)
                else float("nan")
            ),
            trade_count=float(len(self.trades)),
        )
        return result
