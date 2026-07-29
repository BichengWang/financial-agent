# 07 Portfolio Proposal — 2026-07-29

## Outcome: **NO_TRADE** — no portfolio is proposed

## Task 0 — Constraint Feasibility Pre-Check (before any sizing)

Required by `agents.md § Portfolio Construction Agent` Task 0 (Track B, 2026-06-10, `HUMAN_REVIEW`):
compute the achievable sleeve-beta range and sector shares from already-fetched inputs *before*
drafting weights, so an infeasible set is caught without spending the revision pass.

| Input | Value | Source |
|---|---|---|
| Single-name cap | 5% NAV | `rules.md § Risk Controls` (protected) |
| Minimum names for a fully-invested sleeve | 20 | 1 / 0.05 |
| Pool at >= 80th percentile | 103 names | L041 |
| Mean of the 20 highest betas in that pool | **+0.9090** | L015, L045 |
| Required beta band | 0.90 – 1.10 | `rules.md § Risk Controls` (protected) |
| **Beta band attainable?** | **YES** | — |

**The beta band is attainable this run — by 90 basis
points.** This is a genuine change from 2026-07-27, when the same computation returned +0.8519 and the
sleeve was *provably* infeasible. It would be wrong to reuse that infeasibility narrative today, and it
is worth stating why the margin is so thin: 42.02% of the universe carries
negative beta (L015), and the top-10 ranked names average
-0.3790 beta. Reaching the 0.90 floor would require abandoning essentially the
entire top of the leaderboard in favour of the highest-beta names that qualify on percentile alone.

**So the beta band is not the binding constraint. The binding constraint is candidate quality.**

## Why no portfolio is constructed

`agents.md § Portfolio Construction` receives the **investable** set from factor scoring. That set is
**empty**: zero of 514 names clear `rules.md § Evidence Thresholds` (detail in `05`). Under
`rules.md § Downgrade to NO_TRADE` #1 — *fewer than 5 names pass the investable threshold* — the
correct output is `NO_TRADE`, and per `agents.md § Failure Rule` a portfolio is never forced.

Sizing, weights, and the correlation matrix are therefore **not applicable**, not omitted. Computing a
covariance matrix over a set that is not investable would imply a recommendation that the evidence does
not support.

| Required output | State |
|---|---|
| Weights | **N/A** — investable set empty |
| Expected Sharpe / Sortino / IR / tracking error | **N/A** — no positions |
| Expected beta | **N/A** — no positions; attainable range computed in Task 0 above |
| VaR95 / CVaR95 / 95th-pctl 1-month drawdown | **N/A** — no positions |
| Sector concentration table | Reported for the monitoring sleeve in `06`, **not** a portfolio |
| Correlation matrix | **N/A** — not computed for a non-investable set |
| Kelly cap-binding notes | Per-name `0.25 × Kelly` is in `05`; all 24 are cap-bound at the 5% single-name limit, which is a *sizing* input, not an investability grant |

## Excluded-name rationale

Every name is excluded from the portfolio for the same reason, and it is not name-specific: with
`Fund_Z` and `Sent_Z` `UNAVAILABLE` universe-wide (L046, L047), no name can satisfy evidence
thresholds #2, #3 or #4. The unblock is Phase 2 of
`agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` — bulk SEC `companyfacts.zip` plus
threaded Nasdaq sentiment across all 514 names — which is a tooling task, not a market judgment.

## Handoff to Risk Committee

Recommendation: **`NO_TRADE`**. All 24 monitoring-sleeve names carry complete, settleable
forecasts (2026-08-26 target date) so the run still produces auditable evidence.
