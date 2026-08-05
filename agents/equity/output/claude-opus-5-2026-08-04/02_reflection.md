# 02 — Reflection — 2026-08-04

## 0. Prediction Settlement

`settlement_ledger.py --as-of 2026-08-04` reported **48 due keys**, all with
`target_date == 2026-08-04 == run_date`. This run fires **intraday**, before the 2026-08-04 close, so
`rules.md § Settlement Rules` **`TARGET_EQ_RUN_DATE`** applies to every one of them: settle at the
latest completed close, 2026-08-03. No intraday print was used, and nothing was held open past its
target date.

Scanned for due predictions: every `15_predictions.json` under `agents/equity/output/` across all
models (960 candidate settlement rows,
268 audit-only, 87 rejected on timing,
0 conflicts).

### Settled this run (48)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| **ABBV** | claude-fable-5 2026-07-07 | 257.61 | 2026-08-04 | +2.00% | -4.86% | +1.34% | -6.20% | MISS | IN_CI | -0.718 |
| **AMAT** | gpt-5 2026-07-07 | 542.75 | 2026-08-04 | +6.00% | -4.52% | +1.38% | -5.90% | MISS | IN_CI | -0.376 |
| **AMD** | gpt-5 2026-07-07 | 515.31 | 2026-08-04 | +6.00% | -5.95% | +1.38% | -7.33% | MISS | IN_CI | -0.500 |
| **AXON** | claude-fable-5 2026-07-07 | 638.68 | 2026-08-04 | +5.00% | -9.83% | +1.34% | -11.18% | MISS | IN_CI | -0.737 |
| **AXON** | gpt-5 2026-07-07 | 643.00 | 2026-08-04 | +6.00% | -10.44% | +1.38% | -11.82% | MISS | IN_CI | -0.802 |
| **BAX** | claude-fable-5 2026-07-07 | 23.03 | 2026-08-04 | +5.00% | +22.01% | +1.34% | +20.67% | HIT | OUT_CI_HIGH | +1.622 |
| **BAX** | gpt-5 2026-07-07 | 23.09 | 2026-08-04 | +6.00% | +21.67% | +1.38% | +20.29% | HIT | OUT_CI_HIGH | +1.465 |
| **BEN** | claude-fable-5 2026-07-07 | 34.69 | 2026-08-04 | +5.00% | +1.59% | +1.34% | +0.24% | HIT | IN_CI | -0.427 |
| **BEN** | gpt-5 2026-07-07 | 34.67 | 2026-08-04 | +6.00% | +1.63% | +1.38% | +0.25% | HIT | IN_CI | -0.538 |
| **CRWD** | claude-fable-5 2026-07-07 | 196.95 | 2026-08-04 | +6.00% | +2.84% | +1.34% | +1.49% | HIT | IN_CI | -0.201 |
| **CRWD** | gpt-5 2026-07-07 | 196.94 | 2026-08-04 | +6.00% | +2.84% | +1.38% | +1.47% | HIT | IN_CI | -0.198 |
| **DAL** | claude-fable-5 2026-07-07 | 89.35 | 2026-08-04 | +6.00% | +2.51% | +1.34% | +1.16% | HIT | IN_CI | -0.316 |
| **DAL** | gpt-5 2026-07-07 | 89.44 | 2026-08-04 | +6.00% | +2.40% | +1.38% | +1.03% | HIT | IN_CI | -0.320 |
| **DDOG** | claude-fable-5 2026-07-07 | 263.18 | 2026-08-04 | +6.00% | +3.96% | +1.34% | +2.61% | HIT | IN_CI | -0.112 |
| **DDOG** | gpt-5 2026-07-07 | 263.50 | 2026-08-04 | +6.00% | +3.83% | +1.38% | +2.45% | HIT | IN_CI | -0.117 |
| **DOC** | gpt-5 2026-07-07 | 22.00 | 2026-08-04 | +6.00% | -1.66% | +1.38% | -3.04% | MISS | IN_CI | -0.964 |
| **DVA** | claude-fable-5 2026-07-07 | 236.71 | 2026-08-04 | +5.00% | -1.28% | +1.34% | -2.62% | MISS | IN_CI | -0.915 |
| **DVA** | gpt-5 2026-07-07 | 236.90 | 2026-08-04 | +6.00% | -1.36% | +1.38% | -2.74% | MISS | OUT_CI_LOW | -1.055 |
| **ESS** | claude-fable-5 2026-07-07 | 301.82 | 2026-08-04 | +5.00% | -5.28% | +1.34% | -6.63% | MISS | OUT_CI_LOW | -1.880 |
| **FFIV** | claude-fable-5 2026-07-07 | 420.72 | 2026-08-04 | +5.00% | -3.42% | +1.34% | -4.76% | MISS | IN_CI | -0.966 |
| **FFIV** | gpt-5 2026-07-07 | 420.76 | 2026-08-04 | +6.00% | -3.42% | +1.38% | -4.80% | MISS | OUT_CI_LOW | -1.064 |
| **FTNT** | claude-fable-5 2026-07-07 | 159.94 | 2026-08-04 | +5.00% | +2.04% | +1.34% | +0.70% | HIT | IN_CI | -0.235 |
| **FTNT** | gpt-5 2026-07-07 | 160.23 | 2026-08-04 | +6.00% | +1.86% | +1.38% | +0.48% | HIT | IN_CI | -0.325 |
| **HOOD** | gpt-5 2026-07-07 | 114.79 | 2026-08-04 | +6.00% | -21.30% | +1.38% | -22.68% | MISS | OUT_CI_LOW | -1.177 |
| **HUM** | gpt-5 2026-07-07 | 397.35 | 2026-08-04 | +6.00% | -5.75% | +1.38% | -7.13% | MISS | OUT_CI_LOW | -1.049 |
| **LIN** | claude-fable-5 2026-07-07 | 536.68 | 2026-08-04 | +4.00% | -10.48% | +1.34% | -11.82% | MISS | OUT_CI_LOW | -2.449 |
| **LLY** | claude-fable-5 2026-07-07 | 1230.67 | 2026-08-04 | +5.00% | -8.88% | +1.34% | -10.23% | MISS | OUT_CI_LOW | -1.422 |
| **LYV** | claude-fable-5 2026-07-07 | 185.28 | 2026-08-04 | +6.00% | -1.94% | +1.34% | -3.28% | MISS | OUT_CI_LOW | -1.203 |
| **MAS** | claude-fable-5 2026-07-07 | 79.36 | 2026-08-04 | +6.00% | -5.83% | +1.34% | -7.18% | MISS | OUT_CI_LOW | -1.256 |
| **MNST** | claude-fable-5 2026-07-07 | 97.39 | 2026-08-04 | +5.00% | -3.94% | +1.34% | -5.29% | MISS | OUT_CI_LOW | -1.957 |
| **MRNA** | gpt-5 2026-07-07 | 79.14 | 2026-08-04 | +6.00% | -30.33% | +1.38% | -31.70% | MISS | OUT_CI_LOW | -1.614 |
| **PANW** | claude-fable-5 2026-07-07 | 345.76 | 2026-08-04 | +5.00% | +0.40% | +1.34% | -0.95% | MISS | IN_CI | -0.283 |
| **PANW** | gpt-5 2026-07-07 | 345.75 | 2026-08-04 | +6.00% | +0.40% | +1.38% | -0.98% | MISS | IN_CI | -0.339 |
| **RVTY** | claude-fable-5 2026-07-07 | 112.29 | 2026-08-04 | +6.00% | +2.61% | +1.34% | +1.26% | HIT | IN_CI | -0.286 |
| **TROW** | claude-fable-5 2026-07-07 | 120.75 | 2026-08-04 | +5.00% | -6.00% | +1.34% | -7.34% | MISS | OUT_CI_LOW | -1.771 |
| **TTWO** | claude-fable-5 2026-07-07 | 259.53 | 2026-08-04 | +6.00% | -5.54% | +1.34% | -6.89% | MISS | OUT_CI_LOW | -1.112 |
| **TTWO** | gpt-5 2026-07-07 | 259.53 | 2026-08-04 | +6.00% | -5.54% | +1.38% | -6.92% | MISS | OUT_CI_LOW | -1.093 |
| **UAL** | gpt-5 2026-07-07 | 129.12 | 2026-08-04 | +6.00% | -0.57% | +1.38% | -1.94% | MISS | IN_CI | -0.417 |
| **UNH** | gpt-5 2026-07-07 | 427.07 | 2026-08-04 | +6.00% | -2.74% | +1.38% | -4.12% | MISS | OUT_CI_LOW | -1.089 |
| **VRTX** | claude-fable-5 2026-07-07 | 524.22 | 2026-08-04 | +5.00% | -10.21% | +1.34% | -11.55% | MISS | OUT_CI_LOW | -1.852 |
| **VTRS** | claude-fable-5 2026-07-07 | 17.07 | 2026-08-04 | +6.00% | +3.28% | +1.34% | +1.94% | HIT | IN_CI | -0.342 |
| **WST** | gpt-5 2026-07-07 | 353.65 | 2026-08-04 | +6.00% | -1.62% | +1.38% | -2.99% | MISS | OUT_CI_LOW | -1.085 |
| **QQQ** *(MF)* | claude-fable-5 2026-07-07 | 709.86 | 2026-08-04 | +0.84% | -1.38% | N/A | N/A | MISS | IN_CI | -0.263 |
| **QQQ** *(MF)* | gpt-5 2026-07-07 | 709.21 | 2026-08-04 | +0.84% | -1.29% | N/A | N/A | MISS | IN_CI | -0.247 |
| **SOXX** *(MF)* | claude-fable-5 2026-07-07 | 547.93 | 2026-08-04 | +1.73% | -7.35% | N/A | N/A | MISS | IN_CI | -0.413 |
| **SOXX** *(MF)* | gpt-5 2026-07-07 | 546.34 | 2026-08-04 | +2.23% | -7.08% | N/A | N/A | MISS | IN_CI | -0.415 |
| **SPY** *(MF)* | claude-fable-5 2026-07-07 | 747.62 | 2026-08-04 | +0.50% | +1.34% | N/A | N/A | HIT | IN_CI | +0.195 |
| **SPY** *(MF)* | gpt-5 2026-07-07 | 747.37 | 2026-08-04 | +0.50% | +1.38% | N/A | N/A | HIT | IN_CI | +0.199 |

| Cohort | n | Direction hits | IN_CI | Mean z |
|---|---|---|---|---|
| `EQUITY_ALPHA` | 42 | 14/42 = **33.33%** | 23/42 = 54.76% | -0.7494 |
| `MARKET_FORECAST` | 6 | 2/6 = **33.33%** | 6/6 = 100.00% | -0.1574 |

### Rolling calibration metrics (canonical, all models)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range | Verdict |
|---|---|---|---|---|
| Raw n | 515 | 90 | ≥ 10 to report, ≥ 20 for Track A | reportable |
| 28-day `eff_n` | **1** | **1** | ≥ 3 for Track A | **gate fails** |
| Hit rate | 39.81% | 22.09% | > 50% | **below floor** |
| CI coverage | 69.90% | 81.11% | 55–85% (target 70%) | EQ healthy; MF near the upper bound |
| Mean z | -0.5191 | -0.6253 | −0.5 to +0.5 | **both below floor** |
| Rank IC (weighted mean) | -0.0879 | n/a | > 0 | **inverted** |

Worst vintages by rank IC:

| Vintage | n | Rank IC |
|---|---|---|
| gpt-5:2026-06-24 | 14 | -0.6571 |
| gemini-3.5-flash:2026-06-29 | 14 | -0.5912 |
| gpt-5:2026-06-28 | 14 | -0.5912 |
| gpt-5:2026-06-29 | 14 | -0.5912 |
| gpt-5:2026-07-01 | 14 | -0.5399 |
| claude-fable-5:2026-06-10 | 12 | -0.5105 |
| claude-sonnet-5:2026-07-03 | 12 | -0.4685 |
| claude-sonnet-5:2026-07-02 | 12 | -0.3916 |

**Binding consequences, applied to this run:**

1. Rank IC -0.0879 ≤ 0 over 515 ≥ 20 settled records →
   `agents.md § Calibration Feedback Binding` **caps every confidence label at `MEDIUM`**.
2. CI coverage 69.90% sits inside 55–85%, so the wider-sigma rule does **not**
   fire; sigma stays `REALIZED_VOL_30D`.
3. `eff_n` = 1 < 3 → **no Track A calibration change is eligible**; such findings are
   recorded and `DEFER`red, never `REJECT`ed.

### Track A eligibility projection

| Record type | Earliest target | Latest target | Span | `eff_n` increments on | Pending at that date |
|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 2026-07-08 | 2026-08-03 | 26d | **2026-08-05** | 43 |
| `MARKET_FORECAST` | 2026-07-12 | 2026-08-03 | 22d | **2026-08-09** | 6 |

The 2026-07-28 falsifiable claim — `EQUITY_ALPHA` `eff_n` reaches 2 on
2026-08-05 — is **not yet testable**: today is 2026-08-04, one day
earlier. It remains live and unfalsified.

## 1. Prior Run Summary and baseline selection

MoM window 2026-06-20 … 2026-07-14, target 2026-07-07. No `claude-opus-5` folder falls in
that window, so selection moved to the closest in-window cross-model folder →
**`CROSS_MODEL_BASELINE`**. Two folders tie at delta 0d.

### Rule 8 tie-break — every tied candidate disclosed (mandatory)

| Folder | Model | Δ to target | Same family | Usable ledger | Settled n | Hit rate | Mean alpha | Mean z | CI coverage | Selection |
|---|---|---|---|---|---|---|---|---|---|---|
| `claude-fable-5-2026-07-07` | claude-fable-5 | 0d | yes | yes | 22 | 36.36% | -2.99% | -0.8555 | 54.55% | **CHOSEN** |
| `gpt-5-2026-07-07` | gpt-5 | 0d | no | yes | 20 | 30.00% | -4.41% | -0.6328 | 55.00% |  |

Resolution order applied: **(a) same model family** → `claude-fable-5` matches the executing
`claude-opus-5` family and `gpt-5` does not, so (b) usable ledger and (c) lexicographic were not
reached.

**Is the MoM conclusion invariant across the tied books? YES.** The hit-rate spread is
**6.36pp** (30.00% vs 36.36%) — both far below the 50% healthy floor —
and both books carry negative mean alpha and mean z well below −0.5. Either choice supports the same
conclusion: the 2026-07-07 vintage was a losing cohort on both direction and magnitude. This is a
materially narrower spread than the 48pp (2026-07-29) and 40.7pp (2026-07-30) cases that motivated
the rule, and is reported either way as the rule requires.

Baseline book: **`claude-fable-5-2026-07-07`** — 22 `EQUITY_ALPHA` records, vintage
2026-07-07, status `NO_TRADE`.

## 2. MoM Price and Return Table

Prior price = the baseline book's recorded `entry_price` (`claude-fable-5-2026-07-07/15_predictions.json`);
current price = this run's grounded 2026-08-03 close (`L-PX-*`). Hit/Miss is **alpha-based** per
`rules.md § Settlement Rules`.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI Result |
|---|---|---|---|---|---|---|---|---|---|
| **DVA** | 2026-07-07 | 236.71 | 2026-08-03 | 233.68 | -1.28% | +1.34% | -2.62% | MISS | IN_CI |
| **BEN** | 2026-07-07 | 34.69 | 2026-08-03 | 35.24 | +1.59% | +1.34% | +0.24% | HIT | IN_CI |
| **PANW** | 2026-07-07 | 345.76 | 2026-08-03 | 347.13 | +0.40% | +1.34% | -0.95% | MISS | IN_CI |
| **CRWD** | 2026-07-07 | 196.95 | 2026-08-03 | 202.54 | +2.84% | +1.34% | +1.49% | HIT | IN_CI |
| **FTNT** | 2026-07-07 | 159.94 | 2026-08-03 | 163.21 | +2.04% | +1.34% | +0.70% | HIT | IN_CI |
| **VRTX** | 2026-07-07 | 524.22 | 2026-08-03 | 470.72 | -10.21% | +1.34% | -11.55% | MISS | OUT_CI_LOW |
| **DDOG** | 2026-07-07 | 263.18 | 2026-08-03 | 273.60 | +3.96% | +1.34% | +2.62% | HIT | IN_CI |
| **TTWO** | 2026-07-07 | 259.53 | 2026-08-03 | 245.15 | -5.54% | +1.34% | -6.89% | MISS | OUT_CI_LOW |
| **TROW** | 2026-07-07 | 120.75 | 2026-08-03 | 113.51 | -6.00% | +1.34% | -7.34% | MISS | OUT_CI_LOW |
| **VTRS** | 2026-07-07 | 17.07 | 2026-08-03 | 17.63 | +3.28% | +1.34% | +1.94% | HIT | IN_CI |
| **MAS** | 2026-07-07 | 79.36 | 2026-08-03 | 74.73 | -5.83% | +1.34% | -7.18% | MISS | OUT_CI_LOW |
| **LYV** | 2026-07-07 | 185.28 | 2026-08-03 | 181.69 | -1.94% | +1.34% | -3.28% | MISS | OUT_CI_LOW |
| **DAL** | 2026-07-07 | 89.35 | 2026-08-03 | 91.59 | +2.51% | +1.34% | +1.16% | HIT | IN_CI |
| **BAX** | 2026-07-07 | 23.03 | 2026-08-03 | 28.10 | +22.01% | +1.34% | +20.67% | HIT | OUT_CI_HIGH |
| **FFIV** | 2026-07-07 | 420.72 | 2026-08-03 | 406.35 | -3.42% | +1.34% | -4.76% | MISS | IN_CI |
| **MNST** | 2026-07-07 | 97.39 | 2026-08-03 | 93.55 | -3.94% | +1.34% | -5.29% | MISS | OUT_CI_LOW |
| **LLY** | 2026-07-07 | 1230.67 | 2026-08-03 | 1121.36 | -8.88% | +1.34% | -10.23% | MISS | OUT_CI_LOW |
| **AXON** | 2026-07-07 | 638.68 | 2026-08-03 | 575.88 | -9.83% | +1.34% | -11.18% | MISS | IN_CI |
| **RVTY** | 2026-07-07 | 112.29 | 2026-08-03 | 115.22 | +2.61% | +1.34% | +1.27% | HIT | IN_CI |
| **ESS** | 2026-07-07 | 301.82 | 2026-08-03 | 285.88 | -5.28% | +1.34% | -6.63% | MISS | OUT_CI_LOW |
| **LIN** | 2026-07-07 | 536.68 | 2026-08-03 | 480.46 | -10.48% | +1.34% | -11.82% | MISS | OUT_CI_LOW |
| **ABBV** | 2026-07-07 | 257.61 | 2026-08-03 | 245.10 | -4.86% | +1.34% | -6.20% | MISS | IN_CI |

Alpha-based hit rate over the baseline book: **8/22 = 36.36%**.
SPY returned +1.34% over the same
window, so this is a genuine alpha shortfall, not a falling-tape artifact.

## 3. Theme-Level Performance

| Prior theme cluster | Verdict | Evidence |
|---|---|---|
| Defensive Health Care leadership | **partial** | the cluster still ranks at the top of the deduplicated `Tech_Z` today (DXCM, BMY, BAX, COO, IQV, REGN in the top 13), but its settled alpha over the matured window was negative |
| Low-beta / low-volatility tilt | **failed** | the naive top-20 sleeve carries beta +0.5323, far below the 0.90 floor — the score keeps selecting defensives into a rising tape |
| Momentum persistence | **failed** | weighted-mean rank IC -0.0879: the highest-scored names were not the best alpha performers |

## 4. Regime Shift Assessment

| Dimension | Baseline vintage (2026-07-07) | This run (2026-08-04) | Implication |
|---|---|---|---|
| Declared regime | `BULL` (per baseline package) | `BULL` | unchanged — no factor-weight change owed |
| VIX | `UNAVAILABLE` in this artifact (not re-fetched for the vintage date) | 15.86 (2026-08-03) | subdued; supports the `BULL` call |
| SPY vs MA20 / MA50 | `UNAVAILABLE` | above both (757.67 vs MA20 746.01 / MA50 744.60) | trend intact |
| SPY 30d realized vol | `UNAVAILABLE` | 3.76% (prior 30d 4.17%) | falling — no vol-expansion shock |

Regime is unchanged at `BULL`, so the baseline family weights stand. The factor-weight
implication is **none**; the live problem is rank ordering inside the technical family, not the
regime label.

## 5. Carry-Forward Decisions

Prior-book names are re-scored on today's identical-basis cross-section. Decisions are ledger-backed
(`L-TI-*`, `L-RM-*`); every rank and score below is read back out of the computed manifest, not
transcribed.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| **DVA** | +0.4200 | Dialysis oligopoly re-rating on stable volumes; defensive  | -1.28% | **CARRY** | pctl 91.39 (rank 45/512) |
| **BEN** | +0.4060 | Asset-manager torque to risk-on flows; valuation re-rate o | +1.59% | **CARRY** | pctl 99.61 (rank 3/512) |
| **PANW** | +0.4000 | Platformization-led security demand; momentum leadership i | +0.40% | **DOWNGRADE** | pctl 69.28 (rank 158/512) |
| **CRWD** | +0.3830 | Endpoint/identity consolidation winner; high-momentum secu | +2.84% | **DOWNGRADE** | pctl 76.91 (rank 119/512) |
| **FTNT** | +0.3690 | Firewall refresh cycle + SASE attach; security spend resil | +2.04% | **CARRY** | pctl 98.63 (rank 8/512) |
| **VRTX** | +0.3610 | CF franchise durability + pain-pipeline optionality; defen | -10.21% | **DROP** | pctl 58.12 (rank 215/512) |
| **DDOG** | +0.3460 | Observability + AI-workload monitoring attach; high-growth | +3.96% | **CARRY** | pctl 90.61 (rank 49/512) |
| **TTWO** | +0.3360 | GTA VI cycle anticipation; content slate momentum | -5.54% | **DROP** | pctl 53.62 (rank 238/512) |
| **TROW** | +0.3200 | Flows inflection at a discounted asset manager; low-vol fi | -6.00% | **DOWNGRADE** | pctl 63.01 (rank 190/512) |
| **VTRS** | +0.3160 | Deep-value generics turnaround; low-beta momentum re-rate  | +3.28% | **CARRY** | pctl 84.93 (rank 78/512) |
| **MAS** | +0.2980 | Repair/remodel recovery leverage; housing-adjacent momentu | -5.83% | **DROP** | pctl 27.20 (rank 373/512) |
| **LYV** | +0.2950 | Live-events demand secular strength; concert calendar seas | -1.94% | **CARRY** | pctl 83.95 (rank 83/512) |
| **DAL** | +0.2950 | Premium-cabin/loyalty mix strength into summer travel peak | +2.51% | **CARRY** | pctl 82.19 (rank 92/512) |
| **BAX** | +0.2930 | Post-restructuring margin recovery; low-priced HC turnarou | +22.01% | **CARRY** | pctl 99.41 (rank 4/512) |
| **FFIV** | +0.2920 | App-delivery/security hybrid-infra demand; low-vol compoun | -3.42% | **DOWNGRADE** | pctl 77.30 (rank 117/512) |
| **MNST** | +0.2910 | Energy-drink share stability; staples momentum with low be | -3.94% | **DOWNGRADE** | pctl 68.69 (rank 161/512) |
| **LLY** | +0.2890 | GLP-1 franchise; defensive growth at elevated valuation; c | -8.88% | **DROP** | pctl 50.29 (rank 255/512) |
| **AXON** | +0.2730 | Taser/body-cam ecosystem lock-in; extreme momentum, extrem | -9.83% | **DROP** | pctl 45.79 (rank 278/512) |
| **RVTY** | +0.2710 | Life-sciences tools recovery; diagnostics mix shift | +2.61% | **CARRY** | pctl 93.15 (rank 36/512) |
| **ESS** | +0.2580 | West-coast multifamily REIT; negative-beta defensive with  | -5.28% | **DROP** | pctl 58.32 (rank 214/512) |
| **LIN** | +0.1840 | Industrial-gas compounder with pricing power; carry-forwar | -10.48% | **DROP** | pctl 18.59 (rank 417/512) |
| **ABBV** | +0.1440 | Skyrizi/Rinvoq momentum vs Humira erosion; carry-forward,  | -4.86% | **DOWNGRADE** | pctl 76.52 (rank 121/512) |

No `DROP` name re-enters today's scored set on new evidence; `DOWNGRADE` names fall to the
monitoring band or the rejection log strictly by percentile, never by hand.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (2026-08-03 completed close) — 28/28 grounded on 3 independent sources |
| Reflection confidence | **MEDIUM** |
| Rationale | settlement and MoM arithmetic are fully ledger-backed and the tie-break conclusion is invariant; but the underlying forecast quality is poor (hit rate below floor, rank IC inverted), so no directional conclusion is carried forward with strength |
| Structural issues found | (1) rank-order inversion persists at -0.0879; (2) `MARKET_FORECAST` mu derivation remains a category error at 22.09% hit rate; (3) `rate_sens` slot is not reproducible from the prior package's prose disclosure — see `13` |
