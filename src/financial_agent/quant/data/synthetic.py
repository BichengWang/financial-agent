"""Deterministic business-day correlated geometric Brownian market bars."""

from collections.abc import Sequence

import numpy as np
import pandas as pd  # type: ignore[import-untyped]

from .bars import DataError, MarketData


def synthetic_market(
    symbols: Sequence[str],
    sessions: int,
    *,
    seed: int,
    start: str = "2005-01-03",
    annual_drift: float | Sequence[float] = 0.06,
    annual_vol: float | Sequence[float] = 0.18,
    correlation: float = 0.3,
    autocorrelation: float = 0.0,
) -> MarketData:
    """Generate 252-day annualized GBM with stationary AR(1) log returns."""
    count = len(symbols)
    if not count or len(set(symbols)) != count or sessions < 1:
        raise DataError("symbols must be nonempty and unique; sessions positive")
    minimum = -1 / (count - 1) if count > 1 else -1.0
    if not minimum <= correlation <= 1 or not -1 < autocorrelation < 1:
        raise DataError("invalid correlation or autocorrelation")
    drift = np.asarray(annual_drift, dtype=float)
    vol = np.asarray(annual_vol, dtype=float)
    if drift.ndim > 1 or vol.ndim > 1:
        raise DataError("drift and volatility must be scalars or per-symbol sequences")
    if drift.size not in (1, count) or vol.size not in (1, count):
        raise DataError("drift and volatility must match symbol count")
    drift = np.broadcast_to(drift, (count,))
    vol = np.broadcast_to(vol, (count,))
    if not np.isfinite(drift).all() or not np.isfinite(vol).all() or (vol < 0).any():
        raise DataError("drift/volatility must be finite; volatility nonnegative")
    rng = np.random.default_rng(seed)
    covariance = np.full((count, count), correlation)
    np.fill_diagonal(covariance, 1.0)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    root = eigenvectors @ np.diag(np.sqrt(np.maximum(eigenvalues, 0)))
    shocks = rng.standard_normal((sessions, count)) @ root.T
    for i in range(1, sessions):
        shocks[i] = (
            autocorrelation * shocks[i - 1]
            + np.sqrt(1 - autocorrelation**2) * shocks[i]
        )
    returns = (drift - 0.5 * vol**2) / 252 + vol / np.sqrt(252) * shocks
    close = 100 * np.exp(np.cumsum(returns, axis=0))
    opening = np.vstack([np.full(count, 100.0), close[:-1]])
    spread = rng.uniform(0.001, 0.01, (sessions, count))
    index = pd.bdate_range(start, periods=sessions).normalize()

    def frame(values: np.ndarray) -> pd.DataFrame:
        return pd.DataFrame(values, index=index, columns=list(symbols))

    return MarketData(
        open=frame(opening),
        high=frame(np.maximum(opening, close) * (1 + spread)),
        low=frame(np.minimum(opening, close) * (1 - spread)),
        close=frame(close),
        volume=frame(rng.integers(100_000, 10_000_000, (sessions, count))),
        adjusted=True,
        source="synthetic",
    )
