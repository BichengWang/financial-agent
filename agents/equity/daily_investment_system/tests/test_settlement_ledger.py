"""Regression tests for settlement_ledger.py.

Run with: uv run pytest agents/equity/daily_investment_system/tests/
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import settlement_ledger as sl  # type: ignore[import-not-found]  # noqa: E402

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "output"
real_data = pytest.mark.skipif(
    not OUTPUT_DIR.exists(), reason="agents/equity/output data not present"
)


def _packages_as_of(cutoff: str) -> list[dict[str, Any]]:
    """Real packages with run_date <= cutoff. This repo's daily pipeline adds
    a new dated output folder on every run, so pinning to a fixed historical
    cutoff (rather than loading the whole, ever-growing directory) is what
    keeps these tests stable as later runs land -- a package dated after
    `cutoff` must never change what a test pinned to `cutoff` asserts."""
    return [p for p in sl.load_packages(OUTPUT_DIR) if p.get("run_date", "") <= cutoff]


# ---------------------------------------------------------------------------
# Trading calendar
# ---------------------------------------------------------------------------


def test_known_2026_holidays_are_not_trading_days() -> None:
    holidays = [
        "2026-01-01",  # New Year's Day
        "2026-01-19",  # MLK Day
        "2026-02-16",  # Washington's Birthday
        "2026-04-03",  # Good Friday
        "2026-05-25",  # Memorial Day
        "2026-06-19",  # Juneteenth
        "2026-07-03",  # Independence Day (observed; July 4 is a Saturday)
        "2026-09-07",  # Labor Day
        "2026-11-26",  # Thanksgiving
        "2026-12-25",  # Christmas
    ]
    for h in holidays:
        assert not sl.is_trading_day(dt.date.fromisoformat(h)), h


def test_weekends_are_not_trading_days() -> None:
    assert not sl.is_trading_day(dt.date(2026, 7, 11))  # Saturday
    assert not sl.is_trading_day(dt.date(2026, 7, 12))  # Sunday


def test_prior_trading_day_skips_weekend() -> None:
    assert sl.prior_trading_day(dt.date(2026, 7, 14)) == dt.date(2026, 7, 13)
    assert sl.prior_trading_day(dt.date(2026, 7, 13)) == dt.date(2026, 7, 10)


def test_most_recent_trading_day_at_or_before_weekend() -> None:
    assert sl.most_recent_trading_day_at_or_before(dt.date(2026, 7, 12)) == dt.date(
        2026, 7, 10
    )


def test_saturday_new_years_day_is_not_observed_on_the_prior_friday() -> None:
    # NYSE Rule 7.2: Jan 1 on a Saturday has no observed closure, so
    # 2021-12-31 and 2027-12-31 are ordinary sessions.
    assert sl.is_trading_day(dt.date(2021, 12, 31))
    assert sl.is_trading_day(dt.date(2027, 12, 31))
    assert sl.is_trading_day(dt.date(2022, 1, 3))
    assert sl.is_trading_day(dt.date(2028, 1, 3))
    assert sl.is_trading_day(dt.date(2025, 12, 31))


def test_sunday_new_years_day_is_observed_on_monday() -> None:
    assert not sl.is_trading_day(dt.date(2023, 1, 2))


def test_saturday_christmas_is_still_observed_on_friday() -> None:
    assert not sl.is_trading_day(dt.date(2021, 12, 24))


# ---------------------------------------------------------------------------
# Timing validator
# ---------------------------------------------------------------------------


def test_ordinary_settlement_at_target_close_is_valid() -> None:
    convention, valid, reason = sl.validate_timing(
        "2026-07-08", "2026-07-10", "2026-07-08"
    )
    assert (convention, valid, reason) == ("ORDINARY", True, "")


def test_ordinary_settlement_using_a_later_current_price_is_invalid() -> None:
    # The real MCK bug: a 2026-07-09 run settled a 2026-07-08 target using
    # 2026-07-09's "current price" instead of the target date's own close.
    convention, valid, reason = sl.validate_timing(
        "2026-07-08", "2026-07-09", "2026-07-09"
    )
    assert convention == "ORDINARY"
    assert not valid
    assert "2026-07-08" in reason


def test_target_eq_run_date_prior_close_is_valid() -> None:
    # claude-fable-5's real 2026-07-14 package: target == run date, correctly
    # settles at the prior completed close (2026-07-13).
    convention, valid, _ = sl.validate_timing("2026-07-14", "2026-07-14", "2026-07-13")
    assert (convention, valid) == ("TARGET_EQ_RUN_DATE", True)


def test_target_eq_run_date_same_day_close_is_invalid() -> None:
    # gpt-5's real 2026-07-14 conflict: same target/run date, settled using
    # the target date's own not-yet-real close.
    convention, valid, reason = sl.validate_timing(
        "2026-07-14", "2026-07-14", "2026-07-14"
    )
    assert convention == "TARGET_EQ_RUN_DATE"
    assert not valid
    assert "TARGET_DATE_CLOSE" in reason


def test_target_date_close_after_session_is_valid_when_explicit() -> None:
    convention, valid, reason = sl.validate_timing(
        "2026-07-22",
        "2026-07-22",
        "2026-07-22",
        "TARGET_DATE_CLOSE",
        "2026-07-22T20:52:13Z",
    )
    assert (convention, valid, reason) == ("TARGET_DATE_CLOSE", True, "")


def test_target_date_close_before_session_end_is_invalid_even_when_explicit() -> None:
    convention, valid, reason = sl.validate_timing(
        "2026-07-22",
        "2026-07-22",
        "2026-07-22",
        "TARGET_DATE_CLOSE",
        "2026-07-22T19:59:59Z",
    )
    assert convention == "TARGET_DATE_CLOSE"
    assert not valid
    assert "16:00 America/New_York" in reason


def test_target_date_close_valid_when_settled_after_midnight() -> None:
    # claude-opus-5's real 2026-08-07 run: fired 22:02 ET, settlement pass ran past
    # midnight, so a truthful settled_at lands on 2026-08-08. A timestamp *later* than
    # the target-date close is strictly stronger evidence that the completed close was
    # used, so it must validate. (Track B accepted 2026-08-07.)
    convention, valid, reason = sl.validate_timing(
        "2026-08-07",
        "2026-08-07",
        "2026-08-07",
        "TARGET_DATE_CLOSE",
        "2026-08-08T01:30:38-04:00",
    )
    assert (convention, valid, reason) == ("TARGET_DATE_CLOSE", True, "")


def test_target_date_close_requires_timezone_aware_settled_at() -> None:
    for settled_at in (None, "2026-07-22T16:30:00"):
        convention, valid, reason = sl.validate_timing(
            "2026-07-22",
            "2026-07-22",
            "2026-07-22",
            "TARGET_DATE_CLOSE",
            settled_at,
        )
        assert convention == "TARGET_DATE_CLOSE"
        assert not valid
        assert "timezone-aware settled_at" in reason


@pytest.mark.parametrize(
    ("target_date", "run_date"),
    # 0001-01-01 is a holiday; 0001-01-02 trades, but nothing trades before it.
    [("0001-01-01", "2026-07-10"), ("0001-01-02", "0001-01-02")],
)
def test_a_target_date_with_no_prior_close_is_malformed(
    target_date: str, run_date: str
) -> None:
    assert sl.validate_timing(target_date, run_date, "0001-01-01") == (
        "MALFORMED",
        False,
        f"target_date {target_date} has no prior close",
    )


@pytest.mark.parametrize(
    "settled_at", ["0001-01-01T00:00:00+05:00", "9999-12-31T23:59:59-05:00"]
)
def test_target_date_close_rejects_a_settled_at_new_york_cannot_hold(
    settled_at: str,
) -> None:
    convention, valid, reason = sl.validate_timing(
        "2026-07-22", "2026-07-22", "2026-07-22", "TARGET_DATE_CLOSE", settled_at
    )
    assert (convention, valid) == ("TARGET_DATE_CLOSE", False)
    assert "timezone-aware settled_at" in reason


def test_build_manifest_uses_explicit_target_date_close_flag() -> None:
    packages = [
        {
            "run_date": "2026-06-24",
            "model": "gpt-5",
            "_source_file": "gpt-5-2026-06-24",
            "predictions": [
                {
                    "run_date": "2026-06-24",
                    "model": "gpt-5",
                    "ticker": "AAPL",
                    "type": "EQUITY_ALPHA",
                    "target_date": "2026-07-22",
                    "entry_price": 100.0,
                    "mu": 0.02,
                    "sigma": 0.1,
                    "adj_score": 1.0,
                }
            ],
            "settlements": [],
        },
        {
            "run_date": "2026-07-22",
            "model": "gpt-5",
            "_source_file": "gpt-5-2026-07-22",
            "predictions": [],
            "settlements": [
                {
                    "vintage": "2026-06-24",
                    "model": "gpt-5",
                    "ticker": "AAPL",
                    "type": "EQUITY_ALPHA",
                    "target_date": "2026-07-22",
                    "settle_price": 103.0,
                    "settle_price_date": "2026-07-22",
                    "timing_flag": "TARGET_DATE_CLOSE",
                    "settled_at": "2026-07-22T20:52:13Z",
                    "entry_price": 100.0,
                    "mu": 0.02,
                    "sigma": 0.1,
                    "realized_return": 0.03,
                    "benchmark_return": 0.01,
                    "realized_alpha": 0.02,
                    "direction": "HIT",
                    "ci_result": "IN_CI",
                    "z": 0.1,
                }
            ],
        },
    ]

    manifest = sl.build_manifest(packages, as_of="2026-07-22")

    assert manifest["summary"]["canonical_equity_alpha_settlements"] == 1
    assert manifest["summary"]["due_inventory"] == 0
    assert manifest["canonical_settlements"][0]["settlement_convention"] == (
        "TARGET_DATE_CLOSE"
    )


def test_weekend_target_at_prior_friday_close_is_valid() -> None:
    # 2026-07-12 is a Sunday; the prior Friday close (07-10) is correct.
    convention, valid, _ = sl.validate_timing("2026-07-12", "2026-07-12", "2026-07-10")
    assert (convention, valid) == ("WEEKEND_TARGET", True)


def test_weekend_target_using_wrong_date_is_invalid() -> None:
    convention, valid, _ = sl.validate_timing("2026-07-12", "2026-07-12", "2026-07-09")
    assert (convention, valid) == ("WEEKEND_TARGET", False)


def test_premature_settlement_before_target_date_is_invalid() -> None:
    convention, valid, _ = sl.validate_timing("2026-07-20", "2026-07-14", "2026-07-14")
    assert (convention, valid) == ("PREMATURE", False)


def test_missing_price_date_is_invalid() -> None:
    convention, valid, _ = sl.validate_timing("2026-07-08", "2026-07-10", None)
    assert (convention, valid) == ("UNKNOWN", False)


def test_malformed_date_is_invalid() -> None:
    convention, valid, _ = sl.validate_timing("not-a-date", "2026-07-10", "2026-07-08")
    assert (convention, valid) == ("MALFORMED", False)


def test_a_numeric_price_date_is_malformed() -> None:
    assert sl.validate_timing("2026-08-28", "2026-09-02", 20260828) == (
        "MALFORMED",
        False,
        "price_date 20260828 is not a valid date",
    )


# ---------------------------------------------------------------------------
# Normalization -- real schema variants captured from the repo
# ---------------------------------------------------------------------------


def test_normalize_handles_settle_price_schema_variant() -> None:
    raw = {
        "ticker": "GS",
        "type": "EQUITY_ALPHA",
        "vintage": "2026-06-17",
        "model": "gpt-5",
        "target_date": "2026-07-15",
        "settle_date": "2026-07-14",
        "settle_price": 1140.0,
        "direction": "HIT",
        "ci_result": "IN_CI",
        "timing_flag": "TARGET_EQ_RUN_DATE",
    }
    cand = sl.normalize_settlement_candidate(
        raw, "2026-07-15", "claude-fable-5", "f", {}
    )
    assert cand is not None
    assert cand.price == 1140.0
    assert cand.price_date == "2026-07-14"
    assert cand.vintage == "2026-06-17"
    assert cand.declared_timing_flag == "TARGET_EQ_RUN_DATE"


def test_normalize_handles_current_price_variant() -> None:
    raw = {
        "run_date": "2026-06-10",  # NB: this is the *vintage*, not the settlement date
        "model": "claude-fable-5",
        "ticker": "MCK",
        "type": "EQUITY_ALPHA",
        "vintage": "2026-06-10",
        "current_price": 815.34,
        "current_price_date": "2026-07-08",
        "target_date": "2026-07-08",
        "direction": "HIT",
        "ci_result": "IN_CI",
    }
    cand = sl.normalize_settlement_candidate(
        raw, "2026-07-08", "claude-fable-5", "f", {}
    )
    assert cand is not None
    assert cand.price == 815.34
    assert cand.price_date == "2026-07-08"
    # settlement_run_date must come from the *container* package, never from
    # the settlement row's own "run_date" key (which holds the vintage here).
    assert cand.settlement_run_date == "2026-07-08"
    assert cand.vintage == "2026-06-10"


def test_normalize_strips_model_prefixed_vintage_bug() -> None:
    raw = {
        "ticker": "MCK",
        "type": "EQUITY_ALPHA",
        "vintage": "gpt-5-2026-06-11",
        "model": "gpt-5",
        "target_date": "2026-07-09",
        "current_price_date": "2026-07-09",
        "current_price": 789.78,
        "direction": "MISS",
        "ci_result": "IN_CI",
    }
    cand = sl.normalize_settlement_candidate(raw, "2026-07-09", "gpt-5", "f", {})
    assert cand is not None
    assert cand.vintage == "2026-06-11"


def test_normalize_infers_vintage_from_predictions_index_when_absent() -> None:
    pred = sl.Prediction(
        model="gpt-5",
        vintage="2026-06-11",
        ticker="MCK",
        type="EQUITY_ALPHA",
        target_date="2026-07-09",
        adj_score=0.5,
        mu=0.02,
        sigma=0.05,
        entry_price=791.8,
        source_file="gpt-5-2026-06-11",
    )
    lookup = {("gpt-5", "MCK", "EQUITY_ALPHA", "2026-07-09"): [pred]}
    raw = {
        "ticker": "MCK",
        "type": "EQUITY_ALPHA",
        "model": "gpt-5",
        "target_date": "2026-07-09",
        "current_price_date": "2026-07-09",
        "current_price": 789.78,
        "direction": "MISS",
        "ci_result": "IN_CI",
    }
    cand = sl.normalize_settlement_candidate(raw, "2026-07-09", "gpt-5", "f", lookup)
    assert cand is not None
    assert cand.vintage == "2026-06-11"


def test_normalize_accepts_ci_and_spy_return_aliases() -> None:
    raw = {
        "ticker": "SPY",
        "type": "MARKET_FORECAST",
        "vintage": "2026-06-15",
        "model": "claude-fable-5",
        "target_date": "2026-07-13",
        "settle_price": 751.0,
        "settle_date": "2026-07-10",
        "direction": "HIT",
        "ci": "IN_CI",
        "spy_return": 0.01,
    }
    cand = sl.normalize_settlement_candidate(
        raw, "2026-07-13", "claude-fable-5", "f", {}
    )
    assert cand is not None
    assert cand.ci_result == "IN_CI"
    assert cand.benchmark_return == 0.01


def test_normalize_returns_none_for_unkeyable_row() -> None:
    assert sl.normalize_settlement_candidate({}, "2026-07-10", "m", "f", {}) is None
    # Ticker present but no vintage derivable by any fallback and no unique
    # prediction match:
    unresolvable = {"ticker": "ZZZ", "target_date": "2026-07-10", "model": "m"}
    assert (
        sl.normalize_settlement_candidate(unresolvable, "2026-07-10", "m", "f", {})
        is None
    )


@pytest.mark.parametrize(
    ("changes", "container_model", "key"),
    [
        # Missing, the model comes from the package and the type is EQUITY_ALPHA;
        (
            {},
            "claude-fable-5",
            ("claude-fable-5", "2026-06-17", "GS", "EQUITY_ALPHA", "2026-07-15"),
        ),
        # present but not a string, a key field leaves the row unkeyable.
        ({"ticker": 5}, "claude-fable-5", None),
        ({"ticker": ["GS"]}, "claude-fable-5", None),
        ({"model": 5}, "claude-fable-5", None),
        ({"model": {"name": "claude-fable-5"}}, "claude-fable-5", None),
        ({}, 5, None),
        ({"type": 5}, "claude-fable-5", None),
        ({"target_date": 20260715}, "claude-fable-5", None),
        ({"target_date": ["2026-07-15"]}, "claude-fable-5", None),
    ],
    ids=[
        "missing",
        "ticker-5",
        "ticker-list",
        "model-5",
        "model-object",
        "package-model-5",
        "type-5",
        "target_date-20260715",
        "target_date-list",
    ],
)
def test_normalize_returns_none_when_a_key_field_is_not_a_string(
    changes: dict[str, Any], container_model: Any, key: tuple[str, ...] | None
) -> None:
    raw = {"ticker": "GS", "vintage": "2026-06-17", "target_date": "2026-07-15"}
    cand = sl.normalize_settlement_candidate(
        {**raw, **changes}, "2026-07-15", container_model, "f", {}
    )
    assert (cand.key() if cand else None) == key


@pytest.mark.parametrize(
    ("changes", "package_changes", "keys"),
    [
        # Missing, the model and run_date come from the package and the type is
        # EQUITY_ALPHA; present but not a string, a key field skips the prediction.
        ({}, {}, [("model-p", "2026-07-14", "AAA", "EQUITY_ALPHA", "2026-08-10")]),
        ({"model": 5}, {}, []),
        ({"model": {"name": "model-p"}}, {}, []),
        ({}, {"model": 5}, []),
        ({"run_date": 20260713}, {}, []),
        ({}, {"run_date": 20260714}, []),
        ({"ticker": 5}, {}, []),
        ({"ticker": ["AAA"]}, {}, []),
        ({"type": 5}, {}, []),
        ({"target_date": 20260810}, {}, []),
    ],
    ids=[
        "missing",
        "model-5",
        "model-object",
        "package-model-5",
        "run_date-20260713",
        "package-run_date-20260714",
        "ticker-5",
        "ticker-list",
        "type-5",
        "target_date-20260810",
    ],
)
def test_extract_predictions_skips_a_key_field_that_is_not_a_string(
    changes: dict[str, Any],
    package_changes: dict[str, Any],
    keys: list[tuple[str, ...]],
) -> None:
    prediction = {"ticker": "AAA", "target_date": "2026-08-10", **changes}
    package = dict(run_date="2026-07-14", model="model-p", predictions=[prediction])
    package.update(package_changes)
    assert [p.key() for p in sl.extract_predictions([package])] == keys


@pytest.mark.parametrize(
    ("package_model", "prediction_model"),
    [(["model-p"], None), ("model-p", []), ("model-p", {"name": "model-p"})],
    ids=[
        "package-model-list",
        "prediction-model-empty-list",
        "prediction-model-object",
    ],
)
def test_a_list_or_object_model_does_not_break_duplicate_book_detection(
    package_model: Any, prediction_model: Any
) -> None:
    prediction = {"ticker": "AAA", "target_date": "2026-08-10"}
    prediction["model"] = prediction_model
    book = dict(model=package_model, predictions=[prediction])
    packages = [
        dict(book, run_date="2026-07-14", _source_file="a-2026-07-14"),
        dict(book, run_date="2026-07-15", _source_file="b-2026-07-15"),
    ]
    assert list(sl.find_duplicate_books(packages)) == ["b-2026-07-15"]


# ---------------------------------------------------------------------------
# Precedence resolution
# ---------------------------------------------------------------------------


def _candidate(**overrides: Any) -> sl.SettlementCandidate:
    base: dict[str, Any] = dict(
        model="m",
        vintage="2026-06-01",
        ticker="XXX",
        type="EQUITY_ALPHA",
        target_date="2026-07-01",
        source_file="src",
        # Ordinary case (settlement_run_date > target_date, price_date ==
        # target_date) is valid by default. Tests exercising TARGET_EQ_RUN_DATE
        # or invalidity must set settlement_run_date/price_date explicitly --
        # settlement_run_date == target_date is NOT a safe default here since
        # that requires price_date to be the *prior* session, not target_date.
        settlement_run_date="2026-07-02",
        settled_at="2026-07-02",
        price=100.0,
        price_date="2026-07-01",
        price_tag="LIVE",
        declared_timing_flag=None,
        entry_price=90.0,
        mu=0.05,
        sigma=0.1,
        realized_return=0.11,
        benchmark_return=0.02,
        realized_alpha=0.09,
        direction="HIT",
        ci_result="IN_CI",
        z=0.1,
        note=None,
    )
    base.update(overrides)
    cand = sl.SettlementCandidate(**base)
    convention, valid, reason = sl.validate_timing(
        cand.target_date,
        cand.settlement_run_date,
        cand.price_date,
        cand.declared_timing_flag,
        cand.settled_at,
    )
    cand.settlement_convention = convention
    cand.is_timing_valid = valid
    cand.rejection_reason = reason
    return cand


def test_incomplete_candidate_missing_direction_is_not_complete() -> None:
    assert not _candidate(direction=None).is_complete


def test_precedence_prefers_earliest_valid_candidate() -> None:
    early = _candidate(
        source_file="early", settlement_run_date="2026-07-02", price_date="2026-07-01"
    )
    late = _candidate(
        source_file="late",
        settlement_run_date="2026-07-03",
        price_date="2026-07-01",
        price=101.0,
    )
    canonical, conflicts, _rejected, audit_only, _conflicted = (
        sl.build_canonical_ledger([late, early])
    )
    assert canonical[early.key()].source_file == "early"
    assert not conflicts
    assert late in audit_only


def test_precedence_rejects_timing_invalid_and_falls_back_to_next_candidate() -> None:
    # Case B (target == run date) but settled at the same-day close -> invalid.
    bad = _candidate(
        source_file="bad", settlement_run_date="2026-07-01", price_date="2026-07-01"
    )
    # Case C ordinary, settled two days later but correctly cites the
    # target-date close -> valid.
    good = _candidate(
        source_file="good", settlement_run_date="2026-07-03", price_date="2026-07-01"
    )
    canonical, conflicts, rejected, _audit_only, _conflicted = (
        sl.build_canonical_ledger([bad, good])
    )
    assert canonical[bad.key()].source_file == "good"
    assert bad in rejected
    assert not conflicts


def test_precedence_keeps_agreeing_same_tier_duplicates_as_audit_only() -> None:
    a = _candidate(source_file="model-a", settlement_run_date="2026-07-02", price=100.0)
    b = _candidate(
        source_file="model-b", settlement_run_date="2026-07-02", price=100.005
    )
    canonical, conflicts, _rejected, audit_only, conflicted = sl.build_canonical_ledger(
        [b, a]
    )
    assert not conflicts
    assert canonical[a.key()].source_file == "model-a"  # deterministic tiebreak
    assert b in audit_only
    assert not conflicted


def test_precedence_flags_disagreeing_same_tier_candidates_as_unresolved_conflict() -> (
    None
):
    a = _candidate(
        source_file="model-a",
        settlement_run_date="2026-07-02",
        price=100.0,
        direction="HIT",
    )
    b = _candidate(
        source_file="model-b",
        settlement_run_date="2026-07-02",
        price=140.0,
        direction="MISS",
    )
    canonical, conflicts, rejected, audit_only, conflicted = sl.build_canonical_ledger(
        [a, b]
    )
    assert a.key() not in canonical
    assert len(conflicts) == 1
    assert conflicts[0].key == a.key()
    # Disagreeing candidates must not silently vanish: they land in
    # `conflicted`, not `rejected` or `audit_only`, so total row-accounting
    # still holds (see test_every_candidate_lands_in_exactly_one_bucket).
    assert len(conflicted) == 2
    assert a in conflicted and b in conflicted
    assert not rejected
    assert not audit_only


def test_later_valid_duplicate_never_overrides_an_earlier_valid_settlement() -> None:
    early = _candidate(
        source_file="early", settlement_run_date="2026-07-02", price=100.0
    )
    later_disagreeing = _candidate(
        source_file="later",
        settlement_run_date="2026-07-05",
        price_date="2026-07-01",
        price=999.0,
        direction="MISS",
    )
    (
        canonical,
        conflicts,
        _rejected,
        audit_only,
        _conflicted,
    ) = sl.build_canonical_ledger([early, later_disagreeing])
    assert canonical[early.key()].source_file == "early"
    assert not conflicts  # disagreement outside the earliest tier is not a conflict
    assert later_disagreeing in audit_only


def test_every_candidate_lands_in_exactly_one_bucket() -> None:
    a = _candidate(
        source_file="a", settlement_run_date="2026-07-02", price=100.0
    )  # valid, chosen
    b = _candidate(
        source_file="b", settlement_run_date="2026-07-02", price=100.0
    )  # agrees -> audit
    c = _candidate(
        source_file="c", settlement_run_date="2026-07-02", price_date="2026-06-15"
    )  # doesn't match the target-date close -> rejected
    canonical, conflicts, rejected, audit_only, conflicted = sl.build_canonical_ledger(
        [a, b, c]
    )
    assert canonical[a.key()].source_file == "a"
    assert b in audit_only
    assert c in rejected
    total = len(canonical) + len(rejected) + len(audit_only) + len(conflicted)
    assert total == 3
    assert not conflicts

    # A key that conflicts must still be fully accounted for -- this is the
    # bucket a naive implementation drops candidates into nowhere for (see
    # test_precedence_flags_disagreeing_same_tier_candidates_as_unresolved_conflict).
    x = _candidate(
        source_file="x", ticker="YYY", settlement_run_date="2026-07-02", price=100.0
    )
    y = _candidate(
        source_file="y", ticker="YYY", settlement_run_date="2026-07-02", price=140.0
    )
    canonical2, conflicts2, rejected2, audit_only2, conflicted2 = (
        sl.build_canonical_ledger([x, y])
    )
    total2 = len(canonical2) + len(rejected2) + len(audit_only2) + len(conflicted2)
    assert total2 == 2
    assert len(conflicts2) == 1


# ---------------------------------------------------------------------------
# Due inventory
# ---------------------------------------------------------------------------


def test_due_inventory_is_source_keys_minus_canonical_regardless_of_status() -> None:
    pred = sl.Prediction(
        model="m",
        vintage="2026-06-01",
        ticker="XXX",
        type="EQUITY_ALPHA",
        target_date="2026-07-01",
        adj_score=1.0,
        mu=0.05,
        sigma=0.1,
        entry_price=100.0,
        source_file="src",
    )
    # Prediction.key() has no status field at all -- due inventory can only
    # ever be computed from (target_date, canonical membership), never from
    # a source "status" field that the daily system never mutates.
    assert not hasattr(pred, "status")

    due = sl.compute_due_inventory([pred], {}, set(), as_of="2026-07-01")
    assert pred.key() in due

    not_yet_due = sl.compute_due_inventory([pred], {}, set(), as_of="2026-06-15")
    assert pred.key() not in not_yet_due

    settled = sl.compute_due_inventory(
        [pred], {pred.key(): _candidate()}, set(), as_of="2026-07-01"
    )
    assert pred.key() not in settled


def test_due_inventory_excludes_conflicted_keys() -> None:
    # A conflicted key needs manual reconciliation, not another automated
    # settlement attempt -- it must not look like an ordinary open
    # prediction that the next run should just try to settle again.
    pred = sl.Prediction(
        model="m",
        vintage="2026-06-01",
        ticker="XXX",
        type="EQUITY_ALPHA",
        target_date="2026-07-01",
        adj_score=1.0,
        mu=0.05,
        sigma=0.1,
        entry_price=100.0,
        source_file="src",
    )
    due = sl.compute_due_inventory([pred], {}, {pred.key()}, as_of="2026-07-01")
    assert pred.key() not in due


# ---------------------------------------------------------------------------
# Rolling calibration metrics
# ---------------------------------------------------------------------------


def test_spearman_rank_ic_perfect_positive_correlation() -> None:
    pairs = [(1.0, 10.0), (2.0, 20.0), (3.0, 30.0), (4.0, 40.0)]
    assert sl.spearman_rank_ic(pairs) == pytest.approx(1.0)


def test_spearman_rank_ic_perfect_negative_correlation() -> None:
    pairs = [(1.0, 40.0), (2.0, 30.0), (3.0, 20.0), (4.0, 10.0)]
    assert sl.spearman_rank_ic(pairs) == pytest.approx(-1.0)


def test_spearman_rank_ic_insufficient_pairs_is_none() -> None:
    assert sl.spearman_rank_ic([(1.0, 2.0)]) is None
    assert sl.spearman_rank_ic([]) is None


def test_compute_rolling_metrics_separates_equity_and_market_forecast() -> None:
    eq = _candidate(type="EQUITY_ALPHA", direction="HIT", ci_result="IN_CI", z=0.1)
    mf = _candidate(
        type="MARKET_FORECAST",
        ticker="SPY",
        direction="MISS",
        ci_result="OUT_CI_HIGH",
        z=-0.2,
    )
    canonical = {eq.key(): eq, mf.key(): mf}
    metrics = sl.compute_rolling_metrics(canonical, {})
    assert metrics["equity_alpha"]["n"] == 1
    assert metrics["equity_alpha"]["eff_n"] == 1
    assert metrics["market_forecast"]["n"] == 1
    assert metrics["market_forecast"]["eff_n"] == 1
    assert metrics["equity_alpha"]["hit_rate"] == 1.0
    assert metrics["market_forecast"]["hit_rate"] == 0.0
    assert metrics["equity_alpha"]["status"] == "INSUFFICIENT_SETTLED_N"
    assert not metrics["equity_alpha"]["track_a_calibration_proposal_eligible"]


def test_eff_n_counts_non_overlapping_28_day_target_windows() -> None:
    records = [
        _candidate(ticker="A", target_date="2026-07-01"),
        _candidate(ticker="B", target_date="2026-07-01"),
        _candidate(ticker="C", target_date="2026-07-28"),
        _candidate(ticker="D", target_date="2026-07-29"),
        _candidate(ticker="E", target_date="2026-08-26"),
    ]

    assert sl.effective_independent_sample_size(records) == 3


@pytest.mark.parametrize(
    ("value", "date"),
    [
        ("2026-09-03", dt.date(2026, 9, 3)),
        ("not-a-date", None),
        (20260903, None),
        # date.fromisoformat accepts these; the regex does not, so neither did main.
        ("20260903", None),
        ("2026-W36-4", None),
        # The date regex accepts these; the calendar has no such day.
        ("2026-02-30", None),
        ("0000-01-01", None),
    ],
)
def test_parse_date_is_none_for_anything_but_a_calendar_date(
    value: Any, date: dt.date | None
) -> None:
    assert sl._parse_date(value) == date


def test_sample_sizes_skip_a_target_date_no_calendar_has() -> None:
    records = [_candidate(), _candidate(target_date="2026-02-30")]
    assert sl.effective_independent_sample_size(records) == 1
    assert sl.project_effective_sample_size(records, [])["eff_n"] == 1


@pytest.mark.parametrize(
    ("target_date", "next_window_opens"),
    [("9999-12-03", "9999-12-31"), ("9999-12-04", None), ("9999-12-20", None)],
)
def test_projection_has_no_next_window_after_the_last_calendar_date(
    target_date: str, next_window_opens: str | None
) -> None:
    pending = sl.Prediction(
        model="m",
        vintage="9999-12-03",
        ticker="YYY",
        type="EQUITY_ALPHA",
        target_date="9999-12-31",
        adj_score=None,
        mu=None,
        sigma=None,
        entry_price=None,
        source_file="src",
    )
    projection = sl.project_effective_sample_size(
        [_candidate(target_date=target_date)], [pending]
    )
    assert projection == {
        "eff_n": 1,
        "target_date_span_days": 0,
        "earliest_target_date": target_date,
        "latest_target_date": target_date,
        "selected_windows": [target_date],
        "next_window_opens": next_window_opens,
        "eff_n_increments_on": next_window_opens,
        "pending_predictions_at_that_date": 1 if next_window_opens else 0,
    }


def test_track_a_calibration_proposal_requires_raw_and_effective_n() -> None:
    overlapping_candidates = [
        _candidate(
            ticker=f"OVERLAP_{i}",
            vintage=f"2026-06-{(i % 20) + 1:02d}",
            target_date=f"2026-07-{(i % 20) + 1:02d}",
            direction="HIT" if i % 2 == 0 else "MISS",
        )
        for i in range(20)
    ]
    overlapping = {candidate.key(): candidate for candidate in overlapping_candidates}
    overlapping_metrics = sl.compute_rolling_metrics(overlapping, {})["equity_alpha"]

    assert overlapping_metrics["n"] == 20
    assert overlapping_metrics["eff_n"] == 1
    assert overlapping_metrics["hit_rate"] == 0.5
    assert not overlapping_metrics["track_a_calibration_proposal_eligible"]
    assert (
        overlapping_metrics["track_a_calibration_proposal_status"]
        == "INSUFFICIENT_EFFECTIVE_N"
    )

    independent = {
        candidate.key(): candidate
        for candidate in [
            _candidate(
                ticker=f"WINDOW_1_{i}",
                vintage=f"2026-06-{i + 1:02d}",
                target_date="2026-07-01",
            )
            for i in range(7)
        ]
        + [
            _candidate(
                ticker=f"WINDOW_2_{i}",
                vintage=f"2026-07-{i + 1:02d}",
                target_date="2026-07-29",
            )
            for i in range(7)
        ]
        + [
            _candidate(
                ticker=f"WINDOW_3_{i}",
                vintage=f"2026-08-{i + 1:02d}",
                target_date="2026-08-26",
            )
            for i in range(6)
        ]
    }
    independent_metrics = sl.compute_rolling_metrics(independent, {})["equity_alpha"]

    assert independent_metrics["n"] == 20
    assert independent_metrics["eff_n"] == 3
    assert independent_metrics["track_a_calibration_proposal_eligible"]
    assert independent_metrics["track_a_calibration_proposal_status"] == "ELIGIBLE"


# ---------------------------------------------------------------------------
# Duplicate prediction books
# ---------------------------------------------------------------------------


def _book(model: str, source_file: str, run_date: str = "2026-07-13") -> dict[str, Any]:
    """A package whose two-name prediction book targets 2026-08-10 (a Monday)."""
    return {
        "run_date": run_date,
        "model": model,
        "_source_file": source_file,
        "predictions": [
            {
                "run_date": "2026-07-13",
                "model": model,
                "ticker": ticker,
                "type": "EQUITY_ALPHA",
                "target_date": "2026-08-10",
                "entry_price": 100.0,
                "mu": 0.02,
                "sigma": 0.1,
                "adj_score": adj_score,
                "thesis": f"{model} momentum call",
            }
            for ticker, adj_score in (("AAA", 1.0), ("BBB", -0.5))
        ],
        "settlements": [],
    }


def _settler(*models: str) -> dict[str, Any]:
    """A 2026-08-11 run settling each model's 2026-07-13 book at the 08-10 close."""
    return {
        "run_date": "2026-08-11",
        "model": "model-c",
        "_source_file": "model-c-2026-08-11",
        "predictions": [],
        "settlements": [
            {
                "vintage": "2026-07-13",
                "model": model,
                "ticker": ticker,
                "type": "EQUITY_ALPHA",
                "target_date": "2026-08-10",
                "settle_price": price,
                "settle_price_date": "2026-08-10",
                "entry_price": 100.0,
                "mu": 0.02,
                "sigma": 0.1,
                "realized_return": price / 100.0 - 1,
                "benchmark_return": 0.0,
                "realized_alpha": price / 100.0 - 1,
                "direction": "HIT" if price > 100.0 else "MISS",
                "ci_result": "IN_CI",
                "z": 0.1,
            }
            for model in models
            for ticker, price in (("AAA", 105.0), ("BBB", 98.0))
        ],
    }


def test_cloned_package_is_duplicate_of_its_original_and_excluded_from_metrics() -> (
    None
):
    # The gemini-3.5-flash-2026-07-13 incident in miniature: model-b's package is
    # model-a's book republished under another model name (free text included),
    # and a later run settled both copies.
    original = _book("model-a", "model-a-2026-07-13")
    clone = _book("model-b", "model-b-2026-07-13")

    manifest = sl.build_manifest(
        [original, clone, _settler("model-a", "model-b")], as_of="2026-08-11"
    )

    # Counted once: only the original's forecasts are canonical and scored.
    assert manifest["rolling_metrics"]["equity_alpha"]["n"] == 2
    assert {c["model"] for c in manifest["canonical_settlements"]} == {"model-a"}
    assert set(manifest["rolling_metrics"]["rank_ic_by_vintage"]) == {
        "model-a:2026-07-13"
    }

    # Reported: the copy is DUPLICATE_OF the original, with what it excluded.
    (book,) = manifest["duplicate_books"]
    assert (book["source_file"], book["duplicate_of"], book["original_rule"]) == (
        "model-b-2026-07-13",
        "model-a-2026-07-13",
        "FOLDER_NAME_TIEBREAK",
    )
    assert (book["excluded_prediction_keys"], book["excluded_candidate_rows"]) == (2, 2)
    assert {c["model"] for c in manifest["duplicate_book_candidates"]} == {"model-b"}

    s = manifest["summary"]
    assert (s["duplicate_books"], s["duplicate_book_rows"], s["due_inventory"]) == (
        1,
        2,
        0,
    )
    settled = (
        s["canonical_equity_alpha_settlements"]
        + s["canonical_market_forecast_settlements"]
    )
    assert (
        settled
        + s["rejected_rows"]
        + s["audit_only_rows"]
        + s["conflicted_rows"]
        + s["duplicate_book_rows"]
        == s["total_candidate_rows"]
        == 4
    )

    # The copy contributes nothing: metrics match a ledger that never had it...
    never_cloned = sl.build_manifest(
        [original, _settler("model-a")], as_of="2026-08-11"
    )
    assert manifest["rolling_metrics"] == never_cloned["rolling_metrics"]

    # ...and its keys are never due, so no later run is asked to settle them.
    unsettled = sl.build_manifest([original, clone], as_of="2026-08-10")
    assert {d["model"] for d in unsettled["due_inventory"]} == {"model-a"}


def test_pinned_original_overrides_the_folder_name_tiebreak() -> None:
    # In the June pairs the copy's folder (gemini-3.5-flash-*) sorts before its
    # original's (gpt-5-*), so without a pin the tiebreak would keep the copy.
    copy = _book("gemini-x", "gemini-x-2026-06-21")
    original = _book("gpt-x", "gpt-x-2026-06-21")

    unpinned = sl.find_duplicate_books([copy, original], pinned_originals={})
    assert unpinned["gpt-x-2026-06-21"].duplicate_of == "gemini-x-2026-06-21"

    pinned = sl.find_duplicate_books(
        [copy, original], pinned_originals={"gpt-x-2026-06-21": "provenance"}
    )
    assert set(pinned) == {"gemini-x-2026-06-21"}
    book = pinned["gemini-x-2026-06-21"]
    assert (book.duplicate_of, book.original_rule, book.reason) == (
        "gpt-x-2026-06-21",
        "PINNED",
        "provenance",
    )


def test_unpinned_copy_with_a_later_run_date_is_the_duplicate() -> None:
    # A later package republishing an earlier book verbatim loses to the
    # earlier one whatever the folder names are.
    earlier = _book("model-z", "model-z-2026-07-13")
    republished = _book("model-a", "model-a-2026-07-20", run_date="2026-07-20")

    found = sl.find_duplicate_books([republished, earlier], pinned_originals={})

    assert set(found) == {"model-a-2026-07-20"}
    book = found["model-a-2026-07-20"]
    assert (book.duplicate_of, book.original_rule) == (
        "model-z-2026-07-13",
        "EARLIEST_RUN_DATE",
    )


def test_packages_without_predictions_are_never_duplicate_books() -> None:
    # Two NO_TRADE packages with empty books are identical once the model name
    # is masked, but there is no forecast in them to double-count.
    empty = [
        {
            "run_date": "2026-07-13",
            "model": model,
            "_source_file": f"{model}-2026-07-13",
            "predictions": [],
            "settlements": [],
        }
        for model in ("model-a", "model-b")
    ]
    assert sl.find_duplicate_books(empty) == {}


def test_same_model_copy_never_excludes_the_original_books_keys() -> None:
    # A second folder holding the same model's run carries the same canonical
    # keys as the original, so nothing is double-counted: the copy is
    # reported, but the original's settlements must still count.
    original = _book("model-a", "model-a-2026-07-13")
    rerun = _book("model-a", "model-a-2026-07-13-rerun")

    manifest = sl.build_manifest(
        [original, rerun, _settler("model-a")], as_of="2026-08-11"
    )

    assert [
        (b["source_file"], b["excluded_prediction_keys"])
        for b in manifest["duplicate_books"]
    ] == [("model-a-2026-07-13-rerun", 0)]
    assert manifest["rolling_metrics"]["equity_alpha"]["n"] == 2


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _cli_manifest(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    output_dir: Path,
    packages: list[dict[str, Any]],
    as_of: str | None,
) -> Any:
    output_dir.mkdir()
    for pkg in packages:
        folder = output_dir / pkg["_source_file"]
        folder.mkdir()
        (folder / "15_predictions.json").write_text(json.dumps(pkg))
    argv = ["settlement_ledger.py", "--output-dir", str(output_dir)]
    monkeypatch.setattr(sys, "argv", argv + (["--as-of", as_of] if as_of else []))
    sl.main()
    return json.loads(capsys.readouterr().out)


@pytest.mark.parametrize("as_of", [None, "2026-08-11"], ids=["no-as-of", "as-of"])
@pytest.mark.parametrize("copy", [False, True], ids=["own-book", "duplicate-book"])
@pytest.mark.parametrize(
    "run_date", [20260902, None, float("nan")], ids=["number", "null", "nan"]
)
def test_cli_leaves_out_a_package_whose_run_date_is_not_a_string(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    run_date: Any,
    copy: bool,
    as_of: str | None,
) -> None:
    good = [_book("model-a", "model-a-2026-07-13"), _settler("model-a")]
    bad = _book("model-b", "model-b-2026-07-20")
    bad["run_date"] = run_date
    if not copy:
        bad["predictions"] = bad["predictions"][:1]

    manifest = _cli_manifest(monkeypatch, capsys, tmp_path / "a", good + [bad], as_of)

    assert manifest == _cli_manifest(monkeypatch, capsys, tmp_path / "b", good, as_of)


def test_cli_leaves_out_every_package_when_no_run_date_is_a_string(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # Nothing compares these run_dates, so the CLI used to keep both, under as_of
    # 20260903.
    packages = [
        {"run_date": run_date, "_source_file": f"m-{run_date}", "predictions": []}
        for run_date in (20260902, 20260903)
    ]

    manifest = _cli_manifest(monkeypatch, capsys, tmp_path / "a", packages, None)

    assert manifest == _cli_manifest(monkeypatch, capsys, tmp_path / "b", [], None)


# ---------------------------------------------------------------------------
# Integration properties against the real repository data
# ---------------------------------------------------------------------------


@real_data
def test_rerun_is_idempotent_and_never_unsettles_or_changes_a_key() -> None:
    early = _packages_as_of("2026-07-14")
    later = _packages_as_of("2026-07-15")

    m_a = sl.build_manifest(early, as_of="2026-07-14")
    m_b = sl.build_manifest(early, as_of="2026-07-14")
    assert m_a == m_b  # re-scanning identical input is fully deterministic

    m_later = sl.build_manifest(later, as_of="2026-07-15")

    def index(manifest: dict[str, Any]) -> dict[Any, Any]:
        return {
            (c["model"], c["vintage"], c["ticker"], c["type"], c["target_date"]): c
            for c in manifest["canonical_settlements"]
        }

    early_idx, later_idx = index(m_a), index(m_later)
    assert set(early_idx) <= set(later_idx)  # no key is ever un-settled
    for key, cand in early_idx.items():
        later_cand = later_idx[key]
        assert cand["price"] == later_cand["price"]
        assert cand["direction"] == later_cand["direction"]
        assert cand["source_file"] == later_cand["source_file"]


@real_data
def test_july14_conflict_resolves_to_prior_close_and_rejects_intraday_candidate() -> (
    None
):
    manifest = sl.build_manifest(_packages_as_of("2026-07-15"), as_of="2026-07-15")

    accepted = [
        c
        for c in manifest["canonical_settlements"]
        if c["vintage"] == "2026-06-16"
        and c["target_date"] == "2026-07-14"
        and c["ticker"] == "GS"
    ]
    assert len(accepted) == 1
    assert accepted[0]["source_file"] == "claude-fable-5-2026-07-14"
    assert accepted[0]["price_date"] == "2026-07-13"
    assert accepted[0]["settlement_convention"] == "TARGET_EQ_RUN_DATE"

    rejected_intraday = [
        c
        for c in manifest["rejected_candidates"]
        if c["vintage"] == "2026-06-16"
        and c["target_date"] == "2026-07-14"
        and c["ticker"] == "GS"
        and c["source_file"] == "gpt-5-2026-07-14"
    ]
    assert len(rejected_intraday) == 1
    assert rejected_intraday[0]["price_date"] == "2026-07-14"
    assert "intraday" in rejected_intraday[0]["rejection_reason"]


@real_data
def test_market_forecast_counts_match_the_plans_acceptance_criteria() -> None:
    m14 = sl.build_manifest(_packages_as_of("2026-07-14"), as_of="2026-07-14")
    m15 = sl.build_manifest(_packages_as_of("2026-07-15"), as_of="2026-07-15")
    assert m14["summary"]["canonical_market_forecast_settlements"] == 9
    assert m15["summary"]["canonical_market_forecast_settlements"] == 12


@real_data
def test_july24_overlapping_cohort_has_one_effective_window() -> None:
    manifest = sl.build_manifest(_packages_as_of("2026-07-24"), as_of="2026-07-24")
    metrics = manifest["rolling_metrics"]
    equity = metrics["equity_alpha"]
    market = metrics["market_forecast"]

    # Was (189, 1) and (33, 1) before duplicate books were excluded:
    # gemini-3.5-flash-2026-06-21 is a copy of gpt-5-2026-06-21's book, and
    # claude-fable-5-2026-07-20 settled both copies (14 EQ + 3 MF each), so
    # those forecasts were counted twice.
    assert (equity["n"], equity["eff_n"]) == (175, 1)
    assert (market["n"], market["eff_n"]) == (30, 1)
    assert not equity["track_a_calibration_proposal_eligible"]
    assert not market["track_a_calibration_proposal_eligible"]

    # Neither Track B counting change alters scoring math: eff_n left these
    # untouched, and they moved only because the copy's 17 duplicate records
    # left the input (was 0.5291 / 0.7619 / -0.2129, market 0.2121 / 0.6364 /
    # -0.7306, rank IC -0.0939).
    assert equity["hit_rate"] == pytest.approx(0.5371428571428571)
    assert equity["ci_coverage"] == pytest.approx(0.7657142857142857)
    assert equity["mean_z"] == pytest.approx(-0.2005164238724117)
    assert market["hit_rate"] == pytest.approx(0.23333333333333334)
    assert market["ci_coverage"] == pytest.approx(0.6666666666666666)
    assert market["mean_z"] == pytest.approx(-0.7035508867875725)
    assert metrics["rank_ic_weighted_mean"] == pytest.approx(-0.09070225128741728)


@real_data
def test_pre_convention_equity_settlements_without_a_valid_candidate_stay_due() -> None:
    """The 2026-06-10 and 2026-06-11 EQUITY_ALPHA vintages (settled 07-08 and
    07-09, both before the settlement-timing convention was even informally
    applied starting 2026-07-12) only ever produced settlement rows that used
    the *settlement day's* "current price" instead of the target date's own
    close -- an ORDINARY-case violation distinct from the named 07-14
    TARGET_EQ_RUN_DATE conflict. Every one of the 29 candidates for those
    keys is therefore timing-invalid, so they correctly remain in
    due_inventory rather than being silently counted as settled.

    This is why the canonical EQUITY_ALPHA count here (48 through 07-14, 62
    through 07-15) is lower than the plan's stated target (77 / 91), which
    was taken from the 2026-07-15 reflection artifact's hand/LLM-driven
    dedup: that process deduped by identity but did not independently
    re-validate each candidate's price_date against the target date, so it
    missed this second violation class. MARKET_FORECAST is unaffected
    (matches exactly, see test above) because none of its settlements have
    this defect. See the canonical-ledger contract section of rules.md for
    the disclosed rationale.
    """
    manifest = sl.build_manifest(_packages_as_of("2026-07-15"), as_of="2026-07-15")

    due = {(d["model"], d["vintage"], d["ticker"]) for d in manifest["due_inventory"]}
    assert ("claude-fable-5", "2026-06-10", "MCK") in due
    assert ("gpt-5", "2026-06-11", "MCK") in due
    assert manifest["summary"]["due_inventory"] == 29
    assert manifest["summary"]["canonical_equity_alpha_settlements"] == 62
    assert manifest["summary"]["canonical_market_forecast_settlements"] == 12


@real_data
def test_every_real_candidate_row_lands_in_exactly_one_bucket() -> None:
    manifest = sl.build_manifest(_packages_as_of("2026-07-15"), as_of="2026-07-15")
    s = manifest["summary"]
    settled = (
        s["canonical_equity_alpha_settlements"]
        + s["canonical_market_forecast_settlements"]
    )
    assert (
        settled
        + s["rejected_rows"]
        + s["audit_only_rows"]
        + s["conflicted_rows"]
        + s["duplicate_book_rows"]
        == s["total_candidate_rows"]
    )
    assert s["conflicts"] == 0  # no real conflicts observed as of this cutoff
    # gemini-3.5-flash-2026-07-13 copies claude-fable-5-2026-07-13, including
    # its 20 settlement rows. A copy is not independent evidence, so those rows
    # now land in duplicate_book_rows instead of audit_only_rows.
    assert s["duplicate_book_rows"] == 20


@real_data
def test_real_duplicate_books_are_excluded_from_rolling_metrics() -> None:
    """Every gemini-3.5-flash prediction book in the repo is another model's
    book republished under that name, and a later run settled both copies of
    each: claude-fable-5-2026-07-20 (the 06-21 books, 17 + 17), gpt-5-2026-07-27
    (06-29, 17 + 17), and gpt-5.6-sol-2026-08-10 (07-13, 27 + 27). Excluding
    the copies takes EQUITY_ALPHA n from 819 to 767 (-14 - 14 - 24) and
    MARKET_FORECAST n from 132 to 123 (-3 per copy). eff_n stays 2 because each
    original covers the same target dates as its copy."""
    manifest = sl.build_manifest(_packages_as_of("2026-08-10"), as_of="2026-08-10")

    assert {
        b["source_file"]: (
            b["duplicate_of"],
            b["original_rule"],
            b["excluded_prediction_keys"],
        )
        for b in manifest["duplicate_books"]
    } == {
        "gemini-3.5-flash-2026-06-21": ("gpt-5-2026-06-21", "PINNED", 17),
        "gemini-3.5-flash-2026-06-29": ("gpt-5-2026-06-29", "PINNED", 17),
        "gemini-3.5-flash-2026-07-13": ("claude-fable-5-2026-07-13", "PINNED", 27),
    }
    assert not any(
        c["model"] == "gemini-3.5-flash" for c in manifest["canonical_settlements"]
    )

    metrics = manifest["rolling_metrics"]
    equity, market = metrics["equity_alpha"], metrics["market_forecast"]
    assert (equity["n"], equity["eff_n"]) == (767, 2)
    assert (market["n"], market["eff_n"]) == (123, 2)
    # Each original book still counts, once.
    assert metrics["rank_ic_by_vintage"]["claude-fable-5:2026-07-13"]["n"] == 24
    assert metrics["rank_ic_by_vintage"]["gpt-5:2026-06-21"]["n"] == 14
    assert metrics["rank_ic_by_vintage"]["gpt-5:2026-06-29"]["n"] == 14
    assert not any(
        k.startswith("gemini-3.5-flash:") for k in metrics["rank_ic_by_vintage"]
    )
