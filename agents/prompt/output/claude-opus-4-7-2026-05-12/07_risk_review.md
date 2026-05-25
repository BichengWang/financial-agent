# 07 Risk Review

## Committee Decision: REJECT (publication path: REVIEW_ONLY, not GO)

The portfolio agent did not propose a portfolio. There is nothing to approve or revise. The committee endorses publishing the run as `REVIEW_ONLY` with no positions, and explicitly rejects any path that promotes the illustrative top-N to a tradeable list.

## Top Three Concerns (Severity Order)

1. **Data integrity is null across factor families.** Fundamental, technical, and sentiment inputs are all `N/A`. Any positive composite score today is structurally unsupported. This alone would also justify `HALTED` for a live run; the only reason `REVIEW_ONLY` is acceptable is the explicit `ILLUSTRATIVE_MODE` framing.
2. **Event-risk concentration cannot be measured.** With no earnings calendar feed, the 14-day-event filter, the >2-name-cluster `NO_TRADE` trigger, and confidence caps for names near earnings cannot be enforced.
3. **Macro/regime label is illustrative.** The `NEUTRAL` regime is a process placeholder, not evidence. Any sizing path keyed off regime would be unfounded.

## Required Fixes (For Future Live Runs)

- Wire a live or end-of-day verified market-data source before promoting any name.
- Connect a vetted earnings calendar with audit lineage.
- Connect at minimum one sentiment/positioning feed (analyst revisions or short interest) before the 4-family check can pass.

## Final Publication Recommendation

**`REVIEW_ONLY`** — methodology valid, evidence insufficient for sizing.

## Handoff to Orchestrator

Publish `08_final_report.md` with `REVIEW_ONLY` status. Do not attach a candidate table that could be misread as actionable; reproduce the schema demonstration only inside an `ILLUSTRATIVE` block with explicit caveats.
