# 02 — Reflection

Run `2026-08-06` · baseline `claude-fable-5-2026-07-09` · flag `CROSS_MODEL_BASELINE`.

## 0. Prediction Settlement

98 of 98 due keys settled; 0
unsettled. Every settlement uses the **2026-08-05** close (ledger rows L001, L018).

Two timing cohorts, both resolving to that same close:

- **`ORDINARY`** (49 keys) — `target_date = 2026-08-05`, which is strictly before the run date, so the completed target-date close is used.
- **`TARGET_EQ_RUN_DATE`** (49 keys) — `target_date = 2026-08-06` equals the run date and the run fired **intraday**, before that session's close existed. `rules.md § Settlement Rules` settles these at the latest completed close and forbids ever using an intraday print. A post-close fire would have been able to use `TARGET_DATE_CLOSE` and settle a day "later" in basis terms.

Scanned for due predictions: every `15_predictions.json` under `agents/equity/output/`
across all models (75 packages).

### Settled predictions

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z | Timing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DVA | gpt-5-2026-07-08 | 231.43 | 2026-08-05 | +6.00% | -18.47% | +3.34% | -21.81% | MISS | OUT_CI_LOW | -3.405 | ORDINARY |
| DVA | claude-fable-5-2026-07-08 | 231.24 | 2026-08-05 | +5.00% | -18.40% | +3.42% | -21.82% | MISS | OUT_CI_LOW | -3.250 | ORDINARY |
| DVA | gpt-5-2026-07-09 | 227.30 | 2026-08-06 | +6.00% | -16.99% | +2.48% | -19.47% | MISS | OUT_CI_LOW | -3.174 | TARGET_EQ_RUN_DATE |
| DVA | claude-fable-5-2026-07-09 | 226.79 | 2026-08-06 | +6.00% | -16.80% | +2.48% | -19.28% | MISS | OUT_CI_LOW | -3.167 | TARGET_EQ_RUN_DATE |
| BAX | claude-fable-5-2026-07-08 | 22.00 | 2026-08-05 | +5.00% | +24.23% | +3.42% | +20.81% | HIT | OUT_CI_HIGH | +1.712 | ORDINARY |
| LIN | claude-fable-5-2026-07-08 | 529.94 | 2026-08-05 | +3.00% | -7.34% | +3.42% | -10.76% | MISS | OUT_CI_LOW | -1.684 | ORDINARY |
| BAX | claude-fable-5-2026-07-09 | 22.43 | 2026-08-06 | +6.00% | +21.85% | +2.48% | +19.37% | HIT | OUT_CI_HIGH | +1.428 | TARGET_EQ_RUN_DATE |
| HUM | gpt-5-2026-07-08 | 402.05 | 2026-08-05 | +6.00% | -9.51% | +3.34% | -12.85% | MISS | OUT_CI_LOW | -1.381 | ORDINARY |
| LIN | claude-fable-5-2026-07-09 | 524.22 | 2026-08-06 | +2.00% | -6.33% | +2.48% | -8.81% | MISS | OUT_CI_LOW | -1.365 | TARGET_EQ_RUN_DATE |
| MNST | claude-fable-5-2026-07-08 | 95.95 | 2026-08-05 | +5.00% | -1.55% | +3.42% | -4.97% | MISS | OUT_CI_LOW | -1.354 | ORDINARY |
| MRNA | gpt-5-2026-07-09 | 75.76 | 2026-08-06 | +6.00% | -25.75% | +2.48% | -28.23% | MISS | OUT_CI_LOW | -1.344 | TARGET_EQ_RUN_DATE |
| MRNA | gpt-5-2026-07-08 | 74.52 | 2026-08-05 | +6.00% | -24.51% | +3.34% | -27.85% | MISS | OUT_CI_LOW | -1.304 | ORDINARY |
| TTWO | claude-fable-5-2026-07-08 | 252.39 | 2026-08-05 | +6.00% | -6.93% | +3.42% | -10.34% | MISS | OUT_CI_LOW | -1.296 | ORDINARY |
| MRNA | claude-fable-5-2026-07-08 | 74.36 | 2026-08-05 | +6.00% | -24.35% | +3.42% | -27.77% | MISS | OUT_CI_LOW | -1.295 | ORDINARY |
| MNST | claude-fable-5-2026-07-09 | 95.85 | 2026-08-06 | +5.00% | -1.45% | +2.48% | -3.93% | MISS | OUT_CI_LOW | -1.290 | TARGET_EQ_RUN_DATE |
| HUM | claude-fable-5-2026-07-08 | 400.65 | 2026-08-05 | +5.00% | -9.19% | +3.42% | -12.61% | MISS | OUT_CI_LOW | -1.265 | ORDINARY |
| TROW | claude-fable-5-2026-07-09 | 118.13 | 2026-08-06 | +5.00% | -2.67% | +2.48% | -5.15% | MISS | OUT_CI_LOW | -1.198 | TARGET_EQ_RUN_DATE |
| FFIV | claude-fable-5-2026-07-09 | 429.98 | 2026-08-06 | +6.00% | -4.34% | +2.48% | -6.82% | MISS | OUT_CI_LOW | -1.188 | TARGET_EQ_RUN_DATE |
| HUM | claude-fable-5-2026-07-09 | 394.68 | 2026-08-06 | +5.00% | -7.82% | +2.48% | -10.30% | MISS | OUT_CI_LOW | -1.187 | TARGET_EQ_RUN_DATE |
| FFIV | gpt-5-2026-07-09 | 429.29 | 2026-08-06 | +6.00% | -4.19% | +2.48% | -6.67% | MISS | OUT_CI_LOW | -1.153 | TARGET_EQ_RUN_DATE |
| HOOD | gpt-5-2026-07-09 | 116.20 | 2026-08-06 | +6.00% | -20.14% | +2.48% | -22.62% | MISS | OUT_CI_LOW | -1.131 | TARGET_EQ_RUN_DATE |
| TROW | claude-fable-5-2026-07-08 | 117.59 | 2026-08-05 | +5.00% | -2.22% | +3.42% | -5.64% | MISS | OUT_CI_LOW | -1.089 | ORDINARY |
| VRTX | claude-fable-5-2026-07-08 | 506.65 | 2026-08-05 | +5.00% | -4.31% | +3.42% | -7.73% | MISS | OUT_CI_LOW | -1.041 | ORDINARY |
| TTWO | claude-fable-5-2026-07-09 | 244.45 | 2026-08-06 | +6.00% | -3.90% | +2.48% | -6.38% | MISS | IN_CI | -1.010 | TARGET_EQ_RUN_DATE |
| HOOD | gpt-5-2026-07-08 | 111.79 | 2026-08-05 | +6.00% | -16.99% | +3.34% | -20.33% | MISS | IN_CI | -0.991 | ORDINARY |
| WST | claude-fable-5-2026-07-08 | 352.52 | 2026-08-05 | +6.00% | -0.43% | +3.42% | -3.84% | MISS | IN_CI | -0.914 | ORDINARY |
| AMCR | claude-fable-5-2026-07-08 | 41.88 | 2026-08-05 | +6.00% | +14.02% | +3.42% | +10.60% | HIT | IN_CI | +0.845 | ORDINARY |
| LLY | claude-fable-5-2026-07-08 | 1,222.72 | 2026-08-05 | +4.00% | -4.32% | +3.42% | -7.74% | MISS | IN_CI | -0.834 | ORDINARY |
| LYV | claude-fable-5-2026-07-09 | 182.52 | 2026-08-06 | +6.00% | +0.55% | +2.48% | -1.93% | MISS | IN_CI | -0.826 | TARGET_EQ_RUN_DATE |
| CRL | claude-fable-5-2026-07-08 | 222.42 | 2026-08-05 | +6.00% | +17.22% | +3.42% | +13.80% | HIT | IN_CI | +0.759 | ORDINARY |
| AMD | gpt-5-2026-07-09 | 545.36 | 2026-08-06 | +6.00% | -11.61% | +2.48% | -14.09% | MISS | IN_CI | -0.758 | TARGET_EQ_RUN_DATE |
| KLAC | gpt-5-2026-07-09 | 230.69 | 2026-08-06 | +6.00% | -16.42% | +2.48% | -18.91% | MISS | IN_CI | -0.735 | TARGET_EQ_RUN_DATE |
| LYV | claude-fable-5-2026-07-08 | 181.62 | 2026-08-05 | +6.00% | +1.05% | +3.42% | -2.37% | MISS | IN_CI | -0.729 | ORDINARY |
| ARM | gpt-5-2026-07-09 | 333.17 | 2026-08-06 | +6.00% | -17.59% | +2.48% | -20.07% | MISS | IN_CI | -0.711 | TARGET_EQ_RUN_DATE |
| LRCX | gpt-5-2026-07-09 | 353.18 | 2026-08-06 | +6.00% | -12.96% | +2.48% | -15.44% | MISS | IN_CI | -0.700 | TARGET_EQ_RUN_DATE |
| SNDK | gpt-5-2026-07-08 | 1,660.05 | 2026-08-05 | +6.00% | -18.65% | +3.34% | -21.99% | MISS | IN_CI | -0.641 | ORDINARY |
| AIZ | claude-fable-5-2026-07-09 | 278.13 | 2026-08-06 | +5.00% | +8.43% | +2.48% | +5.95% | HIT | IN_CI | +0.635 | TARGET_EQ_RUN_DATE |
| LLY | claude-fable-5-2026-07-09 | 1,208.68 | 2026-08-06 | +3.00% | -3.21% | +2.48% | -5.69% | MISS | IN_CI | -0.627 | TARGET_EQ_RUN_DATE |
| ABBV | claude-fable-5-2026-07-08 | 253.71 | 2026-08-05 | +3.00% | -2.96% | +3.42% | -6.38% | MISS | IN_CI | -0.611 | ORDINARY |
| INTC | gpt-5-2026-07-09 | 112.65 | 2026-08-06 | +6.00% | -10.29% | +2.48% | -12.77% | MISS | IN_CI | -0.608 | TARGET_EQ_RUN_DATE |
| AMAT | gpt-5-2026-07-09 | 593.19 | 2026-08-06 | +6.00% | -9.94% | +2.48% | -12.42% | MISS | IN_CI | -0.580 | TARGET_EQ_RUN_DATE |
| STX | gpt-5-2026-07-09 | 908.55 | 2026-08-06 | +6.00% | -7.80% | +2.48% | -10.29% | MISS | IN_CI | -0.559 | TARGET_EQ_RUN_DATE |
| WDC | gpt-5-2026-07-09 | 586.13 | 2026-08-06 | +6.00% | -11.42% | +2.48% | -13.91% | MISS | IN_CI | -0.556 | TARGET_EQ_RUN_DATE |
| CNC | gpt-5-2026-07-08 | 67.47 | 2026-08-05 | +6.00% | -0.70% | +3.34% | -4.04% | MISS | IN_CI | -0.539 | ORDINARY |
| MU | gpt-5-2026-07-09 | 1,013.99 | 2026-08-06 | +6.00% | -11.91% | +2.48% | -14.40% | MISS | IN_CI | -0.536 | TARGET_EQ_RUN_DATE |
| HPE | gpt-5-2026-07-08 | 44.70 | 2026-08-05 | +6.00% | +19.06% | +3.34% | +15.72% | HIT | IN_CI | +0.507 | ORDINARY |
| AMD | gpt-5-2026-07-08 | 512.41 | 2026-08-05 | +6.00% | -5.93% | +3.34% | -9.26% | MISS | IN_CI | -0.503 | ORDINARY |
| CRL | claude-fable-5-2026-07-09 | 230.99 | 2026-08-06 | +6.00% | +12.87% | +2.48% | +10.39% | HIT | IN_CI | +0.484 | TARGET_EQ_RUN_DATE |
| PANW | claude-fable-5-2026-07-08 | 320.79 | 2026-08-05 | +5.00% | +13.05% | +3.42% | +9.63% | HIT | IN_CI | +0.455 | ORDINARY |
| MAS | claude-fable-5-2026-07-08 | 76.27 | 2026-08-05 | +6.00% | +1.38% | +3.42% | -2.04% | MISS | IN_CI | -0.450 | ORDINARY |
| INTC | gpt-5-2026-07-08 | 107.62 | 2026-08-05 | +6.00% | -6.10% | +3.34% | -9.43% | MISS | IN_CI | -0.449 | ORDINARY |
| ARM | gpt-5-2026-07-08 | 297.38 | 2026-08-05 | +6.00% | -7.67% | +3.34% | -11.00% | MISS | IN_CI | -0.425 | ORDINARY |
| FTNT | gpt-5-2026-07-09 | 163.38 | 2026-08-06 | +6.00% | +0.46% | +2.48% | -2.03% | MISS | IN_CI | -0.422 | TARGET_EQ_RUN_DATE |
| PANW | gpt-5-2026-07-08 | 321.02 | 2026-08-05 | +6.00% | +12.97% | +3.34% | +9.63% | HIT | IN_CI | +0.394 | ORDINARY |
| MRVL | gpt-5-2026-07-08 | 233.42 | 2026-08-05 | +6.00% | -9.60% | +3.34% | -12.94% | MISS | IN_CI | -0.370 | ORDINARY |
| NTAP | gpt-5-2026-07-08 | 164.08 | 2026-08-05 | +6.00% | +13.72% | +3.34% | +10.39% | HIT | IN_CI | +0.352 | ORDINARY |
| FTNT | claude-fable-5-2026-07-09 | 163.27 | 2026-08-06 | +5.00% | +0.53% | +2.48% | -1.95% | MISS | IN_CI | -0.347 | TARGET_EQ_RUN_DATE |
| MU | gpt-5-2026-07-08 | 937.61 | 2026-08-05 | +6.00% | -4.74% | +3.34% | -8.08% | MISS | IN_CI | -0.294 | ORDINARY |
| CRWD | gpt-5-2026-07-08 | 189.52 | 2026-08-05 | +6.00% | +10.73% | +3.34% | +7.39% | HIT | IN_CI | +0.291 | ORDINARY |
| CRWD | claude-fable-5-2026-07-08 | 189.58 | 2026-08-05 | +6.00% | +10.70% | +3.42% | +7.28% | HIT | IN_CI | +0.289 | ORDINARY |
| BEN | claude-fable-5-2026-07-09 | 33.94 | 2026-08-06 | +5.00% | +2.89% | +2.48% | +0.41% | HIT | IN_CI | -0.258 | TARGET_EQ_RUN_DATE |
| DDOG | claude-fable-5-2026-07-08 | 256.57 | 2026-08-05 | +6.00% | +10.37% | +3.42% | +6.95% | HIT | IN_CI | +0.238 | ORDINARY |
| DDOG | gpt-5-2026-07-08 | 256.84 | 2026-08-05 | +6.00% | +10.25% | +3.34% | +6.91% | HIT | IN_CI | +0.232 | ORDINARY |
| AXON | gpt-5-2026-07-08 | 602.40 | 2026-08-05 | +6.00% | +1.18% | +3.34% | -2.16% | MISS | IN_CI | -0.226 | ORDINARY |
| TECH | gpt-5-2026-07-08 | 70.55 | 2026-08-05 | +6.00% | +2.06% | +3.34% | -1.28% | MISS | IN_CI | -0.199 | ORDINARY |
| ABBV | claude-fable-5-2026-07-09 | 248.37 | 2026-08-06 | +1.00% | -0.87% | +2.48% | -3.35% | MISS | IN_CI | -0.193 | TARGET_EQ_RUN_DATE |
| AXON | claude-fable-5-2026-07-08 | 601.93 | 2026-08-05 | +5.00% | +1.26% | +3.42% | -2.16% | MISS | IN_CI | -0.175 | ORDINARY |
| PRU | claude-fable-5-2026-07-09 | 115.71 | 2026-08-06 | +5.00% | +3.85% | +2.48% | +1.37% | HIT | IN_CI | -0.172 | TARGET_EQ_RUN_DATE |
| STT | claude-fable-5-2026-07-08 | 176.06 | 2026-08-05 | +5.00% | +6.24% | +3.42% | +2.82% | HIT | IN_CI | +0.164 | ORDINARY |
| PANW | claude-fable-5-2026-07-09 | 336.45 | 2026-08-06 | +5.00% | +7.79% | +2.48% | +5.31% | HIT | IN_CI | +0.159 | TARGET_EQ_RUN_DATE |
| DELL | claude-fable-5-2026-07-09 | 457.08 | 2026-08-06 | +6.00% | +1.23% | +2.48% | -1.25% | MISS | IN_CI | -0.146 | TARGET_EQ_RUN_DATE |
| DELL | gpt-5-2026-07-09 | 456.69 | 2026-08-06 | +6.00% | +1.32% | +2.48% | -1.17% | MISS | IN_CI | -0.141 | TARGET_EQ_RUN_DATE |
| PANW | gpt-5-2026-07-09 | 336.33 | 2026-08-06 | +6.00% | +7.83% | +2.48% | +5.34% | HIT | IN_CI | +0.102 | TARGET_EQ_RUN_DATE |
| HPE | gpt-5-2026-07-09 | 49.05 | 2026-08-06 | +6.00% | +8.51% | +2.48% | +6.03% | HIT | IN_CI | +0.094 | TARGET_EQ_RUN_DATE |
| DAL | claude-fable-5-2026-07-09 | 88.59 | 2026-08-06 | +6.00% | +5.14% | +2.48% | +2.66% | HIT | IN_CI | -0.079 | TARGET_EQ_RUN_DATE |
| BEN | claude-fable-5-2026-07-08 | 33.44 | 2026-08-05 | +5.00% | +4.43% | +3.42% | +1.01% | HIT | IN_CI | -0.067 | ORDINARY |
| FTNT | gpt-5-2026-07-08 | 155.92 | 2026-08-05 | +6.00% | +5.27% | +3.34% | +1.93% | HIT | IN_CI | -0.057 | ORDINARY |
| ANET | gpt-5-2026-07-09 | 184.78 | 2026-08-06 | +6.00% | +6.78% | +2.48% | +4.29% | HIT | IN_CI | +0.041 | TARGET_EQ_RUN_DATE |
| DELL | gpt-5-2026-07-08 | 431.44 | 2026-08-05 | +6.00% | +7.25% | +3.34% | +3.91% | HIT | IN_CI | +0.038 | ORDINARY |
| ANET | claude-fable-5-2026-07-09 | 184.98 | 2026-08-06 | +6.00% | +6.67% | +2.48% | +4.19% | HIT | IN_CI | +0.036 | TARGET_EQ_RUN_DATE |
| DDOG | gpt-5-2026-07-09 | 268.41 | 2026-08-06 | +6.00% | +5.50% | +2.48% | +3.01% | HIT | IN_CI | -0.027 | TARGET_EQ_RUN_DATE |
| FTNT | claude-fable-5-2026-07-08 | 155.84 | 2026-08-05 | +5.00% | +5.32% | +3.42% | +1.90% | HIT | IN_CI | +0.025 | ORDINARY |
| DDOG | claude-fable-5-2026-07-09 | 267.87 | 2026-08-06 | +6.00% | +5.71% | +2.48% | +3.23% | HIT | IN_CI | -0.016 | TARGET_EQ_RUN_DATE |
| AXON | claude-fable-5-2026-07-09 | 576.79 | 2026-08-06 | +6.00% | +5.67% | +2.48% | +3.19% | HIT | IN_CI | -0.015 | TARGET_EQ_RUN_DATE |
| CRWD | gpt-5-2026-07-09 | 198.22 | 2026-08-06 | +6.00% | +5.87% | +2.48% | +3.39% | HIT | IN_CI | -0.008 | TARGET_EQ_RUN_DATE |
| CRWD | claude-fable-5-2026-07-09 | 197.97 | 2026-08-06 | +6.00% | +6.01% | +2.48% | +3.53% | HIT | IN_CI | +0.000 | TARGET_EQ_RUN_DATE |
| SPY | claude-fable-5-2026-07-08 | 744.34 | 2026-08-05 | +0.50% | +3.42% | N/A | N/A | HIT | IN_CI | +0.663 | ORDINARY |
| SPY | gpt-5-2026-07-08 | 744.92 | 2026-08-05 | +0.50% | +3.34% | N/A | N/A | HIT | IN_CI | +0.644 | ORDINARY |
| SOXX | gpt-5-2026-07-09 | 586.84 | 2026-08-06 | +2.74% | -9.57% | N/A | N/A | MISS | IN_CI | -0.561 | TARGET_EQ_RUN_DATE |
| SOXX | claude-fable-5-2026-07-09 | 586.71 | 2026-08-06 | +1.74% | -9.55% | N/A | N/A | MISS | IN_CI | -0.523 | TARGET_EQ_RUN_DATE |
| SPY | claude-fable-5-2026-07-09 | 751.17 | 2026-08-06 | +0.50% | +2.48% | N/A | N/A | HIT | IN_CI | +0.460 | TARGET_EQ_RUN_DATE |
| SPY | gpt-5-2026-07-09 | 751.13 | 2026-08-06 | +0.50% | +2.48% | N/A | N/A | HIT | IN_CI | +0.449 | TARGET_EQ_RUN_DATE |
| SOXX | gpt-5-2026-07-08 | 561.37 | 2026-08-05 | +2.21% | -5.46% | N/A | N/A | MISS | IN_CI | -0.346 | ORDINARY |
| SOXX | claude-fable-5-2026-07-08 | 559.51 | 2026-08-05 | +1.71% | -5.15% | N/A | N/A | MISS | IN_CI | -0.309 | ORDINARY |
| QQQ | gpt-5-2026-07-09 | 723.12 | 2026-08-06 | +1.04% | -0.80% | N/A | N/A | MISS | IN_CI | -0.215 | TARGET_EQ_RUN_DATE |
| QQQ | claude-fable-5-2026-07-09 | 723.25 | 2026-08-06 | +0.84% | -0.82% | N/A | N/A | MISS | IN_CI | -0.198 | TARGET_EQ_RUN_DATE |
| QQQ | claude-fable-5-2026-07-08 | 708.55 | 2026-08-05 | +0.83% | +1.23% | N/A | N/A | HIT | IN_CI | +0.047 | ORDINARY |
| QQQ | gpt-5-2026-07-08 | 709.53 | 2026-08-05 | +0.83% | +1.10% | N/A | N/A | HIT | IN_CI | +0.031 | ORDINARY |

### Rolling calibration metrics (canonical, from `settlement_ledger.py`)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range |
|---|---|---|---|
| raw `n` | 643 | 108 | >= 10 to report |
| 28-day `eff_n` | **2** | 1 | >= 3 for Track A |
| Hit rate | 39.04% | 25.96% | > 50% |
| CI coverage | 69.36% | 84.26% | 55–85% (target 70%) |
| Mean z | -0.5328 | -0.5285 | −0.5 to +0.5 |
| Track A calibration proposal | False (`INSUFFICIENT_EFFECTIVE_N`) | False (`INSUFFICIENT_EFFECTIVE_N`) | needs `n>=20` **and** `eff_n>=3` |

**This run's own settlements**, scored separately: `EQUITY_ALPHA` n=86,
hit 32/86
(37.2%),
mean alpha -4.2346%,
mean z -0.5091,
IN_CI 63/86.
`MARKET_FORECAST` n=12, hit 6/12,
IN_CI 12/12, mean z +0.0119.

### `eff_n` — the 2026-07-28 prediction resolved

The 2026-07-28 Track B change added `eff_n_projection` and made a falsifiable claim: **EQ
`eff_n` reaches 2 on 2026-08-05**, and *"any run on/after that date still reporting eff_n 1
for that type reverts the change."* This run settled the 2026-08-05/2026-08-06 target
cohort and `eff_n` moved **1 -> 2**, with selected windows
`['2026-07-08', '2026-08-05']`. The claim **held**; the change stands.
`eff_n = 1` was a startup transient, not a design flaw, exactly as that log argued.

Track A stays gated: `eff_n 2 < 3`. Next EQ window opens
`2026-09-02`
(24 pending); `MARKET_FORECAST`
increments `2026-08-09`
(6 pending).

## 1. Prior Run Summary and mandatory tie-break disclosure

MoM window `2026-08-06 − 45d` … `2026-08-06 − 21d` = `2026-06-22` … `2026-07-16`, target
`2026-07-09`. **Two folders tie at delta 0d.** `agents.md § Orchestrator
Step 2` rule 8 requires both the deterministic tie-break *and* disclosure of every tied
candidate — tied books are not interchangeable.

Tie-break applied: **(a) same model family — executing model is claude-opus-5**. Both candidates carry a usable
`15_predictions.json`, so rule 8(a) decides and 8(b)/8(c) are not reached.

| Tied candidate | Settled n | Hit/Scored | Hit rate | Mean alpha | Mean z | CI coverage |
|---|---|---|---|---|---|---|
| `claude-fable-5-2026-07-09` | 23 | 11/23 | 47.8% | -0.6627% | -0.4498 | 69.6% |
| `gpt-5-2026-07-09` | 20 | 5/20 | 25.0% | -9.5207% | -0.6453 | 80.0% |

Both books' predictions matured **on this run date**, so their canonical rows were empty
until this run's settlements were merged in — the stats above are computed on the merged
view (the 2026-08-01 gotcha).

**Is the MoM conclusion invariant across the tied books?** *Directionally yes, in
magnitude no.* Both underperform: hit rates 47.8% and
25.0% are each below the >50% healthy bar, and both mean alphas
are negative (-0.6627% and -9.5207%). But the spread is
**22.8pp of hit rate** and **8.86pp
of mean alpha**, driven by composition rather than luck: the books share only **8 of
35** names in their union. A reader given only the `gpt-5` book would conclude the
prior cycle was a rout; given only the `claude-fable-5` book, a near-miss. Selecting a
baseline without this table would have silently chosen the narrative.

Selected baseline `claude-fable-5-2026-07-09`: age 28 days
(>= the 21-day floor), status `NO_TRADE`, 23 ranked names.

## 2. MoM Price and Return Table

Prior prices are the baseline package's own recorded `entry_price` values; current prices
are the 2026-08-05 closes (ledger rows L001, L018). SPY
751.17 -> 769.79 =
**+2.48%**.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI |
|---|---|---|---|---|---|---|---|---|---|
| DVA | 2026-07-09 | 226.79 | 2026-08-05 | 188.69 | -16.80% | +2.48% | -19.28% | Miss | OUT_CI_LOW |
| FTNT | 2026-07-09 | 163.27 | 2026-08-05 | 164.13 | +0.53% | +2.48% | -1.95% | Miss | IN_CI |
| PANW | 2026-07-09 | 336.45 | 2026-08-05 | 362.66 | +7.79% | +2.48% | +5.31% | Hit | IN_CI |
| DDOG | 2026-07-09 | 267.87 | 2026-08-05 | 283.17 | +5.71% | +2.48% | +3.23% | Hit | IN_CI |
| TROW | 2026-07-09 | 118.13 | 2026-08-05 | 114.98 | -2.67% | +2.48% | -5.15% | Miss | OUT_CI_LOW |
| FFIV | 2026-07-09 | 429.98 | 2026-08-05 | 411.32 | -4.34% | +2.48% | -6.82% | Miss | OUT_CI_LOW |
| BEN | 2026-07-09 | 33.94 | 2026-08-05 | 34.92 | +2.89% | +2.48% | +0.41% | Hit | IN_CI |
| PRU | 2026-07-09 | 115.71 | 2026-08-05 | 120.16 | +3.85% | +2.48% | +1.37% | Hit | IN_CI |
| CRWD | 2026-07-09 | 197.97 | 2026-08-05 | 209.86 | +6.01% | +2.48% | +3.53% | Hit | IN_CI |
| CRL | 2026-07-09 | 230.99 | 2026-08-05 | 260.72 | +12.87% | +2.48% | +10.39% | Hit | IN_CI |
| HUM | 2026-07-09 | 394.68 | 2026-08-05 | 363.82 | -7.82% | +2.48% | -10.30% | Miss | OUT_CI_LOW |
| AXON | 2026-07-09 | 576.79 | 2026-08-05 | 609.49 | +5.67% | +2.48% | +3.19% | Hit | IN_CI |
| TTWO | 2026-07-09 | 244.45 | 2026-08-05 | 234.91 | -3.90% | +2.48% | -6.38% | Miss | IN_CI |
| DAL | 2026-07-09 | 88.59 | 2026-08-05 | 93.14 | +5.14% | +2.48% | +2.66% | Hit | IN_CI |
| AIZ | 2026-07-09 | 278.13 | 2026-08-05 | 301.57 | +8.43% | +2.48% | +5.95% | Hit | IN_CI |
| LYV | 2026-07-09 | 182.52 | 2026-08-05 | 183.52 | +0.55% | +2.48% | -1.93% | Miss | IN_CI |
| BAX | 2026-07-09 | 22.43 | 2026-08-05 | 27.33 | +21.85% | +2.48% | +19.37% | Hit | OUT_CI_HIGH |
| MNST | 2026-07-09 | 95.85 | 2026-08-05 | 94.46 | -1.45% | +2.48% | -3.93% | Miss | OUT_CI_LOW |
| ANET | 2026-07-09 | 184.98 | 2026-08-05 | 197.31 | +6.67% | +2.48% | +4.19% | Hit | IN_CI |
| DELL | 2026-07-09 | 457.08 | 2026-08-05 | 462.70 | +1.23% | +2.48% | -1.25% | Miss | IN_CI |
| LLY | 2026-07-09 | 1,208.68 | 2026-08-05 | 1,169.86 | -3.21% | +2.48% | -5.69% | Miss | IN_CI |
| ABBV | 2026-07-09 | 248.37 | 2026-08-05 | 246.20 | -0.87% | +2.48% | -3.35% | Miss | IN_CI |
| LIN | 2026-07-09 | 524.22 | 2026-08-05 | 491.05 | -6.33% | +2.48% | -8.81% | Miss | OUT_CI_LOW |

Book mean MoM return
+1.82%
vs SPY +2.48% =
**-0.66% alpha**.
Hit/Miss split: {'Miss': 12, 'Hit': 11}.

## 3. Theme-Level Performance

The baseline book was built on the same two-family evidence base as today (`Tech_Z` +
`Macro_Z`, `Fund_Z`/`Sent_Z` UNAVAILABLE), so its themes are trend-persistence themes.

| Theme | Verdict | Evidence |
|---|---|---|
| Trend/momentum persistence over a 4-week hold | **Failed** | The book's mean alpha is -0.6627% with a 47.8% hit rate — a coin-flip that cost the benchmark spread. |
| Magnitude calibration (sigma sizing) | **Validated** | CI coverage 69.6% sits inside the 55–85% band, close to the 70% target: the intervals were honest even when the direction was wrong. |
| Rank ordering within the book | **Partial** | Vintage rank IC for the four cohorts settled this run is `claude-fable-5:2026-07-08` +0.1033, `claude-fable-5:2026-07-09` +0.0099, `gpt-5:2026-07-08` +0.2150, `gpt-5:2026-07-09` -0.0090 — three of four **positive**, which cuts against the standing rank-inversion narrative rather than confirming it. |

## 4. Regime Shift Assessment

| | Baseline (2026-07-09) | Today (2026-08-06, basis 2026-08-05) |
|---|---|---|
| SPY close | 751.17 | 769.79 |
| 4-week SPY move | — | +2.48% |
| Declared regime | `NO_TRADE` package, regime recorded in that folder | **`BULL`** |
| VIX | — | 15.81 |
| SPY 30d realized vol (1m) | — | 3.79%, falling vs the prior 30d (4.30%) |

The tape strengthened over the window: SPY +2.48% with volatility
contracting and VIX at 15.81. Factor-weight implication: none. The family
weights are fixed by `rules.md § Factor Architecture` and only the evolution agent may move
them, under Track A — which is gated at `eff_n = 2 < 3`.

## 5. Carry-Forward Decisions

Ranks and percentiles below are read from this run's `run_computed_manifest.json`, not
transcribed by hand.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| DVA | +0.5260 | Dialysis oligopoly re-rating on stable volumes; defensive HC momentum  | -16.80% | **DROP** | re-ranks #369 (pctl 27.84) — below the 60th-pctl rank floor |
| FTNT | +0.4260 | Firewall refresh cycle + SASE attach; security spend resilience | +0.53% | **DOWNGRADE** | re-ranks #33 (pctl 93.73) — below the published cut, still ranked |
| PANW | +0.4140 | Platformization-led security demand; momentum leadership intact | +7.79% | **DOWNGRADE** | re-ranks #64 (pctl 87.65) — below the published cut, still ranked |
| DDOG | +0.4040 | Observability + AI-workload monitoring attach; high-growth momentum le | +5.71% | **DOWNGRADE** | re-ranks #70 (pctl 86.47) — below the published cut, still ranked |
| TROW | +0.3740 | Flows inflection at a discounted asset manager; low-vol financials mom | -2.67% | **DROP** | re-ranks #265 (pctl 48.24) — below the 60th-pctl rank floor |
| FFIV | +0.3660 | App-delivery/security refresh; low-vol network-infra momentum | -4.34% | **DROP** | re-ranks #240 (pctl 53.14) — below the 60th-pctl rank floor |
| BEN | +0.3640 | Asset-manager torque to risk-on flows; re-rate off multi-year base | +2.89% | **CARRY** | re-ranks #24 (pctl 95.49) — inside today's published set |
| PRU | +0.3520 | Retirement/insurance flows re-rate; low-vol financials momentum | +3.85% | **CARRY** | re-ranks #15 (pctl 97.25) — inside today's published set |
| CRWD | +0.3360 | Endpoint/identity consolidation winner; high-momentum security complex | +6.01% | **DOWNGRADE** | re-ranks #118 (pctl 77.06) — below the published cut, still ranked |
| CRL | +0.3330 | Preclinical CRO demand recovery; biotech funding thaw | +12.87% | **CARRY** | re-ranks #3 (pctl 99.61) — inside today's published set |
| HUM | +0.3250 | Managed-care recovery; MA margin repair momentum | -7.82% | **DOWNGRADE** | re-ranks #133 (pctl 74.12) — below the published cut, still ranked |
| AXON | +0.3230 | Taser/body-cam ecosystem lock-in; extreme momentum, extreme vol | +5.67% | **DOWNGRADE** | re-ranks #151 (pctl 70.59) — below the published cut, still ranked |
| TTWO | +0.3080 | GTA VI cycle anticipation; content slate momentum | -3.90% | **DROP** | re-ranks #350 (pctl 31.57) — below the 60th-pctl rank floor |
| DAL | +0.3040 | Airline momentum; Q2 print released this morning (2026-07-09) | +5.14% | **DOWNGRADE** | re-ranks #94 (pctl 81.76) — below the published cut, still ranked |
| AIZ | +0.2980 | Specialty insurance compounder; low-beta momentum | +8.43% | **CARRY** | re-ranks #1 (pctl 100.00) — inside today's published set |
| LYV | +0.2970 | Live-events demand secular strength; concert calendar seasonality | +0.55% | **DROP** | re-ranks #233 (pctl 54.51) — below the 60th-pctl rank floor |
| BAX | +0.2860 | Post-restructuring margin recovery; low-priced HC turnaround momentum | +21.85% | **CARRY** | re-ranks #14 (pctl 97.45) — inside today's published set |
| MNST | +0.2770 | Energy-drink share stability; staples momentum with low beta | -1.45% | **DROP** | re-ranks #371 (pctl 27.45) — below the 60th-pctl rank floor |
| ANET | +0.2700 | AI-networking capex beneficiary; settled +15.3% alpha HIT today (gpt-5 | +6.67% | **DOWNGRADE** | re-ranks #71 (pctl 86.27) — below the published cut, still ranked |
| DELL | +0.2690 | AI-server backlog torque; hardware momentum leg | +1.23% | **DOWNGRADE** | re-ranks #149 (pctl 70.98) — below the published cut, still ranked |
| LLY | +0.1960 | GLP-1 franchise; defensive growth; carry-forward — 2 settled HITs (+5. | -3.21% | **DOWNGRADE** | re-ranks #109 (pctl 78.82) — below the published cut, still ranked |
| ABBV | +0.1440 | Skyrizi/Rinvoq momentum vs Humira erosion; carry-forward — settled HIT | -0.87% | **DOWNGRADE** | re-ranks #192 (pctl 62.55) — below the published cut, still ranked |
| LIN | +0.1190 | Industrial-gas compounder with pricing power; carry-forward — settled  | -6.33% | **DROP** | re-ranks #455 (pctl 10.98) — below the 60th-pctl rank floor |

Summary: {'DROP': 7, 'DOWNGRADE': 11, 'CARRY': 5}. `DROP` names stay out of today's scored set absent new ledger
evidence; `DOWNGRADE` names remain ranked but fall below the published cut.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (2026-08-05 completed close), grounded on 3 independent sources |
| Reflection confidence | **MEDIUM** |
| Rationale | Settlement inputs are complete and unambiguous (98/98 settled, 0 conflicts, `due_inventory` 0). Confidence is held at MEDIUM rather than HIGH because the MoM baseline is `CROSS_MODEL_BASELINE` and the tied books disagree by 22.8pp of hit rate. |
| Structural issues found | (1) **No 2026-08-05 package exists from any model** — an audit-trail gap that doubled today's settlement queue. (2) `Fund_Z`/`Sent_Z` remain UNAVAILABLE, which is what makes the evidence thresholds unsatisfiable. (3) `EA` delisted and its ticker reassigned by a price vendor to a foreign listing. |
