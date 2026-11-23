from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, market_forecast, real_data, stub_package

from financial_agent.harness.handlers import reflection_handler
from financial_agent.harness.runner import RunContext, default_handlers, run
from financial_agent.harness.lifecycle import RunState


def context(output_dir: Path, model: str, date: str) -> RunContext:
    return RunContext(model, date, output_dir / f"{model}-{date}")


def test_reflection_on_an_empty_history(tmp_path: Path) -> None:
    result = reflection_handler(context(tmp_path, "m", "2026-09-03"))
    assert result.halt is None
    assert "0 canonical EQUITY_ALPHA settlements" in result.note


YEAR_1_SETTLEMENT = {
    "model": "claude-opus-5",
    "vintage": "2026-08-01",
    "ticker": "ABT",
    "type": "EQUITY_ALPHA",
    "target_date": "0001-01-01",  # a holiday with no earlier close
    "settle_price": 112.47,
    "settle_price_date": "2026-08-28",
    "settlement_price_tag": "HISTORICAL",
    "timing_flag": "WEEKEND_TARGET",
    "settled_at": "2026-09-02T19:29:02-04:00",
}


@pytest.mark.parametrize(
    ("prediction", "settlements"),
    [({"mu": 10**400}, []), ({}, [YEAR_1_SETTLEMENT])],
    ids=["mu-10**400", "target-0001-01-01"],
)
def test_reflection_reads_an_earlier_ledger_with_extreme_values(
    tmp_path: Path, prediction: dict[str, Any], settlements: list[dict[str, Any]]
) -> None:
    earlier = dict(market_forecast("SPY", 773.17), run_date="2026-09-02", **prediction)
    payload = {"run_date": "2026-09-02", "predictions": [earlier]}
    stub_package(
        tmp_path / "claude-opus-5-2026-09-02", dict(payload, settlements=settlements)
    )
    report = run("claude-opus-5", "2026-09-03", tmp_path, default_handlers())
    assert report.halt_reason == "no handler for DATA_OK"  # REFLECTION passed


def test_registered_handlers() -> None:
    assert set(default_handlers()) == {RunState.PRECHECK, RunState.REFLECTION}


@real_data
def test_reflection_ignores_this_runs_own_and_later_packages() -> None:
    own = context(OUTPUT_DIR, "claude-opus-5", "2026-09-03")
    result = reflection_handler(own)
    assert result.halt is None
    # Pre-run state: 00_run_manifest.md of this package reports 111 of 113 due
    # keys settled and eff_n 2 -> 3, so the run's own rows must be excluded.
    assert "eff_n 2" in result.note and "113 due" in result.note
    earlier = reflection_handler(context(OUTPUT_DIR, "x", "2026-08-10"))
    assert earlier.note != result.note
