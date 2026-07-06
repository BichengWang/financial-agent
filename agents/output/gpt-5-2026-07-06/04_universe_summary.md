# 04 Universe Summary

## Construction

`build_index_universe.py` produced the normal S&P 500 ∪ Nasdaq-100 candidate universe. No sampled fallback was used.

| Input | Count |
| --- | --- |
| S&P 500 | 503 |
| Nasdaq-100 | 101 |
| Overlap | 89 |
| Union | 515 |

## Inclusion And Exclusion Log

- Included: 515 locally cached index-union tickers.
- Excluded before ranking: core ETFs `SPY`, `QQQ`, `SOXX` because they are market forecasts, not candidates.
- Excluded during technical validation: `FDXF`, because the helper reported fewer than 60 bars.

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Price/history/technical pack | 517 | 1 | Supports review-only technical ranking | `technical_indicators.json` is canonical. |
| Fundamental/revision | 0 | 515 | Blocks investable evidence threshold | No connected feed. |
| Sentiment/positioning | 0 | 515 | Caps confidence | Options/short-interest/borrow unavailable. |
| Earnings dates | 0 | 515 | Blocks `GO` | No earnings-calendar feed. |

## Technical Indicator Coverage

TD-9, RSI(14), MACD(12,26,9), MA alignment, 20/60 momentum, volume ratio, and relative strength are available for 517 of 518 requested records across daily/weekly/monthly frames.
