# 02 — Reflection (Month-over-Month)

Baseline `agents/equity/output/claude-fable-5-2026-07-10` · flag `CROSS_MODEL_BASELINE` · run date `2026-08-07`.

Every price, return and regime claim below cites `01_preflight.md` ledger rows or is marked
`UNAVAILABLE`. Reflection completes before any scoring begins.

## 0. Prediction Settlement

**No canonical settlements were published this run.** 50 keys were due
at `--as-of 2026-08-07` — 44 `EQUITY_ALPHA` + 6 `MARKET_FORECAST`, every one with
`vintage 2026-07-10` and `target_date 2026-08-07`. All 50 were priced at the grounded
2026-08-07 close (`L003`, `L015`, `L018`) and fully scored. None was written as a canonical
row.

The reason is a validator condition, not an evidence gap. This run fired at 22:02 ET and its
settlement pass executed after midnight, so a truthful `settled_at` timestamp falls on
`2026-08-08`. `settlement_ledger.py:577` requires `settled_at.date() == target_date` *in
addition to* the 16:00 ET floor, so it rejects a timestamp that is merely **later** than the
target-date close — strictly stronger evidence that a completed close was used.
`rules.md § Canonical Settlement Ledger` item 5 says such keys are reported as due and the
validator is not loosened without a logged change, so that is what this package does. The
keys settle `ORDINARY` on the next run at this same close; the evidence is deferred, not lost.
The fix is proposed as Track B in `13_evolution_log.md`.

The scored results are reported here as a **diagnostic** (`L018`) because they are what the
MoM analysis below is built on:

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| ZBRA | 2026-07-10 | 272.52 | 2026-08-07 | +6.00% | +38.15% | +2.43% | +35.73% | HIT | OUT_CI_HIGH | +2.4320 |
| ABNB | 2026-07-10 | 148.62 | 2026-08-07 | +6.00% | +19.82% | +2.43% | +17.39% | HIT | OUT_CI_HIGH | +1.3998 |
| CRL | 2026-07-10 | 233.41 | 2026-08-07 | +6.00% | +14.60% | +2.43% | +12.18% | HIT | IN_CI | +0.6015 |
| CRWD | 2026-07-10 | 187.18 | 2026-08-07 | +6.00% | +14.55% | +2.43% | +12.13% | HIT | IN_CI | +0.5088 |
| PANW | 2026-07-10 | 325.91 | 2026-08-07 | +5.00% | +11.64% | +2.43% | +9.22% | HIT | IN_CI | +0.3667 |
| DAL | 2026-07-10 | 87.39 | 2026-08-07 | +6.00% | +4.52% | +2.43% | +2.09% | HIT | IN_CI | -0.1337 |
| AIZ | 2026-07-10 | 278.89 | 2026-08-07 | +5.00% | +3.82% | +2.43% | +1.40% | HIT | IN_CI | -0.2256 |
| TTWO | 2026-07-10 | 243.20 | 2026-08-07 | +6.00% | +1.36% | +2.43% | -1.07% | MISS | IN_CI | -0.4704 |
| FTNT | 2026-07-10 | 157.51 | 2026-08-07 | +5.00% | +1.35% | +2.43% | -1.07% | MISS | IN_CI | -0.2812 |
| AXON | 2026-07-10 | 565.80 | 2026-08-07 | +6.00% | +0.92% | +2.43% | -1.50% | MISS | IN_CI | -0.2303 |
| ANET | 2026-07-10 | 186.96 | 2026-08-07 | +4.00% | +0.91% | +2.43% | -1.51% | MISS | IN_CI | -0.1643 |
| BEN | 2026-07-10 | 33.50 | 2026-08-07 | +5.00% | +0.81% | +2.43% | -1.62% | MISS | IN_CI | -0.5017 |
| CSCO | 2026-07-10 | 121.31 | 2026-08-07 | +6.00% | +0.10% | +2.43% | -2.33% | MISS | IN_CI | -0.4980 |
| LLY | 2026-07-10 | 1,188.58 | 2026-08-07 | +3.00% | -0.24% | +2.43% | -2.67% | MISS | IN_CI | -0.3159 |
| ABBV | 2026-07-10 | 248.08 | 2026-08-07 | +2.00% | -0.82% | +2.43% | -3.25% | MISS | IN_CI | -0.2874 |
| BBY | 2026-07-10 | 82.80 | 2026-08-07 | +6.00% | -0.97% | +2.43% | -3.39% | MISS | IN_CI | -0.4292 |
| MELI | 2026-07-10 | 1,852.22 | 2026-08-07 | +6.00% | -1.70% | +2.43% | -4.13% | MISS | IN_CI | -0.7973 |
| HUM | 2026-07-10 | 392.22 | 2026-08-07 | +5.00% | -1.84% | +2.43% | -4.27% | MISS | IN_CI | -0.6163 |
| TROW | 2026-07-10 | 118.55 | 2026-08-07 | +5.00% | -3.82% | +2.43% | -6.25% | MISS | OUT_CI_LOW | -1.3245 |
| FFIV | 2026-07-10 | 430.39 | 2026-08-07 | +6.00% | -7.01% | +2.43% | -9.43% | MISS | OUT_CI_LOW | -1.5090 |
| MNST | 2026-07-10 | 97.39 | 2026-08-07 | +5.00% | -7.22% | +2.43% | -9.64% | MISS | OUT_CI_LOW | -2.4784 |
| LIN | 2026-07-10 | 529.79 | 2026-08-07 | +4.00% | -7.51% | +2.43% | -9.94% | MISS | OUT_CI_LOW | -1.8814 |
| DDOG | 2026-07-10 | 257.54 | 2026-08-07 | +6.00% | -9.17% | +2.43% | -11.59% | MISS | IN_CI | -0.8029 |
| DVA | 2026-07-10 | 232.80 | 2026-08-07 | +6.00% | -21.06% | +2.43% | -23.49% | MISS | OUT_CI_LOW | -3.8168 |
| QQQ | 2026-07-10 | 725.51 | 2026-08-07 | +0.84% | -0.34% | N/A | N/A | MISS | IN_CI | -0.1377 |
| SOXX | 2026-07-10 | 581.34 | 2026-08-07 | +1.76% | -6.55% | N/A | N/A | MISS | IN_CI | -0.3813 |
| SPY | 2026-07-10 | 754.95 | 2026-08-07 | +0.50% | +2.43% | N/A | N/A | HIT | IN_CI | +0.4336 |

Diagnostic aggregates over the 50 deferred keys:

| Record type | n | Hits | Hit rate | IN_CI | CI coverage | Mean z |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 24 | 7 | 29.17% | 17 | 70.83% | -0.4773 |
| `MARKET_FORECAST` | 3 | 1 | 33.33% | 3 | 100.00% | -0.0285 |

*(the table above covers only the baseline book's rows; the aggregate row counts span all 50
deferred keys across both books — see § 1 for the per-book split.)*

### Canonical rolling calibration (unchanged this run)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range |
|---|---|---|---|
| raw `n` | 643 | 108 | >= 10 to report, >= 20 for Track A |
| 28-day `eff_n` | **2** | 1 | >= 3 for Track A |
| Hit rate | 39.04% | 25.96% | > 50% |
| CI coverage | 69.36% | 84.26% | 55% – 85% |
| Mean z | -0.5328 | -0.5285 | -0.5 to +0.5 |
| Track A eligible | False | False | n >= 20 AND eff_n >= 3 |

Weighted-mean rank IC across vintages: **-0.0430**.

Three readings matter:

1. **Hit rate 39.04% is far below the 50% bar** and has been for the whole
   series. CI coverage 69.36% sits inside the healthy 55–85% band, so the
   intervals are honest; the *direction* calls are not.
2. **Mean z -0.5328 is at the edge of the healthy band**, meaning realized
   returns land systematically below `mu` — the mu table is over-forecasting.
3. **Rank IC -0.0430 is negative but small.**
   `rules.md` freezes confidence at `MEDIUM` when rank IC <= 0 over >= 20 settled predictions;
   that binds this run and is applied in `05`.

`eff_n` remains 2 for equities and 1 for market forecasts, so **no
Track A calibration change is eligible** — the finding is recorded and deferred, per
`rules.md § Rolling Calibration Metrics`. The `MARKET_FORECAST` projection to increment on
`2026-08-09` is still pending and is **not** falsified by
this run: the 6 MF keys that would have moved it are exactly the ones deferred above.

Files scanned: every `15_predictions.json` under `agents/equity/output/` —
76 packages, 1106 candidate
rows, 268 audit-only, 87 rejected,
0 conflicts.

## 1. Prior Run Summary

The MoM window is `run_date - 45d` … `run_date - 21d` (2026-06-23 … 2026-07-17) with target
`2026-07-10`. **No `claude-opus-5` folder exists in the window**, so rule 4 selects the closest
in-window cross-model folder and sets `CROSS_MODEL_BASELINE`.

Two folders tie at delta **0d**. Rule 8 is mandatory here, and both candidates are disclosed:

| Tied candidate | delta from target | EQ n | Hit rate | CI coverage | Mean alpha | Mean z | Vintage rank IC | Selected? |
|---|---|---|---|---|---|---|---|---|
| `claude-fable-5-2026-07-10` | 0d | 24 | 29.17% | 70.83% | -0.29% | -0.4773 | +0.1083 (p=0.614, n=24) | **YES** |
| `gpt-5-2026-07-10` | 0d | 20 | 35.00% | 85.00% | -5.85% | -0.5587 | -0.0496 (p=0.835, n=20) | no |

Tie-break applied: **(a) same model family as the executing model** — `claude-fable-5` shares
the `claude` family with `claude-opus-5`, `gpt-5` does not. Both candidates have a usable
`15_predictions.json`, so rules 8(b) and 8(c) were not reached.

**Is the MoM conclusion invariant across the tied books? Yes — qualitatively, and this run
says so explicitly.** Both books produced a hit rate far below 50%
(29.17% vs 35.00%, spread
5.8pp), both produced **negative** mean alpha, and both produced mean z near
-0.5. Every conclusion drawn in §§ 2–5 holds under either baseline.

The spread is nonetheless worth recording: mean alpha differs by 5.56pp
(-0.29% vs -5.85%), driven by book
composition rather than luck — the `gpt-5` book's mean *raw* return was
-3.42% against +2.13% for the selected
book. That is far narrower than the 48pp (2026-07-29) and 40.7pp (2026-07-30) spreads that made
this rule mandatory, but the direction of the lesson is the same: the two books are not
interchangeable, and picking one without showing the other would have silently selected the
narrative.

Selected baseline `claude-fable-5-2026-07-10`: final status `NO_TRADE`, top-5 by `adj_score`:

| # | Ticker | adj_score | mu | Confidence |
|---|---|---|---|---|
| 1 | DVA | 0.5500 | +6.00% | LOW |
| 2 | CRL | 0.4050 | +6.00% | LOW |
| 3 | CRWD | 0.3860 | +6.00% | LOW |
| 4 | DDOG | 0.3690 | +6.00% | LOW |
| 5 | FTNT | 0.3590 | +5.00% | LOW |

## 2. MoM Price & Return Table

Prior price is each prediction's own recorded `entry_price`; current price is the grounded
2026-08-07 close (`L003`). SPY moved +2.43% over the same window
(`L015`). Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| ZBRA | 2026-07-10 | 272.52 | 2026-08-07 | 376.49 | +38.15% | +2.43% | +35.73% | HIT | OUT_CI_HIGH |
| ABNB | 2026-07-10 | 148.62 | 2026-08-07 | 178.07 | +19.82% | +2.43% | +17.39% | HIT | OUT_CI_HIGH |
| CRL | 2026-07-10 | 233.41 | 2026-08-07 | 267.49 | +14.60% | +2.43% | +12.18% | HIT | IN_CI |
| CRWD | 2026-07-10 | 187.18 | 2026-08-07 | 214.42 | +14.55% | +2.43% | +12.13% | HIT | IN_CI |
| PANW | 2026-07-10 | 325.91 | 2026-08-07 | 363.86 | +11.64% | +2.43% | +9.22% | HIT | IN_CI |
| DAL | 2026-07-10 | 87.39 | 2026-08-07 | 91.34 | +4.52% | +2.43% | +2.09% | HIT | IN_CI |
| AIZ | 2026-07-10 | 278.89 | 2026-08-07 | 289.55 | +3.82% | +2.43% | +1.40% | HIT | IN_CI |
| TTWO | 2026-07-10 | 243.20 | 2026-08-07 | 246.50 | +1.36% | +2.43% | -1.07% | MISS | IN_CI |
| FTNT | 2026-07-10 | 157.51 | 2026-08-07 | 159.64 | +1.35% | +2.43% | -1.07% | MISS | IN_CI |
| AXON | 2026-07-10 | 565.80 | 2026-08-07 | 571.01 | +0.92% | +2.43% | -1.50% | MISS | IN_CI |
| ANET | 2026-07-10 | 186.96 | 2026-08-07 | 188.67 | +0.91% | +2.43% | -1.51% | MISS | IN_CI |
| BEN | 2026-07-10 | 33.50 | 2026-08-07 | 33.77 | +0.81% | +2.43% | -1.62% | MISS | IN_CI |
| CSCO | 2026-07-10 | 121.31 | 2026-08-07 | 121.43 | +0.10% | +2.43% | -2.33% | MISS | IN_CI |
| LLY | 2026-07-10 | 1,188.58 | 2026-08-07 | 1,185.71 | -0.24% | +2.43% | -2.67% | MISS | IN_CI |
| ABBV | 2026-07-10 | 248.08 | 2026-08-07 | 246.04 | -0.82% | +2.43% | -3.25% | MISS | IN_CI |
| BBY | 2026-07-10 | 82.80 | 2026-08-07 | 82.00 | -0.97% | +2.43% | -3.39% | MISS | IN_CI |
| MELI | 2026-07-10 | 1,852.22 | 2026-08-07 | 1,820.69 | -1.70% | +2.43% | -4.13% | MISS | IN_CI |
| HUM | 2026-07-10 | 392.22 | 2026-08-07 | 385.00 | -1.84% | +2.43% | -4.27% | MISS | IN_CI |
| TROW | 2026-07-10 | 118.55 | 2026-08-07 | 114.02 | -3.82% | +2.43% | -6.25% | MISS | OUT_CI_LOW |
| FFIV | 2026-07-10 | 430.39 | 2026-08-07 | 400.23 | -7.01% | +2.43% | -9.43% | MISS | OUT_CI_LOW |
| MNST | 2026-07-10 | 97.39 | 2026-08-07 | 90.36 | -7.22% | +2.43% | -9.64% | MISS | OUT_CI_LOW |
| LIN | 2026-07-10 | 529.79 | 2026-08-07 | 489.98 | -7.51% | +2.43% | -9.94% | MISS | OUT_CI_LOW |
| DDOG | 2026-07-10 | 257.54 | 2026-08-07 | 233.93 | -9.17% | +2.43% | -11.59% | MISS | IN_CI |
| DVA | 2026-07-10 | 232.80 | 2026-08-07 | 183.77 | -21.06% | +2.43% | -23.49% | MISS | OUT_CI_LOW |

## 3. Theme-Level Performance

| Theme (today's sector) | Names | Hits | Mean alpha | Verdict | Members |
|---|---|---|---|---|---|
| Health Care | 5 | 1/5 | -4.30% | failed | CRL, LLY, ABBV, HUM, DVA |
| Technology | 5 | 2/5 | +1.52% | validated | CRWD, PANW, TTWO, FTNT, DDOG |
| Consumer Discretionary | 4 | 2/4 | +2.99% | validated | ABNB, DAL, BBY, MELI |
| Finance | 3 | 1/3 | -2.16% | failed | AIZ, BEN, TROW |
| Telecommunications | 3 | 0/3 | -4.42% | failed | ANET, CSCO, FFIV |
| Industrials | 2 | 1/2 | +17.11% | validated | ZBRA, AXON |
| Consumer Staples | 1 | 0/1 | -9.64% | failed | MNST |
| Basic Materials | 1 | 0/1 | -9.94% | failed | LIN |

## 4. Regime Shift Assessment

| Dimension | Prior vintage (2026-07-10) | Current (2026-08-07) | Implication |
|---|---|---|---|
| Declared regime | see baseline package | `BULL` | SPY prior mu set to +2.00% |
| SPY level | 754.95 | 773.26 | +2.43% over the window |
| VIX | UNAVAILABLE (not re-fetched for the prior date) | 14.9 | low-vol tape; supports a BULL classification |
| Realized breadth | UNAVAILABLE | 47.95% | index at highs on **narrow** breadth — a genuine divergence, disclosed in 03 |
| Factor-weight implication | n/a | none | family weights are fixed absent an evolution change; no Track A eligibility |

The window was a **rising tape** (+2.43% on SPY) in which the prior
book still produced negative mean alpha. That is the signature of the long-diagnosed
rank-order inversion, not of a directional miss: with `Fund_Z`/`Sent_Z` unavailable, `Tech_Z`
carries 66.67% of live conviction and is pure trend-persistence, so it ranks the trailing
60-day winners first and underperforms through a rotation.

## 5. Carry-Forward Decisions

Decisions bind factor scoring when ledger-backed. `DROP` names stay out of today's scored set
absent new ledger evidence.

| Ticker/Theme | Prior Score (realized alpha) | Prior Thesis | MoM Return (alpha) | Decision | Rationale |
|---|---|---|---|---|---|
| ABNB | +0.1739 | mu +6.00% | +17.39% | CARRY | still in the >=80th pctl pool at rank 2 (pctl 99.61) |
| CRL | +0.1218 | mu +6.00% | +12.18% | CARRY | still in the >=80th pctl pool at rank 24 (pctl 95.30) |
| AIZ | +0.0140 | mu +5.00% | +1.40% | CARRY | still in the >=80th pctl pool at rank 43 (pctl 91.59) |
| BEN | -0.0162 | mu +5.00% | -1.62% | CARRY | still in the >=80th pctl pool at rank 60 (pctl 88.26) |
| BBY | -0.0339 | mu +6.00% | -3.39% | CARRY | still in the >=80th pctl pool at rank 63 (pctl 87.67) |
| PANW | +0.0922 | mu +5.00% | +9.22% | CARRY | still in the >=80th pctl pool at rank 67 (pctl 86.89) |
| CRWD | +0.1213 | mu +6.00% | +12.13% | CARRY | still in the >=80th pctl pool at rank 75 (pctl 85.32) |
| FTNT | -0.0107 | mu +5.00% | -1.07% | CARRY | still in the >=80th pctl pool at rank 79 (pctl 84.54) |
| DAL | +0.0209 | mu +6.00% | +2.09% | CARRY | still in the >=80th pctl pool at rank 83 (pctl 83.76) |
| HUM | -0.0427 | mu +5.00% | -4.27% | DOWNGRADE | fell to rank 110 (pctl 78.47) — monitoring band only |
| AXON | -0.0150 | mu +6.00% | -1.50% | DOWNGRADE | fell to rank 131 (pctl 74.36) — monitoring band only |
| MELI | -0.0413 | mu +6.00% | -4.13% | DOWNGRADE | fell to rank 136 (pctl 73.39) — monitoring band only |
| LLY | -0.0267 | mu +3.00% | -2.67% | DOWNGRADE | fell to rank 169 (pctl 66.93) — monitoring band only |
| ABBV | -0.0325 | mu +2.00% | -3.25% | DOWNGRADE | fell to rank 176 (pctl 65.56) — monitoring band only |
| DDOG | -0.1159 | mu +6.00% | -11.59% | DOWNGRADE | fell to rank 191 (pctl 62.62) — monitoring band only |
| ZBRA | +0.3573 | mu +6.00% | +35.73% | DOWNGRADE | fell to rank 195 (pctl 61.84) — monitoring band only |
| TTWO | -0.0107 | mu +6.00% | -1.07% | DOWNGRADE | fell to rank 200 (pctl 60.86) — monitoring band only |
| ANET | -0.0151 | mu +4.00% | -1.51% | DROP | fell below the 60th-pctl rank floor at rank 230 (pctl 54.99) |
| TROW | -0.0625 | mu +5.00% | -6.25% | DROP | fell below the 60th-pctl rank floor at rank 276 (pctl 45.99) |
| CSCO | -0.0233 | mu +6.00% | -2.33% | DROP | fell below the 60th-pctl rank floor at rank 308 (pctl 39.73) |
| MNST | -0.0964 | mu +5.00% | -9.64% | DROP | fell below the 60th-pctl rank floor at rank 310 (pctl 39.33) |
| FFIV | -0.0943 | mu +6.00% | -9.43% | DROP | fell below the 60th-pctl rank floor at rank 333 (pctl 34.83) |
| DVA | -0.2349 | mu +6.00% | -23.49% | DROP | fell below the 60th-pctl rank floor at rank 422 (pctl 17.42) |
| LIN | -0.0994 | mu +4.00% | -9.94% | DROP | fell below the 60th-pctl rank floor at rank 469 (pctl 8.22) |

Summary: **9 CARRY · 8 DOWNGRADE · 7 DROP**. Every decision is derived
from today's computed rank and percentile (`run_computed_manifest.json`), not hand-assigned —
the 2026-07-26 failure mode where 14 of 14 hand-written carry-forward ranks were wrong.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (completed 2026-08-07 close) |
| Grounding | 27/27 on 3 independent sources, max deviation 0.0000% |
| Reflection confidence | **MEDIUM** |
| Canonical settlements added | 0 (50 deferred — see § 0) |

**Confidence rationale (MEDIUM).** Prices and returns are grounded to the cent on three
independent sources, and the settlement arithmetic was computed in full, so the *numbers*
here are solid. Confidence is held at MEDIUM rather than HIGH for two reasons: the MoM
baseline is cross-model (`CROSS_MODEL_BASELINE`), so it compares this model's process against
another model's book; and this run's own settlement rows are unpublished, so the canonical
calibration figures quoted in § 0 are inherited from the prior run rather than advanced by
this one.

**Structural issues found this run.**

1. **`TARGET_DATE_CLOSE` validator is too narrow** — it rejects a settlement stamped later
   than the target date's calendar day even though such a timestamp is strictly stronger
   evidence. Any post-close run whose pipeline crosses midnight silently defers its whole
   settlement queue. Track B proposal in `13`.
2. **Hit rate 39.04% with CI coverage 69.36%** — the
   intervals are calibrated but the direction calls are not; a magnitude-only fix cannot
   address a rank-order problem, and Track A remains gated at `eff_n = 2`.
3. **No 2026-08-05 package exists in the audit trail** (carried forward from the 2026-08-06
   manifest, unresolved and not resolvable retroactively).
