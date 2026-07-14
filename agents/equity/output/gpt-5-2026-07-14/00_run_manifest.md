# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-14 |
| Model | gpt-5 |
| Run mode | Automation run of `agents/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | `NO_TRADE` unless at least five names satisfy the multi-family and 85% completeness gates. |
| Final status | `NO_TRADE` |
| Timing | Late daily full-pipeline run started 2026-07-14 13:04 ET, after the manual 12:15 ET checkpoint. It is not labeled pre-open. |
| Snapshot convention | July 14 delayed intraday Yahoo/Nasdaq quotes ground prices; the Yahoo technical helper, rankings, and regime MAs include the July 14 partial daily bar; completed Nasdaq histories through July 13 ground 30d/60d risk metrics. Asynchronous provider snapshots agree within 1%. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee; preliminary Evolution governance review only (post-close decision deferred). |
| Outstanding blockers | Fundamental/revision, sentiment/positioning, and per-name macro evidence are unavailable, preventing factor breadth. |
| Enhancing limitations (not GO blockers) | Full-universe reference/liquidity, options, short-interest/borrow, and institutional-flow feeds are unavailable. |
| Reflection baseline | `agents/equity/output/gpt-5-2026-06-16` |
| Baseline flag | (none) — the same-model folder is exactly 28 days old, so no exception flag applies. |
| Prediction settlement summary | 17 newly due from gpt-5-2026-06-16: 14 equities and 3 market forecasts. |
| next_due_target_date | 2026-07-15 |
| due_record_count_by_model | `{"gpt-5": 17}` |
| Source Ledger coverage | 107 OBSERVED, 138 DERIVED, 1 INFERRED, 0 ILLUSTRATIVE, 4 UNAVAILABLE. |
| Status eligibility | All five Required inputs pass. Only one family is sourceable, checklist completeness is 14/18 = 77.78%, and Technical is 100% of nonzero conviction; all three evidence gates fail, so no equity is investable. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX. |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED`

The separate 12:15 ET monitor was missed before this invocation; the 15:45 and 16:20 ET checkpoints were not due. No `CLOSE_LOGGED` or completed `EVOLUTION_REVIEW` state is claimed.

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS for published sleeve | Current-run Yahoo helper and Nasdaq quote values agree within 1% for 35 unique published/settled symbols; maximum divergence 0.426474%. | No |
| ~60 trading days history per name and SPY | PASS | 251 completed Nasdaq daily bars for all 20 monitors and SPY/QQQ/SOXX. | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` for all 20 monitors and core ETFs. | No |
| Next earnings date | PASS | 18 current-run Nasdaq/Zacks observations; BAC and GS use official July 14 report dates +91-day cadence, `ESTIMATED (+/-5d)`. | No |
| S&P 500 union Nasdaq-100 universe | PASS | 515-name union; 513 scoreable after SATS/FDXF history exclusions. | No |

Missing Enhancing inputs: options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional flows, and a complete full-universe reference/liquidity panel. They lower DQ and cap confidence/exposure; they are not labeled Required-input failures. The independent three-family, 85% completeness, and max-family-50% evidence gates produce `NO_TRADE`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md through 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PRESENT — missed-checkpoint disclosure; no independent monitor claimed |
| 11_preclose_check.md / 12_close_log.md | PRESENT — not-due placeholders |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PRESENT — Tuesday, not applicable |
| 15_predictions.json | PRESENT — 23 OPEN predictions + 17 settlements |
| 16_monthly_review.md | PRESENT — not month-end |
| eligible_universe.txt / universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT — 516/518 OK |
| nasdaq_verification_manifest.json | PRESENT — 35/35 OK |
| earnings_calendar_manifest.json | PRESENT — top-60 attempt inventory; all 20 published dates grounded |
| history_metrics_manifest.json | PRESENT — 23/23 published/core histories OK |
| settlement_precedence_manifest.json | PRESENT — deterministic canonical settlement selection and duplicate audit |
