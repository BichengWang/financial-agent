# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-04 (**Saturday — U.S. markets closed**; Independence Day observed 2026-07-03; last completed session 2026-07-02) |
| Model | claude-fable-5 |
| Run mode | Manual weekend run of `investments/equity/daily_investment_system/main.md` (runbook holiday rule extended to the closed weekend: publish a full REVIEW_ONLY set, no skipped days in the audit trail) |
| Data mode | DELAYED — official 2026-07-02 closes fetched this run at 2026-07-04T18:28:10Z (freshest completed session; <=1-day lag vs that session). Same declaration and rationale as claude-fable-5-2026-07-03; gpt-5-2026-07-04 declared DELAYED_PARTIAL for the identical state — the standing mode-label divergence is tracked in 13 |
| Status target | REVIEW_ONLY (weekend — no executable session) |
| Final status | **REVIEW_ONLY** |
| Retrieved at | 2026-07-04T18:28:10Z (521/521 universe+ETF+macro bars, official 2026-07-02 closes); 2026-07-04T18:31:54+00:00Z Nasdaq cross-check (0.000% divergence on all 26 published names); 2026-07-04T18:36Z IBKR MCP closed-market snapshots returned 2026-07-01 prior-session closes matching recorded values exactly |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee, Evolution |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (4th consecutive run; Track B proposal pending HUMAN_REVIEW — see 13) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-20..2026-06-13, target 2026-06-06; baseline 4d from target; folder 24d old). Sub-21d folders (fable 07-01/02/03, sonnet 07-02/03, gpt-5 07-03/04, gemini 07-01) used as short-window cross-checks only |
| Prediction settlement summary | 0 settled — no OPEN prediction has target_date <= 2026-07-04; scanned 27 prior ledgers, 491 OPEN records; earliest due 2026-07-08 (this model's 2026-06-10 vintage, 12 records — settle on Wednesday's run) |
| Source Ledger coverage | OBSERVED 56; DERIVED 129; INFERRED 23; ILLUSTRATIVE 0; UNAVAILABLE 0 (208 rows) |
| Status eligibility | All 5 Required inputs grounded to the last completed session → data-eligible; REVIEW_ONLY by the weekend/holiday rule (family gate would independently force NO_TRADE on a trading day) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records in 15 |
| Universe | 515 union; **514 eligible** — only FDXF rejected (26 bars); INDEX_UNION_PCTL (n=514); sampled fallback NOT used |
| rf note | Yahoo ^IRX series still lags the holiday: freshest row 3.663% @ 2026-06-26 (HISTORICAL, cited); ratios use rf_1m 0.305% |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (pre-check -> REVIEW_ONLY/weekend) -> RISK_REVIEW (APPROVE) -> PUBLISHED (REVIEW_ONLY) -> EVOLUTION_REVIEW`

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Official 2026-07-02 closes: Yahoo chart fetch (2026-07-04T18:28:10Z) + Nasdaq last-sale cross-check (2026-07-04T18:31:54+00:00Z) identical to the penny (0.000%) on all 26 published names; IBKR MCP on the closed market serves 2026-07-01 prior-session closes matching our records exactly (SPY 745.76, QQQ 725.17) | No |
| ~60 trading days history | PASS | 5y daily bars ending 2026-07-02 for 521/521 fetched symbols (515 universe + ETFs + macro series) | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | Cadence estimates ESTIMATED (±5d) for the 64-name shortlist; 18 shortlist names inside the <=19d buffered window penalized -0.10 (incl. LII and URI newly vs 07-03), none published | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO is nonetheless unavailable today: markets are closed (Saturday of the Independence Day weekend) — no executable session exists (weekend/holiday rule → REVIEW_ONLY).

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed → DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00–09 | PRESENT |
| 10_midday_monitor.md / 11_preclose_check.md / 12_close_log.md | N/A NOTES (no trading session) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | N/A NOTE (Saturday; the week-ending-07-03 review was published in claude-fable-5-2026-07-03) |
| 15_predictions.json (23 EQUITY_ALPHA + 3 MARKET_FORECAST, settlements []) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (month-end is 2026-07-31) |
| eligible_universe.txt / universe_summary.json / technical_indicators.json (517 OK, FDXF short-history) | PRESENT |
