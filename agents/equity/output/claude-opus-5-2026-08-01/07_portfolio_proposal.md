# 07 — Portfolio Proposal — 2026-08-01

## Result: **NO_TRADE — no portfolio is proposed**

`agents.md § Portfolio Construction Task 0` requires a constraint-feasibility pre-check
**before any sizing**. That pre-check ran, and it is reported in full below even though the
run never reached sizing — because the reason for `NO_TRADE` matters, and this run's reason
is *not* the one the previous runs recorded.

## Task 0 — constraint feasibility pre-check

| Constraint | Computed | Limit | Feasible? |
|---|---|---|---|
| Min names at the 5% single-name cap | 20 | — | — |
| Pool at/above the 80th pctl | 103 | ≥ 20 | **yes** |
| **Max attainable sleeve beta** | **+1.3556** | ≥ 0.90 floor | **yes** |
| **Min attainable sleeve beta** | **-0.5864** | ≤ 1.10 ceiling | **yes** |
| Beta band 0.90–1.10 | attainable range `[-0.5864, +1.3556]` | must intersect | **FEASIBLE** |

**The beta band is feasible.** The highest-beta names available in the ≥80th-pctl pool are
HPE (+2.586), RCL (+1.803), IVZ (+1.648), SWK (+1.550), ARES (+1.499), AMZN (+1.467) …, whose
top-20 mean is +1.3556 — comfortably above
the 0.90 floor. This is the **third consecutive run** in which the 2026-07-27 package's
"provably infeasible beta band" narrative would have been wrong. It is recomputed every run,
never inherited.

## Naive top-20 equal-weight sleeve — diagnostic only

Constructed purely to characterise the geometry of the leaderboard. **Not a proposal**; no
name is investable.

| Analytic | Value | Cap | Result |
|---|---|---|---|
| Portfolio beta | +0.4608 | 0.90–1.10 | **FAIL — too defensive** |
| Average pairwise correlation | 0.1282 | < 0.45 | **PASS** |
| Portfolio sigma (1m) | 4.49% | — | — |
| 95th-pctl 1-month drawdown | 7.41% | ≤ 8% | **PASS** |
| Max sector weight | Health Care 35.0% | ≤ 30% | **FAIL** |

| Sector | Weight | Cap | Result |
|---|---|---|---|
| Health Care | 35.0% | 30% | **BREACH** |
| Finance | 25.0% | 30% | ok |
| Technology | 20.0% | 30% | ok |
| Consumer Discretionary | 10.0% | 30% | ok |
| Industrials | 10.0% | 30% | ok |

Two independent caps break on the naive sleeve: portfolio beta +0.4608
falls **below** the 0.90 floor (the leaderboard is defensive, not risky), and
Health Care concentration reaches 35.0% against the 30% cap.
Both are *composition* failures, which `rules.md § Hard Halt Criteria` #5 explicitly routes
to `NO_TRADE` rather than `HALTED`. Correlation (0.1282) and
drawdown (7.41%) both pass with room.

Note the ordering of causes: even if both breaches were repaired by reweighting — and the
feasibility check shows beta *could* be — **the sleeve would still be unpublishable**,
because no constituent name clears the evidence thresholds. Portfolio geometry is not the
binding constraint this run.

## Computed risk analytics

All values below are computed from the fetched 60-day daily-return window on adjusted
closes, per `rules.md § Computed Risk Analytics`. `N/A - no validated engine` does not appear
anywhere in this package.

| Analytic | Method | Ledger |
|---|---|---|
| Beta | OLS slope of daily returns vs SPY, trailing 60 sessions | `L-RM-*`, `L-HIST` |
| Pairwise correlation | Pearson on the same 60-day window, all 20 names | `L-HIST` |
| Portfolio sigma (1m) | stdev of the equal-weighted portfolio return series × √21 | `L-HIST` |
| 95th-pctl 1m drawdown | 1.65 × portfolio sigma (normality stated) | derived |
| Tracking error | stdev of beta-adjusted residuals vs SPY × √21 | `L-RM-*` |
| VaR95 / CVaR95 | `mu − 1.65σ` / `mu − 2.06σ` (parametric, normality stated) | `L-RM-*` |
| 60d max drawdown | worst peak-to-trough over the 60-session window | `L-RM-*` |

## Excluded names

Every name outside the published 24 was excluded by rank, not by a portfolio
judgement — no sizing pass ran. The 2 universe-filter rejections
are itemised in `04`. Ranked names below the 60th percentile are, per
`rules.md § mu Calibration Table`, not ranked in either sleeve and appear only in the
rejection log.
