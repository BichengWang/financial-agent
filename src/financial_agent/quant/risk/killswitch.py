"""Persistent emergency stop; any KILL file, including an empty one, engages."""

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

from .state import _atomic_json


class KillSwitch:
    def __init__(self, state_dir: str | Path) -> None:
        self.path = Path(state_dir) / "KILL"

    def engaged(self) -> bool:
        """File existence is authoritative, independently of JSON validity."""
        return self.path.exists()

    def _record(self) -> dict[str, Any]:
        try:
            data = json.loads(self.path.read_text())
        except (ValueError, OSError):
            return {"reason": "manual emergency stop"}
        return data if isinstance(data, dict) else {"reason": "manual emergency stop"}

    def reason(self) -> str | None:
        """Return a readable reason even for hand-written or malformed stops."""
        if not self.engaged():
            return None
        value = self._record().get("reason")
        return (
            value
            if isinstance(value, str) and value.strip()
            else "manual emergency stop"
        )

    def engage(self, reason: str, *, source: str) -> None:
        """Persist a stop atomically with UTC timestamp and breach provenance."""
        if not reason.strip() or not source.strip():
            raise ValueError("reason and source must be nonempty")
        _atomic_json(
            self.path,
            {
                "reason": reason,
                "source": source,
                "engaged_at": datetime.now(timezone.utc).isoformat(),
            },
        )

    def release(self, reason: str, *, operator: str) -> dict[str, Any]:
        """Require explicit operator justification and return a journalable record."""
        if not reason.strip() or not operator.strip():
            raise ValueError("release requires nonempty reason and operator")
        released = self._record() if self.engaged() else None
        self.path.unlink(missing_ok=True)
        return {
            "reason": reason,
            "operator": operator,
            "released": released,
            "released_at": datetime.now(timezone.utc).isoformat(),
        }
