# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-27
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

This Monday pre-open run covers the 515-name index union, scores 514 eligible names on the completed 2026-07-24 close, and verifies all 41 settlement/new-forecast symbols across three current-run price sources within 1% (maximum divergence 0.396451%). Thirty-four due predictions settled under `TARGET_EQ_RUN_DATE`, taking the canonical ledger to 231 equity and 42 market-forecast rows with `due_inventory: 0` and `conflicts: 0`. The two value-identical 2026-06-29 vintages both show a statistically significant **rank-order inversion** — the highest-scored names delivered the worst alpha (rank IC −0.5912, p=0.026 each). Of 514 names scored, **zero** clear the investable thresholds: `Fund_Z` and `Sent_Z` remain unavailable universe-wide, while the ranked set is separately infeasible on portfolio beta, sector concentration, and earnings concentration. **Final status is `NO_TRADE`**, with 24 `LOW`-confidence monitoring forecasts and 3 core-ETF market forecasts targeting 2026-08-24.

## MoM Reflection Summary

Baseline `gpt-5-2026-06-29` (`SAME_MODEL_BASELINE`, exact 0-day hit on the 28-day target, baseline age 28 days). A value-identical `gemini-3.5-flash-2026-06-29` vintage also matured today; the two model ledgers are not independent evidence.

Each identical book was positioned almost exactly against the rotation that followed: growth and industrials (CAT −12.27%, SHW −9.08%, GOOGL −6.59%, GE −5.50% alpha) failed, while financials, payments, and energy (CVX +12.51%, JPM +5.98%, BAC +5.84%, V +4.44%) validated. Per vintage: 42.86% hit rate on 14 equity forecasts, 64.29% CI coverage, mean z −0.028.

The decisive detail is the *ordering*: top-7 by `adj_score` averaged **−2.56%** alpha with 2 hits, bottom-7 averaged **+3.35%** with 4 hits. Carry-forward: **8 DROP, 6 DOWNGRADE, 0 CARRY, 0 PROMOTE**. Full detail in `02`.

## Regime Table

| Field | Value | Key evidence | Ledger |
|---|---|---|---|
| **Regime** | **`NEUTRAL`** | SPY 738.93 below MA20 746.15 and MA50 744.12, MACD `BELOW_SIGNAL`, but only −2.47% from its 60d high with +4.09% 60d momentum | L028, L135, L018, L025 |
| **Data quality** | `DELAYED`, DQ multiplier **0.80** | All 5 Required inputs grounded; entire Enhancing block unavailable | L146 |
| **Key macro risk** | Rotation out of growth, not index decline | QQQ −8.20% and SOXX −19.54% from 60d highs; 41.2% of the universe at negative beta; TLT −4.45% from high with RSI 33.19 | L018, L142, L029 |
| VIX | 18.58; 30d avg 17.12 vs prior-30d 17.60 | below 20 and the 30d average is falling → not `HIGH_VOL` | L005, L006 |
| Risk-free (13wk) | 3.81% p.a. | ratios are true excess-return ratios | L007 |

## Core ETF Market Forecast

Summarized from `03` — no new facts. Target date 2026-08-24.

| ETF | Entry (07-24) | mu | sigma | Target | 70% CI | Trend | RS20 vs SPY | Confidence |
|---|---|---|---|---|---|---|---|---|
| SPY | 738.93 | +0.500% | 3.96% | 742.62 | 712.21–773.04 | MIXED | +0.00pp | MEDIUM |
| QQQ | 684.23 | -0.641% | 7.96% | 679.84 | 623.22–736.47 | BEARISH | -5.12pp | MEDIUM |
| SOXX | 527.01 | +0.320% | 20.19% | 528.70 | 418.03–639.36 | BEARISH | -16.34pp | MEDIUM |

**mu derivation:** SPY takes the `NEUTRAL` regime prior of +0.5% unadjusted. QQQ and SOXX take `beta × SPY_mu` then the full permitted −1.5pp relative-view adjustment, justified by `BEARISH` MA alignment, MACD below signal, and RS20 of −5.12pp and −16.34pp against SPY.

**Disclosed structural limitation:** SOXX's beta of 3.64 forces a raw mu of +1.82%, so even the maximum allowed negative adjustment leaves **+0.320%** — a positive expected return on the most technically damaged ETF in the block. This is the `mu = beta × SPY_mu` category error diagnosed on 2026-07-24; both candidate fixes were tested and rejected then, and no further Track A change is permitted at `eff_n = 1`. Because `|mu| < 0.5%`, SOXX settles as **`N/A - FLAT_CALL`** on direction — the rule set abstains rather than recording a view it does not hold.

## Ranked Candidates — Monitoring Sleeve (24 names)

**None of these is a recommendation.** Run status is `NO_TRADE`; all 24 carry `LOW` confidence and exist to produce settleable forecasts. Score construction and full metrics are in `05`.

| Ticker | GICS Sector | Entry (07-24) | Adj Score | Compact Score Trace | Pctl | Beta | 30d RVol | TD9 D | RSI14 D | MACD D | mu | Target | 70% CI | Conf |
|---|---|---:|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|---|
| TRV | Financials | 387.26 | +0.3705 | (0.30×UNAVAILABLE + 0.30×+1.124 + 0.25×UNAVAILABLE + 0.15×+0.840)×0.80 − 0.00 | 100.0 | -0.701 | 9.33% | SELL_SETUP_6 | 80.9 | ABOVE_SIGNAL | +6% | 410.50 | 372.93–448.06 | LOW |
| RTX | Industrials | 212.79 | +0.3089 | (0.30×UNAVAILABLE + 0.30×+0.988 + 0.25×UNAVAILABLE + 0.15×+0.598)×0.80 − 0.00 | 99.8 | -0.061 | 9.75% | SELL_SETUP_3 | 74.0 | ABOVE_SIGNAL | +6% | 225.56 | 203.97–247.14 | LOW |
| PAYX | Industrials | 113.55 | +0.3072 | (0.30×UNAVAILABLE + 0.30×+0.888 + 0.25×UNAVAILABLE + 0.15×+0.783)×0.80 − 0.00 | 99.6 | -0.614 | 9.45% | BUY_SETUP_3 | 64.7 | ABOVE_SIGNAL | +6% | 120.36 | 109.21–131.52 | LOW |
| DGX | Health Care | 227.86 | +0.3058 | (0.30×UNAVAILABLE + 0.30×+0.891 + 0.25×UNAVAILABLE + 0.15×+0.766)×0.80 − 0.00 | 99.4 | -0.576 | 9.55% | SELL_SETUP_7 | 72.7 | ABOVE_SIGNAL | +6% | 241.53 | 218.89–264.17 | LOW |
| UNP | Industrials | 307.32 | +0.2992 | (0.30×UNAVAILABLE + 0.30×+0.866 + 0.25×UNAVAILABLE + 0.15×+0.762)×0.80 − 0.00 | 99.2 | -0.164 | 7.32% | SELL_SETUP_2 | 73.0 | ABOVE_SIGNAL | +6% | 325.76 | 302.38–349.14 | LOW |
| PCG | Utilities | 17.85 | +0.2807 | (0.30×UNAVAILABLE + 0.30×+0.726 + 0.25×UNAVAILABLE + 0.15×+0.888)×0.80 − 0.00 | 99.0 | -0.260 | 7.12% | SELL_SETUP_3 | 60.1 | ABOVE_SIGNAL | +6% | 18.92 | 17.60–20.24 | LOW |
| CSX | Industrials | 53.23 | +0.2777 | (0.30×UNAVAILABLE + 0.30×+0.775 + 0.25×UNAVAILABLE + 0.15×+0.764)×0.80 − 0.00 | 98.8 | +0.113 | 7.22% | SELL_SETUP_2 | 76.1 | ABOVE_SIGNAL | +6% | 56.42 | 52.43–60.42 | LOW |
| WRB | Financials | 75.46 | +0.2523 | (0.30×UNAVAILABLE + 0.30×+0.544 + 0.25×UNAVAILABLE + 0.15×+1.015)×0.80 − 0.00 | 98.6 | -0.922 | 7.27% | SELL_SETUP_5 | 67.4 | BULLISH_CROSS | +6% | 79.99 | 74.28–85.69 | LOW |
| TMO | Health Care | 568.26 | +0.2471 | (0.30×UNAVAILABLE + 0.30×+0.837 + 0.25×UNAVAILABLE + 0.15×+0.385)×0.80 − 0.00 | 98.4 | +0.098 | 10.22% | SELL_SETUP_2 | 70.8 | ABOVE_SIGNAL | +6% | 602.36 | 541.95–662.76 | LOW |
| NSC | Industrials | 350.66 | +0.2423 | (0.30×UNAVAILABLE + 0.30×+0.634 + 0.25×UNAVAILABLE + 0.15×+0.751)×0.80 − 0.00 | 98.2 | -0.100 | 7.05% | SELL_SETUP_2 | 73.2 | ABOVE_SIGNAL | +6% | 371.70 | 345.98–397.42 | LOW |
| GD | Industrials | 386.75 | +0.2366 | (0.30×UNAVAILABLE + 0.30×+1.024 + 0.25×UNAVAILABLE + 0.15×+0.757)×0.80 − 0.10 | 98.0 | -0.019 | 7.69% | SELL_SETUP_5 | 70.3 | ABOVE_SIGNAL | +6% | 409.95 | 379.02–440.89 | LOW |
| PM | Consumer Staples | 193.00 | +0.2286 | (0.30×UNAVAILABLE + 0.30×+0.649 + 0.25×UNAVAILABLE + 0.15×+0.608)×0.80 − 0.00 | 97.9 | -0.540 | 9.45% | SELL_SETUP_1 | 59.7 | ABOVE_SIGNAL | +6% | 204.58 | 185.61–223.55 | LOW |
| MPC | Energy | 309.24 | +0.2267 | (0.30×UNAVAILABLE + 0.30×+1.067 + 0.25×UNAVAILABLE + 0.15×+0.589)×0.80 − 0.10 | 97.7 | -0.439 | 9.70% | BUY_SETUP_2 | 68.2 | ABOVE_SIGNAL | +6% | 327.79 | 296.60–358.99 | LOW |
| CTAS | Industrials | 205.91 | +0.2248 | (0.30×UNAVAILABLE + 0.30×+0.656 + 0.25×UNAVAILABLE + 0.15×+0.561)×0.80 − 0.00 | 97.5 | -0.290 | 10.33% | SELL_SETUP_1 | 72.1 | ABOVE_SIGNAL | +6% | 218.26 | 196.14–240.39 | LOW |
| SJM | Consumer Staples | 118.32 | +0.2245 | (0.30×UNAVAILABLE + 0.30×+0.563 + 0.25×UNAVAILABLE + 0.15×+0.745)×0.80 − 0.00 | 97.3 | -0.756 | 9.47% | SELL_SETUP_7 | 61.2 | ABOVE_SIGNAL | +6% | 125.42 | 113.76–137.07 | LOW |
| CB | Financials | 359.75 | +0.2205 | (0.30×UNAVAILABLE + 0.30×+0.430 + 0.25×UNAVAILABLE + 0.15×+0.976)×0.80 − 0.00 | 97.1 | -0.977 | 8.21% | SELL_SETUP_2 | 60.1 | BELOW_SIGNAL | +6% | 381.33 | 350.64–412.03 | LOW |
| LMT | Industrials | 582.60 | +0.2186 | (0.30×UNAVAILABLE + 0.30×+0.776 + 0.25×UNAVAILABLE + 0.15×+0.269)×0.80 − 0.00 | 96.9 | -0.459 | 12.88% | SELL_SETUP_3 | 71.7 | ABOVE_SIGNAL | +6% | 617.56 | 539.50–695.61 | LOW |
| WAB | Industrials | 302.50 | +0.2103 | (0.30×UNAVAILABLE + 0.30×+0.848 + 0.25×UNAVAILABLE + 0.15×+0.057)×0.80 − 0.00 | 96.7 | +0.806 | 11.10% | SELL_SETUP_4 | 75.1 | ABOVE_SIGNAL | +6% | 320.65 | 285.71–355.59 | LOW |
| EQR | Real Estate | 67.86 | +0.2089 | (0.30×UNAVAILABLE + 0.30×+0.408 + 0.25×UNAVAILABLE + 0.15×+0.924)×0.80 − 0.00 | 96.5 | -0.133 | 6.06% | BUY_SETUP_3 | 49.7 | BELOW_SIGNAL | +6% | 71.93 | 67.66–76.21 | LOW |
| PKG | Materials | 254.39 | +0.2040 | (0.30×UNAVAILABLE + 0.30×+0.810 + 0.25×UNAVAILABLE + 0.15×+0.081)×0.80 − 0.00 | 96.3 | +0.811 | 9.99% | SELL_SETUP_2 | 72.2 | BULLISH_CROSS | +6% | 269.65 | 243.23–296.07 | LOW |
| BNY | Financials | 158.91 | +0.1964 | (0.30×UNAVAILABLE + 0.30×+0.521 + 0.25×UNAVAILABLE + 0.15×+0.594)×0.80 − 0.00 | 96.1 | +0.566 | 7.38% | SELL_SETUP_2 | 63.5 | ABOVE_SIGNAL | +6% | 168.44 | 156.24–180.65 | LOW |
| MET | Financials | 94.83 | +0.1955 | (0.30×UNAVAILABLE + 0.30×+0.830 + 0.25×UNAVAILABLE + 0.15×+0.801)×0.80 − 0.10 | 95.9 | -0.006 | 7.26% | SELL_SETUP_1 | 67.2 | BELOW_SIGNAL | +6% | 100.52 | 93.36–107.68 | LOW |
| VLO | Energy | 302.50 | +0.1859 | (0.30×UNAVAILABLE + 0.30×+0.946 + 0.25×UNAVAILABLE + 0.15×+0.491)×0.80 − 0.10 | 94.7 | -0.737 | 11.78% | BUY_SETUP_2 | 63.1 | ABOVE_SIGNAL | +5% | 317.62 | 280.57–354.68 | LOW |
| HIG | Financials | 140.53 | +0.1830 | (0.30×UNAVAILABLE + 0.30×+0.681 + 0.25×UNAVAILABLE + 0.15×+0.997)×0.80 − 0.10 | 94.3 | -0.575 | 6.26% | SELL_SETUP_5 | 58.2 | ABOVE_SIGNAL | +5% | 147.56 | 138.41–156.71 | LOW |

## No-Trade Rationale

Four independent failures, any one of which forces `NO_TRADE`:

| # | Failure | Evidence |
|---|---|---|
| 1 | **Evidence threshold #2** — ≥3 of 4 families non-negative | Only 2 families available. Max achievable is 2. **Structurally unreachable for all 514 names** |
| 2 | **Evidence threshold #4** — data completeness ≥85% | Actual 80% for all 514 names |
| 3 | **Portfolio beta band** 0.90–1.10 | Max attainable **−0.159** on the top-10 ranked; published set averages −0.247 beta with 19 of 24 negative |
| 4 | **Event concentration** ≤2 names with earnings inside 14d | **5** (GD 2d, VLO 3d, MPC 8d, MET 9d, HIG print-week) |

Sector concentration adds a fifth breach (Industrials 37.5% vs the 30% cap). Evidence threshold #3 fails for 22 of 24 published names (`Tech_Z` averages 69.7% of conviction against a 50% limit).

The Task-0 feasibility pre-check stopped before any sizing, so **0 of 1 revision passes** were used.

## Assumptions and Limitations

1. **`Fund_Z` and `Sent_Z` are unavailable universe-wide** (L144, L145) — the root cause of repeated recent `NO_TRADE` runs. SHADOW tooling exists but is not promoted; promotion needs ≥70% universe coverage, which needs Phase 2 of the SHADOW plan.
2. **The defensive Macro polarity is a disclosed judgment** (`INFERRED`, L140), regime-conditional and not a family-weight change. It is the single largest reason insurers, rails, defense and utilities fill the top of the book.
3. **The composite score's ordering is currently unreliable** — rank IC −0.5912 on both newly settled duplicate vintages and −0.1843 pooled across 16 vintages (n=231). No Track A correction is permissible at `eff_n = 1`, and a mu/sigma transform could not fix a rank inversion regardless.
4. **`eff_n = 1` for both record types** despite raw n of 231 and 42. All settled forecasts still fall inside a single 28-day target window. The next genuinely independent window opens around 2026-08-21.
5. **The adjusted-close return basis accepted on 2026-07-26 is carried forward** for returns, momentum, volatility, and indicators, while entry/settlement/target/CI prices remain unadjusted. Fresh histories reproduced 514/514 prior execution closes and all 517 comparable technical packs exactly.
6. **Earnings dates for 4 of 24 published names rest on a weak signature.** EQR and PKG were classified as post-print on a volume signal alone with ~0.01% price moves; WRB and CB are weaker versions of the same. Disclosed in `01`, escalated in `08` and `13`.
7. **VaR95/CVaR95 are parametric** (`mu − 1.65σ` / `mu − 2.06σ`) and assume normality — stated, not implied.
8. **FOMC calendar and index-rebalance windows are `UNAVAILABLE`** — no source wired. Recorded as a gap, not asserted either way.
9. **Bid-ask spread data is unavailable**, so the 50bps exclusion filter could not be applied. Disclosed as unapplied rather than as passed.
10. **Sigma is under-dispersed in the tails.** AAPL (z=+1.96) and CVX (z=+1.57) breached the upper CI in both duplicate equity vintages while pooled equity coverage remained healthy at 74.03%.
11. **A Monday pre-open run carries no new completed-session information** relative to the Sunday package. The material new content is settlement and calibration: 34 due records closed cleanly, while the current leaderboard and technical pack reproduce the 2026-07-24 basis.

## Next Scheduled Review

| Checkpoint | When | Owner |
|---|---|---|
| Next full pipeline run | 2026-07-28 (Tuesday) pre-open | Orchestrator |
| Next maturity | The 24 forecasts and 3 ETF forecasts published today target **2026-08-24**; a pre-open run would settle them at the completed 2026-08-21 close under `TARGET_EQ_RUN_DATE` | Reflection stage |
| Weekly parameter review | Friday 2026-07-31 after close | Evolution Agent |
| Monthly structural review | 2026-07-31 — last trading day of July | Evolution Agent |
| `eff_n ≥ 3` earliest plausible date | ~2026-09-18 on current cadence | Evolution Agent |

**Scheduler status:** no durable job is active (`runbook.md § Scheduler`); runs are manual or externally triggered until one is recreated.
