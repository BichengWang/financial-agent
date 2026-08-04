# 02 — Reflection — 2026-08-03

## Run context

Final status is `HALTED` and data mode is `DELAYED_PARTIAL`. Price, history, sigma,
universe, and settlement inputs are grounded, but 15 of the 20 pre-halt ranked names have
only a complete no-print-through-42-days result rather than a confirmed or cadence-estimated
next earnings date. At 75% of the pre-halt set, this exceeds Hard Halt Criterion 3's 20%
unresolved-critical-input threshold; the current-run rankings are diagnostics, not predictions.

## 0. Prediction Settlement

All 88 due keys across all models were settled before new scoring. Weekend targets use the
completed 2026-07-31 close; same-day targets use the completed 2026-08-03 close with explicit
`TARGET_DATE_CLOSE` and a timezone-aware post-16:00 ET `settled_at`. Every price passed the
current-run two-source 1% gate. Final canonical state: due=0,
conflicts=0.

| Ticker | Vintage | Entry | Target date | mu | Realized | SPY | Alpha | Direction | CI | z | Timing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABBV | 2026-07-05 | $261.07 | 2026-08-02 | +3.00% | -3.88% | +0.30% | -4.18% | MISS | IN_CI | -0.730 | WEEKEND_TARGET |
| ABNB | 2026-07-05 | $148.93 | 2026-08-02 | +6.00% | +1.74% | +0.30% | +1.44% | HIT | IN_CI | -0.452 | WEEKEND_TARGET |
| AMCR | 2026-07-05 | $45.00 | 2026-08-02 | +6.00% | -0.27% | +0.30% | -0.57% | MISS | IN_CI | -0.759 | WEEKEND_TARGET |
| BAX | 2026-07-05 | $22.65 | 2026-08-02 | +6.00% | +15.50% | +0.30% | +15.19% | HIT | IN_CI | +0.888 | WEEKEND_TARGET |
| BEN | 2026-07-05 | $34.11 | 2026-08-02 | +5.00% | -0.73% | +0.30% | -1.04% | MISS | IN_CI | -0.696 | WEEKEND_TARGET |
| BXP | 2026-07-05 | $69.32 | 2026-08-02 | +5.00% | +1.15% | +0.30% | +0.85% | HIT | IN_CI | -0.475 | WEEKEND_TARGET |
| CCEP | 2026-07-05 | $106.61 | 2026-08-02 | +6.00% | +2.67% | +0.30% | +2.37% | HIT | IN_CI | -0.443 | WEEKEND_TARGET |
| DVA | 2026-07-05 | $234.91 | 2026-08-02 | +5.00% | +2.21% | +0.30% | +1.90% | HIT | IN_CI | -0.400 | WEEKEND_TARGET |
| FFIV | 2026-07-05 | $408.14 | 2026-08-02 | +6.00% | -1.36% | +0.30% | -1.67% | MISS | IN_CI | -0.853 | WEEKEND_TARGET |
| HSIC | 2026-07-05 | $86.43 | 2026-08-02 | +6.00% | -0.79% | +0.30% | -1.09% | MISS | OUT_CI_LOW | -1.172 | WEEKEND_TARGET |
| HUM | 2026-07-05 | $396.75 | 2026-08-02 | +5.00% | -8.29% | +0.30% | -8.59% | MISS | OUT_CI_LOW | -1.165 | WEEKEND_TARGET |
| IFF | 2026-07-05 | $83.83 | 2026-08-02 | +6.00% | -5.50% | +0.30% | -5.80% | MISS | OUT_CI_LOW | -1.269 | WEEKEND_TARGET |
| INCY | 2026-07-05 | $116.86 | 2026-08-02 | +5.00% | +2.28% | +0.30% | +1.97% | HIT | IN_CI | -0.224 | WEEKEND_TARGET |
| LIN | 2026-07-05 | $546.64 | 2026-08-02 | +4.00% | -12.49% | +0.30% | -12.79% | MISS | OUT_CI_LOW | -2.766 | WEEKEND_TARGET |
| LLY | 2026-07-05 | $1,213.91 | 2026-08-02 | +4.00% | -5.36% | +0.30% | -5.66% | MISS | IN_CI | -0.954 | WEEKEND_TARGET |
| LYV | 2026-07-05 | $186.59 | 2026-08-02 | +6.00% | -6.68% | +0.30% | -6.98% | MISS | OUT_CI_LOW | -1.966 | WEEKEND_TARGET |
| MAS | 2026-07-05 | $82.77 | 2026-08-02 | +5.00% | -13.64% | +0.30% | -13.94% | MISS | OUT_CI_LOW | -2.013 | WEEKEND_TARGET |
| MNST | 2026-07-05 | $97.60 | 2026-08-02 | +5.00% | -1.25% | +0.30% | -1.55% | MISS | OUT_CI_LOW | -1.330 | WEEKEND_TARGET |
| MRNA | 2026-07-05 | $79.76 | 2026-08-02 | +5.00% | -31.27% | +0.30% | -31.57% | MISS | OUT_CI_LOW | -1.614 | WEEKEND_TARGET |
| PANW | 2026-07-05 | $348.06 | 2026-08-02 | +5.00% | -4.66% | +0.30% | -4.97% | MISS | IN_CI | -0.599 | WEEKEND_TARGET |
| QQQ | 2026-07-05 | $712.60 | 2026-08-02 | +0.79% | -3.45% | N/A | N/A | MISS | IN_CI | -0.501 | WEEKEND_TARGET |
| SOXX | 2026-07-05 | $566.32 | 2026-08-02 | +0.64% | -10.85% | N/A | N/A | MISS | IN_CI | -0.523 | WEEKEND_TARGET |
| SPY | 2026-07-05 | $744.78 | 2026-08-02 | +0.50% | +0.30% | N/A | N/A | HIT | IN_CI | -0.045 | WEEKEND_TARGET |
| SWK | 2026-07-05 | $91.90 | 2026-08-02 | +6.00% | +2.92% | +0.30% | +2.61% | HIT | IN_CI | -0.265 | WEEKEND_TARGET |
| VRTX | 2026-07-05 | $528.04 | 2026-08-02 | +5.00% | -9.65% | +0.30% | -9.95% | MISS | OUT_CI_LOW | -1.758 | WEEKEND_TARGET |
| WELL | 2026-07-05 | $236.06 | 2026-08-02 | +6.00% | -0.69% | +0.30% | -0.99% | MISS | IN_CI | -0.738 | WEEKEND_TARGET |
| ABBV | 2026-07-06 | $255.26 | 2026-08-03 | +1.00% | -3.98% | +0.93% | -4.91% | MISS | IN_CI | -0.524 | TARGET_DATE_CLOSE |
| AIZ | 2026-07-06 | $277.93 | 2026-08-03 | +5.00% | +1.60% | +0.93% | +0.67% | HIT | IN_CI | -0.633 | TARGET_DATE_CLOSE |
| BEN | 2026-07-06 | $34.46 | 2026-08-03 | +5.00% | +2.26% | +0.93% | +1.33% | HIT | IN_CI | -0.339 | TARGET_DATE_CLOSE |
| BXP | 2026-07-06 | $69.91 | 2026-08-03 | +5.00% | +0.72% | +0.93% | -0.22% | MISS | IN_CI | -0.545 | TARGET_DATE_CLOSE |
| CRWD | 2026-07-06 | $201.91 | 2026-08-03 | +5.00% | +0.31% | +0.93% | -0.62% | MISS | IN_CI | -0.297 | TARGET_DATE_CLOSE |
| DAL | 2026-07-06 | $92.28 | 2026-08-03 | +6.00% | -0.75% | +0.93% | -1.68% | MISS | IN_CI | -0.629 | TARGET_DATE_CLOSE |
| DDOG | 2026-07-06 | $258.92 | 2026-08-03 | +6.00% | +5.67% | +0.93% | +4.74% | HIT | IN_CI | -0.018 | TARGET_DATE_CLOSE |
| DVA | 2026-07-06 | $236.40 | 2026-08-03 | +5.00% | -1.15% | +0.93% | -2.08% | MISS | IN_CI | -0.897 | TARGET_DATE_CLOSE |
| FFIV | 2026-07-06 | $421.26 | 2026-08-03 | +5.00% | -3.54% | +0.93% | -4.47% | MISS | IN_CI | -0.968 | TARGET_DATE_CLOSE |
| FTNT | 2026-07-06 | $163.21 | 2026-08-03 | +5.00% | +0.00% | +0.93% | -0.93% | MISS | IN_CI | -0.398 | TARGET_DATE_CLOSE |
| HUM | 2026-07-06 | $391.70 | 2026-08-03 | +5.00% | -4.39% | +0.93% | -5.32% | MISS | IN_CI | -0.847 | TARGET_DATE_CLOSE |
| LIN | 2026-07-06 | $533.40 | 2026-08-03 | +3.00% | -9.93% | +0.93% | -10.86% | MISS | OUT_CI_LOW | -2.065 | TARGET_DATE_CLOSE |
| LLY | 2026-07-06 | $1,203.25 | 2026-08-03 | +3.00% | -6.81% | +0.93% | -7.74% | MISS | IN_CI | -1.012 | TARGET_DATE_CLOSE |
| LYV | 2026-07-06 | $184.04 | 2026-08-03 | +6.00% | -1.28% | +0.93% | -2.21% | MISS | OUT_CI_LOW | -1.118 | TARGET_DATE_CLOSE |
| MAS | 2026-07-06 | $81.12 | 2026-08-03 | +6.00% | -7.88% | +0.93% | -8.81% | MISS | OUT_CI_LOW | -1.520 | TARGET_DATE_CLOSE |
| MNST | 2026-07-06 | $96.14 | 2026-08-03 | +5.00% | -2.69% | +0.93% | -3.63% | MISS | OUT_CI_LOW | -1.580 | TARGET_DATE_CLOSE |
| MRNA | 2026-07-06 | $83.49 | 2026-08-03 | +5.00% | -33.96% | +0.93% | -34.89% | MISS | OUT_CI_LOW | -1.768 | TARGET_DATE_CLOSE |
| PANW | 2026-07-06 | $357.79 | 2026-08-03 | +5.00% | -2.98% | +0.93% | -3.91% | MISS | IN_CI | -0.503 | TARGET_DATE_CLOSE |
| QQQ | 2026-07-06 | $724.45 | 2026-08-03 | +0.83% | -3.37% | N/A | N/A | MISS | IN_CI | -0.504 | TARGET_DATE_CLOSE |
| SOXX | 2026-07-06 | $589.15 | 2026-08-03 | +1.71% | -13.83% | N/A | N/A | MISS | IN_CI | -0.722 | TARGET_DATE_CLOSE |
| SPY | 2026-07-06 | $750.67 | 2026-08-03 | +0.50% | +0.93% | N/A | N/A | HIT | IN_CI | +0.100 | TARGET_DATE_CLOSE |
| SWK | 2026-07-06 | $92.33 | 2026-08-03 | +6.00% | +6.26% | +0.93% | +5.33% | HIT | IN_CI | +0.023 | TARGET_DATE_CLOSE |
| SYY | 2026-07-06 | $83.29 | 2026-08-03 | +6.00% | +2.03% | +0.93% | +1.10% | HIT | IN_CI | -0.685 | TARGET_DATE_CLOSE |
| TTWO | 2026-07-06 | $257.60 | 2026-08-03 | +6.00% | -4.83% | +0.93% | -5.77% | MISS | OUT_CI_LOW | -1.046 | TARGET_DATE_CLOSE |
| V | 2026-07-06 | $355.98 | 2026-08-03 | +6.00% | +2.72% | +0.93% | +1.79% | HIT | IN_CI | -0.519 | TARGET_DATE_CLOSE |
| VRTX | 2026-07-06 | $525.91 | 2026-08-03 | +5.00% | -10.49% | +0.93% | -11.43% | MISS | OUT_CI_LOW | -1.903 | TARGET_DATE_CLOSE |
| AMAT | 2026-07-05 | $603.04 | 2026-08-02 | +6.00% | -15.81% | +0.30% | -16.12% | MISS | IN_CI | -0.813 | WEEKEND_TARGET |
| AMD | 2026-07-05 | $517.82 | 2026-08-02 | +6.00% | -8.05% | +0.30% | -8.35% | MISS | IN_CI | -0.601 | WEEKEND_TARGET |
| ARM | 2026-07-05 | $315.28 | 2026-08-02 | +6.00% | -23.98% | +0.30% | -24.28% | MISS | IN_CI | -0.829 | WEEKEND_TARGET |
| CNC | 2026-07-05 | $67.86 | 2026-08-02 | +6.00% | -8.31% | +0.30% | -8.61% | MISS | OUT_CI_LOW | -1.159 | WEEKEND_TARGET |
| CRWD | 2026-07-05 | $193.98 | 2026-08-02 | +6.00% | -1.61% | +0.30% | -1.91% | MISS | IN_CI | -0.467 | WEEKEND_TARGET |
| DDOG | 2026-07-05 | $260.36 | 2026-08-02 | +6.00% | +2.92% | +0.30% | +2.62% | HIT | IN_CI | -0.167 | WEEKEND_TARGET |
| DELL | 2026-07-05 | $394.32 | 2026-08-02 | +6.00% | +2.80% | +0.30% | +2.50% | HIT | IN_CI | -0.090 | WEEKEND_TARGET |
| FLEX | 2026-07-05 | $136.86 | 2026-08-02 | +6.00% | -16.89% | +0.30% | -17.19% | MISS | IN_CI | -1.003 | WEEKEND_TARGET |
| HOOD | 2026-07-05 | $112.73 | 2026-08-02 | +6.00% | -23.21% | +0.30% | -23.52% | MISS | OUT_CI_LOW | -1.278 | WEEKEND_TARGET |
| HUM | 2026-07-05 | $396.75 | 2026-08-02 | +6.00% | -8.29% | +0.30% | -8.59% | MISS | OUT_CI_LOW | -1.253 | WEEKEND_TARGET |
| INTC | 2026-07-05 | $120.35 | 2026-08-02 | +6.00% | -25.05% | +0.30% | -25.35% | MISS | OUT_CI_LOW | -1.183 | WEEKEND_TARGET |
| KLAC | 2026-07-05 | $235.55 | 2026-08-02 | +6.00% | -22.39% | +0.30% | -22.69% | MISS | IN_CI | -0.943 | WEEKEND_TARGET |
| LRCX | 2026-07-05 | $351.41 | 2026-08-02 | +6.00% | -16.62% | +0.30% | -16.92% | MISS | IN_CI | -0.843 | WEEKEND_TARGET |
| MRNA | 2026-07-05 | $79.76 | 2026-08-02 | +6.00% | -31.27% | +0.30% | -31.57% | MISS | OUT_CI_LOW | -1.658 | WEEKEND_TARGET |
| MRVL | 2026-07-05 | $245.29 | 2026-08-02 | +6.00% | -23.54% | +0.30% | -23.84% | MISS | IN_CI | -0.707 | WEEKEND_TARGET |
| MU | 2026-07-05 | $975.56 | 2026-08-02 | +6.00% | -15.64% | +0.30% | -15.94% | MISS | IN_CI | -0.594 | WEEKEND_TARGET |
| PANW | 2026-07-05 | $348.06 | 2026-08-02 | +6.00% | -4.66% | +0.30% | -4.97% | MISS | IN_CI | -0.661 | WEEKEND_TARGET |
| QQQ | 2026-07-05 | $712.60 | 2026-08-02 | +0.89% | -3.45% | N/A | N/A | MISS | IN_CI | -0.513 | WEEKEND_TARGET |
| SNDK | 2026-07-05 | $1,745.00 | 2026-08-02 | +6.00% | -30.38% | +0.30% | -30.68% | MISS | IN_CI | -0.934 | WEEKEND_TARGET |
| SOXX | 2026-07-05 | $566.32 | 2026-08-02 | +1.94% | -10.85% | N/A | N/A | MISS | IN_CI | -0.582 | WEEKEND_TARGET |
| SPY | 2026-07-05 | $744.78 | 2026-08-02 | +0.50% | +0.30% | N/A | N/A | HIT | IN_CI | -0.045 | WEEKEND_TARGET |
| STX | 2026-07-05 | $820.16 | 2026-08-02 | +6.00% | +4.39% | +0.30% | +4.08% | HIT | IN_CI | -0.066 | WEEKEND_TARGET |
| WDC | 2026-07-05 | $539.00 | 2026-08-02 | +6.00% | +1.08% | +0.30% | +0.78% | HIT | IN_CI | -0.161 | WEEKEND_TARGET |
| AMD | 2026-07-06 | $559.27 | 2026-08-03 | +6.00% | -13.34% | +0.88% | -14.23% | MISS | IN_CI | -0.828 | TARGET_DATE_CLOSE |
| AXON | 2026-07-06 | $616.54 | 2026-08-03 | +6.00% | -6.59% | +0.88% | -7.47% | MISS | IN_CI | -0.610 | TARGET_DATE_CLOSE |
| CRWD | 2026-07-06 | $201.45 | 2026-08-03 | +6.00% | +0.54% | +0.88% | -0.34% | MISS | IN_CI | -0.340 | TARGET_DATE_CLOSE |
| DDOG | 2026-07-06 | $258.29 | 2026-08-03 | +6.00% | +5.93% | +0.88% | +5.05% | HIT | IN_CI | -0.004 | TARGET_DATE_CLOSE |
| DELL | 2026-07-06 | $410.73 | 2026-08-03 | +6.00% | +4.45% | +0.88% | +3.57% | HIT | IN_CI | -0.044 | TARGET_DATE_CLOSE |
| DVA | 2026-07-06 | $236.19 | 2026-08-03 | +6.00% | -1.06% | +0.88% | -1.94% | MISS | IN_CI | -1.013 | TARGET_DATE_CLOSE |
| HOOD | 2026-07-06 | $117.12 | 2026-08-03 | +6.00% | -22.87% | +0.88% | -23.75% | MISS | OUT_CI_LOW | -1.258 | TARGET_DATE_CLOSE |
| INTC | 2026-07-06 | $124.15 | 2026-08-03 | +6.00% | -26.70% | +0.88% | -27.58% | MISS | OUT_CI_LOW | -1.274 | TARGET_DATE_CLOSE |
| MRNA | 2026-07-06 | $83.31 | 2026-08-03 | +6.00% | -33.81% | +0.88% | -34.69% | MISS | OUT_CI_LOW | -1.778 | TARGET_DATE_CLOSE |
| QQQ | 2026-07-06 | $724.74 | 2026-08-03 | +1.23% | -3.40% | N/A | N/A | MISS | IN_CI | -0.546 | TARGET_DATE_CLOSE |
| SOXX | 2026-07-06 | $589.34 | 2026-08-03 | +2.50% | -13.86% | N/A | N/A | MISS | IN_CI | -0.748 | TARGET_DATE_CLOSE |
| SPY | 2026-07-06 | $751.06 | 2026-08-03 | +0.50% | +0.88% | N/A | N/A | HIT | IN_CI | +0.087 | TARGET_DATE_CLOSE |
| TXN | 2026-07-06 | $304.29 | 2026-08-03 | +6.00% | -11.58% | +0.88% | -12.46% | MISS | IN_CI | -0.967 | TARGET_DATE_CLOSE |

### Rolling calibration

| Record type | raw n | 28d eff_n | Hit rate | CI coverage | Mean z | Rank IC | Track A gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQUITY_ALPHA | 515 | 1 | 39.81% | 69.90% | -0.5191 | -0.0879 weighted mean across vintages | INSUFFICIENT_EFFECTIVE_N |
| MARKET_FORECAST | 90 | 1 | 22.09% | 81.11% | -0.6253 | N/A — rank IC is not defined for this record type | INSUFFICIENT_EFFECTIVE_N |

This run's batch: EQUITY_ALPHA n=76, hit=25.00%,
CI=68.42%, mean z=-0.8561;
MARKET_FORECAST n=12, hit=33.33%,
CI=100.00%, mean z=-0.3785.
The pre-reflection canonical-normalizer pass scanned the following 71 prior prediction
ledgers. The final post-publication pass also scanned this run's ledger, bringing its package
count to 72. `eff_n < 3` keeps every Track A calibration proposal deferred.

```text
agents/equity/output/claude-fable-5-2026-06-10/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-01/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-02/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-03/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-04/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-05/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-06/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-07/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-08/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-09/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-10/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-11/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-12/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-13/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-14/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-15/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-17/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-20/15_predictions.json
agents/equity/output/claude-fable-5-2026-07-21/15_predictions.json
agents/equity/output/claude-opus-4-8-2026-06-30/15_predictions.json
agents/equity/output/claude-opus-5-2026-07-24/15_predictions.json
agents/equity/output/claude-opus-5-2026-07-26/15_predictions.json
agents/equity/output/claude-opus-5-2026-07-27/15_predictions.json
agents/equity/output/claude-opus-5-2026-07-28/15_predictions.json
agents/equity/output/claude-opus-5-2026-07-29/15_predictions.json
agents/equity/output/claude-opus-5-2026-07-30/15_predictions.json
agents/equity/output/claude-opus-5-2026-08-01/15_predictions.json
agents/equity/output/claude-sonnet-5-2026-07-02/15_predictions.json
agents/equity/output/claude-sonnet-5-2026-07-03/15_predictions.json
agents/equity/output/claude-sonnet-5-2026-07-22/15_predictions.json
agents/equity/output/gemini-3.5-flash-2026-06-21/15_predictions.json
agents/equity/output/gemini-3.5-flash-2026-06-29/15_predictions.json
agents/equity/output/gemini-3.5-flash-2026-07-13/15_predictions.json
agents/equity/output/gpt-5-2026-06-11/15_predictions.json
agents/equity/output/gpt-5-2026-06-14/15_predictions.json
agents/equity/output/gpt-5-2026-06-15/15_predictions.json
agents/equity/output/gpt-5-2026-06-16/15_predictions.json
agents/equity/output/gpt-5-2026-06-17/15_predictions.json
agents/equity/output/gpt-5-2026-06-18/15_predictions.json
agents/equity/output/gpt-5-2026-06-19/15_predictions.json
agents/equity/output/gpt-5-2026-06-20/15_predictions.json
agents/equity/output/gpt-5-2026-06-21/15_predictions.json
agents/equity/output/gpt-5-2026-06-22/15_predictions.json
agents/equity/output/gpt-5-2026-06-24/15_predictions.json
agents/equity/output/gpt-5-2026-06-28/15_predictions.json
agents/equity/output/gpt-5-2026-06-29/15_predictions.json
agents/equity/output/gpt-5-2026-06-30/15_predictions.json
agents/equity/output/gpt-5-2026-07-01/15_predictions.json
agents/equity/output/gpt-5-2026-07-02/15_predictions.json
agents/equity/output/gpt-5-2026-07-03/15_predictions.json
agents/equity/output/gpt-5-2026-07-04/15_predictions.json
agents/equity/output/gpt-5-2026-07-05/15_predictions.json
agents/equity/output/gpt-5-2026-07-06/15_predictions.json
agents/equity/output/gpt-5-2026-07-07/15_predictions.json
agents/equity/output/gpt-5-2026-07-08/15_predictions.json
agents/equity/output/gpt-5-2026-07-09/15_predictions.json
agents/equity/output/gpt-5-2026-07-10/15_predictions.json
agents/equity/output/gpt-5-2026-07-11/15_predictions.json
agents/equity/output/gpt-5-2026-07-12/15_predictions.json
agents/equity/output/gpt-5-2026-07-13/15_predictions.json
agents/equity/output/gpt-5-2026-07-14/15_predictions.json
agents/equity/output/gpt-5-2026-07-15/15_predictions.json
agents/equity/output/gpt-5-2026-07-17/15_predictions.json
agents/equity/output/gpt-5-2026-07-20/15_predictions.json
agents/equity/output/gpt-5-2026-07-21/15_predictions.json
agents/equity/output/gpt-5-2026-07-22/15_predictions.json
agents/equity/output/gpt-5-2026-07-24/15_predictions.json
agents/equity/output/gpt-5-2026-07-27/15_predictions.json
agents/equity/output/gpt-5-2026-07-28/15_predictions.json
agents/equity/output/gpt-5-2026-07-29/15_predictions.json
agents/equity/output/gpt-5-2026-07-30/15_predictions.json
```

## 1. Prior Run Summary and deterministic MoM tie

The target date is exactly 2026-07-06. Two folders tie at zero days; criterion (a), same
executing model, selects `gpt-5-2026-07-06`. Both books have usable ledgers and are reported:

| Folder | Settled equity n | Hit rate | Mean alpha | Mean z | Disposition |
| --- | --- | --- | --- | --- | --- |
| gpt-5-2026-07-06 | 10 | 20.00% | -11.38% | -0.812 | SELECTED — same model |
| claude-fable-5-2026-07-06 | 23 | 26.09% | -4.11% | -0.860 | TIED ALTERNATIVE |

The hit-rate spread is 6.09%; the MoM conclusion is **invariant** across the tied
books. The selected baseline was `REVIEW_ONLY` / `NEUTRAL` and carried a technical-monitoring
book rather than an executable portfolio.

| Prior-run field | Selected-baseline value |
| --- | --- |
| Date / model / final status / regime | 2026-07-06 / `gpt-5` / `REVIEW_ONLY` / `NEUTRAL` |
| Monitoring basket | HOOD, CRWD, MRNA, DDOG, AXON, DVA, DELL, INTC, AMD, TXN |
| Top five adjusted scores | HOOD 0.788095; CRWD 0.753630; MRNA 0.706886; DDOG 0.672481; AXON 0.645009 |
| Thesis cluster | Technical relative-strength monitors; no executable portfolio because earnings and non-price evidence were incomplete |

## 2. MoM Price & Return Table — selected baseline

| Ticker | Prior date | Prior price | Current date | Current price | Return | SPY | Alpha | Hit/Miss | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMD | 2026-07-06 | $559.27 | 2026-08-03 | $484.64 | -13.34% | +0.88% | -14.23% | MISS | IN_CI; TARGET_DATE_CLOSE |
| AXON | 2026-07-06 | $616.54 | 2026-08-03 | $575.88 | -6.59% | +0.88% | -7.47% | MISS | IN_CI; TARGET_DATE_CLOSE |
| CRWD | 2026-07-06 | $201.45 | 2026-08-03 | $202.54 | +0.54% | +0.88% | -0.34% | MISS | IN_CI; TARGET_DATE_CLOSE |
| DDOG | 2026-07-06 | $258.29 | 2026-08-03 | $273.60 | +5.93% | +0.88% | +5.05% | HIT | IN_CI; TARGET_DATE_CLOSE |
| DELL | 2026-07-06 | $410.73 | 2026-08-03 | $429.02 | +4.45% | +0.88% | +3.57% | HIT | IN_CI; TARGET_DATE_CLOSE |
| DVA | 2026-07-06 | $236.19 | 2026-08-03 | $233.68 | -1.06% | +0.88% | -1.94% | MISS | IN_CI; TARGET_DATE_CLOSE |
| HOOD | 2026-07-06 | $117.12 | 2026-08-03 | $90.34 | -22.87% | +0.88% | -23.75% | MISS | OUT_CI_LOW; TARGET_DATE_CLOSE |
| INTC | 2026-07-06 | $124.15 | 2026-08-03 | $91.00 | -26.70% | +0.88% | -27.58% | MISS | OUT_CI_LOW; TARGET_DATE_CLOSE |
| MRNA | 2026-07-06 | $83.31 | 2026-08-03 | $55.14 | -33.81% | +0.88% | -34.69% | MISS | OUT_CI_LOW; TARGET_DATE_CLOSE |
| TXN | 2026-07-06 | $304.29 | 2026-08-03 | $269.04 | -11.58% | +0.88% | -12.46% | MISS | IN_CI; TARGET_DATE_CLOSE |

## 3. Theme-Level Performance

The baseline technical-monitor theme is **partial/failed**: the selected book's hit rate is
20.00%, mean alpha -11.38%, and mean z
-0.812. The evidence is observed settlement state, not a narrative
inference. Cross-model dispersion remains material when the hit-rate spread exceeds 10pp.

## 4. Regime Shift Assessment

The selected baseline classified the regime `NEUTRAL`; today's completed-close evidence
supports `BULL`. SPY trend, 60-day momentum, and VIX evidence are ledgered in
`L-TI-SPY`, `L-MAC-VIX`, and `L-MAC-VIX60`. The negative rank IC prevents a confidence upgrade.

## 5. Carry-Forward Decisions

| Ticker/Theme | Prior Score | Prior Thesis | MoM Alpha | Decision | Rationale |
| --- | --- | --- | --- | --- | --- |
| AMD | UNAVAILABLE | 2026-07-06 monitor | -14.23% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| AXON | UNAVAILABLE | 2026-07-06 monitor | -7.47% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| CRWD | UNAVAILABLE | 2026-07-06 monitor | -0.34% | DOWNGRADE | Still scoreable but outside today's published top-20 sleeve. |
| DDOG | UNAVAILABLE | 2026-07-06 monitor | +5.05% | DOWNGRADE | Still scoreable but outside today's published top-20 sleeve. |
| DELL | UNAVAILABLE | 2026-07-06 monitor | +3.57% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| DVA | UNAVAILABLE | 2026-07-06 monitor | -1.94% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| HOOD | UNAVAILABLE | 2026-07-06 monitor | -23.75% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| INTC | UNAVAILABLE | 2026-07-06 monitor | -27.58% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| MRNA | UNAVAILABLE | 2026-07-06 monitor | -34.69% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |
| TXN | UNAVAILABLE | 2026-07-06 monitor | -12.46% | DROP | Does not clear today's 60th-percentile monitoring floor or eligibility filter. |

## 6. Sign-Off

Weekend settlements are tagged `HISTORICAL`; same-day completed target-date-close settlement
same-day and weekend settlement closes are tagged `HISTORICAL`. Reflection confidence is `MEDIUM`: every close was retrieved
and cross-checked this run and canonical timing is grounded, but `eff_n=1` means the large
raw sample is not an independent calibration sample. Final run status is `HALTED` in
`DELAYED_PARTIAL` mode; the pre-halt current-run rankings are diagnostics, not valid
predictions.
