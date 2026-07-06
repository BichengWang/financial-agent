# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-06
Run Status: REVIEW_ONLY
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full index-union and technical-helper path ran successfully, with delayed July 6 bars available for the monitoring sleeve. The strongest technical monitors broaden across fintech, cybersecurity/software, health care, semiconductors, and industrials. No live portfolio is approved because refreshed earnings dates plus fundamental/revision/positioning feeds are unavailable. The package is published as `REVIEW_ONLY` with settleable monitoring predictions, not trade instructions.

## MoM Reflection Summary

No prior machine-readable predictions mature by 2026-07-06. The selected same-model baseline is `investments/equity/output/gpt-5-2026-06-09`, but no forecast settlement is scored today.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| NEUTRAL | DELAYED_PARTIAL | Constructive medium-term trend but missing event/fundamental data and short-term momentum mixed | L001,L003 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 751.06 | 0.50% | 4.39% | 754.82 | 720.55 | 789.08 | MEDIUM |
| QQQ | 724.74 | 1.23% | 8.48% | 733.64 | 669.73 | 797.55 | MEDIUM |
| SOXX | 589.34 | 2.50% | 21.88% | 604.10 | 470.01 | 738.19 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HOOD | Robinhood Markets Inc. | 100.0 | 0.79 | 6.00% | 22.94% | SELL_SETUP_4/SELL_SETUP_7/SELL_SETUP_2 | 69.56/61.16/64.02 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| CRWD | CrowdStrike Holdings Inc. | 99.8 | 0.75 | 6.00% | 16.04% | SELL_SETUP_6/SELL_SETUP_2/SELL_SETUP_3 | 75.76/76.00/74.02 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna Inc. | 99.6 | 0.71 | 6.00% | 22.40% | SELL_SETUP_6/SELL_SETUP_5/SELL_SETUP_8 | 82.48/78.36/58.11 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DDOG | Datadog Inc. | 99.4 | 0.67 | 6.00% | 18.36% | SELL_SETUP_6/SELL_SETUP_2/SELL_SETUP_3 | 67.25/73.36/73.77 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AXON | Axon Enterprise Inc. | 99.2 | 0.65 | 6.00% | 20.64% | SELL_SETUP_8/SELL_SETUP_7/SELL_SETUP_2 | 78.26/61.57/56.17 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| DVA | DaVita Inc. | 99.0 | 0.62 | 6.00% | 6.97% | SELL_SETUP_9/SELL_SETUP_5/SELL_SETUP_6 | 84.99/82.60/74.05 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. | 98.8 | 0.61 | 6.00% | 35.51% | BUY_SETUP_2/SELL_SETUP_1/SELL_SETUP_5 | 56.51/79.36/82.27 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| INTC | Intel Corp. | 98.6 | 0.61 | 6.00% | 25.67% | BUY_SETUP_3/BUY_SETUP_1/SELL_SETUP_9 | 51.56/66.66/77.96 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AMD | Advanced Micro Devices Inc. | 98.4 | 0.58 | 6.00% | 23.36% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | 58.47/75.91/80.22 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| TXN | Texas Instruments Inc. | 98.2 | 0.57 | 6.00% | 18.18% | SELL_SETUP_2/SELL_SETUP_2/SELL_SETUP_7 | 52.12/64.29/68.38 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Missing earnings and non-price factor evidence block the GO gate, so all ranked names remain monitoring records.

## Assumptions And Limitations

- Price and history observations are delayed Yahoo chart/yfinance bars through 2026-07-06.
- Options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, institutional-flow, and cross-sectional fundamental feeds are unavailable.
- Targets and confidence intervals are settleable monitoring records, not trade instructions.

## Next Scheduled Review

Next regular review: Tuesday, 2026-07-07 pre-open ET, with focus on whether a refreshed earnings feed and non-price factor evidence can be added.
