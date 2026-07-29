# 04 Universe Summary — 2026-07-29

## Construction

Index-union path succeeded — the normal daily path, not the emergency sample.

| Field | Value | Source |
|---|---|---|
| S&P 500 constituents | 503 | `agents/equity/turtle-trader/universe/sp500.json` (fetched 2026-06-21T21:05:56Z) |
| Nasdaq-100 constituents | 101 | `agents/equity/turtle-trader/universe/nasdaq100.json` (fetched 2026-06-21T21:05:56Z) |
| Overlap | 89 | — |
| **Union** | **515** | `eligible_universe.txt` |
| Scored after filters | **514** | `run_computed_manifest.json` |

All percentile ranks in this package are labeled **`INDEX_UNION_PCTL (n=514)`**. The Sampled Universe
Protocol was **not** used and is not applicable — `build_index_universe.py` succeeded.

Constituent caches were fetched 2026-06-21, 38 days before this run. Per
`rules.md § Index-Union Universe Protocol` #5 a stale cache is used as-is and logged; refreshing it is
a maintenance task and never a reason to fall back to 30 names.

## Inclusion / Exclusion Log

Filters per `rules.md § Universe Construction`, applied to all 515 union names.

| Filter | Threshold | Excluded |
|---|---|---|
| Listing age | > 6 months | **1** |
| Market cap | > $2B | 0 |
| Avg daily dollar volume | > $20M over 20 sessions | 0 |
| Price | > $5 | 0 |
| Price history available | last bar = 2026-07-28 | 0 |

### Rejection log (complete)

| Ticker | Reason | Detail |
|---|---|---|
| FDXF | Listing age < 6 months | 42bars,first=2026-05-28 — first bar 2026-05-28, a FedEx spin-off; becomes eligible ~2026-11-27 |

No name was excluded for market cap, liquidity, price, or missing history: all 519 fetched
symbols returned a complete 5y series with last bar 2026-07-28.

## Metric Coverage

| Metric group | Sourceable | `UNAVAILABLE` | DQ / confidence effect | Notes |
|---|---|---|---|---|
| Price / return / volatility | 514 / 514 | 0 | none | L002, L003, L013, L014 |
| Beta, tracking error, drawdown | 514 / 514 | 0 | none | L015, L016, L019 |
| Momentum & relative strength | 514 / 514 | 0 | none | L017, L018 |
| Technical indicator pack | 519 / 519 | 0 | none | L021 |
| Sector / industry / market cap | 510 / 514 | 4 | none material | L010 |
| Next earnings date | 514 / 514 | 0 | none | L022 — full-universe coverage this run |
| **Fundamental family** | **0 / 514** | **514** | **DQ 0.80; blocks evidence threshold #2** | L046 |
| **Sentiment family** | **0 / 514** | **514** | **DQ 0.80; blocks evidence threshold #2** | L047 |
| Options IV / skew, short interest, bid-ask, analyst revisions | 0 / 514 | 514 | caps confidence only | L036, L048 |

Fundamental and Sentiment are `UNAVAILABLE` **universe-wide**, not name-specific. `rules.md
§ Financial Metrics and Score Attribution` requires a metric to be sourceable for >= 70% of the
universe before it may contribute to `Adj Score`; both families are at 0%, so both are excluded from
the score and reported as `0.00 (UNAVAILABLE)` in every trace. They are never described as neutral or
supportive.

## Technical Indicator Coverage (daily / weekly / monthly)

Every field below comes from `technical_indicators.json` (L021), computed on the adjusted-close bars.

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 519 / 519 | 519 / 519 | 519 / 519 |
| RSI(14) | 519 / 519 | 519 / 519 | 519 / 519 |
| MACD(12,26,9) state | 519 / 519 | 519 / 519 | 519 / 519 |
| MA20 / MA50 alignment | 519 / 519 | 519 / 519 | 519 / 519 |
| 20 / 60-bar momentum | 519 / 519 | 519 / 519 | 519 / 519 |
| 20-bar volume ratio | 519 / 519 | 519 / 519 | 519 / 519 |
| Relative strength vs SPY | 519 / 519 | 519 / 519 | 519 / 519 |

Coverage is complete on all three timeframes; no indicator was hand-filled and none is `UNAVAILABLE`.

## Handoff to Factor Scoring

514 names with complete price, volatility, beta, drawdown, technical-indicator and earnings-date
coverage. Two of four factor families are `UNAVAILABLE` universe-wide — the scoring agent must set
their contribution to `0.00 (UNAVAILABLE)` and may not count them toward the 3-of-4 threshold.
