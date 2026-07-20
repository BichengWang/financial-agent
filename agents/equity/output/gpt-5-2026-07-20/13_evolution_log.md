# 13 Evolution Log — 2026-07-20

## Run context

- Status/regime: NO_TRADE / NEUTRAL with HIGH_VOL semiconductor watch.
- Window: all 11 dated packages from 2026-07-13 through 2026-07-20: claude-fable-5-2026-07-13, claude-fable-5-2026-07-14, claude-fable-5-2026-07-15, claude-fable-5-2026-07-17, claude-haiku-4-5-2026-07-16, gemini-3.5-flash-2026-07-13, gpt-5-2026-07-13, gpt-5-2026-07-14, gpt-5-2026-07-15, gpt-5-2026-07-17, gpt-5-2026-07-20.
- Canonical ledger: 175 equity + 30 market; due 0; conflicts 0.
- Calibration: equity hit 51.43%, CI 77.14%, mean z -0.2363, weighted rank IC -0.048856.
- Baseline: exact same-model 2026-06-22; `NO_PRIOR_BASELINE=false`, `CROSS_MODEL_BASELINE=false`, `BASELINE_WINDOW_GAP=false`, `NO_VALID_MOM_BASELINE=false`.

## What worked / failed

The timing rules absorbed 51 weekend and 17 same-day targets without intraday contamination or conflicts. CI coverage remains healthy, so sigma scaling is not the main problem. Score ordering remains weak: CAT/GOOGL missed while lower-ranked financial/health names outperformed, and weighted rank IC remains non-positive. Cross-model runs continue to agree on NO_TRADE because production Fundamental/Sentiment coverage is absent.

## Primary diagnosis

**FACTOR_CALIBRATION.** Technical momentum dominates the sourceable composite while Macro is its only balancing family.

## Exactly one proposal — Track A

**Proposal:** reduce Technical weight 0.30→0.25 and increase Macro 0.15→0.20, leaving Fundamental 0.30 and Sentiment 0.25 reserved and every protected rule unchanged.

**Hypothesis:** modestly greater drawdown/volatility/beta-fit weight should reduce momentum-chase reversals and improve rank IC.

**Validation:** the ≥20 settlement floor is met, but older packages do not provide a schema-consistent full-universe replay: sampled vintages used different factor inputs and some prediction records lack comparable components. A valid holdout IR/hit-rate/drawdown/turnover comparison cannot be claimed from settlement rows alone.

**Decision: DEFER — NO_CHANGE_ACCEPTED.** The proposal is not adopted. Next step is a schema-consistent current-feature replay; weights and confidence rules remain unchanged.
