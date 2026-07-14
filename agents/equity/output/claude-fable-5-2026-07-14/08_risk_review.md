# 08 Risk Review — 2026-07-14

## Committee Decision: **APPROVE** (publication as NO_TRADE with 24-name monitoring sleeve + 3 ETF forecasts + 17 settlements)

## Checklist Findings

1. **Fabrication** — none found. Every published price is DELAYED 2026-07-13 with retrieval timestamps; 13/13 IBKR spot-verification exact to the cent (L016) on a single-web-source day (Yahoo 429, L019). Settlement prices tool-verified.
2. **Price/derived-field citations** — clean. All 24 blocks carry price_date + price_tag; targets/CIs derive from tagged entries per formula.
3. **Sigma discipline** — clean. All 24 + 3 ETF sigmas are REALIZED_VOL_30D with per-name ledger rows; no round free-handed values. Note: SOXX sigma 21.8% (2x prior window) is faithfully wide — the 07-13/07-14 MF MISSes settled IN_CI precisely because sigmas were honest.
4. **Score attribution** — full traces on all 24 (family z → DQ 0.80 → penalties → Adj Score); Fund_Z/Sent_Z displayed as 0.00 (UNAVAILABLE), never imputed.
5. **mu calibration** — table-conformant by post-penalty percentile; the single analyst adjustment class (-1pp exhaustion) is disclosed (L022), and its suspension at the band floor for ABBV (avoiding an unsettleable mu=0) is disclosed in 05 and the trace. SOXX MF -1.5pp adjustment is inside the ±1.5pp band with four cited evidence lines (L012/L013). **Flag for evolution (not blocking):** a deliberate near-flat SOXX call (+0.30%) settles direction-N/A — acceptable under §Settlement Rules, but the committee notes flat calls should stay rare or the MF direction record becomes unscoreable.
6. **Event concentration** — the sleeve itself holds zero names inside the ≤14d window except FFIV (13d, penalized -0.10, rank 18 post-penalty) — within the ≤2-names rule. The gated financials wave is outside the sleeve.
7. **GO-blocking discipline** — correct. All five Required inputs grounded; the run is NO_TRADE on evidence-threshold construction (2/4 families), not on missing Enhancing inputs. No improper block.
8. **Prediction-record completeness** — 24 EQUITY_ALPHA with score_explainability + benchmark_price 749.17, 3 MARKET_FORECAST, 17 settlements with convention flag: complete, gate satisfied.
9. **Technical indicator lineage** — all D/W/M values cite technical_indicators.json (L003) + per-name history rows; no standalone TD9/RSI trade signals; FDXF marked UNAVAILABLE, excluded.
10. **Settlement timing** — TARGET_EQ_RUN_DATE applied to an intraday run (07-14 close nonexistent at run time → 07-13 close): consistent with the established convention and codified into rules.md this run (13, Track B). The committee reviewed the wording and confirms it cannot weaken any grounding gate.

## Top Three Concerns (severity order)

1. **The structural GO blocker is now 12 runs old.** Fund/Sent unwiring caps every run at NO_TRADE regardless of signal quality. The standing HUMAN_REVIEW escalation (wire a feed, or formally adopt a 2-family investable standard with tightened thresholds) is the only path to a publishable portfolio. Nothing in this run's power.
2. **Rank IC softness in flat tapes** (02 §0: -0.08, -0.046 consecutive) — if the weighted mean crosses ≤ 0 at n≥20 joinable, the MEDIUM cap binds automatically next run. Watch, not act.
3. **Regime-prior MF mu is 5/12 on direction** with all misses mu-positive-into-corrections; Track A evidence accumulating (needs ≥20 MF settlements; at 12).

## Final Publication Recommendation: **NO_TRADE** — publish full package.
