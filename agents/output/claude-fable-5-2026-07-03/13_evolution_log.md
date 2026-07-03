# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-03 (market holiday) |
| Status | REVIEW_ONLY |
| Regime | NEUTRAL |
| Evaluation window | 2026-06-26 → 2026-07-03, all models |
| Ledger status | 0 settled; 412 prior OPEN + 26 published this run; first settlements due 2026-07-08 |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-28..07-03, daily), gemini-3.5-flash (06-29, 07-01), claude-opus-4-8 (06-30), claude-fable-5 (07-01, 07-02, this run).
- Statuses: NO_TRADE on every trading-day run, REVIEW_ONLY on holiday runs (gpt-5-07-03, this run) — the audit trail has no skipped days across two models for the holiday, as the runbook intends.
- **Holiday data-mode divergence observed**: for the identical data state (no 07-03 session; 07-02 closes fetchable), gpt-5 declared `DELAYED_PARTIAL` (treating "today's tape" as a missing Required input) while this run declares `DELAYED` (all Required inputs grounded to the last completed session; no such session exists to be missing). The runbook itself prescribes `ILLUSTRATIVE_MODE` for holidays — a third convention, written before the fetch stack existed, which neither model followed because fetched real closes dominate fabricated reference values under the Non-Fabrication Contract. Three conventions for one state is a spec-wording gap; logged as a **future Track B candidate** (not proposed today — the one-change slot is occupied by the mandatory item below).
- The family-coverage gate blocked investability again for every completed scoring run in the window (fable ×3, gpt-5's data-completeness variant daily).

## What Worked / What Failed

Worked: holiday pipeline ran clean end-to-end on final session closes (no partial-bar caveats); Yahoo↔Nasdaq verification at 0.000% divergence on all 26 published names; the ±2pp mu clamp held its first live test (UNH → 0.0% → correctly excluded via reflection DOWNGRADE rather than published degenerate); SATS correctly re-entered the universe after trading resumed; weekly review published on schedule under the holiday rule.
Failed / degraded: Yahoo's ^IRX series lags holidays (freshest rf print 06-26; tagged HISTORICAL rather than passed off as fresh); IBKR's closed-market snapshots serve prior-session closes (useful only as prior-record verification — documented so future holiday runs don't mistake them for current corroboration); two consecutive sleeves overlap 19/23 names, so upcoming settlements will be correlated observations (flagged for calibration reading).

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds) — third consecutive run. Per §Evolution Policy this remains **mandatory Track B work** (two-consecutive-flags rule crossed yesterday).

## Proposed Change (exactly one — the mandatory item)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, third escalation.** Proposal unchanged from 07-01/07-02: amend rules.md §Evidence Thresholds #2 so that when a family is UNAVAILABLE universe-wide due to an unwired Enhancing feed, the threshold applies over sourceable families (all non-negative), with LOW confidence cap, DQ ≤ 0.80, and the 50% gross-exposure cap from §Input Classification. Still DEFER for the same governance reason: the change alters investability semantics for all models and ships through an auto-merge pipeline no human has reviewed yet. **The operator now has three consecutive flags and a drafted one-sentence amendment; a decision before 2026-07-08 would let the first settled-evidence week start on a resolved spec.**

## Decision

**DEFER** (HUMAN_REVIEW; mandatory-work escalation, 3rd consecutive). Freeze-criteria check: no changes have been *rejected for lack of evidence* (the streak is DEFER-pending-human, plus one NO_CHANGE_ACCEPTED on 06-30) — formal freeze criterion #1 not triggered; parameter mutation is effectively frozen anyway (Track A locked at 0 settled < 20). Effective next step: Monday 2026-07-06 normal run; **Wednesday 2026-07-08 must run the first settlement pass** (12 records) and report the system's first realized calibration metrics.
