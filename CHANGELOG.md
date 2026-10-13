# Changelog

All notable changes are documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/BichengWang/financial-agent/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/BichengWang/financial-agent/releases/tag/v1.0.0
