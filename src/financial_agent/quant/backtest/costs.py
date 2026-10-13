"""Explicit fill-price and commission costs; bps are 1/10,000 of notional."""

from dataclasses import dataclass, fields
import math


@dataclass(frozen=True)
class CostModel:
    commission_per_share: float = 0.0
    commission_min: float = 0.0
    commission_bps: float = 0.0
    half_spread_bps: float = 2.0
    slippage_bps: float = 3.0

    def __post_init__(self) -> None:
        if any(
            not math.isfinite(getattr(self, f.name)) or getattr(self, f.name) < 0
            for f in fields(self)
        ):
            raise ValueError("cost components must be finite and nonnegative")
        if self.half_spread_bps + self.slippage_bps >= 10_000:
            raise ValueError("spread plus slippage must be below 10,000 bps")

    def fill_price(self, side: str, reference: float) -> float:
        """Adverse spread and slippage relative to a positive reference price."""
        if (
            side not in ("buy", "sell")
            or not math.isfinite(reference)
            or reference <= 0
        ):
            raise ValueError("require buy/sell and a positive finite reference")
        return reference * (
            1
            + (1 if side == "buy" else -1)
            * (self.half_spread_bps + self.slippage_bps)
            / 10_000
        )

    def commission(self, shares: float, price: float) -> float:
        """Currency commission on absolute shares and executed notional."""
        if not math.isfinite(shares) or not math.isfinite(price) or price <= 0:
            raise ValueError("require finite shares and positive finite price")
        if shares == 0:
            return 0.0
        return max(
            self.commission_min,
            abs(shares)
            * (self.commission_per_share + self.commission_bps / 10_000 * price),
        )

    def scaled(self, factor: float) -> "CostModel":
        """Multiply every cost component by a finite nonnegative factor."""
        if not math.isfinite(factor) or factor < 0:
            raise ValueError("factor must be finite and nonnegative")
        return CostModel(
            **{f.name: getattr(self, f.name) * factor for f in fields(self)}
        )

    @classmethod
    def zero(cls) -> "CostModel":
        """Explicitly disable every cost component."""
        return cls(0, 0, 0, 0, 0)
