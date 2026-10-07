"""Kernels: the per-run engine as tested functions (plan Phase 2).

Every run used to re-implement risk analytics, the forecast, and Kelly from
``rules.md`` prose. That is how Sortino came out equal to Sharpe for weeks and
a drawdown sign flipped on a rebuild. Here they are pure functions of their
inputs, defined once:

* ``price_risk`` -- beta, realized and downside vol, tracking error, and 60d
  drawdown from adjusted closes, per the normative Metric Definition Table
  (``claude-opus-5-2026-09-03/05_factor_scores.md``) and ``rules.md``
  § Computed Risk Analytics;
* ``forecast_ratios`` -- Sharpe, Sortino, Information Ratio, Treynor, Calmar
  (``rules.md`` § Ratio Definitions);
* ``equity_record`` / ``market_forecast_records`` -- complete schema-v1 ledger
  records built from data plus the model's judgment inputs;
* ``portfolio_feasibility`` -- the portfolio-level risk controls (protected
  rules 3-7) and the event-risk stop, from proposed weights and closes
  (``rules.md`` § Computed Risk Analytics, § Risk Controls / Portfolio Level).

The model supplies judgment (percentile inputs, a bounded mu adjustment with a
reason, confidence, thesis); the kernel computes every number and refuses a
judgment outside the policy's bounds instead of publishing it.
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import math
import statistics
from dataclasses import dataclass, field
from itertools import combinations
from typing import Any, Mapping, Sequence

from financial_agent.harness.gates import (
    CONFIDENCE_ORDER,
    confidence_ceiling,
    earnings_in_window,
    investability,
)
from financial_agent.harness.policy import FAMILIES, Policy
from financial_agent.harness.schema import (
    CONFIDENCE,
    DATA_MODES,
    FORMULA,
    PRICE_TAGS,
    SCHEMA_VERSION,
    SIGMA_SOURCES,
)

RISK_INTERVALS = 60  # daily return intervals (61 closes): § Computed Risk Analytics
VOL_INTERVALS = 30  # REALIZED_VOL_30D: § Sigma Fallback Chain
MONTH = math.sqrt(21)  # daily -> one-month scaling
PRICE_DP = 4
DECIMAL_DP = 6


class KernelError(ValueError):
    """An input the policy does not allow; the record is not built."""


def daily_returns(closes: Sequence[float]) -> list[float]:
    return [b / a - 1 for a, b in zip(closes, closes[1:])]


def _beta(returns: Sequence[float], benchmark: Sequence[float]) -> float:
    """``cov(r, r_b, ddof=0) / var(r_b)``."""
    mean_r, mean_b = statistics.fmean(returns), statistics.fmean(benchmark)
    var_b = statistics.fmean([(b - mean_b) ** 2 for b in benchmark])
    if var_b == 0:
        raise KernelError("benchmark returns have zero variance: beta undefined")
    cov = statistics.fmean(
        [(r - mean_r) * (b - mean_b) for r, b in zip(returns, benchmark)]
    )
    return cov / var_b


@dataclass(frozen=True)
class PriceRisk:
    """Price-history analytics for one name, all decimals, one-month scale."""

    beta_60d_vs_spy: float
    realized_vol_30d: float
    prior_vol_30d: float  # the 30 intervals before the latest 30
    vol_60d: float
    downside_vol_30d: float | None  # None with fewer than two down days
    tracking_error_1m: float
    max_drawdown_60d: float  # signed, <= 0
    beta_60d_vs_tlt: float | None = None


def _window(name: str, closes: Sequence[float]) -> list[float]:
    need = RISK_INTERVALS + 1
    if len(closes) < need:
        raise KernelError(f"{name}: {len(closes)} closes, need {need}")
    window = [float(c) for c in closes[-need:]]
    if any(not math.isfinite(c) or c <= 0 for c in window):
        raise KernelError(f"{name}: closes must be positive and finite")
    return window


def price_risk(
    closes: Sequence[float],
    spy_closes: Sequence[float],
    *,
    tlt_closes: Sequence[float] | None = None,
) -> PriceRisk:
    """Risk analytics from date-aligned adjusted closes (oldest first).

    Uses the latest 61 closes (60 return intervals); population stdevs
    (``ddof=0``) scaled by ``sqrt(21)``. Downside vol is the stdev of the
    negative daily returns among the latest 30.
    """
    window = _window("closes", closes)
    returns = daily_returns(window)
    spy = daily_returns(_window("spy_closes", spy_closes))
    beta = _beta(returns, spy)
    latest = returns[-VOL_INTERVALS:]
    down = [r for r in latest if r < 0]
    peak, drawdown = window[0], 0.0
    for close in window:
        peak = max(peak, close)
        drawdown = min(drawdown, close / peak - 1)
    tlt_beta = None
    if tlt_closes is not None:
        tlt_beta = _beta(returns, daily_returns(_window("tlt_closes", tlt_closes)))
    return PriceRisk(
        beta_60d_vs_spy=beta,
        realized_vol_30d=statistics.pstdev(latest) * MONTH,
        prior_vol_30d=statistics.pstdev(returns[:-VOL_INTERVALS]) * MONTH,
        vol_60d=statistics.pstdev(returns) * MONTH,
        downside_vol_30d=statistics.pstdev(down) * MONTH if len(down) >= 2 else None,
        tracking_error_1m=statistics.pstdev(
            [r - beta * s for r, s in zip(returns, spy)]
        )
        * MONTH,
        max_drawdown_60d=drawdown,
        beta_60d_vs_tlt=tlt_beta,
    )


@dataclass(frozen=True)
class Ratios:
    sharpe: float
    sortino: float | None
    information_ratio: float | None
    treynor: float | None
    calmar: float | None
    basis: str  # EXCESS_RETURN with a sourced rf_1m, else RAW_DIAGNOSTIC


def _div(numerator: float, denominator: float | None) -> float | None:
    if denominator is None or denominator == 0:
        return None
    return numerator / denominator


def forecast_ratios(
    mu: float,
    sigma: float,
    *,
    rf_1m: float | None = None,
    downside_vol: float | None = None,
    beta: float | None = None,
    tracking_error: float | None = None,
    max_drawdown: float | None = None,
    spy_mu: float | None = None,
) -> Ratios:
    """``rules.md`` § Ratio Definitions; an unavailable input gives ``None``.

    Without a sourced one-month risk-free rate the ratios use raw ``mu`` and are
    labelled ``RAW_DIAGNOSTIC`` (§ Metric History and Grounding).
    """
    excess = mu - (rf_1m or 0.0)
    residual = None if beta is None or spy_mu is None else mu - beta * spy_mu
    return Ratios(
        sharpe=excess / sigma,
        sortino=_div(excess, downside_vol),
        information_ratio=(
            None if residual is None else _div(residual, tracking_error)
        ),
        treynor=_div(excess, beta),
        calmar=_div(excess, None if max_drawdown is None else abs(max_drawdown)),
        basis="RAW_DIAGNOSTIC" if rf_1m is None else "EXCESS_RETURN",
    )


def _round(value: float | None, digits: int = DECIMAL_DP) -> float | None:
    return None if value is None else round(value, digits)


def _require(name: str, value: Any, allowed: Sequence[str]) -> None:
    if value not in allowed:
        raise KernelError(f"{name}={value!r} not in {list(allowed)}")


def _target_date(run_date: str, horizon: int | None, policy: Policy) -> str:
    days = horizon or int(policy.num("forecast.default_horizon_days"))
    allowed = list(policy.get("forecast.allowed_horizon_days"))
    if days not in allowed:
        raise KernelError(f"horizon {days}d not in {allowed}")
    return (dt.date.fromisoformat(run_date) + dt.timedelta(days=days)).isoformat()


def _adjust(prior: float, adjustment: float, reason: str, limit: float) -> float:
    if abs(adjustment) > limit + 1e-12:
        raise KernelError(f"mu adjustment {adjustment:+.4f} exceeds ±{limit}")
    if adjustment and not reason.strip():
        raise KernelError("a mu adjustment needs a stated, ledger-backed reason")
    return prior + adjustment


def _price_fields(
    entry: float, mu: float, sigma: float, policy: Policy
) -> dict[str, Any]:
    if not entry > 0 or not 0 < sigma < 1:
        raise KernelError(f"entry_price {entry} / sigma {sigma} out of range")
    lo, hi = policy.ci70(entry, mu, sigma)
    return {
        "target_price": round(policy.target_price(entry, mu), PRICE_DP),
        "ci70_lo": round(lo, PRICE_DP),
        "ci70_hi": round(hi, PRICE_DP),
    }


@dataclass(frozen=True)
class EquityInputs:
    """One ranked name: grounded data plus the model's judgment calls."""

    ticker: str
    entry_price: float  # raw close from a ledger row
    price_tag: str
    price_date: str
    benchmark_price: float  # SPY close at price_date
    sigma: float  # decimal, one month
    sigma_source: str
    pctl: float  # adjusted-score percentile in the eligible universe
    family_z: Mapping[str, float | None]
    data_quality_multiplier: float
    confidence: str
    thesis: str
    penalties: float = 0.0
    mu_adjustment: float = 0.0
    mu_adjustment_reason: str = ""
    horizon_days: int | None = None
    kelly_raw: float | None = None  # beta-adjusted edge / TE variance, if computed
    earnings_within_window: bool = False
    rf_1m: float | None = None
    spy_mu: float | None = None
    risk: PriceRisk | None = None
    ledger_rows: tuple[str, ...] = ()
    extra: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "EquityInputs":
        values = dict(data)
        known = {f.name for f in dataclasses.fields(cls)}
        unknown = sorted(set(values) - known)
        if unknown:
            raise KernelError(f"unknown equity input(s) {unknown}; use 'extra'")
        if isinstance(values.get("risk"), Mapping):
            values["risk"] = PriceRisk(**values["risk"])
        values["ledger_rows"] = tuple(values.get("ledger_rows", ()))
        try:
            return cls(**values)
        except TypeError as exc:
            raise KernelError(str(exc)) from None


def equity_record(
    run_date: str, model: str, inputs: EquityInputs, policy: Policy
) -> dict[str, Any]:
    """A schema-v1 ``EQUITY_ALPHA`` record with every number computed."""
    _require("price_tag", inputs.price_tag, PRICE_TAGS)
    _require("sigma_source", inputs.sigma_source, SIGMA_SOURCES)
    _require("confidence", inputs.confidence, CONFIDENCE)
    unknown = sorted(set(inputs.family_z) - set(FAMILIES))
    if unknown:
        raise KernelError(f"unknown families {unknown}")
    for family in policy.shadow_families:
        if inputs.family_z.get(family) is not None:
            raise KernelError(
                f"{family} is SHADOW: it may not enter Adj Score until promoted "
                "(rules.md § SHADOW Diagnostic Tooling)"
            )
    band = policy.mu_prior(inputs.pctl)
    if band is None:
        raise KernelError(f"pctl {inputs.pctl} is below every mu band: do not rank")
    mu = _adjust(
        band.mu,
        inputs.mu_adjustment,
        inputs.mu_adjustment_reason,
        policy.num("forecast.mu_adjustment_max"),
    )
    family_z = {f: inputs.family_z.get(f) for f in FAMILIES}
    composite = policy.composite_z(family_z)
    dq = inputs.data_quality_multiplier
    raw = inputs.kelly_raw if inputs.kelly_raw is not None else mu / inputs.sigma**2
    sizing = policy.kelly_sizing(raw)
    metrics: dict[str, Any] = {
        "kelly_raw": _round(raw),
        "kelly_method": (
            "MU_OVER_SIGMA2" if inputs.kelly_raw is None else "BETA_ADJ_TE"
        ),
        "kelly_fractional": _round(sizing.fractional),
        "position_weight": _round(sizing.weight),
        "kelly_gate": sizing.gate,
        "var95": _round(policy.var95(mu, inputs.sigma)),
        "cvar95": _round(policy.cvar95(mu, inputs.sigma)),
    }
    risk = inputs.risk
    if risk is not None:
        metrics.update(
            {
                name: _round(getattr(risk, name))
                for name in (
                    "beta_60d_vs_spy",
                    "realized_vol_30d",
                    "downside_vol_30d",
                    "tracking_error_1m",
                    "max_drawdown_60d",
                )
            }
        )
    ratios = forecast_ratios(
        mu,
        inputs.sigma,
        rf_1m=inputs.rf_1m,
        downside_vol=risk.downside_vol_30d if risk else None,
        beta=risk.beta_60d_vs_spy if risk else None,
        tracking_error=risk.tracking_error_1m if risk else None,
        max_drawdown=risk.max_drawdown_60d if risk else None,
        spy_mu=inputs.spy_mu,
    )
    metrics.update(
        {
            "sharpe": _round(ratios.sharpe),
            "sortino": _round(ratios.sortino),
            "information_ratio": _round(ratios.information_ratio),
            "treynor": _round(ratios.treynor),
            "calmar": _round(ratios.calmar),
            "ratio_basis": ratios.basis,
        }
    )
    record: dict[str, Any] = {
        "run_date": run_date,
        "model": model,
        "ticker": inputs.ticker,
        "type": "EQUITY_ALPHA",
        "entry_price": inputs.entry_price,
        "price_tag": inputs.price_tag,
        "price_date": inputs.price_date,
        "mu": _round(mu),
        "mu_prior": band.mu,
        "mu_adjustment": inputs.mu_adjustment,
        "sigma": _round(inputs.sigma),
        "sigma_source": inputs.sigma_source,
        **_price_fields(inputs.entry_price, mu, inputs.sigma, policy),
        "target_date": _target_date(run_date, inputs.horizon_days, policy),
        "benchmark": "SPY",
        "benchmark_price": inputs.benchmark_price,
        "pctl": inputs.pctl,
        "adj_score": _round(policy.adj_score(composite, dq, inputs.penalties)),
        "sleeve": "MONITORING",
        "confidence": inputs.confidence,
        "status": "OPEN",
        "thesis": inputs.thesis,
        "score_explainability": {
            **family_z,
            "composite_z": _round(composite),
            "data_quality_multiplier": dq,
            "penalties": inputs.penalties,
            "formula": FORMULA,
            "metrics": metrics,
            "ledger_rows": list(inputs.ledger_rows),
        },
    }
    if inputs.mu_adjustment:
        record["mu_adjustment_reason"] = inputs.mu_adjustment_reason
    clash = sorted(set(inputs.extra) & set(record))
    if clash:
        raise KernelError(f"extra fields may not override computed fields {clash}")
    record.update(inputs.extra)

    ceiling, reasons = confidence_ceiling(
        record,
        policy,
        earnings_within_window=inputs.earnings_within_window
        or earnings_in_window(record, policy),
    )
    if CONFIDENCE_ORDER.index(inputs.confidence) > CONFIDENCE_ORDER.index(ceiling):
        raise KernelError(
            f"confidence {inputs.confidence} exceeds the ceiling {ceiling}: "
            + "; ".join(reasons)
        )
    if band.sleeve == "INVESTABLE" and not investability(record, policy):
        record["sleeve"] = "INVESTABLE"
    return record


@dataclass(frozen=True)
class MarketInputs:
    """One core ETF: grounded data plus the model's judgment calls."""

    ticker: str
    entry_price: float
    price_tag: str
    price_date: str
    sigma: float
    sigma_source: str
    thesis: str
    beta_vs_spy: float | None = None  # required for every ETF but SPY
    mu_adjustment: float = 0.0
    mu_adjustment_reason: str = ""
    confidence: str = "MEDIUM"
    horizon_days: int | None = None
    ledger_rows: tuple[str, ...] = ()

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "MarketInputs":
        values = dict(data)
        unknown = sorted(set(values) - {f.name for f in dataclasses.fields(cls)})
        if unknown:
            raise KernelError(f"unknown market input(s) {unknown}")
        values["ledger_rows"] = tuple(values.get("ledger_rows", ()))
        try:
            return cls(**values)
        except TypeError as exc:
            raise KernelError(str(exc)) from None


def market_forecast_records(
    run_date: str,
    model: str,
    regime: str,
    inputs: Sequence[MarketInputs],
    policy: Policy,
) -> list[dict[str, Any]]:
    """``rules.md`` § Core ETF Market Forecast: SPY from the regime prior, the
    others as ``beta x SPY mu``, each within its adjustment band."""
    tickers = list(policy.get("market_forecast.tickers"))
    given = [i.ticker for i in inputs]
    if sorted(given) != sorted(tickers):
        raise KernelError(f"core ETF inputs {given} must be exactly {tickers}")
    priors = policy.get("market_forecast.spy_regime_prior")
    if regime not in priors:
        raise KernelError(f"regime {regime!r} not in {list(priors)}")
    ordered = sorted(inputs, key=lambda i: tickers.index(i.ticker))
    records: list[dict[str, Any]] = []
    spy_mu = 0.0
    for item in ordered:
        _require("price_tag", item.price_tag, PRICE_TAGS)
        _require("sigma_source", item.sigma_source, SIGMA_SOURCES)
        _require("confidence", item.confidence, CONFIDENCE)
        if item.ticker == "SPY":
            prior = policy.spy_mu_prior(regime)
            limit = policy.num("market_forecast.spy_adjustment_max")
            derivation = f"regime prior for {regime}"
        else:
            if item.beta_vs_spy is None:
                raise KernelError(f"{item.ticker} needs beta_vs_spy (60d, DERIVED)")
            prior = item.beta_vs_spy * spy_mu
            limit = policy.num("market_forecast.beta_scaled_adjustment_max")
            derivation = (
                f"beta {item.beta_vs_spy:.4f} x SPY mu {spy_mu:+.4%} = {prior:+.4%}"
            )
        mu = _adjust(prior, item.mu_adjustment, item.mu_adjustment_reason, limit)
        if item.ticker == "SPY":
            spy_mu = mu
        derivation += (
            f"; adjustment {item.mu_adjustment * 100:+.2f}pp: "
            f"{item.mu_adjustment_reason}"
            if item.mu_adjustment
            else "; no adjustment applied"
        )
        record: dict[str, Any] = {
            "run_date": run_date,
            "model": model,
            "ticker": item.ticker,
            "type": "MARKET_FORECAST",
            "entry_price": item.entry_price,
            "price_tag": item.price_tag,
            "price_date": item.price_date,
            "mu": _round(mu),
            "mu_prior": _round(prior),
            "mu_adjustment": item.mu_adjustment,
            "mu_derivation": derivation,
            "sigma": _round(item.sigma),
            "sigma_source": item.sigma_source,
            **_price_fields(item.entry_price, mu, item.sigma, policy),
            "target_date": _target_date(run_date, item.horizon_days, policy),
            "benchmark": "NONE",
            "benchmark_price": None,
            "adj_score": None,
            "beta_vs_spy": item.beta_vs_spy,
            "confidence": item.confidence,
            "status": "OPEN",
            "thesis": item.thesis,
            "score_explainability": None,
            "ledger_rows": list(item.ledger_rows),
        }
        if item.mu_adjustment:
            record["mu_adjustment_reason"] = item.mu_adjustment_reason
        records.append(record)
    return records


def predictions_payload(
    *,
    run_date: str,
    model: str,
    run_status: str,
    data_mode: str,
    regime: str,
    predictions: Sequence[Mapping[str, Any]],
    settlements: Sequence[Mapping[str, Any]] = (),
    **extra: Any,
) -> dict[str, Any]:
    """A schema-v1 ``15_predictions.json`` payload around built records."""
    _require("data_mode", data_mode, DATA_MODES)
    return {
        "schema_version": SCHEMA_VERSION,
        "run_date": run_date,
        "model": model,
        "run_status": run_status,
        "data_mode": data_mode,
        "regime": regime,
        **extra,
        "predictions": [dict(p) for p in predictions],
        "settlements": [dict(s) for s in settlements],
    }


@dataclass(frozen=True)
class Holding:
    """One proposed position: a NAV weight plus its own adjusted closes."""

    ticker: str
    weight: float  # fraction of NAV; the rest of NAV is cash (beta 0, vol 0)
    sector: str  # GICS sector
    closes: Sequence[float]  # date-aligned with the SPY closes, oldest first
    earnings_within_window: bool = False

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "Holding":
        unknown = sorted(set(data) - {f.name for f in dataclasses.fields(cls)})
        if unknown:
            raise KernelError(f"unknown holding field(s) {unknown}")
        try:
            return cls(**data)
        except TypeError as exc:
            raise KernelError(str(exc)) from None


@dataclass(frozen=True)
class PortfolioRisk:
    """Portfolio analytics and the protected limits they breach.

    ``breaches`` feeds ``decide_status(risk_breaches=...)`` directly, so the
    status no longer depends on a model transcribing its own risk review.
    Beta and sector weight come on both bases; ``basis`` says which one the
    beta band and sector cap were checked on (``risk.exposure_basis``).
    """

    names: int
    gross: float
    basis: str  # NAV | INVESTED
    max_name_weight: float
    sector_weights: dict[str, float]  # fraction of NAV
    sector_shares: dict[str, float]  # fraction of gross
    beta_vs_spy: float  # NAV: sum(w * beta), cash at beta 0
    invested_beta: float  # beta_vs_spy / gross
    sigma_1m: float  # NAV: sqrt(w' S w), one-month scale
    dd95_1m: float  # parametric: var95_z * sigma_1m, normality assumed
    avg_pairwise_corr: float | None  # None with fewer than two names
    earnings_names: tuple[str, ...]
    breaches: tuple[str, ...]


def _corr(a: Sequence[float], b: Sequence[float]) -> float:
    sa, sb = statistics.pstdev(a), statistics.pstdev(b)
    mean_a, mean_b = statistics.fmean(a), statistics.fmean(b)
    cov = statistics.fmean([(x - mean_a) * (y - mean_b) for x, y in zip(a, b)])
    return cov / (sa * sb)


def portfolio_feasibility(
    holdings: Sequence[Holding], spy_closes: Sequence[float], policy: Policy
) -> PortfolioRisk:
    """``rules.md`` § Computed Risk Analytics 1-4 and § Risk Controls /
    Portfolio Level, checked against the policy's protected limits.

    Weights are NAV fractions, so uninvested NAV is cash: it adds nothing to
    beta or sigma. The drawdown cap is a loss of NAV and is always checked on
    NAV. The beta band and sector cap are checked on ``risk.exposure_basis``:
    on ``NAV`` a book capped at 5% a name and 10 names (50% gross) can reach
    the 0.90 beta floor only if its average beta is 1.8 or more, which is why
    past runs disagree on the basis (plan/2026-09-28 §6, decision 7).

    Every series uses the latest 61 closes (60 intervals) and population
    moments, as ``price_risk`` does. Factor crowding is not checked here: it
    needs per-name family contributions, not prices.
    """
    basis = str(policy.get("risk.exposure_basis"))
    if basis not in ("NAV", "INVESTED"):
        raise KernelError(f"risk.exposure_basis={basis!r} not in ['NAV', 'INVESTED']")
    if not holdings:
        raise KernelError("no holdings: a portfolio needs at least one name")
    tickers = [h.ticker for h in holdings]
    if len(set(tickers)) != len(tickers):
        raise KernelError(f"duplicate tickers in {tickers}")
    for h in holdings:
        if not math.isfinite(h.weight) or h.weight <= 0:
            raise KernelError(f"{h.ticker}: weight {h.weight} must be positive")
        if not h.sector.strip():
            raise KernelError(f"{h.ticker}: a GICS sector is required")
    gross = math.fsum(h.weight for h in holdings)
    if gross > 1 + 1e-9:
        raise KernelError(f"gross {gross:.4f} exceeds NAV: long-only, no leverage")
    spy = daily_returns(_window("spy_closes", spy_closes))
    returns = [daily_returns(_window(h.ticker, h.closes)) for h in holdings]
    for h, r in zip(holdings, returns):
        if statistics.pstdev(r) == 0:
            raise KernelError(
                f"{h.ticker}: zero return variance, correlation undefined"
            )
    weights = [h.weight for h in holdings]
    betas = [_beta(r, spy) for r in returns]
    beta = math.fsum(w * b for w, b in zip(weights, betas))
    # Portfolio daily return series: the quadratic form w' S w without the matrix.
    book = [
        math.fsum(w * r[t] for w, r in zip(weights, returns)) for t in range(len(spy))
    ]
    sigma = statistics.pstdev(book) * MONTH
    dd95 = policy.num("forecast.var95_z") * sigma
    pairs = [_corr(a, b) for a, b in combinations(returns, 2)]
    avg_corr = statistics.fmean(pairs) if pairs else None
    sectors: dict[str, float] = {}
    for h in holdings:
        sectors[h.sector] = sectors.get(h.sector, 0.0) + h.weight
    earnings = tuple(h.ticker for h in holdings if h.earnings_within_window)

    breaches: list[str] = []
    cap = policy.num("risk.max_single_name_weight")
    for h in holdings:
        if h.weight > cap + 1e-9:
            breaches.append(
                f"{h.ticker} weight {h.weight:.2%} > {cap:.0%} single-name cap"
            )
    shares = {sector: weight / gross for sector, weight in sectors.items()}
    invested = beta / gross
    sector_cap = policy.num("risk.max_sector_weight")
    checked = sectors if basis == "NAV" else shares
    for sector, weight in sorted(checked.items()):
        if weight > sector_cap + 1e-9:
            breaches.append(
                f"{sector} {weight:.2%} of {basis} > {sector_cap:.0%} sector cap"
            )
    lo, hi = (float(x) for x in policy.get("risk.beta_band"))
    checked_beta = beta if basis == "NAV" else invested
    if not lo <= checked_beta <= hi:
        note = (
            f" (invested-book beta {invested:.2f} at gross {gross:.0%})"
            if basis == "NAV" and gross < 1 - 1e-9
            else ""
        )
        breaches.append(
            f"{basis} beta {checked_beta:.2f} outside {lo:.2f}-{hi:.2f}{note}"
        )
    corr_cap = policy.num("risk.max_avg_pairwise_corr")
    if avg_corr is not None and avg_corr >= corr_cap:
        breaches.append(f"avg pairwise corr {avg_corr:.2f} >= {corr_cap:.2f}")
    dd_cap = policy.num("risk.max_dd95_1m")
    if dd95 > dd_cap + 1e-12:
        breaches.append(f"dd95 1m {dd95:.2%} > {dd_cap:.0%}")
    max_earnings = int(policy.num("evidence.max_earnings_names"))
    if len(earnings) > max_earnings:
        breaches.append(
            f"{len(earnings)} names with earnings inside the window "
            f"(> {max_earnings}): {', '.join(earnings)}"
        )
    return PortfolioRisk(
        names=len(holdings),
        gross=gross,
        basis=basis,
        max_name_weight=max(weights),
        sector_weights=dict(sorted(sectors.items())),
        sector_shares=dict(sorted(shares.items())),
        beta_vs_spy=beta,
        invested_beta=invested,
        sigma_1m=sigma,
        dd95_1m=dd95,
        avg_pairwise_corr=avg_corr,
        earnings_names=earnings,
        breaches=tuple(breaches),
    )
