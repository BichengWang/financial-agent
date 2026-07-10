# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-10 |
| Model | gpt-5 |
| Run mode | Automation run of `agents/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | `NO_TRADE` because fewer than five names satisfy the three-family and 85% completeness gates. |
| Final status | `NO_TRADE` |
| Retrieved at | 2026-07-10T22:01:15Z |
| Market-session note | Run completed after the July 10 close; Yahoo daily bars were independently cross-checked against Nasdaq closing quotes for every ranked name and core ETF. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Full-universe fundamentals/revisions and sentiment/positioning feeds are unavailable; only technical/price evidence is cross-sectionally scoreable. |
| Reflection baseline | `agents/equity/output/gpt-5-2026-06-11` |
| Baseline flag | `SAME_MODEL_BASELINE` |
| Prediction settlement summary | No new prediction target date matured on 2026-07-10; rolling ledger contains 70 unique equity settlements. |
| Source Ledger coverage | OBSERVED and DERIVED rows present for universe, technicals, two-source prices, histories, estimated earnings, metrics, scores, and targets; non-price factor families are explicitly `UNAVAILABLE`. |
| Status eligibility | Required operational inputs pass for the ranked sleeve, but no name reaches three supportive families or 85% completeness. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX. |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo close plus Nasdaq closing quote agree within 1% for all ranked names and core ETFs. | No |
| ~60 trading days history | PASS | 516/518 helper records are OK; every ranked name and ETF has a separate one-year Yahoo history fetch. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed from fetched daily returns. | No |
| Next earnings date | PASS | Nasdaq/Zacks estimated dates fetched for the ranked sleeve. | No |
| S&P 500 union Nasdaq-100 universe | PASS | build_index_universe.py wrote 515 tickers. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, analyst-revision breadth, institutional ownership flow, and broad fundamental data are unavailable. Those gaps lower DQ and confidence; the separate three-family evidence threshold is what leaves the investable set empty.

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
