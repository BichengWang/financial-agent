"""Incremental CSV cache with overlap-based adjustment revision detection."""

from collections.abc import Callable, Sequence
import datetime as dt
import json
import os
from pathlib import Path
import tempfile
from typing import Any
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd  # type: ignore[import-untyped]

from .bars import DataError, MarketData
from .providers import (
    BarProvider,
    CsvProvider,
    assemble,
    symbol_frame,
    validate_request,
)

EXCHANGE_TZ = ZoneInfo("America/New_York")


def _retrieved_after(record: dict[str, Any], session: dt.date) -> bool:
    """Whether the record was retrieved on a New York date after `session`."""
    try:
        retrieved = dt.datetime.fromisoformat(record["retrieved_at"])
    except (KeyError, TypeError, ValueError):
        return False
    return (
        retrieved.tzinfo is not None
        and retrieved.astimezone(EXCHANGE_TZ).date() > session
    )


class CachedProvider:
    """Cache received session coverage; refresh five sessions of tail overlap."""

    def __init__(
        self,
        inner: BarProvider,
        cache_dir: str | Path,
        *,
        overlap_sessions: int = 5,
        rtol: float = 1e-9,
        atol: float = 1e-12,
        now: Callable[[], dt.datetime] | None = None,
    ) -> None:
        """`now` is the retrieval clock; it must return timezone-aware datetimes."""
        if overlap_sessions < 1 or rtol < 0 or atol < 0:
            raise DataError("overlap must be positive and tolerances nonnegative")
        self.inner = inner
        self.cache_dir = Path(cache_dir)
        self.overlap_sessions = overlap_sessions
        self.rtol = rtol
        self.atol = atol
        self.now = now or (lambda: dt.datetime.now(dt.timezone.utc))

    def _atomic_write(self, path: Path, content: str) -> None:
        descriptor, temporary = tempfile.mkstemp(dir=self.cache_dir, prefix=".tmp-")
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(content)
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    def _fetch_symbol(self, symbol: str, start: dt.date, end: dt.date) -> MarketData:
        fresh = self.inner.fetch([symbol], start, end)
        if fresh.symbols != (symbol,):
            raise DataError(f"cache: provider returned wrong symbols for {symbol}")
        return fresh.window(pd.Timestamp(start), pd.Timestamp(end))

    def fetch(self, symbols: Sequence[str], start: dt.date, end: dt.date) -> MarketData:
        validate_request(symbols, start, end)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        meta_path = self.cache_dir / "_meta.json"
        try:
            metadata: dict[str, Any] = (
                json.loads(meta_path.read_text()) if meta_path.exists() else {}
            )
            if not isinstance(metadata, dict) or any(
                not isinstance(record, dict) for record in metadata.values()
            ):
                raise ValueError("expected an object of symbol metadata objects")
        except (OSError, ValueError) as exc:
            raise DataError(f"cache: invalid metadata: {exc}") from exc
        frames = {}
        conventions: set[tuple[bool, str]] = set()
        inner_source = getattr(self.inner, "source", None)
        for symbol in symbols:
            record: dict[str, Any] = metadata.get(symbol, {})
            if inner_source is not None and record.get("source") != inner_source:
                record = {}  # bars from another provider are not a cache hit
            cached = None
            if (
                record.get("first_session") is not None
                and (self.cache_dir / f"{symbol}.csv").exists()
            ):
                cached = CsvProvider(self.cache_dir, adjusted=record["adjusted"]).fetch(
                    [symbol], dt.date.min, dt.date.max
                )
            covered_start = (
                dt.date.fromisoformat(record["covered_start"]) if record else start
            )
            covered_end = (
                dt.date.fromisoformat(record["covered_end"])
                if record.get("covered_end") is not None
                else None
            )
            needs_full = cached is None or start < covered_start
            # A last bar retrieved on or before its own session date may be intraday.
            needs_tail = not needs_full and (
                covered_end is None
                or end > covered_end
                or (end == covered_end and not _retrieved_after(record, covered_end))
            )
            if needs_full or needs_tail:
                full_start = min(start, covered_start)
                full_end = max(end, covered_end) if covered_end is not None else end
                fetch_start = full_start
                if needs_tail and cached is not None and len(cached.sessions):
                    fetch_start = max(
                        full_start,
                        cached.sessions[-self.overlap_sessions :][0].date(),
                    )
                retrieved_at: str | None = (
                    self.now().astimezone(dt.timezone.utc).isoformat()
                )
                fresh = self._fetch_symbol(symbol, fetch_start, full_end)
                incoming = symbol_frame(fresh, symbol)
                if incoming.empty and cached is not None:
                    incoming = symbol_frame(cached, symbol)
                    retrieved_at = record.get("retrieved_at")  # nothing new arrived
                elif cached is not None and needs_tail:
                    old = symbol_frame(cached, symbol)
                    overlap = old.index[old.index >= pd.Timestamp(fetch_start)]
                    changed = (
                        fresh.adjusted != record["adjusted"]
                        or fresh.source != record["source"]
                        or not np.allclose(
                            old.loc[overlap].to_numpy(dtype=float),
                            incoming.reindex(overlap).to_numpy(dtype=float),
                            rtol=self.rtol,
                            atol=self.atol,
                            equal_nan=True,
                        )
                    )
                    if changed:
                        fresh = self._fetch_symbol(symbol, full_start, full_end)
                        incoming = symbol_frame(fresh, symbol)
                    else:
                        incoming = pd.concat(
                            [old.loc[old.index < pd.Timestamp(fetch_start)], incoming]
                        ).sort_index()
                self._atomic_write(
                    self.cache_dir / f"{symbol}.csv",
                    incoming.to_csv(index_label="date", float_format="%.17g"),
                )
                record = {
                    "source": fresh.source,
                    "adjusted": fresh.adjusted,
                    "retrieved_at": retrieved_at,
                    "first_session": (
                        incoming.index[0].date().isoformat() if len(incoming) else None
                    ),
                    "last_session": (
                        incoming.index[-1].date().isoformat() if len(incoming) else None
                    ),
                    "covered_start": full_start.isoformat(),
                    "covered_end": (
                        incoming.index[-1].date().isoformat()
                        if len(incoming)
                        else (
                            covered_end.isoformat() if covered_end is not None else None
                        )
                    ),
                }
                metadata[symbol] = record
                self._atomic_write(meta_path, json.dumps(metadata, indent=2))
            else:
                assert cached is not None
                incoming = symbol_frame(cached, symbol)
            conventions.add((record["adjusted"], record["source"]))
            frames[symbol] = incoming.loc[
                (incoming.index >= pd.Timestamp(start))
                & (incoming.index <= pd.Timestamp(end))
            ]
        if len(conventions) != 1:
            raise DataError("cache: mixed source or adjustment conventions")
        adjusted, source = conventions.pop()
        return assemble(frames, adjusted=adjusted, source=source)
