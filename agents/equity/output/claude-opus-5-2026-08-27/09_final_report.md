```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-27
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

Run Status: NO_TRADE

## Executive summary

A post-close fire on a completed 2026-08-27 regular session grounded all five Required inputs and
scored the full 515-name S&P 500 union Nasdaq-100 index union (509 names after
filters), but published **zero investable names**. Two independent causes each force `NO_TRADE`: the
fundamental and sentiment factor families remain `UNAVAILABLE` universe-wide, so evidence thresholds
2, 3 and 4 are arithmetically unsatisfiable; and the 24-name monitoring sleeve is so defensive
that its maximum attainable portfolio beta (+0.2919) falls far below the 0.90
floor, with Health Care at 41.67% against a 30% cap. The run's real output is
the settlement layer — **229 of 231 due predictions settled** with zero
conflicts, taking canonical `EQUITY_ALPHA` `n` to 1355. That batch returned a
26.73% hit rate and confirms the standing diagnosis: with two families dark,
`Tech_Z` is 66.7% of conviction and is pure trend persistence, which the settled record shows is
anti-correlated with forward alpha.

## MoM Reflection Summary

Baseline `claude-opus-5-2026-07-30`, selected from a delta-0d tie with `gpt-5-2026-07-30` under
`agents.md` rule 8(a). Both tied books are disclosed in `02 § 1` and the conclusion is
**invariant** across them (hit-rate spread 3.3pp,
both deeply negative on mean alpha). The baseline book scored **16.67%** on
alpha over the 28-day window with mean alpha **-7.20%**; only
2 of its 24 names survive into today's
sleeve. No new facts are introduced here — see `02`.

## Regime

| Regime | Data quality | Data mode | Key macro risk | Ledger rows |
|---|---|---|---|---|
| **BULL** | 0.80 (two of four families UNAVAILABLE) | `DELAYED` | Narrow leadership inside a rising tape: 37.33% of names are daily-MA-bullish while 42.83% carry a negative 60d beta — a rotation, not a broad advance | L003, L003b, L007, L013, L020 |

## Core ETF market forecast

Summarizing `03`; no new facts.

| ETF | Entry | Price Date | mu | sigma | Target | 70% CI | Target Date | Confidence |
|---|---|---|---|---|---|---|---|---|
| SPY | 771.10 | 2026-08-27 | +2.0000% | 3.49% | 786.52 | 758.55 – 814.49 | 2026-09-24 | MEDIUM |
| QQQ | 721.11 | 2026-08-27 | +2.4418% | 6.09% | 738.72 | 693.04 – 784.40 | 2026-09-24 | MEDIUM |
| SOXX | 525.43 | 2026-08-27 | +5.6956% | 14.38% | 555.36 | 476.75 – 633.96 | 2026-09-24 | MEDIUM |

## Ranked candidates — monitoring sleeve only (24 names, 0 investable)

| Rank | Ticker | Company | Sector | Entry | Adj Score | Pctl | Score Trace | mu | sigma | Target | 70% CI | Beta | Sharpe | Max DD60 | TD9 D/W | RSI14 D/W | MACD D/W | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SJM | The J.M. Smucker Company Common St | Consumer Staples | 131.84 | +0.3392 | 100.00 | (0.30x`UNAVL` + 0.30x+1.4397 + 0.25x`UNAVL` + 0.15x-0.0531) x 0.80 - 0.00 = +0.3392 | +6.00% | 8.68% | 139.75 | 127.85 – 151.65 | -0.6986 | 0.6559 | -8.42% | SELL_SETUP_9 / SELL_SETUP_7 | 72.1 / 74.5 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 2 | RVTY | Revvity Inc. Common Stock | Industrials | 129.71 | +0.3357 | 99.80 | (0.30x`UNAVL` + 0.30x+1.3875 + 0.25x`UNAVL` + 0.15x+0.0221) x 0.80 - 0.00 = +0.3357 | +6.00% | 9.93% | 137.49 | 124.10 – 150.89 | +0.4440 | 0.5733 | -6.38% | SELL_SETUP_7 / SELL_SETUP_4 | 72.2 / 71.6 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 3 | GILD | Gilead Sciences Inc. Common Stock | Health Care | 148.86 | +0.2983 | 99.61 | (0.30x`UNAVL` + 0.30x+0.8990 + 0.25x`UNAVL` + 0.15x+0.6874) x 0.80 - 0.00 = +0.2983 | +6.00% | 7.47% | 157.79 | 146.22 – 169.36 | +0.1043 | 0.7616 | -5.96% | SELL_SETUP_9 / SELL_SETUP_4 | 69.2 / 66.8 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 4 | BLK | BlackRock Inc. Common Stock | Finance | 1167.57 | +0.2977 | 99.41 | (0.30x`UNAVL` + 0.30x+0.7774 + 0.25x`UNAVL` + 0.15x+0.9256) x 0.80 - 0.00 = +0.2977 | +6.00% | 6.76% | 1237.62 | 1155.49 – 1319.76 | +0.8465 | 0.8416 | -10.14% | SELL_SETUP_5 / SELL_SETUP_9 | 61.0 / 62.4 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 5 | AMGN | Amgen Inc. Common Stock | Health Care | 436.99 | +0.2949 | 99.21 | (0.30x`UNAVL` + 0.30x+1.0188 + 0.25x`UNAVL` + 0.15x+0.4200) x 0.80 - 0.00 = +0.2949 | +6.00% | 7.75% | 463.21 | 427.99 – 498.43 | +0.1414 | 0.7346 | -5.05% | BUY_SETUP_1 / SELL_SETUP_9 | 68.9 / 74.4 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 6 | JNJ | Johnson & Johnson Common Stock | Health Care | 265.77 | +0.2918 | 99.02 | (0.30x`UNAVL` + 0.30x+0.9190 + 0.25x`UNAVL` + 0.15x+0.5937) x 0.80 - 0.00 = +0.2918 | +6.00% | 6.20% | 281.72 | 264.57 – 298.86 | -0.7412 | 0.9179 | -7.57% | BUY_SETUP_1 / SELL_SETUP_4 | 54.6 / 63.9 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 7 | RMD | ResMed Inc. Common Stock | Health Care | 235.76 | +0.2915 | 98.82 | (0.30x`UNAVL` + 0.30x+0.9423 + 0.25x`UNAVL` + 0.15x+0.5445) x 0.80 - 0.00 = +0.2915 | +6.00% | 9.85% | 249.91 | 225.74 – 274.07 | +0.1495 | 0.5776 | -12.68% | SELL_SETUP_7 / SELL_SETUP_5 | 66.4 / 59.7 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 8 | A | Agilent Technologies Inc. Common S | Industrials | 157.69 | +0.2907 | 98.62 | (0.30x`UNAVL` + 0.30x+1.2053 + 0.25x`UNAVL` + 0.15x+0.0121) x 0.80 - 0.00 = +0.2907 | +6.00% | 8.26% | 167.15 | 153.60 – 180.70 | +0.3635 | 0.6891 | -10.15% | BUY_SETUP_3 / SELL_SETUP_8 | 70.3 / 69.1 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 9 | VEEV | Veeva Systems Inc. Class A Common  | Technology | 282.13 | +0.2901 | 98.43 | (0.30x`UNAVL` + 0.30x+1.3802 + 0.25x`UNAVL` + 0.15x-0.3429) x 0.80 - 0.00 = +0.2901 | +6.00% | 16.61% | 299.06 | 250.31 – 347.80 | +0.4655 | 0.3427 | -16.28% | SELL_SETUP_1 / SELL_SETUP_9 | 79.6 / 73.6 | `BULLISH_CROSS` / `ABOVE_SIGNAL` | MEDIUM |
| 10 | NWSA | News Corporation Class A Common St | Consumer Discretionary | 31.19 | +0.2868 | 98.23 | (0.30x`UNAVL` + 0.30x+1.2435 + 0.25x`UNAVL` + 0.15x-0.0965) x 0.80 - 0.00 = +0.2868 | +6.00% | 8.39% | 33.06 | 30.34 – 35.78 | -0.3845 | 0.6784 | -9.72% | SELL_SETUP_9 / SELL_SETUP_8 | 71.3 / 69.4 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 11 | FTNT | Fortinet Inc. Common Stock | Technology | 172.78 | +0.2842 | 98.03 | (0.30x`UNAVL` + 0.30x+1.0794 + 0.25x`UNAVL` + 0.15x+0.2095) x 0.80 - 0.00 = +0.2842 | +6.00% | 12.43% | 183.15 | 160.81 – 205.49 | +1.1979 | 0.4578 | -10.40% | SELL_SETUP_3 / SELL_SETUP_2 | 64.7 / 75.3 | `BULLISH_CROSS` / `ABOVE_SIGNAL` | MEDIUM |
| 12 | STT | State Street Corporation Common St | Finance | 193.37 | +0.2784 | 97.83 | (0.30x`UNAVL` + 0.30x+0.7371 + 0.25x`UNAVL` + 0.15x+0.8453) x 0.80 - 0.00 = +0.2784 | +6.00% | 6.74% | 204.97 | 191.42 – 218.52 | +0.6448 | 0.8449 | -5.65% | SELL_SETUP_3 / SELL_SETUP_9 | 62.1 / 81.8 | `BULLISH_CROSS` / `ABOVE_SIGNAL` | MEDIUM |
| 13 | BNY | The Bank of New York Mellon Corpor | Finance | 162.24 | +0.2774 | 97.64 | (0.30x`UNAVL` + 0.30x+0.6397 + 0.25x`UNAVL` + 0.15x+1.0325) x 0.80 - 0.00 = +0.2774 | +6.00% | 5.60% | 171.97 | 162.52 – 181.43 | +0.4917 | 1.0161 | -5.69% | SELL_SETUP_3 / SELL_SETUP_9 | 57.5 / 76.0 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 14 | SCHW | Charles Schwab Corporation (The) C | Finance | 108.05 | +0.2760 | 97.44 | (0.30x`UNAVL` + 0.30x+0.8276 + 0.25x`UNAVL` + 0.15x+0.6445) x 0.80 - 0.00 = +0.2760 | +6.00% | 5.68% | 114.53 | 108.15 – 120.92 | -0.1050 | 1.0017 | -5.36% | BUY_SETUP_2 / SELL_SETUP_9 | 51.7 / 64.2 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 15 | NWS | News Corporation Class B Common St | Consumer Discretionary | 35.32 | +0.2752 | 97.24 | (0.30x`UNAVL` + 0.30x+1.1709 + 0.25x`UNAVL` + 0.15x-0.0487) x 0.80 - 0.00 = +0.2752 | +6.00% | 8.74% | 37.44 | 34.23 – 40.65 | -0.4122 | 0.6512 | -10.48% | SELL_SETUP_9 / SELL_SETUP_8 | 70.1 / 67.6 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 16 | VRTX | Vertex Pharmaceuticals Incorporate | Health Care | 547.55 | +0.2724 | 97.05 | (0.30x`UNAVL` + 0.30x+0.9129 + 0.25x`UNAVL` + 0.15x+0.4441) x 0.80 - 0.00 = +0.2724 | +6.00% | 8.43% | 580.40 | 532.39 – 628.41 | +0.1165 | 0.6752 | -11.12% | BUY_SETUP_1 / SELL_SETUP_4 | 65.1 / 68.9 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 17 | BAC | Bank of America Corporation Common | Finance | 61.17 | +0.2701 | 96.85 | (0.30x`UNAVL` + 0.30x+0.7732 + 0.25x`UNAVL` + 0.15x+0.7048) x 0.80 - 0.00 = +0.2701 | +6.00% | 4.79% | 64.84 | 61.80 – 67.88 | +0.3191 | 1.1895 | -5.62% | BUY_SETUP_1 / BUY_SETUP_2 | 43.1 / 62.4 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 18 | MPC | Marathon Petroleum Corporation Com | Energy | 363.54 | +0.2670 | 96.65 | (0.30x`UNAVL` + 0.30x+1.3078 + 0.25x`UNAVL` + 0.15x-0.3904) x 0.80 - 0.00 = +0.2670 | +6.00% | 10.59% | 385.35 | 345.33 – 425.37 | -0.2006 | 0.5378 | -9.09% | SELL_SETUP_2 / SELL_SETUP_9 | 69.5 / 76.6 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 19 | CRL | Charles River Laboratories Interna | Health Care | 296.41 | +0.2641 | 96.46 | (0.30x`UNAVL` + 0.30x+0.9789 + 0.25x`UNAVL` + 0.15x+0.2429) x 0.80 - 0.00 = +0.2641 | +6.00% | 13.32% | 314.19 | 273.15 – 355.24 | +0.5021 | 0.4275 | -6.38% | SELL_SETUP_7 / SELL_SETUP_9 | 73.9 / 77.3 | `BEARISH_CROSS` / `ABOVE_SIGNAL` | MEDIUM |
| 20 | BMY | Bristol-Myers Squibb Company Commo | Health Care | 66.95 | +0.2633 | 96.26 | (0.30x`UNAVL` + 0.30x+0.6392 + 0.25x`UNAVL` + 0.15x+0.9162) x 0.80 - 0.00 = +0.2633 | +6.00% | 6.73% | 70.97 | 66.28 – 75.65 | +0.0222 | 0.8463 | -5.71% | BUY_SETUP_1 / SELL_SETUP_9 | 60.3 / 68.5 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 21 | TGT | Target Corporation Common Stock | Consumer Discretionary | 165.93 | +0.2614 | 96.06 | (0.30x`UNAVL` + 0.30x+1.1096 + 0.25x`UNAVL` + 0.15x-0.0407) x 0.80 - 0.00 = +0.2614 | +6.00% | 8.64% | 175.89 | 160.97 – 190.80 | +0.0147 | 0.6586 | -10.69% | SELL_SETUP_7 / SELL_SETUP_5 | 69.0 / 75.6 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 22 | TECH | Bio-Techne Corp Common Stock | Health Care | 72.48 | +0.2568 | 95.87 | (0.30x`UNAVL` + 0.30x+0.4908 + 0.25x`UNAVL` + 0.15x+1.1583) x 0.80 - 0.00 = +0.2568 | +6.00% | 1.18% | 76.83 | 75.94 – 77.72 | +0.6904 | 4.8104 | -4.02% | SELL_SETUP_2 / SELL_SETUP_9 | 69.5 / 66.0 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 23 | PFE | Pfizer Inc. Common Stock | Health Care | 28.02 | +0.2556 | 95.67 | (0.30x`UNAVL` + 0.30x+0.7495 + 0.25x`UNAVL` + 0.15x+0.6313) x 0.80 - 0.00 = +0.2556 | +6.00% | 5.92% | 29.70 | 27.97 – 31.43 | +0.0138 | 0.9609 | -9.69% | BUY_SETUP_1 / SELL_SETUP_6 | 65.4 / 66.8 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 24 | ABT | Abbott Laboratories Common Stock | Health Care | 111.59 | +0.2554 | 95.47 | (0.30x`UNAVL` + 0.30x+0.6296 + 0.25x`UNAVL` + 0.15x+0.8693) x 0.80 - 0.00 = +0.2554 | +6.00% | 6.24% | 118.29 | 111.04 – 125.53 | -0.4252 | 0.9119 | -7.18% | BUY_SETUP_2 / SELL_SETUP_9 | 57.6 / 60.3 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |

## No-trade rationale

| Cause | Rule | Evidence |
|---|---|---|
| Fewer than 5 investable names | `rules.md § Downgrade to NO_TRADE` #1 | 0 names clear evidence thresholds 2 (>= 3 of 4 families non-negative), 3 (no family > 50% of conviction) and 4 (data completeness >= 85%) — all three fail from the single cause that `Fund_Z`/`Sent_Z` have no wired fetch path (`05`, L021, L022) |
| Structurally infeasible investable set | `rules.md § Downgrade to NO_TRADE` #6 | 5% single-name cap forces >= 20 names, so max attainable sleeve beta = +0.2919 vs the 0.90 floor; Health Care 41.67% vs the 30% cap (`07`, L016) |

Both are composition failures, not integrity failures, so `HALTED` does not apply
(`§ Hard Halt Criteria` #5). `REVIEW_ONLY` does not apply either: it is reserved for stale or weak
data, and every Required input is grounded at zero lag to a completed session.

## Portfolio analytics (diagnostic only — no proposal)

| Analytic | Value | Cap | Status |
|---|---|---|---|
| Naive top-20 EW expected beta | +0.1633 | 0.90 – 1.10 | **FAIL (too low)** |
| Max attainable sleeve beta | +0.2919 | >= 0.90 | **FAIL** |
| Average pairwise correlation | 0.1416 | < 0.45 | PASS |
| 95th-pctl 1-month drawdown | 6.38% | <= 8% | PASS |
| Max sector share | 41.67% (Health Care) | <= 30% | **FAIL** |

## Settlement layer

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` |
|---|---|---|
| Settled this run | 202 | 27 |
| Canonical n (post-write) | 1355 | 201 |
| 28-day `eff_n` | 2 | 2 |
| Hit rate (all time) | 37.49% | 40.11% |
| CI coverage (all time) | 71.88% | 90.55% |
| Mean z (all time) | -0.5553 | -0.1848 |
| Track A calibration eligible | False | False |

Two `EQR` keys were left **due** as `UNSETTLEABLE_CORPORATE_ACTION` rather than settled against the
successor symbol `VMRK` (`02 § 0`, L025a).

## Assumptions and limitations

1. **Two of four factor families are dark.** `Fund_Z` and `Sent_Z` are `UNAVAILABLE` for every name.
   No ranking outcome could have produced an investable name today; this is a capability gap, not a
   market call.
2. **`Tech_Z` is trend persistence.** It carries 66.7% of live conviction and mechanically ranks the
   trailing 60-day winners first. The settled record (aggregate rank IC -0.0840 over
   60 vintages) says that ordering is anti-correlated with forward alpha.
3. **Normality is assumed** for VaR95, CVaR95 and the 95th-percentile drawdown estimate.
4. **The constituent caches are 67 days stale** (2026-06-21). `rules.md` requires
   using them anyway; the cost is that delisted and renamed names survive in the union until the
   corporate-action classifier catches them (`04`, L025).
5. **The bid-ask exclusion filter could not be applied** — no spread tape is wired. It is an
   Enhancing input and never a `GO` blocker.
6. **No FOMC calendar is wired.** The event-concentration section records that field as
   `UNAVAILABLE` rather than asserting that no meeting falls inside the horizon.
7. **No brokerage cross-check.** The IBKR MCP connector has been invalidated since 2026-08-04;
   grounding rests on three independent web sources, which met the standard on
   27/27 symbols at
   0.095123% max deviation.
8. **Paper forecasts, not recommendations.** All 24 sleeve names carry settleable `mu`/`sigma`
   and are written to `15_predictions.json` under `NO_TRADE`. `rules.md § Settlement Rules` requires
   this — paper forecasts are how the system earns the evidence to ever publish `GO`.

## Next scheduled review

Next daily run per `runbook.md § Cadence`. Two dated commitments carry forward: `EQUITY_ALPHA`
`eff_n` is projected to reach 3 on **2026-09-03** and
`MARKET_FORECAST` on **2026-09-07**, at which point the
deferred Track A calibration work becomes eligible. This run's Track B change takes effect on the
next run unless reverted (`13`).
