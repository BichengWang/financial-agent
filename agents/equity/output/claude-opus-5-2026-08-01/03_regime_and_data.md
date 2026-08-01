# 03 — Regime and Data — 2026-08-01

## Data mode

**`DELAYED`** — every quote was fetched during this run and carries ≤ 1-day lag relative to
the last completed session. 2026-08-01 is a Saturday: the Friday 2026-07-31 close is final at all
vendors, so "delayed" here means *one calendar gap*, not *stale*. This is **not**
`ILLUSTRATIVE` (no reference-state values were used) and **not** `DELAYED_PARTIAL` (no
Required input failed).

| Check | Result |
|---|---|
| Bulk history | 519/519 symbols, 31.8s, 8 workers |
| Last bar on every symbol | **2026-07-31** — 1 distinct value across 519 symbols |
| Price grounding | 77/77 on 3 independent sources, max dev 0.0661% |
| Vendor aliases applied | {'BF-B': 'BF.B', 'BRK-B': 'BRK.B', 'SATS': 'ECHO'} |
| Transport failures | 0 |

`SATS` is fetched as `ECHO` (EchoStar renamed; unfixed upstream since 2026-07-13) and is
aliased in the screener lookup too, so it does not silently drop on
`MARKET_CAP_UNAVAILABLE`. `BRK-B`/`BF-B` use dot notation at stockanalysis and slash
notation (`BRK/B`, `BF/B`) at the Nasdaq screener.

## Regime classification — **`BULL`**

| Evidence | Value | Ledger |
|---|---|---|
| SPY close (adj) | 747.03 | `L-HIST` |
| SPY MA20 / MA50 | 745.69 / 744.23 | `L-HIST` |
| SPY vs MA20 / MA50 | ABOVE / ABOVE | derived |
| SPY MA alignment | `BULLISH` | `technical_indicators.json` |
| SPY 20d / 60d momentum | +0.30% / +3.48% | `technical_indicators.json` |
| SPY RSI(14) daily | 53.14 | `technical_indicators.json` |
| SPY 30d realized vol (ann.) | 12.73% vs prior 30d 14.69% | derived, `L-HIST` |
| SPY drawdown from 60d high | -1.40% | derived, `L-HIST` |
| VIX close | 15.99 | `L-MAC-VIX` |
| VIX 20d ago / 60d mean | 15.81 / 17.4117 | `L-MAC-VIX`, `L-MAC-VIX60` |
| 3m T-bill | 3.69% (2026-07-31) | `L-MAC-RF` |

**Rule applied:** VIX 15.99 < 28 (not `HIGH_VOL`); SPY is above its MA50 with
60d momentum +3.48% > 2% and VIX < 22 → **`BULL`**. The index
sits -1.40% off its 60-day high with realized vol
**falling** — a quiet, grinding advance rather
than a momentum thrust. `RATE_SHOCK` was not triggered: the 3-month bill at
3.69% shows no shock move.

**Honest caveat.** `BULL` is the defensible label on these thresholds, but it is a *thin*
bull: SPY's 20d momentum is only +0.30% and QQQ and SOXX are both
**below** their MA20 *and* MA50 while SPY is above both. Leadership is narrow and rotating
away from growth/semis — which is exactly the condition under which this system's
trend-following `Tech_Z` has historically inverted.

## Core ETF Market Forecast Block

| ETF | Entry | Price Date | Tag | Trend 20d/50d | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Conf | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 747.03 | 2026-07-31 | `HISTORICAL` | ABOVE/ABOVE | 3.67% | +1.0000 | **+2.000%** | 3.67% | `REALIZED_VOL_30D` | 761.97 | 2026-08-29 | 733.42 | 790.52 | MEDIUM | `L-ETF-SPY` |
| QQQ | 687.99 | 2026-07-31 | `HISTORICAL` | BELOW/BELOW | 7.34% | +1.7177 | **+1.935%** | 7.34% | `REALIZED_VOL_30D` | 701.31 | 2026-08-29 | 648.76 | 753.85 | MEDIUM | `L-ETF-QQQ` |
| SOXX | 504.89 | 2026-07-31 | `HISTORICAL` | BELOW/BELOW | 19.53% | +3.6683 | **+5.837%** | 19.53% | `REALIZED_VOL_30D` | 534.36 | 2026-08-29 | 431.82 | 636.90 | MEDIUM | `L-ETF-SOXX` |

**mu derivation** (`rules.md § Core ETF Market Forecast`, never free-handed):

- `SPY`: mu = the `BULL` regime prior = **+2.00%**, unadjusted.
- `QQQ`: mu = beta × SPY mu = 1.7177 × +0.020 =
  +3.4355%, adjusted **-1.50pp** →
  **+1.935%**. Reason: BELOW MA20 (701.02) and MA50 (714.75) while SPY is ABOVE both; RS20 vs SPY -3.75pp -> full -1.5pp.
- `SOXX`: mu = 3.6683 × +0.020 =
  +7.3365%, adjusted **-1.50pp** →
  **+5.837%**. Reason: BELOW MA20 (539.00) and MA50 (567.58) while SPY is ABOVE both; RS20 vs SPY -11.15pp -> full -1.5pp.

**This block is flagged as a known-weak forecast, and the reason is structural.** The
`beta × SPY_mu` rule was diagnosed on 2026-07-24 as a category error: beta measures
co-movement *magnitude*, not expected-return *direction*. Today it shows the failure in the
bullish direction — SOXX's beta of 3.67 against a
+2.0% SPY prior mechanically produces a
+7.34% four-week expected return, **higher than any single
equity mu the calibration table can issue**, for an ETF that is below both its MA20 and MA50
and trailing SPY by -11.15pp over 20 days. The permitted ±1.5pp
adjustment is applied at its full bearish extent and is still far too small to express the
view. Canonical `MARKET_FORECAST` hit rate is 20.27% over n=78.
Fixing this requires changing the mu prior table, which is **Track A** and is blocked by
`eff_n` = 1 — recorded in `13` as a deferred observation, not a change.

**Relative strength:** QQQ/SPY -3.75pp (20d) /
-2.43pp (60d); SOXX/SPY -11.15pp (20d) /
+1.16pp (60d).

**Regime-consistency check:** a `BULL` label with both growth proxies below their
moving averages and negative 20d relative strength is *internally consistent but narrow* —
the advance is being led by defensives and value, not by the high-beta complex. Consistent
with the sector composition of today's leaderboard (Health Care and Finance dominate).

## Event concentration

| Flag | Value |
|---|---|
| Earnings sweep window | 2026-08-01 → 2026-09-07 (26 business days) |
| Sweep complete | **True** (0 transport failures) |
| Universe names with a confirmed print in window | 195 / 515 |
| Names with a print inside 14 days | **153** |
| Names in the published set carrying the 14d penalty | 1 |

153 of 515 names print within 14 days — **peak Q2
reporting season**. This is a genuine event-concentration flag at the universe level. It does
not bind the published set: only
1 of the top 24 carries the penalty, well
inside the "more than 2 names with earnings inside 14 days" `NO_TRADE` trigger — which
therefore did **not** fire. No FOMC meeting falls inside the 2026-08-29 horizon.

## Universe handoff

515 index-union tickers plus core ETFs `SPY QQQ SOXX TLT` were handed to
`technical_indicators.py`; 519 symbols returned daily/weekly/monthly packs. TLT is
fetched for the rate-sensitivity Macro component and the regime cross-check; it is not a
universe member and carries no forecast record.
