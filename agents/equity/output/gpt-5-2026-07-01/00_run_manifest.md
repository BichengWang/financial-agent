# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-01 |
| Model | gpt-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | GO if delayed-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | NO_TRADE |
| Retrieved at | 2026-07-01T23:41:43Z |
| Market-session note | Wednesday run using Yahoo daily history and Nasdaq quote observations dated 2026-07-01. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Missing true fundamental/revision/positioning feeds; fewer than five investable names pass data-completeness gate |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-07` |
| Baseline flag | SAME_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; scanned 18 prior ledgers. |
| Source Ledger coverage | OBSERVED 49; DERIVED 65; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 0 for ranked records |
| Status eligibility | Required price/history/sigma/universe inputs grounded; final status downgraded by investability quality gate |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Ranked entries cross-checked between Yahoo history and Nasdaq quote endpoint within 1% where used. | No |
| ~60 trading days history | PASS | 514 equities plus SPY/QQQ/SOXX have >=60 daily rows. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched daily returns. | No |
| Next earnings date | PASS | Nasdaq/Zacks earnings endpoint used for ranked names; estimated dates flagged. | No |
| S&P 500 union Nasdaq-100 universe | PASS | `build_index_universe.py` wrote 515 tickers. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision feed, institutional ownership flow, and a full fundamental feed are unavailable. Enhancing gaps cap confidence; missing fundamental/revision evidence drives the `NO_TRADE` quality decision.

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
| 15_predictions.json | PRESENT |
| 16_monthly_review.md | PLACEHOLDER |
| eligible_universe.txt | PRESENT |
| universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT |
