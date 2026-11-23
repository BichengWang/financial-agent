from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, market_forecast, real_data, stub_package
from test_schema import SETTLEMENT

from financial_agent.harness.handlers import reflection_handler, settlement_summary
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
    ("package", "prediction", "settlements"),
    [
        ({}, {"mu": 10**400}, []),
        ({}, {}, [YEAR_1_SETTLEMENT]),
        ({"run_date": 20260902}, {}, []),
        ({}, {"target_date": 20261001}, []),
        # eff_n reads pending targets only once their type has a canonical settlement.
        ({}, {"type": "EQUITY_ALPHA", "target_date": "2026-02-30"}, [SETTLEMENT]),
        ({}, {}, [dict(SETTLEMENT, settle_price_date=20260828)]),
        ({}, {}, [dict(SETTLEMENT, model=5)]),
        # Canonical keys sharing a model and vintage are compared by ticker.
        ({}, {}, [SETTLEMENT, dict(SETTLEMENT, ticker=7)]),
        # The duplicate-book check reads every package's and prediction's model.
        ({"model": ["claude-opus-5"]}, {}, []),
        ({}, {"model": {"name": "claude-opus-5"}}, []),
    ],
    ids=[
        "mu-10**400",
        "target-0001-01-01",
        "package-run_date-20260902",
        "prediction-target_date-20261001",
        "prediction-target_date-2026-02-30",
        "settle_price_date-20260828",
        "settlement-model-5",
        "settlement-ticker-7",
        "package-model-list",
        "prediction-model-object",
    ],
)
def test_reflection_reads_an_earlier_ledger_with_extreme_or_wrongly_typed_values(
    tmp_path: Path,
    package: dict[str, Any],
    prediction: dict[str, Any],
    settlements: list[dict[str, Any]],
) -> None:
    earlier = dict(market_forecast("SPY", 773.17), run_date="2026-09-02", **prediction)
    payload = {"run_date": "2026-09-02", "predictions": [earlier], **package}
    stub_package(
        tmp_path / "claude-opus-5-2026-09-02", dict(payload, settlements=settlements)
    )
    report = run("claude-opus-5", "2026-09-03", tmp_path, default_handlers())
    assert report.halt_reason == "no handler for DATA_OK"  # REFLECTION passed


@pytest.mark.parametrize(
    ("run_date", "read"),
    [(..., True), (20260902, False), (None, False), (float("nan"), False)],
    ids=["missing", "number", "null", "nan"],
)
def test_reflection_reads_an_earlier_package_only_when_its_run_date_is_a_string(
    tmp_path: Path, run_date: Any, read: bool
) -> None:
    # A package with no run_date was always read; any other non-string is left out.
    due = dict(
        market_forecast("SPY", 773.17), run_date="2026-08-01", target_date="2026-09-01"
    )
    payload: dict[str, Any] = {"predictions": [due], "settlements": []}
    if run_date is not ...:
        payload["run_date"] = run_date
    stub_package(tmp_path / "claude-opus-5-2026-09-02", payload)
    manifest = settlement_summary(tmp_path, "2026-09-03", "claude-opus-5-2026-09-03")
    assert manifest["generated_from_packages"] == (
        ["claude-opus-5-2026-09-02"] if read else []
    )
    assert manifest["summary"]["due_inventory"] == (1 if read else 0)


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
