# 13 Evolution Log — 2026-07-27

## Run Context

| Field | Value |
|---|---|
| Run / model | 2026-07-27 / `gpt-5` |
| Status / regime | `NO_TRADE` / `NEUTRAL` |
| Evaluation window | all dated packages 2026-07-20 through 2026-07-27, all models |
| Ledger | EQ n=231, eff_n=1; MF n=42, eff_n=1; due 0; conflicts 0 |
| Baseline | `gpt-5-2026-06-29`, same-model exact target |
| Track A eligibility | blocked: `INSUFFICIENT_EFFECTIVE_N` |

## Review Window

The window includes every gpt-5, claude-fable-5, claude-sonnet-5, and claude-opus-5 package dated July 20–27. Every package published `NO_TRADE`; cross-model divergence is not material to the root blocker. The 2026-07-26 package supplied the adjusted-close rule carried forward today.

## What Worked

1. **TARGET_EQ_RUN_DATE settlement worked at scale.** Thirty-four keys across two vintages settled at the completed 2026-07-24 close before Monday's open; due inventory and conflicts are both zero.
2. **Grounding was broadened.** All 41 settlement/new-forecast symbols, not only the settlement set, received three-source current-run verification and passed the 1% gate.
3. **Adjusted/unadjusted separation reproduced deterministically.** Fresh histories matched 514/514 execution closes and 517/517 comparable technical packs.
4. **The effective-N gate correctly rejected duplicate evidence.** Two field-identical model vintages add 34 canonical keys but no independent target window; eff_n remains 1.

## What Failed

1. Equity rank ordering remains inverted: both newly settled equity vintages have rank IC −0.5912; pooled weighted rank IC deteriorates to −0.1843.
2. Market-forecast direction remains poorly calibrated: 23.81% hit rate and mean z −0.6640 over n=42.
3. The vendor-empty earnings signature rule treats flat, high-volume sessions as earnings prints, routing EQR and PKG to the less-conservative unpenalized branch.
4. Fund_Z and Sent_Z remain unavailable at production coverage, preserving the structural NO_TRADE state.

## Primary Diagnosis

**Source grounding:** vendor-empty earnings inference is too permissive. It affects a Required input and can remove an event-risk penalty on weak evidence.

## Proposed Change — Track B

> For a vendor-empty earnings response, classify a recent session as a print only when either (a) absolute one-day price move is at least 3.5%, or (b) volume is at least 1.8× its trailing median **and** the absolute move is at least 1.5%. Otherwise use the conservative `ESTIMATED_PRINT_WEEK (±5d)` branch.

### Problem evidence

The standing rule is `move ≥3.5% OR volume ≥1.8×`. Current-run audit L148 shows:

| Name | 1d move | Volume ratio | Old result | New result |
|---|---:|---:|---|---|
| EQR | 0.01% | 1.97× | cadence +91d, no penalty | print-week, penalized |
| PKG | 0.01% | 2.13× | cadence +91d, no penalty | print-week, penalized |
| WRB | 2.45% | 2.00× | cadence +91d | cadence +91d |
| CB | 2.46% | 1.96× | cadence +91d | cadence +91d |

Across the 19 vendor-empty scoring-pass names, the new rule changes only EQR and PKG; all 16 other cadence classifications remain cadence, and HIG remains print-week. The change therefore removes two demonstrated volume-only false positives without broadly reclassifying the sleeve.

### Track B acceptance standard

1. **Explicit artifact-backed problem:** satisfied by L148 and today's `earnings_calendar_manifest.json`.
2. **No protected rule or grounding gate weakened:** satisfied. The change is strictly more conservative and touches no factor weight, mu/sigma rule, or portfolio limit.
3. **Logged with `HUMAN_REVIEW`, effective next run:** satisfied.

### Decision

**`ACCEPT` — Track B, `HUMAN_REVIEW`, effective 2026-07-28.** Today's scoring remains on the standing rule because evolution runs after publication; EQR and PKG are disclosed as weakly grounded monitor forecasts.

## Track A Observations — Deferred

- Rank inversion needs an ordering-level test, not a uniform mu shrink or sigma widening. `eff_n = 1` forces `DEFER`.
- The ETF `mu = beta × SPY_mu` category error remains diagnosed. `eff_n = 1` forces `DEFER`.
- CI coverage is healthy; no sigma change is indicated.

## Freeze Check

No freeze criterion fires: recent Track B changes have been accepted, there are not two accepted performance changes worsening out of sample, and weights are not oscillating. Track A remains evidence-gated rather than globally frozen.

## Mutation Log

| Field | Value |
|---|---|
| Problem | volume-only earnings signatures can falsely remove the 14-day event penalty |
| Change | require ≥3.5% move, or ≥1.8× volume together with ≥1.5% move |
| Validation | replay on 19 vendor-empty scoring-pass names; only EQR and PKG change, both demonstrated flat-tape false positives |
| Result | 2 false-positive cadence classifications become conservative print-week estimates; 17 other classifications unchanged |
| Decision | `ACCEPT`, Track B, `HUMAN_REVIEW` |
| Effective | next run, 2026-07-28 |
