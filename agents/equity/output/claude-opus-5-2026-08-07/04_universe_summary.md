# 04 — Universe Summary

## Construction

The normal index-union path succeeded; the emergency Sampled Universe Protocol was **not**
used. Percentiles throughout this package are labeled `INDEX_UNION_PCTL (n=511)`.

| Step | Count | Source |
|---|---|---|
| S&P 500 constituents | 503 | `sp500.json`, fetched_at 2026-06-21T21:05:56Z (`L008`) |
| Nasdaq-100 constituents | 101 | `nasdaq100.json`, fetched_at 2026-06-21T21:05:56Z (`L009`) |
| Overlap | 89 | computed by `build_index_universe.py` (`L010`) |
| **Index union** | **515** | `eligible_universe.txt` (`L010`) |
| Rejected by inclusion/exclusion filters | 4 | see log below |
| **Scored universe** | **511** | `run_computed_manifest.json` |

The constituent caches are dated 2026-06-21, **47 days** before this run.
`rules.md § Index-Union Universe Protocol` rule 5 is explicit that stale caches are still used
for the run and the `fetched_at` values logged; a refresh is maintenance, not a reason to fall
back to a 30-name sample. The staleness is disclosed here and is a plausible contributor to the
`EA` and `SATS`/`ECHO` identity issues below.

## Inclusion filters applied

| Filter | Threshold | Applied? | Note |
|---|---|---|---|
| Listing | U.S. primary exchange | Yes | index-union membership implies it |
| Market cap | > $2B | Yes | `L011` screener `marketCap` |
| Average daily dollar volume | > $20M over 20 sessions | Yes | close x volume from `L003` |
| Price | > $5 | Yes | raw close from `L003` |
| Listing age | > 6 months | Yes | first fetched bar; rejects `FDXF` |
| Bid-ask spread | <= 50 bps | **No — UNAVAILABLE** | no spread tape wired; Enhancing input, disclosed, never a GO blocker |
| Session participation | >= 80% of trailing 60 sessions | Yes | implied by the >=61-bar requirement |
| Corporate-action ambiguity | excluded | Yes | 0 symbols carried an ex-div `c != a` on the basis bar |

## Rejection log

| Ticker | Reason | Detail | Filter |
|---|---|---|---|
| BF-B | `MARKET_CAP_UNAVAILABLE` | vendor marketCap field empty | Market cap |
| EA | `DELISTED_OR_HALTED` | last bar 2026-08-04 != basis 2026-08-07 | Exclusion — halted/delisting |
| FDXF | `LISTING_AGE` | 50 daily bars; first bar 2026-05-28 | Listing age |
| Q | `INDICATOR_INCOMPLETE` | 195 daily bars; weekly/daily MA or MACD UNAVAILABLE | Derived-metric completeness |

Notes on each:

- **`BF-B`** — the Nasdaq screener's `marketCap` field is empty for this symbol (keyed
  `BF/B`). This is a real vendor gap, not a fetch error, and it recurs every run. The name is
  marked `UNAVAILABLE` rather than estimated. Its price history fetched cleanly, so the
  exclusion costs only one name and it has never ranked near the published set.
- **`EA`** — last bar 2026-08-04, three sessions before the basis,
  while 518 of 519 symbols carry the basis date. First detected 2026-08-06; the additional
  staleness corroborates a delisting or extended halt rather than a transient gap.
- **`FDXF`** — a FedEx spin-off whose first bar is 2026-05-28
  (50 daily bars). Legitimately excluded on the >6-month
  listing-age filter; becomes eligible around 2026-11-28.
- **`Q`** — 195 daily bars is enough for daily indicators but not
  for weekly MA alignment, so a `Tech_Z` slot would be `UNAVAILABLE`. Rejected as
  `INDICATOR_INCOMPLETE` rather than scored on a partial slot set.

`SATS` required a vendor alias to `ECHO` (EchoStar renamed; unfixed upstream since 2026-07-13)
for **both** the price fetch and the screener lookup — without the screener alias it silently
drops on `MARKET_CAP_UNAVAILABLE`. `BRK-B` and `BF-B` required dot notation for price history
and slash notation (`BRK/B`, `BF/B`) for the screener.

## Sector distribution of the scored universe

| Sector | Names | Share |
|---|---|---|
| Consumer Discretionary | 103 | 20.16% |
| Industrials | 86 | 16.83% |
| Technology | 80 | 15.66% |
| Finance | 68 | 13.31% |
| Health Care | 56 | 10.96% |
| Utilities | 37 | 7.24% |
| Real Estate | 28 | 5.48% |
| Consumer Staples | 21 | 4.11% |
| Energy | 16 | 3.13% |
| Telecommunications | 10 | 1.96% |
| Basic Materials | 5 | 0.98% |
| UNCLASSIFIED | 1 | 0.20% |

## Metric coverage

| Metric group | Sourceable across the universe | Status | Effect |
|---|---|---|---|
| Technical / Price | 511/511 (100.00%) | **LIVE** | full `Tech_Z`; 6 distinct slots |
| Macro / Regime | 511/511 (100.00%) | **LIVE** | full `Macro_Z`; 4 slots |
| Fundamental | 0/511 (0.00%) | **UNAVAILABLE** | `Fund_Z` = 0.00 (UNAVAILABLE); does not count toward the 3-of-4 threshold (`L022`) |
| Sentiment / Positioning | 0/511 (0.00%) | **UNAVAILABLE** | `Sent_Z` = 0.00 (UNAVAILABLE); does not count toward the 3-of-4 threshold (`L023`) |
| Risk / return ratios | 24/24 published names | LIVE | Sharpe, Sortino, IR, Treynor, Calmar computed with a sourced rf (`L006`) |
| Tail risk | 24/24 published names | LIVE | VaR95, CVaR95, 60d max drawdown |
| Sizing | 24/24 published names | LIVE | raw Kelly, 0.25 x Kelly |

**Which missing inputs affect data quality rather than GO eligibility.** All five Required
inputs in `rules.md § Input Classification` are grounded (see the GO-Gate Table in `00`). Every
`UNAVAILABLE` item above — fundamentals, sentiment, options IV, short interest, spread tape,
analyst revisions — is an **Enhancing** input. They cannot block `GO` on their own; they lower
the data-quality multiplier to 0.80 (`L021`) and cap confidence. Their real
cost is indirect but decisive: with two of four families dark, evidence thresholds #2 and #3
become arithmetically unsatisfiable, which is what actually produces `NO_TRADE`.

## Technical indicator coverage (daily / weekly / monthly)

| Indicator / timeframe | Sourceable | UNAVAILABLE | Coverage | Clears 70% bar? |
|---|---|---|---|---|
| 20-bar momentum daily | 511 | 0 | 100.00% | Yes |
| 20-bar momentum monthly | 510 | 1 | 99.80% | Yes |
| 20-bar momentum weekly | 511 | 0 | 100.00% | Yes |
| MA alignment daily | 511 | 0 | 100.00% | Yes |
| MA alignment monthly | 504 | 7 | 98.63% | Yes |
| MA alignment weekly | 511 | 0 | 100.00% | Yes |
| MACD(12,26,9) daily | 511 | 0 | 100.00% | Yes |
| MACD(12,26,9) monthly | 508 | 3 | 99.41% | Yes |
| MACD(12,26,9) weekly | 511 | 0 | 100.00% | Yes |
| RSI(14) daily | 511 | 0 | 100.00% | Yes |
| RSI(14) monthly | 511 | 0 | 100.00% | Yes |
| RSI(14) weekly | 511 | 0 | 100.00% | Yes |
| Relative strength vs SPY daily | 511 | 0 | 100.00% | Yes |
| TD-9 daily | 511 | 0 | 100.00% | Yes |
| TD-9 monthly | 511 | 0 | 100.00% | Yes |
| TD-9 weekly | 511 | 0 | 100.00% | Yes |
| Volume ratio daily | 511 | 0 | 100.00% | Yes |
| Volume ratio monthly | 510 | 1 | 99.80% | Yes |
| Volume ratio weekly | 511 | 0 | 100.00% | Yes |

Every indicator clears the 70%-of-universe threshold that `rules.md § Financial Metrics and
Score Attribution` requires before a metric may contribute to `Adj Score`. Monthly blocks are
present for all 511 scored names; the display-only monthly gaps seen in earlier runs
(GEHC/GEV/KVUE/SNDK/SOLV/VLTO/ARM) do not recur because those names now carry >=61 monthly bars.

Relative strength versus SPY is computed, displayed and ledgered at 100% coverage but is
**not** a `Tech_Z` slot: with a single common benchmark its cross-sectional z-score is
identical to the corresponding momentum z-score (measured identity ~4.4e-16), so scoring it
would double-count momentum. Track B effective 2026-08-03, now codified in `rules.md`.
