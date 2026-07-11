# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-11 |
| Model | gpt-5 |
| Run mode | Automation run of `agents/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | `NO_TRADE` because no name satisfies three supportive families and 85% completeness. |
| Final status | `NO_TRADE` |
| Retrieved at | 2026-07-11T18:00:02Z |
| Market-session note | Saturday run using Friday 2026-07-10 closes; Yahoo values were independently cross-checked against Nasdaq for every published name and core ETF. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Current cross-sectional fundamental/revision, sentiment/positioning, and per-name macro exposure feeds are unavailable. |
| Reflection baseline | `agents/equity/output/gpt-5-2026-06-14` |
| Baseline flag | `SAME_MODEL_BASELINE` |
| Prediction settlement summary | 0 newly due; 29 unique equity settlements after deduplicating 70 repeated stored rows; 0 market settlements. |
| Source Ledger coverage | 67 OBSERVED, 88 DERIVED, 3 UNAVAILABLE. |
| Status eligibility | Required operational inputs pass for the monitoring sleeve, but factor breadth and 78% completeness fail investability. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX. |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo and Nasdaq agree within 1% for all 20 monitors and three core ETFs; current-run retrieval timestamps are in `01`. | No |
| ~60 trading days history | PASS | 516/518 canonical helper records are OK; each published record has 251 separately fetched one-year bars. | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` from current-run daily returns. | No |
| Next earnings date | PASS | Nasdaq/Zacks date for 19 monitors; DAL uses official July 10 report plus 91-day cadence, `ESTIMATED (+/-5d)`. | No |
| S&P 500 union Nasdaq-100 universe | PASS | `build_index_universe.py` wrote 515 tickers; 513 are scoreable. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision breadth, institutional ownership flow, and broad fundamental data are unavailable. These lower DQ and confidence; the independent three-family evidence rule is the binding reason for `NO_TRADE`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md through 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PRESENT - not applicable Saturday |
| 15_predictions.json | PRESENT - 20 equity + 3 market records |
| 16_monthly_review.md | PRESENT - not month-end |
| eligible_universe.txt | PRESENT |
| universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT - 516/518 OK |
| history_prefetch_summary.json | PRESENT - 56/56 quote checks pass |
