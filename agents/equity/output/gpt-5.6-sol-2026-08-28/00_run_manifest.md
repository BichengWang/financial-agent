# 00 — Run Manifest · 2026-08-28

| Field | Value |
|---|---|
| Run id | `gpt-5.6-sol-2026-08-28` |
| Model | `gpt-5.6-sol` |
| Run mode | post-close full pipeline |
| Data mode | **DELAYED** |
| Status target / final | GO evaluation / **NO_TRADE** |
| Regime | **BULL** |
| Evaluation horizon | 2026-09-25 (28 calendar days) |
| Agents executed | Orchestrator; Reflection; Data/Regime; Factor Scoring; Portfolio Construction; Risk Committee; Evolution |
| MoM baseline | `agents/equity/output/gpt-5-2026-07-30` — **CROSS_MODEL_BASELINE** |
| Settlements | due 2; settled 0; conflicts 0; two EQR keys remain `UNSETTLEABLE_CORPORATE_ACTION` |
| Canonical EQ ledger | n=1355; eff_n=2; Track A INSUFFICIENT_EFFECTIVE_N |
| Canonical MF ledger | n=201; eff_n=2; Track A INSUFFICIENT_EFFECTIVE_N |
| Intraday checkpoints | 10–12 omitted because this was a single post-close full-pipeline run |

## GO gate

| Gate | Result | Evidence |
|---|---|---|
| Grounded entry prices | PASS | 23/23 two-source checks, max deviation 0% |
| ~60 trading days history | PASS | 518/519 histories fetched; all ranked rows have >=60 returns |
| Sigma source | PASS | all forecasts use `REALIZED_VOL_30D` |
| Earnings date/status | PASS | 31/31 requested weekdays fetched through 2026-10-09 |
| Index union | PASS | 515 cached constituents; 500 scoreable after seven binding MoM drops |
| ≥5 investable names | **FAIL** | 0 names: only 2/4 families, technical >50% of live conviction, DQ 0.80<0.85 |
| Risk feasibility | **FAIL** | equal-weight monitor beta 0.1523 outside 0.90–1.10; drawdown 8.23%>8.00% |

Enhancing inputs missing: point-in-time fundamentals, sentiment/positioning, options IV/skew,
borrow/short-interest, bid-ask tape, and analyst revisions. Confidence is capped at MEDIUM because
weighted rank IC is -0.0495.

## Working-data checklist

- Index caches: S&P 500 503, Nasdaq-100 101,
  overlap 89, union 515; cache timestamp
  2026-06-21T21:05:56Z.
- History: 518 OK / 1 failed; EQR only.
- Technical indicators: generated for full fetched set through 2026-08-28.
- Core ETF block: SPY, QQQ and SOXX complete, grounded, and written to `15_predictions.json`.

## Durable artifact checklist

- [x] `00_run_manifest.md`
- [x] `01_preflight.md`
- [x] `02_reflection.md`
- [x] `03_regime_and_data.md`
- [x] `04_universe_summary.md`
- [x] `05_factor_scores.md`
- [x] `06_top_candidates.md`
- [x] `07_portfolio_proposal.md`
- [x] `08_risk_review.md`
- [x] `09_final_report.md`
- [x] `13_evolution_log.md`
- [x] `14_weekly_review.md`
- [x] `15_predictions.json`

Outstanding blocker: EQR successor economics require human-approved corporate-action mapping;
the system intentionally leaves both keys due.
