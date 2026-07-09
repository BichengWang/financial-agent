# 02 Reflection

## 0. Prediction Settlement

29 matured predictions settled during this run; equity hit rate 13/29 and CI coverage 21/29.

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MCK | claude-fable-5-2026-06-10 | 790.22 | 2026-07-08 | 0.06 | -0.000557 | 0.031333 | -0.03189 | MISS | IN_CI | -0.933078 |
| COST | claude-fable-5-2026-06-10 | 980.45 | 2026-07-08 | 0.06 | -0.070667 | 0.031333 | -0.101999 | MISS | OUT_CI_LOW | -1.68168 |
| WMT | claude-fable-5-2026-06-10 | 119.83 | 2026-07-08 | 0.05 | -0.067512 | 0.031333 | -0.098845 | MISS | OUT_CI_LOW | -1.182217 |
| CVX | claude-fable-5-2026-06-10 | 191.01 | 2026-07-08 | 0.05 | -0.087901 | 0.031333 | -0.119234 | MISS | OUT_CI_LOW | -1.894247 |
| UNH | claude-fable-5-2026-06-10 | 407.13 | 2026-07-08 | 0.04 | 0.058581 | 0.031333 | 0.027248 | HIT | IN_CI | 0.224677 |
| MU | claude-fable-5-2026-06-10 | 891.66 | 2026-07-08 | 0.01 | 0.137194 | 0.031333 | 0.105861 | HIT | IN_CI | 0.434701 |
| XOM | claude-fable-5-2026-06-10 | 151.35 | 2026-07-08 | 0.02 | -0.090188 | 0.031333 | -0.121521 | MISS | OUT_CI_LOW | -1.26799 |
| LIN | claude-fable-5-2026-06-10 | 509.2 | 2026-07-08 | 0.02 | 0.029222 | 0.031333 | -0.00211 | MISS | IN_CI | 0.146619 |
| LLY | claude-fable-5-2026-06-10 | 1138.16 | 2026-07-08 | 0.02 | 0.064697 | 0.031333 | 0.033364 | HIT | IN_CI | 0.405595 |
| NVDA | claude-fable-5-2026-06-10 | 201.65 | 2026-07-08 | 0.01 | 0.010513 | 0.031333 | -0.02082 | MISS | IN_CI | 0.00431 |
| GOOGL | claude-fable-5-2026-06-10 | 356.64 | 2026-07-08 | 0.01 | 2.8e-05 | 0.031333 | -0.031305 | MISS | IN_CI | -0.095792 |
| ABBV | claude-fable-5-2026-06-10 | 225.82 | 2026-07-08 | 0.01 | 0.099725 | 0.031333 | 0.068393 | HIT | OUT_CI_HIGH | 1.043319 |
| LLY | gpt-5-2026-06-11 | 1163.72 | 2026-07-09 | 0.06 | 0.041312 | 0.021597 | 0.019715 | HIT | IN_CI | -0.156651 |
| CVX | gpt-5-2026-06-11 | 188.14 | 2026-07-09 | 0.06 | -0.073987 | 0.021597 | -0.095584 | MISS | OUT_CI_LOW | -1.805761 |
| UNH | gpt-5-2026-06-11 | 406.33 | 2026-07-09 | 0.06 | 0.060665 | 0.021597 | 0.039068 | HIT | IN_CI | 0.008831 |
| ABBV | gpt-5-2026-06-11 | 226.955 | 2026-07-09 | 0.05 | 0.094226 | 0.021597 | 0.072629 | HIT | IN_CI | 0.620276 |
| BAC | gpt-5-2026-06-11 | 55.11 | 2026-07-09 | 0.04 | 0.076846 | 0.021597 | 0.05525 | HIT | IN_CI | 0.579345 |
| JNJ | gpt-5-2026-06-11 | 239.595 | 2026-07-09 | 0.04 | 0.080511 | 0.021597 | 0.058914 | HIT | IN_CI | 0.711967 |
| ANET | gpt-5-2026-06-11 | 155.37 | 2026-07-09 | 0.03 | 0.189322 | 0.021597 | 0.167726 | HIT | IN_CI | 0.843421 |
| AMT | gpt-5-2026-06-11 | 190.495 | 2026-07-09 | 0.03 | -0.134465 | 0.021597 | -0.156062 | MISS | OUT_CI_LOW | -1.888237 |
| GOOGL | gpt-5-2026-06-11 | 353.82 | 2026-07-09 | 0.05 | 0.007998 | 0.021597 | -0.013598 | MISS | IN_CI | -0.36022 |
| MCK | gpt-5-2026-06-11 | 791.8 | 2026-07-09 | 0.02 | -0.002551 | 0.021597 | -0.024148 | MISS | IN_CI | -0.253668 |
| GS | gpt-5-2026-06-11 | 1024.62 | 2026-07-09 | 0.02 | 0.034564 | 0.021597 | 0.012967 | HIT | IN_CI | 0.142645 |
| KO | gpt-5-2026-06-11 | 83.385 | 2026-07-09 | 0.02 | -0.012112 | 0.021597 | -0.033709 | MISS | IN_CI | -0.552711 |
| GE | gpt-5-2026-06-11 | 328.94 | 2026-07-09 | 0.02 | 0.091825 | 0.021597 | 0.070229 | HIT | IN_CI | 0.639014 |
| JPM | gpt-5-2026-06-11 | 313.91 | 2026-07-09 | 0.01 | 0.067726 | 0.021597 | 0.04613 | HIT | IN_CI | 0.901976 |
| ORCL | gpt-5-2026-06-11 | 182.33 | 2026-07-09 | 0.01 | -0.207645 | 0.021597 | -0.229242 | MISS | OUT_CI_LOW | -1.084432 |
| PG | gpt-5-2026-06-11 | 149.335 | 2026-07-09 | 0.01 | -0.020692 | 0.021597 | -0.042288 | MISS | IN_CI | -0.428656 |
| COP | gpt-5-2026-06-11 | 117.315 | 2026-07-09 | 0.01 | -0.077612 | 0.021597 | -0.099208 | MISS | IN_CI | -0.989961 |

Rolling calibration: equity hit rate 44.8%; CI coverage 72.4%. Market-forecast records are reported separately in `15_predictions.json`.

## 1. Prior Run Summary

Same-model baseline: `agents/equity/output/gpt-5-2026-06-11` (`SAME_MODEL_BASELINE`). That run used a sampled universe and ended `NO_TRADE` because portfolio beta feasibility failed despite several investable-grade names.

## 2. MoM Price & Return Table

Baseline names were settled through the prediction ledger above. Detailed MoM price rows are represented by settlement Source Ledger rows in `01_preflight.md`.

## 3. Theme-Level Performance

Health-care defensives and selected large-cap quality names were mixed; technology relative-strength names remain the strongest technical cohort in today's index-union scan.

## 4. Regime Shift Assessment

Prior sampled-run defensiveness has not cleanly carried forward. The current full-union technical scan points to a neutral tape with concentrated growth and cyber/software/semiconductor momentum.

## 5. Carry-Forward Decisions

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
| --- | --- | --- | --- | --- | --- |
| Health-care defensives | MIXED | Lower beta ballast | See settlements | DOWNGRADE | Mixed alpha and no refreshed fundamentals. |
| Technology momentum | N/A | Relative strength | See current scan | PROMOTE | Full-union technical breadth is strongest in growth/semis, but only as monitoring due missing non-price feeds. |

## 6. Sign-Off

Freshness tag: `DELAYED` for fetched prices/history. Reflection confidence: `MEDIUM`; settlement math is auditable, but non-price factor explanations remain unavailable.
