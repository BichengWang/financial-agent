"""Evidence gates and portable certificates fail closed on missing evidence."""

from dataclasses import replace
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from financial_agent.quant.backtest import BacktestConfig
from financial_agent.quant.data import synthetic_market
from financial_agent.quant.validation import (
    CertificateError,
    Check,
    PromotionPolicy,
    PromotionReport,
    evaluate_promotion,
    verify_certificate,
    write_certificate,
)


def loaded_policy(tmp_path: Path) -> PromotionPolicy:
    path = tmp_path / "policy.toml"
    path.write_text(
        "[promotion]\nmin_oos_sessions = 300\ntrain_sessions = 126\n"
        "test_sessions = 63\nembargo_sessions = 5\npbo_splits = 8\n"
        "[risk]\nmax_weight = 0.3\n",
        encoding="utf-8",
    )
    return PromotionPolicy.load(path)


def test_gate_planted_edge_clears_more_policy_checks_than_noise(tmp_path: Path) -> None:
    policy = loaded_policy(tmp_path)
    grid = [
        {
            "lookbacks": [3, 10],
            "cov_lookback": 21,
            "target_vol": 0.08,
            "max_weight": 0.5,
        },
        {
            "lookbacks": [3, 10],
            "cov_lookback": 21,
            "target_vol": 0.12,
            "max_weight": 0.5,
        },
    ]
    config = BacktestConfig(rebalance="weekly", fractional_shares=True)
    edge = evaluate_promotion(
        "trend_vol_target",
        grid,
        synthetic_market(
            ["A", "B"], 650, seed=15, annual_drift=0.4, autocorrelation=0.85
        ),
        config,
        policy,
    )
    noise = evaluate_promotion(
        "trend_vol_target",
        grid,
        synthetic_market(["A", "B"], 650, seed=15, annual_drift=0.0),
        config,
        policy,
    )
    assert sum(c.passed for c in edge.checks) > sum(c.passed for c in noise.checks)
    threshold_fields = {
        "oos_sessions": "min_oos_sessions",
        "oos_sharpe": "min_oos_sharpe",
        "dsr": "min_dsr",
        "pbo": "max_pbo",
        "oos_drawdown": "max_oos_drawdown",
        "sharpe_2x_costs": "min_sharpe_2x_costs",
        "sharpe_delay_1": "min_sharpe_delay_1",
        "bootstrap_sharpe_p05": "min_bootstrap_sharpe_p05",
    }
    assert len(edge.checks) == 8
    for report in (edge, noise):
        assert report.passed == all(c.passed for c in report.checks)
        for check in report.checks:
            assert check.threshold == getattr(policy, threshold_fields[check.name])
            assert check.detail
        assert report.data_fingerprint
        assert report.selected_params
    path = write_certificate(edge, tmp_path / "edge.json")
    certificate = verify_certificate(path, require_passed=False)
    assert certificate.passed == edge.passed
    assert (
        certificate.policy_sha256
        == hashlib.sha256((tmp_path / "policy.toml").read_bytes()).hexdigest()
    )


def test_insufficient_data_records_failures_and_serializes_nulls(
    tmp_path: Path,
) -> None:
    report = evaluate_promotion(
        "trend_vol_target",
        [{"target_vol": 0.08}, {"target_vol": 0.12}],
        synthetic_market(["SPY"], 20, seed=0),
        BacktestConfig(),
        PromotionPolicy.load(),
    )
    assert not report.passed
    assert all(not c.passed for c in report.checks)
    assert "insufficient" in report.checks[0].detail
    path = write_certificate(report, tmp_path / "failed.json")
    assert json.loads(path.read_text())["checks"][1]["value"] is None
    with pytest.raises(CertificateError, match="failed promotion"):
        verify_certificate(path)
    assert not verify_certificate(path, require_passed=False).passed


@pytest.mark.parametrize(
    "line",
    [
        "unknown = 1",
        "min_dsr = 1.1",
        "max_pbo = -0.1",
        "pbo_splits = 3",
        "train_sessions = 1",
        "min_oos_sessions = true",
        "min_oos_sharpe = inf",
        "min_oos_sharpe = -1",
    ],
)
def test_policy_rejects_unknown_illtyped_and_out_of_range(
    tmp_path: Path, line: str
) -> None:
    path = tmp_path / "bad.toml"
    path.write_text("[promotion]\n" + line)
    with pytest.raises(ValueError):
        PromotionPolicy.load(path)


def report_fixture() -> PromotionReport:
    return PromotionReport(
        "trend_vol_target",
        {"target_vol": 0.1},
        ({"target_vol": 0.1},),
        True,
        [Check("oos_sharpe", 1.0, 0.5, True, "passed")],
        {"sharpe": 1.0},
        "a" * 64,
        "2005-01-03",
        "2025-01-03",
        PromotionPolicy.load(),
    )


def test_certificate_roundtrip_canonical_hash_identity_and_expiry(
    tmp_path: Path,
) -> None:
    report = report_fixture()
    path = write_certificate(report, tmp_path / "certificate.json")
    decoded = json.loads(path.read_bytes())
    claimed = decoded.pop("hash")
    encoded = json.dumps(
        decoded,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode()
    assert claimed == hashlib.sha256(encoded).hexdigest()
    cert = verify_certificate(
        path, expected_strategy=report.strategy, expected_params=report.selected_params
    )
    assert cert.hash == claimed
    assert cert.params == report.selected_params
    created = datetime.fromisoformat(cert.created_at)
    assert created.utcoffset() == timedelta(0)
    verify_certificate(path, now=created + timedelta(days=90))
    with pytest.raises(CertificateError, match="expired"):
        verify_certificate(path, now=created + timedelta(days=90, seconds=1))
    with pytest.raises(CertificateError, match="strategy mismatch"):
        verify_certificate(path, expected_strategy="buy_and_hold")
    with pytest.raises(CertificateError, match="params mismatch"):
        verify_certificate(path, expected_params={"target_vol": 0.2})
    with pytest.raises(CertificateError, match="future"):
        verify_certificate(path, now=created - timedelta(seconds=1))
    with pytest.raises(CertificateError, match="timezone"):
        verify_certificate(path, now=datetime(2026, 1, 1))


@pytest.mark.parametrize(
    "field,value",
    [
        ("params", {"target_vol": 0.3}),
        ("data_fingerprint", "changed"),
        ("passed", False),
    ],
)
def test_certificate_detects_tampering(tmp_path: Path, field: str, value: Any) -> None:
    path = write_certificate(report_fixture(), tmp_path / "certificate.json")
    payload = json.loads(path.read_text())
    payload[field] = value
    path.write_text(json.dumps(payload))
    with pytest.raises(CertificateError, match="hash mismatch.*tamper"):
        verify_certificate(path)


def test_certificate_captures_loaded_policy_bytes_and_rejects_research_overrides(
    tmp_path: Path,
) -> None:
    policy = loaded_policy(tmp_path)
    expected = policy.file_sha256()
    (tmp_path / "policy.toml").write_text("[promotion]\nmin_dsr = 0.1\n")
    assert policy.file_sha256() == expected
    report = replace(report_fixture(), policy=replace(policy, min_dsr=0.8))
    with pytest.raises(ValueError, match="policy differs"):
        write_certificate(report, tmp_path / "certificate.json")


def test_certificate_rejects_malformed_json_and_bad_age_limit(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{")
    with pytest.raises(CertificateError, match="malformed"):
        verify_certificate(path)
    with pytest.raises(CertificateError, match="max_age_days"):
        verify_certificate(path, max_age_days=-1)
    report = replace(
        report_fixture(),
        passed=False,
        checks=[Check("oos_sharpe", 0, 0.5, False, "low Sharpe")],
    )
    path = write_certificate(report, path)
    with pytest.raises(CertificateError, match="failed promotion"):
        verify_certificate(path, now=datetime.now(timezone.utc))
