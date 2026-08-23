# 05 — Factor Scores · 2026-08-14

Universe `INDEX_UNION_PCTL (n=511)` · DQ multiplier 0.80 (`L020`) ·
basis 2026-08-14.

`Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide (`L021`, `L022`), so the live score is
`(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` — stated plainly rather than hidden
behind a composite that looks like it spans four families.

## Calibration feedback binding (read before scoring)

From `02 § 0`: weighted-mean rank IC is **-0.0630** over 950 settled `EQUITY_ALPHA`
records. `rules.md § Rolling Calibration Metrics` and `agents.md § Calibration Feedback Binding`
require: **rank IC <= 0 over >= 20 settled predictions -> cap all confidence at `MEDIUM`.**
That binds this run — no name carries `HIGH` confidence. CI coverage is
70.84%, inside the 55–85% band, so the "widen sigma / shrink mu" branch
does **not** fire and `mu` is taken from the calibration table without positive adjustment.

## Metric Definition Table (normative)

This table is normative: if it and the running code disagree, one of them is wrong and the run
must say which. Polarity is stated as the **post-transform direction**, never as an instruction
word like "negated".

| Metric slot | Family | Source field | Window | Transform before z-score | Polarity (higher-is-better after transform) | Winsorization |
|---|---|---|---|---|---|---|
| `mom20` | Technical | `technical_indicators.json` `daily.momentum_20d_pct` | trailing 20 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `mom60` | Technical | `daily.momentum_60d_pct` | trailing 60 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `ma_align` | Technical | `daily.ma_alignment` + `weekly.ma_alignment` | daily and weekly blocks | encode `BULLISH=+1, MIXED=0, BEARISH=-1`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `macd` | Technical | `daily.macd_state` + `weekly.macd_state` | daily and weekly blocks | encode `BULLISH_CROSS=+2, ABOVE_SIGNAL=+1, ON_SIGNAL=0, BELOW_SIGNAL=-1, BEARISH_CROSS=-2`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `vol_conf` | Technical | `daily.volume_ratio_20d` — the helper's **2-dp rounded** field, not a re-derivation | trailing 20 daily sessions | none (ratio) | **higher raw value is better** | 5th/95th pctl |
| `dd60` | Technical | worst peak-to-trough of adjusted closes | the **61 most recent daily closes** (= the 60 most recent daily return intervals) | none — the field is **already stored as a signed negative number** | **higher raw value is better** (a shallower drawdown scores higher). Do **not** apply a negation. | 5th/95th pctl |
| `beta_prox` | Macro | regression slope of daily adjusted returns vs SPY | trailing 60 daily return intervals; `cov(r, r_SPY, ddof=0) / var(r_SPY)` | `-abs(beta - 1.0)` | **higher transformed value is better** (beta closest to 1.0 scores highest) | 5th/95th pctl |
| `sector_lead` | Macro | `daily.momentum_60d_pct` of every scored member of the sector | trailing 60 daily sessions | **median** across the sector, broadcast to each member | **higher transformed value is better** | 5th/95th pctl |
| `rate_sens` | Macro | regression slope of daily adjusted returns vs **TLT** (`L018`) | trailing 60 daily return intervals; `cov(r, r_TLT, ddof=0) / var(r_TLT)` | `-abs(beta_TLT)` | **higher transformed value is better** (lower absolute rate sensitivity scores higher) | 5th/95th pctl |
| `vol_stability` | Macro | daily adjusted returns | `vol30` = **population** stdev (`ddof=0`) of the trailing 30 daily returns x `sqrt(21)`; `vol60` likewise over 60 | `-(vol30 / vol60)` | **higher transformed value is better** (vol contracting scores higher) | 5th/95th pctl |

**Shared conventions, stated once:**

- **Input basis.** Every metric above is computed from **adjusted** closes (`L002`, Track B
  2026-07-26). Entry, target and CI prices use **raw** closes (`L003`).
- **z-score.** Winsorize the raw (post-transform) cross-section at the 5th and 95th percentiles
  by clipping (linear interpolation between order statistics), then subtract the mean and
  divide by the **population** standard deviation (`ddof=0`) *of the clipped series*.
- **Family aggregation.** Equal-weighted arithmetic mean of the family's slot z-scores.
- **Relative strength is not a slot.** `rs20`/`rs60` are computed, displayed and ledgered as
  diagnostics only.

### Winsorization bounds actually applied this run

| Slot | Family | 5th pctl (clip low) | 95th pctl (clip high) |
|---|---|---|---|
| `mom20` — 20d momentum | Technical | -7.9850 | +20.8900 |
| `mom60` — 60d momentum | Technical | -12.4300 | +39.9800 |
| `ma_align` — MA alignment (D/W) | Technical | -0.5000 | +1.0000 |
| `macd` — MACD state (D/W) | Technical | -1.0000 | +1.0000 |
| `vol_conf` — 20d volume ratio | Technical | +0.4400 | +1.1850 |
| `dd60` — 60d max drawdown | Technical | -0.3659 | -0.0516 |
| `beta_prox` — beta proximity to 1.0 | Macro | -1.9621 | -0.0862 |
| `sector_lead` — sector 60d momentum median | Macro | +0.3200 | +15.4550 |
| `rate_sens` — rate sensitivity vs TLT | Macro | -2.4221 | -0.0441 |
| `vol_stability` — vol30/vol60 contraction | Macro | -1.1774 | -0.7297 |

### Same-basis reproduction check — **executed this run**

The 2026-08-04 package created this table's own falsifiability test and owed it to "the next
run that shares a basis with this one". No run has shared a basis with a prior package since,
so the test has now been outstanding for three consecutive packages (08-04, 08-07 and this
one). Rather than mark it outstanding a fourth time, this run executed it **retrospectively**:
the engine was pointed at a history tree truncated to the **2026-08-07** basis (with
indicators recomputed on that truncated tree) and its output compared field-by-field against
the published `claude-opus-5-2026-08-07` package.

| Check | Result |
|---|---|
| Scored universe | **511 — matches** the published `n=511` |
| Rejection log | **identical** — `BF-B`, `EA`, `FDXF`, `Q`, same reasons |
| Rank order (top 24, penalties removed) | **identical** |
| Entry prices | **exact**, all 24 (max diff 0.0000) |
| `max_drawdown_60d` | **exact**, all 24 |
| `sigma` (`REALIZED_VOL_30D`) | **exact**, all 24 |
| Information Ratio | **exact**, all 24 |
| Sortino | **exact**, all 24 |
| `Macro_Z` | max abs diff **1.9e-06** (exact within published precision) |
| `Tech_Z` | max abs diff **4.0e-03** |
| 9 of 10 metric slots | max abs diff **<= 0.005** — the rounding floor of the published 2-dp driver strings |
| `vol_conf` slot | max abs diff **0.0287** — **a real residual gap** |

**Two findings, both acted on.**

1. **The test caught a live bug in this run's engine.** The first pass scored 510 names, not
   511, because the screener lookup lacked the `SATS -> ECHO` alias (EchoStar's rename) that
   the price fetch already had, so `SATS` dropped on `MARKET_CAP_UNAVAILABLE`. Fixed before any
   scoring in this package was produced. A one-name cross-section difference had shifted every
   `Tech_Z` by ~0.005 — small, but it would have propagated into every published score.
2. **`vol_conf` does not fully reproduce.** The gap is not explained by the winsorization
   convention: five percentile interpolation methods (`linear`, `lower`, `higher`, `midpoint`,
   `nearest`) were tested and `linear` fits best at 0.0287, none closing it. Re-deriving the
   volume ratio at full precision from the CSVs fits **worse** (0.0394), which confirms the
   helper's 2-dp rounded `volume_ratio_20d` is the correct input — that convention is now
   written into the table above, where it was previously implicit. The residual remains
   unexplained and is disclosed rather than papered over, exactly as the 2026-08-04 package did
   for `rate_sens`.

The check is therefore **passed with one disclosed residual**, and its retrospective form is
this run's proposed process change (`13`).

## Ranked candidate table (top 20 of 511)

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Metric Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NTAP | NetApp Inc. Common Stock | 207.08 | 2026-08-14 | `HISTORICAL` | +0.4243 | (0.30x0.00 UNAVL + 0.30x+1.311 + 0.25x0.00 UNAVL + 0.15x+0.914) x 0.80 - 0.00 = +0.4243 | 100.00 | +1.4251 | 12.73% | 0.447 | 0.673 | 0.175 | 0.926 | -15.00% | -20.22% | -15.81% | SELL9 / SELL6 / SELL5 | 77 / 80 / 75 | A / A / A | 19 | +6.00% | 12.73% | `REALIZED_VOL_30D` | 219.50 | 2026-09-11 | 192.09 | 246.92 | `L101`, `L003` | `L201`, `L301`, `L013` | MEDIUM | Rank #1/511 on 60d momentum z +2.17 + 20d momentum z +2.06 | daily RSI 76.7 overbought; monthly RSI 75.3 overbought; daily TD-9 setup 9 (exhaustion) |
| CRL | Charles River Laboratories Interna | 280.05 | 2026-08-14 | `HISTORICAL` | +0.3507 | (0.30x0.00 UNAVL + 0.30x+1.338 + 0.25x0.00 UNAVL + 0.15x+0.246) x 0.80 - 0.00 = +0.3507 | 99.80 | +0.5249 | 13.51% | 0.421 | 1.711 | 0.361 | 0.821 | -16.30% | -21.84% | -6.38% | SELL8 / SELL9 / SELL3 | 76 / 75 / 65 | A / A / A | none <=37d | +6.00% | 13.51% | `REALIZED_VOL_30D` | 296.85 | 2026-09-11 | 257.49 | 336.21 | `L102`, `L003` | `L202`, `L302`, `L013` | MEDIUM | Rank #2/511 on 60d momentum z +2.17 + 20d momentum z +2.06 | daily RSI 76.2 overbought; weekly TD-9 setup 9 (exhaustion); weakest slot rate sensitivity vs TLT z -1.20 |
| MDT | Medtronic plc. Ordinary Shares | 91.27 | 2026-08-14 | `HISTORICAL` | +0.3247 | (0.30x0.00 UNAVL + 0.30x+0.992 + 0.25x0.00 UNAVL + 0.15x+0.723) x 0.80 - 0.00 = +0.3247 | 99.61 | -0.1816 | 7.65% | 0.744 | 0.919 | 0.721 | 2.564 | -6.62% | -9.76% | -6.17% | SELL8 / SELL9 / SELL1 | 71 / 61 / 53 | A / A / b | 18 | +6.00% | 7.65% | `REALIZED_VOL_30D` | 96.75 | 2026-09-11 | 89.49 | 104.01 | `L103`, `L003` | `L203`, `L303`, `L013` | MEDIUM | Rank #3/511 on 20d volume ratio z +2.43 + sector 60d momentum median z +1.26 | daily RSI 71.1 overbought; weekly TD-9 setup 9 (exhaustion); weakest slot beta proximity to 1.0 z -0.33 |
| AME | AMETEK Inc. | 254.79 | 2026-08-14 | `HISTORICAL` | +0.3216 | (0.30x0.00 UNAVL + 0.30x+1.105 + 0.25x0.00 UNAVL + 0.15x+0.470) x 0.80 - 0.00 = +0.3216 | 99.41 | +0.9610 | 5.94% | 0.959 | 1.644 | 0.764 | 4.257 | -3.79% | -6.23% | -4.38% | SELL4 / SELL4 / SELL9 | 63 / 73 / 70 | A / A / A | none <=37d | +6.00% | 5.94% | `REALIZED_VOL_30D` | 270.08 | 2026-09-11 | 254.35 | 285.81 | `L104`, `L003` | `L204`, `L304`, `L013` | MEDIUM | Rank #4/511 on 20d volume ratio z +2.43 + beta proximity to 1.0 z +1.66 | weakest slot rate sensitivity vs TLT z -0.20 |
| KKR | KKR & Co. Inc. Common Stock | 114.01 | 2026-08-14 | `HISTORICAL` | +0.3026 | (0.30x0.00 UNAVL + 0.30x+1.059 + 0.25x0.00 UNAVL + 0.15x+0.404) x 0.80 - 0.00 = +0.3026 | 99.22 | +1.1600 | 11.31% | 0.503 | 1.072 | 0.395 | 1.174 | -12.65% | -17.29% | -10.13% | SELL4 / SELL7 / SELL3 | 69 / 62 / 52 | A / A / b | none <=37d | +6.00% | 11.31% | `REALIZED_VOL_30D` | 120.85 | 2026-09-11 | 107.45 | 134.26 | `L105`, `L003` | `L205`, `L305`, `L013` | MEDIUM | Rank #5/511 on 20d volume ratio z +2.43 + beta proximity to 1.0 z +1.53 | weakest slot vol30/vol60 contraction z -0.96 |
| DXCM | DexCom Inc. Common Stock | 89.75 | 2026-08-14 | `HISTORICAL` | +0.2886 | (0.30x0.00 UNAVL + 0.30x+0.985 + 0.25x0.00 UNAVL + 0.15x+0.435) x 0.80 - 0.00 = +0.2886 | 99.02 | +0.5629 | 14.94% | 0.381 | 0.931 | 0.366 | 0.672 | -18.65% | -24.77% | -13.86% | SELL5 / SELL5 / SELL2 | 67 / 70 / 54 | A / A / A | none <=37d | +6.00% | 14.94% | `REALIZED_VOL_30D` | 95.14 | 2026-09-11 | 81.19 | 109.08 | `L106`, `L003` | `L206`, `L306`, `L013` | MEDIUM | Rank #6/511 on 60d momentum z +1.74 + 20d momentum z +1.58 | weakest slot vol30/vol60 contraction z -1.12 |
| ABNB | Airbnb Inc. Class A Common Stock | 184.06 | 2026-08-14 | `HISTORICAL` | +0.2866 | (0.30x0.00 UNAVL + 0.30x+1.298 + 0.25x0.00 UNAVL + 0.15x-0.207) x 0.80 - 0.00 = +0.2866 | 98.82 | +0.7466 | 16.82% | 0.338 | 1.208 | 0.340 | 0.530 | -21.75% | -28.64% | -7.63% | BUY1 / SELL3 / SELL9 | 75 / 77 / 67 | A / A / A | none <=37d | +6.00% | 16.82% | `REALIZED_VOL_30D` | 195.10 | 2026-09-11 | 162.91 | 227.29 | `L107`, `L003` | `L207`, `L307`, `L013` | MEDIUM | Rank #7/511 on 60d momentum z +2.17 + 20d momentum z +2.06 | daily RSI 75.0 overbought; weakest slot vol30/vol60 contraction z -1.70 |
| WTW | Willis Towers Watson Public Limite | 331.59 | 2026-08-14 | `HISTORICAL` | +0.2845 | (0.30x0.00 UNAVL + 0.30x+1.006 + 0.25x0.00 UNAVL + 0.15x+0.358) x 0.80 - 0.00 = +0.2845 | 98.63 | -0.3695 | 8.64% | 0.659 | 1.945 | 0.796 | 2.009 | -8.26% | -11.80% | -4.15% | BUY2 / SELL8 / SELL2 | 63 / 63 / 59 | b / A / b | none <=37d | +6.00% | 8.64% | `REALIZED_VOL_30D` | 351.49 | 2026-09-11 | 321.69 | 381.28 | `L108`, `L003` | `L208`, `L308`, `L013` | MEDIUM | Rank #8/511 on 20d volume ratio z +2.43 + 60d momentum z +1.51 | weakest slot beta proximity to 1.0 z -0.67; low beta -0.37 — dilutes sleeve beta |
| EXPE | Expedia Group Inc. Common Stock | 332.69 | 2026-08-14 | `HISTORICAL` | +0.2826 | (0.30x0.00 UNAVL + 0.30x+1.233 + 0.25x0.00 UNAVL + 0.15x-0.112) x 0.80 - 0.00 = +0.2826 | 98.43 | +0.4131 | 11.56% | 0.492 | 0.934 | 0.438 | 1.123 | -13.07% | -17.81% | -5.25% | SELL9 / SELL3 / SELL3 | 74 / 72 / 71 | A / A / A | none <=37d | +6.00% | 11.56% | `REALIZED_VOL_30D` | 352.65 | 2026-09-11 | 312.66 | 392.65 | `L109`, `L003` | `L209`, `L309`, `L013` | MEDIUM | Rank #9/511 on 60d momentum z +2.17 + 20d momentum z +2.06 | daily RSI 73.6 overbought; monthly RSI 70.8 overbought; daily TD-9 setup 9 (exhaustion) |
| JCI | Johnson Controls International plc | 153.64 | 2026-08-14 | `HISTORICAL` | +0.2767 | (0.30x0.00 UNAVL + 0.30x+0.664 + 0.25x0.00 UNAVL + 0.15x+0.978) x 0.80 - 0.00 = +0.2767 | 98.24 | +1.2486 | 7.14% | 0.798 | 2.238 | 0.407 | 2.946 | -5.77% | -8.70% | -6.62% | SELL1 / SELL4 / SELL9 | 61 / 66 / 73 | A / B+ / A | none <=37d | +6.00% | 7.14% | `REALIZED_VOL_30D` | 162.86 | 2026-09-11 | 151.46 | 174.26 | `L110`, `L003` | `L210`, `L310`, `L013` | MEDIUM | Rank #10/511 on vol30/vol60 contraction z +1.99 + beta proximity to 1.0 z +1.37 | monthly RSI 73.1 overbought; weakest slot 20d volume ratio z -0.17 |
| BAC | Bank of America Corporation Common | 64.49 | 2026-08-14 | `HISTORICAL` | +0.2753 | (0.30x0.00 UNAVL + 0.30x+0.851 + 0.25x0.00 UNAVL + 0.15x+0.592) x 0.80 - 0.00 = +0.2753 | 98.04 | +0.3282 | 5.12% | 1.111 | 1.393 | 1.045 | 5.721 | -2.45% | -4.55% | -2.74% | SELL9 / SELL9 / SELL3 | 68 / 75 / 74 | A / A / A | none <=37d | +6.00% | 5.12% | `REALIZED_VOL_30D` | 68.36 | 2026-09-11 | 64.93 | 71.79 | `L111`, `L003` | `L211`, `L311`, `L013` | MEDIUM | Rank #11/511 on 60d momentum z +1.28 + sector 60d momentum median z +1.23 | monthly RSI 73.6 overbought; daily TD-9 setup 9 (exhaustion); weekly TD-9 setup 9 (exhaustion) |
| MRK | Merck & Company Inc. Common Stock  | 135.84 | 2026-08-14 | `HISTORICAL` | +0.2720 | (0.30x0.00 UNAVL + 0.30x+0.817 + 0.25x0.00 UNAVL + 0.15x+0.633) x 0.80 - 0.00 = +0.2720 | 97.84 | -0.4080 | 6.91% | 0.823 | 1.400 | 0.804 | 3.137 | -5.41% | -8.24% | -6.78% | SELL6 / SELL8 / SELL9 | 69 / 67 / 70 | A / A / A | none <=37d | +6.00% | 6.91% | `REALIZED_VOL_30D` | 143.99 | 2026-09-11 | 134.22 | 153.76 | `L112`, `L003` | `L212`, `L312`, `L013` | MEDIUM | Rank #12/511 on vol30/vol60 contraction z +1.40 + sector 60d momentum median z +1.26 | monthly RSI 70.0 overbought; weakest slot beta proximity to 1.0 z -0.74; low beta -0.41 — dilutes sleeve beta |
| SOLV | Solventum Corporation Common Stock | 88.59 | 2026-08-14 | `HISTORICAL` | +0.2582 | (0.30x0.00 UNAVL + 0.30x+1.055 + 0.25x0.00 UNAVL + 0.15x+0.042) x 0.80 - 0.00 = +0.2582 | 97.65 | -0.0655 | 10.94% | 0.520 | 1.037 | 0.598 | 1.253 | -12.05% | -16.54% | -10.79% | SELL3 / SELL3 / SELL3 | 63 / 63 / 61 | B+ / A / `UNAVL` | none <=37d | +6.00% | 10.94% | `REALIZED_VOL_30D` | 93.91 | 2026-09-11 | 83.83 | 103.98 | `L113`, `L003` | `L213`, `L313`, `L013` | MEDIUM | Rank #13/511 on 20d volume ratio z +2.35 + sector 60d momentum median z +1.26 | weakest slot vol30/vol60 contraction z -0.79; low beta -0.07 — dilutes sleeve beta |
| BX | Blackstone Inc. Common Stock | 143.93 | 2026-08-14 | `HISTORICAL` | +0.2535 | (0.30x0.00 UNAVL + 0.30x+0.720 + 0.25x0.00 UNAVL + 0.15x+0.672) x 0.80 - 0.00 = +0.2535 | 97.45 | +1.0951 | 10.86% | 0.524 | 1.233 | 0.360 | 1.271 | -11.92% | -16.38% | -11.64% | SELL9 / SELL7 / SELL3 | 64 / 64 / 55 | A / A / b | none <=37d | +6.00% | 10.86% | `REALIZED_VOL_30D` | 152.57 | 2026-09-11 | 136.31 | 168.83 | `L114`, `L003` | `L214`, `L314`, `L013` | MEDIUM | Rank #14/511 on beta proximity to 1.0 z +1.65 + 20d momentum z +1.26 | daily TD-9 setup 9 (exhaustion); weakest slot rate sensitivity vs TLT z -0.37 |
| URI | United Rentals Inc. Common Stock | 1,153.83 | 2026-08-14 | `HISTORICAL` | +0.2523 | (0.30x0.00 UNAVL + 0.30x+0.971 + 0.25x0.00 UNAVL + 0.15x+0.161) x 0.80 - 0.00 = +0.2523 | 97.25 | +0.6718 | 12.35% | 0.461 | 1.210 | 0.432 | 0.983 | -14.38% | -19.45% | -11.13% | SELL1 / SELL2 / SELL5 | 59 / 64 / 68 | A / A / A | none <=37d | +6.00% | 12.35% | `REALIZED_VOL_30D` | 1,223.06 | 2026-09-11 | 1,074.81 | 1,371.31 | `L115`, `L003` | `L215`, `L315`, `L013` | MEDIUM | Rank #15/511 on 20d volume ratio z +1.24 + beta proximity to 1.0 z +1.22 | weakest slot vol30/vol60 contraction z -1.17 |
| SCHW | Charles Schwab Corporation (The) C | 111.09 | 2026-08-14 | `HISTORICAL` | +0.2510 | (0.30x0.00 UNAVL + 0.30x+0.676 + 0.25x0.00 UNAVL + 0.15x+0.740) x 0.80 - 0.00 = +0.2510 | 97.06 | -0.1643 | 5.52% | 1.030 | 1.671 | 0.908 | 4.914 | -3.12% | -5.38% | -7.04% | SELL3 / SELL9 / SELL2 | 76 / 72 / 68 | A / A / B+ | none <=37d | +6.00% | 5.52% | `REALIZED_VOL_30D` | 117.76 | 2026-09-11 | 111.37 | 124.14 | `L116`, `L003` | `L216`, `L316`, `L013` | MEDIUM | Rank #16/511 on vol30/vol60 contraction z +1.50 + sector 60d momentum median z +1.23 | daily RSI 76.4 overbought; weekly TD-9 setup 9 (exhaustion); weakest slot beta proximity to 1.0 z -0.29 |
| STT | State Street Corporation Common St | 191.74 | 2026-08-14 | `HISTORICAL` | +0.2506 | (0.30x0.00 UNAVL + 0.30x+0.676 + 0.25x0.00 UNAVL + 0.15x+0.737) x 0.80 - 0.00 = +0.2506 | 96.86 | +0.6830 | 7.00% | 0.813 | 1.347 | 0.734 | 3.062 | -5.55% | -8.42% | -5.65% | SELL9 / SELL9 / SELL9 | 67 / 88 / 89 | B+ / A / A | none <=37d | +6.00% | 7.00% | `REALIZED_VOL_30D` | 203.24 | 2026-09-11 | 189.29 | 217.20 | `L117`, `L003` | `L217`, `L317`, `L013` | MEDIUM | Rank #17/511 on 60d momentum z +1.27 + beta proximity to 1.0 z +1.24 | monthly RSI 88.6 overbought; daily TD-9 setup 9 (exhaustion); weekly TD-9 setup 9 (exhaustion) |
| AMGN | Amgen Inc. Common Stock | 415.21 | 2026-08-14 | `HISTORICAL` | +0.2490 | (0.30x0.00 UNAVL + 0.30x+0.884 + 0.25x0.00 UNAVL + 0.15x+0.306) x 0.80 - 0.00 = +0.2490 | 96.67 | +0.0836 | 7.78% | 0.732 | 2.094 | 0.770 | 2.479 | -6.83% | -10.02% | -5.05% | BUY1 / SELL8 / SELL2 | 70 / 71 / 69 | A / A / A | none <=37d | +6.00% | 7.78% | `REALIZED_VOL_30D` | 440.12 | 2026-09-11 | 406.54 | 473.71 | `L118`, `L003` | `L218`, `L318`, `L013` | MEDIUM | Rank #18/511 on sector 60d momentum median z +1.26 + MA alignment (D/W) z +1.22 | daily RSI 70.0 overbought; weakest slot vol30/vol60 contraction z -0.46; low beta 0.08 — dilutes sleeve beta |
| FITB | Fifth Third Bancorp Common Stock | 58.06 | 2026-08-14 | `HISTORICAL` | +0.2425 | (0.30x0.00 UNAVL + 0.30x+0.618 + 0.25x0.00 UNAVL + 0.15x+0.785) x 0.80 - 0.00 = +0.2425 | 96.47 | +0.3388 | 5.73% | 0.993 | 1.151 | 0.788 | 4.564 | -3.46% | -5.81% | -4.83% | SELL3 / SELL2 / SELL9 | 59 / 66 / 71 | b / A / A | none <=37d | +6.00% | 5.73% | `REALIZED_VOL_30D` | 61.54 | 2026-09-11 | 58.08 | 65.01 | `L119`, `L003` | `L219`, `L319`, `L013` | MEDIUM | Rank #19/511 on 20d volume ratio z +1.34 + sector 60d momentum median z +1.23 | monthly RSI 71.5 overbought; weakest slot 20d momentum z -0.57; low beta 0.34 — dilutes sleeve beta |
| BNY | The Bank of New York Mellon Corpor | 163.24 | 2026-08-14 | `HISTORICAL` | +0.2396 | (0.30x0.00 UNAVL + 0.30x+0.686 + 0.25x0.00 UNAVL + 0.15x+0.625) x 0.80 - 0.00 = +0.2396 | 96.27 | +0.5161 | 6.98% | 0.815 | 1.585 | 0.802 | 3.074 | -5.53% | -8.39% | -5.69% | SELL9 / SELL9 / SELL9 | 67 / 83 / 91 | A / A / A | none <=37d | +6.00% | 6.98% | `REALIZED_VOL_30D` | 173.03 | 2026-09-11 | 161.18 | 184.89 | `L120`, `L003` | `L220`, `L320`, `L013` | MEDIUM | Rank #20/511 on sector 60d momentum median z +1.23 + MA alignment (D/W) z +1.22 | monthly RSI 91.5 overbought; daily TD-9 setup 9 (exhaustion); weekly TD-9 setup 9 (exhaustion) |

`TD9` values are abbreviated (`BUY2` = `BUY_SETUP_2`, `-` = `NONE`); `MACD` is abbreviated
`B+` bullish cross, `A` above signal, `O` on signal, `b` below signal, `B-` bearish cross.
Full unabbreviated states for all 24 published names are in the technical indicator
summary below.

## Score attribution — all 24 published names

`rules.md § Financial Metrics and Score Attribution` requires an `Adj Score` explanation for
every ranked **or monitored** name, so this table spans all 24 published names
rather than the top 20 the ranked schema shows.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NTAP | `UNAVAILABLE` | +1.3110 | `UNAVAILABLE` | +0.9142 | +0.5304 | 0.80 | 0.00 | +0.4243 | 60d momentum: z +2.17; 20d momentum: z +2.06; vol30/vol60 contraction: z +1.99 | rate sensitivity vs TLT: z +0.66; sector 60d momentum median: z -0.03; 60d max drawdown: z -0.15 | `L101`, `L201`, `L301`, `L401`, `L013`, `L019` |
| CRL | `UNAVAILABLE` | +1.3382 | `UNAVAILABLE` | +0.2463 | +0.4384 | 0.80 | 0.00 | +0.3507 | 60d momentum: z +2.17; 20d momentum: z +2.06; sector 60d momentum median: z +1.26 | 20d volume ratio: z +0.48; vol30/vol60 contraction: z -0.03; rate sensitivity vs TLT: z -1.20 | `L102`, `L202`, `L302`, `L402`, `L013`, `L019` |
| MDT | `UNAVAILABLE` | +0.9916 | `UNAVAILABLE` | +0.7231 | +0.4059 | 0.80 | 0.00 | +0.3247 | 20d volume ratio: z +2.43; sector 60d momentum median: z +1.26; MACD state (D/W): z +1.17 | 60d momentum: z +0.51; MA alignment (D/W): z +0.25; beta proximity to 1.0: z -0.33 | `L103`, `L203`, `L303`, `L403`, `L013`, `L019` |
| AME | `UNAVAILABLE` | +1.1048 | `UNAVAILABLE` | +0.4703 | +0.4020 | 0.80 | 0.00 | +0.3216 | 20d volume ratio: z +2.43; beta proximity to 1.0: z +1.66; MA alignment (D/W): z +1.22 | 20d momentum: z +0.37; sector 60d momentum median: z -0.14; rate sensitivity vs TLT: z -0.20 | `L104`, `L204`, `L304`, `L404`, `L013`, `L019` |
| KKR | `UNAVAILABLE` | +1.0588 | `UNAVAILABLE` | +0.4038 | +0.3782 | 0.80 | 0.00 | +0.3026 | 20d volume ratio: z +2.43; beta proximity to 1.0: z +1.53; sector 60d momentum median: z +1.23 | MA alignment (D/W): z +0.25; rate sensitivity vs TLT: z -0.19; vol30/vol60 contraction: z -0.96 | `L105`, `L205`, `L305`, `L405`, `L013`, `L019` |
| DXCM | `UNAVAILABLE` | +0.9854 | `UNAVAILABLE` | +0.4345 | +0.3608 | 0.80 | 0.00 | +0.2886 | 60d momentum: z +1.74; 20d momentum: z +1.58; sector 60d momentum median: z +1.26 | 20d volume ratio: z +0.13; 60d max drawdown: z +0.07; vol30/vol60 contraction: z -1.12 | `L106`, `L206`, `L306`, `L406`, `L013`, `L019` |
| ABNB | `UNAVAILABLE` | +1.2977 | `UNAVAILABLE` | -0.2073 | +0.3582 | 0.80 | 0.00 | +0.2866 | 60d momentum: z +2.17; 20d momentum: z +2.06; beta proximity to 1.0: z +1.36 | sector 60d momentum median: z +0.32; rate sensitivity vs TLT: z -0.82; vol30/vol60 contraction: z -1.70 | `L107`, `L207`, `L307`, `L407`, `L013`, `L019` |
| WTW | `UNAVAILABLE` | +1.0064 | `UNAVAILABLE` | +0.3580 | +0.3556 | 0.80 | 0.00 | +0.2845 | 20d volume ratio: z +2.43; 60d momentum: z +1.51; sector 60d momentum median: z +1.23 | MACD state (D/W): z -0.27; vol30/vol60 contraction: z -0.28; beta proximity to 1.0: z -0.67 | `L108`, `L208`, `L308`, `L408`, `L013`, `L019` |
| EXPE | `UNAVAILABLE` | +1.2333 | `UNAVAILABLE` | -0.1117 | +0.3532 | 0.80 | 0.00 | +0.2826 | 60d momentum: z +2.17; 20d momentum: z +2.06; MA alignment (D/W): z +1.22 | vol30/vol60 contraction: z +0.01; 20d volume ratio: z -0.28; rate sensitivity vs TLT: z -1.54 | `L109`, `L209`, `L309`, `L409`, `L013`, `L019` |
| JCI | `UNAVAILABLE` | +0.6638 | `UNAVAILABLE` | +0.9783 | +0.3459 | 0.80 | 0.00 | +0.2767 | vol30/vol60 contraction: z +1.99; beta proximity to 1.0: z +1.37; MA alignment (D/W): z +1.22 | 60d momentum: z +0.26; sector 60d momentum median: z -0.14; 20d volume ratio: z -0.17 | `L110`, `L210`, `L310`, `L410`, `L013`, `L019` |
| BAC | `UNAVAILABLE` | +0.8511 | `UNAVAILABLE` | +0.5922 | +0.3442 | 0.80 | 0.00 | +0.2753 | 60d momentum: z +1.28; sector 60d momentum median: z +1.23; MA alignment (D/W): z +1.22 | 20d volume ratio: z +0.28; 20d momentum: z +0.09; vol30/vol60 contraction: z +0.01 | `L111`, `L211`, `L311`, `L411`, `L013`, `L019` |
| MRK | `UNAVAILABLE` | +0.8167 | `UNAVAILABLE` | +0.6329 | +0.3399 | 0.80 | 0.00 | +0.2720 | vol30/vol60 contraction: z +1.40; sector 60d momentum median: z +1.26; MA alignment (D/W): z +1.22 | rate sensitivity vs TLT: z +0.61; 20d momentum: z +0.25; beta proximity to 1.0: z -0.74 | `L112`, `L212`, `L312`, `L412`, `L013`, `L019` |
| SOLV | `UNAVAILABLE` | +1.0548 | `UNAVAILABLE` | +0.0421 | +0.3228 | 0.80 | 0.00 | +0.2582 | 20d volume ratio: z +2.35; sector 60d momentum median: z +1.26; MA alignment (D/W): z +1.22 | beta proximity to 1.0: z -0.12; rate sensitivity vs TLT: z -0.19; vol30/vol60 contraction: z -0.79 | `L113`, `L213`, `L313`, `L413`, `L013`, `L019` |
| BX | `UNAVAILABLE` | +0.7205 | `UNAVAILABLE` | +0.6716 | +0.3169 | 0.80 | 0.00 | +0.2535 | beta proximity to 1.0: z +1.65; 20d momentum: z +1.26; 60d momentum: z +1.24 | vol30/vol60 contraction: z +0.18; 20d volume ratio: z +0.08; rate sensitivity vs TLT: z -0.37 | `L114`, `L214`, `L314`, `L414`, `L013`, `L019` |
| URI | `UNAVAILABLE` | +0.9707 | `UNAVAILABLE` | +0.1610 | +0.3154 | 0.80 | 0.00 | +0.2523 | 20d volume ratio: z +1.24; beta proximity to 1.0: z +1.22; MA alignment (D/W): z +1.22 | sector 60d momentum median: z +0.32; rate sensitivity vs TLT: z +0.27; vol30/vol60 contraction: z -1.17 | `L115`, `L215`, `L315`, `L415`, `L013`, `L019` |
| SCHW | `UNAVAILABLE` | +0.6757 | `UNAVAILABLE` | +0.7403 | +0.3137 | 0.80 | 0.00 | +0.2510 | vol30/vol60 contraction: z +1.50; sector 60d momentum median: z +1.23; MACD state (D/W): z +1.17 | 20d volume ratio: z +0.33; MA alignment (D/W): z +0.25; beta proximity to 1.0: z -0.29 | `L116`, `L216`, `L316`, `L416`, `L013`, `L019` |
| STT | `UNAVAILABLE` | +0.6756 | `UNAVAILABLE` | +0.7370 | +0.3132 | 0.80 | 0.00 | +0.2506 | 60d momentum: z +1.27; beta proximity to 1.0: z +1.24; sector 60d momentum median: z +1.23 | 20d momentum: z +0.06; vol30/vol60 contraction: z -0.38; 20d volume ratio: z -0.68 | `L117`, `L217`, `L317`, `L417`, `L013`, `L019` |
| AMGN | `UNAVAILABLE` | +0.8843 | `UNAVAILABLE` | +0.3063 | +0.3112 | 0.80 | 0.00 | +0.2490 | sector 60d momentum median: z +1.26; MA alignment (D/W): z +1.22; MACD state (D/W): z +1.17 | beta proximity to 1.0: z +0.16; 20d volume ratio: z -0.38; vol30/vol60 contraction: z -0.46 | `L118`, `L218`, `L318`, `L418`, `L013`, `L019` |
| FITB | `UNAVAILABLE` | +0.6180 | `UNAVAILABLE` | +0.7848 | +0.3031 | 0.80 | 0.00 | +0.2425 | 20d volume ratio: z +1.34; sector 60d momentum median: z +1.23; MA alignment (D/W): z +1.22 | rate sensitivity vs TLT: z +0.15; MACD state (D/W): z -0.27; 20d momentum: z -0.57 | `L119`, `L219`, `L319`, `L419`, `L013`, `L019` |
| BNY | `UNAVAILABLE` | +0.6861 | `UNAVAILABLE` | +0.6246 | +0.2995 | 0.80 | 0.00 | +0.2396 | sector 60d momentum median: z +1.23; MA alignment (D/W): z +1.22; MACD state (D/W): z +1.17 | 20d volume ratio: z +0.03; 20d momentum: z -0.04; vol30/vol60 contraction: z -0.82 | `L120`, `L220`, `L320`, `L420`, `L013`, `L019` |
| IVZ | `UNAVAILABLE` | +0.8548 | `UNAVAILABLE` | +0.2824 | +0.2988 | 0.80 | 0.00 | +0.2390 | sector 60d momentum median: z +1.23; MA alignment (D/W): z +1.22; MACD state (D/W): z +1.17 | 60d max drawdown: z +0.35; rate sensitivity vs TLT: z +0.00; vol30/vol60 contraction: z -0.57 | `L121`, `L221`, `L321`, `L421`, `L013`, `L019` |
| DASH | `UNAVAILABLE` | +0.8459 | `UNAVAILABLE` | +0.2741 | +0.2949 | 0.80 | 0.00 | +0.2359 | 60d momentum: z +2.17; 20d momentum: z +1.68; beta proximity to 1.0: z +1.31 | 60d max drawdown: z +0.14; 20d volume ratio: z -0.33; rate sensitivity vs TLT: z -1.08 | `L122`, `L222`, `L322`, `L422`, `L013`, `L019` |
| TECH | `UNAVAILABLE` | +0.4950 | `UNAVAILABLE` | +0.9508 | +0.2911 | 0.80 | 0.00 | +0.2329 | 60d momentum: z +2.17; vol30/vol60 contraction: z +1.99; beta proximity to 1.0: z +1.36 | 20d momentum: z -0.53; 20d volume ratio: z -0.68; rate sensitivity vs TLT: z -0.80 | `L123`, `L223`, `L323`, `L423`, `L013`, `L019` |
| REGN | `UNAVAILABLE` | +0.7308 | `UNAVAILABLE` | +0.4743 | +0.2904 | 0.80 | 0.00 | +0.2323 | 20d momentum: z +1.79; 60d momentum: z +1.27; sector 60d momentum median: z +1.26 | MA alignment (D/W): z +0.25; vol30/vol60 contraction: z -0.68; 20d volume ratio: z -0.88 | `L124`, `L224`, `L324`, `L424`, `L013`, `L019` |

## Metric availability

| Metric Group | Sourceable Count | `UNAVAILABLE` Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, beta, TE) | 511 | 0 | none | computed from fetched adjusted returns + `rf` (`L012`) |
| Tail risk (dd60, VaR95, CVaR95) | 511 | 0 | none | dd60 empirical over 61 closes; VaR/CVaR parametric from sigma |
| Sizing (Kelly raw, 0.25x Kelly) | 511 | 0 | none | `mu / sigma^2` fallback, disclosed |
| Technical (TD-9, RSI, MACD, MA, momentum, volume, RS) | 511 | 0 | none | `technical_indicators.py` (`L013`) |
| Fundamental / quality | 0 | 511 | **DQ 1.00 -> 0.80; family excluded from 3-of-4** | no fetch path at universe scale (`L021`) |
| Sentiment / positioning | 0 | 511 | **DQ contribution; family excluded from 3-of-4** | no fetch path at universe scale (`L022`) |

Data completeness is **80%**, below the 85% floor in
`rules.md § Evidence Thresholds` item 4. Combined with only 2 of 4 families being available
(item 2) and Technical carrying 66.7% of live conviction (item 3), **no name in
this universe can be marked investable**, regardless of its score.

## Technical indicator summary — all 24 published names

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60 Mom D | RS20/60 vs SPY | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|
| NTAP | `SELL_SETUP_9` / `SELL_SETUP_6` / `SELL_SETUP_5` | 76.71 / 79.87 / 75.31 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.2068 / +4.9078 / +9.3001 | BULLISH / BULLISH / BULLISH | +26.36% / +72.24% | +21.91% / +66.16% | `L201`, `L013`, `L002` |
| CRL | `SELL_SETUP_8` / `SELL_SETUP_9` / `SELL_SETUP_3` | 76.21 / 74.79 / 65.10 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +3.3113 / +9.2101 / +12.9818 | BULLISH / BULLISH / MIXED | +24.83% / +83.72% | +20.38% / +77.64% | `L202`, `L013`, `L002` |
| MDT | `SELL_SETUP_8` / `SELL_SETUP_9` / `SELL_SETUP_1` | 71.12 / 61.07 / 53.42 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +0.4314 / +1.5459 / -0.7982 | BULLISH / MIXED / BULLISH | +9.70% / +17.20% | +5.25% / +11.12% | `L203`, `L013`, `L002` |
| AME | `SELL_SETUP_4` / `SELL_SETUP_4` / `SELL_SETUP_9` | 62.97 / 73.43 / 69.76 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.8078 / +1.3708 / +3.9259 | BULLISH / BULLISH / BULLISH | +7.51% / +15.32% | +3.06% / +9.24% | `L204`, `L013`, `L002` |
| KKR | `SELL_SETUP_4` / `SELL_SETUP_7` / `SELL_SETUP_3` | 68.65 / 61.61 / 52.01 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.1209 / +2.6230 / -3.7218 | BULLISH / MIXED / MIXED | +13.16% / +22.93% | +8.71% / +16.85% | `L205`, `L013`, `L002` |
| DXCM | `SELL_SETUP_5` / `SELL_SETUP_5` / `SELL_SETUP_2` | 67.39 / 69.63 / 54.43 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.9338 / +2.0902 / +3.1441 | BULLISH / BULLISH / MIXED | +17.09% / +34.06% | +12.64% / +27.98% | `L206`, `L013`, `L002` |
| ABNB | `BUY_SETUP_1` / `SELL_SETUP_3` / `SELL_SETUP_9` | 74.99 / 76.87 / 66.97 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +3.3648 / +4.1427 / +4.8550 | BULLISH / BULLISH / BULLISH | +26.09% / +40.33% | +21.64% / +34.25% | `L207`, `L013`, `L002` |
| WTW | `BUY_SETUP_2` / `SELL_SETUP_8` / `SELL_SETUP_2` | 63.13 / 63.12 / 58.76 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | -1.2126 / +10.2275 / -2.4830 | BULLISH / MIXED / BULLISH | +13.00% / +30.92% | +8.55% / +24.84% | `L208`, `L013`, `L002` |
| EXPE | `SELL_SETUP_9` / `SELL_SETUP_3` / `SELL_SETUP_3` | 73.60 / 72.25 / 70.83 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +2.2964 / +9.0755 / +7.2489 | BULLISH / BULLISH / BULLISH | +23.78% / +55.07% | +19.33% / +48.99% | `L209`, `L013`, `L002` |
| JCI | `SELL_SETUP_1` / `SELL_SETUP_4` / `SELL_SETUP_9` | 60.93 / 66.21 / 73.06 | `ABOVE_SIGNAL` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | +0.5379 / +0.2707 / +2.6412 | BULLISH / BULLISH / BULLISH | +9.38% / +13.77% | +4.93% / +7.69% | `L210`, `L013`, `L002` |
| BAC | `SELL_SETUP_9` / `SELL_SETUP_9` / `SELL_SETUP_3` | 68.45 / 74.71 / 73.63 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.0104 / +0.9692 / +0.9479 | BULLISH / BULLISH / BULLISH | +5.26% / +27.86% | +0.81% / +21.78% | `L211`, `L013`, `L002` |
| MRK | `SELL_SETUP_6` / `SELL_SETUP_8` / `SELL_SETUP_9` | 68.81 / 66.55 / 70.04 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.4117 / +0.6726 / +4.4636 | BULLISH / BULLISH / MIXED | +6.54% / +19.76% | +2.09% / +13.68% | `L212`, `L013`, `L002` |
| SOLV | `SELL_SETUP_3` / `SELL_SETUP_3` / `SELL_SETUP_3` | 63.17 / 62.98 / 60.62 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `UNAVAILABLE` | +0.0415 / +1.3187 / `UNAVL` | BULLISH / BULLISH / UNAVAILABLE | +8.95% / +18.55% | +4.50% / +12.47% | `L213`, `L013`, `L002` |
| BX | `SELL_SETUP_9` / `SELL_SETUP_7` / `SELL_SETUP_3` | 63.93 / 63.84 / 54.80 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.3027 / +3.5215 / -2.6005 | BULLISH / MIXED / BULLISH | +14.57% / +27.25% | +10.12% / +21.17% | `L214`, `L013`, `L002` |
| URI | `SELL_SETUP_1` / `SELL_SETUP_2` / `SELL_SETUP_5` | 59.01 / 64.08 / 67.78 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.3551 / +10.5956 / +24.2608 | BULLISH / BULLISH / BULLISH | +10.58% / +24.60% | +6.13% / +18.52% | `L215`, `L013`, `L002` |
| SCHW | `SELL_SETUP_3` / `SELL_SETUP_9` / `SELL_SETUP_2` | 76.37 / 72.07 / 68.25 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | +0.1712 / +2.1202 / +0.6152 | BULLISH / MIXED / BULLISH | +9.70% / +21.35% | +5.25% / +15.27% | `L216`, `L013`, `L002` |
| STT | `SELL_SETUP_9` / `SELL_SETUP_9` / `SELL_SETUP_9` | 67.31 / 87.66 / 88.57 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.1426 / +1.8509 / +6.9063 | BULLISH / BULLISH / BULLISH | +5.06% / +27.71% | +0.61% / +21.63% | `L217`, `L013`, `L002` |
| AMGN | `BUY_SETUP_1` / `SELL_SETUP_8` / `SELL_SETUP_2` | 70.05 / 70.74 / 69.24 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +1.8408 / +5.9498 / +7.2521 | BULLISH / BULLISH / BULLISH | +13.36% / +25.54% | +8.91% / +19.46% | `L218`, `L013`, `L002` |
| FITB | `SELL_SETUP_3` / `SELL_SETUP_2` / `SELL_SETUP_9` | 59.40 / 66.20 / 71.45 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.0434 / +0.3697 / +1.1513 | BULLISH / BULLISH / BULLISH | +0.09% / +22.84% | -4.36% / +16.76% | `L219`, `L013`, `L002` |
| BNY | `SELL_SETUP_9` / `SELL_SETUP_9` / `SELL_SETUP_9` | 66.72 / 83.26 / 91.45 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.1529 / +1.3043 / +4.1532 | BULLISH / BULLISH / BULLISH | +4.30% / +20.22% | -0.15% / +14.14% | `L220`, `L013`, `L002` |
| IVZ | `SELL_SETUP_2` / `SELL_SETUP_6` / `SELL_SETUP_9` | 67.48 / 71.19 / 72.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +0.1162 / +0.4133 / +0.8190 | BULLISH / BULLISH / BULLISH | +10.59% / +23.79% | +6.14% / +17.71% | `L221`, `L013`, `L002` |
| DASH | `SELL_SETUP_1` / `SELL_SETUP_3` / `SELL_SETUP_3` | 68.38 / 62.45 / 56.57 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | +1.2991 / +7.1434 / -5.3183 | BULLISH / MIXED / BULLISH | +17.86% / +40.33% | +13.41% / +34.25% | `L222`, `L013`, `L002` |
| TECH | `SELL_SETUP_1` / `SELL_SETUP_9` / `SELL_SETUP_3` | 72.50 / 65.85 / 55.39 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | -0.4215 / +1.8681 / +2.5357 | BULLISH / BULLISH / MIXED | +0.39% / +59.23% | -4.06% / +53.15% | `L223`, `L013`, `L002` |
| REGN | `BUY_SETUP_1` / `SELL_SETUP_8` / `SELL_SETUP_1` | 77.35 / 65.31 / 55.44 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | +5.2250 / +15.9241 / +14.2521 | BULLISH / MIXED / MIXED | +18.74% / +27.67% | +14.29% / +21.59% | `L224`, `L013`, `L002` |

## Investable determination

| Evidence threshold | Requirement | Best attainable | Pass |
|---|---|---|---|
| 1. Percentile rank | >= 80th | 100.00 | **Yes** |
| 2. Families non-negative | >= 3 of 4 | 2 of 4 (Technical, Macro) | **No** |
| 3. Single-family conviction share | <= 50% | 66.7% (Technical) | **No** |
| 4. Data completeness | >= 85% | 80% | **No** |
| 5. No hard stop | none | none triggered | **Yes** |

**Investable set: 0 names. Monitoring sleeve: 24 names.** Every published name
carries a settleable `mu` (from the calibration table band for its percentile) and `sigma`
(from `REALIZED_VOL_30D`), so all 24 produce auditable predictions in `15` — a
monitoring sleeve without `mu`/`sigma` would be a publishing failure, not caution.

Penalties applied: 0 of 24 published names
carry the -0.10 earnings penalty
(none),
and their confidence is capped `LOW` per `rules.md § Risk Controls`. All other published names
are capped `MEDIUM` by the rank-IC binding.

## What drives the leaderboard

With two families live, the composite is
`0.30*Tech_Z + 0.15*Macro_Z`, so **Technical carries 66.7% of conviction and
Macro 33.3%**. Within `Tech_Z` the six slots are equal-weighted, so momentum
(20d + 60d) occupies 2 of 6 slots = 33.3% of `Tech_Z` — down from the 50% it held before the
2026-08-03 dedupe removed the duplicate relative-strength slots.

An independent confirmation of that dedupe landed this run by accident: the engine initially
read the wrong relative-strength key names, so `rs20`/`rs60` were `None` for the whole
universe. Fixing them changed **zero** scores and **zero** ranks — which is exactly what the
Track B change intended, since relative strength is a displayed diagnostic and not a scoring
slot.

The top of the board is led by `NTAP` (`Tech_Z` +1.311, `Macro_Z`
+0.914), whose 20d/60d relative strength versus SPY is
+21.91%/+66.16% — a strong trend-persistence signature. That is
also the leaderboard's structural weakness: `Tech_Z` is trend-persistence by construction, and
`02 § 2` shows the previous book built the same way returned -3.87%
of alpha over the last 21 days. The score is reported as computed; the calibration evidence
against it is reported next to it rather than after the fact.
