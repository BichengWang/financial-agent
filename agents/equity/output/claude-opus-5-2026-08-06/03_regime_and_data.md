# 03 — Regime and Data

## Data-mode declaration

**`DELAYED`** — every quote was fetched this run and carries at most a one-session lag
(the 2026-08-05 completed close, read at ~11:05 ET on 2026-08-06 while the
2026-08-06 session was open). All five Required inputs are grounded, so this mode is
eligible for `GO` at reduced exposure; the run is `NO_TRADE` for evidence reasons, not
data-mode reasons. This is **not** `DELAYED_PARTIAL` (no Required input failed) and **not**
`ILLUSTRATIVE` (nothing is drawn from reference state).

## Regime classification — **`BULL`**

| Evidence | Value | Ledger row |
|---|---|---|
| SPY close (2026-08-05) | 769.79 | L001, L003 |
| SPY vs MA20 | **above** (748.41) | L004 |
| SPY vs MA50 | **above** (745.73) | L004 |
| SPY daily MA alignment | `BULLISH` | L004 |
| SPY 20d momentum | +3.27% | L004 |
| SPY 60d momentum | +4.63% | L004 |
| SPY RSI(14) daily | 64.82 | L004 |
| SPY MACD state (daily) | `ABOVE_SIGNAL` | L004 |
| SPY 30d realized vol (1m) | 3.79% | L012 |
| …vs the prior 30d | 4.30% -> **falling** | L012 |
| SPY drawdown from 60d high | -4.49% | L013 |
| VIX close | **15.81** | L009 |
| 13-week T-bill (bank discount) | 3.74% | L010 |

**Reasoning.** SPY sits above both its MA20 and MA50 with a `BULLISH`
alignment, 60-day momentum of +4.63%, and realized volatility
*contracting* (3.79% vs
4.30% in the prior 30 days) with VIX at
15.81 — far below the 25 threshold that would force `HIGH_VOL`. Drawdown from
the 60-day high is only -4.49%. That combination is `BULL`.
RSI(14) at 64.82 is elevated but below the 70 overbought line and is an
exhaustion flag, not a regime override.

Per `rules.md § Core ETF Market Forecast`, `BULL` sets the **SPY prior mu = +2.00%**
(4-week). No ±1.0pp adjustment applied.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 769.79 | 2026-08-05 | HISTORICAL | above MA20 (748.41) / above MA50 (745.73) | 3.79% | 1.0000 | +2.00% | 3.79% | REALIZED_VOL_30D | 785.19 | 2026-09-03 | 754.81 | 815.56 | MEDIUM | L001, L002, L004, L012 |
| QQQ | 717.30 | 2026-08-05 | HISTORICAL | above MA20 (700.89) / above MA50 (714.72) | 7.29% | 1.7114 | +3.42% | 7.29% | REALIZED_VOL_30D | 741.85 | 2026-09-03 | 687.47 | 796.23 | MEDIUM | L001, L002, L004, L012 |
| SOXX | 530.70 | 2026-08-05 | HISTORICAL | below MA20 (533.27) / below MA50 (567.56) | 18.47% | 3.4992 | +7.00% | 18.47% | REALIZED_VOL_30D | 567.84 | 2026-09-03 | 465.90 | 669.78 | MEDIUM | L001, L002, L004, L012 |

### Analysis minimum (per ETF)

| ETF | 20d mom | 60d mom | RSI(14) d | MACD d | TD-9 d | 30d RVol | Prior 30d RVol | Vol direction | DD from 60d high |
|---|---|---|---|---|---|---|---|---|---|
| SPY | +3.27% | +4.63% | 64.82 | `ABOVE_SIGNAL` | `SELL_SETUP_5` | 3.79% | 4.30% | falling | -4.49% |
| QQQ | +0.82% | +0.96% | 55.42 | `ABOVE_SIGNAL` | `SELL_SETUP_4` | 7.29% | 7.82% | falling | -11.22% |
| SOXX | -5.57% | +2.05% | 48.44 | `BULLISH_CROSS` | `SELL_SETUP_3` | 18.47% | 19.70% | falling | -29.01% |

### Relative strength

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | -2.45% | -3.66% |
| SOXX / SPY | -8.85% | -2.58% |

### mu derivation and a disclosed weakness

`SPY` takes the regime prior directly (+2.00%). `QQQ` and `SOXX` use
`mu = beta_to_SPY x SPY mu` from 60-day fetched daily returns, per the rule; **no ±1.5pp
adjustment was applied** to either.

This produces `SOXX mu = 3.4992 x +2.00%
= +7.00%` — a large number that the run is obliged to publish and
equally obliged to flag. SOXX's beta reads 3.4992
because SPY's own realized volatility is unusually low right now
(3.79% monthly): beta is a ratio, and a small
denominator inflates it. The 2026-07-24 package diagnosed the underlying issue — beta
measures co-movement magnitude, not expected-return direction, so `beta x SPY_mu` cannot
express a bearish ETF view while the SPY prior is non-negative. That diagnosis stands, and
`SOXX`'s -5.57% 20-day momentum is visibly at odds with a
+7.00% prior. Correcting the formula is a **Track A** change to a
protected prior table, gated at `eff_n = 2 < 3`, so this run applies the rule as
written and records the tension rather than free-handing a fix.

### Regime consistency check

Consistent. `BULL` is corroborated by all three ETFs holding above their MA20/MA50 with
`ABOVE_SIGNAL`-or-better MACD states and contracting volatility. The one dissonance is
SOXX's negative 20-day momentum (-5.57%) against positive
60-day momentum (+2.05%) — semiconductor leadership is
wobbling inside an otherwise intact uptrend.

## Event concentration

| Flag | Value |
|---|---|
| Universe names with earnings inside 14 calendar days | **58** of 511 scored (11.4%) |
| Published names inside 14 days | **0** of 24 |
| Sweep completeness | 27/27 business days, zero transport failures |

Early August is peak Q2 season, so a high universe-wide penalty count is expected. The
`NO_TRADE` downgrade criterion "more than 2 names with earnings inside 14 days" is **not**
what drove this run — zero published names carry the penalty.

## Universe handoff

511 scored names + core ETFs `SPY`, `QQQ`, `SOXX` (and `TLT` as the
rate-sensitivity reference) were handed to `technical_indicators.py`. Details and the
rejection log: `04_universe_summary.md`.
