# 03 Regime and Data — 2026-07-22

- Data mode: **DELAYED**; completed close date 2026-07-22.
- Regime: **NEUTRAL** with a high-volatility semiconductor watch (L008).
- Universe handoff: 515 index-union names; 514 scoreable; SATS→ECHO source remap applied and FDXF excluded before scoring.
- Event concentration: July 28–29 FOMC is inside the 28-day horizon (L005); three top-20 equities fall inside the buffered earnings window.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 747.4100 | 2026-07-22 | DELAYED | close 747.41; MA20 745.67; MA50 745.08; BULLISH | 4.02% | 1.000 | +0.50% | 4.02% | REALIZED_VOL_30D | 751.1500 | 2026-08-19 | 719.9000 | 782.3900 | MEDIUM | L009,L010,L011,L012 |
| QQQ | 705.3500 | 2026-07-22 | DELAYED | close 705.35; MA20 714.25; MA50 719.17; BEARISH | 7.98% | 1.733 | +0.37% | 7.98% | REALIZED_VOL_30D | 707.9400 | 2026-08-19 | 649.4000 | 766.4800 | MEDIUM | L013,L014,L015,L016 |
| SOXX | 555.5200 | 2026-07-22 | DELAYED | close 555.52; MA20 572.88; MA50 568.63; MIXED | 20.11% | 3.784 | +0.39% | 20.11% | REALIZED_VOL_30D | 557.7000 | 2026-08-19 | 441.5000 | 673.9000 | MEDIUM | L017,L018,L019,L020 |

QQQ/SPY relative strength is -3.05% over 20d and +1.56% over 60d. SOXX/SPY is -9.82% / +15.66%. This is consistent with NEUTRAL broad-market structure and a high-volatility semiconductor watch, not a broad BEAR call.

Volatility is rising for all three ETFs versus the prior 30-day window: SPY 4.02% vs 3.49%, QQQ 7.98% vs 6.09%, and SOXX 20.11% vs 16.89%. Drawdowns from the trailing 60-day highs are -1.60%, -5.47%, and -15.19%, respectively (ledger rows L010, L014, L018).

Forecast-prior derivation: SPY uses the unadjusted NEUTRAL +0.50% prior. QQQ starts from beta × SPY mu (1.733 × 0.50% = +0.87%) and receives a -0.50pp adjustment for negative 20-day relative strength, producing +0.37%. SOXX starts at +1.89% and receives the maximum -1.50pp adjustment for its -9.82% 20-day relative strength and 20.11% realized volatility, producing +0.39%.

Handoff: the exact 515-name `eligible_universe.txt` plus SPY/QQQ/SOXX produced the canonical `technical_indicators.json` pack before scoring.
