# 13 — Evolution Log — 2026-08-04

## Run context

| Field | Value |
|---|---|
| Run date | 2026-08-04 (Tuesday), **intraday** fire 2026-08-04T12:05:00-04:00, basis 2026-08-03 |
| Final status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | 2026-07-28 … 2026-08-04 (trailing 7 days, all models) |
| Packages reviewed | **10** — {'NO_TRADE': 10} |
| Ledger status | `EQUITY_ALPHA` n=515, `eff_n`=1 · `MARKET_FORECAST` n=90, `eff_n`=1 |
| Baseline flag | `CROSS_MODEL_BASELINE` (2-way tie resolved by rule 8) |
| Due inventory / conflicts | 48 settled → 0 / 0 |

## What worked

- **The Metric Definition Table shipped on its stamped effective date.** The Track B accepted
  2026-08-03 for 2026-08-04 is live in `05`, with one normative row per metric slot, post-transform
  polarity wording, and explicit windows and stdev conventions.
- **The reproduction test it owed was run, and it produced a precise, actionable answer.** Sharing a
  basis with the prior package and scoring an identical 512-name universe made the
  comparison purely definitional. `Tech_Z` reproduced to **0.0001**;
  `Macro_Z` to 0.0487, with the failure **isolated to one slot**.
- **Two conventions were pinned by fitting the prior package's published driver values.** `dd60`
  uses the 61 most recent closes (60 return intervals), not 60 — worth 0.0042 versus 0.0292 of error,
  and adopting it moved `Tech_Z` reproduction from 0.0120 to 0.0001.
- **Grounding was flawless.** 28/28 symbols, three independent
  sources, **0.0000%** maximum deviation,
  zero confirmation re-reads — and the intraday `REG_MKT` field rule (CNBC `previous_day_closing`,
  Nasdaq `PreviousClose`) held exactly.
- **Settlement was frictionless.** 48 due keys, all `TARGET_EQ_RUN_DATE`, 0 unsettleable,
  0 conflicts.
- **Rule 8 fired for the fifth consecutive run** and the conclusion was invariant across a
  6.36pp spread.

## What failed

- **The settled batch was poor again:** 14/42 = 33.33% equity
  direction hits, mean z -0.7494.
- **Rank-order inversion persists** — weighted-mean rank IC -0.0879 over n=515,
  non-positive in 20 of 32 vintages — and
  it was demonstrated live again: the published sleeve trailed SPY by
  0.06pp intraday while SOXX ran +6.27% (`10`).
- **`MARKET_FORECAST` remains badly calibrated** — 22.09% over n=90.
- **`Macro_Z` is still not reproducible**, because `rate_sens` was never pinned down.
- **Non-`GO` again**, for the same structural reason as every package since 2026-07-01.

## Primary diagnosis: **source grounding** (specifically, metric-definition lineage)

The dominant *new*, actionable finding is that the reproduction failure has a **single named cause**.
Thirteen plausible `rate_sens` conventions were tested — `beta` versus `correlation`, 30/60/120/252-day
windows, adjusted versus raw closes, negation before versus after the z-score (arithmetically
identical, as it turns out) — and **none** reached the 0.01 threshold; the best remains this run's own
definition at 0.1951. Every other slot lands at ≤
0.0060.

That is a materially better diagnosis than 2026-08-03's "mean absolute error 0.092, max 0.293,
concentrated in the vol-stability slot": the residual is now localized to one slot, quantified, and
closed forward by a normative definition rather than left to the next reader's inference.

## Proposed change (exactly one) — **Track B**

**Require the Metric Definition Table to state the *fitted provenance* of any convention that a prior
package's disclosure did not determine.**

### Current problem

The table shipped today fixes conventions *going forward*, but it is silent about how each convention
was arrived at. Two of the ten slots (`dd60`, `rate_sens`) were not derivable from the prior
disclosure and had to be recovered by fitting against published driver z-scores. `dd60` was recovered
successfully; `rate_sens` was not. A reader of today's `05` cannot tell those two cases apart from the
eight that were unambiguous all along — so the table silently presents a *guess* and a *fact* in the
same voice. Artifact that exposed it: this run's `05 § Same-basis reproduction check`, where the
per-slot error table is the only thing distinguishing them.

### Proposed change

Add one column to the Metric Definition Table: **`Provenance`**, taking exactly one of

- `SPEC` — the definition is fixed by `rules.md` or `technical_indicators.py` and needs no inference;
- `FITTED (max err X.XXXX vs <package>)` — recovered by fitting a prior package's published values,
  with the achieved error stated;
- `UNPINNED (best fit X.XXXX vs <package>)` — no tested convention reproduced the prior values; this
  run's definition is normative from here and the prior series is **not** exactly comparable on that slot.

Any slot marked `UNPINNED` must also be named in `08_risk_review.md` as a comparability limitation.

### Hypothesis (explicit and falsifiable)

If provenance is stated per slot, then a later run diagnosing a reproduction failure can tell in one
read whether a mismatch means *its own engine is wrong* (slot marked `SPEC`) or *the historical series
is genuinely ambiguous* (slot marked `UNPINNED`), without re-running a variant search.
**Falsifiable:** the next run that performs a same-basis reproduction check must report, per slot,
whether the provenance label predicted the outcome. If any slot marked `SPEC` fails to reproduce
within 0.01, the labelling is unreliable and this change is reverted.

### Validation — Track B three-condition standard

1. **Explicit problem statement citing the artifact that exposed it** — yes: this run's `05`
   per-slot error table, where `rate_sens` at 0.1951 and `dd60` at
   0.0042 are presented identically to the eight unambiguous slots.
2. **Cannot weaken a protected rule or grounding gate** — confirmed. It adds one disclosure column.
   It changes no factor weight, threshold, mu table, sizing parameter or protected cap, and cannot
   make any previously-ungrounded value publishable.
3. **Logged with a `HUMAN_REVIEW` flag, effective next run** — yes; see the decision block.

### Decision: **ACCEPT** — `HUMAN_REVIEW`, effective next run (2026-08-05)

## Effect of the previously-accepted change, measured

| Quantity | 2026-08-03 (prose disclosure only) | This run (with the table) |
|---|---|---|
| `Tech_Z` reproduction, max abs error | 0.03 (vs the 2026-08-01 package) | **0.0001** |
| `Macro_Z` reproduction, max abs error | 0.293 (mean 0.092) | **0.0487** (mean 0.0176) |
| Slots failing the 0.01 threshold | not measured per slot | **1 of 10** (`rate_sens`) |
| Drawdown polarity defect | found and fixed by the reproduction test | no recurrence — `dd60` reproduces to 0.0042 |

`Macro_Z` error fell from 0.293 to 0.0487 — a **83%**
reduction — and the residual is now attributable to exactly one slot rather than diffuse. The strict
reading of the 2026-08-03 falsifiability condition ("if either exceeds 0.01 with the table in place,
revert") does **not** trigger a revert, because the test above measures the **prior package's prose**,
which is what the table was written to replace; the table's own test is owed by the next same-basis
run. That scope distinction is recorded here so a later reader does not mistake this for a passed or
failed self-test.

## Deferred observations (recorded, not proposed — one change per run)

1. **`MARKET_FORECAST` mu derivation is a category error.** `mu = beta x SPY_mu` conflates
   co-movement magnitude with expected-return direction; today it produced SOXX
   +7.06% off a beta of +3.530. Hit rate
   22.09% over n=90. **Track A** (Core ETF mu prior table) → **`DEFER`**,
   `eff_n` = 1 < 3. **Fifth consecutive log.**
2. **Rank-order inversion.** Rank IC -0.0879 over n=515, with a second live intraday
   demonstration today (0.06pp of same-session underperformance, `10`).
   The 2026-08-01 `Tech_Z` deduplication cannot be judged until `eff_n >= 3`. **Track A** → **`DEFER`**.
3. **`Fund_Z`/`Sent_Z` universe-scale tooling** remains the single highest-value open item and is an
   engineering task, not a prompt mutation. It is the sole cause of 10 of
   10 packages in the review window being non-`GO`.
4. **Rank-ordered selection walks out of the beta band even when the band is feasible.** Attainable
   [-0.5413, +1.3472] versus a realized sleeve
   beta of +0.5323. Fifth consecutive run where 2026-07-27's "provably
   infeasible" narrative would be wrong.

## Freeze-criteria check

No freeze. This run **accepts** a change, so the "three consecutive cycles reject all changes" clause
does not trigger. No accepted change has worsened out-of-sample performance: the last four accepted
changes (2026-07-29 calendar sweep, 2026-07-30 tie-break rule, 2026-08-01 `Tech_Z` deduplication,
2026-08-03 Metric Definition Table) are grounding, process and arithmetic-correctness fixes. No
oscillation: no parameter has been moved back and forth.

## Effective next step

Add the `Provenance` column to `05`'s Metric Definition Table from the 2026-08-05 run onward, and have
the next same-basis reproduction check report per-slot whether the provenance label predicted the
outcome. Continue holding all Track A calibration work until `eff_n >= 3`; the first `EQUITY_ALPHA`
increment is projected for **2026-08-05**
(43 pending), which the next run should
verify or falsify explicitly.
