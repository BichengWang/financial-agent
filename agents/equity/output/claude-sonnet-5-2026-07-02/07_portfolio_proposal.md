# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (Task 0, per `agents.md § Portfolio Construction Agent Prompt`)

Before any sizing: the investable set is empty (`06_top_candidates.md` — 0 of 30 names clear the Evidence Thresholds). There is no investable set whose beta band or sector caps could be evaluated for feasibility, because there is nothing to size. Per the portfolio agent's Task 0 directive: *"If the beta band or sector caps are infeasible for any weighting, recommend NO_TRADE immediately with the computed evidence — do not draft weights or spend the revision pass."* The same logic applies a fortiori to an empty investable set — **no weights are drafted.**

## Weights

**None.** No position is sized. `0%` gross, `0%` net, `100%` cash-equivalent (no live capital deployed against this run's output).

## Portfolio Analytics

| Metric | Value |
| --- | --- |
| Expected Sharpe | N/A — no portfolio |
| Expected Sortino | N/A — no portfolio |
| Information Ratio | N/A — no portfolio |
| Tracking Error | N/A — no portfolio |
| Expected Beta | N/A — no portfolio |
| VaR95 / CVaR95 | N/A — no portfolio |
| 95th-pctl 1-month Drawdown | N/A — no portfolio |
| Kelly cap-binding | N/A — no positions to bind |
| Sector concentration | N/A — no positions |
| Correlation matrix | N/A — no positions |
| Factor exposure summary | N/A — no positions |

## Per-Position Recommendation Metrics Table

**Empty — no investable positions.** The 12-name monitoring sleeve (`06_top_candidates.md`) is published for forecast auditability only and explicitly carries no sizing, per `rules.md § ILLUSTRATIVE_MODE`/`REVIEW_ONLY` conventions applied here even though this run is not illustrative: a monitored name is not an executable position.

## Why Every Candidate Was Excluded

All 30 sampled names were excluded from the investable set for the same structural reason: Fundamental and Sentiment/Positioning factor families are `UNAVAILABLE` for the entire sampled universe this session (no fundamentals or positioning feed connected — see `01_preflight.md`, `04_universe_summary.md`, `05_factor_scores.md`). Per `rules.md § Evidence Thresholds`, condition 2 ("at least 3 of 4 factor families are non-negative") requires three sourceable-and-non-negative families; only two families (Technical, Macro) are ever sourceable this run, so the ceiling is 2 of 4 for every name regardless of `Adj Score` or percentile. This is a data-access gap, not a judgment that any individual name (e.g. `MU`, `META`, `AMD` — the top 3 by score) lacks merit; it is a statement that the merit cannot be corroborated across enough independent factor families to meet the system's own investability bar.

A secondary, independent block: no earnings-calendar feed is connected, so `Days to Earnings` is `UNAVAILABLE` for every name (not confirmed-clear) — this alone would prevent any name from carrying more than `LOW`/`MEDIUM`-capped confidence even if the family-count gate were somehow satisfied.

## Failure Rule Applied

Per `agents.md § Portfolio Construction Agent Prompt § Failure Rule`: *"If constraints cannot be met without dropping below the minimum investable count, recommend NO_TRADE — never force a portfolio."* The minimum investable count (5, per `rules.md § Downgrade to NO_TRADE` #1) is not met (0 names qualify). **This artifact recommends `NO_TRADE`**, consistent with `06_top_candidates.md` and carried through to `08_risk_review.md` and `09_final_report.md`.

## Grounding Rules Compliance Note

No name was force-included, no cap was loosened, and no missing family was treated as neutral-or-positive to manufacture a feasible portfolio. Per `rules.md § Computed Risk Analytics`, beta/correlation/drawdown are marked "computable and required" *only when price history is fetchable* — here they were fetchable and were in fact computed for all 30 names (see `05_factor_scores.md`), but the missing Fundamental/Sentiment families are a separate, independent Evidence Threshold that computed technical/macro analytics cannot substitute for.
