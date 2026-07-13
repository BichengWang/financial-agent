# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-13 |
| Model | gpt-5 |
| Run mode | Automation run of `agents/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | `NO_TRADE` because no name satisfies three supportive families and 85% completeness. |
| Final status | `NO_TRADE` |
| Retrieved at | Yahoo histories 2026-07-13T12:33:44Z; Nasdaq close checks 2026-07-13T12:37:56Z-12:38:07Z; earnings checks 2026-07-13T12:38:40Z-12:38:45Z. |
| Precheck timing | Universe and technical files were materialized as raw PRECHECK inputs. Two-source grounding and the 20-record due inventory then completed before REFLECTION closed and before factor scoring. |
| Market-session note | Monday pre-open run using the latest completed regular-session close, Friday 2026-07-10. Nasdaq `Previous Close` independently matched every published and settled Yahoo value. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Current cross-sectional fundamental/revision, sentiment/positioning, and per-name macro feeds are unavailable; full-universe market-cap, ADV, spread, halt/session-completeness, and corporate-action filter feeds are also unavailable. |
| Reflection baseline | `agents/equity/output/gpt-5-2026-06-15` |
| Baseline flag | `NONE` - valid same-model folder exactly at the 28-day target. |
| Prediction settlement summary | 20 newly due from gpt-5-2026-06-15: 17 equities and 3 market forecasts. Normalized rolling set: 63 equities and 6 market forecasts. |
| Source Ledger coverage | 89 OBSERVED, 111 DERIVED, 3 INFERRED, 4 UNAVAILABLE. |
| Status eligibility | Required operational inputs pass for the monitoring sleeve, but factor breadth, 78% completeness, and incomplete full-universe reference/liquidity filters fail investability. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX. |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED -> EVOLUTION_REVIEW`

The 12:15, 15:45, and 16:20 ET checkpoints were not due during this pre-open run; their placeholder artifacts do not claim those states occurred.

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS for published sleeve | Current-run Yahoo history plus Nasdaq `Previous Close` agree within 1% for 38 unique published/settled symbols; maximum divergence 0.000009%. | No |
| ~60 trading days history per name and SPY | PASS | Canonical 5-year Yahoo histories; 516/518 helper records OK. | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` for every ranked equity and core ETF. | No |
| Next earnings date | PASS | Nineteen current-run Nasdaq/Zacks observations; DAL uses official July 10 report date +91d, `ESTIMATED (+/-5d)`. | No |
| S&P 500 union Nasdaq-100 universe | PASS | 515-name union; 513 scoreable after SATS/FDXF history exclusions. | No |

Missing Enhancing inputs: options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional flows, and a complete full-universe reference/liquidity panel. They cap confidence and exposure; they are not labeled Required-input failures. The independent three-family and 85% evidence thresholds produce `NO_TRADE`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md through 09_final_report.md | PRESENT |
| 10_midday_monitor.md, 11_preclose_check.md, 12_close_log.md | PRESENT - not-due placeholders |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PRESENT - Monday, not applicable |
| 15_predictions.json | PRESENT - 23 OPEN predictions + 20 settlements |
| 16_monthly_review.md | PRESENT - not month-end |
| eligible_universe.txt / universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT - 516/518 OK |
| nasdaq_verification_manifest.json | PRESENT - 38/38 OK |
| earnings_calendar_manifest.json | PRESENT - 19/19 OK; DAL cadence fallback disclosed |
