# 09 — Final Report — 2026-08-03

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-03
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

Every Required input was grounded on the completed 2026-08-03 close, yet no name is investable: with
`Fund_Z` and `Sent_Z` unavailable universe-wide, three of the five Evidence Thresholds are
arithmetically unsatisfiable, so the run publishes `NO_TRADE` for the same structural reason as every
package since 2026-07-01. 88 predictions settled cleanly (19/76 equity direction hits), leaving
due inventory at zero. This is the first package built on the deduplicated 6-metric `Tech_Z` accepted
as Track B on 2026-08-01, and pre-publication verification against the prior package caught and fixed
a drawdown-polarity defect in the rebuilt engine. Portfolio beta feasibility was recomputed and is
**feasible** — `NO_TRADE` is an evidence outcome, not a feasibility one.

## MoM Reflection Summary

Baseline **`claude-fable-5-2026-07-06`** (flag `CROSS_MODEL_BASELINE`), selected from a 2-way tie at
`|delta|` = 0d under rule 8; every tied candidate is disclosed in `02 § 1` and the
conclusion is invariant across them (hit-rate spread 6.1pp). The prior book returned
**-4.03%** mean alpha against SPY's +0.85% over the window, hitting
6/23 = 26.09%. Damage concentrated in Health Care
(-10.98% mean alpha over 6 names) — the
composition effect of a momentum-ranked book carried through a leadership rotation. No new facts here;
see `02`.

## Regime

| Regime | Data quality | Key macro risk | Ledger rows |
|---|---|---|---|
| **`BULL`** | `DELAYED`, DQ 0.80 | Peak Q2 earnings season — 153 of 512 scored names print inside 14 days | `L-REG`, `L-ETF-SPY`, `L-ETF-S-SPY`, `L-RF`, `L-EA-SWEEP` |

SPY is above MA20 and above MA50 with
60d momentum +3.51% and 30d realized vol 3.76%/month; the
3-month T-bill is 3.75%.

## Core ETF market forecast

| ETF | Entry | Trend 20d/50d | 30d RVol | Beta vs SPY | mu | sigma | Target | CI Lo | CI Hi | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 757.67 | above/above | 3.76% | +1.000 | +2.00% | 3.76% | 772.82 | 743.18 | 802.46 | MEDIUM |
| QQQ | 700.07 | above/below | 7.18% | +1.706 | +1.91% | 7.18% | 713.46 | 661.19 | 765.72 | MEDIUM |
| SOXX | 507.68 | below/below | 18.60% | +3.530 | +5.56% | 18.60% | 535.91 | 437.71 | 634.10 | MEDIUM |

Summarised from `03`. The `mu = beta x SPY_mu` derivation for QQQ and SOXX is a disclosed category
error with a settled hit rate of 22.09% over n=90; the Track A correction remains
deferred at `eff_n` = 1 < 3.

## Ranked candidates — monitoring sleeve (24 published)

| Rank | Ticker | Sector | Pctl | Adj Score | Score Trace | Entry | mu | sigma | Target | Beta | Sharpe | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | Earnings | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DXCM** | Health Care | 100.00 | **+0.4297** | `(0.3*UA + 0.3*+1.425 + 0.25*UA + 0.15*+0.730)*0.80 - 0.00` | 87.31 | +6.0% | 15.33% | 92.55 | +0.205 | 0.37 | -13.86% | S5/S4/S2 | 72.6/67.8/53.5 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 2 | **BMY** | Health Care | 99.80 | **+0.3993** | `(0.3*UA + 0.3*+1.362 + 0.25*UA + 0.15*+0.603)*0.80 - 0.00` | 65.47 | +6.0% | 8.67% | 69.40 | -0.203 | 0.66 | -9.32% | S9/S7/S2 | 71.8/68.5/65.5 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 3 | **BEN** | Finance | 99.61 | **+0.3643** | `(0.3*UA + 0.3*+1.097 + 0.25*UA + 0.15*+0.842)*0.80 - 0.00` | 35.24 | +6.0% | 8.12% | 37.35 | +1.095 | 0.70 | -6.42% | S7/S1/S8 | 66.1/74.3/71.8 | BULL_X/ABOVE/ABOVE | none | MEDIUM |
| 4 | **BAX** | Health Care | 99.41 | **+0.3377** | `(0.3*UA + 0.3*+1.233 + 0.25*UA + 0.15*+0.349)*0.80 - 0.00` | 28.10 | +6.0% | 14.23% | 29.79 | +0.644 | 0.40 | -7.19% | S7/S9/S3 | 76.4/73.6/51.7 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 5 | **WTW** | Finance | 99.22 | **+0.3289** | `(0.3*UA + 0.3*+1.188 + 0.25*UA + 0.15*+0.364)*0.80 - 0.00` | 341.63 | +6.0% | 9.85% | 362.13 | -0.367 | 0.58 | -6.18% | S7/S7/S2 | 81.6/68.4/60.8 | ABOVE/ABOVE/BELOW | none | MEDIUM |
| 6 | **COO** | Health Care | 99.02 | **+0.2826** | `(0.3*UA + 0.3*+0.839 + 0.25*UA + 0.15*+0.677)*0.80 - 0.00` | 74.23 | +6.0% | 8.75% | 78.68 | -0.380 | 0.65 | -7.67% | S5/S1/S2 | 63.3/55.8/46.2 | BULL_X/ABOVE/BULL_X | 37d | MEDIUM |
| 7 | **BBY** | Consumer Discretionary | 98.83 | **+0.2648** | `(0.3*UA + 0.3*+0.868 + 0.25*UA + 0.15*+0.471)*0.80 - 0.00` | 85.25 | +6.0% | 8.14% | 90.36 | +0.421 | 0.70 | -8.93% | B2/S9/S4 | 56.3/65.1/58.9 | BELOW/ABOVE/ABOVE | 24d | MEDIUM |
| 8 | **FTNT** | Technology | 98.63 | **+0.2643** | `(0.3*UA + 0.3*+0.585 + 0.25*UA + 0.15*+1.032)*0.80 - 0.00` | 163.21 | +6.0% | 10.70% | 173.00 | +0.968 | 0.53 | -10.10% | S4/S9/S6 | 61.3/77.7/78.4 | BELOW/ABOVE/ABOVE | none | MEDIUM |
| 9 | **ROST** | Consumer Discretionary | 98.43 | **+0.2596** | `(0.3*UA + 0.3*+0.909 + 0.25*UA + 0.15*+0.345)*0.80 - 0.00` | 252.91 | +6.0% | 8.84% | 268.08 | +0.219 | 0.64 | -13.03% | S7/S4/S9 | 71.0/69.1/76.4 | ABOVE/BULL_X/ABOVE | 17d | MEDIUM |
| 10 | **NTAP** | Technology | 98.24 | **+0.2576** | `(0.3*UA + 0.3*+0.756 + 0.25*UA + 0.15*+0.634)*0.80 - 0.00` | 182.92 | +6.0% | 12.08% | 193.90 | +1.439 | 0.47 | -15.81% | S9/S5/S5 | 68.0/74.3/71.5 | ABOVE/ABOVE/ABOVE | 23d | MEDIUM |
| 11 | **KKR** | Finance | 98.04 | **+0.2488** | `(0.3*UA + 0.3*+0.784 + 0.25*UA + 0.15*+0.506)*0.80 - 0.00` | 106.56 | +6.0% | 10.42% | 112.95 | +1.273 | 0.55 | -13.08% | S1/S6/S3 | 65.8/55.3/49.3 | ABOVE/ABOVE/BELOW | none | MEDIUM |
| 12 | **IQV** | Health Care | 97.85 | **+0.2463** | `(0.3*UA + 0.3*+0.948 + 0.25*UA + 0.15*+0.156)*0.80 - 0.00` | 233.36 | +6.0% | 15.39% | 247.36 | -0.211 | 0.37 | -10.23% | B1/S7/S3 | 66.4/66.3/57.0 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 13 | **ARES** | Finance | 97.65 | **+0.2416** | `(0.3*UA + 0.3*+0.877 + 0.25*UA + 0.15*+0.259)*0.80 - 0.00` | 138.57 | +6.0% | 13.46% | 146.88 | +1.722 | 0.42 | -20.28% | S2/S3/S3 | 69.3/57.4/51.6 | ABOVE/ABOVE/BELOW | none | MEDIUM |
| 14 | **TGT** | Consumer Discretionary | 97.46 | **+0.2409** | `(0.3*UA + 0.3*+1.050 + 0.25*UA + 0.15*-0.092)*0.80 - 0.00` | 149.35 | +6.0% | 10.03% | 158.31 | -0.164 | 0.57 | -10.69% | S6/S2/S9 | 69.5/68.2/65.0 | ABOVE/ABOVE/ABOVE | 16d | MEDIUM |
| 15 | **REGN** | Health Care | 97.26 | **+0.2396** | `(0.3*UA + 0.3*+0.529 + 0.25*UA + 0.15*+0.939)*0.80 - 0.00` | 759.24 | +6.0% | 9.40% | 804.79 | +0.320 | 0.61 | -16.84% | S5/S7/S1 | 76.4/60.4/52.8 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 16 | **ZBRA** | Industrials | 97.06 | **+0.2361** | `(0.3*UA + 0.3*+1.051 + 0.25*UA + 0.15*+0.699)*0.80 - 0.10` | 291.64 | +6.0% | 11.19% | 309.14 | +1.396 | 0.51 | -16.64% | S6/S7/S4 | 68.0/63.4/50.5 | ABOVE/ABOVE/ABOVE | 1d | MEDIUM |
| 17 | **VEEV** | Technology | 96.87 | **+0.2339** | `(0.3*UA + 0.3*+0.904 + 0.25*UA + 0.15*+0.141)*0.80 - 0.00` | 206.25 | +6.0% | 12.76% | 218.62 | -0.004 | 0.45 | -18.82% | S6/S6/S2 | 63.8/56.8/47.4 | ABOVE/ABOVE/BELOW | 23d | MEDIUM |
| 18 | **GRMN** | Industrials | 96.67 | **+0.2318** | `(0.3*UA + 0.3*+1.020 + 0.25*UA + 0.15*-0.109)*0.80 - 0.00` | 304.76 | +6.0% | 15.28% | 323.05 | +0.173 | 0.37 | -7.03% | S6/S6/S2 | 79.9/73.1/69.9 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 19 | **MSFT** | Technology | 96.48 | **+0.2305** | `(0.3*UA + 0.3*+0.967 + 0.25*UA + 0.15*-0.013)*0.80 - 0.00` | 487.65 | +6.0% | 16.05% | 516.91 | +1.066 | 0.35 | -23.38% | S5/S4/S2 | 78.3/64.0/57.0 | ABOVE/ABOVE/BELOW | none | MEDIUM |
| 20 | **PCAR** | Consumer Discretionary | 96.28 | **+0.2303** | `(0.3*UA + 0.3*+0.862 + 0.25*UA + 0.15*+0.195)*0.80 - 0.00` | 132.06 | +6.0% | 8.90% | 139.98 | +1.034 | 0.64 | -5.86% | B2/S9/S2 | 59.7/66.7/66.6 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 21 | **LH** | Health Care | 96.09 | **+0.2282** | `(0.3*UA + 0.3*+0.820 + 0.25*UA + 0.15*+0.261)*0.80 - 0.00` | 307.42 | +6.0% | 7.92% | 325.87 | -0.106 | 0.72 | -6.20% | B1/S7/S2 | 65.4/66.2/63.5 | ABOVE/ABOVE/ABOVE | none | MEDIUM |
| 22 | **COF** | Finance | 95.89 | **+0.2274** | `(0.3*UA + 0.3*+0.632 + 0.25*UA + 0.15*+0.630)*0.80 - 0.00` | 217.68 | +6.0% | 8.96% | 230.74 | +1.005 | 0.63 | -7.77% | S6/S2/S3 | 64.7/60.4/59.8 | BULL_X/ABOVE/BELOW | none | MEDIUM |
| 23 | **BX** | Finance | 95.69 | **+0.2199** | `(0.3*UA + 0.3*+0.595 + 0.25*UA + 0.15*+0.644)*0.80 - 0.00` | 134.68 | +6.0% | 11.12% | 142.76 | +1.177 | 0.51 | -11.64% | S1/S6/S3 | 64.8/58.2/51.6 | ABOVE/ABOVE/BELOW | none | MEDIUM |
| 24 | **HIG** | Finance | 95.50 | **+0.2190** | `(0.3*UA + 0.3*+0.721 + 0.25*UA + 0.15*+0.383)*0.80 - 0.00` | 142.90 | +6.0% | 6.50% | 151.47 | -0.629 | 0.87 | -7.43% | B1/S7/S2 | 58.6/61.0/65.0 | ABOVE/ABOVE/BELOW | none | MEDIUM |

All 24 are **monitoring-sleeve forecasts**, published so they stay settleable. None is a
recommendation.

## No-trade rationale

| Evidence threshold | Result | Binding reason |
|---|---|---|
| 1. Pctl >= 80th | PASS | 103 names qualify |
| 2. >= 3 of 4 families non-negative | **FAIL** | only 2 of 4 families exist; an `UNAVAILABLE` family cannot count |
| 3. No family > 50% of conviction | **FAIL** | Technical carries 66.67% of live conviction for every name |
| 4. Data completeness >= 85% | **FAIL** | DQ 0.80 < 0.85 |
| 5. No hard stop | PASS | none triggered |

Zero names clear all five, so `rules.md § Downgrade to NO_TRADE` #1 binds. For completeness, the
naive top-20 equal-weight diagnostic sleeve would independently breach the 8% drawdown cap
(8.50%) and sit below the beta floor (+0.5323) — but the run never
reaches sizing.

## Assumptions and limitations

1. **Two of four factor families have no fetch path.** Everything above rests on price-derived
   evidence only. This is the single highest-value open item and it is an engineering task.
2. **The composite's rank ordering is anti-correlated with realized alpha** (rank IC -0.0879,
   n=515, non-positive in 20/32 vintages). Every confidence label is capped at
   `MEDIUM` in response.
3. **`eff_n` = 1.** All 515 canonical settlements still fall in one overlapping 28-day window, so
   no Track A calibration change is licensed. Projection: 2026-08-05 for
   `EQUITY_ALPHA`, 2026-08-09 for `MARKET_FORECAST`.
4. **Normality is assumed** for VaR95, CVaR95 and the 95th-percentile drawdown estimate.
5. **Constituent caches are 43 days old**, used as-is per the index-union protocol.
6. **`sigma` is `REALIZED_VOL_30D` throughout** — no options feed, so IV30 is unavailable.
7. **The Tech_Z engine changed this run.** Rank comparability with packages before 2026-08-03 is broken by
   design; the measured turnover is in `05`.

## Next scheduled review

Next daily run 2026-08-04 pre-open. Weekly parameter review Friday
2026-08-07. `EQUITY_ALPHA` `eff_n` is projected to reach 2 on
**2026-08-05**, which is the first date any Track A calibration work
becomes arguable.
