"""Stage handlers shipped with the harness.

Each handler is deterministic and read-only on prior packages. Stages that need
data adapters or a model are not registered, so ``run`` still halts before them.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from financial_agent.harness.gates import go_reachability
from financial_agent.harness.helpers import load_helper
from financial_agent.harness.market_calendar import session
from financial_agent.harness.policy import load_policy
from financial_agent.harness.runner import RunContext, StageResult

MARKET_TZ = ZoneInfo("America/New_York")


def precheck_handler(context: RunContext) -> StageResult:
    """PRECHECK: the run date's session, and whether GO is reachable at all.

    Plan §3.5 step 2: if no name can pass the evidence thresholds with the
    families that can score, say so on day 1 rather than in run 13. An
    unreachable GO does not halt; the run still publishes NO_TRADE.
    """
    today = dt.datetime.now(MARKET_TZ).date()
    if dt.date.fromisoformat(context.date) > today:
        return StageResult(halt=f"run date {context.date} is after {today} (ET)")
    day = session(context.date)
    reach = go_reachability(context.policy or load_policy())
    note = day.describe() + (
        "; GO reachable"
        if reach.reachable
        else f"; GO unreachable ({len(reach.blockers)} structural blockers)"
    )
    return StageResult(
        note,
        data={
            "session": vars(day),
            "go_reachable": reach.reachable,
            "go_blockers": list(reach.blockers),
        },
    )


def settlement_summary(output_dir: Path, run_date: str, run_id: str) -> dict[str, Any]:
    """Canonical settlement state from packages dated before this run."""
    ledger = load_helper("settlement_ledger")
    packages = [
        p
        for p in ledger.load_packages(output_dir)
        if p["_source_file"] != run_id and p.get("run_date", "") <= run_date
    ]
    manifest: dict[str, Any] = ledger.build_manifest(packages, as_of=run_date)
    return manifest


def reflection_handler(context: RunContext) -> StageResult:
    """REFLECTION: settle what is due from the immutable ledgers, report it."""
    manifest = settlement_summary(
        context.package_dir.parent, context.date, context.run_id
    )
    summary = manifest["summary"]
    metrics = manifest["rolling_metrics"]["equity_alpha"]
    note = (
        f"{summary['canonical_equity_alpha_settlements']} canonical EQUITY_ALPHA "
        f"settlements (eff_n {metrics['eff_n']}), "
        f"{summary['canonical_market_forecast_settlements']} MARKET_FORECAST, "
        f"{summary['due_inventory']} due, {summary['conflicts']} conflicts"
    )
    if summary["conflicts"]:
        return StageResult(halt=f"settlement conflicts need reconciliation: {note}")
    return StageResult(note)
