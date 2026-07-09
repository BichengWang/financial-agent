# 04 Universe Summary

The helper materialized the normal S&P 500 union Nasdaq-100 universe, not the sampled fallback.

| Metric | Value |
| --- | ---: |
| S&P 500 cache count | 503 |
| Nasdaq-100 cache count | 101 |
| Overlap count | 89 |
| Union count | 515 |
| Scoreable technical records | 514 |
| Unavailable helper records | 1 (`FDXF`) |

Percentiles are `INDEX_UNION_PCTL (n=514)`. Technical/price inputs are sourceable across the eligible universe. Fundamental/revision, sentiment/positioning, and earnings-date inputs are `UNAVAILABLE`; they reduce data quality, cap confidence, and block `GO` because earnings date is Required.

Daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength are sourced from `technical_indicators.json`.
