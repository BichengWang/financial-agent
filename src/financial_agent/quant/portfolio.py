"""Pure target-weight to share-delta planning shared by backtest and live."""

from collections.abc import Mapping
import math
import pandas as pd  # type: ignore[import-untyped]


def rebalance_deltas(
    targets: Mapping[str, float] | pd.Series,
    positions: Mapping[str, float] | pd.Series,
    prices: Mapping[str, float] | pd.Series,
    nav: float,
    *,
    drift_threshold: float,
    fractional: bool,
    min_trade_notional: float,
) -> dict[str, float]:
    """Plan sorted share deltas at reference prices, preserving long-only positions.

    Missing targets mean zero exposure. Invalid/missing prices are skipped. Full
    exits bypass drift filtering; whole-share sales never exceed held quantity.
    Notional is in currency units; drift_threshold is a portfolio weight fraction.
    """
    targets = dict(targets)
    positions = dict(positions)
    prices = dict(prices)
    if not math.isfinite(nav) or nav <= 0:
        raise ValueError("nav must be positive and finite")
    if any(
        not math.isfinite(v) or v < 0 for v in (drift_threshold, min_trade_notional)
    ):
        raise ValueError("thresholds must be finite and nonnegative")
    if any(not math.isfinite(v) or v < 0 for v in positions.values()):
        raise ValueError("positions must be finite and nonnegative")
    if (
        any(not math.isfinite(v) or v < 0 for v in targets.values())
        or sum(targets.values()) > 1 + 1e-9
    ):
        raise ValueError("targets must be finite, nonnegative and sum to at most 1")
    deltas: dict[str, float] = {}
    for symbol in sorted(set(targets) | set(positions)):
        price = prices.get(symbol, float("nan"))
        if not math.isfinite(price) or price <= 0:
            continue
        held = positions.get(symbol, 0.0)
        target = targets.get(symbol, 0.0)
        if target != 0 or held == 0:
            if abs(target - held * price / nav) < drift_threshold:
                continue
        delta = target * nav / price - held
        if not fractional and target != 0:
            delta = float(math.trunc(delta))
        delta = max(delta, -held)
        if delta and abs(delta * price) >= min_trade_notional:
            deltas[symbol] = delta
    return deltas
