"""Scoring kernel: slot z-scores, family z, the score trace, and the percentile.

"This run's engine was written from rules.md" (opus-5 07-27). Every run
re-implemented the cross-sectional scoring, and the history shows what that
cost: a drawdown polarity flip (08-03), a 61-vs-60-close window (08-04), a
macro score nobody could reproduce. The normative Metric Definition Table
(Track B, shipped 2026-08-04, carried in each ``05_factor_scores.md`` since) is
implemented once here:

* slot raw values from a ``technical_indicators.py`` record plus ``price_risk``,
  with the table's transforms and polarity;
* per slot, a cross-sectional z: winsorize at the 5th/95th percentile by
  clipping, then the population z of the clipped series, via
  ``factor_scoring.py`` (the helper the SHADOW tools already use);
* family z: the mean of available slot z, ``UNAVAILABLE`` with too few slots;
* composite and Adj Score from the policy, and the universe percentile
  ``100 * (n - rank) / (n - 1)`` (``INDEX_UNION_PCTL``).

The slot list per family lives in the policy. Data quality and penalties stay
inputs: the rules give guideposts for them, not a formula.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from financial_agent.harness.helpers import load_helper
from financial_agent.harness.kernels import KernelError, PriceRisk, price_risk
from financial_agent.harness.policy import FAMILIES, Policy

MA_CODES = {"BULLISH": 1.0, "MIXED": 0.0, "BEARISH": -1.0}
MACD_CODES = {
    "BULLISH_CROSS": 2.0,
    "ABOVE_SIGNAL": 1.0,
    "ON_SIGNAL": 0.0,
    "BELOW_SIGNAL": -1.0,
    "BEARISH_CROSS": -2.0,
}
# Every slot the transforms below define; the policy picks which ones score.
SLOTS = (
    "mom20",
    "mom60",
    "ma_align",
    "macd",
    "vol_conf",
    "dd60",
    "beta",
    "sector_lead",
    "rate_sens",
    "vol_stability",
)


@dataclass(frozen=True)
class NameInputs:
    """One eligible name: its indicator record, sector, and price risk."""

    ticker: str
    sector: str | None
    indicators: Mapping[str, Any]  # one ``technical_indicators.py`` record
    risk: PriceRisk | None = None


def _num(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _encoded(
    indicators: Mapping[str, Any], key: str, codes: Mapping[str, float]
) -> float | None:
    """Mean of the daily and weekly codes; ``None`` unless both are known."""
    values = []
    for frame in ("daily", "weekly"):
        block = indicators.get(frame)
        code = codes.get(str(block.get(key))) if isinstance(block, Mapping) else None
        if code is None:
            return None
        values.append(code)
    return sum(values) / len(values)


def raw_slots(name: NameInputs) -> dict[str, float | None]:
    """Post-transform slot values, higher is better (``sector_lead`` is set
    across the universe by ``score_universe``)."""
    indicators = name.indicators if name.indicators.get("status", "OK") == "OK" else {}
    daily = indicators.get("daily")
    daily = daily if isinstance(daily, Mapping) else {}
    risk = name.risk
    return {
        "mom20": _num(daily.get("momentum_20d_pct")),
        "mom60": _num(daily.get("momentum_60d_pct")),
        "ma_align": _encoded(indicators, "ma_alignment", MA_CODES),
        "macd": _encoded(indicators, "macd_state", MACD_CODES),
        "vol_conf": _num(daily.get("volume_ratio_20d")),
        # Stored signed (<= 0): a shallower drawdown is already higher.
        "dd60": None if risk is None else risk.max_drawdown_60d,
        "beta": None if risk is None else -abs(risk.beta_60d_vs_spy - 1.0),
        "sector_lead": None,
        "rate_sens": (
            None
            if risk is None or risk.beta_60d_vs_tlt is None
            else -abs(risk.beta_60d_vs_tlt)
        ),
        "vol_stability": (
            None
            if risk is None or risk.vol_60d <= 0
            else -(risk.realized_vol_30d / risk.vol_60d)
        ),
    }


@dataclass(frozen=True)
class SlotStats:
    """The cross-section behind one slot's z-scores (the 05 dispersion table)."""

    slot: str
    family: str
    n: int
    coverage: float
    scored: bool  # False: too few names carry it, so it never enters Adj Score
    clip_lo: float | None = None
    clip_hi: float | None = None
    mean: float | None = None
    stdev: float | None = None
    min_z: float | None = None
    median_z: float | None = None
    max_z: float | None = None


@dataclass(frozen=True)
class ScoredName:
    ticker: str
    sector: str | None
    raw: dict[str, float | None]
    slot_z: dict[str, float | None]
    family_z: dict[str, float | None]
    composite_z: float
    data_quality_multiplier: float
    penalties: float
    adj_score: float
    rank: int
    pctl: float

    def equity_fields(self) -> dict[str, Any]:
        """The scored inputs ``EquityInputs`` takes, so none is retyped."""
        return {
            "pctl": self.pctl,
            "family_z": dict(self.family_z),
            "data_quality_multiplier": self.data_quality_multiplier,
            "penalties": self.penalties,
        }


@dataclass(frozen=True)
class Scoreboard:
    names: list[ScoredName]  # by rank
    slots: list[SlotStats] = field(default_factory=list)

    def get(self, ticker: str) -> ScoredName:
        return next(n for n in self.names if n.ticker == ticker)

    def slot_table(self) -> str:
        """Markdown dispersion table, generated rather than transcribed."""
        lines = [
            "| Slot | Family | n | coverage | min z | median z | max z |",
            "|---|---|---|---|---|---|---|",
        ]
        for s in self.slots:
            if not s.scored:
                lines.append(
                    f"| `{s.slot}` | {s.family} | {s.n} | {s.coverage:.0%} | "
                    "not scored | | |"
                )
                continue
            lines.append(
                f"| `{s.slot}` | {s.family} | {s.n} | {s.coverage:.0%} | "
                f"{s.min_z:+.4f} | {s.median_z:+.4f} | {s.max_z:+.4f} |"
            )
        return "\n".join(lines)


def _family_slots(policy: Policy) -> dict[str, list[str]]:
    slots = {family: list(names) for family, names in policy.get("score.slots").items()}
    for family, names in slots.items():
        if family not in FAMILIES:
            raise KernelError(f"score.slots names unknown family {family!r}")
        if family in policy.shadow_families:
            raise KernelError(f"{family} is SHADOW: its slots may not score")
        unknown = sorted(set(names) - set(SLOTS))
        if unknown:
            raise KernelError(f"score.slots.{family} names unknown slots {unknown}")
    return slots


def _per_name(value: float | Mapping[str, float], ticker: str, name: str) -> float:
    if isinstance(value, Mapping):
        if ticker not in value:
            raise KernelError(f"{name} missing for {ticker}")
        value = value[ticker]
    return float(value)


def score_universe(
    names: Sequence[NameInputs],
    policy: Policy,
    *,
    data_quality: float | Mapping[str, float],
    penalties: Mapping[str, float] | None = None,
) -> Scoreboard:
    """Score every eligible name and rank the universe by Adj Score."""
    if not names:
        raise KernelError("no names to score")
    tickers = [n.ticker for n in names]
    if len(set(tickers)) != len(tickers):
        raise KernelError("duplicate tickers in the universe")
    family_slots = _family_slots(policy)
    scoring = load_helper("factor_scoring")

    raw = {n.ticker: raw_slots(n) for n in names}
    by_sector: dict[str, list[float]] = {}
    for name in names:
        mom60 = raw[name.ticker]["mom60"]
        if name.sector and mom60 is not None:
            by_sector.setdefault(name.sector, []).append(mom60)
    for name in names:
        members = by_sector.get(name.sector or "")
        raw[name.ticker]["sector_lead"] = (
            statistics.median(members) if members else None
        )

    slot_family = {s: f for f, slots in family_slots.items() for s in slots}
    minimum = policy.num("score.min_slot_coverage")
    stats: list[SlotStats] = []
    usable: dict[str, dict[str, float | None]] = {t: {} for t in tickers}
    for slot, family in slot_family.items():
        values = [raw[t][slot] for t in tickers if raw[t][slot] is not None]
        coverage = len(values) / len(tickers)
        scored = coverage >= minimum and len(values) >= 2
        for t in tickers:
            usable[t][slot] = raw[t][slot] if scored else None
        if not scored:
            stats.append(SlotStats(slot, family, len(values), coverage, False))
            continue
        clipped = scoring.winsorize(values)
        stats.append(
            SlotStats(
                slot,
                family,
                len(values),
                coverage,
                True,
                clip_lo=min(clipped),
                clip_hi=max(clipped),
                mean=statistics.fmean(clipped),
                stdev=statistics.pstdev(clipped),
            )
        )
    z = scoring.zscore_cross_sectionally(usable, tuple(slot_family), set())
    stats = [
        (
            s
            if not s.scored
            else SlotStats(
                **{
                    **vars(s),
                    "min_z": min(v for t in tickers if (v := z[t][s.slot]) is not None),
                    "median_z": statistics.median(
                        v for t in tickers if (v := z[t][s.slot]) is not None
                    ),
                    "max_z": max(v for t in tickers if (v := z[t][s.slot]) is not None),
                }
            )
        )
        for s in stats
    ]

    min_slots = int(policy.num("score.min_family_slots"))
    unranked = []
    for name in names:
        t = name.ticker
        family_z: dict[str, float | None] = {f: None for f in FAMILIES}
        for family, slots in family_slots.items():
            family_z[family] = scoring.composite_z(
                {s: z[t][s] for s in slots}, min_signals=min_slots
            )[0]
        dq = _per_name(data_quality, t, "data_quality")
        if not 0 < dq <= 1:
            raise KernelError(f"data_quality {dq} for {t} outside (0, 1]")
        penalty = _per_name((penalties or {}).get(t, 0.0), t, "penalties")
        composite = policy.composite_z(family_z)
        unranked.append((t, name.sector, family_z, composite, dq, penalty))

    adj = {t: policy.adj_score(c, dq, pen) for t, _, _, c, dq, pen in unranked}
    n = len(unranked)
    scored_names = []
    for t, sector, family_z, composite, dq, penalty in unranked:
        rank = 1 + sum(1 for other in adj.values() if other > adj[t])
        scored_names.append(
            ScoredName(
                ticker=t,
                sector=sector,
                raw=raw[t],
                slot_z={s: z[t][s] for s in slot_family},
                family_z=family_z,
                composite_z=composite,
                data_quality_multiplier=dq,
                penalties=penalty,
                adj_score=adj[t],
                rank=rank,
                pctl=100.0 if n == 1 else 100.0 * (n - rank) / (n - 1),
            )
        )
    scored_names.sort(key=lambda s: (s.rank, s.ticker))
    return Scoreboard(scored_names, stats)


def score_request(request: Mapping[str, Any], policy: Policy) -> dict[str, Any]:
    """JSON in, JSON out, for the CLI and the MCP server.

    ``indicators`` is a ``technical_indicators.py`` payload (or its list);
    ``sectors`` maps ticker to sector; per-name risk comes from ``risk``
    (``PriceRisk`` fields) or from ``closes`` with ``spy_closes`` and optional
    ``tlt_closes``. ``universe`` defaults to every indicator record except the
    core ETFs, which never count toward percentile distributions.
    """
    records = request["indicators"]
    if isinstance(records, Mapping):
        records = records["indicators"]
    by_ticker = {str(r["ticker"]): r for r in records}
    etfs = set(policy.get("market_forecast.tickers"))
    universe = request.get("universe") or [t for t in by_ticker if t not in etfs]
    sectors = request.get("sectors") or {}
    risks = request.get("risk") or {}
    closes = request.get("closes") or {}
    names = []
    for ticker in universe:
        if ticker not in by_ticker:
            raise KernelError(f"{ticker} has no indicator record")
        if ticker in risks:
            risk: PriceRisk | None = PriceRisk(**risks[ticker])
        elif ticker in closes:
            risk = price_risk(
                closes[ticker],
                request["spy_closes"],
                tlt_closes=request.get("tlt_closes"),
            )
        else:
            risk = None
        names.append(NameInputs(ticker, sectors.get(ticker), by_ticker[ticker], risk))
    board = score_universe(
        names,
        policy,
        data_quality=request["data_quality"],
        penalties=request.get("penalties"),
    )
    return {
        "names": [vars(n) for n in board.names],
        "slots": [vars(s) for s in board.slots],
    }
