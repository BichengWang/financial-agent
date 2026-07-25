# 03 Regime and Data — 2026-07-24

- Data mode: **DELAYED**; completed close date 2026-07-24.
- Regime: **NEUTRAL** with a high-volatility semiconductor watch (L011).
- Universe handoff: 515 index-union names; 511 scoreable; BRK-B, FDX, FDXF, FER excluded before scoring (L009).
- Event screen: July 28–29 FOMC is inside the 28-day horizon (L006); 3 top-20 equities and 6 names in the full monitoring sleeve are inside buffered earnings windows. Penalties are applied, but event names can be omitted from a feasible basket, so this is not an independent NO_TRADE cause.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 738.9300 | 2026-07-24 | DELAYED | close 738.93; MA20 746.15; MA50 745.07; MIXED | 3.92% | 1.000 | +0.50% | 3.92% | REALIZED_VOL_30D | 742.6200 | 2026-08-21 | 712.5200 | 772.7300 | MEDIUM | L012,L013,L014,L015 |
| QQQ | 684.2300 | 2026-07-24 | DELAYED | close 684.23; MA20 711.71; MA50 718.29; BEARISH | 7.96% | 1.722 | +0.36% | 7.96% | REALIZED_VOL_30D | 686.7000 | 2026-08-21 | 630.0600 | 743.3400 | MEDIUM | L016,L017,L018,L019 |
| SOXX | 527.0100 | 2026-07-24 | DELAYED | close 527.01; MA20 565.45; MA50 569.22; BEARISH | 20.18% | 3.637 | +0.32% | 20.18% | REALIZED_VOL_30D | 528.6900 | 2026-08-21 | 418.0800 | 639.3000 | MEDIUM | L020,L021,L022,L023 |

QQQ/SPY relative strength is -5.12% over 20d and +0.23% over 60d. SOXX/SPY is -16.34% / +16.30%. This is consistent with NEUTRAL broad-market structure and a high-volatility semiconductor watch, not a broad BEAR call.

Volatility is rising for all three ETFs versus the prior 30-day window: SPY 3.92% vs 3.75%, QQQ 7.96% vs 6.40%, and SOXX 20.18% vs 16.92%. Drawdowns from the trailing 60-day highs are -2.72%, -8.30%, and -19.54%, respectively (L013,L017,L021).

Forecast-prior derivation: SPY uses the unadjusted NEUTRAL +0.50% prior. QQQ starts from beta × SPY mu (1.722 × 0.50% = +0.86%) and receives a -0.50pp adjustment for negative 20-day relative strength, producing +0.36% (L016,L017,L018,L019). SOXX starts at +1.82% and receives the maximum -1.50pp adjustment for its -16.34% 20-day relative strength and 20.18% realized volatility, producing +0.32% (L020,L021,L022,L023).

Handoff: the exact 515-name `eligible_universe.txt` plus SPY/QQQ/SOXX produced the canonical `technical_indicators.json` pack. Eligibility and earnings screens then retained 511 names before scoring (L003,L009).
