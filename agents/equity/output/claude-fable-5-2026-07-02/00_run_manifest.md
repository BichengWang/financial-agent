# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-02 |
| Model | claude-fable-5 |
| Run mode | Manual intraday run of `investments/equity/daily_investment_system/main.md` (executed ~19:20–19:55Z ≈ 15:20–15:55 ET; ~40 min before the close, last session before the 2026-07-03 holiday) |
| Data mode | LIVE (intraday prints, two-source verified + brokerage MCP corroboration) |
| Status target | GO if live-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** |
| Retrieved at | 2026-07-02T19:21:22Z (universe bars); ~19:29Z (Nasdaq cross-check, max divergence 0.635%); 19:25Z (IBKR live snapshots, max divergence 0.18%) |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee, Evolution |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (2nd consecutive run; also hit by gpt-5-2026-07-02 this morning) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-18..2026-06-11, target 2026-06-04; baseline 6d from target; folder 22d old, ≥21d invariant satisfied). Sub-21d folders (claude-fable-5-2026-07-01, gpt-5-2026-07-02) used only as short-window cross-checks |
| Prediction settlement summary | 0 settled — no OPEN prediction has target_date ≤ 2026-07-02; scanned 21 prior ledgers, 369 OPEN records; earliest due 2026-07-08 (this model's 2026-06-10 vintage, 12 records) |
| Source Ledger coverage | OBSERVED 56; DERIVED 129; INFERRED 23; ILLUSTRATIVE 0; UNAVAILABLE 0 (208 rows) |
| Status eligibility | All 5 Required inputs grounded → GO-eligible on data; NO_TRADE on evidence thresholds (0 investable < 5, stop criterion #1) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records in 15 |
| Universe | 515 index-union names; 513 eligible (SATS stale, FDXF short history); INDEX_UNION_PCTL (n=513); sampled fallback NOT used |
| Engine correction this run | Total per-name mu adjustment now clamped at ±2pp per the Calibration Table (the 2026-07-01 UNH record had stacked −3pp; disclosed in 02 §6 and 13; that prediction stands as recorded) |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (feasibility pre-check -> NO_TRADE, no weights drafted) -> RISK_REVIEW (APPROVE) -> PUBLISHED (NO_TRADE) -> EVOLUTION_REVIEW` (close checkpoint pending at publication — run precedes the 16:00 ET close)

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo v8 intraday prints cross-checked vs api.nasdaq.com for all 23 published names + 3 ETFs (max divergence 0.635%); IBKR MCP live snapshots corroborate SPY/QQQ/SOXX/DVA/HUM/FFIV/MAS (≤0.18%) | No |
| ~60 trading days history | PASS | 5y daily bars for 519/520 tickers incl. today's (partial) bar; 61-bar minimum enforced | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D from fetched bars for every published name and ETF | No |
| Next earnings date | PASS | Cadence estimates ESTIMATED (±5d) for the full 58-name shortlist; 11 names inside the ≤19d buffered window penalized −0.10 (none published) | No |
| Index-union universe | PASS | 503∪101−89 = 515; `eligible_universe.txt` + `universe_summary.json` published | No |

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed. Applied as DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE). The GO blocker is evidence-threshold arithmetic — see 05 and 13.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | PRESENT |
| 01_preflight.md (Source Ledger, 208 rows) | PRESENT |
| 02_reflection.md | PRESENT |
| 03_regime_and_data.md (Core ETF block) | PRESENT |
| 04_universe_summary.md | PRESENT |
| 05_factor_scores.md | PRESENT |
| 06_top_candidates.md | PRESENT |
| 07_portfolio_proposal.md (NO_TRADE) | PRESENT |
| 08_risk_review.md | PRESENT |
| 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PLACEHOLDER (single intraday run) |
| 11_preclose_check.md | PRESENT (folded — run executed in the pre-close window) |
| 12_close_log.md | PLACEHOLDER (publication precedes the close) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | N/A NOTE (Thursday; Friday 2026-07-03 is a market holiday) |
| 15_predictions.json (23 EQUITY_ALPHA + 3 MARKET_FORECAST, settlements []) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (not month-end) |
| eligible_universe.txt / universe_summary.json | PRESENT |
| technical_indicators.json (517 OK / 1 UNAVAILABLE) | PRESENT |
