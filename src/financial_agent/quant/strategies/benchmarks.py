"""Fixed-weight benchmark factories; the engine supplies rebalance cadence."""

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from ..data import MarketData


@dataclass(frozen=True)
class FixedWeights:
    name: str
    allocations: tuple[tuple[str, float], ...]
    warmup: int = 1

    def params(self) -> dict[str, Any]:
        if self.name == "sixty_forty":
            return {
                "equity": self.allocations[0][0],
                "bonds": self.allocations[1][0],
                "equity_weight": self.allocations[0][1],
            }
        return {"weights": dict(self.allocations)}

    def target_weights(self, data: MarketData) -> pd.Series:
        weights: dict[str, float] = {}
        for symbol, weight in self.allocations:
            if symbol in data.symbols:
                weights[symbol] = weights.get(symbol, 0.0) + weight
        return pd.Series(weights, dtype=float).reindex(data.symbols, fill_value=0.0)


def buy_and_hold(weights: Mapping[str, float] | None = None) -> FixedWeights:
    """Hold fixed long-only allocations; missing assets remain in cash."""
    chosen = dict({"SPY": 1.0} if weights is None else weights)
    if (
        any(not isinstance(s, str) or not s for s in chosen)
        or any(not np.isfinite(w) or w < 0 for w in chosen.values())
        or sum(chosen.values()) > 1 + 1e-9
    ):
        raise ValueError("weights must be finite, nonnegative, and sum to at most 1")
    return FixedWeights("buy_and_hold", tuple(sorted(chosen.items())))


def sixty_forty(
    equity: str = "SPY", bonds: str = "IEF", equity_weight: float = 0.6
) -> FixedWeights:
    """Allocate equity_weight to equity and the remainder to bonds."""
    if not np.isfinite(equity_weight) or not 0 <= equity_weight <= 1:
        raise ValueError("equity_weight must be in [0, 1]")
    return FixedWeights(
        "sixty_forty", ((equity, equity_weight), (bonds, 1 - equity_weight))
    )
