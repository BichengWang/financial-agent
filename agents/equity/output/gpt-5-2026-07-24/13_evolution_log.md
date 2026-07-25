# 13 Evolution Log — 2026-07-24

## Run context

- Status: NO_TRADE
- Regime: NEUTRAL (high-volatility semiconductor watch)
- Review window: all 7 dated packages from the seven calendar dates 2026-07-18 through 2026-07-24 across claude-fable-5, claude-sonnet-5, gpt-5
- Ledger status: 189 equity + 33 market canonical settlements; due=0; conflicts=0
- Baseline flag: none (`gpt-5-2026-06-24` selected by the documented earlier-date tie-break)

## Observe

No new forecast matured today. Rolling equity hit/CI/mean-z remain 52.91% / 76.19% / -0.2129, and weighted rank IC remains -0.093914. Market direction/CI remain 21.21% / 63.64%. Recent packages consistently identify the same structural production gap: Fundamental/Sentiment are unpromoted, while Technical leadership alone cannot authorize trades.

## Diagnose

Primary diagnosis: **FACTOR_CALIBRATION**. The mandatory priority trigger is non-positive rank IC over >=20 equity settlements. The latest admitted 2026-06-24 vintage is sharply inverted, so the live question is score ordering rather than merely forecast magnitude.

## Hypothesis — Track A

Proposal: shift 0.05 weight from Technical (0.30 -> 0.25) to Macro (0.15 -> 0.20), leaving Fundamental at 0.30, Sentiment at 0.25, and every protected risk limit unchanged. Hypothesis: less momentum concentration and greater downside-risk/beta-fit weight would reduce rank-order inversion.

## Validation

- Evidence base: 189 canonical equity settlements; sufficient count for Track A, with the 2026-06-24 vintage rank IC negative in the canonical manifest.
- Expected effect: rankings can change because Tech_Z and Macro_Z differ cross-sectionally, so IR, rank IC, turnover, and drawdown all require replay rather than assumption.
- Missing acceptance evidence: no schema-consistent holdout recomputation shows Information Ratio improvement >=0.05 or hit-rate improvement >=2pp without worse drawdown and turnover.
- No new matured predictions arrived today to form an independent holdout slice.

## Decision

**DEFER — NO_CHANGE_ACCEPTED.** The proposal is responsive to score ordering but does not satisfy the Track A acceptance standard. The mu table, family weights, thresholds, confidence rules, and protected limits remain unchanged.

Freeze criteria were assessed and are **not triggered**. The July 21 Sortino-computation correction and July 22 settlement-timing clarification are recent accepted Track B changes, breaking any all-change rejection streak. The present run applies both the trailing-30-day downside-deviation convention and the canonical settlement validator. No accepted-change deterioration or parameter oscillation is present.

## Effective next step

Keep collecting settleable forecasts. Before reconsidering acceptance, run a locked holdout replay of the 0.25 Technical / 0.20 Macro proposal and report IR, hit rate, rank IC, CI coverage, drawdown, and turnover deltas. Evidence: L333,L336.
