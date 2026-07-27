```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-27
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

No position is recommended. 514 S&P 500 ∪ Nasdaq-100 names were scored on the 2026-07-24 close with all
five Required inputs grounded and independently verified, and **zero cleared the investable bar** —
because two of four factor families (Fundamental, Sentiment) have no universe-scale fetch path, which
makes three of the five Evidence Thresholds unpassable by construction rather than by market
judgement. Independently, the portfolio beta band is unreachable: with
41.25% of the universe at negative 60-day beta, even the 20
highest-beta names in the entire ≥80th-percentile pool average
+0.8519 against a 0.90 floor. 24
names are published as monitoring forecasts with settleable `mu`/`sigma`, and the market-forecast
sleeve is unchanged at `NEUTRAL`.

## MoM Reflection Summary

Baseline `gpt-5-2026-06-29` (`CROSS_MODEL_BASELINE`, exact 28-day target hit; no `claude-opus-5`
folder is old enough to qualify). Its 14 equity forecasts settled today at the 2026-07-24 close:
6
HIT / 8
MISS on alpha versus SPY, which returned
+1.36% over the window.
Financials and energy validated; industrial/materials cyclicals failed outright (CAT
-12.27%,
SHW -9.08%).
Magnitude calibration is healthy (CI coverage 74.03%, mean z
-0.1792); **rank ordering is inverted** (weighted-mean rank IC
-0.1843), which caps all confidence at `MEDIUM`. This run settled nothing —
the concurrent `gpt-5-2026-07-27` pre-open run had already settled all 34 due keys,
leaving due inventory 0 and conflicts 0.
Details: `02_reflection.md`.

## Regime

| Field | Value | Ledger |
|---|---|---|
| Regime | **`NEUTRAL`** | L052 |
| Data quality | `DELAYED`, DQ 0.8 | L035 |
| SPY vs MA20 / MA50 | 738.93 vs 746.153 / 744.1202 → `MIXED` | L019, L040 |
| SPY 30d realized vol | 3.96% (RISING) | L013 |
| VIX | 18.58 (07/24/2026), 20d mean 16.83 | L008 |
| 13-week T-bill | 3.81% | L009 |
| Key macro risk | Crowded defensive rotation — 41.25% of the universe at negative beta, so the highest-scoring names have the least market exposure | L015, L049 |

## Core ETF Market Forecast

| ETF | Entry | Date | mu | sigma | Target | Target Date | 70% CI | Beta | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 738.93 | 2026-07-24 | +0.50% | 3.96% | 742.6246 | 2026-08-24 | 712.2125 – 773.0368 | 1.00 | MEDIUM |
| QQQ | 684.23 | 2026-07-24 | +0.86% | 7.96% | 690.1082 | 2026-08-24 | 633.487 – 746.7295 | 1.7182 | MEDIUM |
| SOXX | 527.01 | 2026-07-24 | +1.82% | 20.19% | 536.6005 | 2026-08-24 | 425.9389 – 647.2622 | 3.6395 | MEDIUM |

QQQ and SOXX `mu` follow the `beta × SPY_mu` rule, which is **diagnosed as defective** and applied
unmodified because only the evolution agent may change it and Track A is gated at
`eff_n = 1`. See `03` and `13`.

## Ranked Candidates — Monitoring Sleeve Only

Top 10 of 24 published. Full table with all metric columns: `05_factor_scores.md`.

| Rank | Ticker | Sector | Entry | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | IR | TD9 D | RSI14 D | MACD D | mu | Target | 70% CI | Days→Earn | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TRV | Finance | 387.26 | +0.3705 | (0.30×+1.124 + 0.15×+0.840)×0.8 − 0.00 | 100.00 | -0.701 | 9.33% | 0.609 | 0.798 | SELL_SETUP_6 | 80.9 | ABOVE_SIGNAL | +6.0% | 410.50 | 372.93–448.06 | ~81d est | MEDIUM |
| 2 | RTX | Industrials | 212.79 | +0.3089 | (0.30×+0.988 + 0.15×+0.598)×0.8 − 0.00 | 99.81 | -0.061 | 9.75% | 0.583 | 0.693 | SELL_SETUP_3 | 74.0 | ABOVE_SIGNAL | +6.0% | 225.56 | 203.97–247.14 | ~87d est | MEDIUM |
| 3 | PAYX | Industrials | 113.55 | +0.3072 | (0.30×+0.888 + 0.15×+0.783)×0.8 − 0.00 | 99.61 | -0.614 | 9.45% | 0.602 | 0.672 | BUY_SETUP_3 | 64.7 | ABOVE_SIGNAL | +6.0% | 120.36 | 109.21–131.52 | ~80d est | MEDIUM |
| 4 | DGX | Health Care | 227.86 | +0.3058 | (0.30×+0.891 + 0.15×+0.766)×0.8 − 0.00 | 99.42 | -0.576 | 9.55% | 0.595 | 0.764 | SELL_SETUP_7 | 72.7 | ABOVE_SIGNAL | +6.0% | 241.53 | 218.89–264.17 | ~87d est | MEDIUM |
| 5 | UNP | Industrials | 307.32 | +0.2992 | (0.30×+0.866 + 0.15×+0.762)×0.8 − 0.00 | 99.22 | -0.164 | 7.32% | 0.777 | 0.816 | SELL_SETUP_2 | 73.0 | ABOVE_SIGNAL | +6.0% | 325.76 | 302.38–349.14 | ~87d est | MEDIUM |
| 6 | PCG | Utilities | 17.85 | +0.2807 | (0.30×+0.726 + 0.15×+0.888)×0.8 − 0.00 | 99.03 | -0.260 | 7.12% | 0.798 | 0.803 | SELL_SETUP_3 | 60.1 | ABOVE_SIGNAL | +6.0% | 18.92 | 17.60–20.24 | ~86d est | MEDIUM |
| 7 | CSX | Industrials | 53.23 | +0.2777 | (0.30×+0.775 + 0.15×+0.764)×0.8 − 0.00 | 98.83 | +0.113 | 7.22% | 0.787 | 0.892 | SELL_SETUP_2 | 76.1 | ABOVE_SIGNAL | +6.0% | 56.42 | 52.43–60.42 | ~87d est | MEDIUM |
| 8 | TMO | Industrials | 568.26 | +0.2471 | (0.30×+0.837 + 0.15×+0.385)×0.8 − 0.00 | 98.64 | +0.098 | 10.22% | 0.556 | 0.587 | SELL_SETUP_2 | 70.8 | ABOVE_SIGNAL | +6.0% | 602.36 | 541.95–662.76 | ~87d est | MEDIUM |
| 9 | NSC | Industrials | 350.66 | +0.2423 | (0.30×+0.634 + 0.15×+0.751)×0.8 − 0.00 | 98.44 | -0.100 | 7.05% | 0.806 | 0.852 | SELL_SETUP_2 | 73.2 | ABOVE_SIGNAL | +6.0% | 371.70 | 345.98–397.42 | ~87d est | MEDIUM |
| 10 | WELL | Real Estate | 252.07 | +0.2406 | (0.30×+0.814 + 0.15×+0.794)×0.8 − 0.05 | 98.25 | -0.573 | 6.82% | 0.833 | 0.802 | SELL_SETUP_9 | 74.1 | ABOVE_SIGNAL | +6.0% | 267.19 | 249.30–285.08 | ~80d est | MEDIUM |

`Fund_Z` and `Sent_Z` are `UNAVAILABLE` for every name (L046, L047), which is why each trace shows
only the Technical and Macro terms. Their absence *lowers* data quality and fails the family-count
threshold; it is never treated as neutral.

## No-Trade Rationale

| Gate | Requirement | Actual | Verdict |
|---|---|---|---|
| Evidence Threshold #1 | pctl ≥ 80 | 103 names clear | passes for those names |
| Evidence Threshold #2 | ≥3 of 4 families non-negative | max achievable **2** | **fails universe-wide** |
| Evidence Threshold #3 | no family > 50% of conviction | Technical = 66.7% | **fails universe-wide** |
| Evidence Threshold #4 | data completeness ≥ 85% | 80% | **fails universe-wide** |
| Portfolio beta band | 0.90 – 1.10 | max attainable +0.8519 | **fails** (`NO_TRADE` #6) |
| Avg pairwise correlation | < 0.45 | 0.2784 | passes |
| 95th-pctl 1-month drawdown | ≤ 8% | 7.77% | passes |
| Sector concentration | ≤ 30% | Industrials 60% of top 10 | **fails** |

Correlation and drawdown pass comfortably. The sleeve is disqualified for being **too defensive and
too concentrated in Industrials**, not for being too risky — a mandate-fit failure, not a
risk-control one.

## Assumptions and Limitations

1. **Price basis is the 2026-07-24 close, not live.** The 2026-07-27 session was in progress during execution;
   the live tape is recorded in `10_midday_monitor.md` as observation only and is used in no forecast.
2. **This run shares its market-data layer** with `claude-opus-5-2026-07-26` and
   `gpt-5-2026-07-27` (same Friday close). What is new: an independent recomputation that reproduces
   the 07-26 numbers exactly, an earnings layer three days closer, refreshed calibration state, and
   the first live look at the 2026-07-27 tape.
3. **Two of four factor families are absent.** Every score rests on Technical and Macro only.
4. **`eff_n = 1`.** The 231 settled equity predictions are one overlapping cohort,
   so raw `n ≥ 20` is numerically satisfied and statistically vacuous. No Track A change is licensed.
5. **Normality is assumed** for VaR95, CVaR95 and the 95th-percentile drawdown estimate.
6. **Bid-ask, IV, short interest, revisions and ownership flow are `UNAVAILABLE`**, so the 50bp spread
   exclusion filter could not be enforced and `Sent_Z` could not be built.
7. **Bulk history has no redundancy right now** — Yahoo 429-blocked, Nasdaq bulk-historical serving a
   challenge page; stockanalysis.com was the only bulk source, with CNBC and IBKR as verification.
8. **The ETF `mu` rule is knowingly defective** and applied unmodified pending Track A eligibility.

## Next Scheduled Review

| Checkpoint | Time (ET) | Artifact |
|---|---|---|
| Midday monitor | 12:15 2026-07-27 | `10_midday_monitor.md` — early-session observation already written at ~10:10 |
| Pre-close check | 15:45 2026-07-27 | `11_preclose_check.md` (stub) |
| Close log | 16:20 2026-07-27 | `12_close_log.md` (stub) |
| Next full run | 07:27 2026-07-28 | new dated package |
| Forecast settlement | 2026-08-24 | all 24 equity + 3 ETF records in this run's `15_predictions.json` |
