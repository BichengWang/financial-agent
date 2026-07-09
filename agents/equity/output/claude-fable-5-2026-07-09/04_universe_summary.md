# 04 Universe Summary

## Construction

S&P 500 ∪ Nasdaq-100 index union via `build_index_universe.py` (normal daily path): **503 ∪ 101 − 89 overlap = 515 union** (universe_summary.json 2026-07-09T14:16:19Z; constituent caches fetched_at 2026-06-21T21:05:56Z — stale-cache note: refresh remains a maintenance task per rules.md §Index-Union Universe Protocol, logged not blocking). Sampled fallback **NOT** used. All percentiles labeled `INDEX_UNION_PCTL (n=513)`.

## Inclusion / Exclusion Log

| Filter | Result |
|---|---|
| 5y daily bars fetched (twice) | 521/521 OK both passes (L002) |
| Staleness (last bar ≥ prior session) | **SATS rejected** — no prints since 2026-07-02, standing structural exclusion (delisting/halt suspected, carried from 07-08) |
| Listing age / history depth (≥61 bars) | **FDXF rejected** — 30 bars since listing |
| Price > $5 | 0 rejects |
| 20d ADV > $20M | 0 rejects (index-union membership pre-filters liquidity) |
| Trading ≥80% of trailing-60 sessions | 0 further rejects |
| **Eligible universe** | **513** |

Market-cap filter (>$2B) is implied by index membership; bid-ask-spread and corporate-action screens are not directly observable without the tape (Enhancing inputs) — no evidence of violations among published names.

## Metric Coverage Summary

| Metric Group | Sourceable | UNAVAILABLE | DQ / Confidence Effect | GO Impact |
|---|---|---|---|---|
| Price/volume + derived risk (vol, beta, TE, DD, VaR/CVaR, Kelly) | 513 | 0 | — | Required — grounded |
| Technical indicator pack daily/weekly/monthly (TD-9, RSI14, MACD, MA, momentum, volume ratio, RS) | 513 (100% each timeframe) | 0 | — | Supports Tech_Z (≥70% sourceability rule satisfied) |
| Fundamental family | 0 | 513 | DQ 0.80; family 0.00; confidence LOW | Enhancing — not a GO blocker |
| Sentiment family | 0 | 513 | DQ 0.80; family 0.00; confidence LOW | Enhancing — not a GO blocker |
| Earnings dates | ~76-name shortlist, cadence est ±5d (INFERRED); 28 inside ≤19d buffered window | rest not evaluated | -0.10 inside window | Required input satisfied for published names |
| Risk-free rate | ^IRX 3.688% fresh print (L006) | — | ratios not RAW_DIAGNOSTIC | — |

Limitation (unchanged from 07-08): earnings estimates are evaluated for the ranked shortlist, not all 513 names; a non-shortlist name inside its earnings window could rank above a penalized shortlist name (e.g., AXP, rank 24, mid-July print not evaluated — excluded from near-miss commentary in 05 for that reason). The effect is conservative for published names: their percentiles are understated, never overstated.

## Technical Indicator Coverage (per timeframe, n=513)

TD-9 daily/weekly/monthly: 513/513/513. RSI(14): 513/513/513. MACD(12,26,9): 513/513/513. MA alignment, 20/60-bar momentum, 20-bar volume ratio, 20/60-bar relative strength vs SPY: 513 each (weekly/monthly blocks carried in `technical_indicators.json`). Source: technical_indicators.py --history-dir on the exact refetched bars (L003).
