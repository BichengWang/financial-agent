# 04 Universe Summary

## Universe Construction

No full U.S. equity screening feed is wired, so this run uses the Sampled Universe Protocol: prior carry-forward themes plus 2-3 large liquid S&P 500 names from each GICS sector, expanded to 34 names. Percentiles are labeled `SAMPLED_PCTL (n=34)`.

| Sector | Count |
| --- | --- |
| Communication Services | 3 |
| Consumer Discretionary | 3 |
| Consumer Staples | 2 |
| Energy | 2 |
| Financials | 4 |
| Health Care | 3 |
| Industrials | 3 |
| Information Technology | 5 |
| Materials | 3 |
| Real Estate | 3 |
| Utilities | 3 |

## Inclusion Log

| Ticker | Company | Sector | Entry Price | Price Date | 20d ADV USDmm | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| GOOGL | Alphabet | Communication Services | 354.50 | 2026-06-30 | 14492.9 | INCLUDED |
| META | Meta Platforms | Communication Services | 552.52 | 2026-06-30 | 11035.3 | INCLUDED |
| NFLX | Netflix | Communication Services | 72.17 | 2026-06-30 | 3714.5 | INCLUDED |
| AMZN | Amazon | Consumer Discretionary | 238.12 | 2026-06-30 | 14973.2 | INCLUDED |
| TSLA | Tesla | Consumer Discretionary | 415.11 | 2026-06-30 | 19186.8 | INCLUDED |
| HD | Home Depot | Consumer Discretionary | 352.62 | 2026-06-30 | 1758.6 | INCLUDED |
| WMT | Walmart | Consumer Staples | 113.67 | 2026-06-30 | 2884.0 | INCLUDED |
| PG | Procter & Gamble | Consumer Staples | 145.30 | 2026-06-30 | 1416.3 | INCLUDED |
| XOM | Exxon Mobil | Energy | 135.89 | 2026-06-30 | 2527.0 | INCLUDED |
| CVX | Chevron | Energy | 167.39 | 2026-06-30 | 1620.8 | INCLUDED |
| JPM | JPMorgan Chase | Financials | 329.57 | 2026-06-30 | 3175.3 | INCLUDED |
| BAC | Bank of America | Financials | 57.24 | 2026-06-30 | 2124.1 | INCLUDED |
| GS | Goldman Sachs | Financials | 1015.91 | 2026-06-30 | 2627.4 | INCLUDED |
| V | Visa | Financials | 342.23 | 2026-06-30 | 2944.1 | INCLUDED |
| LLY | Eli Lilly | Health Care | 1206.62 | 2026-06-30 | 3852.4 | INCLUDED |
| UNH | UnitedHealth | Health Care | 416.76 | 2026-06-30 | 2942.9 | INCLUDED |
| JNJ | Johnson & Johnson | Health Care | 255.26 | 2026-06-30 | 2134.0 | INCLUDED |
| CAT | Caterpillar | Industrials | 1068.61 | 2026-06-30 | 3670.5 | INCLUDED |
| GE | GE Aerospace | Industrials | 373.64 | 2026-06-30 | 1806.9 | INCLUDED |
| ETN | Eaton | Industrials | 422.48 | 2026-06-30 | 1029.3 | INCLUDED |
| AAPL | Apple | Information Technology | 287.25 | 2026-06-30 | 19616.2 | INCLUDED |
| MSFT | Microsoft | Information Technology | 369.05 | 2026-06-30 | 18986.1 | INCLUDED |
| NVDA | NVIDIA | Information Technology | 197.58 | 2026-06-30 | 33798.5 | INCLUDED |
| AVGO | Broadcom | Information Technology | 375.30 | 2026-06-30 | 15082.3 | INCLUDED |
| NOW | ServiceNow | Information Technology | 97.51 | 2026-06-30 | 3219.7 | INCLUDED |
| LIN | Linde | Materials | 518.35 | 2026-06-30 | 1352.7 | INCLUDED |
| SHW | Sherwin-Williams | Materials | 343.85 | 2026-06-30 | 926.6 | INCLUDED |
| FCX | Freeport-McMoRan | Materials | 62.79 | 2026-06-30 | 1002.0 | INCLUDED |
| PLD | Prologis | Real Estate | 136.62 | 2026-06-30 | 592.4 | INCLUDED |
| EQIX | Equinix | Real Estate | 1047.96 | 2026-06-30 | 663.6 | INCLUDED |
| CCI | Crown Castle | Real Estate | 75.53 | 2026-06-30 | 420.6 | INCLUDED |
| NEE | NextEra Energy | Utilities | 87.84 | 2026-06-30 | 1020.2 | INCLUDED |
| SO | Southern Company | Utilities | 96.38 | 2026-06-30 | 679.2 | INCLUDED |
| DUK | Duke Energy | Utilities | 127.57 | 2026-06-30 | 463.6 | INCLUDED |

## Exclusion Log

No sampled name failed the price, liquidity, history, or earnings-cadence requirement. Non-sampled S&P 500 constituents were not scored because a full-universe feed is not wired.

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Risk / return | 34 | 0 | Used in ranking diagnostics | Sharpe, Sortino, IR, Kelly, VaR, CVaR, beta, drawdown derived from fetched price history. |
| Technical / price | 34 | 0 | Used in Tech_Z | 20d/60d momentum, relative strength, MA alignment, volume confirmation, TD-9, RSI, MACD. |
| Fundamental / quality proxy | 34 | 0 | Used in Fund_Z | Nasdaq EPS surprise plus realized-risk quality proxies are sourceable for the sampled universe. |
| Sentiment / positioning proxy | 34 | 0 | Partial support only | Uses EPS surprise and price/volume confirmation; true analyst/short/options feeds unavailable. |
| Enhancing feeds | 0 | 34 | Confidence capped at MEDIUM | Options IV/skew, borrow, bid-ask, analyst revisions, institutional flow unavailable. |

## Technical Indicator Coverage

Daily, weekly, and monthly TD-9, RSI(14), MACD, MA alignment, 20/60 momentum, 20-bar volume ratio, and relative strength are available for all 34 equities and SPY/QQQ/SOXX through `technical_indicators.json`.
