# 03 Regime and Data — 2026-07-20

## Data mode and regime

Data mode is **DELAYED**. Yahoo histories were fetched during this run, then all provisional 2026-07-20 bars were removed because the session was still open; the completed 2026-07-17 basis was independently checked against Nasdaq for every published and settled ticker. Regime is **NEUTRAL with HIGH_VOL semiconductor watch**. SPY is near/below its moving averages, QQQ has -4.07% 20-day relative strength, and SOXX carries 22.0% one-month realized sigma with a -20.3% drawdown from its 60-day high. The July 28–29 FOMC meeting is inside the horizon (L005).

## Core ETF Market Forecast Block

| ETF | Entry | Price Date/Tag | Trend vs 20d/50d | 30d RVol | Beta | mu | sigma | Source | Target / Date | 70% CI | Confidence | Ledger |
|---|---:|---|---|---:|---:|---:|---:|---|---|---|---|---|
| SPY | 743.2900 | 2026-07-17 DELAYED | 743.29 vs 745.02/744.38 (MIXED) | 4.54% | 1.000 | +0.50% | 4.54% | REALIZED_VOL_30D | 747.01 / 2026-08-17 | 711.94–782.08 | MEDIUM | L009,L010,L011,L012 |
| QQQ | 695.3300 | 2026-07-17 DELAYED | 695.33 vs 718.35/719.01 (BEARISH) | 8.87% | 1.733 | +0.37% | 8.87% | REALIZED_VOL_30D | 697.90 / 2026-08-17 | 633.75–762.06 | LOW | L013,L014,L015,L016 |
| SOXX | 521.8100 | 2026-07-17 DELAYED | 521.81 vs 586.15/566.37 (MIXED) | 22.04% | 3.710 | +0.35% | 22.04% | REALIZED_VOL_30D | 523.64 / 2026-08-17 | 404.04–643.23 | LOW | L017,L018,L019,L020 |

QQQ/SPY relative strength is -4.07% / +2.35% over 20/60 bars; SOXX/SPY is -13.30% / +18.46%. This supports a NEUTRAL broad call with a high-vol growth warning, not a BEAR call.

## ETF volatility and drawdown check

| ETF | Current 30d RVol | Prior 30d RVol | Direction | Drawdown from 60d high | Ledger Rows |
|---|---:|---:|---|---:|---|
| SPY | 4.54% | 2.76% | RISING | -2.14% | L010,L011 |
| QQQ | 8.87% | 4.45% | RISING | -6.81% | L014,L015 |
| SOXX | 22.04% | 13.34% | RISING | -20.34% | L018,L019 |

The regime label is an analyst inference (L008); the table inputs are completed-history derivations, not intraday observations.

## Universe and event handoff

`build_index_universe.py` materialized 515 names. **513** have ≥60 completed bars and pass the price, liquidity, and listing-age gates; exclusions are `{'FDXF': 'fewer than 60 completed bars', 'SATS': 'fewer than 60 completed bars'}`. The full list plus SPY/QQQ/SOXX was handed to `technical_indicators.py`; sampled fallback was not used.

Earnings were checked for the top-65 preflight and every baseline carry candidate using Nasdaq confirmed dates or +91-day cadence estimates tagged ±5d. **0** of the 23 monitor forecasts land inside the buffered 14-day window. No event exposure is sized because the final state is NO_TRADE.
