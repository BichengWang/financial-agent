# Default strategy evidence — October 2026

Computed 2026-10-13T09:18:17.958727+00:00 with package 1.0.0. Yahoo-adjusted OHLCV covers **2006-02-06 through 2026-10-12**, 5203 sessions. The latest completed session at retrieval was October 12. DBC starts February 6, 2006, the common start for the 11 ETFs. This is historical simulation, not observed live performance.

Universe: SPY, QQQ, IWM, EFA, EEM, TLT, IEF, LQD, GLD, DBC, VNQ.

Data fingerprint: `0eadd19f828b291020379d2d2a34d4a1435f64a8d579b3da62184e661bf76fcc`. Fresh network retrieval through `CachedProvider(YahooProvider)`; quality/freshness check passed: True. Per-symbol retrieval timestamps and all exact outputs are in the [JSON companion](2026-10-default-strategy-evidence.json). Raw market data stays in gitignored `var/quant-release-followup-cache/`.

## Protocol

Initial cash $100,000; whole shares; weekly rebalance; drift threshold 2%; next-open fills; cash buffer 2%. Default costs per side: commission zero, half-spread 2 bps and slippage 3 bps. Cash earns zero, rf = 0, annualization 252 sessions. Turnover counts both buys and sells. Total costs are nominal dollars summed over the growing portfolio, not a fixed percent of initial capital.

The trend grid was fixed before evaluation: target_vol 0.08/0.12 × max_weight 0.25/0.35, **four variants**. Dual momentum and both benchmarks use only their unchanged defaults, **one variant each**; no parameter search was introduced to make their gates pass. Each full-period backtest uses the factory default params, rather than the walk-forward selected params. The JSON records both identities. No parameters or thresholds were tuned after seeing results.

## Full-period default backtests

| Strategy | CAGR | Volatility | Sharpe | Sortino | Max drawdown | Calmar | Turnover/year | Total costs ($) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Trend vol target | 5.625% | 7.815% | 0.739515 | 1.018850 | 16.533% | 0.340246 | 14.375008× | 25379.95 |
| Dual momentum | 11.100% | 15.582% | 0.753678 | 1.061713 | 26.397% | 0.420485 | 10.549913× | 29329.56 |
| SPY buy-and-hold | 11.122% | 18.933% | 0.651866 | 0.920796 | 54.299% | 0.204834 | 0.047581× | 48.95 |
| 60/40 SPY/IEF | 8.212% | 10.793% | 0.785288 | 1.123089 | 31.979% | 0.256784 | 0.205604× | 394.99 |

Performance excludes pre-signal warmup separately for each strategy; these are not identical active windows. Fixed-weight benchmarks rebalance under the same weekly/drift rules and retain the same 2% cash reserve. They are not frictionless index returns.

## Walk-forward OOS

Training 1,260 sessions; test 252; embargo five; complete test windows only. One cash-continuous switching portfolio pays transition costs. Trend and momentum have 14 folds; benchmarks have 15 because their warmup is shorter. Exact dates/params and fold Sharpes are in JSON.

| Strategy | OOS dates | Sessions | CAGR | Volatility | Sharpe | Sortino | Max drawdown | Calmar | Turnover/year | Costs ($) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Trend vol target | 2012-02-17–2026-03-02 | 3528 | 5.291% | 7.454% | 0.729028 | 0.995226 | 17.114% | 0.309137 | 14.213488× | 13728.82 |
| Dual momentum | 2012-02-17–2026-03-02 | 3528 | 11.922% | 14.043% | 0.872555 | 1.225808 | 23.422% | 0.508998 | 9.946270× | 13637.07 |
| SPY buy-and-hold | 2011-02-22–2026-03-04 | 3780 | 13.457% | 17.019% | 0.827345 | 1.164033 | 33.533% | 0.401316 | 0.065438× | 49.15 |
| 60/40 SPY/IEF | 2011-02-22–2026-03-04 | 3780 | 9.243% | 9.738% | 0.956652 | 1.363232 | 20.804% | 0.444279 | 0.205460× | 262.33 |

OOS costs and turnover above sum/annualize the switching portfolio only on included OOS dates; warmup and dates outside folds are excluded.

## Selection, stress and bootstrap

| Strategy | Grid | DSR | PBO | Prob. OOS loss | 2× cost Sharpe | +1 session Sharpe | Bootstrap Sharpe 90% CI |
|---|---:|---:|---:|---:|---:|---:|---|
| Trend vol target | 4 | 0.995503 | 0.650350 | 0.000000 | 0.666504 | 0.888777 | [0.338140, 1.158033] |
| Dual momentum | 1 | 0.999351 | n/a: single pre-registered variant | 0.000000 | 0.838737 | 0.873699 | [0.456651, 1.298235] |
| SPY buy-and-hold | 1 | 0.999211 | n/a: single pre-registered variant | 0.000000 | 0.822159 | 0.822141 | [0.453781, 1.250466] |
| 60/40 SPY/IEF | 1 | 0.999874 | n/a: single pre-registered variant | 0.000000 | 0.951089 | 0.949940 | [0.564355, 1.383996] |

CSCV uses 16 partitions and 12,870 combinations for each run. PBO ≈0.65 means the in-sample winner often ranks poorly out of sample: parameter selection adds no reliable value. Probability of absolute OOS loss is zero in these splits; this does not erase the rank-selection warning. For a single pre-registered variant, loss probability is the fraction of CSCV OOS halves with Sharpe ≤ 0. PBO and degradation slope are n/a: single pre-registered variant (JSON `null`), because rank-based selection diagnostics do not apply. DSR corrects only for the disclosed trials.

Bootstrap: circular 21-session blocks, 2,000 draws, seed 0, equal-tailed 90% interval. Stress uses final selected params on the same OOS dates, not a new walk-forward search. One-day delay means one additional session beyond next-open execution.

## Promotion gate — exact computed verdicts

Values below are displayed to six decimals; unrounded values, thresholds, pass flags and original details are in JSON. No check was overridden.

| Check | Threshold | Trend | Dual momentum | SPY | 60/40 |
|---|---:|---|---|---|---|
| oos_sessions | >= 2520.000000 | 3528.000000 PASS | 3528.000000 PASS | 3780.000000 PASS | 3780.000000 PASS |
| oos_sharpe | >= 0.500000 | 0.729028 PASS | 0.872555 PASS | 0.827345 PASS | 0.956652 PASS |
| dsr | >= 0.950000 | 0.995503 PASS | 0.999351 PASS | 0.999211 PASS | 0.999874 PASS |
| prob_oos_loss | <= 0.100000 | 0.000000 PASS | 0.000000 PASS | 0.000000 PASS | 0.000000 PASS |
| oos_drawdown | <= 0.250000 | 0.171145 PASS | 0.234218 PASS | 0.335326 FAIL | 0.208038 PASS |
| sharpe_2x_costs | >= 0.300000 | 0.666504 PASS | 0.838737 PASS | 0.822159 PASS | 0.951089 PASS |
| sharpe_delay_1 | >= 0.300000 | 0.888777 PASS | 0.873699 PASS | 0.822141 PASS | 0.949940 PASS |
| bootstrap_sharpe_p05 | > 0.000000 | 0.338140 PASS | 0.456651 PASS | 0.453781 PASS | 0.564355 PASS |
| **Verdict** | All eight pass | **PASS** | **PASS** | **FAIL** | **PASS** |

## Conclusion

The default trend grid clears the historical promotion policy, with materially smaller full-period drawdown than SPY and 60/40 in this sample. Its high PBO gives no basis for claiming the selected variant is superior. Dual momentum and 60/40 also clear all eight statistical checks as single pre-registered variants. SPY fails the OOS drawdown budget. The single-variant loss probabilities are computed from CSCV OOS halves; no parameter grid or threshold was added to manufacture a pass.

The pass supports a controlled paper investigation only. Runtime caps and fresh Alpaca-paper evidence still apply; default dual momentum top_k=3 allocates 33.3% per slot, exceeding the 30% per-name cap, and concentrated SPY/60-40 benchmarks also exceed runtime limits. There is no live-performance evidence, profit guarantee, or recommendation to allocate capital.

## Data caveats

Yahoo adjusted prices incorporate splits/dividends retrospectively and may be revised; adjusted openings are proxies for total-return simulation, not raw auction executions. The cache/fingerprint records this retrieval, not a guarantee of reproducing later vendor revisions. The fixed present-day ETF universe excludes defunct or unavailable alternatives; broad funds reduce single-stock survivorship problems but do not eliminate selection bias. No taxes, cash interest, market-impact/capacity model, exact corporate-action share accounting or actual broker fills. rf = 0. Historical bootstrap and DSR cannot establish future regimes.

## Reproduce

First reconstruct the exact four research configs from the committed JSON (paths are relative to `var/release-evidence`):

```sh
uv run python - <<'PY'
import json
from pathlib import Path
e = json.loads(Path('reports/quant/2026-10-default-strategy-evidence.json').read_text())
root = Path('var/release-evidence')
root.mkdir(parents=True, exist_ok=True)
for name, result in e['strategies'].items():
    (root / f'{name}.toml').write_text(result['config_toml'])
PY
for strategy in trend_vol_target dual_momentum buy_and_hold sixty_forty; do
  uv run fa-quant backtest --config "var/release-evidence/$strategy.toml" --end 2026-10-12 --json
  uv run fa-quant validate --config "var/release-evidence/$strategy.toml" --end 2026-10-12 --json
  uv run fa-quant certify --config "var/release-evidence/$strategy.toml" --end 2026-10-12 \
    --output "var/release-evidence/$strategy-certificate.json" --json
done
```

These commands were run with real network retrieval. Expected exit statuses: backtests 0; trend, dual momentum and 60/40 validate/certify 0; SPY validate/certify 2. Certificates carry the computed verdict and identity. CLI reports the bootstrap lower endpoint; the companion adds the upper endpoint and fold detail using `walk_forward` and `block_bootstrap_ci` with the same packaged policy/default seed, asserting the lower endpoint equals CLI output.
