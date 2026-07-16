"""Regression tests for sentiment_diagnostics.py.

Fixtures mirror the real shapes returned by api.nasdaq.com/api/analyst/{sym}/
targetprice and api.nasdaq.com/api/quote/{sym}/short-interest (captured by
hand against AAPL while building this module) -- no network access in tests.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sentiment_diagnostics as sd  # type: ignore[import-not-found]  # noqa: E402


def test_clean_number_handles_commas_dollar_signs_and_na() -> None:
    assert sd._clean_number("140,526,320") == 140526320.0
    assert sd._clean_number("$327.20") == 327.20
    assert sd._clean_number("N/A") is None
    assert sd._clean_number(None) is None
    assert sd._clean_number(42) == 42.0


def test_compute_analyst_signals_tilt_and_momentum() -> None:
    payload = {
        "data": {
            "consensusOverview": {
                "buy": 17,
                "hold": 11,
                "sell": 1,
                "priceTarget": 327.2,
            },
            "historicalConsensus": [
                # x is a unix timestamp (seconds). Point 1 is ~120 days before
                # latest, point 2 is exactly 14 days before the 75-day cutoff.
                {"x": 1735689600, "y": 200.0},
                {"x": 1738368000, "y": 210.0},
                {"x": 1746057600, "y": 327.2},  # latest
            ],
        }
    }
    result = sd.compute_analyst_signals(payload)
    values = result["values"]
    assert values["analyst_tilt"] == pytest.approx((17 - 1) / 29)
    # Momentum compares latest (327.2) to the *closest* qualifying reading at
    # or before the ~75-day cutoff -- both prior points qualify here, so the
    # more recent of the two (210.0), not the earliest (200.0), is used.
    assert values["target_price_momentum"] == pytest.approx(327.2 / 210.0 - 1)
    assert "analyst_tilt" in result["lineage"]


def test_compute_analyst_signals_missing_consensus_is_unavailable() -> None:
    result = sd.compute_analyst_signals({"data": {}})
    assert result["values"] == {}


def test_compute_analyst_signals_zero_total_analysts_is_unavailable() -> None:
    payload = {"data": {"consensusOverview": {"buy": 0, "hold": 0, "sell": 0}}}
    result = sd.compute_analyst_signals(payload)
    assert "analyst_tilt" not in result["values"]


def test_compute_analyst_signals_needs_a_point_at_least_75_days_back() -> None:
    payload = {
        "data": {
            "historicalConsensus": [
                {"x": 1746057600, "y": 300.0},
                {"x": 1746144000, "y": 305.0},  # only 1 day later -- too recent
            ]
        }
    }
    result = sd.compute_analyst_signals(payload)
    assert "target_price_momentum" not in result["values"]


def test_short_interest_percent_change_between_latest_two_settlements() -> None:
    payload = {
        "data": {
            "shortInterestTable": {
                "rows": [
                    {"settlementDate": "06/30/2026", "interest": "140,526,320"},
                    {"settlementDate": "06/15/2026", "interest": "144,248,476"},
                    {"settlementDate": "05/29/2026", "interest": "155,886,024"},
                ]
            }
        }
    }
    result = sd.compute_short_interest_signal(payload)
    assert result["values"]["short_interest_change"] == pytest.approx(
        140526320.0 / 144248476.0 - 1
    )
    assert result["lineage"]["short_interest_change"]["latest"]["date"] == "2026-06-30"


def test_compute_short_interest_signal_needs_at_least_two_rows() -> None:
    payload = {
        "data": {
            "shortInterestTable": {
                "rows": [{"settlementDate": "06/30/2026", "interest": "140,526,320"}]
            }
        }
    }
    result = sd.compute_short_interest_signal(payload)
    assert result["values"] == {}


def test_compute_short_interest_signal_handles_missing_table() -> None:
    result = sd.compute_short_interest_signal({"data": {}})
    assert result["values"] == {}
