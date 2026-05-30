# Universe Summary

**Date:** 2026-05-29  
**Universe Mode:** Sampled liquid U.S.-listed large-cap research universe  
**Full Universe Screen:** `N/A - not wired`

## Universe Counts

| Stage | Count | Notes |
| --- | ---: | --- |
| Sampled candidates reviewed | 28 | Large-cap, liquid, U.S.-listed names and liquid ADRs in AI, cloud, power, financials, consumer, healthcare |
| Names with current delayed quote snapshot | 28 | All sampled names returned public quote data |
| Names with at least one current catalyst source | 18 | Official/indexed company releases or recent earnings context |
| Names eligible for scoring | 28 | Scoring allowed for review-only output |
| Names passing sample-relative threshold | 6 | `NVDA`, `MSFT`, `GEV`, `PLTR`, `ANET`, `GOOGL` |
| Names approved for live portfolio | 0 | Risk feed and full-universe percentile validation missing |

## Scored Universe

| Ticker | Company / ETF | Sector / Role | Current Snapshot | Inclusion Decision |
| --- | --- | --- | ---: | --- |
| `SPY` | SPDR S&P 500 ETF | Benchmark | 757.28 | Benchmark only |
| `QQQ` | Invesco QQQ ETF | Benchmark | 739.20 | Benchmark only |
| `AVGO` | Broadcom | Semis / custom AI silicon | 439.69 | Score; event penalty |
| `META` | Meta Platforms | Communication services / ads + AI | 628.66 | Score; downgrade |
| `NVDA` | NVIDIA | AI compute | 216.59 | Score; candidate |
| `GEV` | GE Vernova | Power / electrification | 965.61 | Score; candidate |
| `MSFT` | Microsoft | Cloud / AI platform | 442.76 | Score; candidate |
| `AMZN` | Amazon | Cloud / retail / AI | 272.68 | Score; candidate |
| `JPM` | JPMorgan Chase | Financials | 297.63 | Score; near miss |
| `BAC` | Bank of America | Financials | 51.28 | Score; reject |
| `WFC` | Wells Fargo | Financials | 77.37 | Score; reject |
| `GS` | Goldman Sachs | Financials | 1025.07 | Score; near miss |
| `AMD` | Advanced Micro Devices | AI compute challenger | 512.72 | Score; near miss |
| `GOOGL` | Alphabet | Search / cloud AI | 383.14 | Score; candidate |
| `TSM` | Taiwan Semiconductor | Semicap supply chain ADR | 418.95 | Score; reject for ADR/geopolitical overlay |
| `ETN` | Eaton | Electrification | 399.87 | Score; near miss |
| `GE` | GE Aerospace | Aerospace industrial | 325.21 | Score; near miss |
| `AAPL` | Apple | Consumer tech | 311.05 | Score; reject |
| `ORCL` | Oracle | AI cloud infrastructure | 221.37 | Score; near miss due event risk |
| `PLTR` | Palantir | AI software | 156.08 | Score; candidate |
| `ANET` | Arista Networks | AI networking | 157.42 | Score; candidate |
| `CEG` | Constellation Energy | Nuclear / power | 287.50 | Score; near miss |
| `VST` | Vistra | Power | 158.84 | Score; near miss |
| `NEE` | NextEra Energy | Utilities / renewables | 86.24 | Score; reject |
| `UBER` | Uber | Mobility / platform | 71.73 | Score; reject |
| `NFLX` | Netflix | Media | 86.22 | Score; reject |
| `CRM` | Salesforce | Enterprise software | 192.62 | Score; near miss |
| `LLY` | Eli Lilly | Healthcare | 1095.17 | Score; reject |

## Rejection / Near-Miss Logic

| Ticker | Decision | Reason |
| --- | --- | --- |
| `ORCL` | Near miss | Strong AI cloud evidence, but expected early-June earnings falls inside the event-risk window. |
| `AMZN` | Near miss | Strong AWS/AI evidence, but sample-relative percentile does not clear the 80th-percentile threshold today. |
| `AVGO` | Event-risk watch | Strong thesis validation, but June 3 earnings prevents investable treatment today. |
| `CRM` | Near miss | Strong snapshot move, but too much of the signal may be short-lived post-earnings repricing. |
| `AMD` | Near miss | AI compute exposure is useful, but current evidence is less clean than `NVDA`. |
| `ETN` | Near miss | Electrification theme remains valid, but `GEV` has stronger current backlog/orders evidence. |
| `CEG` / `VST` | Near miss | Power theme is useful, but current company-specific catalyst evidence is thinner than `GEV`. |
| `META` | Downgrade | Negative MoM return and capex sensitivity despite healthy Q1 evidence. |
| `TSM` | Reject | ADR/geopolitical overlay adds risk not compensated by cleaner U.S. alternatives. |
| `AAPL` | Reject | Weaker fit with current AI-infrastructure leadership cluster. |

## Limitation

This is not a full eligible U.S. equity universe. Percentiles in the scoring file are sample-relative and cannot support a live `GO`.
