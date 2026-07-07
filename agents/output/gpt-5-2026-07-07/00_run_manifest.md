# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-07 |
| Model | gpt-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED_PARTIAL |
| Status target | REVIEW_ONLY because refreshed earnings/fundamental/revision/positioning feeds remain unavailable even though delayed price/history data was fetched. |
| Final status | REVIEW_ONLY |
| Retrieved at | 2026-07-07T16:01:30Z |
| Market-session note | Tuesday regular-session delayed bars were available from Yahoo chart endpoints during the run; no live brokerage feed or earnings feed was wired. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Refreshed earnings dates, fundamental/revision feeds, options/short-interest/borrow, bid-ask tape, and institutional-flow feeds unavailable. |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-09` |
| Baseline flag | SAME_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; scanned prior ledgers and found no OPEN prediction with target_date <= 2026-07-07. |
| Source Ledger coverage | OBSERVED 26; DERIVED 24; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 4 |
| Status eligibility | Universe, price, history, sigma, and technical lineage are grounded; missing earnings and non-price factor feeds keep all names in monitoring only. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo chart prefetch and technical helper rows for ranked names and ETFs; observation date 2026-07-07. | No |
| ~60 trading days history | PASS | 517 of 518 requested history records are OK; every ranked name and ETF has >=60 daily rows. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched Yahoo daily returns. | No |
| Next earnings date | FAIL FOR GO | No connected earnings-calendar feed was available during this run. | Yes |
| S&P 500 union Nasdaq-100 universe | PASS | build_index_universe.py wrote 515 tickers. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision feed, institutional ownership flow, and a broad fundamental feed are unavailable. These are confidence and data-quality caps; the missing earnings-date feed is the GO blocker.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | PRESENT |
| 01_preflight.md | PRESENT |
| 02_reflection.md | PRESENT |
| 03_regime_and_data.md | PRESENT |
| 04_universe_summary.md | PRESENT |
| 05_factor_scores.md | PRESENT |
| 06_top_candidates.md | PRESENT |
| 07_portfolio_proposal.md | PRESENT |
| 08_risk_review.md | PRESENT |
| 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PRESENT |
| 11_preclose_check.md | PRESENT |
| 12_close_log.md | PRESENT |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PRESENT |
| 15_predictions.json | PRESENT |
| 16_monthly_review.md | PRESENT |
| eligible_universe.txt | PRESENT |
| universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT |
| history_prefetch_summary.json | PRESENT |
