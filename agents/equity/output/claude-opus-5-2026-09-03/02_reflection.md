# 02 — MoM Reflection · 2026-09-03

Standalone reflection. Every price, return and regime claim below cites a `01_preflight.md` ledger
row or is marked `UNAVAILABLE`. Reflection completes **before** any scoring in this run.

## 0. Prediction Settlement

Settlement is computed from the canonical normalizer
(`settlement_ledger.py`, L014), never re-derived by hand from raw `15_predictions.json` files.

| Quantity | Value | Ledger |
|---|---|---|
| Due inventory at run start | 113 | L014 |
| Settled this run | 111 (96 EQUITY_ALPHA + 15 MARKET_FORECAST) | L014d |
| Left due (not settled) | 2 `UNSETTLEABLE_CORPORATE_ACTION` | L025a |
| Conflicts | 0 | L014e |
| Rejected candidate rows (unchanged) | 87 | L014e |
| Packages scanned | 83 | L014 |

Settlement conventions used, per `rules.md § Settlement Rules`:

| Convention | Rows | Meaning |
|---|---|---|
| `ORDINARY` | 57 | target_date is a completed past session -> settled at that session's own close |
| `TARGET_DATE_CLOSE` | 27 | target_date == run date and this run fired post-close -> settled at today's own completed close, with a timezone-aware settled_at at or after 16:00 ET |
| `WEEKEND_TARGET` | 27 | target_date is not a trading session -> settled at the last completed close at or before it (2026-08-29 Saturday -> 2026-08-28 close) |

### Rolling Calibration Metrics

Reported separately for each record type, exactly as `rules.md § Rolling Calibration Metrics`
requires. Both blocks come from the **post-write** manifest (L014e).

| Metric | EQUITY_ALPHA | MARKET_FORECAST | Healthy range | Verdict |
|---|---|---|---|---|
| Raw n | 1451 | 216 | n >= 10 to report | both reportable |
| 28-day eff_n | **3** | 2 | eff_n >= 3 for Track A | EQ **clears** the gate for the first time; MF does not |
| Hit rate | 38.11% | 43.75% | > 50% | below target for both |
| CI coverage | 71.74% | 91.20% | 55% - 85% | EQ in band; MF above band (intervals uninformatively wide) |
| Mean z | -0.5517 | -0.1868 | -0.5 to +0.5 | EQ marginally outside; MF inside |
| Track A calibration gate | True | False | n >= 20 AND eff_n >= 3 | **EQ eligible — first time in the series** |

**`eff_n` moved to 3 for `EQUITY_ALPHA`, exactly on the date the 2026-07-28 projection
named.** That projection was recorded as falsifiable: `eff_n_increments_on` = **2026-09-03** with 24
pending predictions (pre-write manifest, L014a). Settling this run's 96 equity keys —
24 of them with `target_date == 2026-09-03` —
opened the third non-overlapping 28-day window
(2026-07-08, 2026-08-05, 2026-09-03). The projection is confirmed, not
falsified, and **Track A calibration proposals for `EQUITY_ALPHA` are unblocked for the first time
in the series**. `MARKET_FORECAST` remains at eff_n 2; its own projection still reads
2026-09-07 with
3 pending.

Rank IC across 73 scored vintages: mean **-0.0659**, median
-0.0462, 54.79% at or below zero
(L014c). Aggregate rank IC is negative, so `rules.md § Rolling Calibration Metrics` binds: **all
confidence is capped at `MEDIUM`** this run.

### This run's own settlement cohort

| Statistic | Value | vs pooled history |
|---|---|---|
| EQUITY_ALPHA settled | 96 | pooled n 1451 |
| Hit rate | 46.88% | pooled 38.11% |
| CI coverage | 69.79% | pooled 71.74% |
| Mean realized alpha | +0.30% | n/a |
| Mean z | -0.4998 | pooled -0.5517 |

Per-vintage rank IC on this run's own cohort:

| Vintage | n | Rank IC |
|---|---|---|
| claude-opus-5:2026-08-01 | 24 | +0.2000 |
| claude-opus-5:2026-08-03 | 24 | -0.2400 |
| claude-opus-5:2026-08-04 | 24 | -0.0348 |
| claude-opus-5:2026-08-06 | 24 | +0.2739 |

### Settled predictions

### `claude-opus-5-2026-08-01` -> target 2026-08-29 · `WEEKEND_TARGET` · 27 rows (10/24 HIT, 19/24 IN_CI)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| ABT | claude-opus-5-2026-08-01 | 105.70 | 2026-08-29 | +6.00% | +6.40% | +2.99% | +3.42% | HIT | IN_CI | +0.0351 |
| AMP | claude-opus-5-2026-08-01 | 545.84 | 2026-08-29 | +6.00% | +2.47% | +2.99% | -0.52% | MISS | IN_CI | -0.4530 |
| BAX | claude-opus-5-2026-08-01 | 26.16 | 2026-08-29 | +6.00% | -0.11% | +2.99% | -3.10% | MISS | IN_CI | -0.4605 |
| BBY | claude-opus-5-2026-08-01 | 86.26 | 2026-08-29 | +6.00% | -4.43% | +2.99% | -7.42% | MISS | OUT_CI_LOW | -1.2399 |
| BEN | claude-opus-5-2026-08-01 | 33.86 | 2026-08-29 | +6.00% | +2.33% | +2.99% | -0.65% | MISS | IN_CI | -0.4902 |
| BMY | claude-opus-5-2026-08-01 | 65.31 | 2026-08-29 | +6.00% | +1.94% | +2.99% | -1.04% | MISS | IN_CI | -0.4501 |
| DXCM | claude-opus-5-2026-08-01 | 83.45 | 2026-08-29 | +6.00% | +8.83% | +2.99% | +5.84% | HIT | IN_CI | +0.1888 |
| F | claude-opus-5-2026-08-01 | 14.68 | 2026-08-29 | +6.00% | -5.45% | +2.99% | -8.44% | MISS | OUT_CI_LOW | -1.5291 |
| FTNT | claude-opus-5-2026-08-01 | 161.95 | 2026-08-29 | +6.00% | +2.50% | +2.99% | -0.49% | MISS | IN_CI | -0.3271 |
| GM | claude-opus-5-2026-08-01 | 88.86 | 2026-08-29 | +6.00% | -2.91% | +2.99% | -5.90% | MISS | IN_CI | -0.9805 |
| GRMN | claude-opus-5-2026-08-01 | 293.78 | 2026-08-29 | +6.00% | -2.92% | +2.99% | -5.91% | MISS | IN_CI | -0.5912 |
| HPQ | claude-opus-5-2026-08-01 | 27.27 | 2026-08-29 | +6.00% | +11.92% | +2.99% | +8.93% | HIT | IN_CI | +0.5076 |
| IQV | claude-opus-5-2026-08-01 | 235.02 | 2026-08-29 | +6.00% | +11.37% | +2.99% | +8.39% | HIT | IN_CI | +0.3467 |
| LH | claude-opus-5-2026-08-01 | 309.20 | 2026-08-29 | +6.00% | +8.38% | +2.99% | +5.39% | HIT | IN_CI | +0.2960 |
| MA | claude-opus-5-2026-08-01 | 573.10 | 2026-08-29 | +6.00% | +3.87% | +2.99% | +0.89% | HIT | IN_CI | -0.3100 |
| MMM | claude-opus-5-2026-08-01 | 176.28 | 2026-08-29 | +6.00% | -1.10% | +2.99% | -4.09% | MISS | IN_CI | -0.7953 |
| MSFT | claude-opus-5-2026-08-01 | 464.72 | 2026-08-29 | +6.00% | +10.50% | +2.99% | +7.52% | HIT | IN_CI | +0.2870 |
| NTAP | claude-opus-5-2026-08-01 | 178.53 | 2026-08-29 | +6.00% | +4.76% | +2.99% | +1.77% | HIT | IN_CI | -0.1019 |
| PCAR | claude-opus-5-2026-08-01 | 132.68 | 2026-08-29 | +6.00% | -5.53% | +2.99% | -8.52% | MISS | OUT_CI_LOW | -1.2949 |
| PFG | claude-opus-5-2026-08-01 | 113.73 | 2026-08-29 | +6.00% | -2.04% | +2.99% | -5.03% | MISS | OUT_CI_LOW | -1.1205 |
| PRU | claude-opus-5-2026-08-01 | 122.08 | 2026-08-29 | +6.00% | -1.88% | +2.99% | -4.86% | MISS | OUT_CI_LOW | -1.3156 |
| REGN | claude-opus-5-2026-08-01 | 762.63 | 2026-08-29 | +6.00% | +4.14% | +2.99% | +1.15% | HIT | IN_CI | -0.1992 |
| STT | claude-opus-5-2026-08-01 | 184.16 | 2026-08-29 | +6.00% | +4.98% | +2.99% | +1.99% | HIT | IN_CI | -0.1296 |
| WTW | claude-opus-5-2026-08-01 | 335.92 | 2026-08-29 | +6.00% | +2.33% | +2.99% | -0.66% | MISS | IN_CI | -0.3631 |
| QQQ | claude-opus-5-2026-08-01 | 687.99 | 2026-08-29 | +1.94% | +4.13% | N/A | N/A | HIT | IN_CI | +0.2993 |
| SOXX | claude-opus-5-2026-08-01 | 504.89 | 2026-08-29 | +5.84% | +0.74% | N/A | N/A | HIT | IN_CI | -0.2610 |
| SPY | claude-opus-5-2026-08-01 | 747.03 | 2026-08-29 | +2.00% | +2.99% | N/A | N/A | HIT | IN_CI | +0.2688 |
### `claude-opus-5-2026-08-03` -> target 2026-08-31 · `ORDINARY` · 27 rows (14/24 HIT, 16/24 IN_CI)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| ARES | claude-opus-5-2026-08-03 | 138.57 | 2026-08-31 | +6.00% | +3.32% | +1.24% | +2.08% | HIT | IN_CI | -0.1991 |
| BAX | claude-opus-5-2026-08-03 | 28.10 | 2026-08-31 | +6.00% | -7.47% | +1.24% | -8.71% | MISS | IN_CI | -0.9468 |
| BBY | claude-opus-5-2026-08-03 | 85.25 | 2026-08-31 | +6.00% | -5.98% | +1.24% | -7.22% | MISS | OUT_CI_LOW | -1.4723 |
| BEN | claude-opus-5-2026-08-03 | 35.24 | 2026-08-31 | +6.00% | -3.09% | +1.24% | -4.33% | MISS | OUT_CI_LOW | -1.1194 |
| BMY | claude-opus-5-2026-08-03 | 65.47 | 2026-08-31 | +6.00% | +2.05% | +1.24% | +0.81% | HIT | IN_CI | -0.4562 |
| BX | claude-opus-5-2026-08-03 | 134.68 | 2026-08-31 | +6.00% | +6.36% | +1.24% | +5.12% | HIT | IN_CI | +0.0320 |
| COF | claude-opus-5-2026-08-03 | 217.68 | 2026-08-31 | +6.00% | -1.46% | +1.24% | -2.69% | MISS | IN_CI | -0.8322 |
| COO | claude-opus-5-2026-08-03 | 74.23 | 2026-08-31 | +6.00% | -5.58% | +1.24% | -6.82% | MISS | OUT_CI_LOW | -1.3228 |
| DXCM | claude-opus-5-2026-08-03 | 87.31 | 2026-08-31 | +6.00% | +4.29% | +1.24% | +3.06% | HIT | IN_CI | -0.1112 |
| FTNT | claude-opus-5-2026-08-03 | 163.21 | 2026-08-31 | +6.00% | +4.73% | +1.24% | +3.49% | HIT | IN_CI | -0.1187 |
| GRMN | claude-opus-5-2026-08-03 | 304.76 | 2026-08-31 | +6.00% | -6.78% | +1.24% | -8.01% | MISS | IN_CI | -0.8360 |
| HIG | claude-opus-5-2026-08-03 | 142.90 | 2026-08-31 | +6.00% | -3.86% | +1.24% | -5.10% | MISS | OUT_CI_LOW | -1.5165 |
| IQV | claude-opus-5-2026-08-03 | 233.36 | 2026-08-31 | +6.00% | +11.93% | +1.24% | +10.69% | HIT | IN_CI | +0.3849 |
| KKR | claude-opus-5-2026-08-03 | 106.56 | 2026-08-31 | +6.00% | +2.97% | +1.24% | +1.73% | HIT | IN_CI | -0.2913 |
| LH | claude-opus-5-2026-08-03 | 307.42 | 2026-08-31 | +6.00% | +8.21% | +1.24% | +6.97% | HIT | IN_CI | +0.2792 |
| MSFT | claude-opus-5-2026-08-03 | 487.65 | 2026-08-31 | +6.00% | +4.03% | +1.24% | +2.79% | HIT | IN_CI | -0.1229 |
| NTAP | claude-opus-5-2026-08-03 | 182.92 | 2026-08-31 | +6.00% | +1.30% | +1.24% | +0.06% | HIT | IN_CI | -0.3893 |
| PCAR | claude-opus-5-2026-08-03 | 132.06 | 2026-08-31 | +6.00% | -6.00% | +1.24% | -7.24% | MISS | OUT_CI_LOW | -1.3492 |
| REGN | claude-opus-5-2026-08-03 | 759.24 | 2026-08-31 | +6.00% | +5.25% | +1.24% | +4.01% | HIT | IN_CI | -0.0801 |
| ROST | claude-opus-5-2026-08-03 | 252.91 | 2026-08-31 | +6.00% | -9.64% | +1.24% | -10.87% | MISS | OUT_CI_LOW | -1.7683 |
| TGT | claude-opus-5-2026-08-03 | 149.35 | 2026-08-31 | +6.00% | +7.72% | +1.24% | +6.48% | HIT | IN_CI | +0.1715 |
| VEEV | claude-opus-5-2026-08-03 | 206.25 | 2026-08-31 | +6.00% | +38.52% | +1.24% | +37.28% | HIT | OUT_CI_HIGH | +2.5479 |
| WTW | claude-opus-5-2026-08-03 | 341.63 | 2026-08-31 | +6.00% | -0.90% | +1.24% | -2.14% | MISS | IN_CI | -0.7009 |
| ZBRA | claude-opus-5-2026-08-03 | 291.64 | 2026-08-31 | +6.00% | +21.23% | +1.24% | +19.99% | HIT | OUT_CI_HIGH | +1.3611 |
| QQQ | claude-opus-5-2026-08-03 | 700.07 | 2026-08-31 | +1.91% | +2.38% | N/A | N/A | HIT | IN_CI | +0.0657 |
| SOXX | claude-opus-5-2026-08-03 | 507.68 | 2026-08-31 | +5.56% | +0.66% | N/A | N/A | HIT | IN_CI | -0.2634 |
| SPY | claude-opus-5-2026-08-03 | 757.67 | 2026-08-31 | +2.00% | +1.24% | N/A | N/A | HIT | IN_CI | -0.2026 |
### `claude-opus-5-2026-08-04` -> target 2026-09-01 · `ORDINARY` · 27 rows (9/24 HIT, 14/24 IN_CI)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| ARES | claude-opus-5-2026-08-04 | 138.57 | 2026-09-01 | +6.00% | +0.38% | +0.54% | -0.17% | MISS | IN_CI | -0.4179 |
| BAX | claude-opus-5-2026-08-04 | 28.10 | 2026-09-01 | +6.00% | -9.32% | +0.54% | -9.87% | MISS | OUT_CI_LOW | -1.0768 |
| BBY | claude-opus-5-2026-08-04 | 85.25 | 2026-09-01 | +6.00% | -3.07% | +0.54% | -3.62% | MISS | OUT_CI_LOW | -1.1148 |
| BEN | claude-opus-5-2026-08-04 | 35.24 | 2026-09-01 | +6.00% | -6.07% | +0.54% | -6.62% | MISS | OUT_CI_LOW | -1.4861 |
| BMY | claude-opus-5-2026-08-04 | 65.47 | 2026-09-01 | +6.00% | +2.21% | +0.54% | +1.67% | HIT | IN_CI | -0.4368 |
| COF | claude-opus-5-2026-08-04 | 217.68 | 2026-09-01 | +6.00% | -2.91% | +0.54% | -3.45% | MISS | IN_CI | -0.9948 |
| COO | claude-opus-5-2026-08-04 | 74.23 | 2026-09-01 | +6.00% | -6.67% | +0.54% | -7.21% | MISS | OUT_CI_LOW | -1.4475 |
| DXCM | claude-opus-5-2026-08-04 | 87.31 | 2026-09-01 | +6.00% | +3.24% | +0.54% | +2.70% | HIT | IN_CI | -0.1799 |
| FTNT | claude-opus-5-2026-08-04 | 163.21 | 2026-09-01 | +6.00% | -0.83% | +0.54% | -1.38% | MISS | IN_CI | -0.6386 |
| GRMN | claude-opus-5-2026-08-04 | 304.76 | 2026-09-01 | +6.00% | -9.71% | +0.54% | -10.25% | MISS | IN_CI | -1.0280 |
| HIG | claude-opus-5-2026-08-04 | 142.90 | 2026-09-01 | +6.00% | -4.04% | +0.54% | -4.58% | MISS | OUT_CI_LOW | -1.5434 |
| IQV | claude-opus-5-2026-08-04 | 233.36 | 2026-09-01 | +6.00% | +10.71% | +0.54% | +10.17% | HIT | IN_CI | +0.3059 |
| KKR | claude-opus-5-2026-08-04 | 106.56 | 2026-09-01 | +6.00% | -0.14% | +0.54% | -0.68% | MISS | IN_CI | -0.5896 |
| LH | claude-opus-5-2026-08-04 | 307.42 | 2026-09-01 | +6.00% | +6.57% | +0.54% | +6.03% | HIT | IN_CI | +0.0717 |
| MSFT | claude-opus-5-2026-08-04 | 487.65 | 2026-09-01 | +6.00% | +2.74% | +0.54% | +2.20% | HIT | IN_CI | -0.2030 |
| NTAP | claude-opus-5-2026-08-04 | 182.92 | 2026-09-01 | +6.00% | +0.13% | +0.54% | -0.41% | MISS | IN_CI | -0.4856 |
| PCAR | claude-opus-5-2026-08-04 | 132.06 | 2026-09-01 | +6.00% | -7.28% | +0.54% | -7.82% | MISS | OUT_CI_LOW | -1.4921 |
| REGN | claude-opus-5-2026-08-04 | 759.24 | 2026-09-01 | +6.00% | +8.51% | +0.54% | +7.96% | HIT | IN_CI | +0.2667 |
| ROST | claude-opus-5-2026-08-04 | 252.91 | 2026-09-01 | +6.00% | -9.36% | +0.54% | -9.90% | MISS | OUT_CI_LOW | -1.7370 |
| TGT | claude-opus-5-2026-08-04 | 149.35 | 2026-09-01 | +6.00% | +9.64% | +0.54% | +9.10% | HIT | IN_CI | +0.3631 |
| VEEV | claude-opus-5-2026-08-04 | 206.25 | 2026-09-01 | +6.00% | +35.38% | +0.54% | +34.84% | HIT | OUT_CI_HIGH | +2.3025 |
| WSM | claude-opus-5-2026-08-04 | 239.80 | 2026-09-01 | +6.00% | -7.37% | +0.54% | -7.92% | MISS | OUT_CI_LOW | -1.4536 |
| WTW | claude-opus-5-2026-08-04 | 341.63 | 2026-09-01 | +6.00% | -2.10% | +0.54% | -2.64% | MISS | IN_CI | -0.8222 |
| ZBRA | claude-opus-5-2026-08-04 | 291.64 | 2026-09-01 | +6.00% | +17.85% | +0.54% | +17.31% | HIT | OUT_CI_HIGH | +1.0592 |
| QQQ | claude-opus-5-2026-08-04 | 700.07 | 2026-09-01 | +3.41% | +1.08% | N/A | N/A | HIT | IN_CI | -0.3247 |
| SOXX | claude-opus-5-2026-08-04 | 507.68 | 2026-09-01 | +7.06% | -1.45% | N/A | N/A | MISS | IN_CI | -0.4577 |
| SPY | claude-opus-5-2026-08-04 | 757.67 | 2026-09-01 | +2.00% | +0.54% | N/A | N/A | HIT | IN_CI | -0.3875 |
### `claude-opus-5-2026-08-06` -> target 2026-09-03 · `TARGET_DATE_CLOSE` · 27 rows (12/24 HIT, 18/24 IN_CI)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| AIZ | claude-opus-5-2026-08-06 | 301.57 | 2026-09-03 | +6.00% | -4.60% | +0.44% | -5.04% | MISS | OUT_CI_LOW | -1.4650 |
| AMGN | claude-opus-5-2026-08-06 | 407.83 | 2026-09-03 | +6.00% | +8.90% | +0.44% | +8.46% | HIT | IN_CI | +0.3608 |
| BAX | claude-opus-5-2026-08-06 | 27.33 | 2026-09-03 | +6.00% | -6.44% | +0.44% | -6.88% | MISS | IN_CI | -0.8509 |
| BEN | claude-opus-5-2026-08-06 | 34.92 | 2026-09-03 | +6.00% | -3.92% | +0.44% | -4.36% | MISS | OUT_CI_LOW | -1.2090 |
| CDW | claude-opus-5-2026-08-06 | 140.10 | 2026-09-03 | +6.00% | +9.86% | +0.44% | +9.43% | HIT | IN_CI | +0.2682 |
| CPAY | claude-opus-5-2026-08-06 | 394.53 | 2026-09-03 | +6.00% | +6.37% | +0.44% | +5.94% | HIT | IN_CI | +0.0416 |
| CRL | claude-opus-5-2026-08-06 | 260.72 | 2026-09-03 | +6.00% | +12.52% | +0.44% | +12.08% | HIT | IN_CI | +0.4267 |
| DXCM | claude-opus-5-2026-08-06 | 82.66 | 2026-09-03 | +6.00% | +8.53% | +0.44% | +8.09% | HIT | IN_CI | +0.1642 |
| EMR | claude-opus-5-2026-08-06 | 162.47 | 2026-09-03 | +6.00% | -7.55% | +0.44% | -7.99% | MISS | OUT_CI_LOW | -1.5456 |
| EXPE | claude-opus-5-2026-08-06 | 319.66 | 2026-09-03 | +6.00% | -5.17% | +0.44% | -5.61% | MISS | IN_CI | -0.8143 |
| GM | claude-opus-5-2026-08-06 | 89.16 | 2026-09-03 | +6.00% | -2.18% | +0.44% | -2.61% | MISS | IN_CI | -0.9120 |
| GRMN | claude-opus-5-2026-08-06 | 302.55 | 2026-09-03 | +6.00% | -8.39% | +0.44% | -8.82% | MISS | IN_CI | -0.9339 |
| HSIC | claude-opus-5-2026-08-06 | 89.59 | 2026-09-03 | +6.00% | +1.42% | +0.44% | +0.98% | HIT | IN_CI | -0.6870 |
| IVZ | claude-opus-5-2026-08-06 | 32.01 | 2026-09-03 | +6.00% | +2.19% | +0.44% | +1.75% | HIT | IN_CI | -0.3302 |
| J | claude-opus-5-2026-08-06 | 144.67 | 2026-09-03 | +6.00% | +1.98% | +0.44% | +1.54% | HIT | IN_CI | -0.5067 |
| JCI | claude-opus-5-2026-08-06 | 153.65 | 2026-09-03 | +6.00% | -7.43% | +0.44% | -7.87% | MISS | OUT_CI_LOW | -1.5112 |
| JPM | claude-opus-5-2026-08-06 | 359.24 | 2026-09-03 | +6.00% | +0.78% | +0.44% | +0.35% | HIT | IN_CI | -0.8726 |
| MELI | claude-opus-5-2026-08-06 | 1922.57 | 2026-09-03 | +6.00% | +3.56% | +0.44% | +3.12% | HIT | IN_CI | -0.3373 |
| MTD | claude-opus-5-2026-08-06 | 1421.52 | 2026-09-03 | +6.00% | -4.59% | +0.44% | -5.03% | MISS | OUT_CI_LOW | -1.2332 |
| NTAP | claude-opus-5-2026-08-06 | 186.60 | 2026-09-03 | +6.00% | -0.65% | +0.44% | -1.09% | MISS | IN_CI | -0.5299 |
| NUE | claude-opus-5-2026-08-06 | 274.74 | 2026-09-03 | +6.00% | -4.47% | +0.44% | -4.91% | MISS | IN_CI | -0.9268 |
| PRU | claude-opus-5-2026-08-06 | 120.16 | 2026-09-03 | +6.00% | +2.53% | +0.44% | +2.09% | HIT | IN_CI | -0.5405 |
| SHOP | claude-opus-5-2026-08-06 | 144.24 | 2026-09-03 | +6.00% | +1.14% | +0.44% | +0.70% | HIT | IN_CI | -0.2264 |
| WSM | claude-opus-5-2026-08-06 | 248.24 | 2026-09-03 | +6.00% | -10.26% | +0.44% | -10.70% | MISS | OUT_CI_LOW | -1.6856 |
| QQQ | claude-opus-5-2026-08-06 | 717.30 | 2026-09-03 | +3.42% | +0.05% | N/A | N/A | HIT | IN_CI | -0.4625 |
| SOXX | claude-opus-5-2026-08-06 | 530.70 | 2026-09-03 | +7.00% | -5.37% | N/A | N/A | MISS | IN_CI | -0.6697 |
| SPY | claude-opus-5-2026-08-06 | 769.79 | 2026-09-03 | +2.00% | +0.44% | N/A | N/A | HIT | IN_CI | -0.4114 |
### `gpt-5-2026-08-03` -> target 2026-08-31 · `ORDINARY` · 3 rows

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | gpt-5-2026-08-03 | 700.07 | 2026-08-31 | +1.91% | +2.38% | N/A | N/A | HIT | IN_CI | +0.0646 |
| SOXX | gpt-5-2026-08-03 | 507.68 | 2026-08-31 | +5.56% | +0.66% | N/A | N/A | HIT | IN_CI | -0.2589 |
| SPY | gpt-5-2026-08-03 | 757.67 | 2026-08-31 | +2.00% | +1.24% | N/A | N/A | HIT | IN_CI | -0.1992 |

### Left due — corporate action

| Ticker | Vintage | Target Date | Type | Reason | Detail |
|---|---|---|---|---|---|
| EQR | claude-opus-5-2026-07-26 | 2026-08-23 | EQUITY_ALPHA | UNSETTLEABLE_CORPORATE_ACTION | no fetchable price history (dead/renamed ticker) |
| EQR | gpt-5-2026-07-27 | 2026-08-24 | EQUITY_ALPHA | UNSETTLEABLE_CORPORATE_ACTION | no fetchable price history (dead/renamed ticker) |

No exchange ratio was inferred and nothing was settled against a successor symbol; that is the
explicit non-goal of the 2026-08-22 Track B (L025a). A key left due for `UNSETTLEABLE_VENDOR_BAR_LAG`
is **not** a corporate action — its security trades normally and the key settles on the next run
that has the basis bar; it is reported separately (L025b) so the two causes are never conflated in
the due inventory.

## 1. Prior Run Summary

Baseline `claude-opus-5-2026-08-06` selected by `agents.md § Orchestrator Step 2`: MoM window
2026-07-20 .. 2026-08-13, target 2026-08-06, chosen folder at delta
**0d**, flag `OK` (L015).

**No tie.** `claude-opus-5-2026-08-06` is the unique folder at delta 0d from the 2026-08-06 target, so rule 8's tie-break did not need to fire. Every in-window candidate and its distance from target is listed for audit.

| Folder | Model | Date | Delta (days) | Age (days) | Has 15_predictions.json | Records | Selected |
|---|---|---|---|---|---|---|---|
| claude-fable-5-2026-07-20 | claude-fable-5 | 2026-07-20 | 17 | 45 | yes | 36 | no |
| gpt-5-2026-07-20 | gpt-5 | 2026-07-20 | 17 | 45 | yes | 26 | no |
| claude-fable-5-2026-07-21 | claude-fable-5 | 2026-07-21 | 16 | 44 | yes | 23 | no |
| gpt-5-2026-07-21 | gpt-5 | 2026-07-21 | 16 | 44 | yes | 26 | no |
| claude-sonnet-5-2026-07-22 | claude-sonnet-5 | 2026-07-22 | 15 | 43 | yes | 29 | no |
| gpt-5-2026-07-22 | gpt-5 | 2026-07-22 | 15 | 43 | yes | 29 | no |
| claude-opus-5-2026-07-24 | claude-opus-5 | 2026-07-24 | 13 | 41 | yes | 29 | no |
| gpt-5-2026-07-24 | gpt-5 | 2026-07-24 | 13 | 41 | yes | 29 | no |
| claude-opus-5-2026-07-26 | claude-opus-5 | 2026-07-26 | 11 | 39 | yes | 27 | no |
| claude-opus-5-2026-07-27 | claude-opus-5 | 2026-07-27 | 10 | 38 | yes | 27 | no |
| gpt-5-2026-07-27 | gpt-5 | 2026-07-27 | 10 | 38 | yes | 27 | no |
| claude-opus-5-2026-07-28 | claude-opus-5 | 2026-07-28 | 9 | 37 | yes | 27 | no |
| gpt-5-2026-07-28 | gpt-5 | 2026-07-28 | 9 | 37 | yes | 23 | no |
| claude-opus-5-2026-07-29 | claude-opus-5 | 2026-07-29 | 8 | 36 | yes | 27 | no |
| gpt-5-2026-07-29 | gpt-5 | 2026-07-29 | 8 | 36 | yes | 23 | no |
| claude-opus-5-2026-07-30 | claude-opus-5 | 2026-07-30 | 7 | 35 | yes | 27 | no |
| gpt-5-2026-07-30 | gpt-5 | 2026-07-30 | 7 | 35 | yes | 23 | no |
| claude-opus-5-2026-08-01 | claude-opus-5 | 2026-08-01 | 5 | 33 | yes | 27 | no |
| claude-opus-5-2026-08-03 | claude-opus-5 | 2026-08-03 | 3 | 31 | yes | 27 | no |
| gpt-5-2026-08-03 | gpt-5 | 2026-08-03 | 3 | 31 | yes | 3 | no |
| claude-opus-5-2026-08-04 | claude-opus-5 | 2026-08-04 | 2 | 30 | yes | 27 | no |
| claude-opus-5-2026-08-06 | claude-opus-5 | 2026-08-06 | 0 | 28 | yes | 27 | **yes** |
| claude-opus-5-2026-08-07 | claude-opus-5 | 2026-08-07 | 1 | 27 | yes | 27 | no |
| claude-opus-5-2026-08-10 | claude-opus-5 | 2026-08-10 | 4 | 24 | no | 0 | no |
| gpt-5.6-sol-2026-08-10 | gpt-5.6-sol | 2026-08-10 | 4 | 24 | yes | 23 | no |

| Field | Baseline value |
|---|---|
| Date / model | claude-opus-5 · 2026-08-06 |
| Final status | `NO_TRADE` |
| Regime | `UNAVAILABLE` |
| Ranked book | 24 EQUITY_ALPHA + 3 MARKET_FORECAST records, investable set empty |
| Top-5 by prior Adj Score | AIZ +0.3793, AMGN +0.3724, CRL +0.3623, JCI +0.3178, EXPE +0.3149 |

The baseline's own predictions matured **on this run date**, so its whole book settles here as the
`TARGET_DATE_CLOSE` cohort above — the MoM table and the settlement table describe the same
observations from two angles, and they agree by construction.

## 2. MoM Price & Return Table

Hit/Miss is alpha-based per `rules.md § Settlement Rules`. Prior prices are the baseline package's
own recorded `entry_price`; current prices are this run's grounded basis-date closes (L2xx, L002).

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| AIZ | 2026-08-05 | 301.57 | 2026-09-03 | 287.71 | -4.60% | +0.44% | -5.04% | MISS | OUT_CI_LOW; z -1.47 |
| AMGN | 2026-08-05 | 407.83 | 2026-09-03 | 444.12 | +8.90% | +0.44% | +8.46% | HIT | IN_CI; z +0.36 |
| CRL | 2026-08-05 | 260.72 | 2026-09-03 | 293.35 | +12.52% | +0.44% | +12.08% | HIT | IN_CI; z +0.43 |
| JCI | 2026-08-05 | 153.65 | 2026-09-03 | 142.23 | -7.43% | +0.44% | -7.87% | MISS | OUT_CI_LOW; z -1.51 |
| EXPE | 2026-08-05 | 319.66 | 2026-09-03 | 303.14 | -5.17% | +0.44% | -5.61% | MISS | IN_CI; z -0.81 |
| CPAY | 2026-08-05 | 394.53 | 2026-09-03 | 419.68 | +6.37% | +0.44% | +5.94% | HIT | IN_CI; z +0.04 |
| NTAP | 2026-08-05 | 186.60 | 2026-09-03 | 185.38 | -0.65% | +0.44% | -1.09% | MISS | IN_CI; z -0.53 |
| HSIC | 2026-08-05 | 89.59 | 2026-09-03 | 90.86 | +1.42% | +0.44% | +0.98% | HIT | IN_CI; z -0.69 |
| DXCM | 2026-08-05 | 82.66 | 2026-09-03 | 89.71 | +8.53% | +0.44% | +8.09% | HIT | IN_CI; z +0.16 |
| IVZ | 2026-08-05 | 32.01 | 2026-09-03 | 32.71 | +2.19% | +0.44% | +1.75% | HIT | IN_CI; z -0.33 |
| J | 2026-08-05 | 144.67 | 2026-09-03 | 147.54 | +1.98% | +0.44% | +1.54% | HIT | IN_CI; z -0.51 |
| NUE | 2026-08-05 | 274.74 | 2026-09-03 | 262.47 | -4.47% | +0.44% | -4.91% | MISS | IN_CI; z -0.93 |
| CDW | 2026-08-05 | 140.10 | 2026-09-03 | 153.92 | +9.86% | +0.44% | +9.43% | HIT | IN_CI; z +0.27 |
| BAX | 2026-08-05 | 27.33 | 2026-09-03 | 25.57 | -6.44% | +0.44% | -6.88% | MISS | IN_CI; z -0.85 |
| PRU | 2026-08-05 | 120.16 | 2026-09-03 | 123.20 | +2.53% | +0.44% | +2.09% | HIT | IN_CI; z -0.54 |
| EMR | 2026-08-05 | 162.47 | 2026-09-03 | 150.21 | -7.55% | +0.44% | -7.99% | MISS | OUT_CI_LOW; z -1.55 |
| WSM | 2026-08-05 | 248.24 | 2026-09-03 | 222.76 | -10.26% | +0.44% | -10.70% | MISS | OUT_CI_LOW; z -1.69 |
| JPM | 2026-08-05 | 359.24 | 2026-09-03 | 362.06 | +0.78% | +0.44% | +0.35% | HIT | IN_CI; z -0.87 |
| GM | 2026-08-05 | 89.16 | 2026-09-03 | 87.22 | -2.18% | +0.44% | -2.61% | MISS | IN_CI; z -0.91 |
| SHOP | 2026-08-05 | 144.24 | 2026-09-03 | 145.88 | +1.14% | +0.44% | +0.70% | HIT | IN_CI; z -0.23 |
| MTD | 2026-08-05 | 1421.52 | 2026-09-03 | 1356.23 | -4.59% | +0.44% | -5.03% | MISS | OUT_CI_LOW; z -1.23 |
| MELI | 2026-08-05 | 1922.57 | 2026-09-03 | 1991.06 | +3.56% | +0.44% | +3.12% | HIT | IN_CI; z -0.34 |
| GRMN | 2026-08-05 | 302.55 | 2026-09-03 | 277.18 | -8.39% | +0.44% | -8.82% | MISS | IN_CI; z -0.93 |
| BEN | 2026-08-05 | 34.92 | 2026-09-03 | 33.55 | -3.92% | +0.44% | -4.36% | MISS | OUT_CI_LOW; z -1.21 |

Book result: **12 of 24 HIT** (50.00%),
18/24 `IN_CI`, mean alpha
-0.68%, mean z
-0.6607. Vintage rank IC **+0.2739** —
positive, meaning the baseline's own score ordering was informative about realized alpha over this
window, which the pooled cross-vintage mean (-0.0659) is not.

## 3. Theme-Level Performance

| Theme (baseline) | Evidence | Verdict |
|---|---|---|
| Defensive / low-beta quality tilt | the baseline book's mean realized alpha was -0.68% over a window in which SPY returned +0.44% | **partial** — the book neither systematically beat nor trailed the tape |
| Trend-persistence ranking (Tech_Z carries 66.7% of live weight) | vintage rank IC +0.2739 on the baseline book vs a cross-vintage mean of -0.0659 | **partial** — informative this window, not across the series |
| CI width calibration | 18/24 in the 70% band on the baseline book; pooled EQ coverage 71.74% | **validated** — coverage sits inside the 55-85% healthy range |

## 4. Regime Shift Assessment

| Dimension | Baseline (2026-08-06) | This run (2026-09-03) | Implication |
|---|---|---|---|
| Declared regime | `UNAVAILABLE` | `BULL` | regime call moved |
| VIX | see baseline `03` | 14.32 (L007) | low-vol tape; supports the BULL prior |
| SPY vs MA20 / MA50 | see baseline `03` | above both (L003, `03`) | trend intact |
| Factor-weight implication | Technical + Macro only | Technical + Macro only | no weight change is available while Fund_Z/Sent_Z are UNAVAILABLE (L021, L022) |

## 5. Carry-Forward Decisions

Binding on factor scoring when ledger-backed. `DROP` names stay out of today's scored set absent
new ledger evidence. Current rank/percentile are this run's computed values, not asserted.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Current Rank / Pctl | Decision | Rationale |
|---|---|---|---|---|---|---|
| AIZ | +0.3793 | Rank #1 of 511 on Tech/Macro evidence only (pctl 100.00); monitoring sleeve — Fund_Z/Sent_ | -4.60% | 209 / 58.97 | **DROP** | fell below the 60th-pctl rank floor (58.97) |
| AMGN | +0.3724 | Rank #2 of 511 on Tech/Macro evidence only (pctl 99.80); monitoring sleeve — Fund_Z/Sent_Z | +8.90% | 35 / 93.29 | **CARRY** | still at the 93.29th pctl (investable floor 80) |
| CRL | +0.3623 | Rank #3 of 511 on Tech/Macro evidence only (pctl 99.61); monitoring sleeve — Fund_Z/Sent_Z | +12.52% | 47 / 90.93 | **CARRY** | still at the 90.93th pctl (investable floor 80) |
| JCI | +0.3178 | Rank #4 of 511 on Tech/Macro evidence only (pctl 99.41); monitoring sleeve — Fund_Z/Sent_Z | -7.43% | 327 / 35.70 | **DROP** | fell below the 60th-pctl rank floor (35.70) |
| EXPE | +0.3149 | Rank #5 of 511 on Tech/Macro evidence only (pctl 99.22); monitoring sleeve — Fund_Z/Sent_Z | -5.17% | 191 / 62.52 | **DOWNGRADE** | fell to the 62.52th pctl - monitoring band only |
| CPAY | +0.3135 | Rank #6 of 511 on Tech/Macro evidence only (pctl 99.02); monitoring sleeve — Fund_Z/Sent_Z | +6.37% | 49 / 90.53 | **CARRY** | still at the 90.53th pctl (investable floor 80) |
| NTAP | +0.3079 | Rank #7 of 511 on Tech/Macro evidence only (pctl 98.82); monitoring sleeve — Fund_Z/Sent_Z | -0.65% | 60 / 88.36 | **CARRY** | still at the 88.36th pctl (investable floor 80) |
| HSIC | +0.3022 | Rank #8 of 511 on Tech/Macro evidence only (pctl 98.63); monitoring sleeve — Fund_Z/Sent_Z | +1.42% | 55 / 89.35 | **CARRY** | still at the 89.35th pctl (investable floor 80) |
| DXCM | +0.3010 | Rank #9 of 511 on Tech/Macro evidence only (pctl 98.43); monitoring sleeve — Fund_Z/Sent_Z | +8.53% | 112 / 78.11 | **DOWNGRADE** | fell to the 78.11th pctl - monitoring band only |
| IVZ | +0.2911 | Rank #10 of 511 on Tech/Macro evidence only (pctl 98.24); monitoring sleeve — Fund_Z/Sent_ | +2.19% | 68 / 86.79 | **CARRY** | still at the 86.79th pctl (investable floor 80) |
| J | +0.2904 | Rank #11 of 511 on Tech/Macro evidence only (pctl 98.04); monitoring sleeve — Fund_Z/Sent_ | +1.98% | 223 / 56.21 | **DROP** | fell below the 60th-pctl rank floor (56.21) |
| NUE | +0.2897 | Rank #12 of 511 on Tech/Macro evidence only (pctl 97.84); monitoring sleeve — Fund_Z/Sent_ | -4.47% | 262 / 48.52 | **DROP** | fell below the 60th-pctl rank floor (48.52) |
| CDW | +0.2893 | Rank #13 of 511 on Tech/Macro evidence only (pctl 97.65); monitoring sleeve — Fund_Z/Sent_ | +9.86% | 82 / 84.02 | **CARRY** | still at the 84.02th pctl (investable floor 80) |
| BAX | +0.2874 | Rank #14 of 511 on Tech/Macro evidence only (pctl 97.45); monitoring sleeve — Fund_Z/Sent_ | -6.44% | 140 / 72.58 | **DOWNGRADE** | fell to the 72.58th pctl - monitoring band only |
| PRU | +0.2747 | Rank #15 of 511 on Tech/Macro evidence only (pctl 97.25); monitoring sleeve — Fund_Z/Sent_ | +2.53% | 23 / 95.66 | **CARRY** | still at the 95.66th pctl (investable floor 80) |
| EMR | +0.2715 | Rank #16 of 511 on Tech/Macro evidence only (pctl 97.06); monitoring sleeve — Fund_Z/Sent_ | -7.55% | 296 / 41.81 | **DROP** | fell below the 60th-pctl rank floor (41.81) |
| WSM | +0.2710 | Rank #17 of 511 on Tech/Macro evidence only (pctl 96.86); monitoring sleeve — Fund_Z/Sent_ | -10.26% | 302 / 40.63 | **DROP** | fell below the 60th-pctl rank floor (40.63) |
| JPM | +0.2692 | Rank #18 of 511 on Tech/Macro evidence only (pctl 96.67); monitoring sleeve — Fund_Z/Sent_ | +0.78% | 32 / 93.89 | **CARRY** | still at the 93.89th pctl (investable floor 80) |
| GM | +0.2656 | Rank #19 of 511 on Tech/Macro evidence only (pctl 96.47); monitoring sleeve — Fund_Z/Sent_ | -2.18% | 129 / 74.75 | **DOWNGRADE** | fell to the 74.75th pctl - monitoring band only |
| SHOP | +0.2633 | Rank #20 of 511 on Tech/Macro evidence only (pctl 96.27); monitoring sleeve — Fund_Z/Sent_ | +1.14% | 315 / 38.07 | **DROP** | fell below the 60th-pctl rank floor (38.07) |
| MTD | +0.2605 | Rank #21 of 511 on Tech/Macro evidence only (pctl 96.08); monitoring sleeve — Fund_Z/Sent_ | -4.59% | 151 / 70.41 | **DOWNGRADE** | fell to the 70.41th pctl - monitoring band only |
| MELI | +0.2560 | Rank #22 of 511 on Tech/Macro evidence only (pctl 95.88); monitoring sleeve — Fund_Z/Sent_ | +3.56% | 102 / 80.08 | **CARRY** | still at the 80.08th pctl (investable floor 80) |
| GRMN | +0.2543 | Rank #23 of 511 on Tech/Macro evidence only (pctl 95.69); monitoring sleeve — Fund_Z/Sent_ | -8.39% | 364 / 28.40 | **DROP** | fell below the 60th-pctl rank floor (28.40) |
| BEN | +0.2519 | Rank #24 of 511 on Tech/Macro evidence only (pctl 95.49); monitoring sleeve — Fund_Z/Sent_ | -3.92% | 126 / 75.35 | **DOWNGRADE** | fell to the 75.35th pctl - monitoring band only |

Summary: **10 CARRY · 6 DOWNGRADE · 8 DROP**.
A `DOWNGRADE` here means the name fell out of the >= 80th-percentile investable band into the
60-80 monitoring band; a `DROP` means it fell below the 60th-percentile rank floor or left the
scored set entirely.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `DELAYED` — basis-date closes fetched this run (L002, L2xx) |
| Reflection confidence | **HIGH** |
| Rationale | 111 of 113 due keys settled with 0 conflicts against a canonical normalizer; the MoM baseline's book is the same cohort settled here, so the two views cross-check each other |
| Structural issue 1 | `eff_n` reached 3 for EQUITY_ALPHA on the exact date the 2026-07-28 projection named — the startup-transient diagnosis is confirmed and Track A is unblocked |
| Structural issue 2 | aggregate rank IC remains negative across vintages; confidence stays capped at MEDIUM |
| Structural issue 3 | 2 prediction key(s) can never settle because their ticker no longer trades (L025a) — dead tickers permanently subtract from the evidence base |
