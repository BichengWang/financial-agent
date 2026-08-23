# 04 — Universe Summary · 2026-08-14

## Construction

| Step | Count | Source |
|---|---|---|
| S&P 500 constituents | 503 | `agents/equity/turtle-trader/universe/sp500.json` (cache `fetched_at` 2026-06-21T21:05:56Z) |
| Nasdaq-100 constituents | 101 | `agents/equity/turtle-trader/universe/nasdaq100.json` (cache `fetched_at` 2026-06-21T21:05:56Z) |
| Overlap | 89 | index-union helper |
| **Union** | **515** | `build_index_universe.py` |
| Rejected by filters | 4 | see rejection log |
| **Scored universe** | **511** | `run_computed_manifest.json` |

Percentiles throughout this package are labeled `INDEX_UNION_PCTL (n=511)`. The
Sampled Universe Protocol was **not** used — the index-union helper succeeded, so the
emergency fallback is not permitted.

Constituent caches are **54 days stale** (fetched 2026-06-21).
`rules.md § Index-Union Universe Protocol` item 5 requires using them anyway and logging the
timestamps, which is done above. The staleness is visible in this run's rejection log: `EA`
is still a cache member but stopped trading on 2026-08-04.

## Inclusion filters applied

| Filter | Threshold | Applied from |
|---|---|---|
| Listing | U.S. primary exchange | index membership |
| Market cap | > $2B | Nasdaq screener `marketCap` (`L009`) |
| Average daily dollar volume | > $20M over 20 sessions | fetched raw closes x volume (`L001`) |
| Price | > $5 | basis-date raw close (`L003`) |
| Listing age | > 6 months (>= 127 daily bars) | fetched history bar count (`L001`) |

Bid-ask spread (50bp) and the 80%-of-sessions test could not be applied: no bid-ask tape is
wired (`Enhancing`, see `00`), and every retained name traded on all 60 trailing sessions.

## Rejection log

| Ticker | Reason | Detail | Filter |
|---|---|---|---|
| BF-B | `MARKET_CAP_UNAVAILABLE` | — | Market cap |
| EA | `STALE_LAST_BAR` | last bar 2026-08-04 != basis 2026-08-14 | Exclusion — halted / pending delisting |
| FDXF | `LISTING_AGE_LT_6M` | 55 bars | Listing age |
| Q | `INDICATOR_INCOMPLETE` | 200 daily bars | Derived-metric completeness |

Notes on each:

- **`BF-B`** — the Nasdaq screener's `marketCap` field is empty for this symbol (keyed
  `BF/B`). A real vendor gap, not a fetch error; it recurs every run. Marked `UNAVAILABLE`
  rather than estimated. Its price history fetched cleanly and it has never ranked near the
  published set.
- **`EA`** — last bar **2026-08-04**, seven sessions before the basis, while
  518 of 519
  symbols carry the basis date. Corroborated independently this run: `api.nasdaq.com` returns
  `"Symbol not exists"` and CNBC returns no quote object. The final bar printed 47.2M shares
  against a ~4.4M recent average with the price pinned near $209.7–209.9 — a deal-close
  signature. Treated as delisted/halted and excluded. First detected 2026-08-06; the staleness
  has since grown from 2 sessions to 7, which settles the transient-gap hypothesis.
- **`FDXF`** — a FedEx spin-off with 55 daily bars (first bar
  2026-05-28). Legitimately excluded on the >6-month listing-age
  filter; becomes eligible around 2026-11-27.
- **`Q`** — 200 daily bars is enough for daily indicators but not
  for weekly MA alignment, so a `Tech_Z` slot would be `UNAVAILABLE`. Rejected as
  `INDICATOR_INCOMPLETE` rather than scored on a partial slot set.

## Metric coverage

| Family | Sourceable coverage | Status | Effect on scoring |
|---|---|---|---|
| Technical / Price | 511/511 (100.00%) | **LIVE** | full `Tech_Z`; 6 distinct slots |
| Macro / Regime | 511/511 (100.00%) | **LIVE** | full `Macro_Z`; 4 slots |
| Fundamental | 0/511 (0.00%) | **`UNAVAILABLE`** | `Fund_Z` = 0.00 (`UNAVAILABLE`); excluded from the 3-of-4 threshold (`L021`) |
| Sentiment / Positioning | 0/511 (0.00%) | **`UNAVAILABLE`** | `Sent_Z` = 0.00 (`UNAVAILABLE`); excluded from the 3-of-4 threshold (`L022`) |

`rules.md § Financial Metrics and Score Attribution` allows a metric into `Adj Score` only when
it is sourceable for at least 70% of the eligible universe. Fundamental and sentiment inputs
are at 0%, so they are excluded from the score entirely rather than imputed as neutral. This
is a **data-quality** failure that also happens to make evidence thresholds 2, 3 and 4
unsatisfiable — it is not a `GO`-blocking Required input under `§ Input Classification`.

### Shadow diagnostic tooling

`fundamental_diagnostics.py` and `sentiment_diagnostics.py` exist and emit
`"gating_status": "SHADOW"`. They were **not** run this session: the shadow run of record
(`claude-haiku-4-5-2026-07-16`) covered 24 names ≈ 4.7% of the universe, and
`rules.md § SHADOW Diagnostic Tooling` is explicit that promotion needs Phase 2 (bulk
`companyfacts.zip` + threaded Nasdaq fetch across all 511 names), which no run has attempted.
Running the shadow tools again on a small sample would add no evidence toward the 70% bar.

## Technical indicator coverage

| Indicator | Sourceable | `UNAVAILABLE` | Coverage | Eligible for `Tech_Z`? |
|---|---|---|---|---|
| TD-9 daily | 511 | 0 | 100.00% | Yes |
| TD-9 weekly | 511 | 0 | 100.00% | Yes |
| TD-9 monthly | 511 | 0 | 100.00% | Yes |
| RSI(14) daily | 511 | 0 | 100.00% | Yes |
| RSI(14) weekly | 511 | 0 | 100.00% | Yes |
| RSI(14) monthly | 511 | 0 | 100.00% | Yes |
| MACD(12,26,9) daily | 511 | 0 | 100.00% | Yes |
| MACD(12,26,9) weekly | 511 | 0 | 100.00% | Yes |
| MACD(12,26,9) monthly | 511 | 0 | 100.00% | Yes |
| MA alignment daily | 511 | 0 | 100.00% | Yes |
| MA alignment weekly | 511 | 0 | 100.00% | Yes |
| MA alignment monthly | 511 | 0 | 100.00% | Yes |
| 20-bar momentum daily | 511 | 0 | 100.00% | Yes |
| 20-bar momentum weekly | 0 | 511 | 0.00% | Diagnostic only |
| 20-bar momentum monthly | 0 | 511 | 0.00% | Diagnostic only |
| 60-bar momentum daily | 511 | 0 | 100.00% | Yes |
| 60-bar momentum weekly | 0 | 511 | 0.00% | Diagnostic only |
| 60-bar momentum monthly | 0 | 511 | 0.00% | Diagnostic only |
| 20-bar volume ratio daily | 511 | 0 | 100.00% | Yes |
| 20-bar volume ratio weekly | 0 | 511 | 0.00% | Diagnostic only |
| 20-bar volume ratio monthly | 0 | 511 | 0.00% | Diagnostic only |
| Relative strength vs SPY daily | 511 | 0 | 100.00% | Yes |
| Relative strength vs SPY weekly | 0 | 511 | 0.00% | Diagnostic only |
| Relative strength vs SPY monthly | 0 | 511 | 0.00% | Diagnostic only |

Monthly-block gaps are display-only and affect no `Tech_Z` slot (the slots use daily and
weekly blocks only).

## Sector distribution of the scored universe

| Sector | Scored names | Share | Median 60d momentum |
|---|---|---|---|
| Consumer Discretionary | 103 | 20.2% | +11.24% |
| Industrials | 86 | 16.8% | +9.15% |
| Technology | 80 | 15.7% | +9.62% |
| Finance | 68 | 13.3% | +15.32% |
| Health Care | 56 | 11.0% | +15.46% |
| Utilities | 37 | 7.2% | +0.32% |
| Real Estate | 28 | 5.5% | +5.57% |
| Consumer Staples | 21 | 4.1% | +4.66% |
| Energy | 16 | 3.1% | -1.76% |
| Telecommunications | 10 | 2.0% | +3.68% |
| Basic Materials | 5 | 1.0% | +12.32% |
| UNAVAILABLE | 1 | 0.2% | +4.91% |

Sector labels come from the Nasdaq screener (`L009`) and use its own taxonomy, not GICS. The
30% sector cap in `rules.md § Risk Controls` is applied against these labels; the mapping
difference is disclosed rather than silently treated as GICS.
