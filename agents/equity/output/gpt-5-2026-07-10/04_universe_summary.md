# 04 Universe Summary

Normal daily path succeeded: S&P 500 union Nasdaq-100 = **503 + 101 - 89 = 515**. Constituent caches were fetched at 2026-06-21T21:05:56Z and 2026-06-21T21:05:56Z; their staleness is logged but does not trigger the sampled fallback. Ledger: L001.

## Inclusion And Exclusion

- 515 names entered the exact index-union candidate list.
- SATS was rejected because Yahoo returned zero bars.
- FDXF was rejected because only 31 bars were available, below the 60-bar minimum.
- 513 names received `INDEX_UNION_PCTL (n=513)` ranks.
- Independent quote/history checks were performed for the top 35 until 20 settleable monitoring records passed.

## Metric Coverage

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Technical/price helper | 513 | 2 | Primary ranking input | Daily/weekly/monthly TD9, RSI, MACD, MA, momentum, volume and SPY-relative strength. |
| Raw 60d risk history | 20 | 0 | Complete for ranked sleeve | Separate one-year Yahoo fetches; SPY benchmark aligned by date. |
| Fundamental/revision | 0 | 515 | Family unavailable; DQ below investable gate | No broad current-run feed. |
| Sentiment/positioning | 0 | 515 | Family unavailable; confidence capped | No options/short/borrow feed. |
| Earnings dates | 20 | 0 | Complete/explicit for ranked sleeve | Nasdaq/Zacks estimated dates, tagged as estimates. |

Technical indicator coverage for all 513 scoreable equities is complete across daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength. Source: L002.
