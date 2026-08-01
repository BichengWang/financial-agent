# 03 Regime and Data — 2026-07-30

Data mode: **DELAYED**. All market inputs are frozen to the completed 2026-07-30 session.

## Regime

| Field | Value | Evidence |
| --- | --- | --- |
| Classification | NEUTRAL, post-FOMC volatility/dispersion watch | L005,L008,L026 |
| VIX | 17.09 vs 20d mean 17.22 | L005 |
| FOMC | Held 3.50%-3.75%, 9-3 vote; three dissenters preferred +25bp | L026 |
| 3M risk-free input | 3.83% annual, used consistently in all ratio calculations | L006 |

## Core ETF Market Forecast Block

| ETF | Entry | Price Date | Price Tag | Trend | 30d RVol | Prior 30d RVol | RVol Direction | DD from 60d High | RS20/60 vs SPY | Beta | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Regime Consistency | Ledger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 741.69 | 2026-07-30 | DELAYED | MIXED (745.582/743.9187) | 3.78% | 4.12% | FALLING | -2.10% | 0.00/0.00pp | 1.000 | 0.50% | 3.78% | REALIZED_VOL_30D | 745.40 | 2026-08-27 | 716.28 | 774.52 | MEDIUM | INFERRED — mixed broad trend and moderate vol fit NEUTRAL | L066,L026 |
| QQQ | 683.55 | 2026-07-30 | DELAYED | BEARISH (702.249/715.0086) | 7.34% | 7.40% | FALLING | -8.29% | -5.19/-1.86pp | 1.725 | -0.64% | 7.34% | REALIZED_VOL_30D | 679.19 | 2026-08-27 | 626.98 | 731.40 | MEDIUM | INFERRED — bearish growth trend supports dispersion caution | L067,L026 |
| SOXX | 504.53 | 2026-07-30 | DELAYED | BEARISH (542.076/567.4107) | 19.59% | 18.92% | RISING | -22.97% | -15.32/5.68pp | 3.731 | 1.87% | 19.59% | REALIZED_VOL_30D | 513.94 | 2026-08-27 | 411.17 | 616.72 | MEDIUM | INFERRED — rising vol and deep drawdown support semiconductor caution | L068,L026 |

Each row provides its own regime-consistency assessment. QQQ/SPY relative strength is -5.19pp over 20d and -1.86pp over 60d; SOXX/SPY is -15.32pp / +5.68pp.

## Universe handoff

The helper materialized 515 names (503 S&P 500, 101 Nasdaq-100, 89 overlap). 517/518 technical packs are OK; FDXF is unavailable and excluded before scoring.

## Event concentration

0 of the 20 monitoring names report inside 14 calendar days: none. The complete Nasdaq forward sweep covered 26/26 business days with zero transport gaps.
