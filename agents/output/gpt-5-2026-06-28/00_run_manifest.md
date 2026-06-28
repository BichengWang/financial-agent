# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-06-28 |
| Model | gpt-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | GO if delayed-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | NO_TRADE |
| Retrieved at | 2026-06-28T19:41:29Z |
| Market-session note | Sunday run; latest regular-session Yahoo chart bars are dated 2026-06-26. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Portfolio beta feasibility under protected 5% single-name cap |
| Reflection baseline | `investments/equity/output/gpt-5-2026-05-29` |
| Baseline flag | SAME_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; No prior OPEN prediction had target_date <= 2026-06-28; scanned 13 prior ledgers. |
| Source Ledger coverage | OBSERVED 74; DERIVED 179; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 0 |
| Status eligibility | Required inputs grounded on delayed public data; portfolio construction downgraded to NO_TRADE |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Yahoo regular-session close cross-checked with Nasdaq quote value within 1% for every sampled ticker and ETF; quote date 2026-06-26. | No |
| ~60 trading days history | PASS | Minimum fetched bars across universe: 1255; histories include the 2026-06-26 regular-session bar. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed for every ETF and equity from fetched daily returns. | No |
| Next earnings date | PASS | Nasdaq prior report + 91d cadence estimate available for all sampled equities. | No |
| Sampled universe | PASS | 34 equities across 11 GICS sectors with grounded prices and liquidity. | No |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, and institutional-flow data are unavailable. They cap confidence and gross exposure but do not block `GO`.

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
| technical_indicators.json | PRESENT |
