"""Inclusive date-range providers and lossless per-symbol CSV interchange."""

from collections.abc import Sequence
import datetime as dt
from pathlib import Path
import time
from typing import Protocol

import pandas as pd  # type: ignore[import-untyped]
import yfinance as yf  # type: ignore[import-untyped]

from .bars import DataError, FIELDS, MarketData


class BarProvider(Protocol):
    def fetch(self, symbols: Sequence[str], start: dt.date, end: dt.date) -> MarketData:
        """Return session bars within the inclusive date range."""
        ...


def validate_request(symbols: Sequence[str], start: dt.date, end: dt.date) -> None:
    if not symbols or len(set(symbols)) != len(symbols):
        raise DataError("symbols must be nonempty and unique")
    if any(
        not isinstance(s, str) or not s or "/" in s or "\\" in s or s in (".", "..")
        for s in symbols
    ):
        raise DataError("symbols must be safe nonempty file names")
    if start > end:
        raise DataError("start must not be after end")


def assemble(
    frames: dict[str, pd.DataFrame], *, adjusted: bool, source: str
) -> MarketData:
    """Align per-symbol bars on the sorted union of sessions."""
    fields = {
        name: pd.concat({s: f[name] for s, f in frames.items()}, axis=1).sort_index()
        for name in FIELDS
    }
    return MarketData(**fields, adjusted=adjusted, source=source)


def symbol_frame(data: MarketData, symbol: str) -> pd.DataFrame:
    return pd.DataFrame({name: getattr(data, name)[symbol] for name in FIELDS})


def write_csv(data: MarketData, directory: str | Path) -> None:
    """Write date,open,high,low,close,volume with float64 round-trip precision."""
    root = Path(directory)
    validate_request(data.symbols, dt.date.min, dt.date.max)
    root.mkdir(parents=True, exist_ok=True)
    for symbol in data.symbols:
        symbol_frame(data, symbol).to_csv(
            root / f"{symbol}.csv", index_label="date", float_format="%.17g"
        )


class CsvProvider:
    def __init__(self, directory: str | Path, *, adjusted: bool = True) -> None:
        self.directory = Path(directory)
        self.adjusted = adjusted

    def fetch(self, symbols: Sequence[str], start: dt.date, end: dt.date) -> MarketData:
        validate_request(symbols, start, end)
        frames = {}
        for symbol in symbols:
            path = self.directory / f"{symbol}.csv"
            try:
                frame = pd.read_csv(path, float_precision="round_trip")
                if list(frame.columns) != ["date", *FIELDS]:
                    raise DataError(f"{symbol}: expected date,{','.join(FIELDS)}")
                frame.index = pd.DatetimeIndex(pd.to_datetime(frame.pop("date")))
                # Validate before slicing, so invalid source rows cannot be hidden.
                bars = assemble({symbol: frame}, adjusted=self.adjusted, source="csv")
                # assemble sorts; enforce the original ordering as well.
                if not frame.index.is_monotonic_increasing:
                    raise DataError(f"{symbol}: sessions must be ascending")
                frames[symbol] = symbol_frame(
                    bars.window(pd.Timestamp(start), pd.Timestamp(end)), symbol
                )
            except (OSError, ValueError, KeyError) as exc:
                raise DataError(f"{symbol}: cannot read {path}: {exc}") from exc
        return assemble(frames, adjusted=self.adjusted, source="csv")


class YahooProvider:
    def __init__(self, *, retries: int = 2, backoff: float = 0.5) -> None:
        if retries < 0 or backoff < 0:
            raise DataError("retries and backoff must be nonnegative")
        self.retries = retries
        self.backoff = backoff

    def fetch(self, symbols: Sequence[str], start: dt.date, end: dt.date) -> MarketData:
        validate_request(symbols, start, end)
        missing = list(symbols)
        cause: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                raw = yf.download(
                    list(symbols),
                    start=start,
                    end=end + dt.timedelta(days=1),
                    auto_adjust=True,
                    actions=False,
                    group_by="ticker",
                    progress=False,
                    threads=False,
                )
                frames = {}
                missing = []
                for symbol in symbols:
                    if raw is None or raw.empty:
                        missing.append(symbol)
                        continue
                    if isinstance(raw.columns, pd.MultiIndex):
                        if symbol not in raw.columns.get_level_values(0):
                            missing.append(symbol)
                            continue
                        frame = raw[symbol].copy()
                    else:
                        frame = raw.copy()
                    frame.columns = [str(c).lower() for c in frame.columns]
                    if "close" not in frame or frame["close"].notna().sum() == 0:
                        missing.append(symbol)
                        continue
                    frame.index = pd.DatetimeIndex(frame.index).tz_localize(None)
                    frames[symbol] = frame[list(FIELDS)]
                if not missing:
                    return assemble(frames, adjusted=True, source="yahoo").window(
                        pd.Timestamp(start), pd.Timestamp(end)
                    )
            except Exception as exc:
                cause = exc
                missing = list(symbols)
            if attempt < self.retries:
                time.sleep(self.backoff * 2**attempt)
        raise DataError(f"yahoo: no data for {', '.join(missing)}") from cause
