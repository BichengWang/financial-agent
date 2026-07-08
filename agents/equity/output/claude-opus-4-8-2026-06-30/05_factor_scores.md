# 05 Factor Scores

Run `claude-opus-4-8` · 2026-06-30 · `SAMPLED_PCTL (n=35)` · Data-Quality multiplier **0.80** (all names).

## Methodology and Family Construction

`Adj Score = (0.30·Fund_Z + 0.30·Tech_Z + 0.25·Sent_Z + 0.15·Macro_Z) · DQ − Penalties`, DQ = 0.80. Z-scores are cross-sectional over the 35-name universe, winsorized at the 5th/95th pctile. **Two families are disclosed price-based proxies** (no fundamentals/short-interest/options/analyst feed — 04):

| Family | Weight | Primary metrics (this run) | Grounded? |
|---|---|---|---|
| Fundamental (quality proxy) | 0.30 | Calmar = mom60/\|DD60\|; inverse realized vol; shallow drawdown | **Proxy** (realized-risk quality) |
| Technical / Price | 0.30 | 60d momentum; RS60 vs SPY; MA alignment (d/w/m); MACD state (d/w) | Genuine (L300–L304, L204–L205) |
| Sentiment / Positioning (proxy) | 0.25 | RS20 vs SPY; RSI-position (favor 45–68, penalize <32/>78); 20d volume ratio | **Proxy** (price/volume positioning) |
| Macro / Regime | 0.15 | low-beta tilt (regime favors defensives); RS60 leadership | Genuine (L202, L205) |

**Penalties** (additive): earnings within buffered 14d+5d window (−0.10); TD9 weekly/monthly SELL_SETUP_9 or monthly RSI ≥ 85 exhaustion (−0.10); realized vol > 2× universe median (−0.10). Momentum/RS appears in more than one proxy family — a disclosed overlap that inflates apparent multi-family confirmation and is why DQ is held at 0.80 and confidence at ≤ MEDIUM.

## Ranked Candidate Table (Top 20)

Entry: LIVE = IBKR (L004–L007); else validated Yahoo (L008–L018). mu = calibration-table prior by percentile (no per-name free-hand adjustment). sigma = REALIZED_VOL_30D. target_date = 2026-07-28. CI = entry·(1+mu±1.04σ). Ratios are `RAW_DIAGNOSTIC` (no rf sourced). Kelly 0.25 shown post-5%-cap.

| # | Tkr | Entry | Tag | Adj | Pctl | Beta | 30dRVol | σ1m | mu | Target | CI70 Lo–Hi | Sleeve | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UNH | 416.49 | LIVE | 0.71 | 100 | −0.16 | 26% | 7.6% | +6.0% | 441.48 | 408.43–474.53 | INVEST-GRADE | LOW¹ |
| 2 | AMD | 576.46 | LIVE | 0.59 | 97 | 3.87 | 76% | 22.0% | +6.0% | 611.05 | 479.21–742.88 | INVEST-GRADE | LOW² |
| 3 | V | 342.92 | DLY | 0.43 | 94 | −0.01 | 20% | 5.7% | +5.0% | 360.07 | 339.70–380.43 | INVEST-GRADE | MEDIUM |
| 4 | LLY | 1209.29 | LIVE | 0.42 | 91 | 0.22 | 35% | 10.0% | +5.0% | 1269.75 | 1143.74–1395.77 | INVEST-GRADE | LOW¹ |
| 5 | BAC | 57.19 | DLY | 0.41 | 89 | 0.32 | 19% | 5.3% | +4.0% | 59.48 | 56.30–62.66 | INVEST-GRADE | LOW¹ |
| 6 | CAT | 1064.99 | DLY | 0.41 | 86 | 1.93 | 49% | 14.1% | +4.0% | 1107.59 | 950.98–1264.20 | INVEST-GRADE | LOW² |
| 7 | MU | 1146.00 | LIVE | 0.31 | 83 | 4.16 | 121% | 35.0% | +3.0% | 1180.38 | 762.76–1598.00 | INVEST-GRADE | LOW² |
| 8 | GE | 372.11 | DLY | 0.30 | 80 | 1.25 | 31% | 9.0% | +3.0% | 383.27 | 348.37–418.18 | INVEST-GRADE | LOW² |
| 9 | SO | 96.42 | DLY | 0.29 | 77 | −0.23 | 18% | 5.3% | +2.0% | 98.35 | 93.06–103.63 | MONITORING | MEDIUM |
| 10 | LIN | 519.75 | DLY | 0.24 | 74 | 0.12 | 18% | 5.3% | +2.0% | 530.14 | 501.33–558.96 | MONITORING | MEDIUM |
| 11 | JPM | 328.25 | DLY | 0.23 | 71 | 0.29 | 24% | 6.9% | +2.0% | 334.81 | 311.33–358.30 | MONITORING | LOW¹ |
| 12 | JNJ | 255.88 | DLY | 0.18 | 69 | −0.31 | 25% | 7.1% | +1.0% | 258.44 | 239.54–277.33 | MONITORING | LOW¹ |
| 13 | HD | 351.79 | DLY | 0.18 | 66 | 0.76 | 28% | 8.2% | +1.0% | 355.31 | 325.49–385.13 | MONITORING | LOW |
| 14 | TSLA | 416.07 | DLY | 0.16 | 63 | 2.07 | 50% | 14.5% | +1.0% | 420.23 | 357.36–483.10 | MONITORING | LOW |
| 15 | PG | 146.06 | DLY | 0.14 | 60 | 0.02 | 24% | 7.0% | +1.0% | 147.52 | 136.86–158.18 | MONITORING | LOW |
| 16 | AAPL | 288.71 | DLY | 0.11 | 57 | 0.62 | 30% | — | N/A | N/A | N/A | NEAR-MISS | — |
| 17 | NEE | 88.14 | DLY | 0.03 | 54 | −0.01 | 24% | — | N/A | N/A | N/A | NEAR-MISS | — |
| 18 | GOOGL | 357.22 | DLY | −0.02 | 51 | 1.51 | 32% | — | N/A | N/A | N/A | NEAR-MISS | — |
| 19 | AMZN | 239.72 | DLY | −0.03 | 49 | 1.27 | 35% | — | N/A | N/A | N/A | NEAR-MISS | — |
| 20 | RTX | 188.50 | DLY | −0.04 | 46 | 0.23 | 29% | — | N/A | N/A | N/A | NEAR-MISS | — |

¹ Confidence `LOW`: Q2 earnings inside buffered window (UNH/BAC ~15d, JPM ~14d, JNJ ~15d, LLY exhaustion flag). ² Confidence `LOW`: momentum-concentrated and/or exhaustion (TD9-9, RSI extreme, extreme beta). Ranks 16–35 are below the 60th-pctl mu floor → no forecast (rejection/near-miss; see bottom).

## Risk / Return Metrics (ranked sleeve)

| Tkr | Sharpe | Sortino | IR | Treynor | Kelly0.25 (cap) | VaR95 | CVaR95 | MaxDD60 | Metric Ledger |
|---|---|---|---|---|---|---|---|---|---|
| UNH | 0.79 | 1.83 | 0.67 | −0.37 | 5.0% | −6.6% | −9.7% | −6.1% | L200–L209 |
| AMD | 0.27 | 0.49 | 0.01 | 0.02 | 5.0% | −30.3% | −39.3% | −16.6% | L200–L209 |
| V | 0.88 | 2.28 | 0.71 | N/A(β≈0) | 5.0% | −4.4% | −6.8% | −6.7% | L200–L209 |
| LLY | 0.50 | 1.22 | 0.44 | 0.23 | 5.0% | −11.5% | −15.6% | −10.9% | L200–L209 |
| BAC | 0.75 | 1.23 | 0.62 | 0.12 | 5.0% | −4.8% | −7.0% | −8.4% | L200–L209 |
| CAT | 0.28 | 0.50 | 0.10 | 0.02 | 5.0% | −19.3% | −25.1% | −9.0% | L200–L209 |
| MU | 0.09 | 0.17 | **−0.14** | 0.01 | 5.0% | −54.8% | −69.2% | −20.0% | L200–L209 |
| GE | 0.33 | 0.44 | 0.11 | 0.02 | 5.0% | −11.9% | −15.6% | −13.1% | L200–L209 |
| SO | 0.38 | 0.59 | 0.45 | −0.09 | 5.0% | −6.7% | −8.9% | −8.8% | L200–L209 |
| LIN | 0.38 | 0.70 | 0.34 | 0.17 | 5.0% | −6.8% | −9.0% | −4.2% | L200–L209 |
| JPM | 0.29 | 0.57 | 0.25 | 0.07 | 5.0% | −9.4% | −12.2% | −6.7% | L200–L209 |
| JNJ | 0.14 | 0.30 | 0.24 | −0.03 | 5.0% | −10.7% | −13.6% | −8.3% | L200–L209 |
| HD | 0.12 | 0.25 | −0.02 | 0.01 | 5.0% | −12.4% | −15.8% | −15.2% | L200–L209 |
| TSLA | 0.07 | 0.13 | −0.21 | 0.00 | 5.0% | −23.0% | −28.9% | −15.8% | L200–L209 |
| PG | 0.14 | 0.32 | 0.15 | 0.00 | 5.0% | −10.6% | −13.5% | −6.0% | L200–L209 |

Raw Kelly is large for low-σ names (mu/σ² form) but the **5% single-name cap binds for every name**; no name has Kelly ≤ 0 (no Kelly investability block). MU IR is **negative** — momentum without risk-adjusted edge.

## Score Attribution (per ticker)

| Tkr | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Comp_Z | DQ | Pen | Adj | Top + Drivers | Top − Drivers |
|---|---|---|---|---|---|---|---|---|---|---|
| UNH | +1.52 | +1.33 | +0.37 | +1.26 | +1.14 | 0.80 | 0.20 | 0.71 | Fund/Macro quality, RS60 +36 | earnings ~15d; TD9-9 |
| AMD | +0.14 | +1.80 | +1.41 | +0.37 | +0.99 | 0.80 | 0.20 | 0.59 | Tech/Sent momentum, RS60 +152 | rvol 76%, β3.9, TD9-9 |
| V | +0.82 | +0.55 | +0.22 | +0.44 | +0.53 | 0.80 | 0.00 | 0.43 | Fund quality, low vol 20% | — (clean) |
| LLY | +0.42 | +0.98 | +0.52 | +0.64 | +0.65 | 0.80 | 0.10 | 0.42 | balanced 4-family, RS60 +16 | TD9-9 (weekly) |
| BAC | +0.74 | +0.58 | +0.77 | +0.31 | +0.64 | 0.80 | 0.10 | 0.41 | balanced 4-family | earnings ~15d |
| CAT | +0.58 | +1.38 | +0.57 | +0.19 | +0.76 | 0.80 | 0.20 | 0.41 | Tech momentum, RS60 +35 | rvol 49%, RSI86, TD9-9 |
| MU | −0.06 | +1.80 | +0.76 | +0.37 | +0.77 | 0.80 | 0.30 | 0.31 | Tech momentum, RS60 +199 | rvol 121%, β4.2, DD−20, TD9-9 |
| GE | +0.36 | +1.05 | **−0.33** | +0.20 | +0.37 | 0.80 | 0.00 | 0.30 | Tech, RS60 +19 | Sent_Z neg; momentum-only |
| SO | +0.46 | +0.46 | +0.17 | +0.23 | +0.36 | 0.80 | 0.00 | 0.29 | Fund quality, low vol 18% | RS60 −15 |
| LIN | +0.71 | +0.12 | +0.11 | +0.15 | +0.30 | 0.80 | 0.00 | 0.24 | Fund quality, DD −4% | RS60 −10; low mu |
| JPM | +0.69 | +0.49 | +0.08 | +0.24 | +0.41 | 0.80 | 0.10 | 0.23 | Fund quality, DD −7% | earnings ~14d |
| JNJ | +0.46 | +0.60 | −0.12 | +0.41 | +0.35 | 0.80 | 0.10 | 0.18 | Fund/Macro defensive | RS60 −8; earnings ~15d |
| HD | +0.08 | +0.37 | +0.38 | −0.04 | +0.22 | 0.80 | 0.00 | 0.18 | Tech/Sent recent | proxy overlap; IR ~0 |
| TSLA | −0.33 | +0.48 | +0.96 | −0.56 | +0.20 | 0.80 | 0.00 | 0.16 | Sent positioning | Fund/Macro neg; β2.1, rvol50% |
| PG | +0.53 | −0.44 | +0.47 | +0.18 | +0.17 | 0.80 | 0.00 | 0.14 | Fund/Sent defensive | Tech_Z neg; RS60 −12 |

## Metric Availability

| Metric Group | Sourceable | UNAVAILABLE | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Risk / return (σ, β, DD, Sharpe, Sortino, IR, Treynor, Kelly, VaR, CVaR) | 35/35 | 0 | genuine input | rf not sourced → ratios `RAW_DIAGNOSTIC` |
| Technical pack (TD9/RSI/MACD/MA/mom/RS/vol) | 35/35 | 0 | genuine Tech_Z | from technical_indicators.json |
| Fundamental (true revisions/margins/FCF) | 0/35 | 35/35 | proxy → DQ 0.80 | quality proxy substituted, disclosed |
| Sentiment (true short/options/analyst) | 0/35 | 35/35 | proxy → DQ 0.80, conf ≤ MEDIUM | price/volume proxy substituted |
| Earnings date | 35/35 (ESTIMATED ±5d) | 0 | penalty on buffered window | cadence estimates, not confirmed |

No `Adj Score` cites a metric absent from `01_preflight.md`; no missing metric is treated as neutral or supportive (proxies are labeled, premium feeds are `UNAVAILABLE`).

## Technical Indicator Summary (ranked sleeve + flags)

| Tkr | TD9 d/w/m | RSI d/w/m | MACD d/w/m | MA-align d/w/m | RS20/RS60 | Indicator Ledger |
|---|---|---|---|---|---|---|
| UNH | S6/–/– | 61/65/52 | ABOVE/ABOVE/ABOVE | BULL/BULL/BULL | +11/+36 | L300–L304 |
| AMD | S2/–/– | 64/77/83 | BELOW/ABOVE/ABOVE | BULL/–/– | +15/+152 | L300–L304 |
| V | S5/–/– | 67/60/58 | ABOVE/ABOVE/BELOW | BULL/BULL/BULL | +8/+0 | L300–L304 |
| LLY | S5/–/– | 69/68/68 | ABOVE/ABOVE/ABOVE | BULL/BULL/BULL | +13/+16 | L300–L304 |
| BAC | B2/–/– | 64/61/65 | ABOVE/ABOVE/B-CROSS | BULL/BULL/– | +13/+2 | L300–L304 |
| CAT | S2/–/– | 65/**86**/86 | ABOVE/ABOVE/ABOVE | BULL/BULL/– | +25/+35 | L300–L304 |
| MU | S2/–/9? | 60/82/**92** | BULL/ABOVE/ABOVE | BULL/–/– | +12/+199 | L300–L304 |
| GE | **S9**/–/– | 73/68/75 | ABOVE/ABOVE/B-CROSS | BULL/BULL/– | +16/+19 | L300–L304 |
| SO | S6/–/– | 60/56/60 | ABOVE/B-CROSS/BELOW | BULL/–/– | +10/−15 | L300–L304 |
| LIN | S1/–/– | 55/60/64 | BELOW/ABOVE/ABOVE | BULL/BULL/– | +6/−10 | L300–L304 |
| SOXX(ref) | S2/**S9**/**S9** | 59/75/**89** | BELOW/ABOVE/ABOVE | BULL/BULL/BULL | +13/+74 | 03 |

(`S`=SELL_SETUP, `B`=BUY_SETUP; bold = exhaustion flag. Full d/w/m for all 35 in `technical_indicators.json`.) TD9-9 / RSI-extreme are treated as **exhaustion flags** (penalty + confidence cap), never standalone signals; MACD supports only when aligned with momentum + RS.

## Investability Gate Determination

A name is investable only if: pctl ≥ 80 **and** ≥ 3 of 4 families non-negative **and** no single family > 50% of composite conviction **and** data completeness ≥ 85% **and** no hard stop.

| Tkr | pctl ≥ 80 | 3/4 fams ≥ 0 | max family ≤ 50% | Verdict |
|---|---|---|---|---|
| UNH | ✓ | 4/4 | Fund 40% | **INVESTABLE** |
| V | ✓ | 4/4 | Fund 46% | **INVESTABLE** |
| LLY | ✓ | 4/4 | Tech 46% | **INVESTABLE** |
| BAC | ✓ | 4/4 | Fund 35% | **INVESTABLE** |
| AMD | ✓ | 4/4 | **Tech 55%** | reject — momentum-concentrated |
| CAT | ✓ | 4/4 | **Tech 55%** | reject — momentum-concentrated |
| MU | ✓ | 3/4 | **Tech 70%** | reject — momentum-concentrated + exhaustion |
| GE | ✓ | 3/4 | **Tech 85%** | reject — momentum-concentrated, Sent neg |

**Only 4 names (UNH, V, LLY, BAC) clear the full investability gate — below the 5-name minimum.** The four ≥80th-pctl rejects are momentum-dominated (Tech_Z is 55–85% of conviction) and three are exhausted high-beta semis/cyclicals. This triggers **NO_TRADE #1** (fewer than 5 names pass). Sizing feasibility is examined in 07 (also infeasible). Score trace example — **UNH**: `(0.30·1.52 + 0.30·1.33 + 0.25·0.37 + 0.15·1.26)·0.80 − 0.20 = (0.456+0.399+0.0925+0.189)·0.80 − 0.20 = 1.137·0.80 − 0.20 = 0.909 − 0.20 = 0.71`.

## Rejection / Near-Miss Log (ranks 16–35, pctl < 60 → not ranked)

AAPL (57), NEE (54), GOOGL (51), AMZN (49), RTX (46), PLD (43), GS (40), AMT (37), COST (34), NVDA (31), FCX (29), WMT (26), CVX (23), XOM (20), MSFT (17), META (14), AVGO (11), NOW (9), NFLX (6), PLTR (3). The bottom cohort (MSFT/META/AVGO/NOW/NFLX/PLTR) are the broken mega-cap-growth leaders confirming the reflection `DROP` decisions (02 §5); energy (XOM/CVX) and rate-sensitive REITs (AMT/PLD) screen weak on negative RS. None carries a forecast (below the 60th-pctl mu floor; rejection log only).
