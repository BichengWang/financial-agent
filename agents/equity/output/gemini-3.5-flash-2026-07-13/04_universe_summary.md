# 04 Universe Summary — 2026-07-13

## Construction

S&P 500 ∪ Nasdaq-100 via `build_index_universe.py` (L001): **503 + 101, 89 overlap → 515 union**; caches dated 2026-06-21 (stale-cache rule applied: used and logged). Percentile label: **INDEX_UNION_PCTL (n=514)**. No sampled fallback used.

## Inclusion/Exclusion Log

| Filter | Threshold | Result |
|---|---|---|
| Fetched history | ≥ 126 bars (6mo listing age) | **FDXF rejected** (31 bars — recent spin-off listing; also technical_indicators UNAVAILABLE) |
| Price | > $5 | 0 rejected |
| ADV 20d | > $20M | 0 rejected (all index members clear) |
| Session coverage | ≥ 80% of trailing 60 SPY sessions | 0 rejected |
| Market cap | > $2B | Structurally satisfied by index membership (INFERRED — no cap feed; smallest S&P 500 members are >$5B) |
| Corporate actions | unresolved ambiguity | **SATS → ECHO ticker rename** resolved (EchoStar; series continuous under ECHO, retained as SATS in universe list); BRK-B/BF-B B-class symbology resolved (L002) |

**Eligible: 514 of 515.** Core ETFs (SPY/QQQ/SOXX) are a separate market-forecast sleeve, never universe members.

## Metric Coverage Summary

| Metric group (rules.md §Financial Metrics) | Sourceable | Notes |
|---|---|---|
| Price/volume history (5y daily) | **514/514** | Nasdaq hist API + 2 symbol-level fallbacks (L002) |
| Risk/return pack (sigma, beta, TE, corr, maxDD, VaR/CVaR, Sharpe/IR, Kelly) | **514/514** | Derived from fetched bars; Sortino omitted this run (downside-sigma series not persisted) → shown RAW_DIAG n/a, not neutral |
| Technical pack (TD9/RSI/MACD/MA/mom/VR/RS, D/W/M) | **513/514 daily-weekly; monthly MA-align UNAVAILABLE for 1 (LIN monthly block partial)** | technical_indicators.json, 517/518 OK incl. ETFs (L003) |
| Earnings dates | **66-symbol shortlist confirmed** (65 vendor-confirmed + DAL vendor-empty → cadence estimate ±5d) | Confirmed-dates preflight per 07-12 accepted Track B change (L015) |
| Fundamental family (revisions, margins, FCF, ROIC…) | **0/514 — UNAVAILABLE** | No wired feed at index-union scale; family zeroed, not imputed |
| Sentiment family (short interest, options skew, analyst tape…) | **0/514 — UNAVAILABLE** | Same; Enhancing-class → DQ 0.80 + LOW confidence, never a GO blocker |

Data-quality effect: DQ ×0.80 universe-wide (L020); with 2/4 families sourceable, **no name can meet evidence threshold #2 (3-of-4 non-negative families)** → investable set structurally empty; every published name is monitoring-sleeve.

## Technical Indicator Coverage (per timeframe)

TD-9, RSI(14), MACD(12,26,9), MA-alignment, 20/60-momentum, volume-ratio, RS-vs-SPY: **daily 514/514, weekly 514/514, monthly 514/514 computed**, except FDXF (all UNAVAILABLE, rejected) and isolated monthly MA-alignment gaps on short-history names (recorded UNAVAILABLE, e.g. LIN monthly alignment: UNAVAILABLE in L214 — displayed as such, never imputed).

## Earnings Penalty Roll (confirmed dates, plain ≤14d window; L015)

Inside the window from 2026-07-13 (≤ 2026-07-27): **BAC 07-14 (1d); PNC, MTB, MS, JBHT 07-15 (2d); STT, USB, CFG, UNH, GE 07-16 (3d); RF 07-17 (4d); KEY, GPC, IBKR 07-21 (8d); URI, NTRS, TDY, LUV, RJF 07-22 (9d); WST, AMP, EW 07-23 (10d); AXP 07-24 (11d); FFIV 07-27 (14d)** — 23 shortlist names carry -0.10. FFIV flipped INTO the window since Friday (was 15d, now exactly 14d) and keeps its rank-12 slot despite the penalty. DAL: vendor-empty post its 07-09 print → next estimated 2026-10-08 (±5d), outside the horizon, no penalty. Names with earnings 15-45d out (HUM 16d, FTNT 16d, MRNA/BEN/TROW 18d, AXON 21d, DVA/DOC/AIZ 22d, CRL/CVS 23d, DDOG/ABNB 24d, TTWO 25d, CSCO 30d, PANW 35d, CRWD 44d, BBY 45d) carry no penalty but are noted per-name in 05.

## Handoff to Factor Scoring

514 names, full risk/technical packs, confirmed earnings dates on the scored shortlist, carry-forward bindings from 02 §5 (LLY/ABBV/LIN/ANET in; UNH/GE event-excluded; 8 DROP names out). Percentile labeling INDEX_UNION_PCTL (n=514).
