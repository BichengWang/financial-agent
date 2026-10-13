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

## IBKR Client Portal Gateway

Install a Java runtime and download/extract the gateway using IBKR's
[installation guide](https://ibkrcampus.com/docs/web-api/authentication/cpgw/installation-authentication).
From its extracted directory run `bin/run.sh root/conf.yaml` (Windows:
`bin\run.bat root\conf.yaml`) and leave that process running. Open
`https://localhost:5000` in a browser and log in with the paper account credentials.
Keep passwords and two-factor authentication in the gateway login flow, never TOML.

On macOS, AirPlay Receiver often occupies port 5000. Set `listenPort: 5001` in
`root/conf.yaml`, restart the gateway, log in at `https://localhost:5001`, and set
`broker.base_url = "https://localhost:5001/v1/api"`. The example uses this port.
The gateway certificate is self-signed: `verify = false` is allowed only for
`localhost`, `127.0.0.1` and `::1`; otherwise use `verify = true` or a CA-bundle
path (relative TOML paths resolve from the configuration directory).

IBKR requires [daily browser reauthentication](https://www.interactivebrokers.com/docs/web-api/authentication/cpgw/client-portal-gateway-faq).
Log out of competing trading platforms and confirm the gateway is authenticated
and connected before the scheduled run. Use a dedicated persistent host and one
adapter per gateway session; the adapter paces its reads and requests.
Account membership, type and USD currency are validated once per adapter instance;
authentication is checked at most once per minute and immediately after HTTP 401.
An 11-order plan normally takes about **one minute** at the documented five-second
order/trade polling pace, plus network latency; replies or retries can extend it.
Allow several minutes of margin before the cutoff rather than starting at 09:27.
**This gateway workflow cannot run from GitHub Actions**: it depends on the local
interactive login, gateway process and durable trading state.

Copy [ibkr-paper.toml](../../examples/quant/ibkr-paper.toml), replace `account_id`
with your USD paper account, and run around **08:45 New York time**:

```sh
uv run fa-quant run --config examples/quant/ibkr-paper.toml --dry-run
uv run fa-quant run --config examples/quant/ibkr-paper.toml
```

The order body is whole-share `MKT` with `tif = "OPG"`. Nasdaq MOO orders must
arrive before **09:28 Eastern**, per [IBKR's order guide](https://www.interactivebrokers.com/en/trading/ordertypes.php).
The runner does not enforce a wall-clock cutoff; do not submit a late catch-up.
Keep `confirm_message_ids = []` until you have reviewed a specific precaution.
A declined question appears in the halt report with its IDs and redacted text;
same-day reruns remain halted. Inspect all earlier acknowledgements before retrying.

Current-session orders are recovered by cOID; previous-session executions are
aggregated from `/iserver/account/trades?days=7`. IBKR supplies at most seven days
of history and trades do not prove the original order quantity or terminal status.
The journal supplies intended quantities and the runner reconciles recovered fills.
Once the data includes the intent session's opening bar, the runner records the
next execution observation as `order_final`: filled, or canceled with any unfilled
remainder. A missing order finalizes with the fills already journaled; final orders
are never polled again. This applies to all broker-backed OPG adapters and avoids
permanent halts when unfilled/partial auction orders leave the history window.
Broker-position reconciliation remains mandatory: an unreported real fill causes
a position break and halts. Before the auction, missing orders still fail closed.
Preserve state and inspect broker records when reconciliation is uncertain.
The implementation follows the [Web API documentation](https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/)
and [current OpenAPI schemas](https://api.ibkr.com/gw/api/v3/api-docs).

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
