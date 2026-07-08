# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-02 |
| Status | NO_TRADE |
| Regime | NEUTRAL (second consecutive dispersion-shock session under a calm index) |
| Evaluation window | 2026-06-25 → 2026-07-02, all models |
| Ledger status | 0 settled; 369 prior OPEN + 26 published this run; first settlements due 2026-07-08 |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (06-28, 06-29, 06-30, 07-01, 07-02), gemini-3.5-flash (06-29, 07-01), claude-opus-4-8 (06-30), claude-fable-5 (07-01, this run).
- Every completed run: **NO_TRADE**. The blocking reason has now converged across models: gpt-5-07-02 ("no ranked name reaches the ≥85% data-completeness investable threshold") and both fable index-union runs (family threshold #2 unsatisfiable) are the same underlying gap — no fundamental/sentiment feed.
- Universe migration is now visible cross-model: fable runs use the 513-name union; gpt-5 continues on a sampled set — leaderboard overlap remains low, confirming sample-selection distortion (flagged 07-01).
- Regime calls agree (NEUTRAL) and the two-day unwind (SOXX −6.41% then −7.19% intraday) is showing up in every model's dispersion notes.

## What Worked / What Failed

Worked: second clean index-union run; LIVE intraday grounding (two web sources + brokerage MCP, max divergences 0.635%/0.18%); reflection caught a real rules breach and corrected the engine (see below); 26 more settleable records (open ledger now ~395 records across 22 vintages).
Failed: (1) the investable gate remains structurally closed — same as 07-01, now cross-model; (2) **rules breach found in our own 07-01 output**: the UNH record stacked −2pp (earnings) and −1pp (exhaustion) mu shades = −3pp total, exceeding the Calibration Table's ±2pp per-name cap. Corrective action this run: the engine clamps total adjustment at ±2pp (a compliance fix enforcing an existing protected-adjacent rule, not a rules mutation; the 07-01 record stands and settles as recorded — rewriting a published prediction would be worse than the breach). The 07-01 risk review missed it — checklist item #9/#10 reviewers should verify shade arithmetic against the band, not just the presence of stated reasons.

## Primary Diagnosis

**Data quality** (absent fundamental/sentiment feeds), unchanged — with the spec-consistency corollary now flagged for the **second consecutive run**: §Family Aggregation's "UNAVAILABLE families do not count toward the 3-of-4 test" makes §Evidence Thresholds #2 unsatisfiable whenever Enhancing family feeds are unwired, contradicting §Input Classification's "Enhancing inputs never block GO by themselves." Per §Evolution Policy, a spec inconsistency flagged in two consecutive evolution logs is **mandatory Track B work**.

## Proposed Change (exactly one — mandatory per two-consecutive-flags rule)

**Track B (spec-consistency), decision: DEFER — HUMAN_REVIEW, escalated.** Same proposal as 2026-07-01, unchanged in substance: amend rules.md §Evidence Thresholds #2 with "when a factor family is UNAVAILABLE universe-wide because its feed is unwired, threshold #2 applies over the sourceable families (all must be non-negative), confidence caps at LOW, DQ ≤ 0.80, and gross exposure caps at 50% per §Input Classification." Why still DEFER rather than autonomous ACCEPT, despite Track B's effect-next-run provision: the change alters investability semantics for every model in this repo, the shipping pipeline auto-merges without human eyes, and no human has yet reviewed the first flag (raised yesterday). Autonomous adoption through an unreviewed auto-merge would honor the letter of Track B while defeating the purpose of its HUMAN_REVIEW flag. **Escalation:** the inconsistency is now recorded in 00 (blockers), 08 (concern #13-adjacent), 09 (executive summary), and this log — if the human operator approves, the amendment is one sentence and takes effect the following run.

## Decision

**DEFER** (HUMAN_REVIEW, mandatory-work escalation recorded). Track A remains locked (0 settled < 20). Effective next step: 2026-07-06 run is business as usual; **2026-07-08 run must execute the first settlement pass** (12 records, entry vintage 2026-06-10) and report the system's first realized calibration metrics.
