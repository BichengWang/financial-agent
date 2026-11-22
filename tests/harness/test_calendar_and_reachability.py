from __future__ import annotations

import json
from pathlib import Path

import pytest
from conftest import (
    GROUNDED,
    OUTPUT_DIR,
    build_package,
    malformed_package,
    market_forecast,
    override,
    real_data,
    stub_package,
)

from financial_agent.harness.gates import (
    decide_status,
    go_reachability,
    replay_history,
    replay_status,
)
from financial_agent.harness.lifecycle import RunStatus
from financial_agent.harness.market_calendar import session
from financial_agent.harness.policy import Policy


@pytest.mark.parametrize(
    ("day", "kind", "basis"),
    [
        ("2026-09-03", "TRADING", "2026-09-03"),
        ("2026-07-03", "HOLIDAY", "2026-07-02"),  # Independence Day observed
        ("2026-06-19", "HOLIDAY", "2026-06-18"),  # Juneteenth
        ("2026-08-22", "WEEKEND", "2026-08-21"),
        ("2026-09-07", "HOLIDAY", "2026-09-04"),  # Labor Day after a weekend
    ],
)
def test_sessions(day: str, kind: str, basis: str) -> None:
    result = session(day)
    assert (result.kind, result.basis_date) == (kind, basis)
    assert result.trading_day is (kind == "TRADING")


def decide(policy: Policy, day: str, **kwargs: object) -> tuple[RunStatus, str]:
    args: dict[str, object] = {
        "data_mode": "DELAYED",
        "required_inputs": GROUNDED,
        "investable_count": 0,
        "policy": policy,
        "session": session(day),
    }
    args.update(kwargs)
    decision = decide_status(**args)  # type: ignore[arg-type]
    return decision.status, "; ".join(decision.reasons)


def test_holidays_publish_review_only(policy: Policy) -> None:
    status, reason = decide(policy, "2026-07-03")
    assert status is RunStatus.REVIEW_ONLY
    assert reason == (
        "2026-07-03 is a market holiday; last close 2026-07-02 "
        "(calendar.holiday_status)"
    )
    # An integrity halt still wins over the calendar.
    status, _ = decide(policy, "2026-07-03", integrity_failures=["clone"])
    assert status is RunStatus.HALTED


def test_weekends_keep_the_computed_status_until_a_rule_is_chosen(
    policy: Policy,
) -> None:
    status, reason = decide(policy, "2026-08-22")
    assert status is RunStatus.NO_TRADE
    assert "no status rule (calendar.weekend_status = COMPUTED)" in reason
    weekend = override(policy, calendar__weekend_status="REVIEW_ONLY")
    status, _ = decide(weekend, "2026-08-22")
    assert status is RunStatus.REVIEW_ONLY


def test_trading_days_are_unaffected(policy: Policy) -> None:
    status, reason = decide(policy, "2026-09-03", investable_count=6)
    assert (status, reason) == (RunStatus.GO, "")


def test_go_is_structurally_unreachable_while_two_families_are_shadow(
    policy: Policy, promoted_policy: Policy
) -> None:
    reach = go_reachability(policy)
    assert reach.gating_families == ("tech_z", "macro_z")
    assert [b.split(":")[0] for b in reach.blockers] == [
        "threshold 2",
        "threshold 3",
        "threshold 4",
    ]
    assert go_reachability(promoted_policy).reachable
    # Promoting one family is not enough: completeness (proxy) needs all four.
    one = go_reachability(
        promoted_policy, available_families=["fund_z", "tech_z", "macro_z"]
    )
    assert [b.split(":")[0] for b in one.blockers] == ["threshold 4"]
    few = go_reachability(promoted_policy, ranked_names=4)
    assert few.blockers == ("4 ranked names < 5 required for GO",)


@real_data
def test_reachability_reproduces_the_runs_own_finding(policy: Policy) -> None:
    """claude-opus-5-2026-09-03 notes: "evidence thresholds 2, 3 and 4 cannot
    be satisfied". The harness derives the same from the ledger."""
    replay = replay_status(OUTPUT_DIR / "claude-opus-5-2026-09-03", policy)
    assert replay is not None and replay.reachability is not None
    assert not replay.reachability.reachable
    assert len(replay.reachability.blockers) == 3
    assert replay.blocking == {
        "#2 families": 24,
        "#3 conviction share": 24,
        "#4 data quality": 24,
    }


def test_replay_skips_a_malformed_ledger_and_goes_on(
    tmp_path: Path, policy: Policy, malformed_ledger: tuple[bytes, str]
) -> None:
    bad = malformed_package(tmp_path / "claude-opus-5-2026-09-02", malformed_ledger[0])
    good = build_package(tmp_path, [market_forecast("SPY", 773.17)])
    assert replay_status(bad, policy) is None
    assert [name for name, _ in replay_history(tmp_path, policy)] == [good.name]


def test_a_run_date_the_calendar_cannot_place_is_like_one_that_does_not_parse(
    tmp_path: Path, policy: Policy
) -> None:
    # 0001-01-01 is a holiday with no earlier close, so session() cannot place it.
    run_dates = {
        "claude-opus-5-0001-01-01": "0001-01-01",
        "claude-opus-5-2026-09-03": "0001-01-01",
        "gpt-5-2026-09-03": "2026-13-01",
        "gemini-3-2026-09-03": "2026-09-05",
    }
    for name, run_date in run_dates.items():
        payload = {"run_date": run_date, "predictions": [market_forecast("SPY", 1.0)]}
        stub_package(tmp_path / name, payload)
    sessions = {name: r.session for name, r in replay_history(tmp_path, policy)}
    assert sessions == {
        "claude-opus-5-0001-01-01": None,
        "claude-opus-5-2026-09-03": session("2026-09-03"),
        "gpt-5-2026-09-03": session("2026-09-03"),
        "gemini-3-2026-09-03": session("2026-09-05"),
    }


@real_data
def test_history_replay_with_the_calendar(policy: Policy) -> None:
    """Pinned like the audit: published packages are immutable."""
    replays = dict(replay_history(OUTPUT_DIR, policy, as_of="2026-09-03"))
    assert len(replays) == 83
    misses = {name for name, replay in replays.items() if not replay.agrees}
    assert len(misses) == 10
    # The holiday rule fixes fable's 07-03 REVIEW_ONLY ...
    assert replays["claude-fable-5-2026-07-03"].agrees
    # ... and surfaces two holiday runs that published NO_TRADE.
    assert {"claude-sonnet-5-2026-07-03", "gpt-5-2026-06-19"} <= misses
    # Weekend REVIEW_ONLY runs stay misses until plan §6 decision 6 is made.
    weekend = replays["claude-fable-5-2026-07-04"]
    assert weekend.session is not None and weekend.session.kind == "WEEKEND"
    assert not weekend.agrees


def test_replay_counts_an_investable_record_without_a_ticker(
    tmp_path: Path, promoted_policy: Policy
) -> None:
    record = {
        "pctl": 96,
        "mu": 0.06,
        "sigma": 0.08,
        "score_explainability": {
            "fund_z": 0.5,
            "tech_z": 0.5,
            "sent_z": 0.5,
            "macro_z": 0.5,
            "data_quality_multiplier": 0.9,
        },
    }
    raw = json.dumps({"predictions": [record]}).encode()
    package = malformed_package(tmp_path / "claude-opus-5-2026-09-03", raw)
    replay = replay_status(package, promoted_policy)
    assert replay is not None and replay.investable == ["?"]
