# 02 — Reflection — 2026-08-03

## 0. Prediction Settlement

Settlement ran **before** any new scoring, per `agents.md § Orchestrator Step 1`. Every prior
package (all models) was rescanned for `OPEN` predictions with `target_date <= 2026-08-03`.

| Field | Value |
|---|---|
| Due keys found | 88 |
| Settled this run | **88** — 76 `EQUITY_ALPHA`, 12 `MARKET_FORECAST` |
| Unsettleable | 0 |
| Conflicts | 0 |
| Due inventory after this run | **0** (verified by a second `settlement_ledger.py --as-of 2026-08-03` pass) |
| Vintages settled | 2026-07-05, 2026-07-06 |
| Models settled | claude-fable-5, gpt-5 |

Two timing cohorts, both resolving against a completed close:

- **`WEEKEND_TARGET`** — 49 keys with a Sunday 2026-08-02 target,
  settled at the last trading close at or before target = **2026-07-31**.
- **`TARGET_DATE_CLOSE`** — 39 keys whose `target_date` equals the run date. This fire is
  **post-close** (2026-08-03 20:08 ET), so the 2026-08-03 close exists and the same-day settlement is valid with the
  explicit flag plus a timezone-aware `settled_at` at/after 16:00 America/New_York, per
  `rules.md § Settlement Rules`. `TARGET_EQ_RUN_DATE` does **not** apply — that exception is for
  pre-open and intraday fires.

### Settled predictions

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z | Timing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 2026-07-05 | 261.07 | 2026-08-02 | +3.00% | -3.88% | +0.30% | -4.18% | MISS | IN_CI | -0.7304 | WEEKEND_TARGET |
| ABBV | 2026-07-06 | 255.26 | 2026-08-03 | +1.00% | -3.98% | +0.93% | -4.91% | MISS | IN_CI | -0.5242 | TARGET_DATE_CLOSE |
| ABNB | 2026-07-05 | 148.93 | 2026-08-02 | +6.00% | +1.74% | +0.30% | +1.44% | HIT | IN_CI | -0.4523 | WEEKEND_TARGET |
| AIZ | 2026-07-06 | 277.93 | 2026-08-03 | +5.00% | +1.60% | +0.93% | +0.67% | HIT | IN_CI | -0.6334 | TARGET_DATE_CLOSE |
| AMAT | 2026-07-05 | 603.04 | 2026-08-02 | +6.00% | -15.81% | +0.30% | -16.12% | MISS | IN_CI | -0.8125 | WEEKEND_TARGET |
| AMCR | 2026-07-05 | 45.00 | 2026-08-02 | +6.00% | -0.27% | +0.30% | -0.57% | MISS | IN_CI | -0.7587 | WEEKEND_TARGET |
| AMD | 2026-07-05 | 517.82 | 2026-08-02 | +6.00% | -8.05% | +0.30% | -8.35% | MISS | IN_CI | -0.6009 | WEEKEND_TARGET |
| AMD | 2026-07-06 | 559.27 | 2026-08-03 | +6.00% | -13.35% | +0.88% | -14.22% | MISS | IN_CI | -0.8282 | TARGET_DATE_CLOSE |
| ARM | 2026-07-05 | 315.28 | 2026-08-02 | +6.00% | -23.98% | +0.30% | -24.28% | MISS | IN_CI | -0.8289 | WEEKEND_TARGET |
| AXON | 2026-07-06 | 616.54 | 2026-08-03 | +6.00% | -6.59% | +0.88% | -7.47% | MISS | IN_CI | -0.6103 | TARGET_DATE_CLOSE |
| BAX | 2026-07-05 | 22.65 | 2026-08-02 | +6.00% | +15.50% | +0.30% | +15.19% | HIT | IN_CI | +0.8884 | WEEKEND_TARGET |
| BEN | 2026-07-05 | 34.11 | 2026-08-02 | +5.00% | -0.73% | +0.30% | -1.03% | MISS | IN_CI | -0.6957 | WEEKEND_TARGET |
| BEN | 2026-07-06 | 34.46 | 2026-08-03 | +5.00% | +2.26% | +0.93% | +1.33% | HIT | IN_CI | -0.3387 | TARGET_DATE_CLOSE |
| BXP | 2026-07-05 | 69.32 | 2026-08-02 | +5.00% | +1.15% | +0.30% | +0.85% | HIT | IN_CI | -0.4748 | WEEKEND_TARGET |
| BXP | 2026-07-06 | 69.91 | 2026-08-03 | +5.00% | +0.72% | +0.93% | -0.22% | MISS | IN_CI | -0.5451 | TARGET_DATE_CLOSE |
| CCEP | 2026-07-05 | 106.61 | 2026-08-02 | +6.00% | +2.67% | +0.30% | +2.37% | HIT | IN_CI | -0.4430 | WEEKEND_TARGET |
| CNC | 2026-07-05 | 67.86 | 2026-08-02 | +6.00% | -8.31% | +0.30% | -8.61% | MISS | OUT_CI_LOW | -1.1588 | WEEKEND_TARGET |
| CRWD | 2026-07-05 | 193.98 | 2026-08-02 | +6.00% | -1.61% | +0.30% | -1.91% | MISS | IN_CI | -0.4667 | WEEKEND_TARGET |
| CRWD | 2026-07-06 | 201.91 | 2026-08-03 | +5.00% | +0.31% | +0.93% | -0.62% | MISS | IN_CI | -0.2965 | TARGET_DATE_CLOSE |
| CRWD | 2026-07-06 | 201.45 | 2026-08-03 | +6.00% | +0.54% | +0.88% | -0.34% | MISS | IN_CI | -0.3403 | TARGET_DATE_CLOSE |
| DAL | 2026-07-06 | 92.28 | 2026-08-03 | +6.00% | -0.75% | +0.93% | -1.68% | MISS | IN_CI | -0.6289 | TARGET_DATE_CLOSE |
| DDOG | 2026-07-05 | 260.36 | 2026-08-02 | +6.00% | +2.92% | +0.30% | +2.62% | HIT | IN_CI | -0.1672 | WEEKEND_TARGET |
| DDOG | 2026-07-06 | 258.92 | 2026-08-03 | +6.00% | +5.67% | +0.93% | +4.74% | HIT | IN_CI | -0.0183 | TARGET_DATE_CLOSE |
| DDOG | 2026-07-06 | 258.29 | 2026-08-03 | +6.00% | +5.93% | +0.88% | +5.05% | HIT | IN_CI | -0.0038 | TARGET_DATE_CLOSE |
| DELL | 2026-07-05 | 394.32 | 2026-08-02 | +6.00% | +2.80% | +0.30% | +2.50% | HIT | IN_CI | -0.0901 | WEEKEND_TARGET |
| DELL | 2026-07-06 | 410.73 | 2026-08-03 | +6.00% | +4.45% | +0.88% | +3.57% | HIT | IN_CI | -0.0436 | TARGET_DATE_CLOSE |
| DVA | 2026-07-05 | 234.91 | 2026-08-02 | +5.00% | +2.21% | +0.30% | +1.90% | HIT | IN_CI | -0.3998 | WEEKEND_TARGET |
| DVA | 2026-07-06 | 236.40 | 2026-08-03 | +5.00% | -1.15% | +0.93% | -2.08% | MISS | IN_CI | -0.8966 | TARGET_DATE_CLOSE |
| DVA | 2026-07-06 | 236.19 | 2026-08-03 | +6.00% | -1.06% | +0.88% | -1.94% | MISS | IN_CI | -1.0127 | TARGET_DATE_CLOSE |
| FFIV | 2026-07-05 | 408.14 | 2026-08-02 | +6.00% | -1.36% | +0.30% | -1.67% | MISS | IN_CI | -0.8534 | WEEKEND_TARGET |
| FFIV | 2026-07-06 | 421.26 | 2026-08-03 | +5.00% | -3.54% | +0.93% | -4.47% | MISS | IN_CI | -0.9682 | TARGET_DATE_CLOSE |
| FLEX | 2026-07-05 | 136.86 | 2026-08-02 | +6.00% | -16.89% | +0.30% | -17.19% | MISS | IN_CI | -1.0026 | WEEKEND_TARGET |
| FTNT | 2026-07-06 | 163.21 | 2026-08-03 | +5.00% | +0.00% | +0.93% | -0.93% | MISS | IN_CI | -0.3981 | TARGET_DATE_CLOSE |
| HOOD | 2026-07-05 | 112.73 | 2026-08-02 | +6.00% | -23.21% | +0.30% | -23.52% | MISS | OUT_CI_LOW | -1.2778 | WEEKEND_TARGET |
| HOOD | 2026-07-06 | 117.12 | 2026-08-03 | +6.00% | -22.87% | +0.88% | -23.75% | MISS | OUT_CI_LOW | -1.2581 | TARGET_DATE_CLOSE |
| HSIC | 2026-07-05 | 86.43 | 2026-08-02 | +6.00% | -0.79% | +0.30% | -1.09% | MISS | OUT_CI_LOW | -1.1722 | WEEKEND_TARGET |
| HUM | 2026-07-05 | 396.75 | 2026-08-02 | +5.00% | -8.29% | +0.30% | -8.59% | MISS | OUT_CI_LOW | -1.1648 | WEEKEND_TARGET |
| HUM | 2026-07-05 | 396.75 | 2026-08-02 | +6.00% | -8.29% | +0.30% | -8.59% | MISS | OUT_CI_LOW | -1.2527 | WEEKEND_TARGET |
| HUM | 2026-07-06 | 391.70 | 2026-08-03 | +5.00% | -4.39% | +0.93% | -5.32% | MISS | IN_CI | -0.8468 | TARGET_DATE_CLOSE |
| IFF | 2026-07-05 | 83.83 | 2026-08-02 | +6.00% | -5.50% | +0.30% | -5.80% | MISS | OUT_CI_LOW | -1.2692 | WEEKEND_TARGET |
| INCY | 2026-07-05 | 116.86 | 2026-08-02 | +5.00% | +2.28% | +0.30% | +1.97% | HIT | IN_CI | -0.2236 | WEEKEND_TARGET |
| INTC | 2026-07-05 | 120.35 | 2026-08-02 | +6.00% | -25.05% | +0.30% | -25.35% | MISS | OUT_CI_LOW | -1.1830 | WEEKEND_TARGET |
| INTC | 2026-07-06 | 124.15 | 2026-08-03 | +6.00% | -26.70% | +0.88% | -27.58% | MISS | OUT_CI_LOW | -1.2737 | TARGET_DATE_CLOSE |
| KLAC | 2026-07-05 | 235.55 | 2026-08-02 | +6.00% | -22.39% | +0.30% | -22.69% | MISS | IN_CI | -0.9427 | WEEKEND_TARGET |
| LIN | 2026-07-05 | 546.64 | 2026-08-02 | +4.00% | -12.49% | +0.30% | -12.79% | MISS | OUT_CI_LOW | -2.7663 | WEEKEND_TARGET |
| LIN | 2026-07-06 | 533.40 | 2026-08-03 | +3.00% | -9.93% | +0.93% | -10.86% | MISS | OUT_CI_LOW | -2.0647 | TARGET_DATE_CLOSE |
| LLY | 2026-07-05 | 1213.91 | 2026-08-02 | +4.00% | -5.36% | +0.30% | -5.66% | MISS | IN_CI | -0.9542 | WEEKEND_TARGET |
| LLY | 2026-07-06 | 1203.25 | 2026-08-03 | +3.00% | -6.81% | +0.93% | -7.74% | MISS | IN_CI | -1.0119 | TARGET_DATE_CLOSE |
| LRCX | 2026-07-05 | 351.41 | 2026-08-02 | +6.00% | -16.62% | +0.30% | -16.92% | MISS | IN_CI | -0.8434 | WEEKEND_TARGET |
| LYV | 2026-07-05 | 186.59 | 2026-08-02 | +6.00% | -6.68% | +0.30% | -6.98% | MISS | OUT_CI_LOW | -1.9655 | WEEKEND_TARGET |
| LYV | 2026-07-06 | 184.04 | 2026-08-03 | +6.00% | -1.28% | +0.93% | -2.21% | MISS | OUT_CI_LOW | -1.1178 | TARGET_DATE_CLOSE |
| MAS | 2026-07-05 | 82.77 | 2026-08-02 | +5.00% | -13.64% | +0.30% | -13.94% | MISS | OUT_CI_LOW | -2.0130 | WEEKEND_TARGET |
| MAS | 2026-07-06 | 81.12 | 2026-08-03 | +6.00% | -7.88% | +0.93% | -8.81% | MISS | OUT_CI_LOW | -1.5200 | TARGET_DATE_CLOSE |
| MNST | 2026-07-05 | 97.60 | 2026-08-02 | +5.00% | -1.25% | +0.30% | -1.55% | MISS | OUT_CI_LOW | -1.3298 | WEEKEND_TARGET |
| MNST | 2026-07-06 | 96.14 | 2026-08-03 | +5.00% | -2.69% | +0.93% | -3.63% | MISS | OUT_CI_LOW | -1.5799 | TARGET_DATE_CLOSE |
| MRNA | 2026-07-05 | 79.76 | 2026-08-02 | +5.00% | -31.27% | +0.30% | -31.57% | MISS | OUT_CI_LOW | -1.6141 | WEEKEND_TARGET |
| MRNA | 2026-07-05 | 79.76 | 2026-08-02 | +6.00% | -31.27% | +0.30% | -31.57% | MISS | OUT_CI_LOW | -1.6585 | WEEKEND_TARGET |
| MRNA | 2026-07-06 | 83.49 | 2026-08-03 | +5.00% | -33.96% | +0.93% | -34.89% | MISS | OUT_CI_LOW | -1.7675 | TARGET_DATE_CLOSE |
| MRNA | 2026-07-06 | 83.31 | 2026-08-03 | +6.00% | -33.81% | +0.88% | -34.69% | MISS | OUT_CI_LOW | -1.7776 | TARGET_DATE_CLOSE |
| MRVL | 2026-07-05 | 245.29 | 2026-08-02 | +6.00% | -23.54% | +0.30% | -23.84% | MISS | IN_CI | -0.7069 | WEEKEND_TARGET |
| MU | 2026-07-05 | 975.56 | 2026-08-02 | +6.00% | -15.64% | +0.30% | -15.94% | MISS | IN_CI | -0.5935 | WEEKEND_TARGET |
| PANW | 2026-07-05 | 348.06 | 2026-08-02 | +5.00% | -4.66% | +0.30% | -4.97% | MISS | IN_CI | -0.5991 | WEEKEND_TARGET |
| PANW | 2026-07-05 | 348.06 | 2026-08-02 | +6.00% | -4.66% | +0.30% | -4.97% | MISS | IN_CI | -0.6613 | WEEKEND_TARGET |
| PANW | 2026-07-06 | 357.79 | 2026-08-03 | +5.00% | -2.98% | +0.93% | -3.91% | MISS | IN_CI | -0.5031 | TARGET_DATE_CLOSE |
| SNDK | 2026-07-05 | 1745.00 | 2026-08-02 | +6.00% | -30.38% | +0.30% | -30.68% | MISS | IN_CI | -0.9343 | WEEKEND_TARGET |
| STX | 2026-07-05 | 820.16 | 2026-08-02 | +6.00% | +4.39% | +0.30% | +4.08% | HIT | IN_CI | -0.0662 | WEEKEND_TARGET |
| SWK | 2026-07-05 | 91.90 | 2026-08-02 | +6.00% | +2.92% | +0.30% | +2.61% | HIT | IN_CI | -0.2647 | WEEKEND_TARGET |
| SWK | 2026-07-06 | 92.33 | 2026-08-03 | +6.00% | +6.26% | +0.93% | +5.33% | HIT | IN_CI | +0.0227 | TARGET_DATE_CLOSE |
| SYY | 2026-07-06 | 83.29 | 2026-08-03 | +6.00% | +2.03% | +0.93% | +1.10% | HIT | IN_CI | -0.6846 | TARGET_DATE_CLOSE |
| TTWO | 2026-07-06 | 257.60 | 2026-08-03 | +6.00% | -4.83% | +0.93% | -5.77% | MISS | OUT_CI_LOW | -1.0457 | TARGET_DATE_CLOSE |
| TXN | 2026-07-06 | 304.29 | 2026-08-03 | +6.00% | -11.58% | +0.88% | -12.46% | MISS | IN_CI | -0.9672 | TARGET_DATE_CLOSE |
| V | 2026-07-06 | 355.98 | 2026-08-03 | +6.00% | +2.72% | +0.93% | +1.79% | HIT | IN_CI | -0.5187 | TARGET_DATE_CLOSE |
| VRTX | 2026-07-05 | 528.04 | 2026-08-02 | +5.00% | -9.65% | +0.30% | -9.95% | MISS | OUT_CI_LOW | -1.7583 | WEEKEND_TARGET |
| VRTX | 2026-07-06 | 525.91 | 2026-08-03 | +5.00% | -10.49% | +0.93% | -11.42% | MISS | OUT_CI_LOW | -1.9024 | TARGET_DATE_CLOSE |
| WDC | 2026-07-05 | 539.00 | 2026-08-02 | +6.00% | +1.08% | +0.30% | +0.78% | HIT | IN_CI | -0.1609 | WEEKEND_TARGET |
| WELL | 2026-07-05 | 236.06 | 2026-08-02 | +6.00% | -0.69% | +0.30% | -0.99% | MISS | IN_CI | -0.7380 | WEEKEND_TARGET |
| QQQ | 2026-07-05 | 712.60 | 2026-08-02 | +0.79% | -3.45% | N/A | N/A | MISS | IN_CI | -0.5010 | WEEKEND_TARGET |
| QQQ | 2026-07-05 | 712.60 | 2026-08-02 | +0.89% | -3.45% | N/A | N/A | MISS | IN_CI | -0.5132 | WEEKEND_TARGET |
| QQQ | 2026-07-06 | 724.45 | 2026-08-03 | +0.83% | -3.37% | N/A | N/A | MISS | IN_CI | -0.5036 | TARGET_DATE_CLOSE |
| QQQ | 2026-07-06 | 724.74 | 2026-08-03 | +1.23% | -3.40% | N/A | N/A | MISS | IN_CI | -0.5463 | TARGET_DATE_CLOSE |
| SOXX | 2026-07-05 | 566.32 | 2026-08-02 | +0.64% | -10.85% | N/A | N/A | MISS | IN_CI | -0.5231 | WEEKEND_TARGET |
| SOXX | 2026-07-05 | 566.32 | 2026-08-02 | +1.94% | -10.85% | N/A | N/A | MISS | IN_CI | -0.5820 | WEEKEND_TARGET |
| SOXX | 2026-07-06 | 589.15 | 2026-08-03 | +1.71% | -13.83% | N/A | N/A | MISS | IN_CI | -0.7224 | TARGET_DATE_CLOSE |
| SOXX | 2026-07-06 | 589.34 | 2026-08-03 | +2.50% | -13.86% | N/A | N/A | MISS | IN_CI | -0.7478 | TARGET_DATE_CLOSE |
| SPY | 2026-07-05 | 744.78 | 2026-08-02 | +0.50% | +0.30% | N/A | N/A | HIT | IN_CI | -0.0449 | WEEKEND_TARGET |
| SPY | 2026-07-05 | 744.78 | 2026-08-02 | +0.50% | +0.30% | N/A | N/A | HIT | IN_CI | -0.0448 | WEEKEND_TARGET |
| SPY | 2026-07-06 | 750.67 | 2026-08-03 | +0.50% | +0.93% | N/A | N/A | HIT | IN_CI | +0.1003 | TARGET_DATE_CLOSE |
| SPY | 2026-07-06 | 751.06 | 2026-08-03 | +0.50% | +0.88% | N/A | N/A | HIT | IN_CI | +0.0866 | TARGET_DATE_CLOSE |

### This batch

| Metric | EQUITY_ALPHA | MARKET_FORECAST |
|---|---|---|
| Settled | 76 | 12 |
| Direction hits | 19/76 = **25.00%** | 4/12 = 33.33% |
| IN_CI | 52/76 = 68.42% | 12/12 |
| Mean z | -0.8561 | -0.3785 |

The `MARKET_FORECAST` split is the familiar one: **SPY 4/4 hits, QQQ 0/4, SOXX 0/4** —
the direct signature of the `mu = beta x SPY_mu` category error, since a high-beta ETF cannot express
a view that differs in *direction* from SPY's.

### Rolling calibration (canonical ledger, all models, all vintages)

| Metric | EQUITY_ALPHA | MARKET_FORECAST | Healthy range |
|---|---|---|---|
| Raw n | **515** | **90** | — |
| 28-day eff_n | **1** | **1** | — |
| Hit rate | 39.81% | 22.09% | > 50% |
| CI coverage | 69.90% | 81.11% | 55% – 85% (target 70%) |
| Mean z | -0.5191 | -0.6253 | -0.5 to +0.5 |
| Rank IC (weighted mean over vintages) | -0.0879 | n/a — MF settles on raw return | > 0 |
| Track A calibration gate | **not eligible** (INSUFFICIENT_EFFECTIVE_N) | **not eligible** (INSUFFICIENT_EFFECTIVE_N) | n >= 20 AND eff_n >= 3 |

Interpretation, applied literally:

- **CI coverage 69.90% sits inside 55–85%**, so the sigma-widening rule does *not* fire and
  sigma stays `REALIZED_VOL_30D`. Magnitude calibration is not the problem.
- **Rank IC -0.0879 <= 0 over n=515 >= 20** does fire: `agents.md § Calibration Feedback Binding`
  **caps every confidence label in this package at `MEDIUM`**. Rank IC is non-positive in
  **20 of 32** vintages — a persistent rank-order inversion, not a single bad window.
- `eff_n` = 1 keeps every Track A proposal in `DEFER`, not `REJECT`. Projection holds:
  `EQUITY_ALPHA` increments on **2026-08-05**, `MARKET_FORECAST` on
  **2026-08-09**.

Ledger files scanned: every `15_predictions.json` under `agents/equity/output/` (all models, all
dates), normalized through `settlement_ledger.py` — 872 candidate rows,
180 audit-only, 87 rejected on timing.

## 1. Prior Run Summary and MoM baseline selection

MoM window **2026-06-19 .. 2026-07-13**, target **2026-07-06**. Closest folders sit at
`|delta|` = **0d**, which is a **2-way tie**, so
`agents.md § Orchestrator Step 2` **rule 8** applies.

### Rule 8 — every tied candidate disclosed (mandatory)

| Folder | Selected | Settled n | Hit rate | Mean alpha | Mean z |
|---|---|---|---|---|---|
| claude-fable-5-2026-07-06 | yes | 23 | 26.09% | -4.11% | -0.8604 |
| gpt-5-2026-07-06 | no | 10 | 20.00% | -11.38% | -0.8116 |

Resolution order: (a) same model family as `claude-opus-5` -> `claude-fable-5-2026-07-06` wins on the
`claude` prefix; (b) usable `15_predictions.json` — both qualify; (c) lexicographic — not reached.

**Is the conclusion invariant across the tied books? Yes.** The hit-rate spread is
**6.1pp** (20.00% vs 26.09%), and both books are far below the 50% healthy
floor with negative mean alpha and mean z near -0.8. Whichever baseline is selected, the MoM verdict is
the same: the prior book underperformed SPY materially. This is the fourth firing of rule 8 and the
second where the conclusion holds across candidates (spreads were 48pp on 2026-07-29, 40.7pp on
2026-07-30, 1.7pp on 2026-08-01).

Prior run: **claude-fable-5-2026-07-06**, final status **`NO_TRADE`**, 23 equity names priced
forward to today.

## 2. MoM Price and Return Table

Benchmark: SPY **751.28** (2026-07-06) -> **757.67** (2026-08-03) = **+0.8505%**.
Hit/Miss is alpha-based per `rules.md § Settlement Rules`. All prices carry ledger rows in `01`
(`L-PX-*`) or are derived from the same fetched history (`L-HIST`).

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI | Prior Thesis |
|---|---|---|---|---|---|---|---|---|---|---|
| PANW | 2026-07-06 | 357.79 | 2026-08-03 | 347.13 | -2.98% | +0.85% | -3.83% | Miss | IN_CI | Platformization-led security demand; momentum leadership re-accelerating |
| DVA | 2026-07-06 | 236.40 | 2026-08-03 | 233.68 | -1.15% | +0.85% | -2.00% | Miss | IN_CI | Dialysis oligopoly re-rating on stable volumes; defensive HC momentum leader |
| FTNT | 2026-07-06 | 163.21 | 2026-08-03 | 163.21 | +0.00% | +0.85% | -0.85% | Miss | IN_CI | Firewall refresh cycle + SASE attach; security spend resilience |
| MAS | 2026-07-06 | 81.12 | 2026-08-03 | 74.73 | -7.88% | +0.85% | -8.73% | Miss | OUT_CI_LOW | Repair/remodel recovery leverage; housing-adjacent momentum with mid beta |
| CRWD | 2026-07-06 | 201.91 | 2026-08-03 | 202.54 | +0.31% | +0.85% | -0.54% | Miss | IN_CI | Endpoint/identity consolidation winner; high-momentum security complex |
| DAL | 2026-07-06 | 92.28 | 2026-08-03 | 91.59 | -0.75% | +0.85% | -1.60% | Miss | IN_CI | Premium-cabin/loyalty mix strength into summer travel peak; earnings 3d away |
| BEN | 2026-07-06 | 34.46 | 2026-08-03 | 35.24 | +2.26% | +0.85% | +1.41% | Hit | IN_CI | Asset-manager torque to risk-on flows; valuation re-rate off multi-year base |
| V | 2026-07-06 | 355.98 | 2026-08-03 | 365.67 | +2.72% | +0.85% | +1.87% | Hit | IN_CI | Payments network volume resilience; defensive quality at negative 60d beta |
| LYV | 2026-07-06 | 184.04 | 2026-08-03 | 181.69 | -1.28% | +0.85% | -2.13% | Miss | OUT_CI_LOW | Live-events demand secular strength; concert calendar seasonality |
| DDOG | 2026-07-06 | 258.92 | 2026-08-03 | 273.60 | +5.67% | +0.85% | +4.82% | Hit | IN_CI | Observability + AI-workload monitoring attach; high-growth momentum leg |
| BXP | 2026-07-06 | 69.91 | 2026-08-03 | 70.41 | +0.72% | +0.85% | -0.14% | Miss | IN_CI | Class-A office REIT recovery on falling vacancy; rate-stability beneficiary |
| SWK | 2026-07-06 | 92.33 | 2026-08-03 | 98.11 | +6.26% | +0.85% | +5.41% | Hit | IN_CI | Tool demand inflection + cost-out program; housing-adjacent cyclical |
| MRNA | 2026-07-06 | 83.49 | 2026-08-03 | 55.14 | -33.96% | +0.85% | -34.81% | Miss | OUT_CI_LOW | Oncology/rare-disease pipeline catalysts; extreme momentum, extreme vol |
| HUM | 2026-07-06 | 391.70 | 2026-08-03 | 374.50 | -4.39% | +0.85% | -5.24% | Miss | IN_CI | Managed-care margin recovery; MA rate environment stabilizing |
| TTWO | 2026-07-06 | 257.60 | 2026-08-03 | 245.15 | -4.83% | +0.85% | -5.68% | Miss | OUT_CI_LOW | GTA VI cycle anticipation; content slate momentum |
| FFIV | 2026-07-06 | 421.26 | 2026-08-03 | 406.35 | -3.54% | +0.85% | -4.39% | Miss | IN_CI | App-delivery/security hybrid-infra demand; low-vol compounder |
| VRTX | 2026-07-06 | 525.91 | 2026-08-03 | 470.76 | -10.49% | +0.85% | -11.34% | Miss | OUT_CI_LOW | CF franchise durability + pain-pipeline optionality; defensive growth |
| MNST | 2026-07-06 | 96.14 | 2026-08-03 | 93.55 | -2.69% | +0.85% | -3.54% | Miss | OUT_CI_LOW | Energy-drink share stability; staples momentum with low beta |
| AIZ | 2026-07-06 | 277.93 | 2026-08-03 | 282.39 | +1.60% | +0.85% | +0.75% | Hit | IN_CI | Specialty insurance compounder; negative-beta defensive with steady momentum |
| SYY | 2026-07-06 | 83.29 | 2026-08-03 | 84.98 | +2.03% | +0.85% | +1.18% | Hit | IN_CI | Foodservice distribution scale winner; low-beta staples momentum |
| LLY | 2026-07-06 | 1203.25 | 2026-08-03 | 1121.36 | -6.81% | +0.85% | -7.66% | Miss | IN_CI | GLP-1 franchise; defensive growth at elevated valuation; carry-forward |
| LIN | 2026-07-06 | 533.40 | 2026-08-03 | 480.46 | -9.93% | +0.85% | -10.78% | Miss | OUT_CI_LOW | Industrial-gas compounder with pricing power; carry-forward from 06-10 book |
| ABBV | 2026-07-06 | 255.26 | 2026-08-03 | 245.10 | -3.98% | +0.85% | -4.83% | Miss | IN_CI | Skyrizi/Rinvoq momentum vs Humira erosion; carry-forward, best prior-book alpha |

**6/23 = 26.09%** alpha hits. Mean alpha **-4.03%**,
median **-2.13%**. The prior book lost to SPY on both the mean and the median,
so this is a broad shortfall rather than one or two outliers.

## 3. Theme-Level Performance

| Sector cluster | Names | Mean alpha | Verdict |
|---|---|---|---|
| Health Care | 6 | -10.98% | failed |
| Consumer Discretionary | 6 | -0.16% | partial |
| Technology | 4 | -0.10% | partial |
| Finance | 2 | +1.08% | validated |
| Industrials | 1 | -8.73% | failed |
| Real Estate | 1 | -0.14% | partial |
| Telecommunications | 1 | -4.39% | failed |
| Consumer Staples | 1 | -3.54% | failed |
| Basic Materials | 1 | -10.78% | failed |

The concentration of the damage in **Health Care** (6 names,
-10.98% mean alpha) is the same
composition effect rule 8 exists to surface: a momentum-ranked book loads on whatever led over the
prior 60 days and then carries that concentration through the reversal.

## 4. Regime Shift Assessment

| Dimension | Prior run (2026-07-06) | This run (2026-08-03) | Implication |
|---|---|---|---|
| Declared regime | `BULL` (per the baseline package) | `BULL` | unchanged label |
| SPY vs MA20 / MA50 | above / above | above / above | trend intact |
| SPY 60d momentum | — | +3.51% | supports the `BULL` prior |
| SPY 30d realized vol | — | 3.76% / month (falling) | calm tape |
| SOXX relative strength 60d | strongly negative into the settled window | -3.30pp vs SPY | semis leadership has re-asserted |
| Factor-weight implication | — | none — family weights are protected and unchanged | `rules.md § Evolution Policy` |

The regime label is stable; what changed underneath it is **leadership**, and that is precisely
what a trend-persistence score handles worst.

## 5. Carry-Forward Decisions

Every row below is re-derived from this run's `run_computed_manifest.json` — no rank or percentile
is hand-written. Decisions bind factor scoring where ledger-backed.

| Ticker | Prior Score | Prior Thesis | MoM Alpha | Decision | Rationale |
|---|---|---|---|---|---|
| PANW | +0.4210 | Platformization-led security demand; momentum leadership re- | -3.83% | DROP | fell below the 60th-pctl rank floor (pctl 47.75), so it is rejection-log only |
| DVA | +0.4190 | Dialysis oligopoly re-rating on stable volumes; defensive HC | -2.00% | CARRY | still at pctl 91.78 (rank 43) despite negative MoM alpha; the score is re-derived, not inherited |
| FTNT | +0.3420 | Firewall refresh cycle + SASE attach; security spend resilie | -0.85% | CARRY | still at pctl 98.63 (rank 8) despite negative MoM alpha; the score is re-derived, not inherited |
| MAS | +0.3420 | Repair/remodel recovery leverage; housing-adjacent momentum  | -8.73% | DROP | fell below the 60th-pctl rank floor (pctl 27.79), so it is rejection-log only |
| CRWD | +0.3310 | Endpoint/identity consolidation winner; high-momentum securi | -0.54% | DOWNGRADE | pctl 77.69 (rank 115) is below the 80th-pctl investable floor; monitoring only |
| DAL | +0.3240 | Premium-cabin/loyalty mix strength into summer travel peak;  | -1.60% | CARRY | still at pctl 82.39 (rank 91) despite negative MoM alpha; the score is re-derived, not inherited |
| BEN | +0.3180 | Asset-manager torque to risk-on flows; valuation re-rate off | +1.41% | CARRY | still at pctl 99.61 (rank 3) and the MoM alpha was positive |
| V | +0.3090 | Payments network volume resilience; defensive quality at neg | +1.87% | DROP | fell below the 60th-pctl rank floor (pctl 59.49), so it is rejection-log only |
| LYV | +0.3010 | Live-events demand secular strength; concert calendar season | -2.13% | CARRY | still at pctl 85.32 (rank 76) despite negative MoM alpha; the score is re-derived, not inherited |
| DDOG | +0.2870 | Observability + AI-workload monitoring attach; high-growth m | +4.82% | CARRY | still at pctl 90.61 (rank 49) and the MoM alpha was positive |
| BXP | +0.2860 | Class-A office REIT recovery on falling vacancy; rate-stabil | -0.14% | CARRY | still at pctl 91.59 (rank 44) despite negative MoM alpha; the score is re-derived, not inherited |
| SWK | +0.2810 | Tool demand inflection + cost-out program; housing-adjacent  | +5.41% | CARRY | still at pctl 82.97 (rank 88) and the MoM alpha was positive |
| MRNA | +0.2810 | Oncology/rare-disease pipeline catalysts; extreme momentum,  | -34.81% | DROP | fell below the 60th-pctl rank floor (pctl 20.35), so it is rejection-log only |
| HUM | +0.2770 | Managed-care margin recovery; MA rate environment stabilizin | -5.24% | CARRY | still at pctl 95.11 (rank 26) despite negative MoM alpha; the score is re-derived, not inherited |
| TTWO | +0.2740 | GTA VI cycle anticipation; content slate momentum | -5.68% | DROP | fell below the 60th-pctl rank floor (pctl 54.01), so it is rejection-log only |
| FFIV | +0.2740 | App-delivery/security hybrid-infra demand; low-vol compounde | -4.39% | DOWNGRADE | pctl 77.50 (rank 116) is below the 80th-pctl investable floor; monitoring only |
| VRTX | +0.2680 | CF franchise durability + pain-pipeline optionality; defensi | -11.34% | DROP | fell below the 60th-pctl rank floor (pctl 36.79), so it is rejection-log only |
| MNST | +0.2600 | Energy-drink share stability; staples momentum with low beta | -3.54% | DOWNGRADE | pctl 68.49 (rank 162) is below the 80th-pctl investable floor; monitoring only |
| AIZ | +0.2590 | Specialty insurance compounder; negative-beta defensive with | +0.75% | CARRY | still at pctl 89.82 (rank 53) and the MoM alpha was positive |
| SYY | +0.2520 | Foodservice distribution scale winner; low-beta staples mome | +1.18% | DOWNGRADE | pctl 79.45 (rank 106) is below the 80th-pctl investable floor; monitoring only |
| LLY | +0.1840 | GLP-1 franchise; defensive growth at elevated valuation; car | -7.66% | DROP | fell below the 60th-pctl rank floor (pctl 50.88), so it is rejection-log only |
| LIN | +0.1590 | Industrial-gas compounder with pricing power; carry-forward  | -10.78% | DROP | fell below the 60th-pctl rank floor (pctl 19.37), so it is rejection-log only |
| ABBV | +0.1370 | Skyrizi/Rinvoq momentum vs Humira erosion; carry-forward, be | -4.83% | DOWNGRADE | pctl 77.30 (rank 117) is below the 80th-pctl investable floor; monitoring only |

**10 CARRY · 5 DOWNGRADE · 8 DROP.** `DROP` names stay out of today's scored set absent new
ledger evidence; because this run re-scores the full index union from scratch, a `DOWNGRADE` simply
means the name did not clear the 80th-pctl floor on today's evidence.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` — completed 2026-08-03 close, fetched this run |
| Prices failing the Price Sourcing Standard | 0 of 27 published symbols |
| Reflection confidence | **MEDIUM** |
| Confidence rationale | Settlement and MoM arithmetic are fully grounded and reproducible (0 conflicts, 0 unsettleable, 3-source price agreement inside 0.08%), but the *interpretive* content is limited by eff_n = 1: one overlapping cohort cannot distinguish a broken score from an unlucky window. |
| Structural issues found | (1) rank-order inversion persists (rank IC -0.0879, non-positive in 20/32 vintages); (2) `MARKET_FORECAST` mu remains a category error; (3) a drawdown-polarity defect was found and fixed in this run's engine during pre-publication verification — see `13` |
