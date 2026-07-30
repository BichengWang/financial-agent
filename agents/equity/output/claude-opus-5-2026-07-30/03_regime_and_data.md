# 03 — Regime & Data — 2026-07-30

## Data mode

**`DELAYED`.** Every price used as a basis is the **2026-07-29** close — the last completed
session — fetched this run and verified across two independent vendors (three for the core
ETFs). The run fired at 2026-07-30T10:06:00-04:00, roughly 36 minutes after the 2026-07-30 open, so the 2026-07-30 session
is in progress and deliberately **not** used as a basis for any entry, target, CI or settlement
price. Live 2026-07-30 quotes appear only in `10_midday_monitor.md`, labelled as observation.

Coverage: **519** symbols fetched with 5 years of daily bars, **zero** fetch
failures, and every symbol's last bar dated `2026-07-29` — one consistent price basis across the
whole universe with no T-1/T-0 reconciliation to carry.

## Regime classification

**`NEUTRAL`**

| Evidence | Value | Ledger |
|---|---|---|
| SPY close (2026-07-29) | 729.46 | L-PX-SPY |
| SPY vs MA20 | **below** (745.79) | L015 |
| SPY vs MA50 | **below** (743.83) | L016 |
| SPY 20d momentum | -2.32% | L-PX-SPY |
| SPY 60d momentum | +1.48% | L-PX-SPY |
| SPY 30d realized vol (1m) | 3.57%, **falling** vs prior 30d 4.17% | L017 |
| SPY drawdown from 60d high | -4.49% | L018 |
| VIX close | **20.66** (prior 18.21, +13.5% in one session) | L005, L006 |
| VIX vs its own 20d mean | 17.17 — VIX sits **20.3%** above it | L005 |

**Why `NEUTRAL` and not something else.** The tape is genuinely mixed, so the label is
argued rather than asserted:

- Not `BULL`: SPY closed **below both** its 20d and 50d moving averages and 20d momentum is
  -2.32%. Trend confirmation is absent.
- Not `BEAR`: 60d momentum is still **+1.48%** and the drawdown from the 60d high
  is only -4.49% — far from a bear structure.
- Not `HIGH_VOL`: VIX 20.66 is elevated and jumped
  13.5% in a session, but it is below the 22 threshold, and
  *realized* vol is **falling** (3.57% vs
  4.17%). Implied stress is rising while realized stress falls.
- Not `RATE_SHOCK`: the 13-week bill sits at 3.70% with no shock event in the
  window.

`NEUTRAL` is the honest label: no directional trend confirmation, contained drawdown, and a
vol picture that disagrees with itself. SPY prior mu is therefore **+0.50%**
per `rules.md § Core ETF Market Forecast`, taken with **no** discretionary adjustment.

### Event concentration

| Flag | Assessment |
|---|---|
| Clustered earnings | **HIGH.** The forward sweep puts **488** companies on 2026-08-05 and **569** on 2026-08-06 across the whole market; 262 of our 513 scored names report inside the 37-day window. |
| Names with earnings ≤14d in the published set | 2 (each penalised −0.10 and confidence-capped `LOW`) |
| FOMC inside horizon | `UNAVAILABLE` — no FOMC calendar feed is wired this run. Recorded, not guessed. |

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 729.46 | 2026-07-29 | HISTORICAL | BELOW / BELOW | 3.57% | 1.0000 | +0.50% | 3.57% | REALIZED_VOL_30D | 733.11 | 2026-08-27 | 706.02 | 760.20 | MEDIUM | L-ETF-SPY, L-PX-SPY |
| QQQ | 661.73 | 2026-07-29 | HISTORICAL | BELOW / BELOW | 6.96% | 1.7022 | +0.85% | 6.96% | REALIZED_VOL_30D | 667.36 | 2026-08-27 | 619.50 | 715.23 | MEDIUM | L-ETF-QQQ, L-PX-QQQ |
| SOXX | 465.00 | 2026-07-29 | HISTORICAL | BELOW / BELOW | 18.86% | 3.6391 | +1.82% | 18.86% | REALIZED_VOL_30D | 473.46 | 2026-08-27 | 382.24 | 564.68 | MEDIUM | L-ETF-SOXX, L-PX-SOXX |

**mu derivation** (never free-handed): SPY mu = the `NEUTRAL` regime prior
+0.50%, unadjusted. QQQ and SOXX use `mu = beta_to_SPY x SPY_mu` with beta from
60 days of fetched daily returns — QQQ 1.7022 → +0.85%,
SOXX 3.6391 → +1.82%. No relative-view adjustment was applied.

> **Known defect, disclosed rather than papered over.** `mu = beta x SPY_mu` is a category
> error diagnosed on 2026-07-24: beta measures co-movement *magnitude*, not expected-return
> *direction*, so with a non-negative SPY prior a high-beta ETF can never express a bearish
> view. SOXX's beta of 3.6391 mechanically forces
> +1.82% regardless of evidence. Settled `MARKET_FORECAST` direction accuracy is
> **16.4%** over n=63. The fix is Track A and **gated**: `eff_n`
> = 1 < 3 (rises 2026-08-09). The forecast is
> published as the rules require, with its known bias stated.

### Relative strength

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | -7.82% | -3.21% |
| SOXX / SPY | -25.11% | -1.59% |

**Regime-consistency check:** relative strength is deeply negative for both growth proxies over
60 days (SOXX -1.59% vs SPY), which is consistent with the `NEUTRAL`
call and with the defensive rotation the settlement batch measured — the index held up while
its highest-beta component fell hard. Consistent, with one caveat recorded in `10`: that
rotation is violently reversing during the 2026-07-30 session itself.

## Universe handoff

`build_index_universe.py` produced **515** tickers
(503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap).
Handed to `technical_indicators.py`: those 515 names plus SPY, QQQ, SOXX, TLT.
Core ETFs are a forecast sleeve and are never universe members, candidates, or percentile
constituents.

## Stop-rule assessment

No `HALTED` condition: benchmark data is present, lineage is complete for every core field, and
the risk committee found no contradictory evidence. Not `REVIEW_ONLY` either — the data is
same-session fresh, not stale. The run proceeds to scoring, where the Evidence Thresholds
decide the outcome.
