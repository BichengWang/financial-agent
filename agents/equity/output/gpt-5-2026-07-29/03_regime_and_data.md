# 03 Regime and Data — 2026-07-29

**Data mode: DELAYED. Regime: NEUTRAL.** Official entry prices are the completed 2026-07-28 close; July 29 intraday prints were ignored during the 09:50 ET post-open revalidation. VIX was 18.21 versus a 20-day mean of 16.9675; DTB3 was 3.82% on 2026-07-27. The FOMC statement is scheduled for 14:00 ET today, after the cutoff (L002,L007-L008,L069).

## Regime evidence

| Signal | Observation | Interpretation | Ledger |
|---|---|---|---|
| SPY trend | close $740.86; MA20 746.65; MA50 743.98; mom20 -0.02% | Mixed short-term trend; 60d momentum remains positive | L010,L042,L065 |
| VIX | 18.21; 20d mean 16.9675 | Elevated but below HIGH_VOL classification threshold evidence | L007 |
| QQQ | mom20 -6.71%; RS20 -6.69pp | Growth underperforms SPY | L066 |
| SOXX | mom20 -20.00%; drawdown60 -24.97% | High-vol semiconductor watch | L067 |
| FOMC | Statement 14:00 ET; press conference 14:30 ET | Same-day event risk; outcome unavailable at cutoff | L069 |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | $740.86 | 2026-07-28 | HISTORICAL | MIXED (746.65/743.98) | 3.62% | 1.000 | 0.50% | 3.62% | REALIZED_VOL_30D | $744.56 | 2026-08-26 | $716.71 | $772.42 | MEDIUM | L065 |
| QQQ | $675.49 | 2026-07-28 | HISTORICAL | BEARISH (708.06/716.37) | 7.27% | 1.731 | -0.63% | 7.27% | REALIZED_VOL_30D | $671.20 | 2026-08-26 | $620.13 | $722.28 | MEDIUM | L066 |
| SOXX | $491.46 | 2026-07-28 | HISTORICAL | BEARISH (555.62/568.10) | 18.86% | 3.648 | 0.32% | 18.86% | REALIZED_VOL_30D | $493.05 | 2026-08-26 | $396.67 | $589.44 | MEDIUM | L067 |

Relative strength: QQQ/SPY is -6.69pp over 20d and -2.08pp over 60d. SOXX/SPY is -19.98pp over 20d and 3.21pp over 60d. The forecasts are consistent with a `NEUTRAL` broad-market prior and explicit negative relative-view adjustments for QQQ/SOXX.

## Universe handoff

The helper produced 515 union tickers. Histories were fetched for all 518 requested symbols; FDXF has only 43 bars, leaving 514 sourceable equities. Ten binding reflection `DROP` names were then excluded, so 504 equities were scored. The 514 sourceable equities plus SPY/QQQ/SOXX were handed to technical computation through `technical_indicators.json`; only the 504-name post-reflection set entered factor scoring (L001,L003,L010,L038,L044).
