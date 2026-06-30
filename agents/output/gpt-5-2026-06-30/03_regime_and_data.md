# 03 Regime And Data

## Data Mode

`LIVE`. Yahoo latest daily chart bars and Nasdaq quote observations are dated 2026-06-30; quote observations were retrieved during the regular session at 2026-06-30T15:04:21Z.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| NEUTRAL | SPY daily MA alignment BULLISH; SPY 20d momentum -1.90%; SPY 60d momentum 13.46%. | L001,L002,L003,L004,L005 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 744.08 | 2026-06-30 | LIVE | BULLISH | 4.42% | 1.000 | +0.50% | 4.42% | REALIZED_VOL_30D | 747.80 | 2026-07-28 | 713.62 | 781.98 | MEDIUM | L001,L002,L003,L004,L005 |
| QQQ | 731.66 | 2026-06-30 | LIVE | BULLISH | 8.17% | 1.562 | +1.78% | 8.17% | REALIZED_VOL_30D | 744.70 | 2026-07-28 | 682.50 | 806.90 | MEDIUM | L006,L007,L008,L009,L010 |
| SOXX | 635.02 | 2026-06-30 | LIVE | BULLISH | 20.51% | 3.168 | +2.58% | 20.51% | REALIZED_VOL_30D | 651.43 | 2026-07-28 | 515.95 | 786.90 | MEDIUM | L011,L012,L013,L014,L015 |

Relative-strength notes: QQQ and SOXX both carry positive 20d/60d relative strength versus SPY in `technical_indicators.json`; this is constructive inside the otherwise mixed `NEUTRAL` regime.

## Universe Handoff

Eligible-universe handoff to the technical helper: `SPY, QQQ, SOXX, GOOGL, META, NFLX, AMZN, TSLA, HD, WMT, PG, XOM, CVX, JPM, BAC, GS, V, LLY, UNH, JNJ, CAT, GE, ETN, AAPL, MSFT, NVDA, AVGO, NOW, LIN, SHW, FCX, PLD, EQIX, CCI, NEE, SO, DUK`.
