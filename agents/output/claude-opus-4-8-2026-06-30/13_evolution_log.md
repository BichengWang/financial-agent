# 13 Evolution Log

Run `claude-opus-4-8` · 2026-06-30 · Status NO_TRADE · Regime BULL(rotating) · Window 2026-06-23→06-30 · Baseline flag CROSS_MODEL_BASELINE · Ledger DQ 0.80.

## Review Window (trailing 7 days, all models)

Packages reviewed: `gpt-5-2026-06-24/28/29/30`, `gemini-3.5-flash-2026-06-29`, and this run. Settled predictions in window: **0** (the primary evidence base is empty — every ledger across history is still OPEN, earliest maturity 2026-07-08). Rolling calibration: `INSUFFICIENT_SETTLED_N` (hit rate / CI coverage / mean-z / rank-IC all unavailable).

## What Worked / What Failed

- **Worked:** Live-data grounding, source ledger, technical helper, and prediction-JSON emission completed cleanly across all models. Today's grounded MoM (02) validated the rotation thesis (defensive-quality +α, mega-cap-growth −α), and the factor model independently reproduced it.
- **Failed (recurring):** Portfolio construction. This is the **16th consecutive cross-model NO_TRADE** in the environment, every one blocked by the same mechanism — the investable-grade quality leadership carries rotation-distorted low/negative 60d beta, so the long-only book cannot reach the **0.90 beta floor** under the protected **5% single-name cap** (this run: max achievable beta 0.59 for the ≥80th set, 0.03 for the full-gate set; 07).

## Primary Diagnosis

`portfolio construction` — a protected-constraint feasibility wall, not a data/grounding failure. Two structural facts compound it: (a) 60d realized betas are distorted by a transient rotation (quality names that are normally ~0.8–1.0 beta print ~0 over the last 60 sessions); (b) the 5%-cap-vs-beta-band interaction has no compliant solution when the quality cohort is low-beta.

## Governance Findings (this is the substance of today's pass)

1. **Freeze Criteria #1 is now MET.** The last three+ evolution cycles (`gpt-5-2026-06-28`, `gpt-5-2026-06-29`, `gpt-5-2026-06-30`, `gemini-3.5-flash-2026-06-29`) all decided `NO_CHANGE_ACCEPTED` "for lack of settled evidence." Per `rules.md § Freeze Criteria`, three consecutive cycles rejecting all changes for lack of evidence → **freeze autonomous parameter mutation and require human review.** Declared below.
2. **The recurring blocker is MANDATORY Track B work the prior cycles wrongly closed.** Per `rules.md § Two-Track Change Classification`, "a spec inconsistency flagged in two consecutive evolution logs … is mandatory Track B work, not optional." The beta-band-vs-5%-cap feasibility wall has now been flagged in ≥4 consecutive logs and repeatedly dismissed as "no Track B needed." That dismissal was incorrect: the issue cannot be fixed by a Track A parameter change (blocked, <20 settled) and its root cause touches **two protected rules** (5% single-name cap, 0.90–1.10 beta band) that only human approval may alter. The correct action is to escalate it as a structured HUMAN_REVIEW item — which prior cycles omitted.

## Proposed Change (exactly one) — Track B, HUMAN_REVIEW

**Problem statement (artifact-cited):** `07_portfolio_proposal.md` (this run and 15 prior) shows max achievable portfolio beta (0.03–0.75) < the 0.90 floor for every quality-respecting investable set under the 5% cap. The system is in a permanent NO_TRADE dead-state in a low-beta-leadership regime, yet generates valid, well-grounded, positive-alpha forecasts it can never size.

**Change:** Amend `agents.md § Portfolio Construction Task 0` (constraint-feasibility pre-check) to require, every run, a **"Beta-Feasibility Verdict"** block in `07`/`00` reporting (i) max achievable long-only portfolio beta under the 5% cap, (ii) the gap to the 0.90 floor, and (iii) a **diagnostic blended 60d/252d beta** per investable name to reveal when the 60d realized beta is rotation-distorted. When ≥ 5 consecutive runs (any model) are NO_TRADE for beta-band infeasibility, raise a standing **HUMAN_REVIEW** item for the monthly structural review to rule on one of: (a) measuring the portfolio beta band on a longer/blended beta window; (b) canonizing the single-name-cap reading (sleeve-relative ≥ 20 names vs NAV-relative + cash); (c) affirming the band/cap as-is and accepting persistent NO_TRADE in this regime. **The official 60d beta used for the band check, the band values, and the 5% cap are unchanged — this adds a diagnostic and an escalation only.**

**Hypothesis:** The persistent NO_TRADE is substantially a 60d-beta-window artifact; exposing the blended beta and forcing the human-review decision will either unlock compliant GO books (if the band/window is revised by humans) or confirm the dead-state is intentional — either way it ends the silent loop.

**Validation (Track B three-condition standard):** (1) explicit problem citing the artifact (07, 16-run series) ✓; (2) weakens no protected rule or grounding gate — diagnostic + escalation only, official band check untouched ✓; (3) logged here with `HUMAN_REVIEW`, effective next run ✓. No Track A statistical holdout required (no scoring math changes).

## Decision

**DEFER → HUMAN_REVIEW**, and **FREEZE autonomous parameter mutation** (Freeze Criteria #1). The daily research loop continues unchanged (keep publishing grounded analysis + paper forecasts); no weights/thresholds/mu-table/Core-ETF-prior mutations until (a) human review resolves the beta-band/5%-cap question and (b) the first settlement wave (~2026-07-08) delivers ≥ 20 settled predictions enabling legitimate Track A calibration. The Track B "Beta-Feasibility Verdict + escalation" above is the one change advanced this pass; it is held for human ratification rather than auto-applied, consistent with the freeze.

**Effective next step:** (1) human review of the beta-band-vs-5%-cap structural tension using the computed evidence in 07; (2) at ~2026-07-08, re-open Track A calibration once predictions begin settling (watch CI coverage and rank IC first). `NO_CHANGE_ACCEPTED` is **not** logged this run — unlike the prior three cycles, the recurring blocker is escalated rather than silently re-deferred.
