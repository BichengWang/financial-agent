# 00 — Run Manifest — 2026-07-30

| Field | Value |
|---|---|
| Run date | 2026-07-30 |
| Model | `claude-opus-5` |
| Fired at | 2026-07-30T10:06:00-04:00 (intraday, ~36 min after the open) |
| Run mode | Scheduled daily run, full pipeline |
| Data mode | `DELAYED` |
| Price basis | 2026-07-29 close (last completed close) |
| Target date | 2026-08-27 (`run_date + 28d`) |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Regime | `NEUTRAL` |
| Data quality multiplier | 0.80 |

## Why `NO_TRADE`

Every one of the five **Required** inputs is grounded, so this is not a data failure and not
`REVIEW_ONLY`. The run stops at the **Evidence Thresholds** in `rules.md`:

- **Threshold 2 — "at least 3 of 4 factor families non-negative": FAILS.** `Fund_Z` and
  `Sent_Z` are `UNAVAILABLE` universe-wide (no wired fetch path; the SHADOW tooling covers far
  less than the 70%-of-universe bar). Per `rules.md § Family Aggregation` an `UNAVAILABLE`
  family may not be counted toward the 3-of-4 threshold, so the maximum attainable count is 2.
- **Threshold 4 — "data completeness at least 85%": FAILS.** Two of four families missing puts
  the data-quality multiplier at 0.80, below the 0.85 bar.

Zero names therefore qualify as investable, which is fewer than 5 → `NO_TRADE`
(`rules.md § Downgrade to NO_TRADE` #1).

**Portfolio feasibility is NOT the blocker this run.** The maximum attainable sleeve beta is
**+1.1258** against the 0.90 floor, so the beta band is *feasible*
(the mean of the 20 highest betas in the ≥80th-pctl pool clears it). The 2026-07-27
"provably infeasible" narrative does not apply today and was re-verified rather than reused.

## GO-Gate Table — Required inputs (only these may block `GO`)

| # | Required input | State | Evidence |
|---|---|---|---|
| 1 | Grounded entry price (Price Sourcing Standard) | `GROUNDED` | 30/30 published names agree within 0.1% across stockanalysis.com and CNBC; core ETFs additionally exact vs IBKR. |
| 2 | ~60d fetched price history per name + SPY | `GROUNDED` | 519/519 symbols fetched 5y daily bars; every last bar = 2026-07-29. |
| 3 | sigma via Sigma Fallback Chain | `GROUNDED` | REALIZED_VOL_30D computed for all 513 scored names; no name published with sigma UNAVAILABLE. |
| 4 | Next earnings date | `GROUNDED` | Forward calendar sweep 27/27 business days, complete=True; 262 CONFIRMED_CALENDAR, 251 NO_PRINT_IN_WINDOW, 0 ungrounded. |
| 5 | S&P 500 ∪ Nasdaq-100 index-union universe | `GROUNDED` | build_index_universe.py wrote 515 tickers (503 S&P 500, 101 Nasdaq-100, 89 overlap). |

**Enhancing inputs missing** (confidence/exposure caps only — never `GO` blockers per
`rules.md § Input Classification`): options IV/skew, short interest & borrow, bid-ask spread
tape, analyst revision tape, institutional ownership flow. Effect applied: data-quality
multiplier 0.80, confidence capped, gross exposure would be capped at 50%
had the run reached `GO`.

## Reflection baseline

| Field | Value |
|---|---|
| Baseline folder | `claude-fable-5-2026-07-02` |
| Baseline flag | `CROSS_MODEL_BASELINE` |
| MoM window | 2026-06-15 → 2026-07-09 (target 2026-07-02) |
| Same-model folders in window | 0 (none — no `claude-opus-5` package in the window) |
| Tied candidates at delta 0d | `claude-fable-5-2026-07-02`, `claude-sonnet-5-2026-07-02`, `gpt-5-2026-07-02` |

The three-way tie is resolved by the tie-break proposed in `13_evolution_log.md` and **all
tied candidates are reported** in `02_reflection.md § 1`, because their outcomes are not
invariant (hit rates claude-fable-5 47.8%, claude-sonnet-5 41.7%, gpt-5 7.1%).

## Prediction settlement summary

| Field | Value |
|---|---|
| Settled this run | 58 (49 `EQUITY_ALPHA`, 9 `MARKET_FORECAST`) |
| Timing flag | `TARGET_EQ_RUN_DATE` (all due keys have `target_date == run_date`; run fires pre-close) |
| Settlement price basis | 2026-07-29 close |
| Due inventory before | 0 |
| Conflicts | 0 |
| Canonical `EQUITY_ALPHA` n / eff_n | 347 / 1 |
| Canonical `MARKET_FORECAST` n / eff_n | 63 / 1 |
| Track A calibration gate | `INSUFFICIENT_EFFECTIVE_N` (needs n≥20 **and** eff_n≥3) |

`eff_n` remains 1 for both record types. The 2026-07-28 falsifiable projection still stands:
`EQUITY_ALPHA` eff_n → 2 on **2026-08-05**
(43 pending),
`MARKET_FORECAST` → 2 on **2026-08-09**
(6 pending). Today is before both
dates, so eff_n=1 is expected, not a regression.

## Source Ledger coverage

| Coverage class | Count |
|---|---|
| `OBSERVED` | 36 |
| `DERIVED` | 56 |
| `INFERRED` | 24 |
| `ILLUSTRATIVE` | 0 |
| `UNAVAILABLE` | 1026 (`Fund_Z`, `Sent_Z` universe-wide) |

Status eligibility: `GO` blocked by Evidence Thresholds 2 and 4 only; no Required input failed,
no fabrication or lineage violation found by the risk committee.

## Agents executed

`Orchestrator → Reflection → Data & Regime → technical_indicators.py → Factor Scoring →
Portfolio Construction (Task-0 feasibility pre-check) → Risk Committee → Evolution`

State machine: `PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED →
PORTFOLIO_DRAFT → RISK_REVIEW → PUBLISHED (NO_TRADE)`. No revision pass was consumed.

## Artifact checklist

| Artifact | Status |
|---|---|
| `eligible_universe.txt` | present — 515 tickers |
| `universe_summary.json` | present — index-union counts |
| `technical_indicators.json` | present — 515 records incl. core ETFs |
| `run_computed_manifest.json` | present — computed analytics (all artifact numerics) |
| `settlement_manifest.json` | present — canonical ledger, due_inventory 0 |
| `15_predictions.json` | present — 24 EQUITY_ALPHA + 3 MARKET_FORECAST + 58 settlements |
| `00`–`09`, `13` | present |
| `10_midday_monitor.md` | present — real monitor (intraday fire) |
| `11`, `12` | stubbed with reason (run fired pre-close) |
| `14_weekly_review.md` | not applicable — Thursday; due Friday after close |
| `16_monthly_review.md` | not applicable — last trading day of July is 2026-07-31 |
| Core ETF Market Forecast Block | present — SPY / QQQ / SOXX in `03`, records in `15` |

## Outstanding blockers

1. **`Fund_Z` / `Sent_Z` unavailable universe-wide** — the single structural blocker to any
   `GO`. Needs Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`
   (bulk `companyfacts.zip` + threaded Nasdaq fetch across all 513 names).
2. **Rank-order inversion in the composite score** — weighted-mean rank IC -0.1975 over
   n=347. Track A calibration proposal is **DEFERRED**, not rejected: eff_n=1 < 3.
3. **`MARKET_FORECAST` direction accuracy 16.4%** (n=63) — the
   `mu = beta x SPY_mu` category error diagnosed 2026-07-24 is unfixed and also Track-A-gated.
