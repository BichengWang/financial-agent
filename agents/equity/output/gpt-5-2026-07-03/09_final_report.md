# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-03
Run Status: REVIEW_ONLY
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

Today is a U.S. equity market holiday, so the correct publication status is `REVIEW_ONLY`. The full index-union and technical-helper path ran successfully, with usable July 2 history for 514 ranked-eligible equities. The strongest monitoring names are price-led technology and selected healthcare names, but no live portfolio is approved. Missing refreshed earnings dates and unavailable fundamental/revision/positioning feeds keep all candidates below the investable evidence threshold.

## MoM Reflection Summary

No prior machine-readable predictions mature by 2026-07-03. The selected same-model baseline is `gpt-5-2026-06-07`, but that package has no `15_predictions.json`, so individual MoM price scoring is marked `UNAVAILABLE` rather than inferred from prose.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| NEUTRAL | DELAYED_PARTIAL | Holiday tape plus weak 20d momentum despite positive 60d trend | L001,L003 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI Lo | 70% CI Hi | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 744.78 | +0.50% | 4.41% | 748.50 | 714.32 | 782.69 | MEDIUM |
| QQQ | 712.60 | +0.79% | 8.47% | 718.26 | 655.47 | 781.05 | MEDIUM |
| SOXX | 566.32 | +1.64% | 21.96% | 575.59 | 446.22 | 704.95 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Company | Pctl | Adj Score | mu | sigma | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MU | Micron Technology, Inc. | 100.0 | 1.35 | +6.00% | 36.45% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 48.47/68.58/77.72 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| INTC | Intel Corporation | 99.8 | 0.98 | +6.00% | 26.25% | BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_9 | 49.15/65.55/75.77 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| AMD | Advanced Micro Devices, Inc. | 99.6 | 0.94 | +6.00% | 23.38% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | 52.25/72.91/74.41 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| WDC | Western Digital Corporation | 99.4 | 0.82 | +6.00% | 30.55% | BUY_SETUP_8/SELL_SETUP_9/SELL_SETUP_9 | 44.48/61.93/79.69 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DELL | Dell Technologies Inc. Class C | 99.2 | 0.83 | +6.00% | 35.48% | BUY_SETUP_1/BUY_SETUP_2/SELL_SETUP_5 | 52.64/77.9/78.69 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| SNDK | Sandisk Corporation | 99.0 | 0.77 | +6.00% | 38.94% | BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_9 | 46.81/65.4/77.84 | BELOW_SIGNAL/ABOVE_SIGNAL/UNAVAILABLE | LOW |
| MRVL | Marvell Technology, Inc. | 98.8 | 0.81 | +6.00% | 41.78% | BUY_SETUP_2/BUY_SETUP_1/SELL_SETUP_5 | 46.51/68.39/71.44 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| DDOG | Datadog, Inc. Class A | 98.6 | 0.81 | +6.00% | 18.40% | SELL_SETUP_5/SELL_SETUP_1/SELL_SETUP_3 | 68.41/73.96/74.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| STX | Seagate Technology Holdings plc | 98.4 | 0.74 | +6.00% | 24.38% | BUY_SETUP_7/BUY_SETUP_1/SELL_SETUP_9 | 41.53/62.58/79.38 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |
| PANW | Palo Alto Networks, Inc. | 98.2 | 0.65 | +6.00% | 16.13% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 78.46/82.17/75.58 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW |

## Portfolio Analytics Or No-Trade Rationale

No portfolio is proposed. This is not a live-entry day, and the GO gate fails on refreshed earnings dates while sourceable factor families remain too narrow for investable classification.

## Assumptions And Limitations

- Price and history observations are delayed regular-session bars through 2026-07-02; no July 3 regular session exists.
- Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision, institutional-flow, and cross-sectional fundamental feeds are unavailable.
- Targets and confidence intervals are settleable monitoring records, not trade instructions.

## Next Scheduled Review

Next regular-session review: Monday, 2026-07-06 pre-open ET, with attention to whether short-term semiconductor weakness persists after the holiday closure.
