from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, market_forecast, real_data

from financial_agent.harness.gates import (
    ALWAYS_ARTIFACTS,
    REQUIRED_INPUTS,
    decide_status,
    investability,
    publish_gate,
)
from financial_agent.harness.lifecycle import (
    LifecycleError,
    RunLifecycle,
    RunState,
    RunStatus,
)
from financial_agent.harness.policy import Policy

GROUNDED = {name: True for name in REQUIRED_INPUTS}


def test_two_family_composite_is_never_investable(
    policy: Policy, vlo_record: dict[str, Any]
) -> None:
    failures = investability(vlo_record, policy)
    assert any(f.startswith("2 of 4 families non-negative") for f in failures)
    assert any("tech_z carries" in f for f in failures)  # threshold 3


def complete_record(vlo_record: dict[str, Any]) -> dict[str, Any]:
    record = dict(vlo_record, pctl=92.0, mu=0.05, sigma=0.08)
    record["score_explainability"] = dict(
        vlo_record["score_explainability"],
        fund_z=0.9,
        tech_z=1.0,
        sent_z=0.8,
        macro_z=0.5,
        data_quality_multiplier=0.9,
    )
    return record


def test_complete_record_can_be_investable_once_families_are_promoted(
    policy: Policy, promoted_policy: Policy, vlo_record: dict[str, Any]
) -> None:
    record = complete_record(vlo_record)
    assert investability(record, promoted_policy) == []
    # rules.md § SHADOW Diagnostic Tooling: SHADOW z-scores never count, even
    # when a record carries them.
    failures = investability(record, policy)
    assert any("fund_z (SHADOW), sent_z (SHADOW)" in f for f in failures)


@pytest.mark.parametrize(
    ("kwargs", "status"),
    [
        ({"integrity_failures": ["fabricated price"]}, RunStatus.HALTED),
        ({"benchmark_available": False}, RunStatus.HALTED),
        ({"data_mode": "ILLUSTRATIVE"}, RunStatus.REVIEW_ONLY),
        ({"data_mode": "DELAYED_PARTIAL"}, RunStatus.REVIEW_ONLY),
        (
            {"required_inputs": dict(GROUNDED, sigma_fallback_chain=False)},
            RunStatus.REVIEW_ONLY,
        ),
        ({"investable_count": 4}, RunStatus.NO_TRADE),
        ({"risk_breaches": ["avg pairwise corr 0.52 > 0.45"]}, RunStatus.NO_TRADE),
        ({}, RunStatus.GO),
    ],
)
def test_stop_criteria(
    policy: Policy, kwargs: dict[str, Any], status: RunStatus
) -> None:
    args: dict[str, Any] = {
        "data_mode": "DELAYED",
        "required_inputs": GROUNDED,
        "investable_count": 6,
        "policy": policy,
    }
    args.update(kwargs)
    assert decide_status(**args).status is status


def test_enhancing_inputs_cap_but_never_block(policy: Policy) -> None:
    decision = decide_status(
        data_mode="DELAYED",
        required_inputs=GROUNDED,
        investable_count=6,
        policy=policy,
        enhancing_missing=["options IV/skew"],
    )
    assert decision.status is RunStatus.GO and decision.gross_cap == 0.5
    with pytest.raises(ValueError):
        decide_status(
            data_mode="DELAYED",
            required_inputs=dict(GROUNDED, options_iv=False),
            investable_count=6,
            policy=policy,
        )


def walk_to_risk_review(run: RunLifecycle) -> None:
    for state in (
        RunState.REFLECTION,
        RunState.DATA_OK,
        RunState.TECHNICALS_OK,
        RunState.SCORED,
        RunState.PORTFOLIO_DRAFT,
        RunState.RISK_REVIEW,
    ):
        run.advance(state, at="2026-09-03T22:00:00Z")


def test_lifecycle_generates_the_manifest_transcript() -> None:
    run = RunLifecycle("claude-opus-5-2026-09-03")
    walk_to_risk_review(run)
    run.publish(RunStatus.NO_TRADE, gate_failures=[])
    run.advance(RunState.EVOLUTION_REVIEW)
    # The state line from claude-opus-5-2026-09-03/00_run_manifest.md
    assert run.transcript() == (
        "PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> "
        "PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> EVOLUTION_REVIEW"
    )
    assert run.status is RunStatus.NO_TRADE


def test_lifecycle_refuses_skips_extra_revisions_and_failed_gates() -> None:
    run = RunLifecycle("r")
    with pytest.raises(LifecycleError):
        run.advance(RunState.SCORED)  # reflection must come first
    walk_to_risk_review(run)
    run.advance(RunState.PORTFOLIO_DRAFT)  # the one allowed revision pass
    run.advance(RunState.RISK_REVIEW)
    with pytest.raises(LifecycleError, match="budget exhausted"):
        run.advance(RunState.PORTFOLIO_DRAFT)
    with pytest.raises(LifecycleError):
        run.advance(RunState.PUBLISHED)
    with pytest.raises(LifecycleError, match="publish gate failed"):
        run.publish(RunStatus.GO, gate_failures=["missing 15_predictions.json"])
    run.halt("fabricated evidence propagated past one revision")
    assert (run.state, run.status) == (RunState.HALTED, RunStatus.HALTED)
    with pytest.raises(LifecycleError):
        run.advance(RunState.EVOLUTION_REVIEW)


def build_package(root: Path, predictions: list[dict[str, Any]]) -> Path:
    package = root / "claude-opus-5-2026-09-03"
    package.mkdir()
    for name in ALWAYS_ARTIFACTS:
        (package / name).write_text(f"# {name}\n", encoding="utf-8")
    payload = {"run_status": "NO_TRADE", "predictions": predictions, "settlements": []}
    (package / "15_predictions.json").write_text(json.dumps(payload), encoding="utf-8")
    return package


def test_publish_gate_reads_the_directory(
    tmp_path: Path, policy: Policy, vlo_record: dict[str, Any]
) -> None:
    etfs = [
        market_forecast(t, p)
        for t, p in (("SPY", 773.17), ("QQQ", 560.0), ("SOXX", 300.0))
    ]
    package = build_package(tmp_path, [vlo_record, *etfs])
    assert publish_gate(package, policy) == []

    (package / "08_risk_review.md").unlink()
    (package / "stockanalysis_history_manifest.json").write_text("{}", encoding="utf-8")
    failures = publish_gate(package, policy)
    assert "missing required artifact 08_risk_review.md" in failures
    assert any("outside the artifact contract" in f for f in failures)


def test_publish_gate_blocks_unsettleable_or_inconsistent_ledgers(
    tmp_path: Path, policy: Policy, vlo_record: dict[str, Any]
) -> None:
    percentile_as_score = dict(vlo_record, adj_score=97.1)
    package = build_package(
        tmp_path, [percentile_as_score, market_forecast("SPY", 773.17)]
    )
    failures = publish_gate(package, policy)
    assert any("no MARKET_FORECAST record for QQQ" in f for f in failures)
    assert any("formula.adj_score" in f and "percentile" in f for f in failures)


@real_data
def test_latest_package_passes_and_replays_its_status(policy: Policy) -> None:
    package = OUTPUT_DIR / "claude-opus-5-2026-09-03"
    assert publish_gate(package, policy) == []
    payload = json.loads((package / "15_predictions.json").read_text(encoding="utf-8"))
    equities = [p for p in payload["predictions"] if p.get("type") == "EQUITY_ALPHA"]
    passing = [p for p in equities if not investability(p, policy)]
    decision = decide_status(
        data_mode=payload["data_mode"],
        required_inputs=GROUNDED,  # 00_run_manifest.md: GO-Gate Table all PASS
        investable_count=len(passing),
        policy=policy,
    )
    assert (len(equities), len(passing)) == (24, 0)
    assert decision.status.value == payload["run_status"] == "NO_TRADE"
