# 13 Evolution Log — 2026-07-22

## Run context

- Status: NO_TRADE
- Regime: NEUTRAL (high-volatility semiconductor watch)
- Review window: all 10 dated packages from 2026-07-15 through 2026-07-22 across gpt-5, claude-fable-5, and claude-haiku-4-5
- Ledger status: 175 equity + 30 market canonical settlements; 0 newly settled; due=17; conflicts=0
- Baseline flag: none (`gpt-5-2026-06-24` selected)

## Observe

Seventeen forecasts from the 2026-06-24 vintage matured today. Their target-date closes passed the two-source gate, but no rows were admitted because this run's canonical snapshot was frozen with the pre-change validator, which did not recognize same-day post-close evidence. The verified candidates are retained outside the ledger (L327); canonical due inventory remains 17. Rolling equity hit/CI/mean-z remain 51.43% / 77.14% / -0.2363, and weighted rank IC remains -0.048856. Market direction/CI remain 20.00% / 60.00%.

## Diagnose

Primary diagnosis: **SOURCE_GROUNDING**. The pre-change validator used to freeze this run's canonical snapshot rejected every same-day target close even after the market had closed. That conflicted with the timing rule's narrower pre-close prior-day exception and stranded 17 due observations despite explicit completed-close markers and two-source verification.

## Hypothesis — Track B

Proposal: beginning next run, permit a same-day target close only when the settlement row explicitly declares `TARGET_DATE_CLOSE` and has a timezone-aware `settled_at` timestamp on the target date at or after 16:00 America/New_York; continue rejecting unlabeled, timestamp-missing, pre-close, or intraday values. Hypothesis: the narrower timing contract restores valid calibration observations without relaxing price provenance, conflict detection, or risk controls.

## Validation

- Artifact-exposed defect: the published canonical manifest leaves all 17 keys due while `pending_target_close_candidates.json` retains 17 rows whose Nasdaq records say `Closed at Jul 22, 2026 4:00 PM ET` and whose two-source gates passed (L328,L327).
- Protected-rule check: no scoring weight, threshold, confidence rule, turnover limit, or risk cap changes. Unlabeled, timestamp-missing, and pre-close same-day values remain rejected.
- Scope limit: the accepted validator covers regular 16:00 ET sessions. Scheduled early-close keys remain due for target-date historical settlement on the next run until exchange-calendar-aware close timing is separately reviewed.
- Test evidence: 42 focused settlement-ledger tests pass, including post-close acceptance, pre-close and missing-timestamp rejection, and end-to-end manifest plumbing. An isolated counterfactual replay of the 17 pending candidates yields 189 equity + 33 market settlements, due=0, conflicts=0; those figures are validation-only and are not used by this run's reports or forecasts.
- Governance: HUMAN_REVIEW because the correction changes what evidence the canonical calibration ledger admits.

## Decision

**ACCEPT — HUMAN_REVIEW.** Land the narrow `TARGET_DATE_CLOSE` validator correction now, effective next run unless reverted. This run retains the pre-change canonical ledger. The mu table, family weights, thresholds, confidence rules, and protected limits remain unchanged.

Freeze criteria were assessed and are **not triggered**. This correction makes the canonical evidence set agree with the already protected close-timing rules; it does not change model behavior or create parameter oscillation.

## Effective next step

Human-review the timing-contract correction and retain the regression tests. On the next run, re-scan the 17 due keys and settle them against the historical 2026-07-22 close; use the new rule for future same-day post-close runs. Negative weighted rank IC remains the next eligible calibration priority, but any scoring proposal still requires an independent holdout replay before acceptance. Evidence: L329,L332.
