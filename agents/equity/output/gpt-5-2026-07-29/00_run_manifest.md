# 00 Run Manifest — 2026-07-29

| Field | Value |
|---|---|
| Model | `gpt-5` |
| Run time | 09:50 ET, post-open revalidation on a prior-close basis |
| Data mode | `DELAYED` |
| Price basis | Official completed close for 2026-07-28; July 29 intraday prints ignored |
| Status target | Quality-gated |
| Final status | **NO_TRADE** |
| Regime | **NEUTRAL**, with same-day FOMC and high-vol semiconductor watch |
| Reflection baseline | `agents/equity/output/gpt-5-2026-07-01`; `SAME_MODEL_BASELINE`; exception `NONE` |
| Prediction settlement | 0 new in this package; upstream same-day run already canonicalized 44; canonical totals 298 + 54; due 0; conflicts 0 |
| Rolling evidence | EQ n=298, eff_n=1; MF n=54, eff_n=1 |
| Source Ledger | L001–L069 contiguous; OBSERVED 15, DERIVED 50, INFERRED 1, ILLUSTRATIVE 0, UNAVAILABLE 3 |
| Agents executed | Orchestrator, Reflection, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee |

Final status: **NO_TRADE**.

The prediction ledger contains **20 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` records and 0 settlements**. `NO_PREDICTION_LEDGER` marks the empty current-run settlement block; the prior canonical ledger remains available.

## Source Ledger claim counts

| Claim type | Rows |
|---|---|
| OBSERVED | 15 |
| DERIVED | 50 |
| INFERRED | 1 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE | 3 |
| TOTAL | 69 |

## State transition log

`PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT → RISK_REVIEW → PUBLISHED`

`MIDDAY_MONITOR`, `PRECLOSE_CHECK`, `CLOSE_LOGGED`, and `EVOLUTION_REVIEW` are not yet due at the 09:50 ET cutoff.

## GO-Gate Table

| Required input | State | Evidence |
|---|---|---|
| Grounded entry price | PASS | 20 equities + 3 ETFs have official 2026-07-28 completed-session closes (L002,L004,L006) |
| ~60 trading days history/name + SPY | PASS | 517/518 histories are GO-grade; FDXF has 43 bars and is excluded (L003,L044) |
| Sigma fallback | PASS | All 23 forecasts use REALIZED_VOL_30D (L011) |
| Next earnings date | PASS for published sleeve | 20/20 published names have exact same-day grounded dates (19 current-run event-calendar + 1 same-day merged forward-calendar); 0/20 unresolved; 1 inside 14d (L019,L068) |
| Index-union universe | PASS | 503 + 101 - 89 = 515 (L001) |

Enhancing inputs unavailable: production-scale fundamental revisions/quality, sentiment/positioning, options IV/skew, short-interest change, bid-ask tape, analyst revisions, and ownership flow. They reduce DQ/confidence but are not mislabeled as Required-input blockers. Required completeness is 100% and the earnings-event count passes. The binding `NO_TRADE` conditions are the 3-of-4 factor-family rule, max-family-conviction rule, beta band, sector cap, and 8% drawdown cap.

## Publication decision

The index union produced 514 sourceable equities and 504 scored equities after FDXF plus ten binding reflection `DROP` exclusions. Twenty names have complete settleable monitoring forecasts, but zero are investable because only Technical and Macro are production-sourceable and one family exceeds 50% of available conviction. The equal-weight monitoring diagnostic has beta -0.386, drawdown95 8.25%, and maximum sector weight 35%, so it independently fails portfolio controls.

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
- [x] `entry_price_manifest.json`
- [x] `settlement_price_manifest.json`
- [x] `price_history_fetch_manifest.json`
- [x] `price_verification.json`
- [x] `earnings_calendar_manifest.json`
- [x] `earnings_event_lookup.json`
- [x] `market_cap_eligibility_manifest.json`
- [x] `sector_manifest.json`
- [x] `regime_data_manifest.json`
- [x] `regime_external_manifest.json`
- [x] `run_computed_manifest.json`
- [x] `portfolio_diagnostics.json`

Core ETF Market Forecast Block: present for SPY, QQQ, and SOXX in `03_regime_and_data.md` and `15_predictions.json`.
