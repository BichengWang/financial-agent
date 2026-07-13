# 03 Regime and Data

## Data Mode Declaration

**DELAYED** — official 2026-07-10 closing prints fetched post-close this run (≤1-day lag; same declaration class as the 07-03/07-04 precedent runs). Sourcing chain per 01 header: Yahoo v8 bulk was IP-throttled (HTTP 429, three documented attempts) → inherited 2026-07-09 Yahoo 5y refetch + **Nasdaq official-close tail repair 07-06..07-10** (517/519 symbols; retrieved 2026-07-11T02:05–02:11Z) + IBKR brokerage MCP corroboration on core ETFs and VIX (max divergence 0.244%, after-hours drift). Two-source verification universe-wide: max 0.005% on completed overlap sessions (L005). All five Required inputs grounded (00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names. DELAYED mode is GO-eligible at reduced exposure per rules.md §Data Mode Taxonomy — the block to GO today is the family-coverage evidence threshold, not data (see 00/05).

## Regime Classification: **NEUTRAL** (carried, fifth consecutive session; vol compressing, growth complex still digesting)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | **15.03** — new 60d low; -6.2% vs 07-09 Yahoo close 16.03; below 20d mean 17.19; 60d range [15.03, 22.22] | L007–L008 |
| SPY vs MA20/MA50 | 754.95 above 743.81 / 741.24 | L010–L011 |
| SPY momentum | mom20 +4.07% / mom60 +8.71% | L012 |
| SPY day | +0.43% (record close on official prints) | L010 |
| Rates (TLT) | 20d -0.48% / 60d -3.14% — no rate shock | L009 |
| ^IRX | 3.682% (2026-07-09 close, 1d lag disclosed) | L006 |

Not BULL yet: SOXX remains **below its MA20** (581.34 vs 599.82, -11.25% from its 60d high) on a 75.5% annualized 30d vol regime (prior window 44.3%), and QQQ 30d vol is still ~2x its prior window (29.7% vs 16.0%) — trend is intact at the index level but the growth complex is digesting, not leading. Not HIGH_VOL: VIX printed a fresh 60d low at 15.03, its 20d mean is falling (17.19), and realized index vol is elevated only in the growth sleeves. No RATE_SHOCK (TLT quiet both windows). **NEUTRAL** — SPY in trend at a record close with compressing implied vol, an elevated-vol growth complex beneath. Internal rotation: yesterday's repair extended — QQQ/SPY 20d RS +0.52% and SOXX/SPY 20d RS +3.29% both positive for a second session (60d: +6.71% / +36.18%), while the cross-sectional leaderboard stays defensive/low-vol (DVA #1 third straight day; asset managers and insurers dense in the top-15). SOXX's flat close (-0.06%) against SPY +0.43% on a VIX-crush day is consistent with digestion, not renewed leadership.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 754.95 | 2026-07-10 | DELAYED | ABOVE MA20 743.81 / ABOVE MA50 741.24 | 15.4% (prev 10.1%) | 1.000 | +0.50% | 4.4% | REALIZED_VOL_30D | 758.72 | 2026-08-07 | 723.83 | 793.62 | MEDIUM | L010–L016, L033 |
| QQQ | 725.51 | 2026-07-10 | DELAYED | ABOVE MA20 722.57 / ABOVE MA50 715.16 | 29.7% (prev 16.0%) | 1.684 | +0.84% | 8.6% | REALIZED_VOL_30D | 731.60 | 2026-08-07 | 666.89 | 796.32 | MEDIUM | L017–L023, L034 |
| SOXX | 581.34 | 2026-07-10 | DELAYED | BELOW MA20 599.82 / ABOVE MA50 558.23 | 75.5% (prev 44.3%) | 3.518 | +1.76% | 21.8% | REALIZED_VOL_30D | 591.57 | 2026-08-07 | 459.81 | 723.33 | LOW | L024–L030, L035 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.684 × 0.5% = **+0.84%**, no relative-view adjustment. SOXX = beta 3.518 × 0.5% = **+1.76%**, no adjustment (two sessions of positive 20d RS on a 75.5%-vol regime is not a ledger-backed relative view). Confidence: SPY MEDIUM (trend aligned; realized vol still 1.5x its prior window against a falling VIX); QQQ MEDIUM (above both MAs on ~2x prior-window vol); SOXX LOW (below MA20, vol regime 1.7x prior window, 11.3% off the 60d high — not aligned with the NEUTRAL call).

Relative strength: QQQ/SPY 20d **+0.52%** / 60d +6.71%; SOXX/SPY 20d **+3.29%** / 60d +36.18% (L031–L032). Consistency check: index trend + positive-but-decelerating 60d growth leadership + compressing VIX is NEUTRAL-consistent; the SOXX vol regime is the one dissenting input and is reflected in its LOW confidence.

## Event Concentration

- **Q2 earnings season is the dominant 2-week event surface**: with cadence estimates now maintained for 384 of 512 names, **179 names sit inside the ≤19d buffered window** and carry the -0.10 penalty. The banks/financials cluster lands 07-14..07-17 (JPM 07-14; BAC/C/WFC/GS/MS/STT/BNY/BLK/PGR/UNH est 07-15; PNC/USB/MTB/NTRS/CFG est 07-16; AXP/SCHW/TRV/SLB + regionals est 07-17) — this cluster alone holds STT (5d), UNH (5d), and BNY (5d) out of the published sleeve. Airlines/industrials wave 07-16..07-23 (UAL, LUV, GE, TXN, URI); mega-cap tech 07-28..07-30 (MSFT/GOOGL est 07-28, META est 07-29, AAPL/AMZN est 07-30). DAL reported 2026-07-09 — its event risk is cleared to October and it enters the sleeve un-penalized at #6.
- **FOMC**: 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- **SATS**: no prints since 2026-07-02 — standing structural exclusion (delisting/halt suspected, carried since 07-08). **BF-B**: new today — Nasdaq vendor gap on both /info and /chart endpoints (documented attempts 01:55Z/02:05Z); no 07-10 print obtainable → stale-bar exclusion for this run only. FDXF excluded (31 bars since listing).

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-10T21:47:35Z); **512 eligible** after screens (rejects: SATS structural-stale, BF-B stale-bar/vendor-gap, FDXF short history). Handed to technical_indicators.py: 512 + SPY/QQQ/SOXX (+TLT/^VIX macro series; ^IRX carried at 07-09 close): 518 indicator records produced, 517 OK, generated_at 2026-07-11T02:13:36Z. INDEX_UNION_PCTL (n=512); sampled fallback NOT used.
