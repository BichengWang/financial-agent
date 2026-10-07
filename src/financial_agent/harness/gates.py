"""Decision gates: evidence thresholds, stop criteria, and the publish gate.

These are the parts of ``rules.md`` that decide outcomes. As prose they are
re-interpreted by every model on every run; as functions they give the same
answer for the same inputs, and the model's job shrinks to explaining it.
"""

from __future__ import annotations

import datetime as dt
import json
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from financial_agent.harness.audit import audit_record
from financial_agent.harness.lifecycle import RunStatus
from financial_agent.harness.market_calendar import HOLIDAY, Session, session
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


def _family_z(record: Mapping[str, Any], policy: Policy) -> dict[str, float | None]:
    """Family z-scores that may count: SHADOW families never do (rules.md
    § SHADOW Diagnostic Tooling), whatever value a record carries."""
    explain = record.get("score_explainability")
    if not isinstance(explain, Mapping):
        return {f: None for f in FAMILIES}
    shadow = set(policy.shadow_families)
    return {f: None if f in shadow else _num(explain.get(f)) for f in FAMILIES}


def _kelly_gate(record: Mapping[str, Any], policy: Policy) -> str | None:
    """A v1 record's own ``kelly_gate`` (it may use the beta-adjusted method);
    otherwise the ``mu / sigma^2`` fallback. ``None`` when unsettleable."""
    explain = record.get("score_explainability")
    metrics = explain.get("metrics") if isinstance(explain, Mapping) else None
    if isinstance(metrics, Mapping) and metrics.get("kelly_gate") in {
        "BLOCKED",
        "PENALTY",
        "OK",
        "CAP_BINDING",
    }:
        return str(metrics["kelly_gate"])
    mu, sigma = _num(record.get("mu")), _num(record.get("sigma"))
    if mu is None or sigma is None or sigma <= 0:
        return None
    return policy.kelly(mu, sigma).gate


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
    family_z = _family_z(record, policy)
    dq: float | None = None
    if isinstance(explain, Mapping):
        dq = _num(explain.get("data_quality_multiplier"))
    else:
        failures.append("score_explainability missing: families unverifiable")

    shadow = set(policy.shadow_families)
    available = [f for f in FAMILIES if family_z[f] is not None]
    non_negative = [f for f in available if (family_z[f] or 0.0) >= 0]
    need = int(policy.num("evidence.min_non_negative_families"))
    if len(non_negative) < need:
        missing = [
            f"{f} (SHADOW)" if f in shadow else f
            for f in FAMILIES
            if family_z[f] is None
        ]
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

    gate = _kelly_gate(record, policy)
    if gate is None:
        failures.append("mu/sigma missing: unsettleable")
    elif gate == "BLOCKED":
        failures.append("fractional Kelly <= 0 blocks investable status")
    return failures


CONFIDENCE_ORDER = ("LOW", "MEDIUM", "HIGH")


def earnings_in_window(record: Mapping[str, Any], policy: Policy) -> bool:
    """``days_to_earnings`` inside ``risk.earnings_window_days`` (rules.md
    § Risk Controls: confidence capped ``LOW``)."""
    days = _num(record.get("days_to_earnings"))
    return days is not None and 0 <= days <= policy.num("risk.earnings_window_days")


def confidence_ceiling(
    record: Mapping[str, Any], policy: Policy, *, earnings_within_window: bool = False
) -> tuple[str, list[str]]:
    """``rules.md`` § Confidence Labels: the highest label the evidence allows.

    Returns the ceiling and the reasons it is not ``HIGH``. The model may
    publish a lower label, never a higher one.
    """
    reasons: list[str] = []
    family_z = _family_z(record, policy)
    supportive = sum(1 for z in family_z.values() if z is not None and z >= 0)
    pctl = _num(record.get("pctl", record.get("percentile"))) or 0.0
    explain = record.get("score_explainability")
    dq = (
        _num(explain.get("data_quality_multiplier"))
        if isinstance(explain, Mapping)
        else None
    ) or 0.0

    def meets(level: str) -> bool:
        return (
            supportive >= policy.num(f"confidence.{level}_min_families")
            and pctl >= policy.num(f"confidence.{level}_min_pctl")
            and dq >= policy.num(f"confidence.{level}_min_data_quality")
        )

    ceiling = "HIGH" if meets("high") else "MEDIUM" if meets("medium") else "LOW"
    if ceiling != "HIGH":
        reasons.append(
            f"{supportive} of 4 families supportive, pctl {pctl:.1f}, DQ {dq:.2f}"
        )
    if _kelly_gate(record, policy) in {"BLOCKED", "PENALTY"}:
        reasons.append("fractional Kelly below the minimum caps MEDIUM")
        ceiling = min(ceiling, "MEDIUM", key=CONFIDENCE_ORDER.index)
    if earnings_within_window:
        reasons.append("earnings inside the window caps LOW")
        ceiling = "LOW"
    return ceiling, reasons


@dataclass(frozen=True)
class Reachability:
    """Whether any name could pass the evidence thresholds with the families
    that can score, before a single record is computed (plan §3.5 step 2)."""

    gating_families: tuple[str, ...]
    blockers: tuple[str, ...]

    @property
    def reachable(self) -> bool:
        return not self.blockers


def go_reachability(
    policy: Policy,
    *,
    available_families: Iterable[str] | None = None,
    ranked_names: int | None = None,
) -> Reachability:
    """Structural blockers of ``GO``: thresholds no record can pass.

    ``available_families`` defaults to every family the policy lets score
    (SHADOW families never do); pass the families a run actually populated to
    check a package. Thresholds that depend on a record's values (percentile,
    Kelly) are never structural and are not checked here.
    """
    wired = set(FAMILIES if available_families is None else available_families)
    gating = tuple(f for f in policy.gating_families if f in wired)
    excluded = [
        f"{f} (SHADOW)" if f in policy.shadow_families else f"{f} (UNAVAILABLE)"
        for f in FAMILIES
        if f not in gating
    ]
    k, blockers = len(gating), []
    need = int(policy.num("evidence.min_non_negative_families"))
    if k < need:
        blockers.append(
            f"threshold 2: needs {need} non-negative families but only {k} can "
            f"score ({', '.join(excluded)} excluded)"
        )
    limit = policy.num("evidence.max_family_conviction_share")
    if k == 0 or 1 / k > limit + 1e-12:
        blockers.append(
            f"threshold 3: with {k} families one carries at least "
            f"{1 / max(k, 1):.0%} of conviction (> {limit:.0%})"
        )
    elif abs(1 / k - limit) <= 1e-12:
        blockers.append(
            f"threshold 3: with {k} families the largest share is at least "
            f"{limit:.0%}, so only an exact tie passes"
        )
    completeness = policy.num("evidence.min_data_completeness")
    if k / len(FAMILIES) < completeness:
        blockers.append(
            f"threshold 4: family completeness at most {k}/{len(FAMILIES)} = "
            f"{k / len(FAMILIES):.0%} < {completeness:.0%} "
            "(family-availability proxy, plan §6 decision 5)"
        )
    minimum = int(policy.num("evidence.min_investable_names"))
    if ranked_names is not None and ranked_names < minimum:
        blockers.append(f"{ranked_names} ranked names < {minimum} required for GO")
    return Reachability(gating, tuple(blockers))


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
    session: Session | None = None,
) -> StatusDecision:
    """``rules.md`` § Stop Criteria + § Input Classification as one function.

    With a ``session``, a non-trading day takes the policy's calendar status
    (integrity halts still win); a ``COMPUTED`` rule keeps the computed status
    and says that no rule applied.
    """
    if integrity_failures:
        return StatusDecision(RunStatus.HALTED, tuple(integrity_failures))
    if not benchmark_available and data_mode != "ILLUSTRATIVE":
        return StatusDecision(
            RunStatus.HALTED, ("benchmark data missing outside ILLUSTRATIVE_MODE",)
        )
    unknown = sorted(set(required_inputs) - set(REQUIRED_INPUTS))
    if unknown:
        raise ValueError(f"not Required inputs (Enhancing never blocks GO): {unknown}")
    note: tuple[str, ...] = ()
    if session is not None and not session.trading_day:
        key = (
            "calendar.holiday_status"
            if session.kind == HOLIDAY
            else "calendar.weekend_status"
        )
        rule = str(policy.get(key))
        if rule != "COMPUTED":
            return StatusDecision(RunStatus(rule), (f"{session.describe()} ({key})",))
        note = (f"{session.describe()}: no status rule ({key} = COMPUTED)",)
    decision = _data_status(
        data_mode=data_mode,
        required_inputs=required_inputs,
        investable_count=investable_count,
        policy=policy,
        risk_breaches=risk_breaches,
        enhancing_missing=enhancing_missing,
    )
    return replace(decision, reasons=decision.reasons + note) if note else decision


def _data_status(
    *,
    data_mode: str,
    required_inputs: Mapping[str, bool],
    investable_count: int,
    policy: Policy,
    risk_breaches: Sequence[str],
    enhancing_missing: Sequence[str],
) -> StatusDecision:
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
    if "schema_version" in payload:
        # A ledger that declares a schema is held to all of it.
        from financial_agent.harness.schema import validate_payload

        failures += [f"schema v1: {f}" for f in validate_payload(payload, policy)]
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
    session: Session | None = None
    reachability: Reachability | None = None
    blocking: dict[str, int] = field(default_factory=dict)

    @property
    def agrees(self) -> bool:
        return self.decision.status.value == self.published


def _run_date(payload: Mapping[str, Any], package_dir: Path) -> str | None:
    for candidate in (payload.get("run_date"), package_dir.name[-10:]):
        try:
            return dt.date.fromisoformat(str(candidate)).isoformat()
        except ValueError:
            continue
    return None


def _threshold(failure: str) -> str:
    """The evidence threshold an ``investability`` failure belongs to."""
    for prefix, label in (
        ("percentile", "#1 percentile"),
        ("score_explainability", "#2 families"),
        ("mu/sigma", "Kelly or mu/sigma"),
        ("fractional Kelly", "Kelly or mu/sigma"),
        ("data-quality", "#4 data quality"),
        ("family completeness", "#4 data quality"),
    ):
        if failure.startswith(prefix):
            return label
    if "families non-negative" in failure:
        return "#2 families"
    if "of conviction" in failure:
        return "#3 conviction share"
    return failure


def replay_status(package_dir: Path, policy: Policy) -> StatusReplay | None:
    """Recompute the run status from the ledger; ``None`` without a ledger.

    Assumes every Required input was grounded: the ledger cannot show otherwise.
    The run date's session applies the calendar rule, and ``blocking`` counts
    the names each evidence threshold rejects.
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
    passing: list[str] = []
    blocking: dict[str, int] = {}
    for record in equities:
        failures = investability(record, policy)
        if not failures:
            passing.append(record["ticker"])
        for label in sorted({_threshold(f) for f in failures}):
            blocking[label] = blocking.get(label, 0) + 1
    run_date = _run_date(payload, package_dir)
    day = session(run_date) if run_date else None
    decision = decide_status(
        data_mode=str(payload.get("data_mode") or "DELAYED"),
        required_inputs={name: True for name in REQUIRED_INPUTS},
        investable_count=len(passing),
        policy=policy,
        session=day,
    )
    published = (
        payload.get("run_status")
        or payload.get("final_status")
        or payload.get("status")
    )
    populated = {
        family
        for record in equities
        for family, z in _family_z(record, policy).items()
        if z is not None
    }
    reach = go_reachability(
        policy, available_families=populated, ranked_names=len(equities)
    )
    return StatusReplay(passing, decision, published, day, reach, blocking)


def replay_history(
    output_dir: Path,
    policy: Policy,
    *,
    since: str | None = None,
    as_of: str | None = None,
) -> list[tuple[str, StatusReplay]]:
    """``replay_status`` for every dated package with a ledger, oldest first."""
    replays: list[tuple[str, StatusReplay]] = []
    for package_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        run_date = package_dir.name[-10:]
        try:
            dt.date.fromisoformat(run_date)
        except ValueError:
            continue
        if (since and run_date < since) or (as_of and run_date > as_of):
            continue
        replay = replay_status(package_dir, policy)
        if replay is not None:
            replays.append((package_dir.name, replay))
    return replays
