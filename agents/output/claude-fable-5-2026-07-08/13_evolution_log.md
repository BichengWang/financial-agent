# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-08 (Wednesday — live session; early-afternoon run) |
| Status | NO_TRADE |
| Regime | NEUTRAL |
| Evaluation window | 2026-07-01 → 2026-07-08, all models |
| Ledger status | **12 settled (first pass)**; 641 prior OPEN + 26 published this run; next due 2026-07-09 (17 records, first gpt-5 vintage) |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (07-01..07-07 daily), gemini-3.5-flash (07-01, 07-06), claude-sonnet-5 (07-02, 07-03), claude-fable-5 (07-01..07-07, this run).
- Statuses: NO_TRADE on all completed trading-day scoring runs; REVIEW_ONLY across the 07-03..07-05 closed days. Audit trail unbroken.
- **First realized evidence (new today)**: the 2026-06-10 vintage settled 6/12 HIT with a striking internal split — the vintage's *investable-grade* names (MCK, COST, WMT, CVX, UNH: 2 HIT/3 MISS) underperformed its *monitor-band* names (MU, LIN, LLY, ABBV: 4/4 HIT + XOM/NVDA/GOOGL 0/3), producing rank IC **-0.51**. Sigma quality: CI coverage 58.3% (in-band), mean z -0.265 (healthy) — the *intervals* were priced roughly right while the *ordering* was wrong. The June 10 book was scored under HIGH_VOL with a heavy defensive tilt; the misses (COST, WMT, CVX, XOM) were all "defensive/hedge" theses that de-rated as vol normalized — a regime-transition ordering error, not a vol-estimation error.
- **Momentum fragility follow-through**: yesterday's -7.0% SOXX break bounced +1.4% today — the two-session swing pattern flagged on 07-07 continues; 30d-realized-vol sigmas on high-beta names (17–23%) remain the operating environment, and today's CI-coverage evidence (58.3%, no OUT_CI on any high-sigma name) supports the current sigma sourcing.
- **Data quality**: fifth consecutive zero-failure universe fetch (521/521, threaded 8-worker — now the standing procedure per the 07-07 note); IBKR live corroboration 0.163%; ^IRX fresh print. **SATS**: third consecutive session without prints → structural exclusion logged (delisting/halt suspected); stop treating as a daily staleness reject.
- Family-coverage gate blocked investability for every completed scoring run in the window (8th consecutive for this model).

## What Worked / What Failed

Worked: first settlement pass executed cleanly against all 34 ledgers (12/12 due records settled, zero parse failures, all prices two-source grounded); the carry-forward mechanism earned realized validation (LLY/ABBV/LIN all HIT); the penalty machinery correctly held UNH out through its noisy interim window (settled +2.47% HIT but flip-flopped daily — the event-window exclusion was the right call for a 7d-to-earnings name); threaded fetch now standard (~96s for 521 symbols).
Failed / degraded: rank IC -0.51 on the first vintage (ordering inverted within the vintage — see diagnosis); standing two-family scoring gap (below); nothing new broke operationally.

## Primary Diagnosis

**Factor calibration** (new, evidence-backed at n=12) now sits alongside the standing **data quality** diagnosis (absent fundamental/sentiment feeds, 8th consecutive run). The two are linked: with only Tech+Macro sourceable, the score is a pure momentum/low-vol composite, and the settled vintage says that composite ordered a regime-transition month backwards. n=12 is below the ≥20 floor for Track A action and below the ≥20 floor for the §Priority Override (rank IC ≤ 0 trigger) — so no parameter change is permissible yet; the correct move is to let the 07-09 (n+17) and 07-12 (n+20) settlements accumulate and re-test.

## Proposed Change (exactly one — the mandatory item)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, eighth escalation.** Proposal unchanged from 07-01..07-07: amend rules.md §Evidence Thresholds #2 so that when a family is UNAVAILABLE universe-wide due to an unwired Enhancing feed, the threshold applies over sourceable families (all non-negative), with LOW confidence cap, DQ <= 0.80, and the 50% gross-exposure cap from §Input Classification. Governance reason for DEFER unchanged: the change alters investability semantics for all models and ships through an auto-merge pipeline no human has reviewed. **New context for the human reviewer**: the first settled vintage shows the two-family composite ordering realized alpha inversely (rank IC -0.51, n=12). If that persists at n≥29 (post 07-09) it *strengthens* the case for keeping the gate closed until a calibration fix lands — i.e., the settled evidence may resolve this DEFER on its merits within the week. Flagging both readings so the review is not one-sided.

## Decision

**DEFER** (HUMAN_REVIEW; mandatory-work escalation, 8th consecutive). Freeze-criteria check: streak is DEFER-pending-human, not evidence-lack rejections; Track A mutation remains de facto frozen at 12 settled (< 20). Effective next step: **Thursday 2026-07-09 settlement pass (17 records — first cross-model vintage)** → cumulative n=29 → re-test rank IC and hit rate; observe DAL print vs its 1d-buffered penalty; if cumulative rank IC ≤ 0 at n ≥ 20, the §Priority Override activates and the next proposal must be a calibration change (score weighting / mu table), superseding the family-coverage item.
