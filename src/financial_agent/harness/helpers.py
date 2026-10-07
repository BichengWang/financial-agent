"""Load the daily system's helper scripts by path, so each rule has one home.

``agents/equity/daily_investment_system/`` holds tested, standard-library
scripts (the canonical settlement ledger, its NYSE calendar). They are not a
package; the harness loads them by path instead of copying their logic.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

SYSTEM_DIR = (
    Path(__file__).resolve().parents[3]
    / "agents"
    / "equity"
    / "daily_investment_system"
)


def load_helper(name: str) -> ModuleType:
    """The helper script ``{SYSTEM_DIR}/{name}.py``, loaded once per process."""
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, SYSTEM_DIR / f"{name}.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name} from {SYSTEM_DIR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
