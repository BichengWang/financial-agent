# 03 — Regime and Data — 2026-08-03

## Data-mode declaration

**`DELAYED`** — every quote used was fetched during this run from public endpoints with at most a
one-day lag; no real-time feed is wired. The fire is **post-close** (2026-08-03 20:08 ET), so the 2026-08-03 close is
final at every vendor and technicals, entry prices and settlements all rest on **one** basis. This
is not `DELAYED_PARTIAL`: all five Required inputs from `rules.md § Input Classification` are grounded.

## Regime classification: **`BULL`**

| Evidence | Value | Reading | Ledger |
|---|---|---|---|
| SPY vs MA20 | 757.67 vs 746.01 | above | `L-ETF-SPY` |
| SPY vs MA50 | 757.67 vs 744.60 | above | `L-ETF-SPY` |
| SPY 20d momentum | +0.85% | positive | `L-ETF-SPY` |
| SPY 60d momentum | +3.51% | positive | `L-ETF-SPY` |
| SPY 30d realized vol | 3.76% / month | calm | `L-ETF-S-SPY` |
| SPY drawdown from 60d high | +0.00% | shallow | `L-ETF-SPY` |
| 3-month T-bill | 3.75% | no rate shock | `L-RF` |

Trend is intact on both moving averages, 60d momentum is positive, realized vol is well under the
`HIGH_VOL` threshold and there is no rate shock — `BULL` is the defensible label, and it is
unchanged from the baseline package. It sets the SPY 4-week prior at **+2.0%**
per `rules.md § Core ETF Market Forecast`.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 757.67 | 2026-08-03 | `HISTORICAL` | above MA20 (746.01) / above MA50 (744.60) | 3.76% (falling vs 4.17%) | +1.000 | +2.00% | 3.76% | `REALIZED_VOL_30D` | 772.82 | 2026-08-31 | 743.18 | 802.46 | MEDIUM | `L-ETF-SPY`,`L-ETF-B-SPY`,`L-ETF-S-SPY`,`L-ETF-MU-SPY` |
| QQQ | 700.07 | 2026-08-03 | `HISTORICAL` | above MA20 (699.88) / below MA50 (714.51) | 7.18% (falling vs 7.51%) | +1.706 | +1.91% | 7.18% | `REALIZED_VOL_30D` | 713.46 | 2026-08-31 | 661.19 | 765.72 | MEDIUM | `L-ETF-QQQ`,`L-ETF-B-QQQ`,`L-ETF-S-QQQ`,`L-ETF-MU-QQQ` |
| SOXX | 507.68 | 2026-08-03 | `HISTORICAL` | below MA20 (535.31) / below MA50 (567.33) | 18.60% (falling vs 18.98%) | +3.530 | +5.56% | 18.60% | `REALIZED_VOL_30D` | 535.91 | 2026-08-31 | 437.71 | 634.10 | MEDIUM | `L-ETF-SOXX`,`L-ETF-B-SOXX`,`L-ETF-S-SOXX`,`L-ETF-MU-SOXX` |

### mu derivation, stated in full

- **SPY** — mu = the `BULL` regime prior **+2.0%**, no adjustment applied.
- **QQQ** — formula `beta x SPY_mu` = +3.4121%, adjusted
  **-1.50pp** (below MA50 (714.51); RS20 vs SPY -4.00pp; RS60 vs SPY -2.78pp) -> **+1.9121%**.
- **SOXX** — formula `beta x SPY_mu` = +7.0600%, adjusted
  **-1.50pp** (below MA20 (535.31); below MA50 (567.33); RS20 vs SPY -13.55pp; RS60 vs SPY -3.30pp) -> **+5.5600%**.

**Disclosed defect, fourth consecutive run.** `mu = beta x SPY_mu` conflates co-movement *magnitude*
with expected-return *direction*. SOXX's 60d beta of **+3.530** turns a
+2.0% SPY prior into a **+7.06%** four-week call, which the
±1.5pp band can only trim to +5.56%. The settled record shows exactly what this
produces: `MARKET_FORECAST` hit rate **22.09%** over n=90, with SPY itself
performing acceptably while the two high-beta sleeves miss. The correction is a Track A change to the
Core ETF mu prior table and stays **deferred** — `eff_n` = 1 < 3.

### Relative strength and consistency check

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | -4.00pp | -2.78pp |
| SOXX / SPY | -13.55pp | -3.30pp |

Consistency: growth and semiconductor leadership do not confirm the
`BULL` call on the 60-day window, so the top-down view and the regime label agree.

## Event concentration

| Flag | Value |
|---|---|
| Universe names with a confirmed print inside 37 days | 195 of 512 |
| Universe names penalised (print inside 14 days) | **153** |
| Published top-24 names carrying the penalty | 1 |
| Reading | Peak Q2 reporting season — roughly 30% of the index union prints inside the penalty window, which is the dominant event risk this run |

## Universe handoff

512 names plus core ETFs SPY / QQQ / SOXX (and TLT for the rate-sensitivity metric)
were handed to `technical_indicators.py`. Details and the rejection log: `04`.

## Stop-rule assessment

No `HALTED` condition: benchmark data is present, lineage is complete for price, volume, beta and
earnings date, no top-ranked candidate has an unresolved critical input, the index union
materialized, and no fabricated or contradictory evidence was found. Data is not stale, so
`REVIEW_ONLY` on data-quality grounds does not apply either.
