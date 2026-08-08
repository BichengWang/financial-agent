# 00 — Run Manifest

| Field | Value |
|---|---|
| Run date | `2026-08-06` (Thursday) |
| Model | `claude-opus-5` |
| Fire window | **INTRADAY** — ~11:05 ET, ~1h35m after the open |
| Price basis | **2026-08-05** — the last completed close |
| Run mode | Scheduled daily run |
| Data mode | `DELAYED` |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-07-09` |
| Baseline flag | `CROSS_MODEL_BASELINE` |
| Universe | S&P 500 ∪ Nasdaq-100 index union, `INDEX_UNION_PCTL (n=511)` |

## Why the basis is 2026-08-05 and not the run date

The run fired intraday at ~11:05 ET, while the 2026-08-06 session was still open. At that
moment no vendor had published a 2026-08-06 daily bar: 518 of
519 symbols carried **2026-08-05** as their last bar. Every entry price,
technical indicator and settlement in this package therefore rests on one internally
consistent completed close. The single exception is documented under
`§ Universe rejections` below.

## Prediction settlement summary

| Field | Value |
|---|---|
| Due keys at `--as-of 2026-08-06` | 98 |
| Settled this run | **98** |
| Unsettled / deferred | 0 |
| Settlement price date | `2026-08-05` (last completed close) |
| `ORDINARY` (target_date 2026-08-05 < run date) | 49 |
| `TARGET_EQ_RUN_DATE` (target_date == run date, fired intraday) | 49 |
| Post-write ledger re-run | `due_inventory: 0`, `conflicts: 0` |

The due queue was unusually large (98 keys vs 48 on 2026-08-04) because
**no package exists for 2026-08-05 from any model** — see `§ Audit-trail gap`.

### Canonical rolling calibration

| Record type | raw `n` | 28-day `eff_n` | Hit rate | CI coverage | Mean z | Track A eligible? |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 643 | **2** | 39.04% | 69.36% | -0.5328 | False — `INSUFFICIENT_EFFECTIVE_N` |
| `MARKET_FORECAST` | 108 | 1 | 25.96% | 84.26% | -0.5285 | False — `INSUFFICIENT_EFFECTIVE_N` |

**`eff_n` for `EQUITY_ALPHA` moved 1 -> 2 this run.** The 2026-07-28 Track B change
predicted exactly this, and stamped it falsifiable: *"EQ eff_n -> 2 on 2026-08-05"*. The
settled windows are now `['2026-07-08', '2026-08-05']`. The prediction
held, so that change stands rather than being reverted. Track A remains gated
(`eff_n 2 < 3`); the next EQ window opens
`2026-09-02` with
24 predictions pending.

## GO-Gate Table — Required inputs

| Required input (`rules.md § Input Classification`) | Status | Evidence | Blocks GO? |
|---|---|---|---|
| 1. Grounded entry price | **PASS** | 27/27 published symbols grounded on 3 independent sources; max deviation 0.0000% | No |
| 2. ~60 trading days of history per name + SPY | **PASS** | 511 scored names with >=61 daily bars (median 1255 bars); SPY 1255 bars | No |
| 3. sigma via the Sigma Fallback Chain | **PASS** | REALIZED_VOL_30D computed for all 24 published names and 3 core ETFs | No |
| 4. Next earnings date | **PASS** | Full-universe forward calendar sweep: 27/27 business days, zero transport failures -> sweep complete; 92 CONFIRMED_CALENDAR, remainder NO_PRINT_IN_WINDOW | No |
| 5. Index-union universe from `build_index_universe.py` | **PASS** | 515 names (503 S&P 500, 101 Nasdaq-100, 89 overlap) | No |

**All five Required inputs are grounded.** `NO_TRADE` is therefore *not* a data-availability
outcome — it is an evidence-threshold outcome, decided below.

### Enhancing inputs (caps only, never GO blockers)

| Enhancing input | Status | Effect (never a GO blocker) |
|---|---|---|
| Options IV / skew | UNAVAILABLE | No IV30 sigma source; REALIZED_VOL_30D used instead |
| Short interest / borrow | UNAVAILABLE | `Sent_Z` family UNAVAILABLE |
| Bid-ask spread tape | UNAVAILABLE | Spread exclusion filter cannot be applied; disclosed |
| Analyst revision tape | UNAVAILABLE | `Sent_Z` family UNAVAILABLE |
| Institutional ownership flow | UNAVAILABLE | `Sent_Z` family UNAVAILABLE |
| Fundamental fetch path (XBRL at universe scale) | UNAVAILABLE | `Fund_Z` family UNAVAILABLE — Phase 2 of the plan is not implemented |

## Evidence thresholds — the actual decision

| # | Evidence threshold | Required | This run | Result |
|---|---|---|---|---|
| 1 | Adjusted-score percentile >= 80th | >= 80.00 | 103 names at or above the 80th pctl | **PASS** |
| 2 | At least 3 of 4 factor families non-negative | >= 3 of 4 | 2 of 4 families available (Tech, Macro); Fund_Z and Sent_Z UNAVAILABLE universe-wide and do not count toward the threshold | **FAIL — unsatisfiable** |
| 3 | No single family > 50% of total conviction | <= 50% | Tech_Z carries 0.30 of the 0.45 live weight = 66.67% | **FAIL — unsatisfiable** |
| 4 | Data completeness >= 85% | >= 85% | DQ multiplier 0.80 (notable coverage gaps: 2 of 4 families missing) | **FAIL** |
| 5 | No hard stop from `rules.md § Stop Criteria` | none triggered | No hard-halt criterion triggered | **PASS** |

Thresholds 2 and 3 are **arithmetically unsatisfiable** while `Fund_Z` and `Sent_Z` are
UNAVAILABLE universe-wide: with only two live families the maximum attainable count is 2,
and Technical necessarily carries 0.30/0.45 = 66.67% of live conviction. No name in any
universe can clear them today, so no name is investable and the run is `NO_TRADE`.

**This is not a feasibility failure.** The portfolio beta band is *feasible* this run
(attainable sleeve beta -0.2803 …
+1.4145 against the 0.90–1.10 band) — the fifth
consecutive run where the 2026-07-27 "provably infeasible" narrative would have been wrong.

## Audit-trail gap — 2026-08-05

`runbook.md § Cadence` requires that no day be skipped in the audit trail. **No package
exists for 2026-08-05 from any model.** This run cannot retroactively create one: doing so
would mean inventing a vintage whose predictions were never recorded at the time, which
`rules.md § Non-Fabrication Contract` forbids (the 2026-07-11 folder is the standing
precedent — backfill artifacts from committed data, never retroactive OPEN predictions).
The gap is reported here and in `13_evolution_log.md`. Its only measurable consequence is
the doubled settlement queue, which this run cleared in full.

## Universe rejections

| Ticker | Reason | Detail |
|---|---|---|
| `BF-B` | `MARKET_CAP_UNAVAILABLE` | vendor marketCap field empty |
| `EA` | `DELISTED_OR_HALTED` | last bar 2026-08-04 != basis 2026-08-05 |
| `FDXF` | `NO_HISTORY` | fetch or indicator pack unavailable |
| `Q` | `INDICATOR_INCOMPLETE` | 193 daily bars; weekly/daily MA or MACD UNAVAILABLE |

`EA` is a **delisting**, newly detected this run — see `01_preflight.md § Vendor identity
hazard` and `13_evolution_log.md`.

## Truncation and backfill (added 2026-08-07)

**This session truncated after writing `00`–`04` and `15_predictions.json`.** The artifact
checklist below originally reported `05`–`10` and `13` as "Published"; they did not exist on
disk. That was a false claim, and its cause is structural rather than incidental: the checklist
is composed before the artifacts are written, so any truncation leaves the manifest asserting
files that were never created.

The missing narrative artifacts were reconstructed on 2026-08-07 from this folder's own
committed data — `15_predictions.json` (which carries per-name family and slot z-scores, the
full metric pack, drivers and ledger rows) plus `00`–`04`. Each backfilled file carries a
`BACKFILLED 2026-08-07` banner. Figures the truncated session never persisted — the full
511-name z-score cross-section, the correlation matrix, portfolio sigma and the 95th-percentile
drawdown — are marked `UNAVAILABLE` rather than recomputed, because this run's basis was the
2026-08-05 close and substituting a later run's numbers would misstate what it actually saw.

`10_midday_monitor.md` is **not** backfilled: a midday monitor is an observation of a moment
that was never observed, and manufacturing one would be fabrication. It is now marked omitted.

No prediction record was created, altered or settled by the backfill. Every forecast this run
made was already durable in `15_predictions.json` before the truncation, so nothing was lost
from the prediction ledger — only the narrative layer.

## Artifact checklist

| Artifact | Status |
|---|---|
| `00_run_manifest.md` | Published |
| `01_preflight.md` | Published |
| `02_reflection.md` | Published |
| `03_regime_and_data.md` | Published |
| `04_universe_summary.md` | Published |
| `05_factor_scores.md` | **BACKFILLED 2026-08-07** *(was "Published" — see § Truncation)* |
| `06_top_candidates.md` | **BACKFILLED 2026-08-07** *(was "Published")* |
| `07_portfolio_proposal.md` | **BACKFILLED 2026-08-07** *(was "Published")* |
| `08_risk_review.md` | **BACKFILLED 2026-08-07** *(was "Published")* |
| `09_final_report.md` | **BACKFILLED 2026-08-07** *(was "Published")* |
| `10_midday_monitor.md` | **Omitted** *(was "Published")* — the checkpoint never ran and no midday observation exists to backfill |
| `13_evolution_log.md` | **BACKFILLED 2026-08-07** *(was "Published")* |
| `15_predictions.json` | Published |
| `11_preclose_check.md` | Omitted — checkpoint has not run (15:45 ET) |
| `12_close_log.md` | Omitted — checkpoint has not run (16:20 ET) |
| `14_weekly_review.md` | Not owed — Friday artifact; today is Thursday |
| `16_monthly_review.md` | Not owed — month-end artifact |

## Working-data checklist

| Working artifact (gitignored `.work/`) | Result | Detail |
|---|---|---|
| `eligible_universe.txt` / `universe_summary.json` | SUCCESS | 515 tickers; caches fetched_at 2026-06-21T21:05:56Z (S&P 500) and 2026-06-21T21:05:56Z (Nasdaq-100) |
| `stockanalysis_history_manifest.json` + `raw/` + `adj/` CSV trees | SUCCESS | 519/519 symbols, 0 failures, 946.8s elapsed |
| `technical_indicators.json` | SUCCESS | 519 symbols x daily/weekly/monthly blocks, computed on the adjusted-close tree |
| `earnings_sweep.json` | SUCCESS | 27/27 business days; sweep_complete=True |
| `price_verification.json` | SUCCESS | 27/27 grounded; 0 confirmation re-reads required |
| `run_computed_manifest.json` | SUCCESS | 511 scored, 4 rejected |
| `settlement_manifest.json` | SUCCESS | due_inventory 0, conflicts 0 |
| `settlements_this_run.json` | SUCCESS | 98/98 due keys settled, 0 unsettled |
| `nasdaq_screener.json` | SUCCESS | market cap + GICS-style sector for the universe (one call) |
| `VIX_History.csv` / `treasury_bills_2026.csv` | SUCCESS | VIX close 15.81; 13-week bank discount 3.74% |

## Core ETF Market Forecast Block

| ETF | Forecast produced? | mu | sigma | Confidence |
|---|---|---|---|---|
| SPY | Yes | +2.00% | 3.79% | MEDIUM |
| QQQ | Yes | +3.42% | 7.29% | MEDIUM |
| SOXX | Yes | +7.00% | 18.47% | MEDIUM |

Block produced in full — see `03_regime_and_data.md`.

## Agents executed

`Orchestrator (preflight + reflection)` -> `Data and Regime` -> `technical_indicators.py`
-> `Factor Scoring` -> `Portfolio Construction (Task 0 feasibility pre-check)` ->
`Risk Committee` -> `Evolution`.

State machine: `PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED ->
PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED` with final status **`NO_TRADE`**.

## Outstanding blockers

1. `Fund_Z` / `Sent_Z` UNAVAILABLE universe-wide — the single structural cause of every
   `NO_TRADE` in this series. Unblocking needs Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk `companyfacts.zip`
   + threaded Nasdaq sentiment fetch across all 511 names).
2. Track A calibration work stays gated at `eff_n = 2 < 3`.
3. No 2026-08-05 package exists in the audit trail.
