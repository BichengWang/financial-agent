# 00 — Run Manifest · 2026-09-03

| Field | Value |
|---|---|
| Run date | **2026-09-03** (Thursday, a completed U.S. trading session) |
| Model | `claude-opus-5` |
| Fire window | 18:11 ET — post-close |
| Run mode | scheduled daily run, full pipeline |
| Data mode | **`DELAYED`** (`rules.md § Data Mode Taxonomy`) |
| Price basis | 2026-09-03 completed close |
| Status target | `GO` if the evidence thresholds could be met |
| **Final status** | **`NO_TRADE`** |
| Universe label | `INDEX_UNION_PCTL (n=508)` |
| Reflection baseline | `agents/equity/output/claude-opus-5-2026-08-06` |
| Baseline flag | `OK` — delta 0d from the 2026-08-06 target; no tie at that delta |

## State-transition log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW ->
PUBLISHED -> EVOLUTION_REVIEW`

| State | Outcome |
|---|---|
| PRECHECK | universe union 515 built; 518/519 histories fetched; 22 names re-fetched to vendor convergence |
| REFLECTION | 111 of 113 due keys settled, 0 conflicts; baseline `claude-opus-5-2026-08-06` |
| DATA_OK | regime `BULL`; all five Required inputs grounded |
| TECHNICALS_OK | `technical_indicators.py` OK on 518 symbols |
| SCORED | 508 names scored; 24 published, ranks 1-24 contiguous |
| PORTFOLIO_DRAFT | Task-0 feasibility pre-check passed; investable set empty, no weights drafted |
| RISK_REVIEW | `APPROVE` for publication as `NO_TRADE` |
| PUBLISHED | `NO_TRADE` |
| EVOLUTION_REVIEW | one Track B `ACCEPT`; Track A eligible and deliberately `DEFER`red |

## GO-Gate Table (Required inputs only)

| # | Required input | Status |
|---|---|---|
| 1 | Grounded entry price per the Price Sourcing Standard | **PASS** — 27/27 on three independent sources (L012a) |
| 2 | ~60 trading days of fetched history per name and for SPY | **PASS** — 518/519 symbols x 5Y daily (L002) |
| 3 | sigma via the Sigma Fallback Chain | **PASS** — `REALIZED_VOL_30D` on all 24 published names and 3 ETFs |
| 4 | Next earnings date — confirmed or cadence-estimated | **PASS** — complete 27-day forward sweep, 0 failures (L010) |
| 5 | Index-union universe from `build_index_universe.py` | **PASS** — union 515 (L001) |

**All five Required inputs are grounded, so `GO` is not blocked by data availability.** The run is
`NO_TRADE` on candidate quality.

Enhancing inputs missing — caps, never blockers (`L023`): options IV/skew, short interest/borrow,
bid-ask spread tape, analyst revision tape, institutional ownership flow. Effect: data-quality
multiplier 0.80, confidence capped `MEDIUM`, and a 50% gross cap would apply if a `GO`
were ever reached.

## Prediction settlement summary

| Quantity | Value |
|---|---|
| Due at run start | 113 |
| Settled this run | 111 (96 EQUITY_ALPHA + 15 MARKET_FORECAST) |
| Left due — corporate action | 2 |
| Conflicts | 0 |
| Rejected candidate rows | 87 |
| Canonical rolling `EQUITY_ALPHA` | raw n **1451**, 28-day eff_n **3** |
| Canonical rolling `MARKET_FORECAST` | raw n **216**, 28-day eff_n **2** |
| Track A calibration gate | EQUITY_ALPHA **True** (first time in the series); MARKET_FORECAST False |

## Source Ledger coverage

| Metric | Value |
|---|---|
| Total ledger rows | 180 |
| Rows per published ticker | 5 (entry price, indicator states, momentum/RS, risk analytics, earnings) plus shared L002/L013/L020 lineage |
| Status eligibility | `GO`-eligible on Required inputs; blocked on evidence thresholds 2/3/4 |

| Freshness tag | Rows |
|---|---|
| DELAYED | 173 |
| HISTORICAL | 2 |
| UNAVAILABLE | 5 |

## Core ETF Market Forecast Block

| ETF | Record written | mu | sigma | Target date |
|---|---|---|---|---|
| SPY | yes | +2.00% | 3.30% | 2026-10-01 |
| QQQ | yes | +1.90% | 5.71% | 2026-10-01 |
| SOXX | yes | +4.98% | 13.88% | 2026-10-01 |

Status: **complete** — analysis block in `03`, summary in `09`, three `MARKET_FORECAST` records in
`15_predictions.json` with `benchmark: "NONE"`, `benchmark_price: null`, `adj_score: null`.

## Durable artifact checklist

Composed **after** the artifacts were written, by listing the package directory. A checklist
written before the files exist is how the 2026-08-06, 08-07 and 08-14 packages came to claim
artifacts they never published.

| Artifact | State | Contents |
|---|---|---|
| 00_run_manifest.md | **Published** | this file |
| 01_preflight.md | **Published** | Source Ledger — grounding gate |
| 02_reflection.md | **Published** | settlement + rolling calibration + MoM |
| 03_regime_and_data.md | **Published** | regime + Core ETF Market Forecast Block |
| 04_universe_summary.md | **Published** | universe construction + coverage |
| 05_factor_scores.md | **Published** | Adj Score explainability |
| 06_top_candidates.md | **Published** | monitoring sleeve, empty investable set |
| 07_portfolio_proposal.md | **Published** | NO_TRADE, feasibility pre-check + diagnostic sleeve |
| 08_risk_review.md | **Published** | committee decision |
| 09_final_report.md | **Published** | final report |
| 13_evolution_log.md | **Published** | one Track B accepted, Track A deferred |
| 15_predictions.json | **Published** | publishing gate |

No files outside the contract are present in the package directory.

## Working-data checklist (gitignored `.work/`, not published)

| Helper / artifact | Result | Detail |
|---|---|---|
| `build_index_universe.py` | **success** | 503 + 101, overlap 89, union 515; caches fetched_at 2026-06-21T21:05:56Z |
| stockanalysis 5Y bulk history | **success** | 518/519 in 58.8s at 8 workers; 516 last bars on the basis date |
| `technical_indicators.py` | **success** | 518 symbols, daily/weekly/monthly blocks, computed from the adjusted-close CSV tree |
| `settlement_ledger.py` (pre and post write) | **success** | due 113 -> 2, conflicts 0 |
| Nasdaq screener | **success** | 7141 rows (market cap + sector) |
| Forward earnings calendar sweep | **success** | 27/27 business days, 0 transport failures |
| Risk-free rate | **fallback** | FRED DTB3 timed out (10th consecutive); Treasury CSV gave 3.75% |
| VIX | **success** | CNBC `.VIX` 14.32 on the basis date; CBOE's file lags one session and its T-1 row matches CNBC `previous_day_closing` to the cent |
| IBKR MCP | **not attempted** | connector invalidated since 2026-08-04 (L017) |
| Corporate-action / liveness screen | **success** | 25 flagged: 22 `VENDOR_BAR_LAG` (recovered), 3 genuine corporate actions |

## Outstanding blockers

| # | Blocker | Owner |
|---|---|---|
| 1 | `Fund_Z` and `Sent_Z` `UNAVAILABLE` universe-wide — Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk SEC `companyfacts` + threaded Nasdaq sentiment across ~510 names) is not implemented. This single gap makes evidence thresholds 2, 3 and 4 unsatisfiable and is the sole reason every run since July has been `NO_TRADE`. | plan Phase 2 |
| 2 | Aggregate rank IC negative across vintages; confidence permanently capped `MEDIUM`. Track A is now *eligible* on evidence but the defect is ordinal and every tested remedy has been a monotonic transform. | `13` |
| 3 | Constituent caches are 74 days stale, which is what leaves renamed/delisted names in the union and permanently strands prediction keys. | maintenance |
| 4 | No scheduler job is active (`runbook.md § Scheduler`); runs remain manual. | maintenance |
