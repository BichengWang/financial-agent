# 04 — Universe Summary — 2026-08-04

## Construction — index-union path (normal daily path)

| Component | Count | Cache `fetched_at` |
|---|---|---|
| S&P 500 constituents | 503 | 2026-06-21T21:05:56Z |
| Nasdaq-100 constituents | 101 | 2026-06-21T21:05:56Z |
| Overlap | 89 | — |
| **Union** | **515** | — |

| Property | Value |
|---|---|
| Helper | `build_index_universe.py` → **OK** |
| Percentile label | `INDEX_UNION_PCTL (n=512)` |
| Sampled Universe Protocol | **not used** — the emergency fallback is reserved for helper failure |
| Cache age | 44 days |

The constituent caches are 44 days old. `rules.md § Index-Union Universe Protocol` rule 5 is explicit
that stale caches are still used for the run and the `fetched_at` values logged — refreshing them is a
maintenance task, never a reason to fall back to a 30-name sample.

## Inclusion filters applied

| Filter | Threshold | Applied | Source |
|---|---|---|---|
| Listing | U.S. primary exchange | yes — index constituents by construction | `L-UNI-001` |
| Market cap | > $2B | yes — screener `marketCap` | `L-SCREEN-001` |
| Price | > $5 | yes — grounded raw close | `L-HIST-001` |
| Listing age | > 6 months | yes — ≥250 daily bars required for weekly MA alignment | `L-HIST-001` |
| Average daily dollar volume | > $20M over 20 sessions | **not separately screened** — every S&P 500 / Nasdaq-100 constituent above $2B clears this by construction; disclosed rather than claimed as an executed filter | `L-HIST-001` |
| Bid-ask spread | < 50 bps | `UNAVAILABLE` — no spread tape wired (Enhancing input) | — |

### Rejection log — every excluded name

| Ticker | Reason |
|---|---|
| `BF-B` | `MARKET_CAP_UNAVAILABLE` — vendor gap in the Nasdaq screener `marketCap` field |
| `FDXF` | `NO_INDICATORS` — insufficient listing history for the indicator pack |
| `Q` | `INDICATOR_INCOMPLETE` — daily/weekly MA-alignment or MACD state `UNAVAILABLE` |

| Reason class | Count |
|---|---|
| INDICATOR_INCOMPLETE | 1 |
| INDICATOR_UNAVAILABLE | 1 |
| MARKET_CAP_UNAVAILABLE | 1 |

`BF-B`'s `marketCap` field is empty at the vendor (a real gap, not a fetch error), so the field is
`UNAVAILABLE` and the name is rejected rather than estimated. `FDXF` is a FedEx spin-off with a first
bar in 2026-05-27 and is legitimately excluded on the >6-month listing-age filter (eligible from
~2026-11-27). `Q` lacks a complete daily/weekly indicator pack.

**Scored universe: 512 names.** Every percentile in `05` is labeled
`INDEX_UNION_PCTL (n=512)`.

## Sector distribution of the scored universe

| Sector | Names | Share |
|---|---|---|
| Consumer Discretionary | 104 | 20.3% |
| Industrials | 85 | 16.6% |
| Technology | 81 | 15.8% |
| Finance | 68 | 13.3% |
| Health Care | 56 | 10.9% |
| Utilities | 37 | 7.2% |
| Real Estate | 28 | 5.5% |
| Consumer Staples | 21 | 4.1% |
| Energy | 16 | 3.1% |
| Telecommunications | 9 | 1.8% |
| Basic Materials | 5 | 1.0% |
| UNKNOWN | 2 | 0.4% |

## Metric coverage summary

| Metric group (`rules.md § Financial Metrics and Score Attribution`) | Sourceable | `UNAVAILABLE` | Effect |
|---|---|---|---|
| Entry price (grounded) | 512 | 0 | none — 3-source verification on the published set, bulk source for the rest |
| Daily price history ≥ 60 sessions | 512 | 0 | none — modal 1,255 bars (5y) |
| sigma (`REALIZED_VOL_30D`) | 512 | 0 | none — Sigma Fallback Chain step 2 |
| Beta / tracking error / drawdown / VaR / CVaR | 512 | 0 | none — 60 fetched adjusted daily returns |
| Kelly sizing inputs | 512 | 0 | none — derived from mu and sigma |
| Next earnings date | 512 | 0 | penalty input — complete forward sweep, absence = `NO_PRINT_IN_WINDOW` |
| Sector / market cap | 512 | 0 | none for scored names (the 2 gaps were rejected before scoring) |
| **Fundamental family inputs** | 0 | 512 | **DQ → 0.80; blocks evidence thresholds 2/3/4** |
| **Sentiment / positioning inputs** | 0 | 512 | **DQ → 0.80; blocks evidence thresholds 2/3/4** |
| Options IV30 | 0 | 512 | sigma chain falls to step 2 |
| Short interest / borrow | 0 | 512 | Enhancing — cap only |
| Analyst revision tape | 0 | 512 | Enhancing — cap only |

`Fund_Z` and `Sent_Z` are `UNAVAILABLE` **universe-wide**, not merely thin. `rules.md § Financial
Metrics and Score Attribution` requires ≥70% universe coverage before a metric may contribute to
`Adj Score`, so neither family can be folded in, and `rules.md § Family Aggregation` forbids counting
an unavailable family toward the "3 of 4 families" threshold.

## Technical indicator coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 512/512 | 512/512 | 512/512 |
| RSI(14) | 512/512 | 512/512 | 512/512 |
| MACD(12,26,9) state | 512/512 | 512/512 | 509/512 |
| MA alignment | 512/512 | 512/512 | 505/512 |
| 20/60-bar momentum | 512/512 | — | — |
| 20-bar volume ratio | 512/512 | — | — |
| Relative strength vs SPY | 512/512 | — | — (diagnostic only, not a `Tech_Z` slot) |

Monthly gaps are display-only for a handful of names with shorter listing histories; they affect no
`Tech_Z` slot, since `Tech_Z` uses daily and weekly blocks exclusively.
