# 03 Regime and Data

## Data Mode Declaration

**LIVE** — intraday prints fetched during the regular session (2026-07-07T15:52:47Z–16:02:07Z, ~11:53–12:02 ET), 521/521 symbols OK (fourth consecutive zero-failure fetch), two-source verified (Nasdaq 2026-07-07T16:05:51Z–16:06:15Z, max divergence 0.772% (AXON)) with IBKR brokerage MCP live corroboration on the core ETFs (2026-07-07T16:02:26Z, max divergence 0.168%, `is_close: false`). All five Required inputs grounded (see 00 GO-Gate Table). Enhancing inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, institutional flow, fundamental feed) remain unwired: DQ 0.80, confidence cap LOW on published names.

## Regime Classification: **NEUTRAL** (carried; broad tape holds while growth/semis digest)

| Evidence | Value | Ledger |
|---|---|---|
| VIX close | 16.24 — below 20d mean 17.85; 60d range 15.32–22.22 | L007-L009 |
| SPY vs MA20/MA50 | 747.62 above 741.29 / 739.01; daily MACD ABOVE_SIGNAL | L013, L022 |
| SPY momentum | mom20 +1.37% / mom60 +9.96% — 20d momentum turned positive today | L019 |
| SPY intraday | -0.49% vs 2026-07-06 close | L011 |
| Rates (TLT) | 20d -0.27% / 60d -2.16% — no rate shock | L010 |
| ^IRX | 3.725% (fresh 2026-07-07 print) | L006 |

Not BULL (QQQ below its MA20, SOXX -16.4% from its 60d high on 76% annualized 30d vol — the growth complex is correcting hard inside a flat index); not HIGH_VOL (VIX 16.2, below its 20d mean); no RATE_SHOCK (TLT quiet). **NEUTRAL** with sharp internal rotation: yesterday's +4% SOXX pop fully reversed (-7.0% intraday today) while SPY gave back only -0.5% — breadth is rotating toward defensives/low-beta, consistent with today's leaderboard (DVA, BEN, TROW, ESS at the top; semis absent).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 747.62 | 2026-07-07 | LIVE | ABOVE MA20 741.29 / MA50 739.01 | 15.0% (prev 10.4%) | 1.000 | +0.50% | 4.3% | REALIZED_VOL_30D | 751.36 | 2026-08-04 | 717.63 | 785.08 | MEDIUM | L013-L023 |
| QQQ | 709.86 | 2026-07-07 | LIVE | BELOW MA20 720.45 / ABOVE MA50 711.67 (marginal) | 29.2% (prev 15.8%) | 1.671 | +0.84% | 8.4% | REALIZED_VOL_30D | 715.79 | 2026-08-04 | 653.48 | 778.10 | MEDIUM | L024-L034 |
| SOXX | 547.93 | 2026-07-07 | LIVE | BELOW MA20 597.14 / MA50 550.77 | 76.2% (prev 40.7%) | 3.453 | +1.73% | 22.0% | REALIZED_VOL_30D | 557.39 | 2026-08-04 | 432.10 | 682.68 | LOW | L035-L045 |

mu derivation (regime-prior rule, no free-handing): SPY = NEUTRAL prior **+0.5%**, no adjustment. QQQ = beta 1.671 x 0.5% = **+0.84%**, no relative-view adjustment. SOXX = beta 3.453 x 0.5% = **+1.73%**, no adjustment (today's -7% intraday semis break is one session, not a ledger-backed relative view; the beta-scaled prior already embeds the leverage). Confidence: SPY/QQQ MEDIUM (default; SPY trend aligned, QQQ mixed — below MA20 on doubled vol); SOXX LOW (30d rvol 76% vs prior 41%, -16.4% from 60d high, daily MACD BELOW_SIGNAL — vol regime not aligned with the NEUTRAL call).

Relative strength: QQQ/SPY 20d -0.68% / 60d +6.38%; SOXX/SPY 20d +0.15% / 60d +34.76% (ledger L031, L042). Consistency check: strong 60d growth/semis leadership decaying toward flat on the 20d window matches a NEUTRAL regime digesting an extended quarter — no contradiction with the classification.

## Event Concentration

- **Earnings season opens inside the horizon**: 35 of the estimate-shortlist names carry cadence-estimated reports inside the <=19d buffered window (banks/airlines cluster 07-09..07-17; industrials/REITs 07-21..07-24). All 35 carry the -0.10 penalty; DAL (est 2026-07-09, ~2d) is the nearest event in the published sleeve and prints the day after tomorrow's first settlement pass.
- **FOMC**: next scheduled meeting 2026-07-28/29 (structural cadence, INFERRED ±2d) — inside every target window; standard macro-event caveat, no additional penalty per spec.
- SATS excluded again (stale last bar 2026-07-02 — second consecutive session without prints at fetch time; flagged in 13 as possible delisting/halt, needs one more day before a structural note); FDXF excluded (28 bars since listing).

## Universe Handoff

515 index-union names (503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap; universe_summary.json generated 2026-07-07T15:52:47Z); **513 eligible** after screens (rejects: SATS stale, FDXF short history). Handed to technical_indicators.py: 513 + SPY/QQQ/SOXX (+TLT/^VIX/^IRX macro series fetched alongside). INDEX_UNION_PCTL (n=513); sampled fallback NOT used.
