# 03 Regime And Data

## Data Mode Declaration

Data mode is `DELAYED`. The run occurred on Sunday after the June 19 U.S. market holiday; quote retrieval occurred at 2026-06-21T16:01:03Z, while every entry price observed from public quote sources is dated 2026-06-18.

## Regime Classification

| Regime | Evidence | Ledger Rows |
| --- | --- | --- |
| BULL | SPY price 746.74 is above MA20 747.08 and MA50 729.66; QQQ/SPY 60d relative strength +12.50%; SOXX/SPY 60d relative strength +73.19%. | L001,L002,L003,L004; L005,L006,L007,L008; L009,L010,L011,L012 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 746.74 | 2026-06-18 | DELAYED | mixed MA20/MA50 | 4.21% | 1.000 | +2.0% | 4.21% | REALIZED_VOL_30D | 761.67 | 2026-07-19 | 729.00 | 794.35 | MEDIUM | L001,L002,L003,L004 |
| QQQ | 740.62 | 2026-06-18 | DELAYED | above MA20/MA50 | 7.63% | 1.433 | +2.9% | 7.63% | REALIZED_VOL_30D | 761.85 | 2026-07-19 | 703.05 | 820.64 | MEDIUM | L005,L006,L007,L008 |
| SOXX | 639.45 | 2026-06-18 | DELAYED | above MA20/MA50 | 19.30% | 2.780 | +5.6% | 19.30% | REALIZED_VOL_30D | 675.00 | 2026-07-19 | 546.65 | 803.35 | MEDIUM | L009,L010,L011,L012 |

## Relative-Strength Notes

- QQQ/SPY: 20d +3.11%, 60d +12.50%.
- SOXX/SPY: 20d +22.16%, 60d +73.19%.
- Regime consistency: broad-market trend supports a BULL label, but the portfolio construction stage must still respect beta and concentration caps.

## Universe Handoff

Proceed with the 35-name sampled universe. Required data are grounded; enhancing feeds are unavailable and cap confidence at `MEDIUM`.
