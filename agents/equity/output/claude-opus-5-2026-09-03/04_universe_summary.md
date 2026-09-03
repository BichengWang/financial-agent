# 04 — Universe Summary · 2026-09-03

## Construction

| Step | Count | Source |
|---|---|---|
| S&P 500 constituents (cache) | 503 | sp500.json fetched_at 2026-06-21T21:05:56Z (L001) |
| Nasdaq-100 constituents (cache) | 101 | nasdaq100.json fetched_at 2026-06-21T21:05:56Z (L001) |
| Overlap | 89 | DERIVED (L001) |
| **Index union** | **515** | `build_index_universe.py` (L001) |
| Price history fetched | 518/519 | stockanalysis 5Y (L002) |
| **Scored universe after filters** | **508** | this artifact, below |

Percentiles in `05`/`06`/`15` are labelled **`INDEX_UNION_PCTL (n=508)`**. The
constituent caches are **74 days old**;
`rules.md § Index-Union Universe Protocol` rule 5 says to use them as-is and log the
`fetched_at` values, which L001 does. Staleness is what leaves renamed or delisted names in the
union — this run found 3 such names (below), all caught before scoring.

## Inclusion filters applied

| Filter | Threshold | Applied to |
|---|---|---|
| Listing | U.S. primary exchange | implicit in the index-union source (L001) |
| Market cap | > $2B | Nasdaq screener `marketCap` (L009), alias-corrected (L009a) |
| Average daily dollar volume | > $20M over 20 sessions | DERIVED from raw close x volume (L002) |
| Price | > $5 | basis-date raw close (L002) |
| Listing age | > 6 months | first fetched bar (L002a) |
| Session coverage | >= 80% of the trailing 60 sessions | DERIVED from the bar dates (L002) |
| Indicator completeness | daily and weekly MA alignment resolvable | `technical_indicators.py` (L013) |

## Inclusion / exclusion log

| Reason | Names | Tickers |
|---|---|---|
| CORPORATE_ACTION_OR_STALE_TAPE | 3 | AVB, EA, EQR |
| MARKET_CAP_UNAVAILABLE | 2 | BF-B, SATS |
| INSUFFICIENT_HISTORY | 2 | FDXF, Q |

### Corporate-action and liveness screen

Track B accepted 2026-08-22 (effective 08-23): any symbol whose last bar predates the basis, or
whose fetch transport-fails, is classified against **two independent references** — the Nasdaq
screener tape (L009) and a CNBC quote gated by the 2026-08-28 symbol-reuse rule.

| Ticker | Classification | stockanalysis last bar | Screener row | CNBC gate | Open prediction keys | Detail |
|---|---|---|---|---|---|---|
| AVB | `CORPORATE_ACTION_DELISTED_OR_RENAMED` | 2026-08-14 | **absent** | fail — NO_LAST | 0 | absent from the Nasdaq screener tape and CNBC returns no usable US quote; last stockanalysis bar 2026-08-14 |
| EA | `CORPORATE_ACTION_DELISTED_OR_RENAMED` | 2026-08-04 | **absent** | fail — NO_LAST | 0 | absent from the Nasdaq screener tape and CNBC returns no usable US quote; last stockanalysis bar 2026-08-04 |
| EQR | `SYMBOL_REUSE_FOREIGN_LISTING` | fetch failed | **absent** | fail — SYMBOL_REUSE_FOREIGN_LISTING:ASX | 2 | CNBC returns 'EQ Resources Ltd' on ASX - the US listing is gone and the ticker has been reused on a foreign venue |

The screen is a **fire-time** observation: it classifies against the first bulk fetch, the state
that tripped the trigger, and records what convergence later resolved.

**It produced a class it has not produced before: `VENDOR_BAR_LAG`.** 22 names were
flagged by the last-bar test at the 18:11 ET fetch yet passed *both* independent references — a
Nasdaq screener row and a live CNBC basis-date US-venue quote with non-zero volume. These are not
corporate actions; the primary vendor simply had not published their 2026-09-03 bar that early. The
lagging set was re-polled every ~7 minutes and drained to zero at
**19:27 ET** (207 minutes after the
close), after which the bulk history was re-fetched and **22 of
22** resolved. All 22 are scored normally in this package.

Had the run treated the last-bar test as decisive on its own, those 22 live
large-caps would have been dropped and labelled corporate actions — and the published book would
have differed by **3 of 24 names** (`13` carries the computed counterfactual).

| Ticker | Screener name | CNBC exchange | CNBC basis-date close | First-fetch bar | Final-fetch bar |
|---|---|---|---|---|---|
| AIG | American International Group Inc. New Co | NYSE | 76.86 | 2026-09-02 | 2026-09-03 |
| AWK | American Water Works Company Inc. Common | NYSE | 140.89 | 2026-09-02 | 2026-09-03 |
| BA | Boeing Company (The) Common Stock | NYSE | 210.51 | 2026-09-02 | 2026-09-03 |
| BEN | Franklin Templeton Inc. Common Stock | NYSE | 33.55 | 2026-09-02 | 2026-09-03 |
| BG | Bunge Limited Common Shares | NYSE | 120.12 | 2026-09-02 | 2026-09-03 |
| CNP | CenterPoint Energy Inc (Holding Co) Comm | NYSE | 39.98 | 2026-09-02 | 2026-09-03 |
| ELV | Elevance Health Inc. Common Stock | NYSE | 414.78 | 2026-09-02 | 2026-09-03 |
| FDS | FactSet Research Systems Inc. Common Sto | NYSE | 312.96 | 2026-09-02 | 2026-09-03 |
| FOX | Fox Corporation Class B Common Stock | NASDAQ | 60.47 | 2026-09-02 | 2026-09-03 |
| MTB | M&T Bank Corporation Common Stock | NYSE | 240.06 | 2026-09-02 | 2026-09-03 |
| OMC | Omnicom Group Inc. Common Stock | NYSE | 84.73 | 2026-09-02 | 2026-09-03 |
| RJF | Raymond James Financial Inc. Common Stoc | NYSE | 181.10 | 2026-09-02 | 2026-09-03 |
| RL | Ralph Lauren Corporation Common Stock | NYSE | 344.20 | 2026-09-02 | 2026-09-03 |
| SBAC | SBA Communications Corporation Class A C | NASDAQ | 191.52 | 2026-09-02 | 2026-09-03 |
| STE | STERIS plc (Ireland) Ordinary Shares | NYSE | 226.83 | 2026-09-02 | 2026-09-03 |
| STZ | Constellation Brands Inc. Common Stock | NYSE | 129.09 | 2026-09-02 | 2026-09-03 |
| SW | Smurfit WestRock plc Ordinary Shares | NYSE | 45.26 | 2026-09-02 | 2026-09-03 |
| TFC | Truist Financial Corporation Common Stoc | NYSE | 51.61 | 2026-09-02 | 2026-09-03 |
| VRSK | Verisk Analytics Inc. Common Stock | NASDAQ | 190.60 | 2026-09-02 | 2026-09-03 |
| VTRS | Viatris Inc. Common Stock | NASDAQ | 16.94 | 2026-09-02 | 2026-09-03 |
| WEC | WEC Energy Group Inc. Common Stock | NYSE | 106.70 | 2026-09-02 | 2026-09-03 |
| WST | West Pharmaceutical Services Inc. Common | NYSE | 342.73 | 2026-09-02 | 2026-09-03 |

## Sector composition of the scored universe

| Sector | Names | Share |
|---|---|---|
| Consumer Discretionary | 102 | 20.08% |
| Industrials | 86 | 16.93% |
| Technology | 80 | 15.75% |
| Finance | 68 | 13.39% |
| Health Care | 56 | 11.02% |
| Utilities | 37 | 7.28% |
| Real Estate | 26 | 5.12% |
| Consumer Staples | 21 | 4.13% |
| Energy | 16 | 3.15% |
| Telecommunications | 10 | 1.97% |
| Basic Materials | 5 | 0.98% |
| UNAVAILABLE | 1 | 0.20% |

## Metric coverage summary

Which `rules.md § Financial Metrics and Score Attribution` inputs are sourceable across the
eligible universe:

| Metric group | Sourceable | Status | Effect |
|---|---|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, Calmar, beta, tracking error) | 508/508 (100.00%) | **AVAILABLE** | feeds Technical and Macro z-scores |
| Tail risk (60d max DD, VaR95, CVaR95) | 508/508 (100.00%) | **AVAILABLE** | `dd60` is a Tech_Z slot; VaR/CVaR are displayed diagnostics |
| Sizing (raw Kelly, 0.25x Kelly) | 508/508 (100.00%) | **AVAILABLE** | investability gate and confidence cap |
| Technical (momentum, RS, MA, volume, TD-9, RSI, MACD) | 508/508 (100.00%) | **AVAILABLE** | six equal-weighted Tech_Z slots |
| Fundamental / quality | 0/508 (0.00%) | **UNAVAILABLE** (L021) | family excluded from the score and from the 3-of-4 threshold; lowers DQ to 0.80 |
| Sentiment / positioning | 0/508 (0.00%) | **UNAVAILABLE** (L022) | same as above |

The two `UNAVAILABLE` families are a **capability gap**, not a market judgment: no fetch path is
wired for them across the full universe (`rules.md § SHADOW Diagnostic Tooling` — the diagnostics
scripts exist but Phase 2 bulk coverage is not implemented, so the 70%-of-universe sourceability
bar is unmet). This affects data quality and blocks investability; it does **not** block `GO` on
the Required-input test, which is why `01`'s GO-Gate Table reads all-PASS while `06` reports an
empty investable set.

## Technical indicator coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 508/508 (100.00%) | 508/508 (100.00%) | 508/508 (100.00%) |
| RSI(14) | 508/508 (100.00%) | 508/508 (100.00%) | 508/508 (100.00%) |
| MACD(12,26,9) state | 508/508 (100.00%) | 508/508 (100.00%) | 508/508 (100.00%) |
| MA alignment | 508/508 (100.00%) | 508/508 (100.00%) | 508/508 (100.00%) |
| 20/60-bar momentum | 508/508 (100.00%) | 508/508 (100.00%) | 507/508 (99.80%) |
| Volume ratio | 508/508 (100.00%) | 508/508 (100.00%) | 508/508 (100.00%) |
| Relative strength vs SPY | 508/508 (100.00%) | 508/508 (100.00%) | 507/508 (99.80%) |

All seven indicator groups clear the 70%-of-universe bar in `rules.md § Technical Indicator Pack
Definition`, so RSI and MACD may contribute to `Tech_Z` rather than appearing only as diagnostics.
Relative strength is computed, displayed and ledgered but is **not** a `Tech_Z` slot (Track B
effective 2026-08-03): under a single common benchmark its cross-sectional z-score is identical to
the corresponding momentum z-score.
