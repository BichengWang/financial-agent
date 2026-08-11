# 04 — Universe Summary

## Construction

`build_index_universe.py` materialized 503 S&P 500 names and 101 Nasdaq-100 names with 89
overlaps, yielding 515 names [L008-L010]. The constituent caches were fetched 2026-06-21 and
used as required; their age is logged rather than silently replaced by a sample.

| Stage | Count | Notes |
| --- | --- | --- |
| S&P 500 cache | 503 | fetched_at 2026-06-21T21:05:56Z |
| Nasdaq-100 cache | 101 | fetched_at 2026-06-21T21:05:56Z |
| Overlap | 89 | deduplicated |
| Union | 515 | INDEX_UNION source |
| Scored | 511 | INDEX_UNION_PCTL denominator |
| Rejected | 4 | logged below |

## Inclusion and exclusion log

| Ticker | Reason | Evidence |
| --- | --- | --- |
| BF-B | MISSING_MARKET_CAP | as_of=2026-08-10; bars=1255; market_cap=None |
| EA | STALE_PRICE_NOT_RUN_DATE_CLOSE | as_of=2026-08-04; bars=1255; market_cap=None |
| FDXF | INSUFFICIENT_HISTORY_LT_60_BARS | as_of=None; bars=None; market_cap=21134388100.0 |
| Q | INCOMPLETE_MULTI_TIMEFRAME_INDICATORS | as_of=2026-08-10; bars=196; market_cap=28111351923.0 |

All 511 scored names clear price >$5, market cap >$2B, ADV20 >$20M and >6-month listing
history. Spread tape is unavailable and is disclosed as an Enhancing-input gap, not fabricated.

## Metric coverage summary

| Metric group | Sourceable | UNAVAILABLE | Effect |
| --- | --- | --- | --- |
| Raw/adjusted price history | 511 | 0 | Required input PASS |
| Market cap and sector | 511 | 0 | Universe filter and Macro slot |
| ADV20, beta, vol, drawdown | 511 | 0 | Risk analytics sourceable |
| Forward earnings calendar | 511 | 0 | Required input PASS |
| Technical family | 511 | 0 | Contributes to score |
| Macro family | 511 | 0 | Contributes to score |
| Fundamental family | 0 | 511 | No support; DQ/family breadth impact |
| Sentiment family | 0 | 511 | No support; DQ/family breadth impact |

## Technical coverage

| Indicator | Timeframe | Sourceable | UNAVAILABLE | Coverage |
| --- | --- | --- | --- | --- |
| TD-9 | daily | 511 | 0 | 100.00% |
| TD-9 | weekly | 511 | 0 | 100.00% |
| TD-9 | monthly | 511 | 0 | 100.00% |
| RSI(14) | daily | 511 | 0 | 100.00% |
| RSI(14) | weekly | 511 | 0 | 100.00% |
| RSI(14) | monthly | 511 | 0 | 100.00% |
| MACD(12,26,9) | daily | 511 | 0 | 100.00% |
| MACD(12,26,9) | weekly | 511 | 0 | 100.00% |
| MACD(12,26,9) | monthly | 508 | 3 | 99.41% |
| MA alignment | daily | 511 | 0 | 100.00% |
| MA alignment | weekly | 511 | 0 | 100.00% |
| MA alignment | monthly | 504 | 7 | 98.63% |
| 20-period momentum | daily | 511 | 0 | 100.00% |
| 20-period momentum | weekly | 511 | 0 | 100.00% |
| 20-period momentum | monthly | 510 | 1 | 99.80% |
| volume ratio | daily | 511 | 0 | 100.00% |
| volume ratio | weekly | 511 | 0 | 100.00% |
| volume ratio | monthly | 510 | 1 | 99.80% |
| relative strength vs SPY | daily | 511 | 0 | 100.00% |
| relative strength vs SPY | weekly | 511 | 0 | 100.00% |
| relative strength vs SPY | monthly | 510 | 1 | 99.80% |

Seven names have partial monthly histories, but daily/weekly score inputs remain fully
sourceable; missing monthly display values stay `UNAVAILABLE`. FDXF is excluded before scoring.
