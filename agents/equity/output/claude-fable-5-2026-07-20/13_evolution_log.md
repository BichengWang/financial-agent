# 13 Evolution Log — 2026-07-20 (claude-fable-5, intraday run)

Per rules.md §Mutation Logging Standard. One proposed change this run (Track A), tested and **rejected**; `NO_CHANGE_ACCEPTED`.

## Run Context

- Date/status: 2026-07-20, NO_TRADE (15th consecutive scoring run on the family-coverage gate); regime NEUTRAL with HIGH_VOL watch; first intraday (12:21 ET) full-pipeline fire.
- Evaluation window: trailing 7 calendar days, all models — gpt-5 07-13..07-17, claude-fable-5 07-13..07-17, claude-haiku-4.5 07-16, gemini-3.5-flash 07-13.
- Ledger status: canonical settlement ledger healthy — 68 settled this run (largest batch), 175 EQ + 30 MF canonical, 0 conflicts, due 0. Source Ledger 325 rows, 0 UNAVAILABLE Required rows.
- Baseline flag: BASELINE_WINDOW_GAP (02 §2).
- **Priority override ACTIVE:** weighted rank IC −0.049 ≤ 0 over ≥20 settled → today's proposal must address calibration (sigma sourcing, mu table, or score weighting).

## What Worked / What Failed (forecast vs realized, cross-model)

- Worked: the weekend/intraday settlement-timing conventions composed exactly as codified — 68 due keys (three weekend vintages + one same-day-target vintage) settled at the 07-17 close with WEEKEND_TARGET/TARGET_EQ_RUN_DATE flags, zero conflicts against prior packages.
- Worked: Nasdaq-bulk-primary fetch chain (07-13 Track B) delivered 518/519 names in 161s on its third consecutive session as primary; Yahoo remains 429-blocked (probe 0/6).
- Worked: two-pass bounded earnings preflight caught 12 in-window names including second-pass entrants AAPL/WST; the rank-floor rule handled ABBV's penalty demotion cleanly (band-floor precedent held).
- **Failed: core-ETF forecasting.** Today's 12 MF settlements went 0/12 on direction; canonical MF accuracy is 20.0% over n=30 with mean z −0.77 — now past the 20-record Track A evidence bar. Every June vintage forecast upside (mus +0.5%..+7.3%) into a tape that finished lower.
- Failed/watch: equity hit rate decayed 55.5% → 51.4% on today's batch; the batch is four republished copies of one June basket (02 §0 concentration note), so the decay is one basket's miss weighted four times — a measurement artifact worth structural attention, not a new signal.
- Cross-model divergence: none material — both 07-17 packages (gpt-5 pre-open, claude at-close) reached NO_TRADE on the same gate with agreeing regime calls; no other model has run since.

## Primary Diagnosis

**Factor calibration** — specifically the Core ETF Market Forecast mu prior. The regime-prior table emits positive mu in NEUTRAL (+0.5% SPY, beta-scaled for QQQ/SOXX up to +7% in bullish spring regimes) and has now been wrong on direction 24 of 30 times, with realized returns averaging 0.77σ below forecast. Equity-side calibration is comparatively healthy (CI 77.1%, mean z −0.24).

## Exactly One Proposed Change — Track A (performance: Core ETF mu prior), tested

**Proposal:** add a calibration-feedback rule to the Core ETF mu derivation: when trailing settled MF mean z < −0.5 over ≥20 canonical records, apply a default −0.5pp adjustment (inside the existing ±1.0/±1.5pp bands) to the regime-prior mu until mean z recovers above −0.5.

**Hypothesis:** a bounded systematic shrink converts persistent overshoot into improved direction accuracy and magnitude error without touching the protected prior table itself.

**Validation (disclosed holdout):** canonical MF records split chronologically — TRAIN = vintages ≤ 2026-06-18 (n=15), TEST = vintages > 2026-06-18 (n=15, includes today's 12 settlements; settlement_manifest.json):

| Slice | Baseline hit (scored) | Shrunk −0.5pp hit | Baseline mean z | Shrunk mean z |
|---|---|---|---|---|
| TRAIN (n=15) | 33.3% (15) | 28.6% (14; 1 → FLAT abstention) | −0.576 | −0.505 |
| TEST (n=15) | 6.7% (15) | 6.7% (15) | −0.968 | −0.898 |

**Decision: REJECT.** The acceptance standard (OOS hit rate +2pp, or IR +0.05, without drawdown/turnover harm) is not met: OOS hit rate is unchanged (6.7% → 6.7%), train-slice hit rate worsens, and the mean-z gain (~0.07σ) is cosmetic. The failure is **directional, not magnitudinal** — most settled mus sit far above the 0.5% FLAT threshold, so any within-band uniform shrink flips almost no calls; shrinks large enough to matter simply convert forecasts into `N/A - FLAT_CALL` abstentions, which the standard cannot score and which would be evidence-avoidance, not calibration. `NO_CHANGE_ACCEPTED`.

**Escalation (queued for 2026-07-31 structural review, human review required):** the miss driver is the regime-prior *sign* — BULL/NEUTRAL priors kept emitting positive beta-scaled mu through a topping tape. Fixing that means revisiting the regime→prior mapping or adding a trend-conditioned prior (e.g., price-below-both-MAs ⇒ shift one regime row down), which touches the protected prior table beyond a daily bounded change. n=30 of evidence now exists to design that test properly.

## Standing Items (not new proposals)

- **Fundamental/Sentiment unwiring — 15th consecutive run**; Phase-2 bulk fetch (full-universe `companyfacts.zip` + threaded Nasdaq sentiment) remains the binding constraint on ever publishing GO (plan: agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md).
- Weekend-republication evidence concentration (four identical vintages settled today) — queued for structural review alongside the MF item (02 §6).
- Operational note for the runbook keeper: `settlement_ledger.py` defaults `as_of` to the max package run_date — a Monday run over a quiet weekend must pass `--as-of {run_date}` explicitly or due weekend-target inventory is invisible (observed and corrected this run; documentation-only note, no rule change proposed under the one-change limit).
- Freeze criteria: not met (accepted changes on 07-16 and 07-17; today's REJECT is the first of its cycle; no oscillation).
