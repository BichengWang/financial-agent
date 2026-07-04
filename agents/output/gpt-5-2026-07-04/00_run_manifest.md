# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-04 |
| Model | gpt-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED_PARTIAL |
| Status target | REVIEW_ONLY because U.S. equity markets are closed for the Saturday Independence Day holiday weekend |
| Final status | REVIEW_ONLY |
| Retrieved at | 2026-07-04T18:12:58Z |
| Market-session note | Saturday run; NYSE/Nasdaq observed Independence Day on 2026-07-03 and no regular session exists on 2026-07-04. Freshest regular-session bars are dated 2026-07-02. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | No July 4 regular-session entry tape; fundamental/revision/positioning feeds and refreshed earnings dates unavailable. |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-07` |
| Baseline flag | SAME_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; scanned 24 prior ledgers. |
| Source Ledger coverage | OBSERVED 25; DERIVED 24; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 4 |
| Status eligibility | Universe, history, sigma, and price lineage are grounded on delayed July 2 data; weekend/holiday and earnings refresh gaps make the package review-only. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS FOR REVIEW | Yahoo chart endpoint fetched during this run for ranked names and ETFs; observation date 2026-07-02. | No for review-only; no live entry session today |
| ~60 trading days history | PASS | 517 of 518 requested technical records are OK; every ranked name and ETF has >=60 Yahoo daily rows. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched Yahoo daily returns. | No |
| Next earnings date | FAIL FOR GO | Earnings-calendar feed was not refreshed during this weekend/holiday review package. | Yes |
| S&P 500 union Nasdaq-100 universe | PASS | build_index_universe.py wrote 515 tickers. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape beyond displayed quote snapshots, analyst-revision feed, institutional ownership flow, and a broad fundamental feed are unavailable. These are confidence and data-quality caps, not standalone GO blockers; the missing refreshed earnings date and closed-market tape block GO.

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
| 10_midday_monitor.md | PLACEHOLDER |
| 11_preclose_check.md | PLACEHOLDER |
| 12_close_log.md | PLACEHOLDER |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PLACEHOLDER |
| 15_predictions.json | PRESENT |
| 16_monthly_review.md | PLACEHOLDER |
| eligible_universe.txt | PRESENT |
| universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT |
