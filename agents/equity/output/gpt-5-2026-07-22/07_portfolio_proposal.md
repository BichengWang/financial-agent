# 07 Portfolio Proposal — 2026-07-22

## Decision: NO_TRADE — no sizing attempted

The factor gate produces **zero investable names**: all 514 names have Fund_Z and Sent_Z unavailable, so none can satisfy three supportive families or the maximum-family-50% rule. Constraint-feasibility therefore stops before weights, correlation optimization, or Kelly sizing. Drafting a portfolio from monitoring names would violate the state machine and evidence thresholds.

| Required portfolio output | Result |
|---|---|
| Weights / sector shares | N/A — no investable set |
| Beta band 0.90–1.10 | N/A — no portfolio |
| Pairwise correlation <0.45 | N/A — no portfolio |
| Sharpe / Sortino / IR / tracking error | N/A — no portfolio |
| VaR95 / CVaR95 / 95th-pctl drawdown | N/A — no portfolio |
| Kelly cap | Candidate diagnostics are computed in `05`; no position is authorized |

Excluded-name rationale: all 26 published names are monitoring-only; all remaining names are below the published sleeve cutoff or lack a binding CARRY/PROMOTE decision. This is a composition/evidence failure and maps to NO_TRADE, not HALTED.
