# 03 Regime and Data — 2026-07-15

## Data Mode Declaration

**DELAYED** — all scored prices are 2026-07-14 Tuesday closes fetched this run (Nasdaq historical API bulk, L002; retrieval timestamps in `price_history_fetch_manifest.json`). Yahoo v8 passed a single-quote probe at 19:37Z but 429-blocked the bulk fetch (third consecutive session of bulk blockage; L019) — the codified source chain executed as designed: Nasdaq bulk 518/519 (~65s incl. volume-parse retry for 6 names) → IBKR straggler (BF-B conid 4931, partial today-bar trimmed) → IBKR settlement verification **16/17 exact to the cent** (L016; FCX $0.15 ex-div divergence disclosed). VIX from CBOE CSV (L007); rf from Treasury.gov after FRED timed out (L008). One symbol excluded: FDXF (33 bars, recent listing; L001). Zero UNAVAILABLE Required fields → GO-eligible on data; the run is intraday (~15:5x ET) so all scored fields are prior-close based.

## Regime Classification: **NEUTRAL** (10th consecutive label; L014)

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MAs | 751.83 > MA20 744.89 > MA50 742.65 (BULLISH alignment); +0.36% Tuesday; -1.02% off 60d high | L004, L010 |
| VIX | 16.50; 20d mean 16.99, range 15.03–19.49 — mid-range, easing | L007 |
| SPY realized vol | 4.40% 1m vs 2.88% prior window — rising off a low base | L010 |
| QQQ internals | 719.69 just below MA20 (722.21), above MA50 (717.20); rvol 8.59% ≈ 1.9x prior; -3.55% off 60d high | L011 |
| SOXX internals | +2.58% Tuesday bounce; reclaimed MA50 (562.43), still below MA20 (596.74); -13.30% off 60d high; rvol 21.9% ≈ 1.74x prior | L012 |
| Relative strength | QQQ/SPY 20d -1.57% (60d +4.87%); SOXX/SPY 20d **-6.03%** (60d +30.56%) | L013 |
| Rates / duration | TLT 84.08 below MA20 85.78, rvol 2.65% — mild duration pressure, no rate shock | L009 |

Call: the growth/semi correction **stabilized** on Tuesday (SOXX reclaimed its MA50; QQQ held its MA50) inside an intact broad-market uptrend. Not BULL (leadership remains defensive — HC services, staples, low-vol financials; SPY rvol rising); not HIGH_VOL (VIX 16.5, SPY realized 4.4%); not BEAR/RATE_SHOCK. NEUTRAL with defensive rotation, 10th consecutive session. Consistency check: the leaderboard (05) is defensive/low-vol momentum plus event-gated financials — regime-consistent.

## Event Concentration

The financials/managed-care wave is **printing now**: JPM/GS/MS/BAC and ELV/JBHT/MTB/PNC/BNY have printed as of this morning (vendor announcement fields already cleared — L015, `earnings_calendar_manifest.json`); STT/UNH/GE print tomorrow 07-16; RF 07-17. Twelve shortlist-relevant names carry the -0.10 penalty (9 print-week + STT/UNH/GE at 1d); FTNT/HUM/LII/ESS/MAS/EBAY flipped into the 14-day window today at exactly 14d. FOMC: outside the 14-day window. Names that printed this morning are additionally flagged: their entry prices are **pre-print 07-14 closes** — today's post-print tape is not in any scored field (disclosed per name in 05/06).

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 751.83 | 2026-07-14 | DELAYED | Above both (BULLISH) | 4.40% (1m) | 1.00 | +0.5% | 4.40% | REALIZED_VOL_30D | 755.59 | 2026-08-12 | 721.19 | 789.99 | MEDIUM | L004, L010 |
| QQQ | 719.69 | 2026-07-14 | DELAYED | Below 20d, above 50d (MIXED) | 8.59% (1m) | 1.689 (DERIVED, 60d) | +0.84% | 8.59% | REALIZED_VOL_30D | 725.74 | 2026-08-12 | 661.47 | 790.06 | LOW | L005, L011 |
| SOXX | 567.92 | 2026-07-14 | DELAYED | Below 20d, reclaimed 50d (MIXED) | 21.90% (1m) | 3.596 (DERIVED, 60d — window spans melt-up + correction, disclosed) | +1.30% | 21.90% | REALIZED_VOL_30D | 575.30 | 2026-08-12 | 445.95 | 704.65 | LOW | L006, L012 |

mu derivation (rules.md §Core ETF): NEUTRAL SPY prior +0.5%, no adjustment. QQQ = 1.689 × 0.5 = +0.84%, no adjustment (evidence mixed: 60d RS +4.87% vs 20d RS -1.57%). SOXX = 3.596 × 0.5 = +1.80%, adjusted **-0.5pp to +1.30%** on ledger-backed partial deterioration: 20d RS -6.03%, rvol 1.74x prior window, still below MA20 — offset by the reclaimed MA50 and the +2.58% Tuesday close, so half of yesterday's full-band (-1.5pp) cut (L012, L013). Confidence: SPY MEDIUM (trend+vol align with regime); QQQ/SOXX LOW (trend and RS disagree with beta-derived positive mu). Settlement context feeding this block: the mu-positive MF calls are 4/12 on direction (02 §0) — the priors are applied as the table requires, with adjustments only where the evidence bands allow.

Relative-strength note: SOXX/SPY 60d +30.56% vs 20d -6.03% remains an extreme momentum-vs-reversal gap, one session narrower than yesterday's record. Regime consistency: intact.

## Universe Handoff

`build_index_universe.py`: 515 union (503 S&P 500 + 101 NDX, 89 overlap; caches 2026-06-21, L001) → 514 eligible after FDXF exclusion (33 bars, listing age <6mo). Inclusion filters passed by all 514: price > $5, 20d ADDV > $20M, history ≥126 bars. Rejection log: FDXF only. Handoff to technical_indicators.py: 514 + SPY/QQQ/SOXX (TLT fetched for macro context only) — executed, 518/518 OK (L003).

## Ledger Coverage Gaps Affecting Scoring

Fundamental and Sentiment family feeds: unwired at index-union scale (**13th consecutive run**) — Enhancing-class per rules.md §Input Classification; DQ 0.80, confidence cap LOW, never a GO blocker. Options IV / short interest / bid-ask tape: unwired (same class). All five Required inputs: GROUNDED (see 00 GO-Gate Table).
