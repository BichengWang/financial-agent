# 09 Final Report

```text
======================================================
QUANTITATIVE EQUITY SELECTION REPORT - 2026-07-10
Run Status: NO_TRADE
Classification: INTERNAL - INVESTMENT COMMITTEE USE
======================================================
```

## Executive Summary

The full 515-name index union and canonical technical helper completed with 513 scoreable equities. The strongest technical monitors are DDOG, DVA, CRWD, MRNA, HOOD, NTAP, CRL, DELL, AXON, AMD, but no name clears the three-family and 85% completeness gates. Two-source July 10 closing prices, raw histories, realized-vol sigma, estimated earnings dates, and settleable targets are present for all published monitors. The risk committee approved `NO_TRADE`; the monitoring records are research forecasts, not trade instructions.

## MoM Reflection Summary

No prediction matured on July 10. The rolling deduplicated settlement set contains 70 equity outcomes with hit rate 48.57% and CI coverage 70.00%; the valid baseline is `gpt-5-2026-06-11`.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| BULL | DELAYED; required operational inputs grounded for monitors | Leadership concentration plus low volume and mixed daily MACD | L004,L005,L006,L007,L008,L009,L010,L011,L012,L013,L014,L015 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 754.95 | 2.00% | 4.44% | 770.05 | 735.16 | 804.94 | MEDIUM |
| QQQ | 725.51 | 3.87% | 8.58% | 753.57 | 688.85 | 818.29 | MEDIUM |
| SOXX | 581.34 | 8.04% | 21.79% | 628.05 | 496.29 | 759.81 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DDOG | Datadog, Inc. Class A Common Stock | 100.0 | 0.42 | 6.00% | 18.89% | SELL_SETUP_2/SELL_SETUP_2/SELL_SETUP_3 | 60.9/72.75/73.34 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DVA | DaVita Inc. Common Stock | 99.8 | 0.39 | 6.00% | 7.09% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 74.31/80.56/73.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | 99.6 | 0.39 | 6.00% | 16.81% | BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 57.04/70.09/70.99 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna, Inc. Common Stock | 99.4 | 0.37 | 6.00% | 25.91% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_8 | 54.83/63.61/52.27 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| HOOD | Robinhood Markets, Inc. Class A Common Stock | 99.2 | 0.36 | 6.00% | 23.35% | BUY_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 61.53/59.27/62.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| NTAP | NetApp, Inc. Common Stock | 99.0 | 0.34 | 6.00% | 22.07% | SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_4 | 63.72/71.7/68.04 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRL | Charles River Laboratories International, Inc. Common Stock | 98.8 | 0.33 | 6.00% | 14.30% | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 73.72/66.99/58.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. Class C Common Stock | 98.6 | 0.31 | 6.00% | 33.41% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_5 | 59.51/81.04/86.9 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AXON | Axon Enterprise, Inc. Common Stock | 98.4 | 0.31 | 6.00% | 22.05% | BUY_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 60.72/57.19/53.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| AMD | Advanced Micro Devices, Inc. Common Stock | 98.2 | 0.30 | 6.00% | 23.26% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 57.47/75.74/79.82 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Zero names satisfy the required factor breadth and completeness gates, so sizing them would invalidate the research architecture before portfolio constraints are applied.

## Assumptions And Limitations

- Closing prices are July 10 Yahoo observations independently cross-checked against Nasdaq closing quotes; they are tagged `DELAYED`, not brokerage-executable.
- Earnings dates are Nasdaq/Zacks estimates where explicitly marked.
- Broad current fundamentals/revisions, options, short interest, borrow, and institutional-flow feeds are unavailable.
- Technical momentum is not treated as a standalone investment recommendation.

## Next Scheduled Review

Next regular review: Monday, 2026-07-13 pre-open ET, with priority on current fundamental/revision and sentiment coverage.
