# 03 Regime and Data

## Data Mode Declaration

**LIVE** — intraday prints fetched during the regular session. Universe fetched twice: 2026-07-09T14:30:05Z–14:47:49Z (~10:47 ET) and refetched 2026-07-09T18:36:05Z–18:36:18Z (~14:36 ET) after the first pass drifted up to 3.06% vs the independent cross-check source across ~4 intraday hours; **all downstream values use the refetch**. Both passes 521/521 OK (sixth and seventh consecutive zero-failure fetches, 8-worker threaded). Two-source verified: Nasdaq last-sale 2026-07-09T18:36:22Z–18:36:23Z, max divergence 0.121% (TTWO) across all 40 published/settled/ETF symbols; IBKR brokerage MCP live corroboration on the core ETFs (2026-07-09T18:36:41Z, max divergence 0.008%, `is_close: false`). All five Required inputs grounded (see 00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names.

## Regime Classification: **NEUTRAL** (carried, fourth consecutive live session; growth complex repairing intraday)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | 16.03 — below 20d mean 17.55; 60d range 15.32–22.22 | L007–L008 |
| SPY vs MA20/MA50 | 751.17 above 742.31 / 740.36 | L010–L011 |
| SPY momentum | mom20 +1.92% / mom60 +9.48% | L012 |
| SPY intraday | +0.92% vs 2026-07-08 close (744.34) | L010, 07-08 ledger |
| Rates (TLT) | 20d -0.65% / 60d -2.52% — no rate shock | L009 |
| ^IRX | 3.688% (fresh 2026-07-09 print) | L006 |

Not BULL yet: the growth complex is repairing, not repaired — SOXX +4.9% intraday to 586.71 but still 10.4% off its 60d high on 74.7% annualized 30d vol (prior window 43.1%), and QQQ only reclaimed its MA20 intraday today (723.25 vs 720.97). Not HIGH_VOL (VIX 16.0, below its 20d mean, lower quartile of the 60d range); no RATE_SHOCK (TLT quiet). **NEUTRAL** — an index in trend with an elevated-vol growth complex digesting beneath it. Internal rotation update: yesterday's "dead-cat or repair?" question resolved toward repair today — SOXX/SPY 20d RS +2.46% and QQQ/SPY 20d RS +0.26% both flipped back positive (yesterday: -2.76% / -1.73%), the BEAR-rotation early warning did not follow through. The defensive/low-beta cross-sectional leadership (DVA, TROW, BEN, PRU at the top of 05) is intact but security software (FTNT, PANW, CRWD) and select high-beta momentum re-strengthened today.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 751.17 | 2026-07-09 | LIVE | ABOVE MA20 742.31 / ABOVE MA50 740.36 | 15.1% (prev 10.3%) | 1.000 | +0.50% | 4.3% | REALIZED_VOL_30D | 754.93 | 2026-08-06 | 720.97 | 788.88 | MEDIUM | L010–L016, L033 |
| QQQ | 723.25 | 2026-07-09 | LIVE | ABOVE MA20 720.97 / ABOVE MA50 713.80 (both marginal-to-firm intraday) | 29.2% (prev 16.1%) | 1.682 | +0.84% | 8.4% | REALIZED_VOL_30D | 729.33 | 2026-08-06 | 665.93 | 792.73 | MEDIUM | L017–L023, L034 |
| SOXX | 586.71 | 2026-07-09 | LIVE | BELOW MA20 598.08 / ABOVE MA50 555.48 | 74.7% (prev 43.1%) | 3.482 | +1.74% | 21.6% | REALIZED_VOL_30D | 596.92 | 2026-08-06 | 465.36 | 728.49 | LOW | L024–L030, L035 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.682 × 0.5% = **+0.84%**, no relative-view adjustment. SOXX = beta 3.482 × 0.5% = **+1.74%**, no adjustment (today's +4.9% bounce is one session against a 74.7%-vol backdrop — not a ledger-backed relative view). Confidence: SPY MEDIUM (trend aligned, vol elevated vs prior window); QQQ MEDIUM (reclaimed MA20 intraday on near-doubled vol); SOXX LOW (vol regime 1.7x its prior window and 10.4% off the 60d high — not aligned with the NEUTRAL call).

Relative strength: QQQ/SPY 20d **+0.26%** / 60d +7.66%; SOXX/SPY 20d **+2.46%** / 60d +39.68% (L031–L032). Consistency check: 60d growth/semis leadership decayed to flat-positive on the 20d window and re-accelerated intraday today — consistent with NEUTRAL-regime digestion resolving upward; yesterday's negative 20d RS flip reversed rather than extended.

## Event Concentration

- **Q2 earnings season opened this morning**: DAL reported pre-market today (2026-07-09) — its live bar embeds the print; DAL remains in the published sleeve at rank 14 with the -0.10 event penalty and its entry price reflecting the post-print tape. The banks/financials cluster lands 07-14..07-17 (JPM, BAC, MS, STT, USB, BNY, IBKR, PGR est), airlines 07-16..07-23 (UAL, LUV). **28 of the ~76-name estimate shortlist sit inside the ≤19d buffered window** and carry the -0.10 penalty — this holds STT (6d), UNH (6d), BNY (6d), IBKR (5d), JBHT (6d), MS (6d), UAL (7d), GE (13d), GL (13d), EW (14d), TXN (12d), URI (13d) and others out of or down-ranked in the published sleeve.
- **FOMC**: 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- **SATS**: no prints since 2026-07-02 — standing structural exclusion (delisting/halt suspected, logged 07-08). FDXF excluded (30 bars since listing).

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-09T14:16:19Z); **513 eligible** after screens (rejects: SATS structural-stale, FDXF short history). Handed to technical_indicators.py: 513 + SPY/QQQ/SOXX (+TLT/^VIX/^IRX macro series fetched alongside; 518 indicator records produced, generated_at 2026-07-09T18:36:52Z). INDEX_UNION_PCTL (n=513); sampled fallback NOT used.
