# 04 Universe Summary — 2026-07-27

## Construction

Built by `build_index_universe.py` from the local constituent caches — the normal daily path, not a sample.

| Field | Value | Source |
|---|---|---|
| S&P 500 count | **503** | `universe_summary.json` (L009) |
| Nasdaq-100 count | **101** | `universe_summary.json` (L009) |
| Overlap count | **89** | `universe_summary.json` (L009) |
| **Union count** | **515** | `universe_summary.json` (L009) |
| Cache paths | `agents/equity/turtle-trader/universe/sp500.json`, `nasdaq100.json` | L009 |
| Cache `fetched_at` | `2026-06-21T21:05:56Z` (both) — 36 days old | L009 |
| **Scored universe** | **514** | L010 |
| Percentile label | **`INDEX_UNION_PCTL (n=514)`** | L010 |

Cache staleness is logged and used as-is per `rules.md § Index-Union Universe Protocol` #5: stale caches are a maintenance item, never grounds for falling back to a 30-name sample.

**Sampled Universe Protocol: NOT used.** The index-union helper succeeded, so per protocol #6 any reuse of a fixed sector sample would itself be a publishing failure.

## Inclusion / Exclusion Log

All filters from `rules.md § Universe Construction`.

| Filter | Threshold | Names failing |
|---|---|---|
| U.S. primary exchange | required | 0 |
| Market cap | > $2B | 0 — 514 current Nasdaq observations plus a recent 2026-07-25 BF-B fallback all clear (L031) |
| Average daily dollar volume | > $20M over 20 sessions | **0** — the minimum ADV20 in the scored set clears the bar (L019) |
| Price | > $5 | 0 |
| **Listing age** | **> 6 months** | **1 — FDXF** |

### Exclusion detail

| Ticker | Bars | First bar | Reason | Ledger |
|---|---|---|---|---|
| **FDXF** | 40 | 2026-05-28 | FedEx Freight spin-off. Fails the >6-month listing-age filter *and* the 60-bar history minimum for beta/vol/drawdown. Becomes eligible ~2026-11-28 | L011 |

### Admission reviewed and upheld

| Ticker | Bars | First bar | Decision | Ledger |
|---|---|---|---|---|
| **Q** (Qnity Electronics) | 185 | 2025-10-28 | **Admitted.** ≈8.9 months of listing history clears the >6-month filter and comfortably exceeds the 60-bar minimum. Daily and weekly indicator coverage is complete; monthly MACD and monthly RSI are `UNAVAILABLE` because 10 monthly bars cannot support MACD(12,26,9) | L012 |

`Q` is a genuine new constituent (DuPont's electronics separation), verified against `api.nasdaq.com/api/quote/Q/info` → *Qnity Electronics, Inc. Common Stock*, NYSE. It is not a cache artifact.

**Exclusions not triggered this run:** thin ADRs, halted/pending-delisting securities, bid-ask above 50bps (bid-ask tape is `UNAVAILABLE` — L146 — so this filter could not be applied and is disclosed as unapplied, not as passed), and names trading fewer than 80% of sessions in the trailing 60.

## Price History Coverage

| Metric | Value |
|---|---|
| Symbols fetched | **519** (all 515 union + SPY/QQQ/SOXX/TLT) |
| Success rate | 519 / 519 = **100%** |
| Bar depth | 40–1,255 daily bars; scored set 185–1,255 |
| Freshest bar | **2026-07-24 on all 519** — no straggler or partial bar |
| Names below the 252-bar preferred lookback | 1 (`Q`, 185 bars) — still far above the 60-bar `GO` minimum |
| Primary source | `stockanalysis.com` adjusted-close history (L003) |
| Alias handling | BF-B→BF.B, BRK-B→BRK.B, SATS→ECHO; no history failure |
| Direct Yahoo branch | not used; accepted adjusted-close rule requires the materialized adjusted CSV path |

## Metric Coverage Summary

Which `rules.md § Financial Metrics and Score Attribution` inputs are sourceable across the eligible universe. A metric may contribute to `Adj Score` only at ≥70% universe coverage.

| Metric Group | Sourceable | Coverage | Contributes to `Adj Score`? | Effect |
|---|---|---|---|---|
| Price / volume history | 514 / 514 | 100% | — | none |
| 30d realized vol, downside vol | 514 / 514 | 100% | yes (Macro_Z) | none |
| 60d beta, tracking error | 514 / 514 | 100% | yes (Macro_Z) | none |
| 60d max drawdown | 514 / 514 | 100% | yes (Macro_Z) | none |
| VaR95 / CVaR95 | 206 / 514 | 40.1% | diagnostic | computed for forecast-eligible names with numeric `mu`; 308 names below the forecast floor are `N/A`, not missing data |
| Kelly sizing | 206 / 514 | 40.1% | investability gate | beta-adjusted edge / tracking-error variance (L016-L017, L150); complete for the forecast-eligible set |
| Sharpe / Sortino / IR / Treynor / Calmar | 206 / 514 | 40.1% | diagnostic | complete for forecast-eligible names; true excess-return ratios (rf sourced, L007) |
| Technical pack (all timeframes) | see next table | ≥99.2% | yes (Tech_Z) | none |
| **Fundamental family** | **0 / 514** | **0%** | **NO — `UNAVAILABLE`** | **`Fund_Z` UNAVAILABLE; DQ → 0.80; blocks evidence threshold #2** (L144) |
| **Sentiment family** | **0 / 514** | **0%** | **NO — `UNAVAILABLE`** | **`Sent_Z` UNAVAILABLE; DQ → 0.80; blocks evidence threshold #2** (L145) |
| Options IV/skew, short interest, bid-ask, analyst revisions, institutional flow | 0 / 514 | 0% | no — **Enhancing** | DQ 0.80 + confidence cap; **never a `GO` blocker** (L146) |
| GICS sector | 24 / 24 published | 100% of published | portfolio constraint | would bind the 30% cap in a live book (L021) |
| Next earnings date | 56 names in bounded scoring passes (37 confirmed, 18 cadence-estimated, 1 print-week) | 100% of 24 published | penalty input | 5 published names penalized (L022–L024) |

**Data-quality consequence:** two of four families are `UNAVAILABLE` universe-wide and the entire Enhancing block is missing. The data-quality multiplier is **0.80** for every name — "notable coverage gaps" on the `rules.md § Data Quality Multiplier` scale. Because 0.80 < 0.85, **evidence threshold #4 independently forbids marking any name investable**, on top of the family gap.

**This is a data-quality limitation, not a `GO` blocker in itself.** Per `rules.md § Input Classification`, missing Enhancing inputs reduce confidence and exposure; they never block `GO` on their own. What blocks `GO` here is that `Fund_Z` and `Sent_Z` are *scoring families*, and their absence makes the "≥3 of 4 families non-negative" threshold unreachable by construction.

## Technical Indicator Coverage

From `technical_indicators.json` (L135): 518 required records, 517 `OK`, and FDXF explicitly `UNAVAILABLE` because it has only 40 usable bars.

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 (setup count only) | 517 / 518 | 517 / 518 | 517 / 518 |
| RSI(14) | 517 / 518 | 517 / 518 | 516 / 518 |
| MACD(12,26,9) | 517 / 518 | 517 / 518 | 513 / 518 |
| MA alignment | 517 / 518 | 516 / 518 | 509 / 518 |
| 20/60-bar momentum | 517 / 518 | 517 / 518 | 515 / 518 |
| 20-bar volume ratio | 517 / 518 | 517 / 518 | 515 / 518 |
| Relative strength vs SPY | 517 / 518 | 517 / 518 | 515 / 518 |

**Every timeframe clears the 70% threshold**, so RSI and MACD are permitted to contribute to `Tech_Z` rather than appearing only as diagnostics.

FDXF is unavailable at the record level. Among the 517 OK records, monthly MACD remains unavailable for GEV, Q, SNDK and SOLV; Q also lacks monthly RSI. Recent-listing monthly gaps are recorded as `UNAVAILABLE`, never hand-filled.

## Ranked Universe — Top 40

Full 514-name ranking is in `run_computed_manifest.json § full_universe_ranked_summary` and `§ records_all`. Score construction is documented in `05`.

| Rank | Ticker | Adj Score | Pctl | Tech_Z | Macro_Z | Penalty | Published? |
|---|---|---|---|---|---|---|---|
| 1 | TRV | +0.3705 | 100.0 | +1.124 | +0.840 | 0.00 | published |
| 2 | RTX | +0.3089 | 99.8 | +0.988 | +0.598 | 0.00 | published |
| 3 | PAYX | +0.3072 | 99.6 | +0.888 | +0.783 | 0.00 | published |
| 4 | DGX | +0.3058 | 99.4 | +0.891 | +0.766 | 0.00 | published |
| 5 | UNP | +0.2992 | 99.2 | +0.866 | +0.762 | 0.00 | published |
| 6 | PCG | +0.2807 | 99.0 | +0.726 | +0.888 | 0.00 | published |
| 7 | CSX | +0.2777 | 98.8 | +0.775 | +0.764 | 0.00 | published |
| 8 | WRB | +0.2523 | 98.6 | +0.544 | +1.015 | 0.00 | published |
| 9 | TMO | +0.2471 | 98.4 | +0.837 | +0.385 | 0.00 | published |
| 10 | NSC | +0.2423 | 98.2 | +0.634 | +0.751 | 0.00 | published |
| 11 | GD | +0.2366 | 98.0 | +1.024 | +0.757 | 0.10 | published |
| 12 | PM | +0.2286 | 97.9 | +0.649 | +0.608 | 0.00 | published |
| 13 | MPC | +0.2267 | 97.7 | +1.067 | +0.589 | 0.10 | published |
| 14 | CTAS | +0.2248 | 97.5 | +0.656 | +0.561 | 0.00 | published |
| 15 | SJM | +0.2245 | 97.3 | +0.563 | +0.745 | 0.00 | published |
| 16 | CB | +0.2205 | 97.1 | +0.430 | +0.976 | 0.00 | published |
| 17 | LMT | +0.2186 | 96.9 | +0.776 | +0.269 | 0.00 | published |
| 18 | WAB | +0.2103 | 96.7 | +0.848 | +0.057 | 0.00 | published |
| 19 | EQR | +0.2089 | 96.5 | +0.408 | +0.924 | 0.00 | published |
| 20 | PKG | +0.2040 | 96.3 | +0.810 | +0.081 | 0.00 | published |
| 21 | BNY | +0.1964 | 96.1 | +0.521 | +0.594 | 0.00 | published |
| 22 | MET | +0.1955 | 95.9 | +0.830 | +0.801 | 0.10 | published |
| 23 | MTB | +0.1905 | 95.7 | +0.431 | +0.726 | 0.00 | **excluded — 3rd-pass entrant, bounded-pass control** |
| 24 | AON | +0.1905 | 95.5 | +0.354 | +0.879 | 0.00 | **excluded — 3rd-pass entrant, bounded-pass control** |
| 25 | ESS | +0.1890 | 95.3 | +0.295 | +0.985 | 0.00 | **excluded — 3rd-pass entrant, bounded-pass control** |
| 26 | ITW | +0.1867 | 95.1 | +0.483 | +0.589 | 0.00 | **excluded — 3rd-pass entrant, bounded-pass control** |
| 27 | WM | +0.1862 | 94.9 | +0.306 | +0.939 | 0.00 | **excluded — 3rd-pass entrant, bounded-pass control** |
| 28 | VLO | +0.1859 | 94.7 | +0.946 | +0.491 | 0.10 | published |
| 29 | JNJ | +0.1834 | 94.5 | +0.355 | +0.819 | 0.00 | **excluded — 3rd-pass entrant, bounded-pass control** |
| 30 | HIG | +0.1830 | 94.3 | +0.681 | +0.997 | 0.10 | published |
| 31 | DUK | +0.1824 | 94.2 | +0.248 | +1.024 | 0.00 | below publication cut |
| 32 | CTVA | +0.1806 | 94.0 | +0.431 | +0.644 | 0.00 | below publication cut |
| 33 | AMP | +0.1804 | 93.8 | +0.469 | +0.566 | 0.00 | below publication cut |
| 34 | MNST | +0.1802 | 93.6 | +0.387 | +0.729 | 0.00 | below publication cut |
| 35 | GL | +0.1786 | 93.4 | +0.388 | +0.713 | 0.00 | below publication cut |
| 36 | VRSK | +0.1782 | 93.2 | +0.557 | +0.370 | 0.00 | below publication cut |
| 37 | PSA | +0.1765 | 93.0 | +0.345 | +0.781 | 0.00 | below publication cut |
| 38 | INCY | +0.1753 | 92.8 | +0.478 | +0.505 | 0.00 | below publication cut |
| 39 | FFIV | +0.1752 | 92.6 | +0.674 | +0.112 | 0.00 | below publication cut |
| 40 | STT | +0.1731 | 92.4 | +0.426 | +0.591 | 0.00 | below publication cut |

**Publication cut:** the 24 published names are the top-30 members admitted within the standing bounded second earnings pass. The **6 excluded** (MTB, AON, ESS, ITW, WM, JNJ) entered only on the *third* re-ranking pass, after that boundary had closed. Current audit-only earnings lookups exist for all six, but per the convention adopted 2026-07-20 and reaffirmed 2026-07-24 they are **excluded with disclosure** rather than introduced through an unbounded rank/fetch loop.

## Handoff to Factor Scoring

- Universe: **514 names**, percentiles labelled `INDEX_UNION_PCTL (n=514)`.
- Carry-forward bindings from `02 § 5`: **8 DROP** (CAT, GOOGL, GE, CVX, SHW, EQIX, GS, FCX), **6 DOWNGRADE** (LLY, UNH, BAC, JPM, V, AAPL). All eight DROP names independently sit below the 60th-percentile ranking floor, so the binding and the mechanical rank agree.
- `Fund_Z` / `Sent_Z` must be carried as `UNAVAILABLE` and must **not** count toward the 3-of-4 family threshold.
- Data-quality multiplier fixed at 0.80 universe-wide.
- Confidence capped at `MEDIUM` by the rank-IC feedback rule; `LOW` where the earnings penalty or the family gap binds.
