# 13 — Evolution Log — 2026-08-03

## Run context

| Field | Value |
| --- | --- |
| Run date / status | 2026-08-03 / `HALTED` |
| Data mode / regime | `DELAYED_PARTIAL` / `BULL` |
| Evaluation window | 2026-07-28 … 2026-08-03 inclusive; trailing 7 calendar days; all models |
| Packages reviewed | 9 — claude-opus-5: 07-28, 07-29, 07-30, 08-01, 08-03; gpt-5: 07-28, 07-29, 07-30, 08-03 |
| Ledger status | EQUITY_ALPHA n=515, eff_n=1; MARKET_FORECAST n=90, eff_n=1; due=0; conflicts=0 |
| Baseline | valid same-model `gpt-5-2026-07-06`; no exception flag; exact-date cross-model tie disclosed |
| Current equity ranks | withdrawn pre-halt diagnostics; excluded from evolution evidence |

## What worked

- All 88 due keys settled with regular-session timing conventions and no conflict.
- Five-year history, index-union, technical-helper, and two-source price fetches completed.
- The accepted Track B `Tech_Z` deduplication is applied and fully ledgered.
- The correction audit detected the Required-input breach and withdrew invalid equity records.

## What failed

- Only 5/20 provisional names had confirmed next earnings dates; zero cadence estimates were
  produced, so 75% had unresolved critical inputs and Hard Halt criterion #3 applied.
- The initial package incorrectly treated a transport-complete no-print sweep as next-date
  completeness and allowed zero event penalties to reach provisional scoring.
- Historical weighted equity rank IC remains -0.0879, but the current provisional ranks are
  not valid evidence for calibration.

## Primary diagnosis: `SOURCE_GROUNDING`

The decisive failure is the missing cadence fallback and pre-scoring completeness assertion,
not a demonstrated factor-weight defect. Settled-history metrics remain valid; current-run
equity ordering is excluded from any model-change decision.

## Proposed change — exactly one — Track B

Add a deterministic pre-scoring earnings completeness validator: require each scoreable name
to have either a confirmed next date or `prior_report_date + ~91d` tagged
`ESTIMATED (±5d)`; otherwise emit the coverage census and halt before score/rank/prediction
generation when unresolved critical inputs exceed 20%.

### Hypothesis

An explicit assertion prevents a complete calendar transport sweep from being mistaken for
complete Required-input coverage and prevents unsupported zero penalties from propagating.

### Three-condition validation

| Track B condition | Result |
| --- | --- |
| Concrete counterexample / invariant | PASS — this run had 15/20 unresolved dates yet initially propagated provisional scores |
| Deterministic and testable | PASS — validator checks confirmed-or-estimated coverage and the >20% halt threshold |
| Protected rules preserved | PASS — it enforces existing Required-input, cadence, and Hard Halt rules; no factor weights or risk caps change |

## Decision

**`DEFER — NO_CHANGE_ACCEPTED`.** The proposal is sound, but this halted correction does not
add untested tooling. Implement it in a dedicated change with fixtures for confirmed,
cadence-estimated, and unresolved earnings cases. No prompt, calibration table, factor weight,
or sizing parameter changes in this run.
