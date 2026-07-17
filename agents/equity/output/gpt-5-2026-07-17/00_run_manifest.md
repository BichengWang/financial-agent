# Run Manifest — 2026-07-17

- Model: `gpt-5`
- Run mode: manual execution of `agents/equity/daily_investment_system/main.md`
- Data mode: `DELAYED` (current-run public Yahoo/Nasdaq observations; completed-history risk windows)
- Final status: `NO_TRADE`
- Final state: `EVOLUTION_REVIEW` (published package complete; scheduled close checkpoints remain not due)
- Reflection baseline: `agents/equity/output/gpt-5-2026-06-19`; exception flag `NONE` (exact same-model target-date match)
- Settlement summary: 63 new exact-date settlements; canonical 119 equity + 18 market records; due inventory 0; conflicts 0.
- Source Ledger: 370 contiguous rows — 148 OBSERVED, 159 DERIVED, 36 INFERRED, 0 ILLUSTRATIVE, 27 UNAVAILABLE.
- Agents executed: Orchestrator; Data and Regime; Factor Scoring; Portfolio Construction feasibility; Risk Committee; Evolution.
- Outstanding blocker to a trade set: none of the five Required inputs. The investability evidence gates fail because Technical is the only supportive family, completeness is 77.78%, and one family supplies 100% of nonzero conviction. Six monitor names (UNP, INCY, AAPL, VLO, CHRW, IQV) have literal earnings dates inside 14 calendar days; applying the required +/-5-day buffer to estimated dates adds MPC, PSX, and DOC, for nine buffered-window names and an independent event-concentration breach (L213,L222,L240,L249,L267,L276,L285,L312,L321).

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED -> EVOLUTION_REVIEW`

## GO-Gate Table

| Required input | Result | Evidence |
| --- | --- | --- |
| Grounded entry price | PASS | 23 forecasts use 38 verified Yahoo/Nasdaq bundles; max divergence 0.103205% (L004). |
| ~60 fetched sessions per name + SPY | PASS | 20 monitors and 3 core ETFs have >=251 Nasdaq bars; risk windows end 2026-07-16. |
| Sigma fallback chain | PASS | All 23 forecasts use REALIZED_VOL_30D from fetched completed histories. |
| Next earnings date | PASS | Every monitor has a future source-backed or cadence-estimated date; buffered penalties applied. |
| Index-union universe | PASS | Helper produced 515 names; 513 scoreable (L002). |

## Enhancing Inputs (Caps, Never Blockers)

Options IV/skew, short interest/borrow, full-universe bid-ask tape, analyst-revision tape, and ownership flow are `UNAVAILABLE` (L012). They lower DQ/confidence; they do not cause `NO_TRADE`. Fundamental and Sentiment diagnostic tooling remains `SHADOW` at 24/515 coverage and is excluded from Adj Score and the 3-of-4 test.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | PRESENT / generated |
| 01_preflight.md | PRESENT / generated |
| 02_reflection.md | PRESENT / generated |
| 03_regime_and_data.md | PRESENT / generated |
| 04_universe_summary.md | PRESENT / generated |
| 05_factor_scores.md | PRESENT / generated |
| 06_top_candidates.md | PRESENT / generated |
| 07_portfolio_proposal.md | PRESENT / generated |
| 08_risk_review.md | PRESENT / generated |
| 09_final_report.md | PRESENT / generated |
| 10_midday_monitor.md | PRESENT / generated |
| 11_preclose_check.md | PRESENT / generated |
| 12_close_log.md | PRESENT / generated |
| 13_evolution_log.md | PRESENT / generated |
| 14_weekly_review.md | PRESENT / generated |
| 15_predictions.json | PRESENT / generated |
| 16_monthly_review.md | PRESENT / generated |
| eligible_universe.txt | PRESENT / generated |
| universe_summary.json | PRESENT / generated |
| technical_indicators.json | PRESENT / generated |
| settlement_manifest.json | PRESENT / generated |

Core ETF forecast block: **PRESENT** for SPY, QQQ, and SOXX in `03`, summarized in `09`, and serialized in `15_predictions.json`.
