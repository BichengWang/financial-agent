# 13 Evolution Log — 2026-07-12

## Run Context

| Field | Value |
|---|---|
| Date / Status / Regime | 2026-07-12 / REVIEW_ONLY (weekend) / NEUTRAL |
| Evaluation window | Trailing 7 days: claude-fable-5 07-05..07-12 (07-10/07-11 partial), gpt-5 07-05..07-11 — all models, all packages |
| Ledger status | 20 settled this run → cumulative EQUITY_ALPHA n=46 + 3 MARKET_FORECAST; 41 ledgers scanned |
| Baseline flag | SAME_MODEL_BASELINE (claude-fable-5-2026-06-10) |

## What Worked

1. **The composite score ranks realized alpha.** The rank-IC re-test flagged by the last three logs resolved decisively: vintage IC +0.554 (gpt-5 06-14, n=17), cumulative weighted IC **+0.200 at n=46** — two consecutive strongly-positive vintages, with the lone negative one (-0.51) being the 06-10 sampled-30-name run. The §Priority Override and MEDIUM-freeze trigger conditions no longer hold; this is a **data-driven trigger reversal, not a rule change** (no mutation required or made).
2. **Zero-failure two-source fetch** recovered from 07-11's Yahoo throttling without fallbacks (521/521 + 0.0000% Nasdaq divergence).
3. **Healthcare carry-forward discipline**: LLY/ABBV/UNH produced their third consecutive settled HITs each; ANET's PROMOTE (07-09) settled +12.75% today.

## What Failed / Weak Spots

1. **Cadence-estimated earnings dates were materially wrong where it counts.** Confirmed Nasdaq dates fetched this run vs the prior ±5d estimates: GE est ~07-22 → confirmed **07-16** (the estimate would have under-penalized a 4d-out print by a week); FFIV est ~18d (penalized) → confirmed 07-27 = **15d, outside the window** (over-penalized); the banks wave is confirmed 07-14..07-17. Estimation error directly moves the -0.10 penalty and therefore ranks, mu bands, and published composition.
2. **REIT sigma calibration**: the only two OUT_CI settlements in the vintage are both REITs breaking low (AMT z -1.38, PLD z -1.20). n=2 — watch item, not actionable; re-examine if DOC (rank 9 today) or further REIT settlements break the same way.
3. **Session reliability**: two consecutive truncated claude sessions (07-10, 07-11) left partial packages and a missed Friday weekly review — an operational failure mode outside prompt-mutation scope; partials committed with this run.

## Primary Diagnosis

**Data quality** (earnings-date estimation error) — the one miss category this run's evidence isolates cleanly.

## Proposed Change (exactly one)

- **Classification: Track B (process/data-sourcing change — no scoring math altered).**
- **Problem statement:** 05 penalty rolls in the 07-04..07-11 packages used `prior_report_date + ~91d` cadence estimates (±5d) for shortlist earnings dates; today's confirmed-date fetch shows estimate errors up to 6 days on names where the ≤14d penalty window flips (GE, FFIV documented above; artifact: this package's 04 §Earnings Penalty Roll vs claude-fable-5-2026-07-09/05 §7).
- **Change:** adopt the confirmed-dates fetch as the standard preflight step — after the shortlist forms, fetch `api.nasdaq.com/api/analyst/{sym}/earnings-date` for shortlist + carry-forward names; use confirmed dates with the plain ≤14d window; fall back to the cadence estimate (±5d, buffered ≤19d window) only when the vendor field is empty (as DAL today).
- **Hypothesis:** confirmed dates eliminate window-flip misclassification (2 documented today out of ~60 shortlist names), tightening the earnings penalty's precision with zero change to scoring math.
- **Validation (Track B three-condition standard):** (1) explicit problem statement above citing the exposing artifacts; (2) weakens no protected rule or grounding gate — it strengthens the earnings-date Required input from INFERRED to OBSERVED; (3) logged here with **HUMAN_REVIEW** flag; effective next run unless reverted.
- **Decision: ACCEPT** (Track B; one change this run).

## Standing Items (not new proposals)

- **Fundamental/Sentiment feed unwiring** — 10th consecutive run; the standing Track B escalation for a human decision on wiring a fundamentals/sentiment source (or formally accepting a permanent 2-family system) remains **pending HUMAN_REVIEW** (first raised 07-01).
- Track A calibration changes: none proposed — CI coverage 78.3% and mean z -0.148 are in band; the mu table's fresh n=17 evidence is consistent with current bands (vintage mean z -0.028). Freeze criteria not triggered (no rejected-for-lack-of-evidence streak; no accepted-change regressions).

## Effective Next Step

Monday 2026-07-13 run: apply the confirmed-dates preflight step; re-evaluate UNH/GE after 07-16 prints; track DOC against the REIT calibration flag; second-settlement watch on LIN.
