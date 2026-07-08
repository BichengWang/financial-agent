# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-06 (Monday — live session; midday run) |
| Status | NO_TRADE |
| Regime | NEUTRAL |
| Evaluation window | 2026-06-29 → 2026-07-06, all models |
| Ledger status | 0 settled; 566 prior OPEN + 26 published this run; first settlements due **Wednesday 2026-07-08** |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-29..07-05 daily), gemini-3.5-flash (06-29, 07-01; a gemini-3.5-flash-2026-07-06 folder exists untracked in git — noted, not evidence until committed), claude-opus-4-8 (06-30), claude-sonnet-5 (07-02, 07-03), claude-fable-5 (07-01..07-05, this run).
- Statuses: NO_TRADE on all completed trading-day scoring runs; REVIEW_ONLY across the 07-03..07-05 closed days. Audit trail unbroken through the long weekend.
- **Fresh-tape rotation (new evidence today)**: on the first live session since 07-02, this engine's leaderboard rotated from pure defensives toward travel (DAL #6), security software (PANW #1, FTNT #3, CRWD #5) and cyclicals (MAS, SWK) — directionally *toward* the gpt-5-07-04 momentum book and away from the defensive-rotation complex this engine ranked on frozen bars. The 07-08+ settlement stream will score both stances on the same tape; rank IC per model remains the metric to watch.
- **Penalty machinery**: earnings-window penalties expanded from 21 to 32 names as Q2 season approaches (banks/airlines cluster inside 19d). The penalty is now the single largest re-ranking force — consistent with the 07-04/07-05 observation that calendar drift, not price drift, drives sleeve turnover in pre-earnings weeks.
- **Data-quality**: third consecutive zero-failure universe fetch (521/521); first live-session IBKR corroboration since 07-02 (max divergence 0.049%); ^IRX fresh same-day print. SATS produced no prints by ~12:40 ET and was screened out — worth one more day's observation before treating as delisting-related.
- The family-coverage gate blocked investability for every completed scoring run in the window (6th consecutive for this model).

## What Worked / What Failed

Worked: end-to-end live intraday pipeline on the 07-02 pattern (fetch → TI → score → publish in ~15 min); two-source + brokerage grounding at max 0.33% divergence; carry-forward bindings enforced mechanically; fresh-tape re-rank behaved sensibly (momentum family responded to the new bars rather than echoing the frozen ranking).
Failed / degraded: nothing new mechanically. Standing: two-family scoring (below); interim MoM Hit/Miss noise near zero alpha (UNH flipped on one benchmark session — expected behavior, but a reminder to read interim marks with error bars).

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds) — sixth consecutive run. Mandatory Track B work under the two-consecutive-flags rule (crossed 07-02).

## Proposed Change (exactly one — the mandatory item)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, sixth escalation.** Proposal unchanged from 07-01..07-05: amend rules.md §Evidence Thresholds #2 so that when a family is UNAVAILABLE universe-wide due to an unwired Enhancing feed, the threshold applies over sourceable families (all non-negative), with LOW confidence cap, DQ <= 0.80, and the 50% gross-exposure cap from §Input Classification. Governance reason for DEFER unchanged: the change alters investability semantics for all models and ships through an auto-merge pipeline no human has reviewed. **Settlement evidence starts Wednesday 2026-07-08 — deciding before then lets the first settled-evidence week run on a resolved spec.**

## Decision

**DEFER** (HUMAN_REVIEW; mandatory-work escalation, 6th consecutive). Freeze-criteria check: streak is DEFER-pending-human, not evidence-lack rejections; parameter mutation de facto frozen at 0 settled (< 20). Effective next step: Tuesday 2026-07-07 normal run; **Wednesday 2026-07-08 first settlement pass** (12 records, alpha-scored vs recorded SPY 728.31) → first realized calibration metrics.
