# 00 Run Manifest — 2026-07-22

- Model: `gpt-5`
- Run mode: full manual daily pipeline
- Data mode: **DELAYED**
- Status target: evaluate `GO` without relaxing gates
- Final status: **NO_TRADE**
- Regime: **NEUTRAL** (high-volatility semiconductor watch)
- Completed price date: **2026-07-22**
- Reflection baseline: `agents/equity/output/gpt-5-2026-06-24`; flag `NONE` — valid same-model baseline inside the 21–45 day window
- Prediction settlement: 0 newly settled; canonical totals 175 EQUITY_ALPHA + 30 MARKET_FORECAST; due=17; conflicts=0 (L328)
- Pending target-close evidence: 17 verified candidates retained for next-run admission under HUMAN_REVIEW governance (L327)
- Source Ledger: 332 contiguous rows; OBSERVED=140, DERIVED=149, INFERRED=42, ILLUSTRATIVE=0, UNAVAILABLE=1
- Agents executed: Orchestrator, Reflection, Data/Regime, Factor Scoring, Portfolio Feasibility, Risk Committee, Evolution

## State transitions

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT(NO_TRADE) -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required input | Result | Evidence |
|---|---|---|
| Grounded entry price | PASS | 29/29 current forecast prices passed Yahoo/Nasdaq <=1% gate (L006) |
| ~60 trading days fetched history | PASS | 514/515 equity names plus core ETFs; SATS→ECHO source remap applied and FDXF excluded before ranking (L002) |
| Sigma fallback | PASS | REALIZED_VOL_30D for every published record |
| Next earnings date | PASS | 109/109 refreshed; 78 confirmed, 31 cadence-estimated, 0 unavailable |
| Index-union universe | PASS | 515 names (L001) |

Enhancing inputs unavailable: production Fundamental/Sentiment families, options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, ownership flow. These cap confidence/gross exposure but are not GO blockers. **NO_TRADE is instead forced by the independent 3-of-4-family and max-family-contribution evidence gates.**

## Outstanding blockers

Fund_Z and Sent_Z remain unpromoted and unavailable. Every equity has at most two supportive families; no name satisfies the required three, and Technical necessarily exceeds the 50% conviction cap when the two absent families contribute zero.

## Artifact checklist

- [x] `00_run_manifest.md`
- [x] `01_preflight.md`
- [x] `02_reflection.md`
- [x] `03_regime_and_data.md`
- [x] `04_universe_summary.md`
- [x] `05_factor_scores.md`
- [x] `06_top_candidates.md`
- [x] `07_portfolio_proposal.md`
- [x] `08_risk_review.md`
- [x] `09_final_report.md`
- [x] `10_midday_monitor.md`
- [x] `11_preclose_check.md`
- [x] `12_close_log.md`
- [x] `13_evolution_log.md`
- [x] `14_weekly_review.md`
- [x] `15_predictions.json`
- [x] `16_monthly_review.md`
- [x] `eligible_universe.txt`
- [x] `universe_summary.json`
- [x] `technical_indicators.json`
- [x] `settlement_manifest.json`
- [x] `pending_target_close_candidates.json`

Core ETF Market Forecast Block: present for SPY/QQQ/SOXX in `03`, `09`, and `15`.
