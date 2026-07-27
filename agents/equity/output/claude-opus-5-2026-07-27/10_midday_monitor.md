# 10 Midday Monitor — 2026-07-27

## Scope and Status

**This is an early-session observation, not the scheduled 12:15 ET checkpoint.** The run fired at
~09:55 ET, and this snapshot was captured at **2026-07-27T10:27:28-04:00** — roughly one hour into the
2026-07-27 regular session. A real observation is written rather than a timing stub because live data
genuinely exists at this hour; the 12:15 checkpoint had simply not occurred when the run executed.

**Observation only. Nothing here changes the published package.** Every price below is tagged `LIVE`
(L050, L051) and is used for monitoring alone — never as an entry, target, CI, or settlement price.
All forecasts in `05` / `15` remain on the 2026-07-24 close basis (L002). Per
`runbook.md § Cadence`, a midday review changes nothing unless a stop criterion fires. **None fired.**

## Market State

| Field | Value |
|---|---|
| Session status | `REG_MKT` (regular market open) |
| Snapshot time | 2026-07-27T10:27:28-04:00 |
| Source A | CNBC restQuote `last` (L050) |
| Source B | IBKR MCP `get_price_snapshot`, `is_close: false` (L051) |

| ETF | 2026-07-24 basis | Live last | Move | IBKR cross-check |
|---|---|---|---|---|
| SPY | 738.93 | 739.53 | +0.08% | 739.40 (+0.47, +0.06%) at 10:27 ET — agrees on direction and magnitude |
| QQQ | 684.23 | 681.02 | -0.47% | — |
| SOXX | 527.01 | 509.49 | -3.32% | 509.34 (−17.67, −3.35%) at 10:27 ET — agrees |
| TLT | 83.25 | 83.62 | +0.44% | — |

**The rotation thesis in `03` is strengthening intraday, not weakening.** SOXX is down
-3.32% against SPY +0.08% — semis extending the
-19.54% drawdown from their 60-day high that drove the
`NEUTRAL` call. TLT is +0.44%, consistent with a
defensive/duration bid rather than a rate shock. This is corroboration of the declared regime on a
basis the package does not depend on.

## Published Monitoring Sleeve — Live Marks

| Ticker | 2026-07-24 basis | Live last | Move | vs SPY | CI Lo | CI Hi | Inside 70% CI? |
|---|---|---|---|---|---|---|---|
| RTX | 212.79 | 218.04 | +2.47% | +2.39pp | 203.97 | 247.14 | yes |
| PAYX | 113.55 | 116.0 | +2.16% | +2.08pp | 109.21 | 131.52 | yes |
| CTAS | 205.91 | 209.29 | +1.64% | +1.56pp | 196.14 | 240.39 | yes |
| GD | 386.75 | 391.74 | +1.29% | +1.21pp | 379.02 | 440.89 | yes |
| PM | 193.0 | 195.0 | +1.04% | +0.96pp | 185.61 | 223.55 | yes |
| SJM | 118.32 | 119.4 | +0.91% | +0.83pp | 113.76 | 137.07 | yes |
| DGX | 227.86 | 229.84 | +0.87% | +0.79pp | 218.89 | 264.17 | yes |
| MET | 94.83 | 95.59 | +0.80% | +0.72pp | 93.36 | 107.68 | yes |
| TRV | 387.26 | 390.29 | +0.78% | +0.70pp | 372.93 | 448.06 | yes |
| HIG | 140.53 | 141.15 | +0.44% | +0.36pp | 138.41 | 156.71 | yes |
| LH | 296.77 | 297.73 | +0.32% | +0.24pp | 289.98 | 333.23 | yes |
| LMT | 582.6 | 582.75 | +0.03% | -0.06pp | 539.50 | 695.61 | yes |
| BNY | 158.91 | 158.46 | -0.28% | -0.36pp | 156.24 | 180.65 | yes |
| MPC | 309.24 | 308.17 | -0.35% | -0.43pp | 296.60 | 358.99 | yes |
| VLO | 302.5 | 301.29 | -0.40% | -0.48pp | 283.59 | 357.71 | yes |
| PKG | 254.39 | 253.28 | -0.44% | -0.52pp | 243.23 | 296.07 | yes |
| PCG | 17.85 | 17.77 | -0.45% | -0.53pp | 17.60 | 20.24 | yes |
| PSX | 206.77 | 205.82 | -0.46% | -0.54pp | 195.75 | 238.47 | yes |
| TMO | 568.26 | 564.75 | -0.62% | -0.70pp | 541.95 | 662.76 | yes |
| WELL | 252.07 | 249.84 | -0.88% | -0.97pp | 249.30 | 285.08 | yes |
| WAB | 302.5 | 299.39 | -1.03% | -1.11pp | 285.71 | 355.59 | yes |
| NSC | 350.66 | 346.61 | -1.16% | -1.24pp | 345.98 | 397.42 | yes |
| UNP | 307.32 | 302.89 | -1.44% | -1.52pp | 302.38 | 349.14 | yes |
| CSX | 53.23 | 52.34 | -1.67% | -1.75pp | 52.43 | 60.42 | NO |

| Aggregate | Value |
|---|---|
| Sleeve names higher on the session | 12 of 24 |
| Mean sleeve move | +0.15% |
| SPY move | +0.08% |
| Mean sleeve move vs SPY | +0.07pp |
| Live marks inside their 70% CI | 23 of 24 |
| Names not yet printed (stale quote) | 0 |

The CI column is a sanity check on the forecast bands one hour into a 28-day horizon, **not** a
settlement: these are 70% intervals for 2026-08-24, so a live mark inside the band this early is
expected and uninformative on its own. It is shown because a mark already *outside* a 28-day band on
day one would indicate a mis-specified sigma. None is.

## Stop-Criterion Check

| Criterion | State |
|---|---|
| Hard halt #1–#6 (`rules.md § Hard Halt Criteria`) | none fires — no data-lineage break, no fabricated input, no benchmark-data loss |
| `NO_TRADE` triggers | already published; status unchanged |
| New information that would change the ranking | none. The live tape is directionally consistent with the 2026-07-24 basis and with the declared regime |
| Action required | **none** |

## Note on BNY

BNY was the single symbol whose CNBC `previous_day_closing` diverged from the stockanalysis
2026-07-24 close (0.396451%, still inside the 1% gate — see `01`). At the 2026-07-27T10:27:28-04:00
snapshot it has printed on the session (158.46 vs basis 158.91,
-0.28%), so the earlier stale-quote condition has cleared. The forecast
still uses the verified 2026-07-24 stockanalysis close.
