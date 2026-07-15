# 13 Evolution Log

| Field | Value |
| --- | --- |
| Date | 2026-07-15 |
| Status | NO_TRADE |
| Regime | BULL |
| Review timing | Preliminary; the runbook-scheduled 17:00 ET daily evolution review was not due at the 16:19 ET publication cut. |
| Evaluation window | 2026-07-09 through 2026-07-15 inclusive, all available models. |
| Packages reviewed | 13 dated directories total: 12 prior packages across claude-fable-5 and gpt-5 plus the current gpt-5 package; the claude-fable-5 July 11 HALTED/backfilled package remains in scope. |
| Ledger status | 91 canonical equities; 59.34% HIT; 83.52% IN_CI; mean z -0.140; weighted rank IC +0.040. |
| Baseline flag | (none) - valid same-model exact-28-day baseline. |

## Trailing Seven-Day Review

- No completed package in the window published GO; missing Fundamental/Sentiment evidence remained the recurring evidence-breadth blocker.
- Timing-valid canonical history through today contains 91 equities and 12 market forecasts. Equity CI coverage and weighted rank IC do not trigger the calibration priority override.
- Settlement accounting is the dominant process failure: 184 prior settlement rows map to only 86 keys, and the two July 14 packages use conflicting price cuts.
- Confirmed earnings retrieval, due-inventory rows, and settlement timing conventions worked; cross-model canonicalization remains missing.

## Primary Diagnosis

`source grounding` / settlement state integrity.

## Proposed Change

**Track B — HUMAN_REVIEW.** Implement the P0 canonical settlement-ledger plan at `plan/2026-07-15-canonical-settlement-ledger.md`: immutable key `(model, vintage_date, ticker, type, target_date)`; standard fields; timing validation before precedence; deterministic first complete valid settlement; later duplicates audit-only; unresolved conflicts excluded; rolling metrics and due inventory consume only canonical keys.

Hypothesis: a single canonical ledger will make rolling calibration and due inventory deterministic across models without changing scoring math, mu priors, thresholds, or protected risk limits.

## Validation

1. Problem evidence: 184 historical rows collapse to 86 keys. The conflict is exposed by `agents/equity/output/gpt-5-2026-07-14/settlement_precedence_manifest.json`, the target-day rows in `agents/equity/output/gpt-5-2026-07-14/15_predictions.json`, and the completed-prior-close treatment in `agents/equity/output/claude-fable-5-2026-07-14/02_reflection.md`; it changes hit rate and rank IC.
2. Protection check: the proposal strengthens the existing completed-close grounding gate and changes no protected rule.
3. Dry test: applying the plan's timing validator yields 91 equity and 12 market canonical keys after today's settlements, stable across the merged repository.

## Decision

`DEFER` — Track B, `HUMAN_REVIEW`. This is the sole proposed change and the requested top-priority plan has been added to `plan/`. The formal acceptance decision remains at the post-close evolution cadence; no scoring formula, factor weight, forecast prior, or protected limit changes in this package.
