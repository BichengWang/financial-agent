# 03 — Regime and Data — 2026-08-28

## Data-mode declaration

**`DELAYED`** per `rules.md § Data Mode Taxonomy` — quotes fetched this run with ≤ 1-day lag
and **all five Required inputs grounded** (`01 § Preflight status`). This run is **not** in
`ILLUSTRATIVE_MODE`; the declared `data_mode` field is `DELAYED` and zero ledger rows carry
`ILLUSTRATIVE_REF`.

Fire window **2026-08-28T22:08:00-04:00** — a Friday post-close run whose price basis is the **same-day
2026-08-28 close**, final at all three vendors.

## Regime classification — `BULL`

| Evidence | Value | Reads as | Ledger |
|---|---|---|---|
| SPY close vs MA20 / MA50 | 769.35 vs 769.22 / 753.96 | above both — `BULLISH` daily **and** weekly MA alignment | L004, L013 |
| SPY 20d / 60d momentum | +2.99% / +2.26% | positive on both horizons | L013 |
| SPY RSI(14) daily | 56.66 | neutral (30–70), no exhaustion | L013 |
| SPY drawdown from 60d high | -1.10% | shallow — no distribution | L004 |
| SPY realized vol 30d (annualized) | 11.70% vs prior 30d 15.58% | **FALLING** — excludes `HIGH_VOL` | L004 |
| VIX close | 14.43 (prior 14.51) | low and easing — excludes `HIGH_VOL` | L007, L007a, L007b |
| 13-week T-bill | 3.74% | stable; no rate shock in the tape | L008 |
| TLT trend | MA alignment MIXED, 60d momentum -2.10% | long rates drifting, not shocking — excludes `RATE_SHOCK` | L013 |

`BULL` is the defensible label: trend up on two horizons, volatility falling on both the realized and
implied measures, and no rate dislocation. `HIGH_VOL`, `RATE_SHOCK` and `BEAR` are each excluded by a
cited row above; `NEUTRAL` is rejected because both momentum horizons and both MA alignments are
positive. **SPY prior mu = +2.0%** per `rules.md § Core ETF Market Forecast`.

## Event concentration

| Flag | Reading | Effect |
|---|---|---|
| Names printing inside 14 calendar days | **15** of 510 scored names | −0.10 adjusted-score penalty and `LOW` confidence cap on those names (L022) |
| Names printing anywhere in the swept window | **27** of 510 through 2026-10-04 | late-August earnings trough; sweep is complete so absence is positive evidence |
| Published names carrying an earnings penalty | **0** | `NO_TRADE` trigger #4 (>2 names with earnings inside 14d) does **not** fire |
| FOMC inside the 28-day horizon | `UNAVAILABLE` — no calendar feed wired this run | disclosed as a coverage gap; does not block `GO` (Enhancing) |

## Core ETF Market Forecast Block

`mu` derivation is fixed **before** looking at any values, per the 2026-08-22 precedent, so the ±1.5pp
band is applied by rule rather than by hand:

> **both RS20 and RS60 negative -> -1.5pp; only RS60 negative -> -1.0pp; neither -> 0.0pp**

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 769.35 | 2026-08-28 | `DELAYED` | ABOVE MA20 / ABOVE MA50 (BULLISH) | 3.38% (FALLING) | +1.0000 | +2.00% | 3.38% | `REALIZED_VOL_30D` | 784.74 | 2026-09-25 | 757.72 | 811.75 | MEDIUM | L800, L224 n/a, L004, L013 |
| QQQ | 716.43 | 2026-08-28 | `DELAYED` | BELOW MA20 / ABOVE MA50 (MIXED) | 5.98% (FALLING) | +1.7389 | +2.48% | 5.98% | `REALIZED_VOL_30D` | 734.18 | 2026-09-25 | 689.66 | 778.70 | MEDIUM | L801, L224 n/a, L004, L013 |
| SOXX | 508.62 | 2026-08-28 | `DELAYED` | BELOW MA20 / BELOW MA50 (BEARISH) | 14.57% (FALLING) | +3.4320 | +5.36% | 14.57% | `REALIZED_VOL_30D` | 535.90 | 2026-09-25 | 458.85 | 612.95 | MEDIUM | L802, L224 n/a, L004, L013 |

mu derivations, stated in full:

| ETF | Derivation |
|---|---|
| SPY | regime prior BULL = +2.0%; adjustment 0.0pp |
| QQQ | beta 1.7389 x SPY mu +2.00% = +3.4778%; RS adj -1.0pp -> +2.4778% |
| SOXX | beta 3.4320 x SPY mu +2.00% = +6.8639%; RS adj -1.5pp -> +5.3639% |

**Relative strength** (`technical_indicators.py` daily block, L013, L800–L802):

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | +1.14% | -5.89% |
| SOXX / SPY | -2.25% | -19.61% |

**Regime-consistency check.** A `BULL` regime with QQQ leading SPY over 20d (+1.14%)
but trailing over 60d (-5.89%), and SOXX trailing on both horizons while
sitting 22.35% below its 60-day high with `BEARISH` MA alignment, is a
**broadening** bull rather than a growth-led one. That is internally consistent: the index is making
new ground while its highest-beta sleeve repairs a drawdown.

**Disclosed defect in this block.** `mu_SOXX = beta x SPY_mu` yields **+5.36%** for a
fund with `BEARISH` daily MA alignment, negative relative strength on both horizons and a
22.35% drawdown, because a beta of 3.43 multiplies any
non-negative SPY prior beyond what the ±1.5pp band can offset. This is the **known category error
diagnosed on 2026-07-24** — beta measures co-movement magnitude, not expected-return direction. The
fix lives in the Core ETF mu prior table, which `rules.md § Evolution Policy` classifies as **Track A**;
with `MARKET_FORECAST` `eff_n` = 2 the Track A gate
is unmet, so the finding is **`DEFER`red, not rejected** (see `13`). The forecast is published as the
rule dictates rather than hand-corrected, because free-handing it would be a calibration violation.

## Universe handoff

515 index-union tickers plus core ETFs `SPY`, `QQQ`, `SOXX` (and `TLT` as the
rate-sensitivity reference) were handed to `technical_indicators.py`; **510** names survived
the inclusion/exclusion filters. Full construction and rejection log: `04`.

## Stop-criteria check at this stage

| Criterion | Result | Evidence |
|---|---|---|
| Hard halt 1 — benchmark data missing outside illustrative mode | **PASS** | SPY 5y daily history fetched, 2026-08-28 close 769.35 grounded on 3 sources (L004, L012, L017) |
| Hard halt 2 — unclear lineage on core fields | **PASS** | every price, volume, beta and earnings date in the published set has an `01` row; 0.0000% max cross-vendor deviation |
| Hard halt 3 — >20% of top candidates with unresolved critical inputs | **PASS** | 0 of 24 published names carry an unresolved Required input |
| Hard halt 4 — index universe cannot be materialized | **PASS** | `build_index_universe.py` produced 515 tickers (L001) |
| Hard halt 5 — limits unreachable for process/data reasons | **N/A** | no portfolio drafted; the blocker is set composition, which routes to `NO_TRADE` #1, not `HALTED` |
| Hard halt 6 — fabricated or contradictory evidence | **PASS** | see `08`; verification pass reported in `09` |

Recommendation to the orchestrator: **proceed to scoring**, data mode `DELAYED`, regime `BULL`.

