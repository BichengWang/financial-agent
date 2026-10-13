"""Performance metrics checked against independently calculated values."""

import math
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from financial_agent.quant.backtest import performance_summary, drawdown_series


def test_hand_metrics() -> None:
    returns = pd.Series([0.1, -0.2, 0.05, -0.1])
    summary = performance_summary(returns, periods_per_year=4)
    total = 1.1 * 0.8 * 1.05 * 0.9 - 1
    mean = -0.15 / 4
    variance = sum((r - mean) ** 2 for r in returns) / 3
    assert summary["total_return"] == pytest.approx(total)
    assert summary["cagr"] == pytest.approx(total)
    assert summary["ann_vol"] == pytest.approx(math.sqrt(variance) * 2)
    assert summary["sharpe"] == pytest.approx(mean / math.sqrt(variance) * 2)
    assert summary["sortino"] == pytest.approx(
        mean / math.sqrt((0.2**2 + 0.1**2) / 4) * 2
    )
    assert summary["max_drawdown"] == pytest.approx(1 - 0.8 * 1.05 * 0.9)
    assert summary["calmar"] == pytest.approx(total / (1 - 0.8 * 1.05 * 0.9))
    assert summary["hit_rate"] == 0.5
    assert summary["var95"] == pytest.approx(0.185)
    assert summary["cvar95"] == pytest.approx(0.2)
    dd = drawdown_series(pd.Series([100, 110, 88, 92.4, 83.16]))
    assert dd.tolist() == pytest.approx([0, 0, 0.2, 0.16, 0.244])


def test_benchmark_alignment_and_degenerate_inputs() -> None:
    benchmark = pd.Series([-0.01, 0.02, -0.03, 0.04], index=[1, 2, 3, 4])
    portfolio = 2 * benchmark + 0.001
    metrics = performance_summary(portfolio, benchmark=benchmark)
    assert metrics["beta"] == pytest.approx(2)
    assert metrics["alpha"] == pytest.approx(0.252)
    assert metrics["correlation"] == pytest.approx(1)
    with np.errstate(all="raise"):
        assert all(
            math.isnan(v)
            for v in performance_summary(pd.Series([], dtype=float)).values()
        )
        zero = performance_summary(pd.Series([0.0, 0.0, 0.0, 0.0]))
        assert math.isnan(zero["sharpe"])
        assert math.isnan(zero["sortino"])
        assert zero["max_drawdown"] == 0
        assert math.isnan(performance_summary(pd.Series([0.1]))["ann_vol"])
    with pytest.raises(ValueError):
        performance_summary(pd.Series([np.nan]))
    with pytest.raises(ValueError):
        performance_summary(pd.Series([-1.0]))
