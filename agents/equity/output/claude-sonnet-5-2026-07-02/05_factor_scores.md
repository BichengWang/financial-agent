# 05 Factor Scores

## Scoring Basis and Structural Constraint (read first)

Every name below is scored from **two of the four** required factor families:

- **Fundamental**: `UNAVAILABLE` for all 30 sampled names — no fundamentals feed connected this session.
- **Technical / Price**: sourced from `technical_indicators.json` (IBKR-grounded 5y daily history) for all 30 names.
- **Sentiment / Positioning**: `UNAVAILABLE` for all 30 sampled names — no positioning/skew/short-interest feed connected.
- **Macro / Regime**: sourced from 2 metrics (60d beta vs SPY, 60d correlation vs SPY, both `DERIVED` from the same IBKR history) for all 30 names.

Per `rules.md § Family Aggregation`, an `UNAVAILABLE` family contributes `0.00` to `Adj Score` and **does not count** toward the "3 of 4 factor families non-negative" Evidence Threshold. With only 2 of 4 families ever sourceable this run, **no name in this universe can reach the 3-of-4 threshold, regardless of score or percentile.** This is a structural, disclosed data-access gap (see `01_preflight.md` and `04_universe_summary.md`), not a judgment call about any individual name's quality. Its consequence for the run's final status is worked through in `08_risk_review.md` and `09_final_report.md`.

**Score Trace formula** (all names): `Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`, with `Fund_Z = 0.00 (UNAVAILABLE)`, `Sent_Z = 0.00 (UNAVAILABLE)`, `DQ = 0.70` (materially incomplete evidence — 2 of 4 families missing entirely), `Penalties = 0.00` (no earnings-date penalty applied because earnings dates are themselves `UNAVAILABLE`, not confirmed-clear — see caveat below).

**Earnings-date caveat**: `Days to Earnings` is `UNAVAILABLE` for all 30 names (no earnings-calendar feed connected). Per `rules.md § Risk Controls`, the 14-day earnings penalty applies only when a date is known and falls inside the window; an `UNAVAILABLE` date is *not* evidence of "clear," so no name here may be marked `HIGH` confidence and no name may be treated as GO-eligible on this basis either (see `08_risk_review.md` point 13).

## Ranked Candidate Table (all 30 sampled names)

Percentiles are `SAMPLED_PCTL (n=30)`, not `INDEX_UNION_PCTL` — see `04_universe_summary.md` for why. `Ledger Rows` for every name: entry-price/history rows + technical-indicator-pack row + finance-metrics row + score-attribution row in `01_preflight.md` (`L002`–`L146`, indexed per ticker).

| Rank | Ticker | Pctl (SAMPLED_PCTL n=30) | Adj Score | Tech_Z | Macro_Z | Beta 60d | 30d RVol(1m) | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Sleeve |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 1 | MU | 100.0 | 0.1843 | 1.826 | -1.8972 | 4.2394 | 35.9658% | -19.9672% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 51.79/72.89/81.66 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Monitoring |
| 2 | META | 96.6 | 0.1574 | 0.6162 | 0.2666 | 1.2263 | 13.5105% | -21.1575% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_1 | 58.45/49.15/51.91 | BULLISH_CROSS/BELOW_SIGNAL/BELOW_SIGNAL | Monitoring |
| 3 | AMD | 93.1 | 0.1366 | 1.6736 | -2.0459 | 3.946 | 23.061% | -16.6114% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_4 | 56.48/74.98/77.43 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Monitoring |
| 4 | PLTR | 89.7 | 0.1144 | 0.2318 | 0.6264 | 0.8843 | 19.0229% | -33.2275% | SELL_SETUP_2/BUY_SETUP_5/BUY_SETUP_2 | 48.36/43.55/53.0 | BELOW_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Monitoring |
| 5 | CAT | 86.2 | 0.0843 | 0.665 | -0.5272 | 1.9902 | 15.2496% | -8.9656% | BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_9 | 54.4/81.03/78.04 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Monitoring |
| 6 | MSFT | 82.8 | 0.0676 | 0.1324 | 0.3792 | 0.517 | 11.7512% | -23.3844% | SELL_SETUP_2/BUY_SETUP_4/SELL_SETUP_1 | 46.94/41.61/45.15 | BELOW_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Monitoring |
| 7 | AAPL | 79.3 | 0.0617 | 0.1533 | 0.2814 | 0.6129 | 8.8027% | -12.7062% | SELL_SETUP_1/BUY_SETUP_4/SELL_SETUP_3 | 50.97/57.74/64.0 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Monitoring |
| 8 | PG | 75.9 | 0.0595 | 0.13 | 0.3069 | 0.0199 | 6.9547% | -6.02% | BUY_SETUP_3/SELL_SETUP_5/SELL_SETUP_1 | 49.72/48.26/46.09 | BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | Monitoring |
| 9 | MCK | 72.4 | 0.0568 | 0.0804 | 0.3804 | -0.6639 | 6.8183% | -16.9745% | SELL_SETUP_1/BUY_SETUP_1/BUY_SETUP_5 | 50.19/43.87/55.09 | BULLISH_CROSS/BELOW_SIGNAL/BELOW_SIGNAL | Monitoring |
| 10 | AMZN | 69.0 | 0.0529 | 0.229 | 0.0454 | 1.2426 | 10.1725% | -17.4479% | SELL_SETUP_3/BUY_SETUP_5/SELL_SETUP_4 | 47.85/51.14/56.55 | BULLISH_CROSS/BELOW_SIGNAL/BEARISH_CROSS | Monitoring |
| 11 | UNH | 65.5 | 0.0389 | 0.0372 | 0.2962 | -0.1855 | 7.8663% | -6.0574% | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_4 | 65.87/68.88/53.38 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | Monitoring |
| 12 | GOOGL | 62.1 | 0.0259 | 0.2168 | -0.1869 | 1.4926 | 9.4289% | -16.2014% | SELL_SETUP_3/BUY_SETUP_6/SELL_SETUP_4 | 50.33/56.9/69.26 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Monitoring |
| 13 | HON | 58.6 | -0.0005 | -0.1506 | 0.2965 | 1.0673 | 11.822% | -13.4449% | BUY_SETUP_3/BUY_SETUP_2/BUY_SETUP_2 | 39.99/45.47/50.53 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 14 | WMT | 55.2 | -0.0035 | -0.1721 | 0.311 | 0.0023 | 8.9613% | -18.9121% | BUY_SETUP_5/BUY_SETUP_7/BUY_SETUP_3 | 25.84/38.82/57.05 | BELOW_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 15 | NEE | 51.7 | -0.0139 | -0.2216 | 0.3109 | 0.0008 | 6.0828% | -14.528% | BUY_SETUP_1/SELL_SETUP_2/BUY_SETUP_3 | 44.84/46.53/55.31 | ABOVE_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 16 | COST | 48.3 | -0.0161 | -0.2633 | 0.3729 | -0.2428 | 6.2417% | -15.5028% | BUY_SETUP_3/BUY_SETUP_6/BUY_SETUP_2 | 33.41/41.32/52.92 | BELOW_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 17 | LLY | 44.8 | -0.0212 | -0.2734 | 0.3448 | 0.218 | 10.026% | -10.8858% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_3 | 64.52/66.18/67.26 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 18 | LIN | 41.4 | -0.0278 | -0.2695 | 0.2747 | 0.1056 | 5.7312% | -4.1868% | SELL_SETUP_2/SELL_SETUP_2/SELL_SETUP_6 | 62.94/63.46/65.85 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 19 | AZO | 37.9 | -0.0341 | -0.3275 | 0.3299 | 0.217 | 10.7633% | -20.7569% | SELL_SETUP_4/SELL_SETUP_2/BUY_SETUP_3 | 55.46/43.34/47.73 | ABOVE_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 20 | PLD | 34.5 | -0.04 | -0.3004 | 0.2195 | 0.5073 | 7.3414% | -8.9216% | BUY_SETUP_9/BUY_SETUP_3/SELL_SETUP_1 | 39.27/49.76/56.27 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 21 | JPM | 31.0 | -0.0408 | -0.3239 | 0.2587 | 0.2654 | 7.0366% | -6.7163% | BUY_SETUP_4/SELL_SETUP_5/SELL_SETUP_2 | 63.34/63.06/69.17 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 22 | GS | 27.6 | -0.0427 | -0.05 | -0.3064 | 1.5001 | 10.7576% | -8.5866% | BUY_SETUP_6/BUY_SETUP_2/SELL_SETUP_9 | 46.47/62.03/75.9 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 23 | NVDA | 24.1 | -0.071 | -0.0311 | -0.6138 | 1.9156 | 11.6608% | -18.3295% | SELL_SETUP_2/BUY_SETUP_5/SELL_SETUP_4 | 43.26/51.27/65.01 | BELOW_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 24 | TSLA | 20.7 | -0.0797 | -0.0319 | -0.6948 | 2.0895 | 14.4108% | -15.7545% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_3 | 58.23/54.44/58.65 | ABOVE_SIGNAL/BULLISH_CROSS/BEARISH_CROSS | Rejected (<60th pctl) |
| 25 | ABBV | 17.2 | -0.0859 | -0.5694 | 0.3208 | -0.3444 | 9.0603% | -7.0716% | SELL_SETUP_8/SELL_SETUP_8/SELL_SETUP_2 | 72.25/65.41/66.51 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 26 | NFLX | 13.8 | -0.0878 | -0.5718 | 0.3073 | -0.0336 | 9.1705% | -34.224% | SELL_SETUP_1/BUY_SETUP_9/BUY_SETUP_2 | 37.52/31.9/42.61 | BELOW_SIGNAL/BELOW_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 27 | HD | 10.3 | -0.0893 | -0.5869 | 0.323 | 0.762 | 8.1986% | -15.2369% | SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_1 | 65.93/53.48/48.48 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | Rejected (<60th pctl) |
| 28 | AVGO | 6.9 | -0.1154 | -0.218 | -0.6632 | 2.2091 | 18.24% | -24.2021% | BUY_SETUP_6/BUY_SETUP_5/SELL_SETUP_4 | 42.0/49.51/61.45 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 29 | CVX | 3.4 | -0.1225 | -0.7623 | 0.3582 | -0.9477 | 6.8409% | -17.788% | BUY_SETUP_9/BUY_SETUP_4/BUY_SETUP_2 | 27.6/40.51/51.03 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |
| 30 | XOM | 0.0 | -0.1482 | -0.8682 | 0.3248 | -0.995 | 7.5783% | -16.991% | BUY_SETUP_9/BUY_SETUP_4/BUY_SETUP_2 | 34.36/45.07/56.36 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | Rejected (<60th pctl) |

Only names at or above the 60th `SAMPLED_PCTL` are ranked into a sleeve per `rules.md § mu Calibration Table` ("Names below the 60th percentile are not ranked in either sleeve — they appear only in the rejection log."). That is ranks 1–12 (`MU` through `GOOGL`, pctl 62.1–100.0). Ranks 13–30 are logged as rejected-by-percentile below, not scored into a monitoring sleeve, even though several (e.g. `HON` at 58.6) are close to the cutoff.

**Investable subset: 0 of 30.** No name clears the "3 of 4 factor families non-negative" Evidence Threshold (structural — see above). Per `rules.md § Evidence Thresholds`, a stock is investable only if *all five* conditions hold; condition 2 fails for every name in this universe. `06_top_candidates.md` and `07_portfolio_proposal.md` therefore carry **zero** investable positions.

**Monitoring subset: 12 of 30** (ranks 1–12, `SAMPLED_PCTL ≥ 60`) — `mu`/`sigma`/target/CI populated per the mu Calibration Table so every ranked name is settleable later, per `rules.md`: "Emitting a monitor list with blanket mu = N/A, sigma = UNAVAILABLE is a publishing failure, not caution." All 12 carry `LOW` confidence (see Confidence rationale below).

## Score Attribution Table

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| MU | 0.00 (UNAVAILABLE) | 1.8260 | 0.00 (UNAVAILABLE) | -1.8972 | -0.284 (0.30·Tech+0.15·Macro only) | 0.70 | 0.00 | 0.1843 | 60d momentum +173.3%; 60d RS vs SPY +160.1%; weekly/monthly RSI 72.9/81.7 (strong trend) | Beta 4.24 (extreme, -1.90 Macro_Z — far outside neutral 1.0); 60d max DD -20.0% (sharp intra-window correction); weekly/monthly TD9 SELL_SETUP_9 (double exhaustion flag) | L119–L122 |
| META | 0.00 (UNAVAILABLE) | 0.6162 | 0.00 (UNAVAILABLE) | 0.2666 | 0.225 | 0.70 | 0.00 | 0.1574 | Daily MACD BULLISH_CROSS; beta 1.23 near-neutral (+0.27 Macro_Z); RSI14 daily 58.5 (healthy, non-overbought) | 60d max DD -21.2%; weekly/monthly RS negative vs SPY (-6.2%) | L095–L098 |
| AMD | 0.00 (UNAVAILABLE) | 1.6736 | 0.00 (UNAVAILABLE) | -2.0459 | -0.29 | 0.70 | 0.00 | 0.1366 | 60d momentum +145.7%; 60d RS vs SPY +132.5%; weekly MACD ABOVE_SIGNAL | Beta 3.95 (extreme, -2.05 Macro_Z); weekly TD9 SELL_SETUP_9 (full exhaustion); 60d max DD -16.6% | L143–L146(AMD block, see ledger) |
| PLTR | 0.00 (UNAVAILABLE) | 0.2318 | 0.00 (UNAVAILABLE) | 0.6264 | 0.164 | 0.70 | 0.00 | 0.1144 | Beta 0.88 near-neutral (+0.63 Macro_Z, best in sample); weekly BUY_SETUP_5 (potential reversal-up setup) | 60d momentum -15.0% (negative, alone among top 5); 60d max DD -33.2% (worst in entire 30-name sample); 60d RS vs SPY -28.2% | ledger rows per ticker |
| CAT | 0.00 (UNAVAILABLE) | 0.6650 | 0.00 (UNAVAILABLE) | -0.5272 | 0.121 | 0.70 | 0.00 | 0.0843 | 60d momentum +37.5%; 60d RS vs SPY +24.3%; daily/weekly/monthly MACD all ABOVE_SIGNAL (rare full alignment) | Weekly RSI 81.0 and monthly RSI 78.0 (both overbought — exhaustion risk); monthly TD9 SELL_SETUP_9 | ledger rows per ticker |
| MSFT | 0.00 (UNAVAILABLE) | 0.1324 | 0.00 (UNAVAILABLE) | 0.3792 | 0.096 | 0.70 | 0.00 | 0.0676 | Beta 0.52 (defensive-tilt within tech, +0.38 Macro_Z); RSI14 daily 46.9 (neutral, room to run) | 60d max DD -23.4% (large for a mega-cap); daily/weekly/monthly MACD all BELOW_SIGNAL (broad-based technical softness) | ledger rows per ticker |
| AAPL | 0.00 (UNAVAILABLE) | 0.1533 | 0.00 (UNAVAILABLE) | 0.2814 | 0.088 | 0.70 | 0.00 | 0.0617 | Weekly/monthly MACD ABOVE_SIGNAL; 60d momentum +13.7% positive; beta 0.61 defensive | Daily momentum modest; RSI14 monthly 64.0 approaching overbought | ledger rows per ticker |
| PG | 0.00 (UNAVAILABLE) | 0.1300 | 0.00 (UNAVAILABLE) | 0.3069 | 0.085 | 0.70 | 0.00 | 0.0595 | Beta 0.02 (lowest in sample, +0.31 Macro_Z — maximal diversification value); 60d max DD only -6.0% (best-controlled drawdown in sample) | 60d momentum only +3.3%; weekly MACD ABOVE_SIGNAL but daily/monthly BELOW_SIGNAL (mixed) | ledger rows per ticker |
| MCK | 0.00 (UNAVAILABLE) | 0.0804 | 0.00 (UNAVAILABLE) | 0.3804 | 0.081 | 0.70 | 0.00 | 0.0568 | Beta -0.66 (negative — genuine diversifier, +0.38 Macro_Z); daily MACD BULLISH_CROSS | 60d momentum -10.4% (negative); 60d RS vs SPY -23.5% | ledger rows per ticker |
| AMZN | 0.00 (UNAVAILABLE) | 0.2290 | 0.00 (UNAVAILABLE) | 0.0454 | 0.075 | 0.70 | 0.00 | 0.0529 | Daily MACD BULLISH_CROSS; 60d momentum +13.6% positive | Monthly MACD BEARISH_CROSS (fresh negative cross, contradicts daily); beta 1.24 (above-market sensitivity) | ledger rows per ticker |
| UNH | 0.00 (UNAVAILABLE) | 0.0372 | 0.00 (UNAVAILABLE) | 0.2962 | 0.056 | 0.70 | 0.00 | 0.0389 | 60d momentum +51.6% (2nd-highest in sample after MU/AMD); beta -0.19 (near-zero/diversifying) | RSI14 daily 65.9, weekly 68.9 (approaching overbought); weekly TD9 SELL_SETUP_9 (exhaustion flag) | ledger rows per ticker |
| GOOGL | 0.00 (UNAVAILABLE) | 0.2168 | 0.00 (UNAVAILABLE) | -0.1869 | 0.037 | 0.70 | 0.00 | 0.0259 | Monthly MACD ABOVE_SIGNAL; 60d momentum +20.4% positive | Beta 1.49 (above-market sensitivity, -0.19 Macro_Z); daily/weekly MACD BELOW_SIGNAL | ledger rows per ticker |

Ranks 13–30 (`HON` through `XOM`) are below the 60th percentile and are not assigned a score-attribution row here; their raw metrics remain visible in the Ranked Candidate Table above for audit purposes (rejection log).

## Metric Availability Table

| Metric Group | Sourceable Count (of 30) | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | ---: | ---: | --- | --- |
| Fundamental (revenue/EPS revision, margin, FCF yield, ROIC, leverage, valuation) | 0 | 30 | Family UNAVAILABLE; blocks 3-of-4 threshold for every name | No fundamentals feed connected |
| Sentiment/Positioning (short interest, options skew, analyst revisions, insider, institutional flow) | 0 | 30 | Family UNAVAILABLE; blocks 3-of-4 threshold for every name | No positioning feed connected |
| Technical/Price (TD9, RSI, MACD, MA, momentum, volume ratio, RS) | 30 | 0 | Full weight to Tech_Z (0.30) | technical_indicators.json, IBKR-sourced |
| Macro (60d beta, 60d corr-to-SPY) | 30 | 0 (for these 2 sub-metrics); 3 of 5 menu items unsourced (sector-rotation leadership, rate sensitivity, VIX-regime cross-section, DXY/oil/credit) | Family sourceable via 2 metrics, but narrower than the full menu | finance_metrics computed from same IBKR history |
| Risk-free rate / Sharpe-Sortino-Treynor-IR | 0 | 30 | All ratio fields `UNAVAILABLE` in `06`/`07`; not guessed | No risk-free rate source connected this run |
| VaR95/CVaR95 (parametric) | 12 (monitoring sleeve only, once mu/sigma exist) | 18 (ranks 13–30, no mu/sigma assigned) | Diagnostic only for the 12 monitoring names | Parametric formula, `rules.md § Ratio Definitions` |
| Earnings date | 0 | 30 | Cannot confirm 14-day-window clear; no `HIGH` confidence possible | No earnings-calendar feed connected |

## Technical Indicator Summary Table (daily / weekly / monthly)

Full detail already shown in the Ranked Candidate Table above (`TD9 D/W/M`, `RSI14 D/W/M`, `MACD D/W/M` columns). MA alignment, 20/60-bar momentum, and 20-bar volume ratio for every name are in `technical_indicators.json` (`indicator_ledger_rows`: the `technical_indicator_pack` row per ticker in `01_preflight.md`).

## Hallucination Prevention Checklist

- [x] Every numeric `entry_price` (12 monitoring names) has `price_date` + `price_tag` (`01_preflight.md` `entry_price_live` rows).
- [x] Every numeric metric cites Source Ledger rows (per-ticker `price_history_5y`, `technical_indicator_pack`, `finance_metrics_60d`, `score_attribution`, `target_and_ci` rows).
- [x] Every `Adj Score` has a score trace with family z-scores, DQ, penalties, and metric drivers (Score Attribution Table above).
- [x] Missing metrics (`Fund_Z`, `Sent_Z`, earnings date, risk-free-adjusted ratios) are `UNAVAILABLE`, not neutral or supportive — never defaulted to `0` as a "no signal" stand-in; the `0.00 (UNAVAILABLE)` display is the required convention per `rules.md § Data Quality Multiplier`, distinct from a true neutral score.
- [x] No investable name has `price_tag = UNAVAILABLE` — moot, since there are zero investable names this run.
- [x] `mu`/`sigma` for all 12 monitoring names derive from the mu Calibration Table and Sigma Fallback Chain, not assertion — see `01_preflight.md` `target_and_ci` rows.
- [x] Every sigma has a stated source (`REALIZED_VOL_30D` for all 12).
- [x] `target_price = entry_price × (1 + mu)` verified for all 12 (see `01_preflight.md`).
- [x] No live-sounding wording ("current", "validated") used without a non-illustrative ledger row backing it — all prices here are `LIVE`/`DELAYED`/`HISTORICAL`-tagged with dates.
