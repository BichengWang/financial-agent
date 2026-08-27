# 07 — Portfolio Proposal · 2026-08-27

## Task 0 — Constraint feasibility pre-check (before any sizing)

`agents.md § Portfolio Construction Agent` requires this check *before* weights are drafted, so an
infeasible set costs no revision pass. It is recomputed every run — the 2026-07-27 "provably
infeasible" narrative was wrong on the four runs that followed it, and the 2026-08-22 feasible
narrative would be wrong today.

| Constraint | Cap / band | Best attainable from the published sleeve | Feasible |
|---|---|---|---|
| Portfolio beta to SPY | 0.90 – 1.10 | **+0.2919** (mean of the 20 highest betas in the pool; lowest attainable +0.0090) | **No** |
| Max single-name weight | 5% | forces >= 20 names, which is what makes the beta bound binding | n/a |
| Max sector concentration | 30% | Health Care is 41.67% of the published 24; the 20-name subset needed for the beta test cannot avoid it | **No** |
| Average pairwise correlation | < 0.45 | 0.1416 over 276 pairs | Yes |
| 95th-pctl 1-month drawdown | <= 8% | 6.38% for a naive top-20 equal-weight sleeve | Yes |

**The beta band is genuinely infeasible this run.** The proof is arithmetic, not a judgment: the 5%
single-name cap forces at least 20 positions, so the highest sleeve beta
any weighting can reach is the equal-weighted mean of the 20 highest betas
available in the pool. That value is **+0.2919**, far below the 0.90 floor.
The 24 published betas, sorted: +1.198, +0.846, +0.690, +0.645, +0.502, +0.492, +0.465, +0.444, +0.363, +0.319, +0.150, +0.141, +0.116, +0.104, +0.022, +0.015, +0.014, -0.105, -0.201, -0.384, -0.412, -0.425, -0.699, -0.741.

This is the **second consecutive** infeasible run (2026-08-22 reached +0.4841) after four
consecutive feasible ones. As on 2026-08-22, the sleeve is disqualified for being **too defensive,
not too risky**: correlation 0.1416 and the 95th-percentile drawdown
6.38% both pass comfortably. Sector concentration fails independently.

Per `rules.md § Downgrade to NO_TRADE` #6, an investable set that is structurally infeasible routes to
**`NO_TRADE`**, not `HALTED` — the cause is set composition, not process or data integrity
(`§ Hard Halt Criteria` #5 explicitly draws that line).

**No weights are drafted and no revision pass is spent.** The tables below are the diagnostic
portfolio analytics `rules.md § Computed Risk Analytics` requires from fetched history — they are
*not* a proposal.

## Diagnostic portfolio analytics — naive top-20 equal-weight sleeve

Computed from 60 trading days of fetched adjusted returns (L002, L016–L016c). This sleeve is shown
to quantify the caps, not to recommend it.

| Analytic | Value | Cap | Status | Formula |
|---|---|---|---|---|
| Expected beta | +0.1633 | 0.90 – 1.10 | **FAIL (too low)** | equal-weighted mean of the 20 constituent 60d betas |
| Portfolio sigma (1m) | 3.86% | n/a | — | `sqrt(w' Sigma w)` on the 60d daily covariance matrix, x `sqrt(21)` |
| 95th-pctl 1-month drawdown | 6.38% | <= 8% | PASS | `1.65 x portfolio_sigma_1m`; normality assumed and stated |
| Average pairwise correlation | 0.1416 | < 0.45 | PASS | mean of all 276 pairwise correlations of 60d daily adjusted returns |
| Max sector share | 41.67% (Health Care) | <= 30% | **FAIL** | count share of the published sleeve |
| Expected Sharpe (sleeve) | 0.7210 | n/a | — | mean of constituent forecast Sharpes |
| Expected Sortino (sleeve) | 1.3620 | n/a | — | mean of constituent Sortinos |
| Expected Information Ratio (sleeve) | 0.6820 | n/a | — | mean of constituent IRs |
| Tracking error (mean constituent, 1m) | 8.85% | n/a | — | pstdev(r - beta x r_SPY) over 60 daily intervals x `sqrt(21)` |
| VaR95 (mean constituent, 1m) | -8.27% | n/a | — | `mu - 1.65 x sigma` |
| CVaR95 (mean constituent, 1m) | -11.81% | n/a | — | `mu - 2.06 x sigma` |
| Kelly cap binding | 20 of 20 names have `0.25 x Kelly` >= 5% NAV | 5% single-name | cap binds for those names | `0.25 x mu / sigma^2`, bounded by the 5% NAV cap; no name has `0.25 x Kelly <= 0` |

## Sector concentration table

| Sector | Names in the published sleeve | Share | Against the 30% cap |
|---|---|---|---|
| Health Care | 10 | 41.67% | **over the 30% cap** |
| Finance | 5 | 20.83% | within cap |
| Consumer Discretionary | 3 | 12.50% | within cap |
| Industrials | 2 | 8.33% | within cap |
| Technology | 2 | 8.33% | within cap |
| Consumer Staples | 1 | 4.17% | within cap |
| Energy | 1 | 4.17% | within cap |

## Correlation structure

Average pairwise correlation across all 276 pairs of the published 24 is
**0.1416** — comfortably inside the 0.45 cap. That low figure is itself
evidence for the diagnosis in `05`: the sleeve is a collection of defensive names that are
uncorrelated with each other *and* with the market, which is precisely why its beta cannot be lifted
to the band.

## Per-position Recommendation Metrics Table

Values are inherited from `05` without recomputation.

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SJM | 131.84 | 2026-08-27 | `DELAYED` | 139.75 | 2026-09-24 | +6.00% | 8.68% | `REALIZED_VOL_30D` | 0.6559 | 1.2731 | 0.7058 | 1.9916 | -8.32% | -11.88% | -8.42% | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.13 / 74.47 / 62.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 127.85 | 151.65 | (0.30x`UNAVL` + 0.30x+1.4397 + 0.25x`UNAVL` + 0.15x-0.0531) x 0.80 - 0.00 = +0.3392 | L200, L300, L400, L500, L600 |
| RVTY | 129.71 | 2026-08-27 | `DELAYED` | 137.49 | 2026-09-24 | +6.00% | 9.93% | `REALIZED_VOL_30D` | 0.5733 | 1.1903 | 0.4929 | 1.5216 | -10.38% | -14.45% | -6.38% | SELL_SETUP_7 / SELL_SETUP_4 / SELL_SETUP_3 | 72.24 / 71.60 / 60.14 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 124.10 | 150.89 | (0.30x`UNAVL` + 0.30x+1.3875 + 0.25x`UNAVL` + 0.15x+0.0221) x 0.80 - 0.00 = +0.3357 | L201, L301, L401, L501, L601 |
| GILD | 148.86 | 2026-08-27 | `DELAYED` | 157.79 | 2026-09-24 | +6.00% | 7.47% | `REALIZED_VOL_30D` | 0.7616 | 1.5365 | 0.6795 | 2.6852 | -6.33% | -9.40% | -5.96% | SELL_SETUP_9 / SELL_SETUP_4 / SELL_SETUP_1 | 69.18 / 66.84 / 71.11 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 146.22 | 169.36 | (0.30x`UNAVL` + 0.30x+0.8990 + 0.25x`UNAVL` + 0.15x+0.6874) x 0.80 - 0.00 = +0.2983 | L202, L302, L402, L502, L602 |
| BLK | 1167.57 | 2026-08-27 | `DELAYED` | 1237.62 | 2026-09-24 | +6.00% | 6.76% | `REALIZED_VOL_30D` | 0.8416 | 1.9414 | 0.5806 | 3.2784 | -5.16% | -7.93% | -10.14% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 61.03 / 62.38 / 61.23 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 1155.49 | 1319.76 | (0.30x`UNAVL` + 0.30x+0.7774 + 0.25x`UNAVL` + 0.15x+0.9256) x 0.80 - 0.00 = +0.2977 | L203, L303, L403, L503, L603 |
| AMGN | 436.99 | 2026-08-27 | `DELAYED` | 463.21 | 2026-09-24 | +6.00% | 7.75% | `REALIZED_VOL_30D` | 0.7346 | 2.3263 | 0.7285 | 2.4978 | -6.79% | -9.96% | -5.05% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 68.94 / 74.38 / 71.79 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 427.99 | 498.43 | (0.30x`UNAVL` + 0.30x+1.0188 + 0.25x`UNAVL` + 0.15x+0.4200) x 0.80 - 0.00 = +0.2949 | L204, L304, L404, L504, L604 |
| JNJ | 265.77 | 2026-08-27 | `DELAYED` | 281.72 | 2026-09-24 | +6.00% | 6.20% | `REALIZED_VOL_30D` | 0.9179 | 1.2779 | 1.1124 | 3.9001 | -4.23% | -6.78% | -7.57% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_9 | 54.62 / 63.93 / 77.55 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 264.57 | 298.86 | (0.30x`UNAVL` + 0.30x+0.9190 + 0.25x`UNAVL` + 0.15x+0.5937) x 0.80 - 0.00 = +0.2918 | L205, L305, L405, L505, L605 |
| RMD | 235.76 | 2026-08-27 | `DELAYED` | 249.91 | 2026-09-24 | +6.00% | 9.85% | `REALIZED_VOL_30D` | 0.5776 | 0.9563 | 0.5375 | 1.5446 | -10.26% | -14.30% | -12.68% | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_1 | 66.40 / 59.71 / 51.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 225.74 | 274.07 | (0.30x`UNAVL` + 0.30x+0.9423 + 0.25x`UNAVL` + 0.15x+0.5445) x 0.80 - 0.00 = +0.2915 | L206, L306, L406, L506, L606 |
| A | 157.69 | 2026-08-27 | `DELAYED` | 167.15 | 2026-09-24 | +6.00% | 8.26% | `REALIZED_VOL_30D` | 0.6891 | 1.1163 | 0.6450 | 2.1981 | -7.63% | -11.02% | -10.15% | BUY_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_4 | 70.27 / 69.14 / 60.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 153.60 | 180.70 | (0.30x`UNAVL` + 0.30x+1.2053 + 0.25x`UNAVL` + 0.15x+0.0121) x 0.80 - 0.00 = +0.2907 | L207, L307, L407, L507, L607 |
| VEEV | 282.13 | 2026-08-27 | `DELAYED` | 299.06 | 2026-09-24 | +6.00% | 16.61% | `REALIZED_VOL_30D` | 0.3427 | 0.9930 | 0.3424 | 0.5435 | -21.41% | -28.22% | -16.28% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 79.57 / 73.59 / 60.55 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 250.31 | 347.80 | (0.30x`UNAVL` + 0.30x+1.3802 + 0.25x`UNAVL` + 0.15x-0.3429) x 0.80 - 0.00 = +0.2901 | L208, L308, L408, L508, L608 |
| NWSA | 31.19 | 2026-08-27 | `DELAYED` | 33.06 | 2026-09-24 | +6.00% | 8.39% | `REALIZED_VOL_30D` | 0.6784 | 0.9828 | 0.8330 | 2.1303 | -7.85% | -11.29% | -9.72% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 71.28 / 69.40 / 62.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 30.34 | 35.78 | (0.30x`UNAVL` + 0.30x+1.2435 + 0.25x`UNAVL` + 0.15x-0.0965) x 0.80 - 0.00 = +0.2868 | L209, L309, L409, L509, L609 |
| FTNT | 172.78 | 2026-08-27 | `DELAYED` | 183.15 | 2026-09-24 | +6.00% | 12.43% | `REALIZED_VOL_30D` | 0.4578 | 1.3919 | 0.3310 | 0.9703 | -14.52% | -19.61% | -10.40% | SELL_SETUP_3 / SELL_SETUP_2 / SELL_SETUP_6 | 64.73 / 75.31 / 80.05 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 160.81 | 205.49 | (0.30x`UNAVL` + 0.30x+1.0794 + 0.25x`UNAVL` + 0.15x+0.2095) x 0.80 - 0.00 = +0.2842 | L210, L310, L410, L510, L610 |
| STT | 193.37 | 2026-08-27 | `DELAYED` | 204.97 | 2026-09-24 | +6.00% | 6.74% | `REALIZED_VOL_30D` | 0.8449 | 1.1408 | 0.7246 | 3.3046 | -5.12% | -7.88% | -5.65% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 62.10 / 81.83 / 88.76 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 191.42 | 218.52 | (0.30x`UNAVL` + 0.30x+0.7371 + 0.25x`UNAVL` + 0.15x+0.8453) x 0.80 - 0.00 = +0.2784 | L211, L311, L411, L511, L611 |
| BNY | 162.24 | 2026-08-27 | `DELAYED` | 171.97 | 2026-09-24 | +6.00% | 5.60% | `REALIZED_VOL_30D` | 1.0161 | 1.4353 | 0.7819 | 4.7788 | -3.24% | -5.54% | -5.69% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 57.46 / 75.98 / 91.33 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 162.52 | 181.43 | (0.30x`UNAVL` + 0.30x+0.6397 + 0.25x`UNAVL` + 0.15x+1.0325) x 0.80 - 0.00 = +0.2774 | L212, L312, L412, L512, L612 |
| SCHW | 108.05 | 2026-08-27 | `DELAYED` | 114.53 | 2026-09-24 | +6.00% | 5.68% | `REALIZED_VOL_30D` | 1.0017 | 1.5782 | 0.9387 | 4.6448 | -3.38% | -5.71% | -5.36% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 51.69 / 64.25 / 66.76 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 108.15 | 120.92 | (0.30x`UNAVL` + 0.30x+0.8276 + 0.25x`UNAVL` + 0.15x+0.6445) x 0.80 - 0.00 = +0.2760 | L213, L313, L413, L513, L613 |
| NWS | 35.32 | 2026-08-27 | `DELAYED` | 37.44 | 2026-09-24 | +6.00% | 8.74% | `REALIZED_VOL_30D` | 0.6512 | 0.9301 | 0.7939 | 1.9632 | -8.42% | -12.01% | -10.48% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 70.10 / 67.64 / 61.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 34.23 | 40.65 | (0.30x`UNAVL` + 0.30x+1.1709 + 0.25x`UNAVL` + 0.15x-0.0487) x 0.80 - 0.00 = +0.2752 | L214, L314, L414, L514, L614 |
| VRTX | 547.55 | 2026-08-27 | `DELAYED` | 580.40 | 2026-09-24 | +6.00% | 8.43% | `REALIZED_VOL_30D` | 0.6752 | 1.7498 | 0.6633 | 2.1103 | -7.91% | -11.37% | -11.12% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_2 | 65.06 / 68.87 / 63.34 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | 532.39 | 628.41 | (0.30x`UNAVL` + 0.30x+0.9129 + 0.25x`UNAVL` + 0.15x+0.4441) x 0.80 - 0.00 = +0.2724 | L215, L315, L415, L515, L615 |
| BAC | 61.17 | 2026-08-27 | `DELAYED` | 64.84 | 2026-09-24 | +6.00% | 4.79% | `REALIZED_VOL_30D` | 1.1895 | 1.7206 | 1.0138 | 6.5499 | -1.90% | -3.86% | -5.62% | BUY_SETUP_1 / BUY_SETUP_2 / SELL_SETUP_3 | 43.15 / 62.35 / 70.00 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 61.80 | 67.88 | (0.30x`UNAVL` + 0.30x+0.7732 + 0.25x`UNAVL` + 0.15x+0.7048) x 0.80 - 0.00 = +0.2701 | L216, L316, L416, L516, L616 |
| MPC | 363.54 | 2026-08-27 | `DELAYED` | 385.35 | 2026-09-24 | +6.00% | 10.59% | `REALIZED_VOL_30D` | 0.5378 | 0.9894 | 0.6252 | 1.3387 | -11.47% | -15.81% | -9.09% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_7 | 69.54 / 76.64 / 85.17 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 345.33 | 425.37 | (0.30x`UNAVL` + 0.30x+1.3078 + 0.25x`UNAVL` + 0.15x-0.3904) x 0.80 - 0.00 = +0.2670 | L217, L317, L417, L517, L617 |
| CRL | 296.41 | 2026-08-27 | `DELAYED` | 314.19 | 2026-09-24 | +6.00% | 13.32% | `REALIZED_VOL_30D` | 0.4275 | 1.5494 | 0.4094 | 0.8460 | -15.97% | -21.43% | -6.38% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_3 | 73.88 / 77.28 / 67.05 | `BEARISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 273.15 | 355.24 | (0.30x`UNAVL` + 0.30x+0.9789 + 0.25x`UNAVL` + 0.15x+0.2429) x 0.80 - 0.00 = +0.2641 | L218, L318, L418, L518, L618 |
| BMY | 66.95 | 2026-08-27 | `DELAYED` | 70.97 | 2026-09-24 | +6.00% | 6.73% | `REALIZED_VOL_30D` | 0.8463 | 1.1608 | 0.7006 | 3.3151 | -5.10% | -7.86% | -5.71% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 60.33 / 68.54 / 66.75 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 66.28 | 75.65 | (0.30x`UNAVL` + 0.30x+0.6392 + 0.25x`UNAVL` + 0.15x+0.9162) x 0.80 - 0.00 = +0.2633 | L219, L319, L419, L519, L619 |
| TGT | 165.93 | 2026-08-27 | `DELAYED` | 175.89 | 2026-09-24 | +6.00% | 8.64% | `REALIZED_VOL_30D` | 0.6586 | 1.1820 | 0.6193 | 2.0080 | -8.26% | -11.80% | -10.69% | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_9 | 68.99 / 75.58 / 70.45 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 160.97 | 190.80 | (0.30x`UNAVL` + 0.30x+1.1096 + 0.25x`UNAVL` + 0.15x-0.0407) x 0.80 - 0.00 = +0.2614 | L220, L320, L420, L520, L620 |
| TECH | 72.48 | 2026-08-27 | `DELAYED` | 76.83 | 2026-09-24 | +6.00% | 1.18% | `REALIZED_VOL_30D` | 4.8104 | 7.5112 | 0.3459 | 107.1161 | +4.05% | +3.56% | -4.02% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 69.49 / 65.96 / 55.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 75.94 | 77.72 | (0.30x`UNAVL` + 0.30x+0.4908 + 0.25x`UNAVL` + 0.15x+1.1583) x 0.80 - 0.00 = +0.2568 | L221, L321, L421, L521, L621 |
| PFE | 28.02 | 2026-08-27 | `DELAYED` | 29.70 | 2026-09-24 | +6.00% | 5.92% | `REALIZED_VOL_30D` | 0.9609 | 2.4778 | 0.9310 | 4.2741 | -3.77% | -6.20% | -9.69% | BUY_SETUP_1 / SELL_SETUP_6 / SELL_SETUP_1 | 65.39 / 66.78 / 58.24 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | 27.97 | 31.43 | (0.30x`UNAVL` + 0.30x+0.7495 + 0.25x`UNAVL` + 0.15x+0.6313) x 0.80 - 0.00 = +0.2556 | L222, L322, L422, L522, L622 |
| ABT | 111.59 | 2026-08-27 | `DELAYED` | 118.29 | 2026-09-24 | +6.00% | 6.24% | `REALIZED_VOL_30D` | 0.9119 | 1.4735 | 0.7271 | 3.8493 | -4.30% | -6.86% | -7.18% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 57.65 / 60.30 / 50.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 111.04 | 125.53 | (0.30x`UNAVL` + 0.30x+0.6296 + 0.25x`UNAVL` + 0.15x+0.8693) x 0.80 - 0.00 = +0.2554 | L223, L323, L423, L523, L623 |

## Factor exposure summary

| Family | Weight | State | Contribution to the sleeve |
|---|---|---|---|
| Fundamental | 0.30 | `UNAVAILABLE` (L021) | `0.00 (UNAVAILABLE)` |
| Technical / Price | 0.30 | live, 6 equal-weighted slots | mean published `Tech_Z` +0.9691 — 66.7% of live conviction |
| Sentiment / Positioning | 0.25 | `UNAVAILABLE` (L022) | `0.00 (UNAVAILABLE)` |
| Macro / Regime | 0.15 | live, 4 equal-weighted slots | mean published `Macro_Z` +0.4138 — 33.3% of live conviction |

Factor crowding flag: **raised**. More than half the sleeve's conviction loads on a single family
(Technical, 66.7%), which `rules.md § Risk Controls` requires to be flagged.

## Why names were excluded

| Exclusion | Names | Reason |
|---|---|---|
| Below the 60th-percentile rank floor | 305 of 509 | `rules.md § mu Calibration Table` — not ranked in either sleeve, rejection log only |
| Ranked but outside the published sleeve | 180 | the published sleeve is the top 24 by post-penalty `Adj Score`, matching recent package precedent |
| Rejected before scoring | 6 | see the `04` rejection log (corporate actions, market-cap vendor gap, listing age, indicator completeness) |
| Core ETFs | SPY, QQQ, SOXX | market-forecast sleeve only — never candidates, never universe members (`rules.md § Core ETF Market Forecast`) |
