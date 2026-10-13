"""Policy-driven promotion checks; missing statistical evidence fails closed."""

from dataclasses import dataclass, field, fields
import hashlib
import math
from pathlib import Path
import tomllib
from typing import Any

import numpy as np

from ..backtest import BacktestConfig, performance_summary
from ..data import MarketData
from ..strategies import build_strategy
from .bootstrap import block_bootstrap_ci
from .overfitting import deflated_sharpe_ratio, pbo_cscv
from .stress import stress_test
from .walkforward import ParameterGrid, annual_sharpe, walk_forward

POLICY_PATH = Path(__file__).resolve().parents[1] / "quant_policy.toml"


@dataclass(frozen=True)
class PromotionPolicy:
    """Finite thresholds and integer session counts; probabilities are fractions."""

    min_oos_sessions: int = 2520
    min_oos_sharpe: float = 0.5
    min_dsr: float = 0.95
    max_prob_oos_loss: float = 0.10
    max_oos_drawdown: float = 0.25
    min_sharpe_2x_costs: float = 0.3
    min_sharpe_delay_1: float = 0.3
    min_bootstrap_sharpe_p05: float = 0.0
    train_sessions: int = 1260
    test_sessions: int = 252
    embargo_sessions: int = 5
    pbo_splits: int = 16
    _source_bytes: bytes = field(default=b"", init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        integers = {
            "min_oos_sessions": 1,
            "train_sessions": 2,
            "test_sessions": 1,
            "embargo_sessions": 0,
            "pbo_splits": 2,
        }
        for item in fields(self):
            if item.name.startswith("_"):
                continue
            value = getattr(self, item.name)
            if item.name in integers:
                if (
                    isinstance(value, bool)
                    or not isinstance(value, int)
                    or value < integers[item.name]
                ):
                    raise ValueError(
                        f"{item.name} must be an integer >= {integers[item.name]}"
                    )
            elif (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
            ):
                raise ValueError(f"{item.name} must be finite and numeric")
            elif item.name in ("min_dsr", "max_prob_oos_loss", "max_oos_drawdown"):
                if not 0 <= value <= 1:
                    raise ValueError(f"{item.name} must be in [0, 1]")
            elif value < 0:
                raise ValueError(f"{item.name} must be nonnegative")
        if self.pbo_splits % 2:
            raise ValueError("pbo_splits must be even")

    @classmethod
    def load(cls, path: str | Path | None = None) -> "PromotionPolicy":
        """Load [promotion], reject unknown keys and retain exact policy bytes."""
        raw = (POLICY_PATH if path is None else Path(path)).read_bytes()
        try:
            table = tomllib.loads(raw.decode("utf-8"))["promotion"]
        except (KeyError, UnicodeError, tomllib.TOMLDecodeError) as exc:
            raise ValueError("invalid policy: expected a [promotion] table") from exc
        if not isinstance(table, dict):
            raise ValueError("promotion must be a table")
        valid = {item.name for item in fields(cls) if item.init}
        unknown = table.keys() - valid
        if unknown:
            raise ValueError(f"unknown promotion keys: {sorted(unknown)}")
        result = cls(**table)
        object.__setattr__(result, "_source_bytes", raw)
        return result

    def file_sha256(self) -> str:
        """Hash policy bytes only when they match the effective thresholds.

        Direct construction is useful for research. Certificates require an
        unchanged loaded policy or exact packaged defaults.
        """
        raw = self._source_bytes or POLICY_PATH.read_bytes()
        loaded = tomllib.loads(raw.decode("utf-8"))["promotion"]
        effective = PromotionPolicy(**loaded)
        if self != effective:
            raise ValueError(
                "certificate policy differs from policy file; "
                "load a matching policy file"
            )
        return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class Check:
    name: str
    value: float
    threshold: float
    passed: bool
    detail: str


@dataclass(frozen=True)
class PromotionReport:
    strategy: str
    selected_params: dict[str, Any]
    grid: tuple[dict[str, Any], ...]
    passed: bool
    checks: list[Check]
    oos_summary: dict[str, float]
    data_fingerprint: str
    data_start: str
    data_end: str
    policy: PromotionPolicy = field(repr=False)
    diagnostics: dict[str, float] = field(default_factory=dict)


def evaluate_promotion(
    name: str,
    grid: ParameterGrid,
    data: MarketData,
    config: BacktestConfig,
    policy: PromotionPolicy,
) -> PromotionReport:
    """Evaluate eight registered checks; insufficient evidence records failures.

    Trial variance uses full-period per-session Sharpes. DSR uses stitched OOS
    returns. Bootstrap is circular (21 sessions, 2000 draws, seed=0), and the
    lower endpoint of its 90% interval is the 5th percentile.
    """
    result = walk_forward(
        lambda params: build_strategy(name, params),
        grid,
        data,
        config,
        train_sessions=policy.train_sessions,
        test_sessions=policy.test_sessions,
        embargo_sessions=policy.embargo_sessions,
    )
    summary = performance_summary(result.oos_returns)
    checks: list[Check] = []

    def check(
        label: str,
        value: float,
        threshold: float,
        reason: str,
        *,
        maximum: bool = False,
        strict: bool = False,
        error: str = "",
    ) -> None:
        passed = math.isfinite(value) and (
            value <= threshold
            if maximum
            else value > threshold if strict else value >= threshold
        )
        relation = "<=" if maximum else ">" if strict else ">="
        detail = (
            f"{label} {value:.6g} {relation} {threshold:.6g}: passed"
            if passed
            else f"{label} {value:.6g} fails {relation} {threshold:.6g}: "
            f"{error or reason}"
        )
        checks.append(
            Check(label, float(value), float(threshold), bool(passed), detail)
        )

    check(
        "oos_sessions",
        len(result.oos_returns),
        policy.min_oos_sessions,
        "insufficient out-of-sample sessions",
    )
    check(
        "oos_sharpe",
        summary["sharpe"],
        policy.min_oos_sharpe,
        "net out-of-sample risk-adjusted return is insufficient",
    )
    dsr, dsr_error = float("nan"), ""
    try:
        scores = np.asarray(
            [
                annual_sharpe(result.variant_returns[i].to_numpy()) / np.sqrt(252)
                for i in result.variant_returns.columns
            ]
        )
        if not np.isfinite(scores).all():
            raise ValueError("insufficient data or undefined trial Sharpe")
        variance = float(scores.var(ddof=1)) if len(scores) > 1 else 0.0
        dsr = deflated_sharpe_ratio(
            result.oos_returns.to_numpy(),
            n_trials=len(grid),
            trials_sharpe_variance=variance,
        )
    except ValueError as exc:
        dsr_error = str(exc)
    check(
        "dsr",
        dsr,
        policy.min_dsr,
        "evidence does not clear the multiple-trial Sharpe benchmark",
        error=dsr_error,
    )
    loss, cscv_error = float("nan"), ""
    diagnostics = {
        "pbo": float("nan"),
        "n_combinations": 0.0,
        "degradation_slope": float("nan"),
    }
    try:
        cscv = pbo_cscv(result.variant_returns, policy.pbo_splits)
        loss = cscv.prob_oos_loss
        diagnostics.update(
            pbo=cscv.pbo,
            n_combinations=float(cscv.n_combinations),
            degradation_slope=cscv.degradation_slope,
        )
    except ValueError as exc:
        cscv_error = str(exc)
    check(
        "prob_oos_loss",
        loss,
        policy.max_prob_oos_loss,
        "in-sample-selected variant too often loses money out of sample",
        maximum=True,
        error=cscv_error,
    )
    check(
        "oos_drawdown",
        summary["max_drawdown"],
        policy.max_oos_drawdown,
        "out-of-sample drawdown exceeds the loss budget",
        maximum=True,
    )
    cost_sharpe, delay_sharpe = float("nan"), float("nan")
    if result.selected_params and len(result.oos_returns) > 1:
        stressed = stress_test(
            build_strategy(name, result.selected_params),
            data,
            config,
            result.oos_returns.index,
        )
        cost_sharpe, delay_sharpe = stressed.sharpe_2x_costs, stressed.sharpe_delay_1
    check(
        "sharpe_2x_costs",
        cost_sharpe,
        policy.min_sharpe_2x_costs,
        "insufficient evidence or the edge does not survive doubled costs",
    )
    check(
        "sharpe_delay_1",
        delay_sharpe,
        policy.min_sharpe_delay_1,
        "insufficient evidence or the edge does not survive an extra session of delay",
    )
    lower, bootstrap_error = float("nan"), ""
    try:
        lower, _ = block_bootstrap_ci(
            result.oos_returns.to_numpy(),
            annual_sharpe,
            seed=0,
        )
    except ValueError as exc:
        bootstrap_error = str(exc)
    check(
        "bootstrap_sharpe_p05",
        lower,
        policy.min_bootstrap_sharpe_p05,
        "the bootstrap lower bound does not support a positive edge",
        strict=True,
        error=bootstrap_error,
    )
    return PromotionReport(
        name,
        result.selected_params,
        tuple(dict(p) for p in grid),
        all(c.passed for c in checks),
        checks,
        summary,
        data.fingerprint(),
        str(data.sessions[0].date()) if len(data.sessions) else "",
        str(data.sessions[-1].date()) if len(data.sessions) else "",
        policy,
        diagnostics,
    )
