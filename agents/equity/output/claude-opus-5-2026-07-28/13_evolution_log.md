# 13 Evolution Log — 2026-07-28

## Run Context

| Field | Value |
|---|---|
| Run date / model | 2026-07-28 / `claude-opus-5` (pre-open, 08:05 ET) |
| Final status | `NO_TRADE` |
| Regime | `NEUTRAL` |
| Evaluation window | all dated packages from the trailing 7 calendar days, all models: 2026-07-21 → 2026-07-28 |
| Ledger status | `EQUITY_ALPHA` n=260, eff_n=1; `MARKET_FORECAST` n=48, eff_n=1 |
| Track A eligibility | **blocked: `INSUFFICIENT_EFFECTIVE_N`** |
| Baseline flag | `CROSS_MODEL_BASELINE` |
| Settled this run | 35 (29 EQ, 6 MF); conflicts 0; due after 0 |

## Cross-Model Review Window

| Package | Status | Notable |
|---|---|---|
| `gpt-5-2026-07-27` | NO_TRADE | Accepted a Track B refinement of the vendor-empty earnings signature, effective 2026-07-28 |
| `claude-opus-5-2026-07-27` | NO_TRADE | Monday intraday fire; accepted Track B earnings retry/convergence rules |
| `claude-opus-5-2026-07-26` | NO_TRADE | Accepted the adjusted-close return basis |
| `gpt-5-2026-07-24`, `claude-opus-5-2026-07-24` | NO_TRADE | Diagnosed the `mu = beta × SPY_mu` category error and the overlapping-cohort `eff_n` problem |
| **this run** | NO_TRADE | Eleven consecutive `NO_TRADE` runs across all models |

**Cross-model agreement is total and has been for eleven runs.** Two different model families,
independently implementing the same spec, reach `NO_TRADE` every day for the same structural reason:
`Fund_Z` and `Sent_Z` do not exist, so the evidence thresholds cannot be met. That consistency is
evidence the spec is being followed faithfully — and evidence that **no amount of further daily
iteration will change the outcome**, because the blocker is a missing data pipeline, not a parameter.

This run also **applied** the gpt-5-2026-07-27 Track B change on its effective date, as designed. It
changed nothing in the published set: no `ESTIMATED_PRINT_WEEK` name reclassified in the top-30.

## 1. Observe — forecast versus realized

| Observation | Value |
|---|---|
| Settled this run | 35 predictions, all `TARGET_EQ_RUN_DATE` at the 2026-07-27 close |
| `EQUITY_ALPHA` this batch | 14/29 direction, 23/29 IN_CI |
| `MARKET_FORECAST` this batch | **0/6 direction** |
| Rolling `EQUITY_ALPHA` | hit 50.77%, CI 74.62%, mean z -0.1973, rank IC -0.1715 |
| Rolling `MARKET_FORECAST` | hit 20.83%, CI 68.75%, mean z -0.6872 |
| MoM baseline | 7/14 alpha hits over 28 days |

## 2. Diagnose

The candidate miss categories, and why each is or is not the primary:

| Category | Verdict |
|---|---|
| Data quality | Not the primary. All five Required inputs grounded, 519/519 symbols fetched, 28/28 prices two-source grounded, zero earnings fetch errors. |
| Regime classification | Not the primary. `NEUTRAL` is well-evidenced and unchanged from the baseline. |
| Factor calibration | **A real defect** — rank IC -0.1715 and `MARKET_FORECAST` at 20.83%. But every fix is Track A, and Track A is gated at `eff_n = 1`. |
| Portfolio construction | Not the primary. The Task-0 pre-check worked; its result was marginal and is labelled as such. |
| Risk review | Not the primary. The committee caught and forced the correct framing of the knife-edge beta result. |
| Output clarity | Not the primary. |
| **Source grounding** | **Primary — but as an evidence-*adequacy* problem, not a grounding failure.** |

**The diagnosis.** For four consecutive runs the binding constraint on improving this system has not
been any measurement — it has been `eff_n = 1` blocking every Track A change. The 2026-07-27 package
escalated this as an open question for the 07-31 structural review, phrased as a worry: *if `eff_n` can
never rise under this cadence, the gate itself needs review, not the parameters.*

That worry is **false**, and this run proves it arithmetically. All 308
canonical settlements have target dates spanning **20 days**
(2026-07-08 → 2026-07-28) — *shorter than the
28-day window itself*. One window fits. `eff_n = 1` is not a pathology, a bug, or a sign of a broken
cadence: it is the arithmetic consequence of a system whose first settleable predictions all matured
inside a single three-week span. Raw `n` rose from 231 to 260 today and `eff_n` correctly did not move.

The real problem is that **`eff_n` was being reported as an opaque blocker rather than as a schedule**.
"INSUFFICIENT_EFFECTIVE_N" tells a reader that work is blocked but not whether it is blocked for a day
or forever — which is exactly why it got escalated to a structural review as a suspected design flaw.
The information needed to answer it was already in the ledger and simply was not computed.

## 3. Hypothesize — the proposed change

> **Add an `eff_n_projection` block to each record type's `rolling_metrics` in
> `settlement_ledger.py`, reporting the target-date span of the settled pool, the date the next
> non-overlapping window opens, the earliest outstanding prediction target date that reaches it, and
> how many predictions already carry that date.**

**Track B — process/schema change.** It adds a reported field. It changes no scoring formula, no factor
weight, no forecast prior, no mu table, no threshold and no protected risk limit. `eff_n` itself, and
the `n ≥ 20` / `eff_n ≥ 3` gate, are untouched: this reports *when* the gate opens, it does not open it.

**Hypothesis (falsifiable).** If the projection is correct, `EQUITY_ALPHA` `eff_n` will read 2 on
**2026-08-05** and `MARKET_FORECAST` `eff_n` will read 2 on **2026-08-09**.
Any run on or after those dates that still reports `eff_n = 1` for the corresponding record type
falsifies it.

This is not a forecast about markets. It is a statement about records that already exist:
43 `EQUITY_ALPHA` predictions already carry target date
2026-08-05, and 6 `MARKET_FORECAST` predictions
already carry 2026-08-09. The only way it fails is if those packages are deleted or
those settlements are rejected by the timing validator.

## 4. Test

Track B does not require a statistical holdout — there is no scoring math to validate. The acceptance
standard is the three-condition test, plus a correctness check on the emitted values.

**Implemented and executed this run.** `settlement_ledger.py` was re-run against the full output tree
after the change:

| Record type | n | eff_n | Span (days) | Next window opens | `eff_n` increments on | Pending at that date |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 260 | 1 | 20 | 2026-08-05 | **2026-08-05** | 43 |
| `MARKET_FORECAST` | 48 | 1 | 16 | 2026-08-09 | **2026-08-09** | 6 |

Correctness checks that passed:

1. **No regression.** Every pre-existing field is unchanged: n 260/48, eff_n
   1/1, hit rate, CI coverage, mean z, rank IC, conflicts
   0, due inventory 0 — all identical before and after.
2. **The two record types project different dates** (2026-08-05 vs
   2026-08-09), confirming the projection is computed per type against that type's own
   prediction inventory rather than pooled — which a pooled implementation would have hidden.
3. **Degenerate input handled**: an empty settled pool returns `eff_n: 0` with null dates rather than
   raising.
4. **Null when unreachable**: `eff_n` reaching 3 is correctly *not* projected, because no outstanding
   prediction yet carries a target date 28 days past 2026-08-05. The field reports what
   the inventory supports and does not extrapolate.

## 5. Decide

**`ACCEPT` — Track B, `HUMAN_REVIEW`, effective immediately (the change is already in
`settlement_ledger.py` and this run's `settlement_manifest.json` carries its output).**

Against the three-condition Track B standard:

1. **Explicit problem statement citing the artifact that exposed it** — satisfied: the 2026-07-27
   `13_evolution_log.md` escalated `eff_n` as a suspected design flaw for the 07-31 structural review,
   and today's `settlement_manifest.json` contains the 20-day span
   that answers it.
2. **Cannot weaken a protected rule or grounding gate** — satisfied: it adds a reported field and
   changes no gate, threshold, weight or limit. The Track A gate still requires `n ≥ 20` **and**
   `eff_n ≥ 3`, unchanged.
3. **Logged with `HUMAN_REVIEW`, takes effect unless reverted** — satisfied by this entry.

One Track B change this run, per the limit.

### What was considered and NOT proposed

- **Changing the `MARKET_FORECAST` mu formula.** The highest-value change available
  (20.83% hit rate, n=48, and all 6 of today's ETF settlements MISS), with the
  mechanism understood: `beta × SPY_mu` scales a magnitude by a direction, and today SOXX drew the
  block's *most bullish* mu (+1.82%) while sitting -21.19%
  below its 60-day high with rising vol. It is squarely Track A and `eff_n = 1` <
  3 ⇒ **`DEFER`, not `REJECT`**, per `rules.md § Rolling Calibration Metrics`. The projection accepted
  above now dates that deferral: draft it now, apply it when the third window opens in early September.
- **A discretionary ±1.5pp adjustment to the SOXX mu.** Rejected on the merits, not just on
  authority: even the full band leaves +0.32%, still non-negative. The band is
  structurally too narrow to express the view, which is itself part of the Track A evidence and should
  be preserved, not papered over.
- **A mu shrink or sigma widen for the equity book.** Retired on 2026-07-26 and it stays retired: CI
  coverage 74.62% and mean z -0.1973 are both healthy, so magnitude is not the
  failure. The failure is rank-order inversion, and a monotonic transform cannot fix an ordering.
- **Specifying a MoM baseline tie-break rule.** A genuine gap found today — two folders landed on the
  exact target date with materially different contents (81
  field differences across 13 shared keys), and
  `agents.md § Orchestrator Step 2` gives no tie-break. Handled this run by computing **both** and
  showing the conclusion is invariant. Held back only because of the one-Track-B-per-run limit; it is
  the natural candidate for the next run.

## 6. Log

| Field | Value |
|---|---|
| Current problem | `eff_n = 1` blocks every Track A calibration change, and was reported as an opaque blocker — escalated on 2026-07-27 as a suspected design flaw needing structural review |
| Proposed change | Emit an `eff_n_projection` block per record type in `settlement_ledger.py` rolling metrics: settled-pool target-date span, next window open date, first qualifying outstanding target date, and pending count |
| Classification | **Track B** (process/schema; no scoring math) |
| Validation method | Implemented and re-run against the full output tree; no-regression check on all pre-existing fields, per-type divergence check, degenerate-input check, unreachable-projection check |
| Result | `EQUITY_ALPHA` eff_n → 2 on **2026-08-05** (43 pending); `MARKET_FORECAST` eff_n → 2 on **2026-08-09** (6 pending); all prior fields unchanged |
| Decision | **`ACCEPT`**, Track B, `HUMAN_REVIEW` |
| Effective | immediately — already applied in this run's `settlement_manifest.json` |

### Effective next step

1. **2026-08-05** — verify `EQUITY_ALPHA` `eff_n` reads 2. If it does not, this change
   is falsified and must be reverted.
2. **2026-07-31 structural review** — close the `eff_n` agenda item rather than reviewing it; the gate
   is a startup transient with a known schedule.
3. **Early September** — the third window opens and Track A becomes eligible. The `MARKET_FORECAST` mu
   formula is first in the queue; draft it in the interim.
4. **Unchanged and still the top priority:** Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (universe-scale `Fund_Z` / `Sent_Z`).
   Eleven consecutive `NO_TRADE` runs across two model families have the same root cause, and no
   calibration change reachable through the evolution loop can address it.
