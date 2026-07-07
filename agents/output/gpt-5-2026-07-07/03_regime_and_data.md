# 03 Regime And Data

## Data Mode

`DELAYED_PARTIAL`. Delayed Yahoo chart histories were fetched for the index-union universe and core ETFs, but earnings-calendar and non-price factor feeds are unavailable.

## Regime Classification

`NEUTRAL`. SPY trend remains constructive (`BULLISH` daily MA alignment, RSI 54.48), but QQQ and SOXX have daily MACD below signal and mixed daily MA alignment after strong 60d relative strength. This is a constructive but not clean risk-on regime.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 747.37 | 2026-07-07 | DELAYED | BULLISH daily; BULLISH weekly | 4.41% (rising vs prior 30d) | 1.00 | 0.50% | 4.41% | REALIZED_VOL_30D | 751.11 | 2026-08-04 | 716.79 | 785.42 | MEDIUM | L009,L010 |
| QQQ | 709.21 | 2026-07-07 | DELAYED | MIXED daily; BULLISH weekly | 8.60% (rising vs prior 30d) | 1.67 | 0.84% | 8.60% | REALIZED_VOL_30D | 715.14 | 2026-08-04 | 651.72 | 778.56 | MEDIUM | L011,L012 |
| SOXX | 546.34 | 2026-07-07 | DELAYED | MIXED daily; BULLISH weekly | 22.42% (rising vs prior 30d) | 3.46 | 2.23% | 22.42% | REALIZED_VOL_30D | 558.52 | 2026-08-04 | 431.15 | 685.89 | MEDIUM | L013,L014 |

## Relative Strength Notes

- QQQ/SPY: daily 20d relative strength is -0.74%, while 60d relative strength is 6.31%.
- SOXX/SPY: daily 20d relative strength is -0.11%, while 60d relative strength is 34.37%.
- Regime consistency: longer-horizon growth/semiconductor strength is still present, but daily momentum has cooled enough to keep the regime at `NEUTRAL` rather than `BULL`.

## Universe Handoff

`build_index_universe.py` materialized 515 S&P 500 union Nasdaq-100 tickers. The technical helper requested 518 records including SPY, QQQ, and SOXX; 517 returned `OK`, and FDXF is `UNAVAILABLE`.

## Event-Concentration Flags

Earnings-date refresh is unavailable for ranked names, so event concentration cannot be cleared for `GO`. This is the Required-input blocker that keeps the output in `REVIEW_ONLY`.
