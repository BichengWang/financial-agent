# 13 Evolution Log — 2026-07-21 (claude-fable-5, intraday run)

Per `rules.md § Mutation Logging Standard`. One proposed change this run (Track B), tested and **accepted**.

## Run Context

- Date/status: 2026-07-21, NO_TRADE (16th consecutive scoring run on the family-coverage gate); regime NEUTRAL with HIGH_VOL watch (unchanged 4th session); intraday (~15:10-15:30 ET) full-pipeline fire.
- Evaluation window: trailing 7 calendar days, all models — claude-fable-5 07-17/07-20/07-21 (this run), gpt-5 07-17/07-20. No other model has run in the window.
- Ledger status: canonical settlement ledger unchanged from 07-20 — `due_inventory = 0`, 175 EQ + 30 MF canonical, 0 conflicts. Source Ledger 155 rows, 0 UNAVAILABLE Required rows (1 UNAVAILABLE row is FDXF, a documented universe exclusion, not a Required-input gap).
- Baseline flag: `BASELINE_WINDOW_GAP` (`02 §1`).
- **Priority override status:** weighted rank IC −0.049 ≤ 0 over ≥20 settled remains active (unchanged from 07-20, since no new settlements occurred). No new evidence exists to re-test the 07-20 Core-ETF mu-shrink proposal meaningfully — retesting against identical data would reproduce an identical REJECT with no informational content, so this run does not repeat that test (see Standing Items).

## What Worked / What Failed

- **Worked, and a notable state change:** Yahoo v8 chart API is unblocked this session — 521/521 symbols fetched cleanly in ~37s (8-worker threaded), a marked change from the five prior sessions (07-13 through 07-20) which found Yahoo 429-blocked and used Nasdaq historical bulk as primary. Two per-symbol repairs were needed (SATS→ECHO rename, `L` transient empty-fetch race) but both were caught and fixed before scoring — no bad data reached the ledger.
- Worked: the two-pass bounded earnings preflight (`rules.md § Input Classification` #4) found zero second-pass entrants — the post-penalty top-20 was a strict subset of the pre-fetched top-60 shortlist, so no additional fetch pass was needed. This is the cleanest earnings-preflight outcome logged since the 2-pass procedure was codified (2026-07-12).
- Worked: SHADOW fundamental/sentiment diagnostics (`fundamental_diagnostics.py`, `sentiment_diagnostics.py`) ran with 100% sourceability on today's 20-name shortlist, consistent with the 2026-07-16 validation run — the tooling itself remains healthy, only universe-scale coverage (Phase 2) is the blocker.
- Failed / no new evidence: `due_inventory = 0` means the equity and market-forecast rolling calibration metrics are byte-identical to 07-20 (EQ hit 51.4%/CI 77.1%/mean z −0.236/rank IC −0.049; MF hit 20.0%/CI 60.0%/mean z −0.772). No fresh signal on whether the 07-20 REJECTed MF mu-shrink hypothesis would perform differently.
- Cross-model divergence: none observable this window — no other model has published since 07-20.

## Primary Diagnosis

**Output clarity / source grounding** (not factor calibration this run, given no new settlement evidence to re-diagnose calibration with). While reviewing `05`'s Sortino column before publication, found that the prior two sessions' Sortino figures were computed with the same `sigma` (total realized vol) used for Sharpe, rather than `rules.md § Ratio Definitions`'s own specification: *"Sortino: (mu - rf_1m) / downside_sigma_1m, where downside sigma uses negative daily returns from the fetched lookback and is scaled to 1 month."* This made Sortino a duplicate of Sharpe in every published table to date rather than a distinct downside-risk-adjusted metric — a genuine spec-compliance gap, not a scoring or protected-rule issue.

## Exactly One Proposed Change — Track B (process/computation correctness), tested and applied

**Problem statement:** `05_factor_scores.md`'s Sortino column (and the underlying `finalize.py` computation this run) used total `REALIZED_VOL_30D` sigma as a stand-in for downside deviation, disclosed as an approximation rather than computed per spec. This is a process/computation-fidelity gap exposed by this run's own draft artifact, not a scoring-weight or threshold change.

**Change:** compute downside deviation directly — standard deviation of only the negative daily returns in the trailing 30-trading-day window, scaled by `sqrt(21)` — and use it as the Sortino denominator, per `rules.md § Ratio Definitions` verbatim. Applied to all 20 published names this run before publication (not deferred to next run).

**Track B acceptance standard (three conditions):**
1. Explicit problem statement citing the artifact that exposed it — this run's own draft `05` Sortino column, cross-checked against `rules.md § Ratio Definitions`. ✔
2. Does not weaken a protected rule or any grounding gate — this is a metric-computation fix, not a change to factor weights, evidence thresholds, or risk caps. Confirmed. ✔
3. Logged here with `HUMAN_REVIEW` flag, effective this run. ✔ **HUMAN_REVIEW: recommended — verify the downside-deviation window (last 30 trading days) and minimum-sample floor (3 negative observations) are the right defaults; no protected rule is touched either way.**

**Decision: ACCEPT.** All 20 published names recomputed successfully (≥3 negative-return observations in the trailing 30d window for every name); Sortino values now diverge meaningfully from Sharpe (e.g., TRV: Sharpe 0.482 vs Sortino 1.299 — the asymmetric-risk signal the metric is supposed to carry). **Effective immediately** (this run's own `05`/`09`); future runs should compute Sortino this way by default rather than reverting to the sigma-proxy placeholder.

## Standing Items (not new proposals)

- **Fundamental/Sentiment unwiring — 16th consecutive run.** Phase-2 bulk fetch (full-universe `companyfacts.zip` + threaded Nasdaq sentiment across ~514 names) remains the binding constraint on ever publishing GO (`agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`); not attempted this run.
- **Core ETF mu-prior calibration (Track A, escalated 07-20 for the 2026-07-31 structural review):** MF hit rate 20% over n=30, mean z −0.77, remains a documented open problem requiring a regime→prior mapping review (protected-table change, needs human approval). No new settlement evidence this run to advance it further; carried forward unchanged.
- **Yahoo-unblocked status is provisional** — one clean session is not proof the 429-blocking is permanently resolved; the fetch pipeline should keep the Nasdaq-bulk fallback path warm rather than removing it, per the 2026-07-13 Track B precedent.
- Freeze criteria: not met. Accepted changes: 07-16, 07-17, and today (07-21); one REJECT (07-20, on a distinct Track A hypothesis). No oscillation, no three-in-a-row reject streak.
