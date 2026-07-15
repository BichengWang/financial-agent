# 03 Regime And Data

Data mode: `DELAYED`. This late daily run uses two-source-grounded July 15 late-session entry prices. The technical helper and ranks use a 15:41 ET partial bar; completed risk histories end July 14. Regime: `BULL` with `MEDIUM` confidence and a short-horizon cooling flag. SPY is above its daily 20d/50d averages with positive 60d momentum; QQQ and SOXX are mixed on daily alignment and have negative 20d but positive 60d relative strength. Regime ledger rows: L250,L013,L019,L025.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | 20d/50d MA | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 754.440 | 2026-07-15 | DELAYED | 744.84/743.32 | 4.47% | 1.00 | +2.00% | 4.47% | REALIZED_VOL_30D | 769.53 | 2026-08-12 | 734.44 | 804.62 | MEDIUM | L008,L009,L010,L011,L012,L013 |
| QQQ | 717.730 | 2026-07-15 | DELAYED | 720.86/718.05 | 8.74% | 1.69 | +3.63% | 8.74% | REALIZED_VOL_30D | 743.76 | 2026-08-12 | 678.54 | 808.99 | MEDIUM | L014,L015,L016,L017,L018,L019 |
| SOXX | 555.695 | 2026-07-15 | DELAYED | 593.08/564.22 | 22.28% | 3.60 | +7.69% | 22.28% | REALIZED_VOL_30D | 598.44 | 2026-08-12 | 469.69 | 727.19 | MEDIUM | L020,L021,L022,L023,L024,L025 |

Realized-volatility direction and 60-day-high drawdown: SPY 30d RVol is 4.47% versus 2.93% in the prior 30d (rising), with a -1.02% drawdown; QQQ is 8.74% versus 4.57% (rising), with a -3.55% drawdown; SOXX is 22.28% versus 12.81% (rising), with a -13.30% drawdown. Ledger: L011,L017,L023.

Daily relative strength: QQQ/SPY -3.52% over 20d and 4.32% over 60d; SOXX/SPY -11.55% and 27.36%. SPY uses the BULL +2.00% prior. QQQ and SOXX use beta times SPY mu plus the disclosed positive 60d/negative 20d relative-view adjustment; confidence remains MEDIUM.

Universe handoff: 515 index-union names; 513 scoreable equities after SATS and FDXF failed the 60-bar minimum. VRTX's first HTTP 400 cleared on a documented helper retry. Price and listing-age screens pass for scored names; unavailable Enhancing screens lower DQ but are not Required blockers.

## Event Concentration

- Buffered earnings penalty window: 2 of 20 monitors (VLO, AAPL). These remain LOW-confidence monitoring forecasts and receive the 0.10 penalty.
- Forecast-horizon earnings: 12 of 20 estimates fall on or before 2026-08-12; this adds gap-risk concentration without creating a new positive score input.
- Macro event: the Federal Reserve's July 28-29 FOMC meeting falls inside the 28-day forecast horizon. Ledger: L244.
- Regime consistency: broad-market long trend is BULL-consistent; growth/semi short-horizon weakness prevents HIGH confidence.
