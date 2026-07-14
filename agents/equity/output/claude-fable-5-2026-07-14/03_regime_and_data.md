# 03 Regime and Data — 2026-07-14

## Data Mode Declaration

**DELAYED** — all scored prices are 2026-07-13 Monday closes fetched this run (Nasdaq historical API bulk, L002; retrieval timestamps in `price_history_fetch_manifest.json`). Yahoo v8 was HTTP-429 blocked for the entire session (second consecutive; probe L019) — the codified source chain (Track B accepted 07-13) executed exactly as designed: Nasdaq bulk 517/519 → IBKR straggler (BF-B conid 4931) → IBKR verification **13/13 exact to the cent** (L016). VIX from CBOE CSV (L007); rf from Treasury.gov after FRED timed out ×3 (L008). One symbol excluded: FDXF (32 bars, recent listing; L001). Zero UNAVAILABLE Required fields → GO-eligible on data; run is intraday so all fields are prior-close based.

## Regime Classification: **NEUTRAL** (9th consecutive label; L014)

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MAs | 749.17 > MA20 744.38 > MA50 741.99 (BULLISH alignment) — but -0.77% Monday | L004, L010 |
| VIX | 17.16; 20d mean 17.00, range 15.03–19.49 — mid-range, not HIGH_VOL | L007 |
| QQQ internals | Below MA20 (722.30), MACD below signal, rvol 8.54% ≈ 1.9x prior window, -4.61% off 60d high | L011 |
| SOXX internals | Below MA20 AND MA50; -15.48% off 60d high; rvol 21.8% ≈ 2x prior; -4.77% Monday alone | L012 |
| Relative strength | QQQ/SPY 20d -2.26% (60d +4.33%); SOXX/SPY 20d **-7.11%** (60d +28.71%) | L013 |
| Rates / duration | TLT 83.97, mom20 -2.34% — mild duration pressure, no rate shock | L009 |

Call: a violent growth/semi correction **inside** an intact broad-market uptrend. Not BULL (breadth is defensive, momentum leaders are HC/staples/REITs); not HIGH_VOL (VIX 17, SPY realized 4.4% 1m); not BEAR/RATE_SHOCK. NEUTRAL with defensive rotation. Consistency check: the leaderboard (05) is defensive/low-vol momentum — regime-consistent.

## Event Concentration

The banks/insurers/managed-care earnings wave is **inside 3 days**: ELV/JBHT/MTB/PNC/BNY print 07-15, STT/UNH/GE 07-16, RF 07-17 (all confirmed; L015). 9 shortlist names carry the -0.10 penalty. FOMC: next meeting outside the 14-day window. This is the second consecutive run where the event gate reshapes the top-30 — expected to unwind progressively from Thursday.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 749.17 | 2026-07-13 | DELAYED | Above both (BULLISH) | 4.39% (1m) | 1.00 | +0.5% | 4.39% | REALIZED_VOL_30D | 752.92 | 2026-08-11 | 718.71 | 787.12 | MEDIUM | L004, L010 |
| QQQ | 711.74 | 2026-07-13 | DELAYED | Below 20d, above 50d (MIXED) | 8.54% (1m) | 1.686 (DERIVED, 60d) | +0.84% | 8.54% | REALIZED_VOL_30D | 717.72 | 2026-08-11 | 654.50 | 780.93 | LOW | L005, L011 |
| SOXX | 553.61 | 2026-07-13 | DELAYED | Below both (broken) | 21.80% (1m) | 3.59 (DERIVED, 60d — window spans melt-up + correction, disclosed) | +0.30% | 21.80% | REALIZED_VOL_30D | 555.27 | 2026-08-11 | 438.06 | 689.09 | LOW | L006, L012 |

mu derivation (rules.md §Core ETF): NEUTRAL SPY prior +0.5%, no adjustment. QQQ = 1.686 × 0.5 = +0.84%, no adjustment (evidence mixed: 60d RS +4.33% vs 20d RS -2.26%). SOXX = 3.59 × 0.5 = +1.80%, adjusted **-1.5pp (max band) to +0.30%** on ledger-backed deterioration: below both MAs, 20d RS -7.11%, MACD below signal, rvol 2x prior window (L012, L013) — a deliberate near-flat call; at |mu| < 0.5% direction settles N/A-FLAT_CALL and the record scores on CI/z only. Confidence: SPY MEDIUM (trend+vol align with regime); QQQ/SOXX LOW (trend and RS disagree with positive beta-derived mu).

Relative-strength note: SOXX/SPY 60d +28.71% vs 20d -7.11% is the widest momentum-vs-reversal gap in the ledger's history of this block — the semi complex is unwinding an extreme. Regime consistency: intact.

## Universe Handoff

`build_index_universe.py`: 515 union (503 S&P 500 + 101 NDX, 89 overlap; caches 2026-06-21, L001) → 514 eligible after FDXF exclusion (32 bars, listing age <6mo). Inclusion filters passed by all 514: price >$5 (min in-universe ~$9), 20d ADDV >$20M (all pass at index-cap scale), history ≥65 bars. Rejection log: FDXF only. Handoff to technical_indicators.py: 514 + SPY/QQQ/SOXX (+TLT context) — executed, 517/518 OK (L003).

## Ledger Coverage Gaps Affecting Scoring

Fundamental and Sentiment family feeds: unwired at index-union scale (12th consecutive run) — Enhancing-class per rules.md §Input Classification; DQ 0.80, confidence cap LOW, never a GO blocker. Options IV / short interest / bid-ask tape: unwired (same class). All five Required inputs: GROUNDED (see 00 GO-Gate Table).
