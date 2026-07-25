# 02 Reflection — 2026-07-24

Standalone MoM reflection. Completed before any scoring. Every price claim cites `01_preflight.md` ledger rows.

## 0. Prediction Settlement

### Settled this run

**None.** `settlements: []` in `15_predictions.json`, with a recorded note.

This is a true empty set, not a skipped scan. `settlement_ledger.py --output-dir agents/equity/output --as-of 2026-07-24` (ledger row L142) returns:

```
due_inventory: 0     conflicts: 0     conflicted_rows: 0
canonical_equity_alpha_settlements: 189
canonical_market_forecast_settlements: 33
audit_only_rows: 145     rejected_rows: 87     total_candidate_rows: 454
```

- The last target date to mature was **2026-07-22**, fully settled by the two 07-22 packages (`gpt-5-2026-07-22`, `claude-sonnet-5-2026-07-22`) using the `TARGET_DATE_CLOSE` mechanism accepted that day.
- **No prediction anywhere carries a target date of 2026-07-23 or 2026-07-24.** There was no 07-23 run in this repository, so no vintage seeded those dates.
- The next maturities are **17 keys dated 2026-07-26** — a Sunday. Because `target_date (2026-07-26) > run_date (2026-07-24)`, they are **not due today** and are correctly left `OPEN`. They will settle on the next run under `WEEKEND_TARGET`, at the last trading close at or before the target — which is today's 2026-07-24 close.
- The explicit `--as-of 2026-07-24` flag was required: `settlement_ledger.py` otherwise defaults `as_of` to the maximum package run_date (2026-07-20 precedent, where 68 weekend-target keys were invisible without it).

**Packages scanned:** every `15_predictions.json` under `agents/equity/output/` across all models (454 candidate settlement rows evaluated, 87 rejected on timing validity, 145 retained as audit-only lineage).

### Rolling calibration metrics

From `settlement_manifest.json § rolling_metrics` — the canonical source per `rules.md § Canonical Settlement Ledger` #6. `EQUITY_ALPHA` and `MARKET_FORECAST` are reported separately and never pooled.

| Metric | EQUITY_ALPHA | MARKET_FORECAST | Healthy range | Verdict |
|---|---|---|---|---|
| n (canonical settlements) | 189 | 33 | ≥ 10 to report | reportable |
| Hit rate | 52.91% | **21.21%** | > 50% | equity OK; **market forecast badly broken** |
| CI coverage | 76.19% | 63.64% | 55–85% (target 70%) | both inside band |
| Mean z | −0.213 | **−0.731** | −0.5 to +0.5 | equity OK; **market forecast outside** |
| Rank IC (weighted mean, 13 vintages) | **−0.0939** | n/a | > 0 | **negative** |

**Bindings triggered for today's scoring** (per `agents.md § Calibration Feedback Binding`):

1. **Rank IC ≤ 0 over ≥ 20 settled predictions** → cap all confidence at `MEDIUM`. Logged as active. Every published name is independently forced to `LOW` by the family-coverage gap, so the cap does not change any published label.
2. CI coverage 76.19% is **inside** 55–85%, so the sigma-widening / no-positive-mu-adjustment override does **not** fire. `mu` is taken straight from the calibration table with no positive per-name adjustments regardless (see `05`).

### Effective sample size — material caveat

The raw `n` above overstates the independent evidence by roughly two orders of magnitude, and this run quantified it (ledger row L143):

| Type | n | Distinct vintages | Vintage span | Target-date span | Non-overlapping 28d target windows |
|---|---|---|---|---|---|
| `MARKET_FORECAST` | 33 | 10 | 2026-06-14 → 2026-06-24 | 2026-07-12 → 2026-07-22 | **1** |
| `EQUITY_ALPHA` | 189 | 12 | 2026-06-10 → 2026-06-24 | 2026-07-08 → 2026-07-22 | **1** |

Every canonical settlement in the system originates from a **single overlapping forecast cohort**: near-identical forecasts issued on consecutive days in mid-June, all resolving into one two-week window in mid-July. "n=189" is not 189 independent bets; it is approximately one market episode observed 189 times. This is the subject of this run's accepted Track B change — see `13_evolution_log.md`.

### Market-forecast decomposition

Because the `MARKET_FORECAST` hit rate is the worst metric in the system, it was decomposed rather than merely reported:

| ETF | n | mean mu | mean realized | mean z | Direction |
|---|---|---|---|---|---|
| SPY | 11 | +1.86% | +0.35% | −0.357 | 6 HIT / 5 MISS |
| QQQ | 11 | +2.99% | −3.65% | −0.878 | 1 HIT / 10 MISS |
| SOXX | 11 | +5.60% | −12.73% | −0.957 | **0 HIT / 11 MISS** |

100% of the 33 forecasts carried a positive `mu`; only 21% of realized returns were positive. **SPY's own regime-prior forecast is acceptable** (54.5% direction, z −0.36). The failure is entirely in the beta-amplified ETFs, and it is *directional*, not a magnitude error. Diagnosis and the two rejected corrections are in `13_evolution_log.md`.

## 1. Prior Run Summary

- **Baseline:** `agents/equity/output/gpt-5-2026-06-24` — flag `CROSS_MODEL_BASELINE`, 2 days from the `run_date − 28d` target, age 30 days (≥21 invariant satisfied). No `claude-opus-5` folder exists anywhere, so no same-model baseline is possible on this model's first run. `gpt-5-2026-06-28` tied at 2 days; the tie was broken toward the earlier date.
- **Prior status:** the baseline package published 14 ranked `EQUITY_ALPHA` names plus 3 `MARKET_FORECAST` records, all with `target_date` 2026-07-22 and `MEDIUM`/`LOW` confidence.
- **Prior regime:** the baseline scored a broad mega-cap-led tape with financials and industrials participating.
- **Top-5 by prior adj score:** CAT (100.0), GOOGL (97.1), GE (94.1), LLY (91.2), FCX (88.2).
- All 14 baseline predictions were settled at their 2026-07-22 target by the 07-22 runs; they are part of the 189 canonical `EQUITY_ALPHA` settlements above and are **not** re-settled here.

## 2. MoM Price & Return Table

Prior prices are the baseline's recorded `entry_price` (ledger row L148, `HISTORICAL`). Current prices are the 2026-07-24 close (ledger rows L001–L029 where published today; all 14 sourced from the same verified bar set). SPY benchmark: 733.24 → 738.93 = **+0.78%**. Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`, never raw return.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Today Rank | Today Pctl | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CAT | 2026-06-24 | 994.45 | 2026-07-24 | 888.73 | -10.63% | +0.78% | -11.41% | Miss | 482 | 6.2 | DROP |
| GOOGL | 2026-06-24 | 345.29 | 2026-07-24 | 319.74 | -7.40% | +0.78% | -8.18% | Miss | 451 | 12.3 | DROP |
| GE | 2026-06-24 | 365.88 | 2026-07-24 | 353.73 | -3.32% | +0.78% | -4.10% | Miss | 240 | 53.4 | DROP |
| LLY | 2026-06-24 | 1117.26 | 2026-07-24 | 1196.03 | +7.05% | +0.78% | +6.27% | Hit | 126 | 75.6 | DOWNGRADE |
| FCX | 2026-06-24 | 61.84 | 2026-07-24 | 62.60 | +1.23% | +0.78% | +0.45% | Hit | 421 | 18.1 | DROP |
| GS | 2026-06-24 | 1076.91 | 2026-07-24 | 1061.23 | -1.46% | +0.78% | -2.23% | Miss | 279 | 45.8 | DROP |
| BAC | 2026-06-24 | 57.73 | 2026-07-24 | 62.05 | +7.48% | +0.78% | +6.71% | Hit | 39 | 92.6 | CARRY |
| CVX | 2026-06-24 | 171.45 | 2026-07-24 | 194.79 | +13.61% | +0.78% | +12.84% | Hit | 338 | 34.3 | DROP |
| UNH | 2026-06-24 | 405.80 | 2026-07-24 | 420.74 | +3.68% | +0.78% | +2.91% | Hit | 115 | 77.8 | DOWNGRADE |
| EQIX | 2026-06-24 | 1095.00 | 2026-07-24 | 1084.24 | -0.98% | +0.78% | -1.76% | Miss | 328 | 36.3 | DROP |
| JPM | 2026-06-24 | 333.45 | 2026-07-24 | 353.21 | +5.93% | +0.78% | +5.15% | Hit | 42 | 92.0 | CARRY |
| NVDA | 2026-06-24 | 199.00 | 2026-07-24 | 206.84 | +3.94% | +0.78% | +3.16% | Hit | 352 | 31.6 | DROP |
| V | 2026-06-24 | 332.23 | 2026-07-24 | 355.74 | +7.08% | +0.78% | +6.30% | Hit | 224 | 56.5 | DROP |
| AAPL | 2026-06-24 | 293.08 | 2026-07-24 | 333.02 | +13.63% | +0.78% | +12.85% | Hit | 114 | 78.0 | DOWNGRADE |

**Score: 9 Hit / 5 Miss = 64.3% alpha hit rate over the month.** Dispersion was wide — a +12.85pp alpha (AAPL) and a −11.41pp alpha (CAT) in the same 14-name book — which is itself the month's defining feature.

## 3. Theme-Level Performance

| Prior theme | Names | Outcome | Evidence |
|---|---|---|---|
| Mega-cap tech / platform | GOOGL, NVDA, AAPL, V | **Partial** | 3 of 4 positive alpha, but the dispersion is enormous: AAPL +12.85pp against GOOGL −8.18pp. Owning "mega-cap tech" as a bloc explained nothing this month. |
| Money-center financials | GS, BAC, JPM | **Validated (partial)** | BAC +6.71pp, JPM +5.15pp after both printed 2026-07-14; GS −2.23pp. Bank earnings were the month's cleanest positive catalyst. |
| Capital-goods industrials | CAT, GE | **Failed** | CAT −11.41pp, GE −4.10pp. 0 of 2. The worst theme in the book. |
| Healthcare | LLY, UNH | **Validated** | LLY +6.27pp, UNH +2.91pp. 2 of 2. |
| Energy / materials | CVX, FCX | **Validated** | CVX +12.84pp, FCX +0.45pp (marginal). 2 of 2, though FCX is barely distinguishable from the benchmark. |
| Data-center REIT | EQIX | **Failed** | −1.76pp. |

The signal is not "the baseline was wrong." It is that **the market re-rated by duration and rate sensitivity**, not by the sector or quality buckets the baseline was organised around: long-duration growth (GOOGL, GE, EQIX, CAT) de-rated while cash-generative defensives and energy (CVX, LLY, AAPL's buyback-heavy profile, banks' rate leverage) were rewarded.

## 4. Regime Shift Assessment

| Dimension | Baseline (2026-06-24) | Today (2026-07-24) | Ledger |
|---|---|---|---|
| Index level | SPY 733.24 | SPY 738.93 (+0.78%) | L001-series, L148 |
| SPY vs MAs | above | **below MA20 (746.15) and MA50 (745.07)**, alignment MIXED | `technical_indicators.json` |
| SPY MACD | — | daily `BELOW_SIGNAL`, weekly `BEARISH_CROSS` | `technical_indicators.json` |
| Semis | leading (SOXX RS20 vs SPY was **+19.6%** at the June vintages) | **SOXX RS20 −16.34%, −19.54% from its 60d high** | L001-series |
| Breadth | — | 54.5% above MA20, median 20d momentum +1.64%, 58.9% positive | L139 |
| Beta dispersion | — | **median 60d beta +0.232; 40.9% of names negative** | L140 |
| Vol | — | VIX 18.58 vs avg60 17.36; only 3.3% of the last 60 sessions closed above 20 | L137 |
| Rates | — | TLT −4.69% over 20d; 13-week bill 3.81% | L136, L138 |

**Assessment: a violent internal rotation inside a flat index, not a broad drawdown.** SPY is only 2.72% off its 60-day high with positive 60-day momentum and majority-positive breadth, while SOXX is down 19.5% from its high and QQQ 8.3%. The single most diagnostic number is L140: **40.9% of the universe now has a negative 60-day beta to SPY**, with a median of just +0.232. That can only happen when the index's own path is dominated by a narrow group moving against the average stock. Falling bonds (TLT −4.69%) point at rising long yields as the mechanism de-rating long-duration growth.

**Factor-weight implication:** this validates keeping the defensive polarity on the Macro/Regime family (lower beta, lower realized vol, shallower drawdown score better) for today's scoring, and it is disclosed as a regime-conditional choice in `05`, not a permanent rule change. No family weight was altered — that would require the evolution policy.

## 5. Carry-Forward Decisions

Binding on today's factor scoring where ledger-backed. Decisions follow today's recomputed percentile: `CARRY` ≥ 80th, `DOWNGRADE` 60–80th, `DROP` < 60th.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Alpha | Decision | Rationale |
|---|---|---|---|---|---|---|
| BAC | 82.4 | Money-center bank | +7.48% | +6.71pp | **CARRY** | Now 92.6th pctl on today's independent scoring. Printed 2026-07-14, so no earnings penalty. Published. |
| JPM | 70.6 | Money-center bank | +5.93% | +5.15pp | **CARRY** | 92.0th pctl today. Printed 2026-07-14. Published. |
| AAPL | 61.8 | Mega-cap platform | +13.63% | +12.85pp | **DOWNGRADE** | Best raw performer in the book, but only 78.0th pctl today and it reports 2026-07-30 (6 days) → penalised. Monitoring sleeve only. |
| UNH | 76.5 | Managed care | +3.68% | +2.91pp | **DOWNGRADE** | 77.8th pctl. Printed 2026-07-21. Monitoring sleeve. |
| LLY | 91.2 | Obesity/diabetes franchise | +7.05% | +6.27pp | **DOWNGRADE** | 75.6th pctl. Reports 2026-08-05 (12 days) → penalised. Monitoring sleeve. |
| V | 64.7 | Payments network | +7.08% | +6.30pp | **DROP** | 56.5th pctl — below the 60th-pctl ranking floor. Rejection log. |
| GE | 94.1 | Aerospace/power cycle | −3.32% | −4.10pp | **DROP** | 53.4th pctl. Thesis did not survive the month. |
| GS | 85.3 | Capital-markets recovery | −1.46% | −2.23pp | **DROP** | 45.8th pctl. |
| EQIX | 73.5 | Data-center REIT | −0.98% | −1.76pp | **DROP** | 36.3rd pctl. |
| CVX | 79.4 | Integrated energy | +13.61% | +12.84pp | **DROP** | 34.3rd pctl **despite** the best-but-one alpha — the move already happened and today's technicals rank it poorly. Dropping a winner on current evidence is the correct behaviour, not a bug. |
| NVDA | 67.6 | AI compute | +3.94% | +3.16pp | **DROP** | 31.6th pctl amid the semis unwind. |
| FCX | 88.2 | Copper cycle | +1.23% | +0.45pp | **DROP** | 18.1st pctl. |
| GOOGL | 97.1 | Search/cloud/AI | −7.40% | −8.18pp | **DROP** | 12.3rd pctl. Printed 2026-07-23 (−7.13%). |
| CAT | 100.0 | Capital-goods cycle | −10.63% | −11.41pp | **DROP** | 6.2nd pctl — the prior run's top-ranked name is now in the bottom decile. |

**2 CARRY, 3 DOWNGRADE, 9 DROP.** All 5 CARRY/DOWNGRADE names have grounded earnings dates and appear in today's published monitoring sleeve. `DROP` names stay out of today's scored set absent new ledger evidence; none was re-admitted.

The most instructive row is CAT: ranked #1 a month ago at adj score 100.0, now 482nd of 514. Combined with the rank IC of −0.0939, this is direct evidence that **the composite score's rank ordering is not yet predictive**, which is exactly why confidence is capped and why `13_evolution_log.md` treats calibration as the priority.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `DELAYED` (2026-07-24 close, 3-source verified) for current; `HISTORICAL` for baseline entries |
| Prices failing the sourcing standard | none |
| Reflection confidence | **HIGH** |
| Basis for confidence | Settlement state verified programmatically (`due_inventory 0`, `conflicts 0`); all 14 MoM current prices drawn from the same 3-source-verified bar set; alpha computed against the baseline's own recorded benchmark price (733.24), not a re-derived one |
| Structural issues found | (1) `Fund_Z`/`Sent_Z` still unavailable → `NO_TRADE` is structural, unchanged since 2026-07-15. (2) Rank IC negative → confidence capped. (3) **New:** the entire settled evidence base is one overlapping cohort with an effective independent N of 1 per type — raw `n` in the rolling metrics is misleading and has been inviting overfitted parameter changes. Escalated to `13_evolution_log.md`. |
