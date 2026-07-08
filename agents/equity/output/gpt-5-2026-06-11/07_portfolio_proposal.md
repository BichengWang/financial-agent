# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

Result: `NO_TRADE` before sizing. The investable-grade set cannot satisfy the protected beta band under the 5% single-name cap.

| Test | Result | Evidence |
|---|---|---|
| Candidate count | PASS | 8 investable-grade names, 9 monitoring names |
| Single-name cap | PASS | Every hypothetical name capped at 5% NAV |
| Sector cap | FAIL in equal 5% sleeve | Health Care would be 20.0% NAV / 50.0% gross |
| Protected NAV beta | FAIL | Max NAV beta from positive-beta investable names at 5% each = 0.199; required 0.90-1.10 |
| Gross-normalized high-beta cross-check | Informational | Top-five positive-beta investable names average beta 0.747, but only at 25% gross and not a NAV-compliant book |
| Avg pairwise correlation | PASS | Equal 5% investable-grade sleeve average pairwise correlation 0.120 |
| 95% one-month drawdown | PASS | Parametric 1.65 x one-month sleeve sigma = 2.91% |

## Hypothetical Equal 5% Sleeve (Rejected)

| Ticker | Weight | Beta | Sector |
|---|---:|---:|---|
| LLY | 5.0% | 0.73 | Health Care |
| CVX | 5.0% | -0.86 | Energy |
| UNH | 5.0% | 0.33 | Health Care |
| ABBV | 5.0% | 0.20 | Health Care |
| BAC | 5.0% | 0.64 | Financials |
| JNJ | 5.0% | 0.04 | Health Care |
| ANET | 5.0% | 1.76 | Information Technology |
| AMT | 5.0% | 0.27 | Real Estate |

## Sector Concentration

| Sector | Weight | Gross Share | Names |
|---|---:|---:|---|
| Energy | 5.0% NAV | 12.5% of gross | CVX |
| Financials | 5.0% NAV | 12.5% of gross | BAC |
| Health Care | 20.0% NAV | 50.0% of gross | LLY, UNH, ABBV, JNJ |
| Information Technology | 5.0% NAV | 12.5% of gross | ANET |
| Real Estate | 5.0% NAV | 12.5% of gross | AMT |

## Recommendation Metrics Table

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | 70% CI Lo | 70% CI Hi | Ledger Rows |
|---|---:|---|---|---:|---|---:|---:|---|---:|---:|---|
| LLY | 1163.72 | 2026-06-11 | DELAYED | 1233.54 | 2026-07-09 | 6.0% | 11.9% | REALIZED_VOL_30D | 1089.16 | 1377.92 | price/history/vol target rows in `01` |
| CVX | 188.14 | 2026-06-11 | DELAYED | 199.43 | 2026-07-09 | 6.0% | 7.4% | REALIZED_VOL_30D | 184.91 | 213.95 | price/history/vol target rows in `01` |
| UNH | 406.33 | 2026-06-11 | DELAYED | 430.71 | 2026-07-09 | 6.0% | 7.5% | REALIZED_VOL_30D | 398.91 | 462.51 | price/history/vol target rows in `01` |
| ABBV | 226.96 | 2026-06-11 | DELAYED | 238.30 | 2026-07-09 | 5.0% | 7.1% | REALIZED_VOL_30D | 221.46 | 255.14 | price/history/vol target rows in `01` |
| BAC | 55.11 | 2026-06-11 | DELAYED | 57.31 | 2026-07-09 | 4.0% | 6.4% | REALIZED_VOL_30D | 53.67 | 60.96 | price/history/vol target rows in `01` |
| JNJ | 239.59 | 2026-06-11 | DELAYED | 249.18 | 2026-07-09 | 4.0% | 5.7% | REALIZED_VOL_30D | 234.99 | 263.37 | price/history/vol target rows in `01` |
| ANET | 155.37 | 2026-06-11 | DELAYED | 160.03 | 2026-07-09 | 3.0% | 18.9% | REALIZED_VOL_30D | 129.51 | 190.55 | price/history/vol target rows in `01` |
| AMT | 190.50 | 2026-06-11 | DELAYED | 196.21 | 2026-07-09 | 3.0% | 8.7% | REALIZED_VOL_30D | 178.95 | 213.47 | price/history/vol target rows in `01` |
| GOOGL | 353.82 | 2026-06-11 | DELAYED | 371.51 | 2026-07-09 | 5.0% | 11.7% | REALIZED_VOL_30D | 328.60 | 414.42 | price/history/vol target rows in `01` |
| MCK | 791.80 | 2026-06-11 | DELAYED | 807.64 | 2026-07-09 | 2.0% | 8.9% | REALIZED_VOL_30D | 734.41 | 880.86 | price/history/vol target rows in `01` |
| GS | 1024.62 | 2026-06-11 | DELAYED | 1045.11 | 2026-07-09 | 2.0% | 10.2% | REALIZED_VOL_30D | 936.36 | 1153.87 | price/history/vol target rows in `01` |
| KO | 83.39 | 2026-06-11 | DELAYED | 85.05 | 2026-07-09 | 2.0% | 5.8% | REALIZED_VOL_30D | 80.02 | 90.09 | price/history/vol target rows in `01` |
| GE | 328.94 | 2026-06-11 | DELAYED | 335.52 | 2026-07-09 | 2.0% | 11.2% | REALIZED_VOL_30D | 297.08 | 373.96 | price/history/vol target rows in `01` |
| JPM | 313.91 | 2026-06-11 | DELAYED | 317.05 | 2026-07-09 | 1.0% | 6.4% | REALIZED_VOL_30D | 296.17 | 337.93 | price/history/vol target rows in `01` |
| ORCL | 182.33 | 2026-06-11 | DELAYED | 184.15 | 2026-07-09 | 1.0% | 20.1% | REALIZED_VOL_30D | 146.09 | 222.22 | price/history/vol target rows in `01` |
| PG | 149.34 | 2026-06-11 | DELAYED | 150.83 | 2026-07-09 | 1.0% | 7.2% | REALIZED_VOL_30D | 139.71 | 161.95 | price/history/vol target rows in `01` |
| COP | 117.31 | 2026-06-11 | DELAYED | 118.49 | 2026-07-09 | 1.0% | 8.8% | REALIZED_VOL_30D | 107.69 | 129.28 | price/history/vol target rows in `01` |

## Exclusion Note

No live weights are proposed. Adding monitoring names does not solve the NAV beta problem without admitting lower-ranked/high-beta names solely to satisfy beta, which would violate the objective function and evidence thresholds.
