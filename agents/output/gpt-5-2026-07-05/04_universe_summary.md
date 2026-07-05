# 04 Universe Summary

## Construction

The normal S&P 500 union Nasdaq-100 path succeeded. No sampled-universe fallback was used.

| Source | Count | Cache Timestamp |
| --- | ---: | --- |
| S&P 500 cache | 503 | 2026-06-21T21:05:56Z |
| Nasdaq-100 cache | 101 | 2026-06-21T21:05:56Z |
| Overlap | 89 | N/A |
| Union | 515 | 2026-07-05T19:18:50Z |

## Inclusion / Exclusion Log

The ranking universe used the 514 eligible names with OK technical-helper records. Non-OK helper rows: FDXF.

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | ---: | ---: | --- | --- |
| Risk / return | 20 ranked names | 0 for ranked names | Diagnostics only | Sharpe, Sortino, IR, Kelly, VaR, CVaR, beta, drawdown from fetched history. |
| Technical / price | 514 eligible equities | 1 | Used in Tech_Z | Helper-generated indicator pack. |
| Fundamental / revisions | 0 | 515 | Blocks investable status | No sourceable cross-sectional feed in this automation run. |
| Sentiment / positioning | 0 | 515 | Confidence capped | Options, short interest, bid-ask depth, institutional flow unavailable. |
| Earnings dates | 0 refreshed | 20 ranked names | Blocks GO | Not refreshed for the weekend review package. |

Daily/weekly/monthly technical indicator coverage for TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength is present for every ranked name and the three core ETFs via `technical_indicators.json`.
