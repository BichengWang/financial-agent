"""Validated policy fractions; runtime overrides can only tighten limits."""

from collections.abc import Mapping
from dataclasses import dataclass, fields, replace
import math
from pathlib import Path
import tomllib
from typing import Any


class RiskConfigError(ValueError):
    """A runtime override attempts to loosen policy."""


@dataclass(frozen=True)
class RiskLimits:
    """Exposure/loss limits are equity fractions; symbols empty means unrestricted."""

    max_weight: float = 0.30
    max_gross: float = 1.0
    allow_short: bool = False
    max_order_notional_pct: float = 0.35
    max_turnover_pct: float = 1.0
    max_daily_loss_pct: float = 0.03
    max_drawdown_pct: float = 0.20
    min_cash_pct: float = 0.01
    price_band_pct: float = 0.05
    max_orders: int = 50
    allowed_symbols: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for field in fields(self):
            value = getattr(self, field.name)
            if field.name in {"allowed_symbols", "allow_short", "max_orders"}:
                continue
            upper = math.inf if field.name in {"max_gross", "max_turnover_pct"} else 1
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not 0 <= value <= upper
            ):
                raise ValueError(f"{field.name} must be finite in [0, {upper}]")
        if not isinstance(self.allow_short, bool):
            raise ValueError("allow_short must be boolean")
        if (
            isinstance(self.max_orders, bool)
            or not isinstance(self.max_orders, int)
            or self.max_orders < 0
        ):
            raise ValueError("max_orders must be a nonnegative integer")
        if not isinstance(self.allowed_symbols, (tuple, list)) or any(
            not isinstance(s, str) or not s.strip() for s in self.allowed_symbols
        ):
            raise ValueError("allowed_symbols must contain nonempty strings")
        object.__setattr__(self, "allowed_symbols", tuple(self.allowed_symbols))

    @classmethod
    def load(cls, path: str | Path | None = None) -> "RiskLimits":
        """Read the risk table, rejecting unknown keys and malformed values."""
        policy = (
            Path(path)
            if path is not None
            else Path(__file__).parents[1] / "quant_policy.toml"
        )
        with policy.open("rb") as stream:
            data = tomllib.load(stream)
        table = data.get("risk")
        if not isinstance(table, dict):
            raise ValueError("policy must contain a [risk] table")
        cls._check_keys(table)
        return cls(**table)

    @staticmethod
    def _check_keys(values: Mapping[str, Any]) -> None:
        unknown = set(values) - {field.name for field in fields(RiskLimits)}
        if unknown:
            raise ValueError(f"unknown risk keys: {sorted(unknown)}")

    def tighten(self, overrides: Mapping[str, Any]) -> "RiskLimits":
        """Return validated stricter limits; reject every expansion of permissions."""
        self._check_keys(overrides)
        try:
            candidate = replace(self, **dict(overrides))
        except ValueError as exc:
            raise RiskConfigError(f"invalid risk override: {exc}") from exc
        for key in overrides:
            old, new = getattr(self, key), getattr(candidate, key)
            loosens = (
                (key.startswith("max_") and new > old)
                or (key == "price_band_pct" and new > old)
                or (key == "min_cash_pct" and new < old)
                or (key == "allow_short" and not old and new)
                or (
                    key == "allowed_symbols"
                    and bool(old)
                    and (not new or not set(new).issubset(old))
                )
            )
            if loosens:
                raise RiskConfigError(f"{key} override {new!r} loosens policy {old!r}")
        return candidate
