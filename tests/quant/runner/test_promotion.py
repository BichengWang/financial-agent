"""Live grants require every independent gate, not just explicit opt-in."""

from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import pytest

from financial_agent.quant.execution import Journal
from financial_agent.quant.runner import PromotionError, TradingConfig, authorize_live
from financial_agent.quant.validation import (
    Check,
    PromotionPolicy,
    PromotionReport,
    write_certificate,
)


@pytest.fixture
def config(config: TradingConfig) -> TradingConfig:
    return replace(config, broker_kind="alpaca")


def certificate(config: TradingConfig, tmp_path: Path) -> Path:
    report = PromotionReport(
        config.strategy_name,
        config.strategy_params,
        (config.strategy_params,),
        True,
        [Check("fixture", 1, 1, True, "passed")],
        {},
        "a" * 64,
        "2019-01-02",
        "2020-06-05",
        PromotionPolicy.load(),
    )
    return write_certificate(report, tmp_path / "certificate.json")


def paper_evidence(config: TradingConfig, path: Path, count: int = 20) -> Journal:
    journal = Journal(path)
    for i in range(count):
        day = (date(2020, 6, 1) + timedelta(days=i)).isoformat()
        journal.append(
            "session_outcome",
            {
                "session": day,
                "status": "TRADED",
                "mode": "paper",
                "broker_kind": "alpaca",
                "strategy": config.strategy_name,
                "params": config.strategy_params,
                "dry_run": False,
                "reconciliation_breaks": 0,
            },
        )
        journal.append(
            "fill",
            {
                "session": day,
                "client_order_id": f"id-{i}",
                "symbol": "SPY",
                "side": "buy",
                "qty": 1,
                "price": 100.05,
                "reference_price": 100,
                "broker_kind": "alpaca",
                "commission": 0,
            },
        )
    return journal


def rewrite_certificate(path: Path, updates: dict[str, Any]) -> None:
    payload = json.loads(path.read_text())
    payload.update(updates)
    payload.pop("hash")
    payload["hash"] = sha256(
        json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode()
    ).hexdigest()
    path.write_text(json.dumps(payload))


def test_all_gates_pass_and_contract_aliases(
    config: TradingConfig, tmp_path: Path
) -> None:
    cert = certificate(config, tmp_path)
    paper = paper_evidence(config, tmp_path / "journal.jsonl")
    now = datetime.now(timezone.utc)
    grant = authorize_live(
        config,
        certificate_path=cert,
        paper_journal_path=paper.path,
        environ={"FA_QUANT_ALLOW_LIVE": "1"},
        now=now,
    )
    assert grant.is_valid(now)
    assert grant.strategy == config.strategy_name
    assert not grant.is_valid(now + timedelta(minutes=15))
    assert (
        authorize_live(
            config,
            certificate=cert,
            journal=paper,
            environ={"FA_QUANT_ALLOW_LIVE": "1"},
            now=now,
        )
        == grant
    )


def test_aggregates_unmet_conditions(config: TradingConfig, tmp_path: Path) -> None:
    cert = certificate(config, tmp_path)
    rewrite_certificate(
        cert,
        {
            "strategy": "wrong",
            "params": {},
            "passed": False,
            "created_at": (datetime.now(timezone.utc) - timedelta(days=91)).isoformat(),
        },
    )
    paper = paper_evidence(config, tmp_path / "paper.jsonl", 1)
    paper.append(
        "session_outcome",
        {
            "session": "2020-06-02",
            "status": "HALTED",
            "mode": "paper",
            "broker_kind": "alpaca",
            "strategy": config.strategy_name,
            "params": config.strategy_params,
            "reconciliation_breaks": 1,
        },
    )
    paper.append(
        "fill",
        {
            "session": "2020-06-02",
            "price": 102,
            "reference_price": 100,
            "broker_kind": "alpaca",
        },
    )
    with pytest.raises(PromotionError) as caught:
        authorize_live(
            config, certificate_path=cert, paper_journal_path=paper.path, environ={}
        )
    reasons = caught.value.reasons
    for fragment in (
        "FA_QUANT",
        "older",
        "did not pass",
        "strategy mismatch",
        "params mismatch",
        "paper sessions",
        "HALTED",
        "reconciliation",
        "slippage",
    ):
        assert any(fragment in r for r in reasons), reasons


@pytest.mark.parametrize(
    "variation", ["reruns", "dry_runs", "other_strategy", "bad_chain"]
)
def test_non_evidence_cannot_promote(
    config: TradingConfig, tmp_path: Path, variation: str
) -> None:
    cert = certificate(config, tmp_path)
    paper = paper_evidence(config, tmp_path / "paper.jsonl", 19)
    payload = dict(paper.events(["session_outcome"])[-1].payload)
    if variation == "dry_runs":
        payload.update(session="2020-07-01", dry_run=True)
    elif variation == "other_strategy":
        payload.update(session="2020-07-01", strategy="other")
    paper.append("session_outcome", payload)
    if variation == "bad_chain":
        paper.path.write_text(paper.path.read_text() + "{}\n")
    with pytest.raises(PromotionError):
        authorize_live(
            config,
            certificate_path=cert,
            paper_journal_path=paper.path,
            environ={"FA_QUANT_ALLOW_LIVE": "1"},
        )


def test_halt_cannot_be_erased_by_successful_retry(
    config: TradingConfig, tmp_path: Path
) -> None:
    cert = certificate(config, tmp_path)
    paper = paper_evidence(config, tmp_path / "paper.jsonl", 21)
    last = dict(paper.events(["session_outcome"])[-1].payload)
    paper.append("session_outcome", {**last, "status": "HALTED"})
    paper.append("session_outcome", last)
    with pytest.raises(PromotionError, match="HALTED"):
        authorize_live(
            config,
            certificate_path=cert,
            paper_journal_path=paper.path,
            environ={"FA_QUANT_ALLOW_LIVE": "1"},
        )


def test_zero_cost_model_and_invalid_fill_fail_closed(
    config: TradingConfig, tmp_path: Path
) -> None:
    from financial_agent.quant.backtest import CostModel

    zero = replace(config, backtest=replace(config.backtest, costs=CostModel.zero()))
    cert = certificate(zero, tmp_path)
    paper = paper_evidence(zero, tmp_path / "paper.jsonl")
    with pytest.raises(PromotionError, match="slippage"):
        authorize_live(
            zero,
            certificate_path=cert,
            paper_journal_path=paper.path,
            environ={"FA_QUANT_ALLOW_LIVE": "1"},
        )
    paper.append(
        "fill",
        {
            "session": "2020-06-20",
            "price": 0,
            "reference_price": 0,
            "broker_kind": "alpaca",
        },
    )
    with pytest.raises(PromotionError, match="invalid"):
        authorize_live(
            config,
            certificate_path=cert,
            paper_journal_path=paper.path,
            environ={"FA_QUANT_ALLOW_LIVE": "1"},
        )


def test_status_reports_authorize_live_reasons_without_broker_or_grant(
    config: TradingConfig, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from financial_agent.quant.execution import AlpacaBroker
    from financial_agent.quant.runner import render_status, status_summary

    def no_broker(*args: Any, **kwargs: Any) -> None:
        raise AssertionError("status must not construct a broker")

    monkeypatch.setattr(AlpacaBroker, "__init__", no_broker)
    cert = certificate(config, tmp_path)
    rewrite_certificate(cert, {"params": {**config.strategy_params, "max_weight": 0.2}})
    config = replace(config, certificate_path=cert)
    config.state_dir.mkdir(parents=True)
    paper = paper_evidence(config, config.state_dir / "journal.jsonl", 19)
    outcome = dict(paper.events(["session_outcome"])[-1].payload)
    paper.append("session_outcome", {**outcome, "session": "2020-06-20"})
    paper.append(
        "session_outcome", {**outcome, "session": "2020-06-20", "status": "HALTED"}
    )
    paper.append(
        "fill",
        {
            "session": "2020-06-20",
            "client_order_id": "late",
            "symbol": "QQQ",
            "price": 102,
            "reference_price": 100,
            "broker_kind": "alpaca",
        },
    )
    before = paper.path.read_bytes()
    summary = status_summary(config)
    with pytest.raises(PromotionError) as caught:
        authorize_live(
            config, paper_journal_path=paper.path, environ={"FA_QUANT_ALLOW_LIVE": "1"}
        )
    readiness = summary["live_readiness"]
    assert readiness["reasons"] == caught.value.reasons
    assert not readiness["ready"]
    assert paper.path.read_bytes() == before
    text = render_status(summary)
    for line in (
        "Live readiness: NOT READY",
        "19 clean of 20 required; window 2020-06-01..2020-06-20: 1 halted (max 0)",
        "worst QQQ 2020-06-20 200.0 bps",
        "Certificate: passed, identity MISMATCH, age 0.0 of 90 days",
        "Unmet: certificate params mismatch",
    ):
        assert line in text, text


def test_cli_status_shows_ready_broker_paper_evidence(
    config_path: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from financial_agent.quant.__main__ import main

    config_path.write_text(
        config_path.read_text().replace('kind = "paper"', 'kind = "alpaca"')
        + '[promotion]\ncertificate = "certificate.json"\n'
    )
    config = TradingConfig.load(config_path)
    certificate(config, tmp_path)
    config.state_dir.mkdir(parents=True)
    paper_evidence(config, config.state_dir / "journal.jsonl")
    assert main(["status", "--config", str(config_path), "--json"]) == 0
    readiness = json.loads(capsys.readouterr().out)["live_readiness"]
    assert readiness["ready"] and readiness["reasons"] == []
    assert readiness["clean_sessions"] == 20 and len(readiness["fills"]) == 20
    assert main(["status", "--config", str(config_path)]) == 0
    assert "Live readiness: READY" in capsys.readouterr().out
    local = config_path.read_text().replace('kind = "alpaca"', 'kind = "paper"')
    config_path.write_text(local)
    assert main(["status", "--config", str(config_path), "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["live_readiness"] is None
