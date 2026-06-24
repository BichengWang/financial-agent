# 03 Regime And Data

## Data Mode Declaration

Data mode is `DELAYED`. Quote retrieval occurred at 2026-06-24T23:39:38Z; regular-session entry prices are dated 2026-06-24 and are cross-checked between Yahoo Finance chart closes and Nasdaq regular-session closes.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| BULL | SPY 733.24 is mixed MA20/MA50; QQQ/SPY 60d RS +10.68%; SOXX/SPY 60d RS +70.31%. | L001,L002,L003,L004,L005; L006,L007,L008,L009,L010; L011,L012,L013,L014,L015 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 733.24 | 2026-06-24 | DELAYED | mixed MA20/MA50 | 4.33% | 1.000 | +1.5% | 4.33% | REALIZED_VOL_30D | 744.24 | 2026-07-22 | 711.20 | 777.28 | MEDIUM | L001,L002,L003,L004,L005 |
| QQQ | 710.62 | 2026-06-24 | DELAYED | mixed MA20/MA50 | 7.96% | 1.526 | +2.3% | 7.96% | REALIZED_VOL_30D | 726.88 | 2026-07-22 | 668.05 | 785.71 | MEDIUM | L006,L007,L008,L009,L010 |
| SOXX | 601.50 | 2026-06-24 | DELAYED | above MA20/MA50 | 19.98% | 3.045 | +5.6% | 19.98% | REALIZED_VOL_30D | 634.99 | 2026-07-22 | 510.00 | 759.98 | MEDIUM | L011,L012,L013,L014,L015 |

## Relative-Strength Notes

- QQQ/SPY: 20d -0.38%, 60d +10.68%.
- SOXX/SPY: 20d +7.82%, 60d +70.31%.
- Regime consistency: broad-market trend is not clean enough for `HIGH` confidence, but the 50d trend and semiconductor leadership support a `BULL` label with beta discipline.

## Universe Handoff

Proceed with the 35-name sampled universe. Required data are grounded; enhancing feeds are unavailable and cap confidence at `MEDIUM`. Technical-indicator helper handoff tickers: SPY, QQQ, SOXX, GOOGL, META, NFLX, AMZN, TSLA, HD, COST, WMT, PG, XOM, CVX, JPM, BAC, GS, V, LLY, UNH, JNJ, CAT, GE, ETN, AAPL, MSFT, NVDA, AVGO, NOW, LIN, SHW, FCX, PLD, EQIX, CCI, NEE, SO, DUK.
