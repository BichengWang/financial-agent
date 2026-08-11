# 08 — Risk Review

## Decision: `NO_TRADE`

Process integrity is intact, so `HALTED` is not warranted. All Required inputs pass, so
`REVIEW_ONLY` for stale or partial data is not warranted. The correct outcome is `NO_TRADE`:
valid inputs, but no evidence-complete candidate set and a monitor diagnostic that breaches
protected portfolio caps.

| Review | Evidence | Result |
| --- | --- | --- |
| Price/target lineage | 23/23 entries cross-verified; targets and CIs formula-derived | PASS |
| Sigma lineage | REALIZED_VOL_30D from 30 adjusted returns for every prediction | PASS |
| Score attribution | All family z, DQ, penalties and drivers persisted | PASS |
| Metric ledger coverage | 136 rows cover all displayed inputs and outputs | PASS |
| Kelly handling | 5% cap would bind for 20/20; no sizing published | PASS |
| Technical lineage | deterministic helper, adjusted tree, D/W/M values persisted | PASS |
| Source Ledger completeness | No downstream fact introduced without row | PASS |
| GO-blocking discipline | Required inputs pass; evidence/protected caps cause NO_TRADE | PASS |
| Prediction completeness | 20 equity + 3 ETF OPEN records; 200 settlements | PASS |
| Canonical settlement state | 951 canonical; due 0; conflicts 0; rejected 87 | PASS |
| Factor breadth | 2/4 available versus >=3 required | FAIL -> NO_TRADE |
| Max family share | 66.67% versus <=50% | FAIL -> NO_TRADE |
| Data completeness | 0.80 versus >=0.85 | FAIL -> NO_TRADE |
| Sector cap | 35% Consumer Discretionary versus 30% | FAIL -> NO_TRADE |
| Drawdown cap | 9.22% versus 8% | FAIL -> NO_TRADE |

## Stop-criteria review

- Hard halt: none triggered.
- `NO_TRADE` #1: triggered — zero names pass the investable threshold.
- `NO_TRADE` #4: not triggered — one top-20 name has earnings inside 14 days.
- `NO_TRADE` #5: triggered — diagnostic drawdown 9.22% > 8%.
- `NO_TRADE` #6: triggered — diagnostic sector share 35% > 30%.
- Correlation cap passes and the protected beta band is attainable in the >=80th-percentile
  pool, but those facts cannot cure the factor-family failures.

## Required revision outcome

One composition revision would be irrelevant because no name clears the upstream evidence
gate. Risk returns the package to the orchestrator with `NO_TRADE`, 23 complete forecast
records, and no weights.
