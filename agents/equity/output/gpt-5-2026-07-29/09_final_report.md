# 09 Final Report — 2026-07-29

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-29
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full 515-name index union produced 514 sourceable equities and 504 scored equities after FDXF plus ten binding reflection `DROP` exclusions. The 20-name LOW-confidence monitoring sleeve has 100% Required-input completeness, but no equity is investable because Fundamental and Sentiment are unavailable and every name breaches the max-family-conviction rule. The equal-weight diagnostic also fails beta, drawdown, and sector controls, while its one buffered earnings event passes the event-count rule. This package added zero settlements because the same-day merged baseline had already canonicalized all 44 due keys; canonical due and conflict counts are both zero. Final status is **NO_TRADE**.

## MoM Reflection Summary

The exact same-model July 1 baseline materially underperformed: its top five AMAT, HUM, KLAC, LRCX, and PANW all missed on alpha, and three semiconductor names settled OUT_CI_LOW (L036,L038). Rolling equity metrics are n=298, eff_n=1, hit 50.00%, CI 74.50%, mean z -0.2596; weighted rank IC is -0.2064 (L037). The scheduled evolution review is not yet due.

## Regime

| Regime | DQ multiplier | Required completeness | Key macro risk | Ledger |
|---|---|---|---|---|
| NEUTRAL | 0.80 | 100.00% | FOMC statement 14:00 ET; QQQ/SOXX bearish daily alignment | L007-L010,L029,L042,L069 |

## Core ETF Market Forecasts

| ETF | Entry | mu | sigma | Target | 70% CI | Ledger | Confidence |
|---|---|---|---|---|---|---|---|
| SPY | $740.86 | 0.50% | 3.62% | $744.56 | $716.71 to $772.42 | L065 | MEDIUM |
| QQQ | $675.49 | -0.63% | 7.27% | $671.20 | $620.13 to $722.28 | L066 | MEDIUM |
| SOXX | $491.46 | 0.32% | 18.86% | $493.05 | $396.67 to $589.44 | L067 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | Sector | Entry | Adj Score | Pctl | mu | sigma | Target | Beta | Sharpe | Kelly cap | Technical state | Earnings | Score trace | Ledger | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAYX | Industrials | $118.87 | 0.349 | 100.00 | 6.00% | 9.57% | $126.00 | -0.562 | 0.594 | 5.00% | SELL_SETUP_2 \| RSI 73.0 \| ABOVE_SIGNAL | 2026-09-29 (CONFIRMED_EVENT_CALENDAR; 13:30 UTC) | F=U0 T=1.090 S=U0 M=0.726 ×DQ=0.80 −P=0.00 → 0.349 | L045 | LOW |
| ADP | Industrials | $264.17 | 0.333 | 99.80 | 6.00% | 9.83% | $280.02 | -0.649 | 0.578 | 5.00% | SELL_SETUP_2 \| RSI 69.2 \| BULLISH_CROSS | 2026-10-28 (CONFIRMED_EVENT_CALENDAR; 12:30 UTC) | F=U0 T=1.045 S=U0 M=0.686 ×DQ=0.80 −P=0.00 → 0.333 | L046 | LOW |
| TRV | Financials | $397.22 | 0.324 | 99.60 | 6.00% | 9.16% | $421.05 | -0.729 | 0.620 | 5.00% | SELL_SETUP_8 \| RSI 83.3 \| ABOVE_SIGNAL | 2026-10-15 (CONFIRMED_EVENT_CALENDAR; 13:00 UTC) | F=U0 T=0.928 S=U0 M=0.840 ×DQ=0.80 −P=0.00 → 0.324 | L047 | LOW |
| MRSH | Financials | $192.19 | 0.317 | 99.40 | 6.00% | 9.42% | $203.72 | -0.872 | 0.603 | 5.00% | SELL_SETUP_2 \| RSI 70.5 \| BULLISH_CROSS | 2026-10-15 (CONFIRMED_EVENT_CALENDAR; 12:00 UTC) | F=U0 T=0.896 S=U0 M=0.853 ×DQ=0.80 −P=0.00 → 0.317 | L048 | LOW |
| BRO | Financials | $73.65 | 0.310 | 99.20 | 6.00% | 11.35% | $78.07 | -0.990 | 0.501 | 5.00% | SELL_SETUP_2 \| RSI 69.1 \| BULLISH_CROSS | 2026-10-27 (CONFIRMED_EVENT_CALENDAR; 12:00 UTC) | F=U0 T=1.013 S=U0 M=0.554 ×DQ=0.80 −P=0.00 → 0.310 | L049 | LOW |
| INCY | Health Care | $129.93 | 0.308 | 99.01 | 6.00% | 12.72% | $137.73 | -0.356 | 0.447 | 5.00% | SELL_SETUP_3 \| RSI 76.8 \| BULLISH_CROSS | 2026-10-27 (CONFIRMED_EVENT_CALENDAR; 12:00 UTC) | F=U0 T=1.171 S=U0 M=0.228 ×DQ=0.80 −P=0.00 → 0.308 | L050 | LOW |
| RTX | Industrials | $218.58 | 0.286 | 98.81 | 6.00% | 9.33% | $231.69 | -0.106 | 0.609 | 5.00% | SELL_SETUP_5 \| RSI 77.4 \| ABOVE_SIGNAL | 2026-10-20 (CONFIRMED_EVENT_CALENDAR; 16:30 UTC) | F=U0 T=0.884 S=U0 M=0.616 ×DQ=0.80 −P=0.00 → 0.286 | L051 | LOW |
| IQV | Health Care | $242.94 | 0.286 | 98.61 | 6.00% | 15.75% | $257.52 | 0.199 | 0.361 | 5.00% | SELL_SETUP_4 \| RSI 79.5 \| BULLISH_CROSS | 2026-10-27 (CONFIRMED_EVENT_CALENDAR; 13:00 UTC) | F=U0 T=1.332 S=U0 M=-0.284 ×DQ=0.80 −P=0.00 → 0.286 | L052 | LOW |
| CTAS | Industrials | $214.90 | 0.279 | 98.41 | 6.00% | 9.87% | $227.79 | -0.295 | 0.576 | 5.00% | SELL_SETUP_3 \| RSI 77.3 \| ABOVE_SIGNAL | 2026-09-23 (CONFIRMED_EVENT_CALENDAR; 14:00 UTC) | F=U0 T=0.878 S=U0 M=0.568 ×DQ=0.80 −P=0.00 → 0.279 | L053 | LOW |
| KO | Consumer Staples | $88.27 | 0.273 | 98.21 | 6.00% | 8.07% | $93.57 | -0.639 | 0.704 | 5.00% | SELL_SETUP_3 \| RSI 67.0 \| BULLISH_CROSS | 2026-10-20 (CONFIRMED_EVENT_CALENDAR; 12:30 UTC) | F=U0 T=0.689 S=U0 M=0.900 ×DQ=0.80 −P=0.00 → 0.273 | L054 | LOW |
| VLTO | Industrials | $98.47 | 0.256 | 98.01 | 6.00% | 7.64% | $104.38 | -0.405 | 0.744 | 5.00% | SELL_SETUP_2 \| RSI 70.2 \| BULLISH_CROSS | 2026-10-28 (CONFIRMED_EVENT_CALENDAR; 12:30 UTC) | F=U0 T=0.660 S=U0 M=0.813 ×DQ=0.80 −P=0.00 → 0.256 | L055 | LOW |
| PM | Consumer Staples | $200.17 | 0.233 | 97.81 | 6.00% | 9.30% | $212.18 | -0.575 | 0.611 | 5.00% | SELL_SETUP_3 \| RSI 65.7 \| ABOVE_SIGNAL | 2026-10-21 (CONFIRMED_EVENT_CALENDAR; 11:00 UTC) | F=U0 T=0.668 S=U0 M=0.607 ×DQ=0.80 −P=0.00 → 0.233 | L056 | LOW |
| SCHW | Financials | $105.97 | 0.232 | 97.61 | 6.00% | 7.57% | $112.33 | -0.331 | 0.751 | 5.00% | SELL_SETUP_2 \| RSI 69.8 \| BULLISH_CROSS | 2026-10-15 (CONFIRMED_EVENT_CALENDAR; 12:30 UTC) | F=U0 T=0.578 S=U0 M=0.780 ×DQ=0.80 −P=0.00 → 0.232 | L057 | LOW |
| ITW | Industrials | $295.16 | 0.232 | 97.42 | 6.00% | 7.14% | $312.87 | 0.560 | 0.795 | 5.00% | SELL_SETUP_4 \| RSI 72.9 \| ABOVE_SIGNAL | 2026-10-23 (CONFIRMED_EVENT_CALENDAR; 14:00 UTC) | F=U0 T=0.675 S=U0 M=0.582 ×DQ=0.80 −P=0.00 → 0.232 | L058 | LOW |
| WELL | Real Estate | $243.57 | 0.215 | 97.22 | 6.00% | 7.11% | $258.18 | -0.646 | 0.799 | 5.00% | BUY_SETUP_1 \| RSI 60.3 \| ABOVE_SIGNAL | 2026-10-27 (CONFIRMED_EVENT_CALENDAR; 13:00 UTC) | F=U0 T=0.501 S=U0 M=0.789 ×DQ=0.80 −P=0.00 → 0.215 | L059 | LOW |
| UNP | Industrials | $294.45 | 0.212 | 97.02 | 6.00% | 7.72% | $312.12 | -0.211 | 0.736 | 5.00% | SELL_SETUP_4 \| RSI 57.1 \| ABOVE_SIGNAL | 2026-10-22 (CONFIRMED_EVENT_CALENDAR; 12:45 UTC) | F=U0 T=0.521 S=U0 M=0.725 ×DQ=0.80 −P=0.00 → 0.212 | L060 | LOW |
| RJF | Financials | $177.18 | 0.207 | 96.82 | 6.00% | 7.32% | $187.81 | 0.241 | 0.777 | 5.00% | SELL_SETUP_3 \| RSI 73.3 \| BULLISH_CROSS | 2026-10-28 (CONFIRMED_EVENT_CALENDAR; 21:00 UTC) | F=U0 T=0.628 S=U0 M=0.467 ×DQ=0.80 −P=0.00 → 0.207 | L061 | LOW |
| AMP | Financials | $546.62 | 0.205 | 96.62 | 6.00% | 7.84% | $579.42 | 0.275 | 0.725 | 5.00% | SELL_SETUP_3 \| RSI 72.8 \| ABOVE_SIGNAL | 2026-10-29 (CONFIRMED_EVENT_CALENDAR; 13:00 UTC) | F=U0 T=0.582 S=U0 M=0.545 ×DQ=0.80 −P=0.00 → 0.205 | L062 | LOW |
| WTW | Financials | $316.16 | 0.202 | 96.42 | 6.00% | 9.18% | $335.13 | -0.835 | 0.619 | 5.00% | SELL_SETUP_3 \| RSI 73.9 \| ABOVE_SIGNAL | 2026-07-30 (CONFIRMED_EVENT_CALENDAR; 13:00 UTC) | F=U0 T=0.841 S=U0 M=0.839 ×DQ=0.80 −P=0.10 → 0.202 | L063 | LOW |
| SJM | Consumer Staples | $123.04 | 0.199 | 96.22 | 6.00% | 9.56% | $130.42 | -0.792 | 0.594 | 5.00% | SELL_SETUP_9 \| RSI 67.2 \| ABOVE_SIGNAL | 2026-08-26 (CONFIRMED_FORWARD_CALENDAR; time-not-supplied) | F=U0 T=0.465 S=U0 M=0.725 ×DQ=0.80 −P=0.00 → 0.199 | L064 | LOW |

## No-Trade Rationale

- Zero equities clear the 3-of-4 family threshold; every name also breaches the 50% max-family-conviction rule.
- Required-input completeness is 100% and therefore passes the 85% threshold.
- Monitoring-basket beta is -0.386, outside 0.90–1.10.
- The 95th-percentile one-month drawdown estimate is 8.25%, above 8%.
- Financials is 35%, above the 30% sector cap.
- WTW is the sole buffered earnings event, so the maximum-two rule passes.

## Assumptions and Limitations

Prices are official 2026-07-28 closes retrieved during this run; July 29 intraday prints were ignored during the 09:50 ET post-open revalidation. Returns and indicators use Yahoo adjusted histories through the same date. Market-cap and GICS metadata use a disclosed one-day cache. Earnings horizon coverage is 514/515: 335 exact dates and 179 grounded lower bounds; all 20 published names have exact same-day grounded dates (19 current-run event-calendar + SJM from the same-day merged forward-calendar). No live options, short-interest, analyst-revision, or ownership-flow inputs are used.

## Next Scheduled Review

Manual midday monitor: 2026-07-29 12:15 ET. Next full pre-open run: 2026-07-30 07:27 ET.
