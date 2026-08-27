# 05 — Factor Scores · 2026-08-27

Universe `INDEX_UNION_PCTL (n=509)` · DQ multiplier 0.80 (`L020`) ·
price basis **2026-08-27** · target date **2026-09-24** (`run_date + 28d`) ·
risk-free 3.69% annual = 0.3075% monthly (`L008`).

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

### Derived ratio definitions used in the tables below

| Metric | Formula | Inputs |
|---|---|---|
| Forecast Sharpe | `(mu - rf_1m) / sigma` | mu from the calibration table; sigma = `REALIZED_VOL_30D`; `rf_1m` = L008 annual / 12 |
| Sortino | `(mu - rf_1m) / downside_sigma_1m` | `downside_sigma_1m` = pstdev of the **negative** daily adjusted returns in the trailing 30 sessions x `sqrt(21)` |
| Information Ratio | `(mu - beta x SPY_mu) / tracking_error_1m` | `SPY_mu` = +2.0% regime prior (`03`); `tracking_error_1m` = pstdev(r - beta x r_SPY) over 60 daily intervals x `sqrt(21)` |
| Treynor | `(mu - rf_1m) / beta` | beta from the 60d regression (L500-L523) |
| Calmar-style | `(mu - rf_1m) / abs(max_drawdown_60d)` | diagnostic and negative-risk screen only |
| VaR95 / CVaR95 | `mu - 1.65 x sigma` / `mu - 2.06 x sigma` | one-month return space; normality assumed and stated |
| Raw Kelly / 0.25x Kelly | `mu / sigma^2` / `0.25 x raw` | documented fallback form (no beta-adjusted edge / tracking-error variance wired); bounded by the 5% single-name cap |

## Calibration feedback binding (read before scoring)

From `02 § 0` / L014a: `EQUITY_ALPHA` CI coverage **71.47%** is inside the
55–85% band, so the "widen sigma" binding does **not** fire and `REALIZED_VOL_30D` stands as the
sigma source. Aggregate rank IC across scored vintages is negative (mean
**-0.0840** over 60 vintages), which triggers the
`rules.md` binding: **all confidence is capped at `MEDIUM`**. No positive per-name mu adjustments
were applied — every `mu` below is the unmodified calibration-table band value for the name's
percentile.

## Ranked candidate table (top 20)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SJM | The J.M. Smucker Company Common St | 131.84 | 2026-08-27 | `DELAYED` | +0.3392 | (0.30x`UNAVL` + 0.30x+1.4397 + 0.25x`UNAVL` + 0.15x-0.0531) x 0.80 - 0.00 = +0.3392 | 100.00 | -0.6986 | 8.68% | 0.6559 | 1.2731 | 0.7058 | 1.9916 | -8.32% | -11.88% | -8.42% | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.13 / 74.47 / 62.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.68% | `REALIZED_VOL_30D` | 139.75 | 2026-09-24 | 127.85 | 151.65 | L200 | L300, L400, L500, L600, L013, L002 | MEDIUM | Consumer Staples at 100.00 pctl; Tech_Z +1.4397 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| RVTY | Revvity Inc. Common Stock | 129.71 | 2026-08-27 | `DELAYED` | +0.3357 | (0.30x`UNAVL` + 0.30x+1.3875 + 0.25x`UNAVL` + 0.15x+0.0221) x 0.80 - 0.00 = +0.3357 | 99.80 | +0.4440 | 9.93% | 0.5733 | 1.1903 | 0.4929 | 1.5216 | -10.38% | -14.45% | -6.38% | SELL_SETUP_7 / SELL_SETUP_4 / SELL_SETUP_3 | 72.24 / 71.60 / 60.14 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 9.93% | `REALIZED_VOL_30D` | 137.49 | 2026-09-24 | 124.10 | 150.89 | L201 | L301, L401, L501, L601, L013, L002 | MEDIUM | Industrials at 99.80 pctl; Tech_Z +1.3875 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| GILD | Gilead Sciences Inc. Common Stock | 148.86 | 2026-08-27 | `DELAYED` | +0.2983 | (0.30x`UNAVL` + 0.30x+0.8990 + 0.25x`UNAVL` + 0.15x+0.6874) x 0.80 - 0.00 = +0.2983 | 99.61 | +0.1043 | 7.47% | 0.7616 | 1.5365 | 0.6795 | 2.6852 | -6.33% | -9.40% | -5.96% | SELL_SETUP_9 / SELL_SETUP_4 / SELL_SETUP_1 | 69.18 / 66.84 / 71.11 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | +6.00% | 7.47% | `REALIZED_VOL_30D` | 157.79 | 2026-09-24 | 146.22 | 169.36 | L202 | L302, L402, L502, L602, L013, L002 | MEDIUM | Health Care at 99.61 pctl; Tech_Z +0.8990 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| BLK | BlackRock Inc. Common Stock | 1167.57 | 2026-08-27 | `DELAYED` | +0.2977 | (0.30x`UNAVL` + 0.30x+0.7774 + 0.25x`UNAVL` + 0.15x+0.9256) x 0.80 - 0.00 = +0.2977 | 99.41 | +0.8465 | 6.76% | 0.8416 | 1.9414 | 0.5806 | 3.2784 | -5.16% | -7.93% | -10.14% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 61.03 / 62.38 / 61.23 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 6.76% | `REALIZED_VOL_30D` | 1237.62 | 2026-09-24 | 1155.49 | 1319.76 | L203 | L303, L403, L503, L603, L013, L002 | MEDIUM | Finance at 99.41 pctl; Tech_Z +0.7774 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| AMGN | Amgen Inc. Common Stock | 436.99 | 2026-08-27 | `DELAYED` | +0.2949 | (0.30x`UNAVL` + 0.30x+1.0188 + 0.25x`UNAVL` + 0.15x+0.4200) x 0.80 - 0.00 = +0.2949 | 99.21 | +0.1414 | 7.75% | 0.7346 | 2.3263 | 0.7285 | 2.4978 | -6.79% | -9.96% | -5.05% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 68.94 / 74.38 / 71.79 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 7.75% | `REALIZED_VOL_30D` | 463.21 | 2026-09-24 | 427.99 | 498.43 | L204 | L304, L404, L504, L604, L013, L002 | MEDIUM | Health Care at 99.21 pctl; Tech_Z +1.0188 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| JNJ | Johnson & Johnson Common Stock | 265.77 | 2026-08-27 | `DELAYED` | +0.2918 | (0.30x`UNAVL` + 0.30x+0.9190 + 0.25x`UNAVL` + 0.15x+0.5937) x 0.80 - 0.00 = +0.2918 | 99.02 | -0.7412 | 6.20% | 0.9179 | 1.2779 | 1.1124 | 3.9001 | -4.23% | -6.78% | -7.57% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_9 | 54.62 / 63.93 / 77.55 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 6.20% | `REALIZED_VOL_30D` | 281.72 | 2026-09-24 | 264.57 | 298.86 | L205 | L305, L405, L505, L605, L013, L002 | MEDIUM | Health Care at 99.02 pctl; Tech_Z +0.9190 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| RMD | ResMed Inc. Common Stock | 235.76 | 2026-08-27 | `DELAYED` | +0.2915 | (0.30x`UNAVL` + 0.30x+0.9423 + 0.25x`UNAVL` + 0.15x+0.5445) x 0.80 - 0.00 = +0.2915 | 98.82 | +0.1495 | 9.85% | 0.5776 | 0.9563 | 0.5375 | 1.5446 | -10.26% | -14.30% | -12.68% | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_1 | 66.40 / 59.71 / 51.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 9.85% | `REALIZED_VOL_30D` | 249.91 | 2026-09-24 | 225.74 | 274.07 | L206 | L306, L406, L506, L606, L013, L002 | MEDIUM | Health Care at 98.82 pctl; Tech_Z +0.9423 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| A | Agilent Technologies Inc. Common S | 157.69 | 2026-08-27 | `DELAYED` | +0.2907 | (0.30x`UNAVL` + 0.30x+1.2053 + 0.25x`UNAVL` + 0.15x+0.0121) x 0.80 - 0.00 = +0.2907 | 98.62 | +0.3635 | 8.26% | 0.6891 | 1.1163 | 0.6450 | 2.1981 | -7.63% | -11.02% | -10.15% | BUY_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_4 | 70.27 / 69.14 / 60.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 8.26% | `REALIZED_VOL_30D` | 167.15 | 2026-09-24 | 153.60 | 180.70 | L207 | L307, L407, L507, L607, L013, L002 | MEDIUM | Industrials at 98.62 pctl; Tech_Z +1.2053 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| VEEV | Veeva Systems Inc. Class A Common  | 282.13 | 2026-08-27 | `DELAYED` | +0.2901 | (0.30x`UNAVL` + 0.30x+1.3802 + 0.25x`UNAVL` + 0.15x-0.3429) x 0.80 - 0.00 = +0.2901 | 98.43 | +0.4655 | 16.61% | 0.3427 | 0.9930 | 0.3424 | 0.5435 | -21.41% | -28.22% | -16.28% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 79.57 / 73.59 / 60.55 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 16.61% | `REALIZED_VOL_30D` | 299.06 | 2026-09-24 | 250.31 | 347.80 | L208 | L308, L408, L508, L608, L013, L002 | MEDIUM | Technology at 98.43 pctl; Tech_Z +1.3802 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| NWSA | News Corporation Class A Common St | 31.19 | 2026-08-27 | `DELAYED` | +0.2868 | (0.30x`UNAVL` + 0.30x+1.2435 + 0.25x`UNAVL` + 0.15x-0.0965) x 0.80 - 0.00 = +0.2868 | 98.23 | -0.3845 | 8.39% | 0.6784 | 0.9828 | 0.8330 | 2.1303 | -7.85% | -11.29% | -9.72% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 71.28 / 69.40 / 62.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 8.39% | `REALIZED_VOL_30D` | 33.06 | 2026-09-24 | 30.34 | 35.78 | L209 | L309, L409, L509, L609, L013, L002 | MEDIUM | Consumer Discretionary at 98.23 pctl; Tech_Z +1.2435 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| FTNT | Fortinet Inc. Common Stock | 172.78 | 2026-08-27 | `DELAYED` | +0.2842 | (0.30x`UNAVL` + 0.30x+1.0794 + 0.25x`UNAVL` + 0.15x+0.2095) x 0.80 - 0.00 = +0.2842 | 98.03 | +1.1979 | 12.43% | 0.4578 | 1.3919 | 0.3310 | 0.9703 | -14.52% | -19.61% | -10.40% | SELL_SETUP_3 / SELL_SETUP_2 / SELL_SETUP_6 | 64.73 / 75.31 / 80.05 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 12.43% | `REALIZED_VOL_30D` | 183.15 | 2026-09-24 | 160.81 | 205.49 | L210 | L310, L410, L510, L610, L013, L002 | MEDIUM | Technology at 98.03 pctl; Tech_Z +1.0794 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| STT | State Street Corporation Common St | 193.37 | 2026-08-27 | `DELAYED` | +0.2784 | (0.30x`UNAVL` + 0.30x+0.7371 + 0.25x`UNAVL` + 0.15x+0.8453) x 0.80 - 0.00 = +0.2784 | 97.83 | +0.6448 | 6.74% | 0.8449 | 1.1408 | 0.7246 | 3.3046 | -5.12% | -7.88% | -5.65% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 62.10 / 81.83 / 88.76 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 6.74% | `REALIZED_VOL_30D` | 204.97 | 2026-09-24 | 191.42 | 218.52 | L211 | L311, L411, L511, L611, L013, L002 | MEDIUM | Finance at 97.83 pctl; Tech_Z +0.7371 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| BNY | The Bank of New York Mellon Corpor | 162.24 | 2026-08-27 | `DELAYED` | +0.2774 | (0.30x`UNAVL` + 0.30x+0.6397 + 0.25x`UNAVL` + 0.15x+1.0325) x 0.80 - 0.00 = +0.2774 | 97.64 | +0.4917 | 5.60% | 1.0161 | 1.4353 | 0.7819 | 4.7788 | -3.24% | -5.54% | -5.69% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 57.46 / 75.98 / 91.33 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 5.60% | `REALIZED_VOL_30D` | 171.97 | 2026-09-24 | 162.52 | 181.43 | L212 | L312, L412, L512, L612, L013, L002 | MEDIUM | Finance at 97.64 pctl; Tech_Z +0.6397 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| SCHW | Charles Schwab Corporation (The) C | 108.05 | 2026-08-27 | `DELAYED` | +0.2760 | (0.30x`UNAVL` + 0.30x+0.8276 + 0.25x`UNAVL` + 0.15x+0.6445) x 0.80 - 0.00 = +0.2760 | 97.44 | -0.1050 | 5.68% | 1.0017 | 1.5782 | 0.9387 | 4.6448 | -3.38% | -5.71% | -5.36% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 51.69 / 64.25 / 66.76 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | +6.00% | 5.68% | `REALIZED_VOL_30D` | 114.53 | 2026-09-24 | 108.15 | 120.92 | L213 | L313, L413, L513, L613, L013, L002 | MEDIUM | Finance at 97.44 pctl; Tech_Z +0.8276 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| NWS | News Corporation Class B Common St | 35.32 | 2026-08-27 | `DELAYED` | +0.2752 | (0.30x`UNAVL` + 0.30x+1.1709 + 0.25x`UNAVL` + 0.15x-0.0487) x 0.80 - 0.00 = +0.2752 | 97.24 | -0.4122 | 8.74% | 0.6512 | 0.9301 | 0.7939 | 1.9632 | -8.42% | -12.01% | -10.48% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 70.10 / 67.64 / 61.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | +6.00% | 8.74% | `REALIZED_VOL_30D` | 37.44 | 2026-09-24 | 34.23 | 40.65 | L214 | L314, L414, L514, L614, L013, L002 | MEDIUM | Consumer Discretionary at 97.24 pctl; Tech_Z +1.1709 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| VRTX | Vertex Pharmaceuticals Incorporate | 547.55 | 2026-08-27 | `DELAYED` | +0.2724 | (0.30x`UNAVL` + 0.30x+0.9129 + 0.25x`UNAVL` + 0.15x+0.4441) x 0.80 - 0.00 = +0.2724 | 97.05 | +0.1165 | 8.43% | 0.6752 | 1.7498 | 0.6633 | 2.1103 | -7.91% | -11.37% | -11.12% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_2 | 65.06 / 68.87 / 63.34 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | +6.00% | 8.43% | `REALIZED_VOL_30D` | 580.40 | 2026-09-24 | 532.39 | 628.41 | L215 | L315, L415, L515, L615, L013, L002 | MEDIUM | Health Care at 97.05 pctl; Tech_Z +0.9129 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| BAC | Bank of America Corporation Common | 61.17 | 2026-08-27 | `DELAYED` | +0.2701 | (0.30x`UNAVL` + 0.30x+0.7732 + 0.25x`UNAVL` + 0.15x+0.7048) x 0.80 - 0.00 = +0.2701 | 96.85 | +0.3191 | 4.79% | 1.1895 | 1.7206 | 1.0138 | 6.5499 | -1.90% | -3.86% | -5.62% | BUY_SETUP_1 / BUY_SETUP_2 / SELL_SETUP_3 | 43.15 / 62.35 / 70.00 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 4.79% | `REALIZED_VOL_30D` | 64.84 | 2026-09-24 | 61.80 | 67.88 | L216 | L316, L416, L516, L616, L013, L002 | MEDIUM | Finance at 96.85 pctl; Tech_Z +0.7732 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| MPC | Marathon Petroleum Corporation Com | 363.54 | 2026-08-27 | `DELAYED` | +0.2670 | (0.30x`UNAVL` + 0.30x+1.3078 + 0.25x`UNAVL` + 0.15x-0.3904) x 0.80 - 0.00 = +0.2670 | 96.65 | -0.2006 | 10.59% | 0.5378 | 0.9894 | 0.6252 | 1.3387 | -11.47% | -15.81% | -9.09% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_7 | 69.54 / 76.64 / 85.17 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 10.59% | `REALIZED_VOL_30D` | 385.35 | 2026-09-24 | 345.33 | 425.37 | L217 | L317, L417, L517, L617, L013, L002 | MEDIUM | Energy at 96.65 pctl; Tech_Z +1.3078 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| CRL | Charles River Laboratories Interna | 296.41 | 2026-08-27 | `DELAYED` | +0.2641 | (0.30x`UNAVL` + 0.30x+0.9789 + 0.25x`UNAVL` + 0.15x+0.2429) x 0.80 - 0.00 = +0.2641 | 96.46 | +0.5021 | 13.32% | 0.4275 | 1.5494 | 0.4094 | 0.8460 | -15.97% | -21.43% | -6.38% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_3 | 73.88 / 77.28 / 67.05 | `BEARISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 13.32% | `REALIZED_VOL_30D` | 314.19 | 2026-09-24 | 273.15 | 355.24 | L218 | L318, L418, L518, L618, L013, L002 | MEDIUM | Health Care at 96.46 pctl; Tech_Z +0.9789 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |
| BMY | Bristol-Myers Squibb Company Commo | 66.95 | 2026-08-27 | `DELAYED` | +0.2633 | (0.30x`UNAVL` + 0.30x+0.6392 + 0.25x`UNAVL` + 0.15x+0.9162) x 0.80 - 0.00 = +0.2633 | 96.26 | +0.0222 | 6.73% | 0.8463 | 1.1608 | 0.7006 | 3.3151 | -5.10% | -7.86% | -5.71% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 60.33 / 68.54 / 66.75 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | +6.00% | 6.73% | `REALIZED_VOL_30D` | 70.97 | 2026-09-24 | 66.28 | 75.65 | L219 | L319, L419, L519, L619, L013, L002 | MEDIUM | Health Care at 96.26 pctl; Tech_Z +0.6392 | Trend-persistence construction; 2 of 4 families UNAVAILABLE |

## Score attribution — all 24 published names

`rules.md § Financial Metrics and Score Attribution` requires an `Adj Score` explanation for every
ranked **or monitored** name, so this table spans all 24 published names, not only the top 20
the ranked-candidate schema shows.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SJM | `UNAVAILABLE` | +1.4397 | `UNAVAILABLE` | -0.0531 | +0.4239 | 0.80 | 0.00 | +0.3392 | 20d volume ratio: z +2.6337 (raw 1.69x); 60d momentum: z +1.8292 (raw +32.45%); MACD state (D/W): z +1.3567 (raw +1.00) | beta proximity to 1.0: z -1.3143 (raw -1.6986); rate sensitivity vs TLT: z -0.1693 (raw -0.7618); sector 60d momentum leadership: z -0.0113 (raw +5.75%) | L300, L400, L500, L600, L013, L002 |
| RVTY | `UNAVAILABLE` | +1.3875 | `UNAVAILABLE` | +0.0221 | +0.4196 | 0.80 | 0.00 | +0.3357 | 60d momentum: z +1.7581 (raw +29.29%); 20d momentum: z +1.4802 (raw +14.24%); 20d volume ratio: z +1.4555 (raw 1.28x) | sector 60d momentum leadership: z -0.6394 (raw +1.82%); rate sensitivity vs TLT: z -0.2005 (raw -0.7785) | L301, L401, L501, L601, L013, L002 |
| GILD | `UNAVAILABLE` | +0.8990 | `UNAVAILABLE` | +0.6874 | +0.3728 | 0.80 | 0.00 | +0.2983 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); 20d momentum: z +1.3707 (raw +13.39%); MACD state (D/W): z +1.3567 (raw +1.00) | 20d volume ratio: z -0.5208 (raw 0.76x); rate sensitivity vs TLT: z -0.1815 (raw -0.7683) | L302, L402, L502, L602, L013, L002 |
| BLK | `UNAVAILABLE` | +0.7774 | `UNAVAILABLE` | +0.9256 | +0.3721 | 0.80 | 0.00 | +0.2977 | 20d volume ratio: z +1.6076 (raw 1.32x); beta proximity to 1.0: z +1.5661 (raw -0.1535); MA alignment (D/W): z +1.3419 (raw +1.00) | rate sensitivity vs TLT: z -0.0121 (raw -0.6776) | L303, L403, L503, L603, L013, L002 |
| AMGN | `UNAVAILABLE` | +1.0188 | `UNAVAILABLE` | +0.4200 | +0.3686 | 0.80 | 0.00 | +0.2949 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); 60d momentum: z +1.8292 (raw +33.90%); 20d momentum: z +1.3707 (raw +13.39%) | 20d volume ratio: z -0.8249 (raw 0.68x); rate sensitivity vs TLT: z -0.4315 (raw -0.9022); vol30/vol60 stability: z -0.2253 (raw -0.9849) | L304, L404, L504, L604, L013, L002 |
| JNJ | `UNAVAILABLE` | +0.9190 | `UNAVAILABLE` | +0.5937 | +0.3647 | 0.80 | 0.00 | +0.2918 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); MACD state (D/W): z +1.3567 (raw +1.00); MA alignment (D/W): z +1.3419 (raw +1.00) | beta proximity to 1.0: z -1.3937 (raw -1.7412) | L305, L405, L505, L605, L013, L002 |
| RMD | `UNAVAILABLE` | +0.9423 | `UNAVAILABLE` | +0.5445 | +0.3644 | 0.80 | 0.00 | +0.2915 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); 60d momentum: z +1.7611 (raw +29.33%); 20d momentum: z +1.3681 (raw +13.37%) | rate sensitivity vs TLT: z -0.4162 (raw -0.8940) | L306, L406, L506, L606, L013, L002 |
| A | `UNAVAILABLE` | +1.2053 | `UNAVAILABLE` | +0.0121 | +0.3634 | 0.80 | 0.00 | +0.2907 | 20d volume ratio: z +2.6337 (raw 1.67x); 20d momentum: z +1.4080 (raw +13.68%); MACD state (D/W): z +1.3567 (raw +1.00) | sector 60d momentum leadership: z -0.6394 (raw +1.82%); vol30/vol60 stability: z -0.3059 (raw -0.9948) | L307, L407, L507, L607, L013, L002 |
| VEEV | `UNAVAILABLE` | +1.3802 | `UNAVAILABLE` | -0.3429 | +0.3626 | 0.80 | 0.00 | +0.2901 | 20d volume ratio: z +2.6337 (raw 3.27x); 20d momentum: z +2.1952 (raw +39.97%); 60d momentum: z +1.8292 (raw +54.22%) | vol30/vol60 stability: z -1.2718 (raw -1.1133); sector 60d momentum leadership: z -1.0971 (raw -1.03%); 60d max drawdown: z -0.2611 (raw -16.28%) | L308, L408, L508, L608, L013, L002 |
| NWSA | `UNAVAILABLE` | +1.2435 | `UNAVAILABLE` | -0.0965 | +0.3586 | 0.80 | 0.00 | +0.2868 | 20d volume ratio: z +2.2537 (raw 1.49x); MACD state (D/W): z +1.3567 (raw +1.00); MA alignment (D/W): z +1.3419 (raw +1.00) | beta proximity to 1.0: z -0.7286 (raw -1.3845); vol30/vol60 stability: z -0.4661 (raw -1.0145) | L309, L409, L509, L609, L013, L002 |
| FTNT | `UNAVAILABLE` | +1.0794 | `UNAVAILABLE` | +0.2095 | +0.3552 | 0.80 | 0.00 | +0.2842 | beta proximity to 1.0: z +1.4834 (raw -0.1979); 20d volume ratio: z +1.3795 (raw 1.26x); MACD state (D/W): z +1.3567 (raw +1.50) | sector 60d momentum leadership: z -1.0971 (raw -1.03%); vol30/vol60 stability: z -0.7119 (raw -1.0446) | L310, L410, L510, L610, L013, L002 |
| STT | `UNAVAILABLE` | +0.7371 | `UNAVAILABLE` | +0.8453 | +0.3479 | 0.80 | 0.00 | +0.2784 | MACD state (D/W): z +1.3567 (raw +1.50); MA alignment (D/W): z +1.3419 (raw +1.00); beta proximity to 1.0: z +1.1901 (raw -0.3552) | 20d volume ratio: z -0.8629 (raw 0.67x); vol30/vol60 stability: z -0.0459 (raw -0.9629) | L311, L411, L511, L611, L013, L002 |
| BNY | `UNAVAILABLE` | +0.6397 | `UNAVAILABLE` | +1.0325 | +0.3468 | 0.80 | 0.00 | +0.2774 | MA alignment (D/W): z +1.3419 (raw +1.00); rate sensitivity vs TLT: z +1.1225 (raw -0.0698); sector 60d momentum leadership: z +1.1034 (raw +12.71%) | INSUFFICIENT_SOURCEABLE_DRIVERS | L312, L412, L512, L612, L013, L002 |
| SCHW | `UNAVAILABLE` | +0.8276 | `UNAVAILABLE` | +0.6445 | +0.3450 | 0.80 | 0.00 | +0.2760 | 20d volume ratio: z +1.8356 (raw 1.38x); 60d momentum: z +1.3342 (raw +23.69%); sector 60d momentum leadership: z +1.1034 (raw +12.71%) | beta proximity to 1.0: z -0.2076 (raw -1.1050) | L313, L413, L513, L613, L013, L002 |
| NWS | `UNAVAILABLE` | +1.1709 | `UNAVAILABLE` | -0.0487 | +0.3440 | 0.80 | 0.00 | +0.2752 | 20d volume ratio: z +1.9876 (raw 1.42x); MACD state (D/W): z +1.3567 (raw +1.00); MA alignment (D/W): z +1.3419 (raw +1.00) | beta proximity to 1.0: z -0.7804 (raw -1.4122); vol30/vol60 stability: z -0.3360 (raw -0.9985) | L314, L414, L514, L614, L013, L002 |
| VRTX | `UNAVAILABLE` | +0.9129 | `UNAVAILABLE` | +0.4441 | +0.3405 | 0.80 | 0.00 | +0.2724 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); 60d momentum: z +1.7218 (raw +28.81%); 20d momentum: z +1.4067 (raw +13.67%) | 20d volume ratio: z -0.7109 (raw 0.71x); rate sensitivity vs TLT: z -0.4248 (raw -0.8987); vol30/vol60 stability: z -0.0892 (raw -0.9682) | L315, L415, L515, L615, L013, L002 |
| BAC | `UNAVAILABLE` | +0.7732 | `UNAVAILABLE` | +0.7048 | +0.3377 | 0.80 | 0.00 | +0.2701 | 20d volume ratio: z +2.6337 (raw 1.64x); sector 60d momentum leadership: z +1.1034 (raw +12.71%); 60d max drawdown: z +1.0245 (raw -5.62%) | 20d momentum: z -0.4716 (raw -0.91%) | L316, L416, L516, L616, L013, L002 |
| MPC | `UNAVAILABLE` | +1.3078 | `UNAVAILABLE` | -0.3904 | +0.3338 | 0.80 | 0.00 | +0.2670 | 60d momentum: z +1.8292 (raw +38.58%); 20d momentum: z +1.7146 (raw +16.06%); MACD state (D/W): z +1.3567 (raw +1.00) | vol30/vol60 stability: z -0.5974 (raw -1.0306); rate sensitivity vs TLT: z -0.4736 (raw -0.9248); beta proximity to 1.0: z -0.3859 (raw -1.2006) | L317, L417, L517, L617, L013, L002 |
| CRL | `UNAVAILABLE` | +0.9789 | `UNAVAILABLE` | +0.2429 | +0.3301 | 0.80 | 0.00 | +0.2641 | 20d momentum: z +2.1952 (raw +26.34%); sector 60d momentum leadership: z +2.0853 (raw +18.85%); 60d momentum: z +1.8292 (raw +69.58%) | rate sensitivity vs TLT: z -1.0649 (raw -1.2415); vol30/vol60 stability: z -0.9728 (raw -1.0766); MACD state (D/W): z -0.5509 (raw -0.50) | L318, L418, L518, L618, L013, L002 |
| BMY | `UNAVAILABLE` | +0.6392 | `UNAVAILABLE` | +0.9162 | +0.3292 | 0.80 | 0.00 | +0.2633 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); 60d momentum: z +1.3819 (raw +24.32%); MACD state (D/W): z +1.3567 (raw +1.00) | 20d volume ratio: z -1.3190 (raw 0.43x) | L319, L419, L519, L619, L013, L002 |
| TGT | `UNAVAILABLE` | +1.1096 | `UNAVAILABLE` | -0.0407 | +0.3268 | 0.80 | 0.00 | +0.2614 | 60d momentum: z +1.8292 (raw +35.74%); 20d momentum: z +1.6683 (raw +15.70%); MACD state (D/W): z +1.3567 (raw +1.00) | rate sensitivity vs TLT: z -0.7277 (raw -1.0609) | L320, L420, L520, L620, L013, L002 |
| TECH | `UNAVAILABLE` | +0.4908 | `UNAVAILABLE` | +1.1583 | +0.3210 | 0.80 | 0.00 | +0.2568 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); 60d momentum: z +1.8292 (raw +45.79%); vol30/vol60 stability: z +1.8015 (raw -0.0868) | 20d volume ratio: z -1.0909 (raw 0.61x); rate sensitivity vs TLT: z -0.5287 (raw -0.9543); 20d momentum: z -0.2591 (raw +0.74%) | L321, L421, L521, L621, L013, L002 |
| PFE | `UNAVAILABLE` | +0.7495 | `UNAVAILABLE` | +0.6313 | +0.3195 | 0.80 | 0.00 | +0.2556 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); MACD state (D/W): z +1.3567 (raw +1.00); MA alignment (D/W): z +1.3419 (raw +1.00) | 20d volume ratio: z -0.4068 (raw 0.79x) | L322, L422, L522, L622, L013, L002 |
| ABT | `UNAVAILABLE` | +0.6296 | `UNAVAILABLE` | +0.8693 | +0.3193 | 0.80 | 0.00 | +0.2554 | sector 60d momentum leadership: z +2.0853 (raw +18.85%); vol30/vol60 stability: z +1.8015 (raw -0.6520); 60d momentum: z +1.7528 (raw +29.22%) | beta proximity to 1.0: z -0.8045 (raw -1.4252) | L323, L423, L523, L623, L013, L002 |

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical (momentum, MA alignment, MACD, volume, drawdown) | 509/509 | 0 | none — full coverage | all six `Tech_Z` slots sourceable universe-wide |
| Macro (beta, sector leadership, rate sensitivity, vol stability) | 509/509 | 0 | none — full coverage | all four `Macro_Z` slots sourceable universe-wide |
| Risk / return ratios (Sharpe, Sortino, IR, Treynor, Calmar) | 509/509 | 0 | none | displayed; only `dd60` enters a score slot |
| Tail risk (VaR95, CVaR95, 60d max drawdown) | 509/509 | 0 | none | `dd60` is a `Tech_Z` slot |
| Sizing (raw Kelly, 0.25x Kelly) | 509/509 | 0 | none | investability gate |
| TD-9 / RSI(14) — daily & weekly | 509/509 | 0 | none | exhaustion flags; not score slots |
| Fundamental family | 0 | 509 | **DQ 1.00 -> 0.80**; blocks evidence threshold #2 | `Fund_Z` `UNAVAILABLE` — no fetch path wired (rules.md § SHADOW Diagnostic Tooling, L021) |
| Sentiment / positioning family | 0 | 509 | **DQ 1.00 -> 0.80**; blocks evidence threshold #2 | `Sent_Z` `UNAVAILABLE` — no fetch path wired (L022) |
| Options IV / skew, short interest, bid-ask tape, analyst revisions | 0 | 509 | confidence capped `MEDIUM` | **Enhancing** inputs — never `GO` blockers (L023) |

No score above cites a metric absent from `01_preflight.md`, and no missing metric is described as
neutral or supportive: `Fund_Z` and `Sent_Z` are carried as `UNAVAILABLE` and contribute
`0.00 (UNAVAILABLE)` to the arithmetic, which is a **penalty via the data-quality multiplier**, not a
neutral pass.

## Technical indicator summary — all 24 published names

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60d Mom | RS20/60 vs SPY | Vol Ratio 20d | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|
| SJM | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.13 / 74.47 / 62.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.0057 / +2.1305 / +3.1533 | BULLISH / BULLISH / MIXED | +8.89% / +32.45% | +4.92% / +30.67% | 1.69 | L400, L013, L002 |
| RVTY | SELL_SETUP_7 / SELL_SETUP_4 / SELL_SETUP_3 | 72.24 / 71.60 / 60.14 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.9873 / +2.4107 / +4.1903 | BULLISH / BULLISH / MIXED | +14.24% / +29.29% | +10.27% / +27.51% | 1.28 | L401, L013, L002 |
| GILD | SELL_SETUP_9 / SELL_SETUP_4 / SELL_SETUP_1 | 69.18 / 66.84 / 71.11 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | +0.9693 / +1.6481 / +0.4327 | BULLISH / BULLISH / BULLISH | +13.39% / +17.46% | +9.42% / +15.68% | 0.76 | L402, L013, L002 |
| BLK | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 61.03 / 62.38 / 61.23 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -1.8894 / +16.9265 / -4.5433 | BULLISH / BULLISH / BULLISH | +6.30% / +15.23% | +2.33% / +13.45% | 1.32 | L403, L013, L002 |
| AMGN | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 68.94 / 74.38 / 71.79 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.6945 / +8.4987 / +8.7539 | BULLISH / BULLISH / BULLISH | +13.39% / +33.90% | +9.42% / +32.12% | 0.68 | L404, L013, L002 |
| JNJ | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_9 | 54.62 / 63.93 / 77.55 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.2243 / +1.0851 / +6.6013 | BULLISH / BULLISH / BULLISH | +4.40% / +19.83% | +0.43% / +18.05% | 1.10 | L405, L013, L002 |
| RMD | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_1 | 66.40 / 59.71 / 51.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.7780 / +5.7075 / -4.8500 | BULLISH / MIXED / MIXED | +13.37% / +29.33% | +9.40% / +27.55% | 1.02 | L406, L013, L002 |
| A | BUY_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_4 | 70.27 / 69.14 / 60.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.3232 / +3.5094 / +2.6042 | BULLISH / MIXED / MIXED | +13.68% / +16.99% | +9.71% / +15.21% | 1.67 | L407, L013, L002 |
| VEEV | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 79.57 / 73.59 / 60.55 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.2453 / +13.4260 / -0.9000 | BULLISH / MIXED / BULLISH | +39.97% / +54.22% | +36.00% / +52.44% | 3.27 | L408, L013, L002 |
| NWSA | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 71.28 / 69.40 / 62.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.1680 / +0.5077 / -0.0024 | BULLISH / BULLISH / BULLISH | +11.04% / +18.10% | +7.07% / +16.32% | 1.49 | L409, L013, L002 |
| FTNT | SELL_SETUP_3 / SELL_SETUP_2 / SELL_SETUP_6 | 64.73 / 75.31 / 80.05 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.3597 / +0.8214 / +8.5893 | BULLISH / BULLISH / BULLISH | +12.01% / +16.07% | +8.04% / +14.29% | 1.26 | L410, L013, L002 |
| STT | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 62.10 / 81.83 / 88.76 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0542 / +1.1981 / +7.0103 | BULLISH / BULLISH / BULLISH | +5.77% / +21.63% | +1.80% / +19.85% | 0.67 | L411, L013, L002 |
| BNY | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 57.46 / 75.98 / 91.33 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2247 / +0.7582 / +4.0894 | BULLISH / BULLISH / BULLISH | +3.95% / +15.29% | -0.02% / +13.51% | 1.04 | L412, L013, L002 |
| SCHW | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 51.69 / 64.25 / 66.76 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | -0.4818 / +1.9046 / +0.4212 | MIXED / BULLISH / BULLISH | +3.87% / +23.69% | -0.10% / +21.91% | 1.38 | L413, L013, L002 |
| NWS | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 70.10 / 67.64 / 61.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.1731 / +0.5603 / -0.1163 | BULLISH / BULLISH / BULLISH | +11.07% / +17.03% | +7.10% / +15.25% | 1.42 | L414, L013, L002 |
| VRTX | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_2 | 65.06 / 68.87 / 63.34 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | +2.3714 / +8.1878 / +4.0056 | BULLISH / BULLISH / BULLISH | +13.67% / +28.81% | +9.70% / +27.03% | 0.71 | L415, L013, L002 |
| BAC | BUY_SETUP_1 / BUY_SETUP_2 / SELL_SETUP_3 | 43.15 / 62.35 / 70.00 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.4375 / +0.4724 / +0.7361 | MIXED / BULLISH / BULLISH | -0.91% / +17.16% | -4.88% / +15.38% | 1.64 | L416, L013, L002 |
| MPC | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_7 | 69.54 / 76.64 / 85.17 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0794 / +8.2665 / +15.9171 | BULLISH / BULLISH / BULLISH | +16.06% / +38.58% | +12.09% / +36.80% | 1.16 | L417, L013, L002 |
| CRL | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_3 | 73.88 / 77.28 / 67.05 | `BEARISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.0117 / +10.5873 / +14.0259 | BULLISH / BULLISH / MIXED | +26.34% / +69.58% | +22.37% / +67.80% | 0.93 | L418, L013, L002 |
| BMY | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 60.33 / 68.54 / 66.75 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0089 / +0.7559 / +1.8693 | BULLISH / BULLISH / BULLISH | +3.22% / +24.32% | -0.75% / +22.54% | 0.43 | L419, L013, L002 |
| TGT | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_9 | 68.99 / 75.58 / 70.45 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.7489 / +2.7930 / +8.2312 | BULLISH / BULLISH / MIXED | +15.70% / +35.74% | +11.73% / +33.96% | 0.91 | L420, L013, L002 |
| TECH | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 69.49 / 65.96 / 55.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.2427 / +1.2945 / +2.5431 | BULLISH / BULLISH / MIXED | +0.74% / +45.79% | -3.23% / +44.01% | 0.61 | L421, L013, L002 |
| PFE | BUY_SETUP_1 / SELL_SETUP_6 / SELL_SETUP_1 | 65.39 / 66.78 / 58.24 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0799 / +0.3249 / +0.5595 | BULLISH / BULLISH / MIXED | +12.48% / +11.59% | +8.51% / +9.81% | 0.79 | L422, L013, L002 |
| ABT | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 57.65 / 60.30 / 50.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -0.3526 / +3.5862 / -2.4638 | BULLISH / MIXED / MIXED | +5.66% / +29.22% | +1.69% / +27.44% | 0.95 | L423, L013, L002 |

TD-9 setup `9` readings and RSI >= 70 / <= 30 are treated as exhaustion or reversal flags that inform
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
2026-10-02, so no name takes the -0.10 earnings penalty and
none is confidence-capped at `LOW` on event risk. All 24 are capped `MEDIUM` by the rank-IC
binding.

Because the sweep grounded the entire universe, the published set is **ranks 1–24 contiguous**
— there are no ungrounded names to skip, so the "first N grounded, skip ungrounded" rule that applied
on 2026-07-27 and 2026-07-28 does not engage.

## What drives the leaderboard

With two families live, the composite reduces to `0.30*Tech_Z + 0.15*Macro_Z`, so **Technical carries
66.7% of conviction and Macro 33.3%** — threshold #3 fails by
construction, not by accident. Within `Tech_Z` the six slots are equal-weighted, so momentum (20d +
60d) occupies 2 of 6 slots = 33.3% of `Tech_Z`.

The board is led by **`SJM`** (`Tech_Z` +1.4397, `Macro_Z`
-0.0531, 20d/60d momentum +8.89%/+32.45%). Sector
composition of the published 24: Health Care 10, Finance 5, Consumer Discretionary 3, Industrials 2, Technology 2, Consumer Staples 1, Energy 1.

That composition is the run's central finding and its central weakness. Published-sleeve betas span
-0.7412 to +1.1979 with a mean of +0.1484 — a defensive, low-beta
book selected by a trend-persistence score in a tape the `03` regime section calls `BULL`.
The 60-day cross-section has 42.83% of names at negative beta, and
the score's `beta` slot rewards proximity to 1.0 rather than magnitude, so it cannot pull the sleeve
up. The mechanical consequence is in `07`: the maximum sleeve beta attainable under the 5%
single-name cap is +0.2919 against a 0.90 floor.

This is the fourth consecutive claude-opus-5 package to publish a defensive book from a
trend-persistence score, and the settled evidence in `02 § 0` says the construction is
anti-correlated with forward alpha (aggregate rank IC -0.0840). The corrective — reweighting
families or shrinking the mu prior — is **Track A** and gated at `eff_n >= 3`; the ledger reports
`eff_n = 2`, so `13` records the finding and defers
rather than acting on it.
