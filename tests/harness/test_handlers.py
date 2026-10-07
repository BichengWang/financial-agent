from __future__ import annotations

from pathlib import Path

from conftest import OUTPUT_DIR, real_data

from financial_agent.harness.handlers import reflection_handler
from financial_agent.harness.runner import RunContext, default_handlers
from financial_agent.harness.lifecycle import RunState


def context(output_dir: Path, model: str, date: str) -> RunContext:
    return RunContext(model, date, output_dir / f"{model}-{date}")


def test_reflection_on_an_empty_history(tmp_path: Path) -> None:
    result = reflection_handler(context(tmp_path, "m", "2026-09-03"))
    assert result.halt is None
    assert "0 canonical EQUITY_ALPHA settlements" in result.note


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
