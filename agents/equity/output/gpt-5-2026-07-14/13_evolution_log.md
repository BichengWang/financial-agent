# 13 Evolution Log

| Field | Value |
| --- | --- |
| Date | 2026-07-14 |
| Status | `NO_TRADE` |
| Regime | `BULL` |
| Review timing | Preliminary only; the required post-close evolution decision was not due. |
| Evaluation window | 2026-07-08 through 2026-07-14 inclusive, all available models. |
| Packages reviewed | 13 dated directories across claude-fable-5 and gpt-5. |
| Ledger status | 77 unique settled equities; 61.04% HIT; 80.52% IN_CI; mean z -0.146; weighted rank IC +0.050. |
| Baseline flag | (none) — valid same-model exact-28-day baseline; no exception flag applies. |

## Trailing Seven-Day Review

- No complete package in the window published GO; principal models continued to find insufficient evidence breadth or protected-constraint infeasibility.
- The accepted July 13 due-inventory Track B change worked: `00` now exposes `next_due_target_date=2026-07-15` and `due_record_count_by_model={"gpt-5":17}` from the normalized scan.
- The June 16 vintage produced 10/14 hits but negative rank IC (-0.292). Rolling CI coverage remains healthy and weighted rank IC remains positive, so the calibration priority override does not fire.
- This run exposed a repeatable time-cut issue: the canonical Yahoo helper included the July 14 partial daily bar while completed Nasdaq histories ended July 13.

## Primary Diagnosis

`source grounding` / snapshot consistency. After-open invocations can mix a partial-session technical bar with completed-session volatility and beta inputs even when every individual source is valid.

## Proposed Change

**Track B — HUMAN_REVIEW.** Add a machine-readable `snapshot_cut` block to `00_run_manifest.md` and require the orchestrator to choose one of: (a) a completed-session cut used consistently for technicals, risk, entries, and settlements; or (b) an explicitly timestamped intraday cut with every source labeled to that cut. If the helper cannot honor the selected cut, it must disclose the mismatch before scoring.

Hypothesis: an explicit cut contract will prevent time-of-run rank drift and make cross-model packages comparable without changing factor weights, mu priors, thresholds, or protected limits.

## Validation

1. Problem evidence: `technical_indicators.json` is as-of July 14, while `history_metrics_manifest.json` is as-of July 13; both were fetched current-run and separately valid.
2. Protection check: the change strengthens timing lineage and does not weaken any grounding gate or protected risk rule.
3. Current-run dry test: the manifest and risk review explicitly disclose both cuts, allowing every downstream metric to trace to the correct one.

## Decision

`DEFER` — Track B, `HUMAN_REVIEW`. This is the only proposed change, but the required after-close review was not executed, so nothing is accepted or effective for the next run. Effective next step: evaluate the proposal after the close against the three-condition Track B standard. No factor weight, mu prior, confidence mapping, sizing rule, or protected limit changes in this package.
