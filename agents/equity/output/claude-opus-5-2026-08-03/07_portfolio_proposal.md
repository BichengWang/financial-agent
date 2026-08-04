# 07 — Portfolio Proposal — 2026-08-03

## Outcome: **no portfolio is proposed**

The investable set is empty (`05`, `06`), so there is nothing to size. Per
`agents.md § Portfolio Construction Agent`, the feasibility pre-check still runs and its evidence is
recorded, and per its Failure Rule a portfolio is never forced.

## Task 0 — constraint feasibility pre-check (run before any sizing)

Computed from already-fetched inputs over the 103-name pctl>=80 pool.

| Constraint | Computed | Band | Verdict |
|---|---|---|---|
| Minimum names under the 5% single-name cap | 20 | — | — |
| Attainable sleeve beta — minimum | -0.5565 | — | — |
| Attainable sleeve beta — maximum | +1.4240 | — | — |
| Portfolio beta band | [-0.5565, +1.4240] | 0.90 – 1.10 | **FEASIBLE** |
| Sectors represented in the pool | 9 | >= 4 for a 30% cap to be satisfiable | **FEASIBLE** |
| Largest single sector in the pool | Finance (32 names, 31.1%) | <= 30% after weighting | satisfiable by selection |

**The beta band is feasible this run** — the fourth consecutive run where it is. The
"provably infeasible sleeve" narrative from 2026-07-27 is specific to that day's pool and must be
recomputed every run rather than inherited; it would have been wrong here.

**`NO_TRADE` is therefore not a feasibility outcome.** It is an evidence outcome, decided upstream
at the threshold gate in `05`.

## Diagnostic sleeve (not a recommendation)

To keep the portfolio-level analytics honest rather than blank, the naive top-20 equal-weight
sleeve is computed from the same fetched history. It is a **diagnostic**: these names do not clear
the Evidence Thresholds, so this is not a proposal and no weights are recommended.

| Portfolio metric | Value | Cap / band | Check |
|---|---|---|---|
| Names | 20 | >= 5 | PASS |
| Weights | equal 5.00% | <= 5% single name | PASS |
| Expected mu (4-week) | +6.00% | — | — |
| Portfolio sigma (1-month) | 5.15% | — | — |
| Expected Sharpe | +1.1036 | — | — |
| Expected Information Ratio | +1.0501 | — | — |
| Tracking error (1-month) | 4.70% | — | — |
| VaR95 (1-month) | -2.50% | — | — |
| CVaR95 (1-month) | -4.62% | — | — |
| Portfolio beta to SPY | +0.5323 | 0.90 – 1.10 | **FAIL** |
| Average pairwise correlation | +0.1482 | < 0.45 | PASS |
| 95th-pctl 1-month drawdown | 8.50% | <= 8% | **FAIL** |
| Largest sector weight | Health Care 30.0% | <= 30% | PASS |

Two independent observations worth recording even though they change nothing today:

1. **Beta +0.5323 is far below the 0.90 floor.** A naive rank-ordered sleeve is defensively
   tilted — the deduplicated engine still favours low-beta, low-drawdown names. Reaching the band
   would require deliberate selection *within* the feasible range established above, not a different
   universe.
2. **The 95th-pctl drawdown estimate is 8.50%, over the 8% cap.** On its own that
   would be an independent `NO_TRADE` trigger under `rules.md § Downgrade to NO_TRADE` #5.

Formulas: portfolio sigma `sqrt(w' Σ w)` from the 60-day fetched covariance matrix scaled to one
month; 95th-pctl drawdown `1.65 x portfolio_sigma_1m` (normality assumed); tracking error the stdev
of beta-adjusted residual returns vs SPY over the same window scaled to one month; VaR95 / CVaR95
parametric per `rules.md § Ratio Definitions`. Inputs: `L-HIST`, `L-RM-*`.

## Sector table (diagnostic sleeve)

| Sector | Weight |
|---|---|
| Health Care | 30.0% |
| Finance | 20.0% |
| Consumer Discretionary | 20.0% |
| Technology | 20.0% |
| Industrials | 10.0% |

## Excluded names

Every name in the 512-name scored universe is excluded from a proposed portfolio,
because no portfolio is proposed. Within the ranked set, exclusion from the published 24 is purely
the post-penalty rank cut at rank 24 (percentile floor 95.50); exclusion from the
ranked set at all is the 60th-percentile floor of the mu Calibration Table. The three names excluded
from scoring entirely (FDXF, BF-B, Q) are itemised with reasons in `04`.
