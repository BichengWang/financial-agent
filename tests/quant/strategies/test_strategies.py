"""Strategy tests cover momentum selection, target risk and invalid exposure."""

from dataclasses import replace
import json
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from financial_agent.quant.data import synthetic_market
from financial_agent.quant.strategies import (
    build_strategy,
    dual_momentum,
    trend_vol_target,
    buy_and_hold,
    sixty_forty,
    validate_weights,
    StrategyError,
)


def test_dual_selection_defensive_and_cash() -> None:
    data = synthetic_market(["A", "B", "C", "D"], 6, seed=4)
    close = pd.DataFrame(
        {
            "A": [10, 11, 12, 14, 15, 1],
            "B": [10, 10, 10, 11, 12, 99],
            "C": [10, 9, 8, 7, 6, 100],
            "D": [10, 10, 10, 11, 11, 1],
        },
        index=data.sessions,
    )
    data = replace(data, close=close)
    strategy = dual_momentum(
        ("A", "B", "C", "ABSENT"), "D", lookback=5, skip=1, top_k=3
    )
    assert strategy.target_weights(data).to_dict() == pytest.approx(
        {"A": 1 / 3, "B": 1 / 3, "C": 0, "D": 1 / 3}
    )
    close.loc[data.sessions[-2], "D"] = 9
    assert strategy.target_weights(data)["D"] == 0
    close.loc[data.sessions[-2], ["A", "B"]] = 9
    assert strategy.target_weights(data).sum() == 0
    assert strategy.target_weights(data.upto(data.sessions[3])).sum() == 0


def test_trend_downtrend_caps_and_target_volatility() -> None:
    data = synthetic_market(
        ["A", "B", "C"], 500, seed=7, annual_drift=1.0, annual_vol=0.3
    )
    strategy = trend_vol_target(lookbacks=(21, 63), target_vol=0.04, max_weight=1)
    weights = strategy.target_weights(data)
    covariance = data.close.pct_change(fill_method=None).tail(126).cov() * 252
    vol = np.sqrt(weights.to_numpy() @ covariance.to_numpy() @ weights.to_numpy())
    assert vol == pytest.approx(0.04, rel=1e-10)
    capped = trend_vol_target(
        lookbacks=(21, 63), target_vol=2, max_weight=0.3
    ).target_weights(data)
    assert capped.max() <= 0.3
    assert capped.sum() <= 1
    down = data.close.copy()
    down.loc[:, :] = np.exp(-np.arange(500)[:, None] / 100) * 100
    assert strategy.target_weights(replace(data, close=down)).sum() == 0
    assert strategy.target_weights(data.upto(data.sessions[20])).sum() == 0
    missing = data.close.copy()
    missing.iloc[:480, 0] = np.nan
    assert strategy.target_weights(replace(data, close=missing))["A"] == 0


@pytest.mark.parametrize(
    "weights",
    [{"A": -1}, {"A": float("nan")}, {"A": float("inf")}, {"X": 0.5}, {"A": 1.1}],
)
def test_weight_errors(weights: dict[str, float]) -> None:
    data = synthetic_market(["A"], 10, seed=7)
    with pytest.raises(StrategyError, match="buy_and_hold"):
        validate_weights(buy_and_hold(), data, pd.Series(weights))
    valid = validate_weights(buy_and_hold(), data, pd.Series(dtype=float))
    assert valid.to_dict() == {"A": 0.0}


def test_registry_validation_json_and_benchmarks() -> None:
    for name in ("dual_momentum", "trend_vol_target", "buy_and_hold", "sixty_forty"):
        strategy = build_strategy(name)
        assert (
            build_strategy(name, json.loads(json.dumps(strategy.params()))).params()
            == strategy.params()
        )
    for params in (
        {"unknown": 1},
        {"top_k": "3"},
        {"lookback": True},
        {"risk_assets": [1]},
        {"skip": 300},
    ):
        with pytest.raises(ValueError, match="valid params"):
            build_strategy("dual_momentum", params)
    with pytest.raises(ValueError, match="valid names"):
        build_strategy("missing")
    data = synthetic_market(["SPY", "IEF"], 2, seed=7)
    assert sixty_forty().target_weights(data).to_dict() == {"SPY": 0.6, "IEF": 0.4}
    assert buy_and_hold({"ABSENT": 1}).target_weights(data).sum() == 0
