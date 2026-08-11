# 07 — Portfolio Proposal

## Decision

**No portfolio is proposed.** The table below is a diagnostic equal-weight monitor sleeve,
not a recommended or executable allocation. Structural family gates fail before sizing; the
same diagnostic also breaches sector and drawdown caps.

## Task 0 feasibility pre-check

| Constraint | Required | Diagnostic | Result |
| --- | --- | --- | --- |
| Investable names | 5–10 | 0 | FAIL — no name clears family/DQ gates |
| Beta | 0.90–1.10 | EW top20 0.5342; attainable -0.3003…1.3530 | Current FAIL; range feasible |
| Max sector | <=30% | 35.0% | FAIL |
| Average correlation | <0.45 | 0.1867 | PASS |
| 95th-pctl drawdown | <=8% | 9.22% | FAIL |

## Diagnostic portfolio analytics

| Expected return | Sigma 1m | Beta | Tracking Error | Sharpe | Sortino | IR | VaR95 | CVaR95 | 95% DD | Kelly raw diagnostic | Kelly .25 uncapped | Per-name cap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6.00% | 5.59% | 0.5342 | 5.15% | 1.018 | 1.859 | 0.958 | -3.22% | -5.51% | 9.22% | 19.210 | 4.803 | 5.00% |

The calculation assumes 5% equal weights across all 20 monitors, 6.00% calibrated mu, 60d
adjusted-return covariance, 13-week bill/12 as rf, and a normal 1.65-sigma drawdown estimate
[L002,L007,L015,L024-L030]. Quarter Kelly exceeds 5% for 20/20 names, so the
single-name cap would bind if they were otherwise investable.

## Sector table

| Sector | Names | Share | Result |
| --- | --- | --- | --- |
| Consumer Discretionary | 7 | 35.0% | FAIL |
| Health Care | 6 | 30.0% | PASS |
| Finance | 3 | 15.0% | PASS |
| Technology | 3 | 15.0% | PASS |
| Industrials | 1 | 5.0% | PASS |

## Full 60d correlation matrix

| Ticker | NTAP | DXCM | CRL | ABNB | BAX | DASH | REGN | WSM | VEEV | COO | J | NTRS | TSCO | CPAY | PFE | TPR | ZS | EXPE | BX | WTW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NTAP | 1.00 | 0.10 | 0.06 | -0.05 | -0.14 | 0.08 | -0.10 | 0.03 | 0.20 | -0.25 | 0.09 | -0.07 | 0.05 | 0.11 | -0.15 | -0.05 | 0.28 | -0.04 | 0.09 | -0.18 |
| DXCM | 0.10 | 1.00 | -0.06 | 0.21 | 0.29 | 0.14 | 0.11 | 0.11 | 0.35 | 0.22 | 0.22 | -0.01 | 0.25 | 0.32 | 0.07 | 0.17 | 0.27 | 0.21 | 0.08 | 0.27 |
| CRL | 0.06 | -0.06 | 1.00 | 0.22 | 0.11 | 0.16 | 0.16 | 0.22 | 0.12 | 0.21 | 0.26 | 0.03 | 0.30 | 0.03 | 0.11 | 0.20 | -0.08 | 0.26 | 0.03 | -0.07 |
| ABNB | -0.05 | 0.21 | 0.22 | 1.00 | 0.22 | 0.45 | 0.23 | 0.21 | 0.48 | 0.19 | 0.08 | 0.17 | 0.21 | 0.18 | 0.21 | 0.17 | 0.24 | 0.49 | 0.21 | 0.20 |
| BAX | -0.14 | 0.29 | 0.11 | 0.22 | 1.00 | 0.26 | 0.37 | 0.49 | 0.16 | 0.56 | 0.23 | 0.22 | 0.18 | 0.31 | 0.17 | 0.35 | 0.01 | 0.31 | 0.36 | 0.56 |
| DASH | 0.08 | 0.14 | 0.16 | 0.45 | 0.26 | 1.00 | 0.23 | 0.19 | 0.47 | 0.12 | 0.14 | 0.10 | 0.30 | 0.29 | 0.04 | 0.22 | 0.16 | 0.50 | 0.23 | 0.26 |
| REGN | -0.10 | 0.11 | 0.16 | 0.23 | 0.37 | 0.23 | 1.00 | 0.15 | 0.08 | 0.23 | 0.05 | 0.20 | -0.16 | -0.04 | 0.37 | 0.27 | -0.09 | 0.31 | 0.16 | 0.26 |
| WSM | 0.03 | 0.11 | 0.22 | 0.21 | 0.49 | 0.19 | 0.15 | 1.00 | -0.02 | 0.26 | 0.41 | 0.22 | 0.17 | 0.15 | 0.16 | 0.49 | -0.12 | 0.43 | 0.37 | -0.03 |
| VEEV | 0.20 | 0.35 | 0.12 | 0.48 | 0.16 | 0.47 | 0.08 | -0.02 | 1.00 | 0.14 | 0.29 | -0.01 | 0.28 | 0.51 | 0.18 | 0.07 | 0.47 | 0.44 | 0.17 | 0.36 |
| COO | -0.25 | 0.22 | 0.21 | 0.19 | 0.56 | 0.12 | 0.23 | 0.26 | 0.14 | 1.00 | 0.23 | -0.02 | 0.24 | 0.19 | 0.25 | 0.27 | 0.06 | 0.29 | 0.18 | 0.28 |
| J | 0.09 | 0.22 | 0.26 | 0.08 | 0.23 | 0.14 | 0.05 | 0.41 | 0.29 | 0.23 | 1.00 | 0.25 | 0.27 | 0.23 | 0.24 | 0.21 | 0.21 | 0.23 | 0.48 | 0.24 |
| NTRS | -0.07 | -0.01 | 0.03 | 0.17 | 0.22 | 0.10 | 0.20 | 0.22 | -0.01 | -0.02 | 0.25 | 1.00 | -0.15 | 0.21 | 0.11 | 0.29 | 0.17 | 0.05 | 0.45 | 0.16 |
| TSCO | 0.05 | 0.25 | 0.30 | 0.21 | 0.18 | 0.30 | -0.16 | 0.17 | 0.28 | 0.24 | 0.27 | -0.15 | 1.00 | 0.20 | 0.15 | -0.01 | 0.08 | 0.07 | 0.28 | 0.14 |
| CPAY | 0.11 | 0.32 | 0.03 | 0.18 | 0.31 | 0.29 | -0.04 | 0.15 | 0.51 | 0.19 | 0.23 | 0.21 | 0.20 | 1.00 | 0.30 | 0.31 | 0.24 | 0.39 | 0.34 | 0.37 |
| PFE | -0.15 | 0.07 | 0.11 | 0.21 | 0.17 | 0.04 | 0.37 | 0.16 | 0.18 | 0.25 | 0.24 | 0.11 | 0.15 | 0.30 | 1.00 | 0.30 | -0.10 | 0.21 | 0.35 | 0.17 |
| TPR | -0.05 | 0.17 | 0.20 | 0.17 | 0.35 | 0.22 | 0.27 | 0.49 | 0.07 | 0.27 | 0.21 | 0.29 | -0.01 | 0.31 | 0.30 | 1.00 | 0.02 | 0.33 | 0.26 | -0.00 |
| ZS | 0.28 | 0.27 | -0.08 | 0.24 | 0.01 | 0.16 | -0.09 | -0.12 | 0.47 | 0.06 | 0.21 | 0.17 | 0.08 | 0.24 | -0.10 | 0.02 | 1.00 | 0.13 | 0.13 | 0.18 |
| EXPE | -0.04 | 0.21 | 0.26 | 0.49 | 0.31 | 0.50 | 0.31 | 0.43 | 0.44 | 0.29 | 0.23 | 0.05 | 0.07 | 0.39 | 0.21 | 0.33 | 0.13 | 1.00 | 0.16 | 0.18 |
| BX | 0.09 | 0.08 | 0.03 | 0.21 | 0.36 | 0.23 | 0.16 | 0.37 | 0.17 | 0.18 | 0.48 | 0.45 | 0.28 | 0.34 | 0.35 | 0.26 | 0.13 | 0.16 | 1.00 | 0.17 |
| WTW | -0.18 | 0.27 | -0.07 | 0.20 | 0.56 | 0.26 | 0.26 | -0.03 | 0.36 | 0.28 | 0.24 | 0.16 | 0.14 | 0.37 | 0.17 | -0.00 | 0.18 | 0.18 | 0.17 | 1.00 |

## Excluded-name rationale

All 20 are excluded from an executable set because `Fund_Z` and `Sent_Z` are unavailable,
live-family concentration is 66.67%, and DQ is below 0.85. TPR has the additional near-term
earnings penalty. The four universe rejections remain outside ranking entirely.
