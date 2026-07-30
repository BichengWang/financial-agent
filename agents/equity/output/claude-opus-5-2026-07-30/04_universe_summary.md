# 04 — Universe Summary — 2026-07-30

## Construction

The normal index-union path succeeded; no sampled fallback was used.

| Field | Value |
|---|---|
| S&P 500 constituents | 503 |
| Nasdaq-100 constituents | 101 |
| Overlap | 89 |
| **Union (candidate universe)** | **515** |
| Scored after inclusion filters | **513** |
| Rejected | 2 |
| Ranked (≥60th pctl, either sleeve) | 205 |
| Published records | 24 |
| Cache timestamps | sp500 2026-06-21, nasdaq100 2026-06-21 (**39 days stale**) |

Percentile label for every rank in this package: **`INDEX_UNION_PCTL (n=513)`**.

The constituent caches are 39 days old. Per
`rules.md § Index-Union Universe Protocol` rule 5 that is logged and used, not treated as a
reason to fall back to a 30-name sample; refreshing them is a maintenance task.

## Inclusion filters applied

| Filter | Threshold | Result |
|---|---|---|
| U.S. primary exchange | required | all union members qualify |
| Market cap | > $2B | 1 exclusion (BF-B, vendor field empty → `UNAVAILABLE`, not estimated) |
| Avg daily dollar volume | > $20M over 20 sessions | 0 exclusions |
| Price | > $5 | 0 exclusions |
| Listing age | > 6 months | 1 exclusion (FDXF) |
| Sessions traded | ≥ 80% of trailing 60 | 0 exclusions |

## Rejection log

| Ticker | Reason |
|---|---|
| BF-B | MARKET_CAP_UNAVAILABLE |
| FDXF | INSUFFICIENT_HISTORY |

**FDXF** is the FedEx freight spin-off; its first bar is recent, so it legitimately fails the
>6-month listing-age filter and becomes eligible around 2026-11-27. **BF-B**'s `marketCap` field
is empty in the Nasdaq screener — a reproducible vendor gap first logged 2026-07-27, marked
`UNAVAILABLE` rather than estimated.

## Sector distribution (scored universe)

| Sector | Names | Median RS60 vs SPY | Median 30d RVol |
|---|---|---|---|
| Consumer Discretionary | 104 | 3.75% | 9.90% |
| Industrials | 85 | 4.28% | 9.92% |
| Technology | 82 | -2.08% | 14.27% |
| Finance | 68 | 9.22% | 8.32% |
| Health Care | 56 | 14.42% | 9.64% |
| Utilities | 37 | -2.67% | 6.17% |
| Real Estate | 28 | 7.32% | 6.84% |
| Consumer Staples | 21 | 7.40% | 9.21% |
| Energy | 16 | -5.06% | 9.45% |
| Telecommunications | 9 | -8.60% | 11.42% |
| Basic Materials | 5 | -0.52% | 10.46% |
| UNAVAILABLE | 2 | 6.16% | 19.23% |

## Metric coverage

| Metric group | Sourceable | `UNAVAILABLE` | Effect | Source |
|---|---|---|---|---|
| Price / OHLCV history (5y daily) | 513 | 0 | none — full coverage | stockanalysis.com bulk, verified vs CNBC/IBKR |
| Market cap | 513 | 1 | BF-B excluded from scoring | Nasdaq screener; empty field is a real vendor gap |
| GICS sector | 511 | 2 | sector caps + sector-median vol penalty | Nasdaq screener |
| Next earnings date | 513 | 0 | 14-day penalty window | forward calendar sweep, 27/27 days complete |
| Beta / correlation / drawdown / TE | 513 | 0 | none | DERIVED from 60d fetched returns |
| Realized vol 30d (sigma) | 513 | 0 | none | Sigma chain step 2 |
| Options IV30 | 0 | 513 | Enhancing — DQ and confidence cap only | no feed wired |
| Short interest / borrow | 0 | 513 | Enhancing — DQ and confidence cap only | no feed wired |
| Analyst revision tape | 0 | 513 | Enhancing — DQ and confidence cap only | no feed wired |
| Fundamental metrics (`Fund_Z`) | 0 | 513 | **Family `UNAVAILABLE` — blocks Evidence Threshold 2** | SHADOW tooling only, ~4.7% coverage |
| Sentiment metrics (`Sent_Z`) | 0 | 513 | **Family `UNAVAILABLE` — blocks Evidence Threshold 2** | SHADOW tooling only |

**The two `UNAVAILABLE` families are the run's binding constraint.** They are not a
data-fetch failure today; they are a structural gap (`rules.md § SHADOW Diagnostic Tooling`).
`fundamental_diagnostics.py` and `sentiment_diagnostics.py` exist but emit `gating_status:
SHADOW` and cover far below the 70%-of-universe bar that
`rules.md § Financial Metrics and Score Attribution` requires before a metric may enter
`Adj Score`. Promotion needs Phase 2 of the plan, not a rule waiver.

## Technical indicator coverage

All values come from `technical_indicators.json`, computed by `technical_indicators.py` on the
fetched **adjusted** bars.

| Indicator | Timeframes | Coverage | % |
|---|---|---|---|
| TD-9 setup | daily/weekly/monthly | 513 / 513 | 100.0% |
| RSI(14) | daily/weekly/monthly | 513 / 513 | 100.0% |
| MACD(12,26,9) state + histogram | daily/weekly/monthly | 513 / 513 | 100.0% |
| MA20/MA50 alignment | daily/weekly/monthly | 513 / 513 | 100.0% |
| 20/60-bar momentum | daily/weekly/monthly | 513 / 513 | 100.0% |
| 20-bar volume ratio | daily/weekly/monthly | 513 / 513 | 100.0% |
| Relative strength vs SPY (20/60) | daily/weekly/monthly | 513 / 513 | 100.0% |

Note on lineage: `technical_indicators.py` prefers a CSV's `Close` column over `AdjClose`, so
to honour the 2026-07-26 adjusted-close rule the run writes a **separate** history directory
whose `Close` column already holds adjusted values, and points `--history-dir` there. Raw closes
are kept in a parallel directory and used only for entry/target/CI prices.
