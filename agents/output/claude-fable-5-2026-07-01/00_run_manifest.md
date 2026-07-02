# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-01 |
| Model | claude-fable-5 |
| Run mode | Manual post-close run of `investments/equity/daily_investment_system/main.md` (executed ~22:36–23:30Z; market closed 20:00Z) |
| Data mode | DELAYED (2026-07-01 official closes, fetched post-close; two-source verified) |
| Status target | GO if live-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** |
| Retrieved at | 2026-07-01T22:37:20Z (universe bars); 2026-07-01T23:03Z (Nasdaq cross-check); IBKR MCP snapshots ~23:19–23:27Z |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee, Evolution |
| Outstanding blockers | Fundamental + Sentiment factor families have no wired source at index-union scale → evidence threshold #2 (3-of-4 families) unsatisfiable → investable set empty |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (in window 2026-05-17..2026-06-10; 7d from the 28d target — at the gap threshold, not over it; folder exactly 21d old, ≥21d invariant satisfied) |
| Prediction settlement summary | 0 settled — no OPEN prediction has target_date ≤ 2026-07-01; scanned 18 prior ledgers, 308 OPEN records; earliest due 2026-07-08 (this model's 2026-06-10 vintage) |
| Source Ledger coverage | OBSERVED 57; DERIVED 133; INFERRED 24; ILLUSTRATIVE 0; UNAVAILABLE 0 (214 rows; fund/sent families declared UNAVAILABLE in prose/tables, not as ledger value rows) |
| Status eligibility | All 5 Required inputs grounded → GO-eligible on data; NO_TRADE on evidence thresholds (0 investable < 5 minimum, stop criterion #1) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records in 15 |
| Universe | 515 index-union names (`build_index_universe.py`, caches 2026-06-21); 513 eligible; INDEX_UNION_PCTL (n=513); sampled fallback NOT used |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (feasibility pre-check -> NO_TRADE, no weights drafted) -> RISK_REVIEW (APPROVE) -> PUBLISHED (NO_TRADE) -> CLOSE_LOGGED (folded: post-close run) -> EVOLUTION_REVIEW`

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo v8 chart closes (per-ticker URL + retrieved_at) cross-checked against api.nasdaq.com for all 24 published names + 3 ETFs (max divergence 0.845%, all <1%); IBKR MCP snapshots corroborate SPY/QQQ/SOXX/DVA/HUM/FFIV/MAS. Ledger L013+ | No |
| ~60 trading days history | PASS | 5y daily bars for 519/520 tickers incl. the 2026-07-01 close; min 61-bar screen enforced (FDXF rejected) | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched bars for every published name and ETF; no sigma emitted without source | No |
| Next earnings date | PASS | Cadence estimates (prior report + ~91d) tagged ESTIMATED (±5d) for the full shortlist; 7 names inside the 19d buffered window penalized −0.10 (only UNH published) | No |
| Index-union universe | PASS | `build_index_universe.py` succeeded: 503∪101−89 = 515; `eligible_universe.txt` + `universe_summary.json` published | No |

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed. Effect applied: DQ 0.80, confidence capped LOW, family contributions 0.00 (UNAVAILABLE). Per rules.md they are not cited as GO blockers; the GO blocker is evidence threshold #2 arithmetic (see 05, 13).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | PRESENT |
| 01_preflight.md (Source Ledger, 214 rows) | PRESENT |
| 02_reflection.md | PRESENT |
| 03_regime_and_data.md (Core ETF block) | PRESENT |
| 04_universe_summary.md | PRESENT |
| 05_factor_scores.md | PRESENT |
| 06_top_candidates.md | PRESENT |
| 07_portfolio_proposal.md (NO_TRADE) | PRESENT |
| 08_risk_review.md | PRESENT |
| 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PLACEHOLDER (post-close run) |
| 11_preclose_check.md | PLACEHOLDER (post-close run) |
| 12_close_log.md | PRESENT (folded into main run) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | N/A NOTE (Wednesday) |
| 15_predictions.json (24 EQUITY_ALPHA + 3 MARKET_FORECAST, settlements []) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (not month-end) |
| eligible_universe.txt / universe_summary.json | PRESENT |
| technical_indicators.json (517 OK / 1 UNAVAILABLE) | PRESENT |
