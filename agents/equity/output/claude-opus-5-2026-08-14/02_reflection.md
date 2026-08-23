# 02 — Reflection · 2026-08-14

## 0. Prediction Settlement

All settlement accounting comes from `settlement_ledger.py` (`L014`), the single normalizer
and precedence resolver, not from hand-reading `15_predictions.json` files.

| Field | Value |
|---|---|
| Due inventory before this run (`--as-of 2026-08-14`) | **149** |
| Settled this run | **149** (131 `EQUITY_ALPHA` + 18 `MARKET_FORECAST`) |
| Skipped / ungrounded | **0** |
| Due inventory after writing `15` | **0** |
| Conflicts | **0** |
| Rejected candidate rows (all history, re-validated) | 87 |

### Settlement timing

| Convention | Rows | Basis |
|---|---|---|
| `ORDINARY` | 100 | `target_date` 2026-08-11 / 2026-08-12, both before the run date — settled at the completed target-date close |
| `TARGET_DATE_CLOSE` | 49 | `target_date` == run date `2026-08-14`; the run fired after the close, so the same-day close is valid with an explicit flag and a timezone-aware `settled_at` of `2026-08-15T01:36:00-04:00` (at/after 16:00 America/New_York on the target date) |

The `TARGET_DATE_CLOSE` cohort validates only because of the 2026-08-07 Track B fix that
removed the calendar-date pin from the validator: this run's `settled_at` falls on
2026-08-15 ET while its `target_date` is 2026-08-14. Under the pre-fix validator all
49 of these rows
would have been rejected and left due. This is the first run to exercise that fix in the exact
after-midnight case it was written for.

### Which ledgers were scanned

Every `agents/equity/output/*/15_predictions.json` across all models
(1455 candidate settlement rows in total). Predictions
settled this run come from **2** models:
`claude-fable-5` (80), `gpt-5` (69).

### This run's settled batch

| Ticker | Vintage | Model | Entry | Target Date | mu | Settle | Realized | SPY Return | Alpha | Direction | CI Result | z | Timing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 2026-07-14 | claude-fable-5 | 248.00 | 2026-08-11 | +1.00% | 250.09 | +0.84% | +2.86% | -2.01% | MISS | `IN_CI` | -0.016 | `ORDINARY` |
| ABNB | 2026-07-14 | claude-fable-5 | 146.33 | 2026-08-11 | +6.00% | 184.98 | +26.41% | +2.86% | +23.56% | HIT | `OUT_CI_HIGH` | +2.091 | `ORDINARY` |
| ADP | 2026-07-14 | claude-fable-5 | 251.05 | 2026-08-11 | +6.00% | 271.09 | +7.98% | +2.86% | +5.13% | HIT | `IN_CI` | +0.211 | `ORDINARY` |
| ALL | 2026-07-14 | gpt-5 | 251.92 | 2026-08-11 | +6.00% | 262.23 | +4.09% | +2.50% | +1.60% | HIT | `IN_CI` | -0.241 | `ORDINARY` |
| AMD | 2026-07-14 | gpt-5 | 555.11 | 2026-08-11 | +6.00% | 474.32 | -14.55% | +2.50% | -17.05% | MISS | `IN_CI` | -0.882 | `ORDINARY` |
| ANET | 2026-07-14 | claude-fable-5 | 181.15 | 2026-08-11 | +5.00% | 197.85 | +9.22% | +2.86% | +6.36% | HIT | `IN_CI` | +0.225 | `ORDINARY` |
| ANET | 2026-07-14 | gpt-5 | 182.65 | 2026-08-11 | +6.00% | 197.85 | +8.32% | +2.50% | +5.83% | HIT | `IN_CI` | +0.122 | `ORDINARY` |
| AXON | 2026-07-14 | gpt-5 | 553.38 | 2026-08-11 | +6.00% | 636.31 | +14.99% | +2.50% | +12.49% | HIT | `IN_CI` | +0.444 | `ORDINARY` |
| BAC | 2026-07-14 | gpt-5 | 60.65 | 2026-08-11 | +6.00% | 64.00 | +5.53% | +2.50% | +3.03% | HIT | `IN_CI` | -0.079 | `ORDINARY` |
| BAX | 2026-07-14 | claude-fable-5 | 22.57 | 2026-08-11 | +5.00% | 27.61 | +22.33% | +2.86% | +19.48% | HIT | `OUT_CI_HIGH` | +1.559 | `ORDINARY` |
| BBY | 2026-07-14 | claude-fable-5 | 81.65 | 2026-08-11 | +5.00% | 83.28 | +2.00% | +2.86% | -0.86% | MISS | `IN_CI` | -0.307 | `ORDINARY` |
| BEN | 2026-07-14 | claude-fable-5 | 32.83 | 2026-08-11 | +6.00% | 33.36 | +1.61% | +2.86% | -1.24% | MISS | `IN_CI` | -0.528 | `ORDINARY` |
| CRL | 2026-07-14 | claude-fable-5 | 229.75 | 2026-08-11 | +5.00% | 282.00 | +22.74% | +2.86% | +19.89% | HIT | `OUT_CI_HIGH` | +1.485 | `ORDINARY` |
| CRL | 2026-07-14 | gpt-5 | 234.93 | 2026-08-11 | +6.00% | 282.00 | +20.04% | +2.50% | +17.54% | HIT | `OUT_CI_HIGH` | +1.155 | `ORDINARY` |
| CRWD | 2026-07-14 | gpt-5 | 207.45 | 2026-08-11 | +6.00% | 221.90 | +6.97% | +2.50% | +4.47% | HIT | `IN_CI` | +0.059 | `ORDINARY` |
| CVS | 2026-07-14 | claude-fable-5 | 105.90 | 2026-08-11 | +5.00% | 93.50 | -11.71% | +2.86% | -14.56% | MISS | `OUT_CI_LOW` | -2.334 | `ORDINARY` |
| DDOG | 2026-07-14 | claude-fable-5 | 260.24 | 2026-08-11 | +6.00% | 246.78 | -5.17% | +2.86% | -8.03% | MISS | `IN_CI` | -0.602 | `ORDINARY` |
| DDOG | 2026-07-14 | gpt-5 | 269.50 | 2026-08-11 | +6.00% | 246.78 | -8.43% | +2.50% | -10.93% | MISS | `IN_CI` | -0.765 | `ORDINARY` |
| DELL | 2026-07-14 | gpt-5 | 456.22 | 2026-08-11 | +6.00% | 440.97 | -3.34% | +2.50% | -5.84% | MISS | `IN_CI` | -0.279 | `ORDINARY` |
| DOC | 2026-07-14 | claude-fable-5 | 21.73 | 2026-08-11 | +6.00% | 20.51 | -5.61% | +2.86% | -8.47% | MISS | `OUT_CI_LOW` | -1.530 | `ORDINARY` |
| DVA | 2026-07-14 | claude-fable-5 | 235.58 | 2026-08-11 | +5.00% | 178.34 | -24.30% | +2.86% | -27.15% | MISS | `OUT_CI_LOW` | -4.197 | `ORDINARY` |
| DVA | 2026-07-14 | gpt-5 | 232.69 | 2026-08-11 | +6.00% | 178.34 | -23.36% | +2.50% | -25.86% | MISS | `OUT_CI_LOW` | -4.137 | `ORDINARY` |
| ESS | 2026-07-14 | claude-fable-5 | 297.48 | 2026-08-11 | +6.00% | 282.46 | -5.05% | +2.86% | -7.90% | MISS | `OUT_CI_LOW` | -1.889 | `ORDINARY` |
| EXPD | 2026-07-14 | claude-fable-5 | 175.50 | 2026-08-11 | +5.00% | 177.21 | +0.97% | +2.86% | -1.88% | MISS | `IN_CI` | -0.671 | `ORDINARY` |
| EXPD | 2026-07-14 | gpt-5 | 178.55 | 2026-08-11 | +6.00% | 177.21 | -0.75% | +2.50% | -3.25% | MISS | `OUT_CI_LOW` | -1.107 | `ORDINARY` |
| FFIV | 2026-07-14 | claude-fable-5 | 420.95 | 2026-08-11 | +6.00% | 414.00 | -1.65% | +2.86% | -4.51% | MISS | `IN_CI` | -0.886 | `ORDINARY` |
| FTNT | 2026-07-14 | claude-fable-5 | 160.62 | 2026-08-11 | +5.00% | 161.89 | +0.79% | +2.86% | -2.06% | MISS | `IN_CI` | -0.329 | `ORDINARY` |
| GEN | 2026-07-14 | gpt-5 | 26.55 | 2026-08-11 | +6.00% | 29.01 | +9.25% | +2.50% | +6.75% | HIT | `IN_CI` | +0.249 | `ORDINARY` |
| GS | 2026-07-14 | gpt-5 | 1,126.05 | 2026-08-11 | +6.00% | 1,034.41 | -8.14% | +2.50% | -10.64% | MISS | `OUT_CI_LOW` | -1.385 | `ORDINARY` |
| HPE | 2026-07-14 | gpt-5 | 49.36 | 2026-08-11 | +6.00% | 54.38 | +10.17% | +2.50% | +7.67% | HIT | `IN_CI` | +0.155 | `ORDINARY` |
| HUM | 2026-07-14 | claude-fable-5 | 406.00 | 2026-08-11 | +5.00% | 372.82 | -8.17% | +2.86% | -11.03% | MISS | `OUT_CI_LOW` | -1.184 | `ORDINARY` |
| KMB | 2026-07-14 | claude-fable-5 | 110.18 | 2026-08-11 | +6.00% | 108.57 | -1.46% | +2.86% | -4.32% | MISS | `IN_CI` | -0.818 | `ORDINARY` |
| LIN | 2026-07-14 | claude-fable-5 | 524.06 | 2026-08-11 | +2.00% | 490.53 | -6.40% | +2.86% | -9.25% | MISS | `OUT_CI_LOW` | -1.400 | `ORDINARY` |
| LLY | 2026-07-14 | claude-fable-5 | 1,181.87 | 2026-08-11 | +2.00% | 1,215.02 | +2.80% | +2.86% | -0.05% | MISS | `IN_CI` | +0.084 | `ORDINARY` |
| LYV | 2026-07-14 | claude-fable-5 | 183.25 | 2026-08-11 | +6.00% | 183.33 | +0.04% | +2.86% | -2.81% | MISS | `IN_CI` | -0.857 | `ORDINARY` |
| MPC | 2026-07-14 | claude-fable-5 | 296.88 | 2026-08-11 | +5.00% | 336.42 | +13.32% | +2.86% | +10.46% | HIT | `IN_CI` | +0.819 | `ORDINARY` |
| MPC | 2026-07-14 | gpt-5 | 300.60 | 2026-08-11 | +6.00% | 336.42 | +11.92% | +2.50% | +9.42% | HIT | `IN_CI` | +0.573 | `ORDINARY` |
| NTAP | 2026-07-14 | gpt-5 | 173.81 | 2026-08-11 | +6.00% | 198.47 | +14.19% | +2.50% | +11.69% | HIT | `IN_CI` | +0.368 | `ORDINARY` |
| PANW | 2026-07-14 | claude-fable-5 | 330.30 | 2026-08-11 | +5.00% | 383.80 | +16.20% | +2.86% | +13.34% | HIT | `IN_CI` | +0.634 | `ORDINARY` |
| PANW | 2026-07-14 | gpt-5 | 351.88 | 2026-08-11 | +6.00% | 383.80 | +9.07% | +2.50% | +6.57% | HIT | `IN_CI` | +0.171 | `ORDINARY` |
| PSX | 2026-07-14 | gpt-5 | 200.65 | 2026-08-11 | +6.00% | 224.36 | +11.82% | +2.50% | +9.32% | HIT | `IN_CI` | +0.615 | `ORDINARY` |
| TROW | 2026-07-14 | claude-fable-5 | 113.65 | 2026-08-11 | +5.00% | 113.75 | +0.09% | +2.86% | -2.77% | MISS | `IN_CI` | -0.657 | `ORDINARY` |
| XYZ | 2026-07-14 | gpt-5 | 80.71 | 2026-08-11 | +6.00% | 79.07 | -2.03% | +2.50% | -4.53% | MISS | `IN_CI` | -0.617 | `ORDINARY` |
| ZS | 2026-07-14 | gpt-5 | 153.59 | 2026-08-11 | +6.00% | 178.55 | +16.25% | +2.50% | +13.76% | HIT | `IN_CI` | +0.551 | `ORDINARY` |
| AAPL | 2026-07-15 | gpt-5 | 327.86 | 2026-08-12 | +6.00% | 302.25 | -7.81% | +2.39% | -10.20% | MISS | `OUT_CI_LOW` | -1.421 | `ORDINARY` |
| ABBV | 2026-07-15 | claude-fable-5 | 244.78 | 2026-08-12 | +1.00% | 248.76 | +1.63% | +2.75% | -1.12% | MISS | `IN_CI` | +0.064 | `ORDINARY` |
| ANET | 2026-07-15 | claude-fable-5 | 182.57 | 2026-08-12 | +2.00% | 210.50 | +15.30% | +2.75% | +12.55% | HIT | `IN_CI` | +0.713 | `ORDINARY` |
| BAC | 2026-07-15 | gpt-5 | 61.49 | 2026-08-12 | +6.00% | 64.81 | +5.40% | +2.39% | +3.01% | HIT | `IN_CI` | -0.101 | `ORDINARY` |
| BBY | 2026-07-15 | gpt-5 | 85.29 | 2026-08-12 | +6.00% | 83.00 | -2.68% | +2.39% | -5.07% | MISS | `IN_CI` | -0.904 | `ORDINARY` |
| CRL | 2026-07-15 | claude-fable-5 | 231.21 | 2026-08-12 | +5.00% | 284.37 | +22.99% | +2.75% | +20.24% | HIT | `OUT_CI_HIGH` | +1.511 | `ORDINARY` |
| CRL | 2026-07-15 | gpt-5 | 227.68 | 2026-08-12 | +6.00% | 284.37 | +24.90% | +2.39% | +22.50% | HIT | `OUT_CI_HIGH` | +1.560 | `ORDINARY` |
| CRWD | 2026-07-15 | claude-fable-5 | 210.73 | 2026-08-12 | +6.00% | 221.78 | +5.24% | +2.75% | +2.50% | HIT | `IN_CI` | -0.043 | `ORDINARY` |
| CRWD | 2026-07-15 | gpt-5 | 207.13 | 2026-08-12 | +6.00% | 221.78 | +7.07% | +2.39% | +4.68% | HIT | `IN_CI` | +0.060 | `ORDINARY` |
| CVS | 2026-07-15 | claude-fable-5 | 106.18 | 2026-08-12 | +5.00% | 94.72 | -10.79% | +2.75% | -13.54% | MISS | `OUT_CI_LOW` | -2.316 | `ORDINARY` |
| CVS | 2026-07-15 | gpt-5 | 105.92 | 2026-08-12 | +6.00% | 94.72 | -10.57% | +2.39% | -12.97% | MISS | `OUT_CI_LOW` | -2.389 | `ORDINARY` |
| DDOG | 2026-07-15 | claude-fable-5 | 270.73 | 2026-08-12 | +6.00% | 240.91 | -11.01% | +2.75% | -13.76% | MISS | `IN_CI` | -0.996 | `ORDINARY` |
| DDOG | 2026-07-15 | gpt-5 | 265.00 | 2026-08-12 | +6.00% | 240.91 | -9.09% | +2.39% | -11.48% | MISS | `IN_CI` | -0.868 | `ORDINARY` |
| DELL | 2026-07-15 | gpt-5 | 415.71 | 2026-08-12 | +6.00% | 484.50 | +16.55% | +2.39% | +14.16% | HIT | `IN_CI` | +0.522 | `ORDINARY` |
| DOC | 2026-07-15 | claude-fable-5 | 21.66 | 2026-08-12 | +6.00% | 20.66 | -4.62% | +2.75% | -7.36% | MISS | `OUT_CI_LOW` | -1.439 | `ORDINARY` |
| DVA | 2026-07-15 | claude-fable-5 | 232.41 | 2026-08-12 | +5.00% | 181.50 | -21.91% | +2.75% | -24.65% | MISS | `OUT_CI_LOW` | -3.860 | `ORDINARY` |
| ELV | 2026-07-15 | claude-fable-5 | 426.79 | 2026-08-12 | +6.00% | 399.14 | -6.48% | +2.75% | -9.23% | MISS | `OUT_CI_LOW` | -1.152 | `ORDINARY` |
| EXPD | 2026-07-15 | claude-fable-5 | 178.22 | 2026-08-12 | +5.00% | 184.47 | +3.51% | +2.75% | +0.76% | HIT | `IN_CI` | -0.248 | `ORDINARY` |
| EXPD | 2026-07-15 | gpt-5 | 177.60 | 2026-08-12 | +6.00% | 184.47 | +3.87% | +2.39% | +1.48% | HIT | `IN_CI` | -0.348 | `ORDINARY` |
| FFIV | 2026-07-15 | claude-fable-5 | 431.26 | 2026-08-12 | +6.00% | 422.95 | -1.93% | +2.75% | -4.67% | MISS | `IN_CI` | -0.901 | `ORDINARY` |
| FTNT | 2026-07-15 | claude-fable-5 | 166.83 | 2026-08-12 | +5.00% | 160.84 | -3.59% | +2.75% | -6.34% | MISS | `IN_CI` | -0.706 | `ORDINARY` |
| GEN | 2026-07-15 | claude-fable-5 | 26.57 | 2026-08-12 | +6.00% | 28.64 | +7.79% | +2.75% | +5.04% | HIT | `IN_CI` | +0.147 | `ORDINARY` |
| GEN | 2026-07-15 | gpt-5 | 26.47 | 2026-08-12 | +6.00% | 28.64 | +8.20% | +2.39% | +5.81% | HIT | `IN_CI` | +0.177 | `ORDINARY` |
| GPN | 2026-07-15 | gpt-5 | 78.17 | 2026-08-12 | +6.00% | 88.53 | +13.25% | +2.39% | +10.86% | HIT | `IN_CI` | +0.523 | `ORDINARY` |
| GS | 2026-07-15 | claude-fable-5 | 1,140.00 | 2026-08-12 | +6.00% | 1,037.21 | -9.02% | +2.75% | -11.76% | MISS | `OUT_CI_LOW` | -1.216 | `ORDINARY` |
| GS | 2026-07-15 | gpt-5 | 1,150.85 | 2026-08-12 | +6.00% | 1,037.21 | -9.87% | +2.39% | -12.27% | MISS | `OUT_CI_LOW` | -1.263 | `ORDINARY` |
| HPE | 2026-07-15 | gpt-5 | 47.63 | 2026-08-12 | +6.00% | 58.79 | +23.42% | +2.39% | +21.03% | HIT | `IN_CI` | +0.691 | `ORDINARY` |
| LIN | 2026-07-15 | claude-fable-5 | 522.54 | 2026-08-12 | +1.00% | 479.43 | -8.25% | +2.75% | -11.00% | MISS | `OUT_CI_LOW` | -1.555 | `ORDINARY` |
| LLY | 2026-07-15 | claude-fable-5 | 1,152.54 | 2026-08-12 | +1.00% | 1,220.28 | +5.88% | +2.75% | +3.13% | HIT | `IN_CI` | +0.503 | `ORDINARY` |
| MNST | 2026-07-15 | claude-fable-5 | 98.00 | 2026-08-12 | +5.00% | 45.98 | -53.08% | +2.75% | -55.83% | MISS | `OUT_CI_LOW` | -12.411 | `ORDINARY` |
| MPC | 2026-07-15 | claude-fable-5 | 303.40 | 2026-08-12 | +5.00% | 348.25 | +14.78% | +2.75% | +12.03% | HIT | `IN_CI` | +0.964 | `ORDINARY` |
| MPC | 2026-07-15 | gpt-5 | 300.05 | 2026-08-12 | +6.00% | 348.25 | +16.06% | +2.39% | +13.67% | HIT | `IN_CI` | +0.975 | `ORDINARY` |
| MS | 2026-07-15 | claude-fable-5 | 227.67 | 2026-08-12 | +5.00% | 217.64 | -4.41% | +2.75% | -7.15% | MISS | `OUT_CI_LOW` | -1.046 | `ORDINARY` |
| MS | 2026-07-15 | gpt-5 | 228.93 | 2026-08-12 | +6.00% | 217.64 | -4.93% | +2.39% | -7.32% | MISS | `OUT_CI_LOW` | -1.196 | `ORDINARY` |
| NTAP | 2026-07-15 | claude-fable-5 | 174.55 | 2026-08-12 | +6.00% | 202.05 | +15.75% | +2.75% | +13.01% | HIT | `IN_CI` | +0.761 | `ORDINARY` |
| PANW | 2026-07-15 | claude-fable-5 | 352.89 | 2026-08-12 | +5.00% | 387.01 | +9.67% | +2.75% | +6.92% | HIT | `IN_CI` | +0.275 | `ORDINARY` |
| PANW | 2026-07-15 | gpt-5 | 355.49 | 2026-08-12 | +6.00% | 387.01 | +8.87% | +2.39% | +6.47% | HIT | `IN_CI` | +0.166 | `ORDINARY` |
| PSX | 2026-07-15 | gpt-5 | 196.15 | 2026-08-12 | +6.00% | 225.58 | +15.00% | +2.39% | +12.61% | HIT | `IN_CI` | +0.951 | `ORDINARY` |
| RVTY | 2026-07-15 | claude-fable-5 | 111.21 | 2026-08-12 | +6.00% | 117.88 | +6.00% | +2.75% | +3.25% | HIT | `IN_CI` | -0.000 | `ORDINARY` |
| STT | 2026-07-15 | claude-fable-5 | 183.65 | 2026-08-12 | +5.00% | 190.11 | +3.52% | +2.75% | +0.77% | HIT | `IN_CI` | -0.204 | `ORDINARY` |
| TRI | 2026-07-15 | gpt-5 | 95.66 | 2026-08-12 | +6.00% | 102.61 | +7.27% | +2.39% | +4.87% | HIT | `IN_CI` | +0.082 | `ORDINARY` |
| VLO | 2026-07-15 | gpt-5 | 293.67 | 2026-08-12 | +6.00% | 330.21 | +12.44% | +2.39% | +10.05% | HIT | `IN_CI` | +0.566 | `ORDINARY` |
| WST | 2026-07-15 | claude-fable-5 | 357.65 | 2026-08-12 | +6.00% | 352.29 | -1.50% | +2.75% | -4.25% | MISS | `OUT_CI_LOW` | -1.119 | `ORDINARY` |
| XYZ | 2026-07-15 | gpt-5 | 81.82 | 2026-08-12 | +6.00% | 78.28 | -4.33% | +2.39% | -6.72% | MISS | `IN_CI` | -0.794 | `ORDINARY` |
| AAPL | 2026-07-17 | gpt-5 | 334.19 | 2026-08-14 | +6.00% | 305.93 | -8.46% | +4.40% | -12.86% | MISS | `OUT_CI_LOW` | -1.454 | `TARGET_DATE_CLOSE` |
| ABBV | 2026-07-17 | claude-fable-5 | 254.59 | 2026-08-14 | +1.00% | 249.46 | -2.02% | +4.47% | -6.48% | MISS | `IN_CI` | -0.298 | `TARGET_DATE_CLOSE` |
| AMCR | 2026-07-17 | claude-fable-5 | 43.94 | 2026-08-14 | +6.00% | 46.03 | +4.76% | +4.47% | +0.29% | HIT | `IN_CI` | -0.132 | `TARGET_DATE_CLOSE` |
| BAC | 2026-07-17 | gpt-5 | 61.17 | 2026-08-14 | +6.00% | 64.49 | +5.42% | +4.40% | +1.02% | HIT | `IN_CI` | -0.099 | `TARGET_DATE_CLOSE` |
| BBY | 2026-07-17 | claude-fable-5 | 85.43 | 2026-08-14 | +5.00% | 86.42 | +1.16% | +4.47% | -3.31% | MISS | `IN_CI` | -0.460 | `TARGET_DATE_CLOSE` |
| BBY | 2026-07-17 | gpt-5 | 84.95 | 2026-08-14 | +6.00% | 86.42 | +1.73% | +4.40% | -2.67% | MISS | `IN_CI` | -0.501 | `TARGET_DATE_CLOSE` |
| CHRW | 2026-07-17 | gpt-5 | 207.22 | 2026-08-14 | +5.00% | 148.57 | -28.30% | +4.40% | -32.70% | MISS | `OUT_CI_LOW` | -3.747 | `TARGET_DATE_CLOSE` |
| CRWD | 2026-07-17 | claude-fable-5 | 203.08 | 2026-08-14 | +6.00% | 216.95 | +6.83% | +4.47% | +2.36% | HIT | `IN_CI` | +0.049 | `TARGET_DATE_CLOSE` |
| CRWD | 2026-07-17 | gpt-5 | 203.95 | 2026-08-14 | +6.00% | 216.95 | +6.38% | +4.40% | +1.98% | HIT | `IN_CI` | +0.022 | `TARGET_DATE_CLOSE` |
| CTAS | 2026-07-17 | claude-fable-5 | 204.45 | 2026-08-14 | +5.00% | 199.52 | -2.41% | +4.47% | -6.88% | MISS | `IN_CI` | -0.661 | `TARGET_DATE_CLOSE` |
| DDOG | 2026-07-17 | claude-fable-5 | 258.69 | 2026-08-14 | +6.00% | 255.46 | -1.25% | +4.47% | -5.71% | MISS | `IN_CI` | -0.571 | `TARGET_DATE_CLOSE` |
| DDOG | 2026-07-17 | gpt-5 | 258.29 | 2026-08-14 | +6.00% | 255.46 | -1.10% | +4.40% | -5.50% | MISS | `IN_CI` | -0.508 | `TARGET_DATE_CLOSE` |
| DG | 2026-07-17 | gpt-5 | 125.46 | 2026-08-14 | +6.00% | 123.28 | -1.74% | +4.40% | -6.14% | MISS | `IN_CI` | -0.708 | `TARGET_DATE_CLOSE` |
| DOC | 2026-07-17 | claude-fable-5 | 22.50 | 2026-08-14 | +5.00% | 20.79 | -7.62% | +4.47% | -12.09% | MISS | `OUT_CI_LOW` | -1.753 | `TARGET_DATE_CLOSE` |
| DOC | 2026-07-17 | gpt-5 | 22.33 | 2026-08-14 | +6.00% | 20.79 | -6.90% | +4.40% | -11.30% | MISS | `OUT_CI_LOW` | -1.720 | `TARGET_DATE_CLOSE` |
| DVA | 2026-07-17 | claude-fable-5 | 237.01 | 2026-08-14 | +5.00% | 180.06 | -24.03% | +4.47% | -28.49% | MISS | `OUT_CI_LOW` | -4.854 | `TARGET_DATE_CLOSE` |
| EXPD | 2026-07-17 | claude-fable-5 | 182.74 | 2026-08-14 | +5.00% | 186.12 | +1.85% | +4.47% | -2.62% | MISS | `IN_CI` | -0.512 | `TARGET_DATE_CLOSE` |
| GE | 2026-07-17 | claude-fable-5 | 348.66 | 2026-08-14 | +3.00% | 368.38 | +5.66% | +4.47% | +1.19% | HIT | `IN_CI` | +0.279 | `TARGET_DATE_CLOSE` |
| GEN | 2026-07-17 | claude-fable-5 | 26.74 | 2026-08-14 | +6.00% | 28.48 | +6.51% | +4.47% | +2.04% | HIT | `IN_CI` | +0.049 | `TARGET_DATE_CLOSE` |
| GEN | 2026-07-17 | gpt-5 | 26.75 | 2026-08-14 | +6.00% | 28.48 | +6.49% | +4.40% | +2.09% | HIT | `IN_CI` | +0.046 | `TARGET_DATE_CLOSE` |
| HPQ | 2026-07-17 | gpt-5 | 24.98 | 2026-08-14 | +5.00% | 30.11 | +20.56% | +4.40% | +16.16% | HIT | `OUT_CI_HIGH` | +1.605 | `TARGET_DATE_CLOSE` |
| INCY | 2026-07-17 | gpt-5 | 117.17 | 2026-08-14 | +6.00% | 120.16 | +2.55% | +4.40% | -1.85% | MISS | `IN_CI` | -0.288 | `TARGET_DATE_CLOSE` |
| IQV | 2026-07-17 | gpt-5 | 206.65 | 2026-08-14 | +5.00% | 236.66 | +14.52% | +4.40% | +10.13% | HIT | `IN_CI` | +0.867 | `TARGET_DATE_CLOSE` |
| JBHT | 2026-07-17 | claude-fable-5 | 291.41 | 2026-08-14 | +6.00% | 279.71 | -4.01% | +4.47% | -8.48% | MISS | `IN_CI` | -0.944 | `TARGET_DATE_CLOSE` |
| LLY | 2026-07-17 | claude-fable-5 | 1,178.86 | 2026-08-14 | +4.00% | 1,180.16 | +0.11% | +4.47% | -4.36% | MISS | `IN_CI` | -0.409 | `TARGET_DATE_CLOSE` |
| MET | 2026-07-17 | claude-fable-5 | 94.00 | 2026-08-14 | +5.00% | 97.66 | +3.90% | +4.47% | -0.57% | MISS | `IN_CI` | -0.151 | `TARGET_DATE_CLOSE` |
| MNST | 2026-07-17 | claude-fable-5 | 97.50 | 2026-08-14 | +5.00% | 46.82 | -51.98% | +4.47% | -56.45% | MISS | `OUT_CI_LOW` | -10.417 | `TARGET_DATE_CLOSE` |
| MNST | 2026-07-17 | gpt-5 | 97.31 | 2026-08-14 | +6.00% | 46.82 | -51.89% | +4.40% | -56.29% | MISS | `OUT_CI_LOW` | -11.709 | `TARGET_DATE_CLOSE` |
| MPC | 2026-07-17 | claude-fable-5 | 312.62 | 2026-08-14 | +5.00% | 355.42 | +13.69% | +4.47% | +9.23% | HIT | `IN_CI` | +0.855 | `TARGET_DATE_CLOSE` |
| MPC | 2026-07-17 | gpt-5 | 311.42 | 2026-08-14 | +6.00% | 355.42 | +14.13% | +4.40% | +9.73% | HIT | `IN_CI` | +0.804 | `TARGET_DATE_CLOSE` |
| NTAP | 2026-07-17 | gpt-5 | 163.55 | 2026-08-14 | +6.00% | 207.08 | +26.62% | +4.40% | +22.22% | HIT | `OUT_CI_HIGH` | +1.472 | `TARGET_DATE_CLOSE` |
| PANW | 2026-07-17 | claude-fable-5 | 358.68 | 2026-08-14 | +5.00% | 384.27 | +7.13% | +4.47% | +2.67% | HIT | `IN_CI` | +0.138 | `TARGET_DATE_CLOSE` |
| PANW | 2026-07-17 | gpt-5 | 356.79 | 2026-08-14 | +6.00% | 384.27 | +7.70% | +4.40% | +3.30% | HIT | `IN_CI` | +0.104 | `TARGET_DATE_CLOSE` |
| PAYX | 2026-07-17 | claude-fable-5 | 114.39 | 2026-08-14 | +5.00% | 122.02 | +6.67% | +4.47% | +2.20% | HIT | `IN_CI` | +0.186 | `TARGET_DATE_CLOSE` |
| PRU | 2026-07-17 | claude-fable-5 | 119.06 | 2026-08-14 | +5.00% | 125.13 | +5.10% | +4.47% | +0.64% | HIT | `IN_CI` | +0.016 | `TARGET_DATE_CLOSE` |
| PSX | 2026-07-17 | gpt-5 | 206.37 | 2026-08-14 | +6.00% | 233.61 | +13.20% | +4.40% | +8.80% | HIT | `IN_CI` | +0.734 | `TARGET_DATE_CLOSE` |
| STT | 2026-07-17 | claude-fable-5 | 182.56 | 2026-08-14 | +5.00% | 191.74 | +5.03% | +4.47% | +0.56% | HIT | `IN_CI` | +0.004 | `TARGET_DATE_CLOSE` |
| TRV | 2026-07-17 | claude-fable-5 | 369.08 | 2026-08-14 | +5.00% | 370.36 | +0.35% | +4.47% | -4.12% | MISS | `IN_CI` | -0.479 | `TARGET_DATE_CLOSE` |
| UNH | 2026-07-17 | claude-fable-5 | 426.06 | 2026-08-14 | +5.00% | 401.73 | -5.71% | +4.47% | -10.18% | MISS | `OUT_CI_LOW` | -1.368 | `TARGET_DATE_CLOSE` |
| UNP | 2026-07-17 | gpt-5 | 299.88 | 2026-08-14 | +6.00% | 293.68 | -2.07% | +4.40% | -6.47% | MISS | `OUT_CI_LOW` | -1.133 | `TARGET_DATE_CLOSE` |
| USB | 2026-07-17 | claude-fable-5 | 63.16 | 2026-08-14 | +6.00% | 65.42 | +3.58% | +4.47% | -0.89% | MISS | `IN_CI` | -0.338 | `TARGET_DATE_CLOSE` |
| VEEV | 2026-07-17 | gpt-5 | 195.75 | 2026-08-14 | +5.00% | 243.75 | +24.52% | +4.40% | +20.12% | HIT | `OUT_CI_HIGH` | +1.520 | `TARGET_DATE_CLOSE` |
| VLO | 2026-07-17 | gpt-5 | 306.70 | 2026-08-14 | +6.00% | 341.67 | +11.40% | +4.40% | +7.00% | HIT | `IN_CI` | +0.465 | `TARGET_DATE_CLOSE` |
| QQQ | 2026-07-14 | claude-fable-5 | 711.74 | 2026-08-11 | +0.84% | 718.45 | +0.94% | N/A | N/A | HIT | `IN_CI` | +0.012 | `ORDINARY` |
| QQQ | 2026-07-14 | gpt-5 | 720.57 | 2026-08-11 | +3.62% | 718.45 | -0.29% | N/A | N/A | MISS | `IN_CI` | -0.451 | `ORDINARY` |
| SOXX | 2026-07-14 | claude-fable-5 | 553.61 | 2026-08-11 | +0.30% | 534.20 | -3.51% | N/A | N/A | N/A - FLAT_CALL | `IN_CI` | -0.175 | `ORDINARY` |
| SOXX | 2026-07-14 | gpt-5 | 570.92 | 2026-08-11 | +7.68% | 534.20 | -6.43% | N/A | N/A | MISS | `IN_CI` | -0.636 | `ORDINARY` |
| SPY | 2026-07-14 | claude-fable-5 | 749.17 | 2026-08-11 | +0.50% | 770.56 | +2.86% | N/A | N/A | HIT | `IN_CI` | +0.536 | `ORDINARY` |
| SPY | 2026-07-14 | gpt-5 | 751.78 | 2026-08-11 | +2.00% | 770.56 | +2.50% | N/A | N/A | HIT | `IN_CI` | +0.111 | `ORDINARY` |
| QQQ | 2026-07-15 | claude-fable-5 | 719.69 | 2026-08-12 | +0.84% | 723.70 | +0.56% | N/A | N/A | HIT | `IN_CI` | -0.033 | `ORDINARY` |
| QQQ | 2026-07-15 | gpt-5 | 717.73 | 2026-08-12 | +3.63% | 723.70 | +0.83% | N/A | N/A | HIT | `IN_CI` | -0.320 | `ORDINARY` |
| SOXX | 2026-07-15 | claude-fable-5 | 567.92 | 2026-08-12 | +1.30% | 546.61 | -3.75% | N/A | N/A | MISS | `IN_CI` | -0.231 | `ORDINARY` |
| SOXX | 2026-07-15 | gpt-5 | 555.70 | 2026-08-12 | +7.69% | 546.61 | -1.63% | N/A | N/A | MISS | `IN_CI` | -0.419 | `ORDINARY` |
| SPY | 2026-07-15 | claude-fable-5 | 751.83 | 2026-08-12 | +0.50% | 772.49 | +2.75% | N/A | N/A | HIT | `IN_CI` | +0.511 | `ORDINARY` |
| SPY | 2026-07-15 | gpt-5 | 754.44 | 2026-08-12 | +2.00% | 772.49 | +2.39% | N/A | N/A | HIT | `IN_CI` | +0.088 | `ORDINARY` |
| QQQ | 2026-07-17 | claude-fable-5 | 695.33 | 2026-08-14 | +0.37% | 731.07 | +5.14% | N/A | N/A | N/A - FLAT_CALL | `IN_CI` | +0.538 | `TARGET_DATE_CLOSE` |
| QQQ | 2026-07-17 | gpt-5 | 696.75 | 2026-08-14 | +0.86% | 731.07 | +4.93% | N/A | N/A | HIT | `IN_CI` | +0.462 | `TARGET_DATE_CLOSE` |
| SOXX | 2026-07-17 | claude-fable-5 | 521.81 | 2026-08-14 | +0.35% | 550.42 | +5.48% | N/A | N/A | N/A - FLAT_CALL | `IN_CI` | +0.233 | `TARGET_DATE_CLOSE` |
| SOXX | 2026-07-17 | gpt-5 | 522.95 | 2026-08-14 | +1.84% | 550.42 | +5.25% | N/A | N/A | HIT | `IN_CI` | +0.155 | `TARGET_DATE_CLOSE` |
| SPY | 2026-07-17 | claude-fable-5 | 743.15 | 2026-08-14 | +0.50% | 776.34 | +4.47% | N/A | N/A | HIT | `IN_CI` | +0.874 | `TARGET_DATE_CLOSE` |
| SPY | 2026-07-17 | gpt-5 | 743.62 | 2026-08-14 | +0.50% | 776.34 | +4.40% | N/A | N/A | HIT | `IN_CI` | +0.867 | `TARGET_DATE_CLOSE` |

**Batch summary.** `EQUITY_ALPHA`: n=131, hit rate
48.9% (64/131), mean alpha
-1.27%, mean z
-0.606, CI coverage
69.5%.
`MARKET_FORECAST`: n=18, 15 direction-scored (3 `N/A - FLAT_CALL` where
`|mu| < 0.5%`), hit rate 73.3% (11/15), CI coverage
100.0%.

This batch's market-forecast hit rate is the **best of the series to date** and sits far above
the 32.2% rolling figure — the batch settled into a rising tape that
matched the positive ETF priors. One good batch is not evidence of fixed calibration; the
rolling numbers below are the grounding target.

### Rolling calibration metrics (canonical)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range | Reading |
|---|---|---|---|---|
| Raw `n` | 950 | 150 | >= 10 to report | OK |
| 28-day `eff_n` | **2** | **2** | >= 3 for Track A | **below gate** |
| Hit rate | 40.53% | 32.17% | > 50% | **both below** |
| CI coverage | 70.84% | 88.67% | 55%–85% | EQ OK · **MF above band** |
| Mean z | -0.5220 | -0.4000 | -0.5 to +0.5 | **EQ marginally below** · MF OK |
| Rank IC (weighted mean) | -0.0630 | n/a (raw-return scoring) | > 0 | **negative** |

`EQUITY_ALPHA` and `MARKET_FORECAST` are reported separately and never pooled, per
`rules.md § Rolling Calibration Metrics`.

**Bindings this creates for factor scoring** (`agents.md § Calibration Feedback Binding`):

1. Rank IC **-0.0630 <= 0** over **950** settled records (>= 20) →
   **all confidence capped at `MEDIUM`.** No name in this package carries `HIGH`.
2. `EQUITY_ALPHA` CI coverage **70.84%** is inside the 55–85% band, so
   the "widen sigma / shrink mu" branch does **not** fire; `mu` is taken from the calibration
   table with no positive adjustment.
3. `MARKET_FORECAST` CI coverage **88.67%** is **above 85%** →
   `rules.md` reads this as "intervals uninformatively wide: tighten". This is a Track A
   change to the ETF sigma/mu chain and is **`DEFER`red** at `eff_n = 2 < 3`; see
   `13`.

### Track A eligibility

| Record type | Raw `n` >= 20 | `eff_n` >= 3 | Eligible | Next increment |
|---|---|---|---|---|
| `EQUITY_ALPHA` | Yes (950) | **No (2)** | **False** | 2026-09-03 (24 pending) |
| `MARKET_FORECAST` | Yes (150) | **No (2)** | **False** | 2026-09-07 (3 pending) |

`eff_n` moved **1 → 2** for both record types since the 2026-08-07 package. The 2026-07-28
package made this falsifiable: it projected `EQUITY_ALPHA` `eff_n -> 2` on 2026-08-05, and
that is what happened. The startup-transient explanation for `eff_n = 1` is now confirmed
rather than assumed, and the machinery is behaving as designed.

## 1. Prior Run Summary — baseline `claude-opus-5-2026-07-24`

| Field | Value |
|---|---|
| Baseline folder | `agents/equity/output/claude-opus-5-2026-07-24` |
| Model | `claude-opus-5` (same model family as this run) |
| Baseline flag | **`NONE`** |
| Selection | MoM window `[2026-06-30, 2026-07-24]`, target `2026-07-17`. Only same-model folder in-window; delta **7d** (rule 3 sets `BASELINE_WINDOW_GAP` only when `> 7d`), age **21d** (rule 7 floor is "less than 21 days", so 21d qualifies). |
| Prior status | `NO_TRADE` |
| Prior regime | `HIGH_VOL` (SPY prior mu 0.00%) |
| Prior book | 26 `EQUITY_ALPHA` monitoring names + 3 `MARKET_FORECAST` |

### Tie-break disclosure (rule 8)

Rule 8 is **not triggered** — there is exactly one same-model in-window folder, so nothing is
tied at the same `|folder_date - target|`. Two cross-model folders sit at delta **0d**
(`claude-fable-5-2026-07-17`, `gpt-5-2026-07-17`), which is closer to target than the selected
baseline, but rule 3 (same-model in-window) is applied before rule 4 (cross-model), so they are
not candidates. They are named here anyway because the rule's purpose is to stop a baseline
being chosen without disclosing the alternatives.

## 2. MoM Price & Return Table

Prior prices are the baseline package's own recorded `entry_price` values; current prices are
this run's grounded basis closes (`L004`, `L005`). Hit/Miss is **alpha-based** for
`EQUITY_ALPHA` and **raw-return-based** for `MARKET_FORECAST`, per `rules.md § Settlement Rules`.

| Ticker | Type | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI Result | Rank today |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | `EQUITY_ALPHA` | 2026-07-24 | 333.02 | 2026-08-14 | 305.93 | -8.13% | +5.06% | -13.20% | Miss | `OUT_CI_LOW` | rank 402/511 |
| BAC | `EQUITY_ALPHA` | 2026-07-24 | 62.05 | 2026-08-14 | 64.49 | +3.93% | +5.06% | -1.13% | Miss | `IN_CI` | rank 11/511 |
| BNY | `EQUITY_ALPHA` | 2026-07-24 | 158.91 | 2026-08-14 | 163.24 | +2.72% | +5.06% | -2.34% | Miss | `IN_CI` | rank 20/511 |
| CSX | `EQUITY_ALPHA` | 2026-07-24 | 53.23 | 2026-08-14 | 50.16 | -5.77% | +5.06% | -10.83% | Miss | `OUT_CI_LOW` | rank 307/511 |
| CTAS | `EQUITY_ALPHA` | 2026-07-24 | 205.91 | 2026-08-14 | 199.52 | -3.10% | +5.06% | -8.17% | Miss | `IN_CI` | rank 314/511 |
| DGX | `EQUITY_ALPHA` | 2026-07-24 | 227.86 | 2026-08-14 | 234.40 | +2.87% | +5.06% | -2.19% | Miss | `IN_CI` | rank 164/511 |
| GD | `EQUITY_ALPHA` | 2026-07-24 | 386.75 | 2026-08-14 | 395.78 | +2.33% | +5.06% | -2.73% | Miss | `IN_CI` | rank 57/511 |
| HIG | `EQUITY_ALPHA` | 2026-07-24 | 140.53 | 2026-08-14 | 138.02 | -1.79% | +5.06% | -6.85% | Miss | `OUT_CI_LOW` | rank 263/511 |
| JPM | `EQUITY_ALPHA` | 2026-07-24 | 353.21 | 2026-08-14 | 362.84 | +2.73% | +5.06% | -2.34% | Miss | `IN_CI` | rank 54/511 |
| LLY | `EQUITY_ALPHA` | 2026-07-24 | 1,196.03 | 2026-08-14 | 1,180.16 | -1.33% | +5.06% | -6.39% | Miss | `IN_CI` | rank 134/511 |
| LMT | `EQUITY_ALPHA` | 2026-07-24 | 582.60 | 2026-08-14 | 608.68 | +4.48% | +5.06% | -0.59% | Miss | `IN_CI` | rank 58/511 |
| MET | `EQUITY_ALPHA` | 2026-07-24 | 94.83 | 2026-08-14 | 97.66 | +2.98% | +5.06% | -2.08% | Miss | `IN_CI` | rank 83/511 |
| MPC | `EQUITY_ALPHA` | 2026-07-24 | 309.24 | 2026-08-14 | 355.42 | +14.93% | +5.06% | +9.87% | Hit | `IN_CI` | rank 69/511 |
| MTB | `EQUITY_ALPHA` | 2026-07-24 | 249.60 | 2026-08-14 | 254.09 | +1.80% | +5.06% | -3.26% | Miss | `IN_CI` | rank 107/511 |
| NSC | `EQUITY_ALPHA` | 2026-07-24 | 350.66 | 2026-08-14 | 334.41 | -4.63% | +5.06% | -9.70% | Miss | `OUT_CI_LOW` | rank 264/511 |
| PAYX | `EQUITY_ALPHA` | 2026-07-24 | 113.55 | 2026-08-14 | 122.02 | +7.46% | +5.06% | +2.40% | Hit | `IN_CI` | rank 209/511 |
| PCG | `EQUITY_ALPHA` | 2026-07-24 | 17.85 | 2026-08-14 | 17.84 | -0.06% | +5.06% | -5.12% | Miss | `IN_CI` | rank 230/511 |
| PKG | `EQUITY_ALPHA` | 2026-07-24 | 254.39 | 2026-08-14 | 255.48 | +0.43% | +5.06% | -4.63% | Miss | `IN_CI` | rank 112/511 |
| PM | `EQUITY_ALPHA` | 2026-07-24 | 193.00 | 2026-08-14 | 190.39 | -1.35% | +5.06% | -6.42% | Miss | `IN_CI` | rank 247/511 |
| RTX | `EQUITY_ALPHA` | 2026-07-24 | 212.79 | 2026-08-14 | 222.97 | +4.78% | +5.06% | -0.28% | Miss | `IN_CI` | rank 92/511 |
| SJM | `EQUITY_ALPHA` | 2026-07-24 | 118.32 | 2026-08-14 | 121.39 | +2.59% | +5.06% | -2.47% | Miss | `IN_CI` | rank 279/511 |
| TMO | `EQUITY_ALPHA` | 2026-07-24 | 568.26 | 2026-08-14 | 588.29 | +3.52% | +5.06% | -1.54% | Miss | `IN_CI` | rank 197/511 |
| TRV | `EQUITY_ALPHA` | 2026-07-24 | 387.26 | 2026-08-14 | 370.36 | -4.36% | +5.06% | -9.43% | Miss | `OUT_CI_LOW` | rank 271/511 |
| UNH | `EQUITY_ALPHA` | 2026-07-24 | 420.74 | 2026-08-14 | 401.73 | -4.52% | +5.06% | -9.58% | Miss | `IN_CI` | rank 272/511 |
| UNP | `EQUITY_ALPHA` | 2026-07-24 | 307.32 | 2026-08-14 | 293.68 | -4.44% | +5.06% | -9.50% | Miss | `OUT_CI_LOW` | rank 224/511 |
| VLO | `EQUITY_ALPHA` | 2026-07-24 | 302.50 | 2026-08-14 | 341.67 | +12.95% | +5.06% | +7.89% | Hit | `IN_CI` | rank 136/511 |
| QQQ | `MARKET_FORECAST` | 2026-07-24 | 684.23 | 2026-08-14 | 731.07 | +6.85% | N/A | N/A | Miss | `IN_CI` | not scored today |
| SOXX | `MARKET_FORECAST` | 2026-07-24 | 527.01 | 2026-08-14 | 550.42 | +4.44% | N/A | N/A | Miss | `IN_CI` | not scored today |
| SPY | `MARKET_FORECAST` | 2026-07-24 | 738.93 | 2026-08-14 | 776.34 | +5.06% | N/A | N/A | N/A - FLAT_CALL | `OUT_CI_HIGH` | not scored today |

**Window summary.** SPY ran +5.06% from 738.93 to
776.34 over the 21-day window. The baseline's 26-name
book returned **+1.19%** on average — positive in absolute terms but
**-3.87% of alpha**, with a hit rate of **11.5%**
(3 of 26). CI coverage was
76.9%, inside the healthy band — the *magnitude* model was calibrated
while the *direction* model was not.

This is the rank-order inversion the system has been diagnosing since 2026-07-22, showing up
again out-of-sample: the book captured about a quarter of the market's move while carrying
full single-name risk. With `Tech_Z` supplying 66.7% of live conviction and
being pure trend-persistence, the leaderboard systematically ranks recent winners first, and
those lag in a broad advance led by names the screen had already de-ranked.

## 3. Theme-Level Performance

| Theme (baseline) | Status | Evidence |
|---|---|---|
| Defensive / low-beta tilt | **Failed** | the baseline book's mean alpha was -3.87% in a +5.06% tape; low-beta names cannot keep pace in a broad advance |
| Momentum persistence (`Tech_Z` leadership) | **Failed** | hit rate 11.5%; ranking on trailing 20/60d momentum did not predict forward 21d alpha |
| Volatility contraction (`vol_stability`) | **Partial** | realized vol did keep falling (SPY 30d RVol 4.37% → 3.55%), so the signal read the vol path correctly; it simply carried no alpha information |
| Core ETF top-down view | **Failed** | `HIGH_VOL` regime priors (SPY 0.00%, QQQ -1.00%, SOXX -1.50%) against realized SPY +5.06%, QQQ +6.85%, SOXX +4.44% |

## 4. Regime Shift Assessment

| Field | Baseline 2026-07-24 | This run 2026-08-14 | Implication |
|---|---|---|---|
| Regime | `HIGH_VOL` | **`BULL`** | SPY prior mu 0.00% → +2.00% |
| SPY vs MA20 / MA50 | below / mixed | **ABOVE / ABOVE** | trend restored |
| SPY 30d realized vol | elevated | **3.55%** (FALLING from 4.37%) | vol compression |
| VIX | elevated | **14.25** | below its 30d mean; calm tape |
| SOXX vs MA50 | below | **BELOW** | semis still the laggard |

**Factor-weight implication.** The regime shift argues for *less* defensive tilt, but family
weights are protected and `Fund_Z`/`Sent_Z` remain unavailable, so no weight change is made
here. The regime enters the run only through the Core ETF mu prior (`L023`) and the
interpretation of `Macro_Z`, exactly as specified.

## 5. Carry-Forward Decisions

Ranks are re-read from this run's `run_computed_manifest.json`, not transcribed.

| Ticker | Prior Score | Prior Thesis | MoM Return | Alpha | Decision | Rationale |
|---|---|---|---|---|---|---|
| BAC | +0.1692 | Finance: low/negative-beta defensive outperforming a flat index during | +3.93% | -1.13% | **CARRY** | re-ranks #11/511 on today's cross-section |
| BNY | +0.1962 | Finance: low/negative-beta defensive outperforming a flat index during | +2.72% | -2.34% | **CARRY** | re-ranks #20/511 on today's cross-section |
| JPM | +0.1674 | Finance: low/negative-beta defensive outperforming a flat index during | +2.73% | -2.34% | **DOWNGRADE** | falls to #54/511 (pctl 89.61) — above the 60th-pctl ranking floor but outside the published set |
| GD | +0.2337 | Industrials: low/negative-beta defensive outperforming a flat index du | +2.33% | -2.73% | **DOWNGRADE** | falls to #57/511 (pctl 89.02) — above the 60th-pctl ranking floor but outside the published set |
| LMT | +0.2155 | Industrials: low/negative-beta defensive outperforming a flat index du | +4.48% | -0.59% | **DOWNGRADE** | falls to #58/511 (pctl 88.82) — above the 60th-pctl ranking floor but outside the published set |
| MPC | +0.2224 | Energy: low/negative-beta defensive outperforming a flat index during  | +14.93% | +9.87% | **DOWNGRADE** | falls to #69/511 (pctl 86.67) — above the 60th-pctl ranking floor but outside the published set |
| MET | +0.1878 | Finance: low/negative-beta defensive outperforming a flat index during | +2.98% | -2.08% | **DOWNGRADE** | falls to #83/511 (pctl 83.92) — above the 60th-pctl ranking floor but outside the published set |
| RTX | +0.2598 | Industrials: low/negative-beta defensive outperforming a flat index du | +4.78% | -0.28% | **DOWNGRADE** | falls to #92/511 (pctl 82.16) — above the 60th-pctl ranking floor but outside the published set |
| MTB | +0.1881 | Finance: low/negative-beta defensive outperforming a flat index during | +1.80% | -3.26% | **DOWNGRADE** | falls to #107/511 (pctl 79.22) — above the 60th-pctl ranking floor but outside the published set |
| PKG | +0.2063 | Consumer Discretionary: low/negative-beta defensive outperforming a fl | +0.43% | -4.63% | **DOWNGRADE** | falls to #112/511 (pctl 78.24) — above the 60th-pctl ranking floor but outside the published set |
| LLY | +0.1190 | sector UNAVAILABLE: low/negative-beta defensive outperforming a flat i | -1.33% | -6.39% | **DOWNGRADE** | falls to #134/511 (pctl 73.92) — above the 60th-pctl ranking floor but outside the published set |
| VLO | +0.1887 | Energy: low/negative-beta defensive outperforming a flat index during  | +12.95% | +7.89% | **DOWNGRADE** | falls to #136/511 (pctl 73.53) — above the 60th-pctl ranking floor but outside the published set |
| DGX | +0.3028 | Health Care: low/negative-beta defensive outperforming a flat index du | +2.87% | -2.19% | **DOWNGRADE** | falls to #164/511 (pctl 68.04) — above the 60th-pctl ranking floor but outside the published set |
| TMO | +0.2025 | Industrials: low/negative-beta defensive outperforming a flat index du | +3.52% | -1.54% | **DOWNGRADE** | falls to #197/511 (pctl 61.57) — above the 60th-pctl ranking floor but outside the published set |
| PAYX | +0.3037 | Industrials: low/negative-beta defensive outperforming a flat index du | +7.46% | +2.40% | **DROP** | falls below the 60th-pctl ranking floor (#209/511) |
| UNP | +0.2991 | Industrials: low/negative-beta defensive outperforming a flat index du | -4.44% | -9.50% | **DROP** | falls below the 60th-pctl ranking floor (#224/511) |
| PCG | +0.2798 | Utilities: low/negative-beta defensive outperforming a flat index duri | -0.06% | -5.12% | **DROP** | falls below the 60th-pctl ranking floor (#230/511) |
| PM | +0.2272 | sector UNAVAILABLE: low/negative-beta defensive outperforming a flat i | -1.35% | -6.42% | **DROP** | falls below the 60th-pctl ranking floor (#247/511) |
| HIG | +0.1811 | Finance: low/negative-beta defensive outperforming a flat index during | -1.79% | -6.85% | **DROP** | falls below the 60th-pctl ranking floor (#263/511) |
| NSC | +0.2571 | Industrials: low/negative-beta defensive outperforming a flat index du | -4.63% | -9.70% | **DROP** | falls below the 60th-pctl ranking floor (#264/511) |
| TRV | +0.3680 | Finance: low/negative-beta defensive outperforming a flat index during | -4.36% | -9.43% | **DROP** | falls below the 60th-pctl ranking floor (#271/511) |
| UNH | +0.1263 | Health Care: low/negative-beta defensive outperforming a flat index du | -4.52% | -9.58% | **DROP** | falls below the 60th-pctl ranking floor (#272/511) |
| SJM | +0.1974 | Consumer Staples: low/negative-beta defensive outperforming a flat ind | +2.59% | -2.47% | **DROP** | falls below the 60th-pctl ranking floor (#279/511) |
| CSX | +0.2315 | Industrials: low/negative-beta defensive outperforming a flat index du | -5.77% | -10.83% | **DROP** | falls below the 60th-pctl ranking floor (#307/511) |
| CTAS | +0.2279 | sector UNAVAILABLE: low/negative-beta defensive outperforming a flat i | -3.10% | -8.17% | **DROP** | falls below the 60th-pctl ranking floor (#314/511) |
| AAPL | +0.1271 | sector UNAVAILABLE: low/negative-beta defensive outperforming a flat i | -8.13% | -13.20% | **DROP** | falls below the 60th-pctl ranking floor (#402/511) |

**Summary: 2 `CARRY`, 12 `DOWNGRADE`, 12 `DROP`.** `DOWNGRADE` names remain in
the scored universe and stay eligible to re-rank; `DROP` names fall below the 60th-percentile
ranking floor and appear only in the rejection log. No carry-forward decision is binding on an
investable set this run, because there is no investable set.

## 6. Sign-Off

| Field | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (basis-date closes, fetched this run) |
| Prices grounded | 137/137 checks, max deviation 0.000000% |
| Reflection confidence | **HIGH** |
| Rationale | Every MoM and settlement price is grounded across 2–3 independent vendors at zero deviation; the baseline was selected by the deterministic Step-2 algorithm with no gap flag and no tie; all 149 due keys settled with zero conflicts and zero skips. |

**Structural issues found this run**

1. **Three trading days have no package from any model** — 2026-08-11, 2026-08-12 and
   2026-08-13. `runbook.md § Cadence` says there should be no skipped days in the audit trail.
   They are **not** backfilled: doing so would require creating retroactive `OPEN` prediction
   records, which the system forbids. Recorded in `13` and `14`.
2. **The constituent caches are 54 days stale** and now contain a delisted name (`EA`).
   Detected and excluded, but cache refresh is overdue.
3. **`MARKET_FORECAST` CI coverage is above the 85% band** (88.67%) —
   intervals are uninformatively wide. Track A, `DEFER`red at `eff_n = 2`.
