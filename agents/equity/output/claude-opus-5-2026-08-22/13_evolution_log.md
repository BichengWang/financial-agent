# 13 — Evolution Log · 2026-08-22

## Run context

| Field | Value |
|---|---|
| Run date | 2026-08-22 (Saturday; basis = Friday 2026-08-21 close) |
| Final status | `NO_TRADE` |
| Regime | `BULL` (prior baseline `NEUTRAL`) |
| Evaluation window | trailing 7 calendar days, all models — 2026-08-15 … 2026-08-22 |
| Ledger status | `EQUITY_ALPHA` n=1,153, eff_n=2; `MARKET_FORECAST` n=174, eff_n=2 |
| Track A gate | **blocked** — INSUFFICIENT_EFFECTIVE_N (needs n>=20 **and** eff_n>=3) |
| Baseline flag | none — same-model folder in-window at delta 1d; 2-way tie resolved by rule 8(c) |
| Settlements this run | 227 (due_inventory now 0, conflicts 0) |

### Review-window census (trailing 7 days, all models)

| Package | Model | Date | Run status | 15_predictions.json |
|---|---|---|---|---|
| claude-opus-5-2026-08-22 | claude-opus-5 | 2026-08-22 | UNAVAILABLE | yes |

The window is unusually thin. The last committed package before this run is dated **2026-08-10**,
and a complete-but-uncommitted `claude-opus-5-2026-08-14` package exists in the working tree (it is
being committed alongside this run with a backfilled `13`). Trading days 2026-08-11 through
2026-08-21 have no package at all. That gap is recorded here as an observation about scheduler
reliability; it is not something this run can repair, because reconstructing market analysis for a
date from a different price basis would be fabrication.

## What worked

- **Grounding was the cleanest of the series.** 27/27 published symbols
  agreed across stockanalysis + CNBC + Nasdaq at **0.000000%** maximum deviation,
  with zero confirmation re-reads and zero ex-dividend `c != a` artifacts on the basis bar. The bulk
  history fetch returned 518/519 symbols in
  14.1s.
- **The complete forward earnings sweep grounded the whole universe** in
  26 requests with zero transport failures, so the
  published set is contiguous ranks 1–24 with no "skip ungrounded names" rule needed.
- **Settlement was total.** All 227 due keys settled under `ORDINARY`
  timing at their own target-date closes; the post-write re-run confirms
  `due_inventory: 0`, `conflicts: 0`.
- **A falsifiable prediction from 2026-07-28 came true.** That package projected `EQ eff_n` would
  increment on 2026-08-05; `eff_n` is now **2** for both record types. The startup-transient
  diagnosis is confirmed and the "the gate itself needs review" escalation stays closed.
- **Feasibility was recomputed, not inherited** — and this time it genuinely failed, which is the
  point of recomputing it.

## What failed

- **Hit rate stays below 50%** (39.38% over 1,153 settled) and mean z
  (-0.5506) sits just outside the healthy floor: the mu prior is modestly too aggressive.
- **`MARKET_FORECAST` CI coverage is 90.23%**, above the 85% ceiling — those
  intervals are uninformatively wide.
- **Rank-order inversion persists** in aggregate (mean vintage rank IC -0.0840 across
  60 vintages, 33 at or below zero).
- **A universe constituent stopped trading with OPEN predictions against it**, and nothing in the
  system detected it as a class — see the diagnosis below.

## Primary diagnosis

**Source grounding.** Not factor calibration: the two calibration findings above are real, but both
are Track A and both are gated at `eff_n = 2 < 3`, so neither can be acted on this run. The
actionable defect is that the system has no procedure for a universe constituent that ceases to
trade under its own symbol — a grounding-lineage gap that silently corrupts due inventory, which is
the very measure that gates all Track A evolution.

## Proposed change (exactly one)

**Track B — process change.** Add a named **dead-constituent / corporate-action screen** to the
Data & Regime stage, with a standard rejection taxonomy and a mandatory cross-check against the open
prediction ledger.

### Problem statement, citing the artifact that exposed it

This run's rejection log (`04 § Inclusion / exclusion log`, ledger row `L025`) contains three names
that stopped trading under their own symbols while still sitting in the constituent caches:
`EQR` (renamed into / absorbed by `VMRK`, Vivmark Residential), `AVB` (last bar 2026-08-14), and
`EA` (last bar 2026-08-04). The engine caught all three, but only **incidentally** — as an HTTP 400
and two stale-last-bar checks — and `rules.md` names the condition ("names with unresolved corporate
action ambiguity") without giving any procedure for detecting it.

The consequence is not hypothetical. **Two OPEN predictions reference `EQR`** —
`claude-opus-5-2026-07-26` (target 2026-08-23) and `gpt-5-2026-07-27` (target 2026-08-24) — and both
come due within two days of this run with no settleable price. `rules.md § Canonical Settlement
Ledger` item 5 already prescribes the correct *handling* (report the key as due, never loosen the
validator to make it fit), but nothing surfaces *why*, so the next run meets it as an unexplained
anomaly and the keys sit in due inventory indefinitely. Due inventory feeds `eff_n`, which gates
every Track A change in the system.

### Proposed change, precisely

1. **Detection.** After the bulk history fetch, classify every universe symbol whose last bar
   predates the basis date, or whose fetch returned a transport-level rejection, against two
   independent references (the Nasdaq screener and one quote vendor). Emit one of:
   `CORPORATE_ACTION_RENAMED` (successor symbol found), `CORPORATE_ACTION_DELISTED` (no successor
   found), or `TRANSIENT_FETCH_FAILURE` (name still quotes normally — retry, do not reject).
2. **Disclosure.** Every such name gets a `04` rejection-log row and an `01` ledger row recording the
   evidence for the classification, including the successor symbol where one exists.
3. **Prediction cross-check (the part that matters).** Intersect the classified set with all OPEN
   prediction keys. Any match is reported in `02 § 0` as `UNSETTLEABLE_CORPORATE_ACTION` with its
   vintage, target date, and successor symbol, and is flagged for human reconciliation.
4. **Explicit non-goal.** The run must **not** infer an exchange ratio or settle a prediction against
   a successor symbol. Where the ratio is unknown, the key stays due and unsettled.

### Hypothesis

Naming the condition and cross-checking it against open predictions converts a silent, recurring
corruption of due inventory into a visible, human-actionable item, at zero risk to any scoring
output. It is falsifiable: **if the next run does not surface the two `EQR` keys with a named
`UNSETTLEABLE_CORPORATE_ACTION` reason, the change did not work.**

### Validation (Track B standard, three conditions)

| Condition | Assessment |
|---|---|
| 1. Explicit problem statement citing the artifact that exposed it | **Met** — `04 § Inclusion / exclusion log`, ledger `L025`, and the two named OPEN `EQR` prediction keys. |
| 2. Cannot weaken a protected rule or any grounding gate | **Met** — it adds a rejection reason and a disclosure step. It strengthens the grounding gate (an unresolvable name is `UNAVAILABLE` and excluded, never estimated) and explicitly forbids inferring an exchange ratio. No scoring formula, factor weight, forecast prior, or risk limit is touched. |
| 3. Logged with a `HUMAN_REVIEW` flag, effective next run unless reverted | **Met** — flagged below. |

Track B does not require settled observations or a statistical holdout, and correctly so: there is
no scoring math here to validate.

### Decision

**`ACCEPT`** — Track B, `HUMAN_REVIEW`, **effective 2026-08-23** (the next run).

Limit respected: this is the only change proposed this run.

## Deferred findings (not proposed — Track A gate)

Both are recorded as observations rather than rejected, per `rules.md § Rolling Calibration Metrics`
("if either gate fails, record the finding as an observation and `DEFER`").

| Finding | Evidence | Track | Disposition |
|---|---|---|---|
| `MARKET_FORECAST` intervals are too wide | CI coverage 90.23% > the 85% ceiling over n=174 | A (sigma sourcing) | **DEFER** — eff_n 2 < 3; gate projected 2026-09-07 |
| `EQUITY_ALPHA` mu prior is modestly too aggressive | mean z -0.5506 (healthy floor −0.5), hit rate 39.38% over n=1,153 | A (mu Calibration Table) | **DEFER** — eff_n 2 < 3; gate projected 2026-09-03 |

A third standing observation is explicitly **not** re-proposed: the rank-order inversion cannot be
fixed by a mu shrink or a sigma widen, because both are monotonic transforms and an inversion is a
rank-order property. That proposal was retired on 2026-07-26 and stays retired.

## Effective next step

The accepted Track B change takes effect on the next run (2026-08-23 or the next scheduled fire).
Its falsification test is concrete: the next run must surface the two OPEN `EQR` keys with a named
`UNSETTLEABLE_CORPORATE_ACTION` reason in `02 § 0`. If it does not, revert.

Standing watch items for that run, carried forward:

- `EQUITY_ALPHA` eff_n projected to reach 3 on **2026-09-03**
  (24 pending), unblocking Track A
  calibration work on the two deferred findings above.
- The constituent caches are
  62
  days stale. A refresh is maintenance, not an evolution change, but it is the upstream cause of the
  defect fixed here.
