# 00 — Run Manifest — 2026-08-01

| Field | Value |
|---|---|
| Run date | 2026-08-01 (Saturday) |
| Fired at | 2026-08-01T14:35:00-04:00 |
| Model | `claude-opus-5` |
| Run mode | Weekend run — no live session; price basis is the completed **Friday 2026-07-31** close |
| Data mode | `DELAYED` |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Regime | `BULL` |
| Universe | S&P 500 ∪ Nasdaq-100 = 515 names; 513 scored, 2 rejected |
| Percentile label | `INDEX_UNION_PCTL (n=513)` |
| Target date | 2026-08-29 (`run_date + 28d`) |
| Data-quality multiplier | 0.80 |

## Why `NO_TRADE`

The investable set is **empty**, and it is empty for structural evidence reasons — not
because the portfolio geometry failed. Three of the five `rules.md § Evidence Thresholds`
fail for **every** name in the universe:

| # | Threshold | Result | Detail |
|---|---|---|---|
| 1 | Adjusted-score pctl ≥ 80 | **PASS** | 103 names at/above the 80th percentile |
| 2 | ≥ 3 of 4 factor families non-negative | **FAIL** | only 2 of 4 families are AVAILABLE (Fund_Z and Sent_Z are UNAVAILABLE universe-wide); a max of 2 can be non-negative, so the 3-of-4 bar is structurally unsatisfiable for every name |
| 3 | No family > 50% of conviction | **FAIL** | Tech_Z carries 66.7% of live composite weight (0.30 of the 0.45 available) — above the 50% cap |
| 4 | Data completeness ≥ 85% | **FAIL** | data-quality multiplier 0.80 < 0.85 |
| 5 | No hard stop | **PASS** | no § Stop Criteria hard halt triggered |

**The portfolio beta band was recomputed this run and is FEASIBLE** — attainable sleeve beta
spans `[-0.5864, +1.3556]` against the
`0.90–1.10` band. The 2026-07-27 "provably infeasible" narrative would have been **wrong
here for the third consecutive run**; it is recomputed, not inherited. `NO_TRADE` is an
evidence-threshold outcome.

## GO-Gate Table — Required inputs (`rules.md § Input Classification`)

| # | Required input | State | Evidence |
|---|---|---|---|
| 1 | Grounded entry price | **GROUNDED** | 77/77 names verified across 3 independent sources; max deviation 0.0661% (tolerance 1%) |
| 2 | ~60d price history per name + SPY | **GROUNDED** | 519/519 symbols × 5y daily bars in 31.8s; every last bar = 2026-07-31 |
| 3 | `sigma` via Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` for all 205 ranked names and all 3 core ETFs |
| 4 | Next earnings date | **GROUNDED** | Forward calendar sweep, 26/26 business days, zero transport failures → complete; 195 CONFIRMED_CALENDAR + 320 NO_PRINT_IN_WINDOW = 515/515 |
| 5 | Index-union universe | **GROUNDED** | `build_index_universe.py` → 515 names (503 S&P 500, 101 Nasdaq-100, 89 overlap) |

All five Required inputs are grounded. **No Required input blocks `GO`.**

### Enhancing inputs missing (confidence / exposure caps only — never GO blockers)

| Enhancing input | State | Effect |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` | No options feed wired; sigma falls to `REALIZED_VOL_30D` (chain step 2) |
| Short interest / borrow | `UNAVAILABLE` | Contributes to `Sent_Z` being `UNAVAILABLE` |
| Bid-ask spread tape | `UNAVAILABLE` | 50bp exclusion filter cannot be applied directly; ADDV20 used as the liquidity proxy |
| Analyst revision tape | `UNAVAILABLE` | Contributes to `Sent_Z` being `UNAVAILABLE` |
| Institutional ownership flow | `UNAVAILABLE` | Contributes to `Sent_Z` being `UNAVAILABLE` |
| Fundamental XBRL at universe scale | `UNAVAILABLE` | `Fund_Z` `UNAVAILABLE` — SHADOW tooling covers ~4.7% of universe, far below the 70% bar |

These are the direct cause of the DQ multiplier 0.80 and of evidence
thresholds 2–4 failing. They are recorded here as caps, **not** as `GO` blockers — the
distinction `rules.md § Input Classification` requires.

## Reflection baseline

| Field | Value |
|---|---|
| Baseline path | `agents/equity/output/claude-fable-5-2026-07-04` |
| Baseline flag | **`CROSS_MODEL_BASELINE`** |
| MoM target date | 2026-07-04 (`run_date - 28d`) |
| Window | 2026-06-17 … 2026-07-11 |
| In-window candidates | 40 |
| Tie at \|Δ\| = 0d | **2 folders** — resolved by `agents.md § Orchestrator Step 2` rule 8 |
| Selection reason | same model family as the executing model claude-opus-5 |

Every tied candidate is disclosed with its own settled statistics in `02 § 1`, as rule 8
requires.

## Prediction settlement summary

| Field | Value |
|---|---|
| Settled this run | **107** (92 `EQUITY_ALPHA`, 15 `MARKET_FORECAST`) |
| Unsettleable | 0 |
| Due inventory after this run | **0** |
| Conflicts | **0** |
| Settlement price basis | 2026-07-31 close (ORDINARY for Friday targets; `WEEKEND_TARGET` for Saturday targets) |

### Canonical rolling calibration

| Record type | raw `n` | 28d `eff_n` | Hit rate | CI coverage | Mean z | Track A gate |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 439 | **1** | 42.37% | 70.16% | -0.4608 | `INSUFFICIENT_EFFECTIVE_N` |
| `MARKET_FORECAST` | 78 | **1** | 20.27% | 78.21% | -0.6633 | `INSUFFICIENT_EFFECTIVE_N` |

`eff_n` projection (emitted by `settlement_ledger.py`, Track B 2026-07-28):
`EQUITY_ALPHA` → **2026-08-05** (43 pending);
`MARKET_FORECAST` → **2026-08-09** (6 pending).
The 2026-07-28 falsifiable claim (EQ increments 2026-08-05) **still holds** after adding
92 equity settlements today. No Track A calibration change is eligible.

## Source Ledger coverage (`01_preflight.md`)

| claim_type | Rows |
|---|---|
| `OBSERVED` | 80 |
| `DERIVED` | 54 |
| `INFERRED` | 24 |
| `ILLUSTRATIVE` | 0 |
| `UNAVAILABLE` | 6 |

Status eligibility: `ILLUSTRATIVE` row count is **0**, so the run is eligible for a live
status. It publishes `NO_TRADE` on evidence, not on data mode.

## Agents executed

`Orchestrator` → `Reflection` → `Data and Regime` → `technical_indicators.py` →
`Factor Scoring` → `Portfolio Construction (Task 0 feasibility pre-check)` →
`Risk Committee` → `Evolution`.

State machine: `PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED →
PORTFOLIO_DRAFT → RISK_REVIEW → NO_TRADE → CLOSE_LOGGED → EVOLUTION_REVIEW`.
Revision passes used: **0 of 1** (the risk committee approved the `NO_TRADE`
recommendation without requesting a revision).

## Artifact checklist

| Artifact | State |
|---|---|
| `00`–`09` | Published |
| `10`, `11`, `12` | Published as weekend stubs — no trading session exists on 2026-08-01 |
| `13_evolution_log.md` | Published |
| `14_weekly_review.md` | **Published (real)** — the Friday 2026-07-31 run never executed, so this run owes it |
| `15_predictions.json` | Published — 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` + 107 settlements |
| `16_monthly_review.md` | **Published (real)** — 2026-07-31 was the last trading day of July and no run fired that day |
| `eligible_universe.txt` | Published (515 tickers) |
| `universe_summary.json` | Published |
| `technical_indicators.json` | Published (519 tickers, daily/weekly/monthly) |
| Core ETF Market Forecast Block | **Present** — SPY, QQQ, SOXX in `03` with 3 `MARKET_FORECAST` records |

## Outstanding blockers

1. **`Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide.** This alone forces `NO_TRADE`
   on every run regardless of market conditions. Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk `companyfacts.zip`
   + threaded Nasdaq sentiment across all 513 names) is the only path
   that clears thresholds 2–4. Unchanged since 2026-07-15.
2. **Rank-order inversion persists** — weighted-mean rank IC -0.1314 over n=439,
   negative in 20 of 28 vintages. Confidence is capped at `MEDIUM` per
   `agents.md § Calibration Feedback Binding`.
3. **`eff_n` = 1 for both record types** — no Track A calibration change is eligible until
   2026-08-05 at the earliest.
4. **IBKR MCP unreachable this run** (weekend); price grounding stood on three independent
   web sources instead. Documented in `01`.
