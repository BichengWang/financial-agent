from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from conftest import market_forecast

from financial_agent.harness.gates import ALWAYS_ARTIFACTS
from financial_agent.harness.lifecycle import RunState, RunStatus
from financial_agent.harness.runner import (
    PIPELINE,
    Handler,
    RunContext,
    RunLock,
    RunLocked,
    StageResult,
    run,
)

MODEL, DATE = "test-model", "2026-09-03"


def noop(_: RunContext) -> StageResult:
    return StageResult("ok")


def write_package(context: RunContext) -> StageResult:
    context.package_dir.mkdir(parents=True)
    for name in ALWAYS_ARTIFACTS:
        (context.package_dir / name).write_text(f"# {name}\n", encoding="utf-8")
    etfs = [market_forecast(t, 100.0) for t in ("SPY", "QQQ", "SOXX")]
    payload: dict[str, Any] = {"predictions": etfs, "settlements": []}
    (context.package_dir / "15_predictions.json").write_text(
        json.dumps(payload), encoding="utf-8"
    )
    return StageResult("wrote package")


def handlers(status: RunStatus | None = RunStatus.NO_TRADE) -> dict[RunState, Handler]:
    table: dict[RunState, Handler] = {state: noop for state in PIPELINE}
    table[RunState.PORTFOLIO_DRAFT] = write_package
    table[RunState.RISK_REVIEW] = lambda _: StageResult("reviewed", status=status)
    return table


def test_full_run_publishes_through_the_gate(tmp_path: Path) -> None:
    report = run(MODEL, DATE, tmp_path, handlers())
    assert report.published and report.gate_failures == []
    assert report.lifecycle.status is RunStatus.NO_TRADE
    assert report.lifecycle.transcript() == (
        "PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> "
        "PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> EVOLUTION_REVIEW"
    )
    assert not list((tmp_path / ".locks").iterdir())


def test_missing_handler_halts_instead_of_skipping(tmp_path: Path) -> None:
    table = handlers()
    del table[RunState.SCORED]
    report = run(MODEL, DATE, tmp_path, table)
    assert not report.published
    assert report.halt_reason == "no handler for SCORED"
    assert report.lifecycle.state is RunState.HALTED
    assert not (tmp_path / f"{MODEL}-{DATE}").exists()


def test_handler_exception_and_explicit_halt_stop_the_run(tmp_path: Path) -> None:
    def boom(_: RunContext) -> StageResult:
        raise ValueError("vendor 500")

    table = handlers()
    table[RunState.DATA_OK] = boom
    assert (
        "DATA_OK handler failed: ValueError: vendor 500"
        == run(MODEL, DATE, tmp_path, table).halt_reason
    )

    table = handlers()
    table[RunState.REFLECTION] = lambda _: StageResult(halt="stale baseline")
    assert run(MODEL, DATE, tmp_path, table).halt_reason == "stale baseline"


def test_failed_publish_gate_halts_and_never_publishes(tmp_path: Path) -> None:
    table = handlers()
    table[RunState.PORTFOLIO_DRAFT] = noop  # the package is never written
    report = run(MODEL, DATE, tmp_path, table)
    assert not report.published
    assert report.gate_failures == [
        f"package directory {tmp_path / f'{MODEL}-{DATE}'} was never created"
    ]
    assert report.halt_reason is not None
    assert report.halt_reason.startswith("publish gate failed")


def test_risk_review_must_return_a_publishable_status(tmp_path: Path) -> None:
    for index, status in enumerate((None, RunStatus.HALTED)):
        report = run(MODEL, DATE, tmp_path / str(index), handlers(status))
        assert (
            report.halt_reason == "RISK_REVIEW handler returned no publishable status"
        )


def test_lock_blocks_a_second_run_and_is_released_on_exit(tmp_path: Path) -> None:
    with RunLock(tmp_path, f"{MODEL}-{DATE}"):
        with pytest.raises(RunLocked, match="in progress or crashed"):
            run(MODEL, DATE, tmp_path, handlers())
    assert run(MODEL, DATE, tmp_path, handlers()).published


def test_default_cli_run_halts_with_no_side_effects(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from financial_agent.harness.__main__ import main

    code = main(
        ["run", "--model", MODEL, "--date", DATE, "--output-dir", str(tmp_path)]
    )
    out = capsys.readouterr().out
    assert code == 1 and "HALTED: no handler for PRECHECK" in out
    assert [p.name for p in tmp_path.iterdir()] == [".locks"]
