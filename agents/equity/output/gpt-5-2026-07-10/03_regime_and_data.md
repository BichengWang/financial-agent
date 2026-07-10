# 03 Regime And Data

Data mode: `DELAYED`. Regime: `BULL` with concentrated growth/semiconductor leadership. SPY, QQQ, and SOXX all have positive 60-day momentum; SPY and QQQ retain bullish daily MA alignment, while SOXX daily alignment is mixed. Low volume ratios and QQQ/SOXX daily MACD below signal temper the regime confidence. Ledger: L004,L005,L006,L007,L008,L009,L010,L011,L012,L013,L014,L015.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | 20d/50d MA | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 754.95 | 2026-07-10 | DELAYED | 743.81/741.24 | 4.44% | 1.00 | 2.00% | 4.44% | REALIZED_VOL_30D | 770.05 | 2026-08-07 | 735.16 | 804.94 | MEDIUM | L004,L005,L006,L007 |
| QQQ | 725.51 | 2026-07-10 | DELAYED | 722.57/715.16 | 8.58% | 1.68 | 3.87% | 8.58% | REALIZED_VOL_30D | 753.57 | 2026-08-07 | 688.85 | 818.29 | MEDIUM | L008,L009,L010,L011 |
| SOXX | 581.34 | 2026-07-10 | DELAYED | 599.82/558.23 | 21.79% | 3.52 | 8.04% | 21.79% | REALIZED_VOL_30D | 628.05 | 2026-08-07 | 496.29 | 759.81 | MEDIUM | L012,L013,L014,L015 |

Relative strength: QQQ vs SPY is 0.52% over 20d and 6.71% over 60d; SOXX vs SPY is 3.29% and 36.18%. The forecasts are regime-consistent, with `MEDIUM` confidence because trend and relative strength are not fully confirmed by daily MACD and volume.

Mu derivation: SPY uses the `BULL` +2.00% four-week prior. QQQ uses `1.68 beta x 2.00% + 0.50pp = 3.87%`; SOXX uses `3.52 beta x 2.00% + 1.00pp = 8.04%`. Both relative-view adjustments are within the permitted +/-1.50pp band and are supported by the relative-strength rows above.

Universe handoff: 515 index-union names; 513 scoreable equities after excluding SATS and FDXF for insufficient bars. Core ETFs are isolated from candidate ranks.
