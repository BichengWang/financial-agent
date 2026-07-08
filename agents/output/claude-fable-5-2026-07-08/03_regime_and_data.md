# 03 Regime and Data

## Data Mode Declaration

**LIVE** — intraday prints fetched during the regular session (2026-07-08T17:46:59Z–17:48:35Z ≈ 13:47–13:49 ET), 521/521 symbols OK (**fifth consecutive zero-failure fetch**, 8-worker threaded), two-source verified (Nasdaq 2026-07-08T17:55:03Z–17:55:20Z, max divergence 0.28% (GOOGL)) with IBKR brokerage MCP live corroboration on the core ETFs (2026-07-08T17:54:28Z–17:54:43Z, max divergence 0.163%, `is_close: false`). All five Required inputs grounded (see 00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names.

## Regime Classification: **NEUTRAL** (carried; index steady while growth/semis digest)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | 16.66 — below 20d mean 17.73; 60d range 15.32–22.22 | L007–L008 |
| SPY vs MA20/MA50 | 744.34 above 741.55 / 739.62; daily MACD ABOVE_SIGNAL | L010–L011 |
| SPY momentum | mom20 +0.69% / mom60 +9.55% | L012 |
| SPY intraday | -0.45% vs 2026-07-07 close | L010 |
| Rates (TLT) | 20d -0.35% / 60d -2.51% — no rate shock | L009 |
| ^IRX | 3.725% (fresh 2026-07-08 print) | L006 |

Not BULL (QQQ 708.55 below its MA20 720.06; SOXX -14.6% from its 60d high on 77% annualized 30d vol — the growth complex is still correcting inside a flat index); not HIGH_VOL (VIX 16.7, below its 20d mean and mid-range); no RATE_SHOCK (TLT quiet). **NEUTRAL** for the third consecutive live session. Internal rotation update: yesterday's -7.0% SOXX break is bouncing +1.42% intraday today while SPY sits -0.45% — a dead-cat stabilization, not repaired leadership (SOXX remains 6.2% below its MA20; QQQ/SPY 20d RS -1.73%). The defensive/low-beta leadership in the cross-section (DVA, BEN, TROW, STT at the top of 05) is intact.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 744.34 | 2026-07-08 | LIVE | ABOVE MA20 741.55 / MA50 739.62 | 15.3% (prev 10.6%) | 1.000 | +0.50% | 4.4% | REALIZED_VOL_30D | 748.06 | 2026-08-05 | 714.00 | 782.12 | MEDIUM | L010–L016, L033 |
| QQQ | 708.55 | 2026-07-08 | LIVE | BELOW MA20 720.06 / ABOVE MA50 712.56 (marginal) | 29.7% (prev 16.0%) | 1.664 | +0.83% | 8.6% | REALIZED_VOL_30D | 714.43 | 2026-08-05 | 651.06 | 777.80 | MEDIUM | L017–L023, L034 |
| SOXX | 559.51 | 2026-07-08 | LIVE | BELOW MA20 596.73 / ABOVE MA50 552.80 | 76.9% (prev 41.4%) | 3.413 | +1.71% | 22.2% | REALIZED_VOL_30D | 569.07 | 2026-08-05 | 439.89 | 698.25 | LOW | L024–L030, L035 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.664 × 0.5% = **+0.83%**, no relative-view adjustment. SOXX = beta 3.413 × 0.5% = **+1.71%**, no adjustment (today's +1.4% bounce after yesterday's -7.0% break is two sessions of chop, not a ledger-backed relative view). Confidence: SPY MEDIUM (trend aligned, vol elevated vs prior window); QQQ MEDIUM (mixed — below MA20 on near-doubled vol); SOXX LOW (30d rvol 77% vs prior 41%, -14.6% from 60d high — vol regime not aligned with the NEUTRAL call).

Relative strength: QQQ/SPY 20d **-1.73%** / 60d +5.85%; SOXX/SPY 20d **-2.76%** / 60d +32.11% (L031–L032). Consistency check: strong 60d growth/semis leadership decaying to *negative* on the 20d window is exactly a NEUTRAL regime digesting an extended quarter — no contradiction with the classification; the 20d RS signs flipped negative today for the first time this window, worth watching as a BEAR-rotation early warning.

## Event Concentration

- **Q2 earnings season opens tomorrow**: DAL (est 2026-07-09, ~1d) is first; the banks/financials cluster follows 07-14..07-17 (JPM, BAC, MS, STT, USB, FITB, HBAN, CFG, IBKR, PGR est), airlines 07-16..07-23 (UAL, LUV). **34 of the 80-name estimate shortlist sit inside the ≤19d buffered window** and carry the -0.10 penalty — this is what keeps STT (7d), WST (15d), UNH (7d), DAL (1d), UAL (8d), FFIV (19d), DOC (16d) out of or down-ranked in the published sleeve.
- **FOMC**: 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- **SATS**: third consecutive session with no prints (last bar 2026-07-02) — per the 07-07 evolution note this is now logged as a **structural exclusion (delisting/halt suspected)**, not a daily staleness reject; see 13. FDXF excluded (29 bars since listing).

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-08T17:40:47Z); **513 eligible** after screens (rejects: SATS structural-stale, FDXF short history). Handed to technical_indicators.py: 513 + SPY/QQQ/SOXX (+TLT/^VIX/^IRX macro series fetched alongside; 518 indicator records produced). INDEX_UNION_PCTL (n=513); sampled fallback NOT used.
