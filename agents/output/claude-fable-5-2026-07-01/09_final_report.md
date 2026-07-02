# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-01
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
Model: claude-fable-5 · Data mode: DELAYED (post-close, two-source verified)
══════════════════════════════════════════════════════
```

## Executive Summary

First index-union run for this model: 515 S&P 500 ∪ Nasdaq-100 names materialized, 513 scored with full 5y histories, dense technical packs, and 27 settleable forecasts published — the largest single-run addition to the prediction ledger yet. The run publishes **NO_TRADE**: with no wired fundamental or sentiment feed at index-union scale, only 2 of 4 factor families are sourceable, evidence threshold #2 (≥3 of 4 families non-negative) is unsatisfiable, and the investable set is empty by arithmetic — independently, the defensive leaderboard's achievable NAV beta (≤0.60 at the 5% cap) cannot reach the protected 0.90 floor. The session itself validated the board's defensive tilt: SPY closed −0.14% while SOXX broke −6.41% (MU −10.57%, AMD −6.89%) and managed care rallied (HUM +3.07%, DVA +2.49%). The 2026-06-10 vintage marks 21-of-28 days: investable sleeve 1/5 on interim alpha (energy/staples legs failed badly), while downgraded monitors MU (+13.4pp) and ABBV (+8.8pp) outperformed — settlement begins 2026-07-08. Core ETF view: NEUTRAL regime, SPY +0.5% / QQQ +0.79% / SOXX +0.62% (shaded for weekly TD9-9 exhaustion) over 28 days.

## MoM Reflection Summary (from 02, no new facts)

Baseline `claude-fable-5-2026-06-10` (SAME_MODEL_BASELINE). Interim, 21d into 28d horizon, SPY +2.40%: investable five 1/5 positive alpha (UNH +2.4pp the only hit; CVX −15.7pp, WMT −11.6pp, COST −8.1pp, MCK −5.2pp) — the staples/energy legs of the defensive thesis failed. Monitor sleeve 4/7 positive (MU +13.4pp — the crowding-unwind shade was 3 weeks early; today's −10.6% break partially vindicates it; ABBV +8.8pp, LIN +2.4pp, LLY +2.3pp). Decisions: DROP MCK/COST/WMT/CVX/XOM/MU/NVDA/GOOGL; CARRY UNH/LLY; PROMOTE LIN/ABBV. 0 settlements due (earliest 2026-07-08); calibration metrics INSUFFICIENT_SETTLED_N.

## Regime Assessment (ledger rows in 03)

| Item | Reading | Implication |
|---|---|---|
| Regime | **NEUTRAL** — SPY 745.76 > MA20 741.55 > MA50 736.61; mom20 −1.8% / mom60 +13.2%; VIX 16.59 < 20d mean 18.10 | Trend intact, short momentum flat; no vol shock at index level |
| Dispersion shock | SPY −0.14% vs SOXX −6.41% today; QQQ rvol30 28.9% (vs 16.9% prior 30d), SOXX 73.9% (vs 43.0%) | Violent AI-capex → defensive rotation under a calm index |
| Rates | TLT +/−0% (20d −0.15%, 60d −1.30%) | Not a rate shock |
| Data quality | DELAYED, all 5 Required inputs grounded, DQ 0.80 (fund/sent families UNAVAILABLE) | GO-eligible on data; NO_TRADE on evidence thresholds |

## Core ETF Market Forecast (summary of 03)

| ETF | Entry (7/1) | mu (28d) | sigma | Target 7/29 | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 745.76 | +0.50% | 4.45% | 749.49 | [714.96, 784.02] | MEDIUM |
| QQQ | 725.17 | +0.79% | 8.35% | 730.90 | [667.91, 793.88] | MEDIUM |
| SOXX | 599.70 | +0.62% | 21.32% | 603.42 | [470.43, 736.41] | LOW — weekly TD9 SELL_SETUP_9, rvol regime doubling, −1.0pp shade applied |

## Ranked Forecasts (NOT positions — full blocks in 05; all MONITOR, LOW confidence)

| Rank | Ticker | Entry (DELAYED 7/1) | Pctl (n=513) | mu | σ(1m) | Target 7/29 | CI70 | Trace (compact) |
|---|---|---|---|---|---|---|---|---|
| 1 | DVA | 228.03 | 100.0 | +5.0% | 7.1% | 239.43 | 222–256 | Tech +1.40, Macro +0.80, pen 0.05 (RSI 81) |
| 2 | HUM | 409.42 | 99.8 | +5.0% | 10.9% | 429.89 | 384–476 | Tech +1.57, Macro +0.41, pen 0.05 (RSI 83) |
| 3 | FFIV | 424.18 | 99.6 | +6.0% | 7.9% | 449.63 | 415–485 | Tech +1.13, Macro +0.82 |
| 4 | MAS | 81.64 | 99.4 | +6.0% | 9.5% | 86.54 | 78–95 | Tech +1.18, Macro +0.48 |
| 5 | BEN | 34.06 | 99.2 | +5.0% | 8.9% | 35.76 | 33–39 | Tech +1.10, Macro +1.02, pen 0.05 (TD9-w 9) |
| 6–20 | URI, LII, WST, PANW, V, CCEP, CVS, SWK, KDP, VTRS, TROW, IEX, IQV, CRL, BAX | | 99.0–96.3 | +5–6% | | | | see 05 |
| carry | LIN 91.0 (+5%), ABBV 88.3 (+4%), UNH 87.3 (+1%, earnings 7/15), LLY 85.9 (+3%) | | | | | | | reflection-bound |

Sector mix (INFERRED): Health Care 10/24, Industrials 5, Financials 4, Staples 2, IT 2, Materials 1 — the board is the defensive rotation.

## Portfolio Analytics / No-Trade Rationale

Investable set: **0 of 513** (families test unsatisfiable with fund/sent UNAVAILABLE) → stop criterion NO_TRADE #1 before sizing; no weights drafted. Independent construction check: max achievable NAV beta at the 5% single-name cap = 0.60 (protected band 0.90–1.10); Health Care share would bind the 30% sector cap immediately. Diagnostics on the equal-weight top-12 sleeve: beta 0.55, avg pairwise corr 0.092 ✓, parametric dd95 7.6% ✓. Risk committee: **APPROVE — NO_TRADE** (08), integrity clean.

## Assumptions and Limitations

- Fundamental/sentiment families UNAVAILABLE universe-wide (no wired feed): scores are momentum/risk-only; DQ 0.80, confidence LOW everywhere; reference-state color appears only as INFERRED thesis text.
- Earnings dates are cadence estimates, ESTIMATED (±5d), INFERRED from reference state (≤2026-01); penalties applied on the buffered ≤19d window.
- Entry prices are official 2026-07-01 closes (DELAYED); settlement uses recorded entries; FOMC lands on the 2026-07-29 target date.
- mu priors remain unvalidated: 0 settlements system-wide; first settlements due 2026-07-08 (12 records), this vintage 2026-07-29 (27 records).
- Sector labels are INFERRED reference classifications (no GICS feed).

## Next Scheduled Review

Per runbook cadence: next full pre-open run next trading day (2026-07-02 07:27 ET; note 2026-07-03 is a market holiday). No scheduler currently active — manual runs until a durable job is recreated. First prediction settlement pass: 2026-07-08.
