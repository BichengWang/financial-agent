# 00 Run Manifest — 2026-07-21 (claude-fable-5)

| Field | Value |
|---|---|
| Run date / fire | 2026-07-21, Tuesday, intraday ~15:10-15:30 ET (scheduled task fire; full-pipeline run) |
| Run mode | Full daily pipeline; entry/settlement basis = last completed close (Mon 2026-07-20) — market open at run time, today's 07-21 intraday bar fetched then trimmed before any computation |
| Data mode | **DELAYED** (L007-L009): Yahoo v8 chart API bulk fetch, 521/521 symbols OK (8-worker threaded, ~37s) — Yahoo unblocked this session after 5 consecutive 429-blocked sessions (2026-07-13 through 07-20 per prior logs); no fallback needed. VIX/rf from Yahoo (`^VIX`, `^IRX`). All five Required inputs grounded; no ILLUSTRATIVE content. |
| Status target → final | GO target → **NO_TRADE** (16th consecutive; structural Fund/Sent family gate + portfolio beta-band infeasibility + earnings-window concentration) |
| Agents executed | Orchestrator (reflection, manifests), Data/Regime (03), Factor Scoring (04/05), Portfolio Construction (07 pre-check only), Risk Committee (08 APPROVE), Evolution (13) |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-06-10` — **BASELINE_WINDOW_GAP** (13d off 2026-06-23 target; only same-model folder in the 45d-21d window) |
| Prediction settlement | **0 newly settled** (due_inventory = 0 — nothing became due between 07-20 and 07-21); canonical ledger unchanged: 175 EQUITY_ALPHA + 30 MARKET_FORECAST settlements, 0 conflicts (`settlement_manifest.json`, `--as-of 2026-07-21`) |
| Rolling calibration | EQ n=175: hit 51.4%, CI 77.1%, mean z −0.236, rank IC (weighted) −0.049 → **MEDIUM cap binds** (calibration feedback, though structurally moot — see below); MF n=30: hit 20%, CI 60% (separate line) |
| Source Ledger coverage | 155 rows — OBSERVED/DERIVED majority, 1 UNAVAILABLE (FDXF), SHADOW-tagged diagnostic rows disclosed but not counted |
| Status eligibility | All Required inputs grounded → GO-eligible on inputs; NO_TRADE on evidence thresholds and portfolio feasibility (below) |
| Outstanding blockers | Fund_Z/Sent_Z unwired at universe scale (Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` still not attempted — bulk `companyfacts.zip` + threaded Nasdaq sentiment across ~514 names); MF mu-prior calibration escalated to 2026-07-31 structural review |

## GO-Gate Table (Required inputs only)

| Required input | Status | Evidence |
|---|---|---|
| 1. Grounded entry price per name | **GROUNDED** | 07-20 closes, Yahoo v8 chart bulk fetch, single-source DELAYED (L007, per-name rows) |
| 2. ≥60 trading days history per name + SPY | **GROUNDED** | 5y daily bars, 517/518 OK (FDXF excluded, disclosed L006) |
| 3. sigma via fallback chain | **GROUNDED** | REALIZED_VOL_30D universe-wide (chain step 2; no IV feed wired) |
| 4. Next earnings date (confirmed or cadence-estimated) | **GROUNDED** | 2-pass preflight on top-60 shortlist: 46 confirmed via Nasdaq analyst endpoint, 14 vendor-empty → +91d post-print cadence estimate (±5d); 0 second-pass entrants needed (top-20 post-penalty is a strict subset of the fetched top-60) |
| 5. Index-union universe | **GROUNDED** | `build_index_universe.py`, 515 union (L001) |

**Missing Enhancing inputs (caps, never GO blockers):** options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional flow, GICS sector feed → DQ 0.80, confidence capped LOW for every ranked name (structural family gate makes even MEDIUM unreachable — see 05/08), 50% gross-cap would apply to any GO.

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00–09 | Published (07 = NO_TRADE pre-check; no weights drafted) |
| 10 | Published (intraday-slot fire; LIVE IBKR-independent observational snapshot, no scoring use) |
| 11 / 12 | N/A stubs with explanation (run precedes 15:45/16:20 ET checkpoints) |
| 13 | Published — Track A/B review, see decision below |
| 14 / 16 | N/A stubs (not Friday close / not month-end) |
| 15_predictions.json | **Published** — 20 EQUITY_ALPHA (monitoring sleeve, all with `score_explainability` + `benchmark_price`) + 3 MARKET_FORECAST (SPY/QQQ/SOXX block present) + settlements: [] (0 newly due) |
| eligible_universe.txt / universe_summary.json | Published (515 union) |
| technical_indicators.json | Published (517/518 OK; FDXF UNAVAILABLE disclosed) |
| settlement_manifest.json | Published (canonical, `--as-of 2026-07-21`) |
| fundamental_diagnostics.json / sentiment_diagnostics.json | Published — SHADOW-only, top-20 shortlist, 100% sourceable both families |

State machine: `PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(pre-check NO_TRADE) → RISK_REVIEW(APPROVE) → PUBLISHED (NO_TRADE) → EVOLUTION_REVIEW(complete)`
