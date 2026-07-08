# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-03 (**U.S. market holiday** — Independence Day observed; no trading session) |
| Model | claude-fable-5 |
| Run mode | Manual holiday run of `investments/equity/daily_investment_system/main.md` (executed ~20:28–21:0xZ ≈ 13:28 PT); runbook holiday rule: publish a full set, no skipped days |
| Data mode | DELAYED — official 2026-07-02 closes fetched this run (≤1-day lag). Runbook names ILLUSTRATIVE_MODE for holidays; fetched real closes dominate reference-state values under the Non-Fabrication Contract, so DELAYED is declared and the deviation documented (01/03/13). gpt-5-2026-07-03 declared DELAYED_PARTIAL for the same state — label divergence noted in 13 |
| Status target | REVIEW_ONLY (holiday — no executable session) |
| Final status | **REVIEW_ONLY** |
| Retrieved at | 2026-07-03T20:29Z (universe bars, official 07-02 closes); ~20:5xZ Nasdaq cross-check (0.000% divergence on all 26 published names); IBKR snapshots on the closed market returned prior-session (07-01) closes matching our records exactly |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee, Evolution (+ weekly review, Friday) |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (3rd consecutive run; Track B proposal pending HUMAN_REVIEW — see 13) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-19..2026-06-12, target 2026-06-05; baseline 5d from target; folder 23d old). Sub-21d folders (fable 07-01/07-02, gpt-5 07-03) used as short-window cross-checks only |
| Prediction settlement summary | 0 settled — no OPEN prediction has target_date ≤ 2026-07-03; scanned 23 prior ledgers, 412 OPEN records; earliest due 2026-07-08 (this model's 2026-06-10 vintage, 12 records — next run with a session) |
| Source Ledger coverage | OBSERVED 56; DERIVED 129; INFERRED 23; ILLUSTRATIVE 0; UNAVAILABLE 0 (208 rows) |
| Status eligibility | All 5 Required inputs grounded to the last completed session → data-eligible; REVIEW_ONLY by holiday rule (family gate would independently force NO_TRADE on a trading day) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records in 15 |
| Universe | 515 union; **514 eligible** — SATS re-eligible (traded 07-02), only FDXF rejected; INDEX_UNION_PCTL (n=514); sampled fallback NOT used |
| rf note | Yahoo ^IRX series lags holidays: freshest row 3.663% @ 2026-06-26 (HISTORICAL, cited); ratios use rf_1m 0.305% |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (pre-check -> REVIEW_ONLY/holiday) -> RISK_REVIEW (APPROVE) -> PUBLISHED (REVIEW_ONLY) -> EVOLUTION_REVIEW (+ weekly review)`

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Official 2026-07-02 closes: Yahoo chart fetch + Nasdaq last-sale identical to the penny (0.000%) for all 26 published names; IBKR (closed market) verifies prior-session records | No |
| ~60 trading days history | PASS | 5y daily bars ending 2026-07-02 for 519/520 tickers | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | Cadence estimates ESTIMATED (±5d) for the 64-name shortlist; 14 names inside the ≤19d buffered window penalized (incl. PPG, GPC newly), none published | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO is nonetheless unavailable today: no trading session exists (holiday rule → REVIEW_ONLY).

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed → DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00–09 | PRESENT |
| 10_midday_monitor.md / 11_preclose_check.md / 12_close_log.md | N/A NOTES (no trading session) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | **PRESENT — real weekly review (Friday, published under the holiday rule)** |
| 15_predictions.json (23 EQUITY_ALPHA + 3 MARKET_FORECAST, settlements []) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (month-end is 2026-07-31) |
| eligible_universe.txt / universe_summary.json / technical_indicators.json (517 OK) | PRESENT |
