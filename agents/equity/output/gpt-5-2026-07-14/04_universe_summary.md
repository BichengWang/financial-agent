# 04 Universe Summary

Normal daily path succeeded: S&P 500 union Nasdaq-100 = **503 + 101 - 89 = 515**. Constituent caches were fetched at 2026-06-21T21:05:56Z; staleness is logged but does not trigger the emergency sampled fallback.

## Inclusion And Exclusion

- 515 names entered the exact index-union candidate list.
- SATS was rejected because the helper returned 0 usable bars.
- FDXF was rejected because 33 bars were available, below the 60-bar minimum.
- The remaining 513 names received `INDEX_UNION_PCTL (n=513)` scores.
- The top 20 adjusted-score records were retained as settleable monitoring forecasts.
- The raw top 60 received current-run earnings attempts before event-window penalties; all final 20 dates are grounded.

### Universe Screen Coverage

Under `rules.md` Input Classification, the five Required GO inputs are price, minimum history, sigma, earnings date, and index-union universe; all five pass for the published sleeve. The additional reference/liquidity screens below are Enhancing. Missing Enhancing fields lower DQ and prevent an affirmative screen pass, but do not independently block GO.

| Filter | Threshold | Current-Run Coverage | Result / Treatment |
| --- | --- | ---: | --- |
| Listing | U.S. primary exchange | 515/515 index-cache members | PASS at constituent-cache level. |
| Market cap | > $2B | 0/515 | `UNAVAILABLE`; no inferred pass. |
| 20d average dollar volume | > $20M | 0/515 absolute ADV | `UNAVAILABLE`; volume ratio is not substituted for dollar ADV. |
| Price | > $5 | 513/515 helper records | PASS for all scored names. |
| Listing age | > 6 months | 513/515 helper records | PASS: every scored name has at least 126 daily bars. |
| Bid-ask spread | <= 50 bps | 0/515 | `UNAVAILABLE` full-universe tape. |
| Trading sessions | >=80% of trailing 60 | 0/515 exact calendar checks | `UNAVAILABLE`; raw bar count is not substituted. |
| Halt/delisting/corporate action | No unresolved ambiguity | 0/515 | `UNAVAILABLE`; no inferred pass. |

## Metric Coverage

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | ---: | ---: | --- | --- |
| Technical/price helper | 513 | 2 | Primary ranking input | Seven-metric technical cross-section. |
| Enhancing reference/liquidity screens | 2 field groups | 6 field groups | Incomplete; lowers DQ/confidence, not an independent GO blocker | Price and listing age sourceable. |
| Completed risk history | 20 | 0 | Complete for published sleeve | 251 Nasdaq bars per monitor. |
| Fundamental/revision | 0 | 515 | Family unavailable; DQ below investable gate | Not treated as neutral. |
| Sentiment/positioning | 0 | 515 | Family unavailable; confidence LOW | Not treated as neutral. |
| Per-name macro exposure | 0 | 515 | Family unavailable | Top-down regime reported separately. |
| Earnings dates | 20 | 0 | Complete for published sleeve | 18 Nasdaq/Zacks + 2 official-date cadence fallbacks. |

## Technical Indicator Coverage

| Indicator | Daily | Weekly | Monthly | Lineage |
| --- | ---: | ---: | ---: | --- |
| TD-9 | 513 | 513 | 513 | technical_indicators.json |
| RSI(14) | 513 | 513 | 512 | technical_indicators.json |
| MACD | 513 | 513 | 508 | technical_indicators.json |
| MA alignment | 513 | 512 | 505 | technical_indicators.json |
| Momentum 20 | 513 | 513 | 511 | technical_indicators.json |
| Momentum 60 | 513 | 512 | 504 | technical_indicators.json |
| Volume ratio 20 | 513 | 513 | 511 | technical_indicators.json |
| RS 20 vs SPY | 513 | 513 | 511 | technical_indicators.json |
| RS 60 vs SPY | 513 | 512 | 504 | technical_indicators.json |

Percentiles use 5th/95th winsorization across seven metrics: daily 20d/60d momentum, daily 20d/60d SPY-relative strength, daily volume ratio, D/W/M MA breadth, and D/W/M MACD breadth. Raw momentum and relative strength are collinear when the benchmark is constant; this is a disclosed technical-family concentration limitation, not multiple-family confirmation.
