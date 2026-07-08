# 13 Evolution Log

## Run Context

- **Date:** 2026-07-03
- **Model:** claude-sonnet-5
- **Status:** `NO_TRADE`
- **Regime:** `BULL` (MEDIUM confidence)
- **Evaluation window:** trailing 7 calendar days (2026-06-26 through 2026-07-03), all models, per `rules.md § Evolution Policy § Review Cadence`
- **Ledger status:** 0 settled predictions system-wide (`INSUFFICIENT_SETTLED_N`); 22 open `15_predictions.json` files scanned, 395 open records, earliest `target_date` 2026-07-08
- **Baseline flag:** `CROSS_MODEL_BASELINE`

## Review Window Scan

Folders dated within the trailing 7 days across all models: `gpt-5-2026-06-28`, `gpt-5-2026-06-29`, `gpt-5-2026-06-30`, `gemini-3.5-flash-2026-06-29`, `claude-fable-5-2026-07-01`, `gpt-5-2026-07-01`, `gemini-3.5-flash-2026-07-01`, `gpt-5-2026-07-02`, `claude-fable-5-2026-07-02`, and this run (`claude-sonnet-5-2026-07-03`). No settled predictions exist in any of these — the review window has no realized-vs-forecast evidence to compare this cycle.

## What Worked

- The IBKR MCP integration is fully functional as a grounded price source (5-year daily history + live snapshots), including corner cases (index/VIX contract resolution).
- A genuine data-integrity issue (duplicate `MU`/`SNDK` series from IBKR) was caught by an explicit pairwise-duplicate check before it propagated into scoring — this validates the value of the check itself as a standing safeguard.
- Documented fallback discipline held: the Sampled Universe Protocol was invoked only after confirming the Yahoo block and the IBKR-at-scale infeasibility, not for convenience, and disclosed consistently across `00/01/03/04/08`.

## What Failed / Gaps

1. **No cross-sectional fundamental or sentiment/positioning feed.** This is the single largest recurring failure mode across this run and (per the prior `gpt-5-2026-07-01`/`gpt-5-2026-07-02` packages referenced in `02_reflection.md`) prior runs in this system: `Fund_Z`/`Sent_Z` are `UNAVAILABLE` universe-wide, which mechanically blocks `GO` via the family-count evidence gate regardless of the quality of the Technical/Macro evidence. This is a **data-source gap**, not a scoring-methodology gap.
2. **Yahoo Finance is blocked in this session's egress policy**, forcing full reliance on IBKR and a 30-name Sampled Universe Protocol rather than the full 515-name union for technicals — a **process/environment gap**.

## Primary Diagnosis

**Source grounding** (the fundamental/sentiment feed gap) is the primary and recurring miss category — not data quality of what *is* sourced, not regime classification, not factor construction, not portfolio construction, and not risk review. The Technical/Macro pipeline is working correctly and consistently produces well-differentiated, ledger-backed scores; it simply cannot single-handedly clear a 4-family evidence bar designed around a fuller data stack.

## Proposed Change (Track B — Process)

**Classification:** Track B (Process change — no scoring math is being altered; this proposes a sequencing/procedure fix, not a weight or threshold change). Does not require settled-prediction evidence.

1. **Problem statement, citing the exposing artifact:** `05_factor_scores.md § Investable Subset` and `07_portfolio_proposal.md § Task 0` (this run), consistent with the same pattern documented in `gpt-5-2026-07-02/05_factor_scores.md § Metric Availability Table` and `gpt-5-2026-07-01`'s equivalent section — three consecutive daily packages across two different models show the identical `Fund_Z`/`Sent_Z` `UNAVAILABLE` root cause blocking `GO`. Per `rules.md § Two-Track Change Classification`: *"A spec inconsistency flagged in two consecutive evolution logs... is mandatory Track B work, not optional."* This is the analogous case for a recurring data-source gap flagged across ≥2 consecutive runs.
2. **Proposed change:** Add an explicit **Enhancing-Feed Reconnaissance step** to the Orchestrator's `PRECHECK` stage in `agents.md § Orchestrator Agent Prompt`: before declaring `Fund_Z`/`Sent_Z` `UNAVAILABLE`, the run must attempt at least one lightweight, session-appropriate probe for fundamental/sentiment signal (e.g., IBKR's `get_price_snapshot` `misc_statistics`/`historical_vol`/`implied_vol_underlying`/`cumulative_perf_*` fields, which were available but not used for scoring this run, or a WebSearch-based earnings-surprise/analyst-revision spot-check for the top-N ranked names) and document the attempt (success or explicit failure) in the Source Ledger, rather than marking the family `UNAVAILABLE` by default without an attempt. This does not weaken any protected rule, evidence threshold, or grounding gate — it only adds a mandatory attempt-and-document step before the existing `UNAVAILABLE` fallback, which remains available when the probe genuinely fails.
3. **Cannot weaken a protected rule or grounding gate:** Confirmed — this proposal adds a documentation/attempt requirement; it does not touch the family weights, the evidence thresholds, the mu Calibration Table, or any position/portfolio cap.
4. **Validation (Track B three-condition standard):** (a) explicit problem statement above, citing the exposing artifacts across two models' consecutive runs; (b) does not weaken any protected rule or grounding gate (confirmed above); (c) logged here with `HUMAN_REVIEW` flag, takes effect next run unless reverted.
5. **Decision: `DEFER`.** This proposal is logged for human review before adoption, per the `HUMAN_REVIEW` flag requirement — it changes what the Orchestrator's `PRECHECK` stage must attempt, which is a meaningful process change even though it is Track B, and a human should confirm the specific IBKR `misc_statistics`/`cumulative_perf_*` fields are an acceptable Enhancing-signal probe before it becomes standard practice.
6. **Effective date if accepted:** Next run following human sign-off.

## Limit Check

Exactly one Track B proposal logged this run, per `rules.md § Two-Track Change Classification` limit ("at most one Track B change per run"). No Track A proposal is made — 0 settled predictions exist, so no Track A acceptance standard (holdout IR/hit-rate/drawdown deltas) can be evaluated.

## Freeze Criteria Check

Not frozen. This is the first `claude-sonnet-5` evolution cycle; no history of 3 consecutive rejected-for-lack-of-evidence cycles or 2 consecutive performance-worsening accepted changes exists for this model yet.
