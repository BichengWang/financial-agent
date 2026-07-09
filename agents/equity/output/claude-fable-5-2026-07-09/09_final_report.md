```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-09
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

Live run on fresh intraday data (521/521 symbols, two-source verified to 0.121%, IBKR-corroborated): regime stays **NEUTRAL** for a fourth session as SPY holds trend (751.17, above both MAs, VIX 16.0) and the semis correction repairs sharply intraday (SOXX +4.9%). The second settlement pass in system history closed the 17-record gpt-5 2026-06-11 vintage at 9/17 alpha HITs with 82% CI coverage and rank IC +0.35 — cumulative calibration now n=29: hit rate 51.7%, CI coverage 72.4%, weighted rank IC -0.007, which technically trips the ≤0 trigger and routes a calibration review to evolution (rejected for action on contradictory per-vintage signs; see 13). Scoring publishes a 23-name monitoring sleeve led by DVA, FTNT, PANW, DDOG, TROW, but the standing family-coverage gate (Fundamental + Sentiment feeds unwired, 9th consecutive run) leaves the investable set empty → **NO_TRADE**.

## MoM Reflection Summary (from 02 — no new facts)

Baseline claude-fable-5-2026-06-10 (SAME_MODEL_BASELINE, 29d old) fully settled 07-08; today's pass settled the cross-model gpt-5 06-11 vintage: healthcare validated again (LLY/UNH/ABBV/JNJ all HIT, +2.7 to +9.6% alpha), financials validated (BAC/GS/JPM 3/3 HIT), energy failed again (CVX/COP MISS — the systematic cross-model error), ANET best in vintage (+15.3% alpha), ORCL worst (-21.9%, OUT_CI_LOW). Carry-forwards: LLY/ABBV/LIN CARRY (published); UNH DOWNGRADE retained (earnings 07-15); ANET PROMOTE (naturally ranked #19); eight prior DROPs confirmed.

## Regime Table

| Field | Value | Ledger |
|---|---|---|
| Regime | NEUTRAL (4th consecutive live session) | L007–L012 |
| Data quality | LIVE, DQ 0.80 (Enhancing feeds unwired); all 5 Required inputs grounded | L001–L005 |
| Key macro risk | Q2 earnings season opened today (banks 07-14..17); FOMC 07-28/29 inside every target window; SOXX vol regime 74.7% ann | 03 |

## Core ETF Market Forecast (summary of 03 — no new facts)

| ETF | Entry (LIVE 2026-07-09) | mu | sigma | Target 2026-08-06 | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 751.17 | +0.50% | 4.3% | 754.93 | [720.97, 788.88] | MEDIUM |
| QQQ | 723.25 | +0.84% | 8.4% | 729.33 | [665.93, 792.73] | MEDIUM |
| SOXX | 586.71 | +1.74% | 21.6% | 596.92 | [465.36, 728.49] | LOW |

## Ranked Candidates (23-name MONITORING sleeve — summary of 05/06, no new facts)

| # | Ticker | Pctl | Adj Score | Score Trace | Entry | mu | Target | 70% CI | TD9 D/W/M | RSI D/W/M | Flags | Thesis (compact) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DVA | 100.0 | +0.526 | `(0.30*+1.74+0.15*+0.91)*0.80-0.00` | 226.79 | +6.0% | 240.4 | [223.5, 257.3] | BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_6 | 67/76/73 | none | Dialysis oligopoly re-rating; defensive HC momentum leader |
| 2 | FTNT | 99.8 | +0.426 | `(0.30*+1.65+0.15*+0.67)*0.80-0.05` | 163.27 | +5.0% | 171.43 | [149.56, 193.31] | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_5 | 68/85/79 | EXHAUSTION | Firewall refresh + SASE attach |
| 3 | PANW | 99.6 | +0.414 | `(0.30*+2.00+0.15*-0.12)*0.80-0.05` | 336.45 | +5.0% | 353.27 | [291.53, 415.0] | BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_3 | 64/77/74 | EXHAUSTION | Platformization-led security demand |
| 4 | DDOG | 99.4 | +0.404 | `(0.30*+1.92+0.15*-0.47)*0.80-0.00` | 267.87 | +6.0% | 283.94 | [233.47, 334.42] | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 70/75/75 | none | Observability + AI-workload monitoring |
| 5 | TROW | 99.2 | +0.374 | `(0.30*+1.25+0.15*+1.04)*0.80-0.05` | 118.13 | +5.0% | 124.04 | [116.13, 131.95] | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 70/71/56 | EXHAUSTION | Flows inflection at discounted asset manager |
| 6 | FFIV | 99.0 | +0.366 | `(0.30*+1.46+0.15*+0.97)*0.80-0.10` | 429.98 | +6.0% | 455.78 | [416.79, 494.77] | SELL_SETUP_1/SELL_SETUP_3/SELL_SETUP_6 | 68/77/77 | EARNINGS | App-delivery/security refresh, low vol |
| 7 | BEN | 98.8 | +0.364 | `(0.30*+1.17+0.15*+1.10)*0.80-0.05` | 33.94 | +5.0% | 35.64 | [32.73, 38.55] | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_7 | 60/75/66 | EXHAUSTION | Asset-manager torque to risk-on flows |
| 8 | PRU | 98.6 | +0.352 | `(0.30*+1.26+0.15*+0.83)*0.80-0.05` | 115.71 | +5.0% | 121.5 | [113.49, 129.5] | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_2 | 68/64/57 | EXHAUSTION | Retirement/insurance flows re-rate, low vol |
| 9 | CRWD | 98.4 | +0.336 | `(0.30*+1.47+0.15*-0.13)*0.80-0.00` | 197.97 | +6.0% | 209.85 | [176.72, 242.98] | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 68/75/73 | none | Endpoint/identity consolidation winner |
| 10 | CRL | 98.2 | +0.333 | `(0.30*+1.34+0.15*+0.09)*0.80-0.00` | 230.99 | +6.0% | 244.85 | [210.73, 278.98] | SELL_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 73/66/58 | none | Preclinical CRO demand recovery |
| 11 | HUM | 98.0 | +0.325 | `(0.30*+1.32+0.15*+0.48)*0.80-0.05` | 394.68 | +5.0% | 414.42 | [370.09, 458.75] | BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_3 | 69/76/61 | EXHAUSTION | Managed-care recovery momentum |
| 12 | AXON | 97.9 | +0.323 | `(0.30*+1.81+0.15*-0.51)*0.80-0.05` | 576.79 | +6.0% | 611.4 | [482.24, 740.56] | BUY_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 63/58/54 | HIGH_VOL | Taser/body-cam ecosystem lock-in |
| 13 | TTWO | 97.7 | +0.308 | `(0.30*+1.08+0.15*+0.41)*0.80-0.00` | 244.45 | +6.0% | 259.11 | [234.15, 284.08] | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_3 | 56/57/59 | none | GTA VI cycle anticipation |
| 14 | DAL | 97.5 | +0.304 | `(0.30*+1.41+0.15*+0.55)*0.80-0.10` | 88.59 | +6.0% | 93.91 | [83.83, 103.98] | BUY_SETUP_4/SELL_SETUP_8/SELL_SETUP_3 | 57/66/69 | EARNINGS | Airline momentum; Q2 print landed today |
| 15 | AIZ | 97.3 | +0.298 | `(0.30*+1.10+0.15*+0.69)*0.80-0.05` | 278.13 | +5.0% | 292.04 | [276.55, 307.52] | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_3 | 72/74/71 | EXHAUSTION | Specialty insurance compounder |
| 16 | LYV | 97.1 | +0.297 | `(0.30*+0.76+0.15*+0.95)*0.80-0.00` | 182.52 | +6.0% | 193.47 | [180.86, 206.08] | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 63/65/67 | none | Live-events secular demand |
| 17 | BAX | 96.9 | +0.286 | `(0.30*+1.01+0.15*+0.35)*0.80-0.00` | 22.43 | +6.0% | 23.78 | [21.18, 26.37] | BUY_SETUP_1/SELL_SETUP_8/SELL_SETUP_2 | 63/60/41 | none | Post-restructuring margin recovery |
| 18 | MNST | 96.7 | +0.277 | `(0.30*+0.87+0.15*+0.99)*0.80-0.05` | 95.85 | +5.0% | 100.64 | [95.69, 105.59] | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 61/71/72 | EXHAUSTION | Energy-drink share stability, low beta |
| 19 | ANET | 96.5 | +0.270 | `(0.30*+1.53+0.15*-0.80)*0.80-0.00` | 184.98 | +6.0% | 196.08 | [160.23, 231.93] | SELL_SETUP_2/SELL_SETUP_2/SELL_SETUP_4 | 62/64/69 | none | AI-networking capex; settled +15.3% alpha HIT today |
| 20 | DELL | 96.3 | +0.269 | `(0.30*+2.00+0.15*-1.33)*0.80-0.05` | 457.08 | +6.0% | 484.5 | [328.91, 640.1] | SELL_SETUP_2/SELL_SETUP_1/SELL_SETUP_5 | 65/82/88 | HIGH_VOL | AI-server backlog torque |
| 21 | LLY | 88.9 | +0.196 | `(0.30*+0.82+0.15*+0.40)*0.80-0.05` | 1208.68 | +3.0% | 1244.94 | [1120.31, 1369.57] | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_3 | 62/68/68 | EXHAUSTION | GLP-1 franchise; carry — 2 settled HITs |
| 22 | ABBV | 78.7 | +0.144 | `(0.30*+0.75+0.15*+0.12)*0.80-0.05` | 248.37 | +1.0% | 250.85 | [225.81, 275.89] | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 61/62/65 | EXHAUSTION | Skyrizi/Rinvoq momentum; carry — settled HIT again today |
| 23 | LIN | 74.6 | +0.119 | `(0.30*+0.11+0.15*+0.76)*0.80-0.00` | 524.22 | +2.0% | 534.7 | [501.27, 568.14] | BUY_SETUP_2/SELL_SETUP_3/SELL_SETUP_6 | 52/58/64 | none | Industrial-gas compounder; carry |

All 23 names LOW confidence (2/4 factor families sourceable; DQ 0.80). Full metric blocks, ratios, and ledger citations: 05/06.

## Portfolio Analytics / No-Trade Rationale

**NO_TRADE — stop criterion #1** (fewer than 5 investable names): with Fundamental and Sentiment families UNAVAILABLE universe-wide, no name can satisfy evidence threshold #2 (3-of-4 non-negative families). This is the 9th consecutive scoring run blocked by the same gate; the standing Track B proposal to redefine the threshold over *sourceable* families remains pending HUMAN_REVIEW (see 13). Feasibility pre-check also reconfirms the defensive sleeve would sit below the 0.90 beta floor if sized (07).

## Assumptions and Limitations

- Fund_Z/Sent_Z = 0.00 (UNAVAILABLE) — scores are a momentum/low-vol composite, not a 4-family composite; the settled evidence on whether that composite orders alpha is mixed (IC -0.51 then +0.35 across the two settled vintages).
- Earnings dates are cadence estimates (±5d, INFERRED) over a ~76-name shortlist; buffered penalties applied (28 names). Not evaluated universe-wide (04 limitation).
- Intraday prints (~14:36 ET) as entry prices; VR20 reflects a ~78%-elapsed session; parametric VaR/CVaR assume normality; FOMC 07-28/29 sits inside every target window.
- mu values come from the Calibration Table bands (only documented -1pp exhaustion adjustments); sigma = REALIZED_VOL_30D throughout.

## Next Scheduled Review

Midday/pre-close checkpoints today per runbook (10 covered retroactively at publication; 11/12 pending at ~15:45/16:20 ET if a session is run); next full pipeline: **Friday 2026-07-10 07:27 ET slot (no scheduler job active — manual)**, which also owes `14_weekly_review.md`. Next settlement wave: **2026-07-12 (20 records) → cumulative n=49**, the decisive rank-IC re-test.
