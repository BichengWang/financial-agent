# 03 — Regime and Data · 2026-08-27

## Data-mode declaration

**Data mode: `DELAYED`.** Quotes were fetched this run at zero lag to the completed
2026-08-27 regular session (post-close fire, 19:09 ET). Every one of the five **Required** inputs in
`rules.md § Input Classification` is grounded (`01` GO-Gate Table), so this is not
`DELAYED_PARTIAL`; the run is not in `ILLUSTRATIVE_MODE` and no table in this package carries the
illustrative banner.

Fetch summary (L002): **518/519** symbols at 5Y depth in **10.7s**
at 8 workers; **515** last bars equal the basis date. Ex-dividend
`c != a` on the basis bar: **7** names
(BAX, EBAY, HII, LH, NEE, TAP, TMUS) — resolved to the unadjusted close for entry/target/CI
and to the adjusted series for all return and indicator math, per the Track B rule of 2026-07-26.

## Regime Classification

**Regime: `BULL`.**

| Evidence | Value | Ledger row | Reading |
|---|---|---|---|
| SPY close vs MA20 / MA50 | 771.10 vs 768.10 / 753.35 | L003, L013 | above both — trend intact |
| SPY 20d / 60d momentum | +3.97% / +1.78% | L013 | positive on both horizons |
| SPY 30d realized vol (1m) | 3.49% (FALLING vs prior 30d 4.46%) | L003b, L003c | compressing |
| SPY drawdown from 60d high | -4.49% | L003d | shallow |
| VIX | 14.51 (T-1 15.21) | L007, L007a | well below the 20 stress threshold |
| Universe breadth: names with positive 60d momentum | 66.60% of 509 | L013 | two thirds of the index union is advancing |
| Universe breadth: daily MA alignment BULLISH | 37.33% | L013 | narrower than the momentum reading — leadership is concentrated |

The classification rule applied, fixed before the values were read: `HIGH_VOL` if VIX >= 25;
otherwise `BULL` if SPY is above both MA20 and MA50 with positive 60d momentum and VIX < 20;
otherwise `BEAR` if SPY is below MA50 with negative 60d momentum; otherwise `NEUTRAL`.
`BULL` follows from the first two clauses.

Consistency note: the tape is trending with compressing volatility, but leadership is narrow —
37.33% daily-MA-bullish against 66.60%
positive 60d momentum — and **42.83%** of scored names carry a *negative*
60-day beta to SPY. A `BULL` label with that much negative-beta mass is a rotation, and it is the
direct cause of the portfolio infeasibility in `07`.

## Core ETF Market Forecast Block

Analysis minimum per `rules.md § Core ETF Market Forecast`, all ledger-backed.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d MA) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 771.10 | 2026-08-27 | `DELAYED` | 768.10 / 753.35 (above both) | 3.49% (FALLING vs 4.46%) | 1.0000 | +2.0000% | 3.49% | `REALIZED_VOL_30D` | 786.52 | 2026-09-24 | 758.55 | 814.49 | `MEDIUM` | L003, L003a/b/c/d/e, L013 |
| QQQ | 721.11 | 2026-08-27 | `DELAYED` | 716.52 / 712.15 (above both) | 6.09% (FALLING vs 8.65%) | 1.7209 | +2.4418% | 6.09% | `REALIZED_VOL_30D` | 738.72 | 2026-09-24 | 693.04 | 784.40 | `MEDIUM` | L004, L004a/b/c/d/e, L013 |
| SOXX | 525.43 | 2026-08-27 | `DELAYED` | 529.31 / 551.94 (mixed) | 14.38% (FALLING vs 21.73%) | 3.3478 | +5.6956% | 14.38% | `REALIZED_VOL_30D` | 555.36 | 2026-09-24 | 476.75 | 633.96 | `MEDIUM` | L005, L005a/b/c/d/e, L013 |

### Relative strength and mu derivation

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | +1.52% | -5.03% |
| SOXX / SPY | +0.17% | -14.89% |

`mu` is never free-handed. `SPY` takes the regime prior for `BULL`
(**+2.0%**) with **no** ±1.0pp adjustment applied. `QQQ` and `SOXX` take
`beta_to_SPY x SPY mu` and then a relative-view adjustment inside the ±1.5pp band. Following the
2026-08-22 rule that the mapping must be **stated before the values are looked at**, the mapping used
this run is:

- both `RS20` and `RS60` negative -> **-1.5pp**
- only `RS60` negative -> **-1.0pp**
- both positive -> **+1.0pp**
- otherwise -> **0.0pp**

| ETF | beta | beta x SPY mu | RS20 | RS60 | Mapping branch | Adjustment | Final mu |
|---|---|---|---|---|---|---|---|
| SPY | 1.0000 | +2.00% | +0.00% | +0.00% | regime prior (no beta step) | +0.0pp | +2.00% |
| QQQ | 1.7209 | +3.4418% | +1.52% | -5.03% | only RS60 negative | -1.0pp | +2.4418% |
| SOXX | 3.3478 | +6.6956% | +0.17% | -14.89% | only RS60 negative | -1.0pp | +5.6956% |

Known limitation, restated rather than quietly carried: `mu_ETF = beta x SPY_mu` is a category error
diagnosed on 2026-07-24 — beta measures co-movement magnitude, not expected-return direction, so a
high-beta ETF cannot express a bearish view against a non-negative SPY prior. Two Track A fixes were
tested and rejected then. The rule remains in force because changing it is Track A work and
`eff_n = 2` < 3. Settled `MARKET_FORECAST` calibration is reported separately in `02 § 0`
(CI coverage 90.55%,
which is *above* the 85% "uninformatively wide" line — also a deferred Track A finding).

Confidence is `MEDIUM` for all three: `HIGH` requires trend, vol and relative strength all aligned
with the regime call **and** data quality >= 0.90, and this run's data-quality multiplier is
0.80.

The three ETFs are a market-forecast sleeve. They are not candidates, not universe members, and do
not enter percentiles or portfolio caps.

## Event concentration

The forward earnings sweep (L010) covers **27 business days**,
2026-08-27 … 2026-10-02, with **27** fetched and zero transport failures — a
**complete** sweep, so absence is positive evidence.

- Names with a confirmed print inside the 14-day penalty window: **22** of 509 scored.
- Names with a confirmed print anywhere in the 37-day window: **35**.
- Names reading `NO_PRINT_IN_WINDOW`: **474**.

Late August remains a genuine earnings trough between quarterly seasons — a marked contrast with the
153-of-512 penalty count on 2026-08-03 at the peak of Q2 season, and slightly lighter than the
29-of-509 recorded on 2026-08-22. **0 names in the published 24
carry an earnings penalty**, so the `rules.md § Downgrade to NO_TRADE` #4 trigger (more than 2
published names printing inside 14 days) is not met.

FOMC: **`UNAVAILABLE`** — no FOMC calendar source is wired and none was fetched this run. That is
recorded as an absence of evidence, not as an assertion that no meeting falls inside the horizon.

## Universe handoff

The exact ticker list handed to `technical_indicators.py` was the 515-name index
union minus the one symbol with no fetched history (`EQR`), plus the four ETFs `SPY QQQ SOXX TLT` —
518 symbols. Filters and the full rejection log are in `04`.

## Stop-rule assessment

| Stop rule | Fires? | Basis |
|---|---|---|
| Hard halt 1 — benchmark data missing outside ILLUSTRATIVE_MODE | No | SPY history and close both grounded (L003) |
| Hard halt 2 — unclear lineage on core fields | No | 27/27 published prices grounded on 3 sources; every scored metric carries a ledger row |
| Hard halt 3 — >20% of top-ranked names missing critical inputs | No | 0 of 24 published names has an ungrounded Required input |
| Hard halt 4 — index union cannot be materialized | No | build_index_universe.py produced 515 tickers |
| Hard halt 5 — caps unreachable for process/data reasons | No | the beta band is unreachable for **composition** reasons, which routes to NO_TRADE #6, not HALTED |
| Hard halt 6 — fabricated or contradictory evidence | No | risk committee found none (`08`) |
| NO_TRADE 1 — fewer than 5 investable names | **Yes** | 0 names clear the evidence thresholds (`05`) |
| NO_TRADE 6 — structurally infeasible investable set | **Yes** | max attainable sleeve beta +0.2919 vs the 0.90 floor; Health Care 41.7% vs the 30% cap (L016) |
| REVIEW_ONLY 1 — data too stale/weak | No | all Required inputs grounded at zero lag to the completed session |

Recommendation to the orchestrator: **`NO_TRADE`**.
