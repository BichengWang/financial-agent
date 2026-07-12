# 04 Universe Summary

Normal daily path succeeded: S&P 500 union Nasdaq-100 = **503 + 101 - 89 = 515**. Constituent caches were fetched at 2026-06-21T21:05:56Z and 2026-06-21T21:05:56Z; staleness is logged but does not trigger the emergency sampled fallback. Ledger: L001.

## Inclusion And Exclusion

- 515 names entered the exact index-union candidate list.
- SATS was rejected because only 1 usable bar was returned.
- FDXF was rejected because only 31 bars were available, below the 60-bar minimum.
- The remaining 513 names succeeded in the canonical helper on the initial current-run pass.
- 513 names received `INDEX_UNION_PCTL (n=513)` scores.
- The top 20 adjusted-score records were retained as fully settleable monitoring forecasts.

### Mandatory Filter Coverage

The union was checked only where the current-run artifacts contain the required field. Missing full-universe reference/liquidity fields are `UNAVAILABLE`, not silently treated as passes. This incomplete filter coverage independently prohibits `GO`; it does not change the technical monitoring ranks or the final `NO_TRADE` status. Ledger: L205-L206.

| Filter | Threshold | Current-Run Coverage | Result / Treatment |
| --- | --- | ---: | --- |
| Listing | U.S. primary exchange | 515/515 index-cache members | PASS at constituent-cache level; no non-U.S. ticker admitted. |
| Market cap | > $2B | 0/515 | `UNAVAILABLE` full-universe feed; no inferred pass. |
| 20d average dollar volume | > $20M | 0/515 | `UNAVAILABLE`; helper output retains volume ratios, not absolute 20d ADV. |
| Price | > $5 | 513/515 grounded helper records | PASS for all 513 scored names; SATS/FDXF already rejected before a usable price/history test. |
| Listing age | > 6 months | 513/515 grounded helper records | PASS: every scored name has >=126 daily bars; SATS/FDXF rejected. |
| Bid-ask spread | <= 50 bps | 0/515 | `UNAVAILABLE` full-universe tape. |
| Trading sessions | >=80% of trailing 60 | 0/515 exact session-calendar checks | `UNAVAILABLE`; total bar count is not substituted for the required calendar-completeness test. |
| Halt/delisting/corporate action | No unresolved ambiguity | 0/515 | `UNAVAILABLE` full-universe reference feed; no inferred pass. |

## Metric Coverage

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | ---: | ---: | --- | --- |
| Technical/price helper | 513 | 2 | Primary ranking input | Cross-sectional technical metrics only. |
| Mandatory universe filters | 2 field groups | 6 field groups | Incomplete; independently prohibits `GO` | Price and listing-age sourceable; L205-L206 document the remaining gaps. |
| Raw 60d risk history | 20 | 0 | Complete for published sleeve | Published names have 352-1,255 current-run daily bars; the last 60/30 drive risk metrics. |
| Fundamental/revision | 0 | 515 | Family unavailable; DQ below investable gate | L156. |
| Sentiment/positioning | 0 | 515 | Family unavailable; confidence LOW | L157. |
| Per-name macro exposure | 0 | 515 | Family unavailable | L158; top-down regime is reported separately. |
| Earnings dates | 20 | 0 | Complete for published sleeve | 19 one-day-old Nasdaq/Zacks observations after a disclosed DNS retry failure; one cadence estimate. |

## Technical Indicator Coverage

| Indicator | Daily | Weekly | Monthly | Lineage |
| --- | ---: | ---: | ---: | --- |
| TD-9 | 513 | 513 | 513 | technical_indicators.json / L002 |
| RSI(14) | 513 | 513 | 512 | technical_indicators.json / L002 |
| MACD | 513 | 513 | 508 | technical_indicators.json / L002 |
| MA alignment | 513 | 512 | 505 | technical_indicators.json / L002 |
| Momentum 20 | 513 | 513 | 511 | technical_indicators.json / L002 |
| Momentum 60 | 513 | 512 | 504 | technical_indicators.json / L002 |
| Volume ratio 20 | 513 | 513 | 511 | technical_indicators.json / L002 |
| RS 20 vs SPY | 513 | 513 | 511 | technical_indicators.json / L002 |
| RS 60 vs SPY | 513 | 512 | 504 | technical_indicators.json / L002 |

Percentiles are computed over the 513 scoreable records after 5th/95th winsorization of seven metrics: daily 20d/60d momentum, daily 20d/60d SPY-relative strength, daily volume ratio, D/W/M MA breadth, and D/W/M MACD breadth. Relative-strength z-scores are collinear with raw momentum z-scores when the benchmark is constant; this is disclosed as a technical-family concentration limitation.
