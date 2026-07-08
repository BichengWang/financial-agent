# 04 Universe Summary

## Universe Construction

`build_index_universe.py` succeeded. The scoring universe is the S&P 500 union Nasdaq-100, not the emergency sampled fallback.

| Field | Value |
| --- | --- |
| S&P 500 count | 503 |
| Nasdaq-100 count | 101 |
| Overlap count | 89 |
| Union count | 515 |
| Cache fetched_at | 2026-06-21T21:05:56Z |
| Universe file | eligible_universe.txt |

## Inclusion / Exclusion Log

- Core ETFs SPY, QQQ, and SOXX are analyzed separately and excluded from the equity percentile universe.
- `FDXF` is excluded from ranked outputs because the helper found only 26 bars, below the 60-bar minimum.
- No emergency sampled-universe fallback was used.

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Risk / return history | 514 ranked-eligible equities | 1 | Supports review-only diagnostics | Yahoo daily history available through 2026-07-02 for all ranked names. |
| Technical / price | 514 ranked-eligible equities | 1 | Used in Tech_Z | TD9, RSI, MACD, MA, momentum, volume, and relative strength from technical_indicators.json. |
| Fundamental / revisions | 0 | 515 | Blocks investable status | No connected cross-sectional fundamental/revision feed. |
| Sentiment / positioning | 0 | 515 | Confidence capped | Options, short-interest, borrow, and analyst-revision feeds unavailable. |
| Next earnings date | 0 refreshed | ranked equities | Blocks GO | Not refreshed during the July 3 holiday review cycle. |

## Technical Indicator Coverage

Daily, weekly, and monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and SPY-relative strength are present for every ranked/monitored equity and for SPY/QQQ/SOXX via `technical_indicators.json`.
