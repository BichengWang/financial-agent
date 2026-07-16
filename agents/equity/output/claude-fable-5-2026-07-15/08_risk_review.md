# 08 Risk Review — 2026-07-15

**Committee decision: APPROVE** publication as **NO_TRADE** with a 24-name monitoring sleeve, 3 MARKET_FORECAST records, and 17 settlements.

## Checklist Findings

1. **Fabricated/weak inputs — none found.** Every published price is a 2026-07-14 close fetched this run (L002); the 17 settlement prices were tool-verified against IBKR (16/17 exact to the cent; FCX's $0.15 gap identified as an ex-dividend adjustment and the unadjusted close correctly used against the unadjusted entry — L016).
2. **Price/derived-field citations — clean.** Spot-checked DVA, CRWD, FTNT, ANET, ABBV: entry has date+tag; target = entry×(1+mu) exact; CI = entry×(1+mu±1.04σ) exact; per-name ledger blocks L053–L220. One error was caught **before publication** during assembly: an early draft of 06 carried hand-written target/CI values that disagreed with the computed blocks (CVS, FFIV, CRL, EXPD, NTAP, MPC, FTNT, DDOG, ANET); 06 was regenerated from `final_tables` values. Root cause (hand transcription of numeric tables) and its process fix are noted in 13 §What Failed.
3. **Sigma discipline — clean.** All 24 sigmas are per-name REALIZED_VOL_30D (range 4.68%–18.64%); no round free-handed values; MF sigmas likewise (4.40/8.59/21.90%).
4. **Score attribution — complete.** Every ranked name shows the full trace with Fund/Sent at `0.00 (UNAVAILABLE)`, DQ 0.80, explicit penalties, drivers, and metric ledger rows. Missing families counted toward nothing.
5. **mu discipline — compliant.** All mu values from the Calibration Table band by post-penalty percentile; exhaustion −1pp applications and the single band-floor suspension (ABBV) disclosed; MF mu from the regime-prior table with one bounded adjustment (SOXX −0.5pp, ledger-backed, inside the ±1.5pp band).
6. **Event concentration — the defining risk this run.** The wave is printing *through* the run: 8 shortlist names printed by this morning (their entries are pre-print closes — flagged per name), 3 more print tomorrow. Under a GO this would violate Downgrade #4; under NO_TRADE it is a monitoring-sleeve caveat, correctly surfaced in 05/06 and in each affected prediction's thesis. The committee flags **pre-print entry prices** (GS, MS, ELV, and print-week estimates BAC/JPM in the near-miss log) as the sleeve's largest single distortion risk for the 08-12 settlement — acceptable only because nothing is sized.
7. **GO-blocking discipline — correct.** The only GO blocker cited is the family-coverage evidence threshold (structural); all five Required inputs are grounded (00 GO-Gate Table); Enhancing gaps are treated as DQ/confidence caps.
8. **Prediction-record completeness — verified.** 27 records (24 EQ with score_explainability + benchmark_price 751.83, 3 MF), 17 settlements with timing flags; every ranked name has a record; JSON validated.
9. **Technical indicator lineage — clean.** All TD9/RSI/MACD/MA/momentum/VR/RS fields trace to `technical_indicators.json` (518/518) and per-name ledger rows; no indicator used as a standalone signal; exhaustion flags feed penalties/mu only.
10. **Settlement-base correction (02 §0) — endorsed.** The strict prediction-identity dedupe (91 EQ + 12 MF distinct vs the previously reported 135) is a *reporting* correction that strengthens evaluation integrity; no protected rule touched; logged as the run's single Track B change with HUMAN_REVIEW flag (13). The committee notes the corrected base sharpens two watch-items: rank IC negative three consecutive vintages, and CI coverage 83.5% near the 85% ceiling.
11. **Live-sounding language — checked.** Names that printed this morning are consistently labeled as scored on pre-print closes; intraday IBKR observations are labeled LIVE verification rows, not scoring inputs.

## Top Three Concerns (severity order)

1. **Pre-print entries inside the sleeve** (GS/MS/ELV published, STT/UNH/GE gating) — forecasts anchored to closes that the market has already repriced intraday. Mitigated by NO_TRADE status, explicit flags, and tomorrow's re-evaluation binding (02 §5).
2. **Composite ordering quality decaying in this tape** — vintage IC −0.248 today, third negative in a row; weighted mean +0.040 is one bad vintage from the automatic MEDIUM cap. The committee endorses the evolution agent's framing (factor calibration diagnosis) and expects the cap to bind imminently absent a trending tape.
3. **Fund/Sent unwiring (13th run)** — the standing structural blocker; escalation unchanged (wire a feed or adopt a 2-family standard by human decision).

## Final Publication Recommendation

**NO_TRADE** — publish the full package. No revision required.
