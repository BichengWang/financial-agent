from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, real_data
from test_kernels import MODEL, RUN, etf_inputs, vlo_inputs

from financial_agent.harness.audit import audit_record
from financial_agent.harness.gates import ALWAYS_ARTIFACTS, publish_gate
from financial_agent.harness.kernels import (
    equity_record,
    market_forecast_records,
    predictions_payload,
)
from financial_agent.harness.policy import Policy
from financial_agent.harness.schema import json_schema, validate_payload

SETTLEMENT = {
    "model": MODEL,
    "vintage": "2026-08-01",
    "ticker": "ABT",
    "type": "EQUITY_ALPHA",
    "target_date": "2026-08-29",
    "settle_price": 112.47,
    "settle_price_date": "2026-08-28",
    "settlement_price_tag": "HISTORICAL",
    "timing_flag": "WEEKEND_TARGET",
    "settled_at": "2026-09-03T19:29:02-04:00",
    "realized_return": 0.064049,
    "direction": "HIT",
    "ci_result": "IN_CI",
}


@pytest.fixture
def payload(policy: Policy) -> dict[str, Any]:
    """A v1 ledger built only by kernels from the 2026-09-03 inputs."""
    records = [
        equity_record(RUN, MODEL, vlo_inputs(), policy),
        *market_forecast_records(RUN, MODEL, "BULL", etf_inputs(), policy),
    ]
    return predictions_payload(
        run_date=RUN,
        model=MODEL,
        run_status="NO_TRADE",
        data_mode="DELAYED",
        regime="BULL",
        predictions=records,
        settlements=[SETTLEMENT],
    )


def test_kernel_output_is_valid_v1_and_audits_clean(
    payload: dict[str, Any], policy: Policy
) -> None:
    assert validate_payload(payload, policy) == []
    for record in payload["predictions"]:
        assert audit_record(record, policy).findings == [], record["ticker"]


def test_kernel_output_passes_the_publish_gate(
    tmp_path: Path, payload: dict[str, Any], policy: Policy
) -> None:
    package = tmp_path / f"{MODEL}-{RUN}"
    package.mkdir()
    for name in ALWAYS_ARTIFACTS:
        (package / name).write_text(f"# {name}\n", encoding="utf-8")
    ledger = package / "15_predictions.json"
    ledger.write_text(json.dumps(payload), encoding="utf-8")
    assert publish_gate(package, policy) == []

    payload["predictions"][0]["confidence"] = "HIGH"
    ledger.write_text(json.dumps(payload), encoding="utf-8")
    failures = publish_gate(package, policy)
    assert any(
        f.startswith("schema v1: predictions[0] VLO: confidence HIGH exceeds")
        for f in failures
    )


def mutate(payload: dict[str, Any], path: str, value: Any) -> dict[str, Any]:
    """A copy with ``a.0.b`` set to ``value`` (``...`` deletes the key)."""
    copied = copy.deepcopy(payload)
    *parents, leaf = path.split(".")
    node: Any = copied
    for part in parents:
        node = node[int(part)] if part.isdigit() else node[part]
    if value is ...:
        del node[leaf]
    else:
        node[leaf] = value
    return copied


METRICS = "predictions.0.score_explainability.metrics"


@pytest.mark.parametrize(
    ("path", "value", "finding"),
    [
        ("run_status", ..., "missing run_status"),
        ("final_status", "NO_TRADE", "final_status is not v1; use run_status"),
        ("data_mode", "PAPER", "data_mode='PAPER' is not one of"),
        ("schema_version", 2, "schema_version must be 1"),
        ("predictions.0.percentile", 100.0, "percentile is not v1; use pctl"),
        ("predictions.0.model", "gpt-5", "model differs from the payload's"),
        ("predictions.0.adj_score", None, "adj_score is null"),
        ("predictions.0.sleeve", "INVESTABLE", "sleeve INVESTABLE but 2 of 4"),
        ("predictions.0.mu", 0.07, "mu 0.07 != mu_prior + mu_adjustment"),
        ("predictions.0.mu_adjustment", 0.01, "needs a mu_adjustment_reason"),
        ("predictions.0.confidence", "MEDIUM", "exceeds ceiling LOW"),
        ("predictions.0.score_explainability.fund_z", 0.4, "fund_z is SHADOW"),
        (f"{METRICS}.kelly_025", 0.05, "kelly_025 is not v1"),
        (f"{METRICS}.var95", -7.92, "metrics.var95=-7.92 must be a decimal"),
        (f"{METRICS}.position_weight", 2.10799, "metrics.position_weight 2.10799"),
        (f"{METRICS}.kelly_gate", "OK", "kelly_gate OK != CAP_BINDING"),
        (f"{METRICS}.kelly_raw", 5.0, "kelly_raw 5.0 != mu/sigma^2"),
        ("predictions.1.adj_score", 0.3, "adj_score must be null on MARKET_FORECAST"),
        ("predictions.2.mu_prior", 0.02, "mu_prior 0.02 != 0.034012"),
        ("predictions.3.beta_vs_spy", None, "SOXX needs beta_vs_spy"),
        ("settlements.0.settled_on", RUN, "settled_on is not v1; use settled_at"),
        ("settlements.0.settled_at", "2026-09-03T19:29:02", "settled_at="),
        ("settlements.0.timing_flag", "LATE", "timing_flag='LATE'"),
    ],
)
def test_v1_findings(
    payload: dict[str, Any], policy: Policy, path: str, value: Any, finding: str
) -> None:
    findings = validate_payload(mutate(payload, path, value), policy)
    assert any(finding in f for f in findings), findings


def test_earnings_inside_the_window_caps_confidence_low(
    promoted_policy: Policy,
) -> None:
    families = {"fund_z": 0.6, "tech_z": 0.9, "sent_z": 0.5, "macro_z": 0.4}
    inputs = vlo_inputs(family_z=families, pctl=92.0, sigma=0.08, confidence="MEDIUM")
    record = equity_record(RUN, MODEL, inputs, promoted_policy)
    payload = predictions_payload(
        run_date=RUN,
        model=MODEL,
        run_status="NO_TRADE",
        data_mode="DELAYED",
        regime="BULL",
        predictions=[record],
    )
    assert validate_payload(payload, promoted_policy) == []
    late = mutate(payload, "predictions.0.days_to_earnings", 20)
    assert validate_payload(late, promoted_policy) == []
    soon = mutate(payload, "predictions.0.days_to_earnings", 6)
    assert any(
        "confidence MEDIUM exceeds ceiling LOW" in f
        for f in validate_payload(soon, promoted_policy)
    )


@real_data
def test_the_latest_published_ledger_is_not_yet_v1(policy: Policy) -> None:
    """Legacy ledgers are never gated on v1; this is how far the newest is."""
    path = OUTPUT_DIR / f"{MODEL}-{RUN}" / "15_predictions.json"
    legacy = json.loads(path.read_text(encoding="utf-8"))
    findings = validate_payload(dict(legacy, schema_version=1), policy)
    assert any("kelly_025 is not v1" in f for f in findings)
    assert any("missing mu_prior" in f for f in findings)
    assert not any("run_status" in f for f in findings)  # already one status key


def test_json_schema_agrees_on_shape(payload: dict[str, Any], policy: Policy) -> None:
    jsonschema = pytest.importorskip("jsonschema")
    document = json_schema(policy)
    jsonschema.Draft202012Validator.check_schema(document)
    validator = jsonschema.Draft202012Validator(document)
    assert list(validator.iter_errors(payload)) == []
    for path, value in (
        (f"{METRICS}.kelly_025", 0.05),
        ("final_status", "NO_TRADE"),
        ("predictions.1.benchmark", "SPY"),
        ("settlements.0.settled_on", RUN),
    ):
        assert list(validator.iter_errors(mutate(payload, path, value))), path
