# Evolution Policy

This document governs how the prompt system can improve itself without drifting into unsafe, overfit, or unauditable behavior.

## Purpose

The evolution loop exists to improve:

- Signal calibration.
- Prompt clarity.
- Handoff quality between agents.
- False-positive control.
- Portfolio construction discipline.

It does not exist to justify more trades, loosen standards, or reverse-engineer recent winners.

## Allowed Mutation Scope

The evolution agent may propose changes to:

1. Prompt wording for clarity or tighter task framing.
2. Output schemas and artifact naming.
3. Sequence or retry logic between agents.
4. Factor weights within a single-step change limit of `+/- 0.05` per family.
5. Non-protected scoring thresholds within a documented hypothesis.
6. Confidence label calibration.

## Protected Rules

These rules may not be weakened by autonomous mutation:

1. No fabricated data.
2. Publish `NO_TRADE` when evidence is insufficient.
3. Max single-name weight of `5%`.
4. Max sector concentration of `30%`.
5. Portfolio beta band of `0.90` to `1.10`.
6. Pairwise correlation cap of `0.45`.
7. 95th percentile 1-month drawdown cap of `8%`.
8. Mandatory logging of accepted and rejected changes.

Any proposal that touches a protected rule requires human approval before it can be adopted.

## Two-Track Change Classification

Every proposal must be classified before evaluation. The last three runs all ended `NO_CHANGE_ACCEPTED` because process-clarity fixes were judged against a statistical acceptance standard they can never meet — while the 20-observation evidence base they were waiting on could never accumulate. The tracks break that deadlock:

**Track A — Performance changes** (factor weights, thresholds, mu Calibration Table, confidence calibration, sizing parameters):

- Require ≥ 20 settled prediction records from `15_predictions.json` files and a holdout/rolling validation per the Acceptance Standard below.

**Track B — Process changes** (prompt wording clarity, artifact naming/numbering, spec-consistency fixes, schema corrections, sequencing, missing-fetch procedure fixes):

- Do NOT require closed observations or a statistical holdout — these changes have no scoring math to validate.
- Acceptance standard: (1) explicit problem statement citing the artifact that exposed it, (2) the change cannot weaken a protected rule or any grounding gate, (3) the change is logged with a `HUMAN_REVIEW` flag in `13_evolution_log.md` and takes effect next run unless reverted.
- Limit: at most one Track B change per run.

A spec inconsistency flagged in two consecutive evolution logs (e.g., `main.md` vs `daily_output_spec.md` layout drift) is mandatory Track B work, not optional.

## Required Evolution Workflow

Every evolution pass must follow this order:

1. Observe:
   Compare forecasted outcomes with realized outcomes.
2. Diagnose:
   Identify whether errors came from data quality, factor construction, regime classification, sizing, or risk review.
3. Hypothesize:
   State one precise change and why it should help.
4. Test:
   Evaluate the change on a holdout window or rolling validation slice.
5. Decide:
   Accept, reject, or defer the change.
6. Log:
   Write the result to the daily evolution artifact.

Do not bundle many unrelated changes into one pass.

## Acceptance Standard

Accept a proposed change only if all of the following are true:

1. The hypothesis is explicit and falsifiable.
2. The validation window is disclosed.
3. Out-of-sample Information Ratio improves by at least `0.05`, or hit rate improves by at least `2 percentage points` without worsening drawdown.
4. Maximum drawdown does not worsen by more than `0.50%`.
5. Turnover does not increase by more than `25%` unless that increase is clearly justified and compensated by better risk-adjusted return.

## Review Cadence

- Daily: light evolution review after close.
- Friday after close: weekly parameter review.
- Last trading day of month: structural review of factors, prompts, and failure modes.

Daily review may adjust wording, thresholds, or sequencing within the allowed mutation scope.

Weekly and monthly reviews may propose broader changes, but they still must respect protected rules.

## Mutation Logging Standard

Every proposal must record:

- Current problem.
- Proposed change.
- Validation method.
- Result.
- Decision.
- Effective date, if accepted.

If no change is accepted, explicitly log `NO_CHANGE_ACCEPTED`.

## Anti-Overfitting Rules

- Do not optimize to a single recent regime.
- Do not promote a feature because of one or two anecdotal winners.
- Do not increase complexity unless the simpler version measurably fails.
- Prefer fewer, better-justified changes over frequent churn.

When in doubt, preserve the current prompt set and log the uncertainty instead of mutating it.
