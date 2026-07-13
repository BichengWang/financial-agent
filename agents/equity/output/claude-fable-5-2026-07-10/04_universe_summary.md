# 04 Universe Summary

## Construction

S&P 500 ∪ Nasdaq-100 index union via `build_index_universe.py` (normal daily path): **503 ∪ 101 − 89 overlap = 515 union** (universe_summary.json 2026-07-10T21:47:35Z; constituent caches fetched_at 2026-06-21T21:05:56Z — stale-cache note: refresh remains a maintenance task per rules.md §Index-Union Universe Protocol, logged not blocking). Sampled fallback **NOT** used. All percentiles labeled `INDEX_UNION_PCTL (n=512)`.

## Inclusion / Exclusion Log

| Filter | Result |
|---|---|
| 5y daily bars available through the 07-10 close | 517/519 fetch-repaired (L002); Yahoo bulk throttled — Nasdaq official-close tail repair path per 01 header |
| Staleness (last bar = run date) | **SATS rejected** — no prints since 2026-07-02, standing structural exclusion (carried from 07-08). **BF-B rejected** — Nasdaq vendor gap on /info and /chart (attempts 2026-07-11T01:55Z/02:05Z documented); last bar 07-09 |
| Listing age / history depth (≥61 bars) | **FDXF rejected** — 31 bars since listing |
| Price > $5 | 0 rejects |
| 20d ADV > $20M | 0 rejects (index-union membership pre-filters liquidity) |
| Trading ≥80% of trailing-60 sessions | 0 further rejects |
| **Eligible universe** | **512** |

Market-cap filter (>$2B) is implied by index membership; bid-ask-spread and corporate-action screens are not directly observable without the tape (Enhancing inputs). Corporate-action integrity was actively checked this run: the Nasdaq tail repair compared implied prior closes and official chart closes against the inherited series — zero unexplained discontinuities beyond the documented intraday-print correction (chart_repair_manifest.json).

## Metric Coverage Summary

| Metric Group | Sourceable | UNAVAILABLE | DQ / Confidence Effect | GO Impact |
|---|---|---|---|---|
| Price/volume + derived risk (vol, beta, TE, DD, VaR/CVaR, Kelly) | 512 | 0 | — | Required — grounded |
| Technical indicator pack daily/weekly/monthly (TD-9, RSI14, MACD, MA, momentum, volume ratio, RS) | 512 (100% each timeframe) | 0 | — | Supports Tech_Z (≥70% sourceability rule satisfied) |
| Fundamental family | 0 | 512 | DQ 0.80; family 0.00; confidence LOW | Enhancing — not a GO blocker |
| Sentiment family | 0 | 512 | DQ 0.80; family 0.00; confidence LOW | Enhancing — not a GO blocker |
| Earnings dates | **384-name cadence-estimate map (±5d, INFERRED); 179 inside ≤19d buffered window penalized -0.10** | 128 not evaluated | -0.10 inside window | Required input satisfied for published names |
| Risk-free rate | ^IRX 3.682% (07-09 close, 1d lag disclosed, L006) | — | ratios not RAW_DIAGNOSTIC | — |

Coverage improvement vs 07-09: the earnings-estimate map grew from ~76 shortlist names to **384 of 512** (75%), directly addressing the prior run's 08 concern #2 (AXP-class blind spots). Residual limitation: 128 names (mostly lower-liquidity index members) still lack estimates; a non-evaluated name inside its window could rank above a penalized name. Every published name has an evaluated estimate — the effect on the published sleeve remains conservative.

## Technical Indicator Coverage (per timeframe, n=512)

TD-9 daily/weekly/monthly: 512/512/512. RSI(14): 512/512/512. MACD(12,26,9): 512/512/512. MA alignment, 20/60-bar momentum, 20-bar volume ratio, 20/60-bar relative strength vs SPY: 512 each (weekly/monthly blocks carried in `technical_indicators.json`). Source: technical_indicators.py --history-dir on the repaired official-close bars (L003). Unlike 07-09, every daily bar in the indicator windows is a full-session official print (no partial-bar caveat).
