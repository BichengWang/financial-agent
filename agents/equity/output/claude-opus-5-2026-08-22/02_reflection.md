# 02 — Reflection · 2026-08-22

Standalone month-over-month reflection. Every price, return, and regime claim below cites a
`01_preflight.md` ledger row or is marked `UNAVAILABLE`. Reflection completed **before** any
scoring; its carry-forward decisions bind factor scoring where ledger-backed.

## 0. Prediction Settlement

`settlement_ledger.py` was run first (L014). Due inventory at `--as-of 2026-08-22` was
**227** keys; **all 227** settled this run and the post-write re-run reports
`due_inventory: 0` and `conflicts: 0`.

Every due key had `target_date` on a completed trading session strictly before the run date, so
**all 227 carry `timing_flag = ORDINARY`** and settle at the target date's own close
(raw, unadjusted — matching the basis on which each entry price was recorded). No key needed
`WEEKEND_TARGET`, `TARGET_EQ_RUN_DATE`, or `TARGET_DATE_CLOSE`.

Packages scanned for due predictions: every `agents/equity/output/*/15_predictions.json`
(1,682 candidate settlement rows across all models).

### This run's settlement batch

| Metric | EQUITY_ALPHA | MARKET_FORECAST |
|---|---|---|
| Settled this run | 203 | 24 |
| Direction-scored | 203 | 11 (13 `N/A - FLAT_CALL`) |
| Hit rate | 34.0% | 81.8% |
| CI coverage | 74.4% | 100.0% |
| Mean z | -0.6845 | +0.3602 |
| Mean realized alpha | -3.22% | N/A — settled on raw return |

Per source model:

| Model | Settled (EQ) | Hit rate | Mean alpha | Mean z | CI coverage |
|---|---|---|---|---|---|
| claude-fable-5 | 53 | 26.4% | -4.27% | -0.7610 | 71.7% |
| claude-opus-5 | 26 | 26.9% | -2.59% | -0.5968 | 76.9% |
| claude-sonnet-5 | 26 | 42.3% | -2.04% | -0.6234 | 69.2% |
| gpt-5 | 98 | 37.8% | -3.13% | -0.6826 | 76.5% |

### Rolling calibration metrics (canonical ledger, all models, all time)

| Record type | raw n | 28-day eff_n | Hit rate | CI coverage | Mean z | Track A eligible |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 1,153 | 2 | 39.38% | 71.47% | -0.5506 | **No** — INSUFFICIENT_EFFECTIVE_N |
| `MARKET_FORECAST` | 174 | 2 | 35.71% | 90.23% | -0.2952 | **No** — INSUFFICIENT_EFFECTIVE_N |

Healthy ranges (`rules.md § Rolling Calibration Metrics`): hit rate > 50%, CI coverage 55–85%,
mean z −0.5 to +0.5.

- `EQUITY_ALPHA` CI coverage **71.47%** is inside the healthy band and close to
  the 70% target — sigma sourcing is well calibrated. Hit rate **39.38%** is below
  50% and mean z **-0.5506** sits just outside the healthy floor: the mu prior is modestly
  too aggressive, but the *interval* is right.
- `MARKET_FORECAST` CI coverage **90.23%** is **above the 85% ceiling** — by the
  interpretation rule these intervals are uninformatively wide and should be tightened. That is a
  Track A change to sigma sourcing and is **gated**: see the eff_n line below.

**eff_n is now 2 for both record types** — up from 1, which is the first movement since the measure
was introduced on 2026-07-24. The 2026-07-28 package made a falsifiable projection that `EQ eff_n`
would increment on 2026-08-05; it did. `eff_n` remains below the `>= 3` Track A gate, so every
calibration proposal this run is `DEFER`, not `REJECT` (`rules.md § Rolling Calibration Metrics`).

| Record type | eff_n | Windows selected | Target-date span | Next window opens | eff_n increments on | Pending at that date |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 2 | 2026-07-08 + 2026-08-05 | 44d | 2026-09-02 | 2026-09-03 | 24 |
| `MARKET_FORECAST` | 2 | 2026-07-12 + 2026-08-09 | 40d | 2026-09-06 | 2026-09-07 | 3 |

Rank IC across all 60 scored vintages: mean **-0.0840**, median **-0.0567**, with 33 of 60 vintages at or below zero. The rank-order inversion documented since
2026-07-22 therefore persists in aggregate, and the `rules.md` binding applies: **confidence is
capped at `MEDIUM` for every name this run**. This run's own batch is a partial exception worth
recording — of the 8 vintages settled today, 5 have positive rank IC:

| Vintage | n | Rank IC |
|---|---|---|
| claude-fable-5:2026-07-20 | 33 | +0.2149 |
| claude-fable-5:2026-07-21 | 20 | +0.1482 |
| claude-opus-5:2026-07-24 | 26 | +0.1330 |
| claude-sonnet-5:2026-07-22 | 26 | -0.1726 |
| gpt-5:2026-07-20 | 23 | -0.6551 |
| gpt-5:2026-07-21 | 23 | -0.2510 |
| gpt-5:2026-07-22 | 26 | +0.0619 |
| gpt-5:2026-07-24 | 26 | +0.1282 |

### Settled predictions (all 227)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z | Timing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | claude-fable-5 2026-07-20 | 333.74 | 2026-08-17 | +2.00% | -8.43% | +3.95% | -12.39% | MISS | OUT_CI_LOW | -1.0615 | ORDINARY |
| ADP | claude-fable-5 2026-07-20 | 255.26 | 2026-08-17 | +4.00% | +4.23% | +3.95% | +0.28% | HIT | IN_CI | +0.0254 | ORDINARY |
| BAC | claude-fable-5 2026-07-20 | 61.27 | 2026-08-17 | +5.00% | +4.28% | +3.95% | +0.32% | HIT | IN_CI | -0.1223 | ORDINARY |
| BBY | claude-fable-5 2026-07-20 | 85.41 | 2026-08-17 | +5.00% | +0.04% | +3.95% | -3.92% | MISS | IN_CI | -0.5946 | ORDINARY |
| CFG | claude-fable-5 2026-07-20 | 72.39 | 2026-08-17 | +6.00% | +2.65% | +3.95% | -1.30% | MISS | IN_CI | -0.4019 | ORDINARY |
| CHRW | claude-fable-5 2026-07-20 | 208.50 | 2026-08-17 | +3.00% | -30.56% | +3.95% | -34.51% | MISS | OUT_CI_LOW | -3.7752 | ORDINARY |
| CSX | claude-fable-5 2026-07-20 | 50.75 | 2026-08-17 | +4.00% | -0.33% | +3.95% | -4.29% | MISS | IN_CI | -0.7461 | ORDINARY |
| CTAS | claude-fable-5 2026-07-20 | 204.45 | 2026-08-17 | +5.00% | -3.24% | +3.95% | -7.20% | MISS | IN_CI | -0.7353 | ORDINARY |
| DOC | claude-fable-5 2026-07-20 | 22.51 | 2026-08-17 | +5.00% | -8.57% | +3.95% | -12.53% | MISS | OUT_CI_LOW | -1.8853 | ORDINARY |
| EXPD | claude-fable-5 2026-07-20 | 182.80 | 2026-08-17 | +5.00% | +2.99% | +3.95% | -0.96% | MISS | IN_CI | -0.3264 | ORDINARY |
| FITB | claude-fable-5 2026-07-20 | 58.01 | 2026-08-17 | +6.00% | -0.71% | +3.95% | -4.66% | MISS | IN_CI | -0.8383 | ORDINARY |
| FRT | claude-fable-5 2026-07-20 | 126.02 | 2026-08-17 | +4.00% | -6.35% | +3.95% | -10.30% | MISS | OUT_CI_LOW | -1.8781 | ORDINARY |
| GE | claude-fable-5 2026-07-20 | 348.83 | 2026-08-17 | +1.00% | +5.91% | +3.95% | +1.95% | HIT | IN_CI | +0.5153 | ORDINARY |
| GEN | claude-fable-5 2026-07-20 | 26.74 | 2026-08-17 | +6.00% | +2.51% | +3.95% | -1.45% | MISS | IN_CI | -0.3406 | ORDINARY |
| IQV | claude-fable-5 2026-07-20 | 206.26 | 2026-08-17 | +4.00% | +16.96% | +3.95% | +13.01% | HIT | OUT_CI_HIGH | +1.1581 | ORDINARY |
| JBHT | claude-fable-5 2026-07-20 | 291.41 | 2026-08-17 | +6.00% | -2.76% | +3.95% | -6.71% | MISS | IN_CI | -0.8255 | ORDINARY |
| KHC | claude-fable-5 2026-07-20 | 25.88 | 2026-08-17 | +6.00% | -4.37% | +3.95% | -8.32% | MISS | OUT_CI_LOW | -1.0720 | ORDINARY |
| LLY | claude-fable-5 2026-07-20 | 1,179.11 | 2026-08-17 | +1.00% | +0.34% | +3.95% | -3.61% | MISS | IN_CI | -0.0690 | ORDINARY |
| MCO | claude-fable-5 2026-07-20 | 510.86 | 2026-08-17 | +4.00% | -6.59% | +3.95% | -10.55% | MISS | OUT_CI_LOW | -1.2164 | ORDINARY |
| MET | claude-fable-5 2026-07-20 | 94.00 | 2026-08-17 | +5.00% | +2.85% | +3.95% | -1.10% | MISS | IN_CI | -0.2944 | ORDINARY |
| MNST | claude-fable-5 2026-07-20 | 97.50 | 2026-08-17 | +4.00% | -53.31% | +3.95% | -57.27% | MISS | OUT_CI_LOW | -10.4777 | ORDINARY |
| MPC | claude-fable-5 2026-07-20 | 312.60 | 2026-08-17 | +5.00% | +14.58% | +3.95% | +10.63% | HIT | IN_CI | +0.9421 | ORDINARY |
| MTB | claude-fable-5 2026-07-20 | 249.24 | 2026-08-17 | +6.00% | +1.45% | +3.95% | -2.50% | MISS | IN_CI | -0.6859 | ORDINARY |
| PAYX | claude-fable-5 2026-07-20 | 114.39 | 2026-08-17 | +5.00% | +3.63% | +3.95% | -0.32% | MISS | IN_CI | -0.1530 | ORDINARY |
| PRU | claude-fable-5 2026-07-20 | 119.07 | 2026-08-17 | +5.00% | +4.61% | +3.95% | +0.66% | HIT | IN_CI | -0.0614 | ORDINARY |
| RF | claude-fable-5 2026-07-20 | 31.65 | 2026-08-17 | +6.00% | +0.16% | +3.95% | -3.79% | MISS | IN_CI | -0.8454 | ORDINARY |
| SNA | claude-fable-5 2026-07-20 | 410.99 | 2026-08-17 | +4.00% | -2.38% | +3.95% | -6.33% | MISS | OUT_CI_LOW | -1.0791 | ORDINARY |
| STT | claude-fable-5 2026-07-20 | 182.50 | 2026-08-17 | +5.00% | +5.78% | +3.95% | +1.82% | HIT | IN_CI | +0.1052 | ORDINARY |
| TRV | claude-fable-5 2026-07-20 | 368.98 | 2026-08-17 | +5.00% | -1.21% | +3.95% | -5.16% | MISS | IN_CI | -0.6404 | ORDINARY |
| UNH | claude-fable-5 2026-07-20 | 426.09 | 2026-08-17 | +4.00% | -7.15% | +3.95% | -11.10% | MISS | OUT_CI_LOW | -1.4241 | ORDINARY |
| UNP | claude-fable-5 2026-07-20 | 301.75 | 2026-08-17 | +4.00% | -0.61% | +3.95% | -4.57% | MISS | IN_CI | -0.6571 | ORDINARY |
| UPS | claude-fable-5 2026-07-20 | 117.72 | 2026-08-17 | +3.00% | -13.34% | +3.95% | -17.29% | MISS | OUT_CI_LOW | -1.7777 | ORDINARY |
| WST | claude-fable-5 2026-07-20 | 358.24 | 2026-08-17 | +3.00% | -3.25% | +3.95% | -7.20% | MISS | IN_CI | -0.9699 | ORDINARY |
| ABT | claude-fable-5 2026-07-21 | 101.66 | 2026-08-18 | +6.00% | +10.84% | +3.42% | +7.42% | HIT | IN_CI | +0.4098 | ORDINARY |
| ADP | claude-fable-5 2026-07-21 | 255.24 | 2026-08-18 | +6.00% | +5.51% | +3.42% | +2.10% | HIT | IN_CI | -0.0543 | ORDINARY |
| BAC | claude-fable-5 2026-07-21 | 60.42 | 2026-08-18 | +6.00% | +6.31% | +3.42% | +2.89% | HIT | IN_CI | +0.0547 | ORDINARY |
| BBY | claude-fable-5 2026-07-21 | 85.13 | 2026-08-18 | +5.00% | +2.51% | +3.42% | -0.90% | MISS | IN_CI | -0.3006 | ORDINARY |
| CTAS | claude-fable-5 2026-07-21 | 201.80 | 2026-08-18 | +5.00% | -1.16% | +3.42% | -4.58% | MISS | IN_CI | -0.5549 | ORDINARY |
| DHR | claude-fable-5 2026-07-21 | 201.11 | 2026-08-18 | +5.00% | -0.76% | +3.42% | -4.18% | MISS | IN_CI | -0.6883 | ORDINARY |
| DOC | claude-fable-5 2026-07-21 | 22.29 | 2026-08-18 | +6.00% | -8.30% | +3.42% | -11.72% | MISS | OUT_CI_LOW | -2.0283 | ORDINARY |
| EFX | claude-fable-5 2026-07-21 | 180.08 | 2026-08-18 | +6.00% | +0.98% | +3.42% | -2.44% | MISS | IN_CI | -0.3729 | ORDINARY |
| EG | claude-fable-5 2026-07-21 | 378.99 | 2026-08-18 | +6.00% | -3.06% | +3.42% | -6.48% | MISS | OUT_CI_LOW | -1.2588 | ORDINARY |
| MRSH | claude-fable-5 2026-07-21 | 182.10 | 2026-08-18 | +6.00% | +2.34% | +3.42% | -1.07% | MISS | IN_CI | -0.4270 | ORDINARY |
| MTB | claude-fable-5 2026-07-21 | 249.44 | 2026-08-18 | +6.00% | +0.83% | +3.42% | -2.59% | MISS | IN_CI | -0.8524 | ORDINARY |
| PAYX | claude-fable-5 2026-07-21 | 115.20 | 2026-08-18 | +5.00% | +4.11% | +3.42% | +0.69% | HIT | IN_CI | -0.0998 | ORDINARY |
| PSX | claude-fable-5 2026-07-21 | 208.80 | 2026-08-18 | +5.00% | +16.61% | +3.42% | +13.20% | HIT | OUT_CI_HIGH | +1.1626 | ORDINARY |
| RF | claude-fable-5 2026-07-21 | 31.11 | 2026-08-18 | +6.00% | +1.90% | +3.42% | -1.52% | MISS | IN_CI | -0.6274 | ORDINARY |
| SCHW | claude-fable-5 2026-07-21 | 102.54 | 2026-08-18 | +6.00% | +8.91% | +3.42% | +5.50% | HIT | IN_CI | +0.3911 | ORDINARY |
| STT | claude-fable-5 2026-07-21 | 182.58 | 2026-08-18 | +5.00% | +5.09% | +3.42% | +1.67% | HIT | IN_CI | +0.0125 | ORDINARY |
| TRV | claude-fable-5 2026-07-21 | 368.50 | 2026-08-18 | +5.00% | -0.15% | +3.42% | -3.57% | MISS | IN_CI | -0.5298 | ORDINARY |
| UNP | claude-fable-5 2026-07-21 | 296.25 | 2026-08-18 | +5.00% | +0.84% | +3.42% | -2.58% | MISS | IN_CI | -0.5714 | ORDINARY |
| USB | claude-fable-5 2026-07-21 | 63.14 | 2026-08-18 | +6.00% | +2.61% | +3.42% | -0.80% | MISS | IN_CI | -0.5300 | ORDINARY |
| WRB | claude-fable-5 2026-07-21 | 72.73 | 2026-08-18 | +6.00% | -3.52% | +3.42% | -6.94% | MISS | OUT_CI_LOW | -1.2592 | ORDINARY |
| AAPL | claude-opus-5 2026-07-24 | 333.02 | 2026-08-21 | +2.00% | -7.11% | +3.63% | -10.73% | MISS | IN_CI | -0.9405 | ORDINARY |
| BAC | claude-opus-5 2026-07-24 | 62.05 | 2026-08-21 | +5.00% | -0.58% | +3.63% | -4.21% | MISS | IN_CI | -1.0016 | ORDINARY |
| BNY | claude-opus-5 2026-07-24 | 158.91 | 2026-08-21 | +6.00% | -0.26% | +3.63% | -3.89% | MISS | IN_CI | -0.8483 | ORDINARY |
| CSX | claude-opus-5 2026-07-24 | 53.23 | 2026-08-21 | +6.00% | -3.08% | +3.63% | -6.71% | MISS | OUT_CI_LOW | -1.2578 | ORDINARY |
| CTAS | claude-opus-5 2026-07-24 | 205.91 | 2026-08-21 | +6.00% | -1.03% | +3.63% | -4.66% | MISS | IN_CI | -0.6803 | ORDINARY |
| DGX | claude-opus-5 2026-07-24 | 227.86 | 2026-08-21 | +6.00% | +7.25% | +3.63% | +3.63% | HIT | IN_CI | +0.1304 | ORDINARY |
| GD | claude-opus-5 2026-07-24 | 386.75 | 2026-08-21 | +6.00% | -0.64% | +3.63% | -4.26% | MISS | IN_CI | -0.8761 | ORDINARY |
| HIG | claude-opus-5 2026-07-24 | 140.53 | 2026-08-21 | +6.00% | -3.15% | +3.63% | -6.78% | MISS | OUT_CI_LOW | -1.4618 | ORDINARY |
| JPM | claude-opus-5 2026-07-24 | 353.21 | 2026-08-21 | +5.00% | -0.46% | +3.63% | -4.09% | MISS | IN_CI | -0.8351 | ORDINARY |
| LLY | claude-opus-5 2026-07-24 | 1,196.03 | 2026-08-21 | +2.00% | +4.96% | +3.63% | +1.34% | HIT | IN_CI | +0.3125 | ORDINARY |
| LMT | claude-opus-5 2026-07-24 | 582.60 | 2026-08-21 | +6.00% | -3.27% | +3.63% | -6.89% | MISS | IN_CI | -0.7193 | ORDINARY |
| MET | claude-opus-5 2026-07-24 | 94.83 | 2026-08-21 | +6.00% | -0.52% | +3.63% | -4.14% | MISS | IN_CI | -0.8981 | ORDINARY |
| MPC | claude-opus-5 2026-07-24 | 309.24 | 2026-08-21 | +6.00% | +16.65% | +3.63% | +13.02% | HIT | OUT_CI_HIGH | +1.0977 | ORDINARY |
| MTB | claude-opus-5 2026-07-24 | 249.60 | 2026-08-21 | +6.00% | -3.71% | +3.63% | -7.34% | MISS | OUT_CI_LOW | -1.5240 | ORDINARY |
| NSC | claude-opus-5 2026-07-24 | 350.66 | 2026-08-21 | +6.00% | +0.02% | +3.63% | -3.61% | MISS | IN_CI | -0.8482 | ORDINARY |
| PAYX | claude-opus-5 2026-07-24 | 113.55 | 2026-08-21 | +6.00% | +9.62% | +3.63% | +6.00% | HIT | IN_CI | +0.3834 | ORDINARY |
| PCG | claude-opus-5 2026-07-24 | 17.85 | 2026-08-21 | +6.00% | -1.40% | +3.63% | -5.03% | MISS | IN_CI | -1.0286 | ORDINARY |
| PKG | claude-opus-5 2026-07-24 | 254.39 | 2026-08-21 | +6.00% | -0.63% | +3.63% | -4.25% | MISS | IN_CI | -0.6655 | ORDINARY |
| PM | claude-opus-5 2026-07-24 | 193.00 | 2026-08-21 | +6.00% | -2.47% | +3.63% | -6.10% | MISS | IN_CI | -0.8983 | ORDINARY |
| RTX | claude-opus-5 2026-07-24 | 212.79 | 2026-08-21 | +6.00% | -1.35% | +3.63% | -4.98% | MISS | IN_CI | -0.7539 | ORDINARY |
| SJM | claude-opus-5 2026-07-24 | 118.32 | 2026-08-21 | +6.00% | +5.07% | +3.63% | +1.45% | HIT | IN_CI | -0.0981 | ORDINARY |
| TMO | claude-opus-5 2026-07-24 | 568.26 | 2026-08-21 | +6.00% | +10.74% | +3.63% | +7.11% | HIT | IN_CI | +0.4636 | ORDINARY |
| TRV | claude-opus-5 2026-07-24 | 387.26 | 2026-08-21 | +6.00% | -6.11% | +3.63% | -9.74% | MISS | OUT_CI_LOW | -1.2989 | ORDINARY |
| UNH | claude-opus-5 2026-07-24 | 420.74 | 2026-08-21 | +2.00% | -7.28% | +3.63% | -10.91% | MISS | OUT_CI_LOW | -1.2728 | ORDINARY |
| UNP | claude-opus-5 2026-07-24 | 307.32 | 2026-08-21 | +6.00% | +0.24% | +3.63% | -3.39% | MISS | IN_CI | -0.7876 | ORDINARY |
| VLO | claude-opus-5 2026-07-24 | 302.50 | 2026-08-21 | +6.00% | +15.33% | +3.63% | +11.70% | HIT | IN_CI | +0.7917 | ORDINARY |
| AAPL | claude-sonnet-5 2026-07-22 | 325.89 | 2026-08-19 | +2.00% | -2.78% | +2.89% | -5.67% | MISS | IN_CI | -0.4804 | ORDINARY |
| BAC | claude-sonnet-5 2026-07-22 | 61.66 | 2026-08-19 | +6.00% | +2.46% | +2.89% | -0.43% | MISS | IN_CI | -0.6349 | ORDINARY |
| BBY | claude-sonnet-5 2026-07-22 | 87.11 | 2026-08-19 | +6.00% | +2.40% | +2.89% | -0.48% | MISS | IN_CI | -0.4342 | ORDINARY |
| CRWD | claude-sonnet-5 2026-07-22 | 188.42 | 2026-08-19 | +6.00% | +7.01% | +2.89% | +4.12% | HIT | IN_CI | +0.0635 | ORDINARY |
| CVS | claude-sonnet-5 2026-07-22 | 108.09 | 2026-08-19 | +6.00% | -13.36% | +2.89% | -16.25% | MISS | OUT_CI_LOW | -3.0680 | ORDINARY |
| DDOG | claude-sonnet-5 2026-07-22 | 245.77 | 2026-08-19 | +6.00% | -4.98% | +2.89% | -7.87% | MISS | IN_CI | -0.8894 | ORDINARY |
| DOC | claude-sonnet-5 2026-07-22 | 22.17 | 2026-08-19 | +6.00% | -6.36% | +2.89% | -9.25% | MISS | OUT_CI_LOW | -1.7458 | ORDINARY |
| DVA | claude-sonnet-5 2026-07-22 | 231.95 | 2026-08-19 | +6.00% | -23.57% | +2.89% | -26.46% | MISS | OUT_CI_LOW | -5.0041 | ORDINARY |
| EXPD | claude-sonnet-5 2026-07-22 | 177.53 | 2026-08-19 | +6.00% | +5.02% | +2.89% | +2.13% | HIT | IN_CI | -0.1447 | ORDINARY |
| FTNT | claude-sonnet-5 2026-07-22 | 155.05 | 2026-08-19 | +5.00% | -1.42% | +2.89% | -4.31% | MISS | IN_CI | -0.5825 | ORDINARY |
| GE | claude-sonnet-5 2026-07-22 | 341.23 | 2026-08-19 | +2.00% | +4.40% | +2.89% | +1.51% | HIT | IN_CI | +0.2613 | ORDINARY |
| GEN | claude-sonnet-5 2026-07-22 | 25.58 | 2026-08-19 | +6.00% | +7.66% | +2.89% | +4.78% | HIT | IN_CI | +0.1600 | ORDINARY |
| JPM | claude-sonnet-5 2026-07-22 | 348.35 | 2026-08-19 | +2.00% | +2.56% | +2.89% | -0.33% | MISS | IN_CI | +0.0835 | ORDINARY |
| LLY | claude-sonnet-5 2026-07-22 | 1,163.01 | 2026-08-19 | +1.00% | +10.09% | +2.89% | +7.20% | HIT | IN_CI | +0.9669 | ORDINARY |
| MCO | claude-sonnet-5 2026-07-22 | 489.73 | 2026-08-19 | +6.00% | +1.49% | +2.89% | -1.40% | MISS | IN_CI | -0.4891 | ORDINARY |
| MMM | claude-sonnet-5 2026-07-22 | 170.79 | 2026-08-19 | +6.00% | +5.78% | +2.89% | +2.89% | HIT | IN_CI | -0.0264 | ORDINARY |
| MTB | claude-sonnet-5 2026-07-22 | 250.80 | 2026-08-19 | +6.00% | -2.49% | +2.89% | -5.38% | MISS | OUT_CI_LOW | -1.3921 | ORDINARY |
| PANW | claude-sonnet-5 2026-07-22 | 335.28 | 2026-08-19 | +6.00% | +7.30% | +2.89% | +4.41% | HIT | IN_CI | +0.0830 | ORDINARY |
| PAYX | claude-sonnet-5 2026-07-22 | 110.74 | 2026-08-19 | +6.00% | +10.62% | +2.89% | +7.73% | HIT | IN_CI | +0.4935 | ORDINARY |
| SCHW | claude-sonnet-5 2026-07-22 | 100.80 | 2026-08-19 | +6.00% | +10.00% | +2.89% | +7.11% | HIT | IN_CI | +0.5096 | ORDINARY |
| TMO | claude-sonnet-5 2026-07-22 | 526.71 | 2026-08-19 | +6.00% | +16.49% | +2.89% | +13.60% | HIT | OUT_CI_HIGH | +1.1915 | ORDINARY |
| TRV | claude-sonnet-5 2026-07-22 | 372.06 | 2026-08-19 | +6.00% | -2.64% | +2.89% | -5.53% | MISS | IN_CI | -0.9119 | ORDINARY |
| UNH | claude-sonnet-5 2026-07-22 | 431.33 | 2026-08-19 | +5.00% | -9.90% | +2.89% | -12.79% | MISS | OUT_CI_LOW | -2.0445 | ORDINARY |
| USB | claude-sonnet-5 2026-07-22 | 64.47 | 2026-08-19 | +6.00% | -2.55% | +2.89% | -5.44% | MISS | OUT_CI_LOW | -1.3362 | ORDINARY |
| V | claude-sonnet-5 2026-07-22 | 353.47 | 2026-08-19 | +1.00% | +3.41% | +2.89% | +0.53% | HIT | IN_CI | +0.3588 | ORDINARY |
| VTRS | claude-sonnet-5 2026-07-22 | 17.01 | 2026-08-19 | +6.00% | -4.50% | +2.89% | -7.38% | MISS | OUT_CI_LOW | -1.1970 | ORDINARY |
| AMCR | gpt-5 2026-07-20 | 43.94 | 2026-08-17 | +6.00% | +3.62% | +3.95% | -0.33% | MISS | IN_CI | -0.2535 | ORDINARY |
| BAC | gpt-5 2026-07-20 | 61.27 | 2026-08-17 | +5.00% | +4.28% | +3.95% | +0.32% | HIT | IN_CI | -0.1223 | ORDINARY |
| BBY | gpt-5 2026-07-20 | 85.41 | 2026-08-17 | +5.00% | +0.04% | +3.95% | -3.92% | MISS | IN_CI | -0.5947 | ORDINARY |
| CRWD | gpt-5 2026-07-20 | 203.08 | 2026-08-17 | +6.00% | +5.33% | +3.95% | +1.38% | HIT | IN_CI | -0.0398 | ORDINARY |
| CTAS | gpt-5 2026-07-20 | 204.45 | 2026-08-17 | +5.00% | -3.24% | +3.95% | -7.20% | MISS | IN_CI | -0.7352 | ORDINARY |
| DOC | gpt-5 2026-07-20 | 22.51 | 2026-08-17 | +5.00% | -8.57% | +3.95% | -12.53% | MISS | OUT_CI_LOW | -1.8849 | ORDINARY |
| DVA | gpt-5 2026-07-20 | 236.97 | 2026-08-17 | +5.00% | -25.43% | +3.95% | -29.39% | MISS | OUT_CI_LOW | -5.0934 | ORDINARY |
| EXPD | gpt-5 2026-07-20 | 182.80 | 2026-08-17 | +5.00% | +2.99% | +3.95% | -0.96% | MISS | IN_CI | -0.3266 | ORDINARY |
| FITB | gpt-5 2026-07-20 | 58.01 | 2026-08-17 | +6.00% | -0.71% | +3.95% | -4.66% | MISS | IN_CI | -0.8388 | ORDINARY |
| GEN | gpt-5 2026-07-20 | 26.74 | 2026-08-17 | +6.00% | +2.51% | +3.95% | -1.45% | MISS | IN_CI | -0.3409 | ORDINARY |
| JBHT | gpt-5 2026-07-20 | 291.41 | 2026-08-17 | +6.00% | -2.76% | +3.95% | -6.71% | MISS | IN_CI | -0.8258 | ORDINARY |
| JPM | gpt-5 2026-07-20 | 341.10 | 2026-08-17 | +2.00% | +5.82% | +3.95% | +1.87% | HIT | IN_CI | +0.5489 | ORDINARY |
| LLY | gpt-5 2026-07-20 | 1,179.11 | 2026-08-17 | +4.00% | +0.34% | +3.95% | -3.61% | MISS | IN_CI | -0.3844 | ORDINARY |
| MNST | gpt-5 2026-07-20 | 97.50 | 2026-08-17 | +5.00% | -53.31% | +3.95% | -57.27% | MISS | OUT_CI_LOW | -10.6560 | ORDINARY |
| MPC | gpt-5 2026-07-20 | 312.60 | 2026-08-17 | +5.00% | +14.58% | +3.95% | +10.63% | HIT | IN_CI | +0.9417 | ORDINARY |
| PANW | gpt-5 2026-07-20 | 358.68 | 2026-08-17 | +5.00% | +4.76% | +3.95% | +0.81% | HIT | IN_CI | -0.0153 | ORDINARY |
| PAYX | gpt-5 2026-07-20 | 114.39 | 2026-08-17 | +5.00% | +3.63% | +3.95% | -0.32% | MISS | IN_CI | -0.1530 | ORDINARY |
| PRU | gpt-5 2026-07-20 | 119.07 | 2026-08-17 | +5.00% | +4.61% | +3.95% | +0.66% | HIT | IN_CI | -0.0614 | ORDINARY |
| RF | gpt-5 2026-07-20 | 31.65 | 2026-08-17 | +6.00% | +0.16% | +3.95% | -3.79% | MISS | IN_CI | -0.8458 | ORDINARY |
| STT | gpt-5 2026-07-20 | 182.50 | 2026-08-17 | +5.00% | +5.78% | +3.95% | +1.82% | HIT | IN_CI | +0.1052 | ORDINARY |
| TRV | gpt-5 2026-07-20 | 368.98 | 2026-08-17 | +5.00% | -1.21% | +3.95% | -5.16% | MISS | IN_CI | -0.6400 | ORDINARY |
| UNH | gpt-5 2026-07-20 | 426.09 | 2026-08-17 | +5.00% | -7.15% | +3.95% | -11.10% | MISS | OUT_CI_LOW | -1.5515 | ORDINARY |
| USB | gpt-5 2026-07-20 | 63.14 | 2026-08-17 | +6.00% | +2.74% | +3.95% | -1.21% | MISS | IN_CI | -0.4548 | ORDINARY |
| ADP | gpt-5 2026-07-21 | 255.24 | 2026-08-18 | +6.00% | +5.51% | +3.42% | +2.10% | HIT | IN_CI | -0.0543 | ORDINARY |
| BAC | gpt-5 2026-07-21 | 60.42 | 2026-08-18 | +6.00% | +6.31% | +3.42% | +2.89% | HIT | IN_CI | +0.0547 | ORDINARY |
| BBY | gpt-5 2026-07-21 | 85.13 | 2026-08-18 | +5.00% | +2.51% | +3.42% | -0.90% | MISS | IN_CI | -0.3007 | ORDINARY |
| BNY | gpt-5 2026-07-21 | 156.93 | 2026-08-18 | +5.00% | +4.46% | +3.42% | +1.04% | HIT | IN_CI | -0.0692 | ORDINARY |
| CVS | gpt-5 2026-07-21 | 107.61 | 2026-08-18 | +5.00% | -11.80% | +3.42% | -15.22% | MISS | OUT_CI_LOW | -2.7876 | ORDINARY |
| DDOG | gpt-5 2026-07-21 | 263.20 | 2026-08-18 | +5.00% | -6.53% | +3.42% | -9.95% | MISS | IN_CI | -0.9221 | ORDINARY |
| DOC | gpt-5 2026-07-21 | 22.29 | 2026-08-18 | +6.00% | -8.30% | +3.42% | -11.72% | MISS | OUT_CI_LOW | -2.0284 | ORDINARY |
| GEN | gpt-5 2026-07-21 | 26.68 | 2026-08-18 | +6.00% | +3.60% | +3.42% | +0.18% | HIT | IN_CI | -0.2343 | ORDINARY |
| GPN | gpt-5 2026-07-21 | 82.37 | 2026-08-18 | +6.00% | +9.71% | +3.42% | +6.29% | HIT | IN_CI | +0.2812 | ORDINARY |
| JPM | gpt-5 2026-07-21 | 338.87 | 2026-08-18 | +1.00% | +7.19% | +3.42% | +3.78% | HIT | IN_CI | +0.9464 | ORDINARY |
| KEY | gpt-5 2026-07-21 | 23.32 | 2026-08-18 | +6.00% | -2.27% | +3.42% | -5.69% | MISS | OUT_CI_LOW | -1.4762 | ORDINARY |
| LLY | gpt-5 2026-07-21 | 1,146.90 | 2026-08-18 | +5.00% | +6.87% | +3.42% | +3.46% | HIT | IN_CI | +0.2038 | ORDINARY |
| MET | gpt-5 2026-07-21 | 92.99 | 2026-08-18 | +5.00% | +4.02% | +3.42% | +0.60% | HIT | IN_CI | -0.1384 | ORDINARY |
| MTB | gpt-5 2026-07-21 | 249.44 | 2026-08-18 | +6.00% | +0.83% | +3.42% | -2.59% | MISS | IN_CI | -0.8521 | ORDINARY |
| PANW | gpt-5 2026-07-21 | 348.66 | 2026-08-18 | +5.00% | +7.31% | +3.42% | +3.89% | HIT | IN_CI | +0.1463 | ORDINARY |
| PAYX | gpt-5 2026-07-21 | 115.20 | 2026-08-18 | +5.00% | +4.11% | +3.42% | +0.69% | HIT | IN_CI | -0.0998 | ORDINARY |
| PSX | gpt-5 2026-07-21 | 208.80 | 2026-08-18 | +5.00% | +16.61% | +3.42% | +13.20% | HIT | OUT_CI_HIGH | +1.1629 | ORDINARY |
| RF | gpt-5 2026-07-21 | 31.11 | 2026-08-18 | +6.00% | +1.90% | +3.42% | -1.52% | MISS | IN_CI | -0.6276 | ORDINARY |
| SCHW | gpt-5 2026-07-21 | 102.54 | 2026-08-18 | +6.00% | +8.91% | +3.42% | +5.50% | HIT | IN_CI | +0.3913 | ORDINARY |
| STT | gpt-5 2026-07-21 | 182.58 | 2026-08-18 | +5.00% | +5.09% | +3.42% | +1.67% | HIT | IN_CI | +0.0125 | ORDINARY |
| TRV | gpt-5 2026-07-21 | 368.50 | 2026-08-18 | +5.00% | -0.15% | +3.42% | -3.57% | MISS | IN_CI | -0.5297 | ORDINARY |
| UNH | gpt-5 2026-07-21 | 421.55 | 2026-08-18 | +5.00% | -6.55% | +3.42% | -9.97% | MISS | OUT_CI_LOW | -1.7084 | ORDINARY |
| USB | gpt-5 2026-07-21 | 63.14 | 2026-08-18 | +6.00% | +2.61% | +3.42% | -0.80% | MISS | IN_CI | -0.5300 | ORDINARY |
| A | gpt-5 2026-07-22 | 133.46 | 2026-08-19 | +6.00% | +16.45% | +2.90% | +13.55% | HIT | OUT_CI_HIGH | +1.2224 | ORDINARY |
| AAPL | gpt-5 2026-07-22 | 325.89 | 2026-08-19 | +4.00% | -2.78% | +2.90% | -5.68% | MISS | IN_CI | -0.6912 | ORDINARY |
| BAC | gpt-5 2026-07-22 | 61.62 | 2026-08-19 | +6.00% | +2.52% | +2.90% | -0.38% | MISS | IN_CI | -0.6296 | ORDINARY |
| BBY | gpt-5 2026-07-22 | 87.11 | 2026-08-19 | +5.00% | +2.41% | +2.90% | -0.49% | MISS | IN_CI | -0.3248 | ORDINARY |
| BNY | gpt-5 2026-07-22 | 160.39 | 2026-08-19 | +5.00% | -0.39% | +2.90% | -3.29% | MISS | IN_CI | -0.6991 | ORDINARY |
| CTAS | gpt-5 2026-07-22 | 201.36 | 2026-08-19 | +6.00% | +0.85% | +2.90% | -2.04% | MISS | IN_CI | -0.4839 | ORDINARY |
| DDOG | gpt-5 2026-07-22 | 245.77 | 2026-08-19 | +6.00% | -4.98% | +2.90% | -7.88% | MISS | IN_CI | -0.8633 | ORDINARY |
| DOC | gpt-5 2026-07-22 | 22.19 | 2026-08-19 | +6.00% | -6.44% | +2.90% | -9.34% | MISS | OUT_CI_LOW | -1.7001 | ORDINARY |
| DVA | gpt-5 2026-07-22 | 232.08 | 2026-08-19 | +5.00% | -23.62% | +2.90% | -26.51% | MISS | OUT_CI_LOW | -4.4956 | ORDINARY |
| GEN | gpt-5 2026-07-22 | 25.58 | 2026-08-19 | +6.00% | +7.66% | +2.90% | +4.77% | HIT | IN_CI | +0.1592 | ORDINARY |
| GS | gpt-5 2026-07-22 | 1,098.20 | 2026-08-19 | +1.00% | -6.97% | +2.90% | -9.87% | MISS | IN_CI | -0.6568 | ORDINARY |
| IVZ | gpt-5 2026-07-22 | 30.50 | 2026-08-19 | +6.00% | +5.61% | +2.90% | +2.71% | HIT | IN_CI | -0.0347 | ORDINARY |
| JBHT | gpt-5 2026-07-22 | 292.24 | 2026-08-19 | +5.00% | -6.78% | +2.90% | -9.68% | MISS | OUT_CI_LOW | -1.1157 | ORDINARY |
| JPM | gpt-5 2026-07-22 | 348.21 | 2026-08-19 | +2.00% | +2.60% | +2.90% | -0.30% | MISS | IN_CI | +0.0900 | ORDINARY |
| LLY | gpt-5 2026-07-22 | 1,163.01 | 2026-08-19 | +2.00% | +10.09% | +2.90% | +7.19% | HIT | IN_CI | +0.8629 | ORDINARY |
| MMM | gpt-5 2026-07-22 | 170.76 | 2026-08-19 | +6.00% | +5.80% | +2.90% | +2.90% | HIT | IN_CI | -0.0242 | ORDINARY |
| MTB | gpt-5 2026-07-22 | 250.73 | 2026-08-19 | +6.00% | -2.46% | +2.90% | -5.36% | MISS | OUT_CI_LOW | -1.3860 | ORDINARY |
| PAYX | gpt-5 2026-07-22 | 110.74 | 2026-08-19 | +5.00% | +10.62% | +2.90% | +7.72% | HIT | IN_CI | +0.6048 | ORDINARY |
| RF | gpt-5 2026-07-22 | 30.86 | 2026-08-19 | +6.00% | -0.87% | +2.90% | -3.77% | MISS | IN_CI | -1.0386 | ORDINARY |
| SJM | gpt-5 2026-07-22 | 118.05 | 2026-08-19 | +6.00% | +4.06% | +2.90% | +1.16% | HIT | IN_CI | -0.1497 | ORDINARY |
| STT | gpt-5 2026-07-22 | 185.24 | 2026-08-19 | +5.00% | +0.31% | +2.90% | -2.59% | MISS | IN_CI | -0.6716 | ORDINARY |
| TRV | gpt-5 2026-07-22 | 372.08 | 2026-08-19 | +5.00% | -2.65% | +2.90% | -5.55% | MISS | IN_CI | -0.8352 | ORDINARY |
| UNH | gpt-5 2026-07-22 | 431.31 | 2026-08-19 | +4.00% | -9.90% | +2.90% | -12.80% | MISS | OUT_CI_LOW | -1.9099 | ORDINARY |
| USB | gpt-5 2026-07-22 | 64.47 | 2026-08-19 | +5.00% | -2.56% | +2.90% | -5.46% | MISS | OUT_CI_LOW | -1.1883 | ORDINARY |
| V | gpt-5 2026-07-22 | 353.42 | 2026-08-19 | +1.00% | +3.43% | +2.90% | +0.53% | HIT | IN_CI | +0.3648 | ORDINARY |
| VTRS | gpt-5 2026-07-22 | 17.01 | 2026-08-19 | +5.00% | -4.50% | +2.90% | -7.39% | MISS | IN_CI | -1.0228 | ORDINARY |
| AAPL | gpt-5 2026-07-24 | 333.02 | 2026-08-21 | +4.00% | -7.11% | +3.63% | -10.73% | MISS | OUT_CI_LOW | -1.1471 | ORDINARY |
| AMCR | gpt-5 2026-07-24 | 44.54 | 2026-08-21 | +6.00% | +9.09% | +3.63% | +5.47% | HIT | IN_CI | +0.3146 | ORDINARY |
| AMP | gpt-5 2026-07-24 | 528.90 | 2026-08-21 | +6.00% | +5.05% | +3.63% | +1.42% | HIT | IN_CI | -0.1197 | ORDINARY |
| BAC | gpt-5 2026-07-24 | 62.05 | 2026-08-21 | +4.00% | -0.58% | +3.63% | -4.21% | MISS | IN_CI | -0.8221 | ORDINARY |
| BBY | gpt-5 2026-07-24 | 85.43 | 2026-08-21 | +6.00% | +0.54% | +3.63% | -3.09% | MISS | IN_CI | -0.6410 | ORDINARY |
| BX | gpt-5 2026-07-24 | 130.00 | 2026-08-21 | +6.00% | +10.29% | +3.63% | +6.67% | HIT | IN_CI | +0.4281 | ORDINARY |
| CSX | gpt-5 2026-07-24 | 53.23 | 2026-08-21 | +5.00% | -3.08% | +3.63% | -6.71% | MISS | OUT_CI_LOW | -1.1191 | ORDINARY |
| DGX | gpt-5 2026-07-24 | 227.86 | 2026-08-21 | +5.00% | +7.25% | +3.63% | +3.63% | HIT | IN_CI | +0.2344 | ORDINARY |
| DOC | gpt-5 2026-07-24 | 22.27 | 2026-08-21 | +6.00% | -3.91% | +3.63% | -7.53% | MISS | OUT_CI_LOW | -1.4607 | ORDINARY |
| DVA | gpt-5 2026-07-24 | 235.44 | 2026-08-21 | +5.00% | -26.17% | +3.63% | -29.80% | MISS | OUT_CI_LOW | -5.2181 | ORDINARY |
| GD | gpt-5 2026-07-24 | 386.75 | 2026-08-21 | +5.00% | -0.64% | +3.63% | -4.26% | MISS | IN_CI | -0.7441 | ORDINARY |
| HPQ | gpt-5 2026-07-24 | 25.75 | 2026-08-21 | +6.00% | +15.38% | +3.63% | +11.75% | HIT | IN_CI | +0.8925 | ORDINARY |
| JPM | gpt-5 2026-07-24 | 353.21 | 2026-08-21 | +4.00% | -0.46% | +3.63% | -4.09% | MISS | IN_CI | -0.6822 | ORDINARY |
| LLY | gpt-5 2026-07-24 | 1,196.03 | 2026-08-21 | +5.00% | +4.96% | +3.63% | +1.34% | HIT | IN_CI | -0.0038 | ORDINARY |
| MTB | gpt-5 2026-07-24 | 249.60 | 2026-08-21 | +6.00% | -3.71% | +3.63% | -7.34% | MISS | OUT_CI_LOW | -1.5240 | ORDINARY |
| PAYX | gpt-5 2026-07-24 | 113.55 | 2026-08-21 | +5.00% | +9.62% | +3.63% | +6.00% | HIT | IN_CI | +0.4892 | ORDINARY |
| PCG | gpt-5 2026-07-24 | 17.85 | 2026-08-21 | +6.00% | -1.40% | +3.63% | -5.03% | MISS | IN_CI | -1.0286 | ORDINARY |
| PKG | gpt-5 2026-07-24 | 254.39 | 2026-08-21 | +5.00% | -0.63% | +3.63% | -4.25% | MISS | IN_CI | -0.5651 | ORDINARY |
| RTX | gpt-5 2026-07-24 | 212.79 | 2026-08-21 | +5.00% | -1.35% | +3.63% | -4.98% | MISS | IN_CI | -0.6514 | ORDINARY |
| STT | gpt-5 2026-07-24 | 185.40 | 2026-08-21 | +5.00% | +0.93% | +3.63% | -2.69% | MISS | IN_CI | -0.5862 | ORDINARY |
| TMO | gpt-5 2026-07-24 | 568.26 | 2026-08-21 | +5.00% | +10.74% | +3.63% | +7.11% | HIT | IN_CI | +0.5614 | ORDINARY |
| TRV | gpt-5 2026-07-24 | 387.26 | 2026-08-21 | +5.00% | -6.11% | +3.63% | -9.74% | MISS | OUT_CI_LOW | -1.1917 | ORDINARY |
| UNH | gpt-5 2026-07-24 | 420.74 | 2026-08-21 | +3.00% | -7.28% | +3.63% | -10.91% | MISS | OUT_CI_LOW | -1.4100 | ORDINARY |
| UNP | gpt-5 2026-07-24 | 307.32 | 2026-08-21 | +5.00% | +0.24% | +3.63% | -3.39% | MISS | IN_CI | -0.6509 | ORDINARY |
| V | gpt-5 2026-07-24 | 355.74 | 2026-08-21 | +2.00% | +4.30% | +3.63% | +0.68% | HIT | IN_CI | +0.3493 | ORDINARY |
| WAB | gpt-5 2026-07-24 | 302.50 | 2026-08-21 | +5.00% | -1.63% | +3.63% | -5.26% | MISS | IN_CI | -0.5970 | ORDINARY |
| QQQ | claude-fable-5 2026-07-20 | 695.33 | 2026-08-17 | +0.37% | +4.97% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.5183 | ORDINARY |
| SOXX | claude-fable-5 2026-07-20 | 521.81 | 2026-08-17 | +0.35% | +7.15% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.3085 | ORDINARY |
| SPY | claude-fable-5 2026-07-20 | 743.29 | 2026-08-17 | +0.50% | +3.95% | N/A | N/A | HIT | IN_CI | +0.7605 | ORDINARY |
| QQQ | claude-fable-5 2026-07-21 | 696.06 | 2026-08-18 | +0.37% | +3.08% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.3057 | ORDINARY |
| SOXX | claude-fable-5 2026-07-21 | 524.14 | 2026-08-18 | +0.37% | +1.38% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.0461 | ORDINARY |
| SPY | claude-fable-5 2026-07-21 | 742.09 | 2026-08-18 | +0.50% | +3.42% | N/A | N/A | HIT | IN_CI | +0.6454 | ORDINARY |
| QQQ | claude-opus-5 2026-07-24 | 684.23 | 2026-08-21 | -1.00% | +4.27% | N/A | N/A | MISS | IN_CI | +0.6620 | ORDINARY |
| SOXX | claude-opus-5 2026-07-24 | 527.01 | 2026-08-21 | -1.50% | -1.32% | N/A | N/A | HIT | IN_CI | +0.0089 | ORDINARY |
| SPY | claude-opus-5 2026-07-24 | 738.93 | 2026-08-21 | +0.00% | +3.63% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.9254 | ORDINARY |
| QQQ | claude-sonnet-5 2026-07-22 | 705.35 | 2026-08-19 | +0.87% | +1.52% | N/A | N/A | HIT | IN_CI | +0.0806 | ORDINARY |
| SOXX | claude-sonnet-5 2026-07-22 | 555.52 | 2026-08-19 | +1.91% | -6.45% | N/A | N/A | MISS | IN_CI | -0.4040 | ORDINARY |
| SPY | claude-sonnet-5 2026-07-22 | 747.48 | 2026-08-19 | +0.50% | +2.89% | N/A | N/A | HIT | IN_CI | +0.5938 | ORDINARY |
| QQQ | gpt-5 2026-07-20 | 695.33 | 2026-08-17 | +0.37% | +4.97% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.5182 | ORDINARY |
| SOXX | gpt-5 2026-07-20 | 521.81 | 2026-08-17 | +0.35% | +7.15% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.3086 | ORDINARY |
| SPY | gpt-5 2026-07-20 | 743.29 | 2026-08-17 | +0.50% | +3.95% | N/A | N/A | HIT | IN_CI | +0.7611 | ORDINARY |
| QQQ | gpt-5 2026-07-21 | 696.06 | 2026-08-18 | +0.37% | +3.08% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.3061 | ORDINARY |
| SOXX | gpt-5 2026-07-21 | 524.14 | 2026-08-18 | +0.37% | +1.38% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.0462 | ORDINARY |
| SPY | gpt-5 2026-07-21 | 742.09 | 2026-08-18 | +0.50% | +3.42% | N/A | N/A | HIT | IN_CI | +0.6450 | ORDINARY |
| QQQ | gpt-5 2026-07-22 | 705.35 | 2026-08-19 | +0.37% | +1.52% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.1447 | ORDINARY |
| SOXX | gpt-5 2026-07-22 | 555.52 | 2026-08-19 | +0.39% | -6.45% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.3403 | ORDINARY |
| SPY | gpt-5 2026-07-22 | 747.41 | 2026-08-19 | +0.50% | +2.90% | N/A | N/A | HIT | IN_CI | +0.5963 | ORDINARY |
| QQQ | gpt-5 2026-07-24 | 684.23 | 2026-08-21 | +0.36% | +4.27% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.4910 | ORDINARY |
| SOXX | gpt-5 2026-07-24 | 527.01 | 2026-08-21 | +0.32% | -1.32% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.0812 | ORDINARY |
| SPY | gpt-5 2026-07-24 | 738.93 | 2026-08-21 | +0.50% | +3.63% | N/A | N/A | HIT | IN_CI | +0.7978 | ORDINARY |

## 1. Prior Run Summary

The MoM window is `2026-08-22 − 45d` … `2026-08-22 − 21d` = **2026-07-08 … 2026-08-01**, target
**2026-07-25**. Two same-model folders tie at `|folder_date − target| = 1d`, so
**tie-break rule 8 applies** and every tied candidate is disclosed below.

| Tied candidate | Date | Delta | Usable 15_predictions.json | Equity records | MoM hit rate | Mean alpha | Mean MoM return | Canonical settled n |
|---|---|---|---|---|---|---|---|---|
| **claude-opus-5-2026-07-24** (selected) | 2026-07-24 | 1d | Yes | 26 | 26.9% | -2.59% | +1.03% | 26 |
| claude-opus-5-2026-07-26 | 2026-07-26 | 1d | Yes | 24 | 26.1% | -2.54% | +1.09% | 0 |

Rule 8 resolution: (a) both are the same model family as the executing model — tie stands;
(b) both carry a usable `15_predictions.json` — tie stands; (c) lexicographic →
**`claude-opus-5-2026-07-24`**.

**Is the MoM conclusion invariant across the tied books? Yes.** The hit-rate spread is
**0.8pp** (26.9% vs 26.1%) and mean alpha differs by
0.06pp; both books underperformed SPY materially and both sit far
below the 50% bar. That is a much tighter tie than the 48pp (2026-07-29) and 40.7pp (2026-07-30)
spreads that motivated the rule — the two books here share a defensive composition rather than
being near-disjoint.

One asymmetry is worth recording because it argues the lexicographic winner was also the
substantively better choice: `claude-opus-5-2026-07-24`'s predictions matured **exactly on this run's basis
date** (target 2026-08-21) and are fully settled in the canonical ledger
(`settled_n = 26`), whereas `claude-opus-5-2026-07-26`'s target date is 2026-08-23 and is **not yet
due** (`settled_n = 0`) — its column above is a mark-to-market against the basis close,
not a settlement.

**Prior run** (`claude-opus-5-2026-07-24`): status **NO_TRADE**, regime **`NEUTRAL`**, universe
`INDEX_UNION_PCTL`, 0 investable / 23 monitored equities plus 3 core-ETF forecasts.
Its thesis cluster was uniform: *low/negative-beta defensives outperforming a flat index during a
growth unwind*. Top-5 by `adj_score`: `TRV` 0.3680, `PAYX` 0.3037, `DGX` 0.3028, `UNP` 0.2991, `PCG` 0.2798.

## 2. MoM Price & Return Table

Prior price = each record's own grounded `entry_price` (2026-07-24 close). Current price = the
**2026-08-21** raw close (L002/L011/L012, 0.000000% max cross-vendor deviation).
Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`, never raw return.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI |
|---|---|---|---|---|---|---|---|---|---|
| TRV | 2026-07-24 | 387.26 | 2026-08-21 | 363.58 | -6.11% | +3.63% | -9.74% | MISS | OUT_CI |
| PAYX | 2026-07-24 | 113.55 | 2026-08-21 | 124.47 | +9.62% | +3.63% | +6.00% | HIT | IN_CI |
| DGX | 2026-07-24 | 227.86 | 2026-08-21 | 244.39 | +7.25% | +3.63% | +3.63% | HIT | IN_CI |
| UNP | 2026-07-24 | 307.32 | 2026-08-21 | 308.05 | +0.24% | +3.63% | -3.39% | MISS | IN_CI |
| PCG | 2026-07-24 | 17.85 | 2026-08-21 | 17.60 | -1.40% | +3.63% | -5.03% | MISS | IN_CI |
| RTX | 2026-07-24 | 212.79 | 2026-08-21 | 209.91 | -1.35% | +3.63% | -4.98% | MISS | IN_CI |
| NSC | 2026-07-24 | 350.66 | 2026-08-21 | 350.72 | +0.02% | +3.63% | -3.61% | MISS | IN_CI |
| GD | 2026-07-24 | 386.75 | 2026-08-21 | 384.29 | -0.64% | +3.63% | -4.26% | MISS | IN_CI |
| CSX | 2026-07-24 | 53.23 | 2026-08-21 | 51.59 | -3.08% | +3.63% | -6.71% | MISS | OUT_CI |
| CTAS | 2026-07-24 | 205.91 | 2026-08-21 | 203.79 | -1.03% | +3.63% | -4.66% | MISS | IN_CI |
| PM | 2026-07-24 | 193.00 | 2026-08-21 | 188.23 | -2.47% | +3.63% | -6.10% | MISS | IN_CI |
| MPC | 2026-07-24 | 309.24 | 2026-08-21 | 360.72 | +16.65% | +3.63% | +13.02% | HIT | OUT_CI |
| LMT | 2026-07-24 | 582.60 | 2026-08-21 | 563.57 | -3.27% | +3.63% | -6.89% | MISS | IN_CI |
| PKG | 2026-07-24 | 254.39 | 2026-08-21 | 252.79 | -0.63% | +3.63% | -4.25% | MISS | IN_CI |
| TMO | 2026-07-24 | 568.26 | 2026-08-21 | 629.27 | +10.74% | +3.63% | +7.11% | HIT | IN_CI |
| SJM | 2026-07-24 | 118.32 | 2026-08-21 | 124.32 | +5.07% | +3.63% | +1.45% | HIT | IN_CI |
| BNY | 2026-07-24 | 158.91 | 2026-08-21 | 158.49 | -0.26% | +3.63% | -3.89% | MISS | IN_CI |
| VLO | 2026-07-24 | 302.50 | 2026-08-21 | 348.86 | +15.33% | +3.63% | +11.70% | HIT | IN_CI |
| MTB | 2026-07-24 | 249.60 | 2026-08-21 | 240.34 | -3.71% | +3.63% | -7.34% | MISS | OUT_CI |
| MET | 2026-07-24 | 94.83 | 2026-08-21 | 94.34 | -0.52% | +3.63% | -4.14% | MISS | IN_CI |
| HIG | 2026-07-24 | 140.53 | 2026-08-21 | 136.10 | -3.15% | +3.63% | -6.78% | MISS | OUT_CI |
| BAC | 2026-07-24 | 62.05 | 2026-08-21 | 61.69 | -0.58% | +3.63% | -4.21% | MISS | IN_CI |
| JPM | 2026-07-24 | 353.21 | 2026-08-21 | 351.58 | -0.46% | +3.63% | -4.09% | MISS | IN_CI |
| AAPL | 2026-07-24 | 333.02 | 2026-08-21 | 309.35 | -7.11% | +3.63% | -10.73% | MISS | IN_CI |
| UNH | 2026-07-24 | 420.74 | 2026-08-21 | 390.11 | -7.28% | +3.63% | -10.91% | MISS | OUT_CI |
| LLY | 2026-07-24 | 1,196.03 | 2026-08-21 | 1,255.40 | +4.96% | +3.63% | +1.34% | HIT | IN_CI |

Book aggregate: mean MoM return **+1.03%**, mean alpha **-2.59%**,
hit rate **26.9%** over 26 names. The book made money in absolute terms and
still lost decisively to SPY — precisely the distinction the IR objective exists to capture, and the
reason raw-return scoring is prohibited.

## 3. Theme-Level Performance

| Theme cluster | Names | Hit rate | Mean alpha | Verdict |
|---|---|---|---|---|
| Industrials | 8 | 25.0% | -2.09% | partial |
| Finance | 7 | 0.0% | -5.74% | failed |
| sector UNAVAILABLE | 4 | 25.0% | -5.04% | partial |
| Health Care | 2 | 50.0% | -3.64% | partial |
| Energy | 2 | 100.0% | +12.36% | validated |
| Utilities | 1 | 0.0% | -5.03% | failed |
| Consumer Discretionary | 1 | 0.0% | -4.25% | failed |
| Consumer Staples | 1 | 100.0% | +1.45% | validated |

The single theme carried the whole book, so there is no cross-theme dispersion to learn from. Its
verdict is **failed**: the defensive/low-beta tilt was the correct read of the *prior* regime
(`NEUTRAL`, growth unwinding) and the wrong position for the window that followed, in which the
index re-established a `BULL` trend and the growth complex recovered. The failure is a regime-timing
failure, not a stock-selection failure — consistent with `claude-opus-5-2026-07-24`'s own positive vintage
rank IC of +0.1330: the ordering *within* the book was informative even though the book's
aggregate alpha was -2.59%.

## 4. Regime Shift Assessment

| Dimension | Prior (2026-07-24) | Current (2026-08-21) | Shift |
|---|---|---|---|
| Declared regime | `NEUTRAL` | `BULL` | **Yes — NEUTRAL → BULL** |
| SPY vs MA20 / MA50 | 738.93 vs 746.15 / 745.07 — below both, `MIXED` | 765.72 vs 762.33 / 751.56 — above both, `BULLISH` | Alignment recovered |
| SPY 60d momentum | +3.83% | +2.29% | Lower but still positive |
| SPY 20d momentum | +0.63% | +3.63% | Materially stronger |
| SPY daily MACD | `BELOW_SIGNAL` | `BELOW_SIGNAL` | Unchanged state |
| VIX | 18.58 | 15.13 (prior close 16.01) | Fell ~3.4 points |
| SPY 30d realized vol (1m) | 3.92%, rising | 3.56%, falling from 4.41% | Compressed |
| SOXX/SPY 60d RS | deeply negative (SOXX −19.54% drawdown) | -9.81% | Still negative, much less extreme |

**Factor-weight implication.** The `NEUTRAL → BULL` shift with compressing volatility argues
*against* the defensive tilt that `Tech_Z` produced last month and is producing again this month.
No factor weights are changed on this evidence: family weights are protected under
`rules.md § Evolution Policy`, and a regime read is not the settled-prediction evidence a Track A
change requires (eff_n = 2 < 3). The observation is logged in `13` instead.

## 5. Carry-Forward Decisions

Binding on factor scoring where ledger-backed. `DROP` names stay out of today's scored set absent
new ledger evidence. Ranks below are this run's, regenerated from
`run_computed_manifest.json` — not transcribed.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| TRV | 0.3680 | low/negative-beta defensive | -6.11% | DROP | re-ranks at #270 (47.05 pctl) — below the 60th-pctl rank floor |
| PAYX | 0.3037 | low/negative-beta defensive | +9.62% | DOWNGRADE | re-ranks at #124 (75.79 pctl) — below the published set, still rankable |
| DGX | 0.3028 | low/negative-beta defensive | +7.25% | DOWNGRADE | re-ranks at #36 (93.11 pctl) — below the published set, still rankable |
| UNP | 0.2991 | low/negative-beta defensive | +0.24% | DOWNGRADE | re-ranks at #81 (84.25 pctl) — below the published set, still rankable |
| PCG | 0.2798 | low/negative-beta defensive | -1.40% | DOWNGRADE | re-ranks at #183 (64.17 pctl) — below the published set, still rankable |
| RTX | 0.2598 | low/negative-beta defensive | -1.35% | DOWNGRADE | re-ranks at #182 (64.37 pctl) — below the published set, still rankable |
| NSC | 0.2571 | low/negative-beta defensive | +0.02% | DOWNGRADE | re-ranks at #166 (67.52 pctl) — below the published set, still rankable |
| GD | 0.2337 | low/negative-beta defensive | -0.64% | DOWNGRADE | re-ranks at #143 (72.05 pctl) — below the published set, still rankable |
| CSX | 0.2315 | low/negative-beta defensive | -3.08% | DOWNGRADE | re-ranks at #155 (69.69 pctl) — below the published set, still rankable |
| CTAS | 0.2279 | low/negative-beta defensive | -1.03% | DROP | re-ranks at #280 (45.08 pctl) — below the 60th-pctl rank floor |
| PM | 0.2272 | low/negative-beta defensive | -2.47% | DROP | re-ranks at #245 (51.97 pctl) — below the 60th-pctl rank floor |
| MPC | 0.2224 | low/negative-beta defensive | +16.65% | CARRY | re-ranks at #21 (96.06 pctl) — inside the published 24 |
| LMT | 0.2155 | low/negative-beta defensive | -3.27% | DROP | re-ranks at #259 (49.21 pctl) — below the 60th-pctl rank floor |
| PKG | 0.2063 | low/negative-beta defensive | -0.63% | DROP | re-ranks at #222 (56.50 pctl) — below the 60th-pctl rank floor |
| TMO | 0.2025 | low/negative-beta defensive | +10.74% | DOWNGRADE | re-ranks at #65 (87.40 pctl) — below the published set, still rankable |
| SJM | 0.1974 | low/negative-beta defensive | +5.07% | DOWNGRADE | re-ranks at #140 (72.64 pctl) — below the published set, still rankable |
| BNY | 0.1962 | low/negative-beta defensive | -0.26% | DOWNGRADE | re-ranks at #90 (82.48 pctl) — below the published set, still rankable |
| VLO | 0.1887 | low/negative-beta defensive | +15.33% | CARRY | re-ranks at #22 (95.87 pctl) — inside the published 24 |
| MTB | 0.1881 | low/negative-beta defensive | -3.71% | DOWNGRADE | re-ranks at #118 (76.97 pctl) — below the published set, still rankable |
| MET | 0.1878 | low/negative-beta defensive | -0.52% | DOWNGRADE | re-ranks at #57 (88.98 pctl) — below the published set, still rankable |
| HIG | 0.1811 | low/negative-beta defensive | -3.15% | DOWNGRADE | re-ranks at #106 (79.33 pctl) — below the published set, still rankable |
| BAC | 0.1692 | low/negative-beta defensive | -0.58% | DOWNGRADE | re-ranks at #49 (90.55 pctl) — below the published set, still rankable |
| JPM | 0.1674 | low/negative-beta defensive | -0.46% | DOWNGRADE | re-ranks at #46 (91.14 pctl) — below the published set, still rankable |
| AAPL | 0.1271 | low/negative-beta defensive | -7.11% | DROP | re-ranks at #372 (26.97 pctl) — below the 60th-pctl rank floor |
| UNH | 0.1263 | low/negative-beta defensive | -7.28% | DROP | re-ranks at #271 (46.85 pctl) — below the 60th-pctl rank floor |
| LLY | 0.1190 | low/negative-beta defensive | +4.96% | DOWNGRADE | re-ranks at #73 (85.83 pctl) — below the published set, still rankable |

Decision counts: **CARRY** 2, **DOWNGRADE** 17, **DROP** 7.

Of the prior book, **2** names re-rank into today's published 24. The persistence is
itself diagnostic: the leaderboard is rebuilt from the same trend-persistence construction, so a
book that just returned -2.59% of alpha regenerates much of itself. That is reported
here, next to the evidence against it, rather than being corrected after the fact.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `DELAYED` — every price fetched this run; no real-time feed wired |
| Entry/settlement price grounding | 27/27 published symbols on 3 independent sources, 0.000000% max deviation |
| Settlement prices | raw (unadjusted) target-date closes from L002 for all 227 keys |
| Reflection confidence | **HIGH** |
| Baseline flag | none — same-model folder in-window at delta 1d |

**Reflection confidence: HIGH.** All 227 due keys settled with zero unsettleable rows and zero
conflicts; the baseline is same-model, in-window, 29 days old, and its predictions matured exactly on
this run's basis date; every MoM price is triple-sourced at 0.0000% deviation.

**Structural issues found this run:**

1. **A universe constituent ceased trading under its own symbol and two OPEN predictions reference
   it.** `EQR` was renamed into / absorbed by `VMRK` (Vivmark Residential): the Nasdaq screener has
   no `EQR` row but does carry `VMRK` at a $52.60B market cap, CNBC returns "Vivmark Residential"
   under the `EQR` ticker, and the bulk history endpoint now 400s on `EQR`. Two predictions —
   `claude-opus-5-2026-07-26` (target 2026-08-23) and `gpt-5-2026-07-27` (target 2026-08-24) — come
   due within two days and **have no settleable price under the current spec**. `AVB` (last bar
   2026-08-14) and `EA` (last bar 2026-08-04) also stopped trading; neither has open predictions.
   This is this run's Track B proposal (`13`).
2. The constituent caches are **62 days stale** (fetched
   2026-06-21), which is why three dead constituents were still
   in the union. Per `rules.md § Index-Union Universe Protocol` rule 5 that is correct behaviour for
   the run — the caches are used as-is and their timestamps logged — but it is the mechanism that
   produced issue 1.
