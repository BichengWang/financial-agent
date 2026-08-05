# 03 — Regime and Data — 2026-08-04

## Data-mode declaration

**`DELAYED`** per `rules.md § Data Mode Taxonomy` — quotes fetched this run with ≤1-day lag and
cross-checked across three independent web sources. All five Required inputs are grounded, so this is
**not** `DELAYED_PARTIAL`. The run is not in `ILLUSTRATIVE_MODE`: no field carries `ILLUSTRATIVE_REF`.

Fire window is **intraday** (2026-08-04T12:05:00-04:00, CNBC `curmktstatus` = `REG_MKT`). The newest completed
close is 2026-08-03; stockanalysis had published no partial same-day bar at fire time
(519/519 symbols
carry 2026-08-03 as their last bar), so technicals, entry prices and settlements share **one basis**.

## Regime classification — `BULL`

| Evidence | Value | Ledger row | Reads toward |
|---|---|---|---|
| VIX close | 15.86 (prior session 15.99) | `L-MACRO-VIX` | `BULL` — subdued, below the 20 threshold |
| SPY vs MA20 | 757.67 vs 746.01 → above | `L-PX-SPY`,`L-HIST-001` | `BULL` |
| SPY vs MA50 | 757.67 vs 744.60 → above | `L-PX-SPY`,`L-HIST-001` | `BULL` |
| SPY 20d / 60d momentum | +0.85% / +3.51% | `L-HIST-001` | `BULL` — positive over both windows |
| SPY 30d realized vol | 3.76% vs prior 30d 4.17% | `L-HIST-001` | not `HIGH_VOL` — vol is contracting |
| SPY drawdown from 60d high | +0.00% | `L-HIST-001` | `BULL` — at the 60-day high |
| 3-month T-bill | 3.75% | `L-MACRO-RF` | not `RATE_SHOCK` — no abrupt repricing |

Decision rule actually executed: price above both the 20- and 50-day moving averages **and** positive
60-day momentum **and** VIX < 20 → `BULL`. No `HIGH_VOL` trigger (VIX < 28 and 30d vol is not 1.5x the
prior 30d), no `BEAR` trigger (60d momentum is not below −5%).

## Event-concentration flags

| Flag | Value | Effect |
|---|---|---|
| Names in the scored universe printing within 14 calendar days | **142** of 512 | peak Q2 earnings season — each takes the `-0.10` adjusted-score penalty |
| Names inside the published set printing within 14 days | 1 of 24 | confidence capped `LOW` for those names by `rules.md § Risk Controls` |
| `NO_TRADE` trigger #4 (>2 names with earnings inside 14d) | not reached — the investable set is empty for other reasons | n/a |
| FOMC inside the 28-day horizon | `UNAVAILABLE` — no calendar feed wired | disclosed, not estimated |

## Core ETF Market Forecast Block

mu derivation is **never free-handed** (`rules.md § Core ETF Market Forecast`): SPY takes the
declared-regime prior; QQQ and SOXX take `beta_to_SPY x SPY mu` with beta from 60 fetched daily
adjusted returns. Regime `BULL` → SPY prior **+2.0%**. No ±1.0pp / ±1.5pp
adjustment was applied, because no ledger-backed relative view exists beyond what beta already carries.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY** | 757.67 | 2026-08-03 | `HISTORICAL` | above MA20 746.01 / above MA50 744.60 | 3.76% (falling vs prior 30d 4.17%) | +1.000 | +2.00% | 3.76% | `REALIZED_VOL_30D` | 772.82 | 2026-09-01 | 743.18 | 802.46 | MEDIUM | `L-PX-SPY`,`L-HIST-001` |
| **QQQ** | 700.07 | 2026-08-03 | `HISTORICAL` | above MA20 699.88 / below MA50 714.51 | 7.18% (falling vs prior 30d 7.51%) | +1.706 | +3.41% | 7.18% | `REALIZED_VOL_30D` | 723.96 | 2026-09-01 | 671.70 | 776.22 | MEDIUM | `L-PX-QQQ`,`L-HIST-001` |
| **SOXX** | 507.68 | 2026-08-03 | `HISTORICAL` | below MA20 535.31 / below MA50 567.33 | 18.60% (falling vs prior 30d 18.98%) | +3.530 | +7.06% | 18.60% | `REALIZED_VOL_30D` | 543.52 | 2026-09-01 | 445.33 | 641.72 | MEDIUM | `L-PX-SOXX`,`L-HIST-001` |

### Relative strength and consistency

| Ratio | 20d | 60d | Reading |
|---|---|---|---|
| QQQ / SPY | -4.00% | -2.78% | growth lagging the broad index over both windows |
| SOXX / SPY | -13.55% | -3.30% | semis lagging sharply over 20d |

**Regime-consistency check:** the `BULL` label rests on index-level trend and subdued
volatility, and SPY is at its 60-day high — but leadership is *not* in the high-beta complex, since
both QQQ and SOXX trail SPY over 20d and 60d. The label is consistent with the tape; the internal
rotation is defensive.

**Known miscalibration, disclosed:** `mu = beta x SPY_mu` gives SOXX **+7.06%**
purely because its beta is +3.530. Beta measures co-movement magnitude, not
expected-return direction, so with a non-negative SPY prior a bearish semis view is unrepresentable.
Settled `MARKET_FORECAST` hit rate is
22.09% over n=90.
This is a **Track A** fix to the Core ETF mu prior table and is `DEFER`red again — `eff_n` = 1 < 3.
The rule is followed as written rather than silently overridden.

## Universe handoff

| Handoff item | Value |
|---|---|
| Core ETFs to `technical_indicators.py` | SPY, QQQ, SOXX (+ TLT for the rate-sensitivity slot) |
| Eligible universe file | `agents/equity/.work/claude-opus-5-2026-08-04/eligible_universe.txt` — 515 tickers |
| Benchmark | SPY |
| History range | 5y daily (monthly indicators need ≥60 monthly bars) |
| Scored after filters | 512 |
