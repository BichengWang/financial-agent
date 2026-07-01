# 16 Monthly Structural Review — June 2026

Run `claude-opus-4-8` · 2026-06-30 (last trading day of June). Structural review per `runbook.md § Cadence` (month-end). Broader scope than the daily evolution pass; protected rules still bind.

## Month in Review

| Dimension | Observation |
|---|---|
| Run cadence | Daily pre-open runs ran (predominantly `gpt-5`; `gemini-3.5-flash` and `claude-*` sporadic). 17 prediction ledgers exist; the system matured to a stable LIVE-data pipeline mid-month. |
| Status distribution | **Persistent NO_TRADE.** `gpt-5` published NO_TRADE every session 06-11 → 06-30 (one off-cycle REVIEW_ONLY). This run (claude-opus-4-8) = NO_TRADE. ~16 consecutive cross-model NO_TRADE. |
| Regime arc | Early/mid-June: AI/semis melt-up (SOXX +87% / MU +213% / AMD +165% on 60d momentum into 06-30). Late June: sharp **rotation** out of mega-cap software (MSFT/NOW/PLTR/NFLX/META −12% to −25% MoM) into healthcare, financials, industrials, and memory. Index-level vol stayed low (~15%) while single-stock dispersion was extreme. |
| Settlements | **Zero.** All 290 logged predictions remain OPEN; every ledger used target ≈ run+28d and the first batch matures 2026-07-08. The calibration engine has produced no realized score in its entire history. |

## Structural Issues (priority order)

1. **Beta-band feasibility dead-state (CRITICAL, recurring).** The 0.90–1.10 portfolio beta band, measured on 60d realized betas, is structurally unreachable for the investable-grade quality cohort under the 5% single-name cap whenever leadership is low-beta (the defining feature of June's rotation). Result: valid, grounded, positive-alpha forecasts that can never be sized. Flagged in ≥4 consecutive daily evolution logs and (until today) dismissed as "no change needed." **Escalated to HUMAN_REVIEW this run (13).** This is the single most important structural item.
2. **Calibration evidence starvation (HIGH).** 0 settled predictions → no hit-rate, CI-coverage, mean-z, or rank-IC. No Track A parameter change is legitimate until ≥ 20 settle. First wave ~2026-07-08; the monthly review should re-run with real settlement data in late July.
3. **Proxy factor families (MEDIUM).** Fundamental and Sentiment are price-derived proxies in every run (no fundamentals/short-interest/options/analyst feed wired), forcing DQ ≤ 0.80, confidence ≤ MEDIUM, and cross-family momentum overlap. Wiring even one real fundamental feed (EPS-revision breadth) and one positioning feed (options IV percentile, available via the IBKR snapshot field set) would materially raise data quality and de-correlate the families.
4. **Cap-reading ambiguity (MEDIUM).** The 5% single-name cap vs a 5–10-name 100% sleeve remains un-canonized (sleeve-relative needs ≥20 names; NAV-relative implies ~40% invested + cash and sub-band beta). Flagged since the 05-30 baseline; still unresolved. Needs a human ruling.

## Cross-Model Notes

Models agree on the mechanism (all diagnose `portfolio construction` / beta feasibility) and on the regime direction. No divergence in regime calls over the window — the disagreement is only in universe breadth and how each handles proxy families. The consistency across `gpt-5`, `gemini`, and `claude` strengthens the conclusion that the blocker is **systemic (rules/constraints), not model-specific**.

## Recommendations for Human Review

1. **Rule on the beta band measurement window** — 60d realized beta vs a blended 60d/252d (the latter would place June's quality leaders nearer 0.8–1.0 and likely unlock compliant books). Protected rule → humans only.
2. **Canonize the single-name-cap reading** for a 5–10-name focused sleeve.
3. **Wire one fundamental + one positioning feed** to retire the proxy families.
4. **Re-convene this review ~2026-07-31** with the first month of settled predictions; only then re-open Track A calibration.

No autonomous parameter mutation is taken (Freeze Criteria #1 in effect, 13). Protected rules unchanged.
