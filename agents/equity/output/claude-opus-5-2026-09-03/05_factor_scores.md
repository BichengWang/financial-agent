# 05 — Factor Scores · 2026-09-03

Universe `INDEX_UNION_PCTL (n=508)` · DQ multiplier 0.80 (`L020`) ·
risk-free 3.75% annual (`L008`) · basis 2026-09-03.

`Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`.
`Fund_Z` and `Sent_Z` contribute **`0.00 (UNAVAILABLE)`** to that arithmetic (`L021`, `L022`);
that is a penalty expressed through the data-quality multiplier, not a neutral assumption, and
those families do **not** count toward the 3-of-4 evidence threshold.

## Metric Definition Table (normative)

Carried forward unchanged from the Track B change accepted in
`claude-opus-5-2026-08-03/13_evolution_log.md` and first shipped 2026-08-04. This table is
**normative**: if it and the running code disagree, one of them is wrong and the run must say
which. Polarity is stated as the **post-transform direction**, never as an instruction word like
"negated", so a reader can answer "does a larger raw value help or hurt?" without knowing the sign
convention of the stored field.

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

### Derived ratio definitions used in the tables below

| Metric | Formula | Inputs |
|---|---|---|
| Forecast Sharpe | `(mu - rf_1m) / sigma` | mu from the calibration table; sigma = `REALIZED_VOL_30D`; `rf_1m` = L008 annual / 12 = 0.003125 |
| Sortino | `(mu - rf_1m) / downside_sigma_1m` | `downside_sigma_1m` = pstdev of the **negative** daily adjusted returns in the trailing 30 sessions x `sqrt(21)` |
| Information Ratio | `(mu - beta x SPY_mu) / tracking_error_1m` | `SPY_mu` = +2.0% regime prior (`03`); `tracking_error_1m` = pstdev(r - beta x r_SPY) over 60 daily intervals x `sqrt(21)` |
| Treynor | `(mu - rf_1m) / beta` | beta from the 60d regression (L500-series) |
| Calmar-style | `(mu - rf_1m) / abs(max_drawdown_60d)` | diagnostic and negative-risk screen only |
| VaR95 / CVaR95 | `mu - 1.65 x sigma` / `mu - 2.06 x sigma` | one-month return space; normality assumed and stated |
| Raw Kelly / 0.25x Kelly | `mu / sigma^2` / `0.25 x raw` | documented fallback form (no beta-adjusted edge / tracking-error variance wired); bounded by the 5% single-name cap |

## Calibration feedback binding (read before scoring)

From `02 § 0` / `L014a`: `EQUITY_ALPHA` CI coverage **71.74%** is inside the
55-85% band, so the "widen sigma" binding does **not** fire and `REALIZED_VOL_30D` stands as the
sigma source. Aggregate rank IC across scored vintages is negative (mean
**-0.0659** over 73 vintages), which triggers the `rules.md` binding:
**all confidence is capped at `MEDIUM`**. No positive per-name mu adjustments were applied — every
`mu` below is the unmodified calibration-table band value for the name's percentile.

## Ranked candidate table (top 20)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VLO | Valero Energy Corporation Common S | 370.69 | 2026-09-03 | `DELAYED` | +0.3727 | (0.30x`UNAVL` + 0.30x+1.4152 + 0.25x`UNAVL` + 0.15x+0.2756) x 0.80 - 0.00 = +0.3727 | 100.00 | -0.3804 | 8.44% | +0.6742 | +2.2165 | +0.6754 | +2.1080 | -7.92% | -11.38% | -8.65% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 75.26 / 78.49 / 87.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.44% | `REALIZED_VOL_30D` | 392.93 | 2026-10-01 | 360.41 | 425.45 | L200 | L300, L400, L500, L600, L013, L002 | MEDIUM | Energy at the 100.00th pctl; Tech_Z +1.4152 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| SPGI | S&P Global Inc. Common Stock | 450.58 | 2026-09-03 | `DELAYED` | +0.3607 | (0.30x`UNAVL` + 0.30x+1.0592 + 0.25x`UNAVL` + 0.15x+0.8874) x 0.80 - 0.00 = +0.3607 | 99.80 | +0.0145 | 7.75% | +0.7338 | +1.5128 | +0.6046 | +2.4969 | -6.79% | -9.97% | -11.40% | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_3 | 63.17 / 57.77 / 52.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 7.75% | `REALIZED_VOL_30D` | 477.61 | 2026-10-01 | 441.29 | 513.93 | L201 | L301, L401, L501, L601, L013, L002 | MEDIUM | Finance at the 99.80th pctl; Tech_Z +1.0592 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| PFG | Principal Financial Group Inc Comm | 118.51 | 2026-09-03 | `DELAYED` | +0.3554 | (0.30x`UNAVL` + 0.30x+1.2136 + 0.25x`UNAVL` + 0.15x+0.5348) x 0.80 - 0.00 = +0.3554 | 99.61 | +0.2053 | 7.54% | +0.7541 | +2.8105 | +0.7718 | +2.6369 | -6.44% | -9.54% | -6.16% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_9 | 68.60 / 70.87 / 74.48 | `BULLISH_CROSS` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 7.54% | `REALIZED_VOL_30D` | 125.62 | 2026-10-01 | 116.32 | 134.92 | L202 | L302, L402, L502, L602, L013, L002 | MEDIUM | Finance at the 99.61th pctl; Tech_Z +1.2136 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| GILD | Gilead Sciences Inc. Common Stock | 151.19 | 2026-09-03 | `DELAYED` | +0.3390 | (0.30x`UNAVL` + 0.30x+1.1288 + 0.25x`UNAVL` + 0.15x+0.5676) x 0.80 - 0.00 = +0.3390 | 99.41 | +0.0885 | 7.45% | +0.7631 | +1.4078 | +0.6767 | +2.7005 | -6.30% | -9.35% | -5.17% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 68.29 / 68.28 / 71.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 7.45% | `REALIZED_VOL_30D` | 160.26 | 2026-10-01 | 148.54 | 171.98 | L203 | L303, L403, L503, L603, L013, L002 | MEDIUM | Health Care at the 99.41th pctl; Tech_Z +1.1288 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| AMP | Ameriprise Financial Inc. Common S | 565.08 | 2026-09-03 | `DELAYED` | +0.3354 | (0.30x`UNAVL` + 0.30x+0.8574 + 0.25x`UNAVL` + 0.15x+1.0804) x 0.80 - 0.00 = +0.3354 | 99.21 | +0.4205 | 5.43% | +1.0475 | +1.8228 | +0.7892 | +5.0880 | -2.96% | -5.19% | -5.34% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.50 / 69.99 / 62.87 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | +6.00% | 5.43% | `REALIZED_VOL_30D` | 598.98 | 2026-10-01 | 567.08 | 630.89 | L204 | L304, L404, L504, L604, L013, L002 | MEDIUM | Finance at the 99.21th pctl; Tech_Z +0.8574 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| IQV | IQVIA Holdings Inc. Common Stock | 271.62 | 2026-09-03 | `DELAYED` | +0.3349 | (0.30x`UNAVL` + 0.30x+1.4310 + 0.25x`UNAVL` + 0.15x-0.0713) x 0.80 - 0.00 = +0.3349 | 99.01 | -0.3776 | 13.80% | +0.4121 | +1.1924 | +0.5338 | +0.7874 | -16.77% | -22.43% | -9.92% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_4 | 75.17 / 75.13 / 63.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 13.80% | `REALIZED_VOL_30D` | 287.92 | 2026-10-01 | 248.93 | 326.91 | L205 | L305, L405, L505, L605, L013, L002 | MEDIUM | Health Care at the 99.01th pctl; Tech_Z +1.4310 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| RVTY | Revvity Inc. Common Stock | 130.63 | 2026-09-03 | `DELAYED` | +0.3329 | (0.30x`UNAVL` + 0.30x+1.3888 + 0.25x`UNAVL` + 0.15x-0.0035) x 0.80 - 0.00 = +0.3329 | 98.82 | +0.3067 | 9.28% | +0.6126 | +1.3308 | +0.5309 | +1.7404 | -9.32% | -13.12% | -6.38% | SELL_SETUP_9 / SELL_SETUP_5 / SELL_SETUP_4 | 68.62 / 72.12 / 60.61 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 9.28% | `REALIZED_VOL_30D` | 138.47 | 2026-10-01 | 125.86 | 151.08 | L206 | L306, L406, L506, L606, L013, L002 | MEDIUM | Industrials at the 98.82th pctl; Tech_Z +1.3888 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| TECH | Bio-Techne Corp Common Stock | 72.45 | 2026-09-03 | `DELAYED` | +0.3192 | (0.30x`UNAVL` + 0.30x+0.7951 + 0.25x`UNAVL` + 0.15x+1.0699) x 0.80 - 0.00 = +0.3192 | 98.62 | +0.6375 | 0.99% | +5.7278 | +15.4694 | +0.3635 | +152.1345 | +4.36% | +3.95% | -4.02% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 66.10 / 65.94 / 55.46 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 0.99% | `REALIZED_VOL_30D` | 76.80 | 2026-10-01 | 76.05 | 77.55 | L207 | L307, L407, L507, L607, L013, L002 | MEDIUM | Health Care at the 98.62th pctl; Tech_Z +0.7951 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| PSX | Phillips 66 Common Stock | 254.66 | 2026-09-03 | `DELAYED` | +0.3190 | (0.30x`UNAVL` + 0.30x+1.3457 + 0.25x`UNAVL` + 0.15x-0.0329) x 0.80 - 0.00 = +0.3190 | 98.42 | -0.6267 | 8.27% | +0.6876 | +1.6811 | +0.8271 | +2.1924 | -7.65% | -11.04% | -8.57% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 74.81 / 78.77 / 81.33 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.27% | `REALIZED_VOL_30D` | 269.94 | 2026-10-01 | 248.03 | 291.85 | L208 | L308, L408, L508, L608, L013, L002 | MEDIUM | Energy at the 98.42th pctl; Tech_Z +1.3457 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| STT | State Street Corporation Common St | 193.94 | 2026-09-03 | `DELAYED` | +0.3157 | (0.30x`UNAVL` + 0.30x+0.9025 + 0.25x`UNAVL` + 0.15x+0.8260) x 0.80 - 0.00 = +0.3157 | 98.22 | +0.7401 | 7.01% | +0.8115 | +1.1424 | +0.7057 | +3.0534 | -5.56% | -8.44% | -5.65% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.03 / 82.05 / 88.94 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 7.01% | `REALIZED_VOL_30D` | 205.58 | 2026-10-01 | 191.44 | 219.71 | L209 | L309, L409, L509, L609, L013, L002 | MEDIUM | Finance at the 98.22th pctl; Tech_Z +0.9025 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| GEN | Gen Digital Inc. Common Stock | 31.33 | 2026-09-03 | `DELAYED` | +0.3148 | (0.30x`UNAVL` + 0.30x+1.2613 + 0.25x`UNAVL` + 0.15x+0.1009) x 0.80 - 0.00 = +0.3148 | 98.03 | +0.4304 | 9.25% | +0.6150 | +0.9782 | +0.5329 | +1.7541 | -9.26% | -13.05% | -7.85% | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_5 | 67.86 / 69.20 / 62.25 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 9.25% | `REALIZED_VOL_30D` | 33.21 | 2026-10-01 | 30.20 | 36.22 | L210 | L310, L410, L510, L610, L013, L002 | MEDIUM | Technology at the 98.03th pctl; Tech_Z +1.2613 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| ICE | Intercontinental Exchange Inc. Com | 164.59 | 2026-09-03 | `DELAYED` | +0.3113 | (0.30x`UNAVL` + 0.30x+0.8835 + 0.25x`UNAVL` + 0.15x+0.8271) x 0.80 - 0.00 = +0.3113 | 97.83 | -0.0545 | 6.24% | +0.9113 | +1.8546 | +0.7777 | +3.8510 | -4.30% | -6.86% | -13.00% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 68.48 / 61.15 / 54.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 6.24% | `REALIZED_VOL_30D` | 174.47 | 2026-10-01 | 163.78 | 185.15 | L211 | L311, L411, L511, L611, L013, L002 | MEDIUM | Finance at the 97.83th pctl; Tech_Z +0.8835 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| BNY | The Bank of New York Mellon Corpor | 164.33 | 2026-09-03 | `DELAYED` | +0.3027 | (0.30x`UNAVL` + 0.30x+0.7190 + 0.25x`UNAVL` + 0.15x+1.0849) x 0.80 - 0.00 = +0.3027 | 97.63 | +0.5101 | 5.32% | +1.0692 | +1.6136 | +0.7909 | +5.3014 | -2.78% | -4.96% | -5.69% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.86 / 77.20 / 91.64 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 5.32% | `REALIZED_VOL_30D` | 174.19 | 2026-10-01 | 165.10 | 183.28 | L212 | L312, L412, L512, L612, L013, L002 | MEDIUM | Finance at the 97.63th pctl; Tech_Z +0.7190 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| DE | Deere & Company Common Stock | 694.41 | 2026-09-03 | `DELAYED` | +0.2997 | (0.30x`UNAVL` + 0.30x+1.3196 + 0.25x`UNAVL` + 0.15x-0.1415) x 0.80 - 0.00 = +0.2997 | 97.44 | +0.4694 | 11.08% | +0.5135 | +1.2207 | +0.5087 | +1.2229 | -12.27% | -16.81% | -9.25% | SELL_SETUP_4 / SELL_SETUP_5 / SELL_SETUP_9 | 68.67 / 65.74 / 67.59 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 11.08% | `REALIZED_VOL_30D` | 736.07 | 2026-10-01 | 656.09 | 816.06 | L213 | L313, L413, L513, L613, L013, L002 | MEDIUM | Industrials at the 97.44th pctl; Tech_Z +1.3196 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| JNJ | Johnson & Johnson Common Stock | 278.43 | 2026-09-03 | `DELAYED` | +0.2946 | (0.30x`UNAVL` + 0.30x+0.9583 + 0.25x`UNAVL` + 0.15x+0.5388) x 0.80 - 0.00 = +0.2946 | 97.24 | -0.7306 | 6.07% | +0.9372 | +1.2736 | +1.1075 | +4.0734 | -4.01% | -6.50% | -7.57% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_9 | 65.95 / 69.40 / 79.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 6.07% | `REALIZED_VOL_30D` | 295.14 | 2026-10-01 | 277.56 | 312.71 | L214 | L314, L414, L514, L614, L013, L002 | MEDIUM | Health Care at the 97.24th pctl; Tech_Z +0.9583 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| VRTX | Vertex Pharmaceuticals Incorporate | 557.96 | 2026-09-03 | `DELAYED` | +0.2822 | (0.30x`UNAVL` + 0.30x+0.9749 + 0.25x`UNAVL` + 0.15x+0.4020) x 0.80 - 0.00 = +0.2822 | 97.04 | +0.1882 | 8.22% | +0.6919 | +1.8707 | +0.6570 | +2.2198 | -7.56% | -10.93% | -11.12% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_3 | 67.51 / 69.51 / 64.46 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.22% | `REALIZED_VOL_30D` | 591.44 | 2026-10-01 | 543.74 | 639.14 | L215 | L315, L415, L515, L615, L013, L002 | MEDIUM | Health Care at the 97.04th pctl; Tech_Z +0.9749 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| MPC | Marathon Petroleum Corporation Com | 387.71 | 2026-09-03 | `DELAYED` | +0.2800 | (0.30x`UNAVL` + 0.30x+1.2621 + 0.25x`UNAVL` + 0.15x-0.1906) x 0.80 - 0.00 = +0.2800 | 96.84 | -0.4642 | 10.42% | +0.5458 | +0.9064 | +0.7050 | +1.3813 | -11.19% | -15.47% | -7.84% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_8 | 77.86 / 79.52 / 86.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 10.42% | `REALIZED_VOL_30D` | 410.97 | 2026-10-01 | 368.95 | 452.99 | L216 | L316, L416, L516, L616, L013, L002 | MEDIUM | Energy at the 96.84th pctl; Tech_Z +1.2621 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| WFC | Wells Fargo & Company Common Stock | 89.19 | 2026-09-03 | `DELAYED` | +0.2688 | (0.30x`UNAVL` + 0.30x+0.7511 + 0.25x`UNAVL` + 0.15x+0.7379) x 0.80 - 0.00 = +0.2688 | 96.65 | +0.4222 | 6.13% | +0.9274 | +1.1794 | +0.8075 | +3.9883 | -4.12% | -6.63% | -5.88% | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_4 | 61.84 / 58.56 / 65.31 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 6.13% | `REALIZED_VOL_30D` | 94.54 | 2026-10-01 | 88.85 | 100.23 | L217 | L317, L417, L517, L617, L013, L002 | MEDIUM | Finance at the 96.65th pctl; Tech_Z +0.7511 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| ELV | Elevance Health Inc. Common Stock | 414.78 | 2026-09-03 | `DELAYED` | +0.2675 | (0.30x`UNAVL` + 0.30x+0.6114 + 0.25x`UNAVL` + 0.15x+1.0062) x 0.80 - 0.00 = +0.2675 | 96.45 | +0.1601 | 6.68% | +0.8517 | +1.5684 | +0.5512 | +3.3635 | -5.02% | -7.76% | -12.64% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_6 | 62.76 / 61.87 / 55.81 | `ABOVE_SIGNAL` / `BELOW_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 6.68% | `REALIZED_VOL_30D` | 439.67 | 2026-10-01 | 410.86 | 468.47 | L218 | L318, L418, L518, L618, L013, L002 | MEDIUM | Health Care at the 96.45th pctl; Tech_Z +0.6114 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| RJF | Raymond James Financial Inc. Commo | 181.10 | 2026-09-03 | `DELAYED` | +0.2628 | (0.30x`UNAVL` + 0.30x+0.7020 + 0.25x`UNAVL` + 0.15x+0.7863) x 0.80 - 0.00 = +0.2628 | 96.25 | +0.4144 | 6.56% | +0.8671 | +1.3379 | +0.7735 | +3.4868 | -4.82% | -7.51% | -6.10% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.09 / 66.38 / 63.10 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | +6.00% | 6.56% | `REALIZED_VOL_30D` | 191.97 | 2026-10-01 | 179.61 | 204.32 | L219 | L319, L419, L519, L619, L013, L002 | MEDIUM | Finance at the 96.25th pctl; Tech_Z +0.7020 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |

## Ranks 21-24 (published monitoring sleeve, same schema)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | Dell Technologies Inc. Class C Com | 516.39 | 2026-09-03 | `DELAYED` | +0.2605 | (0.30x`UNAVL` + 0.30x+1.4805 + 0.25x`UNAVL` + 0.15x-0.7900) x 0.80 - 0.00 = +0.2605 | 96.06 | +2.7270 | 24.80% | +0.2294 | +0.4970 | +0.0271 | +0.2440 | -34.91% | -45.08% | -19.09% | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_7 | 62.55 / 71.51 / 85.88 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 24.80% | `REALIZED_VOL_30D` | 547.37 | 2026-10-01 | 414.21 | 680.53 | L220 | L320, L420, L520, L620, L013, L002 | MEDIUM | Technology at the 96.06th pctl; Tech_Z +1.4805 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| BIIB | Biogen Inc. Common Stock | 224.51 | 2026-09-03 | `DELAYED` | +0.2558 | (0.30x`UNAVL` + 0.30x+0.7022 + 0.25x`UNAVL` + 0.15x+0.7276) x 0.80 - 0.00 = +0.2558 | 95.86 | +0.0234 | 7.62% | +0.7462 | +1.4498 | +0.5327 | +2.5817 | -6.58% | -9.70% | -11.39% | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.50 / 68.75 / 61.91 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 7.62% | `REALIZED_VOL_30D` | 237.98 | 2026-10-01 | 220.18 | 255.78 | L221 | L321, L421, L521, L621, L013, L002 | MEDIUM | Health Care at the 95.86th pctl; Tech_Z +0.7022 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| PRU | Prudential Financial Inc. Common S | 123.20 | 2026-09-03 | `DELAYED` | +0.2552 | (0.30x`UNAVL` + 0.30x+0.7051 + 0.25x`UNAVL` + 0.15x+0.7169) x 0.80 - 0.00 = +0.2552 | 95.66 | +0.3048 | 5.73% | +0.9932 | +1.5883 | +0.9266 | +4.5747 | -3.45% | -5.80% | -5.30% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_4 | 60.95 / 68.44 / 64.68 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 5.73% | `REALIZED_VOL_30D` | 130.59 | 2026-10-01 | 123.26 | 137.93 | L222 | L322, L422, L522, L622, L013, L002 | MEDIUM | Finance at the 95.66th pctl; Tech_Z +0.7051 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| SCHW | Charles Schwab Corporation (The) C | 110.38 | 2026-09-03 | `DELAYED` | +0.2540 | (0.30x`UNAVL` + 0.30x+0.6887 + 0.25x`UNAVL` + 0.15x+0.7391) x 0.80 - 0.00 = +0.2540 | 95.46 | -0.0491 | 5.57% | +1.0216 | +1.7957 | +0.9099 | +4.8394 | -3.19% | -5.47% | -5.36% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 57.13 / 68.58 / 67.90 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 5.57% | `REALIZED_VOL_30D` | 117.00 | 2026-10-01 | 110.61 | 123.39 | L223 | L323, L423, L523, L623, L013, L002 | MEDIUM | Finance at the 95.46th pctl; Tech_Z +0.6887 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |

## Score attribution

Every published name, ranked or monitored — `rules.md § Financial Metrics and Score Attribution`
requires an `Adj Score` explanation for each, not only the top 20.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VLO | `UNAVL` | +1.4152 | `UNAVL` | +0.2756 | +0.4659 | 0.80 | 0.00 | +0.3727 | 20d momentum +2.1917; 60d momentum +2.0088; MACD state (D/W) +1.6777 | beta proximity to 1.0 -0.7053; rate sensitivity vs TLT -0.3745 | L300, L400, L500, L013, L020 |
| SPGI | `UNAVL` | +1.0592 | `UNAVL` | +0.8874 | +0.4509 | 0.80 | 0.00 | +0.3607 | 20d volume confirmation +1.7697; MACD state (D/W) +1.6777; 20d momentum +1.4637 | INSUFFICIENT_SOURCEABLE_DRIVERS | L301, L401, L501, L013, L020 |
| PFG | `UNAVL` | +1.2136 | `UNAVL` | +0.5348 | +0.4443 | 0.80 | 0.00 | +0.3554 | 20d volume confirmation +2.2815; MACD state (D/W) +1.6777; MA alignment (D/W) +1.3741 | 30d/60d vol stability -0.6499 | L302, L402, L502, L013, L020 |
| GILD | `UNAVL` | +1.1288 | `UNAVL` | +0.5676 | +0.4238 | 0.80 | 0.00 | +0.3390 | 20d momentum +2.0047; sector 60d momentum leadership +1.7364; MACD state (D/W) +1.6777 | 20d volume confirmation -0.5763; rate sensitivity vs TLT -0.2935 | L303, L403, L503, L013, L020 |
| AMP | `UNAVL` | +0.8574 | `UNAVL` | +1.0804 | +0.4193 | 0.80 | 0.00 | +0.3354 | 60d momentum +1.5642; MA alignment (D/W) +1.3741; sector 60d momentum leadership +1.3154 | INSUFFICIENT_SOURCEABLE_DRIVERS | L304, L404, L504, L013, L020 |
| IQV | `UNAVL` | +1.4310 | `UNAVL` | -0.0713 | +0.4186 | 0.80 | 0.00 | +0.3349 | 20d volume confirmation +2.2815; 20d momentum +2.1788; 60d momentum +2.0088 | 30d/60d vol stability -1.0297; beta proximity to 1.0 -0.7003; rate sensitivity vs TLT -0.2918 | L305, L405, L505, L013, L020 |
| RVTY | `UNAVL` | +1.3888 | `UNAVL` | -0.0035 | +0.4161 | 0.80 | 0.00 | +0.3329 | 20d momentum +1.8476; MACD state (D/W) +1.6777; 60d momentum +1.5151 | sector 60d momentum leadership -0.8256; rate sensitivity vs TLT -0.0640 | L306, L406, L506, L013, L020 |
| TECH | `UNAVL` | +0.7951 | `UNAVL` | +1.0699 | +0.3990 | 0.80 | 0.00 | +0.3192 | 60d momentum +2.0088; 30d/60d vol stability +1.7695; sector 60d momentum leadership +1.7364 | rate sensitivity vs TLT -0.3504 | L307, L407, L507, L013, L020 |
| PSX | `UNAVL` | +1.3457 | `UNAVL` | -0.0329 | +0.3988 | 0.80 | 0.00 | +0.3190 | 20d momentum +2.1917; 60d momentum +2.0088; MACD state (D/W) +1.6777 | beta proximity to 1.0 -1.1479; rate sensitivity vs TLT -0.5611 | L308, L408, L508, L013, L020 |
| STT | `UNAVL` | +0.9025 | `UNAVL` | +0.8260 | +0.3947 | 0.80 | 0.00 | +0.3157 | MA alignment (D/W) +1.3741; sector 60d momentum leadership +1.3154; beta proximity to 1.0 +1.3087 | 30d/60d vol stability -0.4030 | L309, L409, L509, L013, L020 |
| GEN | `UNAVL` | +1.2613 | `UNAVL` | +0.1009 | +0.3935 | 0.80 | 0.00 | +0.3148 | MACD state (D/W) +1.6777; 60d momentum +1.5515; 20d momentum +1.5362 | sector 60d momentum leadership -0.5690 | L310, L410, L510, L013, L020 |
| ICE | `UNAVL` | +0.8835 | `UNAVL` | +0.8271 | +0.3891 | 0.80 | 0.00 | +0.3113 | 20d volume confirmation +2.2815; sector 60d momentum leadership +1.3154; 20d momentum +1.2618 | beta proximity to 1.0 -0.1194 | L311, L411, L511, L013, L020 |
| BNY | `UNAVL` | +0.7190 | `UNAVL` | +1.0849 | +0.3784 | 0.80 | 0.00 | +0.3027 | MA alignment (D/W) +1.3741; sector 60d momentum leadership +1.3154; 30d/60d vol stability +1.1387 | INSUFFICIENT_SOURCEABLE_DRIVERS | L312, L412, L512, L013, L020 |
| DE | `UNAVL` | +1.3196 | `UNAVL` | -0.1415 | +0.3746 | 0.80 | 0.00 | +0.2997 | MACD state (D/W) +1.6777; 20d momentum +1.6616; 20d volume confirmation +1.4284 | 30d/60d vol stability -1.1256; sector 60d momentum leadership -0.8256 | L313, L413, L513, L013, L020 |
| JNJ | `UNAVL` | +0.9583 | `UNAVL` | +0.5388 | +0.3683 | 0.80 | 0.00 | +0.2946 | sector 60d momentum leadership +1.7364; MACD state (D/W) +1.6777; MA alignment (D/W) +1.3741 | beta proximity to 1.0 -1.3348; 20d volume confirmation -0.2351 | L314, L414, L514, L013, L020 |
| VRTX | `UNAVL` | +0.9749 | `UNAVL` | +0.4020 | +0.3528 | 0.80 | 0.00 | +0.2822 | 20d momentum +1.9690; sector 60d momentum leadership +1.7364; MACD state (D/W) +1.6777 | 20d volume confirmation -1.0455; rate sensitivity vs TLT -0.4136; 30d/60d vol stability -0.0316 | L315, L415, L515, L013, L020 |
| MPC | `UNAVL` | +1.2621 | `UNAVL` | -0.1906 | +0.3500 | 0.80 | 0.00 | +0.2800 | 20d momentum +2.1917; 60d momentum +2.0088; MACD state (D/W) +1.6777 | beta proximity to 1.0 -0.8558; 30d/60d vol stability -0.7161; 20d volume confirmation -0.4910 | L316, L416, L516, L013, L020 |
| WFC | `UNAVL` | +0.7511 | `UNAVL` | +0.7379 | +0.3360 | 0.80 | 0.00 | +0.2688 | MACD state (D/W) +1.6777; sector 60d momentum leadership +1.3154; 60d max drawdown +1.0659 | INSUFFICIENT_SOURCEABLE_DRIVERS | L317, L417, L517, L013, L020 |
| ELV | `UNAVL` | +0.6114 | `UNAVL` | +1.0062 | +0.3344 | 0.80 | 0.00 | +0.2675 | 30d/60d vol stability +1.7695; sector 60d momentum leadership +1.7364; 20d volume confirmation +1.6844 | 60d momentum -0.5213 | L318, L418, L518, L013, L020 |
| RJF | `UNAVL` | +0.7020 | `UNAVL` | +0.7863 | +0.3286 | 0.80 | 0.00 | +0.2628 | MA alignment (D/W) +1.3741; sector 60d momentum leadership +1.3154; rate sensitivity vs TLT +1.1263 | 30d/60d vol stability -0.0196 | L319, L419, L519, L013, L020 |
| DELL | `UNAVL` | +1.4805 | `UNAVL` | -0.7900 | +0.3257 | 0.80 | 0.00 | +0.2605 | 20d volume confirmation +2.2815; 20d momentum +2.1917; 60d momentum +2.0088 | beta proximity to 1.0 -1.3281; 30d/60d vol stability -1.1307; 60d max drawdown -0.6506 | L320, L420, L520, L013, L020 |
| BIIB | `UNAVL` | +0.7022 | `UNAVL` | +0.7276 | +0.3198 | 0.80 | 0.00 | +0.2558 | 30d/60d vol stability +1.7695; sector 60d momentum leadership +1.7364; MACD state (D/W) +1.6777 | 20d volume confirmation -0.8749; rate sensitivity vs TLT -0.6161 | L321, L421, L521, L013, L020 |
| PRU | `UNAVL` | +0.7051 | `UNAVL` | +0.7169 | +0.3191 | 0.80 | 0.00 | +0.2552 | MA alignment (D/W) +1.3741; sector 60d momentum leadership +1.3154; rate sensitivity vs TLT +1.1263 | 30d/60d vol stability -0.1006 | L322, L422, L522, L013, L020 |
| SCHW | `UNAVL` | +0.6887 | `UNAVL` | +0.7391 | +0.3175 | 0.80 | 0.00 | +0.2540 | 60d momentum +1.4542; MA alignment (D/W) +1.3741; sector 60d momentum leadership +1.3154 | 20d volume confirmation -0.3204; beta proximity to 1.0 -0.1098 | L323, L423, L523, L013, L020 |

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical / Price (6 Tech_Z slots) | 508 | 0 | none | all six slots resolve for every scored name |
| Macro / Regime (4 Macro_Z slots) | 508 | 0 | none | beta, sector leadership, rate sensitivity, vol stability |
| Fundamental | 0 | 508 | DQ 1.00 -> 0.80; family excluded from 3-of-4 | `L021` — no full-universe fetch path wired |
| Sentiment / Positioning | 0 | 508 | included in the same 0.80 step | `L022` — same cause |
| Enhancing (IV/skew, short interest, bid-ask, revisions, ownership) | 0 | 508 | confidence capped MEDIUM; gross exposure cap 50% if a GO were ever reached | `L023` — never a GO blocker |

Cross-sectional dispersion of each z-scored slot (a sanity check that no slot is degenerate):

| Slot | Family | n | min z | median z | max z |
|---|---|---|---|---|---|
| `mom20` | Technical | 508 | -1.7199 | -0.0835 | +2.1917 |
| `mom60` | Technical | 508 | -1.7755 | -0.0770 | +2.0088 |
| `ma_align` | Technical | 508 | -1.8954 | -0.2607 | +1.3741 |
| `macd` | Technical | 508 | -1.2739 | +0.2019 | +1.6777 |
| `vol_conf` | Technical | 508 | -1.3868 | -0.1498 | +2.2815 |
| `dd60` | Technical | 508 | -2.6379 | +0.3108 | +1.0949 |
| `beta` | Macro | 508 | -1.9795 | -0.0182 | +1.5607 |
| `sector_lead` | Macro | 508 | -1.4249 | -0.1908 | +1.7364 |
| `rate_sens` | Macro | 508 | -2.4946 | +0.2780 | +1.1263 |
| `vol_stability` | Macro | 508 | -1.8632 | +0.0611 | +1.7695 |

## Technical indicator summary

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60 Mom D | 20/60 Mom W | 20/60 Mom M | RS20/60 vs SPY D | Vol Ratio 20d | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VLO | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 75.26 / 78.49 / 87.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.8627 / +7.5812 / +19.5353 | `BULLISH` / `BULLISH` / `BULLISH` | +22.34% / +46.63% | +67.18% / +149.36% | +189.38% / +513.20% | +21.74% / +41.46% | 1.08 | L300, L400, L013 |
| SPGI | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_3 | 63.17 / 57.77 / 52.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.8869 / +6.1570 / -6.4130 | `BULLISH` / `MIXED` / `MIXED` | +11.44% / +12.39% | +8.13% / -8.66% | -7.33% / +16.97% | +10.84% / +7.22% | 1.37 | L301, L401, L013 |
| PFG | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_9 | 68.60 / 70.87 / 74.48 | `BULLISH_CROSS` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | +0.2645 / +0.0154 / +2.9767 | `BULLISH` / `BULLISH` / `BULLISH` | +3.47% / +11.95% | +25.16% / +54.04% | +53.01% / +119.58% | +2.87% / +6.78% | 3.40 | L302, L402, L013 |
| GILD | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 68.29 / 68.28 / 71.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.3361 / +1.9679 / +0.7793 | `BULLISH` / `BULLISH` / `BULLISH` | +15.54% / +21.26% | +10.57% / +41.49% | +61.86% / +157.19% | +14.94% / +16.09% | 0.82 | L303, L403, L013 |
| AMP | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.50 / 69.99 / 62.87 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | -2.5284 / +9.3377 / +3.0930 | `BULLISH` / `BULLISH` / `BULLISH` | +0.94% / +26.19% | +24.71% / +7.11% | +6.36% / +130.13% | +0.34% / +21.02% | 1.15 | L304, L404, L013 |
| IQV | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_4 | 75.17 / 75.13 / 63.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.0302 / +9.0751 / +9.2316 | `BULLISH` / `BULLISH` / `MIXED` | +16.86% / +45.84% | +53.93% / +66.84% | +34.89% / +13.39% | +16.26% / +40.67% | 1.60 | L305, L405, L013 |
| RVTY | SELL_SETUP_9 / SELL_SETUP_5 / SELL_SETUP_4 | 68.62 / 72.12 / 60.61 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.5692 / +2.5254 / +4.8729 | `BULLISH` / `BULLISH` / `MIXED` | +14.35% / +25.53% | +39.11% / +29.15% | +4.01% / -23.71% | +13.75% / +20.36% | 1.17 | L306, L406, L013 |
| TECH | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 66.10 / 65.94 / 55.46 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.1933 / +1.0164 / +2.6835 | `BULLISH` / `BULLISH` / `MIXED` | +0.88% / +33.30% | +22.68% / +34.78% | -0.51% / -38.81% | +0.28% / +28.13% | 0.96 | L307, L407, L013 |
| PSX | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 74.81 / 78.77 / 81.33 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.4169 / +6.1208 / +11.2513 | `BULLISH` / `BULLISH` / `BULLISH` | +24.57% / +43.02% | +64.91% / +101.04% | +128.85% / +336.02% | +23.97% / +37.85% | 0.98 | L308, L408, L013 |
| STT | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.03 / 82.05 / 88.94 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2891 / +0.9600 / +6.9659 | `BULLISH` / `BULLISH` / `BULLISH` | +4.88% / +19.39% | +34.02% / +81.58% | +98.86% / +166.42% | +4.28% / +14.22% | 1.21 | L309, L409, L013 |
| GEN | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_5 | 67.86 / 69.20 / 62.25 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.1391 / +0.7363 / +0.4876 | `BULLISH` / `BULLISH` / `BULLISH` | +11.99% / +26.02% | +57.24% / +11.83% | +20.28% / +37.40% | +11.39% / +20.85% | 1.10 | L310, L410, L013 |
| ICE | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 68.48 / 61.15 / 54.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -0.2530 / +3.3763 / -2.2518 | `BULLISH` / `MIXED` / `BULLISH` | +9.91% / +16.70% | +2.46% / -7.65% | +4.87% / +52.59% | +9.31% / +11.53% | 1.49 | L311, L411, L013 |
| BNY | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.86 / 77.20 / 91.64 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2195 / +0.6784 / +4.0756 | `BULLISH` / `BULLISH` / `BULLISH` | +3.47% / +15.17% | +22.60% / +79.35% | +96.82% / +263.06% | +2.87% / +10.00% | 1.07 | L312, L412, L013 |
| DE | SELL_SETUP_4 / SELL_SETUP_5 / SELL_SETUP_9 | 68.67 / 65.74 / 67.59 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +7.9042 / +5.8519 / +13.9478 | `BULLISH` / `BULLISH` / `BULLISH` | +12.94% / +20.59% | +17.91% / +37.22% | +48.52% / +120.67% | +12.34% / +15.42% | 1.29 | L313, L413, L013 |
| JNJ | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_9 | 65.95 / 69.40 / 79.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.4982 / +1.7355 / +6.8866 | `BULLISH` / `BULLISH` / `BULLISH` | +8.88% / +18.06% | +20.17% / +82.79% | +91.63% / +98.24% | +8.28% / +12.89% | 0.90 | L314, L414, L013 |
| VRTX | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_3 | 67.51 / 69.51 / 64.46 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.2913 / +8.8534 / +7.1649 | `BULLISH` / `BULLISH` / `BULLISH` | +15.27% / +25.17% | +26.46% / +19.01% | +20.85% / +207.60% | +14.67% / +20.00% | 0.71 | L315, L415, L013 |
| MPC | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_8 | 77.86 / 79.52 / 86.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.1241 / +9.5601 / +19.5759 | `BULLISH` / `BULLISH` / `BULLISH` | +29.92% / +50.60% | +82.63% / +120.38% | +175.15% / +601.17% | +29.32% / +45.43% | 0.84 | L316, L416, L013 |
| WFC | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_4 | 61.84 / 58.56 / 65.31 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.2990 / +0.6032 / -0.6378 | `BULLISH` / `MIXED` / `BULLISH` | +2.41% / +9.39% | +10.82% / +11.05% | +17.55% / +117.07% | +1.81% / +4.22% | 1.10 | L317, L417, L013 |
| ELV | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_6 | 62.76 / 61.87 / 55.81 | `ABOVE_SIGNAL` / `BELOW_SIGNAL` / `ABOVE_SIGNAL` | +1.2908 / -0.0526 / +11.6927 | `BULLISH` / `BULLISH` / `MIXED` | +5.97% / -1.88% | +28.92% / +24.31% | +7.95% / +19.18% | +5.37% / -7.05% | 1.35 | L318, L418, L013 |
| RJF | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.09 / 66.38 / 63.10 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | -0.3964 / +2.4583 / +0.7686 | `BULLISH` / `BULLISH` / `BULLISH` | +0.99% / +20.07% | +19.77% / +15.89% | +9.71% / +110.26% | +0.39% / +14.90% | 1.05 | L319, L419, L013 |
| DELL | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_7 | 62.55 / 71.51 / 85.88 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.6347 / +3.8224 / +37.7577 | `BULLISH` / `BULLISH` / `BULLISH` | +17.99% / +35.47% | +163.92% / +314.11% | +410.14% / +977.61% | +17.39% / +30.30% | 2.45 | L320, L420, L013 |
| BIIB | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.50 / 68.75 / 61.91 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.3716 / +1.0687 / +10.0135 | `BULLISH` / `BULLISH` / `MIXED` | +8.84% / +12.76% | +26.59% / +67.28% | +55.99% / -20.67% | +8.24% / +7.59% | 0.75 | L321, L421, L013 |
| PRU | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_4 | 60.95 / 68.44 / 64.68 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.3158 / +1.2944 / +1.8588 | `BULLISH` / `BULLISH` / `BULLISH` | +2.57% / +20.18% | +24.27% / +24.02% | +11.53% / +49.42% | +1.97% / +15.01% | 0.99 | L322, L422, L013 |
| SCHW | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 57.13 / 68.58 / 67.90 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.6073 / +1.7999 / +0.9279 | `BULLISH` / `BULLISH` / `BULLISH` | +2.83% / +24.71% | +20.39% / +21.89% | +36.41% / +62.02% | +2.23% / +19.54% | 0.88 | L323, L423, L013 |

## Penalties applied

**0 of 24 published names** carry the
`-0.10` earnings penalty from `rules.md § Risk Controls`. The complete forward calendar sweep
(`L010`) grounds the entire universe, so no name is penalised on an estimate and no name is
silently penalty-free for want of a resolution — the failure mode the 2026-07-27 and 2026-07-29
Track B changes were written to close.

| Ticker | Earnings status | Date | Days out | Penalty |
|---|---|---|---|---|
| VLO | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| SPGI | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| PFG | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| GILD | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| AMP | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| IQV | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| RVTY | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| TECH | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| PSX | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| STT | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| GEN | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| ICE | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| BNY | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| DE | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| JNJ | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| VRTX | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| MPC | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| WFC | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| ELV | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| RJF | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| DELL | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| BIIB | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| PRU | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |
| SCHW | `NO_PRINT_IN_WINDOW` | n/a | n/a | 0.00 |

## What drives the leaderboard

With two of four families dark, the composite reduces to
`(0.30 x Tech_Z + 0.15 x Macro_Z) x 0.80`, so **Technical carries
66.7% of live conviction** and Macro the rest. That is above the 50%
single-family ceiling in `rules.md § Evidence Thresholds` #3 by construction, and it is one of the
three reasons no name can be investable today (`06`). It also means the leaderboard is, mechanically,
a trend-persistence ranking: five of the six Tech_Z slots are momentum, trend-alignment or
trend-confirmation measures. The standing diagnosis — that such a ranking is anti-correlated with
forward alpha through a rotation — is the subject of `13` this run, where the Track A calibration
gate is finally open.

## Reproduction test against the prior package

The strongest verification this system has is to rebuild a *previous* package from this artifact's
own normative Metric Definition Table and diff the result against that package's published driver
values. It is what caught the `max_drawdown_60d` polarity bug on 2026-08-03 and the 61-vs-60-close
window convention on 2026-08-04 — neither of which any structural check would have found.

The engine was re-run at the **2026-08-28** basis (the previous `claude-opus-5` package) using
nothing but the table above, and its rebuilt family z-scores were diffed against that package's
own `score_explainability` values:

| Quantity | Result |
|---|---|
| Universe rebuilt at the 2026-08-28 basis | 509 names vs the 24-name published book from a 510-name scored universe |
| Published names reproduced | 24/24 |
| `Tech_Z` max abs difference | 0.0391 |
| `Macro_Z` max abs difference | 0.0012 |
| `Adj Score` max abs difference | 0.0094 |

The residual is explained: the rebuild scores **509** names where the 2026-08-28 run scored 510,
because today's corporate-action screen removes one name that was still trading then. A
one-name change in the cross-section shifts every winsorized z-score slightly, which is exactly
the size of the observed drift. **No metric slot shows a sign error or a systematic offset** — the
failure signature that the 2026-08-03 polarity bug produced was same-magnitude/opposite-sign
values, and nothing of that shape appears here.

## Hallucination-prevention checklist

| Check | Result |
|---|---|
| Every numeric `entry_price` has `price_date` + `price_tag` | PASS — L2xx rows, all `DELAYED` |
| Every numeric metric cites Source Ledger rows | PASS — L3xx/L4xx/L5xx/L6xx per name |
| Every `Adj Score` has a score trace with family z-scores, DQ, penalties, drivers | PASS — score attribution table above spans all 24 published names |
| Missing metrics are `UNAVAILABLE`, not neutral or supportive | PASS — Fund_Z/Sent_Z print `UNAVL` in every trace |
| `target_price = entry_price x (1 + mu)` | PASS — re-derived in the verification pass |
| Every sigma has a stated source | PASS — `REALIZED_VOL_30D` on every row |
| No investable name has `price_tag = UNAVAILABLE` | PASS — the investable set is empty |
| `mu`/`sigma` derive from the architecture, not assertion | PASS — mu from the calibration band for each name's percentile, no per-name adjustment |
| No live-sounding wording without non-illustrative ledger support | PASS — every price claim cites an L-row |
