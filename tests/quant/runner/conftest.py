"""Seeded CSV fixtures keep every session test offline."""

from datetime import date
from pathlib import Path

import pytest

from financial_agent.quant.data import synthetic_market
from financial_agent.quant.data.providers import write_csv
from financial_agent.quant.runner import TradingConfig


@pytest.fixture
def config_path(tmp_path: Path) -> Path:
    data = synthetic_market(
        ["SPY", "QQQ", "IEF", "GLD"],
        420,
        seed=42,
        start="2019-01-02",
        annual_drift=0.30,
        annual_vol=0.03,
        correlation=0.1,
    )
    write_csv(data, tmp_path / "csv")
    path = tmp_path / "paper.toml"
    path.write_text(
        'mode = "paper"\nstate_dir = "state"\n'
        '[strategy]\nname = "trend_vol_target"\n'
        "[strategy.params]\nlookbacks = [3, 10]\ncov_lookback = 10\nmax_weight = 0.25\n"
        '[universe]\nsymbols = ["SPY", "QQQ", "IEF", "GLD"]\n'
        '[data]\nprovider = "csv"\ncsv_dir = "csv"\n'
        'cache_dir = "cache"\nstart = "2019-01-02"\n'
        '[backtest]\ncash_buffer = 0.02\nrebalance = "daily"\n'
        '[broker]\nkind = "paper"\ninitial_cash = 100000.0\n'
    )
    return path


@pytest.fixture
def config(config_path: Path) -> TradingConfig:
    return TradingConfig.load(config_path)


@pytest.fixture
def first_day() -> date:
    return date(2020, 6, 8)
