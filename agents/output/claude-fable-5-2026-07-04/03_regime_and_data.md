# 03 Regime and Data

## Data Mode: DELAYED (weekend — markets closed)

U.S. equity markets are closed today (Saturday; Independence Day observed Friday 2026-07-03); all prices are official 2026-07-02 closes fetched this run (bars retrieved 2026-07-04T18:28:10Z; <=1-day lag vs the last completed session = DELAYED per the taxonomy and the 07-03 precedent). Weekend/holiday rule: publish a full REVIEW_ONLY set with no skipped days. gpt-5-2026-07-04 declared DELAYED_PARTIAL for the identical state — the standing mode-label divergence is tracked as a future Track B item (see 13). Primary source Yahoo v8 chart API per ticker (URLs + retrieved_at in fetch manifest; 521/521 OK); independent Nasdaq quote cross-check at 2026-07-04T18:31:54+00:00Z for all 26 published names (0.000% divergence); IBKR MCP snapshots on the closed market return prior-session (2026-07-01) closes matching our records exactly — prior-record consistency check only (2026-07-04T18:36Z). All 515 union tickers minus FDXF (26 bars) carry the 2026-07-02 bar; bars are final session closes — no partial-bar caveats. DELAYED mode is GO-eligible per the taxonomy, but no executable session exists today or tomorrow: status REVIEW_ONLY per the weekend/holiday rule.

## Regime: NEUTRAL (index level) with an active factor-rotation shock — carried over on identical bars

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MA20/MA50 | 744.78 > 741.08 > 737.43 (BULLISH alignment) | L013,L014 |
| SPY momentum 20d/60d | -1.25% / +12.98% | L019 |
| VIX | 16.15 vs 20d mean 18.10, 60d range 15.32-22.22 | L007,L008,L009 |
| Rates (TLT 20d/60d) | +0.23% / -1.30% — no rate shock | L010 |
| Last session (2026-07-02) | SPY -0.13% vs SOXX -5.57% (off -7.19% intraday low), QQQ -1.73% — dip-buying into the pre-holiday close | L011, per-name rows |
| SPY rvol30 | 15.3% ann (prior window 12.3%) — rising but moderate | L015 |

No session has traded since the 07-03 assessment, so the regime call carries over on identical bars. Not BULL: 20d momentum negative, daily MACD below signal, QQQ below its MA20. Not HIGH_VOL: VIX 16.15, below its 20d mean and well off the 60d high; SPY drawdown from 60d high only -1.9%. Not RATE_SHOCK/BEAR: TLT flat, trend intact. **NEUTRAL**, with the caveat that under-surface dispersion remains violent (QQQ rvol30 29.4% vs 17.2% prior; SOXX 76.1% vs 43.1%).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 744.78 | 2026-07-02 | DELAYED | above MA20 / above MA50 | 15.3% | 1.00 | +0.50% | 4.4% | REALIZED_VOL_30D | 748.50 | 2026-08-01 | 714.35 | 782.66 | MEDIUM | L013,L015,L018,L016 |
| QQQ | 712.60 | 2026-07-02 | DELAYED | below MA20 / above MA50 | 29.4% | 1.59 | +0.79% | 8.5% | REALIZED_VOL_30D | 718.23 | 2026-08-01 | 655.46 | 781.00 | MEDIUM | L024,L026,L029,L027 |
| SOXX | 566.32 | 2026-07-02 | DELAYED | below MA20 / above MA50 | 76.1% | 3.27 | +0.64% | 22.0% | REALIZED_VOL_30D | 569.94 | 2026-08-01 | 440.61 | 699.28 | LOW | L035,L037,L040,L038 |

mu derivation: SPY = NEUTRAL regime prior +0.5% (no adjustment). QQQ = beta x SPY mu = 1.59 x 0.5% = +0.79% (no adjustment). SOXX = 3.27 x 0.5% = +1.64%, shaded **-1.0pp to +0.64%** (within the ±1.5pp band) on ledger-backed exhaustion: weekly and monthly TD9 SELL_SETUP_9, rvol30 76.1% vs 43.1% prior window, and -13.5% from the 60d high (L045,L037,L039). Note: the 07-03 vintage's recorded QQQ/SOXX mu (+0.29%/+0.14%) do not reproduce from this same stated derivation — today's records recompute cleanly; discrepancy flagged in 02/13.

## Relative Strength and Consistency Check

QQQ/SPY RS: 20d -3.00%, 60d +8.09%. SOXX/SPY RS: 20d -6.77%, 60d +49.87%. Growth/semis still lead on 60d but 20d leadership is negative after the two-session unwind — consistent with a NEUTRAL call whose risk is a deeper momentum unwind, and consistent with the defensive tilt of today's equity leaderboard. ETF rows are a market-forecast sleeve — never candidates, never universe members.

## Event Concentration

- Today 2026-07-04 (Sat) and tomorrow: markets closed; next session Monday 2026-07-06. Weekend gap risk on all recorded 2026-07-02 entries.
- 2026-07-08: first-ever settlement pass (12 records, 2026-06-10 vintage) — process event, not market event.
- 2026-07-09: DAL opens Q2 earnings season (est ±5d).
- ~2026-07-14..23: bank/early wave (UNH 7/15, BAC/SNA/UAL ~7/16, IBKR/CFG/PPG/KEY ~7/17, AXP ~7/18, GE/SHW ~7/21, GL/GPC/PKG ~7/22, LII/URI/LUV ~7/23 windows) — 18 shortlist names carry the <=19d penalty; none published.
- ~2026-07-24..31: DOC/WST/KDP (7/24), FFIV (7/27), MAS/HUM/SWK (7/28-29), BEN/ABBV (7/31) — inside the 28d horizon but outside the buffered penalty window; flagged per name in 05.
- 2026-07-28/29 FOMC: the 2026-08-01 target date is three sessions after the decision; 2026-07-31 is also month-end (structural-review day).
- 0 published names have earnings inside 14 calendar days.

## Universe Handoff

Handed to technical_indicators.py and factor scoring: SPY, QQQ, SOXX + 514 eligible universe names (515 union - FDXF short history; 0 names failed price/ADV/coverage screens). Percentile labels: INDEX_UNION_PCTL (n=514). Rejection log in 04.
