# 13 Evolution Log — 2026-07-28

**Final status: NO_TRADE**

| Field | Value |
|---|---|
| Run/status/regime | 2026-07-28 · NO_TRADE · NEUTRAL |
| Evaluation window | canonical settlements through 2026-07-28 |
| Ledger status | EQ n=260 eff_n=1; MF n=48 eff_n=1 |
| Baseline | SAME_MODEL_BASELINE gpt-5-2026-06-30; exception NONE |
| Primary diagnosis | factor calibration |

What worked: required inputs, two-source price grounding, population-volatility lineage, complete predictions, and healthy equity CI coverage. What failed: market direction accuracy is 20.83%, equity weighted rank IC is -0.1715, and missing Fund_Z/Sent_Z keeps all names below the evidence bar.

## Exactly one proposed change

**Track A — recalibrate the Core ETF relative-view adjustment / beta-scaled mu mapping.** Hypothesis: shrinking the QQQ/SOXX beta-scaled prior toward zero will improve market-forecast hit rate and mean z without degrading CI coverage. Evidence gates: raw n=48 passes n≥20, but eff_n=1 fails the required eff_n≥3. Holdout IR, hit-rate, drawdown, and turnover deltas cannot yet be established on independent windows.

**Decision: DEFER — INSUFFICIENT_EFFECTIVE_N.** No rule, weight, threshold, or formula changes this run. Effective next step: accumulate non-overlapping target windows, then test the single proposal on a frozen holdout before acceptance.
