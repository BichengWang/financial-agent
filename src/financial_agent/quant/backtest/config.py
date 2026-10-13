"""Validated backtest settings; cash earns zero interest."""

from collections.abc import Mapping
from dataclasses import dataclass
import math
from typing import Literal
import pandas as pd  # type: ignore[import-untyped]
from .costs import CostModel


@dataclass(frozen=True)
class BacktestConfig:
    initial_cash: float = 100_000.0
    cash_buffer: float = 0.0
    rebalance: Literal["daily", "weekly", "monthly"] = "weekly"
    drift_threshold: float = 0.02
    execution: Literal["next_open", "next_close"] = "next_open"
    extra_delay: int = 0
    fractional_shares: bool = False
    min_trade_notional: float = 0.0
    costs: CostModel = CostModel()
    start: pd.Timestamp | None = None

    def __post_init__(self) -> None:
        if not math.isfinite(self.initial_cash) or self.initial_cash <= 0:
            raise ValueError("initial_cash must be finite and positive")
        if (
            isinstance(self.cash_buffer, bool)
            or not isinstance(self.cash_buffer, (int, float))
            or not math.isfinite(self.cash_buffer)
            or not 0 <= self.cash_buffer < 1
        ):
            raise ValueError("cash_buffer must be finite in [0, 1)")
        if self.rebalance not in (
            "daily",
            "weekly",
            "monthly",
        ) or self.execution not in ("next_open", "next_close"):
            raise ValueError("invalid rebalance or execution")
        if (
            not isinstance(self.extra_delay, int)
            or isinstance(self.extra_delay, bool)
            or self.extra_delay < 0
        ):
            raise ValueError("extra_delay must be a nonnegative integer")
        if any(
            not math.isfinite(v) or v < 0
            for v in (self.drift_threshold, self.min_trade_notional)
        ):
            raise ValueError("thresholds must be finite and nonnegative")
        if not isinstance(self.fractional_shares, bool) or not isinstance(
            self.costs, CostModel
        ):
            raise ValueError("invalid fractional_shares or costs")
        if self.start is not None:
            start = pd.Timestamp(self.start)
            if pd.isna(start) or start.tzinfo is not None:
                raise ValueError("start must be a valid timezone-naive timestamp")
            object.__setattr__(self, "start", start)

    def buffered_targets(self, targets: Mapping[str, float]) -> dict[str, float]:
        """Cap valid long-only target gross at 1 - cash_buffer, preserving ratios.

        Already defensive allocations stay unchanged. This is a decision-price
        reserve; gaps, subsequent price moves and execution costs can consume it.
        """
        total = sum(targets.values())
        if (
            any(not math.isfinite(w) or w < 0 for w in targets.values())
            or total > 1 + 1e-9
        ):
            raise ValueError("targets must be finite, nonnegative and sum to at most 1")
        factor = min(1.0, (1 - self.cash_buffer) / total) if total else 1.0
        return {symbol: weight * factor for symbol, weight in targets.items()}
