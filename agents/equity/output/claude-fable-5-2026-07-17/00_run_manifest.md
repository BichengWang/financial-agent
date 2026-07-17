# 00 Run Manifest — 2026-07-17

| Field | Value |
|---|---|
| Run date / model | 2026-07-17 (Friday; scheduled fire 15:59 ET — **at-the-close run**; all scored fields are the 2026-07-17 official close, collected 16:05–16:45 ET after the close completed) / claude-fable-5 |
| Run mode | Scheduled daily full pipeline |
| Data mode | **DELAYED** (2026-07-17 official close fetched this run; zero UNAVAILABLE Required fields) |
| Status target | GO if evidence thresholds pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** — family-coverage evidence threshold #2 (2/4 sourceable families → investable set empty; **14th consecutive scoring run**); recorded contemporaneously in 15_predictions.json |
| Agents executed | Orchestrator → Reflection → Data/Regime → technical_indicators.py → Factor Scoring → Portfolio §0 pre-check (NO_TRADE, no sizing) → Risk Committee (APPROVE) → Evolution |
| State machine | PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(§0 exit) → RISK_REVIEW → PUBLISHED → CLOSE_LOGGED → EVOLUTION_REVIEW |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-06-10` — **BASELINE_WINDOW_GAP** (window 06-02..06-26, target 06-19; only same-model in-window folder, 9d off target > 7d; L017) |
| Prediction settlement | **0 settled this run; canonical due inventory 0** — settlement_ledger.py ran pre-Reflection (119 EQ + 18 MF canonical, 0 conflicts); all due keys were settled by the same-day gpt-5 pre-open run (63 settlements). Settlements block: `[]` with note (L018) |
| Outstanding blockers | Fund/Sent families unwired (standing HUMAN_REVIEW, 14th run) — the structural GO blocker; Phase 2 bulk fetch is the unblock path (13) |

## Source Ledger Coverage (01; 199 rows)

| claim_type | rows |
|---|---|
| OBSERVED | 61 |
| DERIVED | 137 |
| INFERRED | 1 (regime label) |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE (recorded as field values) | Fund_Z/Sent_Z universe-wide; Treynor class (near-zero/negative betas, disclosed); FDXF pack; 14 monthly-MA50 gaps on short-history names (none published) |

Status eligibility: DELAYED data with all Required inputs grounded → GO-eligible on data; NO_TRADE on evidence-threshold construction.

## GO-Gate Table (Required inputs only may block)

| Required input | Status | Evidence |
|---|---|---|
| 1. Grounded entry prices | **GROUNDED** | Nasdaq official-close chain + IBKR daily-bar cross-check: **13/27 exact to the cent, 14 within 0.05%, 0 mismatches** (L016, `nasdaq_verification_manifest.json`) |
| 2. ~60d price history (names + SPY) | **GROUNDED** | ~1,256 daily bars/name, 5y incl. today's close, 519/519 (518 Nasdaq + BF-B IBKR) (L002) |
| 3. Sigma via fallback chain | **GROUNDED** | REALIZED_VOL_30D computed for all 26 published symbols (chain step 2; no options feed wired) |
| 4. Next earnings date | **GROUNDED** | 65-symbol confirmed-dates preflight: 51 confirmed; 14 cadence-estimated ±5d (post-print vendor-empty per 07-12 convention; TRV past-dated estimate rolled +91d, disclosed) (L015) |
| 5. Index-union universe | **GROUNDED** | build_index_universe.py: 515 union, 514 eligible (L001) |

Missing **Enhancing** inputs (caps, never blockers): options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow, fundamentals/sentiment feeds → DQ 0.80, confidence cap LOW, gross-exposure cap 50% (academic — NO_TRADE).

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00–09, 13 | Published |
| 10 midday monitor | Folded into the at-close run (see file) |
| 11 preclose check | Published — the 15:59 ET fire IS the preclose window; IBKR 16:1x observations recorded |
| 12 close log | **Published with real close data** (first run in this stack executing at the close) |
| 14 weekly review | **Published** (Friday after close — due and delivered this run; gpt-5's same-day pre-open package stubbed it as not-yet-due) |
| 15_predictions.json | **Published**: 23 EQUITY_ALPHA (all with score_explainability + benchmark_price 743.15) + 3 MARKET_FORECAST + `settlements: []` with due-inventory-zero note — publishing gate satisfied |
| 16 monthly review | Stub — not month-end |
| eligible_universe.txt / universe_summary.json | Published (515 union / 514 eligible) |
| technical_indicators.json | Published (518/519 OK; FDXF short-history error disclosed) |
| settlement_manifest.json | Published (canonical ledger output, pre-Reflection) |
| earnings_calendar_manifest.json | Published (65 symbols) |
| nasdaq_verification_manifest.json | Published (IBKR cross-check, 27 symbols) |
| price_history_fetch_manifest.json / today_close_fetch_manifest.json | Published (bulk 5y chain + same-day official-close append chain) |
| run_computed_manifest.json | Published (full computed analytics JSON — the source for every generated table) |
| Core ETF Market Forecast Block | Present (03; SPY/QQQ/SOXX records in 15) |
| Working-tree note | Clean at run time — no foreign uncommitted packages found (07-14 hazard checked); only this run's folder is new |
