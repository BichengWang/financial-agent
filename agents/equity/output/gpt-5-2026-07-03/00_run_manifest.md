# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-03 |
| Model | gpt-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED_PARTIAL |
| Status target | REVIEW_ONLY because Nasdaq/NYSE are closed for Independence Day observed |
| Final status | REVIEW_ONLY |
| Retrieved at | 2026-07-03T13:13:33Z |
| Market-session note | Friday holiday run; U.S. equity markets closed on 2026-07-03 and freshest regular-session bars are dated 2026-07-02. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | No July 3 regular-session entry tape; fundamental/revision/positioning feeds and refreshed earnings dates unavailable. |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-07` |
| Baseline flag | SAME_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; scanned 22 prior ledgers. |
| Source Ledger coverage | OBSERVED 19; DERIVED 18; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 4 |
| Status eligibility | Universe, history, sigma, and price lineage are grounded on delayed July 2 data; holiday/no earnings refresh makes the package review-only. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo regular-session bars and OpenAI finance snapshots agree within 1% for ranked names and ETFs; observation date 2026-07-02. | No |
| ~60 trading days history | PASS | 517 of 518 requested technical records are OK; every ranked name and ETF has >=60 Yahoo daily rows. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched Yahoo daily returns. | No |
| Next earnings date | FAIL FOR GO | Earnings-calendar feed was not refreshed during this holiday review package. | Yes |
| S&P 500 union Nasdaq-100 universe | PASS | build_index_universe.py wrote 515 tickers. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape beyond the displayed quote snapshot, analyst-revision feed, institutional ownership flow, and a broad fundamental feed are unavailable. These are confidence and data-quality caps, not standalone GO blockers; the missing refreshed earnings date is the Required-input blocker for GO.

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
