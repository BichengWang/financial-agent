# 13 Evolution Log — 2026-07-21

## Run context

- Status: NO_TRADE
- Regime: NEUTRAL (high-volatility semiconductor watch)
- Review window: all 9 dated packages from the seven calendar dates 2026-07-15 through 2026-07-21 across gpt-5, claude-fable-5, and claude-haiku-4-5
- Ledger status: 175 equity + 30 market canonical settlements; no due keys; no conflicts
- Baseline flag: none (`gpt-5-2026-06-22` selected)

## Observe

No new forecast matured today. Rolling equity hit/CI/mean-z remain 51.43% / 77.14% / -0.2363, and weighted rank IC remains -0.048856. Market direction/CI remain 20.00% / 60.00%. Recent packages consistently identify the same structural production gap: Fundamental/Sentiment are unpromoted, while Technical leadership alone cannot authorize trades.

## Diagnose

Primary diagnosis: **FACTOR_CALIBRATION**. The mandatory priority trigger is non-positive rank IC over >=20 equity settlements. This is distinct from the July 20 deferred family-weight proposal: today's question is whether forecast-return priors are too aggressive at the top bands, not whether an unavailable family should receive more weight.

## Hypothesis — Track A

Proposal: reduce the >=95th-percentile equity mu prior from +6% to +5% and the 90–95th band from +5% to +4%, leaving lower bands and all protected risk limits unchanged. Hypothesis: smaller top-band priors would move mean z toward zero without changing rank ordering or turnover.

## Validation

- Evidence base: 175 canonical equity settlements; sufficient count for Track A.
- Expected mechanical effect: hit rate and rank IC are unchanged because signs/ranks do not change; turnover and drawdown are unchanged in this NO_TRADE paper sleeve.
- Missing acceptance evidence: no disclosed holdout recomputation shows Information Ratio improvement >=0.05 or hit-rate improvement >=2pp without worse drawdown.
- No new matured predictions arrived today to form an independent holdout slice.

## Decision

**DEFER — NO_CHANGE_ACCEPTED.** The proposal addresses the calibration trigger but does not satisfy the Track A acceptance standard. The mu table, family weights, thresholds, confidence rules, and protected limits remain unchanged.

Freeze criteria were assessed and are **not triggered**. The newly available claude-fable-5 2026-07-21 cycle accepted a Track B Sortino-computation correction, breaking any all-change rejection streak; the present run applies the same trailing-30-day downside-deviation convention. No accepted-change deterioration or parameter oscillation is present.

## Effective next step

Keep collecting settleable forecasts. On the next independent maturity cohort, run a locked counterfactual replay of the two top mu bands and report IR, hit rate, CI coverage, mean z, drawdown, and turnover deltas before reconsidering acceptance. Evidence: L297,L300.
