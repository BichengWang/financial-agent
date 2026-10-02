"""Stage handlers shipped with the harness.

Each handler is deterministic and read-only on prior packages. Stages that need
data adapters or a model are not registered, so ``run`` still halts before them.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

from financial_agent.harness.runner import RunContext, StageResult

_SYSTEM_DIR = (
    Path(__file__).resolve().parents[3]
    / "agents"
    / "equity"
    / "daily_investment_system"
)


def _settlement_ledger() -> ModuleType:
    """The helper script is not a package; load it by path once."""
    name = "settlement_ledger"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, _SYSTEM_DIR / f"{name}.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name} from {_SYSTEM_DIR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def settlement_summary(output_dir: Path, run_date: str, run_id: str) -> dict[str, Any]:
    """Canonical settlement state from packages dated before this run."""
    ledger = _settlement_ledger()
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
