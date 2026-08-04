# 13 — Evolution Log — 2026-08-03

## Run context

| Field | Value |
| --- | --- |
| Run date / status | 2026-08-03 / NO_TRADE |
| Regime | BULL |
| Evaluation window | 2026-07-27 … 2026-08-03, all models |
| Packages reviewed | 10 — claude-opus-5-2026-07-27, claude-opus-5-2026-07-28, claude-opus-5-2026-07-29, claude-opus-5-2026-07-30, claude-opus-5-2026-08-01, gpt-5-2026-07-27, gpt-5-2026-07-28, gpt-5-2026-07-29, gpt-5-2026-07-30, gpt-5-2026-08-03 |
| Ledger status | EQUITY_ALPHA n=515, eff_n=1; MARKET_FORECAST n=90, eff_n=1 |
| Baseline flag | SAME_MODEL_BASELINE; exact-date tie disclosed |
| Due / conflicts | 0 / 0 |

## What worked

- All 88 due keys settled with explicit regular-session timing conventions and no conflict.
- Five-year history, universe, earnings, technical, risk, and two-source published-price gates
  completed without a sampled-universe fallback.
- The 2026-08-01 accepted Track B correction is now applied: `Tech_Z` uses six distinct
  signals, while RS20/RS60 remain diagnostics and lineage is preserved.
- The risk committee reached `NO_TRADE` without spending a revision pass or misclassifying
  missing Enhancing inputs as Required blockers.

## What failed

- Rolling equity rank IC remains -0.0879 over
  n=515; score ordering is still anti-predictive.
- This run's equity settlement batch hit rate is 25.00% with mean z
  -0.8561.
- Structural Fundamental/Sentiment absence again makes `GO` impossible.

## Primary diagnosis: `FACTOR_CALIBRATION`

The negative rank IC priority override requires a calibration proposal before any clarity or
workflow change. The deduplicated Technical construction removes a known defect, but one run
cannot establish that its ordering improves out of sample.

## Proposed change — exactly one — Track A

**Shift family weights Technical `0.30 → 0.25` and Macro `0.15 → 0.20`; leave Fundamental
`0.30` and Sentiment `0.25` unchanged.** The single-step ±0.05 limit is respected.

Hypothesis: reducing trend-persistence exposure and increasing diversified regime/sector/rate
evidence will raise weighted rank IC by at least 0.05 without worsening maximum drawdown more
than 0.50% or turnover more than 25%.

## Validation

| Gate / delta | Result |
| --- | --- |
| Raw settled n ≥20 | PASS — 515 |
| 28d eff_n ≥3 | FAIL — 1 |
| Holdout / rolling validation | UNAVAILABLE — overlapping target windows are not an independent holdout |
| IR delta | UNAVAILABLE |
| Hit-rate delta | UNAVAILABLE |
| Drawdown delta | UNAVAILABLE |
| Turnover delta | UNAVAILABLE |

## Decision: **`DEFER — NO_CHANGE_ACCEPTED`**

Track A is ineligible because `eff_n < 3`; the proposal is recorded as an observation, not
rejected. No family weight, threshold, mu table, sizing parameter, confidence rule, or
protected risk limit changes today. Re-evaluate only after an independent third 28-day window
exists and compare the current six-signal engine with the proposed weights on a locked
holdout.

## Freeze check and next step

No freeze: this is an evidence-gated defer, not a rejected or oscillating parameter change.
Continue the current architecture and promote universe-scale Fundamental/Sentiment data only
through the existing Track B `HUMAN_REVIEW` process.
