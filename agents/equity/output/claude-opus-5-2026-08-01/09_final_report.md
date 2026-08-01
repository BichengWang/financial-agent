# 09 — Final Report — 2026-08-01

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-01
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

This Saturday run is computed entirely on the completed Friday 2026-07-31 close, grounded across
three independent vendors on 77 names with a maximum deviation of
0.0661%. All 107 due
predictions settled cleanly, taking the canonical ledger to `due_inventory: 0` and
`conflicts: 0`; the batch was poor (20/92 = 21.7% equity direction hits, mean z
-0.909).
Of 513 names scored against the full index union, **zero** clear the
evidence thresholds — `Fund_Z` and `Sent_Z` remain unavailable universe-wide, which fails
thresholds 2, 3 and 4 for every name regardless of market state. The portfolio beta band was
recomputed and is **feasible**, so this is explicitly not a geometry outcome. **Final status
is `NO_TRADE`**, with 24 names published as `MEDIUM`-confidence monitoring forecasts
and 3 core-ETF market forecasts so the run stays auditable and settleable.

## MoM reflection summary

Baseline `claude-fable-5-2026-07-04` (flag **`CROSS_MODEL_BASELINE`**), selected from a
**2-way tie** at |Δ| = 0d via `agents.md` rule 8
criterion (a), same model family. Both tied books are disclosed in `02 § 1` with their own
statistics; the hit-rate spread between them is only
1.7pp,
so the MoM conclusion **is invariant** across the tie this run — unlike 2026-07-29 (48pp) and
2026-07-30 (40.7pp). The baseline book returned 21.7% alpha hits over 28
days. No new facts are introduced here; see `02`.

## Regime

| Field | Value | Ledger |
|---|---|---|
| Regime | **`BULL`** | `L-HIST`, `L-MAC-VIX` |
| Evidence | SPY above MA50, 60d momentum +3.48%, VIX 15.99 (60d mean 17.4117) | `L-HIST`, `L-MAC-VIX60` |
| Data quality | 0.80 — two of four factor families unavailable | `L-UNA-FUND`, `L-UNA-SENT` |
| Key macro risk | Narrow leadership: QQQ and SOXX are **below** both MA20 and MA50 while SPY is above both; 153 of 515 universe names report inside 14 days (peak Q2 season) | `L-ETF-*`, earnings sweep |

## Core ETF market forecast

| ETF | Entry | Trend 20d/50d | Beta | mu | sigma | Target | 70% CI | Conf |
|---|---|---|---|---|---|---|---|---|
| SPY | 747.03 | ABOVE/ABOVE | +1.0000 | **+2.000%** | 3.67% | 761.97 | 733.42–790.52 | MEDIUM |
| QQQ | 687.99 | BELOW/BELOW | +1.7177 | **+1.935%** | 7.34% | 701.31 | 648.76–753.85 | MEDIUM |
| SOXX | 504.89 | BELOW/BELOW | +3.6683 | **+5.837%** | 19.53% | 534.36 | 431.82–636.90 | MEDIUM |

Summarised from `03`; no new facts. **These forecasts are published with a stated known
defect**: the `beta × SPY_mu` rule is a category error (diagnosed 2026-07-24), and with a
`BULL` prior it hands SOXX a formula mu of +7.34% —
larger than any equity mu the calibration table can issue — for an ETF trailing SPY by
-11.15pp over 20 days. The full permitted −1.5pp adjustment is
applied and remains inadequate. Canonical `MARKET_FORECAST` hit rate is 20.27%
over n=78. The fix is Track A and is blocked by `eff_n` = 1.

## Ranked candidates — monitoring sleeve only (top 10 of 24 published)

| Rank | Ticker | Sector | Entry | Adj Score | Pctl | Score Trace | Beta | mu | sigma | Target | 70% CI | Days to Earn | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DXCM** | Health Care | 83.45 | +0.4564 | 99.90 | `0.30*+1.578+0.15*+0.648 → *0.80−0.00` | +0.110 | +6.00% | 14.99% | 88.46 | 75.44–101.47 | none in 37d | MEDIUM |
| 2 | **NTAP** | Technology | 178.53 | +0.3886 | 99.71 | `0.30*+1.108+0.15*+1.023 → *0.80−0.00` | +1.306 | +6.00% | 12.18% | 189.24 | 166.63–211.85 | 25 | MEDIUM |
| 3 | **WTW** | Finance | 335.92 | +0.3653 | 99.51 | `0.30*+1.395+0.15*+0.253 → *0.80−0.00` | -0.499 | +6.00% | 10.10% | 356.08 | 320.78–391.37 | none in 37d | MEDIUM |
| 4 | **BAX** | Health Care | 26.16 | +0.3559 | 99.32 | `0.30*+1.345+0.15*+0.276 → *0.80−0.00` | +0.462 | +6.00% | 13.28% | 27.73 | 24.12–31.34 | none in 37d | MEDIUM |
| 5 | **FTNT** | Technology | 161.95 | +0.3458 | 99.12 | `0.30*+0.797+0.15*+1.288 → *0.80−0.00` | +0.948 | +6.00% | 10.70% | 171.67 | 153.65–189.68 | none in 37d | MEDIUM |
| 6 | **HPQ** | Technology | 27.27 | +0.3442 | 98.93 | `0.30*+1.089+0.15*+0.689 → *0.80−0.00` | +0.358 | +6.00% | 11.66% | 28.91 | 25.60–32.21 | 25 | MEDIUM |
| 7 | **REGN** | Health Care | 762.63 | +0.3138 | 98.73 | `0.30*+0.867+0.15*+0.882 → *0.80−0.00` | +0.413 | +6.00% | 9.35% | 808.39 | 734.25–882.53 | none in 37d | MEDIUM |
| 8 | **BMY** | Health Care | 65.31 | +0.3127 | 98.54 | `0.30*+1.070+0.15*+0.466 → *0.80−0.00` | -0.229 | +6.00% | 9.01% | 69.23 | 63.11–75.35 | none in 37d | MEDIUM |
| 9 | **GRMN** | Industrials | 293.78 | +0.2981 | 98.34 | `0.30*+1.325+0.15*-0.165 → *0.80−0.00` | +0.163 | +6.00% | 15.09% | 311.41 | 265.29–357.53 | none in 37d | MEDIUM |
| 10 | **BBY** | Consumer Discretionary | 86.26 | +0.2835 | 98.15 | `0.30*+0.893+0.15*+0.577 → *0.80−0.00` | +0.531 | +6.00% | 8.41% | 91.44 | 83.89–98.98 | 26 | MEDIUM |

Full table of 24 in `06`; all 205 ranked names and score attribution in `05`.

## No-trade rationale

| # | Evidence threshold | Result |
|---|---|---|
| 1 | Pctl ≥ 80 | PASS — 103 names |
| 2 | ≥ 3 of 4 families non-negative | **FAIL** — only 2 families available |
| 3 | No family > 50% of conviction | **FAIL** — `Tech_Z` at 66.7% |
| 4 | Data completeness ≥ 85% | **FAIL** — DQ 0.80 |
| 5 | No hard stop | PASS |

Independently, the naive top-20 equal-weight sleeve breaches two portfolio caps — beta
+0.4608 below the 0.90 floor, and Health Care at
35.0% against the 30% cap — while correlation
(0.1282) and 95th-pctl drawdown
(7.41%) both pass. Those are composition failures routed to
`NO_TRADE`, not `HALTED`. **But they are not the binding constraint**: even a perfectly
shaped sleeve would be unpublishable because no constituent clears the evidence bar.

## Portfolio analytics

None — no portfolio was constructed. Diagnostic analytics for the naive sleeve are in `07`.

## Assumptions and limitations

1. **Two of four factor families have no fetch path.** `Fund_Z` and `Sent_Z` are
   `UNAVAILABLE` for all 513 names. Every score in this package rests on
   45% of the intended evidence base. This is the sole reason for `NO_TRADE`.
2. **The composite's ordering is not predictive.** Weighted-mean rank IC -0.1314 over
   n=439, negative in 20 of 28 vintages. Confidence is capped `MEDIUM`
   system-wide. Magnitude calibration is *healthy* (CI coverage 70.16%) —
   the two failure modes are separate.
3. **`Tech_Z` double-counts momentum.** `rs20`/`rs60` are constant shifts of `mom20`/`mom60`,
   so their z-scores are identical to 4e-16; momentum
   holds 33.3% of live weight rather than 16.7%. Discovered this
   run, disclosed in `05`, fixed as Track B effective next run.
4. **`eff_n` = 1.** All 439 settled records span a single 28-day window. Raw `n` looks
   authoritative and is not; no Track A change is eligible.
5. **Parametric tail estimates.** VaR95/CVaR95 and the 95th-pctl drawdown assume normality.
6. **Enhancing inputs absent** — options IV, short interest, bid-ask tape, analyst revisions.
   These cap confidence and exposure; per `rules.md § Input Classification` they are **not**
   `GO` blockers and were not used as such.
7. **IBKR MCP was unreachable** (weekend outage, 4 attempts). Grounding stood on three
   independent web sources.
8. **Constituent caches are 41 days old** (2026-06-21). Used as-is per protocol rule 5; worth refreshing.

## Next scheduled review

Next daily run: **2026-08-03** (Monday) pre-open. `eff_n` for `EQUITY_ALPHA` is projected to
reach 2 on **2026-08-05**
(43 predictions pending), the first
step toward Track A eligibility (`eff_n ≥ 3`, projected early September).
