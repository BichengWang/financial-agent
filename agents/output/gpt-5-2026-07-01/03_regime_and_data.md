# 03 Regime And Data

## Data Mode

`DELAYED`. Yahoo daily history and Nasdaq quote observations were fetched during this run at 2026-07-01T23:41:43Z; observations are dated 2026-07-01.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| NEUTRAL | SPY daily MA alignment BULLISH; SPY 20d momentum -1.82%; SPY 60d momentum 13.18%; market leadership is constructive but not broad enough for a high-confidence regime upgrade. | L001,L002,L003,L004,L005 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 745.53 | 2026-07-01 | LIVE | BULLISH | 4.49% | 1.000 | 0.50% | 4.49% | REALIZED_VOL_30D | 749.26 | 2026-07-29 | 714.45 | 784.06 | MEDIUM | L001,L002,L003,L004,L005 |
| QQQ | 725.06 | 2026-07-01 | LIVE | BULLISH | 8.35% | 1.576 | 0.79% | 8.35% | REALIZED_VOL_30D | 730.77 | 2026-07-29 | 667.83 | 793.72 | MEDIUM | L006,L007,L008,L009,L010 |
| SOXX | 600.78 | 2026-07-01 | LIVE | MIXED | 21.33% | 3.238 | 2.02% | 21.33% | REALIZED_VOL_30D | 612.91 | 2026-07-29 | 479.63 | 746.19 | MEDIUM | L011,L012,L013,L014,L015 |

Relative-strength notes: QQQ/SPY and SOXX/SPY relative-strength fields are sourced from `technical_indicators.json`; SOXX's one-day weakness keeps the regime call at `NEUTRAL` rather than `BULL`.

## Universe Handoff

The index-union helper materialized 515 candidates. `FDXF` was excluded after the technical helper returned only 25 bars. 514 candidates had enough price history for scoring.
