# 13 Evolution Log

| Field | Value |
| --- | --- |
| Date | 2026-07-12 |
| Status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | Trailing 7 calendar days across all committed model packages plus the current run. |
| Packages reviewed | 14 dated directories from 2026-07-05 through 2026-07-12 across gpt-5, claude-fable-5, and gemini-3.5-flash. |
| Ledger status | 46 unique settled equities; weighted rank IC +0.200; 3 settled market forecasts. |
| Baseline flag | `NONE` — valid same-model in-window baseline. |

## Trailing Seven-Day Package Inventory

| Model / Dates | Packages | Status / Data-Mode Pattern | Cross-Model Finding |
| --- | ---: | --- | --- |
| claude-fable-5 / Jul 5-9 | 5 | Jul 5 `REVIEW_ONLY`; Jul 6-9 `NO_TRADE` with LIVE declarations | Better live-data access did not produce a GO portfolio. |
| gpt-5 / Jul 5-9 | 5 | `REVIEW_ONLY` / `DELAYED_PARTIAL` | Data-access limits drove the status difference versus Claude. |
| gpt-5 / Jul 10-12 | 3 | `NO_TRADE` / `DELAYED` | Required operational inputs improved, but factor breadth remained the common blocker. |
| gemini-3.5-flash / Jul 6 | 1 | Incomplete directory; no `00_run_manifest.md` | Excluded from status comparison and flagged as an audit-trail gap. |

Across all 13 complete packages, no model published `GO`. The principal divergence is data-mode labeling/access, while the convergent outcome is insufficient independent factor breadth; the current path correction addresses execution reliability only, not that research limitation.

## Observe

The June 14 holdout produced 11/17 equity direction hits, 15/17 interval hits, mean z -0.028, and rank IC +0.554. The rolling equity set now has 46 observations, acceptable 78.26% interval coverage, and positive weighted rank IC. The prior deferred proposal to reduce the top mu tier from 6% to 5% is not adopted: it would not change holdout direction, rank ordering, or realized drawdown, and no live portfolio existed to demonstrate the required out-of-sample IR improvement.

Separately, this run could not execute the documented helper commands verbatim. `main.md`, `runbook.md`, `rules.md`, `agents.md`, and the universe helper defaults referenced a nonexistent `investments/equity/...` tree, while the repository's actual root is `agents/equity/...`. The same automation-path drift was recorded in the June 11 and June 14 evolution logs.

## Diagnose

Primary diagnosis: `output clarity`. The research math and grounding gates worked, but stale repo-relative paths create a deterministic preflight failure and force operator inference.

## Hypothesis And Proposed Change

Track B, `HUMAN_REVIEW`: replace every `investments/equity/...` path inside the daily prompt stack and `build_index_universe.py` defaults with the repository's real `agents/equity/...` path. Hypothesis: the documented commands and default helper invocation will run from repo root without manual cache overrides, while leaving all scoring, grounding, and protected risk rules unchanged.

## Validation

The problem is evidenced by the failed default path audit in this run and by the two earlier evolution logs. The bounded patch changes only path strings in five files. Repository search finds no remaining `investments/equity` reference in `agents/equity/daily_investment_system/`; the universe helper succeeds from repo root using its corrected defaults and produces the same 503 + 101 - 89 = 515 union. No protected rule or grounding gate changes, satisfying all three Track B conditions.

## Decision

`ACCEPT` — `HUMAN_REVIEW`. Effective next run. This is the only accepted or proposed mutation in this cycle; no factor weight, mu prior, threshold, confidence rule, or risk limit changes.
