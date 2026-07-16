# 00 Run Manifest — 2026-07-16 (claude-haiku-4-5, SHADOW validation run)

## Scope disclosure

**This is not a full daily investment cycle.** It contains no preflight, reflection/settlement, universe build, candidate ranking, portfolio proposal, risk review, or `15_predictions.json` — intentionally, so it is invisible to tooling that scans `agents/equity/output/*/15_predictions.json` (e.g. `settlement_ledger.py`) and cannot be mistaken for a GO/NO_TRADE/REVIEW_ONLY cycle. It exists solely to execute and record the first Fundamental/Sentiment SHADOW shadow-run called for in `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` §Governance step 1 ("one run of shadow output... before they count toward the 3-of-4 test") and rules.md's §SHADOW Diagnostic Tooling ("after at least one full shadow run").

## What ran

- `agents/equity/daily_investment_system/fundamental_diagnostics.py` and `sentiment_diagnostics.py`, invoked live against a 24-ticker shortlist (the full ranked+monitoring set from the most recent real daily run, `claude-fable-5-2026-07-15`: DVA, CRWD, CVS, FFIV, CRL, EXPD, NTAP, MPC, FTNT, DDOG, STT, MNST, PANW, RVTY, GEN, WST, GS, DOC, MS, ELV, plus carry-forwards LLY, ABBV, LIN, ANET).
- Fetch execution (fundamental + sentiment) was run by a `claude-haiku-4-5` subagent, per user instruction, as a test of running this workflow on a smaller model; verification, bug diagnosis, and the promotion decision below were done by the orchestrating `claude-sonnet-5` session.
- Data mode: `DELAYED` (live SEC EDGAR / Nasdaq endpoint fetches, not cached).

## Result summary

| Family | Sourceable | Fetch failures | n |
|---|---|---|---|
| Fund_Z | 100.0% (24/24) | 0 | avg 6.1 of 8 signals/name |
| Sent_Z | 100.0% (24/24) | 0 | avg 2.3 of 3 signals/name |

**A real bug was found and fixed during this run's verification** (see `13_evolution_log.md` for the full Track B entry): `fundamental_diagnostics.py`'s tag-fallback logic picked the first XBRL tag with *any* quarterly-shaped data, with no check that the data was actually recent. For CVS and ABBV, the first-priority revenue tag had not been filed under since 2019/2017 respectively (both switched to a different tag), so `revenue_yoy_growth` was silently computed from a 6-7-year-old filing instead of falling through to the current tag. FFIV's `Liabilities` tag had the same problem (2 rows, both 2019). Fixed by adding a staleness check (`_MAX_TAG_STALENESS_DAYS = 200`) that rejects a tag's data and falls through to the next synonym when the most recent row is too old, plus deriving liabilities from `Assets - StockholdersEquity` when the raw tag itself is stale or absent. All numbers in this manifest and the evolution log use the corrected (post-fix) output. See PR for `fix/fundamental-diagnostics-stale-tag-fallback`.

**Cross-family check** (plan's acceptance test: "at least one name satisfies 3-of-4 non-negative families"): combining this run's Fund_Z/Sent_Z with real Tech_Z/Macro_Z from `claude-fable-5-2026-07-15/05_factor_scores.md` for the same 24 names, **15 of 24 names satisfy ≥3-of-4 non-negative families** (ABBV, ANET, CRL, CRWD, CVS, DDOG, DOC, ELV, EXPD, FTNT, LIN, LLY, MNST, NTAP, WST). The plan's bar of "at least one" is cleared with wide margin.

## Decision

See `13_evolution_log.md`. Summary: the Track B shadow-run milestone is logged as satisfied. Fund_Z/Sent_Z remain `SHADOW` and do **not** start counting toward the 3-of-4 evidence threshold or Adj Score — coverage is 24 of ~514 eligible names (~4.7%), far below the 70%-of-universe threshold rules.md's own §Financial Metrics and Score Attribution already requires before any metric may contribute to Adj Score. That is Phase 2's job (bulk `companyfacts.zip` + threaded Nasdaq fetch across the full universe), not yet done.
