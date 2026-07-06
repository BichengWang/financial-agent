# 03 Regime And Data

## Data Mode

`DELAYED_PARTIAL`. Yahoo chart/yfinance delayed bars were fetched during this run, but earnings and non-price factor feeds were unavailable.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| NEUTRAL | SPY/QQQ/SOXX medium-term MA alignment is constructive, but 20d momentum is mixed and missing event/fundamental data prevents a higher-conviction regime call. | L001,L003,L008-L013 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (D/W/M) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 751.06 | 2026-07-06 | DELAYED | BULLISH/BULLISH/BULLISH | REALIZED_VOL_30D | 1.00 | 0.50% | 4.39% | REALIZED_VOL_30D | 754.82 | 2026-08-03 | 720.55 | 789.08 | MEDIUM | L008,L009 |
| QQQ | 724.74 | 2026-07-06 | DELAYED | BULLISH/BULLISH/BULLISH | REALIZED_VOL_30D | 1.66 | 1.23% | 8.48% | REALIZED_VOL_30D | 733.64 | 2026-08-03 | 669.73 | 797.55 | MEDIUM | L010,L011 |
| SOXX | 589.34 | 2026-07-06 | DELAYED | MIXED/BULLISH/BULLISH | REALIZED_VOL_30D | 3.41 | 2.50% | 21.88% | REALIZED_VOL_30D | 604.10 | 2026-08-03 | 470.01 | 738.19 | MEDIUM | L012,L013 |

## Universe Handoff

The full S&P 500 union Nasdaq-100 universe contains 515 tickers. `FDXF` is the only non-OK technical helper record and is excluded from ranking. Core ETFs are analyzed separately and are not candidate universe members.

## Event Concentration Flags

Earnings dates were not refreshed; every ranked equity is treated as event-date `UNAVAILABLE`, which blocks `GO` and caps confidence.
