"""Multi-horizon trend with EWMA asset vol and sample portfolio covariance."""

from dataclasses import dataclass
from typing import Any
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from ..data import MarketData


@dataclass(frozen=True)
class TrendVolTarget:
    lookbacks: tuple[int, ...]
    vol_halflife: float
    cov_lookback: int
    target_vol: float
    max_weight: float
    name: str = "trend_vol_target"

    @property
    def warmup(self) -> int:
        return max(self.lookbacks) + 1

    def params(self) -> dict[str, Any]:
        return {
            "lookbacks": list(self.lookbacks),
            "vol_halflife": self.vol_halflife,
            "cov_lookback": self.cov_lookback,
            "target_vol": self.target_vol,
            "max_weight": self.max_weight,
        }

    def target_weights(self, data: MarketData) -> pd.Series:
        weights = pd.Series(0.0, index=data.symbols)
        if len(data.sessions) < self.warmup:
            return weights
        close = data.close
        signal = (
            pd.concat(
                [
                    np.sign(close.iloc[-1] / close.iloc[-1 - lag] - 1)
                    for lag in self.lookbacks
                ],
                axis=1,
            )
            .mean(axis=1, skipna=False)
            .clip(lower=0)
        )
        returns = close.pct_change(fill_method=None)
        vol = returns.ewm(halflife=self.vol_halflife).std().iloc[-1] * np.sqrt(252)
        eligible = (signal > 0) & (vol > 0) & np.isfinite(vol)
        eligible &= returns.tail(self.cov_lookback).notna().all()
        eligible &= close.tail(self.warmup).notna().all()
        symbols = list(close.columns[eligible])
        if not symbols or len(returns.tail(self.cov_lookback)) < 2:
            return weights
        raw = (signal[symbols] / vol[symbols]).to_numpy()
        covariance = returns[symbols].tail(self.cov_lookback).cov().to_numpy() * 252
        variance = float(raw @ covariance @ raw)
        if not np.isfinite(variance) or variance <= 0:
            return weights
        weights.loc[symbols] = np.minimum(
            raw * self.target_vol / np.sqrt(variance), self.max_weight
        )
        if weights.sum() > 1:
            weights /= weights.sum()
        return weights


def trend_vol_target(
    lookbacks: tuple[int, ...] = (21, 63, 126, 252),
    vol_halflife: float = 42,
    cov_lookback: int = 126,
    target_vol: float = 0.10,
    max_weight: float = 0.30,
) -> TrendVolTarget:
    """Target annualized sample portfolio volatility before exposure caps."""
    if (
        not lookbacks
        or any(lag < 1 for lag in lookbacks)
        or cov_lookback < 2
        or any(
            not np.isfinite(v) or v <= 0 for v in (vol_halflife, target_vol, max_weight)
        )
        or max_weight > 1
    ):
        raise ValueError(
            "invalid trend lookbacks, volatility, covariance window or cap"
        )
    return TrendVolTarget(
        tuple(lookbacks), vol_halflife, cov_lookback, target_vol, max_weight
    )
