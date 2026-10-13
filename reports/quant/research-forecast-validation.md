# Research forecast validation

Generated 2026-10-13T07:30:11.568601+00:00. Adjusted Yahoo daily bars: 2025-06-16–2026-10-12 (333 sessions, 239 symbols including SPY). Requested span: 2025-06-14–2026-10-12; the end is the latest completed NYSE session, never an intraday bar.

Loaded 83 packages; accepted 1608 forecasts; 1608 have an active session in the fetched history. Forecast vintages span 2026-06-14–2026-09-03. All eligible historical tickers were fetched, including forecasts now expired; selecting only currently unexpired names would bias history.

Skipped reasons (records unless marked as packages):

| Reason | Count |
|---|---:|
| missing_identity_or_type | 29 |
| type_filter | 240 |

Most recent active run date wins per ticker. Same-date forecasts average mu and sigma equally across models (within-model means) before sizing. Only run_date < decision_session <= target_date is eligible; a package date also bounds row dates from below. Mu and sigma are decimal returns over the same forecast horizon. We use fractional Kelly mu/sigma², clip each name, then scale gross exposure to one. Default type is explicit EQUITY_ALPHA; missing types are skipped rather than invented. No model or sleeve filter is applied; monitoring forecasts are included. Status, confidence, scores and entry prices are metadata, not hindsight selection inputs.

The coordinator-approved warmup is one observed close to match the existing backtester; no price lookback is used. The default 5% cap reads equity policy risk.max_single_name_weight. Fills use next open, whole shares, 2 bps half-spread plus 3 bps slippage, zero commission and a 2% drift threshold. That threshold can leave small residual holdings after a target expires. Cash earns zero. The data cache is gitignored under .cache/quant; no raw price data is committed.

## Net performance versus SPY

Full fetched history includes roughly one year of cash before the first forecast. The second span starts strictly after the first forecast date, with SPY returns on exactly the same sessions. Both summaries are descriptive in-sample evidence, not promotion evidence.

| Cadence / span | Net return | SPY return | Sharpe | SPY Sharpe | Max drawdown | Costs ($) | Trades |
|---|---:|---:|---:|---:|---:|---:|---:|
| weekly / full | 0.00938344 | 0.324267 | 0.349515 | 1.83937 | 0.013851 | 196.762 | 161 |
| weekly / research | 0.00938344 | 0.0542551 | 0.693214 | 1.43905 | 0.013851 | 196.762 | 161 |
| daily / full | -0.0137993 | 0.314812 | -0.380758 | 1.79146 | 0.0294003 | 243.845 | 196 |
| daily / research | -0.0137993 | 0.0539887 | -0.758714 | 1.43885 | 0.0294003 | 243.845 | 196 |

Weekly research span: 2026-06-15–2026-10-12. 664 forecast rows from 67 model/date vintages were active at executed decision dates; skipped fills: 0.


Daily research span: 2026-06-15–2026-10-12. 897 forecast rows from 69 model/date vintages were active at executed decision dates; skipped fills: 0.

## Unchanged promotion gate

Predeclared grid: Kelly fraction {0.25, 0.5} × per-name cap {0.05, 0.10}. The packaged policy remains unchanged: 1260 train sessions, 252 test sessions, five-session embargo and at least 2520 OOS sessions. Undefined statistics are shown explicitly and fail closed.

| Cadence | Check | Value | Threshold | Verdict |
|---|---|---:|---:|---|
| weekly | oos_sessions | 0 | 2520 | FAIL |
| weekly | oos_sharpe | undefined | 0.5 | FAIL |
| weekly | dsr | undefined | 0.95 | FAIL |
| weekly | prob_oos_loss | undefined | 0.1 | FAIL |
| weekly | oos_drawdown | undefined | 0.25 | FAIL |
| weekly | sharpe_2x_costs | undefined | 0.3 | FAIL |
| weekly | sharpe_delay_1 | undefined | 0.3 | FAIL |
| weekly | bootstrap_sharpe_p05 | undefined | 0 | FAIL |
| daily | oos_sessions | 0 | 2520 | FAIL |
| daily | oos_sharpe | undefined | 0.5 | FAIL |
| daily | dsr | undefined | 0.95 | FAIL |
| daily | prob_oos_loss | undefined | 0.1 | FAIL |
| daily | oos_drawdown | undefined | 0.25 | FAIL |
| daily | sharpe_2x_costs | undefined | 0.3 | FAIL |
| daily | sharpe_delay_1 | undefined | 0.3 | FAIL |
| daily | bootstrap_sharpe_p05 | undefined | 0 | FAIL |

Both cadences fail promotion. This short history cannot produce an OOS fold under the unchanged training window, and contains nowhere near ten years of OOS sessions. Net backtest performance does not establish a tradable edge. Continue collecting forecasts and independent outcomes; do not promote this strategy or relax the gate to accommodate the available sample.

The companion JSON contains all checks and failure details, diagnostic PBO, the input manifest hashes, data fingerprint, configuration and generation code. Null means mathematically undefined, not zero. Ticker histories can be incomplete around listings; Yahoo adjustments and historical coverage can change. No missing bar is backfilled; the existing engine skips invalid execution prices and carries only prior marks.

## Reproduce

```sh
uv run python - <<'PY'
import json
from pathlib import Path
report = json.loads(Path('reports/quant/research-forecast-validation.json').read_text())
Path('/tmp/research_report.py').write_text(report['reproduce_python'])
PY
uv run python /tmp/research_report.py
```

Reproduction fetches through the latest completed session at execution time and overwrites the report. The committed snapshot records its own dates and hashes; later runs can differ.
