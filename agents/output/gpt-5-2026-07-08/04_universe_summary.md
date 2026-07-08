# 04 Universe Summary

## Universe Construction

`build_index_universe.py` materialized the S&P 500 union Nasdaq-100 universe.

| Source | Count | Cache Timestamp |
| --- | ---: | --- |
| S&P 500 | 503 | 2026-06-21T21:05:56Z |
| Nasdaq-100 | 101 | 2026-06-21T21:05:56Z |
| Overlap | 89 | n/a |
| Union | 515 | 2026-07-08T17:43:34Z |

Ranks are labeled `INDEX_UNION_PCTL (n=514)`. No sampled-universe fallback was used.

## Inclusion / Exclusion Log

| Item | Status | Reason |
| --- | --- | --- |
| Index union | INCLUDED | Deterministic helper succeeded. |
| Core ETFs | SEPARATE | SPY, QQQ, SOXX are market-forecast sleeve only. |
| FDXF | EXCLUDED FROM SCORING | Yahoo history returned only 29 rows; below 60-row minimum. |

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | ---: | ---: | --- | --- |
| Technical/price | 514 | 1 | Primary ranking input | Sourceable via fetched history and `technical_indicators.json`. |
| Fundamental/revision | 0 | 515 | Blocks investability | No connected feed. |
| Sentiment/positioning | 0 | 515 | Caps confidence | No options/short/borrow feed. |
| Earnings dates | 0 | 515 | Blocks GO | No earnings calendar feed. |

## Technical Indicator Coverage

`technical_indicators.json` covers TD-9, RSI(14), MACD(12,26,9), MA alignment, 20/60 momentum, 20-bar volume ratio, and SPY-relative strength across daily/weekly/monthly bars for 514 scoreable universe members plus SPY, QQQ, and SOXX.
