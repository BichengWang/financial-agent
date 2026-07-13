# 03 Regime and Data

## Data Mode Declaration

**DELAYED** — U.S. markets are closed today (**Sunday 2026-07-12**); the freshest completed session is Friday 2026-07-10, and every price used downstream is that session's official close fetched this run (≤1-day lag vs the last completed session — same declaration class as the 07-04/07-05/07-11 weekend-precedent runs). Sourcing chain per 01 header: **Yahoo v8 threaded fetch 521/521 OK, zero failures** (2026-07-12T12:29:10Z–12:29:55Z — the 07-11 IP throttling did not recur) + **Nasdaq /quote chart cross-check on all 24 published names + SPY/QQQ/SOXX: divergence 0.0000% on all 27** (retrieved 12:54–12:55Z, nasdaq_verification_manifest.json) + IBKR brokerage MCP closed-market snapshots reproducing the 2026-07-09 closes exactly (SPY 751.71 / QQQ 723.28 / SOXX 581.70, `is_close: true` — fourth consecutive reproduction of this closed-market lag behavior; consistency check on prior records, not corroboration of today's entries). All five Required inputs grounded (00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names. Weekend rule: no executable session → **status target REVIEW_ONLY** regardless of data eligibility (07-03/07-04/07-05 precedent).

## Regime Classification: **NEUTRAL** (carried, seventh consecutive session label; unchanged from the 07-10 close — no session has elapsed since Friday)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | **15.03** — 60d low; below 20d mean 17.19; 60d range [15.03, 22.22] | L007–L009 |
| SPY vs MA20/MA50 | 754.95 above 743.81 / 741.24 (record close) | L013–L014 |
| SPY momentum | mom20 +4.07% / mom60 +8.71% | L019 |
| Rates (TLT) | 20d -0.48% / 60d -3.14% — no rate shock | L010 |
| ^IRX | 3.695% (fresh 2026-07-10 print) | L006 |

Not BULL yet: SOXX remains **below its MA20** (581.34 vs 599.82, -11.25% from its 60d high) on a 75.5% annualized 30d vol regime (prior window 44.3%), and QQQ 30d vol is still ~1.9x its prior window (29.7% vs 16.0%) — index-level trend intact, growth complex digesting rather than leading. Not HIGH_VOL: VIX at a 60d low with a falling 20d mean; realized vol elevated only in the growth sleeves. No RATE_SHOCK (TLT quiet both windows). **NEUTRAL** — SPY in trend at a record close with compressed implied vol, an elevated-vol growth complex beneath. Internal rotation unchanged from Friday: QQQ/SPY 20d RS +0.52% and SOXX/SPY 20d RS +3.29% (60d: +6.71% / +36.18%), while the cross-sectional leaderboard stays defensive/low-vol with a security-software momentum block. Today's settlement evidence is regime-consistent: the vintage's raw-return HITs on SPY/QQQ and MISS on SOXX mirror index-trend-up / semis-chop. This weekend run re-reads Friday's tape; the regime call can only change on Monday's session.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 754.95 | 2026-07-10 | DELAYED | ABOVE MA20 743.81 / ABOVE MA50 741.24 | 15.4% (prev 10.1%) | 1.000 | +0.50% | 4.4% | REALIZED_VOL_30D | 758.72 | 2026-08-09 | 723.86 | 793.59 | MEDIUM | L013–L023 |
| QQQ | 725.51 | 2026-07-10 | DELAYED | ABOVE MA20 722.57 / ABOVE MA50 715.16 | 29.7% (prev 16.0%) | 1.684 | +0.84% | 8.6% | REALIZED_VOL_30D | 731.60 | 2026-08-09 | 666.87 | 796.34 | MEDIUM | L024–L034 |
| SOXX | 581.34 | 2026-07-10 | DELAYED | BELOW MA20 599.82 / ABOVE MA50 558.23 | 75.5% (prev 44.3%) | 3.518 | +1.76% | 21.8% | REALIZED_VOL_30D | 591.57 | 2026-08-09 | 459.83 | 723.31 | LOW | L035–L045 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.684 × 0.5% = **+0.84%**, no relative-view adjustment. SOXX = beta 3.518 × 0.5% = **+1.76%**, no adjustment (positive 20d RS on a 75.5%-vol regime is not a ledger-backed relative view; today's settled SOXX MISS at mu +1.84% argues against any positive tilt). Confidence: SPY MEDIUM (trend aligned; realized vol 1.5x its prior window against a compressed VIX); QQQ MEDIUM (above both MAs on ~1.9x prior-window vol); SOXX LOW (below MA20, vol regime 1.7x prior window, 11.3% off the 60d high — not aligned with the NEUTRAL call). Target date = run_date + 28d = 2026-08-09.

Relative strength: QQQ/SPY 20d **+0.52%** / 60d +6.71%; SOXX/SPY 20d **+3.29%** / 60d +36.18% (SOXX/QQQ ledger rows L031/L042-class rows in 01). Consistency check: index trend + positive-but-decelerating growth leadership + compressed VIX is NEUTRAL-consistent; the SOXX vol regime is the one dissenting input, reflected in its LOW confidence. First settled MARKET_FORECAST records (02 §0) score the prior sleeve 2 HIT / 1 MISS, all IN_CI.

## Event Concentration

- **Q2 earnings season is the dominant 2-week event surface — and this run upgrades from cadence estimates to confirmed dates** (api.nasdaq.com earnings-date endpoint, 66 shortlist symbols fetched 2026-07-12T12:43Z, earnings_calendar_manifest.json in the run's fetch artifacts). The banks/financials cluster is confirmed 07-14..07-17: BAC 07-14; PNC/MTB/MS/UAL 07-15; STT/USB/UNH/GE 07-16; RF 07-17. The confirmed dates materially reshape the penalty roll vs prior estimates: **GE confirmed 07-16 (est was ~07-22)** and **UNH confirmed 07-16** stay event-excluded; **FFIV confirmed 07-27 (15d) clears the window** the ±5d cadence buffer had penalized it under.
- **FOMC**: 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- **SATS**: Yahoo now returns a single stale bar — standing structural exclusion carried (delisting/halt suspected, since 07-08). **FDXF**: excluded (31 bars since listing, <60 minimum). **BF-B**: yesterday's Nasdaq vendor gap did not recur — full 5y series fetched cleanly this run; the name re-enters the eligible universe.

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-12T12:28:18Z); **513 eligible** after screens (rejects: SATS structural-stale, FDXF short history — full rejection log in 04; BF-B re-admitted). Handed to technical_indicators.py: 515 universe + SPY/QQQ/SOXX + TLT/^VIX/^IRX macro series → **521 indicator records, 519 OK** (SATS/FDXF UNAVAILABLE, short history), generated_at 2026-07-12T12:30:39Z. INDEX_UNION_PCTL (n=513); sampled fallback NOT used.
