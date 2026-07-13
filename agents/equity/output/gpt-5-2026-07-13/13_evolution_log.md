# 13 Evolution Log

| Field | Value |
| --- | --- |
| Date | 2026-07-13 |
| Status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | 2026-07-06 through 2026-07-13, all models. |
| Packages reviewed | 16 dated directories: claude-fable-5, gpt-5, and gemini-3.5-flash. |
| Ledger status | 63 unique settled equities; 58.73% HIT; 77.78% IN_CI; mean z -0.134; weighted rank IC +0.124. Six settled market forecasts. |
| Baseline flag | `NONE` - valid same-model exact-28-day baseline. |

## Trailing Seven-Day Review

- No complete package in the window published `GO`; both principal models converged on insufficient evidence breadth or protected portfolio constraints despite different data-access paths.
- The accepted July 12 confirmed-earnings Track B change worked: 19/19 Nasdaq/Zacks shortlist requests succeeded, with DAL using the explicit cadence fallback.
- Gemini's July 6 directory still lacks a manifest, and Claude July 10-11 remain partial/backfilled audit gaps.
- The June 15 vintage produced 11/17 hits but slightly negative rank IC (-0.083). Rolling CI coverage and mean z remain healthy, and weighted rank IC remains positive, so the calibration priority override does not fire.

## Primary Diagnosis

`source grounding` / due-inventory visibility. The Claude July 12 manifest stated the next due date was August 4 even though the repository contained 20 gpt-5 records due July 13. The core rules already require an all-model scan, but the manifest schema does not expose the normalized next-due inventory, allowing an execution miss to pass review.

## Proposed Change

**Track B - HUMAN_REVIEW.** Add a machine-derived `next_due_target_date` and `due_record_count_by_model` row to `00_run_manifest.md`, sourced from the same normalized all-model key set used by Reflection. Hypothesis: making the due inventory explicit will prevent model-local scans and false "next due" claims without changing prediction math, scoring thresholds, or any protected risk/grounding rule.

## Validation

1. Problem evidence: `claude-fable-5-2026-07-12/00_run_manifest.md` claimed August 4; normalized scanning found 20 records due July 13 in `gpt-5-2026-06-15/15_predictions.json`.
2. Protection check: the change only exposes an existing mandatory scan result and strengthens auditability; no protected rule or grounding gate is weakened.
3. Current-run test: normalized keying on model, vintage date, ticker, type, and target date produced exactly 20 new settlements and 63-equity/6-market rolling totals with no duplicates.

## Decision

`ACCEPT` - Track B, `HUMAN_REVIEW`, effective next run. This is the only proposed change. No factor weight, mu prior, confidence mapping, sizing rule, or protected limit changes.
