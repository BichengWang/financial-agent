# 03 Regime And Data

## Data Mode

`DELAYED_PARTIAL`. Regular-session prices and histories were fetched during this run, but the run date is a Sunday during the Independence Day holiday weekend after the July 3 observed market closure. Freshest bars are 2026-07-02.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| NEUTRAL | SPY remains above daily 20d/50d moving averages with +12.98% 60d momentum, while QQQ and SOXX have negative 20d momentum and below-signal daily MACD. | L001,L003,L008-L013 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 744.78 | 2026-07-02 | DELAYED | BULLISH | 4.41% | 1.000 | 0.50% | 4.41% | REALIZED_VOL_30D | 748.50 | 2026-08-02 | 714.32 | 782.69 | MEDIUM | L008,L009 |
| QQQ | 712.60 | 2026-07-02 | DELAYED | MIXED | 8.47% | 1.589 | 0.89% | 8.47% | REALIZED_VOL_30D | 718.97 | 2026-08-02 | 656.18 | 781.77 | MEDIUM | L010,L011 |
| SOXX | 566.32 | 2026-07-02 | DELAYED | MIXED | 21.96% | 3.273 | 1.94% | 21.96% | REALIZED_VOL_30D | 577.29 | 2026-08-02 | 447.92 | 706.65 | MEDIUM | L012,L013 |

Relative-strength notes: QQQ trails SPY over 20 daily bars but leads over 60 daily bars; SOXX also trails over 20 daily bars but retains strong 60-day relative strength. Regime consistency check: broad-market trend is constructive, but near-term growth/semiconductor weakness prevents a bullish classification.

## Universe Handoff

`build_index_universe.py` produced 515 tickers from local S&P 500 and Nasdaq-100 caches. The technical helper returned 517 OK rows out of 518 requested, including SPY, QQQ, and SOXX.

## Event Concentration

Earnings dates are `UNAVAILABLE` in this Sunday run; no live portfolio is permitted without a refreshed event calendar.
