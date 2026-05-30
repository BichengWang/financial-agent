# 13 Evolution Log

## Run Context

| Field | Value |
|---|---|
| Date | 2026-05-29 (Friday) |
| Day-of-week role | Friday — weekly-review cadence per `daily_schedule.md` §Weekly And Monthly Cadence |
| Run status | `REVIEW_ONLY` |
| Regime | `NEUTRAL` with `HIGH_VOL` tilt (reference-state) |
| Evaluation window | None — no realized observations available; closed-observation count remains < 20 |
| Model | claude-opus-4-7 |

## What Worked

- Loop ran end-to-end against reference-state inputs; no agent returned an empty artifact.
- The 05-24 `ILLUSTRATIVE_MODE` Operating Procedure (committed in the prior run) held up: every numeric field was tagged `ILLUSTRATIVE_REF` or `N/A` per the structural-cadence vs intra-day-live split.
- The 14-day earnings policy fired correctly through the 19-day buffered window: AVGO at ~7d was dropped at the carry-forward stage (`02_reflection.md` §5) and the factor scoring agent reflected the DROP in the investable subset (not just the portfolio agent).
- The reflection stage produced a standalone `02_reflection.md` artifact with the mandatory schemas from `main.md` §Reflection Required Sections.
- Risk committee correctly preserved the 5% single-name cap as a spec tension (escalated) rather than as a sizing fix to relax.

## What Failed (None Today; No Autonomous Mutation)

No agent failure. No silent disable. No fabricated input. The only "failure-like" surface is the documented spec tension between `main.md` and `daily_output_spec.md`, which is a documentation issue not an agent-loop issue.

## Primary Diagnosis

**Output clarity (documentation tension).** Two specs disagree on file count and on whether the reflection is standalone or embedded:

- `main.md` v3.0 mandates a 14-file layout with `02_reflection.md` standalone (added when the Reflection Stage was made a first-class concept).
- `daily_output_spec.md` still describes a 13-file layout with the reflection embedded inside `00_run_manifest.md` and `08_final_report.md`.

The 05-12 and 05-24 runs followed the 13-file layout; the 2026-05-29 gpt-5 run (already in `investments/equity/output/`) and today's claude-opus-4-7 run follow the 14-file layout because today's cron prompt explicitly directs execution of `main.md`. Both layouts are coherent; the inconsistency is the problem.

## Proposed Change (For Monthly Review, Not Autonomous Adoption)

**Reconcile `daily_output_spec.md` with `main.md` v3.0.** Two consistent paths:

- **Option A** (preferred): Update `daily_output_spec.md` to the 14-file layout, hoisting `02_reflection.md` to standalone and renumbering downstream files (`02_regime_and_data.md` → `03_regime_and_data.md`, etc., through `12_evolution_log.md` → `13_evolution_log.md`). This matches the implementation in `main.md`, the orchestrator prompt, and today's gpt-5 run.
- **Option B**: Revert `main.md` to embed reflection in `00`/`08` per the original 13-file spec. Less work but loses the standalone-reflection benefit of an audit-friendly artifact.

Either change touches the **output schema** (Allowed Mutation Scope item 2 of `evolution_policy.md`). It is allowed scope but warrants human review at the next monthly structural pass because downstream tooling (if any) keys on file count and numbering.

## Hypothesis

Updating `daily_output_spec.md` to the 14-file layout (Option A) reduces audit-trail ambiguity without changing the methodology. Falsifiable check: after the next monthly review, every model's run (claude / gpt-5 / future) emits exactly 14 files; today's gap (claude-opus-4-7 runs 05-12 and 05-24 followed 13-file; 05-29 follows 14-file) does not recur.

## Validation Method

| Check | Result |
|---|---|
| Holdout window used | None — documentation reconciliation does not affect ranking logic |
| IR / hit-rate / DD / turnover delta | `N/A` — schema-only |
| Schema integrity post-merge | Pending monthly review |
| Protected-rule check | Pass — no protected rule touched |
| Non-fabrication contract | Pass |

## Decision

`NO_CHANGE_ACCEPTED` for autonomous adoption today.

- **Spec reconciliation** (above): **`DEFER`** to next monthly structural review.
- **All scoring thresholds / family weights**: **`NO_CHANGE_ACCEPTED`** (closed-observation count < 20 per `stop_criteria.md` §Self-Evolution Stop Criteria item 1).
- **5% single-name cap tension**: **`DEFER`** to monthly structural review (carry-forward from 05-24 evolution log; humans-only per `evolution_policy.md` §Protected Rules).
- **Forward guard from 05-24** (empty `Days→Earnings` should `HALTED`-fail, not silently publish `REVIEW_ONLY`): **`DEFER`** to monthly structural review.

## Effective Next-Step Instruction

- Continue running the daily loop unchanged.
- Add the `daily_output_spec.md` ↔ `main.md` reconciliation, the 5% cap tension, and the empty-DTE forward guard to the next monthly structural review agenda.
- Re-rate AVGO post-print at the first publish slot on or after 2026-06-08.
- Resume normal evolution candidacy (threshold/weight mutation) once a live data feed is wired and ≥ 20 closed observations exist.

---

## Friday Weekly-Review Addendum (Folded In, Not Standalone)

Per `daily_schedule.md` §Weekly And Monthly Cadence, Friday 17:15 ET is the weekly parameter-review checkpoint. The standalone `13_weekly_review.md` artifact is **not** emitted today because the preconditions are not met:

| Precondition | Met? | Reason |
|---|---|---|
| At least one live run has produced realized data | ✗ | No live data adapter wired since the loop was instrumented |
| ≥ 20 closed observations to evaluate | ✗ | Count remains 0 |
| Threshold mutation eligibility | ✗ | Blocked by `stop_criteria.md` §Self-Evolution Stop item 1 |

### Observations carried to next eligible weekly review

1. The `ILLUSTRATIVE_MODE` OP fix from 2026-05-24 has held up across two subsequent runs (05-24 + 05-29). No regression detected. Once live data is wired, validate that live-mode behavior is unchanged from pre-fix (the falsifiable hypothesis recorded on 05-24).
2. The same-model baseline calendar gap (no claude-opus-4-7 run exists at ~30 days back; closest is 17 days) will close naturally as the system runs daily. The first eligible reflection with a true ~30-day same-model baseline arrives on 2026-06-12 (~31 days from 05-12).
3. AVGO event-window discipline drove a portfolio drop today. Record the date for post-print re-rating: first eligible re-evaluation is 2026-06-08 (5d buffer past the expected ~early-Jun reference cadence). If reference cadence drift turns out to exceed `±5d`, widen the buffer band.
4. The 5% single-name cap tension is now compounding cosmetically: the AVGO drop pushed LIN's documented breach from 21% to 22%. The structural tension is unchanged; the *visual* of the breach is slightly worse. This is not evidence to relax the cap; it is evidence that the structural-review decision (Option A: raise to 15-20%, or Option B: NAV-relative with cash overlay) is overdue. Logged.
5. Documentation tension between `main.md` and `daily_output_spec.md` is now active across model families (today's gpt-5 run followed `main.md`; the 05-12 / 05-24 claude runs followed `daily_output_spec.md`). Schema-consistency cost grows with each run until reconciled.

### Weekly Decision

`NO_CHANGE_ACCEPTED` for autonomous adoption. Observations 1-5 above are deferred to the next eligible weekly review (after a live feed is wired AND ≥ 20 closed observations exist) or to the next monthly structural review, whichever the human reviewer prefers.

## Mutation-Logging Summary

| Item | Status | Effective date |
|---|---|---|
| Loop or prompt mutation today | None | — |
| Threshold or weight mutation today | None | — |
| Spec reconciliation (`daily_output_spec.md` ↔ `main.md`) | `DEFER` to monthly review | Pending human approval |
| 5% single-name cap structural review | `DEFER` to monthly review | Pending human approval |
| Empty-DTE forward-guard (committee escalation logic) | `DEFER` to monthly review | Pending human approval |
| Post-AVGO re-rating reminder | Logged | First publish slot ≥ 2026-06-08 |
