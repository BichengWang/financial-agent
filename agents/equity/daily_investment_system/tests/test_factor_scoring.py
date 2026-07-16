"""Regression tests for factor_scoring.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import factor_scoring as fs  # type: ignore[import-not-found]  # noqa: E402


def test_winsorize_clamps_outliers_to_percentile_bounds() -> None:
    # 100 values so the 95th-percentile index (95) doesn't trivially land on
    # the last element -- with too few points the "95th percentile" is just
    # the max and nothing gets clamped.
    values = [float(i) for i in range(1, 100)] + [100000.0]
    out = fs.winsorize(values)
    assert max(out) < 100000.0
    assert len(out) == len(values)


def test_winsorize_is_a_noop_below_two_values() -> None:
    assert fs.winsorize([]) == []
    assert fs.winsorize([5.0]) == [5.0]


def test_zscore_cross_sectionally_higher_is_better_default() -> None:
    per_ticker: dict[str, dict[str, float | None]] = {
        "A": {"metric": 10.0},
        "B": {"metric": 20.0},
        "C": {"metric": 30.0},
    }
    z = fs.zscore_cross_sectionally(per_ticker, ("metric",), lower_is_better=set())
    a, b, c = z["A"]["metric"], z["B"]["metric"], z["C"]["metric"]
    assert a is not None and b is not None and c is not None
    assert a < b < c


def test_zscore_cross_sectionally_inverts_polarity_for_lower_is_better() -> None:
    per_ticker: dict[str, dict[str, float | None]] = {
        "A": {"leverage": 1.0},
        "B": {"leverage": 2.0},
        "C": {"leverage": 3.0},
    }
    z = fs.zscore_cross_sectionally(
        per_ticker, ("leverage",), lower_is_better={"leverage"}
    )
    a, b, c = z["A"]["leverage"], z["B"]["leverage"], z["C"]["leverage"]
    assert a is not None and b is not None and c is not None
    # Lowest raw leverage should score *highest* once polarity is inverted.
    assert a > b > c


def test_zscore_cross_sectionally_none_when_fewer_than_two_carry_the_signal() -> None:
    per_ticker: dict[str, dict[str, float | None]] = {
        "A": {"metric": 10.0},
        "B": {"metric": None},
    }
    z = fs.zscore_cross_sectionally(per_ticker, ("metric",), lower_is_better=set())
    assert z["A"]["metric"] is None
    assert z["B"]["metric"] is None


def test_zscore_cross_sectionally_missing_ticker_stays_none() -> None:
    per_ticker: dict[str, dict[str, float | None]] = {
        "A": {"metric": 10.0},
        "B": {"metric": 20.0},
        "C": {"metric": None},
    }
    z = fs.zscore_cross_sectionally(per_ticker, ("metric",), lower_is_better=set())
    assert z["C"]["metric"] is None
    assert z["A"]["metric"] is not None
    assert z["B"]["metric"] is not None


def test_composite_z_equal_weights_available_signals() -> None:
    composite, n = fs.composite_z({"a": 1.0, "b": 3.0})
    assert composite == pytest.approx(2.0)
    assert n == 2


def test_composite_z_none_below_min_signals() -> None:
    composite, n = fs.composite_z({"a": 1.0, "b": None})
    assert composite is None
    assert n == 1


def test_composite_z_ignores_none_entries_in_the_average() -> None:
    composite, n = fs.composite_z({"a": 2.0, "b": 4.0, "c": None})
    assert composite == pytest.approx(3.0)
    assert n == 2
