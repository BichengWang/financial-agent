"""Deterministic relative momentum with an absolute defensive filter."""

from dataclasses import dataclass
from typing import Any
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from ..data import MarketData


@dataclass(frozen=True)
class DualMomentum:
    risk_assets: tuple[str, ...]
    defensive: str
    lookback: int
    skip: int
    top_k: int
    name: str = "dual_momentum"

    @property
    def warmup(self) -> int:
        return self.lookback + 1

    def params(self) -> dict[str, Any]:
        return {
            "risk_assets": list(self.risk_assets),
            "defensive": self.defensive,
            "lookback": self.lookback,
            "skip": self.skip,
            "top_k": self.top_k,
        }

    def target_weights(self, data: MarketData) -> pd.Series:
        weights = pd.Series(0.0, index=data.symbols)
        if len(data.sessions) < self.warmup:
            return weights
        momentum = (
            data.close.iloc[-1 - self.skip] / data.close.iloc[-1 - self.lookback] - 1
        )
        eligible = [
            s
            for s in self.risk_assets
            if s in momentum.index and np.isfinite(momentum[s]) and momentum[s] > 0
        ]
        selected = sorted(eligible, key=lambda s: (-momentum[s], s))[: self.top_k]
        weights.loc[selected] = 1 / self.top_k
        remaining = self.top_k - len(selected)
        if (
            self.defensive in momentum.index
            and np.isfinite(momentum[self.defensive])
            and momentum[self.defensive] > 0
        ):
            weights[self.defensive] += remaining / self.top_k
        return weights


def dual_momentum(
    risk_assets: tuple[str, ...] = (
        "SPY",
        "QQQ",
        "IWM",
        "EFA",
        "EEM",
        "VNQ",
        "GLD",
        "DBC",
    ),
    defensive: str = "IEF",
    lookback: int = 252,
    skip: int = 21,
    top_k: int = 3,
) -> DualMomentum:
    """Use close[t-skip]/close[t-lookback]-1; unfilled slots are defensive/cash."""
    if (
        lookback <= skip
        or skip < 0
        or top_k < 1
        or len(set(risk_assets)) != len(risk_assets)
    ):
        raise ValueError("require lookback > skip >= 0, top_k >= 1, unique risk_assets")
    return DualMomentum(tuple(risk_assets), defensive, lookback, skip, top_k)
