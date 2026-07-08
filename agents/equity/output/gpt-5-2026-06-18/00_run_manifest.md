# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-06-18 |
| Model | gpt-5 |
| Run mode | Manual automation run |
| Data mode | LIVE |
| Status target | GO if portfolio constraints pass |
| Final status | NO_TRADE |
| Retrieved at | 2026-06-18T18:21:21Z |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Portfolio beta feasibility under protected 5% single-name cap |
| Reflection baseline | `investments/equity/output/claude-opus-4-7-2026-05-24` |
| Baseline flag | CROSS_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; No prior OPEN prediction had target_date <= 2026-06-18; scanned 6 prior ledgers. |
| Source Ledger coverage | OBSERVED 76; DERIVED 146; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 0 |
| Status eligibility | Data eligible for GO; portfolio construction downgraded to NO_TRADE |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required Input | Status | Evidence |
| --- | --- | --- |
| Grounded entry price | PASS | CNBC real-time quotes cross-checked against Yahoo chart latest within 1% for every sampled ticker and ETF |
| ~60 trading days history | PASS | Minimum fetched bars across universe: 116 |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed for every ETF and equity from fetched daily returns |
| Next earnings date | PASS | Nasdaq prior report + 91d cadence estimate available for all sampled equities |
| Sampled universe | PASS | 35 equities across 11 GICS sectors with grounded prices and liquidity |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, and institutional-flow data are unavailable. They cap confidence and gross exposure but do not block `GO`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00 | PRESENT |
| 01 | PRESENT |
| 02 | PRESENT |
| 03 | PRESENT |
| 04 | PRESENT |
| 05 | PRESENT |
| 06 | PRESENT |
| 07 | PRESENT |
| 08 | PRESENT |
| 09 | PRESENT |
| 10_midday_monitor.md | PLACEHOLDER |
| 11_preclose_check.md | PLACEHOLDER |
| 12_close_log.md | PLACEHOLDER |
| 13_evolution_log.md | PRESENT |
| 15_predictions.json | PRESENT |
