"""Atomic equity-risk persistence; the KILL file alone owns killed status."""

from dataclasses import asdict, dataclass
import json
import math
import os
from pathlib import Path
import tempfile
from typing import Any

from .limits import RiskLimits
from .orders import AccountSnapshot


def _atomic_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(descriptor, "w") as stream:
            json.dump(data, stream, allow_nan=False)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@dataclass(frozen=True)
class RiskState:
    """Positive equity anchors in currency units and their session identifier."""

    high_water_mark: float
    day_start_equity: float
    session: str

    def __post_init__(self) -> None:
        if any(
            not math.isfinite(value) or value <= 0
            for value in (self.high_water_mark, self.day_start_equity)
        ):
            raise ValueError("risk state equity anchors must be positive and finite")
        if not isinstance(self.session, str) or not self.session:
            raise ValueError("session must be a nonempty string")

    @classmethod
    def load(cls, path: str | Path) -> "RiskState":
        """Load persisted anchors; missing or malformed state raises."""
        with Path(path).open() as stream:
            return cls(**json.load(stream))

    def save(self, path: str | Path) -> None:
        """Atomically replace JSON so readers never observe partial state."""
        _atomic_json(Path(path), asdict(self))


def update_risk_state(
    state: RiskState, account: AccountSnapshot, limits: RiskLimits, *, session: str
) -> tuple[RiskState, list[str]]:
    """Roll daily equity on session change, retain HWM and report strict breaches."""
    equity = account.equity
    if not math.isfinite(equity) or equity <= 0:
        return state, [f"equity value={equity} threshold=>0 finite"]
    updated = RiskState(
        max(state.high_water_mark, equity),
        equity if session != state.session else state.day_start_equity,
        session,
    )
    reasons = []
    for name, value, threshold in (
        (
            "max_drawdown_pct",
            1 - equity / updated.high_water_mark,
            limits.max_drawdown_pct,
        ),
        (
            "max_daily_loss_pct",
            1 - equity / updated.day_start_equity,
            limits.max_daily_loss_pct,
        ),
    ):
        if value > threshold and not math.isclose(
            value, threshold, rel_tol=1e-12, abs_tol=1e-12
        ):
            reasons.append(f"{name} value={value:.12g} threshold={threshold:.12g}")
    return updated, reasons
