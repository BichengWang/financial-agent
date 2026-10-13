"""Offline point-in-time and portfolio invariants for dated research."""

import json
from pathlib import Path
from typing import Any

import pandas as pd  # type: ignore[import-untyped]
import pytest

from financial_agent.quant.backtest import BacktestConfig, run_backtest
from financial_agent.quant.data import MarketData, synthetic_market
from financial_agent.quant.strategies import build_strategy
from financial_agent.quant.strategies.research import ResearchForecastStrategy

FIXTURES = Path(__file__).parents[1] / "fixtures" / "research"


def market(day: str) -> MarketData:
    return synthetic_market(("AAA", "BBB", "NEG"), 1, seed=0, start=day)


def test_point_in_time_expiry_and_vintage_averaging() -> None:
    strategy = ResearchForecastStrategy(str(FIXTURES))
    assert strategy.target_weights(market("2026-01-05")).sum() == 0
    assert strategy.target_weights(market("2026-01-06"))["AAA"] == pytest.approx(0.04)
    # Same-day new records remain invisible; only the prior vintage is usable.
    assert strategy.target_weights(market("2026-01-07"))["AAA"] == pytest.approx(0.04)
    # Mean mu=.04, mean sigma=1.0, rather than mean individual Kelly weights.
    assert strategy.target_weights(market("2026-01-08"))["AAA"] == pytest.approx(0.01)
    assert strategy.target_weights(market("2026-01-09"))["AAA"] > 0
    assert strategy.target_weights(market("2026-01-12")).sum() == 0


def test_sizing_filters_and_counted_skips() -> None:
    strategy = ResearchForecastStrategy(str(FIXTURES))
    weights = strategy.target_weights(market("2026-01-06"))
    assert weights.to_dict() == pytest.approx({"AAA": 0.04, "BBB": 0.05, "NEG": 0})
    assert strategy.skipped_reasons == {
        "malformed_package": 1,
        "nonpositive_sigma": 1,
        "missing_or_invalid_number": 1,
        "invalid_record": 1,
        "type_filter": 1,
        "missing_identity_or_type": 1,
    }
    filtered = ResearchForecastStrategy(
        str(FIXTURES), models=("one",), sleeves=("CORE",)
    )
    assert filtered.target_weights(market("2026-01-08"))["AAA"] == pytest.approx(0.02)
    assert filtered.skipped_reasons["model_filter"] == 1
    assert filtered.skipped_reasons["sleeve_filter"] > 0
    assert (
        ResearchForecastStrategy(str(FIXTURES), min_mu=0.04).target_weights(
            market("2026-01-06")
        )["AAA"]
        == 0
    )


def test_gross_cap_and_registry_backtest() -> None:
    strategy = build_strategy(
        "research_forecast",
        {
            "output_dir": str(FIXTURES),
            "max_weight": 1.0,
            "kelly_fraction": 1.0,
        },
    )
    weights = strategy.target_weights(market("2026-01-06"))
    assert weights.sum() == pytest.approx(1)
    assert weights["AAA"] == pytest.approx(0.16 / 1.16)
    assert weights["BBB"] == pytest.approx(1 / 1.16)
    data = synthetic_market(("AAA", "BBB", "NEG"), 12, seed=0, start="2026-01-05")
    result = run_backtest(strategy, data, BacktestConfig(rebalance="daily"))
    assert len(result.trades) > 0
    assert result.trades.iloc[0]["decision_session"] > pd.Timestamp("2026-01-05")
    json.dumps(strategy.params())


def test_snapshot_cache_and_bad_rows(tmp_path: Path) -> None:
    folder = tmp_path / "package"
    folder.mkdir()
    file = folder / "15_predictions.json"
    file.write_text(
        json.dumps(
            {
                "run_date": "2026-01-07",
                "model": "one",
                "predictions": [
                    {
                        "run_date": "2026-01-05",
                        "ticker": "AAA",
                        "mu": 0.1,
                        "sigma": 0.5,
                        "type": "EQUITY_ALPHA",
                        "target_date": "2026-01-09",
                    },
                    {
                        "ticker": "AAA",
                        "mu": float("nan"),
                        "sigma": 0.5,
                        "type": "EQUITY_ALPHA",
                        "target_date": "2026-01-09",
                    },
                    {
                        "ticker": "AAA",
                        "mu": 0.1,
                        "sigma": 0.5,
                        "type": "EQUITY_ALPHA",
                        "target_date": "invalid",
                    },
                ],
            }
        )
    )
    strategy = ResearchForecastStrategy(str(tmp_path))
    assert strategy.target_weights(market("2026-01-06")).sum() == 0
    assert strategy.target_weights(market("2026-01-08"))["AAA"] > 0
    assert strategy.skipped_reasons == {
        "nonfinite_number": 1,
        "missing_or_invalid_date": 1,
    }
    file.write_text("{}")
    cached = ResearchForecastStrategy(str(tmp_path))
    assert cached.forecast_count == 1
    assert cached.skipped_reasons == strategy.skipped_reasons


@pytest.mark.parametrize(
    "params",
    [
        {"kelly_fraction": -1},
        {"max_weight": 1.1},
        {"min_mu": float("inf")},
        {"kelly_fraction": True},
        {"types": [42]},
    ],
)
def test_invalid_parameters(params: dict[str, Any]) -> None:
    with pytest.raises(ValueError):
        ResearchForecastStrategy(str(FIXTURES), **params)


def test_models_have_equal_votes_and_package_errors_are_isolated(
    tmp_path: Path,
) -> None:
    rows = []
    for model, mu, sigma in (
        ("one", 0.02, 0.5),
        ("one", 0.02, 0.5),
        ("two", 0.06, 1.5),
    ):
        rows.append(
            dict(
                model=model,
                ticker="AAA",
                mu=mu,
                sigma=sigma,
                type="EQUITY_ALPHA",
                target_date="2026-01-09",
            )
        )
    rows.append(
        dict(
            model="one",
            ticker="AAA",
            mu=0.02,
            sigma=0.5,
            type="EQUITY_ALPHA",
            target_date="2026-01-05",
        )
    )
    for name, package in (
        ("valid", dict(run_date="2026-01-05", predictions=rows)),
        ("missing", {}),
        ("scalar", 42),
    ):
        directory = tmp_path / name
        directory.mkdir()
        (directory / "15_predictions.json").write_text(json.dumps(package))
    strategy = ResearchForecastStrategy(str(tmp_path))
    assert strategy.target_weights(market("2026-01-06"))["AAA"] == pytest.approx(0.01)
    assert strategy.skipped_reasons == {
        "invalid_predictions_list": 1,
        "malformed_package": 1,
        "nonpositive_horizon": 1,
    }
