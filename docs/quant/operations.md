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
For broker-backed adapters (`alpaca`, `ibkr`) the runner submits only when the
New York date equals the session date and the time is before **09:25 ET**, the
packaged `[execution] opening_auction_cutoff` in
[quant_policy.toml](../../src/financial_agent/quant/quant_policy.toml). It checks
before journaling any `submission_intent` and again before every submission.
Otherwise the session is `HALTED` with the observed New York time; synchronization
and reconciliation still run first. A late run on an off-cadence day is still
`NO_CHANGE`, and `--dry-run` previews at any time. `--today` defaults to the
current New York date, so a replayed `--today` against a broker halts. Intents
left unsubmitted when the cutoff passes mid-plan are abandoned at the next
session, never sent to a later auction. Local paper and `fa-quant demo` are exempt.
A window halt counts toward the live gate's halted-session limit.

Templates under [deploy/quant](../../deploy/quant/) cover cron, launchd and
systemd. Each calls the wrapper [run-session.py](../../deploy/quant/run-session.py)
(stdlib only) instead of `fa-quant` directly. Replace the absolute paths, then:

```sh
uv run --no-dev python deploy/quant/run-session.py \
  --env-file /abs/quant-paper.env --config /abs/host.toml
```

Any further arguments (`--dry-run`, `--today`) go to `fa-quant run`, which the
wrapper runs with `--json`; stdout and stderr pass through unchanged and the
wrapper exits with the session's exit code (0 completed or skipped, 2 `HALTED`,
1 usage/config error), so the scheduler still sees failures.

The env file holds `KEY=VALUE` lines (optional `export `, `#` comments, optional
matching quotes, no variable expansion) with the paper keys and, optionally,
`FA_QUANT_ALERT_WEBHOOK`. The wrapper refuses it, exiting 1 without running the
session, unless it is a regular file owned by the current user with mode 600 or
400. Its values override the inherited environment for the session only; never put
credentials in the plist, crontab, unit or TOML.

On a non-zero exit with `FA_QUANT_ALERT_WEBHOOK` set (env file or inherited), the
wrapper makes one attempt with a 10-second timeout to POST one JSON object:

```json
{"text": "fa-quant HALTED 2026-10-20 (exit 2): kill switch engaged",
 "status": "HALTED", "session": "2026-10-20", "exit_code": 2,
 "reasons": ["kill switch engaged"]}
```

`status`, `session` and `reasons` come from the session report. When stdout is not
a report (a config or usage error), `status` is `ERROR`, `session` is `null` and
the single reason is the last non-empty stderr line. Env-file values of eight or
more characters and the webhook URL are replaced with `[redacted]`; reasons are
capped at 10 entries of 500 characters. A delivery failure prints
`alert: delivery failed (<ExceptionType>)` to stderr, never the URL, and does not
change the exit code. Nothing is posted on exit 0. Treat the webhook URL as a
secret: it authorizes anyone holding it to post to your channel.

The cron template requires `CRON_TZ` support; systemd names the exchange timezone,
drops `EnvironmentFile=` because the wrapper loads and checks the file, and
disables persistent catch-up. launchd uses the host timezone: for a Pacific host
the template uses `Hour=5`, `Minute=45` on weekdays (PT and ET change daylight
saving on the same dates, so 05:45 PT is 08:45 ET; Eastern hosts use 8 and 45).
Wake the Mac first with `sudo pmset repeat wakeorpoweron MTWRF 05:40:00`. A late
catch-up run (for example launchd running a missed job on wake) halts at or after
09:25 ET rather than trading. Test daylight-saving behavior and scheduler logs on
your host. The [paper Actions workflow](../../.github/workflows/quant-paper.yml) is
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
Start well before the 09:25 ET runner cutoff: an order still unsent at 09:25 halts
the session mid-plan.
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
The runner's 09:25 ET submission cutoff applies; do not start a late catch-up.
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

For an Alpaca or IBKR paper config, `status` also shows **live readiness**: the
same certificate and paper-evidence checks `authorize_live` applies, except the
`FA_QUANT_ALLOW_LIVE` opt-in. It lists clean sessions against the 20 required,
halts and reconciliation breaks in the evidence window, fill count, mean and
worst per-fill slippage against the allowance, certificate verdict, identity
match, age and expiry, and every unmet reason. Evidence comes from
`[promotion] paper_journal` (default: this state's journal) and the certificate
from `[promotion] certificate`. It reads only those files and grants nothing.
`status --json` includes per-fill slippage under `live_readiness.fills`.

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
