# 03 Regime and Data — 2026-07-27

## Data Mode Declaration

**`DELAYED`** per `rules.md § Data Mode Taxonomy`. Quotes and histories were fetched during this run
from public endpoints, cross-verified across two independent sources, and confirmed for the three
core ETFs by an IBKR brokerage snapshot. There is no streaming feed, so `LIVE` is not claimed for the
forecast basis. All five Required inputs are grounded, so this mode is `GO`-eligible on data grounds
(`DELAYED_PARTIAL` would apply only if a Required input had failed — none did).

### Source availability this session

| Source | State | Use |
|---|---|---|
| stockanalysis.com 5Y history | **OK** — 519/519 symbols in 26.6s at 8 workers | primary bulk history: raw close `c` (entry) + adjusted close `a` (returns) |
| CNBC restQuote | **OK** | independent price verification + live intraday tape |
| IBKR MCP snapshots | **OK** | brokerage confirmation of SPY/QQQ/SOXX basis |
| Nasdaq screener | **OK** | market cap + sector only |
| Nasdaq `analyst/{sym}/earnings-date` | **OK** (6 transient failures, all retried to resolution) | confirmed earnings dates |
| Yahoo v8 chart | **HTTP 429 — blocked** | not used. 8th blocked session of the last 14; availability remains unstable and must not be assumed |
| Nasdaq bulk `historical` | **degraded** — returned a bot-challenge HTML page, not JSON | **not used as a price source** this run |

The Nasdaq bulk-historical degradation is new this session and matters: it was the fallback primary
through most of July. With Yahoo also blocked, stockanalysis.com is currently a single point of
failure for bulk history, with CNBC (per-symbol) and IBKR as the verification layer.

## Regime Classification

**Declared regime: `NEUTRAL`** (L052, `INFERRED` from the ledger rows below).

1. SPY 738.93 below MA20 746.153 and MA50 744.1202 (alignment MIXED), 20d momentum +0.63% -> no trend
2. SPY drawdown from 60d high -2.47% (shallow, not BEAR)
3. VIX 18.58 on 07/24/2026 vs 20d mean 16.83 -> not HIGH_VOL
4. SPY 30d realized vol 3.96% (RISING) -> contained
5. internal rotation: SOXX -19.54% from 60d high, QQQ alignment BEARISH, TLT -4.45% -> defensive leadership, not broad risk-on
6. 13w T-bill 3.81% -> no RATE_SHOCK signature

No `BULL` label is defensible with the index below both moving averages and 20-day momentum at
+0.63%; no `BEAR` label is defensible with a -2.47%
drawdown from the 60-day high; `HIGH_VOL` fails on VIX 18.58 against a 20-day mean
of 16.83 and SPY 30-day realized vol of 3.96%; and
`RATE_SHOCK` fails on a 3.81% 13-week bill with TLT only
-4.45% off its 60-day high. `NEUTRAL` is the residual and
the honest label. It matches both the 2026-06-29 baseline and the concurrent `gpt-5-2026-07-27` call.

### Regime table

| Field | Value | Ledger |
|---|---|---|
| Regime | `NEUTRAL` | L052 |
| Data quality | `DELAYED`, DQ multiplier 0.8 | L035 |
| Key macro risk | Defensive rotation is crowded: 41.25% of the 514-name universe carries negative 60-day beta, so the highest-scoring names are the ones that lose most if the tape turns risk-on | L015, L049 |
| VIX | 18.58 on 07/24/2026 (20d mean 16.83) | L008 |
| 13-week T-bill | 3.81% (bank discount) | L009 |

## Core ETF Market Forecast Block

Analysis plus forecast from ~60 trading days of fetched history per ETF. **These are a market-forecast
sleeve, never candidates and never universe members** — they are excluded from the 514-name
percentile base, the investable count, and every portfolio cap.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 738.93 | 2026-07-24 | HISTORICAL | +0.63% / MA20 746.153 vs MA50 744.1202 (`MIXED`) | 3.96% (RISING) | 1.0 | +0.50% | 3.96% | REALIZED_VOL_30D | 742.6246 | 2026-08-24 | 712.2125 | 773.0368 | MEDIUM | L002, L003, L013, L015, L017, L040 |
| QQQ | 684.23 | 2026-07-24 | HISTORICAL | -4.49% / MA20 711.713 vs MA50 717.8742 (`BEARISH`) | 7.96% (RISING) | 1.7182 | +0.86% | 7.96% | REALIZED_VOL_30D | 690.1082 | 2026-08-24 | 633.487 | 746.7295 | MEDIUM | L002, L003, L013, L015, L017, L041 |
| SOXX | 527.01 | 2026-07-24 | HISTORICAL | -15.71% / MA20 565.4525 vs MA50 569.101 (`BEARISH`) | 20.19% (RISING) | 3.6395 | +1.82% | 20.19% | REALIZED_VOL_30D | 536.6005 | 2026-08-24 | 425.9389 | 647.2622 | MEDIUM | L002, L003, L013, L015, L017, L042 |

### Analysis minimum, per ETF

| Metric | SPY | QQQ | SOXX | TLT (regime cross-check only) |
|---|---|---|---|---|
| Close (2026-07-24, adjusted) | 738.93 | 684.23 | 527.01 | 83.25 |
| MA20 | 746.153 | 711.713 | 565.4525 | 84.6524 |
| MA50 | 744.1202 | 717.8742 | 569.101 | 84.7942 |
| MA alignment | `MIXED` | `BEARISH` | `BEARISH` | `BEARISH` |
| 30d realized vol | 3.96% | 7.96% | 20.19% | 2.57% |
| Prior 30d realized vol | 3.75% | 6.40% | 16.92% | 2.63% |
| Vol direction | RISING | RISING | RISING | FALLING |
| Drawdown from 60d high | -2.47% | -8.20% | -19.54% | -4.45% |
| RSI(14) daily | 45.5 | 39.33 | 42.78 | 33.19 |
| TD-9 daily | `BUY_SETUP_7` | `BUY_SETUP_8` | `SELL_SETUP_3` | `BUY_SETUP_5` |
| MACD state daily | `BELOW_SIGNAL` | `BELOW_SIGNAL` | `BELOW_SIGNAL` | `BELOW_SIGNAL` |
| 60d beta vs SPY | 1.0 | 1.7182 | 3.6395 | 0.2696 |

### Relative strength

| Ratio | 20d | 60d |
|---|---|---|
| QQQ / SPY | -5.12pp | +0.08pp |
| SOXX / SPY | -16.34pp | +16.09pp |

**Regime-consistency check.** Growth and semis are losing relative ground over 20 days
(QQQ -5.12pp, SOXX -16.34pp) while SOXX still
carries a positive 60-day relative reading (+16.09pp). A high-beta leader
rolling over from a large 60-day gain, with the index flat and below both MAs, is consistent with
`NEUTRAL` and rotation — not with either a trend regime or a volatility event.

### mu derivation (never free-handed)

| ETF | Rule | Computation | Result |
|---|---|---|---|
| SPY | regime prior for `NEUTRAL` | +0.50%, no ±1.0pp adjustment applied | +0.50% |
| QQQ | `beta_to_SPY × SPY mu` | 1.7182 × 0.005 | +0.86% |
| SOXX | `beta_to_SPY × SPY mu` | 3.6395 × 0.005 | +1.82% |

**Disclosed known defect, applied as written.** The 2026-07-24 package diagnosed
`mu_ETF = beta × SPY_mu` as a category error: beta measures co-movement magnitude, not expected-return
direction, so a beta of 3.6395 makes any bearish SOXX view unrepresentable while
the SPY prior is non-negative. The settled record is consistent with that diagnosis —
`MARKET_FORECAST` hit rate is 23.81% over n=42 (`02 § 0`), and today's
baseline settled QQQ and SOXX as MISS against a SPY HIT. **The rule is nonetheless applied unmodified
and no discretionary adjustment was used**, because only the evolution agent may change this table
and Track A requires `eff_n ≥ 3` against an actual `eff_n` of 1. Applying a known-bad
formula transparently is the auditable choice; quietly overriding it is not.

## Event Concentration

| Check | Result |
|---|---|
| Names in the published set with earnings inside 14 days (buffered) | 7 of 24 |
| Universe names penalised for earnings proximity | 40 of 514 |
| `NO_TRADE` trigger #4 (>2 investable names with earnings inside 14d) | not reached — the investable set is empty for prior reasons |
| FOMC inside the 2–6 week horizon | `UNAVAILABLE` — no calendar feed wired; disclosed, not estimated |

Peak Q2 reporting season is inside this run's horizon: 34
of the 57 names with grounded dates are `CONFIRMED`, and
40 universe names sit
inside the buffered 14-day window. This reshuffles the leaderboard materially versus the 2026-07-26
package on the same price basis — the earnings layer, three calendar days closer, is the single
largest source of rank change.

## Universe Handoff

515 index-union tickers plus core ETFs SPY, QQQ, SOXX (and TLT for the regime
cross-check) were handed to `technical_indicators.py`; 518 symbols returned complete daily, weekly
and monthly packs. Details and the rejection log: `04_universe_summary.md`.
