# 02 — Reflection · 2026-08-27

Standalone MoM reflection. Every price, return and regime claim below cites `01` Source Ledger rows
or is marked `UNAVAILABLE`. Generated from `settlement_manifest.json`, `settlements_this_run.json`
and `run_computed_manifest.json`.

## 0. Prediction Settlement

### Scan scope

All 79 dated output packages under `agents/equity/output/` were scanned for
`15_predictions.json` files, across every model — settlement is keyed to each prediction's own
`target_date`, never to folder-window proximity (`agents.md § Orchestrator Step 1`). The canonical
ledger (`settlement_ledger.py`, L014) is the single normalizer; due inventory, precedence and rolling
metrics below are read from its manifest and not re-derived by hand.

### This run's settlement batch

Due inventory at fire: **231** keys. Settled: **229**.
Left due: **2** (both `EQR`, see below). Conflicts: **0**.

| Timing flag | Keys | Basis used |
|---|---|---|
| `WEEKEND_TARGET` | 26 | target_date 2026-08-23 is a Sunday -> settled at the last completed close at or before it (Friday 2026-08-21) |
| `ORDINARY` | 153 | target_date 2026-08-24 / -25 / -26, all completed trading sessions before the run date -> settled at each target date's own close |
| `TARGET_DATE_CLOSE` | 50 | target_date == run_date 2026-08-27; post-close fire, so `settled_at` carries a timezone-aware timestamp at/after 16:00 America/New_York and the completed target-date close is used |

| Record type | Settled | HIT | MISS | Flat call | IN_CI | Mean alpha | Mean z |
|---|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 202 | 54 | 148 | n/a | 150 | -2.64% | -0.5825 |
| `MARKET_FORECAST` | 27 | 16 | 7 | 4 | 25 | N/A - raw return | +0.5267 |

`MARKET_FORECAST` records settle on **raw return, not alpha** (`rules.md § Settlement Rules`); a
`|mu| < 0.5%` call is scored `N/A - FLAT_CALL` and contributes only CI calibration and z.

Batch hit rate for `EQUITY_ALPHA` is **26.73%** (54 of 202) against a
mean realized alpha of **-2.64%** — the settled cohort spans vintages
2026-07-26 through 2026-07-30 across 2 models
(claude-opus-5 134, gpt-5 95), resolving into a single late-August window.

### Unsettleable — corporate action

| Model | Vintage | Ticker | Target date | Classification | Disposition |
|---|---|---|---|---|---|
| claude-opus-5 | 2026-07-26 | EQR | 2026-08-23 | `CORPORATE_ACTION_RENAMED` | left **due**; no exchange ratio inferred and no settlement against the successor symbol |
| gpt-5 | 2026-07-27 | EQR | 2026-08-24 | `CORPORATE_ACTION_RENAMED` | left **due**; no exchange ratio inferred and no settlement against the successor symbol |

`EQR` was renamed into / absorbed by `VMRK` (Vivmark Residential). Detection followed the Track B
procedure accepted 2026-08-22 and effective 2026-08-23 (L025): the bulk fetch transport-failed
(HTTP 400), the Nasdaq screener carries no `EQR` row while `VMRK` is present at $51.58B in Real
Estate, and CNBC no longer resolves the US listing at all. Leaving the keys due is the specified
outcome — a settlement against a successor would be a fabricated price, and due inventory feeds
`eff_n`, which gates all Track A work.

### Rolling calibration metrics (canonical ledger, all models, all time)

Read **before** scoring, per `agents.md § Factor Scoring — Calibration Feedback Binding`. The
pre-write column is the state that binds this run's scoring; the post-write column verifies that this
run's 229 rows were absorbed as canonical.

| Metric | `EQUITY_ALPHA` (pre-write) | `EQUITY_ALPHA` (post-write) | `MARKET_FORECAST` (pre-write) | `MARKET_FORECAST` (post-write) | Healthy range |
|---|---|---|---|---|---|
| Raw `n` | 1153 | 1355 | 174 | 201 | >= 10 to report; >= 20 for Track A |
| 28-day `eff_n` | 2 | 2 | 2 | 2 | >= 3 for Track A |
| Hit rate | 39.38% | 37.49% | 35.71% | 40.11% | > 50% |
| CI coverage | 71.47% | 71.88% | 90.23% | 90.55% | 55% - 85% (target 70%) |
| Mean z | -0.5506 | -0.5553 | -0.2952 | -0.1848 | -0.5 to +0.5 |
| Track A eligible | False | False | False | False | raw n >= 20 **and** eff_n >= 3 |

Rank IC by vintage (`EQUITY_ALPHA`, Spearman of `adj_score` vs `realized_alpha` within each vintage,
L014c): **60 vintages**, mean **-0.0840**, median **-0.0567**,
**55.00%** at or below zero.

**Bindings that fire this run:**

- CI coverage 71.47% is inside the 55–85% band, so the "widen sigma sourcing"
  binding does **not** fire and `REALIZED_VOL_30D` stands as the sigma source for every ranked name.
- Aggregate rank IC is negative over far more than 20 settled predictions, so **all confidence is
  capped at `MEDIUM`** and no positive per-name `mu` adjustment is applied — every `mu` in `05` is
  the unmodified calibration-table band value for the name's percentile.
- Mean z -0.5553 sits just outside the −0.5…+0.5 healthy band, i.e. realized returns
  run below `mu` by about half a sigma. The corrective (shrink the mu prior) is a **Track A** change
  and `eff_n = 2` < 3, so it is recorded as an observation and `DEFER`red in `13`,
  not proposed.

**`eff_n` status.** Both record types remain at `eff_n = 2`. The manifest's projection is falsifiable
and unchanged: `EQUITY_ALPHA` increments to 3 on **2026-09-03**
(24 pending predictions at that date) and
`MARKET_FORECAST` on **2026-09-07**
(3 pending). Adding 229 settlements
moved raw `EQUITY_ALPHA` `n` from 1153 to 1355 while `eff_n` stayed at 2 — exactly the
behaviour the metric is designed to expose, since the new target dates (2026-08-27
latest) sit inside the window already opened on 2026-08-05.

### Settled predictions (all 229)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z | Timing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | gpt-5-2026-07-30 | 333.43 | 2026-08-27 | +6.00% | -5.65% | +3.97% | -9.62% | MISS | OUT_CI_LOW | -1.233 | `TARGET_DATE_CLOSE` |
| ACGL | claude-opus-5-2026-07-29 | 106.48 | 2026-08-26 | +6.00% | -5.41% | +3.40% | -8.81% | MISS | OUT_CI_LOW | -1.534 | `ORDINARY` |
| ADP | claude-opus-5-2026-07-29 | 264.17 | 2026-08-26 | +6.00% | +6.52% | +3.40% | +3.11% | HIT | IN_CI | +0.052 | `ORDINARY` |
| ADP | gpt-5-2026-07-29 | 264.17 | 2026-08-26 | +6.00% | +6.52% | +3.40% | +3.11% | HIT | IN_CI | +0.053 | `ORDINARY` |
| ADP | claude-opus-5-2026-07-30 | 273.37 | 2026-08-27 | +6.00% | +4.14% | +5.71% | -1.57% | MISS | IN_CI | -0.183 | `TARGET_DATE_CLOSE` |
| ADP | gpt-5-2026-07-30 | 263.87 | 2026-08-27 | +6.00% | +7.89% | +3.97% | +3.92% | HIT | IN_CI | +0.179 | `TARGET_DATE_CLOSE` |
| AMP | gpt-5-2026-07-29 | 546.62 | 2026-08-26 | +6.00% | +2.50% | +3.40% | -0.91% | MISS | IN_CI | -0.447 | `ORDINARY` |
| AON | gpt-5-2026-07-30 | 366.57 | 2026-08-27 | +6.00% | -4.64% | +3.97% | -8.61% | MISS | OUT_CI_LOW | -1.085 | `TARGET_DATE_CLOSE` |
| AWK | gpt-5-2026-07-30 | 136.81 | 2026-08-27 | +6.00% | -0.09% | +3.97% | -4.05% | MISS | IN_CI | -0.810 | `TARGET_DATE_CLOSE` |
| BAX | gpt-5-2026-07-30 | 26.75 | 2026-08-27 | +6.00% | -3.07% | +3.97% | -7.03% | MISS | IN_CI | -0.647 | `TARGET_DATE_CLOSE` |
| BBY | claude-opus-5-2026-07-28 | 88.45 | 2026-08-25 | +6.00% | -3.57% | +3.63% | -7.20% | MISS | OUT_CI_LOW | -1.071 | `ORDINARY` |
| BBY | gpt-5-2026-07-28 | 88.45 | 2026-08-25 | +6.00% | -3.57% | +3.63% | -7.20% | MISS | OUT_CI_LOW | -1.071 | `ORDINARY` |
| BBY | claude-opus-5-2026-07-29 | 89.47 | 2026-08-26 | +6.00% | -2.27% | +3.40% | -5.67% | MISS | IN_CI | -0.915 | `ORDINARY` |
| BBY | claude-opus-5-2026-07-30 | 90.17 | 2026-08-27 | +6.00% | -7.33% | +5.71% | -13.04% | MISS | OUT_CI_LOW | -1.501 | `TARGET_DATE_CLOSE` |
| BBY | gpt-5-2026-07-30 | 87.82 | 2026-08-27 | +6.00% | -4.85% | +3.97% | -8.82% | MISS | OUT_CI_LOW | -1.234 | `TARGET_DATE_CLOSE` |
| BNY | claude-opus-5-2026-07-26 | 158.91 | 2026-08-23 | +6.00% | -0.26% | +3.63% | -3.89% | MISS | IN_CI | -0.848 | `WEEKEND_TARGET` |
| BNY | claude-opus-5-2026-07-27 | 158.91 | 2026-08-24 | +6.00% | +2.03% | +3.32% | -1.29% | MISS | IN_CI | -0.537 | `ORDINARY` |
| BNY | gpt-5-2026-07-27 | 158.91 | 2026-08-24 | +6.00% | +2.03% | +3.32% | -1.29% | MISS | IN_CI | -0.537 | `ORDINARY` |
| BNY | claude-opus-5-2026-07-28 | 157.77 | 2026-08-25 | +6.00% | +3.73% | +3.63% | +0.10% | HIT | IN_CI | -0.315 | `ORDINARY` |
| BRO | claude-opus-5-2026-07-29 | 73.65 | 2026-08-26 | +6.00% | -1.18% | +3.40% | -4.59% | MISS | IN_CI | -0.622 | `ORDINARY` |
| BRO | gpt-5-2026-07-29 | 73.65 | 2026-08-26 | +6.00% | -1.18% | +3.40% | -4.59% | MISS | IN_CI | -0.633 | `ORDINARY` |
| BRO | claude-opus-5-2026-07-30 | 74.87 | 2026-08-27 | +6.00% | -4.65% | +5.71% | -10.36% | MISS | IN_CI | -0.930 | `TARGET_DATE_CLOSE` |
| BRO | gpt-5-2026-07-30 | 70.87 | 2026-08-27 | +6.00% | +0.73% | +3.97% | -3.23% | MISS | IN_CI | -0.427 | `TARGET_DATE_CLOSE` |
| BXP | claude-opus-5-2026-07-30 | 72.97 | 2026-08-27 | +6.00% | -4.11% | +5.71% | -9.82% | MISS | OUT_CI_LOW | -1.188 | `TARGET_DATE_CLOSE` |
| BXP | gpt-5-2026-07-30 | 71.67 | 2026-08-27 | +6.00% | -2.37% | +3.97% | -6.34% | MISS | IN_CI | -0.981 | `TARGET_DATE_CLOSE` |
| CB | claude-opus-5-2026-07-26 | 359.75 | 2026-08-23 | +6.00% | -5.21% | +3.63% | -8.84% | MISS | OUT_CI_LOW | -1.367 | `WEEKEND_TARGET` |
| CB | gpt-5-2026-07-27 | 359.75 | 2026-08-24 | +6.00% | -3.87% | +3.32% | -7.19% | MISS | OUT_CI_LOW | -1.203 | `ORDINARY` |
| CB | claude-opus-5-2026-07-28 | 358.91 | 2026-08-25 | +6.00% | -4.40% | +3.63% | -8.03% | MISS | OUT_CI_LOW | -1.296 | `ORDINARY` |
| CB | gpt-5-2026-07-28 | 358.91 | 2026-08-25 | +6.00% | -4.40% | +3.63% | -8.03% | MISS | OUT_CI_LOW | -1.296 | `ORDINARY` |
| CPAY | claude-opus-5-2026-07-30 | 392.85 | 2026-08-27 | +6.00% | +2.75% | +5.71% | -2.95% | MISS | IN_CI | -0.342 | `TARGET_DATE_CLOSE` |
| CSX | claude-opus-5-2026-07-26 | 53.23 | 2026-08-23 | +6.00% | -3.08% | +3.63% | -6.71% | MISS | OUT_CI_LOW | -1.258 | `WEEKEND_TARGET` |
| CSX | claude-opus-5-2026-07-27 | 53.23 | 2026-08-24 | +6.00% | -3.36% | +3.32% | -6.68% | MISS | OUT_CI_LOW | -1.297 | `ORDINARY` |
| CSX | gpt-5-2026-07-27 | 53.23 | 2026-08-24 | +6.00% | -3.36% | +3.32% | -6.68% | MISS | OUT_CI_LOW | -1.297 | `ORDINARY` |
| CSX | claude-opus-5-2026-07-28 | 51.80 | 2026-08-25 | +6.00% | -0.56% | +3.63% | -4.19% | MISS | IN_CI | -0.884 | `ORDINARY` |
| CSX | gpt-5-2026-07-28 | 51.80 | 2026-08-25 | +6.00% | -0.56% | +3.63% | -4.19% | MISS | IN_CI | -0.884 | `ORDINARY` |
| CTAS | claude-opus-5-2026-07-26 | 205.91 | 2026-08-23 | +6.00% | -1.03% | +3.63% | -4.66% | MISS | IN_CI | -0.680 | `WEEKEND_TARGET` |
| CTAS | claude-opus-5-2026-07-27 | 205.91 | 2026-08-24 | +6.00% | +0.72% | +3.32% | -2.60% | MISS | IN_CI | -0.511 | `ORDINARY` |
| CTAS | gpt-5-2026-07-27 | 205.91 | 2026-08-24 | +6.00% | +0.72% | +3.32% | -2.60% | MISS | IN_CI | -0.511 | `ORDINARY` |
| CTAS | claude-opus-5-2026-07-28 | 210.98 | 2026-08-25 | +6.00% | -2.95% | +3.63% | -6.58% | MISS | IN_CI | -0.870 | `ORDINARY` |
| CTAS | gpt-5-2026-07-28 | 210.98 | 2026-08-25 | +6.00% | -2.95% | +3.63% | -6.58% | MISS | IN_CI | -0.870 | `ORDINARY` |
| CTAS | claude-opus-5-2026-07-29 | 214.90 | 2026-08-26 | +6.00% | -4.24% | +3.40% | -7.65% | MISS | IN_CI | -1.020 | `ORDINARY` |
| CTAS | gpt-5-2026-07-29 | 214.90 | 2026-08-26 | +6.00% | -4.24% | +3.40% | -7.65% | MISS | IN_CI | -1.038 | `ORDINARY` |
| CTAS | claude-opus-5-2026-07-30 | 216.53 | 2026-08-27 | +6.00% | -5.72% | +5.71% | -11.43% | MISS | OUT_CI_LOW | -1.178 | `TARGET_DATE_CLOSE` |
| CTAS | gpt-5-2026-07-30 | 206.79 | 2026-08-27 | +6.00% | -1.28% | +3.97% | -5.24% | MISS | IN_CI | -0.681 | `TARGET_DATE_CLOSE` |
| DGX | claude-opus-5-2026-07-26 | 227.86 | 2026-08-23 | +6.00% | +7.25% | +3.63% | +3.63% | HIT | IN_CI | +0.131 | `WEEKEND_TARGET` |
| DGX | claude-opus-5-2026-07-27 | 227.86 | 2026-08-24 | +6.00% | +7.03% | +3.32% | +3.71% | HIT | IN_CI | +0.107 | `ORDINARY` |
| DGX | gpt-5-2026-07-27 | 227.86 | 2026-08-24 | +6.00% | +7.03% | +3.32% | +3.71% | HIT | IN_CI | +0.107 | `ORDINARY` |
| DGX | claude-opus-5-2026-07-28 | 231.84 | 2026-08-25 | +6.00% | +5.46% | +3.63% | +1.84% | HIT | IN_CI | -0.057 | `ORDINARY` |
| DGX | gpt-5-2026-07-28 | 231.84 | 2026-08-25 | +6.00% | +5.46% | +3.63% | +1.84% | HIT | IN_CI | -0.057 | `ORDINARY` |
| DGX | claude-opus-5-2026-07-29 | 235.94 | 2026-08-26 | +6.00% | +3.84% | +3.40% | +0.44% | HIT | IN_CI | -0.224 | `ORDINARY` |
| DVA | claude-opus-5-2026-07-30 | 240.96 | 2026-08-27 | +6.00% | -25.76% | +5.71% | -31.47% | MISS | OUT_CI_LOW | -5.761 | `TARGET_DATE_CLOSE` |
| EXR | claude-opus-5-2026-07-28 | 148.29 | 2026-08-25 | +6.00% | -2.31% | +3.63% | -5.94% | MISS | OUT_CI_LOW | -1.307 | `ORDINARY` |
| EXR | gpt-5-2026-07-28 | 148.29 | 2026-08-25 | +6.00% | -2.31% | +3.63% | -5.94% | MISS | OUT_CI_LOW | -1.307 | `ORDINARY` |
| EXR | claude-opus-5-2026-07-29 | 152.21 | 2026-08-26 | +6.00% | -5.33% | +3.40% | -8.74% | MISS | OUT_CI_LOW | -1.659 | `ORDINARY` |
| F | claude-opus-5-2026-07-30 | 15.28 | 2026-08-27 | +6.00% | -8.70% | +5.71% | -14.41% | MISS | OUT_CI_LOW | -1.850 | `TARGET_DATE_CLOSE` |
| FICO | claude-opus-5-2026-07-30 | 1373.08 | 2026-08-27 | +6.00% | -15.73% | +5.71% | -21.44% | MISS | OUT_CI_LOW | -1.820 | `TARGET_DATE_CLOSE` |
| FTNT | claude-opus-5-2026-07-30 | 153.22 | 2026-08-27 | +6.00% | +12.77% | +5.71% | +7.06% | HIT | IN_CI | +0.650 | `TARGET_DATE_CLOSE` |
| GD | claude-opus-5-2026-07-26 | 386.75 | 2026-08-23 | +6.00% | -0.64% | +3.63% | -4.26% | MISS | IN_CI | -0.863 | `WEEKEND_TARGET` |
| GD | claude-opus-5-2026-07-27 | 386.75 | 2026-08-24 | +6.00% | -0.77% | +3.32% | -4.09% | MISS | IN_CI | -0.880 | `ORDINARY` |
| GD | gpt-5-2026-07-27 | 386.75 | 2026-08-24 | +6.00% | -0.77% | +3.32% | -4.09% | MISS | IN_CI | -0.880 | `ORDINARY` |
| GEHC | claude-opus-5-2026-07-30 | 71.90 | 2026-08-27 | +6.00% | +0.81% | +5.71% | -4.90% | MISS | IN_CI | -0.350 | `TARGET_DATE_CLOSE` |
| GRMN | claude-opus-5-2026-07-30 | 294.83 | 2026-08-27 | +6.00% | -1.68% | +5.71% | -7.39% | MISS | IN_CI | -0.497 | `TARGET_DATE_CLOSE` |
| HIG | claude-opus-5-2026-07-26 | 140.53 | 2026-08-23 | +5.00% | -3.15% | +3.63% | -6.78% | MISS | OUT_CI_LOW | -1.302 | `WEEKEND_TARGET` |
| HIG | claude-opus-5-2026-07-27 | 140.53 | 2026-08-24 | +5.00% | -1.10% | +3.32% | -4.42% | MISS | IN_CI | -0.975 | `ORDINARY` |
| HIG | gpt-5-2026-07-27 | 140.53 | 2026-08-24 | +5.00% | -1.10% | +3.32% | -4.42% | MISS | IN_CI | -0.975 | `ORDINARY` |
| HPQ | claude-opus-5-2026-07-30 | 28.41 | 2026-08-27 | +6.00% | +4.29% | +5.71% | -1.41% | MISS | IN_CI | -0.147 | `TARGET_DATE_CLOSE` |
| HUM | claude-opus-5-2026-07-30 | 365.41 | 2026-08-27 | +6.00% | +7.45% | +5.71% | +1.74% | HIT | IN_CI | +0.132 | `TARGET_DATE_CLOSE` |
| IEX | claude-opus-5-2026-07-30 | 229.52 | 2026-08-27 | +6.00% | +1.94% | +5.71% | -3.77% | MISS | IN_CI | -0.785 | `TARGET_DATE_CLOSE` |
| INCY | claude-opus-5-2026-07-29 | 129.93 | 2026-08-26 | +6.00% | -1.39% | +3.40% | -4.80% | MISS | IN_CI | -0.571 | `ORDINARY` |
| INCY | gpt-5-2026-07-29 | 129.93 | 2026-08-26 | +6.00% | -1.39% | +3.40% | -4.80% | MISS | IN_CI | -0.581 | `ORDINARY` |
| INCY | claude-opus-5-2026-07-30 | 127.10 | 2026-08-27 | +6.00% | +0.50% | +5.71% | -5.20% | MISS | IN_CI | -0.464 | `TARGET_DATE_CLOSE` |
| INCY | gpt-5-2026-07-30 | 122.99 | 2026-08-27 | +6.00% | +3.86% | +3.97% | -0.10% | MISS | IN_CI | -0.180 | `TARGET_DATE_CLOSE` |
| IQV | claude-opus-5-2026-07-28 | 213.22 | 2026-08-25 | +6.00% | +21.67% | +3.63% | +18.04% | HIT | OUT_CI_HIGH | +1.388 | `ORDINARY` |
| IQV | gpt-5-2026-07-28 | 213.22 | 2026-08-25 | +6.00% | +21.67% | +3.63% | +18.04% | HIT | OUT_CI_HIGH | +1.388 | `ORDINARY` |
| IQV | claude-opus-5-2026-07-29 | 242.94 | 2026-08-26 | +6.00% | +7.64% | +3.40% | +4.24% | HIT | IN_CI | +0.103 | `ORDINARY` |
| IQV | gpt-5-2026-07-29 | 242.94 | 2026-08-26 | +6.00% | +7.64% | +3.40% | +4.24% | HIT | IN_CI | +0.104 | `ORDINARY` |
| IQV | claude-opus-5-2026-07-30 | 247.56 | 2026-08-27 | +6.00% | +5.99% | +5.71% | +0.28% | HIT | IN_CI | -0.001 | `TARGET_DATE_CLOSE` |
| ITW | claude-opus-5-2026-07-28 | 284.82 | 2026-08-25 | +6.00% | -1.11% | +3.63% | -4.74% | MISS | OUT_CI_LOW | -1.069 | `ORDINARY` |
| ITW | gpt-5-2026-07-28 | 284.82 | 2026-08-25 | +6.00% | -1.11% | +3.63% | -4.74% | MISS | OUT_CI_LOW | -1.069 | `ORDINARY` |
| ITW | claude-opus-5-2026-07-29 | 295.16 | 2026-08-26 | +6.00% | -3.27% | +3.40% | -6.67% | MISS | OUT_CI_LOW | -1.276 | `ORDINARY` |
| ITW | gpt-5-2026-07-29 | 295.16 | 2026-08-26 | +6.00% | -3.27% | +3.40% | -6.67% | MISS | OUT_CI_LOW | -1.298 | `ORDINARY` |
| IVZ | claude-opus-5-2026-07-28 | 30.11 | 2026-08-25 | +6.00% | +8.67% | +3.63% | +5.04% | HIT | IN_CI | +0.243 | `ORDINARY` |
| IVZ | gpt-5-2026-07-28 | 30.11 | 2026-08-25 | +6.00% | +8.67% | +3.63% | +5.04% | HIT | IN_CI | +0.243 | `ORDINARY` |
| KO | claude-opus-5-2026-07-29 | 88.27 | 2026-08-26 | +6.00% | +2.05% | +3.40% | -1.35% | MISS | IN_CI | -0.481 | `ORDINARY` |
| KO | gpt-5-2026-07-29 | 88.27 | 2026-08-26 | +6.00% | +2.05% | +3.40% | -1.35% | MISS | IN_CI | -0.489 | `ORDINARY` |
| LH | claude-opus-5-2026-07-27 | 296.77 | 2026-08-24 | +5.00% | +14.34% | +3.32% | +11.02% | HIT | OUT_CI_HIGH | +1.334 | `ORDINARY` |
| LH | gpt-5-2026-07-30 | 315.53 | 2026-08-27 | +6.00% | +6.66% | +3.97% | +2.69% | HIT | IN_CI | +0.082 | `TARGET_DATE_CLOSE` |
| LMT | claude-opus-5-2026-07-26 | 582.60 | 2026-08-23 | +6.00% | -3.27% | +3.63% | -6.89% | MISS | IN_CI | -0.719 | `WEEKEND_TARGET` |
| LMT | claude-opus-5-2026-07-27 | 582.60 | 2026-08-24 | +6.00% | -3.17% | +3.32% | -6.49% | MISS | IN_CI | -0.712 | `ORDINARY` |
| LMT | gpt-5-2026-07-27 | 582.60 | 2026-08-24 | +6.00% | -3.17% | +3.32% | -6.49% | MISS | IN_CI | -0.712 | `ORDINARY` |
| LMT | claude-opus-5-2026-07-28 | 580.00 | 2026-08-25 | +6.00% | -4.05% | +3.63% | -7.68% | MISS | IN_CI | -0.825 | `ORDINARY` |
| MET | claude-opus-5-2026-07-26 | 94.83 | 2026-08-23 | +6.00% | -0.52% | +3.63% | -4.14% | MISS | IN_CI | -0.898 | `WEEKEND_TARGET` |
| MET | claude-opus-5-2026-07-27 | 94.83 | 2026-08-24 | +6.00% | +1.46% | +3.32% | -1.87% | MISS | IN_CI | -0.626 | `ORDINARY` |
| MET | gpt-5-2026-07-27 | 94.83 | 2026-08-24 | +6.00% | +1.46% | +3.32% | -1.87% | MISS | IN_CI | -0.626 | `ORDINARY` |
| MET | claude-opus-5-2026-07-28 | 95.19 | 2026-08-25 | +6.00% | +0.71% | +3.63% | -2.91% | MISS | IN_CI | -0.751 | `ORDINARY` |
| MET | gpt-5-2026-07-28 | 95.19 | 2026-08-25 | +6.00% | +0.71% | +3.63% | -2.91% | MISS | IN_CI | -0.751 | `ORDINARY` |
| MPC | claude-opus-5-2026-07-26 | 309.24 | 2026-08-23 | +6.00% | +16.65% | +3.63% | +13.02% | HIT | OUT_CI_HIGH | +1.098 | `WEEKEND_TARGET` |
| MPC | claude-opus-5-2026-07-27 | 309.24 | 2026-08-24 | +6.00% | +17.23% | +3.32% | +13.91% | HIT | OUT_CI_HIGH | +1.158 | `ORDINARY` |
| MPC | gpt-5-2026-07-27 | 309.24 | 2026-08-24 | +6.00% | +17.23% | +3.32% | +13.91% | HIT | OUT_CI_HIGH | +1.158 | `ORDINARY` |
| MPC | claude-opus-5-2026-07-28 | 312.35 | 2026-08-25 | +6.00% | +13.62% | +3.63% | +9.99% | HIT | IN_CI | +0.805 | `ORDINARY` |
| MPC | gpt-5-2026-07-28 | 312.35 | 2026-08-25 | +6.00% | +13.62% | +3.63% | +9.99% | HIT | IN_CI | +0.805 | `ORDINARY` |
| MRSH | claude-opus-5-2026-07-29 | 192.19 | 2026-08-26 | +6.00% | +0.56% | +3.40% | -2.85% | MISS | IN_CI | -0.568 | `ORDINARY` |
| MRSH | gpt-5-2026-07-29 | 192.19 | 2026-08-26 | +6.00% | +0.56% | +3.40% | -2.85% | MISS | IN_CI | -0.578 | `ORDINARY` |
| MRSH | claude-opus-5-2026-07-30 | 197.59 | 2026-08-27 | +6.00% | -3.84% | +5.71% | -9.55% | MISS | IN_CI | -1.022 | `TARGET_DATE_CLOSE` |
| MRSH | gpt-5-2026-07-30 | 191.51 | 2026-08-27 | +6.00% | -0.79% | +3.97% | -4.75% | MISS | IN_CI | -0.683 | `TARGET_DATE_CLOSE` |
| NSC | claude-opus-5-2026-07-26 | 350.66 | 2026-08-23 | +6.00% | +0.02% | +3.63% | -3.61% | MISS | IN_CI | -0.848 | `WEEKEND_TARGET` |
| NSC | claude-opus-5-2026-07-27 | 350.66 | 2026-08-24 | +6.00% | +0.66% | +3.32% | -2.66% | MISS | IN_CI | -0.757 | `ORDINARY` |
| NSC | gpt-5-2026-07-27 | 350.66 | 2026-08-24 | +6.00% | +0.66% | +3.32% | -2.66% | MISS | IN_CI | -0.757 | `ORDINARY` |
| NSC | claude-opus-5-2026-07-28 | 343.35 | 2026-08-25 | +6.00% | +2.30% | +3.63% | -1.33% | MISS | IN_CI | -0.511 | `ORDINARY` |
| NSC | gpt-5-2026-07-28 | 343.35 | 2026-08-25 | +6.00% | +2.30% | +3.63% | -1.33% | MISS | IN_CI | -0.511 | `ORDINARY` |
| NTAP | claude-opus-5-2026-07-30 | 173.23 | 2026-08-27 | +6.00% | +10.05% | +5.71% | +4.34% | HIT | IN_CI | +0.316 | `TARGET_DATE_CLOSE` |
| OMC | claude-opus-5-2026-07-29 | 86.22 | 2026-08-26 | +6.00% | +1.94% | +3.40% | -1.47% | MISS | IN_CI | -0.348 | `ORDINARY` |
| PAYX | claude-opus-5-2026-07-26 | 113.55 | 2026-08-23 | +6.00% | +9.62% | +3.63% | +6.00% | HIT | IN_CI | +0.383 | `WEEKEND_TARGET` |
| PAYX | claude-opus-5-2026-07-27 | 113.55 | 2026-08-24 | +6.00% | +10.97% | +3.32% | +7.65% | HIT | IN_CI | +0.526 | `ORDINARY` |
| PAYX | gpt-5-2026-07-27 | 113.55 | 2026-08-24 | +6.00% | +10.97% | +3.32% | +7.65% | HIT | IN_CI | +0.526 | `ORDINARY` |
| PAYX | claude-opus-5-2026-07-28 | 115.48 | 2026-08-25 | +6.00% | +8.24% | +3.63% | +4.61% | HIT | IN_CI | +0.244 | `ORDINARY` |
| PAYX | gpt-5-2026-07-28 | 115.48 | 2026-08-25 | +6.00% | +8.24% | +3.63% | +4.61% | HIT | IN_CI | +0.244 | `ORDINARY` |
| PAYX | claude-opus-5-2026-07-29 | 118.87 | 2026-08-26 | +6.00% | +5.06% | +3.40% | +1.65% | HIT | IN_CI | -0.097 | `ORDINARY` |
| PAYX | gpt-5-2026-07-29 | 118.87 | 2026-08-26 | +6.00% | +5.06% | +3.40% | +1.65% | HIT | IN_CI | -0.099 | `ORDINARY` |
| PAYX | claude-opus-5-2026-07-30 | 122.13 | 2026-08-27 | +6.00% | +3.56% | +5.71% | -2.15% | MISS | IN_CI | -0.247 | `TARGET_DATE_CLOSE` |
| PAYX | gpt-5-2026-07-30 | 116.33 | 2026-08-27 | +6.00% | +8.73% | +3.97% | +4.76% | HIT | IN_CI | +0.256 | `TARGET_DATE_CLOSE` |
| PCG | claude-opus-5-2026-07-26 | 17.85 | 2026-08-23 | +6.00% | -1.40% | +3.63% | -5.03% | MISS | IN_CI | -1.039 | `WEEKEND_TARGET` |
| PCG | claude-opus-5-2026-07-27 | 17.85 | 2026-08-24 | +6.00% | +1.46% | +3.32% | -1.86% | MISS | IN_CI | -0.638 | `ORDINARY` |
| PCG | gpt-5-2026-07-27 | 17.85 | 2026-08-24 | +6.00% | +1.46% | +3.32% | -1.86% | MISS | IN_CI | -0.638 | `ORDINARY` |
| PCG | gpt-5-2026-07-30 | 17.78 | 2026-08-27 | +6.00% | +0.96% | +3.97% | -3.01% | MISS | IN_CI | -0.737 | `TARGET_DATE_CLOSE` |
| PFG | claude-opus-5-2026-07-28 | 111.29 | 2026-08-25 | +6.00% | +0.27% | +3.63% | -3.36% | MISS | IN_CI | -0.823 | `ORDINARY` |
| PFG | claude-opus-5-2026-07-29 | 114.09 | 2026-08-26 | +6.00% | -1.65% | +3.40% | -5.05% | MISS | OUT_CI_LOW | -1.046 | `ORDINARY` |
| PKG | claude-opus-5-2026-07-26 | 254.39 | 2026-08-23 | +6.00% | -0.63% | +3.63% | -4.25% | MISS | IN_CI | -0.664 | `WEEKEND_TARGET` |
| PKG | claude-opus-5-2026-07-27 | 254.39 | 2026-08-24 | +6.00% | -2.17% | +3.32% | -5.49% | MISS | IN_CI | -0.818 | `ORDINARY` |
| PKG | gpt-5-2026-07-27 | 254.39 | 2026-08-24 | +6.00% | -2.17% | +3.32% | -5.49% | MISS | IN_CI | -0.818 | `ORDINARY` |
| PKG | claude-opus-5-2026-07-28 | 252.37 | 2026-08-25 | +5.00% | -2.31% | +3.63% | -5.94% | MISS | IN_CI | -0.766 | `ORDINARY` |
| PM | claude-opus-5-2026-07-26 | 193.00 | 2026-08-23 | +6.00% | -2.47% | +3.63% | -6.10% | MISS | IN_CI | -0.897 | `WEEKEND_TARGET` |
| PM | claude-opus-5-2026-07-27 | 193.00 | 2026-08-24 | +6.00% | -0.80% | +3.32% | -4.12% | MISS | IN_CI | -0.720 | `ORDINARY` |
| PM | gpt-5-2026-07-27 | 193.00 | 2026-08-24 | +6.00% | -0.80% | +3.32% | -4.12% | MISS | IN_CI | -0.720 | `ORDINARY` |
| PM | claude-opus-5-2026-07-28 | 195.66 | 2026-08-25 | +6.00% | -0.89% | +3.63% | -4.52% | MISS | IN_CI | -0.744 | `ORDINARY` |
| PM | gpt-5-2026-07-28 | 195.66 | 2026-08-25 | +6.00% | -0.89% | +3.63% | -4.52% | MISS | IN_CI | -0.744 | `ORDINARY` |
| PM | claude-opus-5-2026-07-29 | 200.17 | 2026-08-26 | +6.00% | -3.03% | +3.40% | -6.44% | MISS | IN_CI | -0.955 | `ORDINARY` |
| PM | gpt-5-2026-07-29 | 200.17 | 2026-08-26 | +6.00% | -3.03% | +3.40% | -6.44% | MISS | IN_CI | -0.971 | `ORDINARY` |
| PM | gpt-5-2026-07-30 | 192.00 | 2026-08-27 | +6.00% | -0.79% | +3.97% | -4.76% | MISS | IN_CI | -0.702 | `TARGET_DATE_CLOSE` |
| PRU | claude-opus-5-2026-07-28 | 121.89 | 2026-08-25 | +6.00% | -1.43% | +3.63% | -5.06% | MISS | OUT_CI_LOW | -1.205 | `ORDINARY` |
| PRU | gpt-5-2026-07-28 | 121.89 | 2026-08-25 | +6.00% | -1.43% | +3.63% | -5.06% | MISS | OUT_CI_LOW | -1.205 | `ORDINARY` |
| PSX | claude-opus-5-2026-07-27 | 206.77 | 2026-08-24 | +5.00% | +17.02% | +3.32% | +13.70% | HIT | OUT_CI_HIGH | +1.210 | `ORDINARY` |
| RJF | gpt-5-2026-07-29 | 177.18 | 2026-08-26 | +6.00% | -0.28% | +3.40% | -3.68% | MISS | IN_CI | -0.858 | `ORDINARY` |
| RTX | claude-opus-5-2026-07-26 | 212.79 | 2026-08-23 | +6.00% | -1.35% | +3.63% | -4.98% | MISS | IN_CI | -0.754 | `WEEKEND_TARGET` |
| RTX | claude-opus-5-2026-07-27 | 212.79 | 2026-08-24 | +6.00% | -1.68% | +3.32% | -5.00% | MISS | IN_CI | -0.787 | `ORDINARY` |
| RTX | gpt-5-2026-07-27 | 212.79 | 2026-08-24 | +6.00% | -1.68% | +3.32% | -5.00% | MISS | IN_CI | -0.787 | `ORDINARY` |
| RTX | claude-opus-5-2026-07-28 | 218.42 | 2026-08-25 | +6.00% | -3.73% | +3.63% | -7.36% | MISS | IN_CI | -1.039 | `ORDINARY` |
| RTX | gpt-5-2026-07-28 | 218.42 | 2026-08-25 | +6.00% | -3.73% | +3.63% | -7.36% | MISS | IN_CI | -1.039 | `ORDINARY` |
| RTX | claude-opus-5-2026-07-29 | 218.58 | 2026-08-26 | +6.00% | -3.01% | +3.40% | -6.42% | MISS | IN_CI | -0.950 | `ORDINARY` |
| RTX | gpt-5-2026-07-29 | 218.58 | 2026-08-26 | +6.00% | -3.01% | +3.40% | -6.42% | MISS | IN_CI | -0.966 | `ORDINARY` |
| RTX | claude-opus-5-2026-07-30 | 215.25 | 2026-08-27 | +6.00% | -1.47% | +5.71% | -7.18% | MISS | IN_CI | -0.774 | `TARGET_DATE_CLOSE` |
| RTX | gpt-5-2026-07-30 | 214.38 | 2026-08-27 | +6.00% | -1.07% | +3.97% | -5.04% | MISS | IN_CI | -0.747 | `TARGET_DATE_CLOSE` |
| SCHW | claude-opus-5-2026-07-29 | 105.97 | 2026-08-26 | +6.00% | +3.23% | +3.40% | -0.18% | MISS | IN_CI | -0.360 | `ORDINARY` |
| SCHW | gpt-5-2026-07-29 | 105.97 | 2026-08-26 | +6.00% | +3.23% | +3.40% | -0.18% | MISS | IN_CI | -0.366 | `ORDINARY` |
| SJM | claude-opus-5-2026-07-26 | 118.32 | 2026-08-23 | +6.00% | +5.07% | +3.63% | +1.45% | HIT | IN_CI | -0.098 | `WEEKEND_TARGET` |
| SJM | claude-opus-5-2026-07-27 | 118.32 | 2026-08-24 | +6.00% | +6.38% | +3.32% | +3.06% | HIT | IN_CI | +0.040 | `ORDINARY` |
| SJM | gpt-5-2026-07-27 | 118.32 | 2026-08-24 | +6.00% | +6.38% | +3.32% | +3.06% | HIT | IN_CI | +0.040 | `ORDINARY` |
| SJM | claude-opus-5-2026-07-28 | 121.05 | 2026-08-25 | +6.00% | +3.63% | +3.63% | +0.01% | HIT | IN_CI | -0.249 | `ORDINARY` |
| SJM | gpt-5-2026-07-28 | 121.05 | 2026-08-25 | +6.00% | +3.63% | +3.63% | +0.01% | HIT | IN_CI | -0.249 | `ORDINARY` |
| SJM | claude-opus-5-2026-07-29 | 123.04 | 2026-08-26 | +6.00% | +6.39% | +3.40% | +2.98% | HIT | IN_CI | +0.040 | `ORDINARY` |
| SJM | gpt-5-2026-07-29 | 123.04 | 2026-08-26 | +6.00% | +6.39% | +3.40% | +2.98% | HIT | IN_CI | +0.041 | `ORDINARY` |
| SJM | claude-opus-5-2026-07-30 | 126.35 | 2026-08-27 | +6.00% | +4.35% | +5.71% | -1.36% | MISS | IN_CI | -0.167 | `TARGET_DATE_CLOSE` |
| SJM | gpt-5-2026-07-30 | 122.21 | 2026-08-27 | +6.00% | +7.88% | +3.97% | +3.91% | HIT | IN_CI | +0.184 | `TARGET_DATE_CLOSE` |
| SYK | gpt-5-2026-07-30 | 348.04 | 2026-08-27 | +6.00% | -7.45% | +3.97% | -11.41% | MISS | OUT_CI_LOW | -1.127 | `TARGET_DATE_CLOSE` |
| TMO | claude-opus-5-2026-07-26 | 568.26 | 2026-08-23 | +6.00% | +10.74% | +3.63% | +7.11% | HIT | IN_CI | +0.463 | `WEEKEND_TARGET` |
| TMO | claude-opus-5-2026-07-27 | 568.26 | 2026-08-24 | +6.00% | +10.64% | +3.32% | +7.32% | HIT | IN_CI | +0.454 | `ORDINARY` |
| TMO | gpt-5-2026-07-27 | 568.26 | 2026-08-24 | +6.00% | +10.64% | +3.32% | +7.32% | HIT | IN_CI | +0.454 | `ORDINARY` |
| TMO | claude-opus-5-2026-07-29 | 576.41 | 2026-08-26 | +6.00% | +9.94% | +3.40% | +6.54% | HIT | IN_CI | +0.382 | `ORDINARY` |
| TRV | claude-opus-5-2026-07-26 | 387.26 | 2026-08-23 | +6.00% | -6.11% | +3.63% | -9.74% | MISS | OUT_CI_LOW | -1.299 | `WEEKEND_TARGET` |
| TRV | claude-opus-5-2026-07-27 | 387.26 | 2026-08-24 | +6.00% | -4.31% | +3.32% | -7.64% | MISS | OUT_CI_LOW | -1.106 | `ORDINARY` |
| TRV | gpt-5-2026-07-27 | 387.26 | 2026-08-24 | +6.00% | -4.31% | +3.32% | -7.64% | MISS | OUT_CI_LOW | -1.106 | `ORDINARY` |
| TRV | claude-opus-5-2026-07-28 | 390.35 | 2026-08-25 | +6.00% | -5.30% | +3.63% | -8.93% | MISS | OUT_CI_LOW | -1.235 | `ORDINARY` |
| TRV | gpt-5-2026-07-28 | 390.35 | 2026-08-25 | +6.00% | -5.30% | +3.63% | -8.93% | MISS | OUT_CI_LOW | -1.235 | `ORDINARY` |
| TRV | claude-opus-5-2026-07-29 | 397.22 | 2026-08-26 | +6.00% | -6.56% | +3.40% | -9.97% | MISS | OUT_CI_LOW | -1.348 | `ORDINARY` |
| TRV | gpt-5-2026-07-29 | 397.22 | 2026-08-26 | +6.00% | -6.56% | +3.40% | -9.97% | MISS | OUT_CI_LOW | -1.371 | `ORDINARY` |
| TRV | claude-opus-5-2026-07-30 | 389.01 | 2026-08-27 | +6.00% | -5.06% | +5.71% | -10.77% | MISS | OUT_CI_LOW | -1.146 | `TARGET_DATE_CLOSE` |
| TRV | gpt-5-2026-07-30 | 375.99 | 2026-08-27 | +6.00% | -1.77% | +3.97% | -5.74% | MISS | IN_CI | -0.771 | `TARGET_DATE_CLOSE` |
| UNP | claude-opus-5-2026-07-26 | 307.32 | 2026-08-23 | +6.00% | +0.24% | +3.63% | -3.39% | MISS | IN_CI | -0.788 | `WEEKEND_TARGET` |
| UNP | claude-opus-5-2026-07-27 | 307.32 | 2026-08-24 | +6.00% | +0.83% | +3.32% | -2.49% | MISS | IN_CI | -0.707 | `ORDINARY` |
| UNP | gpt-5-2026-07-27 | 307.32 | 2026-08-24 | +6.00% | +0.83% | +3.32% | -2.49% | MISS | IN_CI | -0.707 | `ORDINARY` |
| UNP | claude-opus-5-2026-07-28 | 299.30 | 2026-08-25 | +6.00% | +3.44% | +3.63% | -0.19% | MISS | IN_CI | -0.336 | `ORDINARY` |
| UNP | gpt-5-2026-07-28 | 299.30 | 2026-08-25 | +6.00% | +3.44% | +3.63% | -0.19% | MISS | IN_CI | -0.336 | `ORDINARY` |
| UNP | claude-opus-5-2026-07-29 | 294.45 | 2026-08-26 | +6.00% | +5.49% | +3.40% | +2.09% | HIT | IN_CI | -0.065 | `ORDINARY` |
| UNP | gpt-5-2026-07-29 | 294.45 | 2026-08-26 | +6.00% | +5.49% | +3.40% | +2.09% | HIT | IN_CI | -0.066 | `ORDINARY` |
| VLO | claude-opus-5-2026-07-26 | 302.50 | 2026-08-23 | +5.00% | +15.33% | +3.63% | +11.70% | HIT | IN_CI | +0.877 | `WEEKEND_TARGET` |
| VLO | claude-opus-5-2026-07-27 | 302.50 | 2026-08-24 | +6.00% | +14.38% | +3.32% | +11.06% | HIT | IN_CI | +0.711 | `ORDINARY` |
| VLO | gpt-5-2026-07-27 | 302.50 | 2026-08-24 | +5.00% | +14.38% | +3.32% | +11.06% | HIT | IN_CI | +0.796 | `ORDINARY` |
| VLTO | claude-opus-5-2026-07-29 | 98.47 | 2026-08-26 | +6.00% | +0.22% | +3.40% | -3.18% | MISS | IN_CI | -0.744 | `ORDINARY` |
| VLTO | gpt-5-2026-07-29 | 98.47 | 2026-08-26 | +6.00% | +0.22% | +3.40% | -3.18% | MISS | IN_CI | -0.756 | `ORDINARY` |
| VRSK | claude-opus-5-2026-07-30 | 213.15 | 2026-08-27 | +6.00% | -10.38% | +5.71% | -16.09% | MISS | OUT_CI_LOW | -1.546 | `TARGET_DATE_CLOSE` |
| WAB | claude-opus-5-2026-07-26 | 302.50 | 2026-08-23 | +6.00% | -1.63% | +3.63% | -5.26% | MISS | IN_CI | -0.687 | `WEEKEND_TARGET` |
| WAB | claude-opus-5-2026-07-27 | 302.50 | 2026-08-24 | +6.00% | -1.61% | +3.32% | -4.93% | MISS | IN_CI | -0.686 | `ORDINARY` |
| WAB | gpt-5-2026-07-27 | 302.50 | 2026-08-24 | +6.00% | -1.61% | +3.32% | -4.93% | MISS | IN_CI | -0.686 | `ORDINARY` |
| WELL | claude-opus-5-2026-07-27 | 252.07 | 2026-08-24 | +6.00% | -4.78% | +3.32% | -8.11% | MISS | OUT_CI_LOW | -1.580 | `ORDINARY` |
| WELL | claude-opus-5-2026-07-28 | 248.34 | 2026-08-25 | +6.00% | -2.90% | +3.63% | -6.52% | MISS | OUT_CI_LOW | -1.292 | `ORDINARY` |
| WELL | gpt-5-2026-07-28 | 248.34 | 2026-08-25 | +6.00% | -2.90% | +3.63% | -6.52% | MISS | OUT_CI_LOW | -1.292 | `ORDINARY` |
| WELL | claude-opus-5-2026-07-29 | 243.57 | 2026-08-26 | +6.00% | -0.83% | +3.40% | -4.23% | MISS | IN_CI | -0.944 | `ORDINARY` |
| WELL | gpt-5-2026-07-29 | 243.57 | 2026-08-26 | +6.00% | -0.83% | +3.40% | -4.23% | MISS | IN_CI | -0.960 | `ORDINARY` |
| WRB | claude-opus-5-2026-07-26 | 75.46 | 2026-08-23 | +6.00% | -9.09% | +3.63% | -12.72% | MISS | OUT_CI_LOW | -2.076 | `WEEKEND_TARGET` |
| WRB | gpt-5-2026-07-27 | 75.46 | 2026-08-24 | +6.00% | -7.63% | +3.32% | -10.95% | MISS | OUT_CI_LOW | -1.875 | `ORDINARY` |
| WTW | gpt-5-2026-07-29 | 316.16 | 2026-08-26 | +6.00% | +8.53% | +3.40% | +5.12% | HIT | IN_CI | +0.275 | `ORDINARY` |
| WTW | gpt-5-2026-07-30 | 336.05 | 2026-08-27 | +6.00% | +1.05% | +3.97% | -2.91% | MISS | IN_CI | -0.490 | `TARGET_DATE_CLOSE` |
| QQQ | claude-opus-5-2026-07-26 | 684.23 | 2026-08-23 | -0.64% | +4.27% | N/A | N/A | MISS | IN_CI | +0.617 | `WEEKEND_TARGET` |
| QQQ | claude-opus-5-2026-07-27 | 684.23 | 2026-08-24 | +0.86% | +3.23% | N/A | N/A | HIT | IN_CI | +0.298 | `ORDINARY` |
| QQQ | gpt-5-2026-07-27 | 684.23 | 2026-08-24 | -0.64% | +3.23% | N/A | N/A | MISS | IN_CI | +0.486 | `ORDINARY` |
| QQQ | claude-opus-5-2026-07-28 | 682.12 | 2026-08-25 | +0.86% | +4.19% | N/A | N/A | HIT | IN_CI | +0.459 | `ORDINARY` |
| QQQ | gpt-5-2026-07-28 | 682.12 | 2026-08-25 | -0.64% | +4.19% | N/A | N/A | MISS | IN_CI | +0.665 | `ORDINARY` |
| QQQ | claude-opus-5-2026-07-29 | 675.49 | 2026-08-26 | +0.87% | +5.31% | N/A | N/A | HIT | IN_CI | +0.601 | `ORDINARY` |
| QQQ | gpt-5-2026-07-29 | 675.49 | 2026-08-26 | -0.63% | +5.31% | N/A | N/A | MISS | IN_CI | +0.818 | `ORDINARY` |
| QQQ | claude-opus-5-2026-07-30 | 661.73 | 2026-08-27 | +0.85% | +8.97% | N/A | N/A | HIT | OUT_CI_HIGH | +1.168 | `TARGET_DATE_CLOSE` |
| QQQ | gpt-5-2026-07-30 | 683.55 | 2026-08-27 | -0.64% | +5.49% | N/A | N/A | MISS | IN_CI | +0.835 | `TARGET_DATE_CLOSE` |
| SOXX | claude-opus-5-2026-07-26 | 527.01 | 2026-08-23 | +0.32% | -1.32% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.081 | `WEEKEND_TARGET` |
| SOXX | claude-opus-5-2026-07-27 | 527.01 | 2026-08-24 | +1.82% | -3.95% | N/A | N/A | MISS | IN_CI | -0.286 | `ORDINARY` |
| SOXX | gpt-5-2026-07-27 | 527.01 | 2026-08-24 | +0.32% | -3.95% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.212 | `ORDINARY` |
| SOXX | claude-opus-5-2026-07-28 | 516.23 | 2026-08-25 | +1.82% | -0.42% | N/A | N/A | MISS | IN_CI | -0.121 | `ORDINARY` |
| SOXX | gpt-5-2026-07-28 | 516.23 | 2026-08-25 | +0.32% | -0.42% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.040 | `ORDINARY` |
| SOXX | claude-opus-5-2026-07-29 | 491.46 | 2026-08-26 | +1.82% | +4.87% | N/A | N/A | HIT | IN_CI | +0.159 | `ORDINARY` |
| SOXX | gpt-5-2026-07-29 | 491.46 | 2026-08-26 | +0.32% | +4.87% | N/A | N/A | N/A - FLAT_CALL | IN_CI | +0.241 | `ORDINARY` |
| SOXX | claude-opus-5-2026-07-30 | 465.00 | 2026-08-27 | +1.82% | +13.00% | N/A | N/A | HIT | IN_CI | +0.593 | `TARGET_DATE_CLOSE` |
| SOXX | gpt-5-2026-07-30 | 504.53 | 2026-08-27 | +1.87% | +4.14% | N/A | N/A | HIT | IN_CI | +0.116 | `TARGET_DATE_CLOSE` |
| SPY | claude-opus-5-2026-07-26 | 738.93 | 2026-08-23 | +0.50% | +3.63% | N/A | N/A | HIT | IN_CI | +0.790 | `WEEKEND_TARGET` |
| SPY | claude-opus-5-2026-07-27 | 738.93 | 2026-08-24 | +0.50% | +3.32% | N/A | N/A | HIT | IN_CI | +0.713 | `ORDINARY` |
| SPY | gpt-5-2026-07-27 | 738.93 | 2026-08-24 | +0.50% | +3.32% | N/A | N/A | HIT | IN_CI | +0.713 | `ORDINARY` |
| SPY | claude-opus-5-2026-07-28 | 739.09 | 2026-08-25 | +0.50% | +3.63% | N/A | N/A | HIT | IN_CI | +0.860 | `ORDINARY` |
| SPY | gpt-5-2026-07-28 | 739.09 | 2026-08-25 | +0.50% | +3.63% | N/A | N/A | HIT | IN_CI | +0.860 | `ORDINARY` |
| SPY | claude-opus-5-2026-07-29 | 740.86 | 2026-08-26 | +0.50% | +3.40% | N/A | N/A | HIT | IN_CI | +0.790 | `ORDINARY` |
| SPY | gpt-5-2026-07-29 | 740.86 | 2026-08-26 | +0.50% | +3.40% | N/A | N/A | HIT | IN_CI | +0.803 | `ORDINARY` |
| SPY | claude-opus-5-2026-07-30 | 729.46 | 2026-08-27 | +0.50% | +5.71% | N/A | N/A | HIT | OUT_CI_HIGH | +1.458 | `TARGET_DATE_CLOSE` |
| SPY | gpt-5-2026-07-30 | 741.69 | 2026-08-27 | +0.50% | +3.97% | N/A | N/A | HIT | IN_CI | +0.918 | `TARGET_DATE_CLOSE` |

## 1. Prior Run Summary

### MoM baseline selection and mandatory tie disclosure

Window 2026-07-13 … 2026-08-06, target 2026-07-30. Two folders sit at
`|folder_date - target| = 0d`, so `agents.md § Orchestrator Step 2` rule 8 applies. Both carry a usable
`15_predictions.json`, so the tie resolves on rule 8(a) — same model family as the executing model.

**Selected baseline: `claude-opus-5-2026-07-30`.** Baseline flag: `NONE (same-model folder at delta 0d)`.

| Tied candidate | Delta | Settled n | Hit rate | Mean alpha | Mean z | CI coverage | Selected |
|---|---|---|---|---|---|---|---|
| `claude-opus-5-2026-07-30` | 0d | 24 | 16.67% | -7.20% | -0.8667 | 66.67% | **yes** (rule 8a) |
| `gpt-5-2026-07-30` | 0d | 20 | 20.00% | -3.77% | -0.5917 | 80.00% | no |

**The MoM conclusion is invariant across the tied books.** The hit-rate spread is
**3.3pp** (16.67% vs 20.00%) and both books are deeply
negative on mean alpha (-7.20% and -3.77%) — either baseline
supports the same finding. That is a materially different situation from 2026-07-29 (48pp spread) and
2026-07-30 (40.7pp), where the choice of baseline would have changed the narrative; it is closer to
2026-08-01's 1.7pp tie. Both books' settlements were computed **this run**
(24 and 20 rows respectively), so the per-book statistics above
merge this run's computed rows into the canonical pool rather than reporting the empty pre-run state
(the 2026-08-01 gotcha).

### Baseline package

`claude-opus-5-2026-07-30` published **NO_TRADE** on an intraday fire (~10:06 ET) with a
24-name monitoring sleeve and 0 investable names. Its five highest `Adj Score`
names were `GRMN` (+0.3309), `BBY` (+0.3256), `IQV` (+0.3169), `NTAP` (+0.3116), `BXP` (+0.2946).

## 2. MoM Price & Return Table

Prior price = the baseline package's own recorded `entry_price` (its `price_date` is shown); current
price = the 2026-08-27 raw close from L002, cross-verified per L011/L012 for the names still in today's
published set. Hit/Miss is **alpha-based** per `rules.md § Settlement Rules`.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| FTNT | 2026-07-29 | 153.22 | 2026-08-27 | 172.78 | +12.77% | +5.71% | +7.06% | Hit | `IN_CI`; settled `HIT` this run |
| NTAP | 2026-07-29 | 173.23 | 2026-08-27 | 190.64 | +10.05% | +5.71% | +4.34% | Hit | `IN_CI`; settled `HIT` this run |
| HUM | 2026-07-29 | 365.41 | 2026-08-27 | 392.63 | +7.45% | +5.71% | +1.74% | Hit | `IN_CI`; settled `HIT` this run |
| IQV | 2026-07-29 | 247.56 | 2026-08-27 | 262.38 | +5.99% | +5.71% | +0.28% | Hit | `IN_CI`; settled `HIT` this run |
| SJM | 2026-07-29 | 126.35 | 2026-08-27 | 131.84 | +4.35% | +5.71% | -1.36% | Miss | `IN_CI`; settled `MISS` this run |
| HPQ | 2026-07-29 | 28.41 | 2026-08-27 | 29.63 | +4.29% | +5.71% | -1.41% | Miss | `IN_CI`; settled `MISS` this run |
| ADP | 2026-07-29 | 273.37 | 2026-08-27 | 284.68 | +4.14% | +5.71% | -1.57% | Miss | `IN_CI`; settled `MISS` this run |
| PAYX | 2026-07-29 | 122.13 | 2026-08-27 | 126.48 | +3.56% | +5.71% | -2.15% | Miss | `IN_CI`; settled `MISS` this run |
| CPAY | 2026-07-29 | 392.85 | 2026-08-27 | 403.67 | +2.75% | +5.71% | -2.95% | Miss | `IN_CI`; settled `MISS` this run |
| IEX | 2026-07-29 | 229.52 | 2026-08-27 | 233.98 | +1.94% | +5.71% | -3.77% | Miss | `IN_CI`; settled `MISS` this run |
| GEHC | 2026-07-29 | 71.90 | 2026-08-27 | 72.48 | +0.81% | +5.71% | -4.90% | Miss | `IN_CI`; settled `MISS` this run |
| INCY | 2026-07-29 | 127.10 | 2026-08-27 | 127.74 | +0.50% | +5.71% | -5.20% | Miss | `IN_CI`; settled `MISS` this run |
| RTX | 2026-07-29 | 215.25 | 2026-08-27 | 212.08 | -1.47% | +5.71% | -7.18% | Miss | `IN_CI`; settled `MISS` this run |
| GRMN | 2026-07-29 | 294.83 | 2026-08-27 | 289.87 | -1.68% | +5.71% | -7.39% | Miss | `IN_CI`; settled `MISS` this run |
| MRSH | 2026-07-29 | 197.59 | 2026-08-27 | 190.00 | -3.84% | +5.71% | -9.55% | Miss | `IN_CI`; settled `MISS` this run |
| BXP | 2026-07-29 | 72.97 | 2026-08-27 | 69.97 | -4.11% | +5.71% | -9.82% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| BRO | 2026-07-29 | 74.87 | 2026-08-27 | 71.39 | -4.65% | +5.71% | -10.36% | Miss | `IN_CI`; settled `MISS` this run |
| TRV | 2026-07-29 | 389.01 | 2026-08-27 | 369.33 | -5.06% | +5.71% | -10.77% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| CTAS | 2026-07-29 | 216.53 | 2026-08-27 | 204.15 | -5.72% | +5.71% | -11.43% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| BBY | 2026-07-29 | 90.17 | 2026-08-27 | 83.56 | -7.33% | +5.71% | -13.04% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| F | 2026-07-29 | 15.28 | 2026-08-27 | 13.95 | -8.70% | +5.71% | -14.41% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| VRSK | 2026-07-29 | 213.15 | 2026-08-27 | 191.02 | -10.38% | +5.71% | -16.09% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| FICO | 2026-07-29 | 1373.08 | 2026-08-27 | 1157.06 | -15.73% | +5.71% | -21.44% | Miss | `OUT_CI_LOW`; settled `MISS` this run |
| DVA | 2026-07-29 | 240.96 | 2026-08-27 | 178.88 | -25.76% | +5.71% | -31.47% | Miss | `OUT_CI_LOW`; settled `MISS` this run |

Scored rows: **24**. MoM hit rate **16.67%**, mean alpha
**-7.20%**. No row is `UNAVAILABLE` — every baseline name still trades and
has a 2026-08-27 close.

## 3. Theme-Level Performance

The baseline book had one dominant theme and it failed.

| Theme (baseline) | Names | Outcome | Evidence |
|---|---|---|---|
| Defensive sectors (Health Care + Consumer Staples, by today's screener taxonomy) | 6 of 24 | **failed** | mean alpha across the whole book -7.20% over the 28-day window; only 4 of 24 names produced positive alpha |
| Best three names by realized alpha | `FTNT` (+7.06%), `NTAP` (+4.34%), `HUM` (+1.74%) | partial | positive alpha, but not enough of the book to change the aggregate |
| Worst three names by realized alpha | `DVA` (-31.47%), `FICO` (-21.44%), `VRSK` (-16.09%) | **failed** | the tail that drove the mean; their ranks in the baseline book's own `Adj Score` order were `DVA` #23, `FICO` #9, `VRSK` #24 of 24 |

The failure mode is the one this system has now documented repeatedly: with `Fund_Z` and `Sent_Z`
`UNAVAILABLE`, `Tech_Z` carries 66.7% of live conviction and is pure trend-persistence, so the
leaderboard mechanically ranks the trailing 60-day winners first. Through a rotation that is
anti-correlated with forward alpha, which is what the negative aggregate rank IC
(-0.0840 over 60 vintages) measures. This is a **structural** diagnosis, not a
one-window result.

## 4. Regime Shift Assessment

| Dimension | Baseline (2026-07-30) | Today (2026-08-27) | Implication |
|---|---|---|---|
| Declared regime | see baseline `03` | **BULL** | SPY 771.10 above both MA20 (768.10) and MA50 (753.35); 60d momentum +1.78%; VIX 14.51 (L007) |
| Benchmark path over the window | SPY at the baseline's entry basis | SPY 2026-08-27 close 771.10 | the baseline book's mean SPY return over its own 28d window was +5.71% — a rising tape the defensive book did not participate in |
| Semiconductor leadership | not recomputed at the baseline vintage | SOXX RS vs SPY +0.17% (20d) / -14.89% (60d) | the high-beta complex is where the tape's return has been; the score's defensive tilt is the mirror image |
| Cross-sectional beta | not recomputed at the baseline vintage | 42.83% of the 509 scored names carry a negative 60d beta; median beta +0.1966 | this is what makes the 0.90 portfolio-beta floor unreachable from a top-ranked sleeve (see `07`/L016) |

Factor-weight implication: none may be applied here. Changing family weights is a **Track A** change
under `rules.md § Evolution Policy` and requires `eff_n >= 3`; at `eff_n = 2` the
correct action is to record the finding and defer, which `13` does.

## 5. Carry-Forward Decisions

Decisions are computed from today's percentile of each baseline name in the same
`INDEX_UNION_PCTL (n=509)` cross-section: `CARRY` at or above the 80th percentile,
`DOWNGRADE` in the 60–80 monitoring band, `DROP` below the 60th-percentile rank floor. They are
ledger-backed (L200–L523) and therefore **binding** on factor scoring.

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| FTNT | +0.2698 | Technology name at 97.1th pctl on the index-union leaderboar | +12.77% | **CARRY** | still 98.03 pctl (rank 11/509) — investable-band percentile |
| HUM | +0.2763 | Health Care name at 97.7th pctl on the index-union leaderboa | +7.45% | **CARRY** | still 94.69 pctl (rank 28/509) — investable-band percentile |
| INCY | +0.2897 | Health Care name at 98.6th pctl on the index-union leaderboa | +0.50% | **CARRY** | still 84.06 pctl (rank 82/509) — investable-band percentile |
| IQV | +0.3169 | Health Care name at 99.4th pctl on the index-union leaderboa | +5.99% | **CARRY** | still 91.93 pctl (rank 42/509) — investable-band percentile |
| SJM | +0.2665 | Consumer Staples name at 96.9th pctl on the index-union lead | +4.35% | **CARRY** | still 100.00 pctl (rank 1/509) — investable-band percentile |
| ADP | +0.2802 | Industrials name at 98.1th pctl on the index-union leaderboa | +4.14% | **DOWNGRADE** | fell to 70.28 pctl (rank 152/509) — monitoring band only |
| BXP | +0.2946 | Real Estate name at 99.0th pctl on the index-union leaderboa | -4.11% | **DOWNGRADE** | fell to 63.98 pctl (rank 184/509) — monitoring band only |
| CPAY | +0.2724 | Consumer Discretionary name at 97.5th pctl on the index-unio | +2.75% | **DOWNGRADE** | fell to 65.35 pctl (rank 177/509) — monitoring band only |
| CTAS | +0.2283 | Industrials name at 95.9th pctl on the index-union leaderboa | -5.72% | **DOWNGRADE** | fell to 61.02 pctl (rank 199/509) — monitoring band only |
| GEHC | +0.2831 | Health Care name at 98.4th pctl on the index-union leaderboa | +0.81% | **DOWNGRADE** | fell to 77.17 pctl (rank 117/509) — monitoring band only |
| HPQ | +0.2492 | Technology name at 96.3th pctl on the index-union leaderboar | +4.29% | **DOWNGRADE** | fell to 72.83 pctl (rank 139/509) — monitoring band only |
| IEX | +0.2231 | Industrials name at 95.7th pctl on the index-union leaderboa | +1.94% | **DOWNGRADE** | fell to 76.97 pctl (rank 118/509) — monitoring band only |
| MRSH | +0.2531 | Finance name at 96.7th pctl on the index-union leaderboard;  | -3.84% | **DOWNGRADE** | fell to 79.92 pctl (rank 103/509) — monitoring band only |
| PAYX | +0.2701 | Industrials name at 97.3th pctl on the index-union leaderboa | +3.56% | **DOWNGRADE** | fell to 73.62 pctl (rank 135/509) — monitoring band only |
| RTX | +0.2359 | Industrials name at 96.1th pctl on the index-union leaderboa | -1.47% | **DOWNGRADE** | fell to 63.58 pctl (rank 186/509) — monitoring band only |
| BBY | +0.3256 | Consumer Discretionary name at 99.6th pctl on the index-unio | -7.33% | **DROP** | fell below the 60th-pctl rank floor to 49.80 (rank 256/509) |
| BRO | +0.2513 | Finance name at 96.5th pctl on the index-union leaderboard;  | -4.65% | **DROP** | fell below the 60th-pctl rank floor to 54.13 (rank 234/509) |
| DVA | +0.2224 | Health Care name at 95.5th pctl on the index-union leaderboa | -25.76% | **DROP** | fell below the 60th-pctl rank floor to 10.63 (rank 455/509) |
| F | +0.2777 | Industrials name at 97.9th pctl on the index-union leaderboa | -8.70% | **DROP** | fell below the 60th-pctl rank floor to 23.03 (rank 392/509) |
| FICO | +0.2830 | Consumer Discretionary name at 98.2th pctl on the index-unio | -15.73% | **DROP** | fell below the 60th-pctl rank floor to 12.20 (rank 447/509) |
| GRMN | +0.3309 | Industrials name at 99.8th pctl on the index-union leaderboa | -1.68% | **DROP** | fell below the 60th-pctl rank floor to 45.28 (rank 279/509) |
| NTAP | +0.3116 | Technology name at 99.2th pctl on the index-union leaderboar | +10.05% | **DROP** | fell below the 60th-pctl rank floor to 52.56 (rank 242/509) |
| TRV | +0.2926 | Finance name at 98.8th pctl on the index-union leaderboard;  | -5.06% | **DROP** | fell below the 60th-pctl rank floor to 51.38 (rank 248/509) |
| VRSK | +0.2203 | Industrials name at 95.3th pctl on the index-union leaderboa | -10.38% | **DROP** | fell below the 60th-pctl rank floor to 20.08 (rank 407/509) |

Counts: **5 CARRY**, **10 DOWNGRADE**,
**9 DROP**, **0 PROMOTE**.
Of the baseline's 24 names, **2**
(`FTNT`, `SJM`) survive into today's published 24 —
turnover of 91.7% over 28 days from a
trend-persistence score, which is itself a signal-stability finding.

No `DROP` name is scored back into today's published set: today's set is produced by the same
mechanical ranking, and the 9 dropped names all sit below the
60th-percentile floor and are therefore not ranked in either sleeve.

## 6. Sign-Off

| Price used | Freshness tag | Ledger row |
|---|---|---|
| Baseline entry prices | `HISTORICAL` (the baseline package's own recorded basis) | baseline `15_predictions.json` |
| Current 2026-08-27 closes | `DELAYED` | L002, cross-verified L011 / L012 |
| SPY benchmark closes | `DELAYED` | L003, L011, L012 |
| Settlement closes (target-date) | `HISTORICAL` / `DELAYED` (same-day rows) | L002, L014d |

**Reflection confidence: HIGH.** Every settled row is priced from the target date's own completed
close in the same fetched tree used for scoring; 229 of 231 due keys
settled with 0 conflicts and 0 validator rejections; the two unsettled keys have a documented,
two-reference corporate-action cause.

**Structural issues found this run:**

1. A dead ticker still resolves to a *different, foreign* security at one of the three price vendors
   (`EQR` -> "EQ Resources Ltd", ASX, 0.41 — L026). The date gate alone accepts that row. This is the
   subject of this run's Track B proposal in `13`.
2. Mean z has drifted to -0.5553, just outside the healthy band. Corrective is Track A
   and gated by `eff_n`; `DEFER`red.
3. The portfolio beta band is infeasible for a second consecutive run (L016). Recomputed, not assumed
   — see `07`.
