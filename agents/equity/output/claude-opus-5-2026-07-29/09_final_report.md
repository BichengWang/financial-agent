# 09 Final Report — 2026-07-29

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-29
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

A pre-open run on a fully-grounded 2026-07-28 price basis produced **no investable names**, so the status
is `NO_TRADE` and 24 names publish as a settleable monitoring sleeve. The block is structural,
not market-driven: `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide, which makes three of the five
evidence thresholds unreachable for every one of the 514 scored names. The run's substantive finding is
a **defect in earnings-date grounding** — the retired vendor-empty heuristic scored six names as clear
of earnings when all six report today — now replaced by a complete forward calendar sweep that grounds
514/514 names and is this run's accepted Track B change.
44 predictions settled cleanly, leaving due inventory 0 and conflicts 0.

## MoM Reflection Summary

Baseline `claude-fable-5-2026-07-01` (`CROSS_MODEL_BASELINE`): 24 names,
**62.5% alpha-based hit rate**, mean alpha +2.11%, CI
coverage 83.3%. Three folders tied at exactly the target date and `agents.md`
has no tie-break rule; the alternate (`gpt-5-2026-07-01`) returns 14.3% with mean
alpha -14.24%, so **the conclusion is not invariant to a coin flip**. The spread is
a composition effect — the two books shared only 6 of 32 names, and the semiconductor-heavy one was
destroyed over the window. Detail in `02`.

Settlement this run: 38 equity (17/38 HIT, 28/38 `IN_CI`, mean z
-0.6858) and 6 market-forecast records (**6/6 MISS**, all `IN_CI`).

## Regime

| Field | Value | Ledger |
|---|---|---|
| Regime | **NEUTRAL** | L042 |
| Data quality | `DELAYED`, DQ multiplier 0.8 | L049 |
| SPY vs MA20 / MA50 | 740.86 vs 746.65 / 743.99 — below both | L004, L021 |
| VIX | 18.21 | L008 |
| Key macro risk | A flat index masking a 25.0% semis drawdown with 42.0% of the universe at negative beta — a rotation, not a broad drawdown | L006, L015 |

## Core ETF Market Forecast

Summarizing `03` — no new facts. Target date 2026-08-26.

| ETF | Entry | Beta vs SPY | mu | sigma | Target | CI Lo | CI Hi | DD from 60d high | 30d Vol | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 740.86 | +1.0000 | +0.5000% | 3.68% | 744.56 | 716.24 | 772.89 | -2.21% | FALLING | MEDIUM |
| QQQ | 675.49 | +1.7309 | +0.8654% | 7.39% | 681.34 | 629.39 | 733.28 | -9.37% | RISING | MEDIUM |
| SOXX | 491.46 | +3.6481 | +1.8241% | 19.18% | 500.42 | 402.39 | 598.46 | -24.97% | RISING | MEDIUM |

**Read this table with the disclosure in `03`:** the mu column is produced by
`mu = beta × SPY_prior`, which mechanically assigns the largest positive expected return to the most
beaten-down, highest-beta ETF. That rule has a 18.52% direction rate over n=54.
Correcting it is a Track A change gated at `eff_n = 1` until
2026-08-09; it is applied as written and disclosed rather than
hand-overridden.

## Ranked Candidates — Monitoring Sleeve (24 names, zero investable)

Percentiles are `INDEX_UNION_PCTL (n=514)`. Every `mu` is the mu-Calibration-Table `+6.0%` band
(all names at or above the 95th percentile), unadjusted. Every `sigma` is `REALIZED_VOL_30D`.

| Rank | Ticker | Adj Score | Pctl | Compact Trace | Beta | 30d RVol | Sharpe | Sortino | IR | MaxDD60 | TD9 D | RSI14 D | MACD D | Days→Earn | mu | sigma | Target | CI Lo | CI Hi | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TRV | +0.3311 | 100.00 | 0.30×+0.962+0.15×+0.835 ×0.8 −0.00 | -0.729 | 9.32% | 0.6100 | 1.7076 | 0.8693 | -5.96% | SELL_SETUP_8 | 83.33 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 9.32% | 421.05 | 382.55 | 459.56 | MEDIUM |
| 2 | PAYX | +0.3283 | 99.81 | 0.30×+1.004+0.15×+0.727 ×0.8 −0.00 | -0.562 | 9.73% | 0.5844 | 1.3375 | 0.6965 | -6.35% | SELL_SETUP_2 | 73.00 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 9.73% | 126.00 | 113.97 | 138.03 | MEDIUM |
| 3 | INCY | +0.3174 | 99.61 | 0.30×+1.194+0.15×+0.257 ×0.8 −0.00 | -0.356 | 12.94% | 0.4394 | 0.8457 | 0.5664 | -9.50% | SELL_SETUP_3 | 76.76 | BULLISH_CROSS | >2026-09-04 | +6.0% | 12.94% | 137.73 | 120.24 | 155.21 | MEDIUM |
| 4 | BRO | +0.3034 | 99.42 | 0.30×+0.923+0.15×+0.683 ×0.8 −0.00 | -0.990 | 11.54% | 0.4926 | 1.4159 | 0.6581 | -6.59% | SELL_SETUP_2 | 69.06 | BULLISH_CROSS | >2026-09-04 | +6.0% | 11.54% | 78.07 | 69.23 | 86.91 | MEDIUM |
| 5 | RTX | +0.2925 | 99.22 | 0.30×+0.908+0.15×+0.621 ×0.8 −0.00 | -0.105 | 9.49% | 0.5989 | 1.0365 | 0.7017 | -5.58% | SELL_SETUP_5 | 77.42 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 9.49% | 231.69 | 210.11 | 253.28 | MEDIUM |
| 6 | KO | +0.2867 | 99.03 | 0.30×+0.750+0.15×+0.889 ×0.8 −0.00 | -0.639 | 8.21% | 0.6925 | 1.3266 | 0.9465 | -6.23% | SELL_SETUP_3 | 67.03 | BULLISH_CROSS | >2026-09-04 | +6.0% | 8.21% | 93.57 | 86.03 | 101.10 | MEDIUM |
| 7 | MRSH | +0.2796 | 98.83 | 0.30×+0.741+0.15×+0.848 ×0.8 −0.00 | -0.872 | 9.59% | 0.5932 | 1.3437 | 0.8362 | -6.28% | SELL_SETUP_2 | 70.50 | BULLISH_CROSS | >2026-09-04 | +6.0% | 9.59% | 203.72 | 184.56 | 222.88 | MEDIUM |
| 8 | IQV | +0.2690 | 98.64 | 0.30×+1.233+0.15×-0.226 ×0.8 −0.00 | +0.199 | 16.02% | 0.3550 | 1.0069 | 0.4000 | -10.23% | SELL_SETUP_4 | 79.55 | BULLISH_CROSS | >2026-09-04 | +6.0% | 16.02% | 257.52 | 217.05 | 297.98 | MEDIUM |
| 9 | CTAS | +0.2563 | 98.44 | 0.30×+0.780+0.15×+0.576 ×0.8 −0.00 | -0.295 | 10.04% | 0.5663 | 1.3277 | 0.6730 | -7.19% | SELL_SETUP_3 | 77.29 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 10.04% | 227.79 | 205.35 | 250.23 | MEDIUM |
| 10 | ITW | +0.2527 | 98.25 | 0.30×+0.762+0.15×+0.582 ×0.8 −0.00 | +0.560 | 7.27% | 0.7826 | 1.6290 | 0.9490 | -5.65% | SELL_SETUP_4 | 72.92 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 7.27% | 312.87 | 290.57 | 335.17 | MEDIUM |
| 11 | PM | +0.2513 | 98.05 | 0.30×+0.742+0.15×+0.611 ×0.8 −0.00 | -0.575 | 9.46% | 0.6009 | 1.2425 | 0.7163 | -10.01% | SELL_SETUP_3 | 65.71 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 9.46% | 212.18 | 192.48 | 231.88 | MEDIUM |
| 12 | VLTO | +0.2356 | 97.86 | 0.30×+0.580+0.15×+0.804 ×0.8 −0.00 | -0.406 | 7.77% | 0.7320 | 1.5331 | 0.8543 | -7.33% | SELL_SETUP_2 | 70.19 | BULLISH_CROSS | >2026-09-04 | +6.0% | 7.77% | 104.38 | 96.42 | 112.33 | MEDIUM |
| 13 | WELL | +0.2315 | 97.66 | 0.30×+0.576+0.15×+0.777 ×0.8 −0.00 | -0.646 | 7.23% | 0.7864 | 1.4217 | 0.8505 | -11.26% | BUY_SETUP_1 | 60.30 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 7.23% | 258.18 | 239.87 | 276.50 | MEDIUM |
| 14 | UNP | +0.2268 | 97.47 | 0.30×+0.585+0.15×+0.720 ×0.8 −0.00 | -0.211 | 7.85% | 0.7239 | 1.1658 | 0.8135 | -7.58% | SELL_SETUP_4 | 57.11 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 7.85% | 312.12 | 288.06 | 336.17 | MEDIUM |
| 15 | SJM | +0.2185 | 97.27 | 0.30×+0.548+0.15×+0.725 ×0.8 −0.00 | -0.792 | 9.73% | 0.5846 | 1.1665 | 0.6469 | -8.42% | SELL_SETUP_9 | 67.23 | ABOVE_SIGNAL | 28d | +6.0% | 9.73% | 130.42 | 117.98 | 142.87 | MEDIUM |
| 16 | SCHW | +0.2134 | 97.08 | 0.30×+0.503+0.15×+0.772 ×0.8 −0.00 | -0.331 | 7.70% | 0.7385 | 1.2078 | 0.8274 | -7.62% | SELL_SETUP_2 | 69.81 | BULLISH_CROSS | >2026-09-04 | +6.0% | 7.70% | 112.33 | 103.84 | 120.81 | MEDIUM |
| 17 | ACGL | +0.2127 | 96.88 | 0.30×+0.454+0.15×+0.865 ×0.8 −0.00 | -0.753 | 7.44% | 0.7644 | 1.5742 | 1.0359 | -9.52% | SELL_SETUP_3 | 67.47 | BULLISH_CROSS | >2026-09-04 | +6.0% | 7.44% | 112.87 | 104.63 | 121.11 | MEDIUM |
| 18 | ADP | +0.2058 | 96.69 | 0.30×+0.930+0.15×+0.689 ×0.8 −0.10 | -0.649 | 10.00% | 0.5688 | 1.3449 | 0.6983 | -7.49% | SELL_SETUP_2 | 69.25 | BULLISH_CROSS | 0d | +6.0% | 10.00% | 280.02 | 252.56 | 307.48 | LOW |
| 19 | OMC | +0.2035 | 96.49 | 0.30×+0.730+0.15×+0.236 ×0.8 −0.00 | +0.109 | 11.66% | 0.4876 | 0.6751 | 0.5848 | -8.77% | SELL_SETUP_2 | 65.22 | BULLISH_CROSS | >2026-09-04 | +6.0% | 11.66% | 91.39 | 80.94 | 101.85 | MEDIUM |
| 20 | DGX | +0.2004 | 96.30 | 0.30×+0.660+0.15×+0.767 ×0.8 −0.05 | -0.642 | 9.64% | 0.5895 | 1.9766 | 0.8404 | -6.22% | SELL_SETUP_9 | 77.23 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 9.64% | 250.10 | 226.43 | 273.76 | MEDIUM |
| 21 | BBY | +0.1978 | 96.10 | 0.30×+0.713+0.15×+0.222 ×0.8 −0.00 | +0.790 | 9.04% | 0.6293 | 1.1331 | 0.4359 | -8.93% | SELL_SETUP_3 | 72.57 | ABOVE_SIGNAL | 29d | +6.0% | 9.04% | 94.84 | 86.43 | 103.25 | MEDIUM |
| 22 | PFG | +0.1972 | 95.91 | 0.30×+0.439+0.15×+0.766 ×0.8 −0.00 | -0.048 | 7.31% | 0.7780 | 0.9822 | 0.9508 | -6.16% | SELL_SETUP_2 | 60.61 | BELOW_SIGNAL | >2026-09-04 | +6.0% | 7.31% | 120.94 | 112.26 | 129.61 | MEDIUM |
| 23 | EXR | +0.1946 | 95.71 | 0.30×+0.401+0.15×+0.819 ×0.8 −0.00 | -0.002 | 6.83% | 0.8324 | 1.7325 | 0.9050 | -5.45% | SELL_SETUP_3 | 62.32 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 6.83% | 161.34 | 150.53 | 172.16 | MEDIUM |
| 24 | TMO | +0.1942 | 95.52 | 0.30×+0.601+0.15×+0.416 ×0.8 −0.00 | +0.056 | 10.31% | 0.5514 | 1.8403 | 0.5805 | -7.61% | SELL_SETUP_4 | 70.22 | ABOVE_SIGNAL | >2026-09-04 | +6.0% | 10.31% | 610.99 | 549.18 | 672.81 | MEDIUM |

## Portfolio Analytics — No-Trade Rationale

No portfolio was constructed, so portfolio-level analytics are **N/A**, not omitted.

Zero of 514 names clear `rules.md § Evidence Thresholds`. Three tests fail universe-wide:

1. **>= 3 of 4 families non-negative** — only Technical and Macro are sourceable (L046, L047).
2. **No family > 50% of conviction** — Technical carries 0.30 of the 0.45 available weight (66.7%).
3. **Data completeness >= 85%** — DQ is 0.8 (L049).

`rules.md § Downgrade to NO_TRADE` #1 (fewer than 5 investable names) therefore applies.

**Portfolio feasibility was checked and is *not* the binding constraint.** The Task-0 pre-check finds
the maximum attainable sleeve beta at the 5% single-name cap is
**+0.9090** against the 0.90 floor — feasible, unlike 2026-07-27
(+0.8519, infeasible). The blocker is candidate quality alone.

## Assumptions and Limitations

- **Two of four factor families are unavailable, not neutral.** Every score in this package rests on
  Technical and Macro evidence only. This is the single largest limitation and it caps everything
  downstream.
- **The Macro polarity is a disclosed judgment** (L050), not a rule: lower beta, lower volatility and
  shallower drawdown score better because the regime evidence supports a defensive reading. It is
  supported by settled evidence this run (16.3pp realized
  mean-alpha spread between the defensive and semis books) but it would invert the leaderboard in a
  risk-on turn.
- **The monitoring sleeve is not a shadow portfolio.** 19 of 24 names carry negative beta and
  8 sit in Industrials; no correlation matrix or sector cap was
  applied because these are forecasts, not positions.
- **Rank order is inverted** (rank IC -0.2064 over 298 pairs). Confidence is capped at `MEDIUM`
  universe-wide as a result. Magnitude calibration is healthy (CI coverage
  74.50%, mean z -0.2596).
- **Three prior published packages (2026-07-26, -27, -28) relied on the earnings heuristic retired
  today** and should be treated as carrying an unquantified earnings-penalty error.
- **Enhancing inputs are entirely absent** — options IV/skew, short interest, bid-ask tape, analyst
  revisions, institutional flow (L036, L048). Per `rules.md`, these cap confidence and never block `GO`.
- Sector and market-cap labels come from a vendor screener (L010) and are not independently verified.

## Next Scheduled Review

| Checkpoint | When | Note |
|---|---|---|
| Next daily run | 2026-07-30 pre-open | |
| Weekly parameter review | Friday 2026-07-31, 17:15 ET | `14_weekly_review.md` |
| Month-end structural review | Friday 2026-07-31 (last July trading day) | `16_monthly_review.md` |
| `EQUITY_ALPHA` `eff_n` → 2 | **2026-08-05** | unlocks Track A once `n >= 20` and `eff_n >= 3` both hold |
| `MARKET_FORECAST` `eff_n` → 2 | **2026-08-09** | |
| These 24 forecasts settle | **2026-08-26** | |
