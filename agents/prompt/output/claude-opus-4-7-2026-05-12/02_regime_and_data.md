# 02 Regime and Data

## Regime Classification

**Assigned regime:** `NEUTRAL` — illustrative-only, low confidence.

| Signal family | Observation | Tag | Confidence |
|---|---|---|---|
| Index trend (SPY vs 20DMA) | Sideways assumption | ILLUSTRATIVE | Low |
| Volatility (VIX band) | Mid-range (15–22) assumption | ILLUSTRATIVE | Low |
| Rates (2Y change / week) | Stable assumption (`|Δ| < 25 bps`) | ILLUSTRATIVE | Low |
| Credit (HY spread) | No widening assumed | ILLUSTRATIVE | Low |
| Sector rotation | No leadership signal computable | N/A | None |

A defensible regime label cannot be supported on real evidence. The `NEUTRAL` label is held only for downstream process testing, not for sizing.

## Data Integrity View

- Data mode: `ILLUSTRATIVE_MODE`.
- Critical missing fields: live prices, verified earnings dates, options positioning, recent revisions, short interest, 13F flows.
- All four hard-stop critical-input domains (price/volume, earnings calendar, factor inputs ≥3-of-4 families, sentiment & positioning) are missing.
- Stop-rule decision: per `eval/stop_criteria.md`, this would qualify as `HALTED` for live deployment, but methodology-valid dry runs are explicitly covered under `REVIEW_ONLY`. Escalation suppressed.

## Regime → Sizing Implication (Reference Only)

| Regime | Sizing | Notes |
|---|---|---|
| NEUTRAL | Baseline 0.25·Kelly cap | Default — but moot under REVIEW_ONLY (no positions). |

## Handoff to Factor Scoring

Proceed with **illustrative ranked table only** to test orchestration and artifact completeness. Do not promote any name to `INVESTABLE`. Cap all confidence labels at `LOW`.
