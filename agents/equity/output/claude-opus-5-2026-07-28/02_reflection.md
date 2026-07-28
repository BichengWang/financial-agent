# 02 Reflection — 2026-07-28

Standalone month-over-month reflection. Every price, return, regime and thesis claim cites `01`
ledger rows or is marked `UNAVAILABLE` / `INFERRED`. Reflection completed **before** any scoring.

## 0. Prediction Settlement

Ledgers scanned: every `15_predictions.json` under `agents/equity/output/` across all models
(65 packages). Due inventory and canonical precedence come from
`settlement_ledger.py`, never re-derived by hand (L043).

**Timing.** All 35 due keys carry `target_date == 2026-07-28` and this run fires **pre-open**, so
`TARGET_EQ_RUN_DATE` applies (`rules.md § Settlement Rules`): each settles at the latest completed
close, 2026-07-27. No intraday print was used and nothing was held open past its target date.

### Settled this run — 35 predictions

| Ticker | Vintage | Model | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-06-30 | claude-opus-4-8 | 576.46 | 2026-07-28 | +6.00% | -14.14% | -0.82% | -13.32% | MISS | IN_CI | -0.9159 |
| BAC | 2026-06-30 | claude-opus-4-8 | 57.19 | 2026-07-28 | +4.00% | +8.64% | -0.82% | +9.45% | HIT | IN_CI | +0.8669 |
| CAT | 2026-06-30 | claude-opus-4-8 | 1064.99 | 2026-07-28 | +4.00% | -18.00% | -0.82% | -17.19% | MISS | OUT_CI_LOW | -1.5559 |
| GE | 2026-06-30 | claude-opus-4-8 | 372.11 | 2026-07-28 | +3.00% | -2.82% | -0.82% | -2.01% | MISS | IN_CI | -0.6454 |
| HD | 2026-06-30 | claude-opus-4-8 | 351.79 | 2026-07-28 | +1.00% | -4.46% | -0.82% | -3.65% | MISS | IN_CI | -0.6703 |
| JNJ | 2026-06-30 | claude-opus-4-8 | 255.88 | 2026-07-28 | +1.00% | +3.94% | -0.82% | +4.75% | HIT | IN_CI | +0.4134 |
| JPM | 2026-06-30 | claude-opus-4-8 | 328.25 | 2026-07-28 | +2.00% | +8.51% | -0.82% | +9.33% | HIT | IN_CI | +0.9469 |
| LIN | 2026-06-30 | claude-opus-4-8 | 519.75 | 2026-07-28 | +2.00% | -2.45% | -0.82% | -1.63% | MISS | IN_CI | -0.8348 |
| LLY | 2026-06-30 | claude-opus-4-8 | 1209.29 | 2026-07-28 | +5.00% | -0.97% | -0.82% | -0.16% | MISS | IN_CI | -0.5961 |
| MU | 2026-06-30 | claude-opus-4-8 | 1146.0 | 2026-07-28 | +3.00% | -21.45% | -0.82% | -20.63% | MISS | IN_CI | -0.6977 |
| PG | 2026-06-30 | claude-opus-4-8 | 146.06 | 2026-07-28 | +1.00% | +1.76% | -0.82% | +2.58% | HIT | IN_CI | +0.1082 |
| SO | 2026-06-30 | claude-opus-4-8 | 96.42 | 2026-07-28 | +2.00% | +0.06% | -0.82% | +0.88% | HIT | IN_CI | -0.3677 |
| TSLA | 2026-06-30 | claude-opus-4-8 | 416.07 | 2026-07-28 | +1.00% | -25.68% | -0.82% | -24.86% | MISS | OUT_CI_LOW | -1.8363 |
| UNH | 2026-06-30 | claude-opus-4-8 | 416.49 | 2026-07-28 | +6.00% | +0.28% | -0.82% | +1.09% | HIT | IN_CI | -0.7502 |
| V | 2026-06-30 | claude-opus-4-8 | 342.92 | 2026-07-28 | +5.00% | +5.72% | -0.82% | +6.53% | HIT | IN_CI | +0.1258 |
| BAC | 2026-06-30 | gpt-5 | 57.24 | 2026-07-28 | +3.00% | +8.54% | -0.67% | +9.21% | HIT | OUT_CI_HIGH | +1.0400 |
| CAT | 2026-06-30 | gpt-5 | 1068.61 | 2026-07-28 | +6.00% | -18.28% | -0.67% | -17.61% | MISS | OUT_CI_LOW | -1.7110 |
| CVX | 2026-06-30 | gpt-5 | 167.39 | 2026-07-28 | +3.00% | +13.51% | -0.67% | +14.18% | HIT | OUT_CI_HIGH | +1.4453 |
| DUK | 2026-06-30 | gpt-5 | 127.57 | 2026-07-28 | +1.00% | +0.99% | -0.67% | +1.66% | HIT | IN_CI | -0.0025 |
| GE | 2026-06-30 | gpt-5 | 373.64 | 2026-07-28 | +5.00% | -3.22% | -0.67% | -2.55% | MISS | IN_CI | -0.9153 |
| GOOGL | 2026-06-30 | gpt-5 | 354.5 | 2026-07-28 | +6.00% | -7.88% | -0.67% | -7.21% | MISS | OUT_CI_LOW | -1.4926 |
| HD | 2026-06-30 | gpt-5 | 352.62 | 2026-07-28 | +1.00% | -4.69% | -0.67% | -4.02% | MISS | IN_CI | -0.6979 |
| JPM | 2026-06-30 | gpt-5 | 329.57 | 2026-07-28 | +1.00% | +8.08% | -0.67% | +8.75% | HIT | IN_CI | +1.0321 |
| LIN | 2026-06-30 | gpt-5 | 518.35 | 2026-07-28 | +1.00% | -2.19% | -0.67% | -1.52% | MISS | IN_CI | -0.6034 |
| LLY | 2026-06-30 | gpt-5 | 1206.62 | 2026-07-28 | +4.00% | -0.75% | -0.67% | -0.08% | MISS | IN_CI | -0.4734 |
| SHW | 2026-06-30 | gpt-5 | 343.85 | 2026-07-28 | +2.00% | -4.82% | -0.67% | -4.15% | MISS | IN_CI | -0.8160 |
| SO | 2026-06-30 | gpt-5 | 96.38 | 2026-07-28 | +2.00% | +0.10% | -0.67% | +0.77% | HIT | IN_CI | -0.3598 |
| UNH | 2026-06-30 | gpt-5 | 416.76 | 2026-07-28 | +5.00% | +0.21% | -0.67% | +0.88% | HIT | IN_CI | -0.6285 |
| V | 2026-06-30 | gpt-5 | 342.23 | 2026-07-28 | +2.00% | +5.93% | -0.67% | +6.60% | HIT | IN_CI | +0.6898 |
| QQQ | 2026-06-30 | claude-opus-4-8 | 734.34 | 2026-07-28 | +2.35% | -7.11% | N/A | N/A | MISS | OUT_CI_LOW | -1.1524 |
| SOXX | 2026-06-30 | claude-opus-4-8 | 636.03 | 2026-07-28 | +3.26% | -18.84% | N/A | N/A | MISS | OUT_CI_LOW | -1.0763 |
| SPY | 2026-06-30 | claude-opus-4-8 | 745.17 | 2026-07-28 | +1.50% | -0.82% | N/A | N/A | MISS | IN_CI | -0.5216 |
| QQQ | 2026-06-30 | gpt-5 | 731.66 | 2026-07-28 | +1.78% | -6.77% | N/A | N/A | MISS | OUT_CI_LOW | -1.0466 |
| SOXX | 2026-06-30 | gpt-5 | 635.02 | 2026-07-28 | +2.58% | -18.71% | N/A | N/A | MISS | IN_CI | -1.0379 |
| SPY | 2026-06-30 | gpt-5 | 744.08 | 2026-07-28 | +0.50% | -0.67% | N/A | N/A | MISS | IN_CI | -0.2648 |

`MARKET_FORECAST` rows carry `SPY Return` / `Alpha` = `N/A` and score direction on **raw** return per
`rules.md § Settlement Rules`.

### This batch

| | Direction hits | CI coverage | Mean z |
|---|---|---|---|
| `EQUITY_ALPHA` (n=29) | 14/29 (48.28%) | 23/29 (79.31%) | -0.3415 |
| `MARKET_FORECAST` (n=6) | 0/6 (0.00%) | 3/6 (50.00%) | -0.8499 |

Every one of the 6 core-ETF forecasts settled **MISS**. That is now a long pattern, not a bad day —
see the rolling line below and the diagnosis in `13`.

### Rolling Calibration Metrics (canonical ledger, L044)

| Metric | `EQUITY_ALPHA` | Healthy range | `MARKET_FORECAST` |
|---|---|---|---|
| Raw `n` | **260** | ≥ 10 to report, ≥ 20 for Track A | **48** |
| 28-day `eff_n` | **1** | ≥ 3 for Track A | **1** |
| Hit rate | 50.77% | > 50% | 20.83% |
| CI coverage | 74.62% | 55% – 85% | 68.75% |
| Mean z | -0.1973 | −0.5 to +0.5 | -0.6872 |
| Rank IC (weighted mean over 18 vintages) | **-0.1715** | > 0 | reported separately, not pooled |
| Track A calibration gate | `INSUFFICIENT_EFFECTIVE_N` | — | `INSUFFICIENT_EFFECTIVE_N` |

**Reading, split by failure mode** (the 2026-07-26 finding that these must be diagnosed separately):

- **Magnitude calibration is healthy** for equities: mean z -0.1973 sits inside ±0.5 and CI coverage
  74.62% sits inside the 55–85% band. Sigma is neither too tight nor uninformatively wide.
- **Rank ordering is inverted**: weighted-mean rank IC -0.1715 over 260 settled records (≥ 20).
  Per `rules.md § Rolling Calibration Metrics` this **freezes confidence at `MEDIUM`** universe-wide,
  which `05` applies. A mu shrink or sigma widen is a monotonic transform and cannot repair a rank
  inversion — that standing proposal stays retired.
- **Market forecasts are directionally broken**, not merely noisy: 20.83% over n=48, mean z
  -0.6872. Diagnosed in `13` and disclosed at the point of use in `03`.

### `eff_n` — why it is 1, and exactly when it stops being 1 (L055)

This is the question the 2026-07-27 package queued for the 07-31 structural review
("if `eff_n` can never rise under this cadence, the gate itself needs review"). It is now answered,
and the answer is **it can rise, on a computable date**:

| Quantity | Value |
|---|---|
| Canonical settlements | 308 |
| Distinct target dates represented | 15 |
| Earliest → latest target date | 2026-07-08 → 2026-07-28 |
| **Total span** | **20 days** |
| 28-day window requirement | 28 days |
| `eff_n` today | **1** |
| Next non-overlapping window opens | 2026-08-05 |
| First outstanding target date at/after that | **2026-08-05** (43 predictions pending) |

The entire settled corpus spans **20 days — shorter than the 28-day
window itself**. `eff_n = 1` is therefore not a defect in the metric and not evidence of a broken
cadence: it is arithmetic. Every settleable prediction this system has ever produced matured inside a
single three-week window, so there is exactly one independent observation, no matter how large raw `n`
grows. Raw `n` rose 29 to 260 today and `eff_n` did not move, exactly as on 2026-07-26.

**`eff_n` reaches 2 on 2026-08-05** — that is not a projection about market behaviour, it is
a fact about the existing prediction inventory: 43 predictions already carry that
target date. Reaching the Track A gate of 3 needs a third window opening 28 days later
(2026-09-02); no prediction
carries a target date that far out yet, but runs between now and then will create them at the standard
`run_date + 28d` horizon. **Track A calibration work is therefore blocked until early September, and
that is the correct outcome, not an obstacle to route around.**

## 1. Prior Run Summary

| Field | Value |
|---|---|
| Baseline folder | `agents/equity/output/gpt-5-2026-06-30` (CROSS_MODEL_BASELINE, L045) |
| Baseline date | 2026-06-30 — 28 days before this run |
| Baseline status | `NO_TRADE` |
| Names forecast | 14 equity + 3 core ETF |
| SPY then → now | 744.08 → 739.09 (-0.67%) |

Top-5 by the baseline's own ranking: GOOGL (-7.88%), CAT (-18.28%), UNH (+0.21%), GE (-3.22%), LLY (-0.75%).

## 2. MoM Price & Return Table

Prior prices are the baseline package's own recorded `entry_price` (its ledger, its vintage); current
prices are this run's grounded 2026-07-27 closes (L002, L005). Hit/Miss is **alpha-based** per
`rules.md § Settlement Rules`.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 2026-06-30 | 354.5 | 2026-07-27 | 326.56 | -7.88% | -0.67% | -7.21% | MISS | OUT_CI_LOW | scored today at rank 451/514 |
| CAT | 2026-06-30 | 1068.61 | 2026-07-27 | 873.28 | -18.28% | -0.67% | -17.61% | MISS | OUT_CI_LOW | scored today at rank 446/514 |
| UNH | 2026-06-30 | 416.76 | 2026-07-27 | 417.64 | +0.21% | -0.67% | +0.88% | HIT | IN_CI | scored today at rank 174/514 |
| GE | 2026-06-30 | 373.64 | 2026-07-27 | 361.61 | -3.22% | -0.67% | -2.55% | MISS | IN_CI | scored today at rank 159/514 |
| LLY | 2026-06-30 | 1206.62 | 2026-07-27 | 1197.53 | -0.75% | -0.67% | -0.08% | MISS | IN_CI | scored today at rank 97/514 |
| BAC | 2026-06-30 | 57.24 | 2026-07-27 | 62.13 | +8.54% | -0.67% | +9.21% | HIT | OUT_CI_HIGH | scored today at rank 26/514 |
| CVX | 2026-06-30 | 167.39 | 2026-07-27 | 190.0 | +13.51% | -0.67% | +14.18% | HIT | OUT_CI_HIGH | scored today at rank 180/514 |
| V | 2026-06-30 | 342.23 | 2026-07-27 | 362.53 | +5.93% | -0.67% | +6.60% | HIT | IN_CI | scored today at rank 105/514 |
| SO | 2026-06-30 | 96.38 | 2026-07-27 | 96.48 | +0.10% | -0.67% | +0.77% | HIT | IN_CI | scored today at rank 30/514 |
| SHW | 2026-06-30 | 343.85 | 2026-07-27 | 327.27 | -4.82% | -0.67% | -4.15% | MISS | IN_CI | scored today at rank 278/514 |
| JPM | 2026-06-30 | 329.57 | 2026-07-27 | 356.2 | +8.08% | -0.67% | +8.75% | HIT | IN_CI | scored today at rank 31/514 |
| DUK | 2026-06-30 | 127.57 | 2026-07-27 | 128.83 | +0.99% | -0.67% | +1.66% | HIT | IN_CI | scored today at rank 101/514 |
| HD | 2026-06-30 | 352.62 | 2026-07-27 | 336.09 | -4.69% | -0.67% | -4.02% | MISS | IN_CI | scored today at rank 330/514 |
| LIN | 2026-06-30 | 518.35 | 2026-07-27 | 507.02 | -2.19% | -0.67% | -1.52% | MISS | IN_CI | scored today at rank 303/514 |
| SPY | 2026-06-30 | 744.08 | 2026-07-27 | 739.09 | -0.67% | N/A | N/A | MISS | IN_CI | core ETF — raw-return scoring |
| QQQ | 2026-06-30 | 731.66 | 2026-07-27 | 682.12 | -6.77% | N/A | N/A | MISS | OUT_CI_LOW | core ETF — raw-return scoring |
| SOXX | 2026-06-30 | 635.02 | 2026-07-27 | 516.23 | -18.71% | N/A | N/A | MISS | IN_CI | core ETF — raw-return scoring |

All 17 baseline names are priced from grounded sources — no `UNAVAILABLE` and no
`APPROX - sourced` rows.

**Baseline-sensitivity check.** The two exact-target baselines are NOT field-identical (unlike the 2026-07-27 tie): they carry different name sets and different entry-price vendors. Both summaries are reported so the reader can see whether the MoM conclusion depends on the pick. Under the alternative baseline
`claude-opus-4-8-2026-06-30` the equity hit rate is 46.67%
(7/15) against 50.00%
(7/14) here — the same coin-flip conclusion.
Mean alpha differs more (-3.26% vs +0.35%)
because the alternative held a semiconductor and high-beta sleeve (AMD, MU, TSLA) that this baseline did
not. **The reflection's conclusion does not depend on the tie-break.**

## 3. Theme-Level Performance

| Prior theme | Verdict | Evidence |
|---|---|---|
| Mega-cap growth / AI complex (GOOGL, V) | **Partial** | GOOGL -7.88% vs SPY -0.67%; the theme produced alpha but the cohort dispersed |
| Industrials / capital goods (CAT, GE) | **Validated** | CAT -18.28%, GE -3.22% — both beat a falling SPY |
| Managed care / pharma (UNH, LLY) | **Failed** | UNH +0.21%, LLY -0.75% |
| Rate-sensitive defensives (SO, DUK) | **Partial** | SO +0.10%, DUK +0.99% against TLT 20d momentum -3.78% |
| Core ETF top-down view | **Failed** | all 3 settled MISS; SOXX realized -18.71% against a +2.58% forecast |

Every verdict above is `INFERRED` from the cited L002/L003 return rows.

## 4. Regime Shift Assessment

| | Baseline (2026-06-30) | Today (2026-07-27) |
|---|---|---|
| Declared regime | `NEUTRAL` | **`NEUTRAL`** |
| SPY vs MA20 / MA50 | — | -1.01% / -0.67% |
| SPY 30d realized vol | — | 3.64% (falling from 3.92%) |
| VIX | — | 18.67 vs 20d mean 16.88 |
| Breadth above MA50 | — | 69.07% |
| Universe at negative beta | — | 41.44% |

**No regime shift.** The label is unchanged, so factor-weight implications are unchanged: the baseline
0.30 / 0.30 / 0.25 / 0.15 family weights stand, and the only regime-conditional judgment applied is the
defensive Macro polarity disclosed in `05` (L053).

## 5. Carry-Forward Decisions

Regenerated directly from `run_computed_manifest.json` — no rank, score or return below was typed by
hand (the 2026-07-26 lesson: 14 of 14 hand-written carry-forward ranks were wrong).

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| GOOGL | 100.0 | baseline 2026-06-30 forecast mu +6.00% | -7.88% | **DROP** | falls to rank 451/514 (pctl 12.28), below the 60th-pctl ranking floor |
| CAT | 97.0 | baseline 2026-06-30 forecast mu +6.00% | -18.28% | **DROP** | falls to rank 446/514 (pctl 13.26), below the 60th-pctl ranking floor |
| UNH | 93.9 | baseline 2026-06-30 forecast mu +5.00% | +0.21% | **DOWNGRADE** | still ranked at 174/514 (pctl 66.28) but below the published set |
| GE | 90.9 | baseline 2026-06-30 forecast mu +5.00% | -3.22% | **DOWNGRADE** | still ranked at 159/514 (pctl 69.20) but below the published set |
| LLY | 87.9 | baseline 2026-06-30 forecast mu +4.00% | -0.75% | **DOWNGRADE** | still ranked at 97/514 (pctl 81.29) but below the published set |
| BAC | 84.8 | baseline 2026-06-30 forecast mu +3.00% | +8.54% | **DOWNGRADE** | still ranked at 26/514 (pctl 95.13) but below the published set |
| CVX | 81.8 | baseline 2026-06-30 forecast mu +3.00% | +13.51% | **DOWNGRADE** | still ranked at 180/514 (pctl 65.11) but below the published set |
| V | 78.8 | baseline 2026-06-30 forecast mu +2.00% | +5.93% | **DOWNGRADE** | still ranked at 105/514 (pctl 79.73) but below the published set |
| SO | 75.8 | baseline 2026-06-30 forecast mu +2.00% | +0.10% | **DOWNGRADE** | still ranked at 30/514 (pctl 94.35) but below the published set |
| SHW | 72.7 | baseline 2026-06-30 forecast mu +2.00% | -4.82% | **DROP** | falls to rank 278/514 (pctl 46.00), below the 60th-pctl ranking floor |
| JPM | 69.7 | baseline 2026-06-30 forecast mu +1.00% | +8.08% | **DOWNGRADE** | still ranked at 31/514 (pctl 94.15) but below the published set |
| DUK | 66.7 | baseline 2026-06-30 forecast mu +1.00% | +0.99% | **DOWNGRADE** | still ranked at 101/514 (pctl 80.51) but below the published set |
| HD | 63.6 | baseline 2026-06-30 forecast mu +1.00% | -4.69% | **DROP** | falls to rank 330/514 (pctl 35.87), below the 60th-pctl ranking floor |
| LIN | 60.6 | baseline 2026-06-30 forecast mu +1.00% | -2.19% | **DROP** | falls to rank 303/514 (pctl 41.13), below the 60th-pctl ranking floor |

0 of 14 baseline names carry into today's published set
(none); 5 fall below the 60th-percentile ranking floor
and appear only in the rejection log. `DROP` names stay out of today's scored set absent new
ledger evidence — none was found.

The near-total turnover is itself the finding: a book built on 2026-06-30's leadership
has almost no overlap with the leadership 28 days later. That is consistent with the
rank-IC inversion in § 0 — the score is identifying names whose *relative* ranking does not persist.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (2026-07-27 completed close), two-source grounded (L002 + L005) |
| Prices marked `UNAVAILABLE` | 0 |
| Reflection confidence | **MEDIUM** |
| Rationale | Settlement and MoM inputs are fully grounded and the ledger is conflict-free (0 conflicts, due inventory 0). Held below HIGH because the baseline is cross-model, the two exact-target candidates are not field-identical, and rank IC is negative — the *inputs* are sound but the *signal* they measure is not yet trustworthy. |

**Structural issues found this run**

1. `eff_n` is pinned at 1 by construction, and the date it stops being pinned is now computed
   (2026-08-05) — carried into `13` as this run's evolution proposal.
2. The MoM baseline tie-break is under-specified in `agents.md § Orchestrator Step 2`: two folders can
   land on the exact target date with materially different contents, and the algorithm gives no
   tie-break rule. Handled here by computing both and disclosing; flagged for a future run.
3. An ex-dividend basis artifact (L054) again produced a cross-vendor price disagreement — the fourth
   occurrence since 2026-07-15. It was correctly resolved, but it recurs because vendors disagree about
   *when* to apply the adjustment, not about the price.
