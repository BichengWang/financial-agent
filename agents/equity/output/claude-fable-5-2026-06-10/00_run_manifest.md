# 00 Run Manifest

- Date: 2026-06-10
- Run timestamp: 2026-06-10 14:46–15:05 ET (intraday, market open)
- Model: claude-fable-5
- Run mode: MANUAL_AUTOMATION (user-triggered single run of `daily_investment_system/main.md`)
- Data mode: **DELAYED** — all prices tool-fetched this run (IBKR MCP snapshot + history) with retrieval timestamps
- Top-level status target: GO (all Required inputs grounded)
- **Final publication status: NO_TRADE**
- Output folder: `investments/equity/output/claude-fable-5-2026-06-10/`

## Reflection Baseline

- Baseline path: `investments/equity/output/claude-opus-4-7-2026-05-12/`
- Baseline flag: `CROSS_MODEL_BASELINE` (no same-model `claude-fable-5` package exists anywhere; first run of this model)
- Selection rule: MoM window 2026-04-26 → 2026-05-20, target 2026-05-13; only in-window folder is the cross-model 2026-05-12 package (1 day from target).
- Baseline audit note: the baseline run was `ILLUSTRATIVE_MODE` / `REVIEW_ONLY` with placeholder numerics; its top-5 ranking (MSFT, NVDA, META, GOOGL, AMZN) is still scored as a forecast per policy, using fetched historical 2026-05-12 closes as prior reference prices (HISTORICAL, ledger rows in 01).
- Short-window folders explicitly not used for MoM binding: `gpt-5-2026-06-07`, `gpt-5-2026-06-09` (consulted as context only).

## Prediction Settlement Summary

`NO_PREDICTION_LEDGER` — scanned all 12 dated output folders (all models) on 2026-06-10; no `15_predictions.json` exists anywhere. Nothing to settle. This run emits the **first** machine-readable prediction ledger (12 OPEN records, target date 2026-07-08).

## State Trace

`PRECHECK -> REFLECTION -> DATA_OK(DELAYED) -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW(REJECT after 1 revision: beta band + sector caps unfixable) -> NO_TRADE`

## Agents Executed

1. Orchestrator (manifest, preflight Source Ledger, reflection, predictions ledger)
2. Data & Regime agent → 03
3. Factor Scoring agent → 04, 05
4. Portfolio Construction agent → 06, 07
5. Risk Committee agent → 08
6. Evolution agent → 13

## GO-Gate Table (Required inputs — only these may block GO)

| Required input | Status | Evidence |
|---|---|---|
| Grounded entry price per name | **PASS** | 30/30 snapshot-fetched with `retrieved_at` (ledger L-rows) |
| ~60d fetched price history (portfolio names + SPY) | **PASS** | 11 series × 62 daily bars fetched this run |
| Sigma via Sigma Fallback Chain | **PASS** | `REALIZED_VOL_30D` for all 12 ranked names; zero `UNAVAILABLE` sigmas |
| Next earnings date (confirmed or `ESTIMATED (±5d)`) | **PASS** | 4 observed from fetched tape gaps, 8 cadence-estimated; MU inside buffered 19d window → penalized |
| Sampled universe ≥ 30 grounded names | **PASS** | n = 30, sampling rule disclosed in 04 |

Missing **Enhancing** inputs (options IV/skew, short-interest/borrow, bid-ask tape, analyst-revision tape, institutional flow, full-universe screen): present as **confidence cap (MEDIUM) + data-quality multiplier 0.85 + 50% gross-exposure cap**. Per `eval/research_system.md § Input Classification` they are NOT GO blockers and are not cited as such anywhere in this package.

## Why NO_TRADE (not GO, not REVIEW_ONLY)

All five Required inputs are grounded, so `REVIEW_ONLY` on data grounds would be improper GO-blocking. The run fails instead on **portfolio constructability**: the only names clearing the investable bar (5 of 30) form an all-defensive basket with computed sleeve beta **-0.14** vs the protected 0.90–1.10 band, and 3-sector concentration (HC 41% / Staples 39% / Energy 20%) vs the protected 30% sector cap. One revision pass could not fix both without admitting sub-threshold names. Per `eval/stop_criteria.md § Downgrade To No-Trade` (items 2/6): **NO_TRADE**. Full forecasts are still published and settleable.

## Source Ledger Coverage Summary

| Claim type | Rows |
|---|---:|
| OBSERVED | 121 |
| DERIVED | 19 |
| INFERRED | 40 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE | 0 |

(Counts from `01_preflight.md`; INFERRED rows are earnings-cadence estimates and the disclosed fundamental/sentiment/macro sub-scores.)

## Artifact Checklist

| Artifact | Status |
|---|---|
| `00_run_manifest.md` | Complete |
| `01_preflight.md` | Complete — 180-row Source Ledger |
| `02_reflection.md` | Complete — settlement scan + MoM table + carry-forwards |
| `03_regime_and_data.md` | Complete |
| `04_universe_summary.md` | Complete |
| `05_factor_scores.md` | Complete |
| `06_top_candidates.md` | Complete |
| `07_portfolio_proposal.md` | Complete — constraint failure documented |
| `08_risk_review.md` | Complete — REJECT → NO_TRADE |
| `09_final_report.md` | Complete |
| `10_midday_monitor.md` | Placeholder — single-session run, checkpoint not scheduled |
| `11_preclose_check.md` | Placeholder — single-session run |
| `12_close_log.md` | Placeholder — pending close |
| `13_evolution_log.md` | Complete |
| `15_predictions.json` | **Complete — 12 OPEN records + empty settlements block (first ledger in system history)** |
