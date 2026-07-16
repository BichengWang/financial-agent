# 04 Universe Summary — 2026-07-15

## Construction

S&P 500 ∪ Nasdaq-100 index union from local constituent caches via `build_index_universe.py` (L001; `universe_summary.json`): **503 S&P 500 + 101 Nasdaq-100, 89 overlap → 515 union**, caches fetched 2026-06-21 (stale-cache rule: use and log, refresh is maintenance). Core ETFs SPY/QQQ/SOXX are the market-forecast sleeve — never universe members.

## Inclusion / Exclusion Log

| Filter | Threshold | Result |
|---|---|---|
| Listing | U.S. primary exchange | 515/515 pass (index constituents) |
| Price | > $5 | 514/514 fetched names pass (min in-universe ≈ $9) |
| 20d avg daily dollar volume | > $20M | all pass at index-cap scale (min ≈ $21M) |
| History / listing age | ≥ 126 daily bars (~6 months) | **FDXF rejected: 33 bars** |
| Halts / delisting / corporate-action ambiguity | none detected in fetched set | SATS fetched under its ECHO rename and saved as SATS (disclosed, L002) |

**Eligible universe: 514 names** (`eligible_universe.txt`). Percentile labels downstream: `INDEX_UNION_PCTL (n=514)`. Rejection log: FDXF (listing age) only. The 30-40-name sampled protocol was **not** used.

## Metric Coverage Summary

| Metric Group | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Price history / risk-return pack (beta, sigma, TE, DD, VaR/CVaR, Kelly, Sharpe/Sortino/IR) | 514/514 (5y daily bars) | 0 | — (L002) |
| Technical pack D/W/M (TD9, RSI, MACD, MA, momentum, VR, RS) | 514/514 | isolated monthly-MA gaps on short-history names | — (L003) |
| Earnings dates | 45 confirmed + 9 print-week estimates (54-symbol shortlist preflight) | rest of universe unfetched (only shortlist needs the penalty check) | -0.10 penalties per 03 §Event Concentration (L015) |
| Fundamental family | 0 | 514 | family 0.00 (UNAVAILABLE); DQ 0.80; confidence cap LOW — Enhancing-class, not a GO blocker |
| Sentiment family | 0 | 514 | same |
| Options IV / short interest / bid-ask tape | 0 | 514 | Enhancing-class caps only |

Technical indicator coverage detail (from `technical_indicators.json`): daily TD-9/RSI(14)/MACD/MA-alignment/momentum/volume-ratio/relative-strength **514/514**; weekly **514/514**; monthly complete except isolated MA50-class gaps on the shortest-history names (recorded `UNAVAILABLE` per name where they occur — none affect the published 24).

Data-quality consequence: with 2 of 4 families sourceable, no name can satisfy evidence threshold #2 (3-of-4 families non-negative) — the structural NO_TRADE gate, 13th consecutive scoring run (05, 08).
