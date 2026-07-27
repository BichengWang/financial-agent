# 02 Reflection — 2026-07-27

Standalone month-over-month reflection. Completed **before** any scoring in this run. Every price,
return and regime claim cites `01_preflight.md` rows or is marked `UNAVAILABLE` / `INFERRED`.

## 0. Prediction Settlement

**This run settles nothing, by design.** `settlement_ledger.py --as-of 2026-07-27` (L044, L054):

```text
due_inventory: 0      conflicts: 0
canonical_equity_alpha_settlements: 231
canonical_market_forecast_settlements: 42
audit_only_rows: 145   rejected_rows: 87   total_candidate_rows: 505
```

`63` packages were scanned for `15_predictions.json` — every dated
folder under `agents/equity/output/`, all models. The concurrent `gpt-5-2026-07-27` pre-open run
fired roughly an hour before this one and settled all **34** keys that matured
today, so due inventory is genuinely `0`. `15_predictions.json` therefore carries
`"settlements": []` with a `NO_DUE_PREDICTIONS` note — the same situation the 2026-07-17 evening run
documented after a same-day pre-open run. **Those rows were re-validated by this run's ledger pass**
(timing is re-checked for every historical candidate, not only new ones) and all
34 remain timing-valid with 0 conflicts.

### Settlements that matured today (canonical, settled by `gpt-5-2026-07-27`)

Shown because they are this run's calibration evidence, not because this run produced them.

| Ticker | Vintage | Model | Entry | Target Date | mu | Realized | SPY Ret | Alpha | Direction | CI | z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-06-29 | gemini-3.5-flash | 283.78 | 2026-07-27 | +1.00% | +17.35% | +1.36% | +15.99% | HIT | OUT_CI_HIGH | +1.9559 |
| CVX | 2026-06-29 | gemini-3.5-flash | 171.06 | 2026-07-27 | +2.00% | +13.87% | +1.36% | +12.51% | HIT | OUT_CI_HIGH | +1.5663 |
| JPM | 2026-06-29 | gemini-3.5-flash | 329.05 | 2026-07-27 | +3.00% | +7.34% | +1.36% | +5.98% | HIT | IN_CI | +0.6275 |
| BAC | 2026-06-29 | gemini-3.5-flash | 57.88 | 2026-07-27 | +3.00% | +7.20% | +1.36% | +5.84% | HIT | IN_CI | +0.8117 |
| V | 2026-06-29 | gemini-3.5-flash | 336.23 | 2026-07-27 | +1.00% | +5.80% | +1.36% | +4.44% | HIT | IN_CI | +0.8530 |
| GS | 2026-06-29 | gemini-3.5-flash | 1019.61 | 2026-07-27 | +1.00% | +4.08% | +1.36% | +2.72% | HIT | IN_CI | +0.2817 |
| FCX | 2026-06-29 | gemini-3.5-flash | 62.45 | 2026-07-27 | +1.00% | +0.24% | +1.36% | -1.12% | MISS | IN_CI | -0.0457 |
| EQIX | 2026-06-29 | gemini-3.5-flash | 1091.3 | 2026-07-27 | +2.00% | -0.65% | +1.36% | -2.01% | MISS | IN_CI | -0.4611 |
| LLY | 2026-06-29 | gemini-3.5-flash | 1208.12 | 2026-07-27 | +6.00% | -1.00% | +1.36% | -2.36% | MISS | IN_CI | -0.7093 |
| UNH | 2026-06-29 | gemini-3.5-flash | 427.89 | 2026-07-27 | +5.00% | -1.67% | +1.36% | -3.03% | MISS | IN_CI | -0.8895 |
| GE | 2026-06-29 | gemini-3.5-flash | 369.0 | 2026-07-27 | +4.00% | -4.14% | +1.36% | -5.50% | MISS | IN_CI | -0.8304 |
| GOOGL | 2026-06-29 | gemini-3.5-flash | 337.39 | 2026-07-27 | +5.00% | -5.23% | +1.36% | -6.59% | MISS | OUT_CI_LOW | -1.2585 |
| SHW | 2026-06-29 | gemini-3.5-flash | 344.07 | 2026-07-27 | +2.00% | -7.72% | +1.36% | -9.08% | MISS | OUT_CI_LOW | -1.1007 |
| CAT | 2026-06-29 | gemini-3.5-flash | 997.47 | 2026-07-27 | +6.00% | -10.90% | +1.36% | -12.27% | MISS | OUT_CI_LOW | -1.1903 |
| AAPL | 2026-06-29 | gpt-5 | 283.78 | 2026-07-27 | +1.00% | +17.35% | +1.36% | +15.99% | HIT | OUT_CI_HIGH | +1.9559 |
| CVX | 2026-06-29 | gpt-5 | 171.06 | 2026-07-27 | +2.00% | +13.87% | +1.36% | +12.51% | HIT | OUT_CI_HIGH | +1.5663 |
| JPM | 2026-06-29 | gpt-5 | 329.05 | 2026-07-27 | +3.00% | +7.34% | +1.36% | +5.98% | HIT | IN_CI | +0.6275 |
| BAC | 2026-06-29 | gpt-5 | 57.88 | 2026-07-27 | +3.00% | +7.20% | +1.36% | +5.84% | HIT | IN_CI | +0.8117 |
| V | 2026-06-29 | gpt-5 | 336.23 | 2026-07-27 | +1.00% | +5.80% | +1.36% | +4.44% | HIT | IN_CI | +0.8530 |
| GS | 2026-06-29 | gpt-5 | 1019.61 | 2026-07-27 | +1.00% | +4.08% | +1.36% | +2.72% | HIT | IN_CI | +0.2817 |
| FCX | 2026-06-29 | gpt-5 | 62.45 | 2026-07-27 | +1.00% | +0.24% | +1.36% | -1.12% | MISS | IN_CI | -0.0457 |
| EQIX | 2026-06-29 | gpt-5 | 1091.3 | 2026-07-27 | +2.00% | -0.65% | +1.36% | -2.01% | MISS | IN_CI | -0.4611 |
| LLY | 2026-06-29 | gpt-5 | 1208.12 | 2026-07-27 | +6.00% | -1.00% | +1.36% | -2.36% | MISS | IN_CI | -0.7093 |
| UNH | 2026-06-29 | gpt-5 | 427.89 | 2026-07-27 | +5.00% | -1.67% | +1.36% | -3.03% | MISS | IN_CI | -0.8895 |
| GE | 2026-06-29 | gpt-5 | 369.0 | 2026-07-27 | +4.00% | -4.14% | +1.36% | -5.50% | MISS | IN_CI | -0.8304 |
| GOOGL | 2026-06-29 | gpt-5 | 337.39 | 2026-07-27 | +5.00% | -5.23% | +1.36% | -6.59% | MISS | OUT_CI_LOW | -1.2585 |
| SHW | 2026-06-29 | gpt-5 | 344.07 | 2026-07-27 | +2.00% | -7.72% | +1.36% | -9.08% | MISS | OUT_CI_LOW | -1.1007 |
| CAT | 2026-06-29 | gpt-5 | 997.47 | 2026-07-27 | +6.00% | -10.90% | +1.36% | -12.27% | MISS | OUT_CI_LOW | -1.1903 |
| QQQ | 2026-06-29 | gemini-3.5-flash | 706.52 | 2026-07-27 | +1.87% | -3.15% | N/A | N/A | MISS | IN_CI | -0.6289 |
| SOXX | 2026-06-29 | gemini-3.5-flash | 589.94 | 2026-07-27 | +4.01% | -10.67% | N/A | N/A | MISS | IN_CI | -0.7139 |
| SPY | 2026-06-29 | gemini-3.5-flash | 728.99 | 2026-07-27 | +1.00% | +1.36% | N/A | N/A | HIT | IN_CI | +0.0838 |
| QQQ | 2026-06-29 | gpt-5 | 706.52 | 2026-07-27 | +1.87% | -3.15% | N/A | N/A | MISS | IN_CI | -0.6289 |
| SOXX | 2026-06-29 | gpt-5 | 589.94 | 2026-07-27 | +4.01% | -10.67% | N/A | N/A | MISS | IN_CI | -0.7139 |
| SPY | 2026-06-29 | gpt-5 | 728.99 | 2026-07-27 | +1.00% | +1.36% | N/A | N/A | HIT | IN_CI | +0.0838 |

### Rolling Calibration Metrics

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy | Verdict |
|---|---:|---:|---|---|
| Raw `n` | 231 | 42 | ≥ 20 for Track A | satisfied |
| 28-day `eff_n` | **1** | **1** | ≥ 3 for Track A | **fails** |
| Hit rate | 51.08% | 23.81% | > 50% | EQ marginal; MF broken |
| CI coverage | 74.03% | 71.43% | 55–85% | both healthy |
| Mean z | -0.1792 | -0.6640 | −0.5 to +0.5 | EQ healthy; MF outside |
| Track A proposals | `INSUFFICIENT_EFFECTIVE_N` | `INSUFFICIENT_EFFECTIVE_N` | — | `DEFER` only |

Weighted-mean rank IC **-0.1843**:

| Vintage | n | Rank IC |
|---|---:|---:|
| `claude-fable-5:2026-06-10` | 12 | -0.5105 |
| `gemini-3.5-flash:2026-06-21` | 14 | -0.1341 |
| `gemini-3.5-flash:2026-06-29` | 14 | -0.5912 |
| `gpt-5:2026-06-11` | 17 | +0.3480 |
| `gpt-5:2026-06-14` | 17 | +0.5628 |
| `gpt-5:2026-06-15` | 17 | -0.0833 |
| `gpt-5:2026-06-16` | 14 | -0.0462 |
| `gpt-5:2026-06-17` | 14 | -0.2484 |
| `gpt-5:2026-06-18` | 14 | -0.2835 |
| `gpt-5:2026-06-19` | 14 | -0.0637 |
| `gpt-5:2026-06-20` | 14 | -0.1341 |
| `gpt-5:2026-06-21` | 14 | -0.1341 |
| `gpt-5:2026-06-22` | 14 | -0.1341 |
| `gpt-5:2026-06-24` | 14 | -0.6571 |
| `gpt-5:2026-06-28` | 14 | -0.5912 |
| `gpt-5:2026-06-29` | 14 | -0.5912 |

**Three findings, deliberately kept separate.**

1. **Magnitude calibration is healthy.** CI coverage 74.03% sits inside the
   55–85% band and mean z -0.1792 inside ±0.5. No sigma-widening or mu-shrink trigger
   fires, and the `rules.md` interpretation rule for coverage < 55% does not apply.
2. **Rank ordering is inverted.** Weighted-mean rank IC is -0.1843 over
   231 pairs, and the 2026-06-29 vintages that settled today came in
   at -0.5912. Because rank IC ≤ 0 over ≥ 20 settled predictions,
   `agents.md § Calibration Feedback Binding` fires: **all confidence is capped at `MEDIUM`** in this
   run, and no `HIGH` appears anywhere. A mu shrink or sigma widen is a monotonic transform and
   cannot repair an ordering inversion — that standing proposal stays retired.
3. **`eff_n = 1` still gates every Track A change.** 231 `EQUITY_ALPHA` settlements collapse
   into a single non-overlapping 28-day window. Adding 34 settlements today moved
   raw `n` but left `eff_n` at 1, exactly as the 2026-07-26 package predicted. Raw `n ≥ 20` is
   numerically satisfied and statistically vacuous.

The `MARKET_FORECAST` line is reported separately and never pooled with the equity metrics, per
`rules.md`. Its 23.81% hit rate over n=42 remains the worst number in the
system and its diagnosed cause — `mu_ETF = beta × SPY_mu` treating a co-movement magnitude as a
return direction — is unchanged and still `DEFER`red at `eff_n = 1`.

## 1. Prior Run Summary — baseline `gpt-5-2026-06-29`

| Field | Value |
|---|---|
| Baseline folder | `agents/equity/output/gpt-5-2026-06-29` (L045) |
| Flag | `CROSS_MODEL_BASELINE` |
| Baseline date | 2026-06-29, exactly 28 days before this run |
| Records | 14 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` |
| Entry basis | 2026-06-26 close (the baseline run's last completed session) |
| Settled | today, at the 2026-07-24 close, `TARGET_EQ_RUN_DATE` |
| Direction outcome | 6 HIT / 8 MISS = 42.86% |
| CI outcome | 9 IN_CI of 14 = 64.29% |
| Vintage rank IC | -0.5912 |

Names: AAPL, CVX, JPM, BAC, V, GS, FCX, EQIX, LLY, UNH, GE, GOOGL, SHW, CAT.

## 2. MoM Price & Return Table

Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`. Prior price = the baseline's
`entry_price` (its 2026-06-26 close); current price = the 2026-07-24 close (L002). SPY moved from
728.99 to 738.93, +1.36%.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-06-26 | 283.78 | 2026-07-24 | 333.02 | +17.35% | +1.36% | +15.99% | **HIT** | OUT_CI_HIGH, z +1.9559 |
| CVX | 2026-06-26 | 171.06 | 2026-07-24 | 194.79 | +13.87% | +1.36% | +12.51% | **HIT** | OUT_CI_HIGH, z +1.5663 |
| JPM | 2026-06-26 | 329.05 | 2026-07-24 | 353.21 | +7.34% | +1.36% | +5.98% | **HIT** | IN_CI, z +0.6275 |
| BAC | 2026-06-26 | 57.88 | 2026-07-24 | 62.05 | +7.20% | +1.36% | +5.84% | **HIT** | IN_CI, z +0.8117 |
| V | 2026-06-26 | 336.23 | 2026-07-24 | 355.74 | +5.80% | +1.36% | +4.44% | **HIT** | IN_CI, z +0.8530 |
| GS | 2026-06-26 | 1019.61 | 2026-07-24 | 1061.23 | +4.08% | +1.36% | +2.72% | **HIT** | IN_CI, z +0.2817 |
| FCX | 2026-06-26 | 62.45 | 2026-07-24 | 62.6 | +0.24% | +1.36% | -1.12% | **MISS** | IN_CI, z -0.0457 |
| EQIX | 2026-06-26 | 1091.3 | 2026-07-24 | 1084.24 | -0.65% | +1.36% | -2.01% | **MISS** | IN_CI, z -0.4611 |
| LLY | 2026-06-26 | 1208.12 | 2026-07-24 | 1196.03 | -1.00% | +1.36% | -2.36% | **MISS** | IN_CI, z -0.7093 |
| UNH | 2026-06-26 | 427.89 | 2026-07-24 | 420.74 | -1.67% | +1.36% | -3.03% | **MISS** | IN_CI, z -0.8895 |
| GE | 2026-06-26 | 369.0 | 2026-07-24 | 353.73 | -4.14% | +1.36% | -5.50% | **MISS** | IN_CI, z -0.8304 |
| GOOGL | 2026-06-26 | 337.39 | 2026-07-24 | 319.74 | -5.23% | +1.36% | -6.59% | **MISS** | OUT_CI_LOW, z -1.2585 |
| SHW | 2026-06-26 | 344.07 | 2026-07-24 | 317.51 | -7.72% | +1.36% | -9.08% | **MISS** | OUT_CI_LOW, z -1.1007 |
| CAT | 2026-06-26 | 997.47 | 2026-07-24 | 888.73 | -10.90% | +1.36% | -12.27% | **MISS** | OUT_CI_LOW, z -1.1903 |

### Core ETF forecasts from the same baseline

| ETF | Entry | Target Date | mu | Realized | Direction | CI | z |
|---|---|---|---|---|---|---|---|
| QQQ | 706.52 | 2026-07-27 | +1.87% | -3.15% | MISS | IN_CI | -0.6289 |
| SOXX | 589.94 | 2026-07-27 | +4.01% | -10.67% | MISS | IN_CI | -0.7139 |
| SPY | 728.99 | 2026-07-27 | +1.00% | +1.36% | HIT | IN_CI | +0.0838 |

## 3. Theme-Level Performance

| Prior theme | Per-name alpha vs SPY | Positive | Verdict |
|---|---|---:|---|
| Mega-cap tech / platforms | AAPL +15.99%, V +4.44%, GOOGL -6.59% | 2/3 | **partial** |
| Financials | JPM +5.98%, BAC +5.84%, GS +2.72% | 3/3 | **validated** |
| Industrial / materials cyclicals | FCX -1.12%, GE -5.50%, SHW -9.08%, CAT -12.27% | 0/4 | **failed** |
| Healthcare | LLY -2.36%, UNH -3.03% | 0/2 | **failed** |
| Data-centre REIT | EQIX -2.01% | 0/1 | **failed** |
| Energy | CVX +12.51% | 1/1 | **validated** |


The signal in this cohort is not the average outcome but its **ordering**: the baseline's
highest-`adj_score` names were among its worst alpha performers, which is what drives the
-0.5912 vintage rank IC.

## 4. Regime Shift Assessment

| | Baseline 2026-06-29 | This run 2026-07-27 | Implication |
|---|---|---|---|
| Declared regime | `NEUTRAL` (SPY prior mu +1.87%) | `NEUTRAL` (SPY prior mu +0.50%) | unchanged |
| SPY level | 728.99 | 738.93 | +1.36% over 28d |
| SPY vs MA20/MA50 | — | 738.93 vs 746.153 / 744.1202 → `MIXED` | no trend |
| SPY 30d RVol | — | 3.96% (RISING) | contained |
| SOXX from 60d high | — | -19.54% | risk appetite narrowing |
| Negative-beta share | — | 41.25% of 514 names | defensive rotation |

The regime label is unchanged, but the *internals* moved: a 41.25%
negative-beta share and a -19.54% SOXX drawdown describe a market
rotating into defensives rather than one trending. That is the ledger-backed basis for the
`Macro_Z` polarity disclosed in L053, and it is also why the portfolio beta band is unreachable
(`07`).

## 5. Carry-Forward Decisions

Binding on this run's factor scoring where ledger-backed. Decisions are computed from this run's own
re-ranking of each baseline name, not asserted.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| AAPL | None | gpt-5-2026-06-29 ranked long | +17.35% | **DOWNGRADE** | still ranked (pctl 76.02, rank 124) but outside the published set |
| CVX | None | gpt-5-2026-06-29 ranked long | +13.87% | **DROP** | falls to pctl 55.75 (rank 228 of 514) — below the 60th-pctl ranking floor |
| JPM | None | gpt-5-2026-06-29 ranked long | +7.34% | **DOWNGRADE** | still ranked (pctl 91.62, rank 44) but outside the published set |
| BAC | None | gpt-5-2026-06-29 ranked long | +7.20% | **DOWNGRADE** | still ranked (pctl 92.20, rank 41) but outside the published set |
| V | None | gpt-5-2026-06-29 ranked long | +5.80% | **DOWNGRADE** | still ranked (pctl 87.72, rank 64) but outside the published set |
| GS | None | gpt-5-2026-06-29 ranked long | +4.08% | **DROP** | falls to pctl 45.61 (rank 280 of 514) — below the 60th-pctl ranking floor |
| FCX | None | gpt-5-2026-06-29 ranked long | +0.24% | **DROP** | falls to pctl 17.93 (rank 422 of 514) — below the 60th-pctl ranking floor |
| EQIX | None | gpt-5-2026-06-29 ranked long | -0.65% | **DROP** | falls to pctl 56.53 (rank 224 of 514) — below the 60th-pctl ranking floor |
| LLY | None | gpt-5-2026-06-29 ranked long | -1.00% | **DOWNGRADE** | still ranked (pctl 74.27, rank 133) but outside the published set |
| UNH | None | gpt-5-2026-06-29 ranked long | -1.67% | **DOWNGRADE** | still ranked (pctl 74.66, rank 131) but outside the published set |
| GE | None | gpt-5-2026-06-29 ranked long | -4.14% | **DROP** | falls to pctl 52.24 (rank 246 of 514) — below the 60th-pctl ranking floor |
| GOOGL | None | gpt-5-2026-06-29 ranked long | -5.23% | **DROP** | falls to pctl 11.89 (rank 453 of 514) — below the 60th-pctl ranking floor |
| SHW | None | gpt-5-2026-06-29 ranked long | -7.72% | **DROP** | falls to pctl 31.58 (rank 352 of 514) — below the 60th-pctl ranking floor |
| CAT | None | gpt-5-2026-06-29 ranked long | -10.90% | **DROP** | falls to pctl 9.55 (rank 465 of 514) — below the 60th-pctl ranking floor |

8 of 14
baseline names fall below the 60th-percentile ranking floor on today's evidence and are `DROP`ped;
they are absent from this run's published set. No `DROP` name was re-admitted.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness of every price used | `HISTORICAL` (2026-07-24 close, L002/L003), independently verified (L004) and brokerage-confirmed for the ETFs (L005–L007) |
| Live tape | `LIVE` but observation-only (L050, L051) — not used in any forecast or settlement |
| Reflection confidence | **MEDIUM** |
| Rationale | Settlement inputs are fully grounded and the baseline is an exact 28-day target hit with field-identical cross-model duplicates, which is as clean as this system's MoM comparison gets. Capped at MEDIUM rather than HIGH because `eff_n = 1` means the 231-observation base is one overlapping cohort, and because two of four factor families are `UNAVAILABLE` on both sides of the comparison. |
| Structural issues found | (1) rank-order inversion persists and is not addressable by any monotonic mu/sigma transform; (2) `eff_n` remains 1 despite 34 new settlements; (3) a transient earnings-fetch failure can silently publish a name penalty-free — found in this run, evidence and fix in `13`. |
