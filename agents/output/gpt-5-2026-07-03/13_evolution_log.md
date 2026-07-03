# 13 Evolution Log

## Run Context

- Date: 2026-07-03
- Status: REVIEW_ONLY
- Regime: NEUTRAL
- Evaluation window: 2026-06-27 through 2026-07-03 across gpt-5, claude-fable, claude-opus, and gemini packages where present
- Ledger status: price/history/sigma/technical rows grounded; fundamental/revision/sentiment/earnings refresh unavailable
- Baseline flag: SAME_MODEL_BASELINE

## What Worked

The deterministic index-union helper and technical-indicator helper completed on the full universe, avoiding the legacy fixed-sample failure mode.

## What Failed

Holiday handling remains semantically awkward: the runbook says holiday packages are review-only, while the data taxonomy has no dedicated holiday mode. This run used `DELAYED_PARTIAL` to preserve fetched July 2 data without implying a July 3 entry.

## Primary Diagnosis

`output clarity`.

## Proposed Change

Track B: clarify in the prompt stack that closed-market runs with successfully fetched prior-session data should publish `REVIEW_ONLY` as a holiday delayed-data package, without weakening data-source requirements.

## Hypothesis

A specific holiday-handling sentence would reduce inconsistent use of `ILLUSTRATIVE`, `DELAYED`, and `DELAYED_PARTIAL` across weekend/holiday packages.

## Validation

Process-only change. It does not weaken protected risk controls or grounding gates. Human review is needed before changing the data-mode taxonomy.

## Decision

`DEFER` / `NO_CHANGE_ACCEPTED` pending human review. No prompt files were modified in this run.
