# Universe Summary — 2026-07-17

Normal path succeeded: S&P 500 union Nasdaq-100 = **503 + 101 - 89 = 515**. Both constituent caches were fetched at `2026-06-21T21:05:56Z`; their age is disclosed and does not authorize the emergency fallback.

## Inclusion and Exclusion

- 515 names entered the exact index-union list.
- SATS was rejected because Yahoo returned zero usable bars.
- FDXF was rejected because only 36 bars were available, below the 60-bar minimum.
- The remaining 513 names received `INDEX_UNION_PCTL (n=513)` scores.
- The top 120 received current-run earnings attempts; 20 fully grounded future-earnings records were retained as settleable monitoring forecasts.

## Universe Screen Coverage

| Filter | Threshold | Coverage | Treatment |
| --- | --- | --- | --- |
| Listing | U.S. primary exchange | 515/515 index-cache members | PASS at constituent-cache level |
| Market cap | >$2B | 0/515 | UNAVAILABLE; no inferred pass |
| 20d average dollar volume | >$20M | 0/515 absolute ADV | UNAVAILABLE; volume ratio not substituted |
| Price | >$5 | 513/515 helper records | PASS for scored names |
| Listing age | >6 months | 513/515 | PASS; every scored name has >=60 bars |
| Bid-ask spread | <=50 bps | 0/515 full universe | UNAVAILABLE Enhancing input |
| Trading sessions | >=80% of trailing 60 | 0/515 exact-calendar checks | UNAVAILABLE Enhancing input |
| Corporate action ambiguity | None | 0/515 full-universe checks | UNAVAILABLE; no inferred pass |

## Metric Coverage

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Technical/price helper | 513 | 2 | Primary ranking input | Seven-metric 5/95-winsorized technical cross-section |
| Risk/return completed history | 20 | 0 | Complete for monitor sleeve | At least 251 Nasdaq bars per monitor |
| Earnings dates | 20 | 0 | Complete for sleeve | Future source-backed/cadence dates with buffers |
| Fundamental/revision | 0 scoring; 24 SHADOW | 515 scoring | Family unavailable | SHADOW output excluded below 70% coverage |
| Sentiment/positioning | 0 scoring; 24 SHADOW | 515 scoring | Family unavailable | SHADOW output excluded below 70% coverage |
| Per-name macro exposure | 0 | 515 | Family unavailable | Top-down regime reported separately |

## Technical Indicator Coverage

| Indicator | Daily | Weekly | Monthly | Lineage |
| --- | --- | --- | --- | --- |
| ma_alignment | 513 | 513 | 513 | technical_indicators.json |
| macd | 513 | 513 | 513 | technical_indicators.json |
| momentum_20 | 513 | 513 | 511 | technical_indicators.json |
| momentum_60 | 513 | 512 | 504 | technical_indicators.json |
| relative_strength_20 | 513 | 513 | 511 | technical_indicators.json |
| relative_strength_60 | 513 | 512 | 504 | technical_indicators.json |
| rsi_14 | 513 | 513 | 512 | technical_indicators.json |
| td9 | 513 | 513 | 513 | technical_indicators.json |
| volume_ratio_20 | 513 | 513 | 511 | technical_indicators.json |

Percentiles use daily 20d/60d momentum, daily 20d/60d SPY-relative strength, daily volume ratio, D/W/M MA breadth, and D/W/M MACD breadth. Momentum and relative strength are correlated technical inputs, not multiple-family confirmation.
