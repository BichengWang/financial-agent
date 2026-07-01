# 00 Run Manifest

| Field | Value |
|---|---|
| Date | 2026-06-30 (Tuesday; last trading day of June) |
| Model | claude-opus-4-8 |
| Run mode | Manual full-pipeline run of `investments/equity/daily_investment_system/main.md` |
| Data mode | **LIVE** (IBKR real-time feed wired; 7-name + ETF sleeve grounded by connected tool, universe cross-validated within 0.30%) |
| Retrieved at | 2026-06-30T15:55–16:15Z |
| Status target | GO if a constraint-compliant portfolio exists; else NO_TRADE |
| **Final status** | **NO_TRADE** |
| Agents executed | Orchestrator (+Reflection), Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | (1) Only 4 names clear the full investability gate (< 5 min). (2) Portfolio beta band [0.90,1.10] infeasible — max achievable long-book beta 0.59 << 0.90 under the protected 5% single-name cap. (3) 0 settled predictions in system history → calibration `INSUFFICIENT_SETTLED_N`. |
| Reflection baseline | `investments/equity/output/gemini-3-5-flash-2026-05-30` |
| Baseline flag | **CROSS_MODEL_BASELINE** (no same-model folder; closest in-window cross-model, 3d from 2026-06-02 target, 31d old) |
| Prediction settlement summary | **0 settled** — no prior OPEN prediction had target_date ≤ 2026-06-30; scanned 17 ledgers / 290 records (earliest maturity 2026-07-08). `NO_PREDICTION_LEDGER` matured. |
| Source Ledger coverage | OBSERVED: 7 LIVE prices + 31 validated-feed prices + 2 history series; DERIVED: σ/β/DD/momentum/RS/TE/corr/Sharpe/Sortino/IR/Treynor/Kelly/VaR/CVaR/ADV + all TD9/RSI/MACD/MA states (38 symbols); INFERRED: regime + thesis notes; ILLUSTRATIVE: baseline picks; UNAVAILABLE: options/short/analyst/institutional/full-feed/rf (Enhancing) |
| Status eligibility | All five Required inputs grounded; NO_TRADE rests on protected portfolio-construction constraints, not on data grounding or missing Enhancing inputs |
| Core ETF Market Forecast Block | **Present** for SPY, QQQ, SOXX (03 + 3 MARKET_FORECAST records in 15) |
| Evolution | DEFER → HUMAN_REVIEW + **FREEZE** autonomous parameter mutation (Freeze Criteria #1: ≥3 consecutive NO_CHANGE cycles) |

## State Transition Log

`PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(infeasible) → RISK_REVIEW → PUBLISHED(NO_TRADE) → CLOSE_LOGGED(pending checkpoints) → EVOLUTION_REVIEW`

No HALTED condition (data lineage clean). NO_TRADE reached at PORTFOLIO_DRAFT (constraint infeasibility), confirmed by Risk Committee.

## GO-Gate Table (Required inputs only as blockers)

| Required Input | Status | Evidence | Blocks GO? |
|---|---|---|---|
| Grounded entry price | PASS | 7 names IBKR-LIVE (SPY/QQQ/SOXX/MU/AMD/UNH/LLY); universe same-session Yahoo validated ≤0.30% vs connected tool (01) | No |
| ~60 trading days history | PASS | 1y (analytics) + 5y (technicals) daily bars for all 38 symbols | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computed for every name + ETF (L200) | No |
| Next earnings date | PASS | Cadence-estimated `ESTIMATED (±5d)` for all 35; buffered-window penalty applied | No |
| Sampled universe | PASS | 35 names across 11 GICS sectors, grounded prices + liquidity (04) | No |

**All Required inputs grounded → not a data-driven NO_TRADE.** The NO_TRADE is caused by portfolio-construction infeasibility against protected rules (investable count < 5; beta band vs 5% cap).

## Enhancing Inputs Missing (caps, not blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional flow, full-universe feed, risk-free rate — all `UNAVAILABLE`. Effect: data-quality multiplier held at 0.80, all confidence capped ≤ MEDIUM, ratios `RAW_DIAGNOSTIC`. They do **not** block status.

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00_run_manifest.md | PRESENT |
| 01_preflight.md (Source Ledger) | PRESENT |
| 02_reflection.md | PRESENT |
| 03_regime_and_data.md (Core ETF block) | PRESENT |
| 04_universe_summary.md | PRESENT |
| 05_factor_scores.md | PRESENT |
| 06_top_candidates.md | PRESENT |
| 07_portfolio_proposal.md (NO_TRADE feasibility) | PRESENT |
| 08_risk_review.md | PRESENT |
| 09_final_report.md | PRESENT |
| 13_evolution_log.md | PRESENT |
| 15_predictions.json | PRESENT (15 EQUITY_ALPHA + 3 MARKET_FORECAST; settlements []) |
| 16_monthly_review.md | PRESENT (month-end due) |
| technical_indicators.json | PRESENT (38/38 OK) |
| 10_midday_monitor.md / 11_preclose_check.md / 12_close_log.md | PLACEHOLDER (intraday checkpoints not yet reached; pre-open batch) |
| 14_weekly_review.md | N/A (Friday-only; today is Tuesday) |
