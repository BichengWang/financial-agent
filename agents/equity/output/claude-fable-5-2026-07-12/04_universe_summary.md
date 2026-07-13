# 04 Universe Summary

## Construction

S&P 500 ∪ Nasdaq-100 index union via `build_index_universe.py` (universe_summary.json, generated 2026-07-12T12:28:18Z): **503 + 101 − 89 overlap = 515 union** (constituent caches fetched 2026-06-21 — staleness logged per protocol; refresh remains a maintenance task, not a fallback trigger). Percentile labels: **INDEX_UNION_PCTL (n=513)**. Sampled fallback NOT used.

## Inclusion / Exclusion Log

Screens applied to the full union on this run's fetched bars (formulas in 01 header): ≥60 daily bars; last bar = 2026-07-10 (the last completed session); price > $5; 20d dollar-ADV > $20M; ≥80% session coverage over the trailing 60 sessions.

| Ticker | Action | Reason |
|---|---|---|
| SATS | REJECTED | Structural: Yahoo returns a single stale bar; no prints since 2026-07-02 — standing exclusion carried since 07-08 (delisting/halt suspected) |
| FDXF | REJECTED | 31 bars since listing < 60 minimum |
| BF-B | **RE-ADMITTED** | 07-11's Nasdaq vendor-gap exclusion did not recur — full 5y series fetched cleanly this run, last bar 2026-07-10 |

**513 eligible.** No name failed the price, ADV, or session-coverage screens this run (the union is large-cap by construction).

## Metric Coverage Summary (rules.md § Financial Metrics and Score Attribution)

| Metric Group | Sourceable | UNAVAILABLE | DQ / Confidence Effect | GO Relevance |
|---|---|---|---|---|
| Price/volume + derived risk (sigma_1m, dsig_1m, beta60, TE, maxDD60, VaR/CVaR, Kelly) | 513 | 0 | — | Required inputs grounded |
| Technical indicator pack daily/weekly/monthly (TD-9, RSI14, MACD, MA alignment, momentum, volume ratio, RS vs SPY) | 513 | 0 | — | technical_indicators.json 2026-07-12T12:30:39Z (519/521 OK incl. ETFs+macro; SATS/FDXF UNAVAILABLE) |
| Fundamental family | 0 | 513 | DQ 0.80; family 0.00; confidence LOW | **Enhancing** — data-quality cap, never a GO blocker |
| Sentiment family | 0 | 513 | DQ 0.80; family 0.00; confidence LOW | **Enhancing** — data-quality cap, never a GO blocker |
| Earnings dates | 66 shortlist names **confirmed** (Nasdaq earnings-date endpoint, fetched this run); DAL cadence-estimated | rest not evaluated (outside shortlist) | -0.10 inside the ≤14d confirmed window | Required input satisfied for every published name |
| rf (3M T-bill) | ^IRX 3.695% fresh 2026-07-10 print | — | Sharpe/Sortino are rf-adjusted, not RAW_DIAGNOSTIC | — |

Technical indicator coverage by timeframe over the 513 eligible: daily 513/513, weekly 513/513, monthly 513/513 for TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength (SATS/FDXF are the only UNAVAILABLE records and both are excluded upstream).

The missing Fundamental and Sentiment families affect **data quality** (DQ 0.80, confidence LOW, family contributions 0.00) and make evidence threshold #2 (3-of-4 families non-negative) unsatisfiable universe-wide — on a trading day that forces NO_TRADE; today the weekend rule already caps at REVIEW_ONLY. They are Enhancing inputs and do not block GO by themselves (rules.md § Input Classification).

## Earnings Penalty Roll (confirmed-date upgrade)

28 of the top-60 shortlist names carry confirmed earnings inside the ≤14d window → -0.10 penalty. Materially re-ranked vs the prior runs' ±5d cadence estimates: STT (07-16, 4d), PNC/MTB/MS/UAL (07-15, 3d), USB/UNH/GE (07-16, 4d), RF (07-17, 5d), KEY/GPC/IBKR (07-21, 9d), URI/NTRS/GD/TDY/LUV (07-22, 10d), WST/EW/AMP (07-23, 11d), AXP (07-24, 12d) all penalized out of or down the leaderboard; **FFIV (07-27, 15d) clears the window it was previously penalized under**; DAL is 3 days post-print (reported 07-09) with no penalty and a cadence-estimated next date (~2026-10-08 ±5d).
