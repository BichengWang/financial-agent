# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-04 (Saturday — markets closed) |
| Status | REVIEW_ONLY |
| Regime | NEUTRAL |
| Evaluation window | 2026-06-27 → 2026-07-04, all models |
| Ledger status | 0 settled; 491 prior OPEN + 26 published this run; first settlements due 2026-07-08 |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-28..07-04, daily incl. weekend), gemini-3.5-flash (06-29, 07-01), claude-opus-4-8 (06-30), claude-sonnet-5 (07-02, 07-03), claude-fable-5 (07-01, 07-02, 07-03, this run).
- Statuses: NO_TRADE on every trading-day run, REVIEW_ONLY on the closed days (07-03, 07-04) across models — the audit trail has no skipped days through the long weekend.
- **Cross-model divergence (same bars, opposite books)**: on identical 2026-07-02 closes, gpt-5-07-04 ranked a semis/AI momentum sleeve (MU, INTC, AMD, WDC, MRVL, ARM...) while this run's engine ranks the defensive-rotation complex (DVA, HUM, HSIC, staples, REITs) and explicitly penalizes the unwound momentum names. Same data, inverted factor interpretation — when the 07-08+ settlements accumulate, this divergence becomes directly measurable (rank IC per model) and is the single most informative comparison in the window.
- **Numeric-reproduction finding (this model's own 07-03 vintage)**: the recorded QQQ/SOXX MARKET_FORECAST mu (+0.29%/+0.14%) do not reproduce from their stated derivation (beta x SPY prior = +0.79%; 3.27 x 0.5% - 1.0pp = +0.64%). Today's records recompute cleanly from ledger-backed betas. Settlement is unaffected (records settle against their recorded mu), but the derivation chain must be mechanically checkable — logged as a **future Track B candidate** (emit a machine-checkable mu-derivation field in MARKET_FORECAST records); the one-change slot remains occupied by the mandatory item below.
- The family-coverage gate blocked investability again for every completed scoring run in the window (fable ×4, sonnet ×2, gpt-5's data-completeness variant daily).

## What Worked / What Failed

Worked: weekend pipeline ran clean end-to-end on final Thursday closes (521/521 fetches, 0 failures — first zero-failure fetch on record); Yahoo↔Nasdaq verification at 0.000% on all 26 published names; IBKR closed-market behavior matched the documented 07-03 finding (prior-session closes, used for prior-record verification only); the one-day earnings-window roll correctly churned LII/URI/LUV out of the sleeve — the penalty machinery responds to calendar drift, not just price drift.
Failed / degraded: Yahoo ^IRX still stale (06-26 print; tagged HISTORICAL); the 07-03 QQQ/SOXX mu-reproduction issue above; three consecutive vintages now share the same 2026-07-02 entry tape (07-02 intraday, 07-03 close, 07-04 close runs) — settlement observations will be correlated and the calibration metrics must be read with that dependence (risk committee concern #1).

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds) — fourth consecutive run. Per §Evolution Policy this remains **mandatory Track B work** (two-consecutive-flags rule crossed 07-02).

## Proposed Change (exactly one — the mandatory item)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, fourth escalation.** Proposal unchanged from 07-01/07-02/07-03: amend rules.md §Evidence Thresholds #2 so that when a family is UNAVAILABLE universe-wide due to an unwired Enhancing feed, the threshold applies over sourceable families (all non-negative), with LOW confidence cap, DQ <= 0.80, and the 50% gross-exposure cap from §Input Classification. Still DEFER for the same governance reason: the change alters investability semantics for all models and ships through an auto-merge pipeline no human has reviewed. **The operator now has four consecutive flags and a drafted one-sentence amendment; deciding before Wednesday 2026-07-08 lets the first settled-evidence week start on a resolved spec.**

## Decision

**DEFER** (HUMAN_REVIEW; mandatory-work escalation, 4th consecutive). Freeze-criteria check: unchanged from 07-03 — the streak is DEFER-pending-human, not evidence-lack rejections; parameter mutation stays de facto frozen at 0 settled (< 20). Effective next step: Monday 2026-07-06 normal run; **Wednesday 2026-07-08 first settlement pass** (12 records, alpha-scored vs recorded SPY 728.31) and the system's first realized calibration metrics.
