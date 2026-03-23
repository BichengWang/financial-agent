# 02 Regime and Data

## Regime Classification

**Assigned regime:** `NEUTRAL` (illustrative-only, low confidence)

| Signal family | Observation | Tag | Confidence |
|---|---|---|---|
| Index trend | Sideways regime assumption for dry run | ILLUSTRATIVE | Low |
| Volatility | Mid-range VIX assumption | ILLUSTRATIVE | Low |
| Rates | Stable rates assumption | ILLUSTRATIVE | Low |
| Credit stress | No stress assumption | ILLUSTRATIVE | Low |

## Data Integrity View

- Data mode: `ILLUSTRATIVE_MODE`
- Critical missing fields: live prices, verified earnings dates, options positioning, recent revisions.
- Stop-rule decision: do not escalate to `HALTED` because this is a method-valid dry run; set `REVIEW_ONLY`.

## Handoff to Factor Scoring

Proceed with **illustrative ranked table only** to test orchestration and artifact completeness. Any investable labels are disabled for live deployment.
