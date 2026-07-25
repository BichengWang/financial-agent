# 00 Run Manifest — 2026-07-24

- Model: `gpt-5`
- Run mode: full manual daily pipeline
- Data mode: **DELAYED**
- Status target: evaluate `GO` without relaxing gates
- Final status: **NO_TRADE**
- Regime: **NEUTRAL** (high-volatility semiconductor watch)
- Completed price date: **2026-07-24**
- Reflection baseline: `agents/equity/output/gpt-5-2026-06-24`; flag `NONE` — valid same-model baseline inside the 21–45 day window; earlier-date tie-break at equal distance from 2026-06-26
- Prediction settlement: 0 newly settled; canonical totals 189 EQUITY_ALPHA + 33 MARKET_FORECAST; due=0; conflicts=0 (L332)
- Source Ledger: 336 contiguous rows; OBSERVED=141, DERIVED=152, INFERRED=42, ILLUSTRATIVE=0, UNAVAILABLE=1
- Agents executed: Orchestrator, Reflection, Data/Regime, Factor Scoring, Portfolio Feasibility, Risk Committee, Evolution

## State transitions

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT(NO_TRADE) -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required input | Result | Evidence |
|---|---|---|
| Grounded entry price | PASS | 29/29 current forecast prices passed Yahoo/Nasdaq <=1% gate (L007) |
| ~60 trading days fetched history | PASS | 514/515 equities had >=60 completed bars; FDXF was excluded and all 511 scored names passed (L002,L003) |
| Sigma fallback | PASS | REALIZED_VOL_30D for every published record |
| Next earnings date | PASS | 511/511 scored names populated after 514 attempts: 380 confirmed, 131 cadence-estimated, 3 unavailable names excluded before scoring (L008) |
| Index-union universe | PASS | 515 names (L001) |

Universe inclusion filters also passed: 515/515 names exceeded $2B market cap, and every scored name exceeded $5 price and $20M 20-day dollar volume (L004,L009).

Enhancing inputs unavailable: production Fundamental/Sentiment families, options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, ownership flow. These cap confidence/gross exposure but are not GO blockers. **NO_TRADE is forced by the 3-of-4-family evidence gate.** Event-window flags are secondary monitoring constraints, not an independent no-trade cause.

## Outstanding blockers

Fund_Z and Sent_Z remain unpromoted and unavailable. Every equity has at most two countable families, so no name can satisfy the required three-family convergence; any available conviction is necessarily concentrated in Technical/Macro evidence.

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
- [x] `price_history_fetch_manifest.json`
- [x] `price_verification_manifest.json`
- [x] `baseline_price_verification_manifest.json`
- [x] `earnings_calendar_manifest.json`
- [x] `market_cap_eligibility_manifest.json`
- [x] `run_computed_manifest.json`

Core ETF Market Forecast Block: present for SPY/QQQ/SOXX in `03`, `09`, and `15`.

## Validation

- Artifact validator: **PASS** — 27 files, contiguous `L001`–`L336`, 26 equity forecasts, 3 market forecasts, and all eligibility/current/baseline price gates consistent.
- Workflow tests: **77 passed** with `python3 -m pytest agents/equity/daily_investment_system/tests -q`.
- Canonical `uv run pytest ...` was attempted but remains blocked by the pinned `pandas==1.5.3` legacy build requiring undeclared `pkg_resources`; dependency pins were not changed.
