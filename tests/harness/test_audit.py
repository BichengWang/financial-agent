from __future__ import annotations

import copy
import math
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
from financial_agent.harness.gates import investability
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


def test_an_int_too_large_for_a_float_is_not_a_number(
    policy: Policy, vlo_record: dict[str, Any]
) -> None:
    huge, text = dict(vlo_record, mu=10**400), dict(vlo_record, mu="n/a")
    assert audit_record(huge, policy) == audit_record(text, policy)
    assert investability(huge, policy) == investability(text, policy)


@pytest.mark.parametrize(
    ("sigma", "lineage", "kelly_failure"),
    [
        # (1e-160) ** 2 is 1e-320, tiny but not 0.0: -0.06 / 1e-320 is -inf.
        (
            1e-160,
            ["lineage.kelly_raw_method"],
            "fractional Kelly <= 0 blocks investable status",
        ),
        # (1e-200) ** 2 underflows to 0.0 and (1e200) ** 2 overflows.
        (1e-200, [], "mu/sigma missing: unsettleable"),
        (1e200, [], "mu/sigma missing: unsettleable"),
    ],
    ids=["1e-160", "1e-200", "1e200"],
)
def test_mu_over_sigma2_needs_sigma_squared_to_be_a_nonzero_float(
    policy: Policy,
    vlo_record: dict[str, Any],
    sigma: float,
    lineage: list[str],
    kelly_failure: str,
) -> None:
    record = dict(vlo_record, mu=-0.06, sigma=sigma)
    result = audit_record(record, policy)
    kelly_checks = [c for c in result.checks if "kelly" in c]
    assert kelly_checks == ["semantics.kelly_025", "units.kelly_decimal", *lineage]
    assert result.kelly_convention == "UNCAPPED_DECIMAL"
    failures = investability(record, policy)
    assert [f for f in failures if "Kelly" in f or "mu/sigma" in f] == [kelly_failure]


@pytest.mark.parametrize(
    ("sigma", "kelly_checks", "kelly_failures"),
    [
        (math.nan, [], []),  # nan > 0 is false, but so is nan <= 0
        (
            math.inf,
            ["semantics.kelly_025", "units.kelly_decimal", "lineage.kelly_raw_method"],
            ["fractional Kelly <= 0 blocks investable status"],
        ),
    ],
    ids=["nan", "inf"],
)
def test_a_nan_or_inf_sigma_keeps_its_kelly_results(
    policy: Policy,
    vlo_record: dict[str, Any],
    sigma: float,
    kelly_checks: list[str],
    kelly_failures: list[str],
) -> None:
    record = dict(vlo_record, mu=-0.06, sigma=sigma)
    checks = [c for c in audit_record(record, policy).checks if "kelly" in c]
    assert checks == kelly_checks
    failures = investability(record, policy)
    assert [f for f in failures if "Kelly" in f or "mu/sigma" in f] == kelly_failures


@pytest.mark.parametrize("sigma", [1e-200, 1e200])
def test_a_stored_kelly_gate_needs_no_mu_over_sigma2(
    policy: Policy, vlo_record: dict[str, Any], sigma: float
) -> None:
    record = copy.deepcopy(dict(vlo_record, sigma=sigma))
    record["score_explainability"]["metrics"]["kelly_gate"] = "PENALTY"
    assert [f for f in investability(record, policy) if "mu/sigma" in f] == []


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
