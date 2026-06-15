# 13 Evolution Log

## Run Context

| Field | Value |
|---|---|
| Date | 2026-06-14 |
| Status | NO_TRADE |
| Regime | NEUTRAL |
| Evaluation window | trailing 7 calendar days |
| Packages reviewed | claude-fable-5-2026-06-10, gpt-5-2026-06-09, gpt-5-2026-06-11, gpt-5-2026-06-14 |
| Ledger status | 2 prior ledger files; 0 due settlements; insufficient settled n |
| Baseline flag | CROSS_MODEL_BASELINE |

## What Worked

- The run produced cross-checked delayed prices, 60d histories, realized-vol sigma, and earnings cadence estimates for the full sampled universe.
- The system published settleable forecasts while refusing a portfolio that violates protected beta constraints.
- Missing enhancing feeds were treated as confidence caps rather than GO blockers.

## What Failed

- The external automation path `investments/equity/prompt/main.md` was still absent on `origin/main` after rebase, so the requested command could not be executed literally until a compatibility entrypoint was restored.
- No predictions have matured, so calibration metrics remain unavailable.
- The capped long-only beta interpretation continues to force `NO_TRADE` when fewer than roughly 18-20 investable names are available.

## Primary Diagnosis

`output clarity` / `source grounding`: the research artifacts are grounded, but automation wiring drifted from the canonical prompt path.

## Proposed Change

Track B process change: keep `investments/equity/prompt/main.md` as a compatibility entrypoint that redirects to `investments/equity/daily_investment_system/main.md` and contains no separate research logic.

## Hypothesis

A stable compatibility path prevents future automation runs from failing before the prompt system loads, without weakening any protected investment rule or grounding gate.

## Validation

Track B conditions are satisfied: (1) the issue appeared again in this run when the requested path was missing; (2) the compatibility file only redirects and does not modify scoring, risk, or source standards; (3) this log marks the change `HUMAN_REVIEW` for visibility.

## Decision

`ACCEPT` — Track B, `HUMAN_REVIEW`. Effective immediately as a compatibility shim. No factor weights, mu table, sigma sourcing, risk limits, or confidence thresholds changed.
