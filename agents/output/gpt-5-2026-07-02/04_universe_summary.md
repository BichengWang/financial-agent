# 04 Universe Summary

## Construction

The run used the normal index-union path, not the sampled fallback. Source row: L117.

| Input | Count | Cache Timestamp |
| --- | --- | --- |
| S&P 500 | 503 | 2026-06-21T21:05:56Z |
| Nasdaq-100 | 101 | 2026-06-21T21:05:56Z |
| Overlap | 89 | N/A |
| Union | 515 | 2026-07-02T16:05:18Z |

## Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Risk / return | 514 | 1 | Used in diagnostics | Beta, volatility, drawdown, Sharpe, Sortino, IR, Kelly, VaR, CVaR are computed for ranked names from fetched history. |
| Technical / price | 514 | 1 | Used in Tech_Z | Helper-generated TD9, RSI, MACD, MA, momentum, volume ratio, and relative strength. |
| Fundamental / revisions | 0 | 515 | Blocks investable status | No sourceable cross-sectional fundamental or analyst-revision feed is wired. |
| Sentiment / positioning | 0 | 515 | Confidence capped | Options, short interest, borrow, and institutional-flow feeds unavailable. |

## Technical Indicator Coverage

Daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength are available for 514 equities and the three core ETFs through `technical_indicators.json`. Unavailable helper records are not hand-filled.
