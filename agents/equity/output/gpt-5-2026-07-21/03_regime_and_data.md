# 03 Regime and Data — 2026-07-21

- Data mode: **DELAYED**; completed close date 2026-07-20.
- Regime: **NEUTRAL** with a high-volatility semiconductor watch (L008).
- Universe handoff: 515 index-union names; 513 scoreable; SATS and FDXF excluded before scoring.
- Event concentration: July 28–29 FOMC is inside the 28-day horizon (L005); two top-20 equities fall inside the buffered earnings window.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 742.0900 | 2026-07-20 | DELAYED | close 742.09; MA20 744.79; MA50 744.55; MIXED | 4.52% | 1.000 | +0.50% | 4.52% | REALIZED_VOL_30D | 745.8000 | 2026-08-18 | 710.9000 | 780.7100 | MEDIUM | L009,L010,L011,L012 |
| QQQ | 696.0600 | 2026-07-20 | DELAYED | close 696.06; MA20 716.12; MA50 719.01; BEARISH | 8.87% | 1.732 | +0.37% | 8.87% | REALIZED_VOL_30D | 698.6100 | 2026-08-18 | 634.3800 | 762.8300 | MEDIUM | L013,L014,L015,L016 |
| SOXX | 524.1400 | 2026-07-20 | DELAYED | close 524.14; MA20 580.38; MA50 566.72; MIXED | 22.00% | 3.733 | +0.37% | 22.00% | REALIZED_VOL_30D | 526.0600 | 2026-08-18 | 406.1300 | 646.0000 | MEDIUM | L017,L018,L019,L020 |

QQQ/SPY relative strength is -5.40% over 20d and +1.91% over 60d. SOXX/SPY is -17.41% / +17.05%. This is consistent with NEUTRAL broad-market structure and a high-volatility semiconductor watch, not a broad BEAR call.

Volatility is rising for all three ETFs versus the prior 30-day window: SPY 4.52% vs 2.68%, QQQ 8.87% vs 4.39%, and SOXX 22.00% vs 13.59%. Drawdowns from the trailing 60-day highs are -2.30%, -6.71%, and -19.98%, respectively (ledger rows L010, L014, L018).

Forecast-prior derivation: SPY uses the unadjusted NEUTRAL +0.50% prior. QQQ starts from beta × SPY mu (1.732 × 0.50% = +0.87%) and receives a -0.50pp adjustment for negative 20-day relative strength, producing +0.37% (L014–L016). SOXX starts at +1.87% and receives the maximum -1.50pp adjustment for its -17.41% 20-day relative strength and 22.00% realized volatility, producing +0.37% (L018–L020).

Handoff: the exact 515-name `eligible_universe.txt` plus SPY/QQQ/SOXX produced the canonical `technical_indicators.json` pack before scoring.
