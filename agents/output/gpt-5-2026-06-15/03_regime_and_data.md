# 03 Regime and Data

## Data Mode

`DELAYED`. Yahoo Finance chart prices and daily histories plus Nasdaq quote cross-checks were fetched at 2026-06-15T19:07:23Z. Required inputs are grounded for 42 equities plus SPY/QQQ/SOXX; enhancing feeds are unavailable and cap confidence/gross exposure.

## Regime Classification

| Regime | Evidence | Ledger Rows |
|---|---|---|
| BULL | SPY 20d return +2.11%, 60d return +14.40%, 30d realized vol 4.17%, 60d drawdown -0.63%. | L001,L002,L003,L004 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 754.79 | 2026-06-15 | DELAYED | 20d +2.11%; 50d MA below price | 4.17% | 1.000 | +2.25% | 4.17% | REALIZED_VOL_30D | 771.77 | 2026-07-13 | 739.07 | 804.48 | MEDIUM | L001,L002,L003,L004 |
| QQQ | 743.21 | 2026-06-15 | DELAYED | 20d +4.84%; 50d MA below price | 7.27% | 1.397 | +3.29% | 7.27% | REALIZED_VOL_30D | 767.69 | 2026-07-13 | 711.50 | 823.87 | MEDIUM | L005,L006,L007,L008 |
| SOXX | 626.79 | 2026-06-15 | DELAYED | 20d +23.26%; 50d MA below price | 18.33% | 2.663 | +5.83% | 18.33% | REALIZED_VOL_30D | 663.30 | 2026-07-13 | 543.82 | 782.79 | MEDIUM | L009,L010,L011,L012 |

## Relative Strength Notes

| Ratio | 20d | 60d | Interpretation |
|---|---:|---:|---|
| QQQ/SPY | +2.67% | +9.55% | Growth beta is leading over the short window. |
| SOXX/SPY | +20.71% | +61.05% | Semiconductor leadership is supportive but volatile. |

Regime-consistency check: the bottom-up book may rank high-beta technology names, but the risk gate remains constrained by single-name caps and the 0.90-1.10 protected NAV beta band.

## Universe Handoff

The sampled universe contains 42 U.S.-listed liquid large-cap names across all 11 GICS sectors. No sampled name failed required price/history/sigma/earnings inputs. Names below the 60th sampled percentile are not assigned a forecast sleeve.
