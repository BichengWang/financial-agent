# 04 Universe Summary

## Construction

S&P 500 ∪ Nasdaq-100 index union via `build_index_universe.py` (2026-07-05T19:46:29Z): 503 + 101 - 89 overlap = **515 names** (caches fetched 2026-06-21 — 14 days stale, used per protocol rule 5, staleness logged). `universe_summary.json` cited in 00/01/03. Normal index-union path succeeded — the 30-40 name sampled fallback was **not** used; ranks are labeled INDEX_UNION_PCTL (n=514).

## Inclusion/Exclusion Log

| Filter | Threshold | Rejections |
|---|---|---|
| History depth | >= 61 daily bars | 1 — FDXF (26 bars, recent spin-off; also fails 6-month listing age) |
| Bar freshness | last bar = last completed session (2026-07-02) | 0 |
| Price | > $5 | 0 |
| Liquidity | ADV$20d > $20M | 0 |
| Session coverage | >= 80% of last 60 sessions | 0 |
| **Eligible** | | **514** |

Market-cap (> $2B) and listing filters are structurally satisfied by S&P 500 / Nasdaq-100 membership (INFERRED, index inclusion criteria); no independent market-cap feed was fetched. Core ETFs (SPY/QQQ/SOXX) analyzed separately — never universe members. Bars are final 2026-07-02 closes (weekend run — no partial-bar caveats).

## Metric Coverage Summary (per rules.md §Financial Metrics and Score Attribution)

| Input group | Sourceable across eligible universe | Effect |
|---|---|---|
| Price history (5y daily) | 514/514 (100%) | drives all risk/technical metrics |
| Technical pack daily (TD9/RSI/MACD/MA/mom/VR/RS) | 514/514 (>=70% bar met) | contributes to Tech_Z |
| Technical pack weekly/monthly | 514/514 weekly RSI, 513/514 monthly RSI (Q short monthly history) | diagnostics + exhaustion flags |
| Risk metrics (sigma30/beta60/TE/maxDD/VaR/Kelly) | 514/514 | contributes to Macro_Z + sizing gates |
| Fundamental family | 0/514 — UNAVAILABLE | family 0.00; DQ 0.80; data-quality issue, NOT a GO blocker (Enhancing) |
| Sentiment family | 0/514 — UNAVAILABLE | family 0.00; DQ 0.80; data-quality issue, NOT a GO blocker (Enhancing) |
| Earnings dates | 51-name shortlist, cadence-estimated ESTIMATED (±5d) | -0.10 penalty inside 19d buffered window (**21 names hit**: DAL, UNH, BAC, SNA, UAL, IBKR, CFG, PPG, KEY, AXP, GE, SHW, GL, GPC, PKG, LII, URI, LUV, and newly DOC, WST, KDP on the one-day roll); universe rest not evaluated |

RSI and MACD are sourceable for >=70% of the eligible universe, so they may contribute to Tech_Z per rules.md §Technical Indicator Pack; TD-9 setup 9 / RSI>=75 act only as exhaustion penalty flags, never standalone signals. Daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, 20/60d momentum, 20d volume ratio, and RS vs SPY coverage: 514/514 daily, 514/514 weekly, 513/514 monthly (FDXF excluded pre-screen). Earnings-estimate scope note: the cadence-estimate shortlist covers the 07-04 run's 41 estimated names re-based to today plus 10 near-miss/promotion candidates (WELL, INCY, BXP, CINF, TTWO, VTRS, V, FTNT, CRL, PSA) — every published name and every top-30 rank except TROW/CRWD/SYY carries an estimate; those three sit >=9 rank places below the publication cutoff, so the gap cannot change the published set.
