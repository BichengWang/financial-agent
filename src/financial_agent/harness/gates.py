"""Decision gates: evidence thresholds, stop criteria, and the publish gate.

These are the parts of ``rules.md`` that decide outcomes. As prose they are
re-interpreted by every model on every run; as functions they give the same
answer for the same inputs, and the model's job shrinks to explaining it.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from financial_agent.harness.audit import audit_record
from financial_agent.harness.lifecycle import RunStatus
from financial_agent.harness.policy import FAMILIES, Policy

# runbook.md § Artifact Table
ALWAYS_ARTIFACTS = (
    "00_run_manifest.md",
    "01_preflight.md",
    "02_reflection.md",
    "03_regime_and_data.md",
    "04_universe_summary.md",
    "05_factor_scores.md",
    "06_top_candidates.md",
    "07_portfolio_proposal.md",
    "08_risk_review.md",
    "09_final_report.md",
    "13_evolution_log.md",
)
CHECKPOINT_ARTIFACTS = (
    "10_midday_monitor.md",
    "11_preclose_check.md",
    "12_close_log.md",
    "14_weekly_review.md",
    "16_monthly_review.md",
)
PREDICTIONS_FILE = "15_predictions.json"
# rules.md § Input Classification: only these may block GO.
REQUIRED_INPUTS = (
    "grounded_entry_price",
    "price_history_60d",
    "sigma_fallback_chain",
    "next_earnings_date",
    "index_union_universe",
)


def _num(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def investability(record: Mapping[str, Any], policy: Policy) -> list[str]:
    """Failed evidence thresholds for one EQUITY_ALPHA prediction record.

    Recomputes from the record's own inputs (z-scores, mu, sigma) instead of
    trusting stored derived fields, whose conventions drift between runs.
    """
    failures: list[str] = []
    pctl = _num(record.get("pctl", record.get("percentile")))
    if pctl is None:
        failures.append("percentile missing")
    elif pctl < policy.num("evidence.min_pctl"):
        failures.append(
            f"percentile {pctl:.1f} < {policy.num('evidence.min_pctl'):.0f}"
        )

    explain = record.get("score_explainability")
    family_z: dict[str, float | None] = {f: None for f in FAMILIES}
    dq: float | None = None
    if isinstance(explain, Mapping):
        family_z = {f: _num(explain.get(f)) for f in FAMILIES}
        dq = _num(explain.get("data_quality_multiplier"))
    else:
        failures.append("score_explainability missing: families unverifiable")

    available = [f for f in FAMILIES if family_z[f] is not None]
    non_negative = [f for f in available if (family_z[f] or 0.0) >= 0]
    need = int(policy.num("evidence.min_non_negative_families"))
    if len(non_negative) < need:
        missing = [f for f in FAMILIES if family_z[f] is None]
        failures.append(
            f"{len(non_negative)} of 4 families non-negative (< {need}); "
            f"UNAVAILABLE: {', '.join(missing) or 'none'}"
        )

    weights = policy.family_weights
    contributions = {
        f: weights[f] * (family_z[f] or 0.0)
        for f in available
        if (family_z[f] or 0) > 0
    }
    total = sum(contributions.values())
    if total > 0:
        family, top = max(contributions.items(), key=lambda kv: kv[1])
        share = top / total
        limit = policy.num("evidence.max_family_conviction_share")
        if share > limit:
            failures.append(
                f"{family} carries {share:.0%} of conviction (> {limit:.0%})"
            )

    completeness = len(available) / len(FAMILIES)
    if completeness < policy.num("evidence.min_data_completeness"):
        failures.append(
            f"family completeness {completeness:.0%} < "
            f"{policy.num('evidence.min_data_completeness'):.0%} (proxy)"
        )
    if dq is not None and dq < policy.num("evidence.min_data_quality_multiplier"):
        failures.append(f"data-quality multiplier {dq:.2f} below floor")

    mu, sigma = _num(record.get("mu")), _num(record.get("sigma"))
    if mu is None or sigma is None or sigma <= 0:
        failures.append("mu/sigma missing: unsettleable")
    elif policy.kelly(mu, sigma).gate == "BLOCKED":
        failures.append("fractional Kelly <= 0 blocks investable status")
    return failures


@dataclass(frozen=True)
class StatusDecision:
    status: RunStatus
    reasons: tuple[str, ...]
    gross_cap: float | None = None


def decide_status(
    *,
    data_mode: str,
    required_inputs: Mapping[str, bool],
    investable_count: int,
    policy: Policy,
    benchmark_available: bool = True,
    integrity_failures: Sequence[str] = (),
    risk_breaches: Sequence[str] = (),
    enhancing_missing: Sequence[str] = (),
) -> StatusDecision:
    """``rules.md`` § Stop Criteria + § Input Classification as one function."""
    if integrity_failures:
        return StatusDecision(RunStatus.HALTED, tuple(integrity_failures))
    if not benchmark_available and data_mode != "ILLUSTRATIVE":
        return StatusDecision(
            RunStatus.HALTED, ("benchmark data missing outside ILLUSTRATIVE_MODE",)
        )
    unknown = sorted(set(required_inputs) - set(REQUIRED_INPUTS))
    if unknown:
        raise ValueError(f"not Required inputs (Enhancing never blocks GO): {unknown}")
    if data_mode == "ILLUSTRATIVE":
        return StatusDecision(
            RunStatus.REVIEW_ONLY, ("ILLUSTRATIVE_MODE publishes REVIEW_ONLY",)
        )
    failed = [name for name in REQUIRED_INPUTS if not required_inputs.get(name, False)]
    if failed or data_mode == "DELAYED_PARTIAL":
        return StatusDecision(
            RunStatus.REVIEW_ONLY,
            tuple(f"Required input not grounded: {name}" for name in failed)
            or ("DELAYED_PARTIAL data mode",),
        )
    minimum = int(policy.num("evidence.min_investable_names"))
    if investable_count < minimum:
        return StatusDecision(
            RunStatus.NO_TRADE,
            (f"{investable_count} names pass the investable threshold (< {minimum})",),
        )
    if risk_breaches:
        return StatusDecision(RunStatus.NO_TRADE, tuple(risk_breaches))
    cap = policy.num("risk.enhancing_missing_gross_cap") if enhancing_missing else None
    reasons = tuple(
        f"Enhancing input missing (cap, not blocker): {e}" for e in enhancing_missing
    )
    return StatusDecision(RunStatus.GO, reasons, gross_cap=cap)


def publish_gate(package_dir: Path, policy: Policy) -> list[str]:
    """Checklist computed from the directory, never written before the files.

    (Three 2026-08 packages claimed artifacts in their manifest that were
    never published; see ``00_run_manifest.md`` of claude-opus-5-2026-09-03.)
    Every prediction record must also pass the error-severity audit checks.
    """
    failures: list[str] = []
    present = {p.name for p in package_dir.iterdir() if p.is_file()}
    for name in ALWAYS_ARTIFACTS:
        if name not in present:
            failures.append(f"missing required artifact {name}")
    contract = set(ALWAYS_ARTIFACTS) | set(CHECKPOINT_ARTIFACTS) | {PREDICTIONS_FILE}
    for name in sorted(present - contract):
        failures.append(f"file outside the artifact contract: {name}")
    predictions_path = package_dir / PREDICTIONS_FILE
    if not predictions_path.exists():
        # rules.md: a run that ranks names is not publishable without it, and
        # every run forecasts the core ETFs, so absence always fails.
        failures.append(f"missing {PREDICTIONS_FILE} (publishing gate)")
        return failures
    try:
        payload = json.loads(predictions_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return failures + [f"{PREDICTIONS_FILE} is not valid JSON: {exc}"]
    predictions = payload.get("predictions") if isinstance(payload, dict) else None
    if not isinstance(predictions, list):
        return failures + [f"{PREDICTIONS_FILE} has no 'predictions' list"]
    if any(p.get("type", "EQUITY_ALPHA") == "EQUITY_ALPHA" for p in predictions):
        forecast = {
            p.get("ticker") for p in predictions if p.get("type") == "MARKET_FORECAST"
        }
        for etf in policy.get("market_forecast.tickers"):
            if etf not in forecast:
                failures.append(f"ranked names but no MARKET_FORECAST record for {etf}")
    for record in predictions:
        for finding in audit_record(record, policy, package=package_dir.name).findings:
            if finding.severity == "error":
                failures.append(f"{finding.ticker}: {finding.check}: {finding.detail}")
    return failures


@dataclass(frozen=True)
class StatusReplay:
    investable: list[str]
    decision: StatusDecision
    published: str | None


def replay_status(package_dir: Path, policy: Policy) -> StatusReplay | None:
    """Recompute the run status from the ledger; ``None`` without a ledger.

    Assumes every Required input was grounded: the ledger cannot show otherwise.
    """
    path = package_dir / PREDICTIONS_FILE
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    equities = [
        p
        for p in payload.get("predictions", [])
        if p.get("type", "EQUITY_ALPHA") == "EQUITY_ALPHA"
    ]
    passing = [p["ticker"] for p in equities if not investability(p, policy)]
    decision = decide_status(
        data_mode=str(payload.get("data_mode") or "DELAYED"),
        required_inputs={name: True for name in REQUIRED_INPUTS},
        investable_count=len(passing),
        policy=policy,
    )
    published = (
        payload.get("run_status")
        or payload.get("final_status")
        or payload.get("status")
    )
    return StatusReplay(passing, decision, published)
