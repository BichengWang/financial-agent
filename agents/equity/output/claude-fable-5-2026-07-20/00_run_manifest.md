# 00 Run Manifest — 2026-07-20 (claude-fable-5)

| Field | Value |
|---|---|
| Run date / fire | 2026-07-20, Monday, intraday 12:21 ET (scheduled task; first intraday full-pipeline fire) |
| Run mode | Full daily pipeline; entry/settlement basis = last completed close (Fri 2026-07-17) — no intraday prints in scoring or settlement |
| Data mode | **DELAYED** (L002): Nasdaq historical bulk 518/519 + IBKR (BF-B, 17-name verification); Yahoo 429-blocked 5th session |
| Status target → final | GO target → **NO_TRADE** (15th consecutive; structural family gate + event concentration + beta feasibility — 07) |
| Agents executed | Orchestrator (reflection, manifests), Data/Regime (03), Factor Scoring (04/05), Portfolio Construction (07 pre-check only), Risk Committee (08 APPROVE), Evolution (13 REJECT/NO_CHANGE_ACCEPTED) |
| Reflection baseline | agents/equity/output/claude-fable-5-2026-06-10 — **BASELINE_WINDOW_GAP** (12d off 06-22 target; only same-model folder in window) |
| Prediction settlement | **68 settled** (56 EQ + 12 MF) at 07-17 close: 51 WEEKEND_TARGET + 17 TARGET_EQ_RUN_DATE; canonical ledger re-run: 175 EQ + 30 MF, 0 conflicts, due 0 (settlement_manifest.json) |
| Rolling calibration | EQ n=175: hit 51.4%, CI 77.1%, mean z −0.24, rank IC −0.049 → **MEDIUM cap binds**; MF n=30: hit 20%, CI 60% (separate line) |
| Source Ledger coverage | 325 rows — OBSERVED 136, DERIVED 174, INFERRED 15, ILLUSTRATIVE 0, UNAVAILABLE 0 (Required); disclosure row L012 carries UNAVAILABLE freshness by design |
| Status eligibility | All Required inputs grounded → GO-eligible on inputs; NO_TRADE on evidence thresholds (below) |
| Outstanding blockers | Fund/Sent families unwired (15th run; Phase-2 plan pending); MF mu-prior calibration escalated to 07-31 structural review |

## GO-Gate Table (Required inputs only)

| Required input | Status | Evidence |
|---|---|---|
| 1. Grounded entry price per name | **GROUNDED** | 07-17 closes, Nasdaq bulk + IBKR verification (L022–L038, per-name rows) |
| 2. ≥60 trading days history per name + SPY | **GROUNDED** | 5y daily bars, 514/515 (FDXF excluded, disclosed) |
| 3. sigma via fallback chain | **GROUNDED** | REALIZED_VOL_30D universe-wide (chain step 2; no IV feed wired) |
| 4. Next earnings date (confirmed or cadence-estimated) | **GROUNDED** | 2-pass preflight: 20 confirmed, 2 Zacks-estimated, 12 post-print +91d cadence (±5d) — every published name covered |
| 5. Index-union universe | **GROUNDED** | build_index_universe.py, 515 union (L003) |

**Missing Enhancing inputs (caps, never GO blockers):** options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional flow, GICS sector feed → DQ 0.80, confidence caps (MEDIUM ceiling; sleeve LOW), 50% gross-cap would apply to any GO.

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00–09 | Published (07 = NO_TRADE pre-check; no weights) |
| 10 | Published (midday-slot fire; LIVE observations L322–L325, no scoring use) |
| 11 / 12 | N/A stubs with explanation (intraday publish precedes checkpoints) |
| 13 | Published — Track A tested, REJECT, NO_CHANGE_ACCEPTED |
| 14 / 16 | N/A stubs (Friday / month-end) |
| 15_predictions.json | **Published** — 33 EQUITY_ALPHA (all with score_explainability + benchmark_price) + 3 MARKET_FORECAST (SPY/QQQ/SOXX block present) + 68 settlements |
| eligible_universe.txt / universe_summary.json | Published (515 union) |
| technical_indicators.json | Published (517/518 OK; FDXF UNAVAILABLE disclosed) |
| settlement_manifest.json | Published (canonical, --as-of 2026-07-20) |
| price_history / nasdaq_verification / earnings_calendar / run_computed manifests | Published |

State machine: PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(pre-check NO_TRADE) → RISK_REVIEW(APPROVE) → **PUBLISHED (NO_TRADE)** → EVOLUTION_REVIEW(complete).
