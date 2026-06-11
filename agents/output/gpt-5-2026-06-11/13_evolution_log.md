# 13 Evolution Log

## Run Context

| Field | Value |
|---|---|
| Date | 2026-06-11 |
| Status | NO_TRADE |
| Regime | HIGH_VOL / RATE_SHOCK overlay |
| Evaluation window | trailing 7 calendar days |
| Packages reviewed | claude-fable-5-2026-06-10, gpt-5-2026-06-07, gpt-5-2026-06-09, gpt-5-2026-06-11 |
| Ledger status | 1 prior ledger file(s); 0 due settlements; insufficient settled n |
| Baseline flag | CROSS_MODEL_BASELINE |

## What Worked

- Required data grounding improved materially versus the 2026-06-09 `DELAYED_PARTIAL` run: prices, history, sigma, earnings dates, and sampled universe all populated.
- The run published settleable forecasts while still refusing a live portfolio when beta/sector constraints failed.
- Missing enhancing inputs were treated as confidence caps, not automatic GO blockers.

## What Failed

- The automation instruction still referenced `investments/equity/prompt/main.md`, which no longer exists on `origin/main`; the run had to infer the current entrypoint `daily_investment_system/main.md`.
- No closed prediction records exist yet, so calibration metrics remain unavailable.
- The beta-band interpretation remains restrictive for a capped long-only sleeve and continues to force `NO_TRADE` when defensive or low-beta names lead.

## Primary Diagnosis

`output clarity` / `source grounding`: the research loop is now producing grounded data, but the external automation invocation is stale and can fail before the prompt system starts.

## Proposed Change

Track B process change: update the automation invocation text to call `investments/equity/daily_investment_system/main.md` directly, or add a clearly marked compatibility stub at the old `investments/equity/prompt/main.md` path that points to the current entrypoint.

## Hypothesis

Removing the stale path will prevent future runs from depending on operator inference and will make the requested command match the repo's single source of truth.

## Validation

Track B conditions: (1) explicit problem observed this run when the requested path was absent; (2) the change does not weaken any protected investment rule or grounding gate; (3) it should be logged with `HUMAN_REVIEW` because it affects scheduler/operator wiring.

## Decision

`DEFER`. No prompt mutation or compatibility stub was applied in this investment run; the next maintenance pass should update the automation command or add the stub deliberately.

## Effective Next Step

Human/maintenance review: align the automation's run path with `daily_investment_system/main.md`. No factor, risk, mu, or sigma parameter changes are accepted until settled observations exist.
