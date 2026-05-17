# Quantitative Equity Research Prompt System — v3.0

This directory is the entrypoint for a modular, multi-agent, self-evolving prompt system for short-horizon U.S. equity selection.

The design replaces a single monolithic prompt with a controlled workflow:

- `loop/` contains executable agent prompts.
- `eval/` contains shared research rules, evaluation rubrics, stop criteria, and evolution governance.
- `output/` contains the daily run schedule, artifact specification, and output templates.

## Primary Goal

Generate the best **5-10 U.S. equity long candidates** for a **2-6 week horizon** while optimizing for:

1. Expected 1-month Information Ratio.
2. Portfolio coherence under explicit risk limits.
3. Reliability of the research process over headline conviction.

If fewer than 10 names pass the required thresholds, return fewer names. Never fill the list just to hit a target count.

## Execution Model

Use one orchestrator agent plus five specialist agents.

1. Load `eval/research_system.md`.
2. Load `eval/stop_criteria.md`.
3. Load `eval/evolution_policy.md`.
4. Load `output/daily_schedule.md`.
5. Load `output/daily_output_spec.md`.
6. Execute a named `Reflection` stage before new forecasting work begins.
7. Execute `loop/00_orchestrator.md`.
8. The orchestrator invokes the remaining prompts in `loop/` in order.

## Reflection Stage

Before scoring the current day, the orchestrator must perform a dedicated month-over-month (MoM) reflection and publish it as a **standalone artifact** named `02_reflection.md` in the dated output folder.

The reflection uses:

1. the prior same-model dated output package from roughly one month earlier,
2. the current run's draft context and available market evidence, and
3. realized outcome observations (prices, returns, regime changes) available as of the current run date.

The baseline to use is always the most recent same-model run from approximately one month prior. For the April 16, 2026 claude-sonnet-4-6 run, the required baseline is:

`/Users/mac/my-code/diary/investments/equity/output/claude-sonnet-4-6-2026-03-16/`

If no same-model prior run exists, fall back to the most recent available run of any model:

`/Users/mac/my-code/diary/investments/equity/output/claude-opus-4-6-2026-03-16/`

### Required Sections in `02_reflection.md`

The artifact must contain the following sections in order:

#### 1. Prior Run Summary
- Prior run date, model, and final status (GO / NO_TRADE / REVIEW_ONLY / HALTED)
- Prior regime classification
- Prior portfolio or monitoring basket (names and weights/allocations)
- Prior composite scores (top 5)

#### 2. MoM Price & Return Table
A mandatory table comparing prior entry prices against current prices for every name that appeared in the prior portfolio or top-5 candidate list. Use this exact schema:

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | Hit / Miss | Notes |
|--------|-----------|-------------|--------------|---------------|-----------|-----------|-------|

- **Hit**: name delivered positive return AND the research thesis was directionally correct.
- **Miss**: name delivered negative return OR thesis was directionally wrong.
- **Neutral**: name was flagged REVIEW_ONLY and no position was taken.
- If exact prices are unavailable, state `APPROX` and use best available estimate with source note.

#### 3. Theme-Level Performance Summary
Evaluate each research theme from the prior run (e.g., AI infrastructure, power/electrification, financials) and state whether the theme validated, partially validated, or failed over the one-month window. Include quantitative evidence where available.

#### 4. Regime Shift Assessment
Compare the prior regime classification against the current regime. Explain what changed (macro conditions, VIX, rates, sector rotation) and what that implies for today's factor weightings.

#### 5. Carry-Forward Decisions
A mandatory table with an explicit decision for every name and theme from the prior run:

| Ticker / Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---------------|------------|-------------|-----------|----------|-----------|

Valid decisions: `CARRY` / `DOWNGRADE` / `DROP` / `PROMOTE` (names added to today's watchlist due to MoM evidence).

#### 6. Reflection Sign-Off
- Data quality note (LIVE / APPROX / UNAVAILABLE for each price used)
- Confidence in the reflection (HIGH / MEDIUM / LOW) with rationale
- Any structural issues discovered (missing data, regime misclassification in prior run, etc.)

### Reflection Governance Rules

- The reflection must be completed before any new factor scoring begins (state machine enforces REFLECTION before DATA_OK).
- If prior output folder is missing or empty, document the gap in `02_reflection.md` and proceed with `NO_PRIOR_BASELINE` flag.
- Never fabricate prior prices. If unavailable, mark as `APPROX` with a clear source note.
- The carry-forward decisions in `02_reflection.md` are binding inputs to the `02_factor_scoring_agent.md` — names marked DROP are excluded from today's scored set unless new evidence overrides.

## Agent Order

0. `Reflection` (orchestrator-owned) → produces `02_reflection.md`
1. `loop/01_data_regime_agent.md` → produces `03_regime_and_data.md`
2. `loop/02_factor_scoring_agent.md` → produces `04_universe_summary.md` + `05_factor_scores.md` (uses carry-forward decisions from `02_reflection.md`)
3. `loop/03_portfolio_construction_agent.md` → produces `06_top_candidates.md` + `07_portfolio_proposal.md`
4. `loop/04_risk_committee_agent.md` → produces `08_risk_review.md`
5. `loop/05_evolution_agent.md` → produces `13_evolution_log.md`

## State Machine

The run should behave like a state machine instead of a one-shot essay.

`PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

If a hard stop is hit at any stage, transition to:

`HALTED`

If the inputs are valid but no trade set meets the minimum quality bar, transition to:

`NO_TRADE`

## Self-Evolution Cycle

The system should improve itself without relaxing core safeguards.

Daily cycle:

1. Perform the prior-month reflection before new scoring begins.
2. Run the research pipeline.
3. Publish the dated output package in `output/{model-name}-{YYYY-MM-DD}/`.
4. After the close, compare realized behavior versus forecast.
5. Diagnose misses, false positives, missing data, and regime misclassification.
6. Propose bounded prompt or parameter changes.
7. Accept changes only if they pass the policy in `eval/evolution_policy.md`.
8. Log every accepted or rejected change in the daily evolution artifact.

## Non-Negotiable Rules

- Never fabricate live market data.
- If live or delayed market data is unavailable, explicitly switch to `ILLUSTRATIVE_MODE`.
- Never weaken risk limits in order to force a publishable portfolio.
- Never mutate protected rules in `eval/evolution_policy.md` without human approval.
- Always publish a clear `GO`, `NO_TRADE`, or `HALTED` run status.

## Deliverable Standard

Every daily run must produce the following numbered artifacts in the dated output folder `output/{model-name}-{YYYY-MM-DD}/`:

| # | Artifact | Owner | Required |
|---|---------|-------|---------|
| 00 | `00_run_manifest.md` | Orchestrator | Always |
| 01 | `01_preflight.md` | Orchestrator | Always |
| **02** | **`02_reflection.md`** | **Orchestrator (Reflection Stage)** | **Always — MoM comparison table mandatory** |
| 03 | `03_regime_and_data.md` | Data/Regime Agent | Always |
| 04 | `04_universe_summary.md` | Factor Scoring Agent | Always |
| 05 | `05_factor_scores.md` | Factor Scoring Agent | Always |
| 06 | `06_top_candidates.md` | Portfolio Construction Agent | Always |
| 07 | `07_portfolio_proposal.md` | Portfolio Construction Agent | Always |
| 08 | `08_risk_review.md` | Risk Committee Agent | Always |
| 09 | `09_final_report.md` | Orchestrator | Always |
| 10 | `10_midday_monitor.md` | Orchestrator | Scheduled |
| 11 | `11_preclose_check.md` | Orchestrator | Scheduled |
| 12 | `12_close_log.md` | Orchestrator | Scheduled |
| 13 | `13_evolution_log.md` | Evolution Agent | Always |

The `02_reflection.md` artifact (MoM comparison) is the most critical new addition. It must be completed before any new factor scoring begins and its carry-forward decisions are binding inputs to the factor scoring agent.

All naming, timing, and file outputs are defined in `output/daily_schedule.md` and `output/daily_output_spec.md`.
