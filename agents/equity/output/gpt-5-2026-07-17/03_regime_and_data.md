# Regime and Data — 2026-07-17

- Data mode: `DELAYED`. Entry quotes are current-run intraday Yahoo/Nasdaq pairs dated 2026-07-17; risk histories use completed Nasdaq closes through 2026-07-16.
- Regime: `NEUTRAL` (L155). SPY’s 60d trend remains positive, but its daily alignment is mixed and MACD crossed bearish; QQQ/SOXX short-window momentum and relative strength deteriorated.
- Event concentration: the official FOMC calendar places a July 28–29 meeting inside the forecast horizon (L006).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | DD from 60d High | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 743.625 | 2026-07-17 | DELAYED | close 743.83; MA20 745.05; MA50 744.39 (MIXED) | 4.50% RISING | 1.00 | -1.17% | +0.50% | 4.50% | REALIZED_VOL_30D | 747.343 | 2026-08-14 | 712.546 | 782.140 | MEDIUM | L140,L141,L142,L143,L144 |
| QQQ | 696.750 | 2026-07-17 | DELAYED | close 697.68; MA20 718.46; MA50 719.05 (BEARISH) | 8.80% RISING | 1.71 | -5.39% | +0.86% | 8.80% | REALIZED_VOL_30D | 702.718 | 2026-08-14 | 638.945 | 766.491 | MEDIUM | L145,L146,L147,L148,L149 |
| SOXX | 522.950 | 2026-07-17 | DELAYED | close 524.36; MA20 586.28; MA50 566.42 (MIXED) | 22.09% RISING | 3.67 | -19.01% | +1.84% | 22.09% | REALIZED_VOL_30D | 532.550 | 2026-08-14 | 412.422 | 652.679 | MEDIUM | L150,L151,L152,L153,L154 |

### Relative Strength and Regime Consistency

- QQQ/SPY: 20d `-3.83%`; 60d `+2.63%`.
- SOXX/SPY: 20d `-12.96%`; 60d `+18.99%`.
- Consistency: negative 20d growth/semiconductor relative strength and rising ETF volatility offset the still-positive 60d trend, supporting `NEUTRAL`.

## Universe Handoff

`build_index_universe.py` produced `515` names. `technical_indicators.py` returned 513 scoreable equity records; SATS had zero bars and FDXF had fewer than 60. The exact `eligible_universe.txt` and core ETF list were handed to factor scoring. No sampled fallback was used.
