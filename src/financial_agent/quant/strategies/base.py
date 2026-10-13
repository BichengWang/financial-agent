"""Long-only, unlevered strategy contract and output validation."""

from typing import Any, Protocol
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from ..data import MarketData


class StrategyError(ValueError):
    """A strategy produced invalid target weights."""


class Strategy(Protocol):
    @property
    def name(self) -> str: ...

    @property
    def warmup(self) -> int: ...

    def params(self) -> dict[str, Any]: ...

    def target_weights(self, data: MarketData) -> pd.Series: ...


def validate_weights(
    strategy: Strategy, data: MarketData, weights: pd.Series
) -> pd.Series:
    """Validate finite nonnegative exposure; absent symbols become cash weights."""
    if not isinstance(weights, pd.Series):
        raise StrategyError(f"{strategy.name}: expected Series, got {weights!r}")
    try:
        values = weights.to_numpy(dtype=float)
        valid = (
            weights.index.is_unique
            and set(weights.index) <= set(data.symbols)
            and np.isfinite(values).all()
            and (values >= 0).all()
            and values.sum() <= 1 + 1e-9
        )
    except (TypeError, ValueError):
        valid = False
    if not valid:
        raise StrategyError(f"{strategy.name}: invalid weights {weights.to_dict()!r}")
    return weights.astype(float).reindex(data.symbols, fill_value=0.0)
