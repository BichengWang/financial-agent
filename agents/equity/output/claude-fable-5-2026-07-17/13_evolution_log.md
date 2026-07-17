# 13 Evolution Log — 2026-07-17 (claude-fable-5, at-the-close run)

Per rules.md §Mutation Logging Standard. One Track B entry this run (within the "at most one Track B change per run" limit).

## Run Context

- Date/status: 2026-07-17, NO_TRADE (14th consecutive scoring run on the family-coverage gate); regime NEUTRAL with HIGH_VOL watch.
- Evaluation window: trailing 7 calendar days, all models — gpt-5 07-11..07-17 dailies, claude-fable-5 07-12..07-15, claude-haiku-4.5 07-16, gemini-3.5-flash 07-13.
- Ledger status: canonical settlement ledger healthy (119 EQ + 18 MF, 0 conflicts, due 0); Source Ledger 199 rows, 0 UNAVAILABLE-row violations.
- Baseline flag: BASELINE_WINDOW_GAP (02 §1).

## What Worked / What Failed (forecast vs realized, cross-model)

- Worked: the canonical settlement ledger is doing its job — the same-day pre-open (gpt-5) and at-the-close (this) runs composed cleanly: 63 settlements this morning, zero double-settlement this evening, due inventory exactly 0 both times.
- Worked: equity CI coverage 79.8% remains inside the healthy band across 119 canonical settlements; the sigma chain (REALIZED_VOL_30D) is not mis-scaled.
- Worked: the at-the-close fire produced the stack's first real 12_close_log and same-day-close entry basis; the two same-date packages (pre-open + at-close) bracket one session for future timing-sensitivity analysis.
- Failed / watch: weighted rank IC −0.0088 (n=119) — the composite is not demonstrably predictive; five consecutive negative gpt-5 June vintages (gpt-5 07-17 13). MF direction accuracy 33.3% (n=18, below the n=20 Track A bar). The 07-15→07-17 MoM theme reversal (MU +6.6% → −7.2% alpha in three sessions) shows monthly verdicts are window-timing sensitive — reflected in 02 §6, not a rule change.
- Cross-model divergence: none material this week — every model's run reached NO_TRADE on the same structural gate; regime calls agree (NEUTRAL); the haiku 07-16 shadow run cleared Phase 1 governance without promotion (rules.md §SHADOW).

## Primary Diagnosis

**Data quality** (missing-fetch procedure class): the run fired at 15:59 ET, but Nasdaq's historical table does not publish the same-day close until well after the bell (still absent at 16:45 ET). Without a documented at-the-close path, an evening run must either fall back to yesterday's closes (staler entries than necessary, and weekend settlements reference the Friday close) or improvise a close source ad hoc — exactly the failure class the 07-13 Track B (Nasdaq-bulk fallback) existed to prevent for the pre-open case.

## Exactly One Proposed Change — Track B (process / missing-fetch procedure), HUMAN_REVIEW

**Problem (artifact):** this run's fetch chain had to derive the procedure live (today_close_fetch_manifest.json): the historical endpoint served only ≤07-16 bars all session.

**Change:** codify the **at-the-close data path** for runs firing ≥15:59 ET: (1) bulk 5y history from the Nasdaq historical endpoint (through the prior close); (2) append the same-day official close per name from the Nasdaq quote-info `secondaryData` block **only when its timestamp carries the "Closed at [today] 4:00 PM ET" marker**, with volume from the summary endpoint's ShareVolume and the vendor PreviousClose cross-checked against the prior bar (ex-div artifacts disclosed); (3) verify published names against IBKR daily bars (tool source per the Price Sourcing Standard); (4) settle any due `target_date = run_date` predictions at that same-day official close under the primary settlement rule (the close exists at run time) — `TARGET_EQ_RUN_DATE` remains reserved for genuinely pre-close executions. No scoring math, factor weight, mu table, protected limit, or settlement-precedence rule changes.

**Hypothesis:** future evening/at-close runs reproduce today's basis (entry = same-day verified official close) instead of degrading to prior-close entries or improvising, eliminating one recurring source of entry-basis heterogeneity between same-day packages.

**Validation (Track B three-condition standard):** (1) problem statement cites this run's manifests; (2) no protected rule or grounding gate is weakened — the marker requirement plus IBKR verification is stricter than the two-web-source floor; (3) logged here with HUMAN_REVIEW, effective next run unless reverted.

**Decision: ACCEPT** (Track B; the one change this run).

## Standing Items (not new proposals)

- **Fundamental/Sentiment feed unwiring — 14th consecutive run**; standing HUMAN_REVIEW escalation (Phase 2 bulk `companyfacts.zip` + threaded Nasdaq sentiment across the full universe, per `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`) remains the binding constraint on ever publishing GO. The 07-16 haiku shadow run satisfied Phase 1 governance; promotion still requires ≥70% universe sourceability.
- Calibration watch (rank IC ≤ 0): gpt-5's same-day Track A proposal was deferred for lack of a valid holdout; nothing new settled since (due 0), so no re-test is possible this run. Priority-override note: CI coverage is healthy, so the mandatory-calibration trigger (CI < 55%) is not active; the IC trigger sustains the MEDIUM cap only.
- Freeze criteria: not met (accepted changes 07-14, 07-15, 07-16 lineage all functioning; no oscillation).
