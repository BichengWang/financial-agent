# 05 Factor Scores

Percentiles are `SAMPLED_PCTL (n=42)`. Data quality multiplier is 0.90 where quote cross-check, history, and earnings-date rows are present. Confidence is capped at `MEDIUM` because options, short-interest, and full analyst-revision feeds are unavailable.

## Ranked Candidate Table

| Rank | Ticker | Sector | Family Z Scores | Composite Z | DQ | Penalty | Adj Score | Pctl | Sleeve |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | LLY | Health Care | Fund +0.69/Tech +2.46/Sent +2.25/Macr +2.33 | 1.856 | 0.90 | 0.00 | 1.670 | 100.0 | INVESTABLE_GRADE |
| 2 | CVX | Energy | Fund +2.64/Tech +0.33/Sent +0.43/Macr -0.27 | 0.958 | 0.90 | 0.00 | 0.862 | 97.6 | INVESTABLE_GRADE |
| 3 | UNH | Health Care | Fund +0.14/Tech +1.30/Sent +0.84/Macr +2.02 | 0.944 | 0.90 | 0.00 | 0.850 | 95.2 | INVESTABLE_GRADE |
| 4 | ABBV | Health Care | Fund -0.52/Tech +1.44/Sent +1.47/Macr +1.92 | 0.933 | 0.90 | 0.00 | 0.840 | 92.9 | INVESTABLE_GRADE |
| 5 | GOOGL | Communication Services | Fund +5.08/Tech -0.76/Sent -1.03/Macr -0.82 | 0.916 | 0.90 | 0.00 | 0.824 | 90.5 | MONITOR |
| 6 | BAC | Financials | Fund +0.08/Tech +1.04/Sent +1.10/Macr +0.95 | 0.753 | 0.90 | 0.00 | 0.678 | 88.1 | INVESTABLE_GRADE |
| 7 | JNJ | Health Care | Fund -0.52/Tech +0.95/Sent +1.08/Macr +1.79 | 0.668 | 0.90 | 0.00 | 0.601 | 85.7 | INVESTABLE_GRADE |
| 8 | ANET | Information Technology | Fund +0.09/Tech +1.04/Sent +1.36/Macr -0.11 | 0.661 | 0.90 | 0.00 | 0.595 | 83.3 | INVESTABLE_GRADE |
| 9 | AMT | Real Estate | Fund -0.15/Tech +1.19/Sent +1.14/Macr +0.36 | 0.652 | 0.90 | 0.00 | 0.587 | 81.0 | INVESTABLE_GRADE |
| 10 | MCK | Health Care | Fund -0.52/Tech +0.85/Sent +1.20/Macr +1.62 | 0.645 | 0.90 | 0.00 | 0.581 | 78.6 | MONITOR |
| 11 | GS | Financials | Fund -0.14/Tech +0.90/Sent +0.80/Macr +0.81 | 0.553 | 0.90 | 0.00 | 0.497 | 76.2 | MONITOR |
| 12 | KO | Consumer Staples | Fund -0.21/Tech +0.98/Sent +0.90/Macr +0.41 | 0.516 | 0.90 | 0.00 | 0.465 | 73.8 | MONITOR |
| 13 | GE | Industrials | Fund +0.36/Tech +0.92/Sent +0.79/Macr -0.57 | 0.493 | 0.90 | 0.00 | 0.443 | 71.4 | MONITOR |
| 14 | JPM | Financials | Fund -0.09/Tech +0.40/Sent +0.48/Macr +0.99 | 0.362 | 0.90 | 0.00 | 0.326 | 69.0 | MONITOR |
| 15 | ORCL | Information Technology | Fund +0.22/Tech +0.93/Sent +0.41/Macr -0.43 | 0.381 | 0.90 | 0.04 | 0.303 | 66.7 | MONITOR |
| 16 | PG | Consumer Staples | Fund -0.47/Tech +0.59/Sent +0.59/Macr +0.74 | 0.295 | 0.90 | 0.00 | 0.266 | 64.3 | MONITOR |
| 17 | COP | Energy | Fund -0.02/Tech +0.36/Sent +0.54/Macr -0.39 | 0.179 | 0.90 | 0.00 | 0.161 | 61.9 | MONITOR |
| 18 | PLD | Real Estate | Fund -0.50/Tech +0.32/Sent +0.24/Macr +0.70 | 0.112 | 0.90 | 0.00 | 0.101 | 59.5 | REJECTED |
| 19 | V | Financials | Fund -0.15/Tech +0.10/Sent +0.03/Macr +0.65 | 0.089 | 0.90 | 0.00 | 0.080 | 57.1 | REJECTED |
| 20 | AAPL | Information Technology | Fund -0.30/Tech +0.17/Sent +0.04/Macr +0.29 | 0.015 | 0.90 | 0.00 | 0.014 | 54.8 | REJECTED |
| 21 | RTX | Industrials | Fund +0.45/Tech -0.16/Sent -0.00/Macr -0.48 | 0.014 | 0.90 | 0.00 | 0.012 | 52.4 | REJECTED |
| 22 | XOM | Energy | Fund -0.08/Tech +0.05/Sent +0.14/Macr -0.31 | -0.021 | 0.90 | 0.00 | -0.019 | 50.0 | REJECTED |
| 23 | SO | Utilities | Fund -0.03/Tech +0.15/Sent +0.22/Macr -0.82 | -0.035 | 0.90 | 0.00 | -0.031 | 47.6 | REJECTED |
| 24 | HD | Consumer Discretionary | Fund -0.53/Tech +0.23/Sent +0.38/Macr -0.74 | -0.106 | 0.90 | 0.00 | -0.095 | 45.2 | REJECTED |
| 25 | DUK | Utilities | Fund -0.11/Tech +0.01/Sent +0.12/Macr -0.90 | -0.136 | 0.90 | 0.00 | -0.123 | 42.9 | REJECTED |

## Investable-Grade Subset

Names must clear the 80th percentile, have at least 3 of 4 factor families non-negative, and pass data completeness. This is an investable-grade research subset, not an approved portfolio.

| Ticker | Pctl | Support | Beta | 30D RVol | Earnings Date | Confidence | Primary Driver |
|---|---:|---:|---:|---:|---|---|---|
| LLY | 100.0 | 4/4 | 0.73 | 11.9% | 2026-07-30 | MEDIUM | Fund +0.69/Tech +2.46/Sent +2.25/Macr +2.33 |
| CVX | 97.6 | 3/4 | -0.86 | 7.4% | 2026-07-31 | MEDIUM | Fund +2.64/Tech +0.33/Sent +0.43/Macr -0.27 |
| UNH | 95.2 | 4/4 | 0.33 | 7.5% | 2026-08-04 | MEDIUM | Fund +0.14/Tech +1.30/Sent +0.84/Macr +2.02 |
| ABBV | 92.9 | 3/4 | 0.20 | 7.1% | 2026-07-30 | MEDIUM | Fund -0.52/Tech +1.44/Sent +1.47/Macr +1.92 |
| BAC | 88.1 | 4/4 | 0.64 | 6.4% | 2026-07-14 | MEDIUM | Fund +0.08/Tech +1.04/Sent +1.10/Macr +0.95 |
| JNJ | 85.7 | 3/4 | 0.04 | 5.7% | 2026-07-15 | MEDIUM | Fund -0.52/Tech +0.95/Sent +1.08/Macr +1.79 |
| ANET | 83.3 | 3/4 | 1.76 | 18.9% | 2026-08-04 | MEDIUM | Fund +0.09/Tech +1.04/Sent +1.36/Macr -0.11 |
| AMT | 81.0 | 3/4 | 0.27 | 8.7% | 2026-08-04 | MEDIUM | Fund -0.15/Tech +1.19/Sent +1.14/Macr +0.36 |

## Monitoring Sleeve

| Ticker | Pctl | Reason | mu band | Confidence |
|---|---:|---|---:|---|
| GOOGL | 90.5 | Fails 3-of-4 family confirmation | 5.0% | LOW |
| MCK | 78.6 | Below investable percentile | 2.0% | LOW |
| GS | 76.2 | Below investable percentile | 2.0% | LOW |
| KO | 73.8 | Below investable percentile | 2.0% | LOW |
| GE | 71.4 | Below investable percentile | 2.0% | LOW |
| JPM | 69.0 | Below investable percentile | 1.0% | LOW |
| ORCL | 66.7 | Below investable percentile | 1.0% | LOW |
| PG | 64.3 | Below investable percentile | 1.0% | LOW |
| COP | 61.9 | Below investable percentile | 1.0% | LOW |

## Near-Miss Rejections

| Ticker | Pctl | Reason |
|---|---:|---|
| PLD | 59.5 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
| V | 57.1 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
| AAPL | 54.8 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
| RTX | 52.4 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
| XOM | 50.0 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
| SO | 47.6 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
| HD | 45.2 | Below 60th percentile or insufficient cross-family support for a settleable sleeve forecast. |
