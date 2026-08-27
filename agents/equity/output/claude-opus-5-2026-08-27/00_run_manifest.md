# 00 — Run Manifest · 2026-08-27

| Field | Value |
|---|---|
| Run date | 2026-08-27 |
| Model | `claude-opus-5` |
| Run mode | scheduled daily run, post-close fire (19:09 ET) |
| Price basis | **2026-08-27** — completed Thursday regular session |
| Target date | 2026-09-24 (`run_date + 28d`) |
| Data mode | `DELAYED` |
| Status target | `GO` if the evidence thresholds and risk caps allow |
| **Final status** | **`NO_TRADE`** |
| Regime | `BULL` |
| Data quality multiplier | 0.80 (L020) |
| Universe | `INDEX_UNION_PCTL (n=509)` — 515-name index union, 6 rejected |
| Investable set | 0 names |
| Monitoring sleeve | 24 names, ranks 1–24 contiguous |
| Reflection baseline | `claude-opus-5-2026-07-30` |
| Baseline flag | `NONE (same-model folder at delta 0d)` (delta 0d; tie with `gpt-5-2026-07-30` resolved by rule 8(a) and both disclosed in `02 § 1`) |

## Agents executed

| Stage | Agent | Outcome |
|---|---|---|
| 0. Reflection | Orchestrator — Reflection Stage | complete — 229 settlements, 2 left due (corporate action), baseline selected with mandatory tie disclosure |
| 1. Data & regime | Data and Regime Agent | complete — `BULL`, data mode `DELAYED`, core ETF block published |
| 2. Technical indicator compute | `technical_indicators.py` | complete — 518 symbols, daily/weekly/monthly |
| 3. Factor scoring | Factor Scoring Agent | complete — 509 scored, 0 investable, 24 monitored |
| 4. Portfolio construction | Portfolio Construction Agent | **stopped at Task 0** — constraint feasibility pre-check proved the beta band unreachable; no weights drafted, no revision pass spent |
| 5. Risk committee | Risk Committee Agent | complete — `APPROVE` for publication at `NO_TRADE` |
| 6. Evolution | Evolution Agent | complete — one Track B change `ACCEPT`ed, three Track A findings `DEFER`red |

State machine: `PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT
(halted at Task 0) -> RISK_REVIEW -> PUBLISHED -> NO_TRADE -> EVOLUTION_REVIEW`.

## GO-Gate Table

| # | Required input | Status | Blocks GO? |
|---|---|---|---|
| 1 | Grounded entry price | GROUNDED | no |
| 2 | ~60 trading days of history per name + SPY | GROUNDED | no |
| 3 | sigma via the Sigma Fallback Chain | GROUNDED | no |
| 4 | Next earnings date | GROUNDED | no |
| 5 | Index-union universe | GROUNDED | no |

All five Required inputs are grounded, so no Required input blocks `GO`. Missing **Enhancing** inputs
are listed as caps, never blockers:

| Enhancing input missing | Cap applied |
|---|---|
| Options IV / skew | sigma falls to `REALIZED_VOL_30D`; confidence capped `MEDIUM` |
| Short interest / borrow | `Sent_Z` UNAVAILABLE; DQ 0.80 |
| Bid-ask spread tape | 50bp exclusion filter not applied (disclosed in `04`) |
| Analyst revision tape | `Fund_Z`/`Sent_Z` UNAVAILABLE; DQ 0.80 |
| Institutional ownership flow | no additional cap |

**`NO_TRADE` is therefore not an input-availability outcome.** It is forced by
`rules.md § Downgrade to NO_TRADE` #1 (0 names clear the evidence thresholds) and #6 (the sleeve is
structurally infeasible against the beta band and sector cap) — see `05`, `07`, `08`.

## Prediction settlement summary

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` |
|---|---|---|
| Due at fire | 204 | 27 |
| Settled this run | 202 | 27 |
| Left due (corporate action) | 2 | 0 |
| Conflicts | 0 | 0 |
| Canonical raw `n` (post-write) | 1355 | 201 |
| 28-day `eff_n` (post-write) | 2 | 2 |
| Track A calibration gate satisfied | no (`eff_n` < 3) | no (`eff_n` < 3) |

## Source Ledger coverage and status eligibility

| Item | Value |
|---|---|
| Source Ledger rows | 177 |
| Published prices grounded | 27/27 on 3 independent sources |
| Max cross-source deviation | 0.095123% (threshold 1%) |
| Confirmation re-reads required | 0 |
| Earnings sweep | 27/27 business days, 0 transport failures, complete |
| Status eligibility | `GO` not blocked by any Required input; refused on evidence thresholds and portfolio feasibility |

## Core ETF Market Forecast Block status

**Published.** One row each for SPY, QQQ and SOXX in `03`, summarized in `09`, with three
`MARKET_FORECAST` records in `15_predictions.json` carrying `benchmark: "NONE"`,
`benchmark_price: null`, `adj_score: null`.

## Durable artifact checklist

Written as the package was finalized, **after** the artifacts existed — the pre-composed checklist is
the root cause of the false "Published" claims found in the 2026-08-06, 2026-08-07 and 2026-08-14
packages.

| # | Artifact | Required | State |
|---|---|---|---|
| 00 | `00_run_manifest.md` | Always | Published |
| 01 | `01_preflight.md` | Always | Published |
| 02 | `02_reflection.md` | Always | Published |
| 03 | `03_regime_and_data.md` | Always | Published |
| 04 | `04_universe_summary.md` | Always | Published |
| 05 | `05_factor_scores.md` | Always | Published |
| 06 | `06_top_candidates.md` | Always | Published |
| 07 | `07_portfolio_proposal.md` | Always | Published |
| 08 | `08_risk_review.md` | Always | Published |
| 09 | `09_final_report.md` | Always | Published |
| 10 | `10_midday_monitor.md` | Only when the checkpoint runs | Not created — no midday checkpoint ran (single post-close fire) |
| 11 | `11_preclose_check.md` | Only when the checkpoint runs | Not created — no pre-close checkpoint ran |
| 12 | `12_close_log.md` | Only when the checkpoint runs | Not created — no intraday position was taken and no close checkpoint ran |
| 13 | `13_evolution_log.md` | Always | Published |
| 14 | `14_weekly_review.md` | Friday after close | Not created — 2026-08-27 is a Thursday. See the note below. |
| 15 | `15_predictions.json` | Always when any name is ranked | Published — 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` records, 229 settlements |
| 16 | `16_monthly_review.md` | Last trading day of month | Not created — the last August trading day is 2026-08-31 |

**Weekly-review note.** No `14_weekly_review.md` has been written since the scheduler gap began:
2026-08-21 (a Friday) had no run at all, and the 2026-08-22 Saturday package did not produce one
either. This run is a Thursday, so writing a weekly review here would take its census from the wrong
vantage point — the same objection that blocked backfilling `14` on 2026-08-22. The gap is recorded in
`13` instead, and the next Friday run (2026-08-28) owes a real one.

## Working-data checklist

Working files live under `.work/claude-opus-5-2026-08-27/` and the run scratchpad and are **not
committed** (`runbook.md § Retention Contract`, and the 2026-08-01 spec change). Every
decision-relevant value they carry is persisted in `01`, `05` and `15`.

| Working artifact | Helper | Result |
|---|---|---|
| `eligible_universe.txt` / `universe_summary.json` | `build_index_universe.py` | SUCCESS — 503 + 101, overlap 89, union 515; caches fetched_at 2026-06-21 (67 days stale, used per `rules.md` rule 5) |
| `technical_indicators.json` | `technical_indicators.py` | SUCCESS — 518 symbols on the adjusted-close tree, daily/weekly/monthly blocks |
| `settlement_manifest.json` | `settlement_ledger.py` | SUCCESS — pre-write 231 due / 0 conflicts; post-write 2 due / 0 conflicts |
| `stockanalysis_history_manifest.json` | run fetcher | SUCCESS — 518/519 symbols, 10.7s, 1 fetch error (`EQR`, corporate action) |
| `price_verification.json` | run verifier | SUCCESS — 27/27 grounded, max deviation 0.095123% |
| `earnings_sweep.json` | run sweeper | SUCCESS — complete 27-day sweep, 0 transport failures |
| `corporate_actions.json` | run classifier | SUCCESS — 4 candidates classified against two independent references each |
| `run_computed_manifest.json` | run engine | SUCCESS — 509 scored records; every figure in this package is generated from it |

## Outstanding blockers

| Blocker | Class | Owner | Status |
|---|---|---|---|
| `Fund_Z` / `Sent_Z` unsourceable across the universe | capability gap | `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` Phase 2 | **open** — the single cause of every `NO_TRADE` in this series |
| Composite ordering anti-correlated with forward alpha | calibration (Track A) | Evolution Agent | **deferred** — `eff_n` 2 < 3, eligible from 2026-09-03 |
| No wired scheduler | infrastructure | human | **open** — 12 of the 18 completed trading days from 2026-08-03 to 2026-08-26 have no package from any model |
| IBKR MCP connector invalidated since 2026-08-04 | tooling | human | **open** — grounding currently rests on three web sources with no brokerage cross-check |
| No FOMC calendar source | data | human | **open** — the field is reported `UNAVAILABLE`, not assumed absent |
