# 13 — Evolution Log · 2026-08-28

| Context | Value |
|---|---|
| Status / regime | NO_TRADE / BULL |
| Evaluation window | 28 days, target 2026-09-25 |
| Ledger | EQ n=1355, eff_n=2; MF n=201, eff_n=2 |
| Baseline | `agents/equity/output/gpt-5-2026-07-30` — CROSS_MODEL_BASELINE |
| Primary diagnosis | **factor calibration** |

## What worked / failed

The corporate-action process accepted August 22 worked: both EQR keys are visible and remain due
without an inferred successor ratio. The strengthened CNBC identity concept accepted August 27 is
validated by the EQR foreign-symbol hazard. What failed is score ordering: weighted rank IC is
-0.0495, equity hit rate 37.49%, and mean z
-0.5553.

## Exactly one proposed change

**Track A — recalibrate factor weights against canonical forward alpha.** Hypothesis: reducing the
Technical contribution and estimating constrained non-negative family weights on chronological
settled holdouts will raise out-of-sample rank IC above zero without worsening hit rate, maximum
drawdown, turnover or information ratio.

Validation design once eligible: n≥20 **and** eff_n≥3; expanding-window chronological fit with the
latest non-overlapping window held out; compare rank IC, hit-rate delta, IR delta, drawdown delta
and turnover delta against the frozen 30/30/25/15 baseline. Acceptance requires positive holdout
rank IC, non-negative hit-rate and IR deltas, no drawdown deterioration beyond 1pp, and turnover
increase ≤10pp.

## Decision

**DEFER / NO_CHANGE_ACCEPTED.** Raw n passes, but equity eff_n=2 <3. The manifest
projects the next independent equity window on
2026-09-03. No parameter, threshold or risk limit changes.

Effective next step: keep the current model frozen; run the pre-registered holdout comparison only
after the independent-window gate opens.
