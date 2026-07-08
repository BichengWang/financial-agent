# 01 Preflight

## Data Freshness and Coverage Summary

| Domain | Status | Tag | Notes |
|---|---|---|---|
| Prices and returns | Unavailable | ILLUSTRATIVE | No market data provider attached. |
| Fundamentals | Unavailable | ILLUSTRATIVE | No live fundamentals snapshot. |
| Analyst revisions | Unavailable | N/A | Missing critical feed. |
| Options skew / IV | Unavailable | N/A | Missing critical feed. |
| Short interest / borrow | Unavailable | N/A | Missing critical feed. |
| Insider transactions | Unavailable | N/A | No SEC Form 4 feed. |
| Institutional flow (13F) | Unavailable | N/A | No 13F feed; would be ≥45-day delayed regardless. |
| Macro regime inputs | Partial | ILLUSTRATIVE | Simulated SPY/VIX/TLT/DXY context for process check only. |
| Event calendar | Unavailable | N/A | No verified earnings/dividend/split calendar. |

## Lineage Check

- No live data sources authenticated.
- No data tags can be promoted above `ILLUSTRATIVE` or `N/A`.
- Per `eval/research_system.md`, data tag mix materially weakens confidence — recommendation quality must be lowered.

## Validation Result

- Methodology check: PASS — agents, schemas, and artifacts are all wired correctly.
- Trade-readiness check: FAIL — insufficient live data for capital deployment.
- Stop-rule decision: do **not** escalate to `HALTED` because the run is explicitly an `ILLUSTRATIVE_MODE` dry run; instead set `REVIEW_ONLY` per `eval/stop_criteria.md` §Review-Only Mode item 1 (stale/delayed data, methodology valid).
- Recommended run status: **`REVIEW_ONLY`**.

## Handoff to Data & Regime Agent

Proceed to regime classification under `ILLUSTRATIVE_MODE`. Disable any `HIGH` confidence labels for the entire run. Cap final output's per-name confidence at `LOW`.
