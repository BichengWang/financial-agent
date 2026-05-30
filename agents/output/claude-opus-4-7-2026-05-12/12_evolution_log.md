# 12 Evolution Log

## Failure Diagnosis

Today's miss category: **Data quality** (entirely upstream of the prompt stack). No factor, regime, sizing, or risk-review error was observed because no real evaluation occurred.

Per `eval/evolution_policy.md` §Anti-Overfitting, single-day evidence is not a basis for mutation, and per `eval/stop_criteria.md` §Self-Evolution Stop Criteria item 1 (fewer than 20 closed observations), the evolution loop is structurally not eligible to mutate today.

## Proposed Change

None proposed for autonomous adoption today. Filing one **deferred** observation for human review on the next monthly structural pass:

> **Observation (deferred):** In `ILLUSTRATIVE_MODE` runs, `05_top_candidates.md` currently emits placeholder candidate cards with names like MSFT/NVDA. Even with the `ILLUSTRATIVE` banner, the artifact is mis-citation-prone if shared out of context. Consider tightening the spec so that in `ILLUSTRATIVE_MODE`, candidate cards are suppressed and replaced by a single explicit `NO_INVESTABLE_SET` block.
>
> *Rationale:* improves auditability and reduces "what did the model recommend on 2026-05-12?" misreadings. Does not weaken any protected rule.
>
> *Why deferred:* mutation today would be based on a single dry run with no realized comparison data. Awaits ≥20 closed observations or human approval (it touches the output schema, which is allowed scope but should still be reviewed).

## Validation Method

Not run — proposal is `DEFER`, no test was attempted.

## Validation Result

N/A.

## Decision

`NO_CHANGE_ACCEPTED` (one observation deferred to weekly/monthly review).

## Effective Next-Step Instruction

- Continue running the daily loop unchanged.
- Re-evaluate the proposed `ILLUSTRATIVE_MODE` candidate-card suppression at the next monthly structural review.
- Resume normal evolution candidacy once a live data feed is wired and ≥20 closed observations exist.
