# 03 Regime and Data

## Data Mode

`DELAYED`. The run occurred outside regular market hours on 2026-06-14; last available regular-session prices are dated 2026-06-12. All sampled symbols have fetched history and cross-checked entry prices.

## Regime Classification

| Regime | Evidence | Ledger Rows | Implication |
|---|---|---|---|
| NEUTRAL | SPY 60d return 12.45%, 20d return -0.86%, last price below 20d MA but above 50d MA | L001,L002 | Avoid forcing high-beta exposure; require diversified support. |
| Semiconductor leadership pocket | SOXX 60d return 76.25% and 20d return 12.49% | L009,L010 | Positive for AI-infrastructure watchlist, but high sigma limits confidence. |
| Broad growth mixed | QQQ 60d return 21.41%, 20d return 0.22% | L005,L006 | Supports monitor forecasts, not a clean BULL regime. |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 741.75 | 2026-06-12 | DELAYED | MIXED | 3.93% | 1.000 | 0.5% | 3.93% | REALIZED_VOL_30D | 745.46 | 2026-07-12 | 715.14 | 775.78 | MEDIUM | L001,L002,L003,L004,L240 |
| QQQ | 721.34 | 2026-06-12 | DELAYED | MIXED | 6.91% | 1.398 | 1.2% | 6.91% | REALIZED_VOL_30D | 729.99 | 2026-07-12 | 678.15 | 781.83 | MEDIUM | L005,L006,L007,L008,L241 |
| SOXX | 596.25 | 2026-06-12 | DELAYED | ABOVE_20D_50D | 17.99% | 2.688 | 1.8% | 17.99% | REALIZED_VOL_30D | 607.24 | 2026-07-12 | 495.69 | 718.80 | MEDIUM | L009,L010,L011,L012,L242 |

Relative strength: QQQ/SPY is positive over 60d but flat over 20d; SOXX/SPY is strongly positive over both 20d and 60d. Regime consistency: semiconductor strength is a narrow leadership pocket inside a mixed broad-market tape.

## Universe Handoff

The eligible sampled universe contains 42 equities across all 11 GICS sectors. All names passed price, history, liquidity proxy, and listing sanity checks available from the fetched sources. No name was rejected for missing required data; near-misses are rejected by score, family support, or portfolio fit.
