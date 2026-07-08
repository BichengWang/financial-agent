# 04 Universe Summary

## Construction

S&P 500 ∪ Nasdaq-100 index union via `build_index_universe.py`: 503 + 101 - 89 overlap = **515 names** (caches fetched 2026-06-21 — 10 days stale, used per protocol rule 5, staleness logged). `universe_summary.json` cited in 00/01/03. Normal index-union path succeeded — the 30-40 name sampled fallback was **not** used; ranks are labeled INDEX_UNION_PCTL (n=513).

## Inclusion/Exclusion Log

| Filter | Threshold | Rejections |
|---|---|---|
| History depth | >= 61 daily bars | 1 — FDXF (25 bars, recent spin-off; also fails 6-month listing age) |
| Bar freshness | last bar = 2026-07-01 | 1 — SATS (last bar 2026-06-30; did not trade today; unresolved corporate-action state) |
| Price | > $5 | 0 |
| Liquidity | ADV$20d > $20M | 0 |
| Session coverage | >= 80% of last 60 sessions | 0 |
| **Eligible** | | **513** |

Market-cap (> $2B) and listing filters are structurally satisfied by S&P 500 / Nasdaq-100 membership (INFERRED, index inclusion criteria); no independent market-cap feed was fetched. Core ETFs (SPY/QQQ/SOXX) analyzed separately — never universe members.

## Metric Coverage Summary (per rules.md §Financial Metrics and Score Attribution)

| Input group | Sourceable across eligible universe | Effect |
|---|---|---|
| Price history (5y daily) | 513/513 (100%) | drives all risk/technical metrics |
| Technical pack daily (TD9/RSI/MACD/MA/mom/VR/RS) | 514/513 TD9, 514/513 RSI, 514/513 MACD (>=70% bar met) | contributes to Tech_Z |
| Technical pack weekly/monthly | 514/513 weekly RSI, 513/513 monthly RSI | diagnostics + exhaustion flags |
| Risk metrics (sigma30/beta60/TE/maxDD/VaR/Kelly) | 513/513 | contributes to Macro_Z + sizing gates |
| Fundamental family | 0/513 — UNAVAILABLE | family 0.00; DQ 0.80; data-quality issue, NOT a GO blocker (Enhancing) |
| Sentiment family | 0/513 — UNAVAILABLE | family 0.00; DQ 0.80; data-quality issue, NOT a GO blocker (Enhancing) |
| Earnings dates | 52 shortlist names, cadence-estimated ESTIMATED (±5d) | -0.10 penalty inside 19d buffered window (7 names hit: IBKR, JBHT, UAL, UNH, CFG, ELV, AXP) |

RSI and MACD are sourceable for >=70% of the eligible universe, so they may contribute to Tech_Z per rules.md §Technical Indicator Pack; TD-9 setup 9 / RSI>=75 act only as exhaustion penalty flags, never standalone signals.

