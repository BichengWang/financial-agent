# 03 Regime And Data

## Data Mode

Data mode: `LIVE`. CNBC reports real-time quote fields for the sampled universe and Yahoo chart latest bars were fetched in this run. The current-day daily bar may be incomplete, so confidence is capped at `MEDIUM` despite required input coverage.

## Regime Classification

| Regime | Evidence | Ledger Rows | Confidence |
| --- | --- | --- | --- |
| BULL | SPY 20d 0.7%, 60d 14.3%, 30d sigma 4.21%, price above 50d average | L001,L002,L003,L004 | MEDIUM |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 746.68 | 2026-06-18 | LIVE | 20d 0.7%; 50d MA above | 4.21% (falling vs prior 30d) | 1.000 | +2.0% | 4.21% | REALIZED_VOL_30D | 761.61 | 2026-07-16 | 728.95 | 794.28 | MEDIUM | L001,L002,L003,L004 |
| QQQ | 739.68 | 2026-06-18 | LIVE | 20d 3.7%; 50d MA above | 7.61% (rising vs prior 30d) | 1.432 | +3.6% | 7.61% | REALIZED_VOL_30D | 766.04 | 2026-07-16 | 707.53 | 824.55 | MEDIUM | L005,L006,L007,L008 |
| SOXX | 639.46 | 2026-06-18 | LIVE | 20d 22.9%; 50d MA above | 19.30% (rising vs prior 30d) | 2.779 | +6.6% | 19.30% | REALIZED_VOL_30D | 681.40 | 2026-07-16 | 553.03 | 809.77 | MEDIUM | L009,L010,L011,L012 |

Relative-strength notes: QQQ/SPY relative strength: 20d 3.0%, 60d 12.3%. SOXX/SPY relative strength: 20d 22.2%, 60d 73.2%.

Regime-consistency check: SPY, QQQ, and SOXX all support a pro-risk classification, but semiconductor volatility keeps the top-down confidence at `MEDIUM`.

## Universe Handoff

The sampled universe contains 35 liquid U.S. equities across 11 GICS sectors. All pass the price and dollar-volume filters using rows in `01_preflight.md`; full-market percentile feeds, options IV/skew, short interest, bid-ask tape, analyst-revision tape, and institutional flow are unavailable enhancing inputs.

## Event Concentration

All earnings dates are cadence estimates from Nasdaq prior-report rows. No investable-grade name is inside the 14-day earnings stop plus the +/-5 day estimate buffer.
