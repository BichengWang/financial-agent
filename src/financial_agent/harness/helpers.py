"""Load the daily system's helper scripts by path, so each rule has one home.

``agents/equity/daily_investment_system/`` holds tested, standard-library
scripts (the canonical settlement ledger, its NYSE calendar). They are not a
package; builds include them as resources without duplicating their source.
"""

from __future__ import annotations

import importlib.util
import sys
from contextlib import ExitStack
from importlib.resources import as_file, files
from pathlib import Path
from types import ModuleType

SYSTEM_DIR = (
    Path(__file__).resolve().parents[3]
    / "agents"
    / "equity"
    / "daily_investment_system"
)


def load_helper(name: str) -> ModuleType:
    """Load once per process, preferring checkout scripts over wheel resources."""
    if name in sys.modules:
        return sys.modules[name]
    path = SYSTEM_DIR / f"{name}.py"
    with ExitStack() as stack:
        if not path.is_file():
            resource = files("financial_agent.harness").joinpath(
                "_system", f"{name}.py"
            )
            if not resource.is_file():
                raise FileNotFoundError(
                    f"cannot load helper {name!r}: neither {path} nor packaged "
                    f"resource {resource} exists"
                )
            path = stack.enter_context(as_file(resource))
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot load {name} from {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        return module
