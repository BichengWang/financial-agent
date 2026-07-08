# 13 Evolution Log

## What Went Right

- The run obeyed deterministic MoM baseline selection and correctly used the in-window cross-model baseline dated 2026-05-12.
- Source-ledger rows were created before reflection and downstream scoring.
- Derived MoM returns were computed only from source-backed price rows.
- Missing risk inputs were labeled `UNAVAILABLE` and blocked `GO`.

## What Went Wrong

- The automation still lacks a full market-data stack for bars, options IV/skew, short-interest/borrow, bid-ask spreads, and covariance/drawdown.
- The selected baseline uses an older artifact numbering scheme and is illustrative, which weakens MoM interpretability.
- The monitor ranking is sampled and cannot claim full-universe percentiles.

## Proposed Change

Add a prompt-level "baseline audit note" requirement to `00_run_manifest.md` and `02_reflection.md` that explicitly states whether a baseline is same-model, cross-model, older-than-window, illustrative, or live.

## Hypothesis

Making baseline quality explicit will reduce accidental over-weighting of cross-model or illustrative prior runs in carry-forward decisions.

## Validation Method

No valid holdout test was available during this run. The proposal affects output clarity, not factor performance, so it cannot satisfy the evolution policy's acceptance standard today.

## Test Result

UNAVAILABLE.

## Decision

`NO_CHANGE_ACCEPTED`.

## Effective Date

No prompt mutation accepted. Revisit after at least 20 closed observations or a human-approved prompt-maintenance pass.
