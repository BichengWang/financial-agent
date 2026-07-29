# 02 Reflection — 2026-07-29

Standalone month-over-month reflection. Completed **before** any scoring in this run. Every price,
return, regime and thesis claim cites `01_preflight.md` ledger rows or is marked `UNAVAILABLE` /
`INFERRED`.

## 0. Prediction Settlement

### Scope

All 619 candidate settlement rows across every dated
`15_predictions.json` in `agents/equity/output/` (all models) were re-normalized by
`settlement_ledger.py` (L037). Timing is re-validated for every historical candidate, not only new ones.

**44 predictions became due and were settled this run** — 38 `EQUITY_ALPHA` and
6 `MARKET_FORECAST`, from vintages held by `claude-fable-5` and `gpt-5`.

Every due key had `target_date` = **2026-07-29**, equal to this run's date. This run fires **pre-open**,
before the 2026-07-29 session closes, so `rules.md § Settlement Rules` assigns **`TARGET_EQ_RUN_DATE`** to
all 44: settle at the latest completed close, 2026-07-28. No prediction is held open past its
target date, and none is settled on an intraday print.

After settlement: **due inventory 0, conflicts 0** (L037).

### Settled — `EQUITY_ALPHA` (38)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | claude-fable-5:2026-07-01 | 251.06 | 2026-07-29 | +4.00% | +4.84% | -0.66% | +5.49% | HIT | IN_CI | +0.092 |
| AMAT | gpt-5:2026-07-01 | 650.91 | 2026-07-29 | +6.00% | -26.80% | -0.66% | -26.14% | MISS | OUT_CI_LOW | -1.267 |
| BAX | claude-fable-5:2026-07-01 | 21.69 | 2026-07-29 | +6.00% | +12.36% | -0.66% | +13.01% | HIT | IN_CI | +0.611 |
| BEN | claude-fable-5:2026-07-01 | 34.06 | 2026-07-29 | +5.00% | -2.14% | -0.66% | -1.49% | MISS | IN_CI | -0.802 |
| BEN | gpt-5:2026-07-01 | 34.06 | 2026-07-29 | +6.00% | -2.14% | -0.66% | -1.49% | MISS | IN_CI | -0.913 |
| CCEP | claude-fable-5:2026-07-01 | 106.10 | 2026-07-29 | +6.00% | +5.04% | -0.66% | +5.70% | HIT | IN_CI | -0.126 |
| CNC | gpt-5:2026-07-01 | 68.32 | 2026-07-29 | +6.00% | -6.45% | -0.66% | -5.80% | MISS | IN_CI | -1.010 |
| CRL | claude-fable-5:2026-07-01 | 229.09 | 2026-07-29 | +5.00% | +4.95% | -0.66% | +5.61% | HIT | IN_CI | -0.004 |
| CVS | claude-fable-5:2026-07-01 | 104.81 | 2026-07-29 | +5.00% | +4.32% | -0.66% | +4.98% | HIT | IN_CI | -0.093 |
| CVS | gpt-5:2026-07-01 | 104.66 | 2026-07-29 | +6.00% | +4.47% | -0.66% | +5.13% | HIT | IN_CI | -0.210 |
| DVA | claude-fable-5:2026-07-01 | 228.03 | 2026-07-29 | +5.00% | +5.01% | -0.66% | +5.67% | HIT | IN_CI | +0.002 |
| DVA | gpt-5:2026-07-01 | 228.31 | 2026-07-29 | +6.00% | +4.88% | -0.66% | +5.54% | HIT | IN_CI | -0.156 |
| FFIV | claude-fable-5:2026-07-01 | 424.18 | 2026-07-29 | +6.00% | -4.88% | -0.66% | -4.23% | MISS | OUT_CI_LOW | -1.374 |
| HOOD | gpt-5:2026-07-01 | 108.47 | 2026-07-29 | +6.00% | -14.48% | -0.66% | -13.83% | MISS | IN_CI | -0.882 |
| HUM | claude-fable-5:2026-07-01 | 409.42 | 2026-07-29 | +5.00% | -5.06% | -0.66% | -4.40% | MISS | IN_CI | -0.924 |
| HUM | gpt-5:2026-07-01 | 409.32 | 2026-07-29 | +6.00% | -5.04% | -0.66% | -4.38% | MISS | IN_CI | -1.011 |
| IEX | claude-fable-5:2026-07-01 | 224.96 | 2026-07-29 | +6.00% | -0.14% | -0.66% | +0.52% | HIT | IN_CI | -0.990 |
| INTC | gpt-5:2026-07-01 | 127.22 | 2026-07-29 | +6.00% | -32.16% | -0.66% | -31.51% | MISS | OUT_CI_LOW | -1.478 |
| IQV | claude-fable-5:2026-07-01 | 203.20 | 2026-07-29 | +6.00% | +19.56% | -0.66% | +20.21% | HIT | IN_CI | +0.965 |
| KDP | claude-fable-5:2026-07-01 | 33.37 | 2026-07-29 | +6.00% | -6.86% | -0.66% | -6.21% | MISS | OUT_CI_LOW | -1.832 |
| KLAC | gpt-5:2026-07-01 | 266.19 | 2026-07-29 | +6.00% | -28.32% | -0.66% | -27.66% | MISS | OUT_CI_LOW | -1.221 |
| LII | claude-fable-5:2026-07-01 | 571.08 | 2026-07-29 | +6.00% | -4.72% | -0.66% | -4.07% | MISS | IN_CI | -0.979 |
| LIN | claude-fable-5:2026-07-01 | 533.55 | 2026-07-29 | +5.00% | -4.19% | -0.66% | -3.54% | MISS | OUT_CI_LOW | -1.604 |
| LLY | claude-fable-5:2026-07-01 | 1191.74 | 2026-07-29 | +3.00% | +2.43% | -0.66% | +3.08% | HIT | IN_CI | -0.057 |
| LRCX | gpt-5:2026-07-01 | 392.64 | 2026-07-29 | +6.00% | -31.33% | -0.66% | -30.68% | MISS | OUT_CI_LOW | -1.485 |
| MAS | claude-fable-5:2026-07-01 | 81.64 | 2026-07-29 | +6.00% | -0.04% | -0.66% | +0.62% | HIT | IN_CI | -0.637 |
| PANW | claude-fable-5:2026-07-01 | 352.04 | 2026-07-29 | +5.00% | -9.39% | -0.66% | -8.73% | MISS | IN_CI | -0.877 |
| PANW | gpt-5:2026-07-01 | 351.37 | 2026-07-29 | +6.00% | -9.21% | -0.66% | -8.56% | MISS | IN_CI | -0.927 |
| SNDK | gpt-5:2026-07-01 | 2027.41 | 2026-07-29 | +6.00% | -45.94% | -0.66% | -45.28% | MISS | OUT_CI_LOW | -1.416 |
| SWK | claude-fable-5:2026-07-01 | 91.34 | 2026-07-29 | +6.00% | +3.12% | -0.66% | +3.78% | HIT | IN_CI | -0.242 |
| TROW | claude-fable-5:2026-07-01 | 116.11 | 2026-07-29 | +5.00% | +4.80% | -0.66% | +5.45% | HIT | IN_CI | -0.033 |
| UAL | gpt-5:2026-07-01 | 135.04 | 2026-07-29 | +6.00% | -8.35% | -0.66% | -7.69% | MISS | IN_CI | -0.821 |
| UNH | claude-fable-5:2026-07-01 | 426.54 | 2026-07-29 | +1.00% | +0.53% | -0.66% | +1.18% | HIT | IN_CI | -0.060 |
| URI | claude-fable-5:2026-07-01 | 1111.76 | 2026-07-29 | +6.00% | -1.84% | -0.66% | -1.19% | MISS | IN_CI | -0.796 |
| V | claude-fable-5:2026-07-01 | 351.08 | 2026-07-29 | +6.00% | +4.42% | -0.66% | +5.07% | HIT | IN_CI | -0.275 |
| VTRS | claude-fable-5:2026-07-01 | 16.18 | 2026-07-29 | +6.00% | +10.38% | -0.66% | +11.04% | HIT | IN_CI | +0.547 |
| WST | claude-fable-5:2026-07-01 | 365.00 | 2026-07-29 | +5.00% | -7.67% | -0.66% | -7.01% | MISS | OUT_CI_LOW | -1.815 |
| WST | gpt-5:2026-07-01 | 365.00 | 2026-07-29 | +6.00% | -7.67% | -0.66% | -7.01% | MISS | OUT_CI_LOW | -1.958 |

**Batch result:** 17/38 HIT (44.7%), 28/38 `IN_CI`
(73.7%), mean z **-0.6858**.

### Settled — `MARKET_FORECAST` (6)

Core-ETF records settle on **raw return, not alpha** (`rules.md § Settlement Rules`), so `SPY Return`
and `Alpha` are `N/A` by construction.

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | claude-fable-5:2026-07-01 | 725.17 | 2026-07-29 | +0.79% | -6.85% | N/A | N/A | MISS | IN_CI | -0.915 |
| QQQ | gpt-5:2026-07-01 | 725.06 | 2026-07-29 | +0.79% | -6.84% | N/A | N/A | MISS | IN_CI | -0.913 |
| SOXX | claude-fable-5:2026-07-01 | 599.70 | 2026-07-29 | +0.62% | -18.05% | N/A | N/A | MISS | IN_CI | -0.876 |
| SOXX | gpt-5:2026-07-01 | 600.78 | 2026-07-29 | +2.02% | -18.20% | N/A | N/A | MISS | IN_CI | -0.948 |
| SPY | claude-fable-5:2026-07-01 | 745.76 | 2026-07-29 | +0.50% | -0.66% | N/A | N/A | MISS | IN_CI | -0.260 |
| SPY | gpt-5:2026-07-01 | 745.53 | 2026-07-29 | +0.50% | -0.63% | N/A | N/A | MISS | IN_CI | -0.251 |

**All 6 missed**, every one `IN_CI`. Both models forecast a positive drift into a window where
SPY fell 0.66%, QQQ fell
6.85%, and semis fell far more —
SOXX realized -18.05%. This is the known
`mu_ETF = beta x SPY_mu` category error diagnosed 2026-07-24: a positive SPY prior multiplied by
SOXX's large positive beta makes a bearish semis view *unrepresentable*, so the model cannot express
the one call that mattered. That the misses are all `IN_CI` confirms the failure is **directional, not
a sigma problem** — the intervals were wide enough; the central tendency pointed the wrong way.

### Rolling calibration (canonical — `settlement_ledger.py`, L038)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range |
|---|---|---|---|
| Raw `n` | 298 | 54 | >= 10 to report |
| 28-day `eff_n` | **1** | **1** | >= 3 for Track A |
| Hit rate | 50.00% | 18.52% | > 50% |
| CI coverage | 74.50% | 72.22% | 55% – 85% |
| Mean z | -0.2596 | -0.6880 | -0.5 to +0.5 |
| Rank IC (weighted mean, 298 pairs, 20 vintages) | **-0.2064** | n/a | > 0 |
| Track A calibration proposal | **INSUFFICIENT_EFFECTIVE_N** | **INSUFFICIENT_EFFECTIVE_N** | — |

Reading these honestly:

- **Equity magnitude calibration is healthy.** CI coverage 74.50% sits inside the
  55–85% band and mean z -0.2596 inside ±0.5. The sigma-widening rule does **not** fire;
  sigma stays `REALIZED_VOL_30D`.
- **Equity direction is a coin flip.** Hit rate 50.00% over n=298.
- **Rank order is inverted.** -0.2064 over 298 pairs. Per `rules.md § Rolling Calibration Metrics`,
  rank IC <= 0 over >= 20 settled predictions **caps confidence at `MEDIUM` universe-wide** — applied in
  `05`; no name in this package carries `HIGH`. As established 2026-07-22 and 2026-07-26, a mu shrink or
  sigma widen is a *monotonic transform* and cannot repair a rank inversion; that standing proposal
  stays retired.
- **Market-forecast direction is broken**, 18.52% over n=54.

### `eff_n` — the projection is holding

Both types still report `eff_n = 1`, and this remains the **startup transient** diagnosed 2026-07-28,
not a design flaw. The arithmetic: canonical `EQUITY_ALPHA` target dates span
21 days, shorter than the 28-day window, so exactly one
window fits. The projection emitted by `settlement_ledger.py` is unchanged and on schedule:

| Type | `eff_n` today | Increments to 2 on | Pending at that date |
|---|---|---|---|
| `EQUITY_ALPHA` | 1 | **2026-08-05** | 43 |
| `MARKET_FORECAST` | 1 | **2026-08-09** | 6 |

This run adds 38 equity settlements (260 → 298) and `eff_n` does not move — exactly as
predicted, because the new target date sits inside the existing window. Track A remains gated for both
record types. Falsifiable as before: any run on or after those dates still reporting `eff_n = 1` for
that type reverts the 2026-07-28 change.

## 1. Prior Run Summary — and a baseline tie that is *not* benign

The Step-2 algorithm sets the MoM window 2026-07-29 − 45d … − 21d = **2026-06-14 … 2026-07-08**, target
**2026-07-01**. No `claude-opus-5` folder exists in that window (this model's packages begin 2026-07-24), so
rule #4 applies: closest in-window **cross-model** folder, flag **`CROSS_MODEL_BASELINE`**.

**Three folders tie at exactly 0 days from target** — `claude-fable-5-2026-07-01`,
`gemini-3.5-flash-2026-07-01`, `gpt-5-2026-07-01` — and `agents.md § Orchestrator Step 2` has **no
tie-break rule**. The 2026-07-28 run flagged this gap and found the choice immaterial there (50.0% vs
46.7%). **That is not the case today.** Computing all three (L051):

| Tied baseline | Ledger | n | Hit rate | CI coverage | Mean alpha |
|---|---|---|---|---|---|
| `claude-fable-5-2026-07-01` | present | 24 | **62.5%** | 83.3% | +2.11% |
| `gpt-5-2026-07-01` | present | 14 | **14.3%** | 57.1% | -14.24% |
| `gemini-3.5-flash-2026-07-01` | **absent** — no `15_predictions.json` | — | — | — | — |

A **48.2 percentage-point** spread, and it flips the conclusion:
one baseline says the 2026-07-01 cohort beat the 50% floor, the other says it failed catastrophically.
The tie-break choice is **not invariant**, so the honest reading is the *cause*, not either number.

The two books were nearly disjoint — **6 shared names out of 32**. The gpt-5 book was
semiconductor-heavy and the window destroyed it (SNDK -45.9%,
INTC -32.2%,
LRCX -31.3%,
KLAC -28.3%,
AMAT -26.8%). The fable-5 book was
defensive healthcare and staples and held up
(IQV +19.6%,
BAX +12.4%,
VTRS +10.4%).

**`claude-fable-5-2026-07-01` is selected** as the primary baseline: it is the only tied folder with a
usable prediction ledger *and* the nearest same-family model. That selection is disclosed as a judgment
call filling a spec gap, and the alternate is reported above rather than hidden. Prior status,
regime and top names below are read from that package.

## 2. MoM Price & Return Table

Baseline `claude-fable-5-2026-07-01` → current basis 2026-07-28. Prior prices are that package's
recorded `entry_price` (its own ledger); current prices are this run's grounded unadjusted closes
(L002, L011). Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`.
SPY moved -0.66% over the same window.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| DVA | 2026-07-01 | 228.03 | 2026-07-28 | 239.46 | +5.01% | -0.66% | +5.67% | **HIT** | IN_CI; today #110 |
| HUM | 2026-07-01 | 409.42 | 2026-07-28 | 388.71 | -5.06% | -0.66% | -4.40% | **MISS** | IN_CI; today #126 |
| FFIV | 2026-07-01 | 424.18 | 2026-07-28 | 403.46 | -4.88% | -0.66% | -4.23% | **MISS** | OUT_CI_LOW; today #64 |
| MAS | 2026-07-01 | 81.64 | 2026-07-28 | 81.61 | -0.04% | -0.66% | +0.62% | **HIT** | IN_CI; today #150 |
| BEN | 2026-07-01 | 34.06 | 2026-07-28 | 33.33 | -2.14% | -0.66% | -1.49% | **MISS** | IN_CI; today #272 |
| URI | 2026-07-01 | 1111.76 | 2026-07-28 | 1091.26 | -1.84% | -0.66% | -1.19% | **MISS** | IN_CI; today #143 |
| LII | 2026-07-01 | 571.08 | 2026-07-28 | 544.11 | -4.72% | -0.66% | -4.07% | **MISS** | IN_CI; today #360 |
| WST | 2026-07-01 | 365.00 | 2026-07-28 | 337.00 | -7.67% | -0.66% | -7.01% | **MISS** | OUT_CI_LOW; today #184 |
| PANW | 2026-07-01 | 352.04 | 2026-07-28 | 319.00 | -9.39% | -0.66% | -8.73% | **MISS** | IN_CI; today #275 |
| V | 2026-07-01 | 351.08 | 2026-07-28 | 366.59 | +4.42% | -0.66% | +5.07% | **HIT** | IN_CI; today #60 |
| CCEP | 2026-07-01 | 106.10 | 2026-07-28 | 111.45 | +5.04% | -0.66% | +5.70% | **HIT** | IN_CI; today #54 |
| CVS | 2026-07-01 | 104.81 | 2026-07-28 | 109.34 | +4.32% | -0.66% | +4.98% | **HIT** | IN_CI; today #136 |
| SWK | 2026-07-01 | 91.34 | 2026-07-28 | 94.19 | +3.12% | -0.66% | +3.78% | **HIT** | IN_CI; today #171 |
| KDP | 2026-07-01 | 33.37 | 2026-07-28 | 31.08 | -6.86% | -0.66% | -6.21% | **MISS** | OUT_CI_LOW; today #327 |
| VTRS | 2026-07-01 | 16.18 | 2026-07-28 | 17.86 | +10.38% | -0.66% | +11.04% | **HIT** | IN_CI; today #140 |
| TROW | 2026-07-01 | 116.11 | 2026-07-28 | 121.68 | +4.80% | -0.66% | +5.45% | **HIT** | IN_CI; today #152 |
| IEX | 2026-07-01 | 224.96 | 2026-07-28 | 224.65 | -0.14% | -0.66% | +0.52% | **HIT** | IN_CI; today #228 |
| IQV | 2026-07-01 | 203.20 | 2026-07-28 | 242.94 | +19.56% | -0.66% | +20.21% | **HIT** | IN_CI; today #8 |
| CRL | 2026-07-01 | 229.09 | 2026-07-28 | 240.43 | +4.95% | -0.66% | +5.61% | **HIT** | IN_CI; today #244 |
| BAX | 2026-07-01 | 21.69 | 2026-07-28 | 24.37 | +12.36% | -0.66% | +13.01% | **HIT** | IN_CI; today #107 |
| LIN | 2026-07-01 | 533.55 | 2026-07-28 | 511.18 | -4.19% | -0.66% | -3.54% | **MISS** | OUT_CI_LOW; today #305 |
| ABBV | 2026-07-01 | 251.06 | 2026-07-28 | 263.20 | +4.84% | -0.66% | +5.49% | **HIT** | IN_CI; today #146 |
| UNH | 2026-07-01 | 426.54 | 2026-07-28 | 428.79 | +0.53% | -0.66% | +1.18% | **HIT** | IN_CI; today #71 |
| LLY | 2026-07-01 | 1191.74 | 2026-07-28 | 1220.66 | +2.43% | -0.66% | +3.08% | **HIT** | IN_CI; today #174 |

**15 of 24 hits (62.5%),
mean alpha +2.11%, CI coverage 83.3%.**

## 3. Theme-Level Performance

| Prior theme | Evidence | Verdict |
|---|---|---|
| Defensive healthcare / lab services | IQV +20.21% alpha, BAX +13.01%, VTRS +11.04%, CRL +5.61%, DVA +5.67%, ABBV +5.49% | **VALIDATED** |
| Managed care | HUM -4.40%, CVS +4.98%, UNH +1.18% | **PARTIAL** — dispersion inside one theme |
| Security / high-multiple software | PANW -8.73%, FFIV -4.23% | **FAILED** |
| Industrials / building products | LII -4.07%, MAS +0.62%, URI -1.19%, SWK +3.78% | **PARTIAL** |
| Semiconductors (gpt-5 alternate baseline) | 5 of 5 names below −26% | **FAILED** — the dominant window effect |

## 4. Regime Shift Assessment

| | Prior (2026-07-01 baseline) | Current (2026-07-29) |
|---|---|---|
| Regime | NEUTRAL | **NEUTRAL** (L042) |
| SPY vs MA20 / MA50 | — | below both (740.86 vs 746.65 / 743.99) |
| VIX | — | 18.21 (L008) — not an elevated-vol regime |
| SOXX from 60d high | — | -24.97% (L006) |
| Universe at negative beta | — | 42.02% (L015) |

The label is unchanged at `NEUTRAL`, but the *internal* composition shifted hard: the
semiconductor complex fell 24.97% from its 60-day high while
42.02% of the universe now carries negative beta to SPY. Factor-weight
implication: the defensive Macro polarity (L050) is retained — the settled evidence in §2 and §3
supports it directly, since the defensive book beat the growth book by
16.3pp of mean alpha over exactly this window. Family
*weights* are unchanged; only the Macro polarity reading is regime-conditional, and it is disclosed as
`INFERRED`, not promoted to a rule.

## 5. Carry-Forward Decisions

Binding on factor scoring where ledger-backed. Ranks are today's post-penalty ranks out of 514,
read directly from `run_computed_manifest.json` — none is hand-transcribed.

| Ticker | Prior Score | Prior Conf | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| DVA | +0.3828 | LOW | +5.01% | **DOWNGRADE** | rank #110 (pctl 78.75) — below the published cut but still rankable; monitoring only |
| HUM | +0.3756 | LOW | -5.06% | **DOWNGRADE** | rank #126 (pctl 75.63) — below the published cut but still rankable; monitoring only |
| FFIV | +0.3680 | LOW | -4.88% | **DOWNGRADE** | rank #64 (pctl 87.72) — below the published cut but still rankable; monitoring only |
| MAS | +0.3412 | LOW | -0.04% | **DOWNGRADE** | rank #150 (pctl 70.96) — below the published cut but still rankable; monitoring only |
| BEN | +0.3372 | LOW | -2.14% | **DROP** | pctl 47.17 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| URI | +0.3367 | LOW | -1.84% | **DOWNGRADE** | rank #143 (pctl 72.32) — below the published cut but still rankable; monitoring only |
| LII | +0.3344 | LOW | -4.72% | **DROP** | pctl 30.02 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| WST | +0.3337 | LOW | -7.67% | **DOWNGRADE** | rank #184 (pctl 64.33) — below the published cut but still rankable; monitoring only |
| PANW | +0.3313 | LOW | -9.39% | **DROP** | pctl 46.59 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| V | +0.3199 | LOW | +4.42% | **DOWNGRADE** | rank #60 (pctl 88.50) — below the published cut but still rankable; monitoring only |
| CCEP | +0.3161 | LOW | +5.04% | **DOWNGRADE** | rank #54 (pctl 89.67) — below the published cut but still rankable; monitoring only |
| CVS | +0.3106 | LOW | +4.32% | **DOWNGRADE** | rank #136 (pctl 73.68) — below the published cut but still rankable; monitoring only |
| SWK | +0.3090 | LOW | +3.12% | **DOWNGRADE** | rank #171 (pctl 66.86) — below the published cut but still rankable; monitoring only |
| KDP | +0.3044 | LOW | -6.86% | **DROP** | pctl 36.45 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| VTRS | +0.3017 | LOW | +10.38% | **DOWNGRADE** | rank #140 (pctl 72.90) — below the published cut but still rankable; monitoring only |
| TROW | +0.3001 | LOW | +4.80% | **DOWNGRADE** | rank #152 (pctl 70.57) — below the published cut but still rankable; monitoring only |
| IEX | +0.2955 | LOW | -0.14% | **DROP** | pctl 55.75 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| IQV | +0.2884 | LOW | +19.56% | **CARRY** | still rank #8 of 514 (pctl 98.64) on today's basis |
| CRL | +0.2829 | LOW | +4.95% | **DROP** | pctl 52.63 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| BAX | +0.2801 | LOW | +12.36% | **DOWNGRADE** | rank #107 (pctl 79.34) — below the published cut but still rankable; monitoring only |
| LIN | +0.2299 | LOW | -4.19% | **DROP** | pctl 40.74 < 60th — below the rankable floor (`rules.md § mu Calibration Table`) |
| ABBV | +0.2009 | LOW | +4.84% | **DOWNGRADE** | rank #146 (pctl 71.73) — below the published cut but still rankable; monitoring only |
| UNH | +0.1942 | LOW | +0.53% | **DOWNGRADE** | rank #71 (pctl 86.35) — below the published cut but still rankable; monitoring only |
| LLY | +0.1807 | LOW | +2.43% | **DOWNGRADE** | rank #174 (pctl 66.28) — below the published cut but still rankable; monitoring only |

**1 CARRY · 16 DOWNGRADE · 7 DROP.** No `PROMOTE`: promotion requires new
ledger-backed evidence, and with `Fund_Z`/`Sent_Z` `UNAVAILABLE` (L046, L047) no such evidence exists
this run. `DROP` names are excluded from today's scored set absent new evidence; note that a
carry-forward falling below the 60th-percentile floor is a `DOWNGRADE`/`DROP` to the rejection log
rather than a silent disappearance (precedent 2026-07-20).

## 6. Sign-Off

| Price used | Freshness tag | Ledger |
|---|---|---|
| All 24 baseline prior prices | `HISTORICAL` (that package's own recorded entry) | L039 |
| All current prices | `HISTORICAL`, observation date 2026-07-28 | L002, L011 |
| SPY benchmark both ends | `HISTORICAL` | L004, L011 |

**Reflection confidence: MEDIUM.** Settlement mechanics are clean — 44 settled, due inventory 0,
conflicts 0, every timing flag validated by the canonical normalizer. Prices are grounded to the cent
across three to four independent sources. Confidence is held at MEDIUM rather than HIGH for one
reason: the MoM baseline tie is unresolved by spec and the two usable baselines disagree by
48.2pp, so the §2 hit rate is a property of a coin-flip
selection as much as of the market.

### Structural issues found

1. **The MoM baseline tie-break gap is now material** (L051). Flagged as cosmetic on 2026-07-28;
   today it swings the headline reflection metric by 48.2pp.
   Carried to `13` as the leading candidate for the next run's Track B change.
2. **The earnings-grounding heuristic was producing false "clear of earnings" calls** — found and fixed
   this run, and this run's accepted Track B change. Detail in `05 § Earnings-date grounding` and `13`.
3. `MARKET_FORECAST` calibration remains broken with the fix gated behind `eff_n` until
   2026-08-09.
