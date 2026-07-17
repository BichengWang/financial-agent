# Evolution Log — 2026-07-17

## Run Context

- Status / regime: `NO_TRADE` / `NEUTRAL`.
- Review window: every dated package from 2026-07-10 through 2026-07-17 across all models.
- Ledger: 119 canonical equity and 18 market settlements; zero due, zero conflicts.
- Baseline flag: `NONE` — exact same-model 2026-06-19 match.
- Calibration: equity hit `55.46%`, CI `79.83%`, mean z `-0.1745`, weighted rank IC `-0.008757` (L336,L337,L338).

## What Worked / Failed

- Worked: all 63 due keys were repaired with exact target-date two-source closes; the canonical inventory is now zero.
- Worked: equity CI coverage remains inside the healthy 55–85% band.
- Failed: five consecutive GPT vintages from 2026-06-15 through 2026-06-19 have negative rank IC; the weighted aggregate is non-positive. Market direction accuracy is only `33.33%`, but n=18 remains below the Track A 20-record bar for market-prior changes.

| Vintage | n | Rank IC |
| --- | --- | --- |
| claude-fable-5:2026-06-10 | 12 | -0.5105 |
| gpt-5:2026-06-11 | 17 | 0.3480 |
| gpt-5:2026-06-14 | 17 | 0.5628 |
| gpt-5:2026-06-15 | 17 | -0.0833 |
| gpt-5:2026-06-16 | 14 | -0.0462 |
| gpt-5:2026-06-17 | 14 | -0.2484 |
| gpt-5:2026-06-18 | 14 | -0.2835 |
| gpt-5:2026-06-19 | 14 | -0.0637 |

## Primary Diagnosis

`FACTOR_CALIBRATION`. The non-positive rank IC priority override requires calibration work before process-only evolution and keeps confidence capped at `MEDIUM`.

## Exactly One Proposed Change

- Classification: **Track A — Performance**.
- Proposal: shift Technical/Price weight `0.30 -> 0.25` and Fundamental weight `0.30 -> 0.35` (one permitted +/-0.05 reallocation); all other family weights and protected rules remain unchanged.
- Hypothesis: reducing momentum-led Technical concentration would reduce rank inversions once a qualifying full-universe Fundamental family is available.
- Validation: `UNAVAILABLE` (L370). No full-universe counterfactual OOS IR, hit-rate, drawdown, or turnover comparison is available. Fund_Z remains SHADOW at 24/515 coverage, so the proposed weight cannot yet be exercised without violating the 70%-coverage gate.

## Decision

`DEFER — NO_CHANGE_ACCEPTED`. Keep weights unchanged and retain the MEDIUM confidence cap. Re-test only after full-universe Fundamental shadow coverage and a disclosed holdout can satisfy the Track A acceptance standard. No protected risk rule, scoring rule, or prompt file changed.
