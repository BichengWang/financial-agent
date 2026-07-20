══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-20
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════

## Executive Summary

Monday's run — the stack's first intraday fire (12:21 ET), scored off Friday 07-17 closes — settled the largest single-day batch in the ledger's history (68 predictions, all at the 07-17 close under WEEKEND_TARGET/TARGET_EQ_RUN_DATE) and the news is uncomfortable: the June core-ETF forecasts went 0-for-12 on direction, dragging MARKET_FORECAST accuracy to 20% over a now-Track-A-sized n=30, while equity hit rate slipped to 51.4% and weighted rank IC sits at −0.049. The cross-section is unchanged in character from Friday — low-vol defensives and just-printed financials own the leaderboard (DOC, EXPD, RF, JBHT, BBY on top), 12 of 33 published names sit inside the buffered earnings window with CSX/MCO printing in two days, and the top-20's mean beta of +0.10 makes the 0.90–1.10 band structurally unreachable. The run publishes **NO_TRADE for the 15th consecutive scoring session** on the same family-coverage gate, with 33 monitoring-sleeve forecasts (LOW confidence, targets 2026-08-17) and 3 core-ETF records for the evidence engine.

## MoM Reflection Summary (from 02, no new facts)

Baseline claude-fable-5-2026-06-10 (BASELINE_WINDOW_GAP, 12d off target): 4/12 alpha-positive, mean alpha −1.80% vs SPY +2.46%. Defensive pharma/managed-care validated again (ABBV +10.2%, MCK +4.0%, UNH +2.2%, LLY +1.1% alpha); retail staples, energy majors, and semis stay failed. Carry-forwards: UNH/LLY/GE CARRY; ABBV DOWNGRADE (earnings penalty pushed it below the 60th-pctl rank floor — best alpha in the basket, unrankable this run); MCK DOWNGRADE (below floor); LIN DROP (settled MISS). Rolling calibration (canonical, n=175): hit 51.4%, CI coverage 77.1%, mean z −0.24, weighted rank IC −0.049 → MEDIUM cap active (sleeve publishes LOW).

## Regime

| Field | Value | Ledger |
|---|---|---|
| Regime | NEUTRAL — HIGH_VOL watch (VIX>20 + SPY below MAs would trigger) | L018 |
| Data quality | DELAYED, 07-17 closes, all Required inputs grounded; DQ 0.80 (Fund/Sent gap) | L002, L011 |
| Key macro risk | Peak earnings wave (12 published names in buffered window) + FOMC ~07-28/29 inside horizon; SPY rvol 4.5% vs 2.8% prior | L011, L015 |

## Core ETF Market Forecast (from 03, no new facts)

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 743.29 | 2026-07-17 | DELAYED | below MA20 745.02, below MA50 744.38 | 4.54% | 1.000 | +0.50% | 4.54% | REALIZED_VOL_30D | 747.01 | 2026-08-17 | 711.94 | 782.08 | MEDIUM | L014,L015 |
| QQQ | 695.33 | 2026-07-17 | DELAYED | below MA20 718.35, below MA50 719.01 | 8.87% | 1.733 | +0.37% | 8.87% | REALIZED_VOL_30D | 697.9 | 2026-08-17 | 633.75 | 762.06 | LOW | L016,L017 |
| SOXX | 521.81 | 2026-07-17 | DELAYED | below MA20 586.15, below MA50 566.37 | 22.04% | 3.710 | +0.35% | 22.04% | REALIZED_VOL_30D | 523.64 | 2026-08-17 | 404.04 | 643.23 | LOW | L018,L019 |
June's settled MF record (0/12 HIT today; 20% over n=30) is the context for these rows: mus are regime-prior mechanics at MEDIUM/LOW confidence, not conviction (13 logs the rejected calibration fix).

## Ranked Candidates (monitoring sleeve top tier — full 33-name table in 05)

| # | Ticker | Adj Score | Trace (compact) | Pctl | Beta | mu | sigma | Target 08-17 | 70% CI | Conf | Thesis |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DOC | +0.405 | (.30·1.38T+.15·1.04M)·.80−.05 | 100.0 | 0.53 | +5.0% | 7.20% | 23.63 | 21.94–25.32 | LOW | Medical-office REIT recovery; duration bid |
| 2 | EXPD | +0.400 | (.30·1.42T+.15·0.91M)·.80−.05 | 99.8 | 0.20 | +5.0% | 6.15% | 191.88 | 180.29–203.63 | LOW | Low-vol logistics compounder |
| 3 | RF | +0.364 | (.30·1.10T+.15·0.83M)·.80−.00 | 99.6 | 0.18 | +6.0% | 6.90% | 66.16 | 61.75–70.72 | LOW | Regional-bank post-print momentum |
| 4 | JBHT | +0.341 | (.30·1.06T+.15·0.73M)·.80−.00 | 99.4 | 0.57 | +6.0% | 10.61% | 308.89 | 276.75–341.04 | LOW | Intermodal recovery, post-print |
| 5 | BBY | +0.333 | (.30·1.23T+.15·0.72M)·.80−.05 | 99.2 | 0.59 | +5.0% | 8.35% | 89.70 | 82.28–97.13 | LOW | Device replacement cycle |
| 6 | TRV | +0.332 | (.30·1.57T+.15·0.05M)·.80−.05 | 99.0 | −0.76 | +5.0% | 9.72% | 387.53 | 350.20–424.87 | LOW | P&C beat; negative-beta defensive |
| 7 | PRU | +0.313 | (.30·1.06T+.15·0.92M)·.80−.05 | 98.8 | 0.15 | +5.0% | 6.34% | 125.01 | 117.15–132.87 | LOW | Rate-curve life insurer |
| 8 | GEN | +0.311 | (.30·1.11T+.15·0.38M)·.80−.00 | 98.6 | 0.58 | +6.0% | 10.26% | 28.34 | 25.49–31.20 | LOW | Consumer-security compounder |
| 9 | FITB | +0.292 | (.30·0.84T+.15·0.75M)·.80−.00 | 98.4 | 0.23 | +6.0% | 8.04% | 47.83 | 44.06–51.61 | LOW | Regional post-print momentum |
| 10 | STT | +0.291 | (.30·0.85T+.15·1.15M)·.80−.05 | 98.2 | 0.69 | +5.0% | 7.37% | 191.69 | 177.68–205.69 | LOW | Custody fee leverage, stretched |

Carry-forwards publish at their own ranks: UNH #41 (+4.0% mu), LLY #116 (+1.0%), GE #161 (+1.0%). Event-gated names (CSX, UNP, MNST, FRT, ADP, IQV, MCO, CHRW, SNA, UPS, AAPL, WST) publish with −0.10 penalties and LOW confidence.

## No-Trade Rationale / Portfolio Analytics

No portfolio drafted (07 pre-check): (1) the investable set is empty — evidence threshold #2 unsatisfiable with Fund_Z/Sent_Z UNAVAILABLE universe-wide, 15th consecutive run; (2) top-20 mean beta +0.103 (15/20 below 0.5) makes the beta band infeasible without rank-bar violations; (3) 12 in-window earnings names trip downgrade trigger #4. Correlation is not a blocker (top-10 mean 0.208).

## Assumptions and Limitations

- Fund/Sent families UNAVAILABLE; SHADOW Phase-1 tooling exists, promotion still requires Phase-2 full-universe coverage (≥70%). DQ 0.80 caps everything below investable completeness.
- Single-web-source bulk (Nasdaq historical, consolidated tape) + IBKR tool verification on 17 settlement names; consolidated-vs-primary close artifacts ≤0.19% disclosed (SPY 743.29 vs 07-17 package's official 743.15).
- Post-print entries embedded in several leaders (TRV/RF/FITB/STT/CFG/JBHT); 60d betas correction-distorted (SOXX 3.71); parametric VaR/CVaR assume normality; monthly-MA gaps on short-history names (none published).
- Prediction records: 33 EQUITY_ALPHA + 3 MARKET_FORECAST, targets 2026-08-17; 68 settlements embedded (largest batch to date; four-copy concentration disclosed in 02).

## Next Scheduled Review

Next daily full pipeline: Tuesday 2026-07-21 pre-open. Weekly parameter review: Friday 2026-07-24 after close. Monthly structural review: 2026-07-31 — MF mu-prior calibration and weekend-republication policy are queued for it (02 §6, 13).
