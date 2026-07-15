══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-15
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════

## Executive Summary

The 515-name index union produced 513 scoreable equities and 20 settleable technical monitoring forecasts, but no investable set. All five Required inputs pass; the failure is evidence breadth: only Technical/Price is sourceable, DQ is 77.78%, and one family supplies all nonzero conviction. The regime remains BULL with a short-horizon cooling flag in QQQ and SOXX. Seventeen due predictions were settled at the completed July 14 close, producing 9/14 equity hits and 14/14 CI coverage. Final status is `NO_TRADE`.

## MoM Reflection Summary

The exact baseline is `gpt-5-2026-06-17`. Canonical rolling equity calibration is 54/91 HIT, 76/91 IN_CI, mean z -0.140, and weighted rank IC +0.040. The latest vintage's negative rank IC argues for restraint even though aggregate hit rate remains above 50%.

## Regime

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| BULL | 14/18 = 77.78% | July 28-29 FOMC plus clustered forecast-horizon earnings | L250,L244,L005 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | Target Date | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 754.44 | +2.00% | 4.47% | 769.53 | 2026-08-12 | MEDIUM |
| QQQ | 717.73 | +3.63% | 8.74% | 743.76 | 2026-08-12 | MEDIUM |
| SOXX | 555.70 | +7.69% | 22.28% | 598.44 | 2026-08-12 | MEDIUM |

## Ranked Monitoring Candidates

| Ticker | INDEX_UNION_PCTL (n=513) | Adj Score | Entry | mu | sigma | Score Trace | TD9 D/W/M | RSI D/W/M | MACD D/W/M | Confidence/Sleeve |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRWD | 100.0 | 0.404 | 207.13 | 6.00% | 17.90% | Tech_Z=1.73; DQ=0.78; penalty=0.00 | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_3 | 66.24/74.6/74.67 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| DDOG | 99.8 | 0.353 | 265.00 | 6.00% | 17.38% | Tech_Z=1.51; DQ=0.78; penalty=0.00 | BUY_SETUP_1/SELL_SETUP_3/SELL_SETUP_3 | 62.3/73.97/74.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| XYZ | 99.6 | 0.347 | 81.82 | 6.00% | 13.01% | Tech_Z=1.48; DQ=0.78; penalty=0.00 | SELL_SETUP_3/SELL_SETUP_5/SELL_SETUP_4 | 66.07/62.03/53.59 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| MPC | 99.4 | 0.344 | 300.05 | 6.00% | 10.32% | Tech_Z=1.68; DQ=0.78; penalty=0.05 | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_6 | 73.96/72.39/79.18 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| PSX | 99.2 | 0.335 | 196.15 | 6.00% | 9.47% | Tech_Z=1.43; DQ=0.78; penalty=0.00 | SELL_SETUP_9/SELL_SETUP_2/SELL_SETUP_7 | 65.99/65.77/70.48 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | LOW / MONITOR |
| BBY | 99.0 | 0.327 | 85.29 | 6.00% | 9.60% | Tech_Z=1.52; DQ=0.78; penalty=0.03 | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3 | 72.56/64.69/56.18 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| GS | 98.8 | 0.307 | 1150.85 | 6.00% | 12.57% | Tech_Z=1.48; DQ=0.78; penalty=0.04 | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_9 | 68.71/73.0/80.43 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| MS | 98.2 | 0.284 | 228.93 | 6.00% | 9.14% | Tech_Z=1.38; DQ=0.78; penalty=0.04 | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 64.33/73.24/79.51 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| PANW | 98.0 | 0.282 | 355.49 | 6.00% | 17.25% | Tech_Z=1.46; DQ=0.78; penalty=0.06 | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 66.48/76.99/76.15 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |
| BAC | 97.9 | 0.280 | 61.49 | 6.00% | 5.94% | Tech_Z=1.33; DQ=0.78; penalty=0.03 | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 72.25/69.55/69.58 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR |

## Portfolio Analytics / No-Trade Rationale

No weights or portfolio analytics are published. Fundamental, Sentiment, and per-name Macro families are unavailable, leaving one supportive family, 77.78% completeness, and 100% Technical concentration. Constructing weights would bypass the evidence gate.

## Assumptions And Limitations

- Entry prices are late-session July 15 `DELAYED` observations; technical ranks use a 15:41 ET partial bar; risk histories and settlements use completed July 14 rows.
- Sharpe, Sortino, Treynor, and Calmar-style values are `RAW_DIAGNOSTIC` because no current-run risk-free rate was used.
- Options, short-interest, bid-ask, analyst-revision, institutional-flow, and full-universe reference/liquidity fields are unavailable Enhancing inputs.
- The canonical settlement logic rejects timing-invalid duplicates for this package; durable implementation work is documented in `plan/2026-07-15-canonical-settlement-ledger.md`.

Next scheduled review: 2026-07-16 at 07:27 ET (manual until a scheduler is recreated).
