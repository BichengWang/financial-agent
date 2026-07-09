# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-09
Run Status: REVIEW_ONLY
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full index-union and technical-helper path ran successfully, with delayed July 9 bars available for 514 scoreable universe members. The strongest monitors are CRWD, HOOD, DELL, AMD, AMAT, WDC, DDOG, MRNA, PANW, STX. No live portfolio is approved because refreshed earnings dates plus fundamental/revision/positioning feeds are unavailable. The package is published as `REVIEW_ONLY` with settleable monitoring predictions, not trade instructions.

## MoM Reflection Summary

29 matured predictions settled during this run; equity hit rate 13/29 and CI coverage 21/29. The same-model baseline is `agents/equity/output/gpt-5-2026-06-11`; its sampled investable-grade slate did not override today's full-union evidence gates.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| NEUTRAL | DELAYED_PARTIAL | SPY trend remains constructive, but leadership is concentrated and missing event/fundamental data remains the main process risk | L002,L003 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 751.13 | 0.50% | 4.42% | 754.89 | 720.36 | 789.41 | MEDIUM |
| QQQ | 723.12 | 1.04% | 8.57% | 730.65 | 666.20 | 795.10 | MEDIUM |
| SOXX | 586.84 | 2.74% | 21.93% | 602.93 | 469.07 | 736.79 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRWD | CrowdStrike Holdings Inc. | 100.0 | 0.55 | 6.00% | 16.38% | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 68.16/75.09/73.41 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| HOOD | Robinhood Markets Inc. | 99.8 | 0.55 | 6.00% | 23.11% | SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2 | 66.44/60.94/63.86 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| DELL | Dell Technologies Inc. | 99.6 | 0.55 | 6.00% | 33.28% | SELL_SETUP_2/SELL_SETUP_1/SELL_SETUP_5 | 65.3/82.37/87.63 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AMD | Advanced Micro Devices Inc. | 99.4 | 0.54 | 6.00% | 23.25% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | 55.76/74.97/78.14 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AMAT | Applied Materials Inc. | 99.2 | 0.51 | 6.00% | 27.49% | BUY_SETUP_6/SELL_SETUP_9/SELL_SETUP_9 | 53.06/77.42/72.5 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| WDC | Western Digital Corp. | 99.0 | 0.51 | 6.00% | 31.36% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 50.41/64.91/86.99 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DDOG | Datadog Inc. | 98.8 | 0.49 | 6.00% | 18.44% | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 69.52/74.99/74.92 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna Inc. | 98.6 | 0.48 | 6.00% | 23.62% | BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_8 | 66.77/71.58/55.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| PANW | Palo Alto Networks Inc. | 98.4 | 0.48 | 6.00% | 17.94% | BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_3 | 63.45/77.21/73.79 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| STX | Seagate Technology Holdings plc | 98.2 | 0.47 | 6.00% | 24.71% | SELL_SETUP_1/BUY_SETUP_2/SELL_SETUP_9 | 50.62/66.61/88.96 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Missing earnings and non-price factor evidence block the GO gate, and the paper top-10 basket is too concentrated for a live recommendation without a full risk review input set.

## Assumptions And Limitations

- Price and history observations are delayed Yahoo chart bars through 2026-07-09.
- Options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional-flow, and cross-sectional fundamental feeds are unavailable.
- Targets and confidence intervals are settleable monitoring records, not trade instructions.

## Next Scheduled Review

Next regular review: Friday, 2026-07-10 pre-open ET, with focus on whether a refreshed earnings feed and non-price factor evidence can be added.
