# 03 Regime And Data

Data mode: `DELAYED_PARTIAL`. Regime: `NEUTRAL`.

Evidence: SPY is above its daily 20d and 50d moving averages with positive 60d momentum, but QQQ and SOXX both have negative 20d momentum and daily MACD below signal. That mixed growth/semiconductor tape prevents a clean BULL label.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| SPY | 744.92 | 2026-07-08 | DELAYED | BULLISH (0.77%/9.63%) | 4.41% | 1.00 | 0.50% | 4.41% | REALIZED_VOL_30D | 748.64 | 2026-08-05 | 714.47 | 782.82 | MEDIUM | L008,L009 |
| QQQ | 709.53 | 2026-07-08 | DELAYED | MIXED (-0.91%/16.11%) | 8.59% | 1.66 | 0.83% | 8.59% | REALIZED_VOL_30D | 715.44 | 2026-08-05 | 652.08 | 778.79 | MEDIUM | L010,L011 |
| SOXX | 561.37 | 2026-07-08 | DELAYED | MIXED (-1.76%/45.21%) | 22.20% | 3.42 | 2.21% | 22.20% | REALIZED_VOL_30D | 573.77 | 2026-08-05 | 444.13 | 703.40 | MEDIUM | L012,L013 |

## Relative Strength Notes

QQQ/SPY: daily RS20 -1.68%, RS60 6.48%. SOXX/SPY: daily RS20 -2.53%, RS60 35.58%.

## Universe Handoff

`eligible_universe.txt` contains 515 tickers. `FDXF` was excluded from scoreable coverage because only only 29 rows were available; all ranked names have >=60 daily bars.

## Regime Consistency Check

The monitor list is technology-heavy because cross-sectional technical momentum is strongest there, but the regime label remains NEUTRAL due to short-horizon cooling in QQQ and SOXX.
