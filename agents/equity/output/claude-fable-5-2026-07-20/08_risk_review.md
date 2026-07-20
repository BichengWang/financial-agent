# 08 Risk Review — 2026-07-20 (claude-fable-5, Risk Committee)

**Decision: APPROVE for publication as NO_TRADE.** Final publication recommendation: **NO_TRADE** (live DELAYED mode; valid inputs; no candidate set meets the quality bar).

## Checklist Findings

1. **Price/target lineage — PASS.** Every published entry price carries date+tag (2026-07-17, DELAYED), dual-source grounded (Nasdaq bulk + IBKR verification on settlement names; single-web + tool class per Price Sourcing Standard). Targets = entry×(1+mu); CI bounds = entry×(1+mu±1.04σ) — spot-recomputed DOC: 22.505×1.05=23.63 ✓, 22.505×(1+0.05−1.04×0.072)=21.94 ✓.
2. **Sigma lineage — PASS.** All 33 sigmas REALIZED_VOL_30D from fetched bars; no round-number or sourceless sigmas; no blanket UNAVAILABLE.
3. **Score attribution — PASS.** 33/33 rows carry family z-scores, DQ 0.80, penalties, traces, drivers, ledger ranges; UNAVAILABLE families displayed as 0.00 contribution, never neutral-positive.
4. **Metric ledger coverage — PASS.** 325 ledger rows (01); every numeric in 05/06/09 traces to computed JSONs committed as run_computed_manifest.json.
5. **Kelly discipline — PASS.** All published kelly_025 cap-bound at 0.05 NAV; no ≤0 Kelly published as investable (nothing is investable).
6. **Technical indicator lineage — PASS.** All TD9/RSI/MACD/MA/momentum fields cite technical_indicators.json (generated 2026-07-20T16:27:43Z); exhaustion flags used as penalties/mu-adjustments only, never standalone signals; FDXF failure surfaced as exclusion, not hidden.
7. **GO-blocking discipline — PASS.** NO_TRADE is driven by evidence thresholds (family gate) + event concentration + beta feasibility — all Required inputs are grounded; no Enhancing input is cited as a blocker (Fund/Sent gaps act via DQ 0.80 and the threshold count, correctly).
8. **Prediction-record completeness — PASS.** 33 EQUITY_ALPHA (all with score_explainability + benchmark_price 743.29) + 3 MARKET_FORECAST records; 68 settlements embedded; ledger re-run confirms due inventory 0, 0 conflicts.
9. **Live-sounding language — PASS with note.** Intraday IBKR observations appear only in 10_midday_monitor.md, tagged LIVE with tool timestamps, and feed no scoring input.
10. **Concerns (severity order):**
   1. **MF calibration failure** — 20% direction accuracy over n=30 with mean z −0.77: the Core ETF mu prior is systematically optimistic in this tape. Deferred-to-13 (Track A tested and rejected there); the committee flags that continuing to publish positive-mu MF records at MEDIUM confidence deserves the 07-31 structural review's attention.
   2. **Settlement evidence concentration** — today's 68 settlements are four copies of one basket; rolling metrics move materially on correlated evidence (hit rate 55.5%→51.4%). Disclosed in 02; the committee endorses the 02 §6 flag for the structural review.
   3. **Post-print entry embedding** — several sleeve leaders (TRV, RF, FITB, STT, CFG, JBHT) embed print-day pops in their momentum ranks; their forecasts inherit mean-reversion risk. Disclosed per-name in Key Risk.

No fabrication, no inconsistent evidence, one revision not needed → APPROVE (NO_TRADE).
