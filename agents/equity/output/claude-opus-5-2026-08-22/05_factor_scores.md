# 05 — Factor Scores · 2026-08-22

Universe `INDEX_UNION_PCTL (n=509)` · DQ multiplier 0.80 (`L020`) ·
price basis **2026-08-21** · target date **2026-09-19** (`run_date + 28d`).

Every value below is generated from `run_computed_manifest.json`; no figure in this artifact was
typed by hand. Every metric cited has a Source Ledger row in `01`.

## Metric Definition Table (normative)

Carried forward unchanged from the Track B change accepted in
`claude-opus-5-2026-08-03/13_evolution_log.md` and first shipped 2026-08-04. This table is
**normative**: if it and the running code disagree, one of them is wrong and the run must say which.
Polarity is stated as the **post-transform direction**, never as an instruction word like "negated",
so a reader can answer "does a larger raw value help or hurt?" without knowing the sign convention
of the stored field.

| Metric slot | Family | Source field | Window | Transform before z-score | Polarity (higher-is-better after transform) | Winsorization |
|---|---|---|---|---|---|---|
| `mom20` | Technical | `technical_indicators.json` `daily.momentum_20d_pct` | trailing 20 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `mom60` | Technical | `daily.momentum_60d_pct` | trailing 60 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `ma_align` | Technical | `daily.ma_alignment` + `weekly.ma_alignment` | daily and weekly blocks | encode `BULLISH=+1, MIXED=0, BEARISH=-1`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `macd` | Technical | `daily.macd_state` + `weekly.macd_state` | daily and weekly blocks | encode `BULLISH_CROSS=+2, ABOVE_SIGNAL=+1, ON_SIGNAL=0, BELOW_SIGNAL=-1, BEARISH_CROSS=-2`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `vol_conf` | Technical | `daily.volume_ratio_20d` | trailing 20 daily sessions | none (ratio) | **higher raw value is better** | 5th/95th pctl |
| `dd60` | Technical | worst peak-to-trough of adjusted closes | the **61 most recent daily closes** (= the 60 most recent daily return intervals) | none — the field is **already stored as a signed negative number** | **higher raw value is better** (a shallower drawdown scores higher). Do **not** apply a negation. | 5th/95th pctl |
| `beta` | Macro | regression slope of daily adjusted returns vs SPY | trailing 60 daily return intervals; `cov(r, r_SPY, ddof=0) / var(r_SPY)` | `-abs(beta - 1.0)` | **higher transformed value is better** (beta closest to 1.0 scores highest) | 5th/95th pctl |
| `sector_lead` | Macro | `daily.momentum_60d_pct` of every scored member of the name's sector | trailing 60 daily sessions | **median** across the sector's members, broadcast to each member | **higher transformed value is better** | 5th/95th pctl |
| `rate_sens` | Macro | regression slope of daily adjusted returns vs **TLT** | trailing 60 daily return intervals | `-abs(beta_TLT)` | **higher transformed value is better** (lower absolute rate sensitivity scores higher) | 5th/95th pctl |
| `vol_stability` | Macro | daily adjusted returns | `vol30` = population stdev (`ddof=0`) of the trailing 30 daily returns x `sqrt(21)`; `vol60` likewise over 60 | `-(vol30 / vol60)` | **higher transformed value is better** (vol contracting relative to its own 60-day base) | 5th/95th pctl |

**Shared conventions, stated once:**

- **Input basis.** Every metric above is computed from **adjusted** closes (Track B 2026-07-26).
  Entry, target and CI prices use **raw** closes. `technical_indicators.py` is fed the adjusted tree.
- **z-score.** Winsorize the raw (post-transform) cross-section at the 5th and 95th percentiles by
  clipping, then subtract the mean and divide by the **population** standard deviation (`ddof=0`)
  *of the clipped series*.
- **Family aggregation.** Equal-weighted arithmetic mean of the family's slot z-scores.
- **Relative strength is not a slot.** `rs20`/`rs60` are computed, displayed and ledgered as
  diagnostics only (Track B effective 2026-08-03, codified in `rules.md`).

## Calibration feedback binding (read before scoring)

From `02 § 0` / L014a: `EQUITY_ALPHA` CI coverage **71.47%** is inside the
55–85% band, so the "widen sigma" binding does **not** fire and `REALIZED_VOL_30D` stands as the
sigma source. Aggregate rank IC across scored vintages is negative (mean
-0.0840
over 60 vintages), which triggers the
`rules.md` binding: **all confidence is capped at `MEDIUM`**. No positive per-name mu adjustments
were applied — every `mu` below is the unmodified calibration-table band value for the name's
percentile.

## Ranked candidate table (top 20)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BDX | Becton Dickinson and Company Commo | 192.00 | 2026-08-21 | `DELAYED` | +0.3899 | (0.30x`UNAVL` + 0.30x+1.4253 + 0.25x`UNAVL` + 0.15x+0.3983) x 0.80 − 0.00 = +0.3899 | 100.00 | -0.0942 | 8.16% | 0.6972 | 1.6714 | 0.7328 | 2.2520 | -7.47% | -10.81% | -7.45% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 78.53 / 72.66 / 61.51 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.16% | `REALIZED_VOL_30D` | 203.52 | 2026-09-19 | 187.22 | 219.82 | L200 | L300, L400, L500, L013, L002 | MEDIUM | Health Care at 100.00 pctl; Tech_Z +1.4253 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| SCHW | Charles Schwab Corporation (The) C | 112.30 | 2026-08-21 | `DELAYED` | +0.3754 | (0.30x`UNAVL` + 0.30x+1.1643 + 0.25x`UNAVL` + 0.15x+0.7995) x 0.80 − 0.00 = +0.3754 | 99.80 | -0.0653 | 5.18% | 1.0989 | 1.8621 | 0.9502 | 5.5944 | -2.54% | -4.67% | -5.36% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 71.12 / 73.08 / 68.81 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | +6.00% | 5.18% | `REALIZED_VOL_30D` | 119.04 | 2026-09-19 | 112.99 | 125.09 | L201 | L301, L401, L501, L013, L002 | MEDIUM | Finance at 99.80 pctl; Tech_Z +1.1643 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| AMP | Ameriprise Financial Inc. Common S | 555.59 | 2026-08-21 | `DELAYED` | +0.3583 | (0.30x`UNAVL` + 0.30x+0.9245 + 0.25x`UNAVL` + 0.15x+1.1369) x 0.80 − 0.00 = +0.3583 | 99.61 | 0.3483 | 5.17% | 1.1001 | 1.9456 | 0.8062 | 5.6069 | -2.53% | -4.65% | -5.34% | BUY_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 57.90 / 68.16 / 61.86 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 5.17% | `REALIZED_VOL_30D` | 588.93 | 2026-09-19 | 559.04 | 618.81 | L202 | L302, L402, L502, L013, L002 | MEDIUM | Finance at 99.61 pctl; Tech_Z +0.9245 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| CRL | Charles River Laboratories Interna | 295.19 | 2026-08-21 | `DELAYED` | +0.3575 | (0.30x`UNAVL` + 0.30x+1.3093 + 0.25x`UNAVL` + 0.15x+0.3603) x 0.80 − 0.00 = +0.3575 | 99.41 | 0.6061 | 13.48% | 0.4222 | 1.5930 | 0.3524 | 0.8257 | -16.24% | -21.77% | -6.38% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_3 | 76.28 / 77.10 / 66.91 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 13.48% | `REALIZED_VOL_30D` | 312.90 | 2026-09-19 | 271.52 | 354.28 | L203 | L303, L403, L503, L013, L002 | MEDIUM | Health Care at 99.41 pctl; Tech_Z +1.3093 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| REGN | Regeneron Pharmaceuticals Inc. Com | 834.04 | 2026-08-21 | `DELAYED` | +0.3460 | (0.30x`UNAVL` + 0.30x+1.1561 + 0.25x`UNAVL` + 0.15x+0.5710) x 0.80 − 0.00 = +0.3460 | 99.21 | 0.2702 | 8.66% | 0.6574 | 1.2377 | 0.6483 | 2.0023 | -8.28% | -11.83% | -5.32% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_1 | 76.55 / 68.32 / 57.15 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.66% | `REALIZED_VOL_30D` | 884.08 | 2026-09-19 | 809.01 | 959.16 | L204 | L304, L404, L504, L013, L002 | MEDIUM | Health Care at 99.21 pctl; Tech_Z +1.1561 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| FCX | Freeport-McMoRan Inc. Common Stock | 76.66 | 2026-08-21 | `DELAYED` | +0.3420 | (0.30x`UNAVL` + 0.30x+1.2952 + 0.25x`UNAVL` + 0.15x+0.2598) x 0.80 − 0.00 = +0.3420 | 99.02 | 2.3576 | 14.48% | 0.3929 | 1.2251 | 0.1059 | 0.7151 | -17.90% | -23.84% | -19.83% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 69.30 / 64.83 / 69.94 | `ABOVE_SIGNAL` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 14.48% | `REALIZED_VOL_30D` | 81.26 | 2026-09-19 | 69.71 | 92.81 | L205 | L305, L405, L505, L013, L002 | MEDIUM | Basic Materials at 99.02 pctl; Tech_Z +1.2952 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| RVTY | Revvity Inc. Common Stock | 124.75 | 2026-08-21 | `DELAYED` | +0.3417 | (0.30x`UNAVL` + 0.30x+1.3185 + 0.25x`UNAVL` + 0.15x+0.2107) x 0.80 − 0.00 = +0.3417 | 98.82 | 0.4327 | 9.66% | 0.5889 | 1.1825 | 0.4694 | 1.6070 | -9.94% | -13.90% | -6.44% | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_3 | 68.62 / 68.88 / 58.41 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 9.66% | `REALIZED_VOL_30D` | 132.24 | 2026-09-19 | 119.70 | 144.77 | L206 | L306, L406, L506, L013, L002 | MEDIUM | Industrials at 98.82 pctl; Tech_Z +1.3185 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| TGT | Target Corporation Common Stock | 165.44 | 2026-08-21 | `DELAYED` | +0.3388 | (0.30x`UNAVL` + 0.30x+1.4029 + 0.25x`UNAVL` + 0.15x+0.0173) x 0.80 − 0.00 = +0.3388 | 98.62 | 0.0192 | 8.02% | 0.7094 | 1.7787 | 0.6301 | 2.3313 | -7.24% | -10.52% | -10.69% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_9 | 76.54 / 75.41 / 70.32 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.02% | `REALIZED_VOL_30D` | 175.37 | 2026-09-19 | 161.57 | 189.17 | L207 | L307, L407, L507, L013, L002 | MEDIUM | Consumer Discretionary at 98.62 pctl; Tech_Z +1.4029 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| NEM | Newmont Corporation | 131.58 | 2026-08-21 | `DELAYED` | +0.3333 | (0.30x`UNAVL` + 0.30x+1.2021 + 0.25x`UNAVL` + 0.15x+0.3731) x 0.80 − 0.00 = +0.3333 | 98.43 | 1.8321 | 14.24% | 0.3996 | 0.9329 | 0.1903 | 0.7398 | -17.49% | -23.33% | -18.77% | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_1 | 75.93 / 65.61 / 70.66 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 14.24% | `REALIZED_VOL_30D` | 139.47 | 2026-09-19 | 119.99 | 158.96 | L208 | L308, L408, L508, L013, L002 | MEDIUM | Basic Materials at 98.43 pctl; Tech_Z +1.2021 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| TECH | Bio-Techne Corp Common Stock | 72.32 | 2026-08-21 | `DELAYED` | +0.3265 | (0.30x`UNAVL` + 0.30x+0.8182 + 0.25x`UNAVL` + 0.15x+1.0844) x 0.80 − 0.00 = +0.3265 | 98.23 | 0.7445 | 1.25% | 4.5572 | 7.5696 | 0.3270 | 96.2184 | +3.94% | +3.43% | -4.02% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 67.74 / 65.68 / 55.35 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 1.25% | `REALIZED_VOL_30D` | 76.66 | 2026-09-19 | 75.72 | 77.60 | L209 | L309, L409, L509, L013, L002 | MEDIUM | Health Care at 98.23 pctl; Tech_Z +0.8182 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| LH | Labcorp Holdings Inc. Common Stock | 336.34 | 2026-08-21 | `DELAYED` | +0.3138 | (0.30x`UNAVL` + 0.30x+1.1779 + 0.25x`UNAVL` + 0.15x+0.2590) x 0.80 − 0.00 = +0.3138 | 98.03 | -0.0706 | 7.25% | 0.7849 | 1.7776 | 0.8846 | 2.8543 | -5.96% | -8.93% | -6.20% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 75.74 / 74.08 / 68.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 7.25% | `REALIZED_VOL_30D` | 356.52 | 2026-09-19 | 331.16 | 381.88 | L210 | L310, L410, L510, L013, L002 | MEDIUM | Health Care at 98.03 pctl; Tech_Z +1.1779 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| MRK | Merck & Company Inc. Common Stock  | 152.55 | 2026-08-21 | `DELAYED` | +0.3113 | (0.30x`UNAVL` + 0.30x+1.4270 + 0.25x`UNAVL` + 0.15x-0.2595) x 0.80 − 0.00 = +0.3113 | 97.83 | -0.2631 | 12.06% | 0.4718 | 1.3412 | 0.6078 | 1.0314 | -13.90% | -18.84% | -6.78% | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_9 | 77.91 / 75.08 / 75.15 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 12.06% | `REALIZED_VOL_30D` | 161.70 | 2026-09-19 | 142.57 | 180.84 | L211 | L311, L411, L511, L013, L002 | MEDIUM | Health Care at 97.83 pctl; Tech_Z +1.4270 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| RJF | Raymond James Financial Inc. Commo | 175.20 | 2026-08-21 | `DELAYED` | +0.3034 | (0.30x`UNAVL` + 0.30x+0.7866 + 0.25x`UNAVL` + 0.15x+0.9553) x 0.80 − 0.00 = +0.3034 | 97.64 | 0.2523 | 5.57% | 1.0209 | 1.5559 | 0.8299 | 4.8286 | -3.20% | -5.48% | -6.10% | BUY_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 51.45 / 62.55 / 61.20 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 5.57% | `REALIZED_VOL_30D` | 185.71 | 2026-09-19 | 175.56 | 195.87 | L212 | L312, L412, L512, L013, L002 | MEDIUM | Finance at 97.64 pctl; Tech_Z +0.7866 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| DE | Deere & Company Common Stock | 647.47 | 2026-08-21 | `DELAYED` | +0.2946 | (0.30x`UNAVL` + 0.30x+1.1842 + 0.25x`UNAVL` + 0.15x+0.0866) x 0.80 − 0.00 = +0.2946 | 97.44 | 0.6305 | 10.16% | 0.5603 | 1.1853 | 0.4787 | 1.4543 | -10.76% | -14.92% | -9.25% | SELL_SETUP_2 / SELL_SETUP_3 / SELL_SETUP_8 | 62.38 / 61.38 / 64.38 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 10.16% | `REALIZED_VOL_30D` | 686.32 | 2026-09-19 | 617.93 | 754.71 | L213 | L313, L413, L513, L013, L002 | MEDIUM | Industrials at 97.44 pctl; Tech_Z +1.1842 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| NDSN | Nordson Corporation Common Stock | 332.24 | 2026-08-21 | `DELAYED` | +0.2942 | (0.30x`UNAVL` + 0.30x+1.2104 + 0.25x`UNAVL` + 0.15x+0.0310) x 0.80 − 0.00 = +0.2942 | 97.24 | 0.7096 | 8.23% | 0.6917 | 1.6281 | 0.6117 | 2.2166 | -7.57% | -10.95% | -6.81% | SELL_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_9 | 72.55 / 74.54 / 70.55 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.23% | `REALIZED_VOL_30D` | 352.17 | 2026-09-19 | 323.75 | 380.60 | L214 | L314, L414, L514, L013, L002 | MEDIUM | Industrials at 97.24 pctl; Tech_Z +1.2104 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| AMGN | Amgen Inc. Common Stock | 439.33 | 2026-08-21 | `DELAYED` | +0.2833 | (0.30x`UNAVL` + 0.30x+1.0351 + 0.25x`UNAVL` + 0.15x+0.2903) x 0.80 − 0.00 = +0.2833 | 97.05 | 0.1460 | 8.26% | 0.6888 | 2.3406 | 0.7172 | 2.1981 | -7.63% | -11.02% | -5.05% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 74.25 / 75.54 / 72.01 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.26% | `REALIZED_VOL_30D` | 465.69 | 2026-09-19 | 427.95 | 503.43 | L215 | L315, L415, L515, L013, L002 | MEDIUM | Health Care at 97.05 pctl; Tech_Z +1.0351 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| DXCM | DexCom Inc. Common Stock | 92.34 | 2026-08-21 | `DELAYED` | +0.2822 | (0.30x`UNAVL` + 0.30x+0.9044 + 0.25x`UNAVL` + 0.15x+0.5430) x 0.80 − 0.00 = +0.2822 | 96.85 | 0.4604 | 14.86% | 0.3829 | 0.9216 | 0.3965 | 0.6791 | -18.52% | -24.61% | -13.86% | SELL_SETUP_2 / SELL_SETUP_6 / SELL_SETUP_2 | 70.05 / 71.38 / 55.43 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 14.86% | `REALIZED_VOL_30D` | 97.88 | 2026-09-19 | 83.61 | 112.15 | L216 | L316, L416, L516, L013, L002 | MEDIUM | Health Care at 96.85 pctl; Tech_Z +0.9044 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| SYF | Synchrony Financial Common Stock | 79.47 | 2026-08-21 | `DELAYED` | +0.2791 | (0.30x`UNAVL` + 0.30x+0.7749 + 0.25x`UNAVL` + 0.15x+0.7762) x 0.80 − 0.00 = +0.2791 | 96.65 | 1.0828 | 7.76% | 0.7332 | 1.2076 | 0.4128 | 2.4907 | -6.80% | -9.99% | -13.22% | BUY_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_3 | 56.33 / 58.71 / 62.86 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 7.76% | `REALIZED_VOL_30D` | 84.24 | 2026-09-19 | 77.82 | 90.65 | L217 | L317, L417, L517, L013, L002 | MEDIUM | Finance at 96.65 pctl; Tech_Z +0.7749 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| APD | Air Products and Chemicals Inc. Co | 305.10 | 2026-08-21 | `DELAYED` | +0.2773 | (0.30x`UNAVL` + 0.30x+0.6149 + 0.25x`UNAVL` + 0.15x+1.0807) x 0.80 − 0.00 = +0.2773 | 96.46 | 0.1810 | 5.46% | 1.0430 | 1.6201 | 0.7048 | 5.0396 | -3.00% | -5.24% | -6.88% | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_8 | 55.79 / 58.60 / 57.52 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 5.46% | `REALIZED_VOL_30D` | 323.41 | 2026-09-19 | 306.09 | 340.72 | L218 | L318, L418, L518, L013, L002 | MEDIUM | Basic Materials at 96.46 pctl; Tech_Z +0.6149 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| ABT | Abbott Laboratories Common Stock | 116.64 | 2026-08-21 | `DELAYED` | +0.2695 | (0.30x`UNAVL` + 0.30x+1.1161 + 0.25x`UNAVL` + 0.15x+0.0139) x 0.80 − 0.00 = +0.2695 | 96.26 | -0.3849 | 10.78% | 0.5279 | 1.1475 | 0.7242 | 1.2911 | -11.79% | -16.20% | -7.18% | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_2 | 77.93 / 67.86 / 53.02 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 10.78% | `REALIZED_VOL_30D` | 123.64 | 2026-09-19 | 110.56 | 136.71 | L219 | L319, L419, L519, L013, L002 | MEDIUM | Health Care at 96.26 pctl; Tech_Z +1.1161 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |

## Score attribution — all 24 published names

`rules.md § Financial Metrics and Score Attribution` requires an `Adj Score` explanation for every
ranked **or monitored** name, so this table spans all 24 published names, not only the top 20
shown above.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BDX | `UNAVAILABLE` | +1.4253 | `UNAVAILABLE` | +0.3983 | +0.4873 | 0.80 | 0.00 | +0.3899 | `mom20` +1.9853; `sector_lead` +1.8692; `mom60` +1.7182 | `beta` -0.2056; `rate_sens` -0.1352; `vol_stability` +0.0646 | L300, L400, L013 |
| SCHW | `UNAVAILABLE` | +1.1643 | `UNAVAILABLE` | +0.7995 | +0.4692 | 0.80 | 0.00 | +0.3754 | `macd` +1.7859; `mom60` +1.7350; `vol_stability` +1.4896 | `beta` -0.1518; `vol_conf` +0.3892; `mom20` +0.6894 | L301, L401, L013 |
| AMP | `UNAVAILABLE` | +0.9245 | `UNAVAILABLE` | +1.1369 | +0.4479 | 0.80 | 0.00 | +0.3583 | `vol_stability` +1.7746; `vol_conf` +1.6739; `ma_align` +1.3489 | `macd` +0.0023; `mom20` +0.1559; `beta` +0.6185 | L302, L402, L013 |
| CRL | `UNAVAILABLE` | +1.3093 | `UNAVAILABLE` | +0.3603 | +0.4468 | 0.80 | 0.00 | +0.3575 | `mom20` +2.2104; `mom60` +2.1028; `sector_lead` +1.8692 | `rate_sens` -1.4946; `vol_stability` -0.0319; `vol_conf` +0.0588 | L303, L403, L013 |
| REGN | `UNAVAILABLE` | +1.1561 | `UNAVAILABLE` | +0.5710 | +0.4325 | 0.80 | 0.00 | +0.3460 | `mom20` +2.2104; `sector_lead` +1.8692; `mom60` +1.8375 | `vol_stability` -0.4040; `vol_conf` +0.2056; `rate_sens` +0.3456 | L304, L404, L013 |
| FCX | `UNAVAILABLE` | +1.2952 | `UNAVAILABLE` | +0.2598 | +0.4275 | 0.80 | 0.00 | +0.3420 | `vol_conf` +2.3420; `mom20` +1.9506; `sector_lead` +1.8692 | `beta` -0.6961; `dd60` -0.6340; `rate_sens` -0.4049 | L305, L405, L013 |
| RVTY | `UNAVAILABLE` | +1.3185 | `UNAVAILABLE` | +0.2107 | +0.4271 | 0.80 | 0.00 | +0.3417 | `vol_conf` +1.9309; `mom60` +1.5533; `ma_align` +1.3489 | `rate_sens` -0.4099; `sector_lead` -0.3985; `beta` +0.7757 | L306, L406, L013 |
| TGT | `UNAVAILABLE` | +1.4029 | `UNAVAILABLE` | +0.0173 | +0.4235 | 0.80 | 0.00 | +0.3388 | `vol_conf` +1.9309; `mom20` +1.8897; `mom60` +1.6193 | `rate_sens` -0.9781; `sector_lead` -0.0481; `beta` +0.0057 | L307, L407, L013 |
| NEM | `UNAVAILABLE` | +1.2021 | `UNAVAILABLE` | +0.3731 | +0.4166 | 0.80 | 0.00 | +0.3333 | `mom20` +2.2104; `sector_lead` +1.8692; `vol_conf` +1.8575 | `dd60` -0.5099; `rate_sens` -0.4622; `vol_stability` -0.1970 | L308, L408, L013 |
| TECH | `UNAVAILABLE` | +0.8182 | `UNAVAILABLE` | +1.0844 | +0.4081 | 0.80 | 0.00 | +0.3265 | `mom60` +2.1028; `vol_stability` +1.9033; `sector_lead` +1.8692 | `rate_sens` -0.7915; `mom20` -0.3020; `macd` +0.0023 | L309, L409, L013 |
| LH | `UNAVAILABLE` | +1.1779 | `UNAVAILABLE` | +0.2590 | +0.3922 | 0.80 | 0.00 | +0.3138 | `sector_lead` +1.8692; `mom60` +1.6677; `ma_align` +1.3489 | `vol_stability` -0.6132; `beta` -0.1616; `rate_sens` -0.0585 | L310, L410, L013 |
| MRK | `UNAVAILABLE` | +1.4270 | `UNAVAILABLE` | -0.2595 | +0.3892 | 0.80 | 0.00 | +0.3113 | `vol_conf` +2.3420; `sector_lead` +1.8692; `mom60` +1.4698 | `vol_stability` -1.2614; `rate_sens` -1.1257; `beta` -0.5201 | L311, L411, L013 |
| RJF | `UNAVAILABLE` | +0.7866 | `UNAVAILABLE` | +0.9553 | +0.3793 | 0.80 | 0.00 | +0.3034 | `vol_conf` +2.3420; `vol_stability` +1.2270; `rate_sens` +1.1887 | `mom20` -0.0426; `macd` +0.0023; `beta` +0.4397 | L312, L412, L013 |
| DE | `UNAVAILABLE` | +1.1842 | `UNAVAILABLE` | +0.0866 | +0.3682 | 0.80 | 0.00 | +0.2946 | `vol_conf` +2.3420; `macd` +1.7859; `ma_align` +1.3489 | `sector_lead` -0.3985; `rate_sens` -0.2153; `vol_stability` -0.1840 | L313, L413, L013 |
| NDSN | `UNAVAILABLE` | +1.2104 | `UNAVAILABLE` | +0.0310 | +0.3678 | 0.80 | 0.00 | +0.2942 | `vol_conf` +2.3420; `ma_align` +1.3489; `beta` +1.2915 | `vol_stability` -0.4713; `sector_lead` -0.3985; `rate_sens` -0.2978 | L314, L414, L013 |
| AMGN | `UNAVAILABLE` | +1.0351 | `UNAVAILABLE` | +0.2903 | +0.3541 | 0.80 | 0.00 | +0.2833 | `sector_lead` +1.8692; `mom60` +1.7301; `mom20` +1.4308 | `vol_stability` -0.5418; `vol_conf` -0.5285; `rate_sens` -0.4080 | L315, L415, L013 |
| DXCM | `UNAVAILABLE` | +0.9044 | `UNAVAILABLE` | +0.5430 | +0.3528 | 0.80 | 0.00 | +0.2822 | `mom20` +2.2104; `sector_lead` +1.8692; `mom60` +1.7259 | `vol_stability` -1.5275; `vol_conf` -1.1158; `dd60` +0.0654 | L316, L416, L013 |
| SYF | `UNAVAILABLE` | +0.7749 | `UNAVAILABLE` | +0.7762 | +0.3489 | 0.80 | 0.00 | +0.2791 | `vol_conf` +2.2980; `vol_stability` +1.8797; `beta` +1.6296 | `rate_sens` -1.3703; `macd` +0.0023; `dd60` +0.1408 | L317, L417, L013 |
| APD | `UNAVAILABLE` | +0.6149 | `UNAVAILABLE` | +1.0807 | +0.3466 | 0.80 | 0.00 | +0.2773 | `vol_stability` +1.9033; `sector_lead` +1.8692; `vol_conf` +1.5638 | `mom20` -0.1529; `macd` +0.0023; `mom60` +0.0426 | L318, L418, L013 |
| ABT | `UNAVAILABLE` | +1.1161 | `UNAVAILABLE` | +0.0139 | +0.3369 | 0.80 | 0.00 | +0.2695 | `mom60` +2.1028; `sector_lead` +1.8692; `macd` +1.1914 | `vol_stability` -1.4350; `beta` -0.7471; `rate_sens` +0.3685 | L319, L419, L013 |
| MPC | `UNAVAILABLE` | +1.1046 | `UNAVAILABLE` | -0.0097 | +0.3299 | 0.80 | 0.00 | +0.2639 | `mom60` +2.1028; `mom20` +1.3741; `ma_align` +1.3489 | `vol_stability` -0.7853; `beta` -0.3225; `rate_sens` -0.1103 | L320, L420, L013 |
| VLO | `UNAVAILABLE` | +0.9999 | `UNAVAILABLE` | +0.1911 | +0.3286 | 0.80 | 0.00 | +0.2629 | `mom60` +2.1028; `ma_align` +1.3489; `mom20` +1.2480 | `vol_conf` -0.4551; `beta` -0.3749; `vol_stability` -0.0332 | L321, L421, L013 |
| PSX | `UNAVAILABLE` | +1.1361 | `UNAVAILABLE` | -0.1009 | +0.3257 | 0.80 | 0.00 | +0.2606 | `mom60` +2.1028; `mom20` +1.4906; `ma_align` +1.3489 | `beta` -0.7367; `vol_stability` -0.6334; `rate_sens` -0.2131 | L322, L422, L013 |
| PFE | `UNAVAILABLE` | +0.7343 | `UNAVAILABLE` | +0.6744 | +0.3215 | 0.80 | 0.00 | +0.2572 | `sector_lead` +1.8692; `ma_align` +1.3489; `macd` +1.1914 | `beta` -0.0387; `vol_conf` +0.0588; `mom60` +0.1500 | L323, L423, L013 |

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical (momentum, MA alignment, MACD, volume, drawdown) | 509/509 | 0 | none — full coverage | all six `Tech_Z` slots sourceable universe-wide |
| Macro (beta, sector leadership, rate sensitivity, vol stability) | 509/509 | 0 | none — full coverage | all four `Macro_Z` slots sourceable universe-wide |
| Risk / return ratios (Sharpe, Sortino, IR, Treynor, Calmar) | 509/509 | 0 | none | displayed; only `dd60` enters a score slot |
| Tail risk (VaR95, CVaR95, 60d max drawdown) | 509/509 | 0 | none | `dd60` is a `Tech_Z` slot |
| Sizing (raw Kelly, 0.25x Kelly) | 509/509 | 0 | none | investability gate |
| TD-9 / RSI(14) — daily & weekly | 509/509 | 0 | none | exhaustion flags; not score slots |
| Fundamental family | 0 | 509 | **DQ 1.00 → 0.80**; blocks evidence threshold #2 | `Fund_Z` `UNAVAILABLE` — no fetch path wired (rules.md § SHADOW Diagnostic Tooling) |
| Sentiment / positioning family | 0 | 509 | **DQ 1.00 → 0.80**; blocks evidence threshold #2 | `Sent_Z` `UNAVAILABLE` — no fetch path wired |
| Options IV / skew, short interest, bid-ask tape, analyst revisions | 0 | 509 | confidence capped `MEDIUM` | **Enhancing** inputs — never `GO` blockers |

No score below cites a metric absent from `01_preflight.md`, and no missing metric is described as
neutral or supportive: `Fund_Z` and `Sent_Z` are carried as `UNAVAILABLE` and contribute
`0.00 (UNAVAILABLE)` to the arithmetic, which is a **penalty via the data-quality multiplier**, not a
neutral pass.

## Technical indicator summary — all 24 published names

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60d Mom | RS20/60 vs SPY | Vol Ratio 20d | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|
| BDX | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 78.53 / 72.66 / 61.51 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.7794 / +4.3598 / +4.1748 | BULLISH / BULLISH / MIXED | +22.79% / +31.32% | +19.16% / +29.03% | 1.31 | L400, L013, L002 |
| SCHW | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 71.12 / 73.08 / 68.81 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | +0.0105 / +2.2373 / +0.6924 | BULLISH / BULLISH / BULLISH | +10.45% / +31.56% | +6.82% / +29.27% | 1.01 | L401, L013, L002 |
| AMP | BUY_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 57.90 / 68.16 / 61.86 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -3.3528 / +11.4319 / -0.1385 | BULLISH / BULLISH / BULLISH | +5.37% / +25.76% | +1.74% / +23.47% | 1.36 | L402, L013, L002 |
| CRL | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_3 | 76.28 / 77.10 / 66.91 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.5071 / +10.4267 / +13.9480 | BULLISH / BULLISH / MIXED | +30.28% / +79.46% | +26.65% / +77.17% | 0.92 | L403, L013, L002 |
| REGN | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_1 | 76.55 / 68.32 / 57.15 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.2627 / +20.0502 / +16.2456 | BULLISH / MIXED / MIXED | +27.29% / +33.02% | +23.66% / +30.73% | 0.96 | L404, L013, L002 |
| FCX | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 69.30 / 64.83 / 69.94 | `ABOVE_SIGNAL` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | +0.6250 / +0.5144 / +2.4317 | BULLISH / BULLISH / BULLISH | +22.46% / +20.77% | +18.83% / +18.48% | 2.15 | L405, L013, L002 |
| RVTY | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_3 | 68.62 / 68.88 / 58.41 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.6939 / +1.9999 / +3.8738 | BULLISH / BULLISH / MIXED | +12.93% / +28.97% | +9.30% / +26.68% | 1.43 | L406, L013, L002 |
| TGT | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_9 | 76.54 / 75.41 / 70.32 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.8990 / +2.4224 / +8.1999 | BULLISH / BULLISH / MIXED | +21.88% / +29.91% | +18.25% / +27.62% | 1.43 | L407, L013, L002 |
| NEM | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_1 | 75.93 / 65.61 / 70.66 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.1894 / +2.0209 / +2.0829 | BULLISH / BULLISH / BULLISH | +41.20% / +22.71% | +37.57% / +20.42% | 1.41 | L408, L013, L002 |
| TECH | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 67.74 / 65.68 / 55.35 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.3242 / +1.5740 / +2.5306 | BULLISH / BULLISH / MIXED | +1.01% / +50.38% | -2.62% / +48.09% | 1.10 | L409, L013, L002 |
| LH | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 75.74 / 74.08 / 68.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.4172 / +7.0653 / +4.8321 | BULLISH / BULLISH / BULLISH | +13.33% / +30.60% | +9.70% / +28.31% | 1.15 | L410, L013, L002 |
| MRK | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_9 | 77.91 / 75.08 / 75.15 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.0915 / +1.8325 / +5.5300 | BULLISH / BULLISH / BULLISH | +16.39% / +27.78% | +12.76% / +25.49% | 1.59 | L411, L013, L002 |
| RJF | BUY_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 51.45 / 62.55 / 61.20 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -1.2202 / +2.8163 / -0.2424 | MIXED / BULLISH / BULLISH | +3.48% / +20.92% | -0.15% / +18.63% | 1.73 | L412, L013, L002 |
| DE | SELL_SETUP_2 / SELL_SETUP_3 / SELL_SETUP_8 | 62.38 / 61.38 / 64.38 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.0687 / +2.3522 / +10.7266 | BULLISH / BULLISH / BULLISH | +3.07% / +22.62% | -0.56% / +20.33% | 2.03 | L413, L013, L002 |
| NDSN | SELL_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_9 | 72.55 / 74.54 / 70.55 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.9961 / +2.2660 / +9.2175 | BULLISH / BULLISH / BULLISH | +12.33% / +15.39% | +8.70% / +13.10% | 1.74 | L414, L013, L002 |
| AMGN | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 74.25 / 75.54 / 72.01 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.2374 / +7.9205 / +8.9032 | BULLISH / BULLISH / BULLISH | +17.51% / +31.49% | +13.88% / +29.20% | 0.76 | L415, L013, L002 |
| DXCM | SELL_SETUP_2 / SELL_SETUP_6 / SELL_SETUP_2 | 70.05 / 71.38 / 55.43 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.1875 / +2.3901 / +3.3094 | BULLISH / BULLISH / MIXED | +29.07% / +31.43% | +25.44% / +29.14% | 0.60 | L416, L013, L002 |
| SYF | BUY_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_3 | 56.33 / 58.71 / 62.86 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -0.1299 / +0.7426 / -0.3088 | BULLISH / BULLISH / BULLISH | +9.48% / +10.71% | +5.85% / +8.42% | 1.53 | L417, L013, L002 |
| APD | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_8 | 55.79 / 58.60 / 57.52 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2253 / +0.9963 / +2.8964 | BULLISH / BULLISH / BULLISH | +2.43% / +7.44% | -1.20% / +5.15% | 1.33 | L418, L013, L002 |
| ABT | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_2 | 77.93 / 67.86 / 53.02 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.2503 / +3.8468 / -2.1415 | BULLISH / MIXED / MIXED | +13.18% / +37.11% | +9.55% / +34.82% | 1.21 | L419, L013, L002 |
| MPC | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_7 | 72.22 / 76.27 / 84.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.4712 / +7.8793 / +15.7371 | BULLISH / BULLISH / BULLISH | +16.97% / +46.41% | +13.34% / +44.12% | 0.90 | L420, L013, L002 |
| VLO | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 70.67 / 75.52 / 85.84 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.6033 / +6.4725 / +16.9472 | BULLISH / BULLISH / BULLISH | +15.77% / +45.71% | +12.14% / +43.42% | 0.78 | L421, L013, L002 |
| PSX | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_8 | 77.37 / 76.38 / 79.98 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.0097 / +5.0968 / +9.2259 | BULLISH / BULLISH / BULLISH | +18.08% / +39.82% | +14.45% / +37.53% | 0.95 | L422, L013, L002 |
| PFE | SELL_SETUP_5 / SELL_SETUP_5 / SELL_SETUP_1 | 71.77 / 67.21 / 58.36 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.1663 / +0.2541 / +0.5627 | BULLISH / BULLISH / MIXED | +14.38% / +8.97% | +10.75% / +6.68% | 0.92 | L423, L013, L002 |

TD-9 setup `9` readings and RSI ≥ 70 / ≤ 30 are treated as exhaustion or reversal flags that inform
confidence, never as standalone trade signals (`rules.md § TD-9 Definition`). MACD is read as
supportive only where it aligns with 20d/60d momentum and relative strength.

## Investable determination

| Evidence threshold | Requirement | Best attainable | Pass |
|---|---|---|---|
| 1. Percentile rank | >= 80th | 100.00 | **Yes** |
| 2. Families non-negative | >= 3 of 4 | 2 of 4 (Technical, Macro) | **No** |
| 3. Single-family conviction share | <= 50% | 66.7% (Technical) | **No** |
| 4. Data completeness | >= 85% | 80% | **No** |
| 5. No hard stop | none | none triggered | **Yes** |

**Investable set: 0 names. Monitoring sleeve: 24 names.** Every published name carries a
settleable `mu` (the calibration-table band for its percentile) and `sigma` (from
`REALIZED_VOL_30D`), so all 24 produce auditable prediction records in `15` — a monitoring
sleeve without `mu`/`sigma` would be a publishing failure, not caution.

**Penalties applied: 0 of 24 published names.** The
forward earnings sweep is complete and every published name reads `NO_PRINT_IN_WINDOW` through
2026-09-28, so no name takes the −0.10 earnings penalty and none is
confidence-capped at `LOW` on event risk. All 24 are capped `MEDIUM` by the rank-IC binding.

Because the sweep grounded the entire universe, the published set is **ranks 1–24 contiguous**
— there are no ungrounded names to skip, so the "first N grounded, skip ungrounded" rule that applied
on 2026-07-27 and 2026-07-28 does not engage.

## What drives the leaderboard

With two families live, the composite reduces to `0.30*Tech_Z + 0.15*Macro_Z`, so **Technical carries
66.7% of conviction and Macro 33.3%** — threshold #3 fails by
construction, not by accident. Within `Tech_Z` the six slots are equal-weighted, so momentum (20d +
60d) occupies 2 of 6 slots = 33.3% of `Tech_Z`.

The board is led by **`BDX`** (`Tech_Z` +1.4253, `Macro_Z`
+0.3983, 20d/60d momentum +22.79%/+31.32%). Sector
composition of the published 24: Health Care 10, Finance 4, Basic Materials 3, Industrials 3, Energy 3, Consumer Discretionary 1.

That composition is the run's central finding and its central weakness. Published-sleeve betas span
-0.3849 to 2.3576 with a mean of 0.3529 — a defensive, low-beta book
selected by a trend-persistence score in a tape that just re-established a `BULL` trend. Two
consequences follow, and both are computed rather than asserted:

1. **The beta band is structurally infeasible.** Under the 5% single-name cap a sleeve needs ≥ 20
   names, so the maximum attainable sleeve beta is the mean of the 20 highest betas in the pool:
   **0.4841**, against a 0.90 floor. No weighting of
   this pool reaches the band. This is the first run since 2026-07-27 where that is true — the four
   intervening runs were all feasible, so it was recomputed rather than assumed.
2. **The prior book built the same way lost 2.59pp of alpha** over the settled window
   (`02 § 2`), and 2 of today's
   24 published names also appeared in it. The score is reported as computed; the calibration
   evidence against it is reported next to it rather than after the fact.

The honest reading is that `Tech_Z` is trend-persistence by construction and, with `Fund_Z` and
`Sent_Z` dark, it is the whole model. That is a known structural defect under active diagnosis
(rank-order inversion, documented since 2026-07-22), and it is not fixable by any change this run is
permitted to make: the family weights are protected, and a mu-table or weighting change is Track A,
gated at `eff_n = 2 < 3`.
