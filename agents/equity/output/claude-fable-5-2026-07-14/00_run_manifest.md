# 00 Run Manifest — 2026-07-14

| Field | Value |
|---|---|
| Run date / model | 2026-07-14 (Tuesday, intraday 13:0x ET — scheduled fire delayed past the 07:27 pre-open slot; all scored fields are 07-13 closes) / claude-fable-5 |
| Run mode | Scheduled daily full pipeline |
| Data mode | **DELAYED** (2026-07-13 Monday close; fetched this run; zero UNAVAILABLE Required fields) |
| Status target | GO if live-data constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** — family-coverage evidence threshold #2 (2/4 sourceable families → investable set empty; 12th consecutive scoring run); recorded contemporaneously in 15_predictions.json |
| Agents executed | Orchestrator → Reflection → Data/Regime → technical_indicators.py → Factor Scoring → Portfolio §0 pre-check (NO_TRADE, no sizing) → Risk Committee (APPROVE) → Evolution |
| State machine | PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(§0 exit) → RISK_REVIEW → PUBLISHED → EVOLUTION_REVIEW |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-06-10` — **SAME_MODEL_BASELINE**, in-window (window 05-30..06-23, target 06-16, 6d off), no gap flag (L018) |
| Prediction settlement | **17 settled** (gpt-5 2026-06-16 vintage: 14 EQ 8H/6M, 13 IN_CI; 3 MF — SPY/QQQ/SOXX all MISS, QQQ OUT_CI_LOW); TARGET_EQ_RUN_DATE convention (intraday run → settled at 07-13 close; codified into rules.md this run); rolling deduped base n=135 EQ + 12 MF |
| Outstanding blockers | Fund/Sent families unwired (standing HUMAN_REVIEW, 12th run) — the structural GO blocker |

## Source Ledger Coverage (01; 247 rows)

| claim_type | rows |
|---|---|
| OBSERVED | 58 |
| DERIVED | 181 |
| INFERRED | 4 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE (fields recorded as such) | Fund_Z/Sent_Z universe-wide; Treynor; FDXF pack; isolated monthly-MA gaps |

Status eligibility: DELAYED data with all Required inputs grounded → GO-eligible on data; NO_TRADE on evidence-threshold construction.

## GO-Gate Table (Required inputs only may block)

| Required input | Status | Evidence |
|---|---|---|
| 1. Grounded entry prices | **GROUNDED** | Nasdaq hist API bulk + IBKR MCP verification: **13/13 exact priorClose matches to the cent** (L002, L016) |
| 2. ~60d price history (names + SPY) | **GROUNDED** | ~1254 daily bars/name, 5y, 514/514 eligible; source chain: Yahoo(429) → Nasdaq(517) → IBKR(BF-B) (L002, L019) |
| 3. Sigma via fallback chain | **GROUNDED** | REALIZED_VOL_30D computed for all 27 published symbols (chain step 2; no options feed wired) |
| 4. Next earnings date | **GROUNDED** | 63-symbol confirmed-dates fetch: 61 confirmed; FAST cadence-est ±5d (penalized, buffered window); MU vendor-empty outside horizon (L015) |
| 5. Index-union universe | **GROUNDED** | build_index_universe.py: 515 union, 514 eligible (L001) |

Missing **Enhancing** inputs (caps, never blockers): options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow, fundamentals/sentiment feeds → DQ 0.80, confidence cap LOW, gross-exposure cap 50% (academic — NO_TRADE).

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00–09, 13 | Published |
| 10/11/12 (midday/preclose/close) | 10: folded into the intraday run (see file); 11/12: manual checkpoints, stubs |
| 14 weekly review | Stub — not a Friday |
| 15_predictions.json | **Published**: 24 EQUITY_ALPHA (all with score_explainability + benchmark_price 749.17) + 3 MARKET_FORECAST + 17 settlements — publishing gate satisfied |
| 16 monthly review | Stub — not month-end |
| eligible_universe.txt / universe_summary.json | Published (515 union / 514 eligible) |
| technical_indicators.json | Published (517/518 OK; FDXF UNAVAILABLE) |
| earnings_calendar_manifest.json | Published (63 symbols, confirmed-dates preflight) |
| nasdaq_verification_manifest.json | Published (IBKR cross-check, 13/13 exact) |
| price_history_fetch_manifest.json | Published (Nasdaq bulk record; Yahoo 429 outage probe documented) |
| Core ETF Market Forecast Block | Present (03; SPY/QQQ/SOXX records in 15) |
| rules.md §Settlement Rules | **Modified this run** — Track B codification of TARGET_EQ_RUN_DATE / WEEKEND_TARGET (13, HUMAN_REVIEW) |
