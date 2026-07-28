# 00 Run Manifest — 2026-07-28

| Field | Value |
|---|---|
| Run date | 2026-07-28 (Tuesday) |
| Fire time | 2026-07-28T08:05 ET (pre-open) |
| Model | `claude-opus-5` |
| Run mode | Scheduled daily run, full pipeline |
| Data mode | **`DELAYED`** — every price fetched this run, ≤1-day lag |
| Price basis | **2026-07-27 close** (last completed session; the run fires before today's open) |
| Target date | 2026-08-25 (`run_date + 28d`) |
| Status target | `GO` if the evidence thresholds clear |
| **Final status** | **`NO_TRADE`** |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Universe | S&P 500 ∪ Nasdaq-100 index union, 514 scored of 515 |
| Regime | **`NEUTRAL`** |

## State Machine

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

Every transition completed. Terminal state **`NO_TRADE`** — inputs are valid and fully grounded, but
no candidate clears the investable evidence bar (`rules.md § Stop Criteria`, Downgrade to NO_TRADE #1).

## Why `NO_TRADE` and not `GO`

Two independent, non-discretionary blockers. Either alone is sufficient:

1. **Evidence Threshold #2 — "at least 3 of 4 factor families non-negative" cannot be evaluated.**
   `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide (no fetch path wired; L046, L047). At most
   2 of 4 families exist, so the 3-of-4 test is unsatisfiable for every name in the universe.
2. **Evidence Threshold #4 — "data completeness at least 85%".** The data-quality multiplier is
   **0.8** for every name (80% < 85%), set by the two missing families plus the
   entire Enhancing block (L035, L048).

A third, independent finding is recorded but is **not** the binding reason — see the feasibility
pre-check below.

## Portfolio Feasibility Pre-check (Task 0)

| Quantity | Value |
|---|---|
| Single-name cap | 5% ⇒ minimum **20 names** to be fully invested |
| Candidate pool (≥ 80th pctl) | 103 names |
| **Max attainable sleeve beta** | **0.899853** (mean of the 20 highest betas in the pool) |
| Required beta band | 0.90 – 1.10 |
| Shortfall vs the floor | **0.000147** |
| Verdict | `INFEASIBLE` — **but by 1.47 basis points** |

**Read this number honestly.** The beta constraint fails, but it fails by 1.5 bp — a knife-edge miss,
not a structural one. It is materially different from the 2026-07-27 package's 0.8519 (a
4.81pp miss). It would flip to feasible on a trivial change in one constituent's beta.
**The binding reasons for `NO_TRADE` are the two evidence thresholds above, which are not marginal at
all.** The feasibility result is reported as corroborating evidence, not as the load-bearing argument.

Correlation and drawdown, by contrast, both pass with room: average pairwise correlation
0.1931 (cap 0.45) and 95th-pctl 1-month drawdown
7.57% (cap 8%). The sleeve is disqualified for being too
defensive, not too risky.

## Reflection Baseline

- **Folder:** `agents/equity/output/gpt-5-2026-06-30`
- **Flag:** **`CROSS_MODEL_BASELINE`** (L045)
- **Window:** 2026-06-13 → 2026-07-07, target 2026-06-30; the chosen folder is
  an exact target hit, 28 days old.
- **Why cross-model:** the only `claude-opus-5` folders are 2026-07-24, 2026-07-26, 2026-07-27 and
  today — all newer than 21 days, which step 7 of the baseline algorithm forbids.
- **Tie-break, disclosed and materially different from 2026-07-27's.** `agents/equity/output/claude-opus-4-8-2026-06-30` also
  lands exactly on target. Unlike the 07-27 tie, these two packages are **not** field-identical: across
  the 13 shared keys there are **81 field differences**
  (different name sets, different entry-price vendors, different `adj_score` conventions). The pick
  therefore does change individual MoM numbers, so **both were computed**:

  | Baseline | Equity rows | Hits | Hit rate | Mean alpha | Median MoM return |
  |---|---|---|---|---|---|
  | **gpt-5-2026-06-30** (chosen) | 14 | 7 | 50.00% | +0.35% | +0.10% |
  | claude-opus-4-8-2026-06-30 (alternative) | 15 | 7 | 46.67% | -3.26% | -0.97% |

  The **qualitative conclusion is invariant** — a coin-flip direction hit rate over the month under
  either baseline. The mean-alpha gap comes from the alternative's semiconductor and high-beta sleeve
  (AMD, MU, TSLA), which the chosen baseline does not hold. `gpt-5-2026-06-30` was taken
  for continuity with the 2026-07-27 precedent (the model with continuous run history in the window:
  20 folders vs 1).

## Prediction Settlement Summary

| Field | Value |
|---|---|
| Due at `as_of = 2026-07-28` (before this run) | 35 |
| **Settled this run** | **35** (29 `EQUITY_ALPHA`, 6 `MARKET_FORECAST`) |
| Timing flag | `TARGET_EQ_RUN_DATE` — every due key has `target_date == 2026-07-28` and this run fires pre-open, so each settles at the latest completed close (2026-07-27) |
| Unsettled / unresolvable | 0 |
| Due inventory after this run | **0** |
| Conflicts | **0** |
| Canonical `EQUITY_ALPHA` total | 260 (raw `n` 260) |
| Canonical `MARKET_FORECAST` total | 48 (raw `n` 48) |
| `EQUITY_ALPHA` 28-day `eff_n` | **1** — Track A gate `INSUFFICIENT_EFFECTIVE_N` |
| `MARKET_FORECAST` 28-day `eff_n` | **1** — Track A gate `INSUFFICIENT_EFFECTIVE_N` |

## GO-Gate Table — Required inputs only

| # | Required input (`rules.md § Input Classification`) | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price per the Price Sourcing Standard | **GROUNDED** | 28/28 names two-source grounded; Nasdaq vs stockanalysis exact to the cent on 28/28 (max diff 0.000000%). L002, L004, L005, L006 |
| 2 | ~60 trading days of history per name and for SPY | **GROUNDED** | 519/519 symbols fetched, 514 scored names carry ≥186 daily bars. L002, L003, L011 |
| 3 | `sigma` via the Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` for every ranked name and all three ETFs; universe median 9.36%. L013 |
| 4 | Next earnings date (confirmed or cadence-estimated) | **GROUNDED** | 58 names resolved over 2 bounded passes, **0 fetch errors**, converged on a fully-grounded top-20. L022–L026 |
| 5 | Index-union universe from `build_index_universe.py` | **GROUNDED** | 515 tickers (503 S&P 500, 101 Nasdaq-100, 89 overlap). L001 |

**No Required input failed.** The run is therefore not `REVIEW_ONLY` and not `HALTED`: the data is
sound and the abstention is about candidate quality, exactly what `NO_TRADE` means.

### Enhancing inputs — confidence / exposure caps, never GO blockers

| Enhancing input | Status | Effect |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` | sigma falls back to `REALIZED_VOL_30D`; DQ reduced |
| Short interest / borrow | `UNAVAILABLE` | `Sent_Z` `UNAVAILABLE` (L047) |
| Bid-ask spread tape | `UNAVAILABLE` | 50 bp exclusion filter cannot be applied; disclosed in `04` |
| Analyst revision tape | `UNAVAILABLE` | `Sent_Z` `UNAVAILABLE` (L047) |
| Institutional ownership flow | `UNAVAILABLE` | `Sent_Z` `UNAVAILABLE` (L047) |
| Fundamental / XBRL feed at universe scale | `UNAVAILABLE` | `Fund_Z` `UNAVAILABLE` (L046) |

Per `rules.md § Input Classification` these cap confidence and gross exposure; **none of them is cited
as a `GO` blocker anywhere in this package.**

## Source Ledger Coverage

| claim_type | Rows |
|---|---|
| `OBSERVED` | 12 |
| `DERIVED` | 34 |
| `INFERRED` | 4 |
| `UNAVAILABLE` | 5 |
| `ILLUSTRATIVE` | 0 |

Status eligibility: no `ILLUSTRATIVE` rows and no `UNAVAILABLE` Required input ⇒ the run is eligible
for any live status; `NO_TRADE` is chosen on candidate quality.

## Artifact Checklist

| Artifact | Present |
|---|---|
| `00_run_manifest.md` … `09_final_report.md` | yes |
| `10_midday_monitor.md`, `11_preclose_check.md`, `12_close_log.md` | yes (stubs — this is a pre-open fire) |
| `13_evolution_log.md` | yes |
| `14_weekly_review.md` | yes (not due — Tuesday) |
| `15_predictions.json` | **yes — 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` + 35 settlements** |
| `16_monthly_review.md` | yes (not due) |
| `eligible_universe.txt`, `universe_summary.json` | yes |
| `technical_indicators.json` | yes (519 tickers incl. SPY/QQQ/SOXX/TLT) |
| `settlement_manifest.json` | yes |
| `run_computed_manifest.json` | yes (every table in this package is generated from it) |
| `price_verification.json`, `price_history_fetch_manifest.json` | yes |
| `earnings_calendar_manifest.json`, `market_cap_eligibility_manifest.json` | yes |
| `sector_manifest.json`, `regime_data_manifest.json` | yes |
| **Core ETF Market Forecast Block** | **present** — SPY / QQQ / SOXX in `03`, three `MARKET_FORECAST` records in `15` |

## Outstanding Blockers

1. `Fund_Z` / `Sent_Z` remain `UNAVAILABLE` at universe scale — Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` is still not attempted. This is the
   single change that would make a `GO` structurally reachable.
2. `eff_n = 1` gates every Track A calibration proposal. **This run establishes when that
   gate opens — see `13`.**
3. `MARKET_FORECAST` calibration remains broken (20.83% hit rate over n=48); the
   `mu = beta × SPY_mu` formula is applied unmodified and its defect disclosed in `03` and `13`.
