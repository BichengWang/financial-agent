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
| GOOGL | Alphabet | Communication Services | 337.39 | 2026-06-26 | 14732.3 | INCLUDED |
| META | Meta Platforms | Communication Services | 550.25 | 2026-06-26 | 11239.7 | INCLUDED |
| NFLX | Netflix | Communication Services | 73.81 | 2026-06-26 | 3729.1 | INCLUDED |
| AMZN | Amazon | Consumer Discretionary | 232.69 | 2026-06-26 | 14782.2 | INCLUDED |
| TSLA | Tesla | Consumer Discretionary | 379.71 | 2026-06-26 | 18987.8 | INCLUDED |
| HD | Home Depot | Consumer Discretionary | 348.86 | 2026-06-26 | 1767.5 | INCLUDED |
| WMT | Walmart | Consumer Staples | 115.69 | 2026-06-26 | 3011.5 | INCLUDED |
| PG | Procter & Gamble | Consumer Staples | 149.02 | 2026-06-26 | 1427.9 | INCLUDED |
| XOM | Exxon Mobil | Energy | 136.54 | 2026-06-26 | 2648.5 | INCLUDED |
| CVX | Chevron | Energy | 171.06 | 2026-06-26 | 1673.2 | INCLUDED |
| JPM | JPMorgan Chase | Financials | 329.05 | 2026-06-26 | 3252.9 | INCLUDED |
| BAC | Bank of America | Financials | 57.88 | 2026-06-26 | 2189.9 | INCLUDED |
| GS | Goldman Sachs | Financials | 1019.61 | 2026-06-26 | 2641.8 | INCLUDED |
| V | Visa | Financials | 336.23 | 2026-06-26 | 2974.3 | INCLUDED |
| LLY | Eli Lilly | Health Care | 1208.12 | 2026-06-26 | 3879.9 | INCLUDED |
| UNH | UnitedHealth | Health Care | 427.89 | 2026-06-26 | 3029.5 | INCLUDED |
| JNJ | Johnson & Johnson | Health Care | 254.66 | 2026-06-26 | 2179.3 | INCLUDED |
| CAT | Caterpillar | Industrials | 997.47 | 2026-06-26 | 3733.3 | INCLUDED |
| GE | GE Aerospace | Industrials | 369.00 | 2026-06-26 | 1844.7 | INCLUDED |
| ETN | Eaton | Industrials | 402.68 | 2026-06-26 | 1050.9 | INCLUDED |
| AAPL | Apple | Information Technology | 283.78 | 2026-06-26 | 19772.7 | INCLUDED |
| MSFT | Microsoft | Information Technology | 372.97 | 2026-06-26 | 19837.5 | INCLUDED |
| NVDA | NVIDIA | Information Technology | 192.53 | 2026-06-26 | 35404.0 | INCLUDED |
| AVGO | Broadcom | Information Technology | 365.02 | 2026-06-26 | 15563.1 | INCLUDED |
| NOW | ServiceNow | Information Technology | 98.34 | 2026-06-26 | 3518.8 | INCLUDED |
| LIN | Linde | Materials | 519.62 | 2026-06-26 | 1405.0 | INCLUDED |
| SHW | Sherwin-Williams | Materials | 344.07 | 2026-06-26 | 856.7 | INCLUDED |
| FCX | Freeport-McMoRan | Materials | 62.45 | 2026-06-26 | 1001.5 | INCLUDED |
| PLD | Prologis | Real Estate | 139.97 | 2026-06-26 | 626.2 | INCLUDED |
| EQIX | Equinix | Real Estate | 1091.30 | 2026-06-26 | 688.1 | INCLUDED |
| CCI | Crown Castle | Real Estate | 82.62 | 2026-06-26 | 426.8 | INCLUDED |
| NEE | NextEra Energy | Utilities | 88.56 | 2026-06-26 | 1081.2 | INCLUDED |
| SO | Southern Company | Utilities | 97.16 | 2026-06-26 | 702.0 | INCLUDED |
| DUK | Duke Energy | Utilities | 128.40 | 2026-06-26 | 469.5 | INCLUDED |

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
