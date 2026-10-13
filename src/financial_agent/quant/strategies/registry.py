"""Validated strategy construction from JSON-compatible parameters."""

from collections.abc import Callable, Mapping
import inspect
from typing import Any, get_args, get_origin, get_type_hints
from .base import Strategy
from .benchmarks import buy_and_hold, sixty_forty
from .momentum import dual_momentum
from .trend import trend_vol_target
from .research import ResearchForecastStrategy

STRATEGIES: dict[str, Callable[..., Strategy]] = {
    "research_forecast": ResearchForecastStrategy,
    "trend_vol_target": trend_vol_target,
    "dual_momentum": dual_momentum,
    "buy_and_hold": buy_and_hold,
    "sixty_forty": sixty_forty,
}


def _matches(value: Any, annotation: Any) -> bool:
    origin = get_origin(annotation)
    args = get_args(annotation)
    if origin is tuple:
        return isinstance(value, (tuple, list)) and all(
            _matches(v, args[0]) for v in value
        )
    if origin is Mapping:
        return isinstance(value, Mapping) and all(
            _matches(k, args[0]) and _matches(v, args[1]) for k, v in value.items()
        )
    if origin is not None:
        return any(_matches(value, arg) for arg in args)
    if annotation is float:
        return isinstance(value, (float, int)) and not isinstance(value, bool)
    if annotation is int:
        return isinstance(value, int) and not isinstance(value, bool)
    if annotation is type(None):
        return value is None
    return isinstance(value, annotation)


def build_strategy(name: str, params: Mapping[str, Any] | None = None) -> Strategy:
    """Reject unknown strategies/parameters and wrong types before construction."""
    if name not in STRATEGIES:
        raise ValueError(
            f"Unknown strategy {name!r}; valid names: {sorted(STRATEGIES)}"
        )
    factory = STRATEGIES[name]
    supplied = dict(params or {})
    valid = list(inspect.signature(factory).parameters)
    hints = get_type_hints(factory.__init__ if inspect.isclass(factory) else factory)
    invalid = [
        key
        for key, value in supplied.items()
        if key not in valid or not _matches(value, hints[key])
    ]
    if invalid:
        raise ValueError(
            f"{name}: unknown or ill-typed params {invalid}; valid params: {valid}"
        )
    try:
        return factory(**supplied)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: {exc}; valid params: {valid}") from exc
