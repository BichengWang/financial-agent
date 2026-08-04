# 04 — Universe Summary — 2026-08-03

## Construction

The normal index-union path succeeded; the emergency Sampled Universe Protocol was **not** used.

| Field | Value |
|---|---|
| Helper | `build_index_universe.py` |
| S&P 500 constituents | 503 |
| Nasdaq-100 constituents | 101 |
| Overlap | 89 |
| **Union** | **515** |
| S&P 500 cache `fetched_at` | 2026-06-21T21:05:56Z |
| Nasdaq-100 cache `fetched_at` | 2026-06-21T21:05:56Z |
| Cache age at run time | 43 days |
| Percentile label | `INDEX_UNION_PCTL (n=512)` |

Both constituent caches are 43 days old. Per `rules.md § Index-Union Universe Protocol` rule 5 they
are used as-is and the timestamps logged; refreshing them is a maintenance task and is **not** a
reason to fall back to a 30-name sample.

## Price history

| Field | Value |
|---|---|
| Bulk source | `stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y` |
| Symbols requested | 519 |
| Symbols returned | **519** |
| Failures | 0 |
| Elapsed | 183.4s at 8 workers |
| Modal history | 1,255 daily bars (5 years) |
| Last-bar date | 2026-08-03 for 518 of 519 symbols |
| Alias applied | `SATS` -> `ECHO` (EchoStar rename, still unfixed upstream) |
| B-share notation | dots, not hyphens (`BRK.B`, `BF.B`) |
| Ex-dividend `c != a` on the basis bar | 2 — LVS, MET |

## Inclusion and exclusion log

| Filter | Threshold | Applied |
|---|---|---|
| Listing | U.S. primary exchange | index-union membership implies it |
| Market cap | > $2B | Nasdaq screener `marketCap` |
| Average daily dollar volume | > $20M over 20 sessions | close x volume, trailing 20 bars |
| Price | > $5 | basis-date raw close |
| Listing age | > 6 months | >= 126 daily bars |
| Session coverage | traded in >= 80% of the trailing 60 sessions | non-zero volume count |
| Indicator completeness | daily+weekly MA alignment and MACD state must be sourceable | `technical_indicators.py` output |

### Rejection log — every excluded name

| Ticker | Reason |
|---|---|
| BF-B | MARKET_CAP_UNAVAILABLE |
| FDXF | NO_INDICATORS |
| Q | INDICATOR_INCOMPLETE (daily/weekly MA-alignment or MACD state UNAVAILABLE) |

| Reason class | Count |
|---|---|
| INDICATOR_INCOMPLETE | 1 |
| MARKET_CAP_UNAVAILABLE | 1 |
| NO_INDICATORS | 1 |

Notes on the three exclusions:

- **FDXF** — the FedEx spin-off, first bar 2026-05-28, 45 bars. It fails the
  >6-month listing-age filter and additionally has no 2026-08-03 bar (last bar 2026-07-31).
  It becomes eligible around 2026-11-27. This is a correct exclusion, not a fetch failure.
- **BF-B** — the Nasdaq screener returns an **empty** `marketCap` for `BF/B`. That is a real vendor
  gap, so the field is `UNAVAILABLE` and the name is rejected rather than estimated. BF-B has never
  ranked anywhere near the published set.
- **Q** — 191 bars from 2025-10-28: enough for the daily block but not for a
  weekly MA50, so weekly MA alignment is `UNAVAILABLE` and `Tech_Z` cannot be assembled without
  imputing a neutral value, which `rules.md § Family Aggregation` forbids.

**Scored universe: 512 names.** All percentiles in `05` are labelled
`INDEX_UNION_PCTL (n=512)`.

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | DQ / GO effect | Notes |
|---|---|---|---|---|
| Entry price (grounded) | 512 | 0 | none | 3-source verification on the published set; bulk source for the rest |
| Daily price history >= 60 sessions | 512 | 0 | none | modal 1,255 bars (5y) |
| sigma (REALIZED_VOL_30D) | 512 | 0 | none | Sigma Fallback Chain step 2 |
| Beta / TE / drawdown / VaR / CVaR | 512 | 0 | none | 60d fetched adjusted returns |
| Next earnings date | 512 | 0 | penalty input | complete forward sweep; absence = NO_PRINT_IN_WINDOW |
| Market cap / sector | 510 | 2 | negligible | Nasdaq screener |
| **Fundamental family inputs** | 0 | 512 | **DQ -> 0.80; blocks thresholds 2/3/4** | no universe-scale XBRL path wired |
| **Sentiment family inputs** | 0 | 512 | **DQ -> 0.80; blocks thresholds 2/3/4** | no universe-scale analyst/SI path wired |
| Options IV30 | 0 | 512 | sigma chain falls to step 2 | no options feed |

`Fund_Z` and `Sent_Z` are the only coverage gaps that change the outcome, and they are **not** `GO`
blockers under `rules.md § Input Classification` — they are missing *Required-for-thresholds*
evidence rather than missing Required *inputs*. Their effect is on the Evidence Thresholds in `05`.

## Technical indicator coverage

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 512/512 | 512/512 | 512/512 |
| RSI(14) | 512/512 | 512/512 | 512/512 |
| MACD(12,26,9) state | 512/512 | 512/512 | 509/512 |
| MA alignment | 512/512 | 512/512 | 505/512 |
| 20/60-bar momentum | 512/512 | — | — |
| 20-bar volume ratio | 512/512 | — | — |
| Relative strength vs SPY | 512/512 | — | — |

Monthly gaps are concentrated in recently-listed names (GEHC, GEV, KVUE, SNDK, SOLV, VLTO, ARM),
which lack 50 monthly bars. Those gaps affect display only: the monthly block is not an input to
`Tech_Z`, which is built from daily and weekly metrics.
