# 09 Final Report — 2026-07-28

══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-28
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════

## Executive Summary

The run completed on grounded 2026-07-27 closes and classified the regime NEUTRAL. No equity clears the investable evidence bar because Fund_Z and Sent_Z are unavailable and DQ is 80% versus the required 85%. The 20 highest fully earnings-grounded names are published only as monitoring forecasts. A hypothetical equal-weight monitor sleeve has 35% Industrials exposure, above 30%, the 2026-07-29 14:00 ET FOMC statement falls inside the forecast horizon, and the unpenalized SJM/BBY ±5-day earnings bands overlap the target date; the pctl80 beta shortfall is corroborating, not the primary blocker. The committee approves publication as **NO_TRADE**.

## MoM Reflection Summary

The exact same-model baseline is gpt-5-2026-06-30. Its 14 equity forecasts settled with mixed results. This run independently verified all 35 target-date keys, but its agreeing rows are audit-only duplicates because the keys were already canonical; canonical equity calibration remains n=260 / eff_n=1 / 50.77% hit / 74.62% CI, while market forecasts remain n=48 / eff_n=1 / 20.83% hit / 68.75% CI. Track A remains deferred.

## Regime

| Regime | Data quality | Key macro risk | Ledger |
|---|---|---|---|
| NEUTRAL | Required inputs grounded; DQ 0.80 for factor gaps | FOMC meeting 2026-07-28–29, statement 2026-07-29 14:00 ET; VIX 18.67; QQQ/SOXX weak 20d relative strength | L007–L010,L029,L042,L069 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI | Trend | Confidence |
|---|---|---|---|---|---|---|---|
| SPY | $739.09 | +0.50% | 3.64% | $742.79 | $714.83 to $770.74 | MIXED | MEDIUM |
| QQQ | $682.12 | -0.64% | 7.27% | $677.75 | $626.19 to $729.31 | BEARISH | MEDIUM |
| SOXX | $516.23 | +0.32% | 18.58% | $517.90 | $418.14 to $617.66 | BEARISH | MEDIUM |

## Ranked monitoring set — INDEX_UNION_PCTL (n=514)

| Rank | Ticker | Adj Score | Pctl | Tech_Z | Macro_Z | Beta | RVol | Technical state | mu | Target | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RTX | 0.3637 | 100.00 | 1.211 | 0.609 | -0.068 | 9.36% | SELL_SETUP_4; RSI 77.3; ABOVE_SIGNAL | +6.00% | $231.53 | LOW |
| 2 | TRV | 0.3045 | 99.81 | 0.853 | 0.832 | -0.708 | 9.15% | SELL_SETUP_7; RSI 81.7; ABOVE_SIGNAL | +6.00% | $413.77 | LOW |
| 3 | PAYX | 0.2956 | 99.61 | 0.840 | 0.783 | -0.610 | 9.15% | SELL_SETUP_1; RSI 67.5; ABOVE_SIGNAL | +6.00% | $122.41 | LOW |
| 4 | SJM | 0.2715 | 99.42 | 0.771 | 0.721 | -0.762 | 9.49% | SELL_SETUP_8; RSI 64.8; ABOVE_SIGNAL | +6.00% | $128.31 | LOW |
| 5 | CSX | 0.2680 | 99.22 | 0.752 | 0.729 | 0.113 | 7.42% | SELL_SETUP_3; RSI 64.1; ABOVE_SIGNAL | +6.00% | $54.91 | LOW |
| 6 | DGX | 0.2649 | 99.03 | 0.727 | 0.753 | -0.585 | 9.45% | SELL_SETUP_8; RSI 75.0; ABOVE_SIGNAL | +6.00% | $245.75 | LOW |
| 7 | IQV | 0.2551 | 98.83 | 0.975 | 0.176 | 0.148 | 11.29% | SELL_SETUP_3; RSI 65.6; BELOW_SIGNAL | +6.00% | $226.01 | LOW |
| 8 | BBY | 0.2520 | 98.64 | 0.948 | 0.205 | 0.823 | 8.94% | SELL_SETUP_2; RSI 71.0; BULLISH_CROSS | +6.00% | $93.76 | LOW |
| 9 | MET | 0.2468 | 98.44 | 1.043 | 0.803 | -0.005 | 7.04% | SELL_SETUP_2; RSI 68.0; BULLISH_CROSS | +6.00% | $100.90 | LOW |
| 10 | UNP | 0.2429 | 98.25 | 0.655 | 0.714 | -0.163 | 7.63% | SELL_SETUP_3; RSI 62.5; ABOVE_SIGNAL | +6.00% | $317.26 | LOW |
| 11 | IVZ | 0.2411 | 98.05 | 1.164 | -0.320 | 1.527 | 11.00% | SELL_SETUP_4; RSI 60.7; ABOVE_SIGNAL | +6.00% | $31.92 | LOW |
| 12 | PRU | 0.2334 | 97.86 | 0.996 | 0.787 | 0.268 | 6.16% | SELL_SETUP_2; RSI 72.4; ABOVE_SIGNAL | +6.00% | $129.20 | LOW |
| 13 | NSC | 0.2330 | 97.66 | 0.613 | 0.716 | -0.101 | 7.24% | SELL_SETUP_3; RSI 64.2; ABOVE_SIGNAL | +6.00% | $363.95 | LOW |
| 14 | ITW | 0.2269 | 97.47 | 0.614 | 0.663 | 0.464 | 6.66% | SELL_SETUP_3; RSI 66.4; ABOVE_SIGNAL | +6.00% | $301.91 | LOW |
| 15 | CTAS | 0.2262 | 97.27 | 0.673 | 0.539 | -0.294 | 10.29% | SELL_SETUP_2; RSI 75.2; ABOVE_SIGNAL | +6.00% | $223.64 | LOW |
| 16 | EXR | 0.2240 | 97.08 | 0.510 | 0.847 | 0.030 | 6.36% | SELL_SETUP_2; RSI 55.3; BULLISH_CROSS | +6.00% | $157.19 | LOW |
| 17 | MPC | 0.2221 | 96.88 | 1.050 | 0.583 | -0.432 | 9.46% | BUY_SETUP_3; RSI 69.7; ABOVE_SIGNAL | +6.00% | $331.09 | LOW |
| 18 | WELL | 0.2176 | 96.69 | 0.521 | 0.772 | -0.573 | 6.89% | SELL_SETUP_9; RSI 67.6; ABOVE_SIGNAL | +6.00% | $263.24 | LOW |
| 19 | CB | 0.2161 | 96.49 | 0.416 | 0.969 | -0.980 | 8.03% | SELL_SETUP_3; RSI 59.4; BULLISH_CROSS | +6.00% | $380.44 | LOW |
| 20 | PM | 0.2039 | 96.30 | 0.548 | 0.603 | -0.546 | 9.26% | SELL_SETUP_2; RSI 62.0; ABOVE_SIGNAL | +6.00% | $207.40 | LOW |

## No-trade rationale

Zero names are investable; no weights or portfolio analytics are produced. Price and sigma lineage pass, but evidence threshold #2 (3 of 4 families) and threshold #4 (≥85% completeness) fail universally. Industrials concentration is 35% at equal weight and therefore also fails the sector cap; pctl80 maximum beta 0.889447 is a corroborating diagnostic only.

## Assumptions and limitations

Returns, volatility, beta, correlation, and indicators use adjusted closes; entry/target/CI use raw closes. Normal VaR/CVaR and 70% CI formulas are model assumptions. Fund_Z, Sent_Z, and Enhancing feeds are UNAVAILABLE. Forecasts target 2026-08-25 and must be settled against their recorded fields.

Next scheduled review: 2026-07-28 midday monitor, then 2026-07-28 pre-close/close; next full daily run 2026-07-29 pre-open.
