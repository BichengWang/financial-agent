"""Locked, fsynced JSONL audit chain; tampering prevents subsequent appends."""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any
import fcntl
import json
import os
import re

from .broker import BrokerError


@dataclass(frozen=True)
class JournalEvent:
    seq: int
    ts: str
    type: str
    payload: dict[str, Any]
    prev_hash: str
    hash: str


@dataclass(frozen=True)
class JournalCheck:
    ok: bool
    events: int
    first_bad_seq: int | None = None
    reason: str | None = None


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _check_secrets(value: Any) -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if re.search(r"secret|password|token|api_key|key_id", str(key), re.I):
                raise ValueError("secret-like payload keys are forbidden")
            _check_secrets(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _check_secrets(item)


class Journal:
    """One-based sequence; genesis prev_hash is empty; files must be canonical."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _read(content: str) -> tuple[JournalCheck, list[JournalEvent]]:
        events: list[JournalEvent] = []
        previous = ""
        for seq, line in enumerate(content.splitlines(keepends=True), 1):
            try:
                value = json.loads(line)
                event = JournalEvent(**value)
                fields = dict(value)
                digest = fields.pop("hash")
                if (
                    event.seq != seq
                    or event.prev_hash != previous
                    or digest != sha256(_canonical(fields).encode()).hexdigest()
                    or line != _canonical(value) + "\n"
                ):
                    raise ValueError("chain or canonical encoding mismatch")
                _check_secrets(event.payload)
            except (ValueError, TypeError, KeyError):
                return (
                    JournalCheck(False, len(events), seq, "invalid journal record"),
                    events,
                )
            events.append(event)
            previous = digest
        return JournalCheck(True, len(events)), events

    def verify(self) -> JournalCheck:
        """Report the first invalid physical record without exposing its contents."""
        try:
            if not self.path.exists():
                return JournalCheck(True, 0)
            with self.path.open("r", encoding="utf-8", newline="") as handle:
                fcntl.flock(handle, fcntl.LOCK_SH)
                return self._read(handle.read())[0]
        except UnicodeDecodeError as error:
            raw = self.path.read_bytes()
            seq = raw[: error.start].count(b"\n") + 1
            return JournalCheck(False, seq - 1, seq, "invalid UTF-8")

    def events(self, types: Iterable[str] | None = None) -> list[JournalEvent]:
        """Return verified events, optionally filtered by event type."""
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8", newline="") as handle:
            fcntl.flock(handle, fcntl.LOCK_SH)
            try:
                check, records = self._read(handle.read())
            except UnicodeDecodeError:
                raise BrokerError("journal verification failed") from None
        if not check.ok:
            raise BrokerError("journal verification failed")
        selected = None if types is None else set(types)
        return [e for e in records if selected is None or e.type in selected]

    def append(self, event_type: str, payload: Mapping[str, Any]) -> JournalEvent:
        """Reject nested secret keys, verify under lock, append and fsync once."""
        _check_secrets(payload)
        # Freeze a JSON-compatible copy before obtaining the append lock.
        copied = json.loads(_canonical(dict(payload)))
        with self.path.open("a+", encoding="utf-8", newline="") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX)
            handle.seek(0)
            try:
                check, records = self._read(handle.read())
            except UnicodeDecodeError:
                raise BrokerError("journal verification failed") from None
            if not check.ok:
                raise BrokerError("journal verification failed")
            fields = dict(
                seq=check.events + 1,
                ts=datetime.now(timezone.utc).isoformat(),
                type=event_type,
                payload=copied,
                prev_hash=records[-1].hash if records else "",
            )
            event = JournalEvent(
                **fields, hash=sha256(_canonical(fields).encode()).hexdigest()
            )
            handle.write(_canonical(asdict(event)) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        return event
