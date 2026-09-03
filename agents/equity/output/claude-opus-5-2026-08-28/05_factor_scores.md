# 05 — Factor Scores — 2026-08-28

Primary home for `Adj Score` explainability. Every number below is generated from the run's computed
manifest; none is typed by hand. Universe **510** scored names, percentile label
`INDEX_UNION_PCTL (n=510)`.

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
  Entry, target and CI prices use **raw** closes. `technical_indicators.py` is fed the adjusted tree
  (`--history-dir .work/claude-opus-5-2026-08-28/history_adj`), whose `Close` column carries the adjusted values,
  because the helper prefers `Close` over `AdjClose`.
- **z-score.** Winsorize the raw (post-transform) cross-section at the 5th and 95th percentiles by
  clipping, then subtract the mean and divide by the **population** standard deviation (`ddof=0`)
  *of the clipped series*.
- **Family aggregation.** Equal-weighted arithmetic mean of the family's slot z-scores.
- **Relative strength is not a slot.** `rs20`/`rs60` are computed, displayed and ledgered as
  diagnostics only (Track B effective 2026-08-03, codified in `rules.md`).

### Realized winsorization bounds this run

| Slot | 5th pctl (clip) | 95th pctl (clip) | Clipped mean | Clipped population sd |
|---|---|---|---|---|
| `beta` | -1.9697 | -0.1148 | -1.0028 | 0.5412 |
| `dd60` | -0.3558 | -0.0560 | -0.1396 | 0.0804 |
| `ma_align` | -1.0000 | +1.0000 | +0.1676 | 0.5956 |
| `macd` | -1.5000 | +1.0000 | -0.1196 | 0.7780 |
| `mom20` | -9.6000 | +19.8015 | +2.5621 | 7.6863 |
| `mom60` | -20.5435 | +31.6025 | +6.4001 | 14.0531 |
| `rate_sens` | -1.9432 | -0.0410 | -0.6659 | 0.5321 |
| `sector_lead` | -3.4700 | +17.0150 | +5.6565 | 6.6650 |
| `vol_conf` | +0.5245 | +1.4755 | +0.8520 | 0.2526 |
| `vol_stability` | -1.1890 | -0.7325 | -0.9553 | 0.1251 |

### Derived ratio definitions used in the tables below

| Metric | Formula | Inputs |
|---|---|---|
| Forecast Sharpe | `(mu - rf_1m) / sigma` | mu from the calibration table; sigma = `REALIZED_VOL_30D`; `rf_1m` = L008 annual / 12 |
| Sortino | `(mu - rf_1m) / downside_sigma_1m` | `downside_sigma_1m` = pstdev of the **negative** daily adjusted returns in the trailing 30 sessions x `sqrt(21)` |
| Information Ratio | `(mu - beta x SPY_mu) / tracking_error_1m` | `SPY_mu` = +2.0% regime prior (`03`); `tracking_error_1m` = pstdev(r - beta x r_SPY) over 60 daily intervals x `sqrt(21)` |
| Treynor | `(mu - rf_1m) / beta` | beta from the 60d regression (L500+) |
| Calmar-style | `(mu - rf_1m) / abs(max_drawdown_60d)` | diagnostic and negative-risk screen only |
| VaR95 / CVaR95 | `mu - 1.65 x sigma` / `mu - 2.06 x sigma` | one-month return space; normality assumed and stated |
| Raw Kelly / 0.25x Kelly | `mu / sigma^2` / `0.25 x raw` | documented fallback form (no beta-adjusted edge / tracking-error variance wired); bounded by the 5% single-name cap |
| 70% CI bounds | `entry x (1 + mu -/+ 1.04 x sigma)` | factor **1.04** per `rules.md § Price and Target Citation Standard` — not the textbook 1.03643 |

## Calibration feedback binding (read before scoring)

From `02 § 0` / L014a, L014c: `EQUITY_ALPHA` CI coverage **71.88%** is inside the
55–85% band, so the "widen sigma" binding does **not** fire and `REALIZED_VOL_30D` stands as the sigma
source. Aggregate rank IC across scored vintages is negative (weighted mean
**-0.0495** over 69 vintages, 38 of them
below zero), which triggers the `rules.md` binding: **all confidence is capped at `MEDIUM`**. No
positive per-name `mu` adjustments were applied — every `mu` below is the unmodified calibration-table
band value for the name's percentile.

## Ranked candidate table (top 20)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RJF | Raymond James Financial Inc. Commo | 179.36 | 2026-08-28 | `DELAYED` | +0.3519 | (0.30x`UNAVL` + 0.30x+1.0136 + 0.25x`UNAVL` + 0.15x+0.9056) x 0.80 - 0.00 = +0.3519 | 100.00 | +0.2350 | 5.68% | 1.0013 | 1.4956 | 0.8473 | 4.6475 | -3.37% | -5.70% | -6.10% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 58.60 / 65.28 / 62.54 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 26bd | +6.00% | 5.68% | `REALIZED_VOL_30D` | 190.12 | 2026-09-25 | 179.52 | 200.72 | L200 | L300, L400, L500, L600, L700, L008, L021 | MEDIUM | Finance at 100.00 pctl; Tech_Z +1.0136 led by `vol_conf` +2.47 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `mom20` -0.08 |
| SCHW | Charles Schwab Corporation (The) C | 110.16 | 2026-08-28 | `DELAYED` | +0.3505 | (0.30x`UNAVL` + 0.30x+1.1470 + 0.25x`UNAVL` + 0.15x+0.6268) x 0.80 - 0.00 = +0.3505 | 99.80 | -0.1404 | 5.74% | 0.9917 | 1.5192 | 0.9509 | 4.5592 | -3.46% | -5.82% | -5.36% | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 57.26 / 68.35 / 67.81 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 26bd | +6.00% | 5.74% | `REALIZED_VOL_30D` | 116.77 | 2026-09-25 | 110.20 | 123.34 | L201 | L301, L401, L501, L601, L701, L008, L021 | MEDIUM | Finance at 99.80 pctl; Tech_Z +1.1470 led by `vol_conf` +2.47 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -0.25 |
| BLK | BlackRock Inc. Common Stock | 1,164.48 | 2026-08-28 | `DELAYED` | +0.3322 | (0.30x`UNAVL` + 0.30x+0.9108 + 0.25x`UNAVL` + 0.15x+0.9469) x 0.80 - 0.00 = +0.3322 | 99.61 | +0.8093 | 6.64% | 0.8567 | 1.8291 | 0.6017 | 3.4026 | -4.96% | -7.68% | -10.14% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 59.90 / 62.10 / 61.08 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 6.64% | `REALIZED_VOL_30D` | 1,234.35 | 2026-09-25 | 1,153.94 | 1,314.76 | L202 | L302, L402, L502, L602, L702, L008, L021 | MEDIUM | Finance at 99.61 pctl; Tech_Z +0.9108 led by `vol_conf` +2.05 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `rate_sens` +0.05 |
| RVTY | Revvity Inc. Common Stock | 128.80 | 2026-08-28 | `DELAYED` | +0.3112 | (0.30x`UNAVL` + 0.30x+1.2627 + 0.25x`UNAVL` + 0.15x+0.0683) x 0.80 - 0.00 = +0.3112 | 99.41 | +0.4591 | 9.86% | 0.5769 | 1.1665 | 0.4894 | 1.5428 | -10.27% | -14.31% | -6.38% | SELL_SETUP_8 / SELL_SETUP_4 / SELL_SETUP_3 | 69.84 / 71.13 / 59.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 9.86% | `REALIZED_VOL_30D` | 136.53 | 2026-09-25 | 123.32 | 149.74 | L203 | L303, L403, L503, L603, L703, L008, L021 | MEDIUM | Industrials at 99.41 pctl; Tech_Z +1.2627 led by `mom20` +1.55 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `sector_lead` -0.49 |
| SJM | The J.M. Smucker Company Common St | 132.34 | 2026-08-28 | `DELAYED` | +0.3079 | (0.30x`UNAVL` + 0.30x+1.3010 + 0.25x`UNAVL` + 0.15x-0.0364) x 0.80 - 0.00 = +0.3079 | 99.21 | -0.7004 | 8.47% | 0.6719 | 1.2070 | 0.7061 | 2.0929 | -7.97% | -11.44% | -8.42% | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.68 / 74.74 / 63.18 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 8.47% | `REALIZED_VOL_30D` | 140.28 | 2026-09-25 | 128.63 | 151.93 | L204 | L304, L404, L504, L604, L704, L008, L021 | MEDIUM | Consumer Staples at 99.21 pctl; Tech_Z +1.3010 led by `mom60` +1.79 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -1.29 |
| APD | Air Products and Chemicals Inc. Co | 308.09 | 2026-08-28 | `DELAYED` | +0.3067 | (0.30x`UNAVL` + 0.30x+0.9050 + 0.25x`UNAVL` + 0.15x+0.7460) x 0.80 - 0.00 = +0.3067 | 99.02 | +0.1969 | 5.14% | 1.1074 | 1.5949 | 0.7072 | 5.6845 | -2.48% | -4.58% | -6.88% | SELL_SETUP_6 / SELL_SETUP_4 / SELL_SETUP_8 | 58.03 / 59.93 / 58.12 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 5.14% | `REALIZED_VOL_30D` | 326.58 | 2026-09-25 | 310.12 | 343.03 | L205 | L305, L405, L505, L605, L705, L008, L021 | MEDIUM | Basic Materials at 99.02 pctl; Tech_Z +0.9050 led by `vol_stability` +1.78 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `rate_sens` +0.21 |
| BDX | Becton Dickinson and Company Commo | 189.52 | 2026-08-28 | `DELAYED` | +0.3028 | (0.30x`UNAVL` + 0.30x+1.0080 + 0.25x`UNAVL` + 0.15x+0.5071) x 0.80 - 0.00 = +0.3028 | 98.82 | -0.0960 | 7.47% | 0.7612 | 1.9629 | 0.7356 | 2.6860 | -6.33% | -9.39% | -7.45% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 70.05 / 70.20 / 60.81 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 7.47% | `REALIZED_VOL_30D` | 200.89 | 2026-09-25 | 186.16 | 215.62 | L206 | L306, L406, L506, L606, L706, L008, L021 | MEDIUM | Health Care at 98.82 pctl; Tech_Z +1.0080 led by `mom60` +1.76 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -0.17 |
| BNY | The Bank of New York Mellon Corpor | 162.50 | 2026-08-28 | `DELAYED` | +0.3026 | (0.30x`UNAVL` + 0.30x+0.6788 + 0.25x`UNAVL` + 0.15x+1.1645) x 0.80 - 0.00 = +0.3026 | 98.62 | +0.4852 | 5.23% | 1.0881 | 1.5414 | 0.7845 | 5.4887 | -2.63% | -4.77% | -5.69% | SELL_SETUP_4 / SELL_SETUP_9 / SELL_SETUP_9 | 57.98 / 76.13 / 91.36 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 5.23% | `REALIZED_VOL_30D` | 172.25 | 2026-09-25 | 163.42 | 181.08 | L207 | L307, L407, L507, L607, L707, L008, L021 | MEDIUM | Finance at 98.62 pctl; Tech_Z +0.6788 led by `vol_stability` +1.40 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `macd` +0.15 |
| IQV | IQVIA Holdings Inc. Common Stock | 261.75 | 2026-08-28 | `DELAYED` | +0.3020 | (0.30x`UNAVL` + 0.30x+1.3115 + 0.25x`UNAVL` + 0.15x-0.1061) x 0.80 - 0.00 = +0.3020 | 98.43 | -0.2791 | 14.20% | 0.4007 | 1.2765 | 0.5171 | 0.7443 | -17.42% | -23.24% | -10.23% | SELL_SETUP_8 / SELL_SETUP_9 / SELL_SETUP_3 | 72.36 / 73.07 / 61.86 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 14.20% | `REALIZED_VOL_30D` | 277.46 | 2026-09-25 | 238.81 | 316.10 | L208 | L308, L408, L508, L608, L708, L008, L021 | MEDIUM | Health Care at 98.43 pctl; Tech_Z +1.3115 led by `vol_conf` +2.47 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `vol_stability` -1.28 |
| GIS | General Mills Inc. Common Stock | 41.55 | 2026-08-28 | `DELAYED` | +0.2968 | (0.30x`UNAVL` + 0.30x+1.2360 + 0.25x`UNAVL` + 0.15x+0.0017) x 0.80 - 0.00 = +0.2968 | 98.23 | -0.3791 | 9.16% | 0.6213 | 1.0204 | 0.6594 | 1.7894 | -9.11% | -12.86% | -8.14% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_1 | 67.38 / 61.82 / 42.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | 26d (2026-09-23) | +6.00% | 9.16% | `REALIZED_VOL_30D` | 44.04 | 2026-09-25 | 40.09 | 48.00 | L209 | L309, L409, L509, L609, L709, L008, L021 | MEDIUM | Consumer Staples at 98.23 pctl; Tech_Z +1.2360 led by `mom60` +1.78 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -0.70 |
| NWSA | News Corporation Class A Common St | 30.97 | 2026-08-28 | `DELAYED` | +0.2928 | (0.30x`UNAVL` + 0.30x+1.2434 + 0.25x`UNAVL` + 0.15x-0.0466) x 0.80 - 0.00 = +0.2928 | 98.04 | -0.4096 | 8.37% | 0.6793 | 0.9706 | 0.8450 | 2.1389 | -7.82% | -11.25% | -9.72% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 68.15 / 68.78 / 62.08 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 8.37% | `REALIZED_VOL_30D` | 32.83 | 2026-09-25 | 30.13 | 35.53 | L210 | L310, L410, L510, L610, L710, L008, L021 | MEDIUM | Consumer Discretionary at 98.04 pctl; Tech_Z +1.2434 led by `vol_conf` +1.93 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -0.75 |
| NDAQ | Nasdaq Inc. Common Stock | 99.31 | 2026-08-28 | `DELAYED` | +0.2909 | (0.30x`UNAVL` + 0.30x+0.6788 + 0.25x`UNAVL` + 0.15x+1.0661) x 0.80 - 0.00 = +0.2909 | 97.84 | +0.3738 | 4.29% | 1.3269 | 2.8460 | 0.6005 | 8.1622 | -1.07% | -2.83% | -15.59% | SELL_SETUP_7 / SELL_SETUP_7 / SELL_SETUP_2 | 69.08 / 62.82 / 61.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 4.29% | `REALIZED_VOL_30D` | 105.27 | 2026-09-25 | 100.84 | 109.70 | L211 | L311, L411, L511, L611, L711, L008, L021 | MEDIUM | Finance at 97.84 pctl; Tech_Z +0.6788 led by `vol_stability` +1.78 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `dd60` -0.20 |
| NWS | News Corporation Class B Common St | 34.85 | 2026-08-28 | `DELAYED` | +0.2872 | (0.30x`UNAVL` + 0.30x+1.2034 + 0.25x`UNAVL` + 0.15x-0.0136) x 0.80 - 0.00 = +0.2872 | 97.64 | -0.4311 | 8.83% | 0.6444 | 1.0105 | 0.7987 | 1.9250 | -8.57% | -12.18% | -10.48% | BUY_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_3 | 64.48 / 66.46 / 61.28 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 8.83% | `REALIZED_VOL_30D` | 36.94 | 2026-09-25 | 33.74 | 40.14 | L212 | L312, L412, L512, L612, L712, L008, L021 | MEDIUM | Consumer Discretionary at 97.64 pctl; Tech_Z +1.2034 led by `vol_conf` +2.05 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -0.79 |
| VEEV | Veeva Systems Inc. Class A Common  | 276.69 | 2026-08-28 | `DELAYED` | +0.2864 | (0.30x`UNAVL` + 0.30x+1.4098 + 0.25x`UNAVL` + 0.15x-0.4328) x 0.80 - 0.00 = +0.2864 | 97.45 | +0.4360 | 16.72% | 0.3403 | 1.0230 | 0.3466 | 0.5367 | -21.58% | -28.44% | -14.30% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 74.85 / 72.75 / 59.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 16.72% | `REALIZED_VOL_30D` | 293.29 | 2026-09-25 | 245.19 | 341.40 | L213 | L313, L413, L513, L613, L713, L008, L021 | MEDIUM | Technology at 97.45 pctl; Tech_Z +1.4098 led by `vol_conf` +2.47 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `sector_lead` -1.37 |
| A | Agilent Technologies Inc. Common S | 153.84 | 2026-08-28 | `DELAYED` | +0.2740 | (0.30x`UNAVL` + 0.30x+1.0750 + 0.25x`UNAVL` + 0.15x+0.1335) x 0.80 - 0.00 = +0.2740 | 97.25 | +0.4071 | 7.97% | 0.7135 | 1.2798 | 0.6286 | 2.3597 | -7.16% | -10.42% | -10.15% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_4 | 61.01 / 65.27 / 59.19 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 7.97% | `REALIZED_VOL_30D` | 163.07 | 2026-09-25 | 150.31 | 175.83 | L214 | L314, L414, L514, L614, L714, L008, L021 | MEDIUM | Industrials at 97.25 pctl; Tech_Z +1.0750 led by `vol_conf` +2.45 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `sector_lead` -0.49 |
| RMD | ResMed Inc. Common Stock | 240.33 | 2026-08-28 | `DELAYED` | +0.2737 | (0.30x`UNAVL` + 0.30x+0.9021 + 0.25x`UNAVL` + 0.15x+0.4767) x 0.80 - 0.00 = +0.2737 | 97.05 | +0.1674 | 9.70% | 0.5863 | 0.9239 | 0.5344 | 1.5935 | -10.01% | -13.99% | -12.68% | SELL_SETUP_8 / SELL_SETUP_5 / SELL_SETUP_1 | 69.57 / 61.48 / 53.00 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 9.70% | `REALIZED_VOL_30D` | 254.75 | 2026-09-25 | 230.50 | 279.00 | L215 | L315, L415, L515, L615, L715, L008, L021 | MEDIUM | Health Care at 97.05 pctl; Tech_Z +0.9021 led by `sector_lead` +1.70 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `rate_sens` -0.45 |
| ABT | Abbott Laboratories Common Stock | 112.47 | 2026-08-28 | `DELAYED` | +0.2723 | (0.30x`UNAVL` + 0.30x+0.7488 + 0.25x`UNAVL` + 0.15x+0.7715) x 0.80 - 0.00 = +0.2723 | 96.86 | -0.4386 | 6.13% | 0.9282 | 1.4724 | 0.7307 | 3.9944 | -4.11% | -6.62% | -7.18% | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 59.70 / 61.49 / 51.08 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 26bd | +6.00% | 6.13% | `REALIZED_VOL_30D` | 119.22 | 2026-09-25 | 112.05 | 126.39 | L216 | L316, L416, L516, L616, L716, L008, L021 | MEDIUM | Health Care at 96.86 pctl; Tech_Z +0.7488 led by `vol_stability` +1.78 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -0.81 |
| STT | State Street Corporation Common St | 193.33 | 2026-08-28 | `DELAYED` | +0.2712 | (0.30x`UNAVL` + 0.30x+0.6788 + 0.25x`UNAVL` + 0.15x+0.9021) x 0.80 - 0.00 = +0.2712 | 96.66 | +0.6287 | 6.55% | 0.8679 | 1.1180 | 0.7329 | 3.4921 | -4.81% | -7.50% | -5.65% | SELL_SETUP_4 / SELL_SETUP_9 / SELL_SETUP_9 | 62.01 / 81.82 / 88.76 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 6.55% | `REALIZED_VOL_30D` | 204.93 | 2026-09-25 | 191.75 | 218.11 | L217 | L317, L417, L517, L617, L717, L008, L021 | MEDIUM | Finance at 96.66 pctl; Tech_Z +0.6788 led by `macd` +1.44 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `vol_conf` -1.30 |
| JNJ | Johnson & Johnson Common Stock | 268.04 | 2026-08-28 | `DELAYED` | +0.2671 | (0.30x`UNAVL` + 0.30x+0.8606 + 0.25x`UNAVL` + 0.15x+0.5046) x 0.80 - 0.00 = +0.2671 | 96.46 | -0.7547 | 6.17% | 0.9224 | 1.2769 | 1.1181 | 3.9440 | -4.18% | -6.70% | -7.57% | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_9 | 57.07 / 65.56 / 77.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 26bd | +6.00% | 6.17% | `REALIZED_VOL_30D` | 284.12 | 2026-09-25 | 266.93 | 301.31 | L218 | L318, L418, L518, L618, L718, L008, L021 | MEDIUM | Health Care at 96.46 pctl; Tech_Z +0.8606 led by `sector_lead` +1.70 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `beta` -1.39 |
| VRTX | Vertex Pharmaceuticals Incorporate | 541.69 | 2026-08-28 | `DELAYED` | +0.2640 | (0.30x`UNAVL` + 0.30x+0.9337 + 0.25x`UNAVL` + 0.15x+0.3325) x 0.80 - 0.00 = +0.2640 | 96.27 | +0.1319 | 8.51% | 0.6684 | 1.8993 | 0.6568 | 2.0710 | -8.04% | -11.53% | -11.12% | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_2 | 61.43 / 66.90 / 62.80 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 26bd | +6.00% | 8.51% | `REALIZED_VOL_30D` | 574.19 | 2026-09-25 | 526.25 | 622.14 | L219 | L319, L419, L519, L619, L719, L008, L021 | MEDIUM | Health Care at 96.27 pctl; Tech_Z +0.9337 led by `sector_lead` +1.70 | Trend-persistence construction; 2 of 4 families UNAVAILABLE; weakest slot `rate_sens` -0.48 |

Ranks are **contiguous 1..24** with no skipped names: the forward earnings sweep grounded
510/510 scored names, so the "skip
ungrounded entrants" rule used on 2026-07-27/-28 has nothing to skip.

## Score attribution — all 24 published names

`rules.md § Financial Metrics and Score Attribution` requires an `Adj Score` explanation for every
ranked **or monitored** name, so this table spans all 24 published names rather than the top 20
the ranked-candidate schema shows.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RJF | `UNAVAILABLE` | +1.0136 | `UNAVAILABLE` | +0.9056 | +0.4399 | 0.80 | 0.00 | +0.3519 | `vol_conf` +2.47; `ma_align` +1.40; `sector_lead` +1.26 | `mom20` -0.08; `macd` +0.15; `beta` +0.44 | L300, L400, L500, L600 |
| SCHW | `UNAVAILABLE` | +1.1470 | `UNAVAILABLE` | +0.6268 | +0.4381 | 0.80 | 0.00 | +0.3505 | `vol_conf` +2.47; `mom60` +1.51; `ma_align` +1.40 | `beta` -0.25; `macd` +0.15; `mom20` +0.31 | L301, L401, L501, L601 |
| BLK | `UNAVAILABLE` | +0.9108 | `UNAVAILABLE` | +0.9469 | +0.4153 | 0.80 | 0.00 | +0.3322 | `vol_conf` +2.05; `beta` +1.50; `ma_align` +1.40 | `rate_sens` +0.05; `macd` +0.15; `dd60` +0.47 | L302, L402, L502, L602 |
| RVTY | `UNAVAILABLE` | +1.2627 | `UNAVAILABLE` | +0.0683 | +0.3890 | 0.80 | 0.00 | +0.3112 | `mom20` +1.55; `mom60` +1.50; `macd` +1.44 | `sector_lead` -0.49; `rate_sens` -0.25; `vol_stability` +0.16 | L303, L403, L503, L603 |
| SJM | `UNAVAILABLE` | +1.3010 | `UNAVAILABLE` | -0.0364 | +0.3849 | 0.80 | 0.00 | +0.3079 | `mom60` +1.79; `macd` +1.44; `vol_stability` +1.40 | `beta` -1.29; `rate_sens` -0.20; `sector_lead` -0.06 | L304, L404, L504, L604 |
| APD | `UNAVAILABLE` | +0.9050 | `UNAVAILABLE` | +0.7460 | +0.3834 | 0.80 | 0.00 | +0.3067 | `vol_stability` +1.78; `macd` +1.44; `ma_align` +1.40 | `rate_sens` +0.21; `mom60` +0.24; `mom20` +0.25 | L305, L405, L505, L605 |
| BDX | `UNAVAILABLE` | +1.0080 | `UNAVAILABLE` | +0.5071 | +0.3785 | 0.80 | 0.00 | +0.3028 | `mom60` +1.76; `sector_lead` +1.70; `mom20` +1.54 | `beta` -0.17; `rate_sens` -0.05; `macd` +0.15 | L306, L406, L506, L606 |
| BNY | `UNAVAILABLE` | +0.6788 | `UNAVAILABLE` | +1.1645 | +0.3783 | 0.80 | 0.00 | +0.3026 | `vol_stability` +1.40; `ma_align` +1.40; `sector_lead` +1.26 | `macd` +0.15; `mom20` +0.18; `vol_conf` +0.63 | L307, L407, L507, L607 |
| IQV | `UNAVAILABLE` | +1.3115 | `UNAVAILABLE` | -0.1061 | +0.3775 | 0.80 | 0.00 | +0.3020 | `vol_conf` +2.47; `mom60` +1.79; `sector_lead` +1.70 | `vol_stability` -1.28; `beta` -0.51; `rate_sens` -0.34 | L308, L408, L508, L608 |
| GIS | `UNAVAILABLE` | +1.2360 | `UNAVAILABLE` | +0.0017 | +0.3711 | 0.80 | 0.00 | +0.2968 | `mom60` +1.78; `mom20` +1.78; `macd` +1.44 | `beta` -0.70; `sector_lead` -0.06; `rate_sens` +0.19 | L309, L409, L509, L609 |
| NWSA | `UNAVAILABLE` | +1.2434 | `UNAVAILABLE` | -0.0466 | +0.3660 | 0.80 | 0.00 | +0.2928 | `vol_conf` +1.93; `macd` +1.44; `ma_align` +1.40 | `beta` -0.75; `vol_stability` -0.49; `sector_lead` +0.28 | L310, L410, L510, L610 |
| NDAQ | `UNAVAILABLE` | +0.6788 | `UNAVAILABLE` | +1.0661 | +0.3636 | 0.80 | 0.00 | +0.2909 | `vol_stability` +1.78; `macd` +1.44; `ma_align` +1.40 | `dd60` -0.20; `mom20` +0.37; `vol_conf` +0.47 | L311, L411, L511, L611 |
| NWS | `UNAVAILABLE` | +1.2034 | `UNAVAILABLE` | -0.0136 | +0.3590 | 0.80 | 0.00 | +0.2872 | `vol_conf` +2.05; `macd` +1.44; `ma_align` +1.40 | `beta` -0.79; `vol_stability` -0.42; `sector_lead` +0.28 | L312, L412, L512, L612 |
| VEEV | `UNAVAILABLE` | +1.4098 | `UNAVAILABLE` | -0.4328 | +0.3580 | 0.80 | 0.00 | +0.2864 | `vol_conf` +2.47; `mom20` +2.24; `mom60` +1.79 | `sector_lead` -1.37; `vol_stability` -1.34; `dd60` -0.04 | L313, L413, L513, L613 |
| A | `UNAVAILABLE` | +1.0750 | `UNAVAILABLE` | +0.1335 | +0.3425 | 0.80 | 0.00 | +0.2740 | `vol_conf` +2.45; `macd` +1.44; `mom20` +1.12 | `sector_lead` -0.49; `vol_stability` +0.06; `rate_sens` +0.21 | L314, L414, L514, L614 |
| RMD | `UNAVAILABLE` | +0.9021 | `UNAVAILABLE` | +0.4767 | +0.3422 | 0.80 | 0.00 | +0.2737 | `sector_lead` +1.70; `mom60` +1.63; `mom20` +1.52 | `rate_sens` -0.45; `vol_conf` +0.11; `dd60` +0.16 | L315, L415, L515, L615 |
| ABT | `UNAVAILABLE` | +0.7488 | `UNAVAILABLE` | +0.7715 | +0.3404 | 0.80 | 0.00 | +0.2723 | `vol_stability` +1.78; `sector_lead` +1.70; `mom60` +1.69 | `beta` -0.81; `macd` +0.15; `rate_sens` +0.41 | L316, L416, L516, L616 |
| STT | `UNAVAILABLE` | +0.6788 | `UNAVAILABLE` | +0.9021 | +0.3390 | 0.80 | 0.00 | +0.2712 | `macd` +1.44; `ma_align` +1.40; `sector_lead` +1.26 | `vol_conf` -1.30; `vol_stability` +0.09; `mom20` +0.31 | L317, L417, L517, L617 |
| JNJ | `UNAVAILABLE` | +0.8606 | `UNAVAILABLE` | +0.5046 | +0.3339 | 0.80 | 0.00 | +0.2671 | `sector_lead` +1.70; `macd` +1.44; `ma_align` +1.40 | `beta` -1.39; `vol_conf` +0.19; `mom20` +0.33 | L318, L418, L518, L618 |
| VRTX | `UNAVAILABLE` | +0.9337 | `UNAVAILABLE` | +0.3325 | +0.3300 | 0.80 | 0.00 | +0.2640 | `sector_lead` +1.70; `macd` +1.44; `mom20` +1.43 | `rate_sens` -0.48; `vol_conf` -0.44; `vol_stability` -0.14 | L319, L419, L519, L619 |
| NEM | `UNAVAILABLE` | +1.0623 | `UNAVAILABLE` | +0.0597 | +0.3276 | 0.80 | 0.00 | +0.2621 | `mom20` +2.24; `macd` +1.44; `ma_align` +1.40 | `rate_sens` -0.68; `dd60` -0.47; `vol_stability` -0.01 | L320, L420, L520, L620 |
| AMP | `UNAVAILABLE` | +0.4834 | `UNAVAILABLE` | +1.1997 | +0.3250 | 0.80 | 0.00 | +0.2600 | `vol_stability` +1.78; `mom60` +1.48; `sector_lead` +1.26 | `vol_conf` -0.36; `mom20` +0.03; `macd` +0.15 | L321, L421, L521, L621 |
| NOW | `UNAVAILABLE` | +1.0828 | `UNAVAILABLE` | +0.0001 | +0.3249 | 0.80 | 0.00 | +0.2599 | `vol_conf` +2.47; `mom20` +2.24; `macd` +1.44 | `dd60` -1.37; `sector_lead` -1.37; `vol_stability` -0.61 | L322, L422, L522, L622 |
| ICE | `UNAVAILABLE` | +0.6125 | `UNAVAILABLE` | +0.9186 | +0.3215 | 0.80 | 0.00 | +0.2572 | `vol_stability` +1.62; `macd` +1.44; `sector_lead` +1.26 | `beta` -0.20; `dd60` +0.10; `vol_conf` +0.27 | L323, L423, L523, L623 |

Formula, identical for every row:
`Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`, with
`UNAVAILABLE` families contributing `0.00` per `rules.md § Family Aggregation`.

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Risk / return ratios | 510/510 | 0 | none — 100% coverage | all derived from fetched adjusted returns (L500+, L600+) |
| Tail risk (dd60, VaR95, CVaR95) | 510/510 | 0 | none | `dd60` is a scored `Tech_Z` slot; VaR/CVaR are display metrics |
| Sizing (Kelly) | 510/510 | 0 | none | `mu/sigma^2` fallback form, disclosed |
| Technical pack | 510/510 | 0 | none — well above the 70% bar | 6 distinct slots feed `Tech_Z` |
| Fundamental / quality | 0/510 | 510 | **`Fund_Z` UNAVAILABLE** — family excluded from the 3-of-4 count, DQ reduced to 0.80 | L018; SHADOW tooling covers ~4.7% of the universe |
| Sentiment / positioning | 0/510 | 510 | **`Sent_Z` UNAVAILABLE** — family excluded from the 3-of-4 count, DQ reduced to 0.80 | L019; requires the unbuilt Phase 2 fetch |

## Technical indicator summary — all 24 published names

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W | 20/60 Mom D | RS20/60 vs SPY D | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|
| RJF | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 58.60 / 65.28 / 62.54 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | -0.7329 / +2.6335 / +0.0230 | BULLISH / BULLISH | +1.92% / +22.82% | -1.07% / +20.56% | L300, L400, L013, L004 |
| SCHW | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 57.26 / 68.35 / 67.81 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | -0.5097 / +2.0393 / +0.5558 | BULLISH / BULLISH | +4.98% / +27.59% | +1.99% / +25.33% | L301, L401, L013, L004 |
| BLK | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 59.90 / 62.10 / 61.08 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -2.6328 / +16.7293 / -4.7405 | BULLISH / BULLISH | +6.79% / +18.18% | +3.80% / +15.92% | L302, L402, L013, L004 |
| RVTY | SELL_SETUP_8 / SELL_SETUP_4 / SELL_SETUP_3 | 69.84 / 71.13 / 59.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.9672 / +2.3526 / +4.1322 | BULLISH / BULLISH | +14.47% / +27.52% | +11.48% / +25.26% | L303, L403, L013, L004 |
| SJM | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.68 / 74.74 / 63.18 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.0871 / +2.1624 / +3.1852 | BULLISH / BULLISH | +12.01% / +31.91% | +9.02% / +29.65% | L304, L404, L013, L004 |
| APD | SELL_SETUP_6 / SELL_SETUP_4 / SELL_SETUP_8 | 58.03 / 59.93 / 58.12 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0007 / +1.0404 / +3.0872 | BULLISH / BULLISH | +4.48% / +9.83% | +1.49% / +7.57% | L305, L405, L013, L004 |
| BDX | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 70.05 / 70.20 / 60.81 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2662 / +4.5481 / +4.0165 | BULLISH / BULLISH | +14.43% / +31.07% | +11.44% / +28.81% | L306, L406, L013, L004 |
| BNY | SELL_SETUP_4 / SELL_SETUP_9 / SELL_SETUP_9 | 57.98 / 76.13 / 91.36 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2279 / +0.7748 / +4.1060 | BULLISH / BULLISH | +3.95% / +16.06% | +0.96% / +13.80% | L307, L407, L013, L004 |
| IQV | SELL_SETUP_8 / SELL_SETUP_9 / SELL_SETUP_3 | 72.36 / 73.07 / 61.86 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.4182 / +8.8116 / +6.7155 | BULLISH / MIXED | +11.37% / +43.78% | +8.38% / +41.52% | L308, L408, L013, L004 |
| GIS | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_1 | 67.38 / 61.82 / 42.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.2008 / +1.1078 / -0.3899 | BULLISH / MIXED | +16.22% / +31.39% | +13.23% / +29.13% | L309, L409, L013, L004 |
| NWSA | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 68.15 / 68.78 / 62.08 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.1409 / +0.4937 / -0.0164 | BULLISH / BULLISH | +12.37% / +18.89% | +9.38% / +16.63% | L310, L410, L013, L004 |
| NDAQ | SELL_SETUP_7 / SELL_SETUP_7 / SELL_SETUP_2 | 69.08 / 62.82 / 61.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.0170 / +1.3857 / -0.4327 | BULLISH / BULLISH | +5.44% / +14.81% | +2.45% / +12.55% | L311, L411, L013, L004 |
| NWS | BUY_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_3 | 64.48 / 66.46 / 61.28 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.1219 / +0.5303 / -0.1463 | BULLISH / BULLISH | +11.45% / +16.87% | +8.46% / +14.61% | L312, L412, L013, L004 |
| VEEV | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 74.85 / 72.75 / 59.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.8842 / +13.0789 / -1.2471 | BULLISH / MIXED | +35.78% / +54.82% | +32.79% / +52.56% | L313, L413, L013, L004 |
| A | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_4 | 61.01 / 65.27 / 59.19 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0159 / +3.2637 / +2.3585 | BULLISH / MIXED | +11.18% / +12.18% | +8.19% / +9.92% | L314, L414, L013, L004 |
| RMD | SELL_SETUP_8 / SELL_SETUP_5 / SELL_SETUP_1 | 69.57 / 61.48 / 53.00 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.8910 / +5.9992 / -4.5584 | BULLISH / MIXED | +14.24% / +29.26% | +11.25% / +27.00% | L315, L415, L013, L004 |
| ABT | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 59.70 / 61.49 / 51.08 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -0.5252 / +3.6424 / -2.4076 | BULLISH / MIXED | +6.40% / +30.21% | +3.41% / +27.95% | L316, L416, L013, L004 |
| STT | SELL_SETUP_4 / SELL_SETUP_9 / SELL_SETUP_9 | 62.01 / 81.82 / 88.76 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0726 / +1.1956 / +7.0077 | BULLISH / BULLISH | +4.98% / +23.06% | +1.99% / +20.80% | L317, L417, L013, L004 |
| JNJ | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_9 | 57.07 / 65.56 / 77.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0156 / +1.2299 / +6.7462 | BULLISH / BULLISH | +5.08% / +20.66% | +2.09% / +18.40% | L318, L418, L013, L004 |
| VRTX | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_2 | 61.43 / 66.90 / 62.80 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | +1.2455 / +7.8139 / +3.6317 | BULLISH / BULLISH | +13.54% / +26.46% | +10.55% / +24.20% | L319, L419, L013, L004 |
| NEM | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_1 | 64.49 / 62.92 / 69.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.7566 / +2.7572 / +1.8532 | BULLISH / BULLISH | +36.57% / +19.08% | +33.58% / +16.82% | L320, L420, L013, L004 |
| AMP | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 58.51 / 68.87 / 62.22 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | -2.8428 / +10.3289 / +0.0995 | MIXED / BULLISH | +2.79% / +27.25% | -0.20% / +24.99% | L321, L421, L013, L004 |
| NOW | SELL_SETUP_2 / SELL_SETUP_8 / SELL_SETUP_2 | 72.72 / 63.55 / 50.24 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.1699 / +6.1832 / -5.6041 | BULLISH / MIXED | +30.10% / +22.74% | +27.11% / +20.48% | L322, L422, L013, L004 |
| ICE | BUY_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_1 | 72.12 / 59.63 / 53.81 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.2585 / +3.0820 / -3.3121 | BULLISH / MIXED | +6.46% / +17.68% | +3.47% / +15.42% | L323, L423, L013, L004 |

Interpretation discipline per `rules.md § Technical Indicator Pack Definition`: TD-9 setup `9` and
RSI ≥ 70 / ≤ 30 are exhaustion flags affecting confidence and penalties only when confirmed by
ledger-backed price action — never standalone trade signals; MACD supports momentum only when aligned
with the 20d/60d momentum and relative-strength readings.

## Evidence thresholds (`rules.md § Evidence Thresholds`)

| Threshold | Result | Evidence |
|---|---|---|
| 1. Adjusted-score percentile ≥ 80th | **PASS** for all 24 published names | rank floor 95.48 pctl (`INDEX_UNION_PCTL (n=510)`) |
| 2. ≥ 3 of 4 factor families non-negative | **FAIL — arithmetically unsatisfiable** | only 2 families are available at all (Fund_Z and Sent_Z UNAVAILABLE universe-wide (no fetch path wired; SHADOW tooling not promoted)); max attainable = 2 < 3 |
| 3. No family contributes > 50% of conviction | **FAIL** | `Tech_Z` carries 0.30 of the 0.45 live weight = **66.67%** |
| 4. Data completeness ≥ 85% | **FAIL** | DQ multiplier 0.80 (L021) |
| 5. No hard stop from § Stop Criteria | **PASS** | see `03 § Stop-criteria check` and `08` |

**Investable subset: 0 names.** Thresholds 2, 3 and 4 fail for every name in the universe, and they
fail structurally — not because of this cross-section's quality. With `Fund_Z` and `Sent_Z`
`UNAVAILABLE` universe-wide, at most 2 of 4 families can be non-negative, so threshold 2 is
arithmetically unsatisfiable; the same gap forces `Tech_Z` to 66.67% of live conviction (threshold 3)
and pins DQ at 0.80 (threshold 4).

**Monitoring sleeve: 24 names** — the top 24 by post-penalty `Adj Score`, all at or above the
95.48th percentile. They carry full `mu`/`sigma`/CI forecasts and are written to
`15_predictions.json`, because a ranked name without a settleable forecast is a publishing failure,
not caution (`rules.md § Sigma Fallback Chain`).

**Recommendation to portfolio construction: `NO_TRADE`** — fewer than 5 names pass the investable
threshold (`rules.md § Stop Criteria`, Downgrade to NO_TRADE #1).

## What drives the leaderboard

With only `Tech_Z` and `Macro_Z` live, `Tech_Z` carries two-thirds of the conviction and four of its
six slots are trend-derived (`mom20`, `mom60`, `ma_align`, `macd`). The leaderboard is therefore a
60-day trend-persistence ranking with a drawdown and volume overlay — mechanically it ranks recent
winners first. This is the concrete construction behind the rank-order inversion in `02 § 0`
(weighted-mean rank IC -0.0495) and is disclosed as a limitation in `08` and `09`
rather than patched mid-series.

Sector composition of the published set: Finance 8, Health Care 6, Industrials 2, Consumer Staples 2, Basic Materials 2, Consumer Discretionary 2, Technology 2.

