# 09 Final Report — 2026-07-22

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-22
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The completed 2026-07-22 tape supports a NEUTRAL regime with a high-volatility semiconductor watch. All 514 scoreable index-union equities have grounded Technical/Macro evidence, but production Fundamental and Sentiment families remain unavailable. Therefore no name can satisfy three supportive families or the maximum-family-contribution gate, and the run publishes **NO_TRADE**. The 26 equities below are LOW-confidence monitoring forecasts only; all 29 prices passed the two-source gate. Calibration remains mixed: 51.43% equity hit rate, 77.14% CI coverage, and -0.048856 weighted rank IC.

## MoM Reflection Summary

The completed-close comparison for the 2026-06-24 vintage produced 10 hits among 14 equity forecasts (L326). AAPL, BAC, GS, JPM, LLY, UNH, V remain monitored carries after positive realized alpha and current evidence; CAT, CVX, EQIX, FCX, GE, GOOGL, NVDA are dropped unless independent evidence re-admits them. Canonical due inventory remains 17; 17 verified target-close candidates are retained for next-run admission under HUMAN_REVIEW governance (L327).

## Regime

| Regime | Data quality | Key macro risk | Ledger |
|---|---|---|---|
| NEUTRAL (high-volatility semiconductor watch) | DQ 0.80; DELAYED completed close | July 28–29 FOMC inside horizon | L008,L005 |

## Core ETF Market Forecast

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 747.4100 | 2026-07-22 | DELAYED | close 747.41; MA20 745.67; MA50 745.08; BULLISH | 4.02% | 1.000 | +0.50% | 4.02% | REALIZED_VOL_30D | 751.1500 | 2026-08-19 | 719.9000 | 782.3900 | MEDIUM | L009,L010,L011,L012 |
| QQQ | 705.3500 | 2026-07-22 | DELAYED | close 705.35; MA20 714.25; MA50 719.17; BEARISH | 7.98% | 1.733 | +0.37% | 7.98% | REALIZED_VOL_30D | 707.9400 | 2026-08-19 | 649.4000 | 766.4800 | MEDIUM | L013,L014,L015,L016 |
| SOXX | 555.5200 | 2026-07-22 | DELAYED | close 555.52; MA20 572.88; MA50 568.63; MIXED | 20.11% | 3.784 | +0.39% | 20.11% | REALIZED_VOL_30D | 557.7000 | 2026-08-19 | 441.5000 | 673.9000 | MEDIUM | L017,L018,L019,L020 |

## Ranked Monitoring Forecasts

| Ticker | Entry | Adj / Pctl | mu / sigma | Target | Beta / Sharpe / IR | Technical D/W/M | Compact Score Trace | Confidence |
|---|---:|---|---|---:|---|---|---|---|
| BBY | 87.1100 | +0.383 / 100.0 | +5.0% / 7.97% | 91.4700 | 0.71 / 0.59 / 0.36 | TD9 SELL_SETUP_1/SELL_SETUP_4/SELL_SETUP_3; RSI 74.5/65.8/57.0; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.37 Tech + .15*+0.87 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.383` | LOW / MONITORING |
| DVA | 232.0800 | +0.379 / 99.8 | +5.0% / 6.37% | 243.6800 | 0.66 / 0.74 / 0.31 | TD9 BUY_SETUP_1/SELL_SETUP_7/SELL_SETUP_6; RSI 61.0/77.2/73.4; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.66 Tech + .15*+1.09 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.15 = +0.379` | LOW / MONITORING |
| CTAS | 201.3600 | +0.326 / 99.6 | +6.0% / 10.63% | 213.4400 | -0.28 / 0.53 / 0.68 | TD9 BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_1; RSI 68.9/61.7/56.5; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | `(.30*+1.28 Tech + .15*+0.16 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.326` | LOW / MONITORING |
| BAC | 61.6200 | +0.326 / 99.4 | +6.0% / 5.53% | 65.3200 | 0.26 / 1.03 / 1.00 | TD9 SELL_SETUP_1/SELL_SETUP_8/SELL_SETUP_2; RSI 68.0/69.9/69.7; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.92 Tech + .15*+0.89 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.326` | LOW / MONITORING |
| TRV | 372.0800 | +0.323 / 99.2 | +5.0% / 9.16% | 390.6800 | -0.72 / 0.51 / 0.72 | TD9 SELL_SETUP_4/SELL_SETUP_8/SELL_SETUP_4; RSI 76.2/76.7/74.3; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.52 Tech + .15*+0.06 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.323` | LOW / MONITORING |
| MTB | 250.7300 | +0.322 / 99.0 | +6.0% / 6.11% | 265.7700 | 0.24 / 0.93 / 0.96 | TD9 BUY_SETUP_1/SELL_SETUP_8/SELL_SETUP_2; RSI 66.9/69.2/68.6; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.91 Tech + .15*+0.87 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.322` | LOW / MONITORING |
| MMM | 170.7600 | +0.313 / 98.8 | +6.0% / 8.37% | 181.0100 | 0.41 / 0.68 / 0.77 | TD9 SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_1; RSI 68.5/62.5/61.6; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | `(.30*+0.95 Tech + .15*+0.71 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.313` | LOW / MONITORING |
| STT | 185.2400 | +0.305 / 98.6 | +5.0% / 6.99% | 194.5000 | 0.73 / 0.67 / 0.75 | TD9 BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_9; RSI 68.0/87.1/86.4; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.92 Tech + .15*+1.11 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.305` | LOW / MONITORING |
| A | 133.4600 | +0.299 / 98.4 | +6.0% / 8.55% | 141.4700 | 0.94 / 0.67 / 0.44 | TD9 BUY_SETUP_4/BUY_SETUP_1/SELL_SETUP_3; RSI 54.2/55.4/51.4; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.80 Tech + .15*+0.88 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.299` | LOW / MONITORING |
| PAYX | 110.7400 | +0.298 / 98.2 | +5.0% / 9.29% | 116.2800 | -0.69 / 0.50 / 0.60 | TD9 BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2; RSI 60.0/59.1/45.5; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | `(.30*+1.40 Tech + .15*+0.09 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.298` | LOW / MONITORING |
| VTRS | 17.0100 | +0.293 / 98.1 | +5.0% / 9.29% | 17.8600 | 0.29 / 0.50 / 0.49 | TD9 BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_9; RSI 55.9/62.5/68.5; MACD ABOVE_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | `(.30*+1.22 Tech + .15*+0.41 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.293` | LOW / MONITORING |
| JBHT | 292.2400 | +0.284 / 97.9 | +5.0% / 10.56% | 306.8500 | 0.72 / 0.44 / 0.48 | TD9 BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_9; RSI 58.4/70.5/74.1; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.04 Tech + .15*+0.70 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.284` | LOW / MONITORING |
| GEN | 25.5800 | +0.283 / 97.7 | +6.0% / 10.44% | 27.1100 | 0.48 / 0.54 / 0.45 | TD9 BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_3; RSI 49.6/54.7/51.3; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | `(.30*+1.08 Tech + .15*+0.19 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.283` | LOW / MONITORING |
| BNY | 160.3900 | +0.272 / 97.5 | +5.0% / 7.71% | 168.4100 | 0.60 / 0.61 / 0.77 | TD9 BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_9; RSI 67.2/84.2/90.0; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.85 Tech + .15*+0.98 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.272` | LOW / MONITORING |
| SJM | 118.0500 | +0.269 / 97.3 | +6.0% / 12.98% | 125.1300 | -0.86 / 0.44 / 0.66 | TD9 SELL_SETUP_5/SELL_SETUP_2/SELL_SETUP_1; RSI 62.5/62.7/53.8; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.33 Tech + .15*-0.41 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.269` | LOW / MONITORING |
| RF | 30.8600 | +0.268 / 97.1 | +6.0% / 6.62% | 32.7100 | 0.24 / 0.86 / 0.85 | TD9 BUY_SETUP_2/SELL_SETUP_8/SELL_SETUP_2; RSI 55.5/62.0/64.0; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.71 Tech + .15*+0.82 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.268` | LOW / MONITORING |
| DDOG | 245.7700 | +0.268 / 96.9 | +6.0% / 12.72% | 260.5200 | 0.33 / 0.45 / 0.24 | TD9 BUY_SETUP_4/SELL_SETUP_4/SELL_SETUP_3; RSI 48.3/67.1/70.0; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.23 Tech + .15*-0.24 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.00 = +0.268` | LOW / MONITORING |
| USB | 64.4700 | +0.262 / 96.7 | +5.0% / 6.36% | 67.6900 | 0.21 / 0.74 / 0.73 | TD9 SELL_SETUP_7/SELL_SETUP_8/SELL_SETUP_2; RSI 67.9/70.7/68.0; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.89 Tech + .15*+0.82 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.262` | LOW / MONITORING |
| DOC | 22.1900 | +0.258 / 96.5 | +6.0% / 7.32% | 23.5200 | 0.62 / 0.78 / 0.47 | TD9 BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_4; RSI 61.4/66.3/58.2; MACD BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.00 Tech + .15*+0.99 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.10 = +0.258` | LOW / MONITORING |
| IVZ | 30.5000 | +0.257 / 96.3 | +6.0% / 11.35% | 32.3300 | 1.54 / 0.50 / 0.62 | TD9 SELL_SETUP_1/SELL_SETUP_3/SELL_SETUP_3; RSI 64.9/65.3/67.7; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+1.32 Tech + .15*+0.34 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.10 = +0.257` | LOW / MONITORING |
| LLY | 1163.0100 | +0.110 / 72.9 | +2.0% / 9.37% | 1186.2700 | 0.11 / 0.18 / 0.18 | TD9 BUY_SETUP_1/BUY_SETUP_1/SELL_SETUP_3; RSI 51.0/61.8/65.2; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.63 Tech + .15*+0.49 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.10 = +0.110` | LOW / MONITORING |
| GS | 1098.2000 | +0.072 / 62.4 | +1.0% / 12.14% | 1109.1800 | 1.84 / 0.06 / 0.01 | TD9 SELL_SETUP_1/SELL_SETUP_1/SELL_SETUP_9; RSI 56.3/69.6/78.8; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.40 Tech + .15*+0.22 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.072` | LOW / MONITORING |
| UNH | 431.3100 | +0.189 / 90.6 | +4.0% / 7.28% | 448.5600 | -0.16 / 0.51 / 0.55 | TD9 SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4; RSI 58.6/69.5/53.8; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.71 Tech + .15*+0.57 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.189` | LOW / MONITORING |
| JPM | 348.2100 | +0.151 / 82.8 | +2.0% / 6.66% | 355.1700 | 0.32 / 0.25 / 0.29 | TD9 SELL_SETUP_1/SELL_SETUP_8/SELL_SETUP_2; RSI 64.8/68.3/71.6; MACD BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | `(.30*+0.39 Tech + .15*+0.89 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.05 = +0.151` | LOW / MONITORING |
| V | 353.4200 | +0.088 / 67.6 | +1.0% / 6.66% | 356.9500 | -0.36 / 0.10 / 0.15 | TD9 BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_3; RSI 56.2/59.9/60.3; MACD BEARISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | `(.30*+0.54 Tech + .15*+0.49 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.10 = +0.088` | LOW / MONITORING |
| AAPL | 325.8900 | +0.176 / 88.5 | +4.0% / 9.81% | 338.9300 | 0.44 / 0.38 / 0.48 | TD9 BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_3; RSI 62.5/65.3/69.2; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | `(.30*+0.95 Tech + .15*+0.41 Macro + .30*0.00_UNAVAILABLE Fund + .25*0.00_UNAVAILABLE Sent)*.80 - 0.10 = +0.176` | LOW / MONITORING |

## Portfolio analytics / no-trade rationale

No portfolio exists. The investable set is empty before sizing because each name fails the 3-of-4-family and max-family-50% evidence gates. Portfolio beta, correlation, sector allocation, VaR/CVaR, and drawdown are therefore non-applicable rather than estimated.

## Assumptions and limitations

- Completed 2026-07-22 prices are delayed and not executable intraday quotes.
- Fund_Z and Sent_Z remain production-UNAVAILABLE; SHADOW diagnostics are not promoted.
- Options, borrow, bid-ask, analyst-revision, and ownership data are Enhancing-only gaps.
- Normal-distribution VaR/CVaR and 70% CI assumptions are diagnostics, not guarantees.
- Non-positive rank IC caps confidence; earnings dates marked ESTIMATED_CADENCE carry ±5d buffers.

Next scheduled review: 2026-07-23 at 07:27 ET (manual until the scheduler is recreated).
