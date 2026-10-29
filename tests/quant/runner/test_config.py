"""Named configuration errors enforce trading reserves and tighten-only risk."""

from pathlib import Path

import pytest

from financial_agent.quant.runner import ConfigError, TradingConfig


def test_relative_paths_and_normalized_identity(config_path: Path) -> None:
    config = TradingConfig.load(config_path)
    assert config.state_dir == config_path.parent / "state"
    assert config.csv_dir == config_path.parent / "csv"
    assert config.strategy_params["lookbacks"] == [3, 10]
    assert set(config.risk.allowed_symbols) == set(config.symbols)


@pytest.mark.parametrize(
    "change,key",
    [
        ("\n[risk]\nmax_weight = 0.5\n", "max_weight"),
        ("\n[risk]\nmin_cash_pct = 0.005\n", "min_cash_pct"),
        ('\n[risk]\nallowed_symbols = ["UNKNOWN"]\n', "allowed_symbols"),
        ('\n[risk]\nmax_orders = "oops"\n', "max_orders"),
        ('\n[promotion]\ngrid = "oops"\n', "promotion.grid"),
        ("\n[promotion]\ndisclosed_trials = [1]\n", "promotion.disclosed_trials"),
        ("\n[unknown]\na = 1\n", "unknown"),
    ],
)
def test_invalid_overrides_are_named(config_path: Path, change: str, key: str) -> None:
    config_path.write_text(config_path.read_text() + change)
    with pytest.raises(ConfigError, match=key):
        TradingConfig.load(config_path)


@pytest.mark.parametrize(
    "old,new,key",
    [
        ("cash_buffer = 0.02", "cash_buffer = 0.01", "cash_buffer"),
        ("cash_buffer = 0.02", "cash_buffer = 0.0", "cash_buffer"),
        ('mode = "paper"', 'mode = "live"', "broker.kind"),
        ('provider = "csv"', 'provider = "unknown"', "data.provider"),
        ('csv_dir = "csv"', "", "data.csv_dir"),
        ('start = "2019-01-02"', 'start = "bad"', "data.start"),
    ],
)
def test_invalid_trading_settings(
    config_path: Path, old: str, new: str, key: str
) -> None:
    config_path.write_text(config_path.read_text().replace(old, new))
    with pytest.raises(ConfigError, match=key):
        TradingConfig.load(config_path)
