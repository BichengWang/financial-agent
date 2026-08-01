# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-30 |
| Model | gpt-5 |
| Run mode | Manual automation run of `agents/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | GO if all evidence and portfolio gates pass; otherwise NO_TRADE |
| Final status | NO_TRADE |
| Retrieved at | 2026-08-01T19:27:20Z |
| Market-session note | Retrospective continuation of the post-close run; observations remain fixed to the completed 2026-07-30 close, while current-run retrieval timestamps transparently extend through 2026-08-01. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Fund_Z/Sent_Z remain unpromoted; no name reaches the 3-of-4 family threshold. |
| Reflection baseline | `agents/equity/output/gpt-5-2026-07-02` |
| Baseline flag | SAME_MODEL_BASELINE; exact 28-day target; three tied 2026-07-02 folders disclosed; conclusion not invariant |
| Prediction settlement summary | 0 settled this run; upstream same-day package already canonicalized 58; canonical EQ n=347 eff_n=1; MF n=63 eff_n=1; due=0; conflicts=0 |
| Source Ledger coverage | OBSERVED 10; DERIVED 53; INFERRED 2; UNAVAILABLE 3 |
| Status eligibility | All five Required inputs grounded; quality/family and portfolio gates force NO_TRADE |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Nasdaq completed-session close + Yahoo raw-close audit, 23/23 inside 1% | No |
| ~60 trading days history | PASS | 517/518 technical records OK; FDXF excluded before ranking | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D from adjusted closes | No |
| Next earnings date | PASS | All 500 scored names carry an exact or prior-report+91d `ESTIMATED (±5d)` date; universe coverage 512/515 with unresolved names excluded before scoring; complete 26/26 forward and 87/87 historical Nasdaq pages; accepted 2026-07-29 Track B forward-sweep cross-check | No |
| S&P 500 ∪ Nasdaq-100 universe | PASS | 515 tickers from local caches | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision data, and institutional ownership flow are unavailable. They lower DQ and confidence but are not GO blockers. Fund_Z/Sent_Z remain SHADOW/unpromoted, so the 3-of-4 investability gate cannot be met.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md through 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PRESENT — retrospective checkpoint; no position |
| 11_preclose_check.md | PRESENT — retrospective checkpoint; no position |
| 12_close_log.md | PRESENT — completed July 30 close logged |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | NOT APPLICABLE — Thursday |
| 15_predictions.json | PRESENT — 23 OPEN + 0 new settlements |
| 16_monthly_review.md | NOT APPLICABLE — last trading day is 2026-07-31 |
| eligible_universe.txt / universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT — 517/518 OK |
