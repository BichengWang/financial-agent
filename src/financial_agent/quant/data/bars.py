"""Session-aligned OHLCV bars and stable content identities."""

from dataclasses import dataclass
import hashlib
import json

import numpy as np
import pandas as pd  # type: ignore[import-untyped]

FIELDS = ("open", "high", "low", "close", "volume")


class DataError(ValueError):
    """Invalid market data or an unavailable provider response."""


@dataclass(frozen=True)
class MarketData:
    """Wide numeric bars on shared, normalized, timezone-naive sessions."""

    open: pd.DataFrame
    high: pd.DataFrame
    low: pd.DataFrame
    close: pd.DataFrame
    volume: pd.DataFrame
    adjusted: bool
    source: str

    def __post_init__(self) -> None:
        if not isinstance(self.close, pd.DataFrame):
            raise DataError("close: expected a DataFrame")
        for name in FIELDS:
            frame = getattr(self, name)
            if not isinstance(frame, pd.DataFrame):
                raise DataError(f"{name}: expected a DataFrame")
            index = frame.index
            if not isinstance(index, pd.DatetimeIndex):
                raise DataError(f"{name}: expected a DatetimeIndex")
            if index.tz is not None:
                raise DataError(f"{name}: sessions must be timezone-naive")
            if index.hasnans or not index.equals(index.normalize()):
                raise DataError(f"{name}: sessions must be valid normalized dates")
            if not index.is_unique or not index.is_monotonic_increasing:
                raise DataError(f"{name}: sessions must be ascending and unique")
            if not frame.columns.is_unique or not all(
                isinstance(s, str) and s for s in frame.columns
            ):
                raise DataError(f"{name}: symbols must be unique nonempty strings")
            if not index.equals(self.close.index):
                raise DataError(f"{name}: sessions differ from close")
            if not frame.columns.equals(self.close.columns):
                raise DataError(f"{name}: symbols differ from close")
            if any(
                not pd.api.types.is_numeric_dtype(dtype)
                or pd.api.types.is_complex_dtype(dtype)
                for dtype in frame.dtypes
            ):
                raise DataError(f"{name}: values must be real numeric")
        if not isinstance(self.adjusted, bool) or not isinstance(self.source, str):
            raise DataError("adjusted must be bool and source must be str")

    @property
    def symbols(self) -> tuple[str, ...]:
        return tuple(self.close.columns)

    @property
    def sessions(self) -> pd.DatetimeIndex:
        return self.close.index.copy()

    def upto(self, asof: pd.Timestamp) -> "MarketData":
        """Copy bars through asof, inclusive, without exposing future rows."""
        return self.window(None, asof)

    def window(
        self, start: pd.Timestamp | None, end: pd.Timestamp | None
    ) -> "MarketData":
        """Copy the inclusive session range; bounds may be omitted."""
        mask = np.ones(len(self.sessions), dtype=bool)
        if start is not None:
            mask &= self.sessions >= pd.Timestamp(start)
        if end is not None:
            mask &= self.sessions <= pd.Timestamp(end)
        return MarketData(
            **{name: getattr(self, name).loc[mask].copy() for name in FIELDS},
            adjusted=self.adjusted,
            source=self.source,
        )

    def fingerprint(self) -> str:
        """SHA256 of symbols, ISO sessions and canonical little-endian float64."""
        digest = hashlib.sha256()
        digest.update(
            json.dumps(
                [self.symbols, [s.isoformat() for s in self.sessions]],
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode("utf-8")
        )
        for name in FIELDS:
            values = getattr(self, name).to_numpy(dtype="<f8", copy=True)
            values[np.isnan(values)] = np.nan
            digest.update(values.tobytes(order="C"))
        return digest.hexdigest()
