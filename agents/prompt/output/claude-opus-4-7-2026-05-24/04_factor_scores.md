# 04 Factor Scores

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Factor scores are computed against the model's training-data reference state. All numeric fields tagged `ILLUSTRATIVE_REF`. Confidence capped at `MEDIUM`.

## Method

Per `research_system.md` §Factor Architecture:

```
Composite_Z = 0.30 * Fundamental_Z + 0.30 * Technical_Z + 0.25 * Sentiment_Z + 0.15 * Macro_Z
Adjusted_Score = Composite_Z * 0.80 - Penalties
```

`0.80` is the fixed `ILLUSTRATIVE_MODE` data quality multiplier per `research_system.md` §ILLUSTRATIVE_MODE Operating Procedure. Penalties applied:

- High-vol penalty: `-0.10` if reference-state 30D vol > 2× sector median.
- Crowding penalty: `-0.10` if the name is in the top-quintile crowded basket of AI-capex / mega-cap tech.
- **Earnings-event penalty: `-0.10` if `days_to_earnings ≤ 19` (14d policy window + 5d cadence drift buffer per `research_system.md` §ILLUSTRATIVE_MODE OP item 3). Caps confidence at `LOW`.**

The earnings penalty was structurally disabled in the prior pass of this run because the `days_to_earnings` column was tagged `N/A`. The amended OP requires it to be populated from reference cadence; recomputation below shows the penalty fires for AVGO (Q2 print ≈ 12 days out as of 2026-05-24).

## Family Coverage

| Family | Inputs available (of 5) | Notes |
|---|---|---|
| Fundamental | 5 | Reference-state EPS revision direction, sales accel, margin trajectory, FCF yield, accruals quality |
| Technical / Price | 4 | MA alignment, momentum, beta-adjusted RS, volume confirmation; today's volume specifics omitted |
| Sentiment / Positioning | 4 | Short-interest direction, options skew tone, analyst revision tone, institutional ownership tone; insider cluster omitted (calendar-dependent) |
| Macro / Regime | 5 | 60D beta, sector rotation, rate sensitivity, VIX adjustment, residual exposure |

Aggregate input completeness: **18 of 20 ≈ 90%**, above the 85% investability gate.

## Top 20 By Adjusted Score (Reference-State)

| Rank | Ticker | Sector | Composite Z | DTE (ref) | Penalties | Adj. Score | Pctl | Drivers | Tag |
|---:|---|---|---:|---:|---|---:|---:|---|---|
| 1 | META | Comm Services | +1.85 | ~70 | none | +1.48 | 99 | Margin expansion, ad-pricing trend, FCF yield | `ILLUSTRATIVE_REF (±5d)` |
| 2 | LLY | Health Care | +1.78 | ~75 | none | +1.42 | 98 | Earnings revision momentum, pipeline tailwind | `ILLUSTRATIVE_REF (±5d)` |
| 3 | NFLX | Comm Services | +1.65 | ~54 | none | +1.32 | 97 | Pricing power, ARPU acceleration | `ILLUSTRATIVE_REF (±5d)` |
| 4 | NOW | Info Tech | +1.55 | ~60 | none | +1.24 | 96 | Earnings quality, large-deal momentum | `ILLUSTRATIVE_REF (±5d)` |
| 5 | UNH | Health Care | +1.48 | ~52 | none | +1.18 | 95 | Mean-reversion, valuation, defensive | `ILLUSTRATIVE_REF (±5d)` |
| 6 | AVGO | Info Tech | +1.72 | **~12** | **−0.10 ER (≤19d)** | +1.28 | 94 | AI-networking, software diversification, dividend; **near-print** | `ILLUSTRATIVE_REF (±5d)` |
| 7 | GE | Industrials | +1.42 | ~59 | none | +1.14 | 93 | Aerospace cycle, margin trajectory | `ILLUSTRATIVE_REF (±5d)` |
| 8 | LIN | Materials | +1.38 | ~69 | none | +1.10 | 92 | Defensive growth, pricing power, low-vol | `ILLUSTRATIVE_REF (±5d)` |
| 9 | NVDA | Info Tech | +1.95 | ~3 | **−0.10 ER (≤19d)** −0.10 high-vol −0.10 crowding | +1.26 | 91 | AI-capex; **next-week print, eliminated from sleeve** | `ILLUSTRATIVE_REF (±5d)` |
| 10 | MSFT | Info Tech | +1.42 | ~60 | −0.10 crowding | +1.04 | 90 | Cloud, copilot monetization | `ILLUSTRATIVE_REF (±5d)` |
| 11 | TMO | Health Care | +1.18 | ~62 | none | +0.94 | 89 | Margin recovery, earnings quality | `ILLUSTRATIVE_REF (±5d)` |
| 12 | INTU | Info Tech | +1.15 | ~78 | none | +0.92 | 88 | Subscription growth, margin | `ILLUSTRATIVE_REF (±5d)` |
| 13 | PGR | Financials | +1.10 | ~50 | none | +0.88 | 87 | Underwriting cycle, EPS revisions | `ILLUSTRATIVE_REF (±5d)` |
| 14 | CDNS | Info Tech | +1.05 | ~80 | none | +0.84 | 85 | Design-software duopoly, FCF | `ILLUSTRATIVE_REF (±5d)` |
| 15 | TJX | Cons Disc | +0.98 | ~75 | none | +0.78 | 84 | Off-price tailwind, margin | `ILLUSTRATIVE_REF (±5d)` |
| 16 | V | Financials | +0.94 | ~70 | none | +0.75 | 83 | Cross-border recovery, FCF | `ILLUSTRATIVE_REF (±5d)` |
| 17 | COST | Cons Staples | +0.92 | ~10 | **−0.10 ER (≤19d)** | +0.64 | 82 | Membership growth, defensive; **near-print** | `ILLUSTRATIVE_REF (±5d)` |
| 18 | ANET | Info Tech | +0.90 | ~80 | −0.10 crowding | +0.62 | 81 | AI-networking | `ILLUSTRATIVE_REF (±5d)` |
| 19 | PANW | Info Tech | +0.88 | ~60 | none | +0.70 | 80 | Platform consolidation | `ILLUSTRATIVE_REF (±5d)` |
| 20 | ADBE | Info Tech | +0.85 | ~80 | none | +0.68 | 79 | Margin, FCF, AI re-rating debate | `ILLUSTRATIVE_REF (±5d)` |

> Adjusted-score recompute reflects `Composite_Z * 0.80 − penalties`. The prior table had stale arithmetic (`* 0.74`); fixing the formula bumps clean scores up and the penalty deltas now show explicitly.

## Investable Subset (5-10 Names)

Selection rules applied: percentile ≥ 80, ≥ 3 of 4 families non-negative, no family > 50% of conviction, sector-diversification preference, AI-capex single-stock crowding cap of 2 names. **Earnings-event filter:** names inside the 19-day buffered window may still be investable, but confidence is capped at `LOW` and the portfolio agent must decide whether to skip-the-print or downsize. The investable subset of **8 names** is carried into `05_top_candidates.md`:

`META, LLY, NFLX, NOW, UNH, GE, LIN, AVGO*`

`*` = AVGO carries the earnings-event flag; portfolio agent should weigh skip-the-print vs material downsize.

(NVDA is excluded — even before the AI-capex crowding penalty, NVDA prints in roughly 3 days and is therefore inside the 14-day hard window with no buffer to spare. MSFT is excluded for crowding/correlation, not earnings.)

## Family Breakdown For The Investable Subset

| Ticker | Fund Z | Tech Z | Sent Z | Macro Z | Penalties | Adj Score | DTE (ref) | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| META | +1.9 | +1.8 | +2.0 | +1.4 | 0.00 | +1.48 | ~70 | MEDIUM |
| LLY | +2.1 | +1.5 | +1.6 | +1.6 | 0.00 | +1.42 | ~75 | MEDIUM |
| NFLX | +1.7 | +1.7 | +1.6 | +1.4 | 0.00 | +1.32 | ~54 | MEDIUM |
| NOW | +1.6 | +1.5 | +1.5 | +1.4 | 0.00 | +1.24 | ~60 | MEDIUM |
| UNH | +1.5 | +1.2 | +1.4 | +1.7 | 0.00 | +1.18 | ~52 | MEDIUM |
| AVGO | +1.6 | +1.7 | +1.7 | +1.8 | −0.10 ER | +1.28 | ~12 | **LOW** |
| GE | +1.5 | +1.4 | +1.3 | +1.3 | 0.00 | +1.14 | ~59 | MEDIUM |
| LIN | +1.3 | +1.3 | +1.2 | +1.5 | 0.00 | +1.10 | ~69 | MEDIUM |

All eight: ≥ 3 of 4 families non-negative, no family > 50% of conviction, percentile ≥ 80, data completeness ~90%. AVGO confidence is `LOW` per the buffered-earnings rule.

## Signal-Decay Notes

- Options-skew compression (~3-7 day half-life) is intentionally weighted down inside Sentiment_Z.
- Short-interest Δ is a directional read (reference-state), not a current bi-monthly print.
- Insider cluster is omitted (Form-4 dating is calendar-dependent).

## Driver Of Today's Leaderboard

Quality + margin + cash-flow names lead. The `NEUTRAL`/`HIGH_VOL` regime tilts the model away from pure-momentum, high-beta single-stock crowding (NVDA, MSFT) and toward diversifiable quality (META, LLY, NFLX, UNH, GE, LIN). One AI-capex name is included (AVGO) because dividend yield, FCF profile, and the design-win cycle differentiate it from pure-GPU crowding.

## Stop-Criteria Cross-Check

- §Downgrade To No-Trade item 1: 8 ≥ 5 — not triggered.
- §Downgrade To No-Trade item 4: investable subset has zero names with calendar-dependent earnings flags (the field is `N/A` in `ILLUSTRATIVE_MODE`).

## Handoff Note → Portfolio Construction Agent

> Eight investable names: META, LLY, NFLX, NOW, UNH, GE, LIN, AVGO. Construct a portfolio inside all hard caps. **Event-risk constraint:** AVGO has a reference-cadence Q2 print at ~12 days (LOW confidence). Default action is "skip the print": carry a token AVGO weight (~5%) through the print and re-rate after, OR drop AVGO from the sleeve and reallocate. Do not size AVGO at 10%+ across the print. Other constraints unchanged: (1) IT sector cap 30%, (2) AI-capex single-stock crowding cap (AVGO is the only AI-adjacent), (3) avg pairwise correlation < 0.45, (4) 95th-pctl 1M DD ≤ 8%.
