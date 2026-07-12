# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-12 |
| Model | gpt-5 |
| Run mode | Automation run of `agents/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | `NO_TRADE` because no name satisfies three supportive families and 85% completeness. |
| Final status | `NO_TRADE` |
| Retrieved at | 2026-07-12T13:19:04Z |
| Precheck timing | Universe and technical support files were materialized at 12:52Z as raw PRECHECK inputs. Two-source settlement grounding completed at 13:19Z; REFLECTION then closed before any factor score, rank, or portfolio decision was published. State transitions record gate acceptance, not support-file write time. |
| Market-session note | Sunday run using Friday 2026-07-10 closes; Yahoo values were independently cross-checked against Nasdaq for every published name, core ETF, and newly settled name. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Current cross-sectional fundamental/revision, sentiment/positioning, and per-name macro exposure feeds are unavailable. |
| Reflection baseline | `agents/equity/output/gpt-5-2026-06-14` |
| Baseline flag | `NONE` — valid same-model folder exactly at the 28-day target; no exception flag applies. |
| Prediction settlement summary | 20 newly due: 17 equities and 3 market forecasts; rolling canonical set now 46 equities and 3 market forecasts. |
| Source Ledger coverage | 89 OBSERVED, 109 DERIVED, 3 INFERRED, 3 UNAVAILABLE. |
| Status eligibility | Required operational inputs pass for the monitoring sleeve, but factor breadth and 78% completeness fail investability. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX. |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

Raw fetches may occur during `PRECHECK`; neither `DATA_OK` nor `TECHNICALS_OK` was accepted, and no candidate scoring was performed, until the grounded Reflection package was complete.

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Current-run Yahoo and Nasdaq fetches agree within 1% for all 20 monitors, three core ETFs, and 17 newly settled equities; retrieval timestamps are in `01`. | No |
| ~60 trading days history | PASS | 516/518 canonical helper records are OK; published records have 352-1,255 daily bars, exceeding the 60-bar minimum. | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` from current-run daily histories. | No |
| Next earnings date | PASS | One-day-old Nasdaq/Zacks schedule observations for 19 monitors are retained after a disclosed current-run DNS retry failure; DAL uses official July 10 report plus 91-day cadence, `ESTIMATED (+/-5d)`. | No |
| S&P 500 union Nasdaq-100 universe | PASS | `build_index_universe.py` wrote 515 tickers; 513 are scoreable. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision breadth, institutional ownership flow, and broad fundamental data are unavailable. These lower DQ and confidence; the independent three-family evidence rule is the binding reason for `NO_TRADE`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md through 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PRESENT - not applicable Sunday |
| 15_predictions.json | PRESENT - 20 equity + 3 market records; 20 new settlements |
| 16_monthly_review.md | PRESENT - not month-end |
| eligible_universe.txt | PRESENT |
| universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT - 516/518 OK |
