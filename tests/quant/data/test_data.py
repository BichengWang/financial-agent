"""Behavioral coverage for bars, cache revision detection and quality gates."""

from dataclasses import replace
import datetime as dt
import json
from pathlib import Path
from typing import Any
from collections.abc import Sequence

import numpy as np
import pandas as pd
import pytest

from financial_agent.quant.data import (
    CachedProvider,
    CsvProvider,
    DataError,
    MarketData,
    YahooProvider,
    check_quality,
    synthetic_market,
    write_csv,
)
from financial_agent.quant.data.bars import FIELDS


def market(sessions: int = 20) -> MarketData:
    return synthetic_market(["A", "B"], sessions, seed=123)


def test_slicing_has_no_future_and_copies() -> None:
    data = market()
    bound = data.sessions[7] + pd.Timedelta(hours=12)
    cut = data.upto(bound)
    assert len(cut.sessions) == 8
    assert (cut.sessions <= bound).all()
    cut.close.iloc[0, 0] = 1
    assert data.close.iloc[0, 0] != 1
    assert data.upto(data.sessions[0] - pd.Timedelta(days=1)).close.empty
    assert data.window(data.sessions[3], data.sessions[5]).sessions.equals(
        data.sessions[3:6]
    )


@pytest.mark.parametrize("field", FIELDS)
def test_fingerprint_sensitive_to_every_field(field: str) -> None:
    data = market()
    same = replace(data, **{name: getattr(data, name).copy() for name in FIELDS})
    assert same.fingerprint() == data.fingerprint()
    changed = getattr(same, field)
    changed.iloc[2, 1] += 1
    assert same.fingerprint() != data.fingerprint()


def test_fingerprint_sessions_symbols_and_nan_payload() -> None:
    data = market()
    nan1 = data.close.copy()
    nan2 = data.close.copy()
    nan1.iloc[0, 0] = np.nan
    nan2.iloc[0, 0] = np.array([0x7FF8000000000001], dtype=np.uint64).view(np.float64)[
        0
    ]
    assert (
        replace(data, close=nan1).fingerprint()
        == replace(data, close=nan2).fingerprint()
    )
    renamed = replace(
        data,
        **{name: getattr(data, name).rename(columns={"A": "C"}) for name in FIELDS},
    )
    assert renamed.fingerprint() != data.fingerprint()
    shifted = replace(
        data,
        **{
            name: getattr(data, name).set_axis(data.sessions + pd.Timedelta(days=1))
            for name in FIELDS
        },
    )
    assert shifted.fingerprint() != data.fingerprint()


@pytest.mark.parametrize(
    "index, message",
    [
        (pd.Index([1, 2]), "DatetimeIndex"),
        (pd.date_range("2020-01-01", periods=2, tz="UTC"), "timezone"),
        (pd.DatetimeIndex(["2020-01-01 12:00", "2020-01-02"]), "normalized"),
        (pd.DatetimeIndex(["2020-01-01", "2020-01-01"]), "unique"),
        (pd.DatetimeIndex(["2020-01-02", "2020-01-01"]), "ascending"),
        (pd.DatetimeIndex(["2020-01-01", None]), "valid"),
    ],
)
def test_structure_rejects_invalid_sessions(index: pd.Index, message: str) -> None:
    data = market(2)
    with pytest.raises(DataError, match=message):
        replace(data, **{name: getattr(data, name).set_axis(index) for name in FIELDS})


def test_structure_rejects_alignment_and_nonnumeric() -> None:
    data = market()
    with pytest.raises(DataError, match="symbols differ"):
        replace(data, open=data.open[["B", "A"]])
    with pytest.raises(DataError, match="sessions differ"):
        replace(data, high=data.high.iloc[1:])
    with pytest.raises(DataError, match="numeric"):
        replace(data, volume=data.volume.astype(str))
    with pytest.raises(DataError, match="unique nonempty"):
        replace(
            data,
            **{
                name: getattr(data, name).set_axis(["A", "A"], axis=1)
                for name in FIELDS
            },
        )


def test_csv_roundtrip_and_bounds(tmp_path: Path) -> None:
    data = market()
    for name in FIELDS:
        getattr(data, name).iloc[0, 1] = np.nan
    write_csv(data, tmp_path)
    provider = CsvProvider(tmp_path)
    read = provider.fetch(
        data.symbols, data.sessions[0].date(), data.sessions[-1].date()
    )
    assert read.fingerprint() == data.fingerprint()
    bounded = provider.fetch(["B"], data.sessions[2].date(), data.sessions[4].date())
    assert bounded.symbols == ("B",)
    assert len(bounded.sessions) == 3
    with pytest.raises(DataError, match="MISSING"):
        provider.fetch(["MISSING"], dt.date(2005, 1, 1), dt.date(2005, 2, 1))


@pytest.mark.parametrize(
    "text, message",
    [
        ("date,close\n2020-01-01,1\n", "expected date"),
        ("date,open,high,low,close,volume\n2020-01-01,1,2,1,2,no\n", "numeric"),
        (
            "date,open,high,low,close,volume\n2020-01-02,1,2,1,2,1\n"
            "2020-01-01,1,2,1,2,1\n",
            "ascending",
        ),
    ],
)
def test_csv_rejects_bad_inputs(tmp_path: Path, text: str, message: str) -> None:
    (tmp_path / "A.csv").write_text(text)
    with pytest.raises(DataError, match=message):
        CsvProvider(tmp_path).fetch(["A"], dt.date(2020, 1, 1), dt.date(2020, 2, 1))


class CountingProvider:
    def __init__(self, data: MarketData) -> None:
        self.data = data
        self.calls: list[tuple[tuple[str, ...], dt.date, dt.date]] = []

    def fetch(self, symbols: Sequence[str], start: dt.date, end: dt.date) -> MarketData:
        self.calls.append((tuple(symbols), start, end))
        sliced = self.data.window(pd.Timestamp(start), pd.Timestamp(end))
        return replace(
            sliced, **{name: getattr(sliced, name)[list(symbols)] for name in FIELDS}
        )


def test_cache_tail_revision_and_metadata(tmp_path: Path) -> None:
    data = market(30)
    inner = CountingProvider(data)
    cache = CachedProvider(inner, tmp_path)
    start = data.sessions[0].date()
    cache.fetch(["A"], start, data.sessions[14].date())
    tail = cache.fetch(["A"], start, data.sessions[19].date())
    assert inner.calls[-1] == (
        ("A",),
        data.sessions[10].date(),
        data.sessions[19].date(),
    )
    assert len(inner.calls) == 2
    assert tail.close["A"].equals(data.close["A"].iloc[:20])
    meta = json.loads((tmp_path / "_meta.json").read_text())["A"]
    assert meta["source"] == "synthetic" and meta["adjusted"] is True
    assert dt.datetime.fromisoformat(meta["retrieved_at"]).utcoffset() == dt.timedelta(
        0
    )
    cache.fetch(["A"], start, data.sessions[19].date())
    assert len(inner.calls) == 2
    for name in ("open", "high", "low", "close"):
        getattr(data, name)["A"] *= 0.9
    revised = cache.fetch(["A"], start, data.sessions[24].date())
    assert inner.calls[-2][1] == data.sessions[15].date()
    assert inner.calls[-1] == (("A",), start, data.sessions[24].date())
    assert revised.close["A"].equals(data.close["A"].iloc[:25])
    assert not list(tmp_path.glob(".tmp-*"))


def test_cache_extends_start_and_individual_symbols(tmp_path: Path) -> None:
    data = market(30)
    inner = CountingProvider(data)
    cache = CachedProvider(inner, tmp_path)
    cache.fetch(["A", "B"], data.sessions[5].date(), data.sessions[19].date())
    cache.fetch(["B"], data.sessions[0].date(), data.sessions[19].date())
    assert inner.calls[-1] == (
        ("B",),
        data.sessions[0].date(),
        data.sessions[19].date(),
    )
    before = len(inner.calls)
    CachedProvider(inner, tmp_path).fetch(
        ["A"], data.sessions[6].date(), data.sessions[15].date()
    )
    assert len(inner.calls) == before


@pytest.mark.parametrize(
    "metadata", ["[]", "null", '"text"', "42", '{"A": []}', '{"A": null}']
)
def test_cache_rejects_nonobject_metadata(tmp_path: Path, metadata: str) -> None:
    (tmp_path / "_meta.json").write_text(metadata)
    data = market(2)
    inner = CountingProvider(data)
    with pytest.raises(DataError, match="invalid metadata"):
        CachedProvider(inner, tmp_path).fetch(
            ["A"], data.sessions[0].date(), data.sessions[-1].date()
        )
    assert not inner.calls
    assert (tmp_path / "_meta.json").read_text() == metadata


@pytest.mark.parametrize(
    "code,severity",
    [
        ("MISSING_SYMBOL", "error"),
        ("STALE", "error"),
        ("GAP", "error"),
        ("NONPOSITIVE", "error"),
        ("OHLC_INCONSISTENT", "error"),
        ("JUMP", "warning"),
        ("ZERO_VOLUME", "warning"),
    ],
)
def test_quality_codes_and_severity(code: str, severity: str) -> None:
    data = synthetic_market(["A"], 10, seed=1, annual_vol=0, annual_drift=0)
    kwargs: dict[str, Any] = {}
    if code == "MISSING_SYMBOL":
        data.close["A"] = np.nan
    elif code == "STALE":
        kwargs["expected_last_session"] = data.sessions[-1].date() + dt.timedelta(
            days=1
        )
    elif code == "GAP":
        data.close.iloc[4, 0] = np.nan
    elif code == "NONPOSITIVE":
        data.low.iloc[4, 0] = 0
    elif code == "OHLC_INCONSISTENT":
        data.high.iloc[4, 0] = 90
    elif code == "JUMP":
        data.close.iloc[4:, 0] *= 1.5
        data.high.iloc[4:, 0] *= 1.5
    else:
        data.volume.iloc[2:7, 0] = 0
    report = check_quality(data, **kwargs)
    found = [issue for issue in report.issues if issue.code == code]
    assert len(found) == 1
    assert found[0].symbol == "A" and found[0].severity == severity
    assert report.ok == (severity == "warning")


def test_leading_nans_and_envelope_tolerance() -> None:
    data = market()
    for name in FIELDS:
        getattr(data, name).iloc[:3, 1] = np.nan
    data.high.iloc[5, 0] = max(data.open.iloc[5, 0], data.close.iloc[5, 0]) * (
        1 - 5e-10
    )
    assert check_quality(data).ok
    data.high.iloc[5, 0] *= 1 - 2e-9
    assert not check_quality(data).ok


def test_synthetic_determinism_correlation_and_trend() -> None:
    first = synthetic_market(["A", "B"], 10000, seed=3, correlation=0.7)
    same = synthetic_market(["A", "B"], 10000, seed=3, correlation=0.7)
    other = synthetic_market(["A", "B"], 10000, seed=4, correlation=0.7)
    assert first.fingerprint() == same.fingerprint()
    assert first.fingerprint() != other.fingerprint()
    assert check_quality(first).ok
    returns = np.log(first.close).diff()
    assert returns.corr().iloc[0, 1] == pytest.approx(0.7, abs=0.03)
    trend = synthetic_market(["A"], 10000, seed=3, autocorrelation=0.7)
    assert np.log(trend.close["A"]).diff().autocorr() == pytest.approx(0.7, abs=0.03)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"sessions": 0},
        {"correlation": -1.1},
        {"autocorrelation": 1},
        {"annual_vol": -1},
        {"annual_drift": [1, 2, 3]},
    ],
)
def test_synthetic_rejects_invalid_parameters(kwargs: dict[str, Any]) -> None:
    options: dict[str, Any] = {"sessions": 10, "seed": 1}
    options.update(kwargs)
    with pytest.raises(DataError):
        synthetic_market(["A", "B"], **options)


def test_yahoo_batch_retry_and_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[dict[str, Any]] = []
    data = market(3)
    frames = {}
    for symbol in data.symbols:
        frames[symbol] = pd.DataFrame(
            {name.title(): getattr(data, name)[symbol] for name in FIELDS}
        )
    raw = pd.concat(frames, axis=1)

    def download(*args: Any, **kwargs: Any) -> pd.DataFrame:
        calls.append(kwargs)
        return pd.DataFrame() if len(calls) == 1 else raw

    monkeypatch.setattr("financial_agent.quant.data.providers.yf.download", download)
    result = YahooProvider(backoff=0).fetch(
        ["A", "B"], data.sessions[0].date(), data.sessions[-1].date()
    )
    assert result.fingerprint() == data.fingerprint()
    assert len(calls) == 2
    assert calls[0]["auto_adjust"] is True and calls[0]["actions"] is False
    assert calls[0]["end"] == data.sessions[-1].date() + dt.timedelta(days=1)
    raw[("B", "Close")] = np.nan
    with pytest.raises(DataError, match="no data for B"):
        YahooProvider(retries=0).fetch(
            ["A", "B"], data.sessions[0].date(), data.sessions[-1].date()
        )


def test_cache_weekend_coverage_and_csv_path_safety(tmp_path: Path) -> None:
    data = synthetic_market(["A"], 5, seed=1, start="2020-01-06")
    inner = CountingProvider(data)
    cache = CachedProvider(inner, tmp_path / "cache")
    first = cache.fetch(["A"], dt.date(2020, 1, 6), dt.date(2020, 1, 12))
    repeated = cache.fetch(["A"], dt.date(2020, 1, 6), dt.date(2020, 1, 12))
    # Weekend requests remain beyond the last received session and retry.
    assert len(inner.calls) == 2
    assert first.fingerprint() == repeated.fingerprint()
    with pytest.raises(DataError, match="safe"):
        CsvProvider(tmp_path).fetch(["../A"], dt.date(2020, 1, 1), dt.date(2020, 1, 2))
    with pytest.raises(DataError, match="start"):
        cache.fetch(["A"], dt.date(2020, 1, 2), dt.date(2020, 1, 1))


def test_yahoo_flat_single_symbol_and_exhausted_exception(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    data = synthetic_market(["A"], 3, seed=1)
    raw = pd.DataFrame({name.title(): getattr(data, name)["A"] for name in FIELDS})
    raw.index = raw.index.tz_localize("UTC")
    monkeypatch.setattr(
        "financial_agent.quant.data.providers.yf.download", lambda *a, **kw: raw
    )
    actual = YahooProvider(retries=0).fetch(
        ["A"], data.sessions[0].date(), data.sessions[-1].date()
    )
    assert actual.fingerprint() == data.fingerprint()
    attempts = 0

    def unavailable(*args: Any, **kwargs: Any) -> None:
        nonlocal attempts
        attempts += 1
        raise OSError("unavailable")

    monkeypatch.setattr("financial_agent.quant.data.providers.yf.download", unavailable)
    with pytest.raises(DataError, match="no data for A"):
        YahooProvider(retries=2, backoff=0).fetch(
            ["A"], data.sessions[0].date(), data.sessions[-1].date()
        )
    assert attempts == 3


def test_cache_retries_same_end_when_last_session_published_later(
    tmp_path: Path,
) -> None:
    complete = market(20)
    inner = CountingProvider(complete.upto(complete.sessions[-2]))
    start, end = complete.sessions[0].date(), complete.sessions[-1].date()
    first = CachedProvider(inner, tmp_path).fetch(["A"], start, end)
    assert first.sessions[-1] == complete.sessions[-2]
    metadata = json.loads((tmp_path / "_meta.json").read_text())["A"]
    assert metadata["covered_end"] == complete.sessions[-2].date().isoformat()

    inner.data = complete
    second = CachedProvider(inner, tmp_path).fetch(["A"], start, end)
    assert len(inner.calls) == 2
    assert inner.calls[-1] == (("A",), complete.sessions[-6].date(), end)
    assert second.sessions[-1] == complete.sessions[-1]
    assert second.close["A"].equals(complete.close["A"])
    assert check_quality(second, expected_last_session=end).ok
    CachedProvider(inner, tmp_path).fetch(["A"], start, end)
    assert len(inner.calls) == 2


def test_cache_empty_refresh_preserves_previous_coverage(tmp_path: Path) -> None:
    data = market(20)
    inner = CountingProvider(data.upto(data.sessions[9]))
    start = data.sessions[0].date()
    cache = CachedProvider(inner, tmp_path)
    original = cache.fetch(["A"], start, data.sessions[9].date())
    inner.data = data.upto(data.sessions[0] - pd.Timedelta(days=1))
    refreshed = cache.fetch(["A"], start, data.sessions[-1].date())
    assert refreshed.fingerprint() == original.fingerprint()
    metadata = json.loads((tmp_path / "_meta.json").read_text())["A"]
    assert metadata["covered_end"] == data.sessions[9].date().isoformat()
    cache.fetch(["A"], start, data.sessions[-1].date())
    assert len(inner.calls) == 3


def test_cache_initial_empty_response_allows_same_day_retry(tmp_path: Path) -> None:
    data = market(1)
    start = data.sessions[0].date()
    inner = CountingProvider(data.upto(data.sessions[0] - pd.Timedelta(days=1)))
    cache = CachedProvider(inner, tmp_path)
    assert cache.fetch(["A"], start, start).close.empty
    assert json.loads((tmp_path / "_meta.json").read_text())["A"]["covered_end"] is None
    inner.data = data
    recovered = cache.fetch(["A"], start, start)
    assert recovered.sessions.equals(data.sessions)
    assert len(inner.calls) == 2
