# 03 Regime and Data

## Data Mode Declaration

**DELAYED** — U.S. markets are closed today (**Saturday 2026-07-11**); the freshest completed session is Friday 2026-07-10, and every price used downstream is that session's official close (≤1-day lag vs the last completed session — same declaration class as the 07-04/07-05 weekend-precedent runs). Sourcing chain per 01 header: Yahoo v8 bulk remains IP-throttled (HTTP 429; documented attempts this session) → **inherited 2026-07-10 repaired 5y series** (Yahoo 07-09 refetch + Nasdaq official-close tail repair, provenance in the 07-10 package's 01/L002) + **current-run Nasdaq /chart re-verification of the full 07-06..07-10 window: 517/519 symbols, max divergence 0.0000%** (nasdaq_verification_manifest.json, retrieved 2026-07-11T16:03–16:11Z) + IBKR brokerage MCP closed-market snapshots reproducing the 07-09 closes exactly (SPY 751.71 / QQQ 723.28 / SOXX 581.70, `is_close: true`; VIX index snapshot empty with the market closed — attempt documented). All five Required inputs grounded (00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names. Weekend rule: no executable session → **status target REVIEW_ONLY** regardless of data eligibility (07-03/07-04/07-05 precedent).

## Regime Classification: **NEUTRAL** (carried, sixth consecutive session; unchanged from the 07-10 close — no session has elapsed)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | **15.03** — 60d low; -6.2% on 07-10; below 20d mean 17.19; 60d range [15.03, 22.22] | L007–L008 |
| SPY vs MA20/MA50 | 754.95 above 743.81 / 741.24 (record close) | L010–L011 |
| SPY momentum | mom20 +4.07% / mom60 +8.71% | L012 |
| Rates (TLT) | 20d -0.48% / 60d -3.14% — no rate shock | L009 |
| ^IRX | 3.682% (2026-07-09 close, 2d lag disclosed — no 07-10/07-11 index print fetchable: Nasdaq/IBKR lack ^IRX; Yahoo throttled) | L006 |

Not BULL yet: SOXX remains **below its MA20** (581.34 vs 599.82, -11.25% from its 60d high) on a 75.5% annualized 30d vol regime (prior window 44.3%), and QQQ 30d vol is still ~2x its prior window (29.7% vs 16.0%) — index-level trend intact, growth complex digesting rather than leading. Not HIGH_VOL: VIX at a 60d low with a falling 20d mean; realized vol elevated only in the growth sleeves. No RATE_SHOCK (TLT quiet both windows). **NEUTRAL** — SPY in trend at a record close with compressed implied vol, an elevated-vol growth complex beneath. Internal rotation unchanged from Friday: QQQ/SPY 20d RS +0.52% and SOXX/SPY 20d RS +3.29% (60d: +6.71% / +36.18%), while the cross-sectional leaderboard stays defensive/low-vol. This weekend run re-reads Friday's tape; the regime call can only change on Monday's session.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 754.95 | 2026-07-10 | DELAYED | ABOVE MA20 743.81 / ABOVE MA50 741.24 | 15.4% (prev 10.1%) | 1.000 | +0.50% | 4.4% | REALIZED_VOL_30D | 758.72 | 2026-08-08 | 724.18 | 793.27 | MEDIUM | L010–L016, L033 |
| QQQ | 725.51 | 2026-07-10 | DELAYED | ABOVE MA20 722.57 / ABOVE MA50 715.16 | 29.7% (prev 16.0%) | 1.684 | +0.84% | 8.6% | REALIZED_VOL_30D | 731.60 | 2026-08-08 | 666.71 | 796.49 | MEDIUM | L017–L023, L034 |
| SOXX | 581.34 | 2026-07-10 | DELAYED | BELOW MA20 599.82 / ABOVE MA50 558.23 | 75.5% (prev 44.3%) | 3.518 | +1.76% | 21.8% | REALIZED_VOL_30D | 591.57 | 2026-08-08 | 459.77 | 723.37 | LOW | L024–L030, L035 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.684 × 0.5% = **+0.84%**, no relative-view adjustment. SOXX = beta 3.518 × 0.5% = **+1.76%**, no adjustment (positive 20d RS on a 75.5%-vol regime is not a ledger-backed relative view). Confidence: SPY MEDIUM (trend aligned; realized vol 1.5x its prior window against a compressed VIX); QQQ MEDIUM (above both MAs on ~2x prior-window vol); SOXX LOW (below MA20, vol regime 1.7x prior window, 11.3% off the 60d high — not aligned with the NEUTRAL call). Target date = run_date + 28d = 2026-08-08.

Relative strength: QQQ/SPY 20d **+0.52%** / 60d +6.71%; SOXX/SPY 20d **+3.29%** / 60d +36.18% (L031–L032). Consistency check: index trend + positive-but-decelerating growth leadership + compressed VIX is NEUTRAL-consistent; the SOXX vol regime is the one dissenting input, reflected in its LOW confidence.

## Event Concentration

- **Q2 earnings season is the dominant 2-week event surface.** Fresh full-universe earnings-date fetch this run (api.nasdaq.com /analyst/{sym}/earnings-date; Zacks expected dates + Nasdaq cadence-algorithm estimates — earnings_calendar_manifest.json). The banks/financials cluster lands 07-14..07-17 (JPM 07-14 confirmed; BAC/C/WFC/GS/MS/BLK/UNH wave 07-15; regionals 07-16..07-17), holding several otherwise-top-decile financials out of the published sleeve on the -0.10 window penalty. Airlines/industrials wave 07-16..07-23; mega-cap tech est 07-28..07-30. Counts and the per-name penalty roll are in 04/05.
- **FOMC**: 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- **SATS**: no prints since 2026-07-02 — standing structural exclusion (delisting/halt suspected, carried since 07-08). **BF-B**: Nasdaq vendor gap persists (no /chart data returned this run — nasdaq_verification_manifest.json failures); stale-bar exclusion carried from 07-10. **FDXF**: excluded (31 bars since listing, <60 minimum).

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-11T12:55:19Z); **512 eligible** after screens (rejects: SATS structural-stale, BF-B stale-bar/vendor-gap, FDXF short history — full rejection log in 04). Handed to technical_indicators.py: 515 universe + SPY/QQQ/SOXX + TLT/^VIX/^IRX macro series → **521 indicator records, 520 OK** (FDXF UNAVAILABLE, short history), generated_at 2026-07-11T16:28:28Z. INDEX_UNION_PCTL (n=512); sampled fallback NOT used.
