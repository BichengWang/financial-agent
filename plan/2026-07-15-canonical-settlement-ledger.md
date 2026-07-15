# Canonical Settlement Ledger

## Priority

P0 process-integrity improvement for the daily equity research pipeline.

## Problem

Prediction source ledgers are immutable and retain `OPEN` status, while later run
packages append settlement rows independently. As of the 2026-07-15 run, 184
historical settlement rows map to only 86 prediction keys. Every settled key has
duplicates, and the two 2026-07-14 packages use conflicting time cuts for the
same 17 predictions: one uses target-day intraday prices and the other follows
the required `TARGET_EQ_RUN_DATE` prior-completed-close convention. Rolling
calibration therefore depends on which package happens to be scanned first.

## Proposed Improvement

Make a timing-validated canonical settlement ledger the sole input to rolling
calibration and due-inventory calculations.

1. Use the immutable key
   `(model, vintage_date, ticker, type, target_date)`, normalizing a missing
   `type` to `EQUITY_ALPHA` as required by the daily-system rules.
2. Normalize every candidate settlement to one schema containing `settled_at`,
   `price_date`, `settlement_convention`, price-source rows, realized return,
   benchmark return/alpha where applicable, direction, CI result, and z-score.
3. Reject a candidate before precedence selection when an ordinary target does
   not use the completed target-date close, or when its price cut violates the
   prior-completed-session rules for `TARGET_EQ_RUN_DATE` or `WEEKEND_TARGET`.
   Intraday observations are never valid settlement prices.
4. Select the earliest complete, timing-valid candidate whose
   `settlement_run_date == target_date`; its `price_date` may be the prior
   completed session under an exception. If none exists, select the earliest
   complete, timing-valid post-target candidate.
5. Keep later agreeing duplicates as audit-only records. When candidates in the
   same precedence tier materially disagree on normalized price or outcome,
   flag the key as unresolved and exclude it from calibration rather than
   choosing silently; lower-priority post-target observations do not override a
   valid target-date settlement.
6. Generate a machine-readable precedence manifest and compute rolling metrics
   only from its canonical keys.

## Acceptance Criteria

- Re-scanning the same repository produces identical canonical keys and metrics.
- The 2026-07-14 conflict selects the completed 2026-07-13 close and rejects the
  target-day intraday candidate with a recorded reason.
- Counts through 2026-07-14 are exactly 77 equity-alpha settlements and 9 market
  forecasts; after the 2026-07-15 due set they are 91 and 12.
- Re-running a later package cannot increase settled counts for an existing key.
- Due inventory is derived from source prediction keys minus canonical keys, not
  from mutable `status` fields.
- No scoring formula, factor weight, forecast prior, or protected risk limit is
  changed by this work.

## Implementation Order

1. Add a normalizer and timing validator with fixtures for the known schema
   variants.
2. Add deterministic precedence and conflict reporting.
3. Route reflection, rolling calibration, and due inventory through the canonical
   manifest.
4. Add regression tests for duplicate rows, same-day intraday rejection,
   weekend targets, and rerun idempotence.
5. Document the canonical-ledger contract in the daily system rules after the
   regression suite passes.
