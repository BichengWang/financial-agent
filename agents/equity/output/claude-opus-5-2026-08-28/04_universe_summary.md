# 04 — Universe Summary — 2026-08-28

## Construction

Normal index-union path — **no** sampled fallback. Percentiles throughout this package are labeled
`INDEX_UNION_PCTL (n=510)`.

| Input | Value | Ledger |
|---|---|---|
| S&P 500 constituents | 503 | L001, L002 |
| Nasdaq-100 constituents | 101 | L001, L003 |
| Overlap | 89 | L001 |
| **Union** | **515** | L001 |
| S&P 500 cache `fetched_at` | 2026-06-21T21:05:56Z | L002 |
| Nasdaq-100 cache `fetched_at` | 2026-06-21T21:05:56Z | L003 |
| Cache age at run date | **68 days** | L002, L003 |
| Scored after filters | **510** | this artifact |

Per `rules.md § Index-Union Universe Protocol` rule 5, stale constituent caches are still used for the
run and their `fetched_at` values logged; refreshing them is a maintenance task, not a reason to fall
back to a 30-name sample. Staleness is, however, the upstream reason dead names such as `EQR`, `AVB`
and `EA` are still in the union — see the corporate-action log below.

## Inclusion / exclusion log

| Filter (rules.md § Universe Construction) | Threshold | Applied | Rejections |
|---|---|---|---|
| U.S. primary exchange | required | yes — via Nasdaq screener presence (L010) | 0 |
| Market cap | > $2B | yes (L010) | 0 |
| Average daily dollar volume | > $20M over 20 sessions | yes — mean(close x volume) over the trailing 20 raw bars (L004) | 0 |
| Price | > $5 | yes — basis-date raw close (L004) | 0 |
| Listing age | > 6 months | yes — first fetched bar vs basis (L004) | 1 |
| Unresolved corporate-action ambiguity | excluded | yes — classifier below (L016) | 3 |
| Complete indicator pack | required for scoring | yes (L013) | 1 |
| Bid-ask spread > 50 bps | excluded | **not applied** — no spread tape wired | `UNAVAILABLE` |
| Traded < 80% of trailing 60 sessions | excluded | subsumed by the corporate-action classifier's `last_bar != basis` test | see below |

### Rejection log (every rejected name)

| Ticker | Reason | Detail |
|---|---|---|
| AVB | `CORPORATE_ACTION_DELISTED` | {"class": "CORPORATE_ACTION_DELISTED", "last_bar": "2026-08-14", "screener_present": false, "successor_search": "none found by name"} |
| EA | `CORPORATE_ACTION_DELISTED` | {"class": "CORPORATE_ACTION_DELISTED", "last_bar": "2026-08-04", "screener_present": false, "successor_search": "none found by name"} |
| EQR | `CORPORATE_ACTION_RENAMED` | {"class": "CORPORATE_ACTION_RENAMED", "detail": "HTTPError: HTTP Error 400: Bad Request", "screener_present": false} |
| FDXF | `LISTING_AGE_UNDER_6M` | first bar 2026-05-28 |
| Q | `INDICATOR_INCOMPLETE` | MA alignment unavailable |

### Corporate-action classifier (Track B effective 2026-08-23)

Every union member is classified against two independent references before scoring: the bulk-history
fetch result and last-bar date, then the Nasdaq screener roster and the CNBC identity fields.

| Ticker | Classification | Bulk history | Screener | CNBC identity | Open predictions affected |
|---|---|---|---|---|---|
| EQR | `CORPORATE_ACTION_RENAMED` + `SYMBOL_REUSE_FOREIGN_LISTING` | HTTP 400 — symbol retired | absent; `VMRK` (Vivmark Residential, Real Estate, $51.61B) present | returns *EQ Resources Ltd*, exchange **ASX**, last 0.41, volume 0 — **rejected** by the Track B gate effective today | **2** (`claude-opus-5-2026-07-26`, `gpt-5-2026-07-27`) — reported `UNSETTLEABLE_CORPORATE_ACTION` in `02 § 0` |
| AVB | `CORPORATE_ACTION_DELISTED` | last bar **2026-08-14** | absent from all 7,132 rows | no quote returned | 0 |
| EA | `CORPORATE_ACTION_DELISTED` | last bar **2026-08-04** | absent from all 7,132 rows | no quote returned | 0 |

No successor was identified for `AVB` or `EA` by name search across the full screener roster, so no
exchange ratio is inferred and no key is settled against a successor — the explicit non-goal of the
2026-08-22 change. `SATS` is fetched and screened under its post-rename symbol `ECHO` and scores
normally; `BRK-B` maps to the screener key `BRK/B`; `BF-B`'s screener `marketCap` field is empty (a
real vendor gap) and it is excluded on `MARKET_CAP_UNAVAILABLE` rather than estimated.

## Sector distribution of the scored universe

| Sector | Names | Share |
|---|---|---|
| Consumer Discretionary | 103 | 20.2% |
| Industrials | 86 | 16.9% |
| Technology | 80 | 15.7% |
| Finance | 68 | 13.3% |
| Health Care | 56 | 11.0% |
| Utilities | 37 | 7.3% |
| Real Estate | 26 | 5.1% |
| Consumer Staples | 21 | 4.1% |
| Energy | 16 | 3.1% |
| Telecommunications | 10 | 2.0% |
| Basic Materials | 5 | 1.0% |
| UNCLASSIFIED | 2 | 0.4% |

## Metric coverage

| Metric group | Sourceable | Coverage | Effect under rules.md § Financial Metrics |
|---|---|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, beta, TE) | 510/510 | 100.0% | counts toward `Adj Score` |
| Tail risk (dd60, VaR95, CVaR95) | 510/510 | 100.0% | counts toward `Adj Score` |
| Sizing (Kelly) | 510/510 | 100.0% | counts toward `Adj Score` |
| Technical (TD9/RSI/MACD/MA/mom/vol/RS) | 510/510 | 100.0% | counts toward `Adj Score` |
| Fundamental / quality | 0/510 | 0.0% | **below the 70% threshold — diagnostic only** |
| Sentiment / positioning | 0/510 | 0.0% | **below the 70% threshold — diagnostic only** |

`Fund_Z` and `Sent_Z` are `UNAVAILABLE` **universe-wide** (L018, L019). The SHADOW diagnostic tooling
in `rules.md § SHADOW Diagnostic Tooling` exists but its one executed shadow run covered ~4.7% of the
universe, far below the 70% threshold that section requires before a family may contribute — Phase 2
(bulk `companyfacts.zip` + threaded Nasdaq fetch across the full universe) has not been attempted.
This is a **data-quality and evidence-threshold** limitation, not a `GO` blocker under
`rules.md § Input Classification`: none of the five Required inputs is missing.

## Technical indicator coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 510/510 (100.0%) | 510/510 (100.0%) | 510/510 (100.0%) |
| RSI(14) | 510/510 (100.0%) | 510/510 (100.0%) | 510/510 (100.0%) |
| MACD(12,26,9) state | 510/510 (100.0%) | 510/510 (100.0%) | 507/510 (99.4%) |
| MA alignment | 510/510 (100.0%) | 510/510 (100.0%) | display-only for 7 names with monthly gaps |
| 20/60-bar momentum | 510/510 (100.0%) | derived from the same daily block | derived from the same daily block |
| 20-bar volume ratio | 510/510 (100.0%) | — | — |
| Relative strength vs SPY | 510/510 (100.0%) | — | diagnostic only — not a `Tech_Z` slot (Track B 2026-08-03) |

Seven names (`GEHC`, `GEV`, `KVUE`, `SNDK`, `SOLV`, `VLTO`, `ARM`) have short monthly histories; those
gaps are display-only and do not affect any score slot, because no monthly field is a `Tech_Z` input.
`Q` is rejected outright as `INDICATOR_INCOMPLETE` — with 210 daily bars it
cannot produce a weekly MA alignment, which **is** a scored slot.

## Handoff to factor scoring

**510** names with a complete metric pack, grounded basis-date prices, a resolved earnings
state, and `INDEX_UNION_PCTL (n=510)` percentile labeling.

