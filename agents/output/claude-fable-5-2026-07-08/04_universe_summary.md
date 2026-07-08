# 04 Universe Summary

## Construction

Index-union path per rules.md §Index-Union Universe Protocol: `build_index_universe.py` run 2026-07-08T17:40:47Z from local constituent caches (both fetched_at 2026-06-21T21:05:56Z — 17 days stale; per protocol rule 5 used as-is, refresh remains a maintenance task). Counts from `universe_summary.json`: **503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap → 515 union**. All percentiles labeled **INDEX_UNION_PCTL (n=513)**. Sampled fallback NOT used.

## Inclusion / Exclusion Log

Screens applied to all 515 on fetched 5y daily bars (fetch manifest L002):

| Filter | Threshold | Rejects |
|---|---|---|
| History depth | ≥ 61 bars | FDXF (29 bars since listing) |
| Bar freshness | last bar ≥ 2026-07-07 | SATS (last print 2026-07-02 — **third session stale; structural exclusion, delisting/halt suspected — see 13**) |
| Price | > $5 | none |
| 20d ADV$ | > $20M | none |
| Listing | U.S. primary exchange | pre-satisfied by constituent caches |

**513 eligible.** Bid-ask spread and corporate-action screens: not evaluable without a quote tape (Enhancing input) — no name excluded on an unevaluable screen; noted as a data-quality cap, not a GO blocker.

## Metric Coverage Summary (rules.md §Financial Metrics inputs)

| Metric Group | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Price/volume + derived risk (30d vol, 60d beta, TE, maxDD60, VaR95, CVaR95, Kelly) | 513/513 | 0 | Fully computed from fetched bars (formulas in 01 rows) |
| Technical indicator pack d/w/m (TD-9, RSI14, MACD, MA, mom, VR, RS) | 513/513 | 0 | `technical_indicators.json` 2026-07-08T17:48:58Z, 518 records |
| Fundamental family (revisions, margins, FCF, ROIC, leverage) | 0 | 513 | Family 0.00 (UNAVAILABLE); DQ 0.80; confidence LOW; **data-quality issue, not a GO blocker** (Enhancing) |
| Sentiment family (short interest, skew, analyst breadth) | 0 | 513 | Same treatment |
| Earnings dates | 80 (shortlist, cadence est ±5d, INFERRED) | rest not evaluated | -0.10 penalty inside ≤19d buffered window (**34 names**) |
| Risk-free rate | ^IRX fresh 2026-07-08 print 3.725% (L006) | — | Ratios use rf_1m 0.310%; not RAW_DIAGNOSTIC |

Technical indicator coverage by timeframe: daily 513/513, weekly 513/513, monthly 513/513 for TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength vs SPY (SPY rows carry 0.00 RS by construction). No UNAVAILABLE indicator fields among eligible names.

Evidence-threshold consequence (unchanged, 8th consecutive run): with Fundamental and Sentiment UNAVAILABLE universe-wide, at most 2 of 4 families are sourceable, so threshold #2 (3-of-4 non-negative) is unsatisfiable for every name → investable set empty → **NO_TRADE** on stop criterion #1. The Track B proposal addressing this is in its 8th escalation (13).
