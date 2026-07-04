# 13 Evolution Log

## Run Context

- Date: 2026-07-04
- Status: REVIEW_ONLY
- Regime: NEUTRAL
- Evaluation window: 2026-06-28 through 2026-07-04 across gpt-5, claude-fable, claude-opus, and gemini packages where present
- Ledger status: price/history/sigma/technical rows grounded; fundamental/revision/sentiment/earnings refresh unavailable
- Baseline flag: SAME_MODEL_BASELINE

## What Worked

The deterministic index-union helper and technical-indicator helper completed on the full universe again, avoiding the legacy fixed-sample failure mode.

## What Failed

Closed-market handling remains semantically awkward: the runbook requires holiday packages, while the data taxonomy has no dedicated weekend/holiday delayed-data mode.

## Primary Diagnosis

`output clarity`.

## Proposed Change

Track B: add an explicit closed-market delayed-data sentence to the prompt stack so weekend and observed-holiday runs publish `REVIEW_ONLY` without implying live entry availability.

## Hypothesis

A specific closed-market handling sentence would reduce inconsistent use of `ILLUSTRATIVE`, `DELAYED`, and `DELAYED_PARTIAL` across weekend/holiday packages.

## Validation

Process-only change. It does not weaken protected risk controls or grounding gates. Human review is needed before changing the data-mode taxonomy.

## Decision

`DEFER` / `NO_CHANGE_ACCEPTED` pending human review. No prompt files were modified in this run.
