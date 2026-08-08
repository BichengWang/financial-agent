```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-06
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

> **BACKFILLED 2026-08-07.** The 2026-08-06 session truncated after writing `00`-`04` and `15_predictions.json`; this artifact was reconstructed on 2026-08-07 from that folder's own committed data (`15_predictions.json` plus `00`-`04`) and from nothing else. Figures that the truncated session never persisted are marked `UNAVAILABLE` rather than recomputed: the 2026-08-06 run used the 2026-08-05 close as its basis, so substituting a later run's numbers would misstate what that run actually saw. No prediction record was created, altered or settled.

## Executive summary

All five Required inputs were grounded — 27/27 published symbols at 0.0000% max deviation
across three sources, and a complete 27-business-day forward earnings sweep — so 2026-08-06 was
an evidence-threshold `NO_TRADE`, not a data failure. No name was investable because `Fund_Z`
and `Sent_Z` were `UNAVAILABLE` across all 511 scored names, making evidence thresholds #2 and
#3 arithmetically unsatisfiable and holding data completeness at 0.80. 24 names
published as a settleable monitoring sleeve alongside three core ETF forecasts. The run also
settled 98 due prediction keys — an unusually large queue because no package exists for
2026-08-05 from any model.

## MoM reflection summary

Baseline `claude-fable-5-2026-07-09` (`CROSS_MODEL_BASELINE`). Full detail in
`02_reflection.md`, which the truncated session did publish.

## Regime

| Field | Value | Key evidence |
|---|---|---|
| Regime | **BULL** | SPY 769.79 above MA20 748.41 and MA50 745.73; 60d momentum +4.63%; daily MA alignment BULLISH |
| Data quality | 0.80 | 2 of 4 factor families UNAVAILABLE |
| Key macro risk | elevated RSI | SPY daily RSI(14) 64.82; several published names above 70 |

## Core ETF market forecast

| ETF | Entry | mu | sigma | Target | 70% CI | Target Date | Confidence |
|---|---|---|---|---|---|---|---|
| SPY | 769.79 | +2.00% | 3.79% | 785.19 | 754.81–815.56 | 2026-09-03 | MEDIUM |
| QQQ | 717.30 | +3.42% | 7.29% | 741.85 | 687.47–796.23 | 2026-09-03 | MEDIUM |
| SOXX | 530.70 | +7.00% | 18.47% | 567.84 | 465.90–669.78 | 2026-09-03 | MEDIUM |

## Ranked candidates — monitoring sleeve (24 names, 0 investable)

| Rank | Ticker | Entry | Adj Score | Pctl | Score Trace | mu | sigma | Target | 70% CI | Beta | Sharpe | IR | Max DD60 | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AIZ | 301.57 | +0.3793 | 100.00 | T +1.42 / M +0.32 x0.80 - 0.00 | +6.00% | 7.23% | 319.66 | 296.98–342.35 | -0.269 | 0.79 | 1.01 | -4.17% | LOW |
| 2 | AMGN | 407.83 | +0.3724 | 99.80 | T +1.33 / M +0.44 x0.80 - 0.00 | +6.00% | 8.03% | 432.30 | 398.23–466.37 | 0.077 | 0.71 | 0.75 | -5.05% | LOW |
| 3 | CRL | 260.72 | +0.3623 | 99.61 | T +1.45 / M +0.12 x0.80 - 0.00 | +6.00% | 15.27% | 276.36 | 234.96–317.76 | 0.596 | 0.37 | 0.33 | -15.59% | LOW |
| 4 | JCI | 153.65 | +0.3178 | 99.41 | T +0.93 / M +0.80 x0.80 - 0.00 | +6.00% | 8.89% | 162.87 | 148.67–177.07 | 1.377 | 0.64 | 0.38 | -7.67% | LOW |
| 5 | EXPE | 319.66 | +0.3149 | 99.22 | T +1.55 / M -0.48 x0.80 - 0.00 | +6.00% | 13.71% | 338.84 | 293.25–384.43 | 0.359 | 0.41 | 0.44 | -6.67% | LOW |
| 6 | CPAY | 394.53 | +0.3135 | 99.02 | T +1.16 / M +0.29 x0.80 - 0.00 | +6.00% | 9.01% | 418.20 | 381.24–455.16 | 0.299 | 0.63 | 0.61 | -10.52% | LOW |
| 7 | NTAP | 186.60 | +0.3079 | 98.82 | T +0.97 / M +0.63 x0.80 - 0.00 | +6.00% | 12.56% | 197.80 | 173.43–222.16 | 1.448 | 0.45 | 0.17 | -15.81% | LOW |
| 8 | HSIC | 89.59 | +0.3022 | 98.63 | T +1.04 / M +0.43 x0.80 - 0.00 | +6.00% | 6.67% | 94.97 | 88.75–101.18 | 0.155 | 0.85 | 0.88 | -4.23% | LOW |
| 9 | DXCM | 82.66 | +0.3010 | 98.43 | T +0.92 / M +0.67 x0.80 - 0.00 | +6.00% | 15.40% | 87.62 | 74.38–100.86 | 0.209 | 0.37 | 0.38 | -13.86% | LOW |
| 10 | IVZ | 32.01 | +0.2911 | 98.24 | T +1.02 / M +0.39 x0.80 - 0.00 | +6.00% | 11.55% | 33.93 | 30.09–37.78 | 1.698 | 0.49 | 0.31 | -11.40% | LOW |
| 11 | J | 144.67 | +0.2904 | 98.04 | T +1.00 / M +0.43 x0.80 - 0.00 | +6.00% | 7.93% | 153.35 | 141.42–165.28 | 0.431 | 0.72 | 0.55 | -9.42% | LOW |
| 12 | NUE | 274.74 | +0.2897 | 97.84 | T +1.22 / M -0.02 x0.80 - 0.00 | +6.00% | 11.29% | 291.22 | 258.96–323.49 | 0.790 | 0.50 | 0.45 | -17.57% | LOW |
| 13 | CDW | 140.10 | +0.2893 | 97.65 | T +0.92 / M +0.56 x0.80 - 0.00 | +6.00% | 14.41% | 148.51 | 127.51–169.50 | 0.711 | 0.39 | 0.30 | -12.35% | LOW |
| 14 | BAX | 27.33 | +0.2874 | 97.45 | T +1.11 / M +0.18 x0.80 - 0.00 | +6.00% | 14.62% | 28.97 | 24.81–33.13 | 0.625 | 0.39 | 0.38 | -7.19% | LOW |
| 15 | PRU | 120.16 | +0.2747 | 97.25 | T +0.88 / M +0.53 x0.80 - 0.00 | +6.00% | 6.42% | 127.37 | 119.35–135.39 | 0.208 | 0.89 | 0.94 | -3.04% | LOW |
| 16 | EMR | 162.47 | +0.2715 | 97.06 | T +1.19 / M -0.11 x0.80 - 0.00 | +6.00% | 8.76% | 172.22 | 157.41–187.03 | 1.335 | 0.65 | 0.47 | -10.14% | LOW |
| 17 | WSM | 248.24 | +0.2710 | 96.86 | T +1.08 / M +0.10 x0.80 - 0.00 | +6.00% | 9.65% | 263.13 | 238.22–288.05 | 0.957 | 0.59 | 0.41 | -9.79% | LOW |
| 18 | JPM | 359.24 | +0.2692 | 96.67 | T +0.73 / M +0.78 x0.80 - 0.00 | +6.00% | 5.98% | 380.79 | 358.47–403.12 | 0.383 | 0.95 | 0.84 | -3.53% | LOW |
| 19 | GM | 89.16 | +0.2656 | 96.47 | T +0.80 / M +0.61 x0.80 - 0.00 | +6.00% | 8.96% | 94.51 | 86.20–102.82 | 1.102 | 0.63 | 0.41 | -10.27% | LOW |
| 20 | SHOP | 144.24 | +0.2633 | 96.27 | T +1.37 / M -0.54 x0.80 - 0.00 | +6.00% | 21.48% | 152.89 | 120.67–185.12 | 0.767 | 0.26 | 0.24 | -13.59% | LOW |
| 21 | MTD | 1,421.52 | +0.2605 | 96.08 | T +0.83 / M +0.52 x0.80 - 0.00 | +6.00% | 8.59% | 1,506.81 | 1,379.82–1,633.80 | 0.616 | 0.66 | 0.52 | -8.80% | LOW |
| 22 | MELI | 1,922.57 | +0.2560 | 95.88 | T +0.73 / M +0.68 x0.80 - 0.00 | +6.00% | 7.23% | 2,037.92 | 1,893.41–2,182.43 | 0.666 | 0.79 | 0.54 | -8.51% | LOW |
| 23 | GRMN | 302.55 | +0.2543 | 95.69 | T +1.06 / M +0.00 x0.80 - 0.00 | +6.00% | 15.40% | 320.70 | 272.24–369.17 | 0.204 | 0.37 | 0.46 | -6.86% | LOW |
| 24 | BEN | 34.92 | +0.2519 | 95.49 | T +0.63 / M +0.84 x0.80 - 0.00 | +6.00% | 8.21% | 37.02 | 34.03–40.00 | 1.059 | 0.69 | 0.56 | -6.42% | LOW |

Complete score attribution and technical indicator states are in `05_factor_scores.md`.

## No-trade rationale

Evidence thresholds #2 (>=3 of 4 families non-negative), #3 (no family above 50% of conviction)
and #4 (data completeness >= 85%) all failed, the first two unsatisfiably. The beta band was
**feasible** (-0.2803 … +1.4145), so this was not a feasibility outcome. Full threshold table in
`00_run_manifest.md`.

## Assumptions and limitations

1. Two of four factor families unavailable; every ranking rests on technical and macro evidence.
2. Confidence capped; no name carries HIGH.
3. The 2026-08-05 audit-trail gap is documented in `00` and is not resolvable retroactively.
4. **This report is a backfill.** Portfolio-level analytics from that run are `UNAVAILABLE`
   because they were never written to a durable artifact — see `07`.

## Next scheduled review

Superseded: the next package in the audit trail is `claude-opus-5-2026-08-07`.
