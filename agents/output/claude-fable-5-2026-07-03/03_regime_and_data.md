# 03 Regime and Data

## Data Mode: DELAYED (market holiday)

U.S. equity markets are closed today (Independence Day observed); all prices are official 2026-07-02 closes fetched this run (bars retrieved 2026-07-03T20:28:35Z; <=1-day lag = DELAYED per the taxonomy). Runbook holiday rule: publish a REVIEW_ONLY set with no skipped days. The runbook names ILLUSTRATIVE_MODE for holidays; this run declares DELAYED instead because real fetched closes exist and dominate reference-state values under the Non-Fabrication Contract (deviation documented; gpt-5-2026-07-03 declared DELAYED_PARTIAL for the same state — mode-label convergence is a Track B wording candidate, see 13). Primary source Yahoo v8 chart API per ticker (URLs + retrieved_at in fetch manifest); independent Nasdaq quote cross-check at 2026-07-03T20:32:11+00:00Z for all published names (0.000% divergence on all 26 names); IBKR MCP snapshots on the closed market return prior-session (2026-07-01) closes matching our records exactly — prior-record consistency check. 519/520 fetched tickers carry the 2026-07-02 bar (SATS included again — it traded Thursday); FDXF remains short-history. Bars are final session closes — no partial-bar caveats today. DELAYED mode is GO-eligible per the taxonomy, but no executable session exists today: status REVIEW_ONLY per the holiday rule.

## Regime: NEUTRAL (index level) with an active factor-rotation shock

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MA20/MA50 | 744.78 > 741.08 > 737.43 (BULLISH alignment) | L013,L014 |
| SPY momentum 20d/60d | -1.25% / +12.98% | L019 |
| VIX | 16.15 vs 20d mean 18.10, 60d range 15.32-22.22 | L007,L008,L009 |
| Rates (TLT 20d/60d) | +0.23% / -1.30% — no rate shock | L010 |
| Thursday's close (last session) | SPY -0.13% vs SOXX -5.57% (off -7.19% intraday low), QQQ -1.73%, MU -5.49%; DVA +3.02% while HUM -3.09% gave back | L011, per-name rows |
| SPY rvol30 | 15.3% ann (prior window 12.3%) — rising but moderate | L015 |

Not BULL: 20d momentum negative, daily MACD below signal, QQQ below its MA20 (SPY +0.50% above its own). Not HIGH_VOL: VIX fell to 16.15 into the holiday, below its 20d mean and well off the 60d high; SPY drawdown from 60d high only -1.9%. Not RATE_SHOCK/BEAR: TLT flat, trend intact. **NEUTRAL**, with the caveat that under-surface dispersion is violent (QQQ rvol30 29.4% vs 17.2% prior; SOXX 76.1% vs 43.1%).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 744.78 | 2026-07-03 | DELAYED | above MA20 / above MA50 | 15.3% | 1.00 | +0.50% | 4.4% | REALIZED_VOL_30D | 748.50 | 2026-07-31 | 714.32 | 782.69 | MEDIUM | L013,L015,L018,L016 |
| QQQ | 712.60 | 2026-07-03 | DELAYED | below MA20 / above MA50 | 29.4% | 1.59 | +0.29% | 8.5% | REALIZED_VOL_30D | 714.67 | 2026-07-31 | 651.87 | 777.46 | MEDIUM | L024,L026,L029,L027 |
| SOXX | 566.32 | 2026-07-03 | DELAYED | below MA20 / above MA50 | 76.1% | 3.27 | +0.14% | 22.0% | REALIZED_VOL_30D | 567.11 | 2026-07-31 | 437.75 | 696.48 | LOW | L035,L037,L040,L038 |

mu derivation: SPY = NEUTRAL regime prior +0.5% (no adjustment). QQQ = beta x SPY mu = 1.59 x 0.5% = +0.29% (no adjustment). SOXX = 3.27 x 0.5% = +1.61%, shaded **-1.0pp to +0.61%** (within the ±1.5pp band) on ledger-backed exhaustion: weekly TD9 SELL_SETUP_9, weekly RSI 72.5, rvol30 73.9% vs 43.0% prior window, and today's -6.41% break (L045,L043,L037,L035).

## Relative Strength and Consistency Check

QQQ/SPY RS: 20d -3.00%, 60d +8.09%. SOXX/SPY RS: 20d -6.77%, 60d +49.87%. Growth/semis still lead on 60d but 20d leadership has flattened to zero and cracked today — consistent with a NEUTRAL call whose risk is a deeper momentum unwind, and consistent with the defensive tilt of today's equity leaderboard. ETF rows are a market-forecast sleeve — never candidates, never universe members.

## Event Concentration

- Today 2026-07-03: U.S. market holiday; next session Monday 2026-07-06. Weekend gap risk on all recorded 2026-07-02 entries.
- 2026-07-08: first-ever settlement pass (12 records, 2026-06-10 vintage) - process event, not market event.
- 2026-07-09: DAL opens Q2 earnings season (est ±5d).
- ~2026-07-14..21: bank/early wave (BAC, SNA ~7/16, PPG ~7/17, GE ~7/21, GPC/GL/IQV ~7/22 windows) - 14 shortlist names carried the ≤19d penalty; none published.
- ~2026-07-22..31: bulk of sleeve earnings inside the 28d horizon but outside the buffered penalty window; flagged per name in 05.
- 2026-07-28/29 FOMC: the 2026-07-31 target date is two sessions after the decision and is also month-end (structural-review day).
- 0 published names have earnings inside 14 calendar days.

## Universe Handoff

Handed to technical_indicators.py and factor scoring: SPY, QQQ, SOXX + 514 eligible universe names (515 union - SATS stale - FDXF short history; 0 names failed price/ADV/coverage screens). Percentile labels: INDEX_UNION_PCTL (n=514). Rejection log in 04.

