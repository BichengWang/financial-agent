# 07 — Portfolio Proposal

## Decision: `NO_TRADE` — no weights are proposed

## Task 0 — constraint feasibility pre-check (before any sizing)

`agents.md § Portfolio Construction` requires this pre-check to run before weights are drafted,
so an infeasible set costs no revision pass.

| Constraint | Cap / band | Computed this run | Result | Ledger Rows |
|---|---|---|---|---|
| Portfolio beta to SPY | 0.90 – 1.10 | attainable -0.3876 … 1.3387 under the 5% single-name cap | **FEASIBLE** | `L026`, `L301`–`L324` |
| Average pairwise correlation | < 0.45 | 0.1699 (max pair 0.7287, WSM/SWK) | **PASS** | `L024` |
| 95th-pctl 1-month drawdown | <= 8% | 9.15% on the naive top-20 equal-weight sleeve | **FAIL** | `L025` |
| Max sector concentration | <= 30% | 41.67% Consumer Discretionary | **FAIL** | `L011` |
| Minimum investable count | >= 5 | 0 names clear the evidence thresholds | **FAIL** | `05` |

**The beta band is feasible and was recomputed, not inherited.** Attainable sleeve beta spans
-0.3876 to 1.3387, which
straddles the 0.90–1.10 band. This is the **sixth consecutive run** in which the 2026-07-27
"provably infeasible" narrative would have been wrong. The naive top-20 equal-weight sleeve's
own beta is 0.6129 — below the floor — but that is a property of
equal weighting, not of the opportunity set, and re-weighting toward the higher-beta members of
the >=80th-pctl pool reaches the band.

**Two constraints do fail independently of the evidence thresholds**: the 95th-percentile
1-month drawdown at 9.15% against the 8% cap, and
Consumer Discretionary concentration at 41.67% against the 30% cap.
Either alone forces `NO_TRADE` under `rules.md § Stop Criteria` downgrade #5 and #6. So even if
`Fund_Z` and `Sent_Z` were live tomorrow, this particular top-24 set would still need
re-weighting or trimming before it could be sized.

## Portfolio analytics (naive top-20 equal-weight reference sleeve)

These are computed for the feasibility check only. **No sleeve is proposed or sized.**

| Analytic | Value | Formula / basis | Ledger Rows |
|---|---|---|---|
| Names | 20 | top 20 by post-penalty `Adj Score` | `05` |
| Expected beta | 0.6129 | equal-weighted mean of 60d betas | `L301`–`L324` |
| Portfolio sigma (1m) | 5.55% | `sqrt(w' Sigma w) x sqrt(21)` on 60 daily adjusted returns | `L002`, `L024` |
| 95th-pctl 1m drawdown | 9.15% | `1.65 x portfolio_sigma_1m`; normality assumed | `L025` |
| Average pairwise correlation | 0.1699 | mean of the upper triangle | `L024` |
| Max pairwise correlation | 0.7287 (WSM/SWK) | max of the upper triangle | `L024` |
| Min pairwise correlation | -0.3297 | min of the upper triangle | `L024` |

Tracking error, Sharpe, Sortino, IR, VaR95 and CVaR95 are reported **per position** in
`05_factor_scores.md` and inherited unchanged; no portfolio-level aggregate of them is
computed, because aggregating them would imply a weighting scheme and no weights exist.

## Sector concentration (top 24, equal-weight reference)

| Sector | Names in top 24 | Share if equal-weighted | 30% cap |
|---|---|---|---|
| Consumer Discretionary | 10 | 41.67% | **BREACH** |
| Health Care | 6 | 25.00% | ok |
| Technology | 4 | 16.67% | ok |
| Finance | 2 | 8.33% | ok |
| Industrials | 2 | 8.33% | ok |

## Correlation matrix (top 20, 60 daily adjusted returns)

|  | DASH | ABNB | GEN | VEEV | HPQ | WSM | TECH | DXCM | CPAY | NTAP | BAX | GPN | MET | SWK | PH | PFE | TPR | FAST | INSM | GRMN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DASH | 1.00 | 0.49 | 0.36 | 0.50 | 0.15 | 0.20 | 0.19 | 0.19 | 0.33 | 0.09 | 0.29 | 0.46 | 0.16 | 0.24 | 0.07 | 0.05 | 0.23 | 0.03 | 0.07 | 0.10 |
| ABNB | 0.49 | 1.00 | 0.47 | 0.48 | 0.21 | 0.23 | 0.06 | 0.21 | 0.18 | -0.07 | 0.23 | 0.26 | -0.12 | 0.29 | -0.04 | 0.19 | 0.16 | 0.13 | -0.06 | 0.18 |
| GEN | 0.36 | 0.47 | 1.00 | 0.71 | 0.38 | 0.01 | -0.09 | 0.37 | 0.39 | 0.28 | 0.19 | 0.47 | 0.16 | 0.04 | -0.28 | 0.07 | -0.05 | 0.08 | -0.09 | 0.11 |
| VEEV | 0.50 | 0.48 | 0.71 | 1.00 | 0.41 | 0.00 | -0.00 | 0.37 | 0.52 | 0.19 | 0.18 | 0.45 | 0.16 | 0.01 | -0.33 | 0.17 | 0.06 | 0.18 | 0.03 | 0.24 |
| HPQ | 0.15 | 0.21 | 0.38 | 0.41 | 1.00 | 0.09 | -0.03 | 0.19 | 0.17 | 0.61 | -0.02 | 0.16 | 0.12 | 0.05 | -0.28 | 0.13 | -0.12 | 0.10 | -0.11 | 0.10 |
| WSM | 0.20 | 0.23 | 0.01 | 0.00 | 0.09 | 1.00 | 0.34 | 0.14 | 0.18 | 0.03 | 0.51 | 0.37 | 0.09 | 0.73 | 0.30 | 0.16 | 0.49 | 0.36 | 0.10 | 0.25 |
| TECH | 0.19 | 0.06 | -0.09 | -0.00 | -0.03 | 0.34 | 1.00 | 0.12 | -0.18 | 0.04 | 0.27 | 0.17 | -0.09 | 0.36 | 0.29 | -0.16 | 0.02 | 0.19 | 0.08 | 0.03 |
| DXCM | 0.19 | 0.21 | 0.37 | 0.37 | 0.19 | 0.14 | 0.12 | 1.00 | 0.33 | 0.08 | 0.32 | 0.23 | 0.16 | 0.10 | -0.06 | 0.06 | 0.15 | 0.17 | -0.08 | 0.14 |
| CPAY | 0.33 | 0.18 | 0.39 | 0.52 | 0.17 | 0.18 | -0.18 | 0.33 | 1.00 | 0.09 | 0.33 | 0.58 | 0.40 | 0.17 | -0.10 | 0.29 | 0.30 | 0.21 | 0.08 | 0.32 |
| NTAP | 0.09 | -0.07 | 0.28 | 0.19 | 0.61 | 0.03 | 0.04 | 0.08 | 0.09 | 1.00 | -0.14 | 0.02 | 0.03 | 0.08 | -0.01 | -0.16 | -0.06 | -0.04 | 0.06 | -0.03 |
| BAX | 0.29 | 0.23 | 0.19 | 0.18 | -0.02 | 0.51 | 0.27 | 0.32 | 0.33 | -0.14 | 1.00 | 0.42 | 0.33 | 0.48 | 0.08 | 0.16 | 0.34 | 0.30 | -0.08 | 0.38 |
| GPN | 0.46 | 0.26 | 0.47 | 0.45 | 0.16 | 0.37 | 0.17 | 0.23 | 0.58 | 0.02 | 0.42 | 1.00 | 0.34 | 0.39 | -0.02 | 0.18 | 0.27 | 0.13 | 0.02 | 0.26 |
| MET | 0.16 | -0.12 | 0.16 | 0.16 | 0.12 | 0.09 | -0.09 | 0.16 | 0.40 | 0.03 | 0.33 | 0.34 | 1.00 | -0.07 | 0.13 | 0.40 | 0.26 | 0.09 | 0.24 | 0.09 |
| SWK | 0.24 | 0.29 | 0.04 | 0.01 | 0.05 | 0.73 | 0.36 | 0.10 | 0.17 | 0.08 | 0.48 | 0.39 | -0.07 | 1.00 | 0.37 | -0.01 | 0.40 | 0.46 | -0.03 | 0.23 |
| PH | 0.07 | -0.04 | -0.28 | -0.33 | -0.28 | 0.30 | 0.29 | -0.06 | -0.10 | -0.01 | 0.08 | -0.02 | 0.13 | 0.37 | 1.00 | 0.05 | 0.31 | 0.35 | 0.56 | -0.12 |
| PFE | 0.05 | 0.19 | 0.07 | 0.17 | 0.13 | 0.16 | -0.16 | 0.06 | 0.29 | -0.16 | 0.16 | 0.18 | 0.40 | -0.01 | 0.05 | 1.00 | 0.29 | 0.23 | 0.14 | 0.07 |
| TPR | 0.23 | 0.16 | -0.05 | 0.06 | -0.12 | 0.49 | 0.02 | 0.15 | 0.30 | -0.06 | 0.34 | 0.27 | 0.26 | 0.40 | 0.31 | 0.29 | 1.00 | 0.18 | 0.22 | 0.19 |
| FAST | 0.03 | 0.13 | 0.08 | 0.18 | 0.10 | 0.36 | 0.19 | 0.17 | 0.21 | -0.04 | 0.30 | 0.13 | 0.09 | 0.46 | 0.35 | 0.23 | 0.18 | 1.00 | 0.10 | 0.14 |
| INSM | 0.07 | -0.06 | -0.09 | 0.03 | -0.11 | 0.10 | 0.08 | -0.08 | 0.08 | 0.06 | -0.08 | 0.02 | 0.24 | -0.03 | 0.56 | 0.14 | 0.22 | 0.10 | 1.00 | 0.03 |
| GRMN | 0.10 | 0.18 | 0.11 | 0.24 | 0.10 | 0.25 | 0.03 | 0.14 | 0.32 | -0.03 | 0.38 | 0.26 | 0.09 | 0.23 | -0.12 | 0.07 | 0.19 | 0.14 | 0.03 | 1.00 |

## Excluded names — rationale

| Group | Count | Rationale |
|---|---|---|
| All 511 scored names | 511 | no name clears evidence thresholds #2/#3/#4; exclusion is universal, not selective |
| Universe rejections | 4 | failed inclusion filters before scoring — see `04` rejection log |
| Names below the 60th pctl | 307 | `rules.md § mu Calibration Table` — not ranked in either sleeve, rejection log only |
| Names in the >=80th pool outside the published 24 | 78 | publication cut only; same threshold outcome |

## Failure rule

`agents.md § Portfolio Construction` failure rule applies: constraints cannot be met without
dropping below the minimum investable count of 5 — indeed the investable count is 0 — so the
agent recommends **`NO_TRADE`** and does not force a portfolio.
