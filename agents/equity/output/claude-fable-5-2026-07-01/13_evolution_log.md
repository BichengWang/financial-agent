# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-01 |
| Status | NO_TRADE |
| Regime | NEUTRAL (with active factor-rotation shock) |
| Evaluation window | 2026-06-24 → 2026-07-01, all models |
| Ledger status | 0 settled system-wide; 308 prior OPEN records + 27 published this run; first settlements due 2026-07-08 |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-24, 06-28, 06-29, 06-30), gemini-3.5-flash (06-29, partial 07-01), claude-opus-4-8 (06-30), claude-sonnet-4-6 (partial 07-01: universe files only, run aborted), claude-fable-5 (this run).
- **Every completed run in the window published NO_TRADE**, but for two different reasons: gpt-5/opus runs (34-name sampled universe) failed on portfolio beta feasibility; this run (first completed index-union run after fix #286) failed earlier, at the family-coverage evidence gate.
- Cross-model divergence is diagnostic: gpt-5-06-30's sampled top names (GOOGL, CAT, LLY, UNH, GE, BAC…) barely overlap this run's index-union leaders (DVA, HUM, FFIV, MAS, BEN…) — the fixed 34-name sample systematically missed the mid/large-cap defensive leadership the full union surfaces. This validates the universe fix as the correct prior change.
- Regime calls agree across models (NEUTRAL), and today's tape (SOXX −6.41% vs SPY −0.14%) confirms the dispersion-over-direction read.

## What Worked / What Failed

Worked: index-union pipeline end-to-end (515 → 513 scored, 5y bars, dense indicator packs); two-source price grounding (max divergence 0.845%) plus brokerage-MCP corroboration; 27 settleable forecasts — largest single-run ledger contribution to date; reflection produced binding, evidence-cited carry decisions.
Failed: the investable bar is unreachable — with no fundamental/sentiment feed, §Family Aggregation ("UNAVAILABLE families do not count toward the 3-of-4 test") makes evidence threshold #2 unsatisfiable at index-union scale, where per-name INFERRED family scores cannot be produced symmetrically for 513 names. Also: the 2026-06-10 MU shade (crowding-unwind, −2pp) was directionally right but ~3 weeks early, costing ~13pp interim alpha on paper — unsettled, so no calibration action is permitted yet.

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds) with a spec-consistency corollary: §Input Classification promises Enhancing inputs "never block GO by themselves," but their absence zeroes two families and threshold #2 then blocks GO structurally — the exact "permanent dead state" §Input Classification warns against. First formal flagging of this inconsistency (if flagged again next run it becomes mandatory Track B work per policy).

## Proposed Change (exactly one)

**Track B (spec-consistency clarification), decision DEFER — HUMAN_REVIEW required.** Proposal: amend rules.md §Evidence Thresholds #2 with: "When a factor family is UNAVAILABLE universe-wide because its feed is unwired (an Enhancing-input gap), threshold #2 applies over the sourceable families (all must be non-negative), confidence is capped LOW, DQ ≤ 0.80, and gross exposure is capped at 50% per §Input Classification." Rationale: restores reachability of GO consistent with §Input Classification's intent without weakening any protected rule. Because it changes investability semantics (adjacent to Track A territory), autonomous adoption is inappropriate: **DEFER pending human approval**; logged with HUMAN_REVIEW flag. Validation once adopted would be observational: compare investable-set size and realized IR of runs before/after across ≥20 settled predictions.

## Decision

**DEFER** (HUMAN_REVIEW). No autonomous mutation applied this run; Track A remains locked (0 settled predictions < 20). Effective next step: run the 2026-07-08 settlement pass on the 2026-06-10 vintage — the system's first realized-vs-forecast evidence — and re-flag the threshold inconsistency if it binds again.
