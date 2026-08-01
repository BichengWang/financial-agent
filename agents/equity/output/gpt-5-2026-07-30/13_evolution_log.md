# 13 Evolution Log — 2026-07-30

## Run context

| Field | Value |
| --- | --- |
| Status / regime | NO_TRADE / NEUTRAL |
| Evaluation window | All dated packages 2026-07-23 through 2026-07-30, every model |
| Ledger | EQ n=347 eff_n=1; MF n=63 eff_n=1 |
| Track A eligibility | Blocked — INSUFFICIENT_EFFECTIVE_N |
| Baseline | SAME_MODEL_BASELINE `gpt-5-2026-07-02`; three tied folders disclosed; conclusion not invariant |
| Primary diagnosis | factor calibration |

## Observe

Settlement and source-grounding mechanics worked: the merged same-day package had already canonicalized all 58 due keys, this run added zero duplicates, and the fresh normalizer still reports zero due inventory and zero conflicts. The current forward earnings sweep completed 26/26 days, and all published prices passed the two-source gate. Equity weighted rank IC remains -0.1975; 19/23 reported vintages are non-positive.

## Diagnose

The composite leaderboard is not predictive across the available overlapping vintages. Technical momentum has carried twice the active production weight of Macro while Fundamental and Sentiment remain unavailable, so recent momentum-heavy books can dominate even when defensive regime evidence is stronger.

## Exactly one proposed change

**Track A — shift Technical 0.30 → 0.25 and Macro 0.15 → 0.20.** Fundamental remains 0.30 and Sentiment remains 0.25. The change would preserve the total family weight and every protected risk rule.

### Hypothesis

Reducing the active momentum tilt and increasing regime sensitivity should improve out-of-sample equity rank IC by at least 0.05 without worsening maximum drawdown by more than 0.50% or turnover by more than 25%.

### Validation

Raw EQUITY_ALPHA evidence passes `n >= 20` at n=347, but independent-window evidence fails at eff_n=1 versus the required 3. No locked holdout/full-universe replay exists for the proposed weights, so IR, hit-rate, drawdown, and turnover deltas cannot be validly claimed. The proposal is not tested or applied.

## Decision

**DEFER — NO_CHANGE_ACCEPTED.** Re-evaluate when EQUITY_ALPHA eff_n reaches 3 and a locked replay can measure the stated acceptance criteria. Current weights remain unchanged. The separate beta-scaled ETF-mu issue remains queued and is not a second proposal.

## Mutation log

| Field | Value |
| --- | --- |
| Current problem | Weighted equity rank IC is non-positive |
| Proposed change | Technical 0.30→0.25; Macro 0.15→0.20 |
| Validation | n=347 passes; eff_n=1 fails; no locked holdout |
| Result | Insufficient independent evidence; no parameters changed |
| Decision | DEFER — NO_CHANGE_ACCEPTED |
| Effective | None |
