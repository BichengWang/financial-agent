# 03 Regime and Data — 2026-07-28

Data mode is **DELAYED**, with 2026-07-27 completed-close prices. Regime is **NEUTRAL** (INFERRED): VIX 18.67 versus a 20-day mean of 16.8795, SPY +1.39% over 20d and +4.13% over 60d, and the 3-month T-bill at 3.81% (L007,L008,L042). The official Federal Reserve calendar places a two-day FOMC meeting on 2026-07-28–29, with the statement scheduled for 14:00 ET on 2026-07-29, inside the forecast horizon (L069). The earnings score-penalty window captures MET, PRU, and MPC (nominal 7–8 days, within the buffered ≤19-day threshold), so event concentration fails for a hypothetical sleeve. Separately, SJM and BBY are unpenalized because their nominal dates are 29–30 days away, but their ±5-day estimate bands overlap the 2026-08-25 forecast target; they remain horizon-risk flags. These flags do not create weights in a NO_TRADE run.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | $739.09 | 2026-07-27 | HISTORICAL | MIXED ($746.66/$744.09) | 3.64% | 1.0000 | +0.50% | 3.64% | REALIZED_VOL_30D | $742.79 | 2026-08-25 | $714.83 | $770.74 | MEDIUM | L006,L011,L013,L016,L065 |
| QQQ | $682.12 | 2026-07-27 | HISTORICAL | BEARISH ($710.49/$717.24) | 7.27% | 1.7200 | -0.64% | 7.27% | REALIZED_VOL_30D | $677.75 | 2026-08-25 | $626.19 | $729.31 | MEDIUM | L006,L011,L013,L016,L066 |
| SOXX | $516.23 | 2026-07-27 | HISTORICAL | BEARISH ($561.77/$568.86) | 18.58% | 3.6474 | +0.32% | 18.58% | REALIZED_VOL_30D | $517.90 | 2026-08-25 | $418.14 | $617.66 | MEDIUM | L006,L011,L013,L016,L067 |

QQQ/SPY relative strength is -4.84% over 20d and -0.91% over 60d. SOXX/SPY is -13.88% over 20d and +10.64% over 60d. The QQQ and SOXX relative-view adjustment is -1.5pp; SOXX's absolute mu is below 0.5%, so it is a flat call for later direction scoring. The bearish growth/semiconductor short-window trend is consistent with a NEUTRAL rather than BULL regime.

Universe handoff: 514 scored equities; FDXF excluded for insufficient listing age. ETFs are a distinct market-forecast sleeve, never equity candidates.
