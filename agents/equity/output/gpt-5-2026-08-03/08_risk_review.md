# 08 — Risk Review — 2026-08-03

## Committee decision

**`HALTED` / `DELAYED_PARTIAL` — NOT APPROVED FOR EXECUTION.** Fifteen of 20 provisional
equity names (75%) lack a confirmed or cadence-estimated Required earnings date, triggering
Hard Halt criterion #3. Equity scores, targets, and portfolio analytics are audit-only
pre-halt diagnostics; their prediction records were withdrawn.

## Top concerns

1. Unknown earnings dates make event penalties, adjusted scores, percentiles, membership,
   targets, and confidence non-final for the provisional equity set.
2. `Fund_Z` and `Sent_Z` are unavailable for all scoreable names, independently failing the
   3-of-4-family and max-family-contribution gates.
3. Weighted rolling rank IC is -0.0879 over 515 equity settlements and `eff_n=1`; Track A
   changes remain ineligible.

## Review checklist

| Control | Finding | Decision |
| --- | --- | --- |
| Price / target lineage | 23/23 provisional equity/ETF inputs were cross-checked; target formulas are ledgered | PASS for pre-halt diagnostics |
| Sigma lineage | `REALIZED_VOL_30D` comes from fetched adjusted histories | PASS |
| Score attribution | Six-signal traces are persisted, but unknown earnings penalties invalidate final equity scores | FAIL — HALT |
| Metric ledger coverage | Expanded `L-TI-*`, `L-RM-*`, `L-CORR-*`, and `L-SR-*` rows enumerate technical, risk, correlation, target, and settlement inputs/formulas | PASS for persisted fields |
| Source Ledger completeness | Fifteen provisional-name `L-EA-*` rows are explicitly `UNAVAILABLE`; Hard Halt #3 applies | FAIL — HALT |
| Kelly threshold handling | Raw and pre-cap quarter Kelly are disclosed; the bounded field is 5.00% and cap binding for every provisional name | PASS for diagnostics; no weights |
| Technical lineage | Full D/W/M TD9, RSI, MACD state/histogram, MA, momentum, volume, and RS values cite `L-HIST` plus the deterministic helper | PASS |
| GO-blocking discipline | Required gaps are classified `DELAYED_PARTIAL`; the >20% critical-input threshold forces `HALTED` | PASS |
| Prediction completeness | Zero equity predictions were published; SPY/QQQ/SOXX research forecasts and 88 historical settlements remain | PASS for halted package |
| Settlement timing | `due=0`, `conflicts=0`; all settlement closes are `HISTORICAL` with explicit timing flags | PASS |
| Portfolio analytics | `07` lists every required analytic; weight-dependent metrics are `N/A — HALTED`, and the equal-weight basket is diagnostic only | N/A — no portfolio |
| Hard risk caps | No executable portfolio exists; pre-halt equal-weight beta fails the band | NOT APPROVED |

## Required remediation

Populate confirmed or cadence-estimated earnings dates for the scoreable universe, apply the
buffered event penalty, and rerun scoring, equity predictions, and portfolio construction.
The expanded ledger and bounded-Kelly presentation repair the narrative-audit gaps but cannot
cure the missing Required input. Final status: **`HALTED`**.
