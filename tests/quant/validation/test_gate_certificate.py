"""Evidence gates and portable certificates fail closed on missing evidence."""

from dataclasses import replace
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import pytest

from financial_agent.quant.backtest import BacktestConfig
from financial_agent.quant.data import synthetic_market
from financial_agent.quant.strategies import build_strategy
from financial_agent.quant.validation import (
    CertificateError,
    Check,
    PromotionPolicy,
    PromotionReport,
    check_disclosed_trials,
    deflated_sharpe_ratio,
    evaluate_promotion,
    verify_certificate,
    walk_forward,
    write_certificate,
)
from financial_agent.quant.validation.walkforward import annual_sharpe


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
        "prob_oos_loss": "max_prob_oos_loss",
        "oos_drawdown": "max_oos_drawdown",
        "sharpe_2x_costs": "min_sharpe_2x_costs",
        "sharpe_delay_1": "min_sharpe_delay_1",
        "bootstrap_sharpe_p05": "min_bootstrap_sharpe_p05",
    }
    assert len(edge.checks) == 8
    assert next(c for c in edge.checks if c.name == "prob_oos_loss").passed
    assert not next(c for c in noise.checks if c.name == "prob_oos_loss").passed
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
    assert certificate.diagnostics == edge.diagnostics
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


def test_disclosed_trials_deflate_a_frozen_variant_by_every_trial(
    tmp_path: Path,
) -> None:
    policy = loaded_policy(tmp_path)
    trials = [
        {"lookbacks": lb, "cov_lookback": 21, "target_vol": 0.1, "max_weight": 0.5}
        for lb in ([3, 10], [5, 20], [10, 40], [2, 5])
    ]
    frozen = trials[0]
    # A modest edge keeps DSR below saturation at 1.0.
    data = synthetic_market(
        ["A", "B"], 650, seed=15, annual_drift=0.1, autocorrelation=0.3
    )
    config = BacktestConfig(rebalance="weekly", fractional_shares=True)

    def walk(grid: list[dict[str, Any]]) -> Any:
        return walk_forward(
            lambda p: build_strategy("trend_vol_target", p),
            grid,
            data,
            config,
            train_sessions=policy.train_sessions,
            test_sessions=policy.test_sessions,
            embargo_sessions=policy.embargo_sessions,
        )

    searched = walk(trials).variant_returns
    scores = [annual_sharpe(searched[i].to_numpy()) / math.sqrt(252) for i in range(4)]
    mean = sum(scores) / 4
    expected = deflated_sharpe_ratio(
        walk([frozen]).oos_returns.to_numpy(),
        n_trials=4,
        trials_sharpe_variance=sum((s - mean) ** 2 for s in scores) / 3,
    )
    disclosed = evaluate_promotion(
        "trend_vol_target", [frozen], data, config, policy, disclosed_trials=trials
    )
    alone = evaluate_promotion("trend_vol_target", [frozen], data, config, policy)

    def dsr(report: PromotionReport) -> float:
        return next(c.value for c in report.checks if c.name == "dsr")

    assert dsr(disclosed) == pytest.approx(expected)
    # Without the disclosure a lone variant faces a zero benchmark.
    assert dsr(disclosed) < dsr(alone)
    assert (
        disclosed.selected_params == build_strategy("trend_vol_target", frozen).params()
    )
    assert "n_trials" not in alone.diagnostics
    certificate = verify_certificate(
        write_certificate(disclosed, tmp_path / "frozen.json"), require_passed=False
    )
    assert certificate.grid_size == 1
    assert certificate.diagnostics["n_trials"] == 4
    assert certificate.diagnostics["trial_sharpe_variance"] == pytest.approx(
        sum((s - mean) ** 2 for s in scores) / 3
    )


@pytest.mark.parametrize(
    ("trials", "match"),
    [
        ([{"target_vol": 0.08}], "every grid variant"),
        ([{"target_vol": 0.12}, {"target_vol": 0.12, "max_weight": 0.3}], "duplicate"),
    ],
)
def test_disclosure_must_list_each_grid_variant_once(
    trials: list[dict[str, Any]], match: str
) -> None:
    with pytest.raises(ValueError, match=match):
        check_disclosed_trials("trend_vol_target", [{"target_vol": 0.12}], trials)
    # Variants compare with defaults filled in.
    check_disclosed_trials(
        "trend_vol_target",
        [{"target_vol": 0.12}],
        [{"target_vol": 0.12, "max_weight": 0.3}, {"target_vol": 0.08}],
    )


@pytest.mark.parametrize(
    "line",
    [
        "unknown = 1",
        "min_dsr = 1.1",
        "max_prob_oos_loss = -0.1",
        "pbo_splits = 3",
        "train_sessions = 1",
        "min_oos_sessions = true",
        "min_oos_sharpe = inf",
        "min_oos_sharpe = -1",
        "max_pbo = 0.2",
        "max_prob_oos_loss = 1.1",
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
        {"pbo": 0.5, "n_combinations": 70.0, "degradation_slope": -0.8},
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
    assert cert.diagnostics == report.diagnostics
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
        ("diagnostics", {"pbo": 0.0}),
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


def test_certificate_undefined_diagnostics_roundtrip_as_null(tmp_path: Path) -> None:
    import math

    report = replace(
        report_fixture(),
        diagnostics={"pbo": 0.5, "degradation_slope": float("nan")},
    )
    path = write_certificate(report, tmp_path / "undefined.json")
    assert json.loads(path.read_text())["diagnostics"]["degradation_slope"] is None
    cert = verify_certificate(path)
    assert cert.diagnostics["pbo"] == 0.5
    assert math.isnan(cert.diagnostics["degradation_slope"])


def test_single_registered_variant_can_pass_and_noise_fails(tmp_path: Path) -> None:
    import math

    policy = loaded_policy(tmp_path)
    grid = [{"weights": {"SPY": 1.0}}]
    config = BacktestConfig(cash_buffer=0.02)
    edge = evaluate_promotion(
        "buy_and_hold",
        grid,
        synthetic_market(["SPY"], 650, seed=15, annual_drift=0.4, annual_vol=0.08),
        config,
        policy,
    )
    noise = evaluate_promotion(
        "buy_and_hold",
        grid,
        synthetic_market(["SPY"], 650, seed=15, annual_drift=0.0),
        config,
        policy,
    )
    assert edge.passed, [c.detail for c in edge.checks]
    assert not noise.passed
    assert next(c for c in edge.checks if c.name == "prob_oos_loss").value == 0
    loss = next(c for c in noise.checks if c.name == "prob_oos_loss")
    assert loss.value > policy.max_prob_oos_loss and not loss.passed
    assert math.isnan(edge.diagnostics["pbo"])
    assert math.isnan(edge.diagnostics["degradation_slope"])
    path = write_certificate(edge, tmp_path / "single.json")
    certificate = verify_certificate(path)
    assert certificate.passed and certificate.grid_size == 1
    assert math.isnan(certificate.diagnostics["pbo"])
