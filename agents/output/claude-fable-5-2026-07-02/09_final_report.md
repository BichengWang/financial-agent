# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-02
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
Model: claude-fable-5 · Data mode: LIVE (intraday ~15:21 ET, two-source verified)
══════════════════════════════════════════════════════
```

## Executive Summary

Second consecutive index-union run and second NO_TRADE on the same arithmetic: with fundamental and sentiment families unwired, evidence threshold #2 cannot be met — now corroborated by gpt-5's morning run hitting the identical gate, making this the system's dominant open issue (escalated as mandatory Track B work in 13). The AI-capex unwind entered its second violent session — SOXX −7.19% intraday on top of −6.41%, MU −7.46%, with even yesterday's defensive winners churning (HUM −3.75%) — while the index barely moved (SPY −0.56%) and VIX sat at 16.9. The published book is 23 monitoring forecasts (LOW confidence) led by defensive momentum (DVA, HUM, BAX, BEN, URI) plus reflection carries LIN/LLY/ABBV, with 3 core ETF forecasts (SPY +0.50%, QQQ +0.30%, SOXX +0.16% — both shaded for exhaustion/vol regime). The 2026-06-10 vintage marks 22-of-28 days at 1/5 investable interim alpha (ABBV +13.7pp best monitor; MU gave back to +5.3pp, vindicating the exhaustion shade three weeks late); first settlements land 2026-07-08. One compliance fix this run: total per-name mu adjustment is now clamped at ±2pp per the Calibration Table (the 07-01 UNH record had stacked −3pp — disclosed, stands as recorded).

## MoM Reflection Summary (from 02, no new facts)

Baseline `claude-fable-5-2026-06-10` (SAME_MODEL_BASELINE), SPY window +1.82%: investable five 1/5 positive alpha (UNH +2.3pp only; CVX −13.7pp, XOM −11.6pp, WMT −8.3pp, COST −5.1pp, MCK −2.8pp recovering late). Monitors: ABBV +13.7pp, LIN +5.2pp, LLY +4.7pp, MU +5.3pp (peaked +13.4pp), NVDA −6.2pp, GOOGL −1.1pp. Decisions: DROP MCK/COST/WMT/CVX/XOM/MU/NVDA/GOOGL; CARRY LIN/LLY/ABBV; **DOWNGRADE UNH** (74.2 pctl intraday + earnings ~7/15 + exhaustion; mu clamp would leave 0.0% — excluded from today's sleeve; its 6/10 prediction settles 7/8 regardless). 0 settlements due; calibration INSUFFICIENT_SETTLED_N.

## Regime Assessment (ledger rows in 03)

| Item | Reading | Implication |
|---|---|---|
| Regime | **NEUTRAL** — SPY 741.60 riding MA20 (740.92, +0.09%), above MA50 737.36; mom20 −1.7%/mom60 +12.5%; VIX 16.90 < 20d mean 18.14 | Trend intact by a thread; no index-level vol shock |
| Dispersion (day 2) | SPY −0.56% vs SOXX −7.19%, QQQ −2.28% (below its MA20), MU −7.46%; HUM −3.75% gives back while DVA +2.49% holds | De-grossing signature; SOXX −15% off its 60d high, rvol30 77.4% (vs 43.1% prior) |
| Rates | TLT 20d +0.21% / 60d −1.33% | Not a rate shock |
| Data quality | LIVE, all 5 Required inputs grounded, DQ 0.80 (fund/sent UNAVAILABLE) | GO-eligible on data; NO_TRADE on evidence thresholds |

## Core ETF Market Forecast (summary of 03)

| ETF | Entry (7/2 intraday) | mu (28d) | sigma | Target 7/30 | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 741.60 | +0.50% | 4.44% | 745.31 | [711.06, 779.56] | MEDIUM |
| QQQ | 708.64 | +0.30% | 8.57% | 710.77 | [647.62, 773.92] | MEDIUM — −0.5pp shade: below MA20, RS20 −3.1%, rvol doubling |
| SOXX | 556.60 | +0.16% | 22.33% | 557.49 | [428.23, 686.75] | LOW — −1.5pp shade (band max): weekly TD9-9 again, rvol 77% vs 43%, second −7% session |

## Ranked Forecasts (NOT positions — full blocks in 05; all MONITOR, LOW confidence)

| Rank | Ticker | Entry (LIVE 7/2) | Pctl (n=513) | mu | σ(1m) | Target 7/30 | CI70 | Trace (compact) |
|---|---|---|---|---|---|---|---|---|
| 1 | DVA | 233.71 | 100.0 | +5.0% | 6.9% | 245.40 | 229–262 | Tech +1.63, Macro +0.81, pen 0.05 (RSI 84) |
| 2 | HUM | 394.07 | 99.8 | +5.0% | 11.6% | 413.77 | 366–461 | Tech +1.63, Macro +0.45, pen 0.05 (TD9-w) |
| 3 | BAX | 22.55 | 99.6 | +6.0% | 10.6% | 23.90 | 21.4–26.4 | Tech +1.23, Macro +0.43 |
| 4 | BEN | 33.62 | 99.4 | +5.0% | 8.3% | 35.30 | 32.4–38.2 | Tech +1.08, Macro +1.08, pen 0.05 (TD9-w 9) |
| 5 | URI | 1090.01 | 99.2 | +6.0% | 9.9% | 1155.41 | 1043–1267 | Tech +0.97, Macro +0.81 |
| 6–20 | MAS, PANW, LII, DOC, HSIC, MRNA, MNST, FFIV, SWK, GPC, KDP, WST, CCEP, FTNT, LYV | | 99.0–96.3 | +4–6% | | | | see 05 |
| carry | LLY 91.0 (+4%), ABBV 87.3 (+3%), LIN 82.8 (+3%) | | | | | | | reflection-bound |

Sector mix (INFERRED): Health Care 8/23, Industrials 4, Staples 3, IT 3, Financials 1, plus RE/ConsDisc/Comm/Materials singles. Notable churn vs 7/1: BAX/DOC/HSIC/MRNA/MNST/GPC/FTNT/LYV in; V/CVS/VTRS/TROW/IEX/IQV/CRL/BAX-adjacent out — two violent sessions are reshuffling the same defensive complex.

## Portfolio Analytics / No-Trade Rationale

Three independent grounds, all computed and ledger-backed: (1) investable set 0 of 513 — family threshold unsatisfiable (stop criterion #1, binding); (2) max achievable NAV beta at the 5% cap = 0.63 vs the protected 0.90 floor; (3) the equal-weight top-12 diagnostic's parametric dd95 = 9.1% now exceeds the 8% cap (vol expansion). Risk committee: **APPROVE — NO_TRADE** (08).

## Assumptions and Limitations

- Entry prices are intraday prints ~40 minutes before a pre-holiday close; settlement uses recorded entries; the current-day bar is a live partial bar (volume ratios partial, symmetric).
- Fundamental/sentiment families UNAVAILABLE universe-wide; scores are momentum/risk-only; confidence LOW everywhere; DQ 0.80.
- Earnings dates are cadence estimates ESTIMATED (±5d), INFERRED; 11 shortlist names penalized inside the ≤19d window, none published.
- mu priors unvalidated until settlements begin 2026-07-08 (12 records), then 2026-07-29 (27) and 2026-07-30 (26, this vintage — the day after FOMC).
- Sector labels INFERRED (no GICS feed).

## Next Scheduled Review

2026-07-03 is a U.S. market holiday. Next full run: Monday 2026-07-06 07:27 ET (manual — no scheduler active). First settlement pass: 2026-07-08 (12 records from the 2026-06-10 vintage).
