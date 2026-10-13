"""Seeded circular block bootstrap preserving local serial dependence."""

from collections.abc import Callable
import math

import numpy as np
from numpy.typing import ArrayLike

from .overfitting import _returns


def block_bootstrap_ci(
    returns: ArrayLike,
    statistic: Callable[[np.ndarray], float],
    *,
    n: int = 2000,
    block: int = 21,
    seed: int,
    alpha: float = 0.10,
) -> tuple[float, float]:
    """Equal-tailed percentile CI; wrap blocks and truncate to original length."""
    values = _returns(returns, minimum=2)
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (n, block)):
        raise ValueError("n and block must be positive integers")
    if not math.isfinite(alpha) or not 0 < alpha < 1:
        raise ValueError("alpha must be between zero and one")
    if isinstance(seed, bool) or not isinstance(seed, int) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.default_rng(seed)
    estimates = np.empty(n)
    offsets = np.arange(block)
    for i in range(n):
        starts = rng.integers(0, len(values), size=math.ceil(len(values) / block))
        indices = ((starts[:, None] + offsets) % len(values)).ravel()[: len(values)]
        estimates[i] = statistic(values[indices])
    if not np.isfinite(estimates).all():
        raise ValueError("bootstrap statistic must be finite for every sample")
    lo, hi = np.quantile(estimates, [alpha / 2, 1 - alpha / 2])
    return float(lo), float(hi)
