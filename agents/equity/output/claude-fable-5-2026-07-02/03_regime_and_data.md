# 03 Regime and Data

## Data Mode: LIVE

All prices are 2026-07-02 intraday prints fetched during the regular session (bars retrieved 2026-07-02T19:21:22Z ≈ 15:21 ET, ~40 minutes before the close). Primary source Yahoo v8 chart API per ticker (URLs + retrieved_at in fetch manifest); independent Nasdaq quote cross-check at 2026-07-02T19:26:51+00:00Z for all published names (max divergence 0.635%); IBKR MCP live-snapshot corroboration for SPY/QQQ/SOXX/DVA/HUM/FFIV/MAS (max divergence 0.18%). 519/520 fetched tickers carry today's bar; SATS is stale (2026-07-01, excluded). The current-day bar is a live partial bar and volume ratios reflect a partial session (disclosed, symmetric across names). LIVE mode is GO-eligible; the NO_TRADE outcome comes from evidence thresholds, not data mode.

## Regime: NEUTRAL (index level) with an active factor-rotation shock

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MA20/MA50 | 741.60 > 740.92 > 737.36 (BULLISH alignment) | L013,L014 |
| SPY momentum 20d/60d | -1.68% / +12.50% | L019 |
| VIX | 16.90 vs 20d mean 18.14, 60d range 15.32-22.22 | L007,L008,L009 |
| Rates (TLT 20d/60d) | +0.21% / -1.33% — no rate shock | L010 |
| Today's dispersion (day 2) | SPY -0.56% vs SOXX -7.19%, QQQ -2.28%, MU -7.46%; DVA +2.49% holds while HUM -3.75% gives back | L011, per-name rows |
| SPY rvol30 | 15.4% ann (prior window 12.3%) — rising but moderate | L015 |

Not BULL: 20d momentum negative, daily MACD below signal, QQQ below its MA20, SPY riding its MA20 (+0.09%). Not HIGH_VOL (yet): VIX 16.9 still below its 20d mean and well off the 60d high; SPY drawdown from 60d high only -2.4%. Not RATE_SHOCK/BEAR: TLT flat, trend intact. **NEUTRAL**, with the caveat that under-surface dispersion is violent (QQQ rvol30 29.7% vs 17.2% prior; SOXX 77.4% vs 43.1%).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 741.60 | 2026-07-02 | DELAYED | above MA20 / above MA50 | 15.4% | 1.00 | +0.50% | 4.4% | REALIZED_VOL_30D | 745.31 | 2026-07-30 | 711.06 | 779.56 | MEDIUM | L013,L015,L018,L016 |
| QQQ | 708.64 | 2026-07-02 | DELAYED | below MA20 / below MA50 | 29.7% | 1.60 | +0.30% | 8.6% | REALIZED_VOL_30D | 710.77 | 2026-07-30 | 647.62 | 773.92 | MEDIUM | L024,L026,L029,L027 |
| SOXX | 556.60 | 2026-07-02 | DELAYED | below MA20 / above MA50 | 77.4% | 3.33 | +0.16% | 22.3% | REALIZED_VOL_30D | 557.49 | 2026-07-30 | 428.23 | 686.75 | LOW | L035,L037,L040,L038 |

mu derivation: SPY = NEUTRAL regime prior +0.5% (no adjustment). QQQ = beta x SPY mu = 1.60 x 0.5% = +0.30% (no adjustment). SOXX = 3.33 x 0.5% = +1.61%, shaded **-1.0pp to +0.61%** (within the ±1.5pp band) on ledger-backed exhaustion: weekly TD9 SELL_SETUP_9, weekly RSI 72.5, rvol30 73.9% vs 43.0% prior window, and today's -6.41% break (L045,L043,L037,L035).

## Relative Strength and Consistency Check

QQQ/SPY RS: 20d -3.10%, 60d +7.90%. SOXX/SPY RS: 20d -7.92%, 60d +47.55%. Growth/semis still lead on 60d but 20d leadership has flattened to zero and cracked today — consistent with a NEUTRAL call whose risk is a deeper momentum unwind, and consistent with the defensive tilt of today's equity leaderboard. ETF rows are a market-forecast sleeve — never candidates, never universe members.

## Event Concentration

- 2026-07-03 (tomorrow): US market holiday (Independence Day observed) — shortened week; today is the last session before a 3-day weekend.
- 2026-07-09: DAL opens the Q2 earnings season (est ±5d) — DAL penalized out of the sleeve (rank 30).
- ~2026-07-14..21: bank + early industrial wave (BAC, SNA ~7/16, GE ~7/21, all est ±5d) — none published; 11 shortlist names carried the ≤19d penalty this run.
- ~2026-07-22..31: bulk of sleeve earnings (GPC, URI, LII, WST, KDP, HUM, FFIV, MAS, CCEP, LIN, ABBV windows) — inside the 28d horizon, outside the buffered penalty window; flagged per name in 05.
- 2026-07-28/29 FOMC: the 2026-07-30 target date is the day AFTER the decision — this vintage's CI calibration absorbs the macro event plus one session.
- 0 sleeve names have earnings inside 14 calendar days — NO_TRADE trigger #4 not activated.

## Universe Handoff

Handed to technical_indicators.py and factor scoring: SPY, QQQ, SOXX + 513 eligible universe names (515 union - SATS stale - FDXF short history; 0 names failed price/ADV/coverage screens). Percentile labels: INDEX_UNION_PCTL (n=513). Rejection log in 04.

