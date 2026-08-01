# 04 Universe Summary — 2026-07-30

## Construction

`build_index_universe.py` produced the full S&P 500 ∪ Nasdaq-100 union before history fetch and ranking.

| Measure | Count |
| --- | ---: |
| S&P 500 cache | 503 |
| Nasdaq-100 cache | 101 |
| Overlap | 89 |
| Union | 515 |
| Sourceable history | 514 |
| Scored after filters/reflection | 500 |

Percentiles are `INDEX_UNION_PCTL (n=500)`.

## Exclusion log

| Ticker | Reason |
| --- | --- |
| AMAT | binding DROP from exact same-model 2026-07-02 MoM reflection |
| AMD | binding DROP from exact same-model 2026-07-02 MoM reflection |
| ARM | binding DROP from exact same-model 2026-07-02 MoM reflection |
| BKR | next earnings date unavailable after forward and historical calendar sweeps |
| CNC | binding DROP from exact same-model 2026-07-02 MoM reflection |
| FDXF | 45 bars; below 60-bar/listing-age gate |
| FER | next earnings date unavailable after forward and historical calendar sweeps |
| FLEX | binding DROP from exact same-model 2026-07-02 MoM reflection |
| HUM | binding DROP from exact same-model 2026-07-02 MoM reflection |
| INTC | binding DROP from exact same-model 2026-07-02 MoM reflection |
| MRNA | binding DROP from exact same-model 2026-07-02 MoM reflection |
| MRVL | binding DROP from exact same-model 2026-07-02 MoM reflection |
| MU | binding DROP from exact same-model 2026-07-02 MoM reflection |
| PANW | binding DROP from exact same-model 2026-07-02 MoM reflection |
| SNDK | binding DROP from exact same-model 2026-07-02 MoM reflection |

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | Effect |
| --- | ---: | ---: | --- |
| Price/history/sigma/beta/drawdown | 514 | 1 | Required; unavailable names excluded |
| Earnings status | 512 | 3 | Required; complete forward sweep |
| Technical D/W/M pack | 517 | 1 | Score/diagnostic |
| Fundamental production family | 0 | 500 | DQ/confidence; family cannot count |
| Sentiment production family | 0 | 500 | DQ/confidence; family cannot count |

## Technical coverage

`technical_indicators.json` contains the daily/weekly/monthly indicator pack for 517 OK records; field-level availability is reported below. Missing values inside otherwise valid young monthly histories remain `UNAVAILABLE`; they are not hand-filled.

| Indicator | Daily | Weekly | Monthly |
| --- | --- | --- | --- |
| TD9 | 517/518 | 517/518 | 517/518 |
| RSI14 | 517/518 | 517/518 | 516/518 |
| MACD state | 517/518 | 517/518 | 512/518 |
| MA alignment | 517/518 | 516/518 | 509/518 |
| Momentum 20 | 517/518 | 517/518 | 515/518 |
| Momentum 60 | 517/518 | 516/518 | 0/518 |
| Volume ratio 20 | 517/518 | 517/518 | 515/518 |
| Relative strength 20 | 517/518 | 517/518 | 515/518 |
| Relative strength 60 | 517/518 | 516/518 | 0/518 |

Coverage denominators include all 518 requested symbols. In particular, 60-month momentum and relative strength are explicitly `UNAVAILABLE` because the five-year input supplies only 60 monthly bars and those metrics require a prior comparison bar.
