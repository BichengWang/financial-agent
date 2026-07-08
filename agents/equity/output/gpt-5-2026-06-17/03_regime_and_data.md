# 03 Regime and Data

## Data Mode Declaration

`DELAYED`. CNBC quote, Yahoo chart history, and Nasdaq earnings endpoints were fetched during this run at 2026-06-18T00:26:34Z. Required inputs are grounded; enhancing feeds are unavailable and only reduce confidence/exposure.

## Regime Classification

| Input | Value | Ledger Rows |
| --- | --- | --- |
| SPY entry price | 740.96 | L001 |
| SPY 20d return | +0.99% | L002 |
| SPY 60d return | +13.06% | L002 |
| SPY 30d realized sigma | 4.31% | L003 |
| Regime | BULL | derived from SPY trend/vol rows |

Regime consistency check: `BULL` supports risk-aware ranking, but the risk budget still requires beta, volatility, and event-risk discipline.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/60d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 740.96 | 2026-06-17 | DELAYED | 20d +0.99% / 60d +13.06% | 4.31% | 1.000 | +2.0% | 4.31% | REALIZED_VOL_30D | 755.78 | 2026-07-15 | 722.55 | 789.01 | MEDIUM | L001,L002,L003,L004 |
| QQQ | 722.51 | 2026-06-17 | DELAYED | 20d +2.99% / 60d +22.88% | 7.55% | 1.422 | +3.6% | 7.55% | REALIZED_VOL_30D | 748.84 | 2026-07-15 | 692.12 | 805.56 | MEDIUM | L005,L006,L007,L008 |
| SOXX | 599.73 | 2026-06-17 | DELAYED | 20d +20.73% / 60d +78.18% | 18.99% | 2.721 | +6.6% | 18.99% | REALIZED_VOL_30D | 639.56 | 2026-07-15 | 521.09 | 758.03 | MEDIUM | L009,L010,L011,L012 |

## Relative Strength Notes

| Pair | Relative Return |
| --- | --- |
| QQQ/SPY 20d | +2.01% |
| QQQ/SPY 60d | +9.82% |
| SOXX/SPY 20d | +19.75% |
| SOXX/SPY 60d | +65.12% |

## Sampled Universe Handoff

The sampled universe has 35 equities across all 11 GICS sectors. Sector counts:

| Sector | Count |
| --- | --- |
| Communication Services | 3 |
| Consumer Discretionary | 3 |
| Consumer Staples | 3 |
| Energy | 3 |
| Financials | 3 |
| Health Care | 3 |
| Industrials | 3 |
| Information Technology | 5 |
| Materials | 3 |
| Real Estate | 3 |
| Utilities | 3 |

No sampled symbol failed price, history, sigma, earnings-cadence, or 20d dollar-volume checks. Enhancing data gaps are handed to factor scoring as data-quality caps, not GO blockers.
