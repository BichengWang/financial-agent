# 09 — Final Report — 2026-07-30

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-30
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

No portfolio is recommended: zero of 513 scored names clear the Evidence Thresholds,
because `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide and no name can satisfy the
3-of-4-family or 85%-completeness bars. All five Required inputs are grounded, so this is a
quality verdict, not a data failure — and, unlike 2026-07-27, **not** a portfolio-feasibility
verdict: the beta band was re-verified and is feasible at a maximum attainable
+1.1258. All 58 due predictions were settled at the 2026-07-29
close, taking canonical `EQUITY_ALPHA` n to 347 at a 47.8% hit rate and a
rank IC of -0.1975, which caps every confidence label in this package at `MEDIUM`. The
24 published names are settleable monitoring forecasts only.

## MoM reflection summary

The baseline is `claude-fable-5-2026-07-02` (`CROSS_MODEL_BASELINE`), chosen from a **three-way tie** at
delta 0d whose members are not interchangeable: hit rates ranged
7.1%
to 47.8%
across the tied books. The settled cohort lost heavily to a semiconductor collapse
(SOXX -17.89% over the window) that hit semis-weighted books far harder than defensive
ones. Full detail and all tied candidates: `02_reflection.md`.

## Regime

| Regime | Data quality | Key macro risk | Ledger rows |
|---|---|---|---|
| **`NEUTRAL`** | DQ 0.80 (2 of 4 families `UNAVAILABLE`) | VIX 20.66, +13.5% in one session and 20.3% above its 20d mean, while *realized* vol falls — implied and realized stress disagree | L005, L006, L015–L018 |

SPY closed -2.32% over 20 days, below both its MA20 and MA50, with a
-4.49% drawdown from the 60-day high — no trend confirmation in either direction.

## Core ETF market forecast

| ETF | Entry | Trend 20d/50d | 30d RVol | Beta | mu | sigma | Target | 70% CI | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 729.46 | BELOW/BELOW | 3.57% | 1.0000 | +0.50% | 3.57% | 733.11 | 706.02–760.20 | MEDIUM |
| QQQ | 661.73 | BELOW/BELOW | 6.96% | 1.7022 | +0.85% | 6.96% | 667.36 | 619.50–715.23 | MEDIUM |
| SOXX | 465.00 | BELOW/BELOW | 18.86% | 3.6391 | +1.82% | 18.86% | 473.46 | 382.24–564.68 | MEDIUM |

Carries a disclosed known bias (`mu = beta x SPY_mu`); see `03`.

## Ranked candidates — monitoring sleeve (24 names)

**None of these is a recommendation.** The investable sleeve is empty.

| Rank | Ticker | Sector | Entry | Adj Score | Pctl | mu | sigma | Target | 70% CI | Beta | TD9 D/W/M | RSI D/W/M | MACD D/W/M | Days to Earn | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GRMN | Industrials | 294.83 | +0.3309 | 99.81 | +6.00% | 15.47% | 312.52 | 265.10–359.94 | +0.161 | S3/S5/S1 | 80.0/71.0/68.7 | ABOVE/BULL_X/BULL_X | 38 | MEDIUM |
| 2 | BBY | Consumer Discretionary | 90.17 | +0.3256 | 99.61 | +6.00% | 8.88% | 95.58 | 87.25–103.91 | +0.750 | S4/S9/S3 | 73.6/69.4/61.8 | ABOVE/ABOVE/ABOVE | 28 | MEDIUM |
| 3 | IQV | Health Care | 247.56 | +0.3169 | 99.42 | +6.00% | 15.86% | 262.41 | 221.59–303.23 | +0.152 | S5/S6/S2 | 80.8/70.0/59.6 | ABOVE/ABOVE/BULL_X | 38 | MEDIUM |
| 4 | NTAP | Technology | 173.23 | +0.3116 | 99.22 | +6.00% | 12.82% | 183.62 | 160.53–206.72 | +1.420 | S7/S4/S4 | 60.6/71.4/69.8 | ABOVE/ABOVE/ABOVE | 27 | MEDIUM |
| 5 | BXP | Real Estate | 72.97 | +0.2946 | 99.03 | +6.00% | 8.51% | 77.35 | 70.89–83.80 | +0.347 | S4/S9/S2 | 70.3/67.9/58.2 | BULL_X/ABOVE/BULL_X | 38 | MEDIUM |
| 6 | TRV | Finance | 389.01 | +0.2926 | 98.83 | +6.00% | 9.65% | 412.35 | 373.32–451.38 | -0.590 | S9/S9/S9 | 74.7/80.0/77.4 | ABOVE/ABOVE/ABOVE | 38 | MEDIUM |
| 7 | INCY | Health Care | 127.10 | +0.2897 | 98.64 | +6.00% | 11.86% | 134.73 | 119.05–150.40 | -0.242 | S4/S9/S2 | 69.9/71.3/76.5 | ABOVE/ABOVE/ABOVE | 38 | MEDIUM |
| 8 | GEHC | Health Care | 71.90 | +0.2831 | 98.44 | +6.00% | 14.84% | 76.21 | 65.12–87.31 | -0.256 | S2/S1/S1 | 68.8/54.3/49.2 | BULL_X/BULL_X/BELOW | 38 | MEDIUM |
| 9 | FICO | Consumer Discretionary | 1373.08 | +0.2830 | 98.25 | +6.00% | 11.94% | 1455.46 | 1284.96–1625.97 | -0.094 | S3/S5/S1 | 67.9/55.6/48.6 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |
| 10 | ADP | Industrials | 273.37 | +0.2802 | 98.05 | +6.00% | 10.15% | 289.77 | 260.90–318.64 | -0.729 | S3/S6/S2 | 73.5/67.5/56.7 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |
| 11 | F | Industrials | 15.28 | +0.2777 | 97.86 | +6.00% | 7.95% | 16.20 | 14.93–17.46 | +1.730 | S4/S3/S1 | 66.3/59.5/60.0 | ABOVE/ABOVE/ABOVE | 38 | MEDIUM |
| 12 | HUM | Health Care | 365.41 | +0.2763 | 97.66 | +6.00% | 10.98% | 387.33 | 345.60–429.06 | +0.620 | B5/B1/S3 | 41.5/64.3/57.8 | BELOW/ABOVE/ABOVE | 38 | MEDIUM |
| 13 | CPAY | Consumer Discretionary | 392.85 | +0.2724 | 97.47 | +6.00% | 9.49% | 416.42 | 377.63–455.21 | +0.460 | S4/S3/S4 | 69.0/64.7/61.9 | ABOVE/ABOVE/BULL_X | 6 | LOW |
| 14 | PAYX | Industrials | 122.13 | +0.2701 | 97.27 | +6.00% | 9.89% | 129.46 | 116.90–142.01 | -0.613 | S3/S9/S2 | 76.1/71.8/55.5 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |
| 15 | FTNT | Technology | 153.22 | +0.2698 | 97.08 | +6.00% | 10.40% | 162.41 | 145.83–178.99 | +0.925 | S1/B1/S5 | 50.1/74.3/76.5 | BELOW/ABOVE/ABOVE | 38 | MEDIUM |
| 16 | SJM | Consumer Staples | 126.35 | +0.2665 | 96.88 | +6.00% | 9.92% | 133.93 | 120.89–146.97 | -0.821 | S9/S3/S1 | 70.8/69.3/60.0 | ABOVE/ABOVE/ABOVE | 27 | MEDIUM |
| 17 | MRSH | Finance | 197.59 | +0.2531 | 96.69 | +6.00% | 9.62% | 209.45 | 189.67–229.22 | -0.909 | S3/S6/S1 | 74.1/65.8/53.6 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |
| 18 | BRO | Finance | 74.87 | +0.2513 | 96.49 | +6.00% | 11.45% | 79.36 | 70.45–88.28 | -0.954 | S3/S9/S1 | 70.9/59.2/46.4 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |
| 19 | HPQ | Technology | 28.41 | +0.2492 | 96.30 | +6.00% | 11.63% | 30.11 | 26.68–33.55 | +0.620 | S4/S3/S3 | 72.8/66.3/55.9 | ABOVE/ABOVE/BULL_X | 27 | MEDIUM |
| 20 | RTX | Industrials | 215.25 | +0.2359 | 96.10 | +6.00% | 9.65% | 228.17 | 206.56–249.77 | -0.020 | S6/S9/S1 | 71.2/67.9/75.4 | ABOVE/ABOVE/ABOVE | 38 | MEDIUM |
| 21 | CTAS | Industrials | 216.53 | +0.2283 | 95.91 | +6.00% | 9.95% | 229.52 | 207.12–251.93 | -0.274 | S4/S6/S1 | 78.1/69.4/61.1 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |
| 22 | IEX | Industrials | 229.52 | +0.2231 | 95.71 | +6.00% | 5.17% | 243.29 | 230.96–255.62 | +0.529 | S4/S1/S9 | 62.9/68.8/60.8 | BULL_X/ABOVE/ABOVE | 38 | MEDIUM |
| 23 | DVA | Health Care | 240.96 | +0.2224 | 95.52 | +6.00% | 5.51% | 255.42 | 241.60–269.24 | +0.579 | S2/S8/S6 | 69.5/81.3/74.7 | BELOW/ABOVE/ABOVE | 5 | LOW |
| 24 | VRSK | Industrials | 213.15 | +0.2203 | 95.32 | +6.00% | 10.60% | 225.94 | 202.45–249.43 | -0.948 | S3/S9/S1 | 70.4/59.8/45.3 | ABOVE/ABOVE/BELOW | 38 | MEDIUM |

Score attribution for every name is in `05_factor_scores.md`; this table introduces no new
metric or fact.

## No-trade rationale

| # | Evidence Threshold | Result |
|---|---|---|
| 1 | Percentile ≥ 80th | PASS (102 names) |
| 2 | ≥3 of 4 families non-negative | **FAIL** — only 2 families exist |
| 3 | No family > 50% of conviction | **FAIL** — `Tech_Z` = 66.7% |
| 4 | Data completeness ≥ 85% | **FAIL** — DQ 0.80 |
| 5 | No hard stop | PASS |

Fewer than 5 investable names ⇒ `NO_TRADE` (`rules.md § Downgrade to NO_TRADE` #1).

## Assumptions and limitations

1. **`Fund_Z`/`Sent_Z` unavailable** is the single structural blocker to any `GO`. Until Phase 2
   of the SHADOW plan reaches 70% universe coverage, every run ends here regardless of tape.
2. **The composite score is rank-inverted** (rank IC -0.1975). Treat the ordering above as
   unreliable; `08 § 1` documents a same-session live example.
3. **Normality is assumed** for VaR95 (`mu − 1.65σ`), CVaR95 (`mu − 2.06σ`) and the parametric
   drawdown estimate.
4. **Basis is the 2026-07-29 close.** The 2026-07-30 session was open and moving sharply during the run;
   nothing intraday feeds any published number. See `10`.
5. **Constituent caches are 39 days stale**; used and logged per protocol rather than triggering a fallback.
6. **Enhancing inputs missing** (IV, short interest, bid-ask, revisions) — reflected in DQ
   0.80 and the confidence caps, never used to block `GO`.

## Next scheduled review

| Checkpoint | When |
|---|---|
| Pre-close check | 2026-07-30 15:45 ET (`11`, stubbed — run fired pre-close) |
| Close log | 2026-07-30 16:20 ET (`12`, stubbed) |
| Weekly parameter review | 2026-07-31 17:15 ET (Friday) |
| **Month-end structural review** | **2026-07-31** — last trading day of July |
| `eff_n` gate re-check | 2026-08-05 (`EQUITY_ALPHA` → 2), 2026-08-09 (`MARKET_FORECAST` → 2) |
