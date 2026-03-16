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
6. Execute `loop/00_orchestrator.md`.
7. The orchestrator invokes the remaining prompts in `loop/` in order.

## Agent Order

1. `loop/01_data_regime_agent.md`
2. `loop/02_factor_scoring_agent.md`
3. `loop/03_portfolio_construction_agent.md`
4. `loop/04_risk_committee_agent.md`
5. `loop/05_evolution_agent.md`

## State Machine

The run should behave like a state machine instead of a one-shot essay.

`PRECHECK -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

If a hard stop is hit at any stage, transition to:

`HALTED`

If the inputs are valid but no trade set meets the minimum quality bar, transition to:

`NO_TRADE`

## Self-Evolution Cycle

The system should improve itself without relaxing core safeguards.

Daily cycle:

1. Run the research pipeline.
2. Publish the dated output package in `output/<YYYY-MM-DD>/`.
3. After the close, compare realized behavior versus forecast.
4. Diagnose misses, false positives, missing data, and regime misclassification.
5. Propose bounded prompt or parameter changes.
6. Accept changes only if they pass the policy in `eval/evolution_policy.md`.
7. Log every accepted or rejected change in the daily evolution artifact.

## Non-Negotiable Rules

- Never fabricate live market data.
- If live or delayed market data is unavailable, explicitly switch to `ILLUSTRATIVE_MODE`.
- Never weaken risk limits in order to force a publishable portfolio.
- Never mutate protected rules in `eval/evolution_policy.md` without human approval.
- Always publish a clear `GO`, `NO_TRADE`, or `HALTED` run status.

## Deliverable Standard

Every daily run must produce:

1. A preflight and regime assessment.
2. A scored candidate set.
3. A portfolio proposal or explicit no-trade decision.
4. A risk committee decision.
5. A final report.
6. A close log.
7. An evolution log.

All naming, timing, and file outputs are defined in `output/daily_schedule.md` and `output/daily_output_spec.md`.
