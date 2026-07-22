"""Regression tests for settlement_ledger.py.

Run with: uv run pytest agents/equity/daily_investment_system/tests/
"""

from __future__ import annotations

import datetime as dt
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


def test_new_years_observance_crossing_a_year_boundary_is_not_a_trading_day() -> None:
    # Jan 1 2022 is a Saturday, so NYSE observed New Year's Day on the
    # preceding Friday, 2021-12-31 -- a holiday whose date falls in a
    # *different* calendar year than the Jan-1 holiday that produced it.
    assert not sl.is_trading_day(dt.date(2021, 12, 31))
    assert not sl.is_trading_day(dt.date(2027, 12, 31))  # 2028-01-01 is a Saturday
    # An ordinary Dec 31 (no adjacent-year Saturday New Year's) is unaffected.
    assert sl.is_trading_day(dt.date(2025, 12, 31))


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
    assert metrics["market_forecast"]["n"] == 1
    assert metrics["equity_alpha"]["hit_rate"] == 1.0
    assert metrics["market_forecast"]["hit_rate"] == 0.0
    assert metrics["equity_alpha"]["status"] == "INSUFFICIENT_SETTLED_N"


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
        settled + s["rejected_rows"] + s["audit_only_rows"] + s["conflicted_rows"]
        == s["total_candidate_rows"]
    )
    assert s["conflicts"] == 0  # no real conflicts observed as of this cutoff
