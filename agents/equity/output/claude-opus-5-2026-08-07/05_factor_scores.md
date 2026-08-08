# 05 — Factor Scores

Universe `INDEX_UNION_PCTL (n=511)` · DQ multiplier 0.80 (`L021`) · basis 2026-08-07.

`Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide (`L022`, `L023`), so the live score is
`(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` — stated plainly rather than hidden behind a
composite that looks like it spans four families.

## Calibration feedback binding (read before scoring)

From `02 § 0`: weighted-mean rank IC is
**-0.0430** over 643 settled
`EQUITY_ALPHA` records. `rules.md § Rolling Calibration Metrics` and
`agents.md § Calibration Feedback Binding` require: **rank IC <= 0 over >= 20 settled
predictions -> cap all confidence at `MEDIUM`.** That binds this run — no name carries `HIGH`
confidence. CI coverage is 69.36%, inside the 55–85% band, so the
"widen sigma / shrink mu" branch does **not** fire and `mu` is taken from the calibration
table without positive adjustment.

## Metric Definition Table (normative)

This table is normative: if it and the running code disagree, one of them is wrong and the run
must say which. Polarity is stated as the **post-transform direction**, never as an
instruction word like "negated".

| Metric slot | Family | Source field | Window | Transform before z-score | Polarity (higher-is-better after transform) | Winsorization |
|---|---|---|---|---|---|---|
| `mom20` | Technical | `technical_indicators.json` `daily.momentum_20d_pct` | trailing 20 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `mom60` | Technical | `daily.momentum_60d_pct` | trailing 60 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `ma_align` | Technical | `daily.ma_alignment` + `weekly.ma_alignment` | daily and weekly blocks | encode `BULLISH=+1, MIXED=0, BEARISH=-1`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `macd` | Technical | `daily.macd_state` + `weekly.macd_state` | daily and weekly blocks | encode `BULLISH_CROSS=+2, ABOVE_SIGNAL=+1, ON_SIGNAL=0, BELOW_SIGNAL=-1, BEARISH_CROSS=-2`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `vol_conf` | Technical | `daily.volume_ratio_20d` | trailing 20 daily sessions | none (ratio) | **higher raw value is better** | 5th/95th pctl |
| `dd60` | Technical | worst peak-to-trough of adjusted closes | the **61 most recent daily closes** (= the 60 most recent daily return intervals) | none — the field is **already stored as a signed negative number** | **higher raw value is better** (a shallower drawdown scores higher). Do **not** apply a negation. | 5th/95th pctl |
| `beta` | Macro | regression slope of daily adjusted returns vs SPY | trailing 60 daily return intervals; `cov(r, r_SPY, ddof=0) / var(r_SPY)` | `-abs(beta - 1.0)` | **higher transformed value is better** (beta closest to 1.0 scores highest) | 5th/95th pctl |
| `sector_lead` | Macro | `daily.momentum_60d_pct` of every scored member of the sector | trailing 60 daily sessions | **median** across the sector, broadcast to each member | **higher transformed value is better** | 5th/95th pctl |
| `rate_sens` | Macro | regression slope of daily adjusted returns vs **TLT** (`L020`) | trailing 60 daily return intervals; `cov(r, r_TLT, ddof=0) / var(r_TLT)` | `-abs(beta_TLT)` | **higher transformed value is better** (lower absolute rate sensitivity scores higher) | 5th/95th pctl |
| `vol_stability` | Macro | daily adjusted returns | `vol30` = **population** stdev (`ddof=0`) of the trailing 30 daily returns x `sqrt(21)`; `vol60` likewise over 60 | `-(vol30 / vol60)` | **higher transformed value is better** (vol contracting scores higher) | 5th/95th pctl |

**Shared conventions, stated once:**

- **Input basis.** Every metric above is computed from **adjusted** closes (`L002`, Track B
  2026-07-26). Entry, target and CI prices use **raw** closes (`L003`).
- **z-score.** Winsorize the raw (post-transform) cross-section at the 5th and 95th percentiles
  by clipping, then subtract the mean and divide by the **population** standard deviation
  (`ddof=0`) *of the clipped series*.
- **Family aggregation.** Equal-weighted arithmetic mean of the family's slot z-scores.
- **Relative strength is not a slot.** `rs20`/`rs60` are computed, displayed and ledgered as
  diagnostics only.

### Same-basis reproduction check — not available this run

The 2026-08-04 package stated that this table's own falsifiability test is owed by "the next
run that shares a basis with this one". **This run does not share a basis with any prior
package**: its basis is 2026-08-07, while 2026-08-04 used 2026-08-03 and 2026-08-06 used
2026-08-05. No package exists on the 2026-08-07 basis, so the test cannot be run today and is
**still outstanding** — it is not silently marked passed. It becomes available to the next run
that shares the 2026-08-07 basis, which would be any run firing before the 2026-08-10 close.

## Ranked candidate table (top 20 of 511)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DASH | DoorDash Inc. Class A Common Stock | 216.26 | 2026-08-07 | `HISTORICAL` | +0.3755 | (0.30x0.00 UNAVL + 0.30x+1.212 + 0.25x0.00 UNAVL + 0.15x+0.705) x 0.80 - 0.00 = +0.3755 | 99.80 | 1.1917 | 12.30% | 0.463 | 0.781 | 0.269 | 0.991 | -14.30% | -19.34% | -13.26% | SELL9 / SELL2 / SELL3 | 71 / 62 / 56 | A / A / b | none <=37d | +6.00% | 12.30% | `REALIZED_VOL_30D` | 229.24 | 2026-09-04 | 201.57 | 256.90 | `L101`, `L003` | `L201`, `L019` | MEDIUM | Rank #1/511 on 20d volume ratio z +2.61 + 60d momentum z +2.06 | daily RSI 71.3 overbought; daily TD-9 setup 9 (exhaustion); weakest slot rate sensitivity vs TLT z -0.61 |
| ABNB | Airbnb Inc. Class A Common Stock | 178.07 | 2026-08-07 | `HISTORICAL` | +0.3531 | (0.30x0.00 UNAVL + 0.30x+1.542 + 0.25x0.00 UNAVL + 0.15x-0.142) x 0.80 - 0.00 = +0.3531 | 99.61 | 0.7421 | 16.69% | 0.341 | 1.171 | 0.345 | 0.538 | -21.54% | -28.38% | -7.63% | SELL3 / SELL2 / SELL9 | 79 / 75 / 66 | A / A / A | none <=37d | +6.00% | 16.69% | `REALIZED_VOL_30D` | 188.75 | 2026-09-04 | 157.84 | 219.66 | `L102`, `L003` | `L202`, `L019` | MEDIUM | Rank #2/511 on 20d volume ratio z +2.61 + 20d momentum z +1.90 | daily RSI 79.1 overbought; monthly TD-9 setup 9 (exhaustion); weakest slot vol30/vol60 contraction z -1.63 |
| GEN | Gen Digital Inc. Common Stock | 29.17 | 2026-08-07 | `HISTORICAL` | +0.3448 | (0.30x0.00 UNAVL + 0.30x+1.101 + 0.25x0.00 UNAVL + 0.15x+0.671) x 0.80 - 0.00 = +0.3448 | 99.41 | 0.4017 | 9.66% | 0.589 | 1.265 | 0.469 | 1.609 | -9.93% | -13.89% | -17.11% | SELL9 / SELL6 / SELL4 | 70 / 65 / 59 | A / A / B+ | none <=37d | +6.00% | 9.66% | `REALIZED_VOL_30D` | 30.92 | 2026-09-04 | 27.99 | 33.85 | `L103`, `L003` | `L203`, `L019` | MEDIUM | Rank #3/511 on 20d volume ratio z +2.61 + 60d momentum z +1.84 | daily TD-9 setup 9 (exhaustion); weakest slot 60d max drawdown z -0.28; low beta 0.40 — dilutes sleeve beta |
| VEEV | Veeva Systems Inc. Class A Common  | 230.47 | 2026-08-07 | `HISTORICAL` | +0.3439 | (0.30x0.00 UNAVL + 0.30x+1.225 + 0.25x0.00 UNAVL + 0.15x+0.416) x 0.80 - 0.00 = +0.3439 | 99.22 | 0.1662 | 12.86% | 0.443 | 1.131 | 0.422 | 0.908 | -15.21% | -20.48% | -18.82% | SELL9 / SELL6 / SELL2 | 76 / 63 / 52 | A / A / b | 19 | +6.00% | 12.86% | `REALIZED_VOL_30D` | 244.30 | 2026-09-04 | 213.49 | 275.11 | `L104`, `L003` | `L204`, `L019` | MEDIUM | Rank #4/511 on 20d volume ratio z +2.61 + 60d momentum z +2.06 | daily RSI 75.6 overbought; daily TD-9 setup 9 (exhaustion); weakest slot 60d max drawdown z -0.47 |
| HPQ | HP Inc. Common Stock | 30.05 | 2026-08-07 | `HISTORICAL` | +0.3231 | (0.30x0.00 UNAVL + 0.30x+1.046 + 0.25x0.00 UNAVL + 0.15x+0.601) x 0.80 - 0.00 = +0.3231 | 99.02 | 0.4424 | 13.38% | 0.425 | 0.811 | 0.307 | 0.837 | -16.08% | -21.57% | -24.35% | SELL4 / SELL4 / SELL4 | 70 / 70 / 58 | A / A / A | 19 | +6.00% | 13.38% | `REALIZED_VOL_30D` | 31.85 | 2026-09-04 | 27.67 | 36.04 | `L105`, `L003` | `L205`, `L019` | MEDIUM | Rank #5/511 on 60d momentum z +2.06 + 20d momentum z +1.90 | daily RSI 70.2 overbought; weakest slot 60d max drawdown z -1.09; low beta 0.44 — dilutes sleeve beta |
| WSM | Williams-Sonoma Inc. Common Stock  | 251.78 | 2026-08-07 | `HISTORICAL` | +0.3229 | (0.30x0.00 UNAVL + 0.30x+1.188 + 0.25x0.00 UNAVL + 0.15x+0.314) x 0.80 - 0.00 = +0.3229 | 98.83 | 0.9798 | 9.11% | 0.625 | 1.451 | 0.417 | 1.808 | -9.03% | -12.76% | -9.79% | SELL5 / SELL2 / SELL3 | 69 / 68 / 70 | A / A / A | 19 | +6.00% | 9.11% | `REALIZED_VOL_30D` | 266.89 | 2026-09-04 | 243.04 | 290.74 | `L106`, `L003` | `L206`, `L019` | MEDIUM | Rank #6/511 on 60d momentum z +2.06 + beta proximity to 1.0 z +1.62 | monthly RSI 70.4 overbought; weakest slot rate sensitivity vs TLT z -2.24 |
| TECH | Bio-Techne Corp Common Stock | 72.29 | 2026-08-07 | `HISTORICAL` | +0.3054 | (0.30x0.00 UNAVL + 0.30x+0.835 + 0.25x0.00 UNAVL + 0.15x+0.875) x 0.80 - 0.00 = +0.3054 | 98.63 | 0.7110 | 1.42% | 4.006 | 6.915 | 0.314 | 74.344 | 3.66% | 3.07% | -8.69% | SELL1 / SELL9 / SELL3 | 74 / 66 / 55 | b / A / A | none <=37d | +6.00% | 1.42% | `REALIZED_VOL_30D` | 76.63 | 2026-09-04 | 75.56 | 77.70 | `L107`, `L003` | `L207`, `L019` | MEDIUM | Rank #7/511 on 20d volume ratio z +2.52 + 60d momentum z +2.06 | daily RSI 73.7 overbought; weekly TD-9 setup 9 (exhaustion); weakest slot rate sensitivity vs TLT z -0.97 |
| DXCM | DexCom Inc. Common Stock | 84.75 | 2026-08-07 | `HISTORICAL` | +0.3045 | (0.30x0.00 UNAVL + 0.30x+0.973 + 0.25x0.00 UNAVL + 0.15x+0.592) x 0.80 - 0.00 = +0.3045 | 98.43 | 0.2453 | 15.32% | 0.371 | 0.853 | 0.383 | 0.639 | -19.28% | -25.56% | -13.86% | BUY2 / SELL4 / SELL2 | 64 / 66 / 52 | A / A / A | none <=37d | +6.00% | 15.32% | `REALIZED_VOL_30D` | 89.84 | 2026-09-04 | 76.33 | 103.34 | `L108`, `L003` | `L208`, `L019` | MEDIUM | Rank #8/511 on 60d momentum z +2.06 + MA alignment (D/W) z +1.28 | weakest slot vol30/vol60 contraction z -0.46; low beta 0.25 — dilutes sleeve beta |
| CPAY | Corpay Inc. Common Stock | 392.94 | 2026-08-07 | `HISTORICAL` | +0.2975 | (0.30x0.00 UNAVL + 0.30x+0.843 + 0.25x0.00 UNAVL + 0.15x+0.793) x 0.80 - 0.00 = +0.2975 | 98.24 | 0.2729 | 7.66% | 0.743 | 1.589 | 0.611 | 2.560 | -6.63% | -9.77% | -10.52% | SELL9 / SELL4 / SELL5 | 62 / 65 / 62 | A / A / A | none <=37d | +6.00% | 7.66% | `REALIZED_VOL_30D` | 416.52 | 2026-09-04 | 385.23 | 447.80 | `L109`, `L003` | `L209`, `L019` | MEDIUM | Rank #9/511 on vol30/vol60 contraction z +1.40 + MA alignment (D/W) z +1.28 | daily TD-9 setup 9 (exhaustion); weakest slot 60d max drawdown z +0.45; low beta 0.27 — dilutes sleeve beta |
| NTAP | NetApp Inc. Common Stock | 189.52 | 2026-08-07 | `HISTORICAL` | +0.2943 | (0.30x0.00 UNAVL + 0.30x+0.809 + 0.25x0.00 UNAVL + 0.15x+0.833) x 0.80 - 0.00 = +0.2943 | 98.04 | 1.4032 | 12.57% | 0.453 | 0.731 | 0.179 | 0.949 | -14.74% | -19.90% | -15.81% | SELL9 / SELL5 / SELL5 | 68 / 76 / 73 | A / A / A | 19 | +6.00% | 12.57% | `REALIZED_VOL_30D` | 200.89 | 2026-09-04 | 176.11 | 225.67 | `L110`, `L003` | `L210`, `L019` | MEDIUM | Rank #10/511 on 60d momentum z +2.06 + vol30/vol60 contraction z +1.96 | monthly RSI 72.7 overbought; daily TD-9 setup 9 (exhaustion); weakest slot 20d volume ratio z -0.45 |
| BAX | Baxter International Inc. Common S | 27.55 | 2026-08-07 | `HISTORICAL` | +0.2914 | (0.30x0.00 UNAVL + 0.30x+1.151 + 0.25x0.00 UNAVL + 0.15x+0.126) x 0.80 - 0.00 = +0.2914 | 97.85 | 0.6615 | 14.38% | 0.396 | 0.912 | 0.377 | 0.726 | -17.72% | -23.61% | -7.19% | BUY1 / SELL9 / SELL3 | 69 / 73 / 51 | A / A / A | none <=37d | +6.00% | 14.38% | `REALIZED_VOL_30D` | 29.20 | 2026-09-04 | 25.08 | 33.32 | `L111`, `L003` | `L211`, `L019` | MEDIUM | Rank #11/511 on 60d momentum z +2.06 + 20d momentum z +1.90 | weekly TD-9 setup 9 (exhaustion); weakest slot vol30/vol60 contraction z -1.08 |
| GPN | Global Payments Inc. Common Stock | 86.12 | 2026-08-07 | `HISTORICAL` | +0.2908 | (0.30x0.00 UNAVL + 0.30x+1.017 + 0.25x0.00 UNAVL + 0.15x+0.390) x 0.80 - 0.00 = +0.2908 | 97.65 | 0.8468 | 12.62% | 0.451 | 0.896 | 0.358 | 0.942 | -14.82% | -19.99% | -17.27% | BUY1 / SELL6 / SELL2 | 60 / 62 / 49 | A / A / A | none <=37d | +6.00% | 12.62% | `REALIZED_VOL_30D` | 91.29 | 2026-09-04 | 79.99 | 102.59 | `L112`, `L003` | `L212`, `L019` | MEDIUM | Rank #12/511 on 20d volume ratio z +2.56 + beta proximity to 1.0 z +1.55 | weakest slot rate sensitivity vs TLT z -0.63 |
| MET | MetLife Inc. Common Stock | 97.77 | 2026-08-07 | `HISTORICAL` | +0.2871 | (0.30x0.00 UNAVL + 0.30x+0.934 + 0.25x0.00 UNAVL + 0.15x+0.524) x 0.80 - 0.00 = +0.2871 | 97.46 | -0.0820 | 6.70% | 0.849 | 1.961 | 0.900 | 3.340 | -5.06% | -7.80% | -4.77% | SELL2 / SELL9 / SELL5 | 65 / 74 / 70 | A / A / A | none <=37d | +6.00% | 6.70% | `REALIZED_VOL_30D` | 103.64 | 2026-09-04 | 96.82 | 110.45 | `L113`, `L003` | `L213`, `L019` | MEDIUM | Rank #13/511 on MA alignment (D/W) z +1.28 + 60d momentum z +1.26 | weekly TD-9 setup 9 (exhaustion); weakest slot beta proximity to 1.0 z -0.14; low beta -0.08 — dilutes sleeve beta |
| SWK | Stanley Black & Decker Inc. Common | 103.89 | 2026-08-07 | `HISTORICAL` | +0.2786 | (0.30x0.00 UNAVL + 0.30x+1.196 + 0.25x0.00 UNAVL + 0.15x-0.070) x 0.80 - 0.00 = +0.2786 | 97.26 | 1.6043 | 10.51% | 0.541 | 1.225 | 0.309 | 1.357 | -11.35% | -15.66% | -8.47% | SELL9 / SELL2 / SELL9 | 70 / 73 / 62 | A / A / A | none <=37d | +6.00% | 10.51% | `REALIZED_VOL_30D` | 110.12 | 2026-09-04 | 98.76 | 121.48 | `L114`, `L003` | `L214`, `L019` | MEDIUM | Rank #14/511 on 60d momentum z +1.85 + 20d momentum z +1.82 | daily TD-9 setup 9 (exhaustion); monthly TD-9 setup 9 (exhaustion); weakest slot rate sensitivity vs TLT z -2.24 |
| PH | Parker-Hannifin Corporation Common | 1,073.87 | 2026-08-07 | `HISTORICAL` | +0.2755 | (0.30x0.00 UNAVL + 0.30x+1.082 + 0.25x0.00 UNAVL + 0.15x+0.132) x 0.80 - 0.00 = +0.2755 | 97.06 | 0.5754 | 8.54% | 0.666 | 1.181 | 0.645 | 2.057 | -8.09% | -11.59% | -6.69% | SELL5 / SELL3 / SELL2 | 74 / 70 / 73 | A / A / A | none <=37d | +6.00% | 8.54% | `REALIZED_VOL_30D` | 1,138.30 | 2026-09-04 | 1,042.94 | 1,233.67 | `L115`, `L003` | `L215`, `L019` | MEDIUM | Rank #15/511 on MA alignment (D/W) z +1.28 + 20d volume ratio z +1.28 | daily RSI 74.2 overbought; monthly RSI 72.9 overbought; weakest slot vol30/vol60 contraction z -0.65 |
| PFE | Pfizer Inc. Common Stock | 26.76 | 2026-08-07 | `HISTORICAL` | +0.2733 | (0.30x0.00 UNAVL + 0.30x+0.846 + 0.25x0.00 UNAVL + 0.15x+0.586) x 0.80 - 0.00 = +0.2733 | 96.87 | -0.0451 | 5.68% | 1.001 | 1.977 | 1.042 | 4.644 | -3.38% | -5.71% | -9.69% | SELL4 / SELL3 / SELL1 | 75 / 61 / 55 | A / B+ / A | none <=37d | +6.00% | 5.68% | `REALIZED_VOL_30D` | 28.37 | 2026-09-04 | 26.78 | 29.95 | `L116`, `L003` | `L216`, `L019` | MEDIUM | Rank #16/511 on MACD state (D/W) z +1.60 + MA alignment (D/W) z +1.28 | daily RSI 74.7 overbought; weakest slot 60d momentum z -0.20; low beta -0.05 — dilutes sleeve beta |
| TPR | Tapestry Inc. Common Stock | 162.36 | 2026-08-07 | `HISTORICAL` | +0.2713 | (0.30x0.00 UNAVL + 0.30x+1.199 + 0.25x0.00 UNAVL + 0.15x+0.695) x 0.80 - 0.10 = +0.2713 | 96.67 | 0.7401 | 8.52% | 0.668 | 0.868 | 0.519 | 2.065 | -8.06% | -11.56% | -10.35% | SELL9 / SELL2 / SELL2 | 72 / 66 / 79 | A / B+ / A | 6 | +6.00% | 8.52% | `REALIZED_VOL_30D` | 172.10 | 2026-09-04 | 157.71 | 186.49 | `L117`, `L003` | `L217`, `L019` | LOW | Rank #17/511 on MACD state (D/W) z +1.60 + 20d momentum z +1.53 | earnings in 6d (-0.10, confidence capped LOW); daily RSI 72.5 overbought; monthly RSI 78.7 overbought |
| FAST | Fastenal Company Common Stock | 51.84 | 2026-08-07 | `HISTORICAL` | +0.2693 | (0.30x0.00 UNAVL + 0.30x+0.994 + 0.25x0.00 UNAVL + 0.15x+0.255) x 0.80 - 0.00 = +0.2693 | 96.48 | 0.3731 | 7.44% | 0.765 | 1.407 | 0.784 | 2.713 | -6.27% | -9.32% | -7.90% | SELL6 / SELL1 / SELL7 | 72 / 67 / 69 | A / A / A | none <=37d | +6.00% | 7.44% | `REALIZED_VOL_30D` | 54.95 | 2026-09-04 | 50.94 | 58.96 | `L118`, `L003` | `L218`, `L019` | MEDIUM | Rank #18/511 on MA alignment (D/W) z +1.28 + 20d momentum z +1.13 | daily RSI 72.5 overbought; weakest slot vol30/vol60 contraction z -0.64; low beta 0.37 — dilutes sleeve beta |
| INSM | Insmed Incorporated Common Stock | 131.10 | 2026-08-07 | `HISTORICAL` | +0.2672 | (0.30x0.00 UNAVL + 0.30x+0.883 + 0.25x0.00 UNAVL + 0.15x+0.460) x 0.80 - 0.00 = +0.2672 | 96.28 | 0.8074 | 29.31% | 0.194 | 0.937 | 0.188 | 0.175 | -42.36% | -54.38% | -22.13% | SELL2 / SELL1 / BUY7 | 74 / 54 / 55 | A / B+ / b | none <=37d | +6.00% | 29.31% | `REALIZED_VOL_30D` | 138.97 | 2026-09-04 | 99.01 | 178.93 | `L119`, `L003` | `L219`, `L019` | MEDIUM | Rank #19/511 on 20d volume ratio z +2.59 + MACD state (D/W) z +1.60 | daily RSI 73.7 overbought; weakest slot vol30/vol60 contraction z -1.63 |
| GRMN | Garmin Ltd. Common Stock (Switzerl | 310.89 | 2026-08-07 | `HISTORICAL` | +0.2638 | (0.30x0.00 UNAVL + 0.30x+1.127 + 0.25x0.00 UNAVL + 0.15x-0.055) x 0.80 - 0.00 = +0.2638 | 96.09 | 0.2193 | 15.34% | 0.371 | 1.379 | 0.454 | 0.638 | -19.31% | -25.59% | -5.71% | SELL9 / SELL6 / SELL2 | 78 / 74 / 71 | A / A / A | none <=37d | +6.00% | 15.34% | `REALIZED_VOL_30D` | 329.54 | 2026-09-04 | 279.96 | 379.13 | `L120`, `L003` | `L220`, `L019` | MEDIUM | Rank #20/511 on 20d momentum z +1.90 + 60d momentum z +1.75 | daily RSI 77.9 overbought; monthly RSI 70.6 overbought; daily TD-9 setup 9 (exhaustion) |

`TD9` values are abbreviated (`BUY2` = `BUY_SETUP_2`, `-` = `NONE`); `MACD` is abbreviated
`B+` bullish cross, `A` above signal, `O` on signal, `b` below signal, `B-` bearish cross. Full
unabbreviated states for all 24 published names are in the technical indicator summary
below.

## Score attribution — all 24 published names

`rules.md § Financial Metrics and Score Attribution` requires an `Adj Score` explanation for
every ranked **or monitored** name, so this table spans all 24 published names rather
than the top 20 the ranked schema shows.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DASH | `UNAVAILABLE` | +1.2123 | `UNAVAILABLE` | +0.7046 | +0.4694 | 0.80 | 0.00 | +0.3755 | 20d volume ratio: z +2.61; 60d momentum: z +2.06; beta proximity to 1.0: z +1.48 | MA alignment (D/W): z +0.29; 60d max drawdown: z +0.15; rate sensitivity vs TLT: z -0.61 | `L101`, `L201`, `L301`, `L401`, `L019`, `L021` |
| ABNB | `UNAVAILABLE` | +1.5420 | `UNAVAILABLE` | -0.1416 | +0.4414 | 0.80 | 0.00 | +0.3531 | 20d volume ratio: z +2.61; 20d momentum: z +1.90; 60d momentum: z +1.73 | sector 60d momentum median: z +0.63; rate sensitivity vs TLT: z -0.93; vol30/vol60 contraction: z -1.63 | `L102`, `L202`, `L302`, `L402`, `L019`, `L021` |
| GEN | `UNAVAILABLE` | +1.1014 | `UNAVAILABLE` | +0.6706 | +0.4310 | 0.80 | 0.00 | +0.3448 | 20d volume ratio: z +2.61; 60d momentum: z +1.84; vol30/vol60 contraction: z +1.31 | MA alignment (D/W): z +0.29; sector 60d momentum median: z -0.10; 60d max drawdown: z -0.28 | `L103`, `L203`, `L303`, `L403`, `L019`, `L021` |
| VEEV | `UNAVAILABLE` | +1.2248 | `UNAVAILABLE` | +0.4162 | +0.4299 | 0.80 | 0.00 | +0.3439 | 20d volume ratio: z +2.61; 60d momentum: z +2.06; 20d momentum: z +1.90 | MA alignment (D/W): z +0.29; sector 60d momentum median: z -0.10; 60d max drawdown: z -0.47 | `L104`, `L204`, `L304`, `L404`, `L019`, `L021` |
| HPQ | `UNAVAILABLE` | +1.0457 | `UNAVAILABLE` | +0.6008 | +0.4038 | 0.80 | 0.00 | +0.3231 | 60d momentum: z +2.06; 20d momentum: z +1.90; vol30/vol60 contraction: z +1.87 | sector 60d momentum median: z -0.10; rate sensitivity vs TLT: z -0.18; 60d max drawdown: z -1.09 | `L105`, `L205`, `L305`, `L405`, `L019`, `L021` |
| WSM | `UNAVAILABLE` | +1.1881 | `UNAVAILABLE` | +0.3144 | +0.4036 | 0.80 | 0.00 | +0.3229 | 60d momentum: z +2.06; beta proximity to 1.0: z +1.62; 20d momentum: z +1.35 | sector 60d momentum median: z +0.63; 60d max drawdown: z +0.54; rate sensitivity vs TLT: z -2.24 | `L106`, `L206`, `L306`, `L406`, `L019`, `L021` |
| TECH | `UNAVAILABLE` | +0.8348 | `UNAVAILABLE` | +0.8750 | +0.3817 | 0.80 | 0.00 | +0.3054 | 20d volume ratio: z +2.52; 60d momentum: z +2.06; vol30/vol60 contraction: z +1.96 | 20d momentum: z -0.20; MACD state (D/W): z -0.32; rate sensitivity vs TLT: z -0.97 | `L107`, `L207`, `L307`, `L407`, `L019`, `L021` |
| DXCM | `UNAVAILABLE` | +0.9726 | `UNAVAILABLE` | +0.5921 | +0.3806 | 0.80 | 0.00 | +0.3045 | 60d momentum: z +2.06; MA alignment (D/W): z +1.28; 20d momentum: z +1.24 | 20d volume ratio: z +0.21; 60d max drawdown: z +0.08; vol30/vol60 contraction: z -0.46 | `L108`, `L208`, `L308`, `L408`, `L019`, `L021` |
| CPAY | `UNAVAILABLE` | +0.8432 | `UNAVAILABLE` | +0.7926 | +0.3719 | 0.80 | 0.00 | +0.2975 | vol30/vol60 contraction: z +1.40; MA alignment (D/W): z +1.28; 20d momentum: z +1.00 | 60d momentum: z +0.60; beta proximity to 1.0: z +0.50; 60d max drawdown: z +0.45 | `L109`, `L209`, `L309`, `L409`, `L019`, `L021` |
| NTAP | `UNAVAILABLE` | +0.8094 | `UNAVAILABLE` | +0.8333 | +0.3678 | 0.80 | 0.00 | +0.2943 | 60d momentum: z +2.06; vol30/vol60 contraction: z +1.96; MA alignment (D/W): z +1.28 | sector 60d momentum median: z -0.10; 60d max drawdown: z -0.14; 20d volume ratio: z -0.45 | `L110`, `L210`, `L310`, `L410`, `L019`, `L021` |
| BAX | `UNAVAILABLE` | +1.1509 | `UNAVAILABLE` | +0.1265 | +0.3642 | 0.80 | 0.00 | +0.2914 | 60d momentum: z +2.06; 20d momentum: z +1.90; sector 60d momentum median: z +1.21 | MA alignment (D/W): z +0.29; rate sensitivity vs TLT: z -0.84; vol30/vol60 contraction: z -1.08 | `L111`, `L211`, `L311`, `L411`, `L019`, `L021` |
| GPN | `UNAVAILABLE` | +1.0169 | `UNAVAILABLE` | +0.3897 | +0.3635 | 0.80 | 0.00 | +0.2908 | 20d volume ratio: z +2.56; beta proximity to 1.0: z +1.55; 60d momentum: z +1.33 | vol30/vol60 contraction: z +0.02; 60d max drawdown: z -0.30; rate sensitivity vs TLT: z -0.63 | `L112`, `L212`, `L312`, `L412`, `L019`, `L021` |
| MET | `UNAVAILABLE` | +0.9343 | `UNAVAILABLE` | +0.5238 | +0.3589 | 0.80 | 0.00 | +0.2871 | MA alignment (D/W): z +1.28; 60d momentum: z +1.26; 60d max drawdown: z +1.07 | 20d volume ratio: z +0.51; vol30/vol60 contraction: z +0.28; beta proximity to 1.0: z -0.14 | `L113`, `L213`, `L313`, `L413`, `L019`, `L021` |
| SWK | `UNAVAILABLE` | +1.1956 | `UNAVAILABLE` | -0.0698 | +0.3482 | 0.80 | 0.00 | +0.2786 | 60d momentum: z +1.85; 20d momentum: z +1.82; MA alignment (D/W): z +1.28 | vol30/vol60 contraction: z +0.60; 20d volume ratio: z +0.58; rate sensitivity vs TLT: z -2.24 | `L114`, `L214`, `L314`, `L414`, `L019`, `L021` |
| PH | `UNAVAILABLE` | +1.0821 | `UNAVAILABLE` | +0.1317 | +0.3444 | 0.80 | 0.00 | +0.2755 | MA alignment (D/W): z +1.28; 20d volume ratio: z +1.28; 20d momentum: z +1.08 | rate sensitivity vs TLT: z +0.14; sector 60d momentum median: z -0.01; vol30/vol60 contraction: z -0.65 | `L115`, `L215`, `L315`, `L415`, `L019`, `L021` |
| PFE | `UNAVAILABLE` | +0.8455 | `UNAVAILABLE` | +0.5863 | +0.3416 | 0.80 | 0.00 | +0.2733 | MACD state (D/W): z +1.60; MA alignment (D/W): z +1.28; sector 60d momentum median: z +1.21 | vol30/vol60 contraction: z +0.33; beta proximity to 1.0: z -0.07; 60d momentum: z -0.20 | `L116`, `L216`, `L316`, `L416`, `L019`, `L021` |
| TPR | `UNAVAILABLE` | +1.1992 | `UNAVAILABLE` | +0.6954 | +0.4641 | 0.80 | 0.10 | +0.2713 | MACD state (D/W): z +1.60; 20d momentum: z +1.53; beta proximity to 1.0: z +1.35 | sector 60d momentum median: z +0.63; 60d max drawdown: z +0.47; rate sensitivity vs TLT: z +0.05; earnings in 6d: -0.10 penalty | `L117`, `L217`, `L317`, `L417`, `L019`, `L021` |
| FAST | `UNAVAILABLE` | +0.9945 | `UNAVAILABLE` | +0.2555 | +0.3367 | 0.80 | 0.00 | +0.2693 | MA alignment (D/W): z +1.28; 20d momentum: z +1.13; MACD state (D/W): z +0.96 | sector 60d momentum median: z +0.63; rate sensitivity vs TLT: z +0.34; vol30/vol60 contraction: z -0.64 | `L118`, `L218`, `L318`, `L418`, `L019`, `L021` |
| INSM | `UNAVAILABLE` | +0.8834 | `UNAVAILABLE` | +0.4597 | +0.3340 | 0.80 | 0.00 | +0.2672 | 20d volume ratio: z +2.59; MACD state (D/W): z +1.60; beta proximity to 1.0: z +1.47 | MA alignment (D/W): z +0.29; 60d max drawdown: z -0.84; vol30/vol60 contraction: z -1.63 | `L119`, `L219`, `L319`, `L419`, `L019`, `L021` |
| GRMN | `UNAVAILABLE` | +1.1268 | `UNAVAILABLE` | -0.0549 | +0.3298 | 0.80 | 0.00 | +0.2638 | 20d momentum: z +1.90; 60d momentum: z +1.75; MA alignment (D/W): z +1.28 | sector 60d momentum median: z -0.01; 20d volume ratio: z -0.12; vol30/vol60 contraction: z -1.63 | `L120`, `L220`, `L320`, `L420`, `L019`, `L021` |
| EXPE | `UNAVAILABLE` | +1.1547 | `UNAVAILABLE` | -0.1140 | +0.3293 | 0.80 | 0.00 | +0.2634 | 60d momentum: z +2.06; 20d momentum: z +1.45; MA alignment (D/W): z +1.28 | 20d volume ratio: z +0.14; vol30/vol60 contraction: z -0.39; rate sensitivity vs TLT: z -1.43 | `L121`, `L221`, `L321`, `L421`, `L019`, `L021` |
| BKNG | `UNAVAILABLE` | +1.1584 | `UNAVAILABLE` | -0.1370 | +0.3270 | 0.80 | 0.00 | +0.2616 | 60d momentum: z +1.90; 20d momentum: z +1.90; 20d volume ratio: z +0.98 | MA alignment (D/W): z +0.29; vol30/vol60 contraction: z -0.61; rate sensitivity vs TLT: z -1.38 | `L122`, `L222`, `L322`, `L422`, `L019`, `L021` |
| WTW | `UNAVAILABLE` | +0.9773 | `UNAVAILABLE` | +0.2246 | +0.3269 | 0.80 | 0.00 | +0.2615 | 60d momentum: z +2.06; 20d momentum: z +1.90; rate sensitivity vs TLT: z +1.10 | 20d volume ratio: z -0.41; vol30/vol60 contraction: z -0.52; beta proximity to 1.0: z -0.59 | `L123`, `L223`, `L323`, `L423`, `L019`, `L021` |
| CRL | `UNAVAILABLE` | +0.9211 | `UNAVAILABLE` | +0.3074 | +0.3224 | 0.80 | 0.00 | +0.2579 | 60d momentum: z +2.06; 20d momentum: z +1.43; MA alignment (D/W): z +1.28 | 60d max drawdown: z +0.39; 20d volume ratio: z -0.59; rate sensitivity vs TLT: z -1.79 | `L124`, `L224`, `L324`, `L424`, `L019`, `L021` |

`Fund_Z` and `Sent_Z` display as `UNAVAILABLE`, not `0.00`, to keep the distinction visible;
per `rules.md § Family Aggregation` their **arithmetic** contribution is `0.00 (UNAVAILABLE)`
and they do not count toward the 3-of-4 threshold. No missing metric is described as neutral or
supportive anywhere in this package.

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical / Price (6 slots) | 511/511 | 0 | none | `Tech_Z` fully live; carries 0.30 of 0.45 live weight |
| Macro / Regime (4 slots) | 511/511 | 0 | none | `Macro_Z` fully live; carries 0.15 of 0.45 live weight |
| Fundamental (5 signals) | 0/511 | 511 | DQ -> 0.80; blocks evidence threshold #2 | no XBRL fetch path at universe scale (`L022`) |
| Sentiment / Positioning (5 signals) | 0/511 | 511 | DQ -> 0.80; blocks evidence threshold #2 | no short-interest / revision / IV feed (`L023`) |
| Risk / return ratios | 24/24 | 0 | none | rf sourced (`L006`), so ratios are not `RAW_DIAGNOSTIC` |
| Tail risk | 24/24 | 0 | none | VaR95/CVaR95 parametric; normality stated |
| Sizing (Kelly) | 24/24 | 0 | confidence capped where 0.25xKelly < 2% NAV | see the Kelly column in the ranked table |

## Technical indicator summary — all 24 published names

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60 Mom D | 20/60 Mom W | 20/60 Mom M | RS20/60 vs SPY D | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|
| DASH | SELL_SETUP_9 / SELL_SETUP_2 / SELL_SETUP_3 | 71.3 / 62.2 / 56.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | +2.454 / +6.442 / -5.367 | BULLISH / MIXED / BULLISH | +12.74% / +39.35% | +38.06% / -1.23% | +28.92% / +12.99% | +10.31% / +34.33% | `L019`, `L002` |
| ABNB | SELL_SETUP_3 / SELL_SETUP_2 / SELL_SETUP_9 | 79.1 / 75.0 / 65.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +1.926 / +2.831 / +4.473 | BULLISH / BULLISH / BULLISH | +19.82% / +31.44% | +38.55% / +31.38% | +35.51% / +14.89% | +17.39% / +26.42% | `L019`, `L002` |
| GEN | SELL_SETUP_9 / SELL_SETUP_6 / SELL_SETUP_4 | 69.8 / 65.2 / 58.7 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | +0.149 / +0.684 / +0.078 | BULLISH / MIXED / BULLISH | +12.58% / +33.06% | +39.85% / -0.14% | +9.58% / +21.33% | +10.15% / +28.04% | `L019`, `L002` |
| VEEV | SELL_SETUP_9 / SELL_SETUP_6 / SELL_SETUP_2 | 75.6 / 63.4 / 52.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | +2.403 / +8.829 / -4.197 | BULLISH / MIXED / BULLISH | +21.22% / +44.57% | +25.21% / -18.43% | +9.62% / -30.58% | +18.79% / +39.55% | `L019`, `L002` |
| HPQ | SELL_SETUP_4 / SELL_SETUP_4 / SELL_SETUP_4 | 70.2 / 69.5 / 58.2 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +0.298 / +0.720 / +0.672 | BULLISH / BULLISH / MIXED | +24.07% / +44.29% | +66.48% / +32.52% | -1.07% / +21.61% | +21.64% / +39.27% | `L019`, `L002` |
| WSM | SELL_SETUP_5 / SELL_SETUP_2 / SELL_SETUP_3 | 69.0 / 68.4 / 70.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +2.009 / +3.871 / +3.275 | BULLISH / BULLISH / BULLISH | +13.92% / +44.03% | +42.15% / +66.48% | +39.48% / +196.44% | +11.49% / +39.01% | `L019`, `L002` |
| TECH | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 73.7 / 65.7 / 55.3 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | -0.544 / +2.136 / +2.529 | BULLISH / MIXED / MIXED | +1.39% / +52.73% | +40.68% / +43.96% | +1.25% / -40.80% | -1.04% / +47.71% | `L019`, `L002` |
| DXCM | BUY_SETUP_2 / SELL_SETUP_4 / SELL_SETUP_2 | 64.3 / 65.9 / 52.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +0.938 / +1.672 / +2.825 | BULLISH / BULLISH / MIXED | +13.06% / +38.62% | +26.59% / +3.37% | +8.98% / -35.97% | +10.63% / +33.60% | `L019`, `L002` |
| CPAY | SELL_SETUP_9 / SELL_SETUP_4 / SELL_SETUP_5 | 62.5 / 64.9 / 61.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +1.330 / +4.761 / +6.026 | BULLISH / BULLISH / BULLISH | +11.11% / +16.14% | +36.69% / +21.56% | +16.11% / +49.25% | +8.68% / +11.12% | `L019`, `L002` |
| NTAP | SELL_SETUP_9 / SELL_SETUP_5 / SELL_SETUP_5 | 67.6 / 76.0 / 72.7 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +1.759 / +3.828 / +8.180 | BULLISH / BULLISH / BULLISH | +12.23% / +63.55% | +88.97% / +92.83% | +68.76% / +138.79% | +9.80% / +58.53% | `L019`, `L002` |
| BAX | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 68.8 / 72.6 / 50.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +0.321 / +0.954 / +1.310 | BULLISH / MIXED / MIXED | +21.79% / +54.08% | +70.68% / -9.26% | -3.71% / -60.00% | +19.36% / +49.06% | `L019`, `L002` |
| GPN | BUY_SETUP_1 / SELL_SETUP_6 / SELL_SETUP_2 | 60.1 / 62.2 / 49.2 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +0.031 / +2.137 / +1.909 | BULLISH / MIXED / MIXED | +13.26% / +26.00% | +26.20% / +16.93% | -21.68% / -44.41% | +10.83% / +20.98% | `L019`, `L002` |
| MET | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_5 | 65.3 / 74.3 / 69.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +0.087 / +1.568 / +1.605 | BULLISH / BULLISH / BULLISH | +7.34% / +25.10% | +44.59% / +31.00% | +25.46% / +83.30% | +4.91% / +20.08% | `L019`, `L002` |
| SWK | SELL_SETUP_9 / SELL_SETUP_2 / SELL_SETUP_9 | 69.9 / 72.8 / 62.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +1.043 / +1.939 / +4.179 | BULLISH / BULLISH / MIXED | +17.76% / +33.11% | +56.06% / +66.45% | +38.40% / -35.67% | +15.33% / +28.09% | `L019`, `L002` |
| PH | SELL_SETUP_5 / SELL_SETUP_3 / SELL_SETUP_2 | 74.2 / 70.2 / 72.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +8.584 / +10.029 / +10.712 | BULLISH / BULLISH / BULLISH | +11.71% / +21.85% | +20.34% / +65.60% | +71.19% / +284.75% | +9.28% / +16.83% | `L019`, `L002` |
| PFE | SELL_SETUP_4 / SELL_SETUP_3 / SELL_SETUP_1 | 74.7 / 61.1 / 55.0 | ABOVE_SIGNAL / BULLISH_CROSS / ABOVE_SIGNAL | +0.221 / +0.009 / +0.479 | BULLISH / BULLISH / MIXED | +12.65% / +5.25% | +2.62% / +18.71% | +13.75% / -24.32% | +10.22% / +0.23% | `L019`, `L002` |
| TPR | SELL_SETUP_9 / SELL_SETUP_2 / SELL_SETUP_2 | 72.5 / 65.8 / 78.7 | ABOVE_SIGNAL / BULLISH_CROSS / ABOVE_SIGNAL | +1.841 / +0.462 / +2.798 | BULLISH / BULLISH / BULLISH | +15.37% / +23.60% | +15.58% / +108.40% | +153.93% / +358.41% | +12.94% / +18.58% | `L019`, `L002` |
| FAST | SELL_SETUP_6 / SELL_SETUP_1 / SELL_SETUP_7 | 72.5 / 66.5 / 69.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +0.529 / +0.408 / +0.306 | BULLISH / BULLISH / BULLISH | +12.12% / +20.32% | +19.75% / +26.19% | +49.66% / +109.40% | +9.69% / +15.30% | `L019`, `L002` |
| INSM | SELL_SETUP_2 / SELL_SETUP_1 / BUY_SETUP_7 | 73.7 / 53.6 / 55.4 | ABOVE_SIGNAL / BULLISH_CROSS / BELOW_SIGNAL | +2.501 / +2.053 / -7.207 | BULLISH / MIXED / BULLISH | +13.40% / +13.02% | -3.60% / +32.79% | +89.89% / +367.55% | +10.97% / +8.00% | `L019`, `L002` |
| GRMN | SELL_SETUP_9 / SELL_SETUP_6 / SELL_SETUP_2 | 77.9 / 74.2 / 70.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +5.088 / +5.856 / +5.644 | BULLISH / BULLISH / BULLISH | +27.88% / +31.77% | +34.39% / +57.66% | +54.44% / +98.39% | +25.45% / +26.75% | `L019`, `L002` |
| EXPE | SELL_SETUP_9 / SELL_SETUP_2 / SELL_SETUP_3 | 66.1 / 68.4 / 68.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +2.571 / +7.027 / +5.844 | BULLISH / BULLISH / BULLISH | +14.71% / +40.57% | +32.38% / +89.05% | +68.80% / +117.67% | +12.28% / +35.55% | `L019`, `L002` |
| BKNG | SELL_SETUP_3 / SELL_SETUP_2 / SELL_SETUP_3 | 73.2 / 65.3 / 61.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | +2.406 / +5.142 / -3.313 | BULLISH / MIXED / BULLISH | +20.20% / +33.88% | +24.28% / +2.03% | +9.21% / +138.05% | +17.77% / +28.86% | `L019`, `L002` |
| WTW | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 79.8 / 69.1 / 61.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | +2.882 / +10.307 / -1.639 | BULLISH / MIXED / BULLISH | +19.05% / +37.64% | +19.22% / +18.17% | +12.10% / +67.06% | +16.62% / +32.62% | `L019`, `L002` |
| CRL | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_3 | 76.2 / 72.7 / 63.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | +2.821 / +7.866 / +12.180 | BULLISH / BULLISH / MIXED | +14.60% / +58.57% | +74.15% / +78.98% | +44.90% / -39.74% | +12.17% / +53.55% | `L019`, `L002` |

## Investable determination

| Sleeve | Count | Basis |
|---|---|---|
| Investable (5–10 target) | **0** | evidence thresholds #2, #3 and #4 fail for every name in the universe |
| Monitoring sleeve | **24** | post-penalty ranks 1–24 of 511; every name carries mu and sigma so each is settleable |
| Near-miss rejection log | 78 | names in the >=80th-pctl pool (102 total) that fall outside the published 24 |

The published set is post-penalty ranks 1–24, **contiguous** with no skipped names:
the forward calendar sweep grounded the earnings date for the entire universe, so the
"skip ungrounded names" rule that produced rank jumps on 2026-07-27 and 2026-07-28 does not
apply. 1 of the 24 published names carry the 14-day earnings penalty
(TPR).

**Fewer than 5 names pass the investable threshold, so factor scoring recommends `NO_TRADE`.**
The recommendation is unconditional on candidate quality: thresholds #2 and #3 cannot be
satisfied by any name while two families are dark.

## What drives the leaderboard

With `Tech_Z` at 0.30 of 0.45 live weight (66.67%) and `Macro_Z` at
33.33%, the ranking is dominated by trend persistence. That is a known
structural weakness, not a feature: it mechanically ranks the trailing 60-day winners first and
is anti-correlated with forward returns through a rotation, which is the mechanism behind the
negative rank IC quoted above. It is disclosed here so no reader mistakes the leaderboard for a
multi-factor consensus.
