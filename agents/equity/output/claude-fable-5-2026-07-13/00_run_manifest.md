# 00 Run Manifest — 2026-07-13

| Field | Value |
|---|---|
| Run date / model | 2026-07-13 (Monday pre-open, 08:0x ET) / claude-fable-5 |
| Run mode | Scheduled daily pre-open full pipeline |
| Data mode | **DELAYED** (2026-07-10 Friday close; fetched this run; zero UNAVAILABLE Required fields) |
| Status target | GO if live-data constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** — family-coverage evidence threshold #2 (2/4 sourceable families → investable set empty; 11th consecutive scoring run); recorded contemporaneously in 15_predictions.json |
| Agents executed | Orchestrator → Reflection → Data/Regime → technical_indicators.py → Factor Scoring → Portfolio §0 pre-check (NO_TRADE, no sizing) → Risk Committee (APPROVE) → Evolution |
| State machine | PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(§0 exit) → RISK_REVIEW → PUBLISHED → EVOLUTION_REVIEW |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-06-10` — **SAME_MODEL_BASELINE**, in-window (target 06-15, 5d off), no gap flag |
| Prediction settlement | **20 settled** (gpt-5 2026-06-15 vintage: 17 EQ 11H/6M; 3 MF — SPY HIT, QQQ/SOXX MISS, all IN_CI); TARGET_EQ_RUN_DATE convention (settled at 07-10 close, pre-open run); rolling deduped base n=121 EQ + 9 MF |
| Outstanding blockers | Fund/Sent families unwired (standing HUMAN_REVIEW, 11th run) — the structural GO blocker |

## Source Ledger Coverage (01; 223 rows)

| claim_type | rows |
|---|---|
| OBSERVED | 57 |
| DERIVED | 162 |
| INFERRED | 4 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE (fields recorded as such) | Fund_Z/Sent_Z universe-wide; Sortino; FDXF pack; isolated monthly-alignment gaps |

Status eligibility: DELAYED data with all Required inputs grounded → GO-eligible on data; NO_TRADE on evidence-threshold construction.

## GO-Gate Table (Required inputs only may block)

| Required input | Status | Evidence |
|---|---|---|
| 1. Grounded entry prices | **GROUNDED** | Nasdaq hist API bulk + IBKR MCP verification: 12/12 exact priorClose matches, 15 corroborated premkt (L002, L016) |
| 2. ~60d price history (names + SPY) | **GROUNDED** | 1254 daily bars/name, 5y, 514/514 eligible (L002) |
| 3. Sigma via fallback chain | **GROUNDED** | REALIZED_VOL_30D computed for all 27 published symbols (step 2 of chain; no options feed wired) |
| 4. Next earnings date | **GROUNDED** | 66-symbol confirmed-dates fetch (65 confirmed; DAL cadence-est ±5d outside horizon) (L015) |
| 5. Index-union universe | **GROUNDED** | build_index_universe.py: 515 union, 514 eligible (L001) |

Missing **Enhancing** inputs (caps, never blockers): options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow, fundamentals/sentiment feeds → DQ 0.80, confidence cap LOW, gross-exposure cap 50% (academic — NO_TRADE).

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00–09, 13 | Published |
| 10/11/12 (midday/preclose/close) | Stubs — manual checkpoints, not yet reached at pre-open publication |
| 14 weekly review | Stub — not a Friday |
| 15_predictions.json | **Published**: 24 EQUITY_ALPHA (all with score_explainability + benchmark_price 754.95) + 3 MARKET_FORECAST + 20 settlements — publishing gate satisfied |
| 16 monthly review | Stub — not month-end |
| eligible_universe.txt / universe_summary.json | Published (515 union / 514 eligible) |
| technical_indicators.json | Published (517/518 OK; FDXF UNAVAILABLE) |
| earnings_calendar_manifest.json | Published (66 symbols, confirmed-dates preflight) |
| nasdaq_verification_manifest.json | Published (IBKR cross-check, 27 symbols) |
| price_history_fetch_manifest.json | Published (Nasdaq bulk fetch record; Yahoo 429 outage documented) |
| Core ETF Market Forecast Block | Present (03; SPY/QQQ/SOXX records in 15) |
