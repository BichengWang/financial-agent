# 07 — Portfolio Proposal · 2026-09-03

**Recommendation: `NO_TRADE`. No weights are proposed.** Task 0 of
`agents.md § Portfolio Construction` requires a constraint-feasibility pre-check before any
sizing; that check runs below and passes, but the investable set handed over by `05`/`06` is
**empty**, so there is nothing to size. The analytics on this page describe a *naive top-20
equal-weighted sleeve* built solely to quantify what a portfolio out of this leaderboard would
look like — it is a diagnostic, never a recommendation.

## Task 0 — constraint feasibility pre-check

| Constraint | Attainable range / value | Cap | Feasible? | Ledger |
|---|---|---|---|---|
| Sleeve beta to SPY | -0.6671 to +1.4337 | 0.90 - 1.10 | **yes** | L016 |
| Single-name weight | 5.00% at the cap => >= 20 names | 5% | yes | rules.md § Risk Controls |
| Sector concentration (pool) | Finance 31, Health Care 25, Technology 14, Consumer Discretionary 8 | 30% of the sleeve | yes — the >= 80th-pctl pool is deep enough in several sectors | L009 |

The beta band is **feasible** this run: with 102 names at or above the 80th
percentile, the 20 highest betas average +1.4337, above the 0.90
floor. That is the opposite finding from the two prior claude-opus-5 runs — 2026-08-22 (max
attainable +0.4841) and 2026-08-27 (+0.2919) — where the band was provably unreachable.
**Feasibility is recomputed every run and neither narrative may be reused.**
39.17% of the 508 scored names still
carry a negative 60-day beta, which is why the naive rank-ordered sleeve below fails the band even
though a differently-selected sleeve could clear it.

## Naive top-20 equal-weighted sleeve — diagnostic only

Weights are `1/20 = 5.00%` each, the maximum allowed single-name weight, applied to the 20
highest-ranked published names. **This is not a proposal.**

| Portfolio metric | Value | Cap | Result | Ledger |
|---|---|---|---|---|
| Expected 1-month return (equal-weighted mu) | +6.00% | n/a | n/a | 05 |
| Portfolio sigma (1 month) | 3.52% | n/a | n/a | L016b |
| Expected Sharpe | +1.6140 | n/a | n/a | DERIVED |
| Portfolio beta to SPY | +0.1187 | 0.90 - 1.10 | **FAIL** | L016c |
| Tracking error (1 month) | 3.50% | n/a | n/a | DERIVED |
| Information Ratio | +1.6485 | n/a | n/a | DERIVED |
| Average pairwise correlation | 0.1227 | < 0.45 | PASS | L016a |
| Max pairwise correlation | 0.8925 | n/a | n/a | L016a |
| 95th-pctl 1-month drawdown | 5.81% | <= 8% | PASS | L016b |
| VaR95 (portfolio, parametric) | +0.19% | n/a | n/a | DERIVED |
| CVaR95 (portfolio, parametric) | -1.26% | n/a | n/a | DERIVED |
| Max sector share | 40.00% | <= 30% | **FAIL** | L009 |

Normality is assumed for the parametric 95th-percentile drawdown, VaR95 and CVaR95
(`1.65 x sigma`, `2.06 x sigma`); this is stated rather than hidden because the fetched 60-day
window is the empirical alternative and is short.

Two independent caps fail on this naive construction: **portfolio beta
+0.1187**, far below the 0.90 floor, and **Finance at
40.00%** against the 30% cap. Correlation
(0.1227) and drawdown
(5.81%) both pass comfortably — the sleeve is disqualified for being too
**defensive and sector-concentrated**, not too risky. Each of these is an independent `NO_TRADE`
trigger (`rules.md § Downgrade to NO_TRADE` #5, #6) on top of the evidence-threshold failure that
already emptied the investable set.

## Sector concentration (naive sleeve)

| Sector | Names | Weight | Cap | Result |
|---|---|---|---|---|
| Finance | 8 | 40.00% | 30% | **FAIL** |
| Health Care | 6 | 30.00% | 30% | PASS |
| Energy | 3 | 15.00% | 30% | PASS |
| Industrials | 2 | 10.00% | 30% | PASS |
| Technology | 1 | 5.00% | 30% | PASS |

## Factor exposure summary

| Family | Weight in composite | Share of live conviction | Status |
|---|---|---|---|
| Fundamental | 0.30 | 0.0% | `UNAVAILABLE` (L021) |
| Technical / Price | 0.30 | 66.7% | live — 6 equal-weighted slots |
| Sentiment / Positioning | 0.25 | 0.0% | `UNAVAILABLE` (L022) |
| Macro / Regime | 0.15 | 33.3% | live — 4 equal-weighted slots |

**Factor crowding flag: RAISED.** More than half the sleeve's conviction loads on a single factor
family (Technical, 66.7%), which `rules.md § Risk Controls` requires be flagged.

## Correlation matrix (60d daily adjusted returns, naive top-20)

| _ | VLO | SPGI | PFG | GILD | AMP | IQV | RVTY | TECH | PSX | STT | GEN | ICE | BNY | DE | JNJ | VRTX | MPC | WFC | ELV | RJF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VLO | 1.00 | 0.09 | 0.10 | -0.09 | -0.05 | -0.14 | -0.15 | 0.11 | 0.88 | 0.06 | -0.05 | -0.03 | -0.06 | -0.04 | 0.10 | -0.05 | 0.89 | 0.09 | 0.20 | -0.07 |
| SPGI | 0.09 | 1.00 | 0.38 | 0.24 | 0.51 | 0.17 | -0.07 | -0.12 | 0.11 | 0.04 | 0.58 | 0.58 | -0.01 | -0.09 | 0.19 | 0.19 | 0.13 | 0.26 | 0.21 | 0.44 |
| PFG | 0.10 | 0.38 | 1.00 | 0.14 | 0.54 | 0.08 | -0.26 | -0.24 | 0.04 | 0.35 | 0.33 | 0.44 | 0.22 | -0.11 | 0.21 | 0.10 | 0.05 | 0.24 | 0.20 | 0.55 |
| GILD | -0.09 | 0.24 | 0.14 | 1.00 | 0.09 | 0.25 | -0.07 | -0.05 | 0.00 | 0.05 | 0.17 | 0.30 | 0.09 | -0.09 | 0.42 | 0.47 | -0.00 | 0.03 | 0.07 | 0.13 |
| AMP | -0.05 | 0.51 | 0.54 | 0.09 | 1.00 | 0.14 | -0.09 | -0.23 | -0.04 | 0.45 | 0.33 | 0.41 | 0.45 | -0.01 | -0.04 | 0.17 | -0.03 | 0.59 | 0.22 | 0.85 |
| IQV | -0.14 | 0.17 | 0.08 | 0.25 | 0.14 | 1.00 | 0.51 | 0.08 | -0.07 | -0.23 | 0.44 | 0.30 | -0.20 | 0.09 | 0.26 | 0.34 | -0.15 | 0.02 | 0.17 | 0.17 |
| RVTY | -0.15 | -0.07 | -0.26 | -0.07 | -0.09 | 0.51 | 1.00 | 0.54 | -0.18 | -0.19 | 0.12 | -0.15 | -0.08 | 0.21 | -0.06 | 0.18 | -0.20 | 0.05 | 0.10 | -0.19 |
| TECH | 0.11 | -0.12 | -0.24 | -0.05 | -0.23 | 0.08 | 0.54 | 1.00 | -0.03 | -0.12 | 0.02 | -0.29 | -0.02 | 0.27 | 0.01 | 0.04 | -0.00 | -0.02 | 0.01 | -0.31 |
| PSX | 0.88 | 0.11 | 0.04 | 0.00 | -0.04 | -0.07 | -0.18 | -0.03 | 1.00 | -0.01 | -0.04 | 0.11 | -0.09 | -0.12 | 0.18 | -0.02 | 0.89 | 0.06 | 0.23 | -0.02 |
| STT | 0.06 | 0.04 | 0.35 | 0.05 | 0.45 | -0.23 | -0.19 | -0.12 | -0.01 | 1.00 | -0.09 | 0.10 | 0.85 | 0.06 | -0.07 | 0.08 | 0.04 | 0.49 | 0.10 | 0.52 |
| GEN | -0.05 | 0.58 | 0.33 | 0.17 | 0.33 | 0.44 | 0.12 | 0.02 | -0.04 | -0.09 | 1.00 | 0.40 | -0.18 | 0.02 | 0.15 | 0.13 | -0.05 | 0.06 | 0.21 | 0.33 |
| ICE | -0.03 | 0.58 | 0.44 | 0.30 | 0.41 | 0.30 | -0.15 | -0.29 | 0.11 | 0.10 | 0.40 | 1.00 | 0.07 | -0.14 | 0.12 | 0.01 | 0.02 | -0.00 | 0.13 | 0.47 |
| BNY | -0.06 | -0.01 | 0.22 | 0.09 | 0.45 | -0.20 | -0.08 | -0.02 | -0.09 | 0.85 | -0.18 | 0.07 | 1.00 | 0.08 | -0.09 | 0.10 | -0.00 | 0.52 | 0.03 | 0.48 |
| DE | -0.04 | -0.09 | -0.11 | -0.09 | -0.01 | 0.09 | 0.21 | 0.27 | -0.12 | 0.06 | 0.02 | -0.14 | 0.08 | 1.00 | -0.08 | 0.06 | -0.06 | 0.15 | -0.08 | -0.07 |
| JNJ | 0.10 | 0.19 | 0.21 | 0.42 | -0.04 | 0.26 | -0.06 | 0.01 | 0.18 | -0.07 | 0.15 | 0.12 | -0.09 | -0.08 | 1.00 | 0.44 | 0.08 | 0.04 | 0.26 | 0.04 |
| VRTX | -0.05 | 0.19 | 0.10 | 0.47 | 0.17 | 0.34 | 0.18 | 0.04 | -0.02 | 0.08 | 0.13 | 0.01 | 0.10 | 0.06 | 0.44 | 1.00 | -0.01 | 0.12 | 0.07 | 0.19 |
| MPC | 0.89 | 0.13 | 0.05 | -0.00 | -0.03 | -0.15 | -0.20 | -0.00 | 0.89 | 0.04 | -0.05 | 0.02 | -0.00 | -0.06 | 0.08 | -0.01 | 1.00 | 0.12 | 0.13 | -0.02 |
| WFC | 0.09 | 0.26 | 0.24 | 0.03 | 0.59 | 0.02 | 0.05 | -0.02 | 0.06 | 0.49 | 0.06 | -0.00 | 0.52 | 0.15 | 0.04 | 0.12 | 0.12 | 1.00 | 0.19 | 0.55 |
| ELV | 0.20 | 0.21 | 0.20 | 0.07 | 0.22 | 0.17 | 0.10 | 0.01 | 0.23 | 0.10 | 0.21 | 0.13 | 0.03 | -0.08 | 0.26 | 0.07 | 0.13 | 0.19 | 1.00 | 0.24 |
| RJF | -0.07 | 0.44 | 0.55 | 0.13 | 0.85 | 0.17 | -0.19 | -0.31 | -0.02 | 0.52 | 0.33 | 0.47 | 0.48 | -0.07 | 0.04 | 0.19 | -0.02 | 0.55 | 0.24 | 1.00 |

## Per-position Recommendation Metrics (inherited from `05`, no recomputation)

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VLO | 370.69 | 2026-09-03 | `DELAYED` | 392.93 | 2026-10-01 | +6.00% | 8.44% | `REALIZED_VOL_30D` | +0.6742 | +2.2165 | +0.6754 | +2.1080 | -7.92% | -11.38% | -8.65% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 75.26 / 78.49 / 87.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 360.41 | 425.45 | (0.30x`UNAVL` + 0.30x+1.4152 + 0.25x`UNAVL` + 0.15x+0.2756) x 0.80 - 0.00 = +0.3727 | L200, L500 |
| SPGI | 450.58 | 2026-09-03 | `DELAYED` | 477.61 | 2026-10-01 | +6.00% | 7.75% | `REALIZED_VOL_30D` | +0.7338 | +1.5128 | +0.6046 | +2.4969 | -6.79% | -9.97% | -11.40% | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_3 | 63.17 / 57.77 / 52.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 441.29 | 513.93 | (0.30x`UNAVL` + 0.30x+1.0592 + 0.25x`UNAVL` + 0.15x+0.8874) x 0.80 - 0.00 = +0.3607 | L201, L501 |
| PFG | 118.51 | 2026-09-03 | `DELAYED` | 125.62 | 2026-10-01 | +6.00% | 7.54% | `REALIZED_VOL_30D` | +0.7541 | +2.8105 | +0.7718 | +2.6369 | -6.44% | -9.54% | -6.16% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_9 | 68.60 / 70.87 / 74.48 | `BULLISH_CROSS` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | 116.32 | 134.92 | (0.30x`UNAVL` + 0.30x+1.2136 + 0.25x`UNAVL` + 0.15x+0.5348) x 0.80 - 0.00 = +0.3554 | L202, L502 |
| GILD | 151.19 | 2026-09-03 | `DELAYED` | 160.26 | 2026-10-01 | +6.00% | 7.45% | `REALIZED_VOL_30D` | +0.7631 | +1.4078 | +0.6767 | +2.7005 | -6.30% | -9.35% | -5.17% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 68.29 / 68.28 / 71.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 148.54 | 171.98 | (0.30x`UNAVL` + 0.30x+1.1288 + 0.25x`UNAVL` + 0.15x+0.5676) x 0.80 - 0.00 = +0.3390 | L203, L503 |
| AMP | 565.08 | 2026-09-03 | `DELAYED` | 598.98 | 2026-10-01 | +6.00% | 5.43% | `REALIZED_VOL_30D` | +1.0475 | +1.8228 | +0.7892 | +5.0880 | -2.96% | -5.19% | -5.34% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.50 / 69.99 / 62.87 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 567.08 | 630.89 | (0.30x`UNAVL` + 0.30x+0.8574 + 0.25x`UNAVL` + 0.15x+1.0804) x 0.80 - 0.00 = +0.3354 | L204, L504 |
| IQV | 271.62 | 2026-09-03 | `DELAYED` | 287.92 | 2026-10-01 | +6.00% | 13.80% | `REALIZED_VOL_30D` | +0.4121 | +1.1924 | +0.5338 | +0.7874 | -16.77% | -22.43% | -9.92% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_4 | 75.17 / 75.13 / 63.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 248.93 | 326.91 | (0.30x`UNAVL` + 0.30x+1.4310 + 0.25x`UNAVL` + 0.15x-0.0713) x 0.80 - 0.00 = +0.3349 | L205, L505 |
| RVTY | 130.63 | 2026-09-03 | `DELAYED` | 138.47 | 2026-10-01 | +6.00% | 9.28% | `REALIZED_VOL_30D` | +0.6126 | +1.3308 | +0.5309 | +1.7404 | -9.32% | -13.12% | -6.38% | SELL_SETUP_9 / SELL_SETUP_5 / SELL_SETUP_4 | 68.62 / 72.12 / 60.61 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 125.86 | 151.08 | (0.30x`UNAVL` + 0.30x+1.3888 + 0.25x`UNAVL` + 0.15x-0.0035) x 0.80 - 0.00 = +0.3329 | L206, L506 |
| TECH | 72.45 | 2026-09-03 | `DELAYED` | 76.80 | 2026-10-01 | +6.00% | 0.99% | `REALIZED_VOL_30D` | +5.7278 | +15.4694 | +0.3635 | +152.1345 | +4.36% | +3.95% | -4.02% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 66.10 / 65.94 / 55.46 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 76.05 | 77.55 | (0.30x`UNAVL` + 0.30x+0.7951 + 0.25x`UNAVL` + 0.15x+1.0699) x 0.80 - 0.00 = +0.3192 | L207, L507 |
| PSX | 254.66 | 2026-09-03 | `DELAYED` | 269.94 | 2026-10-01 | +6.00% | 8.27% | `REALIZED_VOL_30D` | +0.6876 | +1.6811 | +0.8271 | +2.1924 | -7.65% | -11.04% | -8.57% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 74.81 / 78.77 / 81.33 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 248.03 | 291.85 | (0.30x`UNAVL` + 0.30x+1.3457 + 0.25x`UNAVL` + 0.15x-0.0329) x 0.80 - 0.00 = +0.3190 | L208, L508 |
| STT | 193.94 | 2026-09-03 | `DELAYED` | 205.58 | 2026-10-01 | +6.00% | 7.01% | `REALIZED_VOL_30D` | +0.8115 | +1.1424 | +0.7057 | +3.0534 | -5.56% | -8.44% | -5.65% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.03 / 82.05 / 88.94 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 191.44 | 219.71 | (0.30x`UNAVL` + 0.30x+0.9025 + 0.25x`UNAVL` + 0.15x+0.8260) x 0.80 - 0.00 = +0.3157 | L209, L509 |
| GEN | 31.33 | 2026-09-03 | `DELAYED` | 33.21 | 2026-10-01 | +6.00% | 9.25% | `REALIZED_VOL_30D` | +0.6150 | +0.9782 | +0.5329 | +1.7541 | -9.26% | -13.05% | -7.85% | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_5 | 67.86 / 69.20 / 62.25 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 30.20 | 36.22 | (0.30x`UNAVL` + 0.30x+1.2613 + 0.25x`UNAVL` + 0.15x+0.1009) x 0.80 - 0.00 = +0.3148 | L210, L510 |
| ICE | 164.59 | 2026-09-03 | `DELAYED` | 174.47 | 2026-10-01 | +6.00% | 6.24% | `REALIZED_VOL_30D` | +0.9113 | +1.8546 | +0.7777 | +3.8510 | -4.30% | -6.86% | -13.00% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 68.48 / 61.15 / 54.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 163.78 | 185.15 | (0.30x`UNAVL` + 0.30x+0.8835 + 0.25x`UNAVL` + 0.15x+0.8271) x 0.80 - 0.00 = +0.3113 | L211, L511 |
| BNY | 164.33 | 2026-09-03 | `DELAYED` | 174.19 | 2026-10-01 | +6.00% | 5.32% | `REALIZED_VOL_30D` | +1.0692 | +1.6136 | +0.7909 | +5.3014 | -2.78% | -4.96% | -5.69% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.86 / 77.20 / 91.64 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 165.10 | 183.28 | (0.30x`UNAVL` + 0.30x+0.7190 + 0.25x`UNAVL` + 0.15x+1.0849) x 0.80 - 0.00 = +0.3027 | L212, L512 |
| DE | 694.41 | 2026-09-03 | `DELAYED` | 736.07 | 2026-10-01 | +6.00% | 11.08% | `REALIZED_VOL_30D` | +0.5135 | +1.2207 | +0.5087 | +1.2229 | -12.27% | -16.81% | -9.25% | SELL_SETUP_4 / SELL_SETUP_5 / SELL_SETUP_9 | 68.67 / 65.74 / 67.59 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 656.09 | 816.06 | (0.30x`UNAVL` + 0.30x+1.3196 + 0.25x`UNAVL` + 0.15x-0.1415) x 0.80 - 0.00 = +0.2997 | L213, L513 |
| JNJ | 278.43 | 2026-09-03 | `DELAYED` | 295.14 | 2026-10-01 | +6.00% | 6.07% | `REALIZED_VOL_30D` | +0.9372 | +1.2736 | +1.1075 | +4.0734 | -4.01% | -6.50% | -7.57% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_9 | 65.95 / 69.40 / 79.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 277.56 | 312.71 | (0.30x`UNAVL` + 0.30x+0.9583 + 0.25x`UNAVL` + 0.15x+0.5388) x 0.80 - 0.00 = +0.2946 | L214, L514 |
| VRTX | 557.96 | 2026-09-03 | `DELAYED` | 591.44 | 2026-10-01 | +6.00% | 8.22% | `REALIZED_VOL_30D` | +0.6919 | +1.8707 | +0.6570 | +2.2198 | -7.56% | -10.93% | -11.12% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_3 | 67.51 / 69.51 / 64.46 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 543.74 | 639.14 | (0.30x`UNAVL` + 0.30x+0.9749 + 0.25x`UNAVL` + 0.15x+0.4020) x 0.80 - 0.00 = +0.2822 | L215, L515 |
| MPC | 387.71 | 2026-09-03 | `DELAYED` | 410.97 | 2026-10-01 | +6.00% | 10.42% | `REALIZED_VOL_30D` | +0.5458 | +0.9064 | +0.7050 | +1.3813 | -11.19% | -15.47% | -7.84% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_8 | 77.86 / 79.52 / 86.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 368.95 | 452.99 | (0.30x`UNAVL` + 0.30x+1.2621 + 0.25x`UNAVL` + 0.15x-0.1906) x 0.80 - 0.00 = +0.2800 | L216, L516 |
| WFC | 89.19 | 2026-09-03 | `DELAYED` | 94.54 | 2026-10-01 | +6.00% | 6.13% | `REALIZED_VOL_30D` | +0.9274 | +1.1794 | +0.8075 | +3.9883 | -4.12% | -6.63% | -5.88% | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_4 | 61.84 / 58.56 / 65.31 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 88.85 | 100.23 | (0.30x`UNAVL` + 0.30x+0.7511 + 0.25x`UNAVL` + 0.15x+0.7379) x 0.80 - 0.00 = +0.2688 | L217, L517 |
| ELV | 414.78 | 2026-09-03 | `DELAYED` | 439.67 | 2026-10-01 | +6.00% | 6.68% | `REALIZED_VOL_30D` | +0.8517 | +1.5684 | +0.5512 | +3.3635 | -5.02% | -7.76% | -12.64% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_6 | 62.76 / 61.87 / 55.81 | `ABOVE_SIGNAL` / `BELOW_SIGNAL` / `ABOVE_SIGNAL` | 410.86 | 468.47 | (0.30x`UNAVL` + 0.30x+0.6114 + 0.25x`UNAVL` + 0.15x+1.0062) x 0.80 - 0.00 = +0.2675 | L218, L518 |
| RJF | 181.10 | 2026-09-03 | `DELAYED` | 191.97 | 2026-10-01 | +6.00% | 6.56% | `REALIZED_VOL_30D` | +0.8671 | +1.3379 | +0.7735 | +3.4868 | -4.82% | -7.51% | -6.10% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.09 / 66.38 / 63.10 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 179.61 | 204.32 | (0.30x`UNAVL` + 0.30x+0.7020 + 0.25x`UNAVL` + 0.15x+0.7863) x 0.80 - 0.00 = +0.2628 | L219, L519 |

## Why the remaining published names were excluded from the diagnostic sleeve

Ranks 21-24 were left out only because the diagnostic is defined on the top 20 at the 5%
single-name cap. They are not excluded on quality grounds and they carry full forecast records in
`15_predictions.json` exactly as ranks 1-20 do:
DELL, BIIB, PRU, SCHW.
