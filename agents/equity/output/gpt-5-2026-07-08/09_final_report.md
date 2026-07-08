# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-08
Run Status: REVIEW_ONLY
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full index-union and technical-helper path ran successfully, with delayed July 8 bars available for 514 scoreable universe members. The strongest monitors are technology-heavy, led by DDOG, DELL, PANW, CRWD, and HUM. No live portfolio is approved because refreshed earnings dates plus fundamental/revision/positioning feeds are unavailable. The package is published as `REVIEW_ONLY` with settleable monitoring predictions, not trade instructions.

## MoM Reflection Summary

Twelve prior `claude-fable-5` predictions matured on 2026-07-08; equity hit rate was 50.0% and CI coverage was 58.3%. The same-model baseline is `investments/equity/output/gpt-5-2026-06-09`; its defensive basket produced mixed alpha versus SPY.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| NEUTRAL | DELAYED_PARTIAL | SPY trend remains constructive, but QQQ/SOXX daily momentum cooled and missing event/fundamental data remains the main process risk | L009,L003 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SPY | 744.92 | 0.50% | 4.41% | 748.64 | 714.47 | 782.82 | MEDIUM |
| QQQ | 709.53 | 0.83% | 8.59% | 715.44 | 652.08 | 778.79 | MEDIUM |
| SOXX | 561.37 | 2.21% | 22.20% | 573.77 | 444.13 | 703.40 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| DDOG | Datadog Inc. | 100.0 | 1.19 | 6.00% | 18.34% | BUY_SETUP_2/SELL_SETUP_2/SELL_SETUP_3 | 65.05/72.46/73.13 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. | 99.8 | 1.09 | 6.00% | 33.12% | SELL_SETUP_1/SELL_SETUP_1/SELL_SETUP_5 | 60.67/80.8/86.77 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| PANW | Palo Alto Networks Inc. | 99.6 | 0.95 | 6.00% | 17.69% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 59.09/71.83/70.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRWD | CrowdStrike Holdings Inc. | 99.4 | 0.86 | 6.00% | 16.27% | BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 62.43/71.48/71.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MU | Micron Technology Inc. | 99.2 | 0.81 | 6.00% | 36.54% | BUY_SETUP_5/BUY_SETUP_1/SELL_SETUP_9 | 46.21/65.77/75.29 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| HUM | Humana Inc. | 99.0 | 0.81 | 6.00% | 11.23% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 72.13/77.0/61.4 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| FTNT | Fortinet Inc. | 98.8 | 0.77 | 6.00% | 12.82% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_5 | 61.71/83.23/77.21 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AMD | Advanced Micro Devices Inc. | 98.6 | 0.74 | 6.00% | 23.72% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 50.57/71.78/73.74 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna Inc. | 98.4 | 0.71 | 6.00% | 23.39% | SELL_SETUP_8/SELL_SETUP_5/SELL_SETUP_8 | 66.3/70.25/54.94 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AXON | Axon Enterprise Inc. | 98.2 | 0.70 | 6.00% | 21.36% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2 | 69.58/60.91/55.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Missing earnings and non-price factor evidence block the GO gate, and the paper top-10 basket is too beta/technology concentrated for a live recommendation without a full risk review input set.

## Assumptions And Limitations

- Price and history observations are delayed Yahoo chart bars through 2026-07-08.
- Options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional-flow, and cross-sectional fundamental feeds are unavailable.
- Targets and confidence intervals are settleable monitoring records, not trade instructions.

## Next Scheduled Review

Next regular review: Thursday, 2026-07-09 pre-open ET, with focus on whether a refreshed earnings feed and non-price factor evidence can be added.
