# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-09 (Thursday — live session; afternoon publication ~14:45 ET) |
| Status | NO_TRADE |
| Regime | NEUTRAL |
| Evaluation window | 2026-07-02 → 2026-07-09, all models |
| Ledger status | **17 settled this run (second pass; first cross-model)**; cumulative 29 settled; 702 prior OPEN + 26 published this run; next due **2026-07-12 (20 records) → n=49** |
| Baseline flag | SAME_MODEL_BASELINE |

## Window Review (cross-model, trailing 7 days)

- Packages: gpt-5 (07-02..07-08 daily), gemini-3.5-flash (07-06), claude-sonnet-5 (07-02, 07-03), claude-fable-5 (07-02..07-08, this run). Statuses: NO_TRADE on all completed trading-day scoring runs; REVIEW_ONLY on the 07-03..07-05 closed days. Audit trail unbroken.
- **Cross-model settled evidence (new today)**: the gpt-5 2026-06-11 vintage settled 9/17 HIT (52.9%), CI coverage 82.4%, mean z -0.185, **rank IC +0.348** — the opposite ordering sign from the claude-fable-5 06-10 vintage settled yesterday (-0.51, n=12). Same market window, different books: the divergence is model-mix, not regime. Shared systematic error confirmed across both vintages: **energy** (CVX MISS twice, XOM/COP MISS) — every energy record settled negative-alpha while healthcare went 7/8 HIT across vintages.
- **Sigma quality at n=29**: CI coverage 72.4% — essentially on the 70% target; mean z -0.218 (mu mildly optimistic). The sigma machinery is performing; ordering, not calibration width, is the open question.
- **Operational**: the intraday-drift refetch procedure fired for the first time (first fetch 10:47 ET, cross-check at 14:35 ET diverged up to 3.06% → refetch 14:36 ET, final max div 0.121%) — the two-source standard caught exactly the failure mode it exists for. Both fetch passes 521/521.
- Family-coverage gate blocked investability for every completed scoring run in the window (9th consecutive for this model).

## What Worked / What Failed

Worked: cross-model settlement (foreign pre-06-11 ledger schema handled cleanly); two-source verification caught intraday drift before any published price went stale; carry-forward mechanism re-validated (LLY/ABBV settled HIT again in the gpt-5 vintage; ANET promote-by-rank after its +15.3% HIT); DAL event penalty correctly kept a same-day reporter down-ranked rather than excluded on live post-print data.
Failed / degraded: weighted rank IC crossed the ≤0 trigger at n=29 (-0.007) — though per-vintage signs conflict; the standing two-family scoring gap persists; nothing new broke operationally.

## Primary Diagnosis

**Factor calibration**, now with a triggered review obligation: rules.md §Rolling Calibration says rank IC ≤ 0 over ≥ 20 settled → composite not predictive → MEDIUM confidence freeze + calibration-first evolution priority (§Priority Override). The trigger fired on the letter of the rule (-0.007 at n=29). On the substance, the pooled number is a knife-edge average of two conflicting vintages (-0.51 n=12 vs +0.348 n=17) from overlapping calendar windows — evidence of *heterogeneity*, not of a stably non-predictive score. The linked standing diagnosis is unchanged: with only Tech+Macro sourceable, the score is a momentum/low-vol composite (data quality, 9th consecutive run).

## Proposed Change (exactly one — Priority Override routes this to calibration)

**Track A (factor calibration): cap the mu Calibration Table's top band at +5.0% (remove the ≥95th-pctl +6.0% tier) — i.e., shrink the mu prior where the settled evidence shows the most optimism.** Hypothesis: top-band forecasts are systematically too aggressive (cumulative mean z -0.218; yesterday's vintage: the +6% mu names went 1/2 HIT with COST OUT_CI_LOW; today's: the +6% mu names CVX/UNH split 1 HIT/1 hard MISS), so flattening the top of the prior should improve CI coverage symmetry and reduce magnitude error without touching ordering.

Validation (acceptance standard): requires ≥20 settled records — available (29) — **but** a holdout test needs vintages not used to form the hypothesis. Both settled vintages ARE the hypothesis source; no out-of-sample window exists yet (first testable holdout: the 07-12 wave, n+20). Splitting 29 records across two heterogeneous vintages gives no stable OOS IR/hit-rate delta (per-vintage IC signs conflict; mean z is inside the healthy band at -0.218, so the trigger condition itself is marginal).

## Decision

**REJECT — insufficient out-of-sample evidence (NO_CHANGE_ACCEPTED).** The §Priority Override was honored (the one proposal addresses calibration, not the family gate), but the acceptance standard cannot be met with in-sample vintages, and anti-overfitting rules forbid tuning to two adjacent-week vintages. MEDIUM confidence freeze per §Rolling Calibration is **recorded as active** (operationally non-binding — all published names are LOW on the family gate). Freeze-criteria check: this is the 1st consecutive evidence-lack rejection (prior cycles were HUMAN_REVIEW defers, a different category); no mutation freeze.

Standing item (not this run's proposal, noted for continuity): the Track B family-coverage amendment remains pending HUMAN_REVIEW — **9th escalation**. Today's cross-model evidence *weakens* the case for keeping the gate closed on ordering grounds (gpt-5 vintage IC +0.348; pooled hit rate 51.7% ≥ 50%) while yesterday's weakened the case for opening it — the human review should weigh both vintages, not the pooled average.

Effective next step: **2026-07-12 settlement wave (20 records → n=49, three vintages)** — re-test cumulative and per-vintage rank IC; if IC ≤ 0 holds at n=49 across ≥3 vintages, re-propose the mu-table cap with the 07-12 wave as the holdout; if IC turns positive, the trigger clears and the family-coverage human review becomes the sole blocker.
