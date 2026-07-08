# 03 Regime and Data

## Data Mode Declaration

**LIVE** — intraday prints fetched during the regular session (2026-07-06T16:36:52Z–2026-07-06T16:41:50Z, ~12:37–12:42 ET), 521/521 symbols OK (third consecutive zero-failure fetch), two-source verified (Nasdaq 2026-07-06T16:47:03Z, max divergence 0.327%) with IBKR brokerage MCP live corroboration on the core ETFs (2026-07-06T16:48:41Z, max divergence 0.049%, `is_close: false`). All five Required inputs grounded (see 00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names.

## Regime Classification: **NEUTRAL** (carried, now confirmed on a live tape)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | 15.91 — below 20d mean 18.13; 60d range 15.32–22.22 | L007-L009 |
| SPY vs MA20/MA50 | 750.67 above 740.75 / 738.21; daily MACD **BULLISH_CROSS** on today's live bar | L014, L022 |
| SPY momentum | mom20 -0.85% / mom60 +11.04% — flat near-term, strong trailing quarter | L019 |
| SPY intraday | +0.79% vs 2026-07-02 close | L011 |
| Rates (TLT) | 20d -0.23% / 60d -1.86% — no rate shock | L010 |
| ^IRX | 3.693% (fresh 2026-07-06 print) | L006 |

Not BULL (mom20 still negative, VIX only mid-range); not HIGH_VOL (VIX 15.9 vs the June 22 peak); no RATE_SHOCK (TLT quiet). **NEUTRAL** with a risk-on tilt today: QQQ -2.2%/20d relative strength -1.33% and SOXX intraday +4.0% suggest growth re-risking; watch for BULL confirmation if SPY mom20 turns positive with VIX < 16.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 750.67 | 2026-07-06 | LIVE | ABOVE MA20 740.75 / MA50 738.21 | 14.9% (prev 10.5%) | 1.000 | +0.50% | 4.3% | REALIZED_VOL_30D | 754.42 | 2026-08-03 | 720.78 | 788.07 | MEDIUM | L013-L023 |
| QQQ | 724.45 | 2026-07-06 | LIVE | ABOVE MA20 720.30 / MA50 710.54 | 28.9% (prev 15.7%) | 1.658 | +0.83% | 8.3% | REALIZED_VOL_30D | 730.46 | 2026-08-03 | 667.70 | 793.22 | MEDIUM | L024-L034 |
| SOXX | 589.15 | 2026-07-06 | LIVE | ABOVE MA20 597.11 / MA50 548.78 | 74.5% (prev 40.8%) | 3.410 | +1.71% | 21.5% | REALIZED_VOL_30D | 599.22 | 2026-08-03 | 467.43 | 731.02 | LOW | L035-L045 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.658 x 0.5% = **+0.83%**, no relative-view adjustment. SOXX = beta 3.410 x 0.5% = **+1.71%**, no adjustment (the +4.0% intraday semis pop is one session, not a ledger-backed relative view). Confidence: SPY/QQQ MEDIUM (default; trend and vol aligned but 20d momentum still negative); SOXX LOW (30d rvol 74% vs prior 41%, -13.5% from 60d high — vol regime not aligned with the NEUTRAL call).

Relative strength: QQQ/SPY 20d -1.33% / 60d +8.49%; SOXX/SPY 20d -1.40% / 60d +48.02% (ledger L031, L042). Consistency check: 60d leadership in QQQ/SOXX with flat-to-negative 20d RS matches a NEUTRAL regime digesting a strong quarter — no contradiction with the classification.

## Event Concentration

- **Earnings season opens inside the horizon**: 32 of the top-ranked names carry cadence-estimated reports inside the <=19d buffered window (banks/airlines cluster 07-09..07-17; industrials/REITs 07-21..07-24). All 32 carry the -0.10 penalty; DAL (est 2026-07-09, ~3d) is the nearest event in the published sleeve.
- **FOMC**: next scheduled meeting 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- SATS excluded (stale last bar 2026-07-02 — no prints in today's session at fetch time); FDXF excluded (27 bars since listing).

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-06T16:36:26Z); **513 eligible** after screens (rejects: SATS stale, FDXF short history). Handed to technical_indicators.py: 513 + SPY/QQQ/SOXX (+TLT/^VIX/^IRX macro series fetched alongside). INDEX_UNION_PCTL (n=513); sampled fallback NOT used.
