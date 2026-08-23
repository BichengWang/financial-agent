# 00 — Run Manifest · 2026-08-22

| Field | Value |
|---|---|
| Run date | `2026-08-22` (Saturday) |
| Price basis | `2026-08-21` (Friday) close — final at every vendor |
| Fire window | 2026-08-22 ~15:06 ET, markets closed |
| Model | `claude-opus-5` |
| Run mode | Weekend, full pipeline |
| Data mode | `DELAYED` — every price fetched this run; no real-time feed wired |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Regime | `BULL` (prior same-model baseline: `NEUTRAL`) |
| Universe | `INDEX_UNION_PCTL (n=509)` |
| Published names | 24 (monitoring sleeve only — 0 investable) |
| Target date | `2026-09-19` (`run_date + 28d`) |

## Weekend-run convention

A Saturday run shares the Friday close exactly, so **it adds no new market information**. Its value
is the settlement and calibration layer — 227 predictions settled this
run — plus keeping the audit trail unbroken (`runbook.md`: no skipped days). The ranking is a fresh
computation on an unchanged basis, and `09` says so plainly rather than implying a new read of the
tape.

`NO_TRADE` is the accurate label rather than `REVIEW_ONLY`: all five Required inputs are grounded and
the blocker is candidate quality and portfolio feasibility, not stale or weak data. `REVIEW_ONLY` is
reserved for the latter, and a Friday close read on the following Saturday is neither.

## State transitions

```text
PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT ->
RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW
```

No stage halted. `PORTFOLIO_DRAFT` terminated at the Task-0 feasibility pre-check with `NO_TRADE`, so
no weights were drafted and the intra-loop revision budget was untouched.

## Agents executed

Orchestrator (manifest, preflight, reflection, publication) · Data and Regime · Factor Scoring ·
Portfolio Construction (Task 0 only) · Risk Committee · Evolution.

## GO-Gate Table

Only the five **Required** inputs from `rules.md § Input Classification` may block `GO`.

| Required input | Status | Blocks GO? | Evidence |
|---|---|---|---|
| 1. Grounded entry price | **GROUNDED** | No | 27/27 symbols, 3 independent sources, 0.000000% max deviation (L002/L011/L012) |
| 2. ~60d price history per name + SPY | **GROUNDED** | No | 518/519 symbols at 5Y depth in 14.1s (L002) |
| 3. sigma via the Sigma Fallback Chain | **GROUNDED** | No | `REALIZED_VOL_30D` for all 509 scored names (L300-series) |
| 4. Next earnings date | **GROUNDED** | No | complete forward sweep, 26/26 business days, zero transport failures (L010) |
| 5. Index-union universe | **GROUNDED** | No | 515-name union from `build_index_universe.py` (L001) |

**Enhancing inputs missing** — these are caps, never blockers:

| Missing Enhancing input | Effect |
|---|---|
| Options IV / skew | data-quality multiplier → 0.80; confidence capped `MEDIUM` |
| Short interest / borrow | same |
| Bid-ask spread tape | same |
| Analyst revision tape | same |
| Institutional ownership flow | same |

None of the above is cited as a `GO` blocker anywhere in this package.

## Final status determination

`NO_TRADE` on five independent grounds — any one sufficient:

| # | Ground | Evidence |
|---|---|---|
| 1 | Evidence threshold 2 | only 2 of 4 factor families are available (Fund_Z / Sent_Z UNAVAILABLE universe-wide) |
| 2 | Evidence threshold 3 | Technical carries 66.7% of live conviction, above the 50% cap |
| 3 | Evidence threshold 4 | data completeness 80% < 85% |
| 4 | Stop criteria NO_TRADE #6 | beta band structurally infeasible — max attainable sleeve beta 0.4841 < the 0.90 floor under the 5% single-name cap |
| 5 | Stop criteria NO_TRADE #6 | sector concentration — Health Care 45.0% on the naive top-20 EW sleeve, above the 30% cap |

Grounds 4 and 5 are **new this run** and were recomputed rather than inherited: the four runs from
2026-07-29 through 2026-08-03 were all beta-feasible.

## Reflection baseline

| Field | Value |
|---|---|
| Baseline path | `agents/equity/output/claude-opus-5-2026-07-24` |
| Baseline flag | **none** — same-model folder in-window at delta 1d |
| Tie | 2-way at delta 1d with `claude-opus-5-2026-07-26`, resolved by rule 8(c) lexicographic |
| Tie spread | 0.8pp hit rate — **conclusion invariant** |
| MoM window | 2026-07-08 … 2026-08-01, target 2026-07-25 |

## Prediction settlement summary

| Field | Value |
|---|---|
| Due inventory at `--as-of 2026-08-22` | 227 keys |
| Settled this run | **227** (203 `EQUITY_ALPHA`, 24 `MARKET_FORECAST`) |
| Unsettleable | 0 |
| Timing flags used | `ORDINARY` for all keys — every target date is a completed trading session before the run date |
| Post-write due inventory | **0** |
| Post-write conflicts | **0** |

### Canonical rolling calibration

| Record type | raw n | 28-day eff_n | Hit rate | CI coverage | Mean z | Track A eligible |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 1,153 | 2 | 39.38% | 71.47% | -0.5506 | No — INSUFFICIENT_EFFECTIVE_N |
| `MARKET_FORECAST` | 174 | 2 | 35.71% | 90.23% | -0.2952 | No — INSUFFICIENT_EFFECTIVE_N |

**`eff_n` moved off 1 for the first time**, to 2 for both record types — validating the falsifiable
projection made by the 2026-07-28 package. The `>= 3` Track A gate projects to
2026-09-03 (`EQUITY_ALPHA`) and
2026-09-07 (`MARKET_FORECAST`).

## Source Ledger coverage

| Field | Value |
|---|---|
| Ledger rows in `01` | **171** |
| Rows tagged `ILLUSTRATIVE` | **0** — the run is not in `ILLUSTRATIVE_MODE` |
| Rows tagged `UNAVAILABLE` | 1 (FRED `DTB3` fetch failure, L008b — documented fallback used) |
| Status eligibility | all five Required inputs grounded ⇒ eligible for `GO`; `NO_TRADE` is driven by evidence thresholds and portfolio feasibility, not by grounding |

## Durable artifact checklist

Verified against files on disk **after** they were written. (The 2026-08-07 package recorded why:
this checklist is normally composed before the artifacts exist, so a truncated run produces a false
claim.)

| Artifact | Required | Status | Size |
|---|---|---|---|
| `00_run_manifest.md` | Always | **Published** (this file) | — |
| `01_preflight.md` | Always | **Published** | 49,320 bytes |
| `02_reflection.md` | Always | **Published** | 47,210 bytes |
| `03_regime_and_data.md` | Always | **Published** | 7,239 bytes |
| `04_universe_summary.md` | Always | **Published** | 7,260 bytes |
| `05_factor_scores.md` | Always | **Published** | 35,444 bytes |
| `06_top_candidates.md` | Always | **Published** | 9,935 bytes |
| `07_portfolio_proposal.md` | Always | **Published** | 13,798 bytes |
| `08_risk_review.md` | Always | **Published** | 8,263 bytes |
| `09_final_report.md` | Always | **Published** | 14,486 bytes |
| `13_evolution_log.md` | Always | **Published** | 9,243 bytes |
| `15_predictions.json` | Always | **Published** | 294,393 bytes |

Optional checkpoint artifacts, correctly omitted rather than stubbed:

| Artifact | Required | Status | Size |
|---|---|---|---|
| `10_midday_monitor.md` | Only when the checkpoint runs | Not created — no midday checkpoint on a Saturday | — |
| `11_preclose_check.md` | Only when the checkpoint runs | Not created — market closed | — |
| `12_close_log.md` | Only when the checkpoint runs | Not created — market closed | — |
| `14_weekly_review.md` | Friday after close | Not owed — this is a Saturday run; the Friday 2026-08-21 session had no run | — |
| `16_monthly_review.md` | Last trading day of month | Not owed — 2026-08-31 is the last trading day of August | — |

## Working-data checklist

Written to `agents/equity/.work/claude-opus-5-2026-08-22/` and **not committed** (spec change 2026-08-01).
Every decision-relevant value they contain is persisted inline in `01`, `05`, and `15`.

| Working file | Contents | Status |
|---|---|---|
| `eligible_universe.txt` | 515 tickers | OK |
| `universe_summary.json` | S&P 503 / NDX 101 / overlap 89 / union 515 | OK |
| `technical_indicators.json` | 519 symbols, daily+weekly+monthly blocks | OK |
| `run_computed_manifest.json` | 509 scored records + regime + ETF block + feasibility | OK |
| `settlement_manifest.json` | 1,682 candidate rows, due_inventory 0 | OK |
| `price_verification.json` | 27 symbols x 3 sources | OK |
| `portfolio_feasibility.json` | beta / correlation / drawdown / sector pre-check | OK |

| Helper | Result |
|---|---|
| `build_index_universe.py` | **success** — 515 tickers (S&P 503, NDX 101, overlap 89); caches fetched 2026-06-21, **62 days stale**; used as-is per `rules.md` rule 5 |
| `technical_indicators.py` | **success** — 519 symbols, computed from the adjusted-close tree |
| `settlement_ledger.py` | **success** — 1,682 candidate rows; due_inventory 0, conflicts 0 |
| Bulk history fetch | **518/519** symbols in 14.1s; 1 failure (`EQR`, corporate action — L025) |
| Forward earnings sweep | **complete** — 26/26 business days, zero transport failures |
| FRED `DTB3` | **failed** (8th consecutive) — Treasury CSV fallback used, 3.72% (L008, L008b) |
| IBKR MCP | **not attempted** — connector was reported invalidated on 2026-08-04 and no reconnect has occurred; grounding stands on three independent web sources |

## Core ETF Market Forecast Block status

**Complete.** All three core ETFs analysed and forecast in `03`, summarised in `09`, and written to
`15_predictions.json` as `MARKET_FORECAST` records with `benchmark: "NONE"`,
`benchmark_price: null`, `adj_score: null`.

| ETF | Entry | Beta vs SPY | mu | sigma | Confidence | Record present |
|---|---|---|---|---|---|---|
| SPY | 765.72 | 1.0000 | +2.00% | 3.56% | MEDIUM | yes |
| QQQ | 713.44 | 1.7144 | +2.43% | 6.34% | MEDIUM | yes |
| SOXX | 520.05 | 3.3339 | +5.17% | 15.28% | MEDIUM | yes |

## Outstanding blockers

| # | Blocker | Owner | Status |
|---|---|---|---|
| 1 | `Fund_Z` / `Sent_Z` `UNAVAILABLE` universe-wide — makes evidence thresholds 2/3/4 arithmetically unsatisfiable | Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` | **open** — needs bulk `companyfacts.zip` + threaded Nasdaq fetch across all ~509 names |
| 2 | Rank-order inversion in the composite score | Evolution | **open, unactionable** — Track A, gated at eff_n 2 < 3 |
| 3 | Two OPEN `EQR` predictions unsettleable after a corporate action (due 2026-08-23 / 2026-08-24) | Evolution | **addressed** — Track B accepted this run, effective 2026-08-23 |
| 4 | Constituent caches 62 days stale | Maintenance | **open** — upstream cause of blocker 3; refresh is maintenance, not an evolution change |
| 5 | No package for trading days 2026-08-11 … 2026-08-21 | Scheduler | **open** — recorded in `13`; not repairable, since reconstructing analysis from a different price basis would be fabrication |
