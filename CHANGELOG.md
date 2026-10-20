# Changelog

All notable changes are documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `fa-quant status` shows live readiness for Alpaca and IBKR paper configs:
  clean sessions, halts and breaks in the evidence window, mean and per-fill
  slippage against the allowance, certificate verdict, identity match, age and
  expiry, and every unmet reason. It reads only the journal and certificate,
  makes no broker call and grants nothing.

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

[Unreleased]: https://github.com/BichengWang/financial-agent/compare/v1.1.1...HEAD
[1.1.1]: https://github.com/BichengWang/financial-agent/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/BichengWang/financial-agent/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/BichengWang/financial-agent/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/BichengWang/financial-agent/releases/tag/v1.0.0
