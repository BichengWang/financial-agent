# 02 — Reflection — 2026-08-28

Standalone month-over-month reflection. Every price, return and regime claim below cites an `01`
Source Ledger row or is marked `UNAVAILABLE`. Reflection completed **before** any scoring in `04`/`05`.

## 0. Prediction Settlement

### Settlements this run

**`settlements: []`** — this run settles **zero** predictions, and that is the correct output rather
than an omission.

The canonical ledger (L014, L014d) reports **2** due keys at
`as_of 2026-08-28`, and both are the `EQR` corporate-action keys first documented on 2026-08-22:

| Ticker | Model | Vintage | Target Date | Classification | Disposition |
|---|---|---|---|---|---|
| EQR | claude-opus-5 | 2026-07-26 | 2026-08-23 | `UNSETTLEABLE_CORPORATE_ACTION` | EQR renamed into VMRK (Vivmark Residential); no exchange ratio inferred, no settlement against a successor (L016) |
| EQR | gpt-5 | 2026-07-27 | 2026-08-24 | `UNSETTLEABLE_CORPORATE_ACTION` | EQR renamed into VMRK (Vivmark Residential); no exchange ratio inferred, no settlement against a successor (L016) |

No prediction anywhere in the corpus carries `target_date == 2026-08-28`. The
`claude-opus-5-2026-07-30`-era books matured on 2026-08-27 and were settled by the
`claude-opus-5-2026-08-27` run (229 keys); the next cohort is the **27** records in
`claude-opus-5-2026-08-01`, all targeting **2026-08-29** — a Saturday, so they settle
`WEEKEND_TARGET` at today's Friday close on the next run.

Per `rules.md § Canonical Settlement Ledger` item 5, keys with no valid candidate are reported as
**due, not settled**; the validator is not loosened to make the `EQR` keys fit. Per the same section's
explicit non-goal (Track B, 2026-08-22) no exchange ratio is inferred and no settlement is made
against the successor symbol `VMRK`.

### Rolling calibration metrics

Computed from `settlement_ledger.py` output (L014, L014a, L014b, L014c), never re-derived by hand
from raw `15_predictions.json` files. `80` packages scanned across all models.

| Metric | Healthy range | EQUITY_ALPHA | EQUITY_ALPHA verdict | MARKET_FORECAST |
|---|---|---|---|---|
| Hit rate | > 50% | 37.49% | **below band** | 40.11% |
| CI coverage | 55% – 85% (target 70%) | 71.88% | inside band | 90.55% |
| Mean z | -0.5 to +0.5 | -0.5553 | **below band** | -0.1848 |
| Rank IC (Spearman, per vintage) | > 0 | -0.0495 weighted mean over 69 vintages | **at or below 0** | `N/A` — rank IC is an `EQUITY_ALPHA` metric only |
| Raw n | ≥ 20 for Track A | 1355 | satisfied | 201 |
| eff_n (28d non-overlapping) | ≥ 3 for Track A | 2 | **not satisfied** | 2 |

Supporting counts: **1355** canonical `EQUITY_ALPHA`
settlements and **201** canonical
`MARKET_FORECAST` settlements from **1911** candidate rows;
**268** audit-only lineage rows; **0** conflicts;
**87** rejected rows.

**Rank IC detail.** Of 69 scored vintages, **38** are
negative; the median vintage rank IC is **-0.0496** and the n-weighted mean is
**-0.0495**. Rank IC ≤ 0 over ≥ 20 settled predictions triggers the
`rules.md § Rolling Calibration Metrics` binding: **confidence is frozen at a `MEDIUM` cap** until a
corrective change passes evolution policy. That cap is applied in `05` and `06`.

**Two failure modes, diagnosed separately.** Magnitude calibration is mildly stretched
(mean z -0.5553, just outside the −0.5…+0.5 band) while CI coverage
71.88% sits comfortably inside 55–85%. Rank-order behaviour is the separate and
larger problem. A mu shrink or sigma widen is a monotonic transform and **cannot** repair a rank-order
inversion — that standing proposal remains retired (2026-07-26).

### Track A eligibility

| Record type | raw n | n ≥ 20 | eff_n | eff_n ≥ 3 | Track A calibration proposals |
|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 1355 | YES | 2 | **NO** | `INSUFFICIENT_EFFECTIVE_N` — DEFER, never REJECT |
| `MARKET_FORECAST` | 201 | YES | 2 | **NO** | `INSUFFICIENT_EFFECTIVE_N` — DEFER, never REJECT |

The `eff_n` projection emitted by `settlement_ledger.py` remains **falsifiable and on track**:

| Record type | Target-date span | Selected windows | eff_n → 3 on | Pending at that date |
|---|---|---|---|---|
| `EQUITY_ALPHA` | 2026-07-08 .. 2026-08-27 (50d) | 2026-07-08, 2026-08-05 | **2026-09-03** | 24 |
| `MARKET_FORECAST` | 2026-07-12 .. 2026-08-27 (46d) | 2026-07-12, 2026-08-09 | **2026-09-07** | 3 |

Any run on or after those dates still reporting `eff_n` 2 for that record type refutes the projection
and reverts the 2026-07-28 change that produced it.

## 1. Prior Run Summary

Baseline folder **`claude-opus-5-2026-07-30`** (L015) — selected by the
`agents.md § Orchestrator Step 2` algorithm: MoM window 2026-07-14 … 2026-08-07,
target 2026-07-31, delta **1d**, age **29d**
(≥ the 21-day floor), flag **`OK`**.

**Tie-break (rule 8, mandatory disclosure).** 2 folders sat at delta
1d. Rule 8(a) (same model family) and 8(b) (usable `15_predictions.json`) did
not discriminate — both are `claude-opus-5` packages carrying prediction records — so 8(c)
lexicographic selected `claude-opus-5-2026-07-30`. Every tied candidate, with its own settled statistics:

| Tied folder | Settled n | Hit rate | Mean alpha | Mean z | CI coverage | Note |
|---|---|---|---|---|---|---|
| `claude-opus-5-2026-07-30` | 24 | 16.67% | -7.20% | -0.8667 | 66.67% | selected by rule 8(c) lexicographic |
| `claude-opus-5-2026-08-01` | 0 | `UNAVAILABLE` | `UNAVAILABLE` | `UNAVAILABLE` | `UNAVAILABLE` | 27 records, all `target_date` 2026-08-29 — not yet due, so no settled statistics exist |

**Is the MoM conclusion invariant across the tied candidates? Yes, by construction.** Only one tied
book has any settled record; `claude-opus-5-2026-08-01`'s 27 predictions target 2026-08-29 and are not
yet due, so it supplies no competing hit rate, alpha or z. This is a materially weaker tie than the
48pp (2026-07-29) and 40.7pp (2026-07-30) spreads that motivated rule 8 — but the disclosure is made
either way, because a baseline chosen without showing the alternatives silently selects the narrative.

**Baseline run characteristics** (from that package): status `NO_TRADE`, 24 `EQUITY_ALPHA` records and
3 `MARKET_FORECAST` records, entry basis 2026-07-29 close, `target_date` 2026-08-27. Its canonical
settled outcome — hit rate **16.67%**, mean alpha
**-7.20%**, mean z
**-0.8667**, CI coverage
**66.67%** — was already settled and published by the
2026-08-27 run; it is restated here as context, not re-settled.

## 2. MoM Price and Return Table

Prior prices are the baseline package's own recorded `entry_price` values; current prices are this
run's grounded basis-date closes (L200+, L017). This is a **29-day realized read**, one session
past the book's 2026-08-27 `target_date`, so it is a short-window cross-check and **not** the settled
record. Hit/Miss is alpha-based per `rules.md § Settlement Rules`.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| FTNT | 2026-07-29 | 153.22 | 2026-08-28 | 166.00 | +8.34% | +5.47% | +2.87% | Hit | `IN_CI` | mu +6.00% |
| NTAP | 2026-07-29 | 173.23 | 2026-08-28 | 187.02 | +7.96% | +5.47% | +2.49% | Hit | `IN_CI` | mu +6.00% |
| HPQ | 2026-07-29 | 28.41 | 2026-08-28 | 30.52 | +7.43% | +5.47% | +1.96% | Hit | `IN_CI` | mu +6.00% |
| IQV | 2026-07-29 | 247.56 | 2026-08-28 | 261.75 | +5.73% | +5.47% | +0.26% | Hit | `IN_CI` | mu +6.00% |
| HUM | 2026-07-29 | 365.41 | 2026-08-28 | 385.54 | +5.51% | +5.47% | +0.04% | Hit | `IN_CI` | mu +6.00% |
| ADP | 2026-07-29 | 273.37 | 2026-08-28 | 287.48 | +5.16% | +5.47% | -0.31% | Miss | `IN_CI` | mu +6.00% |
| SJM | 2026-07-29 | 126.35 | 2026-08-28 | 132.34 | +4.74% | +5.47% | -0.73% | Miss | `IN_CI` | mu +6.00% |
| PAYX | 2026-07-29 | 122.13 | 2026-08-28 | 127.04 | +4.02% | +5.47% | -1.45% | Miss | `IN_CI` | mu +6.00% |
| CPAY | 2026-07-29 | 392.85 | 2026-08-28 | 407.88 | +3.83% | +5.47% | -1.64% | Miss | `IN_CI` | mu +6.00% |
| IEX | 2026-07-29 | 229.52 | 2026-08-28 | 230.28 | +0.33% | +5.47% | -5.14% | Miss | `OUT_CI_LOW` | mu +6.00% |
| GEHC | 2026-07-29 | 71.90 | 2026-08-28 | 71.72 | -0.24% | +5.47% | -5.71% | Miss | `IN_CI` | mu +6.00% |
| RTX | 2026-07-29 | 215.25 | 2026-08-28 | 211.71 | -1.64% | +5.47% | -7.11% | Miss | `IN_CI` | mu +6.00% |
| BRO | 2026-07-29 | 74.87 | 2026-08-28 | 73.31 | -2.08% | +5.47% | -7.55% | Miss | `IN_CI` | mu +6.00% |
| INCY | 2026-07-29 | 127.10 | 2026-08-28 | 124.37 | -2.15% | +5.47% | -7.62% | Miss | `IN_CI` | mu +6.00% |
| MRSH | 2026-07-29 | 197.59 | 2026-08-28 | 192.64 | -2.51% | +5.47% | -7.97% | Miss | `IN_CI` | mu +6.00% |
| GRMN | 2026-07-29 | 294.83 | 2026-08-28 | 285.19 | -3.27% | +5.47% | -8.74% | Miss | `IN_CI` | mu +6.00% |
| TRV | 2026-07-29 | 389.01 | 2026-08-28 | 369.90 | -4.91% | +5.47% | -10.38% | Miss | `OUT_CI_LOW` | mu +6.00% |
| BXP | 2026-07-29 | 72.97 | 2026-08-28 | 69.32 | -5.00% | +5.47% | -10.47% | Miss | `OUT_CI_LOW` | mu +6.00% |
| CTAS | 2026-07-29 | 216.53 | 2026-08-28 | 204.18 | -5.70% | +5.47% | -11.17% | Miss | `OUT_CI_LOW` | mu +6.00% |
| BBY | 2026-07-29 | 90.17 | 2026-08-28 | 82.44 | -8.57% | +5.47% | -14.04% | Miss | `OUT_CI_LOW` | mu +6.00% |
| F | 2026-07-29 | 15.28 | 2026-08-28 | 13.88 | -9.16% | +5.47% | -14.63% | Miss | `OUT_CI_LOW` | mu +6.00% |
| VRSK | 2026-07-29 | 213.15 | 2026-08-28 | 191.77 | -10.03% | +5.47% | -15.50% | Miss | `OUT_CI_LOW` | mu +6.00% |
| FICO | 2026-07-29 | 1,373.08 | 2026-08-28 | 1,153.57 | -15.99% | +5.47% | -21.46% | Miss | `OUT_CI_LOW` | mu +6.00% |
| DVA | 2026-07-29 | 240.96 | 2026-08-28 | 180.68 | -25.02% | +5.47% | -30.49% | Miss | `OUT_CI_LOW` | mu +6.00% |

Book summary: **24/24** names priced on the basis date, mean return
**-1.80%** against SPY **+5.47%** for mean alpha
**-7.27%**; hit rate **20.83%**; **15** of
24 inside the recorded 70% CI. These figures track the canonical settled record for the
same book (16.67% hit,
-7.20% mean alpha) to within the one extra session
of drift, which is the expected relationship — the canonical row settles at the 2026-08-27 target-date
close, this table reads the 2026-08-28 close.

### Core ETF market-forecast leg of the same baseline

| ETF | Prior Price | Current Price | Raw Return | mu | Direction | CI | Scoring basis |
|---|---|---|---|---|---|---|---|
| SPY | 729.46 | 769.35 | +5.47% | +0.50% | HIT | `OUT_CI` | raw-return scoring per `rules.md § Settlement Rules`; `SPY Return` / `Alpha` = `N/A` |
| QQQ | 661.73 | 716.43 | +8.27% | +0.85% | HIT | `OUT_CI` | raw-return scoring per `rules.md § Settlement Rules`; `SPY Return` / `Alpha` = `N/A` |
| SOXX | 465.00 | 508.62 | +9.38% | +1.82% | HIT | `IN_CI` | raw-return scoring per `rules.md § Settlement Rules`; `SPY Return` / `Alpha` = `N/A` |

All three core-ETF calls were directionally right and all three under-forecast the magnitude — the
same magnitude-compression signature the `MARKET_FORECAST` CI coverage of 90.55%
(above the 85% ceiling) reflects.

## 3. Theme-Level Performance

Sector attribution of the baseline book's realized alpha (sectors from L010):

| Sector | Names | Mean Alpha | Verdict |
|---|---|---|---|
| Consumer Staples | 1 | -0.73% | failed |
| Technology | 5 | -1.70% | failed |
| Industrials | 6 | -8.04% | failed |
| Finance | 3 | -8.64% | failed |
| Health Care | 5 | -8.70% | failed |
| Real Estate | 1 | -10.47% | failed |
| Consumer Discretionary | 3 | -12.38% | failed |

**All 7 sector themes failed.** Nothing in the book was rescued by sector selection,
which is itself diagnostic: the loss is not a sector bet gone wrong but a cross-sectional ranking that
was inverted against a broad +5.47% market. The defensive tilt that produced
the book — negative-beta, low-momentum-dispersion names — is exactly what underperforms a rising tape.

## 4. Regime Shift Assessment

| Dimension | Baseline run (2026-07-30 basis 2026-07-29) | This run (2026-08-28) | Implication |
|---|---|---|---|
| Declared regime | `BULL` | `BULL` | unchanged |
| SPY 20d momentum | `UNAVAILABLE` in this artifact — see the baseline package `03` | +2.99% | positive and improving |
| VIX | `UNAVAILABLE` in this artifact — see the baseline package `03` | 14.43 (prior 14.51) | low and falling |
| SPY realized vol (30d, ann.) | `UNAVAILABLE` in this artifact | 11.70% vs prior-30d 15.58% | **falling** |
| Realized SPY move over the window | — | +5.47% | risk-on continued through the window |

Factor-weight implication: none. The family weights in `rules.md § Factor Architecture` are fixed
absent an evolution-policy change, and `eff_n` = 2 bars any Track A weight or mu-table work
regardless of what this window shows.

## 5. Carry-Forward Decisions

Prior scores are the baseline package's recorded `adj_score`; today's ranks and percentiles are
recomputed from this run's cross-section (never asserted — see `05`). Decision floors:
`CARRY` at ≥ 80th percentile, `DOWNGRADE` in [60, 80), `DROP` below the 60th-percentile rank floor.

| Ticker | Prior Score | Prior Thesis | MoM Return | Today Rank | Today Pctl | Today Score | Decision | Rationale |
|---|---|---|---|---|---|---|---|---|
| SJM | +0.2665 | trend/technical composite, 2 of 4 families UNAVAILABLE | +4.74% | 5 | 99.21 | +0.3079 | **CARRY** | pctl 99.21 >= 80 investable-rank floor |
| IQV | +0.3169 | trend/technical composite, 2 of 4 families UNAVAILABLE | +5.73% | 9 | 98.43 | +0.3020 | **CARRY** | pctl 98.43 >= 80 investable-rank floor |
| HUM | +0.2763 | trend/technical composite, 2 of 4 families UNAVAILABLE | +5.51% | 48 | 90.77 | +0.2148 | **CARRY** | pctl 90.77 >= 80 investable-rank floor |
| FTNT | +0.2698 | trend/technical composite, 2 of 4 families UNAVAILABLE | +8.34% | 56 | 89.19 | +0.2034 | **CARRY** | pctl 89.19 >= 80 investable-rank floor |
| ADP | +0.2802 | trend/technical composite, 2 of 4 families UNAVAILABLE | +5.16% | 93 | 81.93 | +0.1576 | **CARRY** | pctl 81.93 >= 80 investable-rank floor |
| CPAY | +0.2724 | trend/technical composite, 2 of 4 families UNAVAILABLE | +3.83% | 100 | 80.55 | +0.1534 | **CARRY** | pctl 80.55 >= 80 investable-rank floor |
| INCY | +0.2897 | trend/technical composite, 2 of 4 families UNAVAILABLE | -2.15% | 128 | 75.05 | +0.1288 | **DOWNGRADE** | pctl 75.05 in [60,80) monitoring band |
| TRV | +0.2926 | trend/technical composite, 2 of 4 families UNAVAILABLE | -4.91% | 132 | 74.26 | +0.1250 | **DOWNGRADE** | pctl 74.26 in [60,80) monitoring band |
| PAYX | +0.2701 | trend/technical composite, 2 of 4 families UNAVAILABLE | +4.02% | 135 | 73.67 | +0.1234 | **DOWNGRADE** | pctl 73.67 in [60,80) monitoring band |
| BRO | +0.2513 | trend/technical composite, 2 of 4 families UNAVAILABLE | -2.08% | 142 | 72.30 | +0.1185 | **DOWNGRADE** | pctl 72.30 in [60,80) monitoring band |
| MRSH | +0.2531 | trend/technical composite, 2 of 4 families UNAVAILABLE | -2.51% | 147 | 71.32 | +0.1144 | **DOWNGRADE** | pctl 71.32 in [60,80) monitoring band |
| BXP | +0.2946 | trend/technical composite, 2 of 4 families UNAVAILABLE | -5.00% | 165 | 67.78 | +0.0957 | **DOWNGRADE** | pctl 67.78 in [60,80) monitoring band |
| BBY | +0.3256 | trend/technical composite, 2 of 4 families UNAVAILABLE | -8.57% | 171 | 66.60 | +0.0921 | **DOWNGRADE** | pctl 66.60 in [60,80) monitoring band |
| HPQ | +0.2492 | trend/technical composite, 2 of 4 families UNAVAILABLE | +7.43% | 177 | 65.42 | +0.0857 | **DOWNGRADE** | pctl 65.42 in [60,80) monitoring band |
| IEX | +0.2231 | trend/technical composite, 2 of 4 families UNAVAILABLE | +0.33% | 185 | 63.85 | +0.0815 | **DOWNGRADE** | pctl 63.85 in [60,80) monitoring band |
| CTAS | +0.2283 | trend/technical composite, 2 of 4 families UNAVAILABLE | -5.70% | 186 | 63.65 | +0.0814 | **DOWNGRADE** | pctl 63.65 in [60,80) monitoring band |
| GEHC | +0.2831 | trend/technical composite, 2 of 4 families UNAVAILABLE | -0.24% | 191 | 62.67 | +0.0782 | **DOWNGRADE** | pctl 62.67 in [60,80) monitoring band |
| RTX | +0.2359 | trend/technical composite, 2 of 4 families UNAVAILABLE | -1.64% | 241 | 52.85 | +0.0302 | **DROP** | pctl 52.85 < 60 rank floor |
| GRMN | +0.3309 | trend/technical composite, 2 of 4 families UNAVAILABLE | -3.27% | 248 | 51.47 | +0.0184 | **DROP** | pctl 51.47 < 60 rank floor |
| NTAP | +0.3116 | trend/technical composite, 2 of 4 families UNAVAILABLE | +7.96% | 324 | 36.54 | -0.0653 | **DROP** | pctl 36.54 < 60 rank floor |
| F | +0.2777 | trend/technical composite, 2 of 4 families UNAVAILABLE | -9.16% | 337 | 33.99 | -0.0828 | **DROP** | pctl 33.99 < 60 rank floor |
| VRSK | +0.2203 | trend/technical composite, 2 of 4 families UNAVAILABLE | -10.03% | 402 | 21.22 | -0.1481 | **DROP** | pctl 21.22 < 60 rank floor |
| FICO | +0.2830 | trend/technical composite, 2 of 4 families UNAVAILABLE | -15.99% | 420 | 17.68 | -0.1746 | **DROP** | pctl 17.68 < 60 rank floor |
| DVA | +0.2224 | trend/technical composite, 2 of 4 families UNAVAILABLE | -25.02% | 459 | 10.02 | -0.2353 | **DROP** | pctl 10.02 < 60 rank floor |

Decisions: **6 CARRY · 11 DOWNGRADE · 7 DROP**.
These bind factor scoring in `05`: no `DROP` name may enter today's scored set on carry-forward
grounds alone. In practice none needed to be forced out — every `DROP` name fell below the rank floor
on today's own cross-section, and `EQR` is excluded upstream by the corporate-action classifier (L016).

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `DELAYED` — basis-date closes retrieved this run (L200+, L017) |
| Reflection confidence | **MEDIUM** |
| Confidence rationale | Settlement arithmetic and rolling metrics come from the canonical normalizer with 0 conflicts; the MoM read is grounded on three agreeing vendors. Capped below HIGH because 2 of 4 factor families are `UNAVAILABLE` and the rank-IC binding is active. |
| Structural issues found | (1) 2 permanently unsettleable EQR keys still consume due inventory and therefore suppress `eff_n` growth; (2) all 7 baseline themes failed, consistent with the standing rank-order-inversion diagnosis rather than a new fault; (3) 12 of the 20 trading days from 2026-08-03 to 2026-08-28 have no package from any model (2026-08-05, 2026-08-11, 2026-08-12, 2026-08-13, 2026-08-17, 2026-08-18, 2026-08-19, 2026-08-20, 2026-08-21, 2026-08-24, 2026-08-25, 2026-08-26) — the scheduler gap is the largest structural reliability problem in the series. |

