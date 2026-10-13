# Platform architecture

`financial_agent.quant` is a long-only, unlevered ETF platform. The binding
[contracts](../../plan/2026-10-12-risk-managed-trading-platform.md#32-contracts)
connect research, validation, paper execution and an explicitly authorized live
runner. The historical RL and deep-learning stacks remain research code.

| Module | Contract and invariant |
|---|---|
| [data](../../src/financial_agent/quant/data/) | `BarProvider.fetch(symbols, start, end)` uses inclusive dates. Immutable `MarketData` has aligned, ascending, unique, timezone-naive session frames; `upto` includes only observations at or before a decision. `fingerprint` hashes OHLCV values and axes. |
| [strategies](../../src/financial_agent/quant/strategies/base.py) | `Strategy.name`, `warmup`, `params()` and `target_weights(data)` describe a JSON-serializable identity and nonnegative weights summing to at most one. Unallocated weight is cash. |
| [backtest](../../src/financial_agent/quant/backtest/) | `run_backtest(strategy, data, config)` supplies only the decision prefix, fills later, and charges commission, spread and slippage. `BacktestResult.summary()` excludes pre-signal warmup from performance and annual turnover. |
| [portfolio](../../src/financial_agent/quant/portfolio.py) | `rebalance_deltas` converts weights into share deltas; the runner and backtester share drift, rounding and minimum-notional behavior. Targets are scaled proportionally only above the configured cash-buffer ceiling. |
| [validation](../../src/financial_agent/quant/validation/) | Rolling training selection, embargoed disjoint OOS windows and one cash-continuous switching portfolio. Eight promotion checks, DSR, CSCV loss/PBO, bootstrap and execution stress. Certificates bind parameters, data fingerprint, policy bytes and package version. |
| [risk](../../src/financial_agent/quant/risk/) | Tighten-only `RiskLimits`, deterministic `plan_orders`, whole-plan `check_orders`, persisted `RiskState` and `KillSwitch`. Rejected plans approve no orders. |
| [execution](../../src/financial_agent/quant/execution/) | `Broker.account/submit/open_orders/cancel_all`; persisted local `PaperBroker` and Alpaca REST adapter. Client IDs make submission idempotent. `Journal` is hash-chained JSONL; `reconcile` compares expected and observed quantities. |
| [runner](../../src/financial_agent/quant/runner/) | `TradingConfig.load` validates TOML and resolves paths from its directory. `run_session(config, today=..., dry_run=...)` locks state, validates data and journal, authorizes live, synchronizes/reconciles, checks risk, journals intents, submits and writes reports. |
| [CLI](../../src/financial_agent/quant/__main__.py) / [MCP](../../src/financial_agent/quant/mcp.py) | Operator commands and research tools reuse these modules. MCP accepts paper configurations only and cannot submit, cancel, kill, unkill or reach live mode. |

Yahoo uses `auto_adjust=True`; the cache stores per-symbol CSV and retrieval
metadata, refreshes a five-session overlap and refetches history when adjustments
change. CSV sources must explicitly supply consistent adjusted OHLCV. Quality
checks distinguish errors from warnings; the runner checks freshness against the
previous completed exchange session.

A trading session decides from the previous close and submits whole-share OPG
orders for today's opening auction. Local paper settlement is observed on the
following invocation, once today's bar is available. Weekly/monthly cadence
controls planning, while journal integrity, synchronization, reconciliation and
account loss checks still run daily. Restart recovery looks up persisted intents
before resubmitting; an unresolved earlier-day intent is observed or abandoned,
never blindly sent at a later auction.

State lives under the configured `state_dir`: `journal.jsonl`, `risk_state.json`,
`paper.json` for local paper, kill-switch files, `session.lock`, and reports.
Reports preserve the first attempt as `DATE.json/.md`; later attempts use
`DATE.2`, `DATE.3`, and so on. Previews have a separate `DATE.preview` stem.
`status` reads persisted observations and does not refresh the broker.

Hash chains and certificate hashes detect accidental alteration; they are not
signatures or protection against an operator able to rewrite files and hashes.
Use a protected, backed-up state directory. See [safety](safety.md) and
[operations](operations.md) for the boundaries of the guarantee.
