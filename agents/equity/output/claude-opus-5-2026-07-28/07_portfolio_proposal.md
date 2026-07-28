# 07 Portfolio Proposal — 2026-07-28

## Outcome: **NO PORTFOLIO — `NO_TRADE`**

No weights are proposed. Per `agents.md § Portfolio Construction` Task 0, the feasibility pre-check runs
**before** any sizing, and per the failure rule a portfolio is never forced.

## Task 0 — Constraint Feasibility Pre-check

| Quantity | Value | Source |
|---|---|---|
| Single-name cap | 5% | `rules.md § Risk Controls` (protected) |
| ⇒ minimum names to be fully invested | **20** | 1 / 0.05 |
| Candidate pool at ≥ 80th percentile | 103 names | L039 |
| **Max attainable sleeve beta** | **0.899853** | mean of the 20 highest betas in the pool (L015, L049) |
| Min attainable sleeve beta | -0.820703 | mean of the 20 lowest betas |
| Required band | 0.90 – 1.10 | `rules.md § Risk Controls` (protected) |
| **Shortfall vs the floor** | **0.000147** (1.47 bp) | — |
| Verdict | `INFEASIBLE` | — |

The 20 highest betas available in the pool are:

+1.5274, +1.4119, +1.2827, +1.1605, +1.1168, +1.0538, +0.9887, +0.9653, +0.9529, +0.8233, +0.8057, +0.8047, +0.7098, +0.6868, +0.6758, +0.6448, +0.6175, +0.6050, +0.5993, +0.5643

Their mean is 0.899853. Because 5% is a hard cap, no weighting of the ≥80th-percentile
pool can reach 0.90: putting the maximum 5% into each of the twenty highest-beta names *is*
the maximum, and it lands 1.47 basis points short.

**Stated plainly: this is a knife-edge result and should not be oversold.** A miss of 1.5 bp is inside
any reasonable estimation error on a 60-day beta regression, and it would flip on a single constituent's
daily return. It is *not* comparable to the 2026-07-27 package's 0.8519 (a 4.81pp
miss) or the 2026-07-24 package's +0.114. **The load-bearing reasons for `NO_TRADE` are the evidence
thresholds in `05`, which fail by wide, non-marginal margins.** This pre-check corroborates; it does not
carry the decision. Reporting it the other way round would be overstating the evidence.

## Risk Analytics on the Top-10 Sleeve (diagnostic, equal-weighted)

Computed so the caps are actually tested rather than asserted. Basis: 60 trading days of adjusted daily
returns (L003, L050, L051).

| Metric | Value | Cap | Verdict |
|---|---|---|---|
| Expected beta to SPY | -0.1815 | 0.90 – 1.10 | **FAIL** (far below the floor) |
| Average pairwise correlation | 0.1931 | < 0.45 | **PASS** |
| Portfolio sigma (1-month) | 4.59% | — | — |
| 95th-pctl 1-month drawdown | 7.57% | ≤ 8% | **PASS** |
| Max sector share | 33.3% (Industrials) | ≤ 30% | **PASS** |

`dd95 = 1.65 × portfolio_sigma_1m`, normal distribution assumed and stated.

**The sleeve is disqualified for being too defensive, not too risky.** Correlation, drawdown and sector
concentration all pass with room; the only breached risk cap is the beta *floor*.

### Correlation matrix — top-10 sleeve

| | RTX | TRV | PAYX | SJM | CSX | DGX | BBY | IQV | MET | UNP |
|---|---|---|---|---|---|---|---|---|---|---|
| **RTX** | +1.000 | +0.158 | +0.036 | +0.119 | +0.171 | +0.510 | -0.025 | +0.173 | +0.226 | +0.168 |
| **TRV** | +0.158 | +1.000 | +0.254 | +0.241 | +0.183 | +0.349 | -0.086 | -0.037 | +0.406 | +0.331 |
| **PAYX** | +0.036 | +0.254 | +1.000 | +0.360 | -0.007 | +0.200 | +0.046 | +0.318 | +0.365 | +0.163 |
| **SJM** | +0.119 | +0.241 | +0.360 | +1.000 | -0.060 | +0.395 | +0.121 | +0.172 | +0.229 | +0.131 |
| **CSX** | +0.171 | +0.183 | -0.007 | -0.060 | +1.000 | +0.395 | -0.134 | +0.080 | +0.281 | +0.826 |
| **DGX** | +0.510 | +0.349 | +0.200 | +0.395 | +0.395 | +1.000 | -0.003 | +0.400 | +0.109 | +0.407 |
| **BBY** | -0.025 | -0.086 | +0.046 | +0.121 | -0.134 | -0.003 | +1.000 | +0.361 | +0.070 | -0.192 |
| **IQV** | +0.173 | -0.037 | +0.318 | +0.172 | +0.080 | +0.400 | +0.361 | +1.000 | -0.010 | +0.091 |
| **MET** | +0.226 | +0.406 | +0.365 | +0.229 | +0.281 | +0.109 | +0.070 | -0.010 | +1.000 | +0.401 |
| **UNP** | +0.168 | +0.331 | +0.163 | +0.131 | +0.826 | +0.407 | -0.192 | +0.091 | +0.401 | +1.000 |

### Sector table — published set

| Sector | Names | Share of the 24-name set | Members |
|---|---|---|---|
| Industrials | 8 | 33.3% | RTX, PAYX, CSX, UNP, NSC, ITW, CTAS, LMT |
| Finance | 7 | 29.2% | TRV, MET, IVZ, PFG, PRU, CB, BNY |
| Health Care | 3 | 12.5% | DGX, IQV, PM |
| Consumer Discretionary | 2 | 8.3% | BBY, PKG |
| Real Estate | 2 | 8.3% | EXR, WELL |
| Consumer Staples | 1 | 4.2% | SJM |
| Energy | 1 | 4.2% | MPC |

## Per-Position Recommendation Metrics

Inherited unchanged from `05` — nothing is recomputed here. Since no position is sized, these are
forecast records, not allocations.

| Ticker | Entry | Date | Tag | Target | Target Date | mu | sigma | SigSrc | Sharpe | Sortino | IR | Kelly .25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | CI Lo | CI Hi | Score Trace | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTX | 218.42 | 2026-07-27 | HISTORICAL | 231.53 | 2026-08-25 | +6.0% | 9.36% | REALIZED_VOL_30D | 0.6070 | 1.1111 | 0.7014 | 0.0500 | -9.44% | -13.28% | -5.58% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 77.33/69.16/75.98 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 210.26 | 252.79 | T +1.216 · M +0.610 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| TRV | 390.35 | 2026-07-27 | HISTORICAL | 413.77 | 2026-08-25 | +6.0% | 9.15% | REALIZED_VOL_30D | 0.6207 | 1.8099 | 0.8771 | 0.0500 | -9.10% | -12.86% | -5.96% | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_9 | 81.67/80.19/77.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 376.61 | 450.93 | T +0.865 · M +0.834 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| PAYX | 115.48 | 2026-07-27 | HISTORICAL | 122.41 | 2026-08-25 | +6.0% | 9.15% | REALIZED_VOL_30D | 0.6211 | 1.3870 | 0.7236 | 0.0500 | -9.09% | -12.85% | -6.35% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 67.48/66.21/51.32 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 111.42 | 133.40 | T +0.838 · M +0.784 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| SJM | 121.05 | 2026-07-27 | HISTORICAL | 128.31 | 2026-08-25 | +6.0% | 9.49% | REALIZED_VOL_30D | 0.5986 | 1.1540 | 0.6501 | 0.0500 | -9.66% | -13.55% | -8.42% | SELL_SETUP_8/SELL_SETUP_3/SELL_SETUP_1 | 64.82/65.78/57.81 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 116.36 | 140.26 | T +0.780 · M +0.722 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| CSX | 51.8 | 2026-07-27 | HISTORICAL | 54.91 | 2026-08-25 | +6.0% | 7.42% | REALIZED_VOL_30D | 0.7657 | 1.4335 | 0.8689 | 0.0500 | -6.24% | -9.29% | -4.20% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9 | 64.1/72.1/75.39 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 50.91 | 58.91 | T +0.762 · M +0.728 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| DGX | 231.84 | 2026-07-27 | HISTORICAL | 245.75 | 2026-08-25 | +6.0% | 9.45% | REALIZED_VOL_30D | 0.6011 | 2.0692 | 0.8294 | 0.0500 | -9.59% | -13.47% | -6.22% | SELL_SETUP_8/SELL_SETUP_6/SELL_SETUP_6 | 75.04/69.79/69.55 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 222.96 | 268.54 | T +0.743 · M +0.754 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| BBY | 88.45 | 2026-07-27 | HISTORICAL | 93.76 | 2026-08-25 | +6.0% | 8.94% | REALIZED_VOL_30D | 0.6356 | 1.1826 | 0.4372 | 0.0500 | -8.75% | -12.41% | -8.93% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 71.0/68.3/60.98 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 85.53 | 101.98 | T +0.958 · M +0.205 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| IQV | 213.22 | 2026-07-27 | HISTORICAL | 226.01 | 2026-08-25 | +6.0% | 11.29% | REALIZED_VOL_30D | 0.5032 | 1.0473 | 0.4797 | 0.0500 | -12.63% | -17.26% | -10.23% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_2 | 65.6/60.89/53.47 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 200.98 | 251.05 | T +0.963 · M +0.174 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| MET | 95.19 | 2026-07-27 | HISTORICAL | 100.90 | 2026-08-25 | +6.0% | 7.04% | REALIZED_VOL_30D | 0.8069 | 1.2326 | 0.9176 | 0.0500 | -5.62% | -8.50% | -4.77% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 68.04/71.35/67.86 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | 93.93 | 107.87 | T +1.054 · M +0.803 · DQ 0.8 · P −0.10 | L002,L003,L013-L021,L027-L039 |
| UNP | 299.3 | 2026-07-27 | HISTORICAL | 317.26 | 2026-08-25 | +6.0% | 7.63% | REALIZED_VOL_30D | 0.7447 | 1.1719 | 0.8175 | 0.0500 | -6.59% | -9.72% | -7.58% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_9 | 62.46/67.48/67.29 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 293.51 | 341.01 | T +0.664 · M +0.717 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| IVZ | 30.11 | 2026-07-27 | HISTORICAL | 31.92 | 2026-08-25 | +6.0% | 11.00% | REALIZED_VOL_30D | 0.5167 | 0.8159 | 0.6304 | 0.0500 | -12.14% | -16.65% | -11.40% | SELL_SETUP_4/SELL_SETUP_4/SELL_SETUP_9 | 60.68/65.03/69.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 28.47 | 35.36 | T +1.167 · M -0.323 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| PFG | 111.29 | 2026-07-27 | HISTORICAL | 117.97 | 2026-08-25 | +6.0% | 6.97% | REALIZED_VOL_30D | 0.8157 | 1.0252 | 0.9755 | 0.0500 | -5.49% | -8.35% | -6.16% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 54.18/66.53/73.58 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 109.91 | 126.03 | T +0.602 · M +0.789 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| PRU | 121.89 | 2026-07-27 | HISTORICAL | 129.20 | 2026-08-25 | +6.0% | 6.16% | REALIZED_VOL_30D | 0.9219 | 1.9234 | 1.0053 | 0.0500 | -4.17% | -6.70% | -2.66% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 72.36/70.86/64.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 121.39 | 137.02 | T +1.013 · M +0.787 · DQ 0.8 · P −0.10 | L002,L003,L013-L021,L027-L039 |
| NSC | 343.35 | 2026-07-27 | HISTORICAL | 363.95 | 2026-08-25 | +6.0% | 7.24% | REALIZED_VOL_30D | 0.7851 | 1.3473 | 0.8589 | 0.0500 | -5.94% | -8.91% | -7.86% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_4 | 64.18/66.04/66.36 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 338.11 | 389.79 | T +0.622 · M +0.719 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| ITW | 284.82 | 2026-07-27 | HISTORICAL | 301.91 | 2026-08-25 | +6.0% | 6.66% | REALIZED_VOL_30D | 0.8536 | 1.7159 | 0.9586 | 0.0500 | -4.98% | -7.71% | -5.65% | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_1 | 66.39/64.09/60.75 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 282.19 | 321.63 | T +0.613 · M +0.666 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| CTAS | 210.98 | 2026-07-27 | HISTORICAL | 223.64 | 2026-08-25 | +6.0% | 10.29% | REALIZED_VOL_30D | 0.5523 | 1.2639 | 0.6819 | 0.0500 | -10.97% | -15.19% | -7.19% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 75.19/67.27/59.73 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 201.07 | 246.21 | T +0.677 · M +0.539 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| EXR | 148.29 | 2026-07-27 | HISTORICAL | 157.19 | 2026-08-25 | +6.0% | 6.36% | REALIZED_VOL_30D | 0.8940 | 1.7965 | 0.9211 | 0.0500 | -4.49% | -7.09% | -5.45% | SELL_SETUP_2/BUY_SETUP_2/SELL_SETUP_1 | 55.25/56.59/55.03 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 147.39 | 166.99 | T +0.518 · M +0.851 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| MPC | 312.35 | 2026-07-27 | HISTORICAL | 331.09 | 2026-08-25 | +6.0% | 9.46% | REALIZED_VOL_30D | 0.6008 | 1.0461 | 0.6321 | 0.0500 | -9.60% | -13.48% | -9.09% | BUY_SETUP_3/SELL_SETUP_6/SELL_SETUP_6 | 69.71/73.77/81.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 300.37 | 361.81 | T +1.064 · M +0.584 · DQ 0.8 · P −0.10 | L002,L003,L013-L021,L027-L039 |
| WELL | 248.34 | 2026-07-27 | HISTORICAL | 263.24 | 2026-08-25 | +6.0% | 6.89% | REALIZED_VOL_30D | 0.8251 | 1.4755 | 0.8431 | 0.0500 | -5.36% | -8.19% | -11.26% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_4 | 67.61/69.59/77.07 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 245.46 | 281.03 | T +0.528 · M +0.775 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| CB | 358.91 | 2026-07-27 | HISTORICAL | 380.44 | 2026-08-25 | +6.0% | 8.03% | REALIZED_VOL_30D | 0.7079 | 1.3335 | 1.1227 | 0.0500 | -7.24% | -10.53% | -6.57% | SELL_SETUP_3/BUY_SETUP_1/SELL_SETUP_9 | 59.4/64.6/69.25 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 350.49 | 410.40 | T +0.422 · M +0.968 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| LMT | 580.0 | 2026-07-27 | HISTORICAL | 614.80 | 2026-08-25 | +6.0% | 12.18% | REALIZED_VOL_30D | 0.4663 | 1.1869 | 0.6500 | 0.0500 | -14.10% | -19.10% | -10.40% | SELL_SETUP_4/SELL_SETUP_2/BUY_SETUP_3 | 70.25/56.94/58.69 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | 541.31 | 688.29 | T +0.711 · M +0.296 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| PM | 195.66 | 2026-07-27 | HISTORICAL | 207.40 | 2026-08-25 | +6.0% | 9.26% | REALIZED_VOL_30D | 0.6139 | 1.2923 | 0.7233 | 0.0500 | -9.27% | -13.07% | -10.01% | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_1 | 62.03/65.58/69.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 188.57 | 226.23 | T +0.555 · M +0.604 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| BNY | 157.77 | 2026-07-27 | HISTORICAL | 167.24 | 2026-08-25 | +6.0% | 7.21% | REALIZED_VOL_30D | 0.7881 | 1.5655 | 0.9372 | 0.0500 | -5.89% | -8.85% | -3.34% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 62.23/82.91/90.85 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 155.41 | 179.06 | T +0.547 · M +0.592 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |
| PKG | 252.37 | 2026-07-27 | HISTORICAL | 264.99 | 2026-08-25 | +5.0% | 9.54% | REALIZED_VOL_30D | 0.4908 | 1.1079 | 0.5098 | 0.0500 | -10.74% | -14.65% | -10.43% | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_2 | 69.48/65.62/67.69 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 239.95 | 290.02 | T +0.681 · M +0.096 · DQ 0.8 · P −0.00 | L002,L003,L013-L021,L027-L039 |

**Kelly note.** Every published name computes `0.25 × Kelly` above the 5% single-name cap, so the cap
binds for all 24 and none trips the `< 2% NAV` penalty. That is a consequence of the low realized
vols in this defensive cohort (`raw Kelly = mu / sigma²` with sigma around 9.36%), not
evidence of unusual conviction.

## Excluded Names

| Group | Count | Why |
|---|---|---|
| Below the 60th percentile | 308 | not ranked in either sleeve (`rules.md § mu Calibration Table`) |
| Ranked but below the published set | 182 | monitoring-eligible; publication is capped at 24 names |
| Top-30 entrants never earnings-grounded | 7 | DXCM, BXP, BAC, FRT, KVUE, FFIV, SO — excluded rather than published penalty-free |
| Failed universe filters | 1 | FDXF (listing age) |
