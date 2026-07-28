# 04 Universe Summary — 2026-07-28

| Stage | Count | Result |
|---|---|---|
| S&P 500 | 503 | source cache |
| Nasdaq-100 | 101 | source cache |
| Overlap | 89 | deduplicated |
| Index union | 515 | eligible_universe.txt |
| Scored | 514 | INDEX_UNION_PCTL (n=514) |
| Excluded | 1 | FDXF: listing age 61d ≤ six months |

Inclusion requires index membership, price/history, market cap ≥$2B, liquidity, and listing age >6 months. FDXF is the only computation exclusion (L044). Market cap, sector, price history, earnings for published ranks, volatility, beta, drawdown, momentum, volume, and technical states are sourceable. Fund_Z and Sent_Z are UNAVAILABLE; Enhancing feeds (IV/skew, spreads, shorts, revisions, ownership) are also UNAVAILABLE and affect DQ/confidence rather than Required-input eligibility (L039–L041).

## Metric and indicator coverage

| Metric group | Sourceable | UNAVAILABLE | Effect | Lineage |
|---|---|---|---|---|
| Raw/adjusted history | 518 | 0 | Required grounded | L002–L005 |
| Scored financial/risk metrics | 514 | 0 | full computation on scored set | L011–L018 |
| Published earnings | 20 | 0 | all top20 grounded | L019 |
| Fundamental family | 0 | 514 | DQ/evidence threshold | L039 |
| Sentiment family | 0 | 514 | DQ/evidence threshold | L040 |
| Daily TD9/RSI/MACD/MA/momentum/volume/RS | 517 | 1 | FDXF unavailable | L010,L017 |
| Weekly pack | 517 | 1 | FDXF unavailable | L010,L017 |
| Monthly pack | 517 | 1 | FDXF unavailable | L010,L017 |

| Indicator | Daily | Weekly | Monthly | Source |
|---|---|---|---|---|
| TD-9 | 517 / 518 | 517 / 518 | 517 / 518 | technical_indicators.json |
| RSI(14) | 517 / 518 | 517 / 518 | 516 / 518 | technical_indicators.json |
| MACD(12,26,9) | 517 / 518 | 517 / 518 | 513 / 518 | technical_indicators.json |
| MA alignment | 517 / 518 | 516 / 518 | 509 / 518 | technical_indicators.json |
| 20/60-bar momentum | 517 / 518 | 516 / 518 | 507 / 518 | technical_indicators.json |
| 20-bar volume ratio | 517 / 518 | 517 / 518 | 515 / 518 | technical_indicators.json |
| Relative strength vs SPY | 517 / 518 | 516 / 518 | 507 / 518 | technical_indicators.json |

All ranks in this package are **INDEX_UNION_PCTL (n=514)**; no sampled-universe fallback was used.
