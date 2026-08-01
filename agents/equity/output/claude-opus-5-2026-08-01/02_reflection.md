# 02 — Reflection — 2026-08-01

Standalone month-over-month reflection. Every price, return and regime claim cites `01`
ledger rows or is marked `UNAVAILABLE`. Reflection completed **before** any scoring.

## 0. Prediction Settlement

Ledgers scanned: **every** `agents/equity/output/*/15_predictions.json` across all models,
normalized through `settlement_ledger.py` (the single canonical normalizer per
`rules.md § Canonical Settlement Ledger`).

| Field | Value |
|---|---|
| Due keys found (`--as-of 2026-08-01`) | **107** |
| Settled this run | **107** (92 `EQUITY_ALPHA`, 15 `MARKET_FORECAST`) |
| Unsettleable | **0** |
| Due inventory after re-run | **0** |
| Conflicts | **0** |
| Settlement price | 2026-07-31 close (raw, unadjusted — matches the entry-price basis) |
| SPY settle close | 747.03 |

### Settlement timing

The due inventory split cleanly into two cohorts, both settling at the same 2026-07-31 close:

| Timing flag | Keys | Vintage | Target date | Rule |
|---|---|---|---|---|
| `ORDINARY` | 58 | 2026-07-03 | 2026-07-31 (Friday) | target-date close exists at run time and was used |
| `WEEKEND_TARGET` | 49 | 2026-07-04 | 2026-08-01 (Saturday) | not a trading day → last completed close at or before target |

Neither `TARGET_EQ_RUN_DATE` nor `TARGET_DATE_CLOSE` applies: 2026-08-01 is not a trading day, so
there is no same-day close to contest. `settlement_ledger.py` re-validated all
784 historical candidate rows and accepted these
107 with **0** conflicts.

### This run's settled batch

| Ticker | Vintage | Model | Entry | Settle | Target Date | Timing | mu | Realized | SPY Ret | Alpha | Direction | CI | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 2026-07-03 | claude-fable-5 | 261.07 | 250.94 | 2026-07-31 | `ORDINARY` | +3.00% | -3.88% | +0.30% | -4.18% | **MISS** | `IN_CI` | -0.730 |
| AMAT | 2026-07-03 | claude-sonnet-5 | 650.91 | 507.67 | 2026-07-31 | `ORDINARY` | +6.00% | -22.01% | +0.17% | -22.18% | **MISS** | `OUT_CI_LOW` | -1.043 |
| AMAT | 2026-07-03 | gpt-5 | 603.04 | 507.67 | 2026-07-31 | `ORDINARY` | +6.00% | -15.81% | +0.30% | -16.12% | **MISS** | `IN_CI` | -0.813 |
| AMCR | 2026-07-03 | claude-fable-5 | 45.00 | 44.88 | 2026-07-31 | `ORDINARY` | +6.00% | -0.27% | +0.30% | -0.57% | **MISS** | `IN_CI` | -0.759 |
| AMD | 2026-07-03 | claude-sonnet-5 | 540.88 | 476.15 | 2026-07-31 | `ORDINARY` | +5.00% | -11.97% | +0.17% | -12.14% | **MISS** | `IN_CI` | -0.726 |
| AMD | 2026-07-03 | gpt-5 | 517.82 | 476.15 | 2026-07-31 | `ORDINARY` | +6.00% | -8.05% | +0.30% | -8.35% | **MISS** | `IN_CI` | -0.601 |
| ARM | 2026-07-03 | gpt-5 | 315.28 | 239.69 | 2026-07-31 | `ORDINARY` | +6.00% | -23.98% | +0.30% | -24.28% | **MISS** | `IN_CI` | -0.829 |
| BAX | 2026-07-03 | claude-fable-5 | 22.65 | 26.16 | 2026-07-31 | `ORDINARY` | +6.00% | +15.50% | +0.30% | +15.19% | **HIT** | `IN_CI` | +0.888 |
| BEN | 2026-07-03 | claude-fable-5 | 34.11 | 33.86 | 2026-07-31 | `ORDINARY` | +5.00% | -0.73% | +0.30% | -1.03% | **MISS** | `IN_CI` | -0.696 |
| BXP | 2026-07-03 | claude-fable-5 | 69.32 | 70.12 | 2026-07-31 | `ORDINARY` | +5.00% | +1.15% | +0.30% | +0.85% | **HIT** | `IN_CI` | -0.475 |
| CAT | 2026-07-03 | claude-sonnet-5 | 991.41 | 814.81 | 2026-07-31 | `ORDINARY` | +1.00% | -17.81% | +0.17% | -17.98% | **MISS** | `OUT_CI_LOW` | -1.215 |
| CCEP | 2026-07-03 | claude-fable-5 | 106.61 | 109.46 | 2026-07-31 | `ORDINARY` | +6.00% | +2.67% | +0.30% | +2.37% | **HIT** | `IN_CI` | -0.443 |
| CRL | 2026-07-03 | claude-fable-5 | 230.69 | 232.51 | 2026-07-31 | `ORDINARY` | +5.00% | +0.79% | +0.30% | +0.49% | **HIT** | `IN_CI` | -0.296 |
| DDOG | 2026-07-03 | claude-sonnet-5 | 264.48 | 267.97 | 2026-07-31 | `ORDINARY` | +1.00% | +1.32% | +0.17% | +1.15% | **HIT** | `IN_CI` | +0.017 |
| DDOG | 2026-07-03 | gpt-5 | 260.36 | 267.97 | 2026-07-31 | `ORDINARY` | +6.00% | +2.92% | +0.30% | +2.62% | **HIT** | `IN_CI` | -0.167 |
| DELL | 2026-07-03 | claude-sonnet-5 | 425.25 | 405.37 | 2026-07-31 | `ORDINARY` | +2.00% | -4.67% | +0.17% | -4.85% | **MISS** | `IN_CI` | -0.188 |
| DELL | 2026-07-03 | gpt-5 | 394.32 | 405.37 | 2026-07-31 | `ORDINARY` | +6.00% | +2.80% | +0.30% | +2.50% | **HIT** | `IN_CI` | -0.090 |
| DOC | 2026-07-03 | claude-fable-5 | 21.89 | 21.83 | 2026-07-31 | `ORDINARY` | +6.00% | -0.27% | +0.30% | -0.58% | **MISS** | `IN_CI` | -0.786 |
| DVA | 2026-07-03 | claude-fable-5 | 234.91 | 240.09 | 2026-07-31 | `ORDINARY` | +5.00% | +2.21% | +0.30% | +1.90% | **HIT** | `IN_CI` | -0.400 |
| FFIV | 2026-07-03 | claude-fable-5 | 408.14 | 402.57 | 2026-07-31 | `ORDINARY` | +6.00% | -1.36% | +0.30% | -1.67% | **MISS** | `IN_CI` | -0.853 |
| FLEX | 2026-07-03 | claude-sonnet-5 | 153.53 | 113.75 | 2026-07-31 | `ORDINARY` | +2.00% | -25.91% | +0.17% | -26.08% | **MISS** | `OUT_CI_LOW` | -1.223 |
| HSIC | 2026-07-03 | claude-fable-5 | 86.43 | 85.75 | 2026-07-31 | `ORDINARY` | +6.00% | -0.79% | +0.30% | -1.09% | **MISS** | `OUT_CI_LOW` | -1.172 |
| HUM | 2026-07-03 | claude-fable-5 | 396.75 | 363.86 | 2026-07-31 | `ORDINARY` | +5.00% | -8.29% | +0.30% | -8.59% | **MISS** | `OUT_CI_LOW` | -1.165 |
| HUM | 2026-07-03 | claude-sonnet-5 | 409.42 | 363.86 | 2026-07-31 | `ORDINARY` | +1.00% | -11.13% | +0.17% | -11.30% | **MISS** | `OUT_CI_LOW` | -1.063 |
| HUM | 2026-07-03 | gpt-5 | 396.75 | 363.86 | 2026-07-31 | `ORDINARY` | +6.00% | -8.29% | +0.30% | -8.59% | **MISS** | `OUT_CI_LOW` | -1.253 |
| INTC | 2026-07-03 | claude-sonnet-5 | 127.02 | 90.20 | 2026-07-31 | `ORDINARY` | +6.00% | -28.99% | +0.17% | -29.16% | **MISS** | `OUT_CI_LOW` | -1.333 |
| INTC | 2026-07-03 | gpt-5 | 120.35 | 90.20 | 2026-07-31 | `ORDINARY` | +6.00% | -25.05% | +0.30% | -25.35% | **MISS** | `OUT_CI_LOW` | -1.183 |
| KDP | 2026-07-03 | claude-fable-5 | 33.30 | 31.12 | 2026-07-31 | `ORDINARY` | +6.00% | -6.55% | +0.30% | -6.85% | **MISS** | `OUT_CI_LOW` | -1.864 |
| LII | 2026-07-03 | claude-fable-5 | 570.03 | 415.88 | 2026-07-31 | `ORDINARY` | +6.00% | -27.04% | +0.30% | -27.34% | **MISS** | `OUT_CI_LOW` | -3.193 |
| LIN | 2026-07-03 | claude-fable-5 | 546.64 | 478.38 | 2026-07-31 | `ORDINARY` | +3.00% | -12.49% | +0.30% | -12.79% | **MISS** | `OUT_CI_LOW` | -2.599 |
| LLY | 2026-07-03 | claude-fable-5 | 1213.91 | 1148.84 | 2026-07-31 | `ORDINARY` | +4.00% | -5.36% | +0.30% | -5.66% | **MISS** | `IN_CI` | -0.954 |
| MAS | 2026-07-03 | claude-fable-5 | 82.77 | 71.48 | 2026-07-31 | `ORDINARY` | +5.00% | -13.64% | +0.30% | -13.94% | **MISS** | `OUT_CI_LOW` | -2.013 |
| MNST | 2026-07-03 | claude-fable-5 | 97.60 | 96.38 | 2026-07-31 | `ORDINARY` | +5.00% | -1.25% | +0.30% | -1.55% | **MISS** | `OUT_CI_LOW` | -1.330 |
| MRNA | 2026-07-03 | claude-fable-5 | 79.76 | 54.82 | 2026-07-31 | `ORDINARY` | +5.00% | -31.27% | +0.30% | -31.57% | **MISS** | `OUT_CI_LOW` | -1.614 |
| MRNA | 2026-07-03 | claude-sonnet-5 | 72.50 | 54.82 | 2026-07-31 | `ORDINARY` | +2.00% | -24.39% | +0.17% | -24.56% | **MISS** | `OUT_CI_LOW` | -1.174 |
| MRNA | 2026-07-03 | gpt-5 | 79.76 | 54.82 | 2026-07-31 | `ORDINARY` | +6.00% | -31.27% | +0.30% | -31.57% | **MISS** | `OUT_CI_LOW` | -1.658 |
| MRVL | 2026-07-03 | claude-sonnet-5 | 272.05 | 187.56 | 2026-07-31 | `ORDINARY` | +3.00% | -31.06% | +0.17% | -31.23% | **MISS** | `IN_CI` | -0.815 |
| MRVL | 2026-07-03 | gpt-5 | 245.29 | 187.56 | 2026-07-31 | `ORDINARY` | +6.00% | -23.54% | +0.30% | -23.84% | **MISS** | `IN_CI` | -0.707 |
| MU | 2026-07-03 | claude-sonnet-5 | 1032.28 | 823.03 | 2026-07-31 | `ORDINARY` | +4.00% | -20.27% | +0.17% | -20.44% | **MISS** | `IN_CI` | -0.666 |
| MU | 2026-07-03 | gpt-5 | 975.56 | 823.03 | 2026-07-31 | `ORDINARY` | +6.00% | -15.64% | +0.30% | -15.94% | **MISS** | `IN_CI` | -0.594 |
| PANW | 2026-07-03 | claude-fable-5 | 348.06 | 331.83 | 2026-07-31 | `ORDINARY` | +5.00% | -4.66% | +0.30% | -4.97% | **MISS** | `IN_CI` | -0.599 |
| PANW | 2026-07-03 | claude-sonnet-5 | 352.04 | 331.83 | 2026-07-31 | `ORDINARY` | +4.00% | -5.74% | +0.17% | -5.91% | **MISS** | `IN_CI` | -0.604 |
| PANW | 2026-07-03 | gpt-5 | 348.06 | 331.83 | 2026-07-31 | `ORDINARY` | +6.00% | -4.66% | +0.30% | -4.97% | **MISS** | `IN_CI` | -0.661 |
| SNDK | 2026-07-03 | gpt-5 | 1745.00 | 1214.83 | 2026-07-31 | `ORDINARY` | +6.00% | -30.38% | +0.30% | -30.68% | **MISS** | `IN_CI` | -0.934 |
| STX | 2026-07-03 | gpt-5 | 820.16 | 855.91 | 2026-07-31 | `ORDINARY` | +6.00% | +4.36% | +0.30% | +4.06% | **HIT** | `IN_CI` | -0.067 |
| SWK | 2026-07-03 | claude-fable-5 | 91.90 | 94.58 | 2026-07-31 | `ORDINARY` | +6.00% | +2.92% | +0.30% | +2.61% | **HIT** | `IN_CI` | -0.265 |
| URI | 2026-07-03 | claude-fable-5 | 1098.59 | 1079.26 | 2026-07-31 | `ORDINARY` | +6.00% | -1.76% | +0.30% | -2.06% | **MISS** | `IN_CI` | -0.795 |
| WDC | 2026-07-03 | gpt-5 | 539.00 | 544.48 | 2026-07-31 | `ORDINARY` | +6.00% | +1.02% | +0.30% | +0.71% | **HIT** | `IN_CI` | -0.163 |
| WST | 2026-07-03 | claude-fable-5 | 365.74 | 340.96 | 2026-07-31 | `ORDINARY` | +5.00% | -6.78% | +0.30% | -7.08% | **MISS** | `OUT_CI_LOW` | -1.692 |
| ABBV | 2026-07-04 | claude-fable-5 | 261.07 | 250.94 | 2026-08-01 | `WEEKEND_TARGET` | +3.00% | -3.88% | +0.30% | -4.18% | **MISS** | `IN_CI` | -0.730 |
| ABNB | 2026-07-04 | claude-fable-5 | 148.93 | 151.52 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +1.74% | +0.30% | +1.44% | **HIT** | `IN_CI` | -0.452 |
| AMAT | 2026-07-04 | gpt-5 | 603.04 | 507.67 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -15.81% | +0.30% | -16.12% | **MISS** | `IN_CI` | -0.813 |
| AMCR | 2026-07-04 | claude-fable-5 | 45.00 | 44.88 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -0.27% | +0.30% | -0.57% | **MISS** | `IN_CI` | -0.759 |
| AMD | 2026-07-04 | gpt-5 | 517.82 | 476.15 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -8.05% | +0.30% | -8.35% | **MISS** | `IN_CI` | -0.601 |
| ARM | 2026-07-04 | gpt-5 | 315.28 | 239.69 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -23.98% | +0.30% | -24.28% | **MISS** | `IN_CI` | -0.829 |
| BAX | 2026-07-04 | claude-fable-5 | 22.65 | 26.16 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +15.50% | +0.30% | +15.19% | **HIT** | `IN_CI` | +0.888 |
| BEN | 2026-07-04 | claude-fable-5 | 34.11 | 33.86 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -0.73% | +0.30% | -1.03% | **MISS** | `IN_CI` | -0.696 |
| CCEP | 2026-07-04 | claude-fable-5 | 106.61 | 109.46 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +2.67% | +0.30% | +2.37% | **HIT** | `IN_CI` | -0.443 |
| CNC | 2026-07-04 | gpt-5 | 67.86 | 62.22 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -8.31% | +0.30% | -8.61% | **MISS** | `OUT_CI_LOW` | -1.159 |
| CRWD | 2026-07-04 | gpt-5 | 193.98 | 190.86 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -1.61% | +0.30% | -1.91% | **MISS** | `IN_CI` | -0.467 |
| DDOG | 2026-07-04 | gpt-5 | 260.36 | 267.97 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +2.92% | +0.30% | +2.62% | **HIT** | `IN_CI` | -0.167 |
| DELL | 2026-07-04 | gpt-5 | 394.32 | 405.37 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +2.80% | +0.30% | +2.50% | **HIT** | `IN_CI` | -0.090 |
| DOC | 2026-07-04 | claude-fable-5 | 21.89 | 21.83 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -0.27% | +0.30% | -0.58% | **MISS** | `IN_CI` | -0.786 |
| DVA | 2026-07-04 | claude-fable-5 | 234.91 | 240.09 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | +2.21% | +0.30% | +1.90% | **HIT** | `IN_CI` | -0.400 |
| FFIV | 2026-07-04 | claude-fable-5 | 408.14 | 402.57 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -1.36% | +0.30% | -1.67% | **MISS** | `IN_CI` | -0.853 |
| FLEX | 2026-07-04 | gpt-5 | 136.86 | 113.75 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -16.89% | +0.30% | -17.19% | **MISS** | `IN_CI` | -1.003 |
| HOOD | 2026-07-04 | gpt-5 | 112.73 | 86.56 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -23.21% | +0.30% | -23.52% | **MISS** | `OUT_CI_LOW` | -1.278 |
| HSIC | 2026-07-04 | claude-fable-5 | 86.43 | 85.75 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -0.79% | +0.30% | -1.09% | **MISS** | `OUT_CI_LOW` | -1.172 |
| HUM | 2026-07-04 | claude-fable-5 | 396.75 | 363.86 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -8.29% | +0.30% | -8.59% | **MISS** | `OUT_CI_LOW` | -1.165 |
| HUM | 2026-07-04 | gpt-5 | 396.75 | 363.86 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -8.29% | +0.30% | -8.59% | **MISS** | `OUT_CI_LOW` | -1.253 |
| IFF | 2026-07-04 | claude-fable-5 | 83.83 | 79.22 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -5.50% | +0.30% | -5.80% | **MISS** | `OUT_CI_LOW` | -1.269 |
| INTC | 2026-07-04 | gpt-5 | 120.35 | 90.20 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -25.05% | +0.30% | -25.35% | **MISS** | `OUT_CI_LOW` | -1.183 |
| KDP | 2026-07-04 | claude-fable-5 | 33.30 | 31.12 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -6.55% | +0.30% | -6.85% | **MISS** | `OUT_CI_LOW` | -1.864 |
| KLAC | 2026-07-04 | gpt-5 | 235.55 | 182.82 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -22.39% | +0.30% | -22.69% | **MISS** | `IN_CI` | -0.943 |
| LIN | 2026-07-04 | claude-fable-5 | 546.64 | 478.38 | 2026-08-01 | `WEEKEND_TARGET` | +4.00% | -12.49% | +0.30% | -12.79% | **MISS** | `OUT_CI_LOW` | -2.766 |
| LLY | 2026-07-04 | claude-fable-5 | 1213.91 | 1148.84 | 2026-08-01 | `WEEKEND_TARGET` | +4.00% | -5.36% | +0.30% | -5.66% | **MISS** | `IN_CI` | -0.954 |
| LRCX | 2026-07-04 | gpt-5 | 351.41 | 293.15 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -16.58% | +0.30% | -16.88% | **MISS** | `IN_CI` | -0.842 |
| LYV | 2026-07-04 | claude-fable-5 | 186.59 | 174.13 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -6.68% | +0.30% | -6.98% | **MISS** | `OUT_CI_LOW` | -1.966 |
| MAS | 2026-07-04 | claude-fable-5 | 82.77 | 71.48 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -13.64% | +0.30% | -13.94% | **MISS** | `OUT_CI_LOW` | -2.013 |
| MNST | 2026-07-04 | claude-fable-5 | 97.60 | 96.38 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -1.25% | +0.30% | -1.55% | **MISS** | `OUT_CI_LOW` | -1.330 |
| MRNA | 2026-07-04 | claude-fable-5 | 79.76 | 54.82 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -31.27% | +0.30% | -31.57% | **MISS** | `OUT_CI_LOW` | -1.614 |
| MRNA | 2026-07-04 | gpt-5 | 79.76 | 54.82 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -31.27% | +0.30% | -31.57% | **MISS** | `OUT_CI_LOW` | -1.658 |
| MRVL | 2026-07-04 | gpt-5 | 245.29 | 187.56 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -23.54% | +0.30% | -23.84% | **MISS** | `IN_CI` | -0.707 |
| MU | 2026-07-04 | gpt-5 | 975.56 | 823.03 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -15.64% | +0.30% | -15.94% | **MISS** | `IN_CI` | -0.594 |
| PANW | 2026-07-04 | claude-fable-5 | 348.06 | 331.83 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -4.66% | +0.30% | -4.97% | **MISS** | `IN_CI` | -0.599 |
| PANW | 2026-07-04 | gpt-5 | 348.06 | 331.83 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -4.66% | +0.30% | -4.97% | **MISS** | `IN_CI` | -0.661 |
| SNDK | 2026-07-04 | gpt-5 | 1745.00 | 1214.83 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | -30.38% | +0.30% | -30.68% | **MISS** | `IN_CI` | -0.934 |
| STX | 2026-07-04 | gpt-5 | 820.16 | 855.91 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +4.36% | +0.30% | +4.06% | **HIT** | `IN_CI` | -0.067 |
| SWK | 2026-07-04 | claude-fable-5 | 91.90 | 94.58 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +2.92% | +0.30% | +2.61% | **HIT** | `IN_CI` | -0.265 |
| VRTX | 2026-07-04 | claude-fable-5 | 528.04 | 477.10 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -9.65% | +0.30% | -9.95% | **MISS** | `OUT_CI_LOW` | -1.758 |
| WDC | 2026-07-04 | gpt-5 | 539.00 | 544.48 | 2026-08-01 | `WEEKEND_TARGET` | +6.00% | +1.02% | +0.30% | +0.71% | **HIT** | `IN_CI` | -0.163 |
| WST | 2026-07-04 | claude-fable-5 | 365.74 | 340.96 | 2026-08-01 | `WEEKEND_TARGET` | +5.00% | -6.78% | +0.30% | -7.08% | **MISS** | `OUT_CI_LOW` | -1.692 |
| QQQ | 2026-07-03 | claude-fable-5 | 712.60 | 687.99 | 2026-07-31 | `ORDINARY` | +0.29% | -3.45% | N/A | N/A | **N/A - FLAT_CALL** | `IN_CI` | -0.442 |
| QQQ | 2026-07-03 | claude-sonnet-5 | 725.17 | 687.99 | 2026-07-31 | `ORDINARY` | +3.20% | -5.13% | N/A | N/A | **MISS** | `IN_CI` | -0.983 |
| QQQ | 2026-07-03 | gpt-5 | 712.60 | 687.99 | 2026-07-31 | `ORDINARY` | +0.79% | -3.45% | N/A | N/A | **MISS** | `IN_CI` | -0.501 |
| SOXX | 2026-07-03 | claude-fable-5 | 566.32 | 504.89 | 2026-07-31 | `ORDINARY` | +0.14% | -10.85% | N/A | N/A | **N/A - FLAT_CALL** | `IN_CI` | -0.500 |
| SOXX | 2026-07-03 | claude-sonnet-5 | 599.70 | 504.89 | 2026-07-31 | `ORDINARY` | +5.00% | -15.81% | N/A | N/A | **MISS** | `IN_CI` | -0.948 |
| SOXX | 2026-07-03 | gpt-5 | 566.32 | 504.89 | 2026-07-31 | `ORDINARY` | +1.64% | -10.85% | N/A | N/A | **MISS** | `IN_CI` | -0.568 |
| SPY | 2026-07-03 | claude-fable-5 | 744.78 | 747.03 | 2026-07-31 | `ORDINARY` | +0.50% | +0.30% | N/A | N/A | **HIT** | `IN_CI` | -0.045 |
| SPY | 2026-07-03 | claude-sonnet-5 | 745.76 | 747.03 | 2026-07-31 | `ORDINARY` | +2.00% | +0.17% | N/A | N/A | **HIT** | `IN_CI` | -0.415 |
| SPY | 2026-07-03 | gpt-5 | 744.78 | 747.03 | 2026-07-31 | `ORDINARY` | +0.50% | +0.30% | N/A | N/A | **HIT** | `IN_CI` | -0.045 |
| QQQ | 2026-07-04 | claude-fable-5 | 712.60 | 687.99 | 2026-08-01 | `WEEKEND_TARGET` | +0.79% | -3.45% | N/A | N/A | **MISS** | `IN_CI` | -0.501 |
| QQQ | 2026-07-04 | gpt-5 | 712.60 | 687.99 | 2026-08-01 | `WEEKEND_TARGET` | +0.89% | -3.45% | N/A | N/A | **MISS** | `IN_CI` | -0.513 |
| SOXX | 2026-07-04 | claude-fable-5 | 566.32 | 504.89 | 2026-08-01 | `WEEKEND_TARGET` | +0.64% | -10.85% | N/A | N/A | **MISS** | `IN_CI` | -0.523 |
| SOXX | 2026-07-04 | gpt-5 | 566.32 | 504.89 | 2026-08-01 | `WEEKEND_TARGET` | +1.94% | -10.85% | N/A | N/A | **MISS** | `IN_CI` | -0.582 |
| SPY | 2026-07-04 | claude-fable-5 | 744.78 | 747.03 | 2026-08-01 | `WEEKEND_TARGET` | +0.50% | +0.30% | N/A | N/A | **HIT** | `IN_CI` | -0.045 |
| SPY | 2026-07-04 | gpt-5 | 744.78 | 747.03 | 2026-08-01 | `WEEKEND_TARGET` | +0.50% | +0.30% | N/A | N/A | **HIT** | `IN_CI` | -0.045 |

**Batch summary.** `EQUITY_ALPHA`: 20/92 direction hits = **21.7%**,
58/92 `IN_CI` = **63.0%**, mean z **-0.9090**,
mean realized alpha **-9.40%**. `MARKET_FORECAST`: 5/13 =
**38.5%**, 15/15 `IN_CI`,
mean z **-0.4438**. This is a **poor batch** — the equity hit rate is less
than half the >50% healthy bar and mean z is well outside the ±0.5 band, meaning realized
returns came in materially below the forecast mu.

### Rolling calibration (canonical, post-settlement)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range | Verdict |
|---|---|---|---|---|
| Raw `n` | 439 | 78 | ≥ 10 to report | OK |
| 28-day `eff_n` | **1** | **1** | ≥ 3 for Track A | **blocks Track A** |
| Hit rate | 42.37% | 20.27% | > 50% | **below** |
| CI coverage | 70.16% | 78.21% | 55–85% (target 70%) | **healthy** |
| Mean z | -0.4608 | -0.6633 | −0.5 … +0.5 | EQ marginal, MF **outside** |
| Rank IC (weighted mean) | **-0.1314** | n/a | > 0 | **negative** |

Rank IC is negative in **20 of 28** vintages. Two distinct failure modes
remain separable and must not be conflated (established 2026-07-26):

- **Magnitude calibration is broadly healthy** — CI coverage 70.16% sits
  essentially on the 70% target, so sigma sourcing is not the problem.
- **Rank-order inversion persists** — the composite ranks the wrong names first. A mu
  shrink or sigma widen is a *monotonic transform* and cannot fix a rank inversion; that
  standing proposal stays retired.

**Binding consequences for this run** (`agents.md § Calibration Feedback Binding`):
rank IC ≤ 0 over ≥ 20 settled records → **all confidence capped at `MEDIUM`**. CI coverage
is inside 55–85%, so the wider-sigma rule does **not** fire and sigma stays
`REALIZED_VOL_30D`.

**Track A eligibility: `INSUFFICIENT_EFFECTIVE_N`.** Both record types sit
at `eff_n` = 1. The `eff_n` projection says `EQUITY_ALPHA` increments to 2 on
**2026-08-05** (43 pending)
and `MARKET_FORECAST` on **2026-08-09**
(6 pending). Adding 92
equity settlements today moved raw `n` 347 → 439 but left `eff_n` at 1,
exactly as the startup-transient arithmetic predicts (target-date span is now
24d, still inside one 28-day window). The
2026-07-28 falsifiable claim **holds**.

## 1. Prior Run Summary — and the mandatory tie-break disclosure

MoM target **2026-07-04**, window 2026-06-17 … 2026-07-11,
40 in-window folders. The closest sit at |Δ| =
**0d**, and **2 folders tie** there. No
`claude-opus-5` folder exists in-window, so the baseline is cross-model:
flag **`CROSS_MODEL_BASELINE`**.

Rule 8 of `agents.md § Orchestrator Step 2` (implemented 2026-07-30) requires resolving the
tie deterministically **and reporting every tied candidate**:

| Folder | Same family | `15_predictions.json` | Settled n | Hit rate | Mean alpha | Mean z |
|---|---|---|---|---|---|---|
| `claude-fable-5-2026-07-04` **← selected** | yes | yes (26 records) | 23 | 21.7% | -0.0441 | -1.0721 |
| `gpt-5-2026-07-04` | no | yes (23 records) | 20 | 20.0% | -0.1353 | -0.7705 |

Selection: `claude-fable-5-2026-07-04` — same model family as the executing model claude-opus-5 (criterion (a), same model family).

**Is the MoM conclusion invariant across the tied books? Yes, this time.** The hit-rate
spread is **1.7pp** (20.0% vs 21.7%) and both books are
decisively poor; either choice supports the same conclusion — the 2026-07-04 vintage
underperformed badly on alpha regardless of which model's book is read. That is a materially
different situation from 2026-07-29 (48pp spread) and 2026-07-30 (40.7pp spread), where the
choice *did* determine the narrative. The rule earned its keep on those days; today it
confirms robustness instead. Both books are still reported rather than silently collapsed
into one.

Prior run (`claude-fable-5-2026-07-04`): status `NO_TRADE`-class monitoring package,
26 prediction records, of which
23 equity names carried settleable forecasts.

## 2. MoM Price & Return Table

Prior prices are the baseline package's own recorded `entry_price` values with their
recorded `price_date`; current prices are the 2026-07-31 raw closes from `01` ledger rows
`L-PX-*`. Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| BAX | 2026-07-02 | 22.65 | 2026-07-31 | 26.16 | +15.50% | +0.30% | +15.19% | **Hit** | `IN_CI` | — |
| SWK | 2026-07-02 | 91.90 | 2026-07-31 | 94.58 | +2.92% | +0.30% | +2.61% | **Hit** | `IN_CI` | — |
| CCEP | 2026-07-02 | 106.61 | 2026-07-31 | 109.46 | +2.67% | +0.30% | +2.37% | **Hit** | `IN_CI` | — |
| DVA | 2026-07-02 | 234.91 | 2026-07-31 | 240.09 | +2.21% | +0.30% | +1.90% | **Hit** | `IN_CI` | — |
| ABNB | 2026-07-02 | 148.93 | 2026-07-31 | 151.52 | +1.74% | +0.30% | +1.44% | **Hit** | `IN_CI` | — |
| AMCR | 2026-07-02 | 45.00 | 2026-07-31 | 44.88 | -0.27% | +0.30% | -0.57% | **Miss** | `IN_CI` | — |
| DOC | 2026-07-02 | 21.89 | 2026-07-31 | 21.83 | -0.27% | +0.30% | -0.58% | **Miss** | `IN_CI` | — |
| BEN | 2026-07-02 | 34.11 | 2026-07-31 | 33.86 | -0.73% | +0.30% | -1.04% | **Miss** | `IN_CI` | — |
| HSIC | 2026-07-02 | 86.43 | 2026-07-31 | 85.75 | -0.79% | +0.30% | -1.09% | **Miss** | `OUT_CI_LOW` | — |
| MNST | 2026-07-02 | 97.60 | 2026-07-31 | 96.38 | -1.25% | +0.30% | -1.55% | **Miss** | `OUT_CI_LOW` | — |
| FFIV | 2026-07-02 | 408.14 | 2026-07-31 | 402.57 | -1.36% | +0.30% | -1.67% | **Miss** | `IN_CI` | — |
| ABBV | 2026-07-02 | 261.07 | 2026-07-31 | 250.94 | -3.88% | +0.30% | -4.18% | **Miss** | `IN_CI` | — |
| PANW | 2026-07-02 | 348.06 | 2026-07-31 | 331.83 | -4.66% | +0.30% | -4.97% | **Miss** | `IN_CI` | — |
| LLY | 2026-07-02 | 1213.91 | 2026-07-31 | 1148.84 | -5.36% | +0.30% | -5.66% | **Miss** | `IN_CI` | — |
| IFF | 2026-07-02 | 83.83 | 2026-07-31 | 79.22 | -5.50% | +0.30% | -5.80% | **Miss** | `OUT_CI_LOW` | — |
| KDP | 2026-07-02 | 33.30 | 2026-07-31 | 31.12 | -6.55% | +0.30% | -6.85% | **Miss** | `OUT_CI_LOW` | — |
| LYV | 2026-07-02 | 186.59 | 2026-07-31 | 174.13 | -6.68% | +0.30% | -6.98% | **Miss** | `OUT_CI_LOW` | — |
| WST | 2026-07-02 | 365.74 | 2026-07-31 | 340.96 | -6.78% | +0.30% | -7.08% | **Miss** | `OUT_CI_LOW` | — |
| HUM | 2026-07-02 | 396.75 | 2026-07-31 | 363.86 | -8.29% | +0.30% | -8.59% | **Miss** | `OUT_CI_LOW` | — |
| VRTX | 2026-07-02 | 528.04 | 2026-07-31 | 477.10 | -9.65% | +0.30% | -9.95% | **Miss** | `OUT_CI_LOW` | — |
| LIN | 2026-07-02 | 546.64 | 2026-07-31 | 478.38 | -12.49% | +0.30% | -12.79% | **Miss** | `OUT_CI_LOW` | — |
| MAS | 2026-07-02 | 82.77 | 2026-07-31 | 71.48 | -13.64% | +0.30% | -13.94% | **Miss** | `OUT_CI_LOW` | — |
| MRNA | 2026-07-02 | 79.76 | 2026-07-31 | 54.82 | -31.27% | +0.30% | -31.57% | **Miss** | `OUT_CI_LOW` | — |

**Aggregate:** 5/23 =
**21.7%** alpha hits, mean alpha **-4.41%**, CI outcomes
{'IN_CI': 12, 'OUT_CI_LOW': 11}. SPY returned +0.30% over the same window.

## 3. Theme-Level Performance

| Prior theme | Evidence | Verdict |
|---|---|---|
| Momentum / relative-strength leadership | The baseline book was built on the same `Tech_Z`-dominant engine in use today; it produced 21.7% alpha hits and -4.41% mean alpha over 28 days | **FAILED** |
| Defensive tilt (Health Care / Staples) | Names in these sectors carried the book but did not generate positive alpha as a group | **FAILED** |
| Semiconductor exposure | SOXX-linked names were the worst contributors in the settled batch — SNDK, MRVL, MU, INTC all settled `MISS` | **FAILED** |
| Magnitude calibration (CI width) | 58/92 of this run's settled batch landed `IN_CI`; canonical coverage 70.16% | **VALIDATED** |

The pattern is consistent and now well-evidenced: **the intervals are the right width, the
ordering is wrong.** The system knows how uncertain it is; it does not know which names to
rank first.

## 4. Regime Shift Assessment

| | Baseline (2026-07-04) | Current (2026-07-31) |
|---|---|---|
| Regime | `NEUTRAL`-to-`BULL` (per baseline package) | **`BULL`** |
| SPY vs MA50 | — | ABOVE (747.03 vs 744.23) |
| SPY 60d momentum | — | +3.48% |
| VIX | — | 15.99 (20d ago 15.81, 60d mean 17.4117) |
| SPY 30d realized vol (ann.) | — | 12.73% vs prior 30d 14.69% → **falling** |

Factor-weight implication: the declared `BULL` regime with falling realized vol
and a sub-16 VIX would ordinarily favour beta and momentum exposure. **It changes nothing
here**, because family weights are fixed by `rules.md § Factor Architecture` and two of the
four families are `UNAVAILABLE` — there is no live weighting decision left to make. Recording
this explicitly so the regime call is not mistaken for a factor-tilt decision it cannot
drive.

## 5. Carry-Forward Decisions

Ranks and percentiles below are read programmatically out of `run_computed_manifest.json` —
never hand-transcribed. Decisions bind factor scoring where ledger-backed.

| Ticker | Prior Adj Score | Prior Thesis (abridged) | MoM Alpha | Current Rank | Current Pctl | Decision | Rationale |
|---|---|---|---|---|---|---|---|
| DVA | +0.4460 | Dialysis duopoly defensive; +57% 60d momentum on managed-care recovery | +1.90% | 48 | 90.7 | **CARRY** | still at/above the 80th pctl (rank 48, pctl 90.7) |
| PANW | +0.3662 | Cybersecurity platform consolidation momentum; +105% 60d leadership | -4.97% | 153 | 70.3 | **DOWNGRADE** | monitoring band only (rank 153, pctl 70.3) |
| DOC | +0.3354 | Healthcare REIT defensive yield; improving occupancy; low beta | -0.58% | 99 | 80.8 | **CARRY** | still at/above the 80th pctl (rank 99, pctl 80.8) |
| BEN | +0.3336 | Asset-manager torque to flows recovery; +43% 60d with cheap multiple | -1.04% | 14 | 97.4 | **CARRY** | still inside the published set at rank 14 |
| HUM | +0.3291 | Medicare Advantage margin-recovery leader; strongest 60d relative stre | -8.59% | 41 | 92.1 | **CARRY** | still at/above the 80th pctl (rank 41, pctl 92.1) |
| HSIC | +0.3034 | Dental/medical distribution defensive; 5.8% sigma among lowest in slee | -1.09% | 187 | 63.6 | **DOWNGRADE** | monitoring band only (rank 187, pctl 63.6) |
| MNST | +0.3031 | Energy-drink staples compounder; 4.7% sigma lowest in sleeve | -1.55% | 164 | 68.1 | **DOWNGRADE** | monitoring band only (rank 164, pctl 68.1) |
| MAS | +0.2975 | Housing-products cyclical; rare >1.25-beta name among rotation leaders | -13.94% | — | 21.2 | **DROP** | fell below the 60th-pctl rank floor (pctl 21.2) |
| BAX | +0.2969 | Med-tech turnaround; divestiture-simplified story | +15.19% | 4 | 99.3 | **CARRY** | still inside the published set at rank 4 |
| VRTX | +0.2947 | CF franchise durability plus pain-franchise optionality; defensive bio | -9.95% | — | 31.9 | **DROP** | fell below the 60th-pctl rank floor (pctl 31.9) |
| CCEP | +0.2936 | European bottler defensive; monthly MACD bullish cross | +2.37% | 129 | 75.0 | **DOWNGRADE** | monitoring band only (rank 129, pctl 75.0) |
| SWK | +0.2854 | Toolmaker turnaround leverage; highest beta (1.53) in the leader set | +2.61% | 63 | 87.8 | **CARRY** | still at/above the 80th pctl (rank 63, pctl 87.8) |
| MRNA | +0.2844 | +63% 20d squeeze off a multi-year base; pipeline re-rate momentum | -31.57% | — | 23.9 | **DROP** | fell below the 60th-pctl rank floor (pctl 23.9) |
| LYV | +0.2836 | Live-events demand compounder; low-vol uptrend with shallow drawdowns | -6.98% | 111 | 78.5 | **DOWNGRADE** | monitoring band only (rank 111, pctl 78.5) |
| AMCR | +0.2669 | Defensive packaging re-rate +19% 20d; beta 1.26 rare among defensives | -0.57% | 119 | 76.9 | **DOWNGRADE** | monitoring band only (rank 119, pctl 76.9) |
| WST | +0.2637 | Injectable-drug components (GLP-1 fill-finish adjacency); low-beta pha | -7.08% | 156 | 69.7 | **DOWNGRADE** | monitoring band only (rank 156, pctl 69.7) |
| ABNB | +0.2570 | Travel platform share-gainer; steady accumulation above rising MAs | +1.44% | — | 49.4 | **DROP** | fell below the 60th-pctl rank floor (pctl 49.4) |
| KDP | +0.2499 | Staples compounder; negative beta with steady accumulation | -6.85% | — | 29.5 | **DROP** | fell below the 60th-pctl rank floor (pctl 29.5) |
| FFIV | +0.2476 | App-delivery/security hybrid-infra demand; low-vol compounder | -1.67% | 177 | 65.6 | **DOWNGRADE** | monitoring band only (rank 177, pctl 65.6) |
| IFF | +0.2470 | Specialty-ingredients recovery; high-beta quality laggard catch-up | -5.80% | — | 48.1 | **DROP** | fell below the 60th-pctl rank floor (pctl 48.1) |
| LLY | +0.2243 | CARRY (+4.4pp interim alpha); GLP-1 defensive growth, 93.6 pctl | -5.66% | — | 54.3 | **DROP** | fell below the 60th-pctl rank floor (pctl 54.3) |
| ABBV | +0.1935 | CARRY (+13.4pp interim alpha, best in prior book); immunology momentum | -4.18% | 121 | 76.5 | **DOWNGRADE** | monitoring band only (rank 121, pctl 76.5) |
| LIN | +0.1810 | CARRY (+5.1pp interim alpha); industrial-gas compounder, 86.0 pctl | -12.79% | — | 30.3 | **DROP** | fell below the 60th-pctl rank floor (pctl 30.3) |

**Summary:** {'CARRY': 6, 'DOWNGRADE': 9, 'DROP': 8}. `DROP` names stay out of today's scored set absent new ledger
evidence; none were re-admitted.

## 6. Sign-Off

| Field | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (2026-07-31 close), grounded on 3 independent sources |
| Reflection confidence | **MEDIUM** |
| Confidence rationale | Settlement inputs are fully grounded and the ledger is conflict-free (0 conflicts, 0 due remaining), so the arithmetic is trustworthy. Capped below HIGH because `eff_n` = 1 means all 439 settled records still represent a single overlapping 28-day window — the sample is numerically large and statistically thin. |
| Structural issues found | (1) Rank-order inversion persists — rank IC -0.1314 over n=439. (2) `Fund_Z`/`Sent_Z` remain `UNAVAILABLE`, forcing `NO_TRADE` independent of market state. (3) **New this run:** `rs20`/`rs60` are constant shifts of `mom20`/`mom60`, so their z-scores are numerically identical and `Tech_Z` double-counts momentum — see `13`. |
