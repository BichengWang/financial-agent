"""Helper loading preserves checkout precedence and supports wheel resources."""

from __future__ import annotations

import datetime as dt
import shutil
import sys
from pathlib import Path

import pytest

from financial_agent.harness import helpers


@pytest.mark.parametrize("name", ["settlement_ledger", "factor_scoring"])
def test_resource_fallback(
    name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    resources = tmp_path / "harness"
    system = resources / "_system"
    system.mkdir(parents=True)
    shutil.copyfile(helpers.SYSTEM_DIR / f"{name}.py", system / f"{name}.py")
    monkeypatch.setattr(helpers, "SYSTEM_DIR", tmp_path / "missing-checkout")
    monkeypatch.setattr(helpers, "files", lambda package: resources)
    monkeypatch.delitem(sys.modules, name, raising=False)

    module = helpers.load_helper(name)

    if name == "settlement_ledger":
        assert module.is_trading_day(dt.date(2026, 10, 13))
        assert not module.is_trading_day(dt.date(2026, 10, 11))
    else:
        assert module.read_tickers(["SPY", "SPY", "IEF"], None) == ["SPY", "IEF"]
    assert helpers.load_helper(name) is module


def test_missing_helper_names_both_locations(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    checkout = tmp_path / "checkout"
    resources = tmp_path / "harness"
    monkeypatch.setattr(helpers, "SYSTEM_DIR", checkout)
    monkeypatch.setattr(helpers, "files", lambda package: resources)

    with pytest.raises(FileNotFoundError) as error:
        helpers.load_helper("missing_helper")

    assert str(checkout / "missing_helper.py") in str(error.value)
    assert str(resources / "_system" / "missing_helper.py") in str(error.value)
    assert "missing_helper" not in sys.modules
