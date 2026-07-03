# 14 Weekly Review — week ending 2026-07-03 (published on the holiday per runbook §Cadence)

Owner: Evolution Agent. Scope: parameter review over all models' packages, 2026-06-29 → 2026-07-03.

## Week in Summary

| Day | Sessions/runs | Statuses | Market |
|---|---|---|---|
| Mon 6/29 | gpt-5, gemini | NO_TRADE | Drift higher, calm |
| Tue 6/30 | gpt-5, opus-4-8 (month-end reviews) | NO_TRADE | NEUTRAL consensus; sampled-universe era ends (fix #286 merges) |
| Wed 7/1 | gpt-5, fable (first full index-union run) | NO_TRADE | **Unwind day 1**: SOXX −6.41%, MU −10.57% vs SPY −0.14% |
| Thu 7/2 | gpt-5, fable (intraday LIVE) | NO_TRADE | **Unwind day 2**: SOXX −5.57% (−7.19% low), dip-bought into the pre-holiday close; VIX fell to 16.15 |
| Fri 7/3 | gpt-5, fable (holiday runs) | REVIEW_ONLY | Market closed |

Regime: NEUTRAL all week, every model — correct at the index level (SPY never lost its MA50, VIX peaked ~17) while the AI-capex complex de-grossed violently underneath (SOXX −11.6% in two sessions; QQQ rvol30 doubled to ~29%). The week's factual verdict on the June-10 thesis family: defensive-healthcare leg validated (DVA/HUM/ABBV/LLY), staples/energy legs failed (COST/WMT/CVX/XOM), and the MU exhaustion call was right three weeks early.

## Parameter Review (the actual mandate)

1. **Factor weights (0.30/0.30/0.25/0.15)** — no change proposed or permitted: Track A requires ≥20 settled predictions; the system has **0 settled** (first settlements 2026-07-08). Weights unchanged since inception.
2. **mu Calibration Table** — untouched (evolution-agent-only, Track A locked). One enforcement fix shipped this week (07-02): total per-name adjustment is now clamped at ±2pp after the 07-01 UNH record stacked −3pp. This is compliance with the existing table, not a table change. Clamp held its first live test today.
3. **Sigma sourcing** — REALIZED_VOL_30D functioning across 513-514 names; no IV feed exists to prefer. Watch item: 30d realized vol is rising fast in the growth complex; if CI coverage comes in below 55% when settlements accumulate, the mandated first fix is wider sigma sourcing (rules §Rolling Calibration).
4. **Confidence calibration** — LOW-everywhere is currently forced by family coverage (2/4). No labels to calibrate until the family question resolves.
5. **Universe protocol** — the index-union path (fix #286) ran three consecutive fable runs cleanly (515 → 513/514 eligible); the sampled-set era's distortion is documented (leaderboard overlap with gpt-5's 34-name sample remains low). SATS demonstrated the freshness screen works in both directions (excluded 07-01/02, re-admitted 07-03).
6. **Open mandatory item** — the family-coverage/evidence-threshold spec inconsistency: three consecutive evolution-log flags, drafted Track B amendment pending **HUMAN_REVIEW**. This is the single decision blocking any path back to GO-eligibility. Recommendation to the operator: adjudicate before 2026-07-08 so the first settled-evidence week starts on a resolved spec.

## Freeze Check (rules §Freeze Criteria)

Not triggered: no accepted changes have worsened performance (none accepted); rejections have not been for lack of evidence (DEFER-pending-human ≠ evidence-lack rejection); no oscillation. Parameter mutation remains de facto frozen by the 0-settled state.

## Next Week

Mon 7/6 normal run; **Wed 7/8 first settlement pass** (12 records, 2026-06-10 vintage — alpha-based scoring vs recorded SPY 728.31); Fri 7/10 next weekly review with, for the first time, realized calibration metrics on the table. Earnings season opens ~7/9 (DAL); bank wave 7/14-17 — expect the ≤19d penalty set to grow and churn the top-20.
