# 13 — Evolution Log · 2026-08-28 *(backfilled)*

> **BACKFILLED 2026-09-03** — the 2026-08-28 scheduled run wrote `01`-`07` and `15_predictions.json`
> and then truncated before publishing this artifact. It is reconstructed here from that package's
> **own committed data** (`01`-`07`, `15_predictions.json`) by the 2026-09-03 run. No analytical content
> is invented: anything the truncated run never persisted is marked `UNAVAILABLE` rather than
> recomputed from a different basis. No prediction record was added, altered, or removed.

## Run context

| Field | Value |
|---|---|
| Run date / model | 2026-08-28 · `claude-opus-5` · post-close fire 22:08 ET |
| Status | `NO_TRADE` |
| Regime | `BULL` |
| Ledger status — EQUITY_ALPHA | raw n 1355, eff_n 2, hit 37.49%, CI 71.88%, mean z -0.5553 |
| Ledger status — MARKET_FORECAST | raw n 201, eff_n 2, hit 40.11%, CI 90.55%, mean z -0.1848 |
| Track A gate | `INSUFFICIENT_EFFECTIVE_N` for both record types |
| Baseline flag | see `02` |

## Decision: `NO_CHANGE_ACCEPTED`

A reconstructed artifact cannot satisfy the required evolution workflow
(`rules.md § Required Evolution Workflow`): Observe -> Diagnose -> Hypothesize -> **Test** ->
Decide. The Test step needs a holdout or rolling-validation slice evaluated *at the time of the
run*, and this log is written 6 days
later from a different vantage point. Proposing a change here would be manufacturing an evolution
pass that never happened. `NO_CHANGE_ACCEPTED` is the honest record.

## Observations preserved from the package's own artifacts

1. **The symbol-reuse price gate accepted 2026-08-27 was applied for the first time on this run**
   (`01` states it explicitly). It is the earliest live application of that Track B.
2. **The beta band was feasible** (max attainable +1.1177, `07` Task 0) after two consecutive
   infeasible runs — evidence that the feasibility narrative must be recomputed every run.
3. **`settlements: []` was correct, not an omission.** No prediction in the corpus carried
   `target_date == 2026-08-28`; the package says so and cites
   `rules.md § Canonical Settlement Ledger` item 5.
4. **The `eff_n` projection recorded here** — `EQUITY_ALPHA` incrementing on
   2026-09-03 with
   24 pending — **was confirmed on that
   date** by the 2026-09-03 run, which observed eff_n move to 3.

## Root cause of the truncation

The 2026-08-28 session stopped after writing `15_predictions.json`. The package's `01` states that every
fact used downstream by "`02`-`09`, `13`, `14`" appears in its ledger, which was true of the
artifacts that were written and an over-claim for `08`, `09`, `13` and `14`, which were not. This
is the same pre-composition failure mode recorded for the 2026-08-06, 2026-08-07 and 2026-08-14
packages: **forward references to artifacts are composed before those artifacts exist.** The
2026-09-03 run's `00` is composed after the fact by listing the package directory, which is the
mitigation.

## Deliberately not backfilled

| Artifact | Reason |
|---|---|
| `10_midday_monitor.md` | an observation artifact for a moment that was never observed — writing one would be fabrication |
| `11_preclose_check.md` | same |
| `12_close_log.md` | same |
| `14_weekly_review.md` | 2026-08-28 was a Friday and owed one, but its census would be taken from the 2026-09-03 vantage point and would silently include packages that did not exist on 2026-08-28 |
