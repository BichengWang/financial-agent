# 07 — Portfolio Proposal — 2026-08-28

**Status: `NO_TRADE`. No weights are proposed.** `rules.md § Stop Criteria` (Downgrade to `NO_TRADE`
#1) fires: zero names pass the investable threshold, against a minimum of 5. The analytics below are
published as the **evidence** for that decision, not as a portfolio.

## Task 0 — constraint feasibility pre-check (before any sizing)

Run per `agents.md § Portfolio Construction Agent` task 0, from already-fetched inputs.

| Quantity | Value | Bound | Verdict |
|---|---|---|---|
| Investable-percentile pool (≥ 80th pctl) | 102 names | — | — |
| Single-name cap | 5.0% NAV | `rules.md § Risk Controls` (protected) | implies **≥ 20 names** in any compliant book |
| Maximum attainable sleeve beta | **+1.1177** | 0.90 floor | **≥ floor — the beta band is FEASIBLE** |
| Minimum attainable sleeve beta | -0.5713 | 1.10 ceiling | ≤ ceiling |
| Share of the scored universe at negative 60d beta | 43.33% | — | structural headwind, not a bar |

The maximum attainable beta is the mean of the 20 highest 60-day betas in the ≥80th-percentile pool —
the best case a 5%-capped book can reach. At **+1.1177** it clears the 0.90 floor, so the
beta band is **feasible this run**. This must be recomputed every run: the two immediately preceding
packages (2026-08-22 at +0.4841 and 2026-08-27 at +0.2919) were provably **infeasible**, and reusing
either narrative here would be wrong. Feasibility is not why this run does not trade.

## What a naive equal-weight sleeve would look like

Constructed only to test the portfolio-level caps against a concrete book. It is **not** a
recommendation and no name is investable.

| Analytic | Top-20 EW | Top-24 EW | Cap (rules.md § Risk Controls) | Top-20 verdict |
|---|---|---|---|---|
| Weight per name | 5.00% | 4.17% | ≤ 5.00% | PASS |
| Portfolio beta to SPY | **+0.0351** | +0.1359 | 0.90 – 1.10 | **FAIL — far below the floor** |
| Average pairwise correlation | 0.2068 | 0.2058 | < 0.45 | PASS |
| Portfolio sigma (1-month) | 4.61% | 4.65% | — | — |
| 95th-pctl 1-month drawdown | 7.60% | 7.67% | ≤ 8.00% | PASS |
| Tracking error (1-month) | 4.60% | 4.62% | — | — |
| Expected Sharpe | 1.2352 | 1.2234 | — | — |
| Expected Information Ratio | 1.2882 | 1.2404 | — | — |
| VaR95 (1-month return space) | -1.60% | -1.67% | — | normality assumed |
| CVaR95 (1-month return space) | -3.49% | -3.58% | — | normality assumed |
| Largest sector share | 30.00% | 33.33% | ≤ 30.00% | **at the cap** (30.00%) |

Two independent facts about that naive sleeve are worth recording. First, its realized beta of
**+0.0351** is nowhere near the 0.90–1.10 band, so an equal-weight book over the top ranks
would itself be non-compliant — even though a *beta-targeted* book drawn from the same pool is
feasible (Task 0 above). Second, correlation (0.2068) and 95th-percentile drawdown
(7.60%) both pass comfortably: the sleeve is disqualified for being **too defensive**,
not too risky. The top-24 variant additionally breaches the 30% sector cap at
33.33% Finance.

Portfolio sigma is `sqrt(w' Σ w)` from the fetched 60-day covariance of adjusted returns scaled by
`sqrt(21)`; the 95th-percentile 1-month drawdown is the parametric `1.65 x portfolio_sigma_1m`
estimate and assumes normality. Inputs: L500+, L600+, L004.

## Correlation matrix — naive top-20 sleeve (60 daily adjusted return intervals)

|   | RJF | SCHW | BLK | RVTY | SJM | APD | BDX | BNY | IQV | GIS | NWSA | NDAQ | NWS | VEEV | A | RMD | ABT | STT | JNJ | VRTX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RJF | +1.00 | +0.74 | +0.59 | -0.23 | +0.01 | +0.36 | +0.13 | +0.48 | +0.14 | +0.20 | +0.39 | +0.53 | +0.38 | +0.10 | -0.19 | +0.45 | +0.14 | +0.50 | +0.09 | +0.24 |
| SCHW | +0.74 | +1.00 | +0.44 | -0.36 | -0.02 | +0.22 | +0.03 | +0.38 | +0.11 | +0.18 | +0.31 | +0.40 | +0.29 | +0.08 | -0.23 | +0.28 | +0.21 | +0.38 | +0.21 | +0.08 |
| BLK | +0.59 | +0.44 | +1.00 | +0.00 | -0.02 | +0.23 | +0.20 | +0.51 | +0.04 | +0.13 | +0.28 | +0.50 | +0.28 | +0.07 | +0.01 | +0.28 | +0.12 | +0.41 | -0.20 | +0.10 |
| RVTY | -0.23 | -0.36 | +0.00 | +1.00 | +0.16 | +0.03 | +0.43 | -0.04 | +0.51 | +0.11 | +0.01 | +0.03 | -0.00 | +0.09 | +0.70 | +0.26 | +0.15 | -0.18 | -0.06 | +0.15 |
| SJM | +0.01 | -0.02 | -0.02 | +0.16 | +1.00 | +0.09 | +0.41 | -0.24 | +0.23 | +0.59 | +0.35 | +0.20 | +0.33 | +0.23 | +0.13 | +0.25 | +0.31 | -0.26 | +0.40 | +0.03 |
| APD | +0.36 | +0.22 | +0.23 | +0.03 | +0.09 | +1.00 | +0.08 | +0.10 | +0.03 | +0.16 | +0.11 | +0.35 | +0.10 | +0.10 | +0.09 | +0.07 | +0.10 | +0.05 | -0.02 | +0.20 |
| BDX | +0.13 | +0.03 | +0.20 | +0.43 | +0.41 | +0.08 | +1.00 | -0.09 | +0.52 | +0.55 | +0.53 | +0.31 | +0.52 | +0.32 | +0.39 | +0.64 | +0.63 | -0.25 | +0.34 | +0.40 |
| BNY | +0.48 | +0.38 | +0.51 | -0.04 | -0.24 | +0.10 | -0.09 | +1.00 | -0.18 | -0.12 | -0.02 | +0.19 | -0.01 | -0.23 | -0.10 | +0.11 | -0.07 | +0.85 | -0.08 | +0.13 |
| IQV | +0.14 | +0.11 | +0.04 | +0.51 | +0.23 | +0.03 | +0.52 | -0.18 | +1.00 | +0.37 | +0.33 | +0.37 | +0.30 | +0.34 | +0.52 | +0.41 | +0.30 | -0.24 | +0.25 | +0.35 |
| GIS | +0.20 | +0.18 | +0.13 | +0.11 | +0.59 | +0.16 | +0.55 | -0.12 | +0.37 | +1.00 | +0.43 | +0.35 | +0.42 | +0.38 | +0.13 | +0.39 | +0.39 | -0.19 | +0.31 | +0.14 |
| NWSA | +0.39 | +0.31 | +0.28 | +0.01 | +0.35 | +0.11 | +0.53 | -0.02 | +0.33 | +0.43 | +1.00 | +0.39 | +0.99 | +0.37 | -0.05 | +0.53 | +0.46 | -0.10 | +0.23 | +0.18 |
| NDAQ | +0.53 | +0.40 | +0.50 | +0.03 | +0.20 | +0.35 | +0.31 | +0.19 | +0.37 | +0.35 | +0.39 | +1.00 | +0.39 | +0.37 | +0.19 | +0.40 | +0.27 | +0.15 | +0.02 | +0.09 |
| NWS | +0.38 | +0.29 | +0.28 | -0.00 | +0.33 | +0.10 | +0.52 | -0.01 | +0.30 | +0.42 | +0.99 | +0.39 | +1.00 | +0.35 | -0.07 | +0.53 | +0.46 | -0.11 | +0.21 | +0.17 |
| VEEV | +0.10 | +0.08 | +0.07 | +0.09 | +0.23 | +0.10 | +0.32 | -0.23 | +0.34 | +0.38 | +0.37 | +0.37 | +0.35 | +1.00 | +0.21 | +0.30 | +0.18 | -0.23 | +0.16 | +0.26 |
| A | -0.19 | -0.23 | +0.01 | +0.70 | +0.13 | +0.09 | +0.39 | -0.10 | +0.52 | +0.13 | -0.05 | +0.19 | -0.07 | +0.21 | +1.00 | +0.24 | +0.11 | -0.19 | -0.01 | +0.20 |
| RMD | +0.45 | +0.28 | +0.28 | +0.26 | +0.25 | +0.07 | +0.64 | +0.11 | +0.41 | +0.39 | +0.53 | +0.40 | +0.53 | +0.30 | +0.24 | +1.00 | +0.47 | +0.01 | +0.25 | +0.46 |
| ABT | +0.14 | +0.21 | +0.12 | +0.15 | +0.31 | +0.10 | +0.63 | -0.07 | +0.30 | +0.39 | +0.46 | +0.27 | +0.46 | +0.18 | +0.11 | +0.47 | +1.00 | -0.11 | +0.39 | +0.34 |
| STT | +0.50 | +0.38 | +0.41 | -0.18 | -0.26 | +0.05 | -0.25 | +0.85 | -0.24 | -0.19 | -0.10 | +0.15 | -0.11 | -0.23 | -0.19 | +0.01 | -0.11 | +1.00 | -0.03 | +0.12 |
| JNJ | +0.09 | +0.21 | -0.20 | -0.06 | +0.40 | -0.02 | +0.34 | -0.08 | +0.25 | +0.31 | +0.23 | +0.02 | +0.21 | +0.16 | -0.01 | +0.25 | +0.39 | -0.03 | +1.00 | +0.46 |
| VRTX | +0.24 | +0.08 | +0.10 | +0.15 | +0.03 | +0.20 | +0.40 | +0.13 | +0.35 | +0.14 | +0.18 | +0.09 | +0.17 | +0.26 | +0.20 | +0.46 | +0.34 | +0.12 | +0.46 | +1.00 |

Distribution over the 190 distinct pairs: mean **0.2068**, minimum
**-0.3616** (SCHW/RVTY), maximum **+0.9895**
(NWSA/NWS). The 0.45 cap is not approached.

## Sector concentration — naive top-20 sleeve

| Sector | Names | Weight | vs 30% cap |
|---|---|---|---|
| Finance | 6 | 30.00% | **at cap** |
| Health Care | 6 | 30.00% | **at cap** |
| Industrials | 2 | 10.00% | ok |
| Consumer Staples | 2 | 10.00% | ok |
| Consumer Discretionary | 2 | 10.00% | ok |
| Basic Materials | 1 | 5.00% | ok |
| Technology | 1 | 5.00% | ok |

## Factor exposure summary

| Family | Live weight | Share of conviction | State |
|---|---|---|---|
| Fundamental | 0.30 | 0.00% | `UNAVAILABLE` (L018) |
| Technical / Price | 0.30 | **66.67%** | live — 6 distinct slots |
| Sentiment / Positioning | 0.25 | 0.00% | `UNAVAILABLE` (L019) |
| Macro / Regime | 0.15 | 33.33% | live — 4 slots |

Factor crowding **flagged**: more than half the conviction loads on one family, per
`rules.md § Risk Controls` (Portfolio Level). This is structural, not a property of this cross-section.

## Per-position Recommendation Metrics — monitoring sleeve

Values inherited from `05` with no recomputation.

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RJF | 179.36 | 2026-08-28 | `DELAYED` | 190.12 | 2026-09-25 | +6.00% | 5.68% | `REALIZED_VOL_30D` | 1.0013 | 1.4956 | 0.8473 | 4.6475 | -3.37% | -5.70% | -6.10% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 58.60 / 65.28 / 62.54 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 179.52 | 200.72 | Tech +1.0136 / Macro +0.9056 x 0.80 - 0.00 = +0.3519 | L200, L300, L400, L500, L600, L700 |
| SCHW | 110.16 | 2026-08-28 | `DELAYED` | 116.77 | 2026-09-25 | +6.00% | 5.74% | `REALIZED_VOL_30D` | 0.9917 | 1.5192 | 0.9509 | 4.5592 | -3.46% | -5.82% | -5.36% | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 57.26 / 68.35 / 67.81 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 110.20 | 123.34 | Tech +1.1470 / Macro +0.6268 x 0.80 - 0.00 = +0.3505 | L201, L301, L401, L501, L601, L701 |
| BLK | 1,164.48 | 2026-08-28 | `DELAYED` | 1,234.35 | 2026-09-25 | +6.00% | 6.64% | `REALIZED_VOL_30D` | 0.8567 | 1.8291 | 0.6017 | 3.4026 | -4.96% | -7.68% | -10.14% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 59.90 / 62.10 / 61.08 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 1,153.94 | 1,314.76 | Tech +0.9108 / Macro +0.9469 x 0.80 - 0.00 = +0.3322 | L202, L302, L402, L502, L602, L702 |
| RVTY | 128.80 | 2026-08-28 | `DELAYED` | 136.53 | 2026-09-25 | +6.00% | 9.86% | `REALIZED_VOL_30D` | 0.5769 | 1.1665 | 0.4894 | 1.5428 | -10.27% | -14.31% | -6.38% | SELL_SETUP_8 / SELL_SETUP_4 / SELL_SETUP_3 | 69.84 / 71.13 / 59.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 123.32 | 149.74 | Tech +1.2627 / Macro +0.0683 x 0.80 - 0.00 = +0.3112 | L203, L303, L403, L503, L603, L703 |
| SJM | 132.34 | 2026-08-28 | `DELAYED` | 140.28 | 2026-09-25 | +6.00% | 8.47% | `REALIZED_VOL_30D` | 0.6719 | 1.2070 | 0.7061 | 2.0929 | -7.97% | -11.44% | -8.42% | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.68 / 74.74 / 63.18 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 128.63 | 151.93 | Tech +1.3010 / Macro -0.0364 x 0.80 - 0.00 = +0.3079 | L204, L304, L404, L504, L604, L704 |
| APD | 308.09 | 2026-08-28 | `DELAYED` | 326.58 | 2026-09-25 | +6.00% | 5.14% | `REALIZED_VOL_30D` | 1.1074 | 1.5949 | 0.7072 | 5.6845 | -2.48% | -4.58% | -6.88% | SELL_SETUP_6 / SELL_SETUP_4 / SELL_SETUP_8 | 58.03 / 59.93 / 58.12 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 310.12 | 343.03 | Tech +0.9050 / Macro +0.7460 x 0.80 - 0.00 = +0.3067 | L205, L305, L405, L505, L605, L705 |
| BDX | 189.52 | 2026-08-28 | `DELAYED` | 200.89 | 2026-09-25 | +6.00% | 7.47% | `REALIZED_VOL_30D` | 0.7612 | 1.9629 | 0.7356 | 2.6860 | -6.33% | -9.39% | -7.45% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 70.05 / 70.20 / 60.81 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 186.16 | 215.62 | Tech +1.0080 / Macro +0.5071 x 0.80 - 0.00 = +0.3028 | L206, L306, L406, L506, L606, L706 |
| BNY | 162.50 | 2026-08-28 | `DELAYED` | 172.25 | 2026-09-25 | +6.00% | 5.23% | `REALIZED_VOL_30D` | 1.0881 | 1.5414 | 0.7845 | 5.4887 | -2.63% | -4.77% | -5.69% | SELL_SETUP_4 / SELL_SETUP_9 / SELL_SETUP_9 | 57.98 / 76.13 / 91.36 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 163.42 | 181.08 | Tech +0.6788 / Macro +1.1645 x 0.80 - 0.00 = +0.3026 | L207, L307, L407, L507, L607, L707 |
| IQV | 261.75 | 2026-08-28 | `DELAYED` | 277.46 | 2026-09-25 | +6.00% | 14.20% | `REALIZED_VOL_30D` | 0.4007 | 1.2765 | 0.5171 | 0.7443 | -17.42% | -23.24% | -10.23% | SELL_SETUP_8 / SELL_SETUP_9 / SELL_SETUP_3 | 72.36 / 73.07 / 61.86 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 238.81 | 316.10 | Tech +1.3115 / Macro -0.1061 x 0.80 - 0.00 = +0.3020 | L208, L308, L408, L508, L608, L708 |
| GIS | 41.55 | 2026-08-28 | `DELAYED` | 44.04 | 2026-09-25 | +6.00% | 9.16% | `REALIZED_VOL_30D` | 0.6213 | 1.0204 | 0.6594 | 1.7894 | -9.11% | -12.86% | -8.14% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_1 | 67.38 / 61.82 / 42.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 40.09 | 48.00 | Tech +1.2360 / Macro +0.0017 x 0.80 - 0.00 = +0.2968 | L209, L309, L409, L509, L609, L709 |
| NWSA | 30.97 | 2026-08-28 | `DELAYED` | 32.83 | 2026-09-25 | +6.00% | 8.37% | `REALIZED_VOL_30D` | 0.6793 | 0.9706 | 0.8450 | 2.1389 | -7.82% | -11.25% | -9.72% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 68.15 / 68.78 / 62.08 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 30.13 | 35.53 | Tech +1.2434 / Macro -0.0466 x 0.80 - 0.00 = +0.2928 | L210, L310, L410, L510, L610, L710 |
| NDAQ | 99.31 | 2026-08-28 | `DELAYED` | 105.27 | 2026-09-25 | +6.00% | 4.29% | `REALIZED_VOL_30D` | 1.3269 | 2.8460 | 0.6005 | 8.1622 | -1.07% | -2.83% | -15.59% | SELL_SETUP_7 / SELL_SETUP_7 / SELL_SETUP_2 | 69.08 / 62.82 / 61.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 100.84 | 109.70 | Tech +0.6788 / Macro +1.0661 x 0.80 - 0.00 = +0.2909 | L211, L311, L411, L511, L611, L711 |
| NWS | 34.85 | 2026-08-28 | `DELAYED` | 36.94 | 2026-09-25 | +6.00% | 8.83% | `REALIZED_VOL_30D` | 0.6444 | 1.0105 | 0.7987 | 1.9250 | -8.57% | -12.18% | -10.48% | BUY_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_3 | 64.48 / 66.46 / 61.28 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 33.74 | 40.14 | Tech +1.2034 / Macro -0.0136 x 0.80 - 0.00 = +0.2872 | L212, L312, L412, L512, L612, L712 |
| VEEV | 276.69 | 2026-08-28 | `DELAYED` | 293.29 | 2026-09-25 | +6.00% | 16.72% | `REALIZED_VOL_30D` | 0.3403 | 1.0230 | 0.3466 | 0.5367 | -21.58% | -28.44% | -14.30% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 74.85 / 72.75 / 59.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 245.19 | 341.40 | Tech +1.4098 / Macro -0.4328 x 0.80 - 0.00 = +0.2864 | L213, L313, L413, L513, L613, L713 |
| A | 153.84 | 2026-08-28 | `DELAYED` | 163.07 | 2026-09-25 | +6.00% | 7.97% | `REALIZED_VOL_30D` | 0.7135 | 1.2798 | 0.6286 | 2.3597 | -7.16% | -10.42% | -10.15% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_4 | 61.01 / 65.27 / 59.19 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 150.31 | 175.83 | Tech +1.0750 / Macro +0.1335 x 0.80 - 0.00 = +0.2740 | L214, L314, L414, L514, L614, L714 |
| RMD | 240.33 | 2026-08-28 | `DELAYED` | 254.75 | 2026-09-25 | +6.00% | 9.70% | `REALIZED_VOL_30D` | 0.5863 | 0.9239 | 0.5344 | 1.5935 | -10.01% | -13.99% | -12.68% | SELL_SETUP_8 / SELL_SETUP_5 / SELL_SETUP_1 | 69.57 / 61.48 / 53.00 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 230.50 | 279.00 | Tech +0.9021 / Macro +0.4767 x 0.80 - 0.00 = +0.2737 | L215, L315, L415, L515, L615, L715 |
| ABT | 112.47 | 2026-08-28 | `DELAYED` | 119.22 | 2026-09-25 | +6.00% | 6.13% | `REALIZED_VOL_30D` | 0.9282 | 1.4724 | 0.7307 | 3.9944 | -4.11% | -6.62% | -7.18% | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 59.70 / 61.49 / 51.08 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 112.05 | 126.39 | Tech +0.7488 / Macro +0.7715 x 0.80 - 0.00 = +0.2723 | L216, L316, L416, L516, L616, L716 |
| STT | 193.33 | 2026-08-28 | `DELAYED` | 204.93 | 2026-09-25 | +6.00% | 6.55% | `REALIZED_VOL_30D` | 0.8679 | 1.1180 | 0.7329 | 3.4921 | -4.81% | -7.50% | -5.65% | SELL_SETUP_4 / SELL_SETUP_9 / SELL_SETUP_9 | 62.01 / 81.82 / 88.76 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 191.75 | 218.11 | Tech +0.6788 / Macro +0.9021 x 0.80 - 0.00 = +0.2712 | L217, L317, L417, L517, L617, L717 |
| JNJ | 268.04 | 2026-08-28 | `DELAYED` | 284.12 | 2026-09-25 | +6.00% | 6.17% | `REALIZED_VOL_30D` | 0.9224 | 1.2769 | 1.1181 | 3.9440 | -4.18% | -6.70% | -7.57% | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_9 | 57.07 / 65.56 / 77.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 266.93 | 301.31 | Tech +0.8606 / Macro +0.5046 x 0.80 - 0.00 = +0.2671 | L218, L318, L418, L518, L618, L718 |
| VRTX | 541.69 | 2026-08-28 | `DELAYED` | 574.19 | 2026-09-25 | +6.00% | 8.51% | `REALIZED_VOL_30D` | 0.6684 | 1.8993 | 0.6568 | 2.0710 | -8.04% | -11.53% | -11.12% | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_2 | 61.43 / 66.90 / 62.80 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 526.25 | 622.14 | Tech +0.9337 / Macro +0.3325 x 0.80 - 0.00 = +0.2640 | L219, L319, L419, L519, L619, L719 |
| NEM | 127.98 | 2026-08-28 | `DELAYED` | 135.66 | 2026-09-25 | +6.00% | 13.87% | `REALIZED_VOL_30D` | 0.4102 | 1.0386 | 0.1853 | 0.7801 | -16.88% | -22.56% | -17.74% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_1 | 64.49 / 62.92 / 69.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 117.20 | 154.11 | Tech +1.0623 / Macro +0.0597 x 0.80 - 0.00 = +0.2621 | L220, L320, L420, L520, L620, L720 |
| AMP | 559.32 | 2026-08-28 | `DELAYED` | 592.88 | 2026-09-25 | +6.00% | 4.73% | `REALIZED_VOL_30D` | 1.2031 | 1.9299 | 0.8215 | 6.7102 | -1.80% | -3.74% | -5.34% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 58.51 / 68.87 / 62.22 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 565.38 | 620.38 | Tech +0.4834 / Macro +1.1997 x 0.80 - 0.00 = +0.2600 | L221, L321, L421, L521, L621, L721 |
| NOW | 144.71 | 2026-08-28 | `DELAYED` | 153.39 | 2026-09-25 | +6.00% | 18.12% | `REALIZED_VOL_30D` | 0.3139 | 0.6413 | 0.2846 | 0.4567 | -23.90% | -31.33% | -25.00% | SELL_SETUP_2 / SELL_SETUP_8 / SELL_SETUP_2 | 72.72 / 63.55 / 50.24 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 126.12 | 180.67 | Tech +1.0828 / Macro +0.0001 x 0.80 - 0.00 = +0.2599 | L222, L322, L422, L522, L622, L722 |
| ICE | 162.33 | 2026-08-28 | `DELAYED` | 172.07 | 2026-09-25 | +6.00% | 5.78% | `REALIZED_VOL_30D` | 0.9843 | 1.4979 | 0.8127 | 4.4914 | -3.54% | -5.90% | -13.16% | BUY_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_1 | 72.12 / 59.63 / 53.81 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 162.31 | 181.83 | Tech +0.6125 / Macro +0.9186 x 0.80 - 0.00 = +0.2572 | L223, L323, L423, L523, L623, L723 |

## Excluded names — why

| Exclusion | Count | Rationale |
|---|---|---|
| Below the 60th-percentile rank floor | 306 | `rules.md § mu Calibration Table` — names under the 60th percentile are not ranked in either sleeve and appear only in the rejection log |
| Scored at or above the 60th pctl but below the published cut | 180 | settleable in principle, but outside the 24 names this run publishes (cut at pctl 95.48) |
| Filtered out of the universe | 5 | see `04 § Rejection log` — corporate actions, listing age, incomplete indicator pack |
| Every published name | 24 | **monitoring only** — zero pass the investable evidence thresholds |

## Failure rule

`agents.md § Portfolio Construction Agent § Failure Rule`: constraints cannot be met without dropping
below the minimum investable count of 5 — in fact the investable count is **0** — so the agent
recommends **`NO_TRADE`** and forces no portfolio. The single revision pass permitted by
`rules.md § Intra-Loop Revision Limit` was **not** consumed: Task 0 established the position before any
sizing, exactly as that task exists to do.

