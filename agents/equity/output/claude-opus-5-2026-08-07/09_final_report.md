```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-07
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

All five Required inputs are grounded — 27/27 published prices agree
to 0.0000% across three independent sources, and the forward earnings
sweep grounded the entire 511-name universe — so this is an evidence-threshold `NO_TRADE`, not a
data failure. No name is investable because `Fund_Z` and `Sent_Z` are `UNAVAILABLE`
universe-wide, which makes evidence thresholds #2 and #3 arithmetically unsatisfiable and holds
data completeness at 0.80. Two further caps fail independently: the naive top-20 sleeve's
95th-percentile 1-month drawdown is 9.15% against an 8% cap, and
Consumer Discretionary concentration is 41.67% against a 30% cap.
24 names publish as a settleable monitoring sleeve alongside the three core ETF
forecasts. Separately, 50 due settlement keys were computed but deferred
one run on a validator technicality, which is this run's Track B fix.

## MoM reflection summary

Baseline `claude-fable-5-2026-07-10` (`CROSS_MODEL_BASELINE`; 0-day tie with `gpt-5-2026-07-10`, both disclosed in
`02 § 1`). Over the 2026-07-10 → 2026-08-07 window SPY returned
+2.43%. The baseline book returned +2.13%
mean raw, for -0.29% mean alpha and a 29.17% hit
rate; the tied `gpt-5` book returned -3.42% for
-5.85% alpha and 35.00%. **The conclusion is
invariant across both**: negative alpha and sub-50% direction accuracy in a rising tape — the
signature of the rank-order inversion that a trend-dominated `Tech_Z` produces through a
rotation. Canonical rolling metrics are unchanged this run (EQ n=643,
`eff_n`=2, hit 39.04%, CI 69.36%, mean z
-0.5328) because no settlement was published.

## Regime

| Field | Value | Key evidence | Ledger Rows |
|---|---|---|---|
| Regime | **BULL** | SPY 773.26 above MA20 750.17 and MA50 746.62; mom60 +5.02%; VIX 14.9 falling | `L001`, `L004`, `L019` |
| Data quality | 0.80 | 2 of 4 factor families UNAVAILABLE | `L021`–`L023` |
| Key macro risk | narrow breadth | only 47.95% of the universe has bullish daily MA alignment while the index sits at its 60-day high; SPY daily TD-9 `SELL_SETUP_7` | `L019` |

## Core ETF market forecast

| ETF | Entry | mu | sigma | Target | 70% CI | Beta vs SPY | Trend 20d/50d | RS20 vs SPY | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 773.26 | +2.00% | 3.82% | 788.73 | 758.02–819.43 | 1.0000 | ABOVE/ABOVE | +0.00% | MEDIUM |
| QQQ | 723.03 | +2.92% | 7.32% | 744.16 | 689.12–799.21 | 1.7115 | ABOVE/ABOVE | -2.77% | MEDIUM |
| SOXX | 543.27 | +5.45% | 18.23% | 572.90 | 469.88–675.92 | 3.4767 | ABOVE/BELOW | -8.98% | MEDIUM |

Summarized from `03`; no new facts. The `mu = beta x SPY_mu` mapping is a known category error
(diagnosed 2026-07-24) and remains Track-A-gated — see `03` for the full derivation and the
ledger-backed adjustments applied.

## Ranked candidates — monitoring sleeve (24 names, 0 investable)

| # | Ticker | Sector | Entry | Adj Score | Pctl | Score Trace | mu | sigma | Target | 70% CI | Beta | Sharpe | IR | Max DD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | Earnings | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DASH | Consumer Discretionary | 216.26 | +0.3755 | 99.80 | T +1.21 / M +0.70 x0.80 - 0.00 | +6.00% | 12.30% | 229.24 | 201.57–256.90 | 1.192 | 0.46 | 0.27 | -13.26% | SELL9 / SELL2 / SELL3 | 71 / 62 / 56 | A / A / b | none | MEDIUM |
| 2 | ABNB | Consumer Discretionary | 178.07 | +0.3531 | 99.61 | T +1.54 / M -0.14 x0.80 - 0.00 | +6.00% | 16.69% | 188.75 | 157.84–219.66 | 0.742 | 0.34 | 0.34 | -7.63% | SELL3 / SELL2 / SELL9 | 79 / 75 / 66 | A / A / A | none | MEDIUM |
| 3 | GEN | Technology | 29.17 | +0.3448 | 99.41 | T +1.10 / M +0.67 x0.80 - 0.00 | +6.00% | 9.66% | 30.92 | 27.99–33.85 | 0.402 | 0.59 | 0.47 | -17.11% | SELL9 / SELL6 / SELL4 | 70 / 65 / 59 | A / A / B+ | none | MEDIUM |
| 4 | VEEV | Technology | 230.47 | +0.3439 | 99.22 | T +1.22 / M +0.42 x0.80 - 0.00 | +6.00% | 12.86% | 244.30 | 213.49–275.11 | 0.166 | 0.44 | 0.42 | -18.82% | SELL9 / SELL6 / SELL2 | 76 / 63 / 52 | A / A / b | 19d | MEDIUM |
| 5 | HPQ | Technology | 30.05 | +0.3231 | 99.02 | T +1.05 / M +0.60 x0.80 - 0.00 | +6.00% | 13.38% | 31.85 | 27.67–36.04 | 0.442 | 0.43 | 0.31 | -24.35% | SELL4 / SELL4 / SELL4 | 70 / 70 / 58 | A / A / A | 19d | MEDIUM |
| 6 | WSM | Consumer Discretionary | 251.78 | +0.3229 | 98.83 | T +1.19 / M +0.31 x0.80 - 0.00 | +6.00% | 9.11% | 266.89 | 243.04–290.74 | 0.980 | 0.62 | 0.42 | -9.79% | SELL5 / SELL2 / SELL3 | 69 / 68 / 70 | A / A / A | 19d | MEDIUM |
| 7 | TECH | Health Care | 72.29 | +0.3054 | 98.63 | T +0.83 / M +0.87 x0.80 - 0.00 | +6.00% | 1.42% | 76.63 | 75.56–77.70 | 0.711 | 4.01 | 0.31 | -8.69% | SELL1 / SELL9 / SELL3 | 74 / 66 / 55 | b / A / A | none | MEDIUM |
| 8 | DXCM | Health Care | 84.75 | +0.3045 | 98.43 | T +0.97 / M +0.59 x0.80 - 0.00 | +6.00% | 15.32% | 89.84 | 76.33–103.34 | 0.245 | 0.37 | 0.38 | -13.86% | BUY2 / SELL4 / SELL2 | 64 / 66 / 52 | A / A / A | none | MEDIUM |
| 9 | CPAY | Consumer Discretionary | 392.94 | +0.2975 | 98.24 | T +0.84 / M +0.79 x0.80 - 0.00 | +6.00% | 7.66% | 416.52 | 385.23–447.80 | 0.273 | 0.74 | 0.61 | -10.52% | SELL9 / SELL4 / SELL5 | 62 / 65 / 62 | A / A / A | none | MEDIUM |
| 10 | NTAP | Technology | 189.52 | +0.2943 | 98.04 | T +0.81 / M +0.83 x0.80 - 0.00 | +6.00% | 12.57% | 200.89 | 176.11–225.67 | 1.403 | 0.45 | 0.18 | -15.81% | SELL9 / SELL5 / SELL5 | 68 / 76 / 73 | A / A / A | 19d | MEDIUM |
| 11 | BAX | Health Care | 27.55 | +0.2914 | 97.85 | T +1.15 / M +0.13 x0.80 - 0.00 | +6.00% | 14.38% | 29.20 | 25.08–33.32 | 0.661 | 0.40 | 0.38 | -7.19% | BUY1 / SELL9 / SELL3 | 69 / 73 / 51 | A / A / A | none | MEDIUM |
| 12 | GPN | Consumer Discretionary | 86.12 | +0.2908 | 97.65 | T +1.02 / M +0.39 x0.80 - 0.00 | +6.00% | 12.62% | 91.29 | 79.99–102.59 | 0.847 | 0.45 | 0.36 | -17.27% | BUY1 / SELL6 / SELL2 | 60 / 62 / 49 | A / A / A | none | MEDIUM |
| 13 | MET | Finance | 97.77 | +0.2871 | 97.46 | T +0.93 / M +0.52 x0.80 - 0.00 | +6.00% | 6.70% | 103.64 | 96.82–110.45 | -0.082 | 0.85 | 0.90 | -4.77% | SELL2 / SELL9 / SELL5 | 65 / 74 / 70 | A / A / A | none | MEDIUM |
| 14 | SWK | Consumer Discretionary | 103.89 | +0.2786 | 97.26 | T +1.20 / M -0.07 x0.80 - 0.00 | +6.00% | 10.51% | 110.12 | 98.76–121.48 | 1.604 | 0.54 | 0.31 | -8.47% | SELL9 / SELL2 / SELL9 | 70 / 73 / 62 | A / A / A | none | MEDIUM |
| 15 | PH | Industrials | 1,073.87 | +0.2755 | 97.06 | T +1.08 / M +0.13 x0.80 - 0.00 | +6.00% | 8.54% | 1,138.30 | 1,042.94–1,233.67 | 0.575 | 0.67 | 0.64 | -6.69% | SELL5 / SELL3 / SELL2 | 74 / 70 / 73 | A / A / A | none | MEDIUM |
| 16 | PFE | Health Care | 26.76 | +0.2733 | 96.87 | T +0.85 / M +0.59 x0.80 - 0.00 | +6.00% | 5.68% | 28.37 | 26.78–29.95 | -0.045 | 1.00 | 1.04 | -9.69% | SELL4 / SELL3 / SELL1 | 75 / 61 / 55 | A / B+ / A | none | MEDIUM |
| 17 | TPR | Consumer Discretionary | 162.36 | +0.2713 | 96.67 | T +1.20 / M +0.70 x0.80 - 0.10 | +6.00% | 8.52% | 172.10 | 157.71–186.49 | 0.740 | 0.67 | 0.52 | -10.35% | SELL9 / SELL2 / SELL2 | 72 / 66 / 79 | A / B+ / A | 6d | LOW |
| 18 | FAST | Consumer Discretionary | 51.84 | +0.2693 | 96.48 | T +0.99 / M +0.26 x0.80 - 0.00 | +6.00% | 7.44% | 54.95 | 50.94–58.96 | 0.373 | 0.77 | 0.78 | -7.90% | SELL6 / SELL1 / SELL7 | 72 / 67 / 69 | A / A / A | none | MEDIUM |
| 19 | INSM | Health Care | 131.10 | +0.2672 | 96.28 | T +0.88 / M +0.46 x0.80 - 0.00 | +6.00% | 29.31% | 138.97 | 99.01–178.93 | 0.807 | 0.19 | 0.19 | -22.13% | SELL2 / SELL1 / BUY7 | 74 / 54 / 55 | A / B+ / b | none | MEDIUM |
| 20 | GRMN | Industrials | 310.89 | +0.2638 | 96.09 | T +1.13 / M -0.05 x0.80 - 0.00 | +6.00% | 15.34% | 329.54 | 279.96–379.13 | 0.219 | 0.37 | 0.45 | -5.71% | SELL9 / SELL6 / SELL2 | 78 / 74 / 71 | A / A / A | none | MEDIUM |
| 21 | EXPE | Consumer Discretionary | 310.68 | +0.2634 | 95.89 | T +1.15 / M -0.11 x0.80 - 0.00 | +6.00% | 12.68% | 329.32 | 288.36–370.29 | 0.400 | 0.45 | 0.44 | -5.25% | SELL9 / SELL2 / SELL3 | 66 / 68 / 69 | A / A / A | none | MEDIUM |
| 22 | BKNG | Consumer Discretionary | 214.42 | +0.2616 | 95.69 | T +1.16 / M -0.14 x0.80 - 0.00 | +6.00% | 12.38% | 227.29 | 199.68–254.89 | 0.446 | 0.46 | 0.45 | -6.38% | SELL3 / SELL2 / SELL3 | 73 / 65 / 61 | A / A / b | none | MEDIUM |
| 23 | WTW | Finance | 344.82 | +0.2615 | 95.50 | T +0.98 / M +0.22 x0.80 - 0.00 | +6.00% | 9.65% | 365.51 | 330.91–400.11 | -0.329 | 0.59 | 0.75 | -4.15% | SELL9 / SELL7 / SELL2 | 80 / 69 / 61 | A / A / b | none | MEDIUM |
| 24 | CRL | Health Care | 267.49 | +0.2579 | 95.30 | T +0.92 / M +0.31 x0.80 - 0.00 | +6.00% | 13.55% | 283.54 | 245.85–321.22 | 0.602 | 0.42 | 0.33 | -11.12% | SELL3 / SELL9 / SELL3 | 76 / 73 / 63 | A / A / A | none | MEDIUM |

`TD9` abbreviated (`BUY2` = `BUY_SETUP_2`, `-` = `NONE`); `MACD`: `B+` bullish cross, `A` above
signal, `O` on signal, `b` below signal, `B-` bearish cross. Full states and complete score
attribution for every name are in `05_factor_scores.md`.

## No-trade rationale

| # | Trigger | Rule | This run | Sufficient alone? |
|---|---|---|---|---|
| 1 | Evidence thresholds #2 / #3 / #4 | >=3 of 4 families; no family >50%; DQ >=85% | 2 families live; Tech_Z 66.67%; DQ 0.80 | Yes |
| 2 | 95th-pctl 1-month drawdown | <= 8% | 9.15% | Yes |
| 3 | Sector concentration | <= 30% | 41.67% Consumer Discretionary | Yes |
| 4 | Event concentration | <= 2 names with earnings <=14d | 1 of 24 published names | Yes |

The beta band, by contrast, is **feasible** (-0.3876 …
1.3387 against 0.90–1.10) — the sixth consecutive run in
which the 2026-07-27 "provably infeasible" narrative would have been wrong. It is recomputed
every run.

## Assumptions and limitations

1. **Two of four factor families are unavailable, not merely sparse.** Every ranking in this
   report rests on technical and macro evidence alone. This is the single structural cause of
   every `NO_TRADE` in this series.
2. **The ranking has a negative measured rank IC** (-0.0430
   over 643 settled records). Confidence is capped at MEDIUM everywhere as a result. The
   monitoring sleeve is a set of falsifiable forecasts, not a recommendation.
3. **VaR95, CVaR95 and the 95th-pctl drawdown assume normality**; they are parametric estimates
   from `REALIZED_VOL_30D`, not empirical tail measurements.
4. **Constituent caches are 47 days old** (2026-06-21). Used as-is per
   `rules.md`; a plausible contributor to the `EA` and `SATS`/`ECHO` identity issues.
5. **No options, short-interest, spread, revision or ownership tape is wired**, so no name
   could reach `HIGH` confidence even with a live fundamental family.
6. **50 settlement keys are deferred one run**, so this package's calibration figures are
   inherited from 2026-08-06 rather than advanced.
7. **Earnings dates are calendar-confirmed for the 37-day window only.** A name absent from the
   complete sweep is `NO_PRINT_IN_WINDOW`, which is positive evidence about that window and
   silent about anything beyond it.

## Next scheduled review

Next daily run per `runbook.md § Cadence` (07:27 ET weekdays; the scheduler is not currently
active, so runs are manual or task-triggered). The next run inherits 50
due settlement keys, which settle `ORDINARY` at the 2026-08-07 close.
