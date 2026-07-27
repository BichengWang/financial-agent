# 00 Run Manifest — 2026-07-27

## Run Identity

- **Run date:** 2026-07-27 (Monday); execution began about 08:47 ET, before the 09:30 ET regular-session open. The latest completed session was Friday 2026-07-24.
- **Model:** `gpt-5`
- **Run mode:** full pre-open pipeline. `00`–`09`, `13`, and `15` are complete; `10`–`12` are timing stubs because their checkpoints had not occurred; `14` and `16` are not applicable on Monday.
- **Data mode:** `DELAYED` — public endpoints, no live brokerage feed. Every history and every settlement/forecast price was retrieved during this run.
- **Final status:** **`NO_TRADE`**.
- **Branch basis:** `run/gpt-5-2026-07-27` rebased cleanly on `origin/main` commit `7bdc90a` before execution.

## Price and Return Basis

All settlement and new-forecast entry prices use the **unadjusted 2026-07-24 official close**. Every one of the 41 unique symbols appearing in a settlement or new forecast was freshly checked against StockAnalysis, Nasdaq historical, and CNBC; all pass the 1% gate, with maximum divergence **0.396451%** (BNY), while the 17 due-settlement symbols agree exactly.

The 2026-07-26 accepted Track B rule is carried forward: return-derived metrics and `technical_indicators.json` use **adjusted closes**; entry, target, and CI prices use unadjusted closes. The new 519-symbol fetch reproduced all 514 scoreable raw closes and all 517 comparable technical packs exactly versus the prior package.

## Reflection Baseline

- **Folder:** `agents/equity/output/gpt-5-2026-06-29`
- **Selection:** `SAME_MODEL_BASELINE`; exception flag **`NONE`**.
- **Window:** 2026-06-12 through 2026-07-06; target 2026-06-29. The folder is an exact target hit and 28 days old.
- The same vintage is one of the two model ledgers that matured today, so the formal MoM reflection is directly settleable.

## Prediction Settlement Summary

`settlement_ledger.py --output-dir agents/equity/output --as-of 2026-07-27` after writing today's ledger:

```text
due_inventory: 0     conflicts: 0
canonical_equity_alpha_settlements: 231   (203 before this run)
canonical_market_forecast_settlements: 42 (36 before this run)
audit_only_rows: 145     rejected_rows: 87     total_candidate_rows: 505
```

**34 forecasts matured:** two field-identical 2026-06-29 model vintages (`gpt-5` and `gemini-3.5-flash`), each with 14 `EQUITY_ALPHA` and 3 `MARKET_FORECAST` records. Because the run is pre-open on their target date, every key settles at the latest completed close, 2026-07-24, with explicit `TARGET_EQ_RUN_DATE` timing.

| Metric | EQUITY_ALPHA | MARKET_FORECAST | Healthy range |
|---|---:|---:|---:|
| Raw `n` | 231 | 42 | ≥20 for Track A |
| `eff_n` | **1** | **1** | ≥3 for Track A |
| Hit rate | 51.08% | **23.81%** | >50% |
| CI coverage | 74.03% | 71.43% | 55–85% |
| Mean z | −0.1792 | **−0.6640** | −0.5 to +0.5 |
| Weighted rank IC | **−0.1843** (16 vintages) | N/A | >0 |

`eff_n = 1` blocks every Track A calibration proposal. Negative rank IC keeps the `MEDIUM` confidence cap active; all new equity forecasts are independently `LOW` because the family-coverage gate fails.

## GO-Gate Table

| # | Required input | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price | **GROUNDED** | 41/41 settlement/forecast symbols, three sources, max divergence 0.396451%; per-source `retrieved_at` in `price_verification.json` |
| 2 | ~60 trading days history per name + SPY | **GROUNDED** | 519/519 histories fetched; 514/515 equities scoreable; only FDXF has 40 usable bars and fails listing-age/history gates |
| 3 | Sigma fallback chain | **GROUNDED** | `REALIZED_VOL_30D` from adjusted closes for all 514 scoreable names and 3 core ETFs |
| 4 | Next earnings date | **GROUNDED for all 24 published names** | Current-run Nasdaq fetch; 56 names in the bounded scoring passes (37 confirmed, 18 cadence-estimated, 1 conservative print-week estimate) |
| 5 | Index-union universe | **GROUNDED** | 503 S&P + 101 Nasdaq-100 − 89 overlap = 515; helper succeeded |

**Enhancing inputs unavailable:** options IV/skew, short interest/borrow, bid-ask tape, analyst revisions, and institutional flow. They reduce DQ to 0.80 and cap gross exposure; they are not cited as `GO` blockers.

## Status Rationale

**`NO_TRADE`** is required because zero of 514 names is investable:

1. `Fund_Z` and `Sent_Z` remain unpromoted/`UNAVAILABLE`, so no name can reach three supportive families.
2. DQ is 0.80, below the 0.85 completeness threshold.
3. The top-10 maximum attainable sleeve beta is −0.159 versus the protected 0.90–1.10 band.
4. Industrials are 37.5% of the published set and five names are inside the earnings-risk gate.

The 24-name sleeve is monitoring-only and exists to create settleable evidence. No portfolio weights were drafted.

## Source Ledger Coverage

| Claim type | Rows |
|---|---:|
| `OBSERVED` | 15 |
| `DERIVED` | 26 |
| `INFERRED` | 4 |
| `ILLUSTRATIVE` | 0 |
| `UNAVAILABLE` | 3 |
| **Total** | **48** |

## State and Agent Outcomes

`PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(pre-check failed) → RISK_REVIEW → PUBLISHED → NO_TRADE`

| Stage | Artifact | Outcome |
|---|---|---|
| Reflection | `02` | 34 settled; due 0; conflicts 0 |
| Data / regime | `03` | `DELAYED`; `NEUTRAL`; full index union |
| Technical compute | `technical_indicators.json` | 518 records: 517 OK, FDXF explicitly unavailable |
| Factor scoring | `04`, `05` | 514 ranked; 0 investable; 24 monitoring forecasts |
| Portfolio | `06`, `07` | Task-0 beta feasibility failed before sizing |
| Risk | `08` | `APPROVE` the `NO_TRADE` publication |
| Evolution | `13` | Track B earnings-signature tightening `ACCEPT`, effective next run |

## Artifact Checklist

All required artifacts are present: `00`–`09`, timing stubs `10`–`12`, `13`, Monday stubs `14`/`16`, `15_predictions.json`, `eligible_universe.txt`, `universe_summary.json`, `technical_indicators.json`, `settlement_manifest.json`, and the current-run support manifests for history, price, market cap, earnings, sectors, regime, and deterministic scoring.

`15_predictions.json` contains **24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` predictions and 34 settlements**. The Core ETF block is present in `03`, summarized in `09`, and represented by SPY/QQQ/SOXX records.

## Outstanding Blockers

1. Full-universe production `Fund_Z` / `Sent_Z` coverage is still the engineering unblock for the repeated `NO_TRADE` result.
2. `eff_n = 1` blocks Track A repair of negative rank ordering and the ETF-mu category error.
3. Market-forecast calibration remains poor (23.81% direction hit rate; mean z −0.6640).
4. The vendor-empty earnings signature rule is tightened in `13` for the next run; EQR and PKG remain disclosed under today's prior rule.
