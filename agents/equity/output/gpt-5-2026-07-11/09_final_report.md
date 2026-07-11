# 09 Final Report

```text
======================================================
QUANTITATIVE EQUITY SELECTION REPORT - 2026-07-11
Run Status: NO_TRADE
Classification: INTERNAL - INVESTMENT COMMITTEE USE
======================================================
```

## Executive Summary

The full 515-name index union and canonical technical helper completed with 513 scoreable equities. The strongest technical monitors are DDOG, CRWD, DVA, MRNA, NTAP, CRL, DELL, SNDK, AXON, ANET, but no name clears the three-family and 85% completeness gates. Two-source July 10 prices, current-run histories, realized-vol sigma, earnings dates, and settleable forecasts are present for all published monitors. The risk committee approved `NO_TRADE`; these are research forecasts, not trade instructions.

## MoM Reflection Summary

No unique prediction matured on July 11. The corrected normalized settlement set contains 29 equity outcomes with 51.72% hit rate, 72.41% CI coverage, mean z -0.218, and weighted rank IC -0.007; the active confidence cap remains. The valid baseline is `gpt-5-2026-06-14`; its July 12 holdout is not settled early.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| BULL | DELAYED; Required inputs grounded for monitors | Rising realized volatility and concentrated semiconductor/growth leadership | L004-L015 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SPY | 754.95 | 2.00% | 4.44% | 770.05 | 735.16 | 804.94 | MEDIUM |
| QQQ | 725.51 | 3.87% | 8.58% | 753.57 | 688.85 | 818.29 | MEDIUM |
| SOXX | 581.34 | 8.04% | 21.79% | 628.05 | 496.29 | 759.81 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| DDOG | Datadog, Inc. Class A Common Stock | 100.0 | 0.426 | 6.00% | 18.89% | SELL_SETUP_2/SELL_SETUP_2/SELL_SETUP_3 | 60.9/72.75/73.34 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | 99.8 | 0.408 | 6.00% | 16.81% | BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 57.04/70.09/70.99 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DVA | DaVita Inc. Common Stock | 99.6 | 0.377 | 6.00% | 7.09% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 74.31/80.56/73.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna, Inc. Common Stock | 99.4 | 0.351 | 6.00% | 25.91% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_8 | 54.83/63.61/52.27 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| NTAP | NetApp, Inc. Common Stock | 99.2 | 0.348 | 6.00% | 22.07% | SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_4 | 63.72/71.7/68.04 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRL | Charles River Laboratories International, Inc. Common Stock | 99.0 | 0.344 | 6.00% | 14.30% | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 73.72/66.99/58.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. Class C Common Stock  | 98.8 | 0.302 | 6.00% | 33.41% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_5 | 59.51/81.04/86.9 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| SNDK | Sandisk Corporation Common Stock | 98.6 | 0.298 | 6.00% | 38.81% | SELL_SETUP_2/BUY_SETUP_1/SELL_SETUP_9 | 52.12/68.28/83.68 | BELOW_SIGNAL/ABOVE_SIGNAL/UNAVAILABLE | LOW |
| AXON | Axon Enterprise, Inc. Common Stock | 98.4 | 0.297 | 6.00% | 22.05% | BUY_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 60.72/57.19/53.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| ANET | Arista Networks, Inc. Common Stock | 98.2 | 0.293 | 6.00% | 18.78% | SELL_SETUP_3/SELL_SETUP_2/SELL_SETUP_4 | 62.92/64.73/69.64 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Zero names satisfy the factor breadth and completeness gates, so sizing the monitoring sleeve would invalidate the research architecture before protected portfolio constraints are applied.

## Assumptions And Limitations

- Friday July 10 closes were fetched Saturday and tagged `DELAYED`, not brokerage-executable.
- Nasdaq's quote display timestamps lag one session while values match Yahoo within 1%; this is disclosed in `01_preflight.md`.
- Broad fundamentals/revisions, options, short interest, borrow, and institutional-flow feeds are unavailable.
- Relative-strength and raw-momentum z-scores are collinear within the technical family; the resulting concentration is not treated as multi-family support.
- Rank-IC calibration remains active at -0.007 until the July 12 holdout is settled separately for equities and ETFs.

## Next Scheduled Review

Next regular review: Monday, 2026-07-13 pre-open ET. The July 12 target-date holdout must be settled first using the last grounded session close and a disclosed non-trading-day convention.
