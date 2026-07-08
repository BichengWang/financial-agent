# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-07 (Tuesday — live session; midday run) |
| Status | NO_TRADE |
| Regime | NEUTRAL |
| Evaluation window | 2026-06-30 → 2026-07-07, all models |
| Ledger status | 0 settled; 605 prior OPEN + 25 published this run; first settlements due **tomorrow, Wednesday 2026-07-08** (12 records, 06-10 vintage) |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-30..07-06 daily), gemini-3.5-flash (07-01, 07-06), claude-opus-4-8 (06-30), claude-sonnet-5 (07-02, 07-03), claude-fable-5 (07-01..07-06, this run).
- Statuses: NO_TRADE on all completed trading-day scoring runs; REVIEW_ONLY across the 07-03..07-05 closed days. Audit trail unbroken.
- **Momentum fragility observed live (new evidence today)**: yesterday's leaderboard rotation toward semis-adjacent momentum (SOXX +4.0% intraday on 07-06) fully reversed today (SOXX -7.0% intraday, MU -8.2%), while this engine's low-beta defensive core (DVA, BEN, TROW, ESS, MNST, LYV) held rank. Two live sessions produced two opposite-sign 4–8% swings in the same sleeve — direct, dated evidence that the 30d-realized-vol sigmas on high-beta names (15–22%) are not conservative padding but the actual operating environment. Tomorrow's settlement pass starts scoring whether the CI machinery priced this correctly.
- **Penalty machinery**: earnings-window penalties expanded from 32 to 35 names; the penalty is now visibly reshaping the top-20 (IBKR, WST, DOC, BAC, GE, LUV, UAL, AXP, STT, EW, CFG all pushed out today) — consistent with the standing observation that calendar drift, not price drift, drives sleeve turnover in pre-earnings weeks.
- **Data-quality**: fourth consecutive zero-failure universe fetch (521/521); IBKR live corroboration both live sessions this week (max divergence 0.168% today); ^IRX fresh same-day print. SATS: second consecutive session with no prints (last bar 2026-07-02) — if it prints nothing again tomorrow, log a structural exclusion note (delisting/halt suspected) rather than a daily staleness reject.
- The family-coverage gate blocked investability for every completed scoring run in the window (7th consecutive for this model).

## What Worked / What Failed

Worked: end-to-end live intraday pipeline (fetch → TI → score → publish in ~35 min; a slow sequential fetch was detected mid-run and replaced with an 8-worker threaded fetch — 10x faster, 521/521, zero failures); two-source + brokerage grounding at max 0.77% divergence; carry-forward bindings enforced mechanically; defensive re-rank on the fresh tape behaved sensibly (high-beta names de-ranked by Macro_Z and penalties, not by discretion).
Failed / degraded: the sequential fetch pattern inherited from prior runs degraded to ~10 symbols/min (rate-limiting suspected) — worth folding the threaded fetch into the standing runbook procedure notes; standing: two-family scoring (below); interim MoM Hit/Miss noise (UNH flipped for the third session running — expected near zero alpha, documented in 02 §6).

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds) — seventh consecutive run. Mandatory Track B work under the two-consecutive-flags rule (crossed 07-02).

## Proposed Change (exactly one — the mandatory item)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, seventh escalation.** Proposal unchanged from 07-01..07-06: amend rules.md §Evidence Thresholds #2 so that when a family is UNAVAILABLE universe-wide due to an unwired Enhancing feed, the threshold applies over sourceable families (all non-negative), with LOW confidence cap, DQ <= 0.80, and the 50% gross-exposure cap from §Input Classification. Governance reason for DEFER unchanged: the change alters investability semantics for all models and ships through an auto-merge pipeline no human has reviewed. **The first settled-evidence arrives tomorrow (2026-07-08); a decision this week would let the first realized-calibration cycle run on a resolved spec.**

## Decision

**DEFER** (HUMAN_REVIEW; mandatory-work escalation, 7th consecutive). Freeze-criteria check: streak is DEFER-pending-human, not evidence-lack rejections; parameter mutation de facto frozen at 0 settled (< 20). Effective next step: **Wednesday 2026-07-08 first settlement pass** (12 records: MCK, COST, WMT, CVX, UNH, MU, XOM, LIN, LLY, NVDA, GOOGL, ABBV — alpha-scored vs recorded SPY 728.31) → first realized calibration metrics (hit rate, CI coverage, mean z on n=12; rank IC needs the full vintage).
