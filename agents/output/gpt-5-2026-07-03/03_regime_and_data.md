# 03 Regime And Data

## Data Mode

`DELAYED_PARTIAL`. The market-calendar row `L001` records that U.S. equity markets are closed on 2026-07-03; all price and history rows are delayed observations from 2026-07-02. The run is therefore a review-only monitoring package.

## Regime Classification

`NEUTRAL`, medium confidence. SPY has positive 60-day momentum and bullish moving-average alignment, while the latest 20-day momentum and daily MACD state are negative. QQQ and SOXX show stronger 60-day relative strength but weaker 20-day action.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 744.78 | 2026-07-02 | DELAYED | BULLISH daily; 20d mom -1.25%, 60d mom 12.98% | 4.41% | 1.00 | +0.50% | 4.41% | REALIZED_VOL_30D | 748.50 | 2026-07-31 | 714.32 | 782.69 | MEDIUM | L008,L009 |
| QQQ | 712.60 | 2026-07-02 | DELAYED | MIXED daily; 20d mom -4.25%, 60d mom 21.07% | 8.47% | 1.59 | +0.79% | 8.47% | REALIZED_VOL_30D | 718.26 | 2026-07-31 | 655.47 | 781.05 | MEDIUM | L010,L011 |
| SOXX | 566.32 | 2026-07-02 | DELAYED | MIXED daily; 20d mom -8.02%, 60d mom 62.85% | 21.96% | 3.27 | +1.64% | 21.96% | REALIZED_VOL_30D | 575.59 | 2026-07-31 | 446.22 | 704.95 | MEDIUM | L012,L013 |

## Relative Strength Notes

- QQQ/SPY: 20d relative strength -3.0%, 60d relative strength 8.09%.
- SOXX/SPY: 20d relative strength -6.77%, 60d relative strength 49.87%.
- Regime consistency: broad index trend is not bearish, but short-horizon momentum does not support a holiday `GO` publication.

## Universe Handoff

`eligible_universe.txt` contains 515 index-union tickers. `technical_indicators.json` includes core ETFs and the full eligible universe; 517 records are usable and one (`FDXF`) is unavailable.
