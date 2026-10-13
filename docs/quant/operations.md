# Operations

Use one persistent state directory per account/strategy, on a local filesystem
with POSIX locks. `TradingConfig` resolves relative paths from the TOML file,
not the working directory. The bundled [paper config](../../examples/quant/paper.toml)
uses `var/quant-paper` and `var/quant-cache`; these are gitignored.

## Daily schedule

Run around **08:45 America/New_York**, before the opening auction, with yesterday's
completed close available. Weekly plans are due on the first exchange session of
the ISO week; monthly plans on the first session of the month. Other sessions
still synchronize fills and check account safety. Weekends/holidays skip.

Alpaca OPG orders participate only in the opening auction. Orders submitted after
09:28 and before 19:00 ET are rejected; after 19:00 they queue for the following
auction. See [Alpaca's order documentation](https://docs.alpaca.markets/us/docs/orders-at-alpaca).
The runner does not enforce a wall-clock OPG cutoff. Do not catch up a missed run
late or use `--today` to replay old sessions against an actual broker.

Templates under [deploy/quant](../../deploy/quant/) cover cron, launchd and
systemd. Replace absolute paths and supply credentials through a protected
environment file/wrapper. The cron template requires `CRON_TZ` support; launchd
uses the host timezone; systemd names the exchange timezone and disables
persistent catch-up. Test daylight-saving behavior and scheduler logs on your
host. The [paper Actions workflow](../../.github/workflows/quant-paper.yml) is
manual dispatch, not a precise clock. It restores state from Actions cache and
uploads reports; cache eviction/loss must halt operations until state is restored.
A dedicated persistent host is preferable for ongoing execution.

With paper credentials already loaded in the environment:

```sh
uv run fa-quant run --config examples/quant/paper.toml --dry-run
uv run fa-quant run --config examples/quant/paper.toml
uv run fa-quant status --config examples/quant/paper.toml
```

The release smoke verifies these interfaces using local synthetic CSV data and
fake Alpaca transport, not owner credentials. A dry run journals observations
and can synchronize prior fills; it does not submit new orders and cannot count
as live-promotion paper evidence.

## Reports and journal

Exit code 0 means completed/skip, 2 means halted trading or failed validation,
and 1 means usage/configuration/research error. Inspect the status and reasons,
not just the exit code. `TRADED` means submissions were acknowledged, not that
all fills completed. `NO_CHANGE` can mean no rebalance, no deltas, retry or preview.

Read `state_dir/reports/DATE.md` and `.json`: decision close, NAV, targets versus
actual weights, orders, fills and limit utilization. The first report remains;
reruns append `.2`, `.3`, etc. Previews use `.preview` and their own attempt suffix.
On off-cadence days, `Target (last plan)` retains the last execution plan; `—`
means no target is known. `status` reads persisted observations and shows their
age; it does not call the broker. Broker account/fill observations may be stale.

`journal.jsonl` records session starts/outcomes, quality results, reconciliation,
risk state, plans, submission intents/acks, fill observations and stop actions.
Each event contains sequence, timestamp, predecessor and hash. Do not hand-edit
it. Back up the journal with broker/risk state and reports after every session.
A hash chain is an audit aid, not cryptographic authentication.

## Incident runbook

1. Stop the scheduler and engage the stop with the command below. Check open
   orders and actual positions at the broker; cancel or manage them there if
   necessary. Kill does not cancel or liquidate.
2. Read the earliest halt report, later attempt reports, journal validity and
   broker acknowledgements. Preserve files before repair. Check environment,
   provider freshness, exchange date, credentials and connectivity without
   logging secrets.
3. For a reconciliation break, compare journaled fill quantities with the broker.
   Look for external trades, splits/dividends, partial fills or interrupted
   submission/settlement. Reruns recover known client IDs; they must not invent a
   replacement order for an uncertain acknowledgement. Never erase the journal
   or reset a high-water mark merely to bypass a halt.
4. For data errors, verify adjusted OHLCV and every symbol's last close. The cache
   detects revisions on overlap refresh. Restore trusted cache/state backups
   rather than inserting guessed rows. For broken journal/risk state, restore
   the mutually consistent backup and reconcile the actual broker before resume.
5. For daily loss/drawdown, inspect capital and strategy suitability. The persisted
   stop remains until an operator explicitly releases it. Pre-trade/quality
   halts do not all engage the stop automatically, so keep scheduling disabled
   during diagnosis.
6. Release only after documenting cause and corrective action, verify status,
   then preview before the next valid opening window. If evidence is uncertain,
   keep the stop engaged and investigate.

```sh
uv run fa-quant kill --config examples/quant/paper.toml --reason 'investigating halt'
uv run fa-quant status --config examples/quant/paper.toml
uv run fa-quant unkill --config examples/quant/paper.toml \
  --reason 'cause resolved and broker reconciled' --operator 'Kenneth'
```

`unkill` first verifies the journal and persists the justification. A broken
chain prevents release. These commands were smoke-tested with a separate local
paper state; do not release an operational stop merely to test a command.
