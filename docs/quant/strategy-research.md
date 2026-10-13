# Strategy research

Implement the [Strategy protocol](../../src/financial_agent/quant/strategies/base.py):
`name: str`, `warmup: int`, `params() -> dict[str, Any]`, and
`target_weights(data: MarketData) -> pd.Series`. Return finite nonnegative weights
indexed by `data.symbols`, summing to at most one; residual allocation is cash.
Register a factory in [registry.py](../../src/financial_agent/quant/strategies/registry.py)
to expose it through CLI/config. Keep parameter identity JSON-serializable and
stable. Warmup must cover every lookback needed for the first signal.

## Prevent lookahead

The engine supplies `data.upto(decision_session)` and fills at the next open by
default. Compute features solely from that prefix; never capture full-history
frames in a strategy closure or backfill missing observations from future rows.
A strategy can still introduce leakage through external evidence: require dated,
point-in-time inputs and forbid revising old signals using later outcomes.
[research_forecast](../../src/financial_agent/quant/strategies/research.py) uses
package dates; its [real-ledger report](../../reports/quant/research-forecast-validation.md)
fails promotion because history is too short.

Add deterministic, offline tests under `tests/quant/strategies/` for allocations,
warmup, missing data and perturbing observations after the decision. Test fills,
costs, cash and invariants a consumer can observe. An RL policy must implement
this same contract; notebook simulation results do not bypass validation.

## Backtest, validate, certify

Run from the repository root. The example supplies the 11-ETF universe, weekly
next-open execution, whole shares, 2% cash buffer and default modeled costs.
`--end` is inclusive; use only the latest completed session. These dated commands
were executed for the release (the evidence report uses the earlier common
February 6 start rather than the example's March 1 start).

```sh
uv run fa-quant backtest --config examples/quant/paper.toml --end 2026-10-12 --json
uv run fa-quant validate --config examples/quant/paper.toml --end 2026-10-12 --json
uv run fa-quant certify --config examples/quant/paper.toml --end 2026-10-12 \
  --output var/quant-paper/certificate.json
```

With `--config`, strategy, universe, provider, start and backtest settings come
from that file; the standalone flags do not override them. `--grid` does override
the configured grid and accepts an explicit JSON array, not Cartesian shorthand.
Without `--config`, CLI research defaults to zero cash buffer; use a config for
matching paper settings. All market downloads stay in a gitignored cache.

Register a grid before examining results; report its size and every variant.
The release trend grid is target volatility `{0.08, 0.12}` × cap `{0.25, 0.35}`,
four trials. No parameters or thresholds were tuned after evaluation. Default
backtests and the walk-forward switching portfolio are distinct experiments.

Rolling validation uses 1,260 training sessions, 252 test sessions and a five
session embargo, selecting by training Sharpe. It stitches complete disjoint
OOS windows into one cash-continuous portfolio, including switching costs.
Warmup is excluded from variant comparison. Final selected parameters use the
latest complete trailing training window, not necessarily the last historical
fold's winner. The JSON evidence contains fold dates and selected identities.

## Read statistics without overclaiming

- DSR is the probability that observed OOS Sharpe exceeds a benchmark corrected
  for grid size and trial Sharpe variance, using sample skew/kurtosis. It does
  not account for unreported experiments performed outside the disclosed grid.
- CSCV partitions variant returns into 16 blocks and evaluates 12,870 splits.
  PBO measures relative rank reversal of an in-sample winner; probability of OOS
  loss measures its absolute negative Sharpe. Only the latter blocks promotion.
  High PBO means choosing the in-sample winner adds no reliable value even if
  the variants have positive returns.
- A single pre-registered variant still has a defined CSCV loss probability:
  the fraction of partitions where its OOS-half Sharpe is ≤ 0. There is no
  parameter selection, so PBO and degradation slope are `n/a: single pre-registered
  variant` (JSON `null`), not blocking checks. Keep the original single variant;
  adding a grid merely to certify introduces unnecessary multiple testing.
- The 90% circular block-bootstrap Sharpe interval uses 21-session blocks, 2,000
  draws and seed 0. Its lower endpoint is the blocking 5th percentile. It models
  sampling uncertainty under the historical process, not regime-change risk.
- Stress freezes the final selected identity and reruns the full history at
  2× costs or one extra fill-delay session; Sharpe is measured on the same OOS
  dates. It does not repeat rolling selection under the stressed assumptions.

Costs are 2 bps half-spread plus 3 bps slippage per side by default, with zero
commission. Cash and risk-free return are zero. Annualization uses 252 sessions;
turnover is gross traded notional / NAV per year (buys and sells both count).
Full-period metrics start after each strategy's first decision, so warmup and
OOS date ranges differ across strategies. Taxes, borrow, market impact, capacity,
raw tradable corporate-action accounting and actual auction fills are not modeled.

Read every [promotion threshold](safety.md), then inspect execution limits and
paper evidence independently. A historical pass is a reason to investigate
paper execution, not a return forecast or permission to skip the live gate.
