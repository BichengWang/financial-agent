# 07 — Portfolio Proposal · 2026-08-22

**Result: `NO_TRADE`. No weights were drafted and the intra-loop revision budget was not spent.**

Portfolio construction terminated at **Task 0**, the constraint-feasibility pre-check that
`agents.md § Portfolio Construction` requires *before* any sizing (Track B, 2026-06-10). Two hard
caps are infeasible for this investable pool under any weighting, so drafting weights would have
been wasted work.

## Task 0 — constraint feasibility pre-check

All inputs below are already-fetched values from `01` (L002, L003, L009, L016-series); nothing was
re-fetched for this stage.

### Beta band — **INFEASIBLE**

`rules.md § Risk Controls` fixes the portfolio beta band at **0.90–1.10** and the single-name cap at
**5%**. A 5% cap implies at least **20 positions**, so the highest sleeve beta any weighting can
reach is the mean of the 20 largest betas in the pool.

| Quantity | Value | Constraint | Result |
|---|---|---|---|
| Max attainable sleeve beta | **0.4841** | ≥ 0.90 floor | **FAIL** |
| Min attainable sleeve beta | 0.1226 | ≤ 1.10 ceiling | pass |
| Positions implied by the 5% cap | 20 | — | — |
| Highest single-name beta in the pool | 2.3576 (`FCX`) | — | — |
| Lowest single-name beta in the pool | -0.3849 (`ABT`) | — | — |
| Mean beta of the published sleeve | 0.3529 | — | — |

The gap is not marginal: the best attainable beta is **0.4159 below the
floor**. Every name in the pool is defensive by construction, and no reweighting of defensives
produces a market-beta sleeve.

This is the first run since 2026-07-27 to be beta-infeasible. The four runs between (2026-07-29,
07-30, 08-01, 08-03) were all feasible, so feasibility was **recomputed this run rather than
inherited from the 07-27 narrative**.

### Sector concentration — **INFEASIBLE at equal weight**

| Sector | Weight in the naive top-20 EW sleeve | Cap | Result |
|---|---|---|---|
| Health Care | 45.0% | 30% | **FAIL** |
| Finance | 20.0% | 30% | pass |
| Basic Materials | 15.0% | 30% | pass |
| Industrials | 15.0% | 30% | pass |
| Consumer Discretionary | 5.0% | 30% | pass |

Health Care reaches **45.0%**, well past the 30% cap. Respecting the cap
would force dropping roughly half the Health Care names, which would in turn push the sleeve below
the 20 positions the 5% cap requires — the two constraints bind against each other.

### Constraints that *do* pass

| Constraint | Value | Cap | Result |
|---|---|---|---|
| Average pairwise correlation | 0.1045 | < 0.45 | **PASS** |
| 95th-pctl 1-month drawdown (naive top-20 EW) | 7.32% | ≤ 8% | **PASS** |
| Portfolio sigma (1m, naive top-20 EW) | 4.44% | — | — |
| Tracking error (1m, naive top-20 EW) | 4.04% | — | — |

Worth stating plainly: the sleeve is disqualified for being **too defensive and too concentrated**,
not for being too risky. Its correlation (0.1045) and drawdown
(7.32%) are comfortably inside their caps.

### Hypothetical analytics of the naive top-20 equal-weight sleeve

Reported as **diagnostics only** — this sleeve is not proposed, not sized, and not executable.

| Metric | Value | Formula / lineage |
|---|---|---|
| Expected 1m return (mu) | +6.00% | equal-weighted mean of per-name calibration-table mu |
| Portfolio beta | 0.4598 | equal-weighted mean of 60d betas (L016) |
| Portfolio sigma (1m) | 4.44% | pstdev of the EW portfolio daily return series x sqrt(21); input L002 |
| Tracking error (1m) | 4.04% | pstdev of beta-adjusted residuals vs SPY x sqrt(21); inputs L002, L003 |
| Information Ratio | 1.2582 | (mu − beta x SPY_mu) / tracking error; inputs L022, L016 |
| Sharpe | 1.2822 | (mu − rf_1m) / portfolio sigma; input L008a |
| 95th-pctl 1m drawdown | 7.32% | 1.65 x portfolio sigma (normality assumed); L016b |

The IR of 1.2582 looks attractive and is exactly the number **not** to act on:
it is computed from a `mu` prior that the settled record says is too aggressive (mean z
-0.5506, hit rate 39.38%), and from a beta so far below 1.0 that the
residual-return term flatters itself.

## Per-position recommendation metrics (top 20, inherited from `05`)

Values are inherited, not recomputed; no new facts.

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BDX | 192.00 | 2026-08-21 | `DELAYED` | 203.52 | 2026-09-19 | +6.00% | 8.16% | `REALIZED_VOL_30D` | 0.6972 | 1.6714 | 0.7328 | 2.2520 | -7.47% | -10.81% | -7.45% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 78.5/72.7/61.5 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 187.22 | 219.82 | 0.30x+1.4253 + 0.15x+0.3983 x0.80 − 0.00 = +0.3899 | L200, L300, L400 |
| SCHW | 112.30 | 2026-08-21 | `DELAYED` | 119.04 | 2026-09-19 | +6.00% | 5.18% | `REALIZED_VOL_30D` | 1.0989 | 1.8621 | 0.9502 | 5.5944 | -2.54% | -4.67% | -5.36% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 71.1/73.1/68.8 | `BULLISH_CROSS`/`ABOVE_SIGNAL`/`BULLISH_CROSS` | 112.99 | 125.09 | 0.30x+1.1643 + 0.15x+0.7995 x0.80 − 0.00 = +0.3754 | L201, L301, L401 |
| AMP | 555.59 | 2026-08-21 | `DELAYED` | 588.93 | 2026-09-19 | +6.00% | 5.17% | `REALIZED_VOL_30D` | 1.1001 | 1.9456 | 0.8062 | 5.6069 | -2.53% | -4.65% | -5.34% | BUY_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 57.9/68.2/61.9 | `BELOW_SIGNAL`/`ABOVE_SIGNAL`/`BELOW_SIGNAL` | 559.04 | 618.81 | 0.30x+0.9245 + 0.15x+1.1369 x0.80 − 0.00 = +0.3583 | L202, L302, L402 |
| CRL | 295.19 | 2026-08-21 | `DELAYED` | 312.90 | 2026-09-19 | +6.00% | 13.48% | `REALIZED_VOL_30D` | 0.4222 | 1.5930 | 0.3524 | 0.8257 | -16.24% | -21.77% | -6.38% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_3 | 76.3/77.1/66.9 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 271.52 | 354.28 | 0.30x+1.3093 + 0.15x+0.3603 x0.80 − 0.00 = +0.3575 | L203, L303, L403 |
| REGN | 834.04 | 2026-08-21 | `DELAYED` | 884.08 | 2026-09-19 | +6.00% | 8.66% | `REALIZED_VOL_30D` | 0.6574 | 1.2377 | 0.6483 | 2.0023 | -8.28% | -11.83% | -5.32% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_1 | 76.5/68.3/57.1 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 809.01 | 959.16 | 0.30x+1.1561 + 0.15x+0.5710 x0.80 − 0.00 = +0.3460 | L204, L304, L404 |
| FCX | 76.66 | 2026-08-21 | `DELAYED` | 81.26 | 2026-09-19 | +6.00% | 14.48% | `REALIZED_VOL_30D` | 0.3929 | 1.2251 | 0.1059 | 0.7151 | -17.90% | -23.84% | -19.83% | SELL_SETUP_3/SELL_SETUP_5/SELL_SETUP_2 | 69.3/64.8/69.9 | `ABOVE_SIGNAL`/`BULLISH_CROSS`/`ABOVE_SIGNAL` | 69.71 | 92.81 | 0.30x+1.2952 + 0.15x+0.2598 x0.80 − 0.00 = +0.3420 | L205, L305, L405 |
| RVTY | 124.75 | 2026-08-21 | `DELAYED` | 132.24 | 2026-09-19 | +6.00% | 9.66% | `REALIZED_VOL_30D` | 0.5889 | 1.1825 | 0.4694 | 1.6070 | -9.94% | -13.90% | -6.44% | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_3 | 68.6/68.9/58.4 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 119.70 | 144.77 | 0.30x+1.3185 + 0.15x+0.2107 x0.80 − 0.00 = +0.3417 | L206, L306, L406 |
| TGT | 165.44 | 2026-08-21 | `DELAYED` | 175.37 | 2026-09-19 | +6.00% | 8.02% | `REALIZED_VOL_30D` | 0.7094 | 1.7787 | 0.6301 | 2.3313 | -7.24% | -10.52% | -10.69% | SELL_SETUP_3/SELL_SETUP_4/SELL_SETUP_9 | 76.5/75.4/70.3 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 161.57 | 189.17 | 0.30x+1.4029 + 0.15x+0.0173 x0.80 − 0.00 = +0.3388 | L207, L307, L407 |
| NEM | 131.58 | 2026-08-21 | `DELAYED` | 139.47 | 2026-09-19 | +6.00% | 14.24% | `REALIZED_VOL_30D` | 0.3996 | 0.9329 | 0.1903 | 0.7398 | -17.49% | -23.33% | -18.77% | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 75.9/65.6/70.7 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 119.99 | 158.96 | 0.30x+1.2021 + 0.15x+0.3731 x0.80 − 0.00 = +0.3333 | L208, L308, L408 |
| TECH | 72.32 | 2026-08-21 | `DELAYED` | 76.66 | 2026-09-19 | +6.00% | 1.25% | `REALIZED_VOL_30D` | 4.5572 | 7.5696 | 0.3270 | 96.2184 | +3.94% | +3.43% | -4.02% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 67.7/65.7/55.4 | `BELOW_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 75.72 | 77.60 | 0.30x+0.8182 + 0.15x+1.0844 x0.80 − 0.00 = +0.3265 | L209, L309, L409 |
| LH | 336.34 | 2026-08-21 | `DELAYED` | 356.52 | 2026-09-19 | +6.00% | 7.25% | `REALIZED_VOL_30D` | 0.7849 | 1.7776 | 0.8846 | 2.8543 | -5.96% | -8.93% | -6.20% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 75.7/74.1/68.5 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 331.16 | 381.88 | 0.30x+1.1779 + 0.15x+0.2590 x0.80 − 0.00 = +0.3138 | L210, L310, L410 |
| MRK | 152.55 | 2026-08-21 | `DELAYED` | 161.70 | 2026-09-19 | +6.00% | 12.06% | `REALIZED_VOL_30D` | 0.4718 | 1.3412 | 0.6078 | 1.0314 | -13.90% | -18.84% | -6.78% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_9 | 77.9/75.1/75.2 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 142.57 | 180.84 | 0.30x+1.4270 + 0.15x-0.2595 x0.80 − 0.00 = +0.3113 | L211, L311, L411 |
| RJF | 175.20 | 2026-08-21 | `DELAYED` | 185.71 | 2026-09-19 | +6.00% | 5.57% | `REALIZED_VOL_30D` | 1.0209 | 1.5559 | 0.8299 | 4.8286 | -3.20% | -5.48% | -6.10% | BUY_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 51.5/62.5/61.2 | `BELOW_SIGNAL`/`ABOVE_SIGNAL`/`BELOW_SIGNAL` | 175.56 | 195.87 | 0.30x+0.7866 + 0.15x+0.9553 x0.80 − 0.00 = +0.3034 | L212, L312, L412 |
| DE | 647.47 | 2026-08-21 | `DELAYED` | 686.32 | 2026-09-19 | +6.00% | 10.16% | `REALIZED_VOL_30D` | 0.5603 | 1.1853 | 0.4787 | 1.4543 | -10.76% | -14.92% | -9.25% | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_8 | 62.4/61.4/64.4 | `BULLISH_CROSS`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 617.93 | 754.71 | 0.30x+1.1842 + 0.15x+0.0866 x0.80 − 0.00 = +0.2946 | L213, L313, L413 |
| NDSN | 332.24 | 2026-08-21 | `DELAYED` | 352.17 | 2026-09-19 | +6.00% | 8.23% | `REALIZED_VOL_30D` | 0.6917 | 1.6281 | 0.6117 | 2.2166 | -7.57% | -10.95% | -6.81% | SELL_SETUP_2/SELL_SETUP_4/SELL_SETUP_9 | 72.5/74.5/70.5 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 323.75 | 380.60 | 0.30x+1.2104 + 0.15x+0.0310 x0.80 − 0.00 = +0.2942 | L214, L314, L414 |
| AMGN | 439.33 | 2026-08-21 | `DELAYED` | 465.69 | 2026-09-19 | +6.00% | 8.26% | `REALIZED_VOL_30D` | 0.6888 | 2.3406 | 0.7172 | 2.1981 | -7.63% | -11.02% | -5.05% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 74.2/75.5/72.0 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 427.95 | 503.43 | 0.30x+1.0351 + 0.15x+0.2903 x0.80 − 0.00 = +0.2833 | L215, L315, L415 |
| DXCM | 92.34 | 2026-08-21 | `DELAYED` | 97.88 | 2026-09-19 | +6.00% | 14.86% | `REALIZED_VOL_30D` | 0.3829 | 0.9216 | 0.3965 | 0.6791 | -18.52% | -24.61% | -13.86% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_2 | 70.0/71.4/55.4 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 83.61 | 112.15 | 0.30x+0.9044 + 0.15x+0.5430 x0.80 − 0.00 = +0.2822 | L216, L316, L416 |
| SYF | 79.47 | 2026-08-21 | `DELAYED` | 84.24 | 2026-09-19 | +6.00% | 7.76% | `REALIZED_VOL_30D` | 0.7332 | 1.2076 | 0.4128 | 2.4907 | -6.80% | -9.99% | -13.22% | BUY_SETUP_3/SELL_SETUP_3/SELL_SETUP_3 | 56.3/58.7/62.9 | `BELOW_SIGNAL`/`ABOVE_SIGNAL`/`BELOW_SIGNAL` | 77.82 | 90.65 | 0.30x+0.7749 + 0.15x+0.7762 x0.80 − 0.00 = +0.2791 | L217, L317, L417 |
| APD | 305.10 | 2026-08-21 | `DELAYED` | 323.41 | 2026-09-19 | +6.00% | 5.46% | `REALIZED_VOL_30D` | 1.0430 | 1.6201 | 0.7048 | 5.0396 | -3.00% | -5.24% | -6.88% | SELL_SETUP_1/SELL_SETUP_3/SELL_SETUP_8 | 55.8/58.6/57.5 | `BELOW_SIGNAL`/`ABOVE_SIGNAL`/`ABOVE_SIGNAL` | 306.09 | 340.72 | 0.30x+0.6149 + 0.15x+1.0807 x0.80 − 0.00 = +0.2773 | L218, L318, L418 |
| ABT | 116.64 | 2026-08-21 | `DELAYED` | 123.64 | 2026-09-19 | +6.00% | 10.78% | `REALIZED_VOL_30D` | 0.5279 | 1.1475 | 0.7242 | 1.2911 | -11.79% | -16.20% | -7.18% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_2 | 77.9/67.9/53.0 | `ABOVE_SIGNAL`/`ABOVE_SIGNAL`/`BELOW_SIGNAL` | 110.56 | 136.71 | 0.30x+1.1161 + 0.15x+0.0139 x0.80 − 0.00 = +0.2695 | L219, L319, L419 |

## Correlation matrix (first 12 published names, 60d daily adjusted returns)

Full 24x24 matrix is in the working manifest; the average over all
276 pairs is **0.1045**.

|  | BDX | SCHW | AMP | CRL | REGN | FCX | RVTY | TGT | NEM | TECH | LH | MRK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BDX | +1.000 | -0.018 | +0.154 | +0.367 | +0.468 | -0.170 | +0.435 | +0.457 | +0.070 | +0.308 | +0.487 | +0.519 |
| SCHW | -0.018 | +1.000 | +0.665 | -0.112 | +0.048 | -0.152 | -0.310 | -0.087 | -0.007 | -0.330 | +0.053 | -0.076 |
| AMP | +0.154 | +0.665 | +1.000 | -0.088 | +0.184 | +0.029 | -0.098 | -0.083 | +0.081 | -0.207 | +0.026 | -0.019 |
| CRL | +0.367 | -0.112 | -0.088 | +1.000 | +0.126 | +0.117 | +0.619 | +0.062 | +0.221 | +0.429 | +0.471 | +0.228 |
| REGN | +0.468 | +0.048 | +0.184 | +0.126 | +1.000 | -0.002 | +0.122 | +0.255 | +0.168 | -0.009 | +0.407 | +0.455 |
| FCX | -0.170 | -0.152 | +0.029 | +0.117 | -0.002 | +1.000 | +0.219 | -0.041 | +0.760 | +0.065 | -0.052 | +0.002 |
| RVTY | +0.435 | -0.310 | -0.098 | +0.619 | +0.122 | +0.219 | +1.000 | +0.250 | +0.341 | +0.603 | +0.258 | +0.326 |
| TGT | +0.457 | -0.087 | -0.083 | +0.062 | +0.255 | -0.041 | +0.250 | +1.000 | +0.025 | +0.085 | +0.076 | +0.262 |
| NEM | +0.070 | -0.007 | +0.081 | +0.221 | +0.168 | +0.760 | +0.341 | +0.025 | +1.000 | +0.132 | -0.003 | +0.169 |
| TECH | +0.308 | -0.330 | -0.207 | +0.429 | -0.009 | +0.065 | +0.603 | +0.085 | +0.132 | +1.000 | +0.087 | +0.176 |
| LH | +0.487 | +0.053 | +0.026 | +0.471 | +0.407 | -0.052 | +0.258 | +0.076 | -0.003 | +0.087 | +1.000 | +0.378 |
| MRK | +0.519 | -0.076 | -0.019 | +0.228 | +0.455 | +0.002 | +0.326 | +0.262 | +0.169 | +0.176 | +0.378 | +1.000 |

## Excluded names

No name was excluded at this stage: portfolio construction never reached position selection. The
485 scored names outside the published 24 were excluded at
factor scoring on percentile rank, and the 6 names rejected before scoring are
itemised with reasons in `04`.
