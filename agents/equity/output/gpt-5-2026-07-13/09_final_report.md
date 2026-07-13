# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-13
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full 515-name index union and canonical technical helper completed with 513 scoreable equities. The strongest technical monitors remain DDOG, CRWD, DVA, MRNA, HOOD, NTAP, CRL, DELL, SNDK, and AXON, but no name clears the three-family and 85% completeness gates. Two-source July 10 prices, current-run histories, realized-vol sigma, current shortlist earnings checks, and settleable forecasts are present; 20 due June 15 forecasts were also settled. The risk committee approved `NO_TRADE`; these are research forecasts, not trade instructions.

## MoM Reflection Summary

The June 15 holdout was settled at the latest completed close available pre-open: 11/17 equities HIT, 13/17 were IN_CI, mean z was -0.097, and rank IC was -0.083. The normalized all-model equity set now contains 63 outcomes with 58.73% hit rate, 77.78% CI coverage, mean z -0.134, and weighted rank IC +0.124. The new SPY/QQQ/SOXX sleeve scored 1/3 direction hits and 3/3 interval hits; the rolling market sleeve is 3/6 direction and 6/6 interval hits. The valid MoM baseline is `gpt-5-2026-06-15`.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| BULL | DELAYED; Required inputs grounded for monitors | Rising realized volatility, concentrated growth leadership, and July 28-29 FOMC inside horizon | L004-L015,L199 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SPY | 754.95 | 2.00% | 4.44% | 770.05 | 735.16 | 804.94 | MEDIUM |
| QQQ | 725.51 | 3.87% | 8.58% | 753.57 | 688.85 | 818.29 | MEDIUM |
| SOXX | 581.34 | 8.04% | 21.79% | 628.05 | 496.29 | 759.81 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | Compact Score Trace | Sharpe | IR | Max DD60 | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| DDOG | Datadog, Inc. Class A Common Stock | 100.0 | 0.426 | Tech_Z=1.82; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.32 | 0.21 | -20.51% | 6.00% | 18.89% | SELL_SETUP_2/SELL_SETUP_2/SELL_SETUP_3 | 60.9/72.75/73.34 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | 99.8 | 0.408 | Tech_Z=1.74; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.36 | 0.23 | -17.55% | 6.00% | 16.81% | BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 57.04/70.09/70.99 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DVA | DaVita Inc. Common Stock | 99.6 | 0.377 | Tech_Z=1.83; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.05 | 0.85 | 0.32 | -6.31% | 6.00% | 7.09% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 74.31/80.56/73.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MRNA | Moderna, Inc. Common Stock | 99.4 | 0.351 | Tech_Z=1.50; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.23 | 0.18 | -18.40% | 6.00% | 25.91% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_8 | 54.83/63.61/52.27 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| HOOD | Robinhood Markets, Inc. Class A Common Stock | 99.2 | 0.349 | Tech_Z=1.49; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.26 | 0.08 | -21.99% | 6.00% | 23.35% | BUY_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 61.53/59.27/62.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |
| NTAP | NetApp, Inc. Common Stock | 99.0 | 0.348 | Tech_Z=1.49; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.27 | 0.20 | -15.81% | 6.00% | 22.07% | SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_4 | 63.72/71.7/68.04 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRL | Charles River Laboratories International, Inc. Common Stock | 98.8 | 0.344 | Tech_Z=1.60; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.03 | 0.42 | 0.27 | -19.19% | 6.00% | 14.30% | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 73.72/66.99/58.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. Class C Common Stock | 98.6 | 0.302 | Tech_Z=1.46; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.04 | 0.18 | 0.04 | -20.63% | 6.00% | 33.41% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_5 | 59.51/81.04/86.9 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| SNDK | Sandisk Corporation Common Stock | 98.4 | 0.298 | Tech_Z=1.44; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.04 | 0.15 | -0.07 | -30.72% | 6.00% | 38.81% | SELL_SETUP_2/BUY_SETUP_1/SELL_SETUP_9 | 52.12/68.28/83.68 | BELOW_SIGNAL/ABOVE_SIGNAL/UNAVAILABLE | LOW |
| AXON | Axon Enterprise, Inc. Common Stock | 98.2 | 0.297 | Tech_Z=1.27; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.27 | 0.22 | -20.10% | 6.00% | 22.05% | BUY_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 60.72/57.19/53.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Zero names satisfy the factor breadth and completeness gates, so sizing the monitoring sleeve would invalidate the research architecture before protected portfolio constraints are applied.

## Assumptions And Limitations

- July 10 closes were fetched Monday pre-open and tagged `DELAYED`, not brokerage-executable.
- Nasdaq `Previous Close` matched the Yahoo histories within 1% for all published and settled symbols.
- Nineteen shortlist earnings dates were fetched this run; DAL uses a disclosed official-date cadence estimate.
- Full-universe market-cap, ADV, spread, exact session-completeness, halt/delisting, and corporate-action filters are unavailable; no `GO` portfolio is permitted from these monitoring ranks.
- Broad fundamentals/revisions, options, short interest, borrow, and institutional-flow feeds are unavailable.
- Relative-strength and raw-momentum z-scores are collinear within the technical family; the concentration is not treated as multi-family support.
- The June 15 vintage's slightly negative rank IC does not trigger a parameter change because the normalized weighted rank IC remains positive; confidence is already `LOW` due to missing families.

## Next Scheduled Review

Next manual checkpoint: Monday 2026-07-13 at 12:15 ET. Refresh after the regular-session close before changing any monitor or confidence label.
