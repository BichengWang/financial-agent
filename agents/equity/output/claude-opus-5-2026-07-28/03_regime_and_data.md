# 03 Regime and Data — 2026-07-28

## Data Mode Declaration

**`DELAYED`** — every price used downstream was fetched during this run and logged with a
retrieval timestamp (L002–L006). The run fires pre-open, so the basis is the last completed close,
2026-07-27; nothing here is an intraday print.

| Source | Role | Status |
|---|---|---|
| stockanalysis.com 5Y history | bulk primary (raw `c` + adjusted `a`) | **519/519 symbols, 26.5s, 0 failures** |
| api.nasdaq.com quote-info | independent close #2 (unadjusted) | 28/28 exact to the cent |
| quote.cnbc.com restQuote | independent close #3 | 27/28 exact to the cent (1 ex-div artifact, L054) |
| IBKR MCP snapshot | core ETF corroboration | SPY/QQQ/SOXX exact to the cent |
| Yahoo v8 chart | — | **429 BLOCKED** (probed 08:06 ET) |
| api.nasdaq.com bulk `historical` | — | **bot-challenge HTML, unusable** (unchanged since 2026-07-27) |

**Bulk history still has no redundancy.** stockanalysis.com is the only working bulk source; the other
three are per-symbol verification paths, not substitutes. That is a standing single-point-of-failure.

## Regime Classification — **`NEUTRAL`**

| Evidence | Value | Reading |
|---|---|---|
| SPY vs MA20 | -1.01% | below, but marginally |
| SPY vs MA50 | -0.67% | below, but marginally |
| SPY MA alignment | `MIXED` | neither trend regime |
| SPY 20d / 60d momentum | +1.39% / +4.13% | mildly positive |
| SPY 30d realized vol | 3.64% vs prior 30d 3.92% | **falling**, and low |
| SPY drawdown from 60d high | -2.45% | shallow |
| VIX | 18.67 vs 20d mean 16.88 | above average, below 20 |
| Breadth above MA50 / MA20 | 69.07% / 64.01% | healthy |
| Universe at negative 60d beta | 41.44% (213 of 514) | **rotation signature** |
| Universe median 30d realized vol | 9.36% | contained |
| TLT 20d / 60d momentum | -3.78% / -1.16% | drift, not a shock |

**Why `NEUTRAL` and not something else** — each alternative is excluded on cited evidence:

- Not `BULL`: SPY sits below both moving averages with `MIXED` alignment, and the
  growth complex is falling (QQQ -4.90% vs MA50, SOXX -9.25%).
- Not `BEAR`: breadth is 69.07% above MA50 and SPY is only -2.45%
  off its 60-day high.
- Not `HIGH_VOL`: SPY 30d realized vol is 3.64% and **falling**; VIX 18.67 is below 20.
- Not `RATE_SHOCK`: TLT is -3.78% over 20 days — a drift, not a shock.

The defining feature is **41.44% of the universe carrying negative 60-day beta**
alongside a flat index: money is moving *between* sectors, not into or out of equities as a block.

## Core ETF Market Forecast Block

A market-forecast sleeve — **never candidates, never universe members**. Excluded from the 514-name
percentile base, the investable count and every portfolio cap.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 739.09 | 2026-07-27 | HISTORICAL | -1.01% / -0.67% (`MIXED`) | 3.64% (FALLING) | 1.0000 | +0.50% | 3.64% | REALIZED_VOL_30D | 742.7854 | 2026-08-25 | 714.8330 | 770.7379 | MEDIUM | L002, L003, L013, L015, L040 |
| QQQ | 682.12 | 2026-07-27 | HISTORICAL | -3.99% / -4.90% (`BEARISH`) | 7.27% (RISING) | 1.7200 | +0.86% | 7.27% | REALIZED_VOL_30D | 687.9864 | 2026-08-25 | 636.4270 | 739.5458 | MEDIUM | L002, L003, L013, L015, L041 |
| SOXX | 516.23 | 2026-07-27 | HISTORICAL | -8.11% / -9.25% (`BEARISH`) | 18.58% (RISING) | 3.6474 | +1.82% | 18.58% | REALIZED_VOL_30D | 525.6445 | 2026-08-25 | 425.8826 | 625.4064 | MEDIUM | L002, L003, L013, L015, L042 |

### Analysis minimum, per ETF

| Metric | SPY | QQQ | SOXX | TLT (regime cross-check only) |
|---|---|---|---|---|
| Close (2026-07-27, raw) | 739.09 | 682.12 | 516.23 | 83.75 |
| MA20 | 746.658 | 710.493 | 561.767 | 84.488 |
| MA50 | 744.0936 | 717.2381 | 568.8648 | 84.786 |
| MA alignment | `MIXED` | `BEARISH` | `BEARISH` | `BEARISH` |
| 30d realized vol | 3.64% | 7.27% | 18.58% | 2.32% |
| Prior 30d realized vol | 3.92% | 6.81% | 17.73% | 2.73% |
| Vol direction | FALLING | RISING | RISING | FALLING |
| Drawdown from 60d high | -2.45% | -8.48% | -21.19% | -3.88% |
| RSI(14) daily | 45.65 | 38.64 | 40.89 | 40.96 |
| TD-9 daily | `BUY_SETUP_8` | `BUY_SETUP_9` | `BUY_SETUP_1` | `SELL_SETUP_1` |
| MACD state daily | `BELOW_SIGNAL` | `BELOW_SIGNAL` | `BELOW_SIGNAL` | `BELOW_SIGNAL` |
| 60d beta vs SPY | 1.0000 | 1.7200 | 3.6474 | 0.2673 |

### Relative strength

| Ratio | 20d | 60d |
|---|---|---|
| QQQ / SPY | -4.84pp | -0.91pp |
| SOXX / SPY | -13.88pp | +10.64pp |

**Regime-consistency check.** Growth and semis are losing relative ground over 20 days
(QQQ -4.84pp, SOXX -13.88pp) while SOXX still carries a positive
60-day reading (+10.64pp) and sits -21.19% below its
60-day high. A high-beta leader unwinding a large 60-day gain, with the index flat, low-vol and below
both moving averages, is consistent with `NEUTRAL` and rotation — not with a trend regime and not
with a volatility event.

### mu derivation (never free-handed)

| ETF | Rule | Computation | Result |
|---|---|---|---|
| SPY | regime prior for `NEUTRAL` | +0.50%, no ±1.0pp adjustment applied | +0.50% |
| QQQ | `beta_to_SPY × SPY mu` | 1.7200 × 0.005 | +0.86% |
| SOXX | `beta_to_SPY × SPY mu` | 3.6474 × 0.005 | +1.82% |

**Disclosed known defect, applied as written — with today's evidence sharpening it.** The 2026-07-24
package diagnosed `mu_ETF = beta × SPY_mu` as a category error: beta measures co-movement *magnitude*,
not expected-return *direction*. Today makes the failure concrete and quantifiable:

- SOXX is -21.19% below its 60-day high, -9.25% below
  its MA50, with realized vol 18.58% and **rising**, and RS20 -13.88pp.
  Every piece of ledger-backed evidence points down.
- The formula nonetheless returns **+1.82%**, the single most bullish forecast in the
  block, purely because SOXX's beta is 3.6474.
- Even the full ±1.5pp adjustment band cannot express a bearish SOXX view: +1.82% − 1.5pp =
  +0.32%, still non-negative and inside the `|mu| < 0.5%` flat-call zone.
  **The band is structurally too narrow to fix a beta-scaled prior.**

**No discretionary adjustment was applied**, matching the 2026-07-27 decision. Only the evolution agent
may change this table, and Track A requires `eff_n ≥ 3` against an actual `eff_n` of 1.
Applying a known-bad formula transparently, and settling it honestly, is what earns the evidence to
replace it; quietly overriding it would destroy that evidence. The settled record is unambiguous —
20.83% hit rate over n=48, and all 6 of today's settlements were MISS.

## Event Concentration

| Flag | Value |
|---|---|
| Names with earnings inside 14 calendar days (buffered) | 34 of 514 scored |
| …of which in the published set | **3** of 24 |
| `NO_TRADE` trigger #4 threshold | more than 2 names with earnings inside 14 days |
| Verdict | **the published set breaches it** (3 > 2) — an additional, independent `NO_TRADE` ground |
| FOMC inside horizon | `UNAVAILABLE` — no calendar feed wired; disclosed, not inferred |

## Universe Handoff

515 index-union tickers plus SPY/QQQ/SOXX/TLT were handed to `technical_indicators.py`
(L010). 514 names survive the inclusion filters and are scored; the rejection log is in `04`.

## Stop-Rule Assessment

No `HALTED` condition is met: benchmark data is present, lineage is explicit for every core field, no
top-ranked candidate has an unresolved critical input, the index union materialized, and the risk
committee found no fabricated or contradictory evidence. Data is fresh rather than stale, so
`REVIEW_ONLY` does not apply either. **Recommendation to the orchestrator: `NO_TRADE`** on candidate
quality.
