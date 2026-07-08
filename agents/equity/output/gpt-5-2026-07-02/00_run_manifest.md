# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-02 |
| Model | gpt-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | GO if delayed-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | NO_TRADE |
| Retrieved at | 2026-07-02T16:15:11Z |
| Market-session note | Thursday run using Nasdaq quote observations dated 2026-07-02 and Yahoo daily history through 2026-07-02. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | True fundamental/revision/positioning feeds are unavailable; no ranked name reaches the >=85% data-completeness investable threshold. |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-07` |
| Baseline flag | SAME_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; scanned 20 prior ledgers. |
| Source Ledger coverage | OBSERVED 39; DERIVED 78; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 2 for ranked records and core ETFs |
| Status eligibility | Required price/history/sigma/universe inputs grounded; final status downgraded by investability quality gate |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Ranked entries use Nasdaq quote endpoint observations retrieved this run; Yahoo daily history divergence is disclosed separately. | No |
| ~60 trading days history | PASS | 514 equities plus SPY/QQQ/SOXX have usable technical history; ranked names have >=60 Yahoo daily rows. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched Yahoo daily returns. | No |
| Next earnings date | PASS | Nasdaq/Zacks earnings endpoint used where available; cadence estimates from earnings-surprise history are flagged. | No |
| S&P 500 union Nasdaq-100 universe | PASS | `build_index_universe.py` wrote 515 tickers. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape beyond displayed quote, analyst-revision feed, institutional ownership flow, and a full fundamental feed are unavailable. These are not GO blockers by themselves, but the unavailable fundamental/revision/positioning families keep data completeness below the investable threshold.

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
