# 09 — Final Report · 2026-08-14

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-14
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

Run Status: NO_TRADE

## Executive summary

All five Required inputs are grounded — 137/137 price-date checks
verified across three independent vendors at 0.000000% maximum deviation —
and the regime is a clean `BULL`, so this is not a data failure. It is an evidence failure:
`Fund_Z` and `Sent_Z` remain `UNAVAILABLE` across all 511 scored names, which makes three of
the five evidence thresholds arithmetically unsatisfiable and leaves zero names investable
against a minimum of five. 24 names are published as a monitoring sleeve with full
settleable forecasts, and all 149 due
predictions were settled, taking canonical `eff_n` to **2** for both record types — the first
confirmation of the falsifiable projection made on 2026-07-28. The ranking model's own record
argues against its leaderboard (rolling rank IC -0.0630; the prior book returned
-3.87% of alpha over the last 21 days), so every confidence label
is capped `MEDIUM`.

## MoM reflection summary

Summarizes `02`; introduces no new facts. Baseline `claude-opus-5-2026-07-24` (same model,
in-window, delta 7d, flag `NONE`). Over the 21-day window SPY ran
+5.06% while the baseline's
26-name book returned +1.19% — a
hit rate of 11.5% and mean alpha of
-3.87%. CI coverage was 76.9%,
inside the healthy band: the magnitude model was calibrated, the direction model was not. All
three core ETF forecasts from that vintage missed, having been drawn from a `HIGH_VOL` regime
prior into what became a broad advance.

## Regime assessment

| Field | Value | Evidence | Ledger Rows |
|---|---|---|---|
| Regime | `BULL` | SPY ABOVE/ABOVE vs MA20/MA50, mom20 +4.45%, 30d RVol 3.55% FALLING, VIX 14.25 | `L023`, `L013`, `L011` |
| Data quality | 0.80 | 2 of 4 factor families `UNAVAILABLE` universe-wide | `L020`–`L022` |
| Key macro risk | trend exhaustion, not deterioration | SPY daily TD-9 `SELL_SETUP_9` and monthly RSI 76.79 (overbought) against a tape -0.20% from its 60d high | `L013` |

## Core ETF market forecast

Summarizes `03 § Core ETF Market Forecast Block`; no new facts.

| ETF | Entry | mu | sigma | Target | 70% CI | Trend | Confidence |
|---|---|---|---|---|---|---|---|
| SPY | 776.34 | +2.00% | 3.55% | 791.87 | 763.24 – 820.50 | ABOVE/ABOVE | MEDIUM |
| QQQ | 731.07 | +2.99% | 6.60% | 752.91 | 702.77 – 803.05 | ABOVE/ABOVE | MEDIUM |
| SOXX | 550.42 | +5.53% | 15.73% | 580.87 | 490.84 – 670.89 | ABOVE/BELOW | MEDIUM |

`SOXX`'s +5.53% is the mechanical output of `beta x SPY_mu` with beta
3.5158, reduced by the full -1.50pp adjustment band. The
underlying `mu = beta x SPY_mu` rule is a known category error (`03`), it is the diagnosed
cause of the 32.17% rolling `MARKET_FORECAST` hit rate, and repairing it is
Track A work gated at `eff_n = 2 < 3` until
2026-09-07.

## Ranked candidates — monitoring sleeve (24 names)

| Rank | Ticker | Entry | Adj Score | Pctl | Score Trace | Beta | sigma | Sharpe | IR | Max DD60 | TD9 D/W/M | RSI D | MACD D/W | Earnings | mu | Target | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NTAP | 207.08 | +0.4243 | 100.00 | (0.30x0.00 UNAVL + 0.30x+1.311 + 0.25x0.00 UNAVL + 0.15x+0.914) x 0.80 - 0.00 = +0.4243 | +1.4251 | 12.73% | 0.447 | 0.175 | -15.81% | SELL9 / SELL6 / SELL5 | 76.7 | A / A | 19 | +6.00% | 219.50 | MEDIUM |
| 2 | CRL | 280.05 | +0.3507 | 99.80 | (0.30x0.00 UNAVL + 0.30x+1.338 + 0.25x0.00 UNAVL + 0.15x+0.246) x 0.80 - 0.00 = +0.3507 | +0.5249 | 13.51% | 0.421 | 0.361 | -6.38% | SELL8 / SELL9 / SELL3 | 76.2 | A / A | none <=37d | +6.00% | 296.85 | MEDIUM |
| 3 | MDT | 91.27 | +0.3247 | 99.61 | (0.30x0.00 UNAVL + 0.30x+0.992 + 0.25x0.00 UNAVL + 0.15x+0.723) x 0.80 - 0.00 = +0.3247 | -0.1816 | 7.65% | 0.744 | 0.721 | -6.17% | SELL8 / SELL9 / SELL1 | 71.1 | A / A | 18 | +6.00% | 96.75 | MEDIUM |
| 4 | AME | 254.79 | +0.3216 | 99.41 | (0.30x0.00 UNAVL + 0.30x+1.105 + 0.25x0.00 UNAVL + 0.15x+0.470) x 0.80 - 0.00 = +0.3216 | +0.9610 | 5.94% | 0.959 | 0.764 | -4.38% | SELL4 / SELL4 / SELL9 | 63.0 | A / A | none <=37d | +6.00% | 270.08 | MEDIUM |
| 5 | KKR | 114.01 | +0.3026 | 99.22 | (0.30x0.00 UNAVL + 0.30x+1.059 + 0.25x0.00 UNAVL + 0.15x+0.404) x 0.80 - 0.00 = +0.3026 | +1.1600 | 11.31% | 0.503 | 0.395 | -10.13% | SELL4 / SELL7 / SELL3 | 68.7 | A / A | none <=37d | +6.00% | 120.85 | MEDIUM |
| 6 | DXCM | 89.75 | +0.2886 | 99.02 | (0.30x0.00 UNAVL + 0.30x+0.985 + 0.25x0.00 UNAVL + 0.15x+0.435) x 0.80 - 0.00 = +0.2886 | +0.5629 | 14.94% | 0.381 | 0.366 | -13.86% | SELL5 / SELL5 / SELL2 | 67.4 | A / A | none <=37d | +6.00% | 95.14 | MEDIUM |
| 7 | ABNB | 184.06 | +0.2866 | 98.82 | (0.30x0.00 UNAVL + 0.30x+1.298 + 0.25x0.00 UNAVL + 0.15x-0.207) x 0.80 - 0.00 = +0.2866 | +0.7466 | 16.82% | 0.338 | 0.340 | -7.63% | BUY1 / SELL3 / SELL9 | 75.0 | A / A | none <=37d | +6.00% | 195.10 | MEDIUM |
| 8 | WTW | 331.59 | +0.2845 | 98.63 | (0.30x0.00 UNAVL + 0.30x+1.006 + 0.25x0.00 UNAVL + 0.15x+0.358) x 0.80 - 0.00 = +0.2845 | -0.3695 | 8.64% | 0.659 | 0.796 | -4.15% | BUY2 / SELL8 / SELL2 | 63.1 | b / A | none <=37d | +6.00% | 351.49 | MEDIUM |
| 9 | EXPE | 332.69 | +0.2826 | 98.43 | (0.30x0.00 UNAVL + 0.30x+1.233 + 0.25x0.00 UNAVL + 0.15x-0.112) x 0.80 - 0.00 = +0.2826 | +0.4131 | 11.56% | 0.492 | 0.438 | -5.25% | SELL9 / SELL3 / SELL3 | 73.6 | A / A | none <=37d | +6.00% | 352.65 | MEDIUM |
| 10 | JCI | 153.64 | +0.2767 | 98.24 | (0.30x0.00 UNAVL + 0.30x+0.664 + 0.25x0.00 UNAVL + 0.15x+0.978) x 0.80 - 0.00 = +0.2767 | +1.2486 | 7.14% | 0.798 | 0.407 | -6.62% | SELL1 / SELL4 / SELL9 | 60.9 | A / B+ | none <=37d | +6.00% | 162.86 | MEDIUM |
| 11 | BAC | 64.49 | +0.2753 | 98.04 | (0.30x0.00 UNAVL + 0.30x+0.851 + 0.25x0.00 UNAVL + 0.15x+0.592) x 0.80 - 0.00 = +0.2753 | +0.3282 | 5.12% | 1.111 | 1.045 | -2.74% | SELL9 / SELL9 / SELL3 | 68.5 | A / A | none <=37d | +6.00% | 68.36 | MEDIUM |
| 12 | MRK | 135.84 | +0.2720 | 97.84 | (0.30x0.00 UNAVL + 0.30x+0.817 + 0.25x0.00 UNAVL + 0.15x+0.633) x 0.80 - 0.00 = +0.2720 | -0.4080 | 6.91% | 0.823 | 0.804 | -6.78% | SELL6 / SELL8 / SELL9 | 68.8 | A / A | none <=37d | +6.00% | 143.99 | MEDIUM |
| 13 | SOLV | 88.59 | +0.2582 | 97.65 | (0.30x0.00 UNAVL + 0.30x+1.055 + 0.25x0.00 UNAVL + 0.15x+0.042) x 0.80 - 0.00 = +0.2582 | -0.0655 | 10.94% | 0.520 | 0.598 | -10.79% | SELL3 / SELL3 / SELL3 | 63.2 | B+ / A | none <=37d | +6.00% | 93.91 | MEDIUM |
| 14 | BX | 143.93 | +0.2535 | 97.45 | (0.30x0.00 UNAVL + 0.30x+0.720 + 0.25x0.00 UNAVL + 0.15x+0.672) x 0.80 - 0.00 = +0.2535 | +1.0951 | 10.86% | 0.524 | 0.360 | -11.64% | SELL9 / SELL7 / SELL3 | 63.9 | A / A | none <=37d | +6.00% | 152.57 | MEDIUM |
| 15 | URI | 1,153.83 | +0.2523 | 97.25 | (0.30x0.00 UNAVL + 0.30x+0.971 + 0.25x0.00 UNAVL + 0.15x+0.161) x 0.80 - 0.00 = +0.2523 | +0.6718 | 12.35% | 0.461 | 0.432 | -11.13% | SELL1 / SELL2 / SELL5 | 59.0 | A / A | none <=37d | +6.00% | 1,223.06 | MEDIUM |
| 16 | SCHW | 111.09 | +0.2510 | 97.06 | (0.30x0.00 UNAVL + 0.30x+0.676 + 0.25x0.00 UNAVL + 0.15x+0.740) x 0.80 - 0.00 = +0.2510 | -0.1643 | 5.52% | 1.030 | 0.908 | -7.04% | SELL3 / SELL9 / SELL2 | 76.4 | A / A | none <=37d | +6.00% | 117.76 | MEDIUM |
| 17 | STT | 191.74 | +0.2506 | 96.86 | (0.30x0.00 UNAVL + 0.30x+0.676 + 0.25x0.00 UNAVL + 0.15x+0.737) x 0.80 - 0.00 = +0.2506 | +0.6830 | 7.00% | 0.813 | 0.734 | -5.65% | SELL9 / SELL9 / SELL9 | 67.3 | B+ / A | none <=37d | +6.00% | 203.24 | MEDIUM |
| 18 | AMGN | 415.21 | +0.2490 | 96.67 | (0.30x0.00 UNAVL + 0.30x+0.884 + 0.25x0.00 UNAVL + 0.15x+0.306) x 0.80 - 0.00 = +0.2490 | +0.0836 | 7.78% | 0.732 | 0.770 | -5.05% | BUY1 / SELL8 / SELL2 | 70.0 | A / A | none <=37d | +6.00% | 440.12 | MEDIUM |
| 19 | FITB | 58.06 | +0.2425 | 96.47 | (0.30x0.00 UNAVL + 0.30x+0.618 + 0.25x0.00 UNAVL + 0.15x+0.785) x 0.80 - 0.00 = +0.2425 | +0.3388 | 5.73% | 0.993 | 0.788 | -4.83% | SELL3 / SELL2 / SELL9 | 59.4 | b / A | none <=37d | +6.00% | 61.54 | MEDIUM |
| 20 | BNY | 163.24 | +0.2396 | 96.27 | (0.30x0.00 UNAVL + 0.30x+0.686 + 0.25x0.00 UNAVL + 0.15x+0.625) x 0.80 - 0.00 = +0.2396 | +0.5161 | 6.98% | 0.815 | 0.802 | -5.69% | SELL9 / SELL9 / SELL9 | 66.7 | A / A | none <=37d | +6.00% | 173.03 | MEDIUM |
| 21 | IVZ | 32.55 | +0.2390 | 96.08 | (0.30x0.00 UNAVL + 0.30x+0.855 + 0.25x0.00 UNAVL + 0.15x+0.282) x 0.80 - 0.00 = +0.2390 | +1.7447 | 11.19% | 0.508 | 0.306 | -11.40% | SELL2 / SELL6 / SELL9 | 67.5 | A / A | none <=37d | +6.00% | 34.50 | MEDIUM |
| 22 | DASH | 217.02 | +0.2359 | 95.88 | (0.30x0.00 UNAVL + 0.30x+0.846 + 0.25x0.00 UNAVL + 0.15x+0.274) x 0.80 - 0.00 = +0.2359 | +1.2809 | 12.32% | 0.462 | 0.272 | -13.26% | SELL1 / SELL3 / SELL3 | 68.4 | A / A | none <=37d | +6.00% | 230.04 | MEDIUM |
| 23 | TECH | 72.40 | +0.2329 | 95.69 | (0.30x0.00 UNAVL + 0.30x+0.495 + 0.25x0.00 UNAVL + 0.15x+0.951) x 0.80 - 0.00 = +0.2329 | +0.7450 | 1.31% | 4.356 | 0.326 | -4.02% | SELL1 / SELL9 / SELL3 | 72.5 | b / A | none <=37d | +6.00% | 76.74 | MEDIUM |
| 24 | REGN | 803.48 | +0.2323 | 95.49 | (0.30x0.00 UNAVL + 0.30x+0.731 + 0.25x0.00 UNAVL + 0.15x+0.474) x 0.80 - 0.00 = +0.2323 | +0.2527 | 8.92% | 0.638 | 0.653 | -7.56% | BUY1 / SELL8 / SELL1 | 77.3 | A / A | none <=37d | +6.00% | 851.69 | MEDIUM |

## No-trade rationale

| Evidence threshold | Requirement | This run | Pass |
|---|---|---|---|
| 1. Percentile rank | >= 80th | up to 100.00 | Yes |
| 2. Families non-negative | >= 3 of 4 | **2 of 4** | **No** |
| 3. Family conviction share | <= 50% | **66.7%** | **No** |
| 4. Data completeness | >= 85% | **80%** | **No** |
| 5. Hard stops | none | none | Yes |

Zero names investable against a minimum of five → `rules.md § Downgrade to NO_TRADE` trigger 1.

Portfolio feasibility is **not** the cause and was recomputed rather than assumed: the
>=80th-percentile pool spans an attainable sleeve beta of
[-0.2791, +1.5397], which contains the
0.90–1.10 band. A naive top-20 equal-weight sleeve would separately have failed on beta
(+0.4785) and sector concentration
(40.0% Finance), while passing correlation
(0.1386) and drawdown
(6.64%).

## Assumptions and limitations

1. **Two of four factor families are unavailable.** `Adj Score` is a technical/macro composite
   with Technical carrying 66.7% of conviction. It is not a four-family
   conviction score and should not be read as one.
2. **The ranking is not validated out of sample.** Rolling rank IC -0.0630 over 950
   settled records; hit rate 40.53% against a >50% healthy floor.
3. **VaR95, CVaR95 and the 95th-percentile drawdown assume normality**, stated where used.
4. **Kelly uses the `mu / sigma^2` fallback**, disclosed, because no beta-adjusted edge and
   tracking-error variance pairing is wired.
5. **Sector labels are the Nasdaq screener's taxonomy, not GICS.** The 30% cap is applied
   against those labels.
6. **Constituent caches are 54 days stale** and contained one delisted name (`EA`), detected
   and excluded this run.
7. **Three trading days have no package from any model** — 2026-08-11, 2026-08-12, 2026-08-13.
   Not backfilled; creating retroactive `OPEN` predictions is forbidden.
8. **`mu = beta x SPY_mu` for QQQ/SOXX is a known category error**, disclosed at the point of
   use, unrepairable until Track A opens.

## Next scheduled review

| Checkpoint | When |
|---|---|
| Next daily run | next trading session, 2026-08-17 (Monday) |
| Predictions in this package settle | 2026-09-11 |
| `EQUITY_ALPHA` `eff_n` -> 3 (Track A opens) | 2026-09-03 |
| `MARKET_FORECAST` `eff_n` -> 3 | 2026-09-07 |
| Month-end structural review | 2026-08-31 |
