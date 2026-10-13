"""Incremental CSV cache with overlap-based adjustment revision detection."""

from collections.abc import Sequence
import datetime as dt
import json
import os
from pathlib import Path
import tempfile
from typing import Any

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


class CachedProvider:
    """Cache inclusive request coverage; refresh five sessions of tail overlap."""

    def __init__(
        self,
        inner: BarProvider,
        cache_dir: str | Path,
        *,
        overlap_sessions: int = 5,
        rtol: float = 1e-9,
        atol: float = 1e-12,
    ) -> None:
        if overlap_sessions < 1 or rtol < 0 or atol < 0:
            raise DataError("overlap must be positive and tolerances nonnegative")
        self.inner = inner
        self.cache_dir = Path(cache_dir)
        self.overlap_sessions = overlap_sessions
        self.rtol = rtol
        self.atol = atol

    def _atomic_write(self, path: Path, content: str) -> None:
        descriptor, temporary = tempfile.mkstemp(dir=self.cache_dir, prefix=".tmp-")
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(content)
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    def fetch(self, symbols: Sequence[str], start: dt.date, end: dt.date) -> MarketData:
        validate_request(symbols, start, end)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        meta_path = self.cache_dir / "_meta.json"
        try:
            metadata: dict[str, Any] = (
                json.loads(meta_path.read_text()) if meta_path.exists() else {}
            )
        except (OSError, ValueError) as exc:
            raise DataError(f"cache: invalid metadata: {exc}") from exc
        frames = {}
        conventions: set[tuple[bool, str]] = set()
        for symbol in symbols:
            record: dict[str, Any] = metadata.get(symbol, {})
            cached = None
            if record and (self.cache_dir / f"{symbol}.csv").exists():
                cached = CsvProvider(self.cache_dir, adjusted=record["adjusted"]).fetch(
                    [symbol], dt.date.min, dt.date.max
                )
            covered_start = (
                dt.date.fromisoformat(record["covered_start"]) if record else start
            )
            covered_end = (
                dt.date.fromisoformat(record["covered_end"]) if record else start
            )
            needs_full = cached is None or start < covered_start
            needs_tail = not needs_full and end > covered_end
            if needs_full or needs_tail:
                full_start = min(start, covered_start)
                full_end = max(end, covered_end) if cached is not None else end
                fetch_start = full_start
                if needs_tail and cached is not None and len(cached.sessions):
                    fetch_start = max(
                        full_start,
                        cached.sessions[-self.overlap_sessions :][0].date(),
                    )
                fresh = self.inner.fetch([symbol], fetch_start, full_end)
                if fresh.symbols != (symbol,):
                    raise DataError(
                        f"cache: provider returned wrong symbols for {symbol}"
                    )
                fresh = fresh.window(pd.Timestamp(fetch_start), pd.Timestamp(full_end))
                incoming = symbol_frame(fresh, symbol)
                if cached is not None and needs_tail:
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
                        fresh = self.inner.fetch([symbol], full_start, full_end)
                        if fresh.symbols != (symbol,):
                            raise DataError(f"cache: wrong symbols for {symbol}")
                        incoming = symbol_frame(
                            fresh.window(
                                pd.Timestamp(full_start), pd.Timestamp(full_end)
                            ),
                            symbol,
                        )
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
                    "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "first_session": (
                        incoming.index[0].date().isoformat() if len(incoming) else None
                    ),
                    "last_session": (
                        incoming.index[-1].date().isoformat() if len(incoming) else None
                    ),
                    "covered_start": full_start.isoformat(),
                    "covered_end": full_end.isoformat(),
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
