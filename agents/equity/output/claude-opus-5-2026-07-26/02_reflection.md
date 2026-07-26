# 02 Reflection — 2026-07-26

Standalone month-over-month reflection. Every price, return, regime and thesis-validation claim below cites `01_preflight.md` ledger rows or is marked `UNAVAILABLE` / `INFERRED`. Completed **before** any new scoring.

- **Baseline:** `agents/equity/output/gpt-5-2026-06-28` — flag **`CROSS_MODEL_BASELINE`**
- **Window:** `2026-06-11 → 2026-07-05`, target `2026-06-28`; the baseline is an exact hit at 0 days from target. Baseline age 28 days (≥21-day invariant satisfied). 31 folders sat in-window; the only `claude-opus-5` folder in existence (`2026-07-24`) is 2 days old and therefore barred.
- **Ledger scan:** every `15_predictions.json` under `agents/equity/output/` (all models, all dates), normalized through `settlement_ledger.py --as-of 2026-07-26` (L138).

---

## § 0 — Prediction Settlement

**17 predictions matured this run** — every one from vintage `gpt-5-2026-06-28` with `target_date = 2026-07-26`. That target date is a **Sunday**, so all 17 settle under the **`WEEKEND_TARGET`** exception at the last trading close at or before target: the **2026-07-24 close** (L136). No prediction was held open past its target date, and none was settled on an intraday print.

Settlement prices are 3-source verified to the cent (L001, `price_verification.json`). Arithmetic per `rules.md § Settlement Rules` steps 1–6 (L137).

| Ticker | Type | Vintage | Entry | Target Date | Settle (07-24) | mu | Realized | SPY Ret | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAT | EQUITY_ALPHA | 2026-06-28 | 997.47 | 2026-07-26 | 888.73 | +6.00% | -10.90% | +1.36% | -12.27% | **MISS** | OUT_CI_LOW | -1.19 |
| LLY | EQUITY_ALPHA | 2026-06-28 | 1208.12 | 2026-07-26 | 1196.03 | +6.00% | -1.00% | +1.36% | -2.36% | **MISS** | IN_CI | -0.71 |
| GOOGL | EQUITY_ALPHA | 2026-06-28 | 337.39 | 2026-07-26 | 319.74 | +5.00% | -5.23% | +1.36% | -6.59% | **MISS** | OUT_CI_LOW | -1.26 |
| UNH | EQUITY_ALPHA | 2026-06-28 | 427.89 | 2026-07-26 | 420.74 | +5.00% | -1.67% | +1.36% | -3.03% | **MISS** | IN_CI | -0.89 |
| GE | EQUITY_ALPHA | 2026-06-28 | 369.00 | 2026-07-26 | 353.73 | +4.00% | -4.14% | +1.36% | -5.50% | **MISS** | IN_CI | -0.83 |
| BAC | EQUITY_ALPHA | 2026-06-28 | 57.88 | 2026-07-26 | 62.05 | +3.00% | +7.20% | +1.36% | +5.84% | **HIT** | IN_CI | +0.81 |
| JPM | EQUITY_ALPHA | 2026-06-28 | 329.05 | 2026-07-26 | 353.21 | +3.00% | +7.34% | +1.36% | +5.98% | **HIT** | IN_CI | +0.63 |
| CVX | EQUITY_ALPHA | 2026-06-28 | 171.06 | 2026-07-26 | 194.79 | +2.00% | +13.87% | +1.36% | +12.51% | **HIT** | OUT_CI_HIGH | +1.57 |
| SHW | EQUITY_ALPHA | 2026-06-28 | 344.07 | 2026-07-26 | 317.51 | +2.00% | -7.72% | +1.36% | -9.08% | **MISS** | OUT_CI_LOW | -1.10 |
| EQIX | EQUITY_ALPHA | 2026-06-28 | 1091.30 | 2026-07-26 | 1084.24 | +2.00% | -0.65% | +1.36% | -2.01% | **MISS** | IN_CI | -0.46 |
| V | EQUITY_ALPHA | 2026-06-28 | 336.23 | 2026-07-26 | 355.74 | +1.00% | +5.80% | +1.36% | +4.44% | **HIT** | IN_CI | +0.85 |
| GS | EQUITY_ALPHA | 2026-06-28 | 1019.61 | 2026-07-26 | 1061.23 | +1.00% | +4.08% | +1.36% | +2.72% | **HIT** | IN_CI | +0.28 |
| FCX | EQUITY_ALPHA | 2026-06-28 | 62.45 | 2026-07-26 | 62.60 | +1.00% | +0.24% | +1.36% | -1.12% | **MISS** | IN_CI | -0.05 |
| AAPL | EQUITY_ALPHA | 2026-06-28 | 283.78 | 2026-07-26 | 333.02 | +1.00% | +17.35% | +1.36% | +15.99% | **HIT** | OUT_CI_HIGH | +1.96 |
| QQQ | MARKET_FORECAST | 2026-06-28 | 706.52 | 2026-07-26 | 684.23 | +1.87% | -3.15% | N/A | N/A | **MISS** | IN_CI | -0.63 |
| SOXX | MARKET_FORECAST | 2026-06-28 | 589.94 | 2026-07-26 | 527.01 | +4.01% | -10.67% | N/A | N/A | **MISS** | IN_CI | -0.71 |
| SPY | MARKET_FORECAST | 2026-06-28 | 728.99 | 2026-07-26 | 738.93 | +1.00% | +1.36% | N/A | N/A | **HIT** | IN_CI | +0.08 |

**This batch, by record type:**

| | n | HIT | Hit rate | IN_CI | CI coverage | Mean z |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 14 | 6 | 42.86% | 9 | 64.29% | −0.028 |
| `MARKET_FORECAST` | 3 | 1 | 33.33% | 3 | 100.00% | −0.420 |

SPY returned **+1.36%** over the window (728.99 → 738.93), so alpha is scored against a modestly rising tape — five of the six `MISS` calls are names that fell in absolute terms as well.

### The finding that matters: a significant rank-order inversion

Sorting this vintage's 14 equity forecasts by the `adj_score` they were assigned at vintage, against the alpha they actually delivered:

| Score cohort | Mean realized alpha | Hits |
|---|---|---|
| Top 7 by `adj_score` (100.0 → 81.8) | **−2.56%** | 2 / 7 |
| Bottom 7 by `adj_score` (78.8 → 60.6) | **+3.35%** | 4 / 7 |

**Rank IC (Spearman, `adj_score` vs `realized_alpha`) = −0.5912, p = 0.026, n = 14.** The extremes invert cleanly: the highest-scored name (CAT, 100.0) delivered the worst alpha in the batch (−12.27%), and the lowest-scored name (AAPL, 60.6) delivered the best (+15.99%).

This is the same failure mode the 2026-07-22 run identified (a 71.4% hit-rate batch with rank IC −0.712) and it is **not** a magnitude-calibration problem. A mu shrink or a sigma widening is a monotonic transform of the score — it cannot repair an ordering that is inverted. Diagnosis and disposition in `13_evolution_log.md`.

### Rolling calibration (all models, full history, post-settlement)

Source: `settlement_manifest.json § rolling_metrics` (L138). `EQUITY_ALPHA` and `MARKET_FORECAST` are reported separately and never pooled.

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range | Verdict |
|---|---|---|---|---|
| Raw `n` | 203 (was 189) | 36 (was 33) | ≥ 20 for Track A | pass |
| **`eff_n` (28-day non-overlapping)** | **1** | **1** | **≥ 3 for Track A** | **fail** |
| Hit rate | 52.22% | **22.22%** | > 50% | pass / **fail** |
| CI coverage | 75.37% | 66.67% | 55–85% | pass / pass |
| Mean z | −0.2001 | **−0.7047** | −0.5 to +0.5 | pass / **fail** |
| Rank IC (weighted mean, 14 vintages) | **−0.1282** | n/a | > 0 | **fail** |
| Track A calibration proposal eligible | **No** — `INSUFFICIENT_EFFECTIVE_N` | **No** — `INSUFFICIENT_EFFECTIVE_N` | | |

**`eff_n` did not move.** Adding 17 settlements took raw `n` from 189 to 203, but the new target date (2026-07-26) sits only 18 calendar days after the earliest target date in the settled pool — inside the same 28-day window. The effective independent sample remains **1** for both record types. This is the gate accepted on 2026-07-24 doing exactly its job: it prevents a 14-name batch drawn from one overlapping cohort from licensing a parameter change.

The rank IC weighted mean **deteriorated** from −0.0939 to −0.1282 with this vintage's −0.5912 added.

### Calibration feedback binding today's scoring

Per `agents.md § Calibration Feedback Binding`:

- **Rank IC ≤ 0 over ≥ 20 settled equity predictions** (−0.1282, n=203) → **all confidence capped at `MEDIUM`**. Recorded as active; non-binding in effect because every published name is independently forced to `LOW` by the family-coverage gap (L144, L145).
- **CI coverage 75.37% is inside the healthy 55–85% band** → the sigma-widening override does **not** fire. `REALIZED_VOL_30D` remains the sigma source.
- **No positive per-name `mu` adjustments** were made anywhere in this run. Every `mu` in `05` is the unmodified mu-Calibration-Table value for the name's percentile band.

---

## § 1 — Prior Run Summary

| Field | Value |
|---|---|
| Date / model | 2026-06-28 / `gpt-5` |
| Final status | **`NO_TRADE`** |
| Data mode | `DELAYED` (prices dated 2026-06-26) |
| Regime | Not separately labelled in the baseline's `03`; its `09` describes a rising, mega-cap-led tape |
| Portfolio | None published — `NO_TRADE` |
| Reason for no trade | *"the investable set cannot meet the protected 0.90–1.10 NAV beta band under the 5% single-name cap"* |
| Top-5 by `adj_score` | CAT 100.0, LLY 97.0, GOOGL 93.9, UNH 90.9, GE 87.9 — all `MEDIUM` confidence |
| Forecasts published | 17 (14 equity + 3 core ETF), all settled today |

**Continuity note (`INFERRED`, L141):** the baseline failed on *exactly the same* beta-band infeasibility that fails again today (L141: max attainable top-10 beta −0.159). Four weeks apart, two different models, two different candidate sets, same structural blocker. That persistence is itself evidence — see `13`.

---

## § 2 — MoM Price & Return Table

Because the baseline is also the settled vintage, the MoM table is the settlement table on its own terms: prior price = the vintage `entry_price` (2026-06-26, L001 of the baseline package), current price = the 2026-07-24 close (L136, 3-source verified). Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`; CI state is recorded because a CI was recorded at vintage.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| CAT | 2026-06-26 | 997.47 | 2026-07-24 | 888.73 | −10.90% | +1.36% | −12.27% | **Miss** | OUT_CI_LOW; worst alpha in batch, was top-ranked |
| LLY | 2026-06-26 | 1208.12 | 2026-07-24 | 1196.03 | −1.00% | +1.36% | −2.36% | **Miss** | IN_CI |
| GOOGL | 2026-06-26 | 337.39 | 2026-07-24 | 319.74 | −5.23% | +1.36% | −6.59% | **Miss** | OUT_CI_LOW |
| UNH | 2026-06-26 | 427.89 | 2026-07-24 | 420.74 | −1.67% | +1.36% | −3.03% | **Miss** | IN_CI |
| GE | 2026-06-26 | 369.00 | 2026-07-24 | 353.73 | −4.14% | +1.36% | −5.50% | **Miss** | IN_CI |
| BAC | 2026-06-26 | 57.88 | 2026-07-24 | 62.05 | +7.20% | +1.36% | +5.84% | **Hit** | IN_CI |
| JPM | 2026-06-26 | 329.05 | 2026-07-24 | 353.21 | +7.34% | +1.36% | +5.98% | **Hit** | IN_CI |
| CVX | 2026-06-26 | 171.06 | 2026-07-24 | 194.79 | +13.87% | +1.36% | +12.51% | **Hit** | OUT_CI_HIGH — sigma too tight |
| SHW | 2026-06-26 | 344.07 | 2026-07-24 | 317.51 | −7.72% | +1.36% | −9.08% | **Miss** | OUT_CI_LOW |
| EQIX | 2026-06-26 | 1091.30 | 2026-07-24 | 1084.24 | −0.65% | +1.36% | −2.01% | **Miss** | IN_CI |
| V | 2026-06-26 | 336.23 | 2026-07-24 | 355.74 | +5.80% | +1.36% | +4.44% | **Hit** | IN_CI |
| GS | 2026-06-26 | 1019.61 | 2026-07-24 | 1061.23 | +4.08% | +1.36% | +2.72% | **Hit** | IN_CI |
| FCX | 2026-06-26 | 62.45 | 2026-07-24 | 62.60 | +0.24% | +1.36% | −1.12% | **Miss** | IN_CI; positive raw return, negative alpha — correctly a Miss |
| AAPL | 2026-06-26 | 283.78 | 2026-07-24 | 333.02 | +17.35% | +1.36% | +15.99% | **Hit** | OUT_CI_HIGH — sigma far too tight on the best performer |

FCX is the textbook case for alpha-based scoring: **+0.24% raw is a Miss**, because the benchmark did better.

---

## § 3 — Theme-Level Performance

| Prior theme | Names | Outcome | Evidence |
|---|---|---|---|
| **Mega-cap quality / AI complex** | GOOGL, LLY, UNH | **Failed** | All three negative alpha (−6.59%, −2.36%, −3.03%). QQQ −3.15% and SOXX −10.67% over the same window confirm this was a broad growth de-rating, not stock selection |
| **Industrial / capex cycle** | CAT, GE, SHW | **Failed** | −12.27%, −5.50%, −9.08% alpha. The worst-performing theme in the batch |
| **Money-centre banks** | BAC, JPM, GS | **Validated** | +5.84%, +5.98%, +2.72% alpha; 3 for 3 |
| **Payments / consumer rails** | V | **Validated** | +4.44% alpha |
| **Energy** | CVX | **Validated** | +12.51% alpha, though OUT_CI_HIGH — the direction was right and the magnitude badly under-forecast |
| **Materials / mining** | FCX | **Partial** | +0.24% raw but −1.12% alpha; a lagging positive |
| **Data-centre REIT** | EQIX | **Failed** | −2.01% alpha |

**Synthesis (`INFERRED`, cites L025, L026, L028):** capital rotated *out* of growth and industrials and *into* financials, energy and defensives over these four weeks. The baseline's book was positioned almost exactly backwards relative to that rotation — which is what produces a −0.59 rank IC rather than merely a poor hit rate.

---

## § 4 — Regime Shift Assessment

| | Baseline (2026-06-28) | Current (2026-07-26, on the 07-24 close) | Shift |
|---|---|---|---|
| Declared regime | not labelled; `09` describes a rising mega-cap-led tape | **`NEUTRAL`** (L139) | Softer |
| SPY vs MA20 / MA50 | above both | **below both** (738.93 vs 746.15 / 744.12) | Deteriorated |
| SPY MACD (daily) | — | `BELOW_SIGNAL` | Deteriorated |
| QQQ | leading | **`BEARISH`** MA alignment, −8.20% from 60d high, RS20 −5.12pp vs SPY | Sharply weaker |
| SOXX | leading | **`BEARISH`**, −19.54% from 60d high, RS20 −16.34pp vs SPY | Sharply weaker |
| VIX | — | 18.58; 30d avg 17.12 vs prior-30d 17.60 (L005, L006) | Low, stable |
| TLT | — | 83.25, RSI 33.19, −4.45% from 60d high (L029) | Bonds weak |

**Factor-weight implication:** none. Family weights are fixed at 0.30/0.30/0.25/0.15 and only the evolution agent may change them under Track A — which is gated off at `eff_n = 1`. The regime read is expressed instead through the **disclosed defensive Macro polarity** (L140) documented in `05`, and through the core-ETF mu derivation in `03`.

**The rotation is confirmed by the settlements themselves**, not merely asserted: financials and energy delivered positive alpha while growth and industrials delivered negative alpha over precisely this window.

---

## § 5 — Carry-Forward Decisions

Binding on today's factor scoring where ledger-backed. Only names the baseline actually ranked appear here. Rank/percentile are today's values from `run_computed_manifest.json`; the 60th-percentile floor is `rules.md § mu Calibration Table` ("names below the 60th percentile are not ranked in either sleeve").

| Ticker | Prior Score | Prior Thesis | MoM Return (Alpha) | Today Rank / Pctl | Decision | Rationale |
|---|---|---|---|---|---|---|
| CAT | 100.0 | Industrial capex cycle | -10.90% (-12.27%) | 465/514 · 9.55 | **DROP** | Thesis failed. pctl 9.55 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| LLY | 97.0 | Mega-cap pharma | -1.00% (-2.36%) | 135/514 · 73.88 | **DOWNGRADE** | Thesis failed. still inside the ranked band (pctl 73.88) but outside the top-30 publication cut; CONFIRMED earnings 2026-08-05 (10d) carries the −0.10 penalty and caps confidence LOW |
| GOOGL | 93.9 | AI/search franchise | -5.23% (-6.59%) | 453/514 · 11.89 | **DROP** | Thesis failed. pctl 11.89 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| UNH | 90.9 | Managed care recovery | -1.67% (-3.03%) | 134/514 · 74.07 | **DOWNGRADE** | Thesis failed. still inside the ranked band (pctl 74.07) but outside the top-30 publication cut |
| GE | 87.9 | Aerospace/industrial | -4.14% (-5.50%) | 246/514 · 52.24 | **DROP** | Thesis failed. pctl 52.24 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| BAC | 84.8 | Money-centre bank | +7.20% (+5.84%) | 44/514 · 91.62 | **DOWNGRADE** | Thesis validated. still inside the ranked band (pctl 91.62) but outside the top-30 publication cut |
| JPM | 81.8 | Money-centre bank | +7.34% (+5.98%) | 47/514 · 91.03 | **DOWNGRADE** | Thesis validated. still inside the ranked band (pctl 91.03) but outside the top-30 publication cut |
| CVX | 78.8 | Integrated energy | +13.87% (+12.51%) | 228/514 · 55.75 | **DROP** | Thesis validated. pctl 55.75 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| SHW | 75.8 | Coatings/housing | -7.72% (-9.08%) | 352/514 · 31.58 | **DROP** | Thesis failed. pctl 31.58 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| EQIX | 72.7 | Data-centre REIT | -0.65% (-2.01%) | 224/514 · 56.53 | **DROP** | Thesis failed. pctl 56.53 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| V | 69.7 | Payments rails | +5.80% (+4.44%) | 67/514 · 87.13 | **DOWNGRADE** | Thesis validated. still inside the ranked band (pctl 87.13) but outside the top-30 publication cut |
| GS | 66.7 | Investment bank | +4.08% (+2.72%) | 280/514 · 45.61 | **DROP** | Thesis validated. pctl 45.61 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| FCX | 63.6 | Copper/mining | +0.24% (-1.12%) | 422/514 · 17.93 | **DROP** | Thesis failed. pctl 17.93 is below the 60th-percentile ranking floor — rejection log only, not ranked in either sleeve |
| AAPL | 60.6 | Mega-cap hardware | +17.35% (+15.99%) | 127/514 · 75.44 | **DOWNGRADE** | Thesis validated. still inside the ranked band (pctl 75.44) but outside the top-30 publication cut; CONFIRMED earnings 2026-07-30 (4d) carries the −0.10 penalty and caps confidence LOW |

**8 DROP, 6 DOWNGRADE, 0 CARRY, 0 PROMOTE.** No name is carried into an investable set because there is no investable set — the run is `NO_TRADE`. The `DROP` decisions bind today's scoring, and each is independently supported: all eight sit below the 60th-percentile ranking floor on their own merits, so none appears in either sleeve.

**Two observations worth recording.** First, the decisions do not track thesis outcome — CVX and GS were *validated* (+12.51% and +2.72% alpha) yet are dropped, because the move has already happened and their current technical/macro setup no longer ranks. Second, BAC and JPM now sit at the 91.6th and 91.0th percentile, i.e. *above* the 80th-percentile investable bar on rank alone; they are unpublishable only because of the family-coverage gap and the top-30 cut, not because of anything about the names.

---

## § 6 — Sign-Off

**Freshness tag per price used:**

| Price | Tag | Basis |
|---|---|---|
| Settlement prices (17) | `HISTORICAL` | 2026-07-24 close, 3-source verified to the cent (L001, L136) |
| Vintage entry prices (17) | `DELAYED` | as recorded at vintage in `gpt-5-2026-06-28/15_predictions.json`, price_date 2026-06-26 |
| Today's entry prices (24 + 3 ETFs) | `HISTORICAL` | 2026-07-24 close (L001, L002, L028) |
| Benchmark SPY | `HISTORICAL` | 728.99 → 738.93, both ledger-backed |

**Reflection confidence: `HIGH`.** Justification: the settlement set is complete (`due_inventory: 0`, `conflicts: 0`), every settlement price is verified by three independent sources agreeing to the cent, the baseline is an exact 0-day hit on the MoM target date, and the baseline *is* the settled vintage — so §0 and §2 describe one coherent forecast cohort rather than two loosely-coupled ones. This is the strongest grounding a reflection in this system has had.

**Structural issues found:**

1. **Rank-order inversion, now statistically significant at the vintage level** (−0.5912, p=0.026, n=14) and negative in the pooled weighted mean (−0.1282 over 14 vintages, n=203). The composite score is anti-predictive on this evidence, not merely uninformative.
2. **`eff_n` remains 1** despite raw `n` reaching 203. No Track A calibration change is permissible. The next genuinely independent window opens around 2026-08-21.
3. **Sigma is too tight in the tails.** Both large winners breached the upper CI (AAPL z = +1.96, CVX z = +1.57) while overall CI coverage (75.37%) sits comfortably inside the healthy band — the interval is well-calibrated on average and under-dispersed at the extremes. Not actionable under Track A gating; recorded as an observation.
4. **`MARKET_FORECAST` remains structurally broken** — 22.22% hit rate, mean z −0.705 across n=36. Today's batch added QQQ and SOXX misses, both driven by the `mu = beta × SPY_mu` category error diagnosed on 2026-07-24. See `03` for how this run expresses a bearish ETF view within the rules as written.
