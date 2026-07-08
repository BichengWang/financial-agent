# 04 Universe Summary

## Sampled Universe Protocol

The run uses a deterministic 42-name sampled universe because no full U.S. screen is wired. It includes prior carry-forward/monitor names, 2-3+ large liquid names from every GICS sector, and current watchlist names. All 42 names have grounded prices and Nasdaq 60-day history.

| Sector | Names | Count |
|---|---|---:|
| Communication Services | META, GOOGL, NFLX | 3 |
| Consumer Discretionary | AMZN, TSLA, HD, AZO | 4 |
| Consumer Staples | WMT, COST, PG, KO | 4 |
| Energy | XOM, CVX, COP | 3 |
| Financials | JPM, BAC, GS, V | 4 |
| Health Care | LLY, UNH, JNJ, ABBV, MCK | 5 |
| Industrials | GE, CAT, RTX, GEV | 4 |
| Information Technology | MSFT, NVDA, AAPL, AVGO, ANET, ORCL | 6 |
| Materials | LIN, APD, SHW | 3 |
| Real Estate | PLD, AMT, EQIX | 3 |
| Utilities | NEE, SO, DUK | 3 |

## Inclusion Checks

| Ticker | Sector | Entry Price | Hist Rows | 20D Dollar Volume | Bid/Ask Spread | Result |
|---|---|---:|---:|---:|---:|---|
| LLY | Health Care | 1163.72 | 71 | $3769.6M | 0.11% | PASS |
| CVX | Energy | 188.14 | 71 | $1724.6M | 0.02% | PASS |
| UNH | Health Care | 406.33 | 71 | $2919.9M | 0.04% | PASS |
| ABBV | Health Care | 226.96 | 71 | $1221.5M | 0.03% | PASS |
| GOOGL | Communication Services | 353.82 | 71 | $11295.9M | 0.01% | PASS |
| BAC | Financials | 55.11 | 71 | $2178.5M | 0.02% | PASS |
| JNJ | Health Care | 239.59 | 71 | $1890.8M | 0.04% | PASS |
| ANET | Information Technology | 155.37 | 71 | $1539.2M | 0.13% | PASS |
| AMT | Real Estate | 190.50 | 71 | $612.2M | 0.05% | PASS |
| MCK | Health Care | 791.80 | 71 | $968.8M | 0.04% | PASS |
| GS | Financials | 1024.62 | 71 | $2340.0M | 0.04% | PASS |
| KO | Consumer Staples | 83.39 | 71 | $1348.7M | 0.01% | PASS |
| GE | Industrials | 328.94 | 71 | $1581.9M | 0.07% | PASS |
| JPM | Financials | 313.91 | 71 | $2737.1M | 0.03% | PASS |
| ORCL | Information Technology | 182.33 | 71 | $4207.7M | 0.05% | PASS |
| PG | Consumer Staples | 149.34 | 71 | $1280.3M | 0.02% | PASS |
| COP | Energy | 117.31 | 71 | $757.8M | 0.02% | PASS |
| PLD | Real Estate | 147.91 | 71 | $524.2M | 0.07% | PASS |
| V | Financials | 321.06 | 71 | $2557.0M | 0.03% | PASS |
| AAPL | Information Technology | 295.74 | 71 | $15029.4M | 0.01% | PASS |
| RTX | Industrials | 183.88 | 71 | $1053.9M | 0.07% | PASS |
| XOM | Energy | 148.52 | 71 | $2466.5M | 0.03% | PASS |
| SO | Utilities | 94.25 | 71 | $542.1M | 0.02% | PASS |
| HD | Consumer Discretionary | 324.06 | 71 | $1756.1M | 0.02% | PASS |
| DUK | Utilities | 125.31 | 71 | $404.3M | 0.02% | PASS |
| EQIX | Real Estate | 1045.37 | 71 | $568.8M | 0.06% | PASS |
| COST | Consumer Staples | 979.42 | 71 | $2460.1M | 0.03% | PASS |
| LIN | Materials | 516.32 | 71 | $1217.9M | 0.06% | PASS |
| MSFT | Information Technology | 387.87 | 71 | $14202.2M | 0.01% | PASS |
| CAT | Industrials | 893.50 | 71 | $2452.3M | 0.04% | PASS |
| SHW | Materials | 313.78 | 71 | $744.5M | 0.05% | PASS |
| WMT | Consumer Staples | 121.00 | 71 | $3180.6M | 0.01% | PASS |
| META | Communication Services | 567.68 | 71 | $9879.3M | 0.02% | PASS |
| NVDA | Information Technology | 202.27 | 71 | $36219.9M | 0.01% | PASS |
| NEE | Utilities | 85.29 | 71 | $1191.1M | 0.01% | PASS |
| NFLX | Communication Services | 81.20 | 71 | $2693.5M | 0.01% | PASS |
| AZO | Consumer Discretionary | 3076.79 | 71 | $1163.6M | 0.16% | PASS |
| APD | Materials | 279.67 | 71 | $333.8M | 0.06% | PASS |
| AVGO | Information Technology | 384.06 | 71 | $11612.7M | 0.04% | PASS |
| AMZN | Consumer Discretionary | 239.69 | 71 | $9747.0M | 0.01% | PASS |
| GEV | Industrials | 909.99 | 71 | $2386.0M | 0.07% | PASS |
| TSLA | Consumer Discretionary | 393.27 | 71 | $18753.5M | 0.03% | PASS |

## Rejection Log

No sampled name failed the price, history, price > $5, 20-day dollar-volume, or available bid/ask spread checks. Names can still be rejected later for score percentile, factor support, event risk, or portfolio construction constraints.
