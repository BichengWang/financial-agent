# 00 Run Manifest — 2026-07-15

| Field | Value |
|---|---|
| Run date / model | 2026-07-15 (Wednesday, intraday ~15:5x ET — scheduled fire ran during RTH; all scored fields are 07-14 closes) / claude-fable-5 |
| Run mode | Scheduled daily full pipeline |
| Data mode | **DELAYED** (2026-07-14 Tuesday close; fetched this run; zero UNAVAILABLE Required fields) |
| Status target | GO if live-data constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** — family-coverage evidence threshold #2 (2/4 sourceable families → investable set empty; 13th consecutive scoring run); recorded contemporaneously in 15_predictions.json |
| Agents executed | Orchestrator → Reflection → Data/Regime → technical_indicators.py → Factor Scoring → Portfolio §0 pre-check (NO_TRADE, no sizing) → Risk Committee (APPROVE) → Evolution |
| State machine | PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(§0 exit) → RISK_REVIEW → PUBLISHED → EVOLUTION_REVIEW |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-06-10` — **SAME_MODEL_BASELINE**, in-window (window 05-31..06-24, target 06-17, folder 7d off — at the limit, not over), no gap flag (L018) |
| Prediction settlement | **17 settled** (gpt-5 2026-06-17 vintage: 14 EQ 9H/5M, **14/14 IN_CI**, mean z −0.013, vintage IC −0.248; 3 MF — SPY HIT, QQQ/SOXX MISS); `TARGET_EQ_RUN_DATE` flag (intraday run → settled at 07-14 close per rules.md §Settlement Rules); **rolling base corrected to strict prediction identity: 91 EQ + 12 MF distinct** (was reported 135 EQ — Track B in 13) |
| Outstanding blockers | Fund/Sent families unwired (standing HUMAN_REVIEW, 13th run) — the structural GO blocker |

## Source Ledger Coverage (01; 220 rows)

| claim_type | rows |
|---|---|
| OBSERVED | 57 |
| DERIVED | 158 |
| INFERRED | 5 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE (fields recorded as such) | Fund_Z/Sent_Z universe-wide; Treynor; FDXF pack; isolated monthly-MA gaps outside the published 24 |

Status eligibility: DELAYED data with all Required inputs grounded → GO-eligible on data; NO_TRADE on evidence-threshold construction.

## GO-Gate Table (Required inputs only may block)

| Required input | Status | Evidence |
|---|---|---|
| 1. Grounded entry prices | **GROUNDED** | Nasdaq hist API bulk + IBKR MCP verification: **16/17 exact to the cent**, FCX gap = ex-div adjustment, disclosed (L002, L016) |
| 2. ~60d price history (names + SPY) | **GROUNDED** | ~1,254 daily bars/name, 5y, 514/514 eligible; chain: Yahoo probe OK/bulk 429 → Nasdaq 518 → IBKR BF-B (L002, L019) |
| 3. Sigma via fallback chain | **GROUNDED** | REALIZED_VOL_30D computed for all 27 published symbols (chain step 2; no options feed wired) |
| 4. Next earnings date | **GROUNDED** | 54-symbol confirmed-dates preflight: 45 confirmed; 9 vendor-empty classified print-week `ESTIMATED (±5d)` and penalized on the buffered window (L015) |
| 5. Index-union universe | **GROUNDED** | build_index_universe.py: 515 union, 514 eligible (L001) |

Missing **Enhancing** inputs (caps, never blockers): options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow, fundamentals/sentiment feeds → DQ 0.80, confidence cap LOW, gross-exposure cap 50% (academic — NO_TRADE).

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00–09, 13 | Published |
| 10/11/12 (midday/preclose/close) | 10: folded into the intraday run (see file); 11: published with the run's ~15:5x ET IBKR observations; 12: manual checkpoint, stub |
| 14 weekly review | Stub — not a Friday |
| 15_predictions.json | **Published**: 24 EQUITY_ALPHA (all with score_explainability + benchmark_price 751.83) + 3 MARKET_FORECAST + 17 settlements — publishing gate satisfied |
| 16 monthly review | Stub — not month-end |
| eligible_universe.txt / universe_summary.json | Published (515 union / 514 eligible) |
| technical_indicators.json | Published (518/518 OK) |
| earnings_calendar_manifest.json | Published (54 symbols, confirmed-dates preflight) |
| nasdaq_verification_manifest.json | Published (IBKR cross-check, 16/17 exact + FCX ex-div note) |
| price_history_fetch_manifest.json | Published (Nasdaq bulk record; Yahoo probe/429 documented) |
| Core ETF Market Forecast Block | Present (03; SPY/QQQ/SOXX records in 15) |
| Working-tree note | The uncommitted `gemini-3.5-flash-2026-07-13` package from a dead session remains in the tree; excluded from this run's commit via `.git/info/exclude` and reported — its ledger was still scanned for settlement/dedupe purposes |
