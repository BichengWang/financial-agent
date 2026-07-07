# 04 Universe Summary

## Universe Construction

Normal path succeeded. `eligible_universe.txt` contains the S&P 500 union Nasdaq-100 set from local caches.

| Source | Count | Cache Timestamp |
| --- | ---: | --- |
| S&P 500 | 503 | 2026-06-21T21:05:56Z |
| Nasdaq-100 | 101 | 2026-06-21T21:05:56Z |
| Overlap | 89 | n/a |
| Union | 515 | generated 2026-07-07T15:53:57Z |

Percentiles in the factor artifact are `INDEX_UNION_PCTL (n=514)`, excluding the one unavailable technical record.

## Inclusion / Exclusion Log

No sampled-universe fallback was used. FDXF is excluded from scoring because the history prefetch returned only 28 rows, below the 60-row minimum for GO-grade indicators.

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | ---: | ---: | --- | --- |
| Technical/price | 514 | 1 | Primary ranking input | Sourceable through fetched history and `technical_indicators.py`. |
| Fundamental/revision | 0 | 514 | Blocks investability | No connected feed. |
| Sentiment/positioning | 0 | 514 | Caps confidence | No options/short/borrow/revision feed. |
| Earnings dates | 0 | 514 | Blocks GO | No earnings calendar. |

## Technical Indicator Coverage

Daily/weekly/monthly TD-9, RSI(14), MACD, MA alignment, 20/60 momentum, volume ratio, and SPY-relative strength are present for 514 eligible tickers. FDXF is `UNAVAILABLE`.
