# 09 — Final Report · 2026-09-03

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-09-03
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## 1. Executive summary

All five Required inputs are grounded and 508 index-union names were scored on a
2026-09-03 close, but no name is investable because `Fund_Z` and `Sent_Z` remain
`UNAVAILABLE` universe-wide, making three of the five evidence thresholds unsatisfiable by
construction. 111 of 113 due prediction keys settled with
zero conflicts, and that settlement pushed `EQUITY_ALPHA` `eff_n` from 2 to **3** on
exactly the date the 2026-07-28 projection named — unblocking Track A calibration work for the
first time in the series. The run declines to spend that eligibility, because the diagnosed defect
is a rank-order inversion and every tested remedy so far has been a monotonic transform that
cannot repair one. The one process change accepted this run is a fire-window and vendor-lag rule
prompted by 22 live large-caps that had no basis bar at the 18:11 ET primary fetch.

## 2. MoM Reflection Summary

Summarises `02`; introduces no new facts.

| Item | Value |
|---|---|
| Baseline | `claude-opus-5-2026-08-06` (delta 0d, flag `OK`, no tie at that delta) |
| Baseline book result | 12 of 24 HIT (50.00%), mean alpha -0.68% |
| Baseline vintage rank IC | +0.2739 — positive over this window |
| Settled this run | 111 rows (96 EQUITY_ALPHA, 15 MARKET_FORECAST), 0 conflicts |
| Left due | 2 — 2 corporate action; see `02 § 0` |
| Canonical rolling EQUITY_ALPHA | raw n **1451**, 28-day eff_n **3**, hit 38.11%, CI 71.74%, mean z -0.5517 |
| Canonical rolling MARKET_FORECAST | raw n **216**, 28-day eff_n **2**, hit 43.75%, CI 91.20%, mean z -0.1868 |
| Carry-forward | 10 CARRY, 8 DROP, 6 DOWNGRADE |

## 3. Regime

| Regime | Data quality | Key macro risk | Ledger rows |
|---|---|---|---|
| **`BULL`** (7/7 classification tests bullish) | 0.80 — two of four factor families unsourceable | VIX 14.32 is deep in the low-vol band; a vol expansion would hit the trend-persistence leaderboard hardest, and the sleeve's negative-beta tilt gives it no market-direction protection either way | L003, L003b, L003d, L007, L007a, L008, L020 |

## 4. Core ETF market forecast

Summarises `03 § Core ETF Market Forecast Block`; no new facts.

| ETF | Entry | Beta vs SPY | mu | sigma | Target | 70% CI | RS20 / RS60 vs SPY | Confidence |
|---|---|---|---|---|---|---|---|---|
| SPY | 773.17 | 1.0000 (self) | +2.00% | 3.30% | 788.63 | 762.10 - 815.17 | +0.00% / +0.00% | MEDIUM |
| QQQ | 717.67 | 1.7006 | +1.90% | 5.71% | 731.31 | 688.68 - 773.95 | -0.18% / -3.67% | MEDIUM |
| SOXX | 502.20 | 3.2402 | +4.98% | 13.88% | 527.21 | 454.74 - 599.68 | -6.29% / -15.79% | MEDIUM |

`03` records the one internal inconsistency in this block: SOXX is the weakest ETF on relative
strength yet carries the highest mu, because `mu = beta x SPY_mu` scales with a beta of
3.2402 and the permitted ±1.5pp relative-view adjustment cannot
overcome it. That is the 2026-07-24 category error, still standing.

## 5. Ranked candidates (24 names, monitoring sleeve only)

| Rank | Ticker | Sector | Entry | Adj Score | Pctl | Score Trace | mu | sigma | Target | 70% CI | Beta | Sharpe | IR | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | VLO | Energy | 370.69 | +0.3727 | 100.00 | (0.30x`UNAVL` + 0.30x+1.4152 + 0.25x`UNAVL` + 0.15x+0.2756) x 0.80 - 0.00 = +0.3727 | +6.00% | 8.44% | 392.93 | 360.41 - 425.45 | -0.3804 | +0.6742 | +0.6754 | -8.65% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 75.26 / 78.49 / 87.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 2 | SPGI | Finance | 450.58 | +0.3607 | 99.80 | (0.30x`UNAVL` + 0.30x+1.0592 + 0.25x`UNAVL` + 0.15x+0.8874) x 0.80 - 0.00 = +0.3607 | +6.00% | 7.75% | 477.61 | 441.29 - 513.93 | +0.0145 | +0.7338 | +0.6046 | -11.40% | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_3 | 63.17 / 57.77 / 52.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 3 | PFG | Finance | 118.51 | +0.3554 | 99.61 | (0.30x`UNAVL` + 0.30x+1.2136 + 0.25x`UNAVL` + 0.15x+0.5348) x 0.80 - 0.00 = +0.3554 | +6.00% | 7.54% | 125.62 | 116.32 - 134.92 | +0.2053 | +0.7541 | +0.7718 | -6.16% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_9 | 68.60 / 70.87 / 74.48 | `BULLISH_CROSS` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | MEDIUM |
| 4 | GILD | Health Care | 151.19 | +0.3390 | 99.41 | (0.30x`UNAVL` + 0.30x+1.1288 + 0.25x`UNAVL` + 0.15x+0.5676) x 0.80 - 0.00 = +0.3390 | +6.00% | 7.45% | 160.26 | 148.54 - 171.98 | +0.0885 | +0.7631 | +0.6767 | -5.17% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 68.29 / 68.28 / 71.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 5 | AMP | Finance | 565.08 | +0.3354 | 99.21 | (0.30x`UNAVL` + 0.30x+0.8574 + 0.25x`UNAVL` + 0.15x+1.0804) x 0.80 - 0.00 = +0.3354 | +6.00% | 5.43% | 598.98 | 567.08 - 630.89 | +0.4205 | +1.0475 | +0.7892 | -5.34% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.50 / 69.99 / 62.87 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | MEDIUM |
| 6 | IQV | Health Care | 271.62 | +0.3349 | 99.01 | (0.30x`UNAVL` + 0.30x+1.4310 + 0.25x`UNAVL` + 0.15x-0.0713) x 0.80 - 0.00 = +0.3349 | +6.00% | 13.80% | 287.92 | 248.93 - 326.91 | -0.3776 | +0.4121 | +0.5338 | -9.92% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_4 | 75.17 / 75.13 / 63.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 7 | RVTY | Industrials | 130.63 | +0.3329 | 98.82 | (0.30x`UNAVL` + 0.30x+1.3888 + 0.25x`UNAVL` + 0.15x-0.0035) x 0.80 - 0.00 = +0.3329 | +6.00% | 9.28% | 138.47 | 125.86 - 151.08 | +0.3067 | +0.6126 | +0.5309 | -6.38% | SELL_SETUP_9 / SELL_SETUP_5 / SELL_SETUP_4 | 68.62 / 72.12 / 60.61 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 8 | TECH | Health Care | 72.45 | +0.3192 | 98.62 | (0.30x`UNAVL` + 0.30x+0.7951 + 0.25x`UNAVL` + 0.15x+1.0699) x 0.80 - 0.00 = +0.3192 | +6.00% | 0.99% | 76.80 | 76.05 - 77.55 | +0.6375 | +5.7278 | +0.3635 | -4.02% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 66.10 / 65.94 / 55.46 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 9 | PSX | Energy | 254.66 | +0.3190 | 98.42 | (0.30x`UNAVL` + 0.30x+1.3457 + 0.25x`UNAVL` + 0.15x-0.0329) x 0.80 - 0.00 = +0.3190 | +6.00% | 8.27% | 269.94 | 248.03 - 291.85 | -0.6267 | +0.6876 | +0.8271 | -8.57% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 74.81 / 78.77 / 81.33 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 10 | STT | Finance | 193.94 | +0.3157 | 98.22 | (0.30x`UNAVL` + 0.30x+0.9025 + 0.25x`UNAVL` + 0.15x+0.8260) x 0.80 - 0.00 = +0.3157 | +6.00% | 7.01% | 205.58 | 191.44 - 219.71 | +0.7401 | +0.8115 | +0.7057 | -5.65% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.03 / 82.05 / 88.94 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 11 | GEN | Technology | 31.33 | +0.3148 | 98.03 | (0.30x`UNAVL` + 0.30x+1.2613 + 0.25x`UNAVL` + 0.15x+0.1009) x 0.80 - 0.00 = +0.3148 | +6.00% | 9.25% | 33.21 | 30.20 - 36.22 | +0.4304 | +0.6150 | +0.5329 | -7.85% | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_5 | 67.86 / 69.20 / 62.25 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 12 | ICE | Finance | 164.59 | +0.3113 | 97.83 | (0.30x`UNAVL` + 0.30x+0.8835 + 0.25x`UNAVL` + 0.15x+0.8271) x 0.80 - 0.00 = +0.3113 | +6.00% | 6.24% | 174.47 | 163.78 - 185.15 | -0.0545 | +0.9113 | +0.7777 | -13.00% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 68.48 / 61.15 / 54.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 13 | BNY | Finance | 164.33 | +0.3027 | 97.63 | (0.30x`UNAVL` + 0.30x+0.7190 + 0.25x`UNAVL` + 0.15x+1.0849) x 0.80 - 0.00 = +0.3027 | +6.00% | 5.32% | 174.19 | 165.10 - 183.28 | +0.5101 | +1.0692 | +0.7909 | -5.69% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.86 / 77.20 / 91.64 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 14 | DE | Industrials | 694.41 | +0.2997 | 97.44 | (0.30x`UNAVL` + 0.30x+1.3196 + 0.25x`UNAVL` + 0.15x-0.1415) x 0.80 - 0.00 = +0.2997 | +6.00% | 11.08% | 736.07 | 656.09 - 816.06 | +0.4694 | +0.5135 | +0.5087 | -9.25% | SELL_SETUP_4 / SELL_SETUP_5 / SELL_SETUP_9 | 68.67 / 65.74 / 67.59 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 15 | JNJ | Health Care | 278.43 | +0.2946 | 97.24 | (0.30x`UNAVL` + 0.30x+0.9583 + 0.25x`UNAVL` + 0.15x+0.5388) x 0.80 - 0.00 = +0.2946 | +6.00% | 6.07% | 295.14 | 277.56 - 312.71 | -0.7306 | +0.9372 | +1.1075 | -7.57% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_9 | 65.95 / 69.40 / 79.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 16 | VRTX | Health Care | 557.96 | +0.2822 | 97.04 | (0.30x`UNAVL` + 0.30x+0.9749 + 0.25x`UNAVL` + 0.15x+0.4020) x 0.80 - 0.00 = +0.2822 | +6.00% | 8.22% | 591.44 | 543.74 - 639.14 | +0.1882 | +0.6919 | +0.6570 | -11.12% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_3 | 67.51 / 69.51 / 64.46 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 17 | MPC | Energy | 387.71 | +0.2800 | 96.84 | (0.30x`UNAVL` + 0.30x+1.2621 + 0.25x`UNAVL` + 0.15x-0.1906) x 0.80 - 0.00 = +0.2800 | +6.00% | 10.42% | 410.97 | 368.95 - 452.99 | -0.4642 | +0.5458 | +0.7050 | -7.84% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_8 | 77.86 / 79.52 / 86.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 18 | WFC | Finance | 89.19 | +0.2688 | 96.65 | (0.30x`UNAVL` + 0.30x+0.7511 + 0.25x`UNAVL` + 0.15x+0.7379) x 0.80 - 0.00 = +0.2688 | +6.00% | 6.13% | 94.54 | 88.85 - 100.23 | +0.4222 | +0.9274 | +0.8075 | -5.88% | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_4 | 61.84 / 58.56 / 65.31 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 19 | ELV | Health Care | 414.78 | +0.2675 | 96.45 | (0.30x`UNAVL` + 0.30x+0.6114 + 0.25x`UNAVL` + 0.15x+1.0062) x 0.80 - 0.00 = +0.2675 | +6.00% | 6.68% | 439.67 | 410.86 - 468.47 | +0.1601 | +0.8517 | +0.5512 | -12.64% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_6 | 62.76 / 61.87 / 55.81 | `ABOVE_SIGNAL` / `BELOW_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 20 | RJF | Finance | 181.10 | +0.2628 | 96.25 | (0.30x`UNAVL` + 0.30x+0.7020 + 0.25x`UNAVL` + 0.15x+0.7863) x 0.80 - 0.00 = +0.2628 | +6.00% | 6.56% | 191.97 | 179.61 - 204.32 | +0.4144 | +0.8671 | +0.7735 | -6.10% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.09 / 66.38 / 63.10 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | MEDIUM |
| 21 | DELL | Technology | 516.39 | +0.2605 | 96.06 | (0.30x`UNAVL` + 0.30x+1.4805 + 0.25x`UNAVL` + 0.15x-0.7900) x 0.80 - 0.00 = +0.2605 | +6.00% | 24.80% | 547.37 | 414.21 - 680.53 | +2.7270 | +0.2294 | +0.0271 | -19.09% | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_7 | 62.55 / 71.51 / 85.88 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 22 | BIIB | Health Care | 224.51 | +0.2558 | 95.86 | (0.30x`UNAVL` + 0.30x+0.7022 + 0.25x`UNAVL` + 0.15x+0.7276) x 0.80 - 0.00 = +0.2558 | +6.00% | 7.62% | 237.98 | 220.18 - 255.78 | +0.0234 | +0.7462 | +0.5327 | -11.39% | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.50 / 68.75 / 61.91 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 23 | PRU | Finance | 123.20 | +0.2552 | 95.66 | (0.30x`UNAVL` + 0.30x+0.7051 + 0.25x`UNAVL` + 0.15x+0.7169) x 0.80 - 0.00 = +0.2552 | +6.00% | 5.73% | 130.59 | 123.26 - 137.93 | +0.3048 | +0.9932 | +0.9266 | -5.30% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_4 | 60.95 / 68.44 / 64.68 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 24 | SCHW | Finance | 110.38 | +0.2540 | 95.46 | (0.30x`UNAVL` + 0.30x+0.6887 + 0.25x`UNAVL` + 0.15x+0.7391) x 0.80 - 0.00 = +0.2540 | +6.00% | 5.57% | 117.00 | 110.61 - 123.39 | -0.0491 | +1.0216 | +0.9099 | -5.36% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 57.13 / 68.58 / 67.90 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |

## 6. No-trade rationale

| Trigger | Rule | Evidence |
|---|---|---|
| Fewer than 5 names pass the investable threshold | `rules.md § Downgrade to NO_TRADE` #1 | 0 names pass; evidence thresholds 2, 3 and 4 fail universe-wide (`06`) |
| Publishing would require violating the beta band | `rules.md § Downgrade to NO_TRADE` #6 | the rank-ordered top-20 sleeve has beta +0.1187 against a 0.90 floor and 40.00% in one sector against a 30% cap (`07`) |

The band itself is **attainable** (-0.6671 to
+1.4337); the failure is composition, not infeasibility. Both the
2026-08-22 and 2026-08-27 runs found the opposite, so the feasibility narrative is recomputed
every run rather than carried.

## 7. Assumptions and limitations

| # | Assumption / limitation |
|---|---|
| 1 | Return and indicator math uses **adjusted** closes; entry, target and CI prices use **raw** closes (Track B 2026-07-26). Mixing them silently is the corporate-action basis bug that produced a 4.6x sigma error on 2026-07-24. |
| 2 | Parametric normality is assumed for VaR95, CVaR95 and the 95th-percentile drawdown (`1.65 x sigma`, `2.06 x sigma`). |
| 3 | Constituent caches are 74 days old (L001). `rules.md` requires using them as-is and logging `fetched_at`; staleness is what leaves renamed and delisted names in the union. |
| 4 | No options feed is wired, so sigma never reaches the IV30 step of the fallback chain. |
| 5 | The IBKR MCP connector has been invalidated since 2026-08-04 and was not attempted; grounding rests on three independent web sources (L017). |
| 6 | 2 prediction key(s) can never settle because the underlying ticker no longer trades. No exchange ratio was inferred (L025a). |
| 7 | `Fund_Z` and `Sent_Z` are `UNAVAILABLE` for the whole universe. Every published score is a Technical+Macro composite, and Technical alone carries 66.7% of live conviction. |

## 8. Next scheduled review

Next daily run: **2026-09-04** (Friday) —
a Friday close also owes `14_weekly_review.md`. The Track B accepted below is effective from that
run. `MARKET_FORECAST` `eff_n` is projected to reach 3 on
**2026-09-07**
(3 pending), which is when the core-ETF
mu prior table becomes Track-A eligible.
