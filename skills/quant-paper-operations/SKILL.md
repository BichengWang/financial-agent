---
name: quant-paper-operations
description: Operates fa-quant paper trading sessions on Alpaca, IBKR Client Portal or the local simulator - dry-run previews, scheduled pre-open runs, reading session reports, status and live readiness, and the kill/unkill incident runbook for halts, reconciliation breaks and loss stops. Use when asked to run, schedule, check or debug a quant paper session, explain a HALTED report, or measure progress toward the live gate. Never use it to enable live trading.
compatibility: Python 3.12 via uv, run from the repository root. Broker sessions need paper credentials in the environment (Alpaca) or an authenticated local IBKR gateway; the local simulator is offline.
---

# Quant paper operations

The runner owns safety: limits and the 09:25 ET cutoff live in
`src/financial_agent/quant/quant_policy.toml`; procedures in
`docs/quant/operations.md` and `docs/quant/safety.md`. This skill says which
command to run when, and what an agent may and may not do.

## Boundaries

- Read-only and safe at any time: `status`, `run --dry-run`, reading reports
  and the journal. Previews never count as paper evidence.
- A submitting `run`, `kill` and `unkill` only on the operator's explicit
  request in this conversation. Never `unkill` to test a command.
- Never create a live config, set `FA_QUANT_ALLOW_LIVE`, widen
  `confirm_message_ids`, loosen risk overrides or edit the policy file.
- Credentials come only from the environment or a mode-600 env file. Never put
  them in TOML, commands, reports or commits, and never print them.
- Never hand-edit or delete `journal.jsonl`, risk state or reports, and never
  reset a high-water mark to clear a halt.

## Run a session

Broker sessions submit only on the New York session date before 09:25 ET; run
near 08:45 ET with yesterday's close available. Weekly plans trade on the first
session of the ISO week; other days synchronize fills and check safety. The
local simulator (`broker.kind = "paper"`) is exempt from the window.

```bash
uv run fa-quant run --config examples/quant/paper.toml --dry-run
uv run fa-quant run --config examples/quant/paper.toml
uv run fa-quant status --config examples/quant/paper.toml
```

For IBKR use `examples/quant/ibkr-paper.toml` with a `D…` paper account; the
gateway must be running and logged in through the browser that morning, and
cannot run in GitHub Actions. Scheduled hosts call
`deploy/quant/run-session.py --env-file /abs/quant-paper.env --config /abs/host.toml`,
which posts an alert to `FA_QUANT_ALERT_WEBHOOK` on a non-zero exit.

## Read the result

Exit 0 is completed or skipped, 2 is `HALTED`, 1 a usage or configuration
error. Always read the status and reasons, not just the code:

- `TRADED`: orders acknowledged, not necessarily filled.
- `NO_CHANGE`: no rebalance due, no deltas, a retry or a preview.
- `NO_SESSION`: exchange closed.
- `HALTED`: read `state_dir/reports/DATE.md` and `.json`. The first report of
  the day is kept; reruns add `.2`, `.3`, and previews `.preview`.

`status` reads persisted state only; it never calls the broker, so account and
fill observations can be stale. On an Alpaca or IBKR paper config it also
prints live readiness: clean sessions against the 20 required, halts and
reconciliation breaks in the window, fill slippage against twice modeled
costs, certificate verdict, identity match and expiry, and every unmet reason.
Report those reasons verbatim; readiness grants nothing.

## Incident runbook

1. Ask the operator to stop the scheduler, then engage the stop:
   `uv run fa-quant kill --config <toml> --reason '<cause>'`. Kill stops new
   submissions only; open orders and positions must be checked and managed at
   the broker.
2. Read the earliest halt report, later attempts, journal validity and broker
   acknowledgements. Back up the state directory before any repair.
3. Reconciliation break: compare journaled fills with broker positions; look
   for external trades, splits, partial fills or an interrupted submission.
   Reruns recover known client IDs; never invent a replacement order.
4. Data error: verify adjusted bars and each symbol's last close
   (`fa-quant data check --config <toml> --expected-last-session YYYY-MM-DD`).
   Restore trusted cache or state backups; never insert guessed rows.
5. Loss or drawdown stop: the persisted stop stays until the operator releases
   it after reviewing capital and strategy suitability.
6. Release only when the operator has documented cause and fix:
   `uv run fa-quant unkill --config <toml> --reason '<cause and fix>' --operator '<name>'`,
   then `status` and a `--dry-run` before the next valid window. If evidence
   is uncertain, keep the stop engaged.
