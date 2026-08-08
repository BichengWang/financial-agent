# 03 — Regime and Data

## Data mode

**`DELAYED`** per `rules.md § Data Mode Taxonomy`. Quotes were fetched this run from the
completed 2026-08-07 session — no real-time feed is wired, and no Required input is missing,
so neither `DELAYED_PARTIAL` nor `ILLUSTRATIVE` applies. The run is **not** in
`ILLUSTRATIVE_MODE`.

| Check | Result |
|---|---|
| Symbols fetched | 519/519, 0 failures, 12.2s |
| Last bar == basis | 518/519 |
| Benchmark history | SPY 1255 daily bars (`L001`, `L015`) |
| Independent price sources | 3; 27/27 grounded at 0.0000% max deviation |
| Lineage gaps affecting scoring | `Fund_Z` (`L022`) and `Sent_Z` (`L023`) UNAVAILABLE universe-wide |

## Regime classification — `BULL`

| Evidence | Value | Reading | Ledger Rows |
|---|---|---|---|
| SPY close vs MA20 | 773.26 vs 750.17 | ABOVE — trend intact | `L001`, `L019` |
| SPY close vs MA50 | 773.26 vs 746.62 | ABOVE — trend intact | `L001`, `L019` |
| SPY 20d / 60d momentum | +2.43% / +5.02% | positive on both horizons | `L019` |
| SPY 30d realized vol | 3.82% | low; falling vs the prior 30d | `L001` |
| SPY drawdown from 60d high | 0.00% | at the 60-day high | `L001` |
| VIX close | 14.9 (prior 15.15) | well below 20 and falling | `L004`, `L005` |
| SPY RSI(14) daily | 66.03 | elevated but below the 70 overbought line | `L019` |
| SPY TD-9 daily | `SELL_SETUP_7` | **exhaustion watch** — two bars from a 9 setup | `L019` |
| Breadth (daily MA alignment BULLISH) | 47.95% | **narrow** — fewer than half the universe confirms the index | `L019` |
| 13-week bank discount | 3.72% | no rate shock | `L006` |

**Call: `BULL`**, which sets the SPY 4-week prior to
**+2.00%** per `rules.md § Core ETF Market Forecast`.

**The honest caveat, stated rather than buried.** Two pieces of evidence cut against the
label. Breadth is only 47.95% — fewer than half the scored
universe has bullish daily MA alignment while the index sits at its 60-day high — and daily
SPY TD-9 reads `SELL_SETUP_7`, two bars from an exhaustion 9. A `BULL` call on narrowing
breadth is the weaker kind of BULL. It is not downgraded to `NEUTRAL` because the
classification inputs `rules.md` names (trend vs MA20/MA50, realized vol, VIX regime,
momentum) are unanimous; the divergence is recorded here, and it is the stated reason SPY's mu
takes **no upward adjustment** off its prior.

## Event concentration

| Flag | Value | Assessment |
|---|---|---|
| Forward calendar sweep | 26/26 business days, complete=True | full-universe grounding; absence is positive evidence |
| Universe names printing within 37d | 59 | late-season tail |
| Universe names printing within 14d (penalized) | 26 | -0.10 Adj Score each; 5.09% of the scored universe |
| Published names with earnings <= 14d | 1 | `rules.md § Stop Criteria` downgrade #4 threshold is >2 — see 08 |
| FOMC inside horizon | UNAVAILABLE — no FOMC calendar feed wired | disclosed, not estimated |

Q2 season is winding down: 26 names carry the 14-day penalty against
153 on 2026-08-03, four sessions earlier.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 773.26 | 2026-08-07 | `HISTORICAL` | ABOVE/ABOVE | 3.82% | 1.0000 | +2.00% | 3.82% | `REALIZED_VOL_30D` | 788.73 | 2026-09-04 | 758.02 | 819.43 | MEDIUM | `L001`, `L015`, `L019`, `L020` |
| QQQ | 723.03 | 2026-08-07 | `HISTORICAL` | ABOVE/ABOVE | 7.32% | 1.7115 | +2.92% | 7.32% | `REALIZED_VOL_30D` | 744.16 | 2026-09-04 | 689.12 | 799.21 | MEDIUM | `L001`, `L015`, `L019` |
| SOXX | 543.27 | 2026-08-07 | `HISTORICAL` | ABOVE/BELOW | 18.23% | 3.4767 | +5.45% | 18.23% | `REALIZED_VOL_30D` | 572.90 | 2026-09-04 | 469.88 | 675.92 | MEDIUM | `L001`, `L015`, `L019` |

**mu derivation** (never free-handed):

| ETF | Rule | Computation | Adjustment applied | Final mu |
|---|---|---|---|---|
| SPY | regime prior, +/-1.0pp | `BULL` -> +2.00% | **none** — breadth divergence and TD-9 SELL_SETUP_7 argue against an upward adjustment | +2.00% |
| QQQ | beta x SPY mu, +/-1.5pp | 1.7115 x +2.00% = +3.42% | **-0.50pp** — rs20 -2.77% and rs60 -2.67% vs SPY | +2.92% |
| SOXX | beta x SPY mu, +/-1.5pp | 3.4767 x +2.00% = +6.95% | **-1.50pp (band max)** — only core ETF below its MA50, rs20 -8.98%, -17.06% below its 60d high | +5.45% |

**Known defect, disclosed rather than silently carried.** `mu = beta x SPY_mu` is a category
error diagnosed on 2026-07-24: beta measures co-movement magnitude, not expected-return
direction, so with any non-negative SPY prior a high-beta ETF cannot express a bearish view.
SOXX's beta of 3.4767 mechanically produces
+6.95% before adjustment. The -1.5pp band maximum is applied on ledger-backed
relative weakness, but it cannot repair the mapping. Replacing the rule is a **Track A** change
to the Core ETF mu prior table and remains gated at `eff_n = 1 < 3`.

**Relative strength and analysis minimum:**

| ETF | vs MA20 | vs MA50 | 30d RVol | vs prior 30d | Drawdown from 60d high | RS 20d vs SPY | RS 60d vs SPY | RSI(14) | TD-9 | MACD |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | ABOVE | ABOVE | 3.82% | FALLING | 0.00% | +0.00% | +0.00% | 66.03 | `SELL_SETUP_7` | `ABOVE_SIGNAL` |
| QQQ | ABOVE | ABOVE | 7.32% | FALLING | -2.99% | -2.77% | -2.67% | 57.18 | `SELL_SETUP_6` | `ABOVE_SIGNAL` |
| SOXX | ABOVE | BELOW | 18.23% | FALLING | -17.06% | -8.98% | +0.32% | 51.20 | `SELL_SETUP_5` | `ABOVE_SIGNAL` |

**Regime-consistency check.** The `BULL` call is consistent with SPY and QQQ (both
above MA20 and MA50, both with `ABOVE_SIGNAL` MACD, both with falling realized vol) and
**partially inconsistent with SOXX**, which sits below its 50-day MA and
-17.06% off its 60-day high. Semis lagging a broad-market
high is the same narrow-breadth signal flagged above.

ETF rows are a market-forecast sleeve — never candidates, never universe members, exempt from
the single-name filters, and excluded from every percentile distribution and portfolio cap.

## Universe handoff

Handed to `technical_indicators.py` and then to Factor Scoring: the 515-name
index union plus core ETFs `SPY`, `QQQ`, `SOXX` and the `TLT` rate proxy — 519
symbols total. 511 names survived the inclusion/exclusion filters and were scored; see
`04_universe_summary.md` for the rejection log.

## Stop-rule assessment

No `HALTED` condition applies: benchmark data is present, lineage is complete for every core
field, and no fabricated or contradictory evidence was found. Data is current rather than
stale, so `REVIEW_ONLY` on staleness grounds does not apply either. The status decision is an
evidence-threshold question, handled in `08` and `00`.
