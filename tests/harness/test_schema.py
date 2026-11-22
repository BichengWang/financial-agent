from __future__ import annotations

import copy
import json
import math
from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, real_data, stub_package
from test_kernels import MODEL, RUN, etf_inputs, vlo_inputs

from financial_agent.harness.audit import audit_record
from financial_agent.harness.gates import publish_gate
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
    package = stub_package(tmp_path / f"{MODEL}-{RUN}", payload)
    ledger = package / "15_predictions.json"
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


def test_v1_an_int_too_large_for_a_float_is_not_a_number(
    payload: dict[str, Any], policy: Policy
) -> None:
    huge = validate_payload(mutate(payload, "predictions.0.mu", 10**400), policy)
    assert f"predictions[0] VLO: mu={10**400} is not number" in huge


@pytest.mark.parametrize(
    ("spy_mu", "beta", "qqq"),
    [
        # ints whose product is a float: checked as before
        (
            0,
            1,
            [
                "mu_prior 0.034012 != 0.000000",
                "mu 0.019012 != mu_prior + mu_adjustment",
            ],
        ),
        # two 201-digit ints are each a number; their product is not
        (10**200, 10**200, ["QQQ beta_vs_spy x SPY mu is too large for a float"]),
    ],
    ids=["in-range", "too-large"],
)
def test_v1_checks_beta_x_spy_mu_from_int_inputs(
    payload: dict[str, Any], policy: Policy, spy_mu: int, beta: int, qqq: list[str]
) -> None:
    ledger = mutate(payload, "predictions.1.mu", spy_mu)  # SPY
    ledger = mutate(ledger, "predictions.2.beta_vs_spy", beta)  # QQQ
    findings = [f for f in validate_payload(ledger, policy) if "QQQ" in f]
    assert findings == [f"predictions[2] QQQ: {finding}" for finding in qqq]


def test_v1_reports_a_beta_scaled_mu_beyond_the_float_range(
    payload: dict[str, Any], policy: Policy
) -> None:
    # The prior 1 x 10**308 is a float; adding mu_adjustment 10**308 is not.
    ledger = mutate(payload, "predictions.1.mu", 10**308)  # SPY
    ledger = mutate(ledger, "predictions.2.beta_vs_spy", 1)  # QQQ
    ledger = mutate(ledger, "predictions.2.mu_adjustment", 10**308)
    findings = validate_payload(ledger, policy)
    assert "predictions[2] QQQ: mu 0.019012 != mu_prior + mu_adjustment" in findings


@pytest.mark.parametrize("sigma", [1e200, 1e-200])  # sigma**2 overflows; is 0.0
def test_v1_beta_adjusted_kelly_is_checked_whatever_sigma_squares_to(
    payload: dict[str, Any], policy: Policy, sigma: float
) -> None:
    # The kernel writes BETA_ADJ_TE when it is given kelly_raw.
    record = equity_record(RUN, MODEL, vlo_inputs(kelly_raw=8.431961), policy)
    record["sigma"] = sigma
    record["score_explainability"]["metrics"].update(kelly_fractional=9.0, var95=-7.92)
    payload["predictions"][0] = record
    assert validate_payload(payload, policy) == [
        "predictions[0] VLO: metrics.var95=-7.92 must be a decimal",
        "predictions[0] VLO: metrics.kelly_fractional 9.0 != 2.107990",
    ]


@pytest.mark.parametrize(
    ("sigma", "compared"),
    [
        (1e-160, True),  # sigma**2 is 1e-320: tiny, but not 0.0
        (1e-200, False),  # sigma**2 underflows to 0.0
        (1e200, False),  # sigma**2 overflows
        (10**200, False),  # sigma**2 is an int too large for a float
    ],
    ids=["1e-160", "1e-200", "1e200", "int-10**200"],
)
def test_v1_checks_kelly_raw_against_mu_over_sigma2_when_it_is_a_float(
    payload: dict[str, Any], policy: Policy, sigma: float, compared: bool
) -> None:
    # With mu 0, mu/sigma^2 is 0.0 at 1e-160 and the stored kelly_raw 8.43 is
    # wrong; 0.06 / 1e-320 would be inf, which _close accepts for any kelly_raw.
    ledger = mutate(payload, "predictions.0.mu", 0.0)
    ledger = mutate(ledger, "predictions.0.sigma", sigma)
    findings = validate_payload(ledger, policy)
    assert any("mu/sigma^2" in f for f in findings) is compared


@pytest.mark.parametrize(
    ("sigma", "fallback"),
    [(math.nan, "nan"), (math.inf, "0.000000")],
    ids=["nan", "inf"],
)
def test_v1_checks_kelly_raw_for_a_nan_or_inf_sigma(
    payload: dict[str, Any], policy: Policy, sigma: float, fallback: str
) -> None:
    ledger = mutate(payload, "predictions.0.sigma", sigma)
    assert validate_payload(ledger, policy) == [
        f"predictions[0] VLO: metrics.kelly_raw 8.43198 != mu/sigma^2 {fallback}"
    ]


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
