# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-14
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full 515-name index union and canonical technical helper completed with 513 scoreable equities. The strongest technical monitors are CRWD, DDOG, DELL, NTAP, XYZ, MPC, CRL, BAC, PANW, and GS, but no name clears the three-family, 85% completeness, or max-family-50% gates. Two-source July 14 prices, completed risk histories, realized-vol sigma, and current-run ledger-backed earnings checks (L206) support settleable forecasts; 17 due June 16 forecasts were also settled. The risk committee approved `NO_TRADE`; these are research forecasts, not trade instructions.

## MoM Reflection Summary

The June 16 holdout produced 10/14 equity hits, 13/14 interval hits, mean z -0.201, and rank IC -0.292. The normalized equity set now contains 77 outcomes with 61.04% hit rate, 80.52% CI coverage, mean z -0.146, and weighted rank IC +0.050. All three newly due ETF forecasts missed direction but remained inside their 70% intervals. The valid MoM baseline is `gpt-5-2026-06-16`.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| BULL | DELAYED; five Required inputs grounded; DQ=14/18=0.78 | Rising realized volatility, short-horizon QQQ/SOXX cooling, July 28-29 FOMC, and a 12-name estimated Aug 3-6 earnings cluster | L001,L245,L207,L011,L017,L023,L013,L019,L025 |

## Core ETF Market Forecast

| ETF | Entry | Price Date | Price Tag | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | ---: | --- | --- | ---: | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| SPY | 751.785 | 2026-07-14 | DELAYED | 2.00% | 4.47% | REALIZED_VOL_30D | 766.82 | 2026-08-11 | 731.89 | 801.75 | MEDIUM | L008,L009,L010,L011,L012,L013 |
| QQQ | 720.572 | 2026-07-14 | DELAYED | 3.62% | 8.69% | REALIZED_VOL_30D | 746.67 | 2026-08-11 | 681.57 | 811.77 | MEDIUM | L014,L015,L016,L017,L018,L019 |
| SOXX | 570.925 | 2026-07-14 | DELAYED | 7.68% | 22.17% | REALIZED_VOL_30D | 614.77 | 2026-08-11 | 483.10 | 746.43 | MEDIUM | L020,L021,L022,L023,L024,L025 |

## Ranked Monitoring Candidates

| Ticker | Company | INDEX_UNION_PCTL (n=513) | Adj Score | Compact Score Trace | Sharpe (RAW_DIAGNOSTIC) | IR | Max DD60 | mu | sigma | Sigma Source | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | 100.0 | 0.453 | Tech_Z=1.94; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.36 | 0.24 | -17.55% | 6.00% | 16.55% | REALIZED_VOL_30D | SELL_SETUP_1/SELL_SETUP_3/SELL_SETUP_3 | 68.19/74.67/74.72 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DDOG | Datadog, Inc. Class A Common Stock | 99.8 | 0.397 | Tech_Z=1.78; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.02 | 0.32 | 0.22 | -20.51% | 6.00% | 18.87% | REALIZED_VOL_30D | SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_3 | 66.21/74.65/75.14 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. Class C Common Stock  | 99.6 | 0.368 | Tech_Z=1.74; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.04 | 0.18 | 0.03 | -20.63% | 6.00% | 33.44% | REALIZED_VOL_30D | SELL_SETUP_5/SELL_SETUP_2/SELL_SETUP_5 | 62.97/82.45/87.62 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| NTAP | NetApp, Inc. Common Stock | 99.4 | 0.337 | Tech_Z=1.44; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.27 | 0.20 | -15.81% | 6.00% | 22.26% | REALIZED_VOL_30D | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_4 | 64.96/73.21/69.01 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| XYZ | Block, Inc. Class A Common Stock, | 99.2 | 0.314 | Tech_Z=1.34; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 0.46 | 0.26 | -12.44% | 6.00% | 13.03% | REALIZED_VOL_30D | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_4 | 63.56/60.99/52.91 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| MPC | Marathon Petroleum Corporation Common Stock | 99.0 | 0.309 | Tech_Z=1.53; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.05 | 0.58 | 0.70 | -9.09% | 6.00% | 10.33% | REALIZED_VOL_30D | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_6 | 76.64/72.47/79.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| CRL | Charles River Laboratories International, Inc. Common Stock | 98.8 | 0.308 | Tech_Z=1.44; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.03 | 0.49 | 0.27 | -19.19% | 6.00% | 12.16% | REALIZED_VOL_30D | SELL_SETUP_4/SELL_SETUP_8/SELL_SETUP_2 | 71.82/67.35/58.63 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| BAC | Bank of America Corporation Common Stock | 98.6 | 0.306 | Tech_Z=1.31; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.00 | 1.02 | 0.95 | -8.38% | 6.00% | 5.90% | REALIZED_VOL_30D | SELL_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 69.66/68.33/68.91 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| PANW | Palo Alto Networks, Inc. Common Stock | 98.4 | 0.304 | Tech_Z=1.55; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.06 | 0.33 | 0.21 | -13.30% | 6.00% | 17.97% | REALIZED_VOL_30D | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_3 | 65.64/76.62/75.88 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| GS | Goldman Sachs Group, Inc. (The) Common Stock | 98.2 | 0.300 | Tech_Z=1.45; Fund/Sent/Macro UNAVAILABLE; DQ=0.78; penalty=0.04 | 0.59 | 0.42 | -8.59% | 6.00% | 10.21% | REALIZED_VOL_30D | SELL_SETUP_2/SELL_SETUP_1/SELL_SETUP_9 | 65.83/71.42/79.71 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. Zero names satisfy the three-family, 85% checklist-completeness, or max-family-50% conviction gates, so sizing the monitoring sleeve would invalidate the research architecture before protected portfolio constraints are applied.

## Assumptions And Limitations

- July 14 prices are delayed intraday public-endpoint observations, not brokerage-executable quotes.
- The Yahoo technical helper, rankings, and regime moving averages include the July 14 partial daily bar, while risk histories use the completed July 13 Nasdaq session; the mismatch is explicit and queued for post-close process review.
- Full-universe market-cap, ADV, spread, exact session coverage, halt/delisting, and corporate-action screens are Enhancing and unavailable. They lower DQ and prevent claiming those screens passed, but do not independently block GO; the factor-evidence gates do.
- Twelve of 20 estimated monitor earnings dates cluster on August 3-6 inside the forecast horizon, creating gap and concentration risk even though none yet enters the buffered hard-penalty window (ledger L207).
- Broad fundamentals/revisions, options, short interest, borrow, and institutional-flow feeds are unavailable.
- Relative-strength and raw-momentum z-scores are collinear within the technical family and do not count as multi-family support.
- Rolling rank IC remains only narrowly positive; confidence is LOW for all equity monitors.

## Next Scheduled Review

Next manual checkpoint: Tuesday 2026-07-14 at 15:45 ET. The next normalized prediction due date is 2026-07-15 with 17 gpt-5 records.
