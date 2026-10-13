"""Share planning tests exercise drift, rounding, exits and notional filters."""

import pytest
from financial_agent.quant.portfolio import rebalance_deltas


def plan(
    targets: dict[str, float],
    positions: dict[str, float],
    *,
    fractional: bool = False,
    threshold: float = 0.02,
    minimum: float = 0,
) -> dict[str, float]:
    return rebalance_deltas(
        targets,
        positions,
        {"A": 10, "B": 30},
        1000,
        drift_threshold=threshold,
        fractional=fractional,
        min_trade_notional=minimum,
    )


def test_drift_exit_rounding_and_order() -> None:
    assert plan({"A": 0.501, "B": 0.1}, {"A": 50}) == {"B": 3.0}
    assert plan({"A": 0}, {"A": 1}, threshold=0.9) == {"A": -1.0}
    assert plan({"B": 0.1}, {}, fractional=True) == {"B": pytest.approx(10 / 3)}
    assert plan({}, {"A": 2}, minimum=21) == {}
    assert list(plan({"B": 0.3, "A": 0.3}, {})) == ["A", "B"]
    assert plan({"A": 0.1}, {"A": 11.5}, threshold=0) == {"A": -1.0}


def test_invalid_inputs_and_missing_prices() -> None:
    with pytest.raises(ValueError):
        plan({"A": -1}, {})
    with pytest.raises(ValueError):
        plan({}, {"A": -1})
    assert (
        rebalance_deltas(
            {"X": 1},
            {},
            {},
            100,
            drift_threshold=0,
            fractional=False,
            min_trade_notional=0,
        )
        == {}
    )


def test_series_inputs_and_fractional_full_exit() -> None:
    import pandas as pd  # type: ignore[import-untyped]

    assert rebalance_deltas(
        pd.Series({"A": 0.0}),
        pd.Series({"A": 0.5}),
        pd.Series({"A": 10.0}),
        100,
        drift_threshold=0.9,
        fractional=True,
        min_trade_notional=0,
    ) == {"A": -0.5}
