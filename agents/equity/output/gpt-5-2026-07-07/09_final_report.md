# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-07
Run Status: REVIEW_ONLY
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full index-union and technical-helper path ran successfully, with delayed July 7 bars available for the monitoring sleeve. The strongest monitors rotate toward cybersecurity/software, health care, and selective cyclicals. No live portfolio is approved because refreshed earnings dates plus fundamental/revision/positioning feeds are unavailable. The package is published as `REVIEW_ONLY` with settleable monitoring predictions, not trade instructions.

## MoM Reflection Summary

No prior machine-readable predictions mature by 2026-07-07. The selected same-model baseline is `investments/equity/output/gpt-5-2026-06-09`; ABBV, JPM, MCK, UNH, and PG beat SPY from that baseline, while WMT, XOM, and AZO lagged.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| NEUTRAL | DELAYED_PARTIAL | Constructive SPY trend but daily growth/semiconductor momentum has cooled; missing event/fundamental data remains the main process risk | L001,L003,L004 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 747.37 | 0.50% | 4.41% | 751.11 | 716.79 | 785.42 | MEDIUM |
| QQQ | 709.21 | 0.84% | 8.60% | 715.14 | 651.72 | 778.56 | MEDIUM |
| SOXX | 546.34 | 2.23% | 22.42% | 558.52 | 431.15 | 685.89 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRWD | CrowdStrike Holdings Inc. | 100.0 | 0.87 | 6.00% | 15.98% | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_3 | 71.29/74.93/73.30 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| PANW | Palo Alto Networks Inc. | 99.8 | 0.86 | 6.00% | 16.54% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 72.19/81.17/75.40 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna Inc. | 99.6 | 0.81 | 6.00% | 22.51% | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_8 | 75.66/76.12/56.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| HOOD | Robinhood Markets Inc. | 99.4 | 0.80 | 6.00% | 23.18% | SELL_SETUP_5/SELL_SETUP_7/SELL_SETUP_2 | 66.33/60.41/63.50 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| DDOG | Datadog Inc. | 99.2 | 0.80 | 6.00% | 18.49% | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_3 | 67.72/74.44/74.53 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DVA | DaVita Inc. | 99.0 | 0.79 | 6.00% | 6.97% | SELL_SETUP_9/SELL_SETUP_5/SELL_SETUP_6 | 85.19/82.68/74.11 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| WST | West Pharmaceutical Services Inc. | 98.8 | 0.76 | 6.00% | 7.02% | BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_4 | 64.24/67.17/60.64 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| UAL | United Airlines Holdings Inc. | 98.6 | 0.76 | 6.00% | 15.75% | BUY_SETUP_3/SELL_SETUP_8/SELL_SETUP_3 | 61.57/62.20/65.24 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| BEN | Franklin Resources Inc. | 98.4 | 0.75 | 6.00% | 8.12% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_7 | 68.43/77.23/67.41 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| FTNT | Fortinet Inc. | 98.2 | 0.75 | 6.00% | 12.75% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_5 | 68.08/84.56/78.00 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Missing earnings and non-price factor evidence block the GO gate, and the paper top-10 basket's drawdown proxy is above the 8% target.

## Assumptions And Limitations

- Price and history observations are delayed Yahoo chart bars through 2026-07-07.
- Options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional-flow, and cross-sectional fundamental feeds are unavailable.
- Targets and confidence intervals are settleable monitoring records, not trade instructions.

## Next Scheduled Review

Next regular review: Wednesday, 2026-07-08 pre-open ET, with focus on whether a refreshed earnings feed and non-price factor evidence can be added.
