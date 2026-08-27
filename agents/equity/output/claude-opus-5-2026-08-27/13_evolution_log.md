# 13 — Evolution Log · 2026-08-27

## Run context

| Field | Value |
|---|---|
| Run date | 2026-08-27 |
| Model | `claude-opus-5` |
| Fire window | post-close, 19:09 ET |
| Final status | `NO_TRADE` |
| Regime | `BULL` |
| Data mode | `DELAYED` |
| Evaluation window (mandatory 7 calendar days, all models) | 2026-08-20 … 2026-08-27 |
| Packages in window | 1 prior (`claude-opus-5-2026-08-22`) plus this run — see the census note below |
| Ledger status — `EQUITY_ALPHA` | raw n 1355, `eff_n` 2, hit 37.49%, CI 71.88%, mean z -0.5553 |
| Ledger status — `MARKET_FORECAST` | raw n 201, `eff_n` 2, hit 40.11%, CI 90.55%, mean z -0.1848 |
| Track A calibration gate | **not satisfied** — needs raw n >= 20 **and** `eff_n` >= 3; `eff_n` is 2 (EQ) / 2 (MF) |
| MoM baseline flag | `NONE (same-model folder at delta 0d)` — `claude-opus-5-2026-07-30`, delta 0d, tie resolved by rule 8(a) |

### Review-window census

The mandatory review window is the trailing 7 calendar days across **all** models. Only one prior
dated package falls inside it: `claude-opus-5-2026-08-22`. Trading days **2026-08-24, 2026-08-25, 2026-08-26 have
no package from any model**, extending the scheduler-reliability gap first recorded on 2026-08-22
(which found 2026-08-11 … 2026-08-21 empty). Counting only completed days — that is, excluding
2026-08-27 itself, which this package fills — **12 of the 18 trading days from 2026-08-03 to 2026-08-26 have no
package from any model** (2026-08-05, 2026-08-11, 2026-08-12, 2026-08-13, 2026-08-17, 2026-08-18, 2026-08-19, 2026-08-20, 2026-08-21, 2026-08-24, 2026-08-25, 2026-08-26). It is a scheduling-infrastructure problem, not a prompt-system problem, and it is recorded
here rather than converted into a prompt change: `runbook.md § Scheduler` already documents both
promotion paths (launchd plist, GitHub Actions cron) and neither is implemented.

The working tree carried no orphaned uncommitted package this run (`git status` clean at fire), and
`settlement_ledger.py` found no canonical rows sourced from an uncommitted folder — so the
2026-08-22 orphan-commit test did not need to be applied.

## What worked

1. **Post-close remains the best fire window.** 518/519 symbols in
   10.7s, 515 last bars on the basis date, and same-day
   `TARGET_DATE_CLOSE` settlement available — 50 of the 231 due keys
   settled a day earlier than a pre-open fire would have allowed. `POST_MKT` field semantics held
   exactly as documented 2026-08-03.
2. **The corporate-action Track B accepted 2026-08-22 worked on its first live run.** It caught
   4 candidates, classified each against two
   independent references, correctly separated the one benign case (`FDXF`, vendor bar lag — present
   in the screener and live at CNBC) from the three real ones, and intersected the set with open
   prediction keys to report 2 `UNSETTLEABLE_CORPORATE_ACTION` rows instead of silently leaving them
   invisible.
3. **Settlement throughput.** 229 of 231 due keys settled, 0
   conflicts, and the post-write re-run shows `rejected_rows` unchanged at
   87 — this run's rows produced **zero** new validator rejections.
4. **Feasibility was recomputed, not inherited.** The beta band is infeasible today
   (+0.2919) after being feasible on four consecutive runs and infeasible on
   2026-08-22; neither narrative was assumed.

## What failed

1. **The score remains anti-predictive.** This run's settlement batch scored
   54/202 = 26.73% on alpha direction, and aggregate rank IC is
   -0.0840 across 60 vintages. Diagnosed, not fixable within Track B.
2. **Mean z drifted outside the healthy band** to -0.5553 (band -0.5…+0.5) — realized
   returns run about half a sigma below `mu`. CI coverage 71.88% is healthy,
   so this is a `mu`-prior problem, not a sigma problem.
3. **`MARKET_FORECAST` CI coverage is 90.55%**, above the 85% line that
   `rules.md § Rolling Calibration Metrics` calls "uninformatively wide — tighten".

All three are **Track A** and all three fail the `eff_n >= 3` gate. Per
`rules.md § Two-Track Change Classification`, the correct disposition is to record them as
observations and `DEFER`, which is done above; a Track A proposal is not made this run.

## Primary diagnosis

**Source grounding.** Not because grounding failed — 27/27
published prices were grounded on three independent sources at 0.095123%
max deviation — but because this run surfaced a *latent* way for the grounding gate to accept a wrong
price, and that is the one thing in scope for a bounded change today.

## Proposed change (exactly one)

### Problem statement

`EQR`'s US listing has been absorbed into `VMRK`. Queried today, CNBC returns a quote under the legacy
ticker `EQR` — but it is a **different company on a different continent**: `name` = "EQ Resources
Ltd", `exchange` = `ASX`, `last` = 0.41, `volume` = 0, with `last_time` = 2026-08-27 (L026). The current
CNBC grounding gate is a **date test only** (`last_time` date == basis). That test **accepts** this row.

Nothing in this package consumed that value: `EQR`'s bulk fetch transport-failed, the ticker was
rejected before scoring, and its two open prediction keys were left due. The protection came from the
*fetch failing*, not from the gate. Had stockanalysis returned any series for `EQR`, or had a future
run used CNBC as a settlement price source for a name in this state, the gate would have supplied
`0.41` as a US equity close — a ~99% price error on a name with open predictions.

The 2026-08-22 note that "CNBC still returns the price under the legacy ticker but with `name` = the
successor — that name field is the cheapest tell" is now **incomplete**: five days later the same
symbol resolves to an unrelated foreign issuer, so the name field no longer identifies a successor
and the price is no longer approximately right.

### Proposed change (Track B)

Strengthen the CNBC grounding gate from a date test to a **three-part identity test**. A CNBC row may
be used as a US equity/ETF price only when all three hold:

1. `last_time` date == the basis date (unchanged);
2. `exchange` is a U.S. venue — `NYSE`, `NASDAQ`, `NYSE Arca`, `NYSE American`, `BATS`, `CBOE`,
   `AMEX`, `NYSE MKT`, `OTC` (case-insensitive);
3. `volume` > 0.

A row failing (2) or (3) is `UNAVAILABLE` for pricing and is additionally recorded in the
corporate-action ledger as a new classification, **`SYMBOL_REUSE_FOREIGN_LISTING`**, alongside the
existing `CORPORATE_ACTION_RENAMED` / `CORPORATE_ACTION_DELISTED` / `TRANSIENT_FETCH_FAILURE` labels.

### Track classification

**Track B — process change** (missing-fetch procedure fix / grounding-gate correction). It changes no
scoring formula, factor weight, forecast prior, threshold, or protected risk limit. It *strengthens*
the Price Sourcing Standard rather than weakening it, satisfying acceptance condition (2).

### Hypothesis (explicit and falsifiable)

Adding the exchange and volume assertions rejects the symbol-reuse row while rejecting **zero**
legitimate published rows. Falsifiable: any run in which the strengthened gate rejects a price that
the three-source cross-check independently confirms within 1% refutes it and reverts the change.

### Validation

Both gates were run against live CNBC responses for all 24 published names, the three core
ETFs, and `EQR`, this run:

| Gate | Legitimate rows accepted | `EQR` symbol-reuse row | False rejects |
|---|---|---|---|
| Current (date only) | 27/27 | **accepted** (false accept — 0.41, ASX) | 0 |
| Proposed (date + US exchange + volume > 0) | 27/27 | **rejected** | **0** |

Retroactive scope was measured before proposing, per the 2026-08-07 lesson that validator changes
re-validate history: the gate governs *fetch-time acceptance*, not stored settlement rows, so no
canonical settlement is re-classified and no `15_predictions.json` value changes. The measured effect
on this run's package is **zero** — every published price is identical with and without the change.

### Decision

**`ACCEPT`** — Track B, flagged **`HUMAN_REVIEW`**, effective **2026-08-28** (next run) unless
reverted. One Track B change this run, per the policy limit.

### Effective next step

The next run implements the three-part gate in its price-verification pass and adds
`SYMBOL_REUSE_FOREIGN_LISTING` to the corporate-action classifier's label set. If any legitimate name
is rejected by it, revert and log the counterexample.

## Deferred findings (recorded, not proposed)

| Finding | Track | Gate that blocks it | Disposition |
|---|---|---|---|
| Aggregate rank IC -0.0840 over 60 vintages — the composite ordering is anti-correlated with forward alpha | A (factor weights / score construction) | `eff_n` 2 < 3 | **DEFER** |
| `EQUITY_ALPHA` mean z -0.5553, outside the -0.5…+0.5 band — the `mu` prior is too high for this regime | A (mu Calibration Table) | `eff_n` 2 < 3 | **DEFER** |
| `MARKET_FORECAST` CI coverage 90.55% > 85% — intervals uninformatively wide | A (Core ETF sigma / mu prior) | `eff_n` 2 < 3 | **DEFER** |
| `mu_ETF = beta x SPY_mu` is a category error (diagnosed 2026-07-24); a high-beta ETF cannot express a bearish view against a non-negative SPY prior | A (Core ETF mu prior table) | `eff_n` 2 < 3 | **DEFER** — unchanged since 2026-07-24 |
| 12 of the 18 completed trading days from 2026-08-03 to 2026-08-26 have no package from any model | neither — infrastructure | no wired scheduler | recorded; `runbook.md § Scheduler` already specifies the two promotion paths |

`rules.md § Freeze Criteria` check: this is **not** three consecutive cycles rejecting all changes —
a Track B change is accepted this run, and 2026-08-22 also accepted one. No freeze.

## `eff_n` projection (falsifiable, carried forward)

| Record type | Current `eff_n` | Projected to reach 3 | Pending predictions at that date | Window span |
|---|---|---|---|---|
| `EQUITY_ALPHA` | 2 | 2026-09-03 | 24 | 2026-07-08 … 2026-08-27 (50d) |
| `MARKET_FORECAST` | 2 | 2026-09-07 | 3 | 2026-07-12 … 2026-08-27 (46d) |

Adding 229 settlements moved raw `EQUITY_ALPHA` `n` from 1153 to 1355 while
`eff_n` held at 2 — the intended behaviour, since every new target date falls inside the window
already opened on 2026-08-05. This run's own
24 predictions target 2026-09-24, which is what opens the third window.
