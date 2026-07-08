# 03 Regime And Data

## Data Mode Declaration

Data mode is `DELAYED`. Quote retrieval occurred at 2026-06-29T19:41:29Z; regular-session entry prices are dated 2026-06-26 and are cross-checked between Yahoo Finance chart closes and Nasdaq quote values.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| BULL | SPY 728.99 has mixed daily MA20/MA50 alignment but 12.09% 60d momentum; QQQ/SPY 60d RS 10.32%; SOXX/SPY 60d RS 67.41%. | L001,L002,L003,L004,L005; L006,L007,L008,L009,L010; L011,L012,L013,L014,L015 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 728.99 | 2026-06-26 | DELAYED | mixed MA20/MA50 | 4.34% | 1.000 | +1.0% | 4.34% | REALIZED_VOL_30D | 736.28 | 2026-07-27 | 703.35 | 769.21 | MEDIUM | L001,L002,L003,L004,L005 |
| QQQ | 706.52 | 2026-06-26 | DELAYED | mixed MA20/MA50 | 7.99% | 1.566 | +1.9% | 7.99% | REALIZED_VOL_30D | 719.70 | 2026-07-27 | 660.98 | 778.43 | MEDIUM | L006,L007,L008,L009,L010 |
| SOXX | 589.94 | 2026-06-26 | DELAYED | mixed MA20/MA50 | 20.56% | 3.214 | +4.0% | 20.56% | REALIZED_VOL_30D | 613.62 | 2026-07-27 | 487.45 | 739.78 | MEDIUM | L011,L012,L013,L014,L015 |

## Relative-Strength Notes

- QQQ/SPY: 20d -0.56%, 60d 10.32%.
- SOXX/SPY: 20d 6.98%, 60d 67.41%.
- Regime consistency: weekly/monthly trend support keeps the label `BULL`, but daily pullback and missing enhancing feeds keep confidence `MEDIUM`.

## Universe Handoff

Proceed with the 35-name sampled universe. Required data are grounded; enhancing feeds are unavailable and cap confidence at `MEDIUM`. Technical-indicator helper handoff tickers: SPY, QQQ, SOXX, GOOGL, META, NFLX, AMZN, TSLA, HD, WMT, PG, XOM, CVX, JPM, BAC, GS, V, LLY, UNH, JNJ, CAT, GE, ETN, AAPL, MSFT, NVDA, AVGO, NOW, LIN, SHW, FCX, PLD, EQIX, CCI, NEE, SO, DUK.
