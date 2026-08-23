# 09 — Final Report · 2026-08-22

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-22
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

The run is **`NO_TRADE`** on five independent grounds, and the two newest ones are structural rather
than evidentiary: the published pool's maximum attainable sleeve beta is
**0.4841** against a 0.90 floor, and Health Care alone would be
**45.0%** of an equal-weighted sleeve against a 30% cap. Data quality was
the best of the series — 27/27 published prices agreed across three
independent vendors at **0.000000%** deviation, and a complete
26-day forward earnings sweep grounded the entire universe.
All **227** due predictions settled with zero conflicts and zero
unsettleable rows, and **`eff_n` moved off 1 to 2 for the first time**, exactly on the date the
2026-07-28 package projected. The binding constraint remains what it has been since the series began:
`Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide, so evidence thresholds 2, 3, and 4 are
arithmetically unsatisfiable no matter what the market does.

## MoM Reflection Summary

Summarizes `02`; introduces no new facts.

The MoM baseline is **`claude-opus-5-2026-07-24`**, selected from a two-way same-model tie at
`|folder_date − target| = 1d` by rule 8(c) (lexicographic). Both tied candidates are disclosed in
`02 § 1`; the hit-rate spread is **0.8pp** and the **conclusion is invariant** across
them — far tighter than the 48pp and 40.7pp spreads that motivated the rule.

The prior book returned **+1.03%** in absolute terms and
**-2.59%** of alpha, hitting on
**26.9%** of 26 names. It made
money and still lost decisively to SPY — the distinction the IR objective exists to capture. Its
single theme (low/negative-beta defensives) is judged **failed**: correct for the `NEUTRAL` regime it
was written in, wrong for the window that followed. Notably that book's *internal ordering* was
informative (vintage rank IC
+0.1330),
so the failure is regime timing, not stock selection.

**2 of today's 24
published names also appeared in that book** — the leaderboard regenerates itself because `Tech_Z` is
trend-persistence by construction.

## Regime

| Regime | Data quality | Key macro risk | Ledger rows |
|---|---|---|---|
| **`BULL`** (prior baseline: `NEUTRAL`) | 0.80 — two of four factor families `UNAVAILABLE` | Growth complex still trails the index (SOXX/SPY 60d -9.81%, QQQ/SPY 60d -4.28%) while VIX sits at 15.13 — a low-volatility advance with narrow leadership | L021, L003, L007, L020, L024 |

SPY is above both moving averages (`BULLISH`) with 20d momentum
+3.63%, realized vol falling from 4.41% to
3.56%, and VIX down from 16.01 to 15.13. The lone
dissenting signal is SPY's daily MACD at `BELOW_SIGNAL` (weekly reads
`ABOVE_SIGNAL`).

## Core ETF market forecast

Summarizes `03`; no new facts.

| ETF | Entry | Beta vs SPY | mu = beta x SPY mu | Adjustment | Final mu | sigma | Target | 70% CI Lo | 70% CI Hi | 20/60d Mom | RVol | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 765.72 | 1.0000 | +2.00% | +0.0pp | +2.00% | 3.56% | 781.03 | 752.69 | 809.38 | +3.63%/+2.29% | FALLING | MEDIUM |
| QQQ | 713.44 | 1.7144 | +3.43% | -1.0pp | +2.43% | 6.34% | 730.77 | 683.70 | 777.84 | +4.27%/-2.09% | FALLING | MEDIUM |
| SOXX | 520.05 | 3.3339 | +6.67% | -1.5pp | +5.17% | 15.28% | 546.93 | 464.29 | 629.56 | -1.32%/-7.75% | FALLING | MEDIUM |

## Ranked candidates — monitoring sleeve (24 names, 0 investable)

| Rank | Ticker | Sector | Entry | Pctl | Adj Score | Score Trace | Beta | 30d RVol | Max DD60 | 20/60d Mom | MA D/W | MACD D | RSI14 D | TD9 D | mu | sigma | Target | 70% CI | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BDX | Health Care | 192.00 | 100.00 | +0.3899 | 0.30x+1.4253+0.15x+0.3983 x0.80 | -0.094 | 8.16% | -7.45% | +22.8%/+31.3% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 78.5 | SELL_SETUP_3 | +6.00% | 8.16% | 203.52 | 187.22–219.82 | MEDIUM |
| 2 | SCHW | Finance | 112.30 | 99.80 | +0.3754 | 0.30x+1.1643+0.15x+0.7995 x0.80 | -0.065 | 5.18% | -5.36% | +10.4%/+31.6% | BULLISH/BULLISH | `BULLISH_CROSS` | 71.1 | SELL_SETUP_1 | +6.00% | 5.18% | 119.04 | 112.99–125.09 | MEDIUM |
| 3 | AMP | Finance | 555.59 | 99.61 | +0.3583 | 0.30x+0.9245+0.15x+1.1369 x0.80 | 0.348 | 5.17% | -5.34% | +5.4%/+25.8% | BULLISH/BULLISH | `BELOW_SIGNAL` | 57.9 | BUY_SETUP_5 | +6.00% | 5.17% | 588.93 | 559.04–618.81 | MEDIUM |
| 4 | CRL | Health Care | 295.19 | 99.41 | +0.3575 | 0.30x+1.3093+0.15x+0.3603 x0.80 | 0.606 | 13.48% | -6.38% | +30.3%/+79.5% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 76.3 | SELL_SETUP_3 | +6.00% | 13.48% | 312.90 | 271.52–354.28 | MEDIUM |
| 5 | REGN | Health Care | 834.04 | 99.21 | +0.3460 | 0.30x+1.1561+0.15x+0.5710 x0.80 | 0.270 | 8.66% | -5.32% | +27.3%/+33.0% | BULLISH/MIXED | `ABOVE_SIGNAL` | 76.5 | SELL_SETUP_5 | +6.00% | 8.66% | 884.08 | 809.01–959.16 | MEDIUM |
| 6 | FCX | Basic Materials | 76.66 | 99.02 | +0.3420 | 0.30x+1.2952+0.15x+0.2598 x0.80 | 2.358 | 14.48% | -19.83% | +22.5%/+20.8% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 69.3 | SELL_SETUP_3 | +6.00% | 14.48% | 81.26 | 69.71–92.81 | MEDIUM |
| 7 | RVTY | Industrials | 124.75 | 98.82 | +0.3417 | 0.30x+1.3185+0.15x+0.2107 x0.80 | 0.433 | 9.66% | -6.44% | +12.9%/+29.0% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 68.6 | SELL_SETUP_3 | +6.00% | 9.66% | 132.24 | 119.70–144.77 | MEDIUM |
| 8 | TGT | Consumer Discretionary | 165.44 | 98.62 | +0.3388 | 0.30x+1.4029+0.15x+0.0173 x0.80 | 0.019 | 8.02% | -10.69% | +21.9%/+29.9% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 76.5 | SELL_SETUP_3 | +6.00% | 8.02% | 175.37 | 161.57–189.17 | MEDIUM |
| 9 | NEM | Basic Materials | 131.58 | 98.43 | +0.3333 | 0.30x+1.2021+0.15x+0.3731 x0.80 | 1.832 | 14.24% | -18.77% | +41.2%/+22.7% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 75.9 | SELL_SETUP_3 | +6.00% | 14.24% | 139.47 | 119.99–158.96 | MEDIUM |
| 10 | TECH | Health Care | 72.32 | 98.23 | +0.3265 | 0.30x+0.8182+0.15x+1.0844 x0.80 | 0.745 | 1.25% | -4.02% | +1.0%/+50.4% | BULLISH/BULLISH | `BELOW_SIGNAL` | 67.7 | BUY_SETUP_2 | +6.00% | 1.25% | 76.66 | 75.72–77.60 | MEDIUM |
| 11 | LH | Health Care | 336.34 | 98.03 | +0.3138 | 0.30x+1.1779+0.15x+0.2590 x0.80 | -0.071 | 7.25% | -6.20% | +13.3%/+30.6% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 75.7 | SELL_SETUP_3 | +6.00% | 7.25% | 356.52 | 331.16–381.88 | MEDIUM |
| 12 | MRK | Health Care | 152.55 | 97.83 | +0.3113 | 0.30x+1.4270+0.15x-0.2595 x0.80 | -0.263 | 12.06% | -6.78% | +16.4%/+27.8% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 77.9 | SELL_SETUP_9 | +6.00% | 12.06% | 161.70 | 142.57–180.84 | MEDIUM |
| 13 | RJF | Finance | 175.20 | 97.64 | +0.3034 | 0.30x+0.7866+0.15x+0.9553 x0.80 | 0.252 | 5.57% | -6.10% | +3.5%/+20.9% | MIXED/BULLISH | `BELOW_SIGNAL` | 51.5 | BUY_SETUP_5 | +6.00% | 5.57% | 185.71 | 175.56–195.87 | MEDIUM |
| 14 | DE | Industrials | 647.47 | 97.44 | +0.2946 | 0.30x+1.1842+0.15x+0.0866 x0.80 | 0.631 | 10.16% | -9.25% | +3.1%/+22.6% | BULLISH/BULLISH | `BULLISH_CROSS` | 62.4 | SELL_SETUP_2 | +6.00% | 10.16% | 686.32 | 617.93–754.71 | MEDIUM |
| 15 | NDSN | Industrials | 332.24 | 97.24 | +0.2942 | 0.30x+1.2104+0.15x+0.0310 x0.80 | 0.710 | 8.23% | -6.81% | +12.3%/+15.4% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 72.5 | SELL_SETUP_2 | +6.00% | 8.23% | 352.17 | 323.75–380.60 | MEDIUM |
| 16 | AMGN | Health Care | 439.33 | 97.05 | +0.2833 | 0.30x+1.0351+0.15x+0.2903 x0.80 | 0.146 | 8.26% | -5.05% | +17.5%/+31.5% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 74.2 | SELL_SETUP_5 | +6.00% | 8.26% | 465.69 | 427.95–503.43 | MEDIUM |
| 17 | DXCM | Health Care | 92.34 | 96.85 | +0.2822 | 0.30x+0.9044+0.15x+0.5430 x0.80 | 0.460 | 14.86% | -13.86% | +29.1%/+31.4% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 70.0 | SELL_SETUP_2 | +6.00% | 14.86% | 97.88 | 83.61–112.15 | MEDIUM |
| 18 | SYF | Finance | 79.47 | 96.65 | +0.2791 | 0.30x+0.7749+0.15x+0.7762 x0.80 | 1.083 | 7.76% | -13.22% | +9.5%/+10.7% | BULLISH/BULLISH | `BELOW_SIGNAL` | 56.3 | BUY_SETUP_3 | +6.00% | 7.76% | 84.24 | 77.82–90.65 | MEDIUM |
| 19 | APD | Basic Materials | 305.10 | 96.46 | +0.2773 | 0.30x+0.6149+0.15x+1.0807 x0.80 | 0.181 | 5.46% | -6.88% | +2.4%/+7.4% | BULLISH/BULLISH | `BELOW_SIGNAL` | 55.8 | SELL_SETUP_1 | +6.00% | 5.46% | 323.41 | 306.09–340.72 | MEDIUM |
| 20 | ABT | Health Care | 116.64 | 96.26 | +0.2695 | 0.30x+1.1161+0.15x+0.0139 x0.80 | -0.385 | 10.78% | -7.18% | +13.2%/+37.1% | BULLISH/MIXED | `ABOVE_SIGNAL` | 77.9 | SELL_SETUP_9 | +6.00% | 10.78% | 123.64 | 110.56–136.71 | MEDIUM |
| 21 | MPC | Energy | 360.72 | 96.06 | +0.2639 | 0.30x+1.1046+0.15x-0.0097 x0.80 | -0.157 | 11.04% | -9.09% | +17.0%/+46.4% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 72.2 | SELL_SETUP_9 | +6.00% | 11.04% | 382.36 | 340.94–423.78 | MEDIUM |
| 22 | VLO | Energy | 348.86 | 95.87 | +0.2629 | 0.30x+0.9999+0.15x+0.1911 x0.80 | -0.185 | 10.03% | -9.62% | +15.8%/+45.7% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 70.7 | SELL_SETUP_1 | +6.00% | 10.03% | 369.79 | 333.40–406.18 | MEDIUM |
| 23 | PSX | Energy | 242.87 | 95.67 | +0.2606 | 0.30x+1.1361+0.15x-0.1009 x0.80 | -0.379 | 9.44% | -10.04% | +18.1%/+39.8% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 77.4 | SELL_SETUP_9 | +6.00% | 9.44% | 257.44 | 233.60–281.28 | MEDIUM |
| 24 | PFE | Health Care | 28.07 | 95.47 | +0.2572 | 0.30x+0.7343+0.15x+0.6744 x0.80 | -0.005 | 5.87% | -9.69% | +14.4%/+9.0% | BULLISH/BULLISH | `ABOVE_SIGNAL` | 71.8 | SELL_SETUP_5 | +6.00% | 5.87% | 29.75 | 28.04–31.47 | MEDIUM |

## No-trade rationale

| # | Ground | Evidence |
|---|---|---|
| 1 | Evidence threshold 2 | only 2 of 4 factor families are available (Fund_Z / Sent_Z UNAVAILABLE universe-wide) |
| 2 | Evidence threshold 3 | Technical carries 66.7% of live conviction, above the 50% cap |
| 3 | Evidence threshold 4 | data completeness 80% < 85% |
| 4 | Stop criteria NO_TRADE #6 | beta band structurally infeasible — max attainable sleeve beta 0.4841 < the 0.90 floor under the 5% single-name cap |
| 5 | Stop criteria NO_TRADE #6 | sector concentration — Health Care 45.0% on the naive top-20 EW sleeve, above the 30% cap |

Grounds 1–3 are the standing coverage failure. Grounds 4–5 are **new this run** and are the more
interesting result: even if the fundamental and sentiment families were live tomorrow, this
particular pool could not be assembled into a compliant portfolio. Every name in it is defensive, and
no reweighting of defensives reaches a 0.90 market beta.

Both were recomputed this run rather than inherited — the four runs between 2026-07-29 and 2026-08-03
were all beta-**feasible**, so the 2026-07-27 infeasibility narrative would have been wrong for each
of them.

## Portfolio analytics

No portfolio was constructed; construction terminated at the Task-0 feasibility pre-check without
spending the revision budget. Diagnostics for the hypothetical naive top-20 equal-weight sleeve
(**not proposed, not sized, not executable**):

| Metric | Value | Cap | Result |
|---|---|---|---|
| Max attainable sleeve beta | 0.4841 | 0.90–1.10 | **FAIL** |
| Max sector weight (Health Care) | 45.0% | 30% | **FAIL** |
| Average pairwise correlation | 0.1045 | < 0.45 | PASS |
| 95th-pctl 1-month drawdown | 7.32% | ≤ 8% | PASS |
| Portfolio sigma (1m) | 4.44% | — | — |
| Tracking error (1m) | 4.04% | — | — |
| Information Ratio | 1.2582 | — | diagnostic only — built on a mu prior the settled record says is too aggressive |

## Calibration state

| Record type | raw n | eff_n | Hit rate | CI coverage | Mean z | Track A gate |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 1,153 | 2 | 39.38% | 71.47% | -0.5506 | **blocked** — INSUFFICIENT_EFFECTIVE_N |
| `MARKET_FORECAST` | 174 | 2 | 35.71% | 90.23% | -0.2952 | **blocked** — INSUFFICIENT_EFFECTIVE_N |

`eff_n` reaching **2** is the first movement since the measure was introduced on 2026-07-24, and it
validates the 2026-07-28 falsifiable projection that `EQ eff_n` would increment on 2026-08-05. The
`>= 3` Track A gate now projects to **2026-09-03** for
`EQUITY_ALPHA` and **2026-09-07** for `MARKET_FORECAST`.

## Assumptions and limitations

1. **Data mode `DELAYED`.** No real-time feed is wired. Every price was fetched this run; the
   2026-08-21 Friday close is final at every vendor and is the single basis for indicators, entry
   prices, and settlements.
2. **A Saturday run adds no new market information.** It shares the Friday close exactly. Its value
   is the settlement and calibration layer, not a fresh read of the tape.
3. **Two of four factor families are dark.** `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide.
   They are shown as `UNAVAILABLE` and contribute `0.00` to the arithmetic — a penalty through the
   0.80 data-quality multiplier, never a neutral pass.
4. **Rank-order inversion is unresolved.** Mean vintage rank IC is -0.0840 across
   60 vintages, so all confidence is capped `MEDIUM`. A mu shrink cannot fix a rank
   inversion (it is a monotonic transform); that proposal was retired on 2026-07-26.
5. **Normality is assumed** for VaR95, CVaR95, and the 95th-percentile drawdown estimate.
6. **`EQR`, `AVB`, and `EA` were excluded on corporate actions** and no exchange ratio is asserted for
   any of them. Two OPEN `EQR` predictions come due within two days and currently have no settleable
   price — see `13`.
7. **Constituent caches are 62 days stale.** Used as-is per
   `rules.md`; this is the mechanism that left three dead constituents in the union.

## Next scheduled review

Next daily run per `runbook.md § Cadence`. The nearest dated commitments this package creates:

| Date | Event |
|---|---|
| 2026-08-23 | `claude-opus-5-2026-07-26` EQR prediction comes due — unsettleable under the current spec |
| 2026-08-24 | `gpt-5-2026-07-27` EQR prediction comes due — same |
| 2026-09-03 | `EQUITY_ALPHA` eff_n projected to reach 3 (24 pending) — Track A calibration proposals become eligible |
| 2026-09-07 | `MARKET_FORECAST` eff_n projected to reach 3 (3 pending) |
| 2026-09-19 | target date for all 24 equity forecasts and 3 market forecasts published today |
