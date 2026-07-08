# 03 Regime And Data

## Data Mode

Data mode is `DELAYED`: Nasdaq quote observations and Yahoo daily history were retrieved during the run, but the workflow is not a full execution-grade live data stack.

## Regime Classification

Declared regime: `NEUTRAL`. SPY remains above 20d/50d moving averages, but negative 20d momentum and open-session dispersion keep the call neutral rather than bullish. Evidence rows: L001,L002,L003,L004,L005,L006.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 744.41 | 2026-07-02 | LIVE | MA20 741.06; MA50 737.42; BULLISH | 4.42% | 1.00 | 0.50% | 4.42% | REALIZED_VOL_30D | 748.13 | 2026-07-30 | 713.94 | 782.33 | MEDIUM | L001,L002,L003,L004,L005,L006 |
| QQQ | 715.13 | 2026-07-02 | LIVE | MA20 721.23; MA50 709.20; MIXED | 8.43% | 1.59 | 0.79% | 8.43% | REALIZED_VOL_30D | 720.81 | 2026-07-30 | 658.08 | 783.54 | MEDIUM | L007,L008,L009,L010,L011,L012 |
| SOXX | 573.10 | 2026-07-02 | LIVE | MA20 598.07; MA50 545.74; MIXED | 21.80% | 3.27 | 2.00% | 21.80% | REALIZED_VOL_30D | 584.56 | 2026-07-30 | 454.60 | 714.52 | MEDIUM | L013,L014,L015,L016,L017,L018 |

## Relative Strength Notes

QQQ/SPY daily relative strength: 20d -2.61%, 60d 8.57%. SOXX/SPY daily relative strength: 20d -5.82%, 60d 51.53%.

## Universe Handoff

`eligible_universe.txt` contains 515 tickers from the S&P 500 union Nasdaq-100 cache. Technical helper output contains 518 total records, including core ETFs; 514 equities are scoreable for the price-led monitor rank.
