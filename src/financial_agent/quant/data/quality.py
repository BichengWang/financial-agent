"""Content checks separate from the structural MarketData contract."""

from dataclasses import dataclass
import datetime as dt
from typing import Literal

import numpy as np
import pandas as pd  # type: ignore[import-untyped]

from .bars import DataError, MarketData


@dataclass(frozen=True)
class QualityIssue:
    code: str
    symbol: str
    session: pd.Timestamp | None
    detail: str
    severity: Literal["error", "warning"]


@dataclass(frozen=True)
class QualityReport:
    issues: list[QualityIssue]

    @property
    def ok(self) -> bool:
        """True exactly when no error-severity issues exist."""
        return not any(issue.severity == "error" for issue in self.issues)


def check_quality(
    data: MarketData,
    *,
    expected_last_session: dt.date | None = None,
    max_abs_return: float = 0.25,
    zero_volume_run: int = 5,
) -> QualityReport:
    """Check prices and close coverage; return thresholds are decimal fractions."""
    if max_abs_return < 0 or zero_volume_run < 1:
        raise DataError("return threshold must be nonnegative; volume run positive")
    issues: list[QualityIssue] = []

    def add(
        code: str,
        symbol: str,
        session: pd.Timestamp | None,
        detail: str,
        severity: Literal["error", "warning"] = "error",
    ) -> None:
        issues.append(QualityIssue(code, symbol, session, detail, severity))

    for symbol in data.symbols:
        close = data.close[symbol]
        valid = close.dropna()
        if valid.empty:
            add("MISSING_SYMBOL", symbol, None, "no valid closes")
        else:
            if (
                expected_last_session is not None
                and valid.index[-1].date() < expected_last_session
            ):
                add(
                    "STALE",
                    symbol,
                    valid.index[-1],
                    "last close precedes expected session",
                )
            for session in close.loc[valid.index[0] :].index[
                close.loc[valid.index[0] :].isna()
            ]:
                add("GAP", symbol, session, "missing close after first valid close")
        for name in ("open", "high", "low", "close"):
            series = getattr(data, name)[symbol]
            for session in series.index[series <= 0]:
                add("NONPOSITIVE", symbol, session, f"{name} must be positive")
            for session in series.index[series.notna() & ~np.isfinite(series)]:
                add("NONFINITE", symbol, session, f"{name} must be finite")
        upper = pd.concat([data.open[symbol], close], axis=1).max(axis=1)
        lower = pd.concat([data.open[symbol], close], axis=1).min(axis=1)
        inconsistent = (
            (data.high[symbol] < upper - upper.abs() * 1e-9)
            | (data.low[symbol] > lower + lower.abs() * 1e-9)
            | (data.high[symbol] < data.low[symbol])
        )
        for session in data.sessions[inconsistent]:
            add("OHLC_INCONSISTENT", symbol, session, "high/low fail OHLC envelope")
        returns = close.pct_change(fill_method=None)
        for session in returns.index[returns.abs() > max_abs_return]:
            add(
                "JUMP", symbol, session, f"return {returns.loc[session]:.6g}", "warning"
            )
        run = 0
        run_start = None
        for session, volume in data.volume[symbol].items():
            if volume == 0:
                if run == 0:
                    run_start = session
                run += 1
                if run == zero_volume_run:
                    add("ZERO_VOLUME", symbol, run_start, "zero volume run", "warning")
            else:
                run = 0
    return QualityReport(issues)
