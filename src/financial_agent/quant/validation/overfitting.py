"""Selection-bias statistics using per-period, zero-risk-free-rate Sharpe."""

from dataclasses import dataclass
from itertools import combinations
import math
from statistics import NormalDist

import numpy as np
from numpy.typing import ArrayLike
import pandas as pd  # type: ignore[import-untyped]


@dataclass(frozen=True)
class PBOResult:
    """CSCV relative ranks, absolute OOS loss probability and OLS degradation."""

    pbo: float
    logits: tuple[float, ...]
    n_combinations: int
    prob_oos_loss: float
    degradation_slope: float


def _returns(returns: ArrayLike, minimum: int = 4) -> np.ndarray:
    values = np.asarray(returns, dtype=float)
    if values.ndim != 1 or len(values) < minimum or not np.isfinite(values).all():
        raise ValueError(
            f"returns must be one-dimensional, finite, and length >= {minimum}"
        )
    return values


def probabilistic_sharpe_ratio(returns: ArrayLike, sr_benchmark: float = 0.0) -> float:
    """Bailey PSR; sample Sharpe, adjusted skew and non-excess kurtosis.

    At least four finite observations and positive sample variance are required.
    Sharpe and its benchmark are per-period, never annualized.
    """
    values = _returns(returns)
    std = float(values.std(ddof=1))
    if std <= 0 or not math.isfinite(sr_benchmark):
        raise ValueError("positive return variance and finite benchmark required")
    sr = float(values.mean()) / std
    series = pd.Series(values)
    skew, kurtosis = float(series.skew()), float(series.kurt()) + 3
    variance = 1 - skew * sr + (kurtosis - 1) / 4 * sr**2
    if not math.isfinite(variance) or variance <= 0:
        raise ValueError("nonpositive Sharpe estimator variance")
    z = (sr - sr_benchmark) * math.sqrt(len(values) - 1) / math.sqrt(variance)
    return NormalDist().cdf(z)


def expected_max_sharpe(n_trials: int, trials_sharpe_variance: float) -> float:
    """Expected maximum of N trials in per-period Sharpe units."""
    if isinstance(n_trials, bool) or not isinstance(n_trials, int) or n_trials < 1:
        raise ValueError("n_trials must be a positive integer")
    if not math.isfinite(trials_sharpe_variance) or trials_sharpe_variance < 0:
        raise ValueError("trials_sharpe_variance must be finite and nonnegative")
    if n_trials == 1 or trials_sharpe_variance == 0:
        return 0.0
    normal = NormalDist()
    gamma = 0.5772156649015329
    return math.sqrt(trials_sharpe_variance) * (
        (1 - gamma) * normal.inv_cdf(1 - 1 / n_trials)
        + gamma * normal.inv_cdf(1 - 1 / (n_trials * math.e))
    )


def deflated_sharpe_ratio(
    returns: ArrayLike, *, n_trials: int, trials_sharpe_variance: float
) -> float:
    """PSR against the expected maximum Sharpe across the searched trials."""
    benchmark = expected_max_sharpe(n_trials, trials_sharpe_variance)
    return probabilistic_sharpe_ratio(returns, benchmark)


def pbo_cscv(variant_returns: pd.DataFrame, n_splits: int = 16) -> PBOResult:
    """Enumerate equal-block half-sample partitions; discard leading remainder.

    Ascending OOS ranks use average ties (worst=1, best=N). IS ties choose the
    first column deterministically. Loss means selected OOS Sharpe <= 0.
    Degradation is OLS OOS-on-IS slope with an intercept, in per-period Sharpe
    units; constant selected IS Sharpe yields NaN. Nonfinite inputs/undefined
    Sharpe fail.
    """
    if (
        isinstance(n_splits, bool)
        or not isinstance(n_splits, int)
        or n_splits < 2
        or n_splits % 2
    ):
        raise ValueError("n_splits must be an even integer >= 2")
    values = variant_returns.to_numpy(dtype=float)
    if (
        values.ndim != 2
        or values.shape[1] < 2
        or len(values) < n_splits
        or not np.isfinite(values).all()
        or not variant_returns.columns.is_unique
    ):
        raise ValueError("need >= 2 unique variants, finite returns and enough rows")
    block = len(values) // n_splits
    count = block * (n_splits // 2)
    if count < 2:
        raise ValueError("each half-sample needs at least two observations")
    blocks = values[len(values) % n_splits :].reshape(n_splits, block, -1)
    sums, squares = blocks.sum(axis=1), (blocks**2).sum(axis=1)
    total, total_squares = sums.sum(axis=0), squares.sum(axis=0)

    def sharpe(s: np.ndarray, q: np.ndarray) -> np.ndarray:
        variance = (q - s**2 / count) / (count - 1)
        if (variance <= 0).any():
            raise ValueError("CSCV half-sample Sharpe requires positive variance")
        return np.asarray((s / count) / np.sqrt(variance), dtype=float)

    logits: list[float] = []
    selected_is: list[float] = []
    selected_oos: list[float] = []
    for selected in combinations(range(n_splits), n_splits // 2):
        s, q = sums[list(selected)].sum(axis=0), squares[list(selected)].sum(axis=0)
        ins = sharpe(s, q)
        winner = int(np.argmax(ins))
        oos = sharpe(total - s, total_squares - q)
        score = oos[winner]
        selected_is.append(float(ins[winner]))
        selected_oos.append(float(score))
        rank = 1 + int((oos < score).sum()) + (int((oos == score).sum()) - 1) / 2
        omega = rank / (values.shape[1] + 1)
        logits.append(math.log(omega / (1 - omega)))
    x, y = np.asarray(selected_is), np.asarray(selected_oos)
    centered = x - x.mean()
    variance = float(centered @ centered)
    slope = (
        float(centered @ (y - y.mean()) / variance) if variance > 0 else float("nan")
    )
    return PBOResult(
        float(np.mean(np.asarray(logits) <= 0)),
        tuple(logits),
        len(logits),
        float(np.mean(y <= 0)),
        slope,
    )
