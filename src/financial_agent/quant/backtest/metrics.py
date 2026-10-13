"""Net-return metrics: sample volatility, zero rf, historical loss quantiles."""

import math
import numpy as np
import pandas as pd  # type: ignore[import-untyped]


def drawdown_series(equity: pd.Series) -> pd.Series:
    """Positive fractional drawdown from the running equity peak."""
    if not np.isfinite(equity.to_numpy(dtype=float)).all() or (equity <= 0).any():
        raise ValueError("equity must be finite and positive")
    return 1 - equity / equity.cummax()


def performance_summary(
    returns: pd.Series,
    *,
    benchmark: pd.Series | None = None,
    periods_per_year: int = 252,
) -> dict[str, float]:
    """Summarize simple returns; undefined metrics are NaN, without warnings.

    Reject missing/nonfinite returns and returns <= -1. CAGR uses n observations;
    drawdown includes initial unit wealth. Sortino uses the RMS of min(r, 0)
    over all observations. VaR is the clipped negative 5th percentile; CVaR is
    the clipped negative mean at/below that percentile. Benchmark regression
    uses aligned observations; alpha is annualized arithmetic intercept.
    """
    if periods_per_year <= 0:
        raise ValueError("periods_per_year must be positive")
    values = returns.to_numpy(dtype=float)
    if not np.isfinite(values).all() or (values <= -1).any():
        raise ValueError("returns must be finite and greater than -1")
    keys = (
        "total_return",
        "cagr",
        "ann_vol",
        "sharpe",
        "sortino",
        "max_drawdown",
        "calmar",
        "hit_rate",
        "skew",
        "kurtosis",
        "var95",
        "cvar95",
    )
    result = dict.fromkeys(keys, float("nan"))
    n = len(values)
    if n:
        log_growth = float(np.log1p(values).sum())
        total = math.expm1(log_growth)
        cagr = math.expm1(log_growth * periods_per_year / n)
        mean = float(values.mean())
        std = float(values.std(ddof=1)) if n > 1 else float("nan")
        downside = float(np.sqrt(np.mean(np.minimum(values, 0) ** 2)))
        wealth = pd.Series(np.r_[1.0, np.cumprod(1 + values)])
        drawdown = float(drawdown_series(wealth).max())
        quantile = float(np.quantile(values, 0.05))
        result.update(
            total_return=total,
            cagr=cagr,
            ann_vol=std * np.sqrt(periods_per_year),
            sharpe=mean / std * np.sqrt(periods_per_year) if std > 0 else float("nan"),
            sortino=(
                mean / downside * np.sqrt(periods_per_year)
                if downside > 0
                else float("nan")
            ),
            max_drawdown=drawdown,
            calmar=cagr / drawdown if drawdown > 0 else float("nan"),
            hit_rate=float((values > 0).mean()),
            skew=float(returns.skew()) if n >= 3 and std > 0 else float("nan"),
            kurtosis=float(returns.kurt()) if n >= 4 and std > 0 else float("nan"),
            var95=max(0.0, -quantile),
            cvar95=max(0.0, -float(values[values <= quantile].mean())),
        )
    if benchmark is not None:
        if (
            not np.isfinite(benchmark.to_numpy(dtype=float)).all()
            or (benchmark <= -1).any()
        ):
            raise ValueError("benchmark must contain finite returns greater than -1")
        result.update(beta=float("nan"), alpha=float("nan"), correlation=float("nan"))
        aligned = pd.concat(
            [returns.rename("portfolio"), benchmark.rename("benchmark")],
            axis=1,
            join="inner",
        ).dropna()
        if len(aligned) > 1:
            x = aligned["benchmark"].to_numpy(dtype=float)
            y = aligned["portfolio"].to_numpy(dtype=float)
            variance = float(x.var(ddof=1))
            if variance > 0:
                beta = float(np.cov(x, y, ddof=1)[0, 1] / variance)
                result.update(
                    beta=beta,
                    alpha=float((y.mean() - beta * x.mean()) * periods_per_year),
                )
                if y.std(ddof=1) > 0:
                    result["correlation"] = float(np.corrcoef(x, y)[0, 1])
    return result
