# 03 Regime And Data

## Preflight Summary

Data state is `DELAYED_PARTIAL`. The run has enough source-backed information for regime classification and review-only candidate monitoring, but not enough for live sizing or `GO`.

## Regime Classification

| Regime Label | Evidence | Source Ledger Rows | Confidence |
|---|---|---|---|
| HIGH_VOL | VIX 19.55 versus prior close 18.92, delayed at least 20 minutes on Cboe page. | L001, L002 | MEDIUM |
| RATE_SHOCK | Official 10-year Treasury observation 4.55% on 2026-06-05. | L003 | MEDIUM |
| Defensive rotation | SPY -0.55%, XLV +1.48%, XLP +1.00% in the sampled session. | L004-L006 | MEDIUM |

Final regime label: `HIGH_VOL / RATE_SHOCK`.

## Data Mode Decision

| Data Class | Coverage | Downstream Use |
|---|---|---|
| Prices | Partial delayed | Allowed for review-only monitoring and MoM reflection. |
| Beta | Partial sampled universe | Allowed for review-only ranking, not enough for portfolio approval. |
| Fundamentals | Partial sampled universe | Allowed for review-only ranking. |
| Earnings dates | Partial sampled universe | Allowed for immediate event-risk screen, but no full calendar feed. |
| Options IV/skew | Missing | Blocks sigma, CI, and `GO`. |
| Short interest / borrow | Missing as complete feed | Blocks `GO`. |
| Execution liquidity | Missing | Blocks `GO`. |
| Covariance / drawdown | Missing | Blocks `GO`. |

## Universe Summary

| Universe Step | Count | Notes |
|---|---:|---|
| Initial sampled names | 18 | Prior run monitors, defensive rotation names, mega-cap reflection names, and financial/energy diversifiers. |
| Source-backed candidate pages | 10 | MCK, PG, WMT, ABBV, JPM, XOM, AZO, UNH, CAT, GS. |
| Review-only monitor names | 8 | MCK, PG, WMT, ABBV, JPM, XOM, AZO, UNH. |
| Near misses / exclusions | 2 | CAT and GS. |
| Full U.S. universe screened | 0 | No full universe feed; this is a sampled review-only run. |

## Rejection Log

| Ticker | Rejection Reason | Source Ledger Rows |
|---|---|---|
| CAT | High beta 1.60 and only +2.62% consensus target upside; useful cyclical cross-check but not preferred under `HIGH_VOL / RATE_SHOCK`. | L070-L074 |
| GS | Analyst consensus `Hold` and target downside despite strong earnings growth; event date July 14. | L075-L079 |
| MSFT | Downgraded by reflection; no source-backed short-horizon catalyst strong enough to override. | L011-L013 |
| NVDA | Dropped by reflection after -6.31% MoM return and high-beta chip risk. | L014-L016 |
| META | Downgraded by reflection; negative MoM return. | L017-L019 |
| GOOGL | Dropped by reflection; negative MoM return. | L020-L022 |
| AMZN | Dropped by reflection; negative MoM return. | L023-L025 |

## Handoff To Factor Scoring

Rank only the review-only monitor set. Do not mark any name investable because complete data coverage, IV/skew, short-interest, execution-quality liquidity, and covariance/drawdown inputs are unavailable (L090-L093).
