# 03 Regime and Data

## Data Mode Declaration

`DELAYED`. Nasdaq quote, Nasdaq historical, Yahoo chart cross-check, and Nasdaq earnings endpoints were fetched during this run at 2026-06-16T15:12:55Z. Required inputs are grounded; enhancing feeds are unavailable and only reduce confidence/exposure.

## Regime Classification

| Input | Value | Ledger Rows |
|---|---|---|
| SPY entry price | 753.35 | L001 |
| SPY 20d return | +2.12% | L002 |
| SPY 60d return | +14.40% | L002 |
| SPY 30d realized sigma | 4.17% | L003 |
| Regime | BULL | derived from SPY trend/vol rows |

Regime consistency check: `BULL` supports trend-following and cyclical-quality candidates, but the risk budget still requires beta, volatility, and event-risk discipline.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/60d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 753.35 | 2026-06-16 | DELAYED | 20d +2.1% / 60d +14.4% | 4.2% | 1.000 | +2.2% | 4.2% | REALIZED_VOL_30D | 769.92 | 2026-07-14 | 737.27 | 802.58 | MEDIUM | L001,L002,L003,L004 |
| QQQ | 737.56 | 2026-06-16 | DELAYED | 20d +4.9% / 60d +25.5% | 7.3% | 1.393 | +4.6% | 7.3% | REALIZED_VOL_30D | 771.23 | 2026-07-14 | 715.24 | 827.22 | MEDIUM | L005,L006,L007,L008 |
| SOXX | 612.81 | 2026-06-16 | DELAYED | 20d +23.6% / 60d +84.7% | 18.4% | 2.657 | +7.3% | 18.4% | REALIZED_VOL_30D | 657.82 | 2026-07-14 | 540.71 | 774.93 | MEDIUM | L009,L010,L011,L012 |

## Relative Strength Notes

| Pair | Relative Return |
|---|---|
| QQQ/SPY 20d | +2.83% |
| QQQ/SPY 60d | +11.06% |
| SOXX/SPY 20d | +21.47% |
| SOXX/SPY 60d | +70.33% |

## Sampled Universe Handoff

The sampled universe has 35 equities across all 11 GICS sectors. Sector counts:

| Sector | Count |
|---|---|
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
