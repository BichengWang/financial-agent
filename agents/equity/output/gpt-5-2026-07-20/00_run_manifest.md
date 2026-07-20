# 00 Run Manifest — 2026-07-20

| Field | Value |
|---|---|
| Run date / model | 2026-07-20 Monday / gpt-5; manual catch-up begun 12:27 ET after inactive 07:27 scheduler; 12:15 midpoint included |
| Run mode | Full pipeline from `agents/equity/daily_investment_system/main.md` |
| Data mode | **DELAYED** — completed 2026-07-17 closes; 518 provisional 07-20 bars removed before compute |
| Status target | GO only if every evidence and portfolio gate passes |
| Final status | **NO_TRADE** — zero equities pass three-of-four family coverage |
| Agents executed | Orchestrator → Reflection → Data/Regime → Technical → Factor → Portfolio §0 exit → Risk → Midday → Evolution |
| State machine | PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(§0 exit) → RISK_REVIEW → PUBLISHED → MIDDAY_MONITOR → EVOLUTION_REVIEW |
| Reflection baseline | `agents/equity/output/gpt-5-2026-06-22` — exact 28-day same-model match; exception flags `NO_PRIOR_BASELINE=false`, `CROSS_MODEL_BASELINE=false`, `BASELINE_WINDOW_GAP=false`, `NO_VALID_MOM_BASELINE=false` |
| Settlement | **68 settled; due 0; conflicts 0** — 51 WEEKEND_TARGET + 17 TARGET_EQ_RUN_DATE; canonical 175 EQ / 30 MF |
| New forecasts | 23 EQUITY_ALPHA monitors + 3 MARKET_FORECAST; target 2026-08-17 |
| Outstanding blocker | Fund/Sent production feeds remain SHADOW/unpromoted below the 70%-universe sourceability bar |

## Source Ledger coverage

251 rows: OBSERVED=65, DERIVED=184, INFERRED=1, ILLUSTRATIVE=0, UNAVAILABLE=1. All Required inputs are grounded, so the data layer is GO-eligible; NO_TRADE comes from the evidence gate.

## GO-Gate Table

| Required input | Status | Evidence |
|---|---|---|
| Grounded entry prices | PASS | Yahoo + Nasdaq; 36 comparisons within 1%, 0 failures (L006) |
| ~60d histories + SPY | PASS | current-run 5y fetch, provisional bars filtered; 513/513 eligible (L002) |
| Sigma fallback | PASS | REALIZED_VOL_30D for every published equity/ETF |
| Next earnings date | PASS | confirmed or cadence-estimated for scored shortlist; buffers applied |
| Index-union universe | PASS | 515 materialized; 513 eligible (L001) |

Missing Enhancing inputs: options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional flow, and production Fundamental/Sentiment feeds. Treatment is DQ 0.80, LOW confidence, and a hypothetical 50% gross cap; none is mislabeled a Required-input blocker.

## Artifact checklist

Present: 00–09, 10 midday, 11/12 timing stubs, 13, 14 weekly stub, 15_predictions.json, 16 monthly stub, eligible_universe.txt, universe_summary.json, technical_indicators.json, settlement_manifest.json, price_history_fetch_manifest.json, settlement_price_verification_manifest.json, price_verification_manifest.json, earnings_calendar_manifest.json, run_computed_manifest.json. The ETF block and SPY/QQQ/SOXX prediction records are complete. Files 11/12/14/16 are explicit timing stubs.
