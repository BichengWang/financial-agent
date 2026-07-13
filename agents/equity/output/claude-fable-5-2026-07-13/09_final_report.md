# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-13
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
Model: claude-fable-5 · Data mode: DELAYED (Fri 07-10 close, Mon pre-open)
══════════════════════════════════════════════════════
```

## Executive Summary

All five Required-for-GO inputs are grounded — Nasdaq-fetched 5y histories for the full 514-name index union (Yahoo was 429-blocked all session; the fallback chain held at zero failures), IBKR-verified prices (12/12 exact priorClose matches), full sigma chain, confirmed earnings dates, and the index-union universe — but the run publishes **NO_TRADE** for the 11th consecutive scoring session: with fundamentals and sentiment feeds unwired, only 2 of 4 factor families are sourceable, so no name can meet the 3-of-4 evidence threshold and the investable set is structurally empty. Twenty predictions from the gpt-5 06-15 vintage settled today at 11 HIT / 6 MISS with all three ETF calls IN_CI; the rolling ledger stands at 121 settled records with 55.4% hit rate, 76% CI coverage, and positive rank IC. Twenty-four monitoring-sleeve forecasts (top 20 + 4 validated carry-forwards) and three core-ETF forecasts are published, all fully settleable on 2026-08-10.

## MoM Reflection Summary (from 02, no new facts)

Baseline claude-fable-5-2026-06-10 (SAME_MODEL_BASELINE): its defensive top-5 failed (MCK/COST/WMT/CVX all negative alpha; basket -3.08% mean alpha vs SPY +4.07%) while its monitor sleeve outperformed (MU +5.8%, ABBV +5.8% alpha) — the HIGH_VOL defensive tilt was wrong within days. Validated themes: managed-care recovery (UNH 4 straight HITs; HUM now #4), GLP-1/defensive pharma (LLY 4 straight HITs), AI-networking (ANET +11.9% settled alpha today). Carry-forwards binding today: LLY/ABBV/LIN/ANET in; UNH/GE event-excluded (07-16 prints); 8 DROPs confirmed.

## Market Regime Assessment

| Metric | Observation | Ledger | Implication |
|---|---|---|---|
| Regime | **NEUTRAL** (8th consecutive label; no session since 07-10) | L019 | Momentum-led defensive leaderboard is regime-consistent |
| Index | SPY 754.95 record close, BULLISH MA alignment, dd -0.61% | L004, L010 | Trend intact |
| Vol | VIX 15.03 = 60d low; but SOXX rvol 74% (1.7x prior), QQQ 29% (1.9x) | L007, L011-L012 | Growth complex digesting under a calm index |
| Semis | SOXX below MA20, -11.25% from 60d high; premkt -3.3% this morning (context only) | L006, L016 | Digestion extending into Monday |
| Rates | TLT quiet (20d -0.5%) | L009 | No rate shock |
| Data quality | DELAYED; 0 UNAVAILABLE Required fields; DQ ×0.80 (families) | L020 | NO_TRADE on construction, not data |

## Core ETF Market Forecast (summary of 03, no new facts)

| ETF | Entry (7/10) | mu | sigma | Target 8/10 | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 754.95 | +0.5% | 4.37% | 758.72 | 724.42–793.02 | MEDIUM |
| QQQ | 725.51 | +0.8% | 8.43% | 731.31 | 667.71–794.92 | MEDIUM |
| SOXX | 581.34 | +1.7% | 21.43% | 591.22 | 461.65–720.79 | LOW |

## Ranked Forecasts (NOT positions; full blocks in 05, records in 15)


| Rank | Ticker | Entry (DELAYED 7/10) | Pctl | mu | sigma(1m) | Target 8/10 | CI70 | TD9 D | RSI D | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DVA | 232.8 | 100.0 | +5.0% | 7.0% | 244.44 | 227.56-261.32 | BUY_SETUP_2 | 74 | LOW |
| 2 | CRL | 233.41 | 99.8 | +6.0% | 14.1% | 247.41 | 213.29-281.54 | SELL_SETUP_2 | 74 | LOW |
| 3 | CRWD | 187.18 | 99.6 | +6.0% | 16.5% | 198.41 | 166.24-230.58 | BUY_SETUP_1 | 57 | LOW |
| 4 | HUM | 392.22 | 99.4 | +5.0% | 10.9% | 411.83 | 367.33-456.33 | BUY_SETUP_1 | 66 | LOW |
| 5 | DDOG | 257.54 | 99.2 | +6.0% | 18.6% | 272.99 | 223.25-322.73 | SELL_SETUP_2 | 61 | LOW |
| 6 | FTNT | 157.51 | 99.0 | +5.0% | 12.8% | 165.39 | 144.49-186.28 | BUY_SETUP_1 | 60 | LOW |
| 7 | DOC | 21.65 | 98.8 | +6.0% | 7.8% | 22.95 | 21.19-24.7 | BUY_SETUP_2 | 62 | LOW |
| 8 | CSCO | 121.31 | 98.6 | +6.0% | 11.7% | 128.59 | 113.89-143.28 | SELL_SETUP_2 | 58 | LOW |
| 9 | BEN | 33.5 | 98.4 | +5.0% | 8.2% | 35.18 | 32.31-38.04 | BUY_SETUP_3 | 56 | LOW |
| 10 | AXON | 565.8 | 98.2 | +6.0% | 21.7% | 599.75 | 472.18-727.32 | BUY_SETUP_2 | 61 | LOW |

Ranks 11-20: TROW, FFIV (-0.10 penalty, earnings 14d), AIZ, TTWO, CVS, BBY, MRNA, DAL, ABNB, PANW. Carry-forwards: ANET 86.0 pctl (mu +4%), LLY 85.4 (+3%), LIN 84.0 (+3%), ABBV 77.6 (+1%). All LOW confidence (2/4 families).

## Portfolio Analytics / No-Trade Rationale

No portfolio: the investable set is empty at the family gate, and the §0 feasibility pre-check additionally shows the defensive leaderboard (weighted beta ≈0.66) cannot reach the protected 0.90–1.10 beta band under the caps — the same composition infeasibility as the 06-10 baseline. Construction was not attempted; no revision pass was spent (07).

## Assumptions and Limitations

Prices are Friday's close read pre-open Monday (DELAYED); premarket shows semis -3.3% — the 12:15 checkpoint should re-read the growth complex. Fund_Z/Sent_Z families are UNAVAILABLE universe-wide (DQ 0.80, LOW confidence, standing HUMAN_REVIEW escalation). Sortino not computed this run. VaR/CVaR are parametric (normality assumed). Market-cap filter is inferred from index membership. Earnings-date vendor field is authoritative but one name (DAL) is cadence-estimated (±5d, outside horizon).

## Next Scheduled Review

Midday monitor 12:15 ET (manual); pre-close 15:45; close log 16:20; evolution 17:00 (folded into this package's 13). Next full pre-open run: Tuesday 2026-07-14 — re-evaluate the banks wave names as they print, and UNH/GE after 07-16.
