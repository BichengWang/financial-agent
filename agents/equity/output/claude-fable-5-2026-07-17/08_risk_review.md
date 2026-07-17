# 08 Risk Review — 2026-07-17

Committee decision: **APPROVE** publication as `NO_TRADE` with the 23-name monitoring sleeve. One pass, no revision spent.

## Checklist Findings (agents.md §Risk Committee items 1–15)

1–2. Fabrication / overfitting: none found. Every numeric table is generated from `run_computed_manifest.json` (no hand-transcribed numbers, 07-15 Track B); formulas cite rules.md sections; no signal claims beyond the documented factor construction.
3. Event concentration: **breach flagged and recorded** (27 preflight names inside the buffered window, 03) — moot under NO_TRADE, but it independently blocks any GO this week.
4–5. Correlation / beta: no portfolio drafted; the §0 pre-check (07) documents the negative-beta infeasibility honestly rather than forcing a sleeve.
6. Thesis quality vs confidence: all published names LOW — consistent with 2/4 family coverage; no thesis language exceeds its ledger support.
7. Rules mismatch: none found. mu strictly from the Calibration Table bands (post-penalty percentile); the ABBV band-floor exhaustion suspension is disclosed in 05 and L022.
8. Price/derived-field citations: every entry price carries date + tag + ledger row; targets/CIs derive from tagged entries; no CI populated on any untagged price.
9. Sigma: REALIZED_VOL_30D for all 26 published symbols with stated derivation; no round-sigma fabrication; no ranked name lacks mu/sigma.
10. Score attribution: all 23 names carry the full trace (family z-scores, DQ 0.80, penalties, drivers, ledger rows); missing families shown as `0.00 (UNAVAILABLE)`, never neutral-positive.
11. Source Ledger: 199 rows; spot-checked lineage on DOC, TRV, ABBV, and the three ETFs — values match `run_computed_manifest.json` and `technical_indicators.json`.
12. Live-sounding claims: "official close" language is backed by the close-marker fetch chain (L002) and IBKR verification (L016) — non-illustrative ledger rows exist; allowed.
13. GO-blocking discipline: correct — all five Required inputs GROUNDED; NO_TRADE rests on evidence threshold #2 (a scoring gate), not on missing Enhancing inputs.
14. Prediction records: 23 EQ (all with `score_explainability` and `benchmark_price`) + 3 MF present; settlements block empty with the due-inventory-zero note — complete and auditable.
15. Technical-indicator lineage: all displayed values trace to `technical_indicators.json`; TD-9/RSI treated as exhaustion flags (−0.05 penalty, −1pp mu) not standalone signals; 14 monthly-MA gaps disclosed, none published.

## Top Three Concerns (severity order)

1. **Post-print entries in the sleeve (TRV +9.25%, RF/FITB −2.3% print-day closes).** Their momentum ranks embed a one-day print reaction; TRV's rank is materially print-inflated. Mitigation accepted: flagged in 05/06/09 per name, penalties applied to RF/FITB (est. ±5d window), confidence LOW; monitor-only status makes this an evaluation risk, not an execution risk.
2. **Chase risk at the top of the book:** 15 of the top 20 carry an exhaustion flag or earnings penalty; the defensive rotation is one session old and VIX is rising. The −1pp exhaustion mu adjustments and LOW confidence partially price this; the 14 weekly review carries the watch item.
3. **Calibration watch:** weighted rank IC −0.009 (n=119) with MF direction 33% (n=18) — the composite's predictive power is statistically indistinguishable from zero on the settled base. The MEDIUM cap is active (academic on a LOW sleeve); the corrective path is the standing Fund/Sent Phase 2 escalation, not a new parameter change (13).

## Publication Recommendation

`NO_TRADE` — publish the full package. Required fixes: none.
