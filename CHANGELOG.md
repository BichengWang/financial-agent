# Changelog

All notable changes are documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- The RL examples moved from `example/rl/` to `examples/rl/`.

### Removed

- Unused names from the historical `financial_agent.trading` package, which the
  wheel ships. Nothing in the repository or its notebooks referenced them:
  `DEFAULT_DATA_COLUMNS` and every ticker list in `config.config` except
  `SP500_100_TICKER`, `SP500_20_TICKER` and `DOW_30_TICKER`;
  `backtest.convert_daily_return_to_pyfolio_ts` and `backtest.trx_plot`;
  `preprocessing.data.load_dataset` and `convert_to_datetime`;
  `YahooDownloader.select_equal_rows_stock`; and `configure_mixed_precision`,
  `get_optimal_batch_size`, `create_device_aware_model` and `train_on_device` in
  `utils.gpu_config`.

### Fixed

- The market-data cache raises a data error naming the symbol and field when the
  metadata record of a symbol it is fetching is missing a field the cache needs for
  it or holds a coverage date that is not an ISO date. It used to fail with an
  uncaught `KeyError`, `TypeError` or `ValueError`. Records the cache already
  refetched, such as one written by another provider, are still refetched. A
  retrieval time outside the range that converts to New York time now counts as
  unreadable, so the last bar is fetched again instead of raising `OverflowError`.
- `examples/rl/run_all_examples.py` counts only the examples that exit 0, and exits
  with status 1 when any of them fails or the run is interrupted. It used to report
  `4/4 examples completed successfully` and exit 0 even when an example failed.
- `fundamental_diagnostics.py` and `sentiment_diagnostics.py` upper-case, trim and
  comma-split `--tickers` values like `--tickers-file` lines, and drop empty ones.
  `--tickers aapl` used to find no SEC CIK mapping, `--tickers SPY,QQQ` stayed one
  ticker, and `--tickers ""` ran with an empty ticker instead of reporting none.
- Both MCP servers answer a request containing `NaN`, `Infinity` or `-Infinity`,
  which are not JSON, or a number too large for a float such as `1e999`, with the
  same parse error as any other malformed line and keep serving. `fa-quant mcp`
  used to exit with `error: ValueError`, and `python -m financial_agent.harness mcp`
  echoed the value back as non-JSON.
- The quant MCP tools default `today` to the current New York date, as
  `fa-quant run` does, instead of the host's local date. On a host whose date
  differs from New York's, `quant_preview_orders` without `today` used to plan the
  wrong session; ahead of New York it planned off an unfinished close and failed
  its freshness gate.
- `AlpacaBroker` rejects a `max_retries` that is not an integer, such as `1.5` or
  `True`, with `ValueError` at construction, as `IBKRBroker` does. A fractional count
  used to be accepted and fail the first request with `TypeError`.
- `fa-quant run --dry-run` still reports a dry run when another session holds the
  lock. The halted report used to say `"dry_run": false` and `Dry run: False`, and
  list its orders under `Orders` instead of `Planned orders`.
- A `KILL` file written mid-session now stops the remaining orders: each
  submission loop checks the kill switch before every order and halts. Orders
  already submitted stay submitted and journalled; kill still cancels nothing.
- `fa-quant kill` engages the stop even while a session is running. It used to
  fail with `SessionLocked` and write no `KILL` file. If the session lock is held
  the journal entry is skipped and the command says so.
- The NYSE calendar no longer closes on the Friday before a Saturday January 1,
  so 2021-12-31 and 2027-12-31 are trading days; a Sunday January 1 is still
  observed on Monday.
- Yahoo downloads retry four times over about 30 seconds (2 s backoff, doubling)
  instead of twice over 1.5 seconds. A scheduled session that starts just after
  the host wakes no longer halts because DNS is not resolving yet. The 2026-10-30
  paper session halted that way. Callers can still pass `retries` and `backoff`.
- The launchd template runs the session wrapper under `/usr/bin/caffeinate -i`, so
  the Mac doesn't idle-sleep in the middle of a session. The operations guide says
  to keep a laptop host on power.
- The live gate rejects a certificate whose `policy_sha256` differs from the packaged
  policy file, so `certify --policy` with looser thresholds can no longer authorize live.
- A paper `session_outcome` counts as live evidence only when its journal timestamp falls
  on that session's New York date, so replaying `run --today <old date>` adds no sessions.
- The paper-slippage allowance caps the config's half-spread and slippage at the packaged
  `CostModel` defaults, so inflating `[backtest.costs]` can no longer loosen it.
- The market-data cache refetches a last bar retrieved on or before its session's
  New York date, or with no readable retrieval time. A bar cached while the market
  was open used to be served for that end date forever, so the next session could
  decide on an intraday price.
- The market-data cache fetches a symbol again in full when its cached bars came
  from another provider. A cache filled by `--provider csv` used to be served for
  `--provider yahoo` without contacting Yahoo, labelled `csv`.
- A same-day rerun of a broker-backed session after the opening auction filled no
  longer halts. The next session journals those fills against their session's open.

## [1.3.0] - 2026-10-28

### Fixed

- Research CLI commands honor `--provider yahoo` when `--csv-dir` is also set.
- Non-object cache metadata raises a data error instead of an uncaught attribute error.

### Added

- A documentation site at <https://bichengwang.github.io/financial-agent/>, built
  with MkDocs Material and deployed from `main` by the Pages workflow: on push,
  and within 30 minutes of an auto-merge, whose `GITHUB_TOKEN` push starts no
  workflows. It serves the README, `docs/` (quant guides, releasing, equity research
  reports), the quant evidence reports and this changelog. Repository links that
  aren't site pages open on GitHub. Pull requests that touch these files run a
  strict build. Preview locally with
  `uv run --only-group docs mkdocs serve`.
- Two agent skills for the quant platform, discoverable through `.agents/skills/`:
  `quant-strategy-research` (backtest, validate and certify a strategy, read the
  eight promotion checks, write dated evidence) and `quant-paper-operations`
  (dry-run and scheduled paper sessions, status and live readiness, and the
  kill/unkill incident runbook). Neither can enable live trading.
- Contributor and security docs: `CONTRIBUTING.md` (setup, checks, quant and
  pull request rules), `SECURITY.md` (private vulnerability reporting, now enabled),
  `CODE_OF_CONDUCT.md`, issue forms for bugs and features, and a pull request
  template. The README shows CI, PyPI, Python, docs and license badges.
- `[promotion] disclosed_trials` lists every variant tried when the certified
  grid is narrower, e.g. one frozen identity. DSR then deflates by all of them:
  their count and the variance of their full-period Sharpes on the certified
  data. The certificate records `n_trials` and `trial_sharpe_variance` in its
  diagnostics; certificates without a disclosure are unchanged. The disclosure
  must list each grid variant once. `evaluate_promotion` takes it as the
  keyword `disclosed_trials`.

### Changed

- The `Documentation` project URL and the README link to the site.
- The Alpaca and IBKR example configs freeze the certified identity
  (`target_vol=0.12, max_weight=0.25`): it is the configured strategy and the
  only grid variant, with the four searched variants disclosed. A
  re-certification can no longer switch parameters and restart paper evidence.
  Pass the four-variant `--grid` to rerun the original search.
- The README opens with the current paper-to-live status, installs from PyPI,
  compares the four-variant and frozen-identity gate results, lists the live
  gate's conditions and documents the scheduler wrapper.
- Saved notebooks shrank from 10.9 MB to 3.1 MB without re-execution: training
  logs keep their first and last 40 lines, very long printed lines are clipped,
  and plots are 256-colour PNGs. Each cut is marked in the output.
- GitHub language statistics exclude `.ipynb` files (`linguist-documentation`),
  so the repository reports as Python rather than Jupyter Notebook.
- The notebooks README lists each notebook and how to run it.

### Removed

- Six research notebooks: the three AI4Finance FinRL tutorial copies in
  `archive/`, the upstream `Crypto_Binance_Historical_Data` tutorial, and
  `multistock_variant_2` and `this_works_1_18`, which largely duplicate
  `multistock_docker`. They remain in git history.

## [1.2.1] - 2026-10-20

### Added

- The Release workflow can publish to PyPI through trusted publishing once the
  `PYPI_PUBLISH` repository variable is `true`. Manual dispatch rehearses the
  upload on TestPyPI. Pull requests and releases run `twine check --strict`. See
  `docs/releasing.md`.

### Changed

- The distribution is renamed `fa-quant`, because `financial-agent` on PyPI is an
  unrelated project. The `financial_agent` import package (declared as PEP 794
  `import-names`) and the `fa-quant` command are unchanged. Certificates and MCP
  report the `fa-quant` version. Run `uv sync` after pulling.
- Packaging uses the SPDX license expression `MIT`. The sdist holds only what
  building the wheel needs (31.7 MB to 0.2 MB). The PyPI description links to the
  tagged repository files.

## [1.2.0] - 2026-10-19

### Added

- `fa-quant status` shows live readiness for Alpaca and IBKR paper configs:
  clean sessions, halts and breaks in the evidence window, mean and per-fill
  slippage against the allowance, certificate verdict, identity match, age and
  expiry, and every unmet reason. It reads only the journal and certificate,
  makes no broker call and grants nothing.
- `deploy/quant/run-session.py`, a stdlib-only scheduler wrapper. It loads
  credentials from a chmod 600 env file (refused when a symlink,
  group/other-accessible or not user-owned), runs `fa-quant run --json`, passes
  output and the exit code through (128 + N after signal N), and on a non-zero
  exit posts one sanitized JSON alert (status, session, reasons) to
  `FA_QUANT_ALERT_WEBHOOK` when set. The launchd, cron and systemd templates call
  it; the launchd template gives a Pacific-host example (`Hour=5`, `Minute=45`)
  and the `pmset` wake command.

### Changed

- `live_readiness(config, *, now)` holds the certificate and paper-evidence
  evaluation; `authorize_live` adds the `FA_QUANT_ALLOW_LIVE` opt-in and the
  grant. Thresholds and reasons are unchanged.

## [1.1.1] - 2026-10-19

### Fixed

- Broker-backed (Alpaca, IBKR) sessions submit opening-auction orders only when
  the New York date equals the session date and the time is before the packaged
  09:25 ET `[execution] opening_auction_cutoff`. The check runs before journaling
  submission intents and before every submission, including interrupted-submission
  recovery; otherwise the session halts with the observed time. Late or replayed
  runs can no longer queue orders for a later auction. Local paper and the demo
  are unchanged.
- `fa-quant run --today` defaults to the current New York date instead of the
  host-local date.
- CHANGELOG link references cover every release.

### Changed

- `run_session` accepts `now`, an injectable clock returning timezone-aware
  datetimes. Adding the policy section changes `quant_policy.toml` bytes, so new
  certificates record a different `policy_sha256`; thresholds are unchanged and
  existing certificates still verify.

## [1.1.0] - 2026-10-13

### Added

- IBKR Client Portal Gateway execution with guarded paper/live accounts, USD
  portfolio observation, whole-share opening-auction orders, contract resolution,
  precaution allow-lists, order recovery and gateway operations guidance.

### Changed

- Public broker `lookup(client_order_id)` supports runner recovery across adapters.
- Live evidence must come from the same broker as the live configuration;
  local simulation never authorizes live execution.

### Fixed

- Finalize broker-backed opening-auction intents after observing their auction
  session, preventing vanished zero-fill or partial orders from halting later runs.
  Reconciliation still halts on unreported fills.
- Validate IBKR account metadata once per adapter and cache authentication status
  for 60 seconds, refreshing immediately after HTTP 401, to reduce gateway pacing
  delays without bypassing live guards.

## [1.0.1] - 2026-10-13

### Fixed

- Wheel installations can run trading sessions and the offline demo outside a
  source checkout without failing with `FileNotFoundError` for missing helper scripts.

## [1.0.0] - 2026-10-13

### Added

- Risk-managed systematic ETF platform with binding strategy/data/broker contracts
  and research → certify → paper → live delivery plan (#91).
- Adjusted Yahoo/CSV data, incremental revision-aware cache, quality checks and
  deterministic synthetic fixtures (#92).
- Cost-aware, next-bar portfolio backtesting, shared weight-to-share sizing,
  trend/volatility targeting, dual momentum and fixed-weight benchmarks (#93).
- Tighten-only pre-trade limits, account loss/drawdown state and persistent
  operator-released kill switch (#94).
- Embargoed walk-forward validation, DSR, CSCV/PBO diagnostics, bootstrap,
  execution stress, policy gates and hashed certificates (#95).
- Dated research-forecast adapter and honest failing short-history evidence (#97).
- Persisted paper broker, guarded Alpaca REST execution, idempotent orders,
  reconciliation and hash-chained audit journal (#98).
- Operator CLI, session runner, live authorization from certificate and clean
  Alpaca-paper evidence, offline demo, paper-only MCP previews and deployment
  templates (#99).
- Release documentation, real-data comparison with unchanged gate verdicts,
  wheel installation smoke and tag-triggered release workflow.

### Changed

- Core installation is separated from optional RL, deep-learning, notebook and
  development stacks; NumPy/pandas pins remain unchanged (#96).
- Package metadata now describes the platform and uses the existing maintainer
  identity. Version 1.0.0 is classified beta: live performance is unproven.
- CLI help describes every command/option; session reports retain every attempt
  and show last planned targets on off-cadence days.
- MCP initialization reports the installed package version.

### Fixed

- A single pre-registered parameter set can clear the promotion gate: CSCV now
  computes its absolute OOS loss frequency instead of rejecting one-column input.
  PBO and degradation slope remain not applicable; multi-variant calculations
  and every promotion threshold are unchanged.

[Unreleased]: https://github.com/BichengWang/financial-agent/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/BichengWang/financial-agent/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/BichengWang/financial-agent/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/BichengWang/financial-agent/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/BichengWang/financial-agent/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/BichengWang/financial-agent/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/BichengWang/financial-agent/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/BichengWang/financial-agent/releases/tag/v1.0.0
