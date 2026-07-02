# 03 Regime and Data

## Data Mode: DELAYED

All prices are 2026-07-01 official closes fetched post-close (bars retrieved 2026-07-01T22:37:20Z; market close 20:00Z; run executed ~22:36-23:1xZ). Primary source Yahoo v8 chart API per ticker (URLs + retrieved_at in fetch manifest); independent Nasdaq quote cross-check at 2026-07-01T22:49:12+00:00Z for all published names (max divergence 0.845%); IBKR MCP snapshot corroboration for SPY/QQQ/SOXX/DVA/HUM/FFIV/MAS. 519/520 fetched tickers carry today's bar; SATS is stale (2026-06-30, excluded). DELAYED mode is GO-eligible at reduced exposure per the taxonomy; the NO_TRADE outcome comes from evidence thresholds, not data mode.

## Regime: NEUTRAL (index level) with an active factor-rotation shock

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MA20/MA50 | 745.76 > 741.55 > 736.61 (BULLISH alignment) | L013,L014 |
| SPY momentum 20d/60d | -1.82% / +13.18% | L019 |
| VIX | 16.59 vs 20d mean 18.10, 60d range 15.32-22.22 | L007,L008,L009 |
| Rates (TLT 20d/60d) | -0.15% / -1.30% — no rate shock | L010 |
| Today's dispersion | SPY -0.14% vs SOXX -6.41%, MU -10.57%, AMD -6.89%; HUM +3.07%, DVA +2.49% | L011, per-name rows |
| SPY rvol30 | 15.4% ann (prior window 12.0%) — rising but moderate | L015 |

Not BULL: 20d momentum negative, daily MACD below signal, defensive leadership. Not HIGH_VOL: VIX 16.6 below its 20d mean and 25% off the 60d high; SPY drawdown from 60d high only -1.8%. Not RATE_SHOCK/BEAR: TLT flat, trend intact. **NEUTRAL**, with the caveat that under-surface dispersion is violent (QQQ rvol30 28.9% vs 16.9% prior; SOXX 73.9% vs 43.0%).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 745.76 | 2026-07-01 | DELAYED | above MA20 / above MA50 | 15.4% | 1.00 | +0.50% | 4.5% | REALIZED_VOL_30D | 749.49 | 2026-07-29 | 714.96 | 784.02 | MEDIUM | L013,L015,L018,L016 |
| QQQ | 725.17 | 2026-07-01 | DELAYED | above MA20 / above MA50 | 28.9% | 1.58 | +0.79% | 8.4% | REALIZED_VOL_30D | 730.90 | 2026-07-29 | 667.91 | 793.88 | MEDIUM | L024,L026,L029,L027 |
| SOXX | 599.70 | 2026-07-01 | DELAYED | below MA20 / above MA50 | 73.9% | 3.23 | +0.62% | 21.3% | REALIZED_VOL_30D | 603.42 | 2026-07-29 | 470.43 | 736.41 | LOW | L035,L037,L040,L038 |

mu derivation: SPY = NEUTRAL regime prior +0.5% (no adjustment). QQQ = beta x SPY mu = 1.58 x 0.5% = +0.79% (no adjustment). SOXX = 3.23 x 0.5% = +1.61%, shaded **-1.0pp to +0.61%** (within the ±1.5pp band) on ledger-backed exhaustion: weekly TD9 SELL_SETUP_9, weekly RSI 72.5, rvol30 73.9% vs 43.0% prior window, and today's -6.41% break (L045,L043,L037,L035).

## Relative Strength and Consistency Check

QQQ/SPY RS: 20d -0.99%, 60d +10.04%. SOXX/SPY RS: 20d +0.94%, 60d +61.10%. Growth/semis still lead on 60d but 20d leadership has flattened to zero and cracked today — consistent with a NEUTRAL call whose risk is a deeper momentum unwind, and consistent with the defensive tilt of today's equity leaderboard. ETF rows are a market-forecast sleeve — never candidates, never universe members.

## Event Concentration

- 2026-07-03 (Fri): US market holiday (Independence Day observed) — shortened week, thin volumes (SPY VR20 0.61).
- ~2026-07-14..18: money-center bank + first mega-cap earnings wave; sleeve name UNH reports ~2026-07-15 (est ±5d) — penalized -0.10, LOW confidence, mu shaded.
- ~2026-07-22..31: bulk of sleeve earnings (URI, LII, WST, CVS, HUM, FFIV, MAS, V, CCEP, TROW, GOOGL-window) — inside the 28d horizon but outside the 19d buffered penalty window; flagged per name in 05.
- 2026-07-28/29: FOMC — decision lands ON the 2026-07-29 target date; CI calibration for this vintage will absorb a macro event.
- Only 1 sleeve name (UNH) has earnings inside 14d — NO_TRADE trigger #4 (>2 names) not activated.

## Universe Handoff

Handed to technical_indicators.py and factor scoring: SPY, QQQ, SOXX + 513 eligible universe names (515 union - SATS stale - FDXF short history; 0 names failed price/ADV/coverage screens). Percentile labels: INDEX_UNION_PCTL (n=513). Rejection log in 04.

