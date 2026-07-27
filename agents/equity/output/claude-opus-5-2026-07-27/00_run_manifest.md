# 00 Run Manifest — 2026-07-27

## Run Identity

- **Run date:** 2026-07-27 (Monday). The scheduled job fired at **~09:55 ET**, i.e. ~25 minutes *after* the
  09:30 regular-session open, so this is an **intraday fire**, not the 07:27 pre-open slot.
- **Model:** `claude-opus-5`
- **Run mode:** full pipeline. `00`–`09`, `13`, `15` complete. `10` is a real early-session
  observation (live tape exists); `11`/`12` are timing stubs; `14`/`16` are not applicable on a
  Monday that is not month-end.
- **Data mode:** `DELAYED` — public endpoints plus an IBKR brokerage snapshot; no streaming feed.
  Every price used downstream was retrieved during this run.
- **Status target:** `GO` if and only if the evidence thresholds cleared. **Final status: `NO_TRADE`.**
- **Branch basis:** `run/claude-opus-5-2026-07-27`, rebased on `origin/main` commit `b988c5f`
  (which already contains the concurrent `gpt-5-2026-07-27` pre-open package, PR #50).

## Price and Return Basis

The last completed session is **2026-07-24** (Friday). The 2026-07-27 session was in progress while this run
executed, so:

- **Entry / target / CI / settlement basis:** the 2026-07-24 unadjusted official close (L002).
- **Return / indicator basis:** the 2026-07-24 **adjusted** close (L003) — momentum, relative strength,
  realized vol, downside vol, beta, tracking error, drawdown, and the `technical_indicators.py`
  input. This is the Track B rule accepted 2026-07-26 after the HON/FDX/SPGI corporate-action
  audit found a 4.6x sigma error from mixing bases.
- **The live 2026-07-27 tape is observation only** (L050, L051). It appears in `10_midday_monitor.md` and
  nowhere else — never as an entry, target, CI, or settlement price.

Because a Friday close is the basis, this run shares its entire market-data layer with the
`claude-opus-5-2026-07-26` and `gpt-5-2026-07-27` packages. That is disclosed rather than presented
as new information: what this run adds is an independent recomputation on the same basis, an updated
earnings-proximity layer (three calendar days closer than the 07-26 package), the refreshed
settlement/calibration state, and the first live look at the 2026-07-27 tape.

**Independent reproduction check.** This run's engine was written from `rules.md` plus the
`claude-opus-5-2026-07-26` methodology disclosure, then compared against that package: TRV
`Adj Score` `+0.3705`, `Tech_Z +1.1240`,
`Macro_Z +0.8397`, `beta -0.7014`,
`sigma 0.0933`, and the universe median sigma
`0.0961` all reproduce exactly. The scoring layer is therefore verified
against a prior package on an identical price basis, not merely self-consistent.

## Reflection Baseline

- **Folder:** `agents/equity/output/gpt-5-2026-06-29`
- **Flag:** **`CROSS_MODEL_BASELINE`** (L045).
- **Window:** 2026-06-12 → 2026-07-06, target 2026-06-29. `gpt-5-2026-06-29` is an exact target hit, 28 days old.
- **Why cross-model:** the only `claude-opus-5` folders are 2026-07-24, 2026-07-26 and 2026-07-27 —
  all newer than 21 days, which step 7 of the baseline algorithm forbids as a baseline.
- **Tiebreak, disclosed:** `gemini-3.5-flash-2026-06-29` also lands exactly on target. The two
  packages were verified **field-identical** on `entry_price`, `mu`, `sigma`, both CI bounds,
  `target_date`, `benchmark_price` and `adj_score` across all 17 shared records, so every MoM number
  is invariant to the choice; `gpt-5-2026-06-29` was taken as the model with the continuous run history in the
  window.

## Prediction Settlement Summary

`settlement_ledger.py --output-dir agents/equity/output --as-of 2026-07-27`:

```text
due_inventory: 0      conflicts: 0
canonical_equity_alpha_settlements: 231
canonical_market_forecast_settlements: 42
audit_only_rows: 145   rejected_rows: 87   total_candidate_rows: 505
```

**This run settles nothing, and that is the correct outcome** (L054). The concurrent
`gpt-5-2026-07-27` pre-open run fired ~1 hour before this one and settled all 34
keys that matured today. Due inventory is therefore `0` and `15_predictions.json` carries
`"settlements": []` with a `NO_DUE_PREDICTIONS` note — the 07-17 precedent for a same-day second
run. Those 34 canonical rows were re-validated by this run's ledger pass, not
re-settled.

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range |
|---|---:|---:|---|
| Raw `n` | 231 | 42 | ≥ 20 for Track A |
| 28-day `eff_n` | **1** | **1** | ≥ 3 for Track A |
| Hit rate | 51.08% | 23.81% | > 50% |
| CI coverage | 74.03% | 71.43% | 55–85% |
| Mean z | -0.1792 | -0.6640 | −0.5 to +0.5 |
| Track A eligible | `INSUFFICIENT_EFFECTIVE_N` | `INSUFFICIENT_EFFECTIVE_N` | — |

Weighted-mean rank IC across vintages: **-0.1843** over
231 scored pairs in
16 vintages.

## Source Ledger Coverage

| Claim type | Rows |
|---|---:|
| `OBSERVED` | 17 |
| `DERIVED` | 30 |
| `INFERRED` | 4 |
| `ILLUSTRATIVE` | 0 |
| `UNAVAILABLE` | 4 |
| **Total** | **55** |

No `ILLUSTRATIVE` rows: this is a live-data run. Status eligibility is not limited by ledger
coverage — all five Required inputs are grounded (below). It is limited by the evidence thresholds.

## GO-Gate Table

| # | Required input | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price (Price Sourcing Standard) | **GROUNDED** | Two independent web sources on all 28 published/ETF symbols: stockanalysis.com raw close (L002) vs CNBC `previous_day_closing` (L004). 27 of 28 agree to the cent; max divergence 0.396451% (BNY), inside the 1% gate. SPY/QQQ/SOXX additionally confirmed to the cent by IBKR brokerage snapshots (L005-L007). |
| 2 | ~60 trading days of history per name and for SPY | **GROUNDED** | 519/519 symbols fetched at 5Y range (L012); min 1255 bars across scoreable names is 185, well above 60. Only FDXF failed, on listing age. |
| 3 | sigma via the Sigma Fallback Chain | **GROUNDED** | REALIZED_VOL_30D computed for all 514 scoreable names and all 4 ETFs (L013). No name in either sleeve carries sigma = UNAVAILABLE. |
| 4 | Next earnings date — confirmed or cadence-estimated | **GROUNDED** | 57 names grounded across three bounded shortlist passes plus two retry rounds (L022-L026): CONFIRMED 34, ESTIMATED_CADENCE 16, ESTIMATED_PRINT_WEEK 7. The post-penalty top-20 is fully grounded; later entrants are excluded from publication, not scored penalty-free. |
| 5 | S&P 500 ∪ Nasdaq-100 index-union universe | **GROUNDED** | build_index_universe.py wrote 515 tickers (503 S&P 500, 101 Nasdaq-100, 89 overlap) -> eligible_universe.txt / universe_summary.json (L001). No sampled fallback used. |

**All five Required inputs are grounded, so `GO` is not blocked by data availability.** `NO_TRADE`
is forced by the *quality* gates in `rules.md § Evidence Thresholds`, three of which fail
independently — see `08_risk_review.md`.

### Enhancing inputs — confidence and exposure caps, never GO blockers

| Enhancing input | State | Effect |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` (L048) | sigma falls back to `REALIZED_VOL_30D`; no IV30 path |
| Short interest / borrow | `UNAVAILABLE` (L048) | `Sent_Z` cannot be built |
| Bid-ask spread tape | `UNAVAILABLE` (L048) | 50bp exclusion filter unenforceable; disclosed in `04` |
| Analyst revision tape | `UNAVAILABLE` (L048) | `Sent_Z` cannot be built |
| Institutional ownership flow | `UNAVAILABLE` (L048) | `Sent_Z` cannot be built |
| Full-universe fundamental feed | `UNAVAILABLE` (L046) | `Fund_Z` cannot be built |

Per `rules.md § Input Classification` these cap confidence at `MEDIUM` and gross exposure at 50%.
They are **not** cited as `GO` blockers anywhere in this package.

## Agents Executed

| Stage | Agent | Artifacts | Outcome |
|---|---|---|---|
| 0 | Orchestrator — Reflection | `02` | `CROSS_MODEL_BASELINE`; 0 due settlements |
| 1 | Data & Regime | `03`, `eligible_universe.txt`, `universe_summary.json` | `DELAYED`; regime `NEUTRAL` |
| 2 | Technical compute | `technical_indicators.json` | 518/518 symbols, 3 timeframes |
| 3 | Factor Scoring | `04`, `05` | 514 scored, 206 ranked, **0 investable** |
| 4 | Portfolio Construction | `06`, `07` | Task-0 feasibility fail → `NO_TRADE` |
| 5 | Risk Committee | `08` | `APPROVE` the `NO_TRADE` decision |
| 6 | Evolution | `13` | 1 Track B change `ACCEPT`ed |

## State Transitions

`PRECHECK` → `REFLECTION` → `DATA_OK` → `TECHNICALS_OK` → `SCORED` → `PORTFOLIO_DRAFT`(blocked at
Task 0) → `RISK_REVIEW` → **`NO_TRADE`** → `EVOLUTION_REVIEW`

## Outstanding Blockers

1. **`Fund_Z` / `Sent_Z` `UNAVAILABLE` universe-wide** (L046, L047) — the structural blocker. Two of
   four families are absent, so Evidence Threshold #2 (≥3 of 4 non-negative) is unreachable and #3
   (no family > 50% of conviction) fails arithmetically. Fix is Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`: bulk EDGAR `companyfacts.zip` plus
   threaded Nasdaq sentiment across the full universe to clear the 70%-coverage bar.
2. **`eff_n = 1` for both record types** (L044) — 231 `EQUITY_ALPHA` settlements still collapse
   into one non-overlapping 28-day window, so every Track A calibration proposal is `DEFER`red for
   insufficient effective evidence, including the diagnosed ETF `mu = beta × SPY_mu` error.
3. **Portfolio beta band structurally infeasible** (L049) — with
   41.2% of the universe at negative 60-day beta, the
   highest-beta 20 names in the entire ≥80th-percentile pool average
   +0.8519 against a 0.90 floor.

## Artifact Checklist

| Artifact | Present | Note |
|---|---|---|
| `00_run_manifest.md` | yes | this file |
| `01_preflight.md` | yes | 55-row Source Ledger |
| `02_reflection.md` | yes | 0 due settlements + MoM vs `gpt-5-2026-06-29` |
| `03_regime_and_data.md` | yes | regime + Core ETF Market Forecast Block |
| `04_universe_summary.md` | yes | index-union counts + coverage |
| `05_factor_scores.md` | yes | 24 published rows + attribution |
| `06_top_candidates.md` | yes | inherited, no new facts |
| `07_portfolio_proposal.md` | yes | `NO_TRADE` with computed feasibility evidence |
| `08_risk_review.md` | yes | 15-point checklist |
| `09_final_report.md` | yes | banner + summary |
| `10_midday_monitor.md` | yes | real early-session observation |
| `11_preclose_check.md` | yes | stub — 15:45 checkpoint not reached |
| `12_close_log.md` | yes | stub — 16:20 checkpoint not reached |
| `13_evolution_log.md` | yes | 1 Track B `ACCEPT` |
| `14_weekly_review.md` | yes | N/A — Monday |
| `15_predictions.json` | yes | 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST`, `settlements: []` |
| `16_monthly_review.md` | yes | N/A — not month-end |
| `eligible_universe.txt` | yes | 515 tickers |
| `universe_summary.json` | yes | cache timestamps + counts |
| `technical_indicators.json` | yes | 518 symbols x 3 timeframes |
| `run_computed_manifest.json` | yes | all 514 scored records |
| `settlement_manifest.json` | yes | canonical ledger as-of 2026-07-27 |
| `price_verification.json` | yes | 2-source price check |
| `price_history_fetch_manifest.json` | yes | per-symbol fetch result |
| `earnings_calendar_manifest.json` | yes | 57 names, 4 passes |
| `market_cap_eligibility_manifest.json` | yes | 1 `UNAVAILABLE` (BF-B, L055) |
| `sector_manifest.json` | yes | sector map + published-set sectors |
| `regime_data_manifest.json` | yes | regime evidence + ETF block |

**Core ETF Market Forecast Block:** present and complete for SPY, QQQ, SOXX in
`03_regime_and_data.md`, with three matching `MARKET_FORECAST` records in `15_predictions.json`.
