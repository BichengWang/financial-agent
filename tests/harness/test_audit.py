from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from conftest import (
    OUTPUT_DIR,
    build_package,
    malformed_package,
    market_forecast,
    real_data,
)

from financial_agent.harness.audit import (
    Finding,
    audit_output_dir,
    audit_record,
    kelly_convention,
)
from financial_agent.harness.policy import Policy


def failed_checks(record: dict[str, Any], policy: Policy) -> dict[str, str]:
    return {f.check: f.detail for f in audit_record(record, policy).findings}


def test_published_record_is_clean(policy: Policy, vlo_record: dict[str, Any]) -> None:
    result = audit_record(vlo_record, policy)
    assert result.findings == []
    assert {"formula.ci70", "formula.adj_score", "formula.mu_band"} <= set(
        result.checks
    )
    assert result.kelly_convention == "UNCAPPED_DECIMAL"


def test_percentile_stored_as_adj_score(
    policy: Policy, vlo_record: dict[str, Any]
) -> None:
    fails = failed_checks(dict(vlo_record, adj_score=97.1), policy)
    assert "percentile rank" in fails["formula.adj_score"]


def test_missing_dq_multiplier(policy: Policy, vlo_record: dict[str, Any]) -> None:
    fails = failed_checks(dict(vlo_record, adj_score=0.465898), policy)
    assert "DQ multiplier not applied" in fails["formula.adj_score"]


def test_percent_units_are_drift_not_formula_errors(
    policy: Policy, vlo_record: dict[str, Any]
) -> None:
    record = dict(vlo_record)
    explain = dict(record["score_explainability"])
    explain["metrics"] = dict(explain["metrics"], var95=-7.9186)
    record["score_explainability"] = explain
    findings = audit_record(record, policy).findings
    assert [(f.check, f.severity) for f in findings] == [
        ("units.var95_decimal", "drift")
    ]


def test_mu_outside_calibration_band(
    policy: Policy, vlo_record: dict[str, Any]
) -> None:
    # claude-fable-5-2026-07-01 UNH: pctl 87.3 (prior +4%) published mu +1%
    fails = failed_checks(dict(vlo_record, pctl=87.3, mu=0.01), policy)
    assert "formula.mu_band" in fails


def test_market_forecast_shape(policy: Policy) -> None:
    assert audit_record(market_forecast("SPY", 773.17), policy).findings == []
    bad = dict(market_forecast("SPY", 773.17), benchmark="SPY")
    assert "market_forecast.shape" in failed_checks(bad, policy)


@pytest.mark.parametrize(
    ("raw", "stored", "convention"),
    [
        (8.431961, 2.10799, "UNCAPPED_DECIMAL"),  # claude-opus-5
        (2.0327, 0.05, "CAPPED_DECIMAL"),  # claude-fable-5, gpt-5
        (527.94, 5.0, "CAPPED_PERCENT"),  # claude-fable-5-2026-07-21
        (10.306, 5.0, "CAPPED_MIXED_UNITS"),  # claude-opus-4-8-2026-06-30
        (1.0, 0.9, "UNRECOGNIZED"),
    ],
)
def test_kelly_conventions_seen_in_history(
    raw: float, stored: float, convention: str
) -> None:
    assert kelly_convention(raw, stored, cap=0.05) == convention


def test_malformed_ledger_is_one_error_and_the_audit_goes_on(
    tmp_path: Path, policy: Policy, malformed_ledger: tuple[bytes, str]
) -> None:
    ledger, failure = malformed_ledger
    malformed_package(tmp_path / "claude-opus-5-2026-09-02", ledger)
    build_package(tmp_path, [market_forecast("SPY", 773.17)])
    report = audit_output_dir(tmp_path, policy)
    assert (report.packages, report.records) == (2, 1)
    assert report.failed("package.ledger") == [
        Finding("package.ledger", "error", "claude-opus-5-2026-09-02", "-", failure)
    ]
    row = "| package.ledger | error | 1 | 1 | 100.0 | 1 | claude-opus-5 |"
    assert row in report.to_markdown()


@real_data
def test_history_audit_pinned_to_2026_09_03(policy: Policy) -> None:
    """Spike findings, pinned so later runs cannot move them.

    Published packages are immutable, so these counts should never change.
    """
    report = audit_output_dir(OUTPUT_DIR, policy, as_of="2026-09-03")
    assert (report.packages, report.records, report.settlement_rows) == (95, 1877, 2022)
    assert len(report.packages_without_ledger) == 12
    adj = report.failed("formula.adj_score")
    assert (len(adj), len({f.package for f in adj})) == (234, 16)
    assert len(report.failed("units.var95_decimal")) == 106
    for check in (
        "formula.ci70",
        "formula.var95",
        "formula.composite_z",
        "schema.enums",
    ):
        assert report.failed(check) == [], check
    assert len(report.settlement_keysets) == 35
    assert set(report.kelly_by_model["claude-opus-5"]) == {
        "CAPPED_DECIMAL",
        "UNCAPPED_DECIMAL",
    }
