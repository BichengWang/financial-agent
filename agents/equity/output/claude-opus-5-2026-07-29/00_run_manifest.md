# 00 Run Manifest — 2026-07-29

| Field | Value |
|---|---|
| Run date | 2026-07-29 (Wednesday) |
| Model | `claude-opus-5` |
| Fire window | **Pre-open**, 08:05 ET — before the 2026-07-29 session opens |
| Price basis | **2026-07-28** close (the last completed session) |
| Run mode | Full pipeline (`00`–`09`, `13`, `15`) |
| Data mode | `DELAYED` |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Target date for all forecasts | 2026-08-26 (`run_date + 28d`) |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-07-01` |
| Baseline flag | **`CROSS_MODEL_BASELINE`** |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |

## State Transitions

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED (NO_TRADE) -> EVOLUTION_REVIEW`

No stage halted. `NO_TRADE` is the composition outcome defined in `rules.md § Downgrade to NO_TRADE` #1,
not a data or process failure.

## Why `NO_TRADE`

Zero of 514 scored names clear `rules.md § Evidence Thresholds`. Three of the five checks fail for
**every** name in the universe, and all three are structural rather than name-specific:

| Threshold | Result |
|---|---|
| #1 Adjusted-score pctl >= 80 | **PASS** for 103 names |
| #2 >= 3 of 4 factor families non-negative | **FAIL** universe-wide — only 2 families are sourceable (`Fund_Z` and `Sent_Z` are `UNAVAILABLE`, L046/L047) |
| #3 No family > 50% of conviction | **FAIL** universe-wide — Technical carries 0.30 of the 0.45 available weight |
| #4 Data completeness >= 85% | **FAIL** universe-wide — data-quality multiplier is 0.80 (L049) |
| #5 No hard stop | PASS |

Fewer than 5 investable names → `NO_TRADE`. All 24 published names are **monitoring sleeve**.

**Portfolio feasibility is NOT the binding constraint this run.** The Task-0 pre-check finds the
beta band *marginally attainable*: a fully-invested sleeve at the 5% single-name cap needs >= 20 names,
and the mean of the 20 highest betas in the >= 80th-pctl pool is **+0.9090**
against the 0.90 floor — feasible by 0.90bp. This differs from
2026-07-27 (+0.8519, infeasible). The blocker is candidate quality, and it is worth stating precisely
rather than reusing the prior run's infeasibility narrative.

## GO-Gate Table — Required Inputs

| # | Required input (`rules.md § Input Classification`) | State | Evidence |
|---|---|---|---|
| 1 | Grounded entry price per the Price Sourcing Standard | **GROUNDED** | 28/28 symbols verified, **28/28 exact to the cent** across stockanalysis.com + CNBC + Nasdaq; core ETFs additionally match IBKR (L002, L011, L012) |
| 2 | ~60 trading days of history per name and for SPY | **GROUNDED** | 519/519 symbols, 5y daily bars, 25.8s, zero failures (L003, L004) |
| 3 | `sigma` via the Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` for all 514 scored names (L013) |
| 4 | Next earnings date, confirmed or cadence-estimated | **GROUNDED** | **514/514 of the universe** via a complete 28/28-business-day forward calendar sweep (L022), cross-validated 25/25 against the per-name endpoint (L023) |
| 5 | S&P 500 ∪ Nasdaq-100 index union | **GROUNDED** | `build_index_universe.py` → 515 tickers (503 S&P 500, 101 Nasdaq-100, 89 overlap) (L001) |

All five Required inputs are grounded. No Required input blocks `GO`; the block is candidate quality.

### Enhancing inputs missing (confidence / exposure caps only — never GO blockers)

Options IV/skew, short interest & borrow, bid-ask tape, analyst revision tape, institutional ownership
flow, full-universe fundamental feed (L036, L046, L047, L048). Effect: data-quality multiplier held at
0.80 and confidence capped — never cited as a `GO` blocker.

## Prediction Settlement Summary

| Field | Value |
|---|---|
| Settled this run | **44** (38 `EQUITY_ALPHA`, 6 `MARKET_FORECAST`) |
| Timing flag | `TARGET_EQ_RUN_DATE` on all 44 — every due key had `target_date` = 2026-07-29 = run date, and this run fires pre-open, so each settles at the last completed close (2026-07-28) |
| Due inventory after settlement | **0** |
| Conflicts | **0** |
| Canonical rows total | 298 `EQUITY_ALPHA`, 54 `MARKET_FORECAST` |

### Rolling calibration (canonical, from `settlement_ledger.py`)

| Record type | raw `n` | 28d `eff_n` | Hit rate | CI coverage | Mean z | Track A gate |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 298 | **1** | 50.00% | 74.50% | -0.2596 | **INSUFFICIENT_EFFECTIVE_N** |
| `MARKET_FORECAST` | 54 | **1** | 18.52% | 72.22% | -0.6880 | **INSUFFICIENT_EFFECTIVE_N** |

Weighted-mean rank IC **-0.2064** over 298 settled pairs across 20 vintages.
`eff_n` projections hold: `EQUITY_ALPHA` reaches 2 on **2026-08-05**
(43 pending),
`MARKET_FORECAST` on **2026-08-09**
(6 pending). Track A stays gated.

## Source Ledger Coverage (`01_preflight.md`)

| claim_type | Rows |
|---|---|
| `OBSERVED` | 12 |
| `DERIVED` | 33 |
| `INFERRED` | 2 |
| `UNAVAILABLE` | 4 |
| `ILLUSTRATIVE` | 0 |

No `ILLUSTRATIVE` rows: this is a live `DELAYED` run. Status eligibility: all Required inputs
`OBSERVED`/`DERIVED`; `NO_TRADE` reflects composition, not lineage.

## Artifact Checklist

| Artifact | State |
|---|---|
| `00_run_manifest.md` … `09_final_report.md` | present |
| `10` / `11` / `12` | present — not applicable to a pre-open fire, one-line explanation each |
| `13_evolution_log.md` | present — 1 Track B change **ACCEPTED** |
| `14_weekly_review.md` | present — not Friday; one-line explanation |
| `15_predictions.json` | **present** — 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` + 44 settlements |
| `16_monthly_review.md` | present — 2026-07-29 is not the last trading day of July (that is 2026-07-31); one-line explanation |
| `eligible_universe.txt` / `universe_summary.json` | present — 515 tickers |
| `technical_indicators.json` | present — 519 tickers, daily/weekly/monthly |
| `settlement_manifest.json` | present — due inventory 0, conflicts 0 |
| `run_computed_manifest.json` | present — every published figure derives from it |
| `price_verification.json` | present — 28 symbols, 28 exact |
| `earnings_calendar.json` | present — 28/28 business days, 0 failures |
| `stockanalysis_history_manifest.json` | present — 519/519 symbols |
| `mom.json` | present — all tied MoM baselines computed |
| **Core ETF Market Forecast Block** | **present** — SPY / QQQ / SOXX, all fields populated |

## Outstanding Blockers

1. `Fund_Z` / `Sent_Z` `UNAVAILABLE` universe-wide keeps evidence threshold #2 unreachable. Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk `companyfacts.zip` + threaded
   Nasdaq sentiment across all 514 names) is the unblock. Unchanged this run.
2. `MARKET_FORECAST` calibration remains broken (18.52% direction over n=54). Root cause was
   diagnosed 2026-07-24 (`mu_ETF = beta x SPY_mu` is a category error). The fix is Track A and gated
   at `eff_n = 1` until 2026-08-09.
3. `agents.md § Orchestrator Step 2` still has **no MoM baseline tie-break rule**. This run shows the gap
   is now material, not cosmetic — see `02 § 1`. Carried as the next run's Track B candidate.
