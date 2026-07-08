# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-05 (Sunday — markets closed) |
| Status | REVIEW_ONLY |
| Regime | NEUTRAL |
| Evaluation window | 2026-06-28 → 2026-07-05, all models |
| Ledger status | 0 settled; 517 prior OPEN + 26 published this run; first settlements due 2026-07-08 |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-28..07-04, daily incl. the holiday weekend; no 07-05 package exists at this run's execution time), gemini-3.5-flash (06-29, 07-01), claude-opus-4-8 (06-30), claude-sonnet-5 (07-02, 07-03), claude-fable-5 (07-01, 07-02, 07-03, 07-04, this run).
- Statuses: NO_TRADE on every trading-day run, REVIEW_ONLY on the closed days (07-03, 07-04, 07-05) — the audit trail has no skipped days through the long weekend.
- **Cross-model divergence (same bars, opposite books)**: unchanged and still the window's most informative comparison — on identical 2026-07-02 closes, gpt-5-07-04 ranked a semis/AI momentum sleeve (MU, INTC, AMD, WDC, MRVL, ARM...) while this engine ranks the defensive-rotation complex and penalizes the unwound momentum names. The 07-08+ settlement stream makes the divergence measurable (per-model rank IC).
- **Penalty-machinery observation (new, this run)**: the one-day calendar roll alone re-ranked the sleeve — DOC (yesterday #3), WST (#16) and KDP (#18) dropped when their est. 7/24 reports crossed the <=19d buffered window, and WELL/INCY/BXP promoted. Two consecutive days of pure calendar-driven churn (LII/URI/LUV on 07-04, DOC/WST/KDP today) confirm the earnings penalty responds to calendar drift independent of price drift — by design, but it concentrates sleeve turnover into pre-earnings weeks, which will feed the turnover term of any future Track A evaluation.
- **Data-quality self-resolution**: Yahoo ^IRX caught up this run (3.668% @ 2026-07-02, DELAYED) after two runs of documented staleness — no process change needed; the freshness-tagging discipline handled the lag correctly while it lasted.
- The family-coverage gate blocked investability again for every completed scoring run in the window (fable ×5, sonnet ×2, gpt-5's data-completeness variant daily).

## What Worked / What Failed

Worked: weekend pipeline clean end-to-end on final Thursday closes (521/521 fetches, second consecutive zero-failure run); Yahoo↔Nasdaq verification at 0.000% on all 26 published names; IBKR closed-market behavior reproduced for the third time and correctly quarantined as prior-record verification; the deterministic engine reproduced the 07-04 scores to the third decimal on identical bars (score stability under re-execution), with all deltas attributable to the documented calendar roll and rf refresh; `mu_derivation` blocks carried in all three MARKET_FORECAST records.
Failed / degraded: nothing new this run. Standing items: two-family scoring (below); the 07-03 QQQ/SOXX mu-reproduction discrepancy remains on record (superseded operationally by the mu_derivation field from 07-04 onward); four vintages now share the 2026-07-02 entry tape — the correlated-settlement caveat is at maximum until Monday's session produces a new tape.

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds) — fifth consecutive run. Per §Evolution Policy this remains **mandatory Track B work** (two-consecutive-flags rule crossed 07-02).

## Proposed Change (exactly one — the mandatory item)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, fifth escalation.** Proposal unchanged from 07-01/07-02/07-03/07-04: amend rules.md §Evidence Thresholds #2 so that when a family is UNAVAILABLE universe-wide due to an unwired Enhancing feed, the threshold applies over sourceable families (all non-negative), with LOW confidence cap, DQ <= 0.80, and the 50% gross-exposure cap from §Input Classification. Still DEFER for the same governance reason: the change alters investability semantics for all models and ships through an auto-merge pipeline no human has reviewed. **The operator now has five consecutive flags and a drafted one-sentence amendment; deciding before Wednesday 2026-07-08 lets the first settled-evidence week start on a resolved spec.**

## Decision

**DEFER** (HUMAN_REVIEW; mandatory-work escalation, 5th consecutive). Freeze-criteria check: unchanged — the streak is DEFER-pending-human, not evidence-lack rejections; parameter mutation stays de facto frozen at 0 settled (< 20). Effective next step: Monday 2026-07-06 normal run on a fresh tape; **Wednesday 2026-07-08 first settlement pass** (12 records, alpha-scored vs recorded SPY 728.31) and the system's first realized calibration metrics.
