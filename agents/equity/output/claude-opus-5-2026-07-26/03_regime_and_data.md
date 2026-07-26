# 03 Regime and Data — 2026-07-26

Data-integrity and market-regime stage. Every fact below carries a `01_preflight.md` ledger row or is marked `UNAVAILABLE`.

## Data Mode Declaration

**`DELAYED`** — quotes fetched this run with ≤1-day lag from public endpoints; no live brokerage equity feed is wired.

The 2026-07-24 close is the most recent tape that exists: this run fires on **Sunday 2026-07-26** with no U.S. equity session since Friday. The basis is therefore one day *stale by the calendar* and zero days stale *by market activity*. `DELAYED_PARTIAL` does not apply — no Required input is missing (see `00 § GO-Gate Table`).

| Check | Result |
|---|---|
| Bars fetched this run | 518 symbols (514 union names + SPY/QQQ/SOXX/TLT), 185–1,255 daily bars each (L003) |
| Coverage of the eligible universe | 514 / 515 = **99.8%** (only FDXF excluded, L011) |
| Freshest bar | 2026-07-24 on **all 518** symbols — no straggler, no partial bar |
| Price verification | 17 settlement/ETF symbols at 3 sources, 0.0000% max difference (L001) |
| Lineage clarity for core fields | price ✅ volume ✅ beta ✅ earnings date ✅ — no `HALTED` trigger |
| Benchmark availability | SPY full history present — no `HALTED` trigger under Hard Halt #1 |

## Regime Classification

**Declared regime: `NEUTRAL`** (L139, `INFERRED` from the cited rows).

| Evidence | Value | Points toward | Ledger |
|---|---|---|---|
| SPY vs MA20 / MA50 | 738.93 vs **746.15 / 744.12** — below both | not `BULL` | L028, L135 |
| SPY MACD daily | `BELOW_SIGNAL` | not `BULL` | L135 |
| SPY RSI(14) daily | 45.5 — mid-range, neither extreme | `NEUTRAL` | L135 |
| SPY drawdown from 60d high | **−2.47%** | not `BEAR` | L018 |
| SPY 60d momentum | **+4.09%** | not `BEAR` | L025 |
| SPY 30d realized vol | 3.96% monthly, rising from 3.75% | not `HIGH_VOL` | L013, L014 |
| VIX | **18.58**; 30d avg 17.12 vs prior-30d 17.60 | not `HIGH_VOL` (VIX < 20 and 30d average *falling*) | L005, L006 |
| TLT | 83.25, −4.45% from 60d high, RSI 33.19, 60d momentum −2.52% | rates drifting up — **not a shock** | L029 |
| QQQ / SOXX | `BEARISH` MA alignment; −8.20% / **−19.54%** from 60d high | risk-off *within* the index, i.e. rotation | L018, L135 |
| Universe beta distribution | **212 of 514 names (41.2%) at negative 60d beta**, median +0.228 | dispersion consistent with rotation | L016, L142 |

**Why not each alternative:** `BULL` fails on price below both moving averages with MACD below signal. `BEAR` fails on a −2.47% index drawdown and +4.09% 60-day momentum. `HIGH_VOL` fails on VIX 18.58 with a *falling* 30-day average and 3.96% monthly realized vol. `RATE_SHOCK` fails because TLT's move is a −4.45% drift from its 60-day high, not a dislocation.

**The defensible label is `NEUTRAL`, and the substantive story is a rotation, not a direction.** The index is flat-to-slightly-soft while growth and semiconductors are in a real drawdown and defensives, financials and energy absorb the flow. This is corroborated out-of-sample by `02 § 0`: over exactly this window, financials and energy produced positive alpha and growth and industrials produced negative alpha.

**SPY prior mu under `NEUTRAL` = +0.5%** per `rules.md § Core ETF Market Forecast`.

## Core ETF Market Forecast Block

Per `rules.md § Core ETF Market Forecast`. Prices are 3-source verified (L001, L028); sigma is `REALIZED_VOL_30D` from the fetched adjusted bars (L013, L030); beta is the OLS slope of 60 daily returns vs SPY (L016). Target date is `run_date + 28d = 2026-08-23`.

| ETF | Entry | Price Date | Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 738.93 | 2026-07-24 | HISTORICAL | MA20 746.15 / MA50 744.12 (MIXED) | 3.96% (RISING) | 1.0000 | +0.500% | 3.96% | REALIZED_VOL_30D | 742.62 | 2026-08-23 | 712.21 | 773.04 | MEDIUM | L028,L029,L030,L135 |
| QQQ | 684.23 | 2026-07-24 | HISTORICAL | MA20 711.71 / MA50 717.87 (BEARISH) | 7.96% (RISING) | 1.7182 | -0.641% | 7.96% | REALIZED_VOL_30D | 679.84 | 2026-08-23 | 623.22 | 736.47 | MEDIUM | L028,L029,L030,L135 |
| SOXX | 527.01 | 2026-07-24 | HISTORICAL | MA20 565.45 / MA50 569.10 (BEARISH) | 20.19% (RISING) | 3.6395 | +0.320% | 20.19% | REALIZED_VOL_30D | 528.70 | 2026-08-23 | 418.03 | 639.36 | MEDIUM | L028,L029,L030,L135 |

**mu derivation (never free-handed):**

| ETF | Derivation | Result |
|---|---|---|
| SPY | Regime prior for `NEUTRAL` = +0.5%, applied **unadjusted**. The ±1.0pp band was available; no adjustment was made because the evidence is genuinely two-sided (below both MAs and MACD below signal, but only −2.47% off the high with +4.09% 60d momentum). | **+0.500%** |
| QQQ | `beta 1.7182 × +0.5% = +0.859%`, then the **full allowed −1.5pp** relative-view adjustment | **−0.641%** |
| SOXX | `beta 3.6395 × +0.5% = +1.820%`, then the **full allowed −1.5pp** relative-view adjustment | **+0.320%** |

**Ledger-backed basis for the −1.5pp relative view on both** (L018, L026, L135): `BEARISH` MA alignment on daily bars, MACD `BELOW_SIGNAL`, RS20 of −5.12pp (QQQ) and −16.34pp (SOXX) versus SPY, and drawdowns of −8.20% and −19.54% from their 60-day highs.

**Disclosed limitation — and why SOXX still carries a positive mu.** `rules.md` derives ETF mu as `beta × SPY_mu`. With a non-negative SPY prior, a beta of 3.64 forces SOXX's raw mu to +1.82%, and even the maximum permitted −1.5pp adjustment leaves it at **+0.320%** — a *positive* expected return on the most technically damaged of the three ETFs. This is precisely the category error diagnosed on 2026-07-24 (beta measures co-movement magnitude, not expected-return direction). Two candidate fixes were tested and rejected that day, and **no further Track A change is permissible at `eff_n = 1`** (`02 § 0`). The rule is therefore applied exactly as written and the consequence is disclosed rather than engineered around.

Because `|mu| = 0.320% < 0.5%`, SOXX's direction call settles as **`N/A - FLAT_CALL`** per `rules.md § Settlement Rules`; only CI calibration and magnitude error z will be scored on it. That is the honest outcome: the rule set cannot currently express the bearish SOXX view the evidence supports, so it abstains on direction rather than recording a view it does not hold.

**Counter-evidence, stated plainly:** on a 60-day view SOXX is still the strongest of the three (momentum +20.18%, RS60 +16.09pp vs SPY). The bearish read rests on the 20-day window. A monthly TD-9 `SELL_SETUP_9` on SOXX with monthly RSI 70.02 is a textbook exhaustion flag — it supports the bearish tilt but, per `rules.md § TD-9 Definition`, is not a standalone signal.

### Analysis Minimum (per ETF)

| Metric | SPY | QQQ | SOXX |
|---|---|---|---|
| Trend vs MA20 / MA50 | below / below (`MIXED`) | below / below (`BEARISH`) | below / below (`BEARISH`) |
| 30d realized vol (monthly) | 3.96% | 7.96% | 20.19% |
| vs prior 30d | 3.75% → **rising** | 6.40% → **rising** | 16.92% → **rising** |
| Drawdown from 60d high | −2.47% | −8.20% | −19.54% |
| RSI(14) d / w / m | 45.5 / 59.11 / 71.95 | 39.33 / 53.44 / 66.63 | 42.78 / 58.36 / 70.02 |
| MACD daily | `BELOW_SIGNAL` | `BELOW_SIGNAL` | `BELOW_SIGNAL` |
| TD-9 d / w / m | BUY_SETUP_7 / SELL_SETUP_1 / SELL_SETUP_4 | BUY_SETUP_8 / BUY_SETUP_2 / SELL_SETUP_4 | SELL_SETUP_3 / BUY_SETUP_3 / **SELL_SETUP_9** |
| 60d beta vs SPY | 1.0000 | 1.7182 | 3.6395 |

**Relative strength:** `QQQ/SPY` **−5.12pp** over 20d, **+0.08pp** over 60d. `SOXX/SPY` **−16.34pp** over 20d, **+16.09pp** over 60d. Both ratios have rolled over hard on the 20-day window while remaining flat-to-positive on 60 days — the signature of a recent, sharp reversal rather than a sustained downtrend.

**Regime-consistency check:** the ETF block is consistent with the declared `NEUTRAL` regime. Realized vol is rising on all three but from a low base, with VIX at 18.58 — this is rotation pressure inside a calm index, not a volatility regime change. Realized vol *falling* on TLT (2.57% vs 2.63%) argues the same way.

**Sleeve isolation:** SPY, QQQ and SOXX are a market-forecast sleeve only. They are not candidates, are not universe members, do not enter any percentile distribution, do not count toward the 5–10 investable set, and are exempt from the single-name universe filters.

## Universe Construction and Handoff

| Step | Result | Ledger |
|---|---|---|
| `build_index_universe.py` | **515 tickers** — 503 S&P 500, 101 Nasdaq-100, 89 overlap. Caches stamped `2026-06-21T21:05:56Z` | L009 |
| Cache staleness | 35 days old. Per `rules.md § Index-Union Universe Protocol` #5 the run uses them and logs `fetched_at`; refresh is maintenance, never grounds for the 30-name fallback | L009 |
| Price history fetched | 514 / 515 | L003 |
| Excluded | **FDXF** — 40 bars from 2026-05-28 (FedEx Freight spin-off); fails the >6-month listing-age filter. Eligible ~2026-11-28 | L011 |
| Admitted after review | **Q** (Qnity Electronics) — first bar 2025-10-28, 185 bars ≈ 8.9 months, clears the >6-month filter. Daily and weekly indicators are full; monthly MACD is thin and marked accordingly | L012 |
| Final scored universe | **514 names** | L010 |
| Percentile label | **`INDEX_UNION_PCTL (n=514)`** | L010 |

**Inclusion filters applied** (`rules.md § Universe Construction`): all 514 clear U.S. primary listing, price > $5, ADV20 > $20M (L019), and listing age > 6 months. No name was excluded on liquidity or price this run.

**Emergency Sampled Universe Protocol: NOT used.** The index-union helper succeeded.

**Handoff to `technical_indicators.py`:** the 514 scored names plus SPY, QQQ, SOXX, TLT — 518 symbols. Result: 518 records, all `status: OK`, all `as_of: 2026-07-24` (L135). Coverage detail in `04`.

## Event Concentration

| Flag | Status |
|---|---|
| Clustered earnings in the published set | **4 of 24** carry `CONFIRMED` earnings inside 14 days (GD 3d, MPC 9d, MET 10d, VLO 4d), plus **HIG** on the conservative `ESTIMATED_PRINT_WEEK` branch — 5 penalized names in total |
| `NO_TRADE` trigger #4 ("more than 2 names with earnings inside 14 days") | **TRIPPED** — 5 names. Independent of the family-coverage failure, this alone would block a `GO` on the published set as constructed |
| Peak earnings density | 2026-07-27 → 2026-08-06 across the wider top-40; U.S. Q2 reporting season is at its peak |
| FOMC inside the 2026-08-23 horizon | **`UNAVAILABLE`** — no FOMC calendar source is wired this run. Recorded as a gap, not asserted either way |
| Index-rebalance / expiry windows | **`UNAVAILABLE`** — not sourced |

## Recommendation to Orchestrator

**Data is sufficient for `GO`; the candidate evidence is not.**

- No `HALTED` condition: lineage is clear for every core field, the benchmark is present, and the index union materialized.
- Not `REVIEW_ONLY` on data-quality grounds: all five Required inputs are grounded on the most recent close in existence, verified three ways to the cent.
- Recommend the orchestrator carry the run forward to scoring and expect **`NO_TRADE`**, driven by evidence thresholds #2/#4 (`Fund_Z` / `Sent_Z` unavailable, L144/L145) and, independently, by portfolio infeasibility on the beta band (L141) and by earnings concentration (5 penalized names against a limit of 2).
