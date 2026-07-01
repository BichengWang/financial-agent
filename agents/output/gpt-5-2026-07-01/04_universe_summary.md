# 04 Universe Summary

The normal index-union path succeeded. `eligible_universe.txt` contains 515 tickers: 503 S&P 500 constituents plus 101 Nasdaq-100 constituents with 89 overlaps. Percentiles are labeled `INDEX_UNION_PCTL (n=514)`.

## Inclusion / Exclusion Log

- Included for scoring: 514 names with >=60 daily bars and an OK technical-indicator record.
- Excluded: `FDXF` because `technical_indicators.py` reported only 25 bars; additional thin or failed Yahoo histories were not ranked.

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Price/history/risk | 514 | 1 | Required for ranking | Yahoo daily history; ranked entries cross-checked with Nasdaq quotes. |
| Technical pack | 517 | 1 | Used in Tech_Z | TD-9, RSI, MACD, MA, momentum, volume, and relative strength from `technical_indicators.json`. |
| Fundamental/revision feeds | 0 | 514 | Data completeness below GO threshold | True fundamental and analyst-revision feeds were not wired in this automation environment. |
| Enhancing feeds | 0 | 514 | Confidence capped at MEDIUM | Options IV/skew, short interest, bid-ask tape, and institutional flow unavailable. |
