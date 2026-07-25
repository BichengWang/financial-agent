```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-24
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

A flat index is concealing a violent internal rotation: SPY sits 2.7% off its high while SOXX is down 19.5% from its own, and **40.9% of the 514-name universe now carries a negative 60-day beta to SPY**. The leaderboard is accordingly a single defensive trade — insurers, rails, defense, healthcare services and utilities — led by TRV at the 100th percentile. No name is investable: `Fund_Z` and `Sent_Z` remain unavailable universe-wide, so evidence thresholds #2 and #4 fail for all 514 names, unchanged since 2026-07-15. Independently of that, portfolio construction establishes that this leaderboard **cannot** be assembled inside the 0.90–1.10 beta band — the highest beta available in the top 10 is +0.114 — nor under the 30% sector cap, with Industrials at 60% of the top 10. The run publishes `NO_TRADE` with 26 settleable monitoring forecasts and three ETF market forecasts.

## MoM Reflection Summary

Baseline `gpt-5-2026-06-24` (`CROSS_MODEL_BASELINE`, 30 days old; no `claude-opus-5` folder exists — this is the model's first run). Over the month SPY returned **+0.78%**; the baseline's 14 names scored **9 Hit / 5 Miss (64.3%) on alpha**.

The month rewarded duration and rate positioning rather than sector or quality buckets: healthcare (LLY +6.27pp, UNH +2.91pp) and energy (CVX +12.84pp) validated fully, banks validated on their 07-14 prints (BAC +6.71pp, JPM +5.15pp), while capital-goods industrials failed outright (CAT −11.41pp, GE −4.10pp). The prior run's top-ranked name, CAT, now ranks 482nd of 514.

Carry-forward: **2 CARRY** (BAC, JPM), **3 DOWNGRADE** (AAPL, UNH, LLY), **9 DROP**. Full table in `02_reflection.md`.

**Settlement:** nothing matured on or before today. `settlement_ledger.py --as-of 2026-07-24` returns `due_inventory 0`, `conflicts 0`; the next 17 keys mature 2026-07-26 (Sunday) and will settle `WEEKEND_TARGET` at today's close on the next run.

**Rolling calibration:** `EQUITY_ALPHA` n=189 — hit 52.91%, CI coverage 76.19%, mean z −0.213 (all healthy). `MARKET_FORECAST` n=33 — hit **21.21%**, mean z **−0.731** (broken). Weighted rank IC **−0.0939** → confidence capped at `MEDIUM` system-wide. **Caveat established this run: those n values are pseudo-replicated — the effective independent sample is 1 window per type** (see `13_evolution_log.md`).

## Regime

| Item | Assessment | Key evidence | Ledger |
|---|---|---|---|
| **Regime** | **`NEUTRAL`** | SPY −2.72% from 60d high with +3.83% 60d momentum, but below MA20 (746.15) and MA50 (745.07); daily MACD `BELOW_SIGNAL`, weekly `BEARISH_CROSS` | L001-series, `technical_indicators.json` |
| Volatility | Not elevated | SPY 30d realized vol 3.92% (≈13.5% ann.); VIX 18.58 vs avg60 17.36; only 3.3% of the last 60 sessions closed above 20 | L137 |
| Breadth | Healthy | 54.5% above MA20; 64.6% above MA50; median 20d momentum +1.64%; 58.9% positive | L139 |
| **Internal dispersion** | **Extreme** | median 60d beta +0.232; **40.9% of names negative**; SOXX RS20 −16.34% vs SPY | L140 |
| Rates | Pressure, not shock | TLT −4.69% (20d); 13-week bill 3.81%, stable | L136, L138 |
| Data quality | 0.80 | Two of four factor families `UNAVAILABLE`; all Enhancing inputs absent | L144–L146 |
| **Key macro risk** | A reversal of the rotation — semis bouncing or long yields retreating — would hit every name on this leaderboard simultaneously | — | — |

`BEAR` and `HIGH_VOL` are rejected on the drawdown/breadth and vol evidence respectively; `RATE_SHOCK` is the closest rejected call but the front end is stable and the bond move is an ordinary repricing.

## Core ETF Market Forecast

Summarised from `03_regime_and_data.md`. No new facts.

| ETF | Entry | Px Date | Tag | Trend (20d/50d) | 30d RVol | RVol Trend | Beta vs SPY | DD from 60d High | mu | sigma | Sigma Src | Target | Target Date | CI70 Lo | CI70 Hi | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 738.93 | 2026-07-24 | DELAYED | MA20 746.15 / MA50 745.07 (MIXED) | 3.92% | RISING | 1.0000 | -2.72% | +0.00% | 3.92% | REALIZED_VOL_30D | 738.93 | 2026-08-21 | 708.82 | 769.04 | MEDIUM |
| QQQ | 684.23 | 2026-07-24 | DELAYED | MA20 711.71 / MA50 718.29 (BEARISH) | 7.96% | RISING | 1.7222 | -8.30% | -1.00% | 7.96% | REALIZED_VOL_30D | 677.39 | 2026-08-21 | 620.75 | 734.03 | MEDIUM |
| SOXX | 527.01 | 2026-07-24 | DELAYED | MA20 565.45 / MA50 569.22 (BEARISH) | 20.18% | RISING | 3.6366 | -19.54% | -1.50% | 20.18% | REALIZED_VOL_30D | 519.10 | 2026-08-21 | 408.50 | 629.71 | MEDIUM |

- Relative strength: QQQ/SPY **−5.12%** (20d) vs **+0.23%** (60d); SOXX/SPY **−16.34%** (20d) vs **+16.30%** (60d) — leadership given back violently in a month.
- `mu` derivation: SPY = `NEUTRAL` prior +0.5% **−0.5pp** (below both MAs, MACD below signal, weekly bearish cross, rising vol) → **0.00%**. QQQ and SOXX take `beta × SPY_mu` = 0.00% plus band adjustments of −1.0pp and −1.5pp for their own documented weakness.
- **Two disclosures.** With SPY mu at exactly 0.00% the beta multiplier degenerates, so the QQQ and SOXX forecasts come entirely from the adjustment band rather than the beta rule — direct evidence for the structural flaw analysed in `13`. And `|SPY mu| < 0.5%` means SPY settles `N/A - FLAT_CALL`, with only CI and z scored.

## Ranked Candidates

26 monitoring-sleeve names, all `LOW` confidence, target date **2026-08-21**. Entry prices are the 2026-07-24 official close, each confirmed by three independent sources at 0.000% difference. Compact traces and full metrics in `05`/`06`.

| # | Ticker | Sector | Entry | Adj Score (compact trace) | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | MaxDD60 | RSI14 D | MACD D/W | TD9 D/W | RS20 | Days→Earn | mu | Target | CI70 | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TRV | Finance | 387.26 | (.30×+1.11+.15×+0.84)×.80−0.00=+0.3680 | 100.0 | -0.693 | 9.33% | 0.61 | 1.71 | 0.80 | -5.96% | 80.8 | ABOV/ABOV | SELL_6/SELL_8 | +21.04% | 84 | +6.0% | 410.50 | 372.93–448.06 | LOW |
| 2 | PAYX | Industrials | 113.55 | (.30×+0.87+.15×+0.80)×.80−0.00=+0.3037 | 99.8 | -0.638 | 9.45% | 0.60 | 1.37 | 0.66 | -6.35% | 64.6 | ABOV/ABOV | BUY_3/SELL_9 | +16.77% | 83 | +6.0% | 120.36 | 109.21–131.52 | LOW |
| 3 | DGX | Health Care | 227.86 | (.30×+0.89+.15×+0.75)×.80−0.00=+0.3028 | 99.6 | -0.568 | 9.62% | 0.59 | 1.9 | 0.76 | -6.60% | 72.1 | ABOV/ABOV | SELL_7/SELL_5 | +9.85% | 90 | +6.0% | 241.53 | 218.74–264.33 | LOW |
| 4 | UNP | Industrials | 307.32 | (.30×+0.87+.15×+0.75)×.80−0.00=+0.2991 | 99.4 | -0.164 | 7.32% | 0.78 | 1.17 | 0.81 | -8.06% | 72.8 | ABOV/ABOV | SELL_2/SELL_5 | +14.16% | 90 | +6.0% | 325.76 | 302.38–349.14 | LOW |
| 5 | PCG | Utilities | 17.85 | (.30×+0.72+.15×+0.89)×.80−0.00=+0.2798 | 99.2 | -0.268 | 7.19% | 0.79 | 1.32 | 0.80 | -5.71% | 59.8 | ABOV/ABOV | SELL_3/SELL_3 | +3.88% | 89 | +6.0% | 18.92 | 17.59–20.26 | LOW |
| 6 | RTX | Industrials | 212.79 | (.30×+0.99+.15×+0.60)×.80−0.05=+0.2598 | 99.0 | -0.040 | 9.75% | 0.58 | 1.06 | 0.69 | -5.58% | 74.0 | ABOV/ABOV | SELL_3/SELL_9 | +13.41% | 90 | +6.0% | 225.56 | 203.97–247.14 | LOW |
| 7 | NSC | Industrials | 350.66 | (.30×+0.69+.15×+0.76)×.80−0.00=+0.2571 | 98.8 | -0.107 | 7.05% | 0.81 | 1.32 | 0.85 | -7.86% | 73.2 | ABOV/ABOV | SELL_2/SELL_5 | +11.74% | 90 | +6.0% | 371.70 | 345.98–397.42 | LOW |
| 8 | GD | Industrials | 386.75 | (.30×+1.01+.15×+0.76)×.80−0.10=+0.2337 | 98.6 | +0.008 | 7.57% | 0.75 | 1.25 | 0.75 | -5.70% | 70.0 | ABOV/ABOV | SELL_5/SELL_4 | +11.57% | 5 | +6.0% | 409.95 | 379.49–440.42 | LOW |
| 9 | CSX | Industrials | 53.23 | (.30×+0.79+.15×+0.76)×.80−0.05=+0.2315 | 98.4 | +0.114 | 7.22% | 0.79 | 1.63 | 0.89 | -4.20% | 76.0 | ABOV/ABOV | SELL_2/SELL_9 | +11.57% | 90 | +6.0% | 56.42 | 52.43–60.42 | LOW |
| 10 | CTAS | UNAVAIL | 205.91 | (.30×+0.67+.15×+0.57)×.80−0.00=+0.2279 | 98.2 | -0.287 | 10.33% | 0.55 | 1.21 | 0.67 | -7.19% | 72.1 | ABOV/ABOV | SELL_1/SELL_5 | +21.15% | 83 | +6.0% | 218.26 | 196.14–240.39 | LOW |
| 11 | PM | UNAVAIL | 193.00 | (.30×+0.64+.15×+0.62)×.80−0.00=+0.2272 | 98.0 | -0.542 | 9.43% | 0.60 | 1.28 | 0.68 | -10.01% | 59.4 | ABOV/ABOV | SELL_1/SELL_2 | +7.23% | 83 | +6.0% | 204.58 | 185.65–223.51 | LOW |
| 12 | MPC | Energy | 309.24 | (.30×+1.04+.15×+0.60)×.80−0.10=+0.2224 | 97.9 | -0.445 | 9.70% | 0.59 | 1.04 | 0.59 | -9.09% | 68.1 | ABOV/ABOV | BUY_2/SELL_5 | +21.33% | 11 | +6.0% | 327.79 | 296.60–358.99 | LOW |
| 13 | LMT | Industrials | 582.60 | (.30×+0.76+.15×+0.27)×.80−0.00=+0.2155 | 97.7 | -0.441 | 12.88% | 0.44 | 1.14 | 0.62 | -10.40% | 71.5 | ABOV/BELO | SELL_3/SELL_1 | +14.73% | 90 | +6.0% | 617.56 | 539.50–695.61 | LOW |
| 14 | PKG | Consumer Discretionary | 254.39 | (.30×+0.81+.15×+0.10)×.80−0.00=+0.2063 | 97.5 | +0.794 | 9.96% | 0.57 | 1.26 | 0.65 | -10.43% | 72.1 | BULL/ABOV | SELL_2/SELL_7 | +4.89% | 91 | +6.0% | 269.65 | 243.30–296.01 | LOW |
| 15 | TMO | Industrials | 568.26 | (.30×+0.85+.15×+0.39)×.80−0.05=+0.2025 | 97.3 | +0.093 | 10.22% | 0.56 | 1.93 | 0.59 | -8.48% | 70.8 | ABOV/ABOV | SELL_2/SELL_9 | +11.73% | 90 | +6.0% | 602.36 | 541.97–662.74 | LOW |
| 16 | SJM | Consumer Staples | 118.32 | (.30×+0.45+.15×+0.74)×.80−0.00=+0.1974 | 97.1 | -0.715 | 9.47% | 0.60 | 1.07 | 0.61 | -8.42% | 61.1 | ABOV/ABOV | SELL_7/SELL_2 | +4.54% | 33 | +6.0% | 125.42 | 113.76–137.07 | LOW |
| 17 | BNY | Finance | 158.91 | (.30×+0.52+.15×+0.59)×.80−0.00=+0.1962 | 96.9 | +0.585 | 7.38% | 0.77 | 1.49 | 0.97 | -3.34% | 63.5 | ABOV/ABOV | SELL_2/SELL_9 | +8.64% | 82 | +6.0% | 168.44 | 156.24–180.65 | LOW |
| 18 | VLO | Energy | 302.50 | (.30×+0.96+.15×+0.48)×.80−0.10=+0.1887 | 96.7 | -0.735 | 11.78% | 0.48 | 1.12 | 0.54 | -10.02% | 63.0 | ABOV/ABOV | BUY_2/SELL_5 | +17.97% | 6 | +6.0% | 320.65 | 283.59–357.71 | LOW |
| 19 | MTB | Finance | 249.60 | (.30×+0.42+.15×+0.73)×.80−0.00=+0.1881 | 96.5 | +0.293 | 6.37% | 0.89 | 1.4 | 0.96 | -6.66% | 62.5 | BELO/ABOV | SELL_1/SELL_8 | +4.79% | 82 | +6.0% | 264.58 | 248.04–281.11 | LOW |
| 20 | MET | Finance | 94.83 | (.30×+0.80+.15×+0.80)×.80−0.10=+0.1878 | 96.3 | +0.003 | 7.26% | 0.78 | 1.18 | 0.91 | -4.77% | 67.1 | BELO/ABOV | SELL_1/SELL_9 | +11.42% | 12 | +6.0% | 100.52 | 93.36–107.68 | LOW |
| 21 | HIG | Finance | 140.53 | (.30×+0.68+.15×+0.98)×.80−0.10=+0.1811 | 96.1 | -0.576 | 6.26% | 0.91 | 1.76 | 1.00 | -7.95% | 58.1 | ABOV/ABOV | SELL_5/SELL_5 | +7.16% | 4 | +6.0% | 148.96 | 139.81–158.11 | LOW |
| 22 | BAC | Finance | 62.05 | (.30×+0.32+.15×+0.78)×.80−0.00=+0.1692 | 92.6 | +0.274 | 5.57% | 0.84 | 1.42 | 0.85 | -7.15% | 68.4 | BELO/ABOV | SELL_3/SELL_8 | +6.00% | 81 | +5.0% | 65.15 | 61.56–68.75 | LOW |
| 23 | JPM | Finance | 353.21 | (.30×+0.33+.15×+0.74)×.80−0.00=+0.1674 | 92.0 | +0.295 | 6.54% | 0.72 | 1.19 | 0.78 | -6.10% | 68.2 | ABOV/ABOV | SELL_3/SELL_8 | +4.77% | 81 | +5.0% | 370.87 | 346.85–394.89 | LOW |
| 24 | AAPL | UNAVAIL | 333.02 | (.30×+0.88+.15×+0.13)×.80−0.10=+0.1271 | 78.0 | +0.498 | 9.68% | 0.17 | 0.24 | 0.25 | -12.71% | 65.2 | ABOV/ABOV | SELL_1/SELL_4 | +20.40% | 6 | +2.0% | 339.68 | 306.14–373.22 | LOW |
| 25 | UNH | Health Care | 420.74 | (.30×+0.13+.15×+0.79)×.80−0.00=+0.1263 | 77.8 | -0.042 | 7.29% | 0.23 | 0.67 | 0.27 | -6.06% | 51.5 | BELO/ABOV | BUY_2/BUY_1 | +0.62% | 88 | +2.0% | 429.15 | 397.25–461.06 | LOW |
| 26 | LLY | UNAVAIL | 1196.03 | (.30×+0.65+.15×+0.52)×.80−0.10=+0.1190 | 75.6 | +0.070 | 9.49% | 0.18 | 0.43 | 0.18 | -7.18% | 57.0 | BELO/ABOV | SELL_2/BUY_1 | +5.43% | 12 | +2.0% | 1219.95 | 1101.96–1337.94 | LOW |

**Investable set: empty (0 of 514).** Thresholds #2 (≥3 of 4 families non-negative — only 2 exist) and #4 (data completeness ≥85% — actual 80%) fail for every name in the universe.

## Portfolio Analytics — No-Trade Rationale

No weights proposed. `rules.md § Downgrade to NO_TRADE` conditions **1, 4 and 6** are met:

| Constraint | Cap | Computed | Verdict |
|---|---|---|---|
| Investable names | ≥ 5 | **0** | fails |
| Portfolio beta | 0.90 – 1.10 | equal-weight **−0.264**; max attainable **+0.114** | **infeasible** |
| Single sector | ≤ 30% | **Industrials 60%** of top 10 (30.8% of the 26-name sleeve) | **infeasible** |
| Names with earnings ≤ 14d | ≤ 2 | **7 of 26** | fails |
| Avg pairwise correlation | < 0.45 | 0.261 | passes |
| 95th-pctl 1m drawdown | ≤ 8% | 7.51% | passes |

The beta finding is the substantive one and is new to this stage: the rotation has placed every high-scoring name inside the negative-beta cohort, so a market-neutral-band portfolio is unreachable without importing names the model ranks in the bottom half. The mandatory feasibility pre-check caught this before any sizing, and the revision pass was not spent. Cause is set composition, not process integrity — so `NO_TRADE`, not `HALTED`.

## Assumptions and Limitations

1. **`Fund_Z` / `Sent_Z` unavailable** — the sole blocker to any `GO`. SHADOW tooling exists but covers ~4.7% of the universe against a 70% bar; Phase 2 was not attempted this run.
2. **All Enhancing inputs missing** — options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow. Correctly treated as confidence/exposure caps, never as `GO` blockers.
3. **Yahoo 429-blocked for the entire session**, both hosts, bulk and single-symbol. Nasdaq bulk historical carried the run; treat Yahoo availability as unstable rather than resolved despite its 2026-07-21 recovery.
4. **Six earnings dates rest on inference** (CB, HIG, WRB, EQR, AMP, JNJ — conservatively penalised) and BAC's non-penalty rests on a sub-threshold volume signal, labelled `INFERRED`.
5. **Sector medians substituted by universe median** for the volatility penalty — GICS labels are not sourceable universe-wide.
6. **Defensive Macro polarity is a disclosed regime-conditional judgment**, not a validated rule and not a family-weight change.
7. **Signal decay is the leading risk to today's forecasts** — 9 of the top 15 names printed earnings within the last 7 sessions, so their momentum scores rest substantially on one already-realised gap.
8. **VaR95/CVaR95 and the drawdown estimate are parametric**, assuming normality, from the same sigma as the forecast.
9. **Rolling calibration statistics are pseudo-replicated** — effective independent N is 1 window per type, not 189/33.
10. `FDXF` excluded (41 bars since 2026-05-27, fails the listing-age and history minimums).

## Next Scheduled Review

| When | What |
|---|---|
| Next run (Mon 2026-07-27 or earlier) | Settle the 17 keys maturing 2026-07-26 under `WEEKEND_TARGET` at today's close. **Apply the accepted Track B `eff_n` reporting change** from `13_evolution_log.md`. |
| 2026-07-31 | Month-end structural review (`16_monthly_review.md`) — the queued regime→prior mapping review, now informed by this run's effective-sample finding. |
| 2026-08-21 | Target date for all 29 forecasts published today. |

**Status: `NO_TRADE`.** Full package published; `15_predictions.json` contains 26 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` records and `settlements: []` with note.
