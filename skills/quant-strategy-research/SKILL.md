---
name: quant-strategy-research
description: Researches, backtests, validates and certifies systematic ETF strategies with the fa-quant CLI - adding a strategy to the registry, pre-registering a parameter grid, running backtest/validate/certify, reading the eight promotion checks (walk-forward OOS Sharpe, DSR, CSCV, bootstrap, cost and delay stress) and writing dated evidence under reports/quant. Use when asked to test, compare, tune or promote a quant strategy, or to explain why a strategy passes or fails promotion. Not for placing paper or live orders.
compatibility: Python 3.12 via uv, run from the repository root. The yahoo provider needs network access; the csv provider and fa-quant demo are offline.
---

# Quant strategy research

The package owns the rules: thresholds live in
`src/financial_agent/quant/quant_policy.toml`, the method in
`docs/quant/strategy-research.md` and the gates in `docs/quant/safety.md`.
This skill says how to run them and what an honest result looks like.

## Ground rules

- Freeze the universe, costs, strategy and grid **before** reading any result.
  Report the grid size and every variant, including the failures.
- Never change parameters, the grid, the date range or thresholds after seeing
  a result to make a check pass. Never pass a looser `--policy`; certify with
  the packaged thresholds.
- A failing check is a finding: report the verdict unchanged. Undefined
  statistics fail closed; print them as `n/a` with the reason.
- Historical passes are not return forecasts and never authorize capital.
- Market downloads and state stay in the gitignored `var/` and cache
  directories. Commit only dated aggregate evidence under `reports/quant/`.

## Run the pipeline

Use the latest completed session for `--end` (inclusive). With `--config`, the
file supplies strategy, universe, provider, start and backtest settings; the
standalone flags do not override them, except `--grid` (an explicit JSON array).

```bash
uv run fa-quant data check --config examples/quant/paper.toml --expected-last-session YYYY-MM-DD
uv run fa-quant backtest --config examples/quant/paper.toml --end YYYY-MM-DD --json
uv run fa-quant validate --config examples/quant/paper.toml --end YYYY-MM-DD --json
uv run fa-quant certify --config examples/quant/paper.toml --end YYYY-MM-DD \
  --output var/quant-paper/certificate.json
```

`validate` and `certify` exit 0 when every check passes, 2 when a check or the
data-quality screen fails, 1 on a usage, configuration or data error. `certify`
also writes failed certificates; read the verdict, not the file's existence.

Offline: `uv run fa-quant demo --state-dir var/quant-demo` runs a synthetic
research-to-paper loop, and `examples/quant/local-paper.toml` reads
`SYMBOL.csv` files (`date,open,high,low,close,volume`) from `var/quant-csv`.

## Read the evidence

Report all eight checks against the policy value, not a subset:

| Check | Policy |
|---|---:|
| Complete walk-forward OOS sessions | >= 2,520 |
| OOS net Sharpe | >= 0.5 |
| Deflated Sharpe probability | >= 0.95 |
| CSCV probability of OOS loss | <= 0.10 |
| OOS max drawdown | <= 25% |
| Sharpe at 2x costs | >= 0.3 |
| Sharpe with one extra session of delay | >= 0.3 |
| Bootstrap Sharpe 5th percentile | > 0 |

- PBO is a diagnostic, not a gate. High PBO means picking the in-sample winner
  adds nothing, even when every variant is profitable.
- A single pre-registered variant has `null` PBO and degradation slope. Do not
  add a grid just to certify; that adds multiple testing.
- DSR corrects only for the disclosed grid, not for experiments run outside it.
- Costs default to 2 bps half-spread plus 3 bps slippage per side; taxes,
  impact, capacity and real auction fills are not modeled. Say so.

## Add a strategy

1. Implement the protocol in `src/financial_agent/quant/strategies/base.py`:
   `name`, `warmup`, `params()`, `target_weights(data)` returning finite,
   nonnegative weights over `data.symbols` that sum to at most one.
2. Compute features only from the `data` prefix the engine passes. Never
   capture full-history frames in a closure or backfill from later rows;
   external inputs must be dated and point-in-time.
3. Register a factory in `src/financial_agent/quant/strategies/registry.py`
   with JSON-serializable, stable parameters.
4. Add seeded, network-free tests under `tests/quant/strategies/`: allocations,
   warmup, missing data, and that perturbing bars after the decision session
   leaves the weights unchanged.
5. Pre-register its grid in the config, then run the pipeline above.

## Write the evidence report

Save `reports/quant/YYYY-MM-<slug>.md` with its `.json` beside it, following
`reports/quant/2026-10-default-strategy-evidence.md`: the exact commands, data
provider and date range, grid and every variant, all eight checks with
verdicts, PBO, the selected identity, and the limits above. A strategy that
fails stays documented as failing (see
`reports/quant/research-forecast-validation.md`).
