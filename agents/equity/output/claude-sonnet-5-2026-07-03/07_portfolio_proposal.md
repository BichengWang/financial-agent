# 07 Portfolio Proposal

## Task 0 — Constraint Feasibility Pre-Check

Per `agents.md § Portfolio Construction Agent Prompt` Task 0 (Track B, 2026-06-10, `HUMAN_REVIEW`), the feasibility pre-check runs **before** any sizing is attempted, using already-fetched inputs.

**Result: No portfolio can be drafted.** `05_factor_scores.md § Investable Subset` supplies **zero** investable names — Factor Scoring's own family-count gate (Fundamental and Sentiment/Positioning both `UNAVAILABLE` universe-wide → at most 2 of 4 families sourceable for any name → fails `rules.md § Evidence Thresholds` item 2, "≥3 of 4 factor families non-negative") applies identically to all 30 sampled names, independent of Adj Score. There is no candidate set to size, no beta/sector-share feasibility to check, and no weighting to draft.

This is not a beta-band or sector-cap infeasibility (the kind Task 0 is designed to catch pre-emptively when an investable set exists but can't be balanced) — it is a **zero-candidate-set** condition inherited directly from Factor Scoring. Per `agents.md § Portfolio Construction Agent Prompt § Failure Rule`: *"If constraints cannot be met without dropping below the minimum investable count, recommend `NO_TRADE` — never force a portfolio."* With 0 candidates against a minimum investable count of 5, `NO_TRADE` is recommended without proceeding to sizing.

## Recommendation

**`NO_TRADE`.** No weights, no portfolio-level Sharpe/Sortino/IR/tracking-error/VaR/CVaR/drawdown, no correlation matrix, and no sector-concentration table are computed this run — publishing placeholder portfolio analytics against zero names would misrepresent the evidence.

## Why Excluded Names Were Left Out

All 30 sampled names are excluded from any portfolio, for the identical, universal reason stated above (Fund_Z and Sent_Z `UNAVAILABLE`), not for name-specific reasons. See `05_factor_scores.md § Score Attribution` for each name's individual `Tech_Z`/`Macro_Z` and `06_top_candidates.md` for the 12-name monitoring sleeve that would be the natural starting point for sizing **if** a third or fourth family became sourceable in a future run.

## What Would Change This

Per `03_regime_and_data.md § Ledger Coverage Gaps` and `00_run_manifest.md § Outstanding Blockers`: wiring a cross-sectional fundamental feed (earnings-revision momentum, revenue acceleration, margin trajectory, FCF yield, ROIC/ROE, leverage, valuation) **or** a sentiment/positioning feed (short interest, options IV/skew, analyst-revision breadth, institutional ownership trend) for at least 70% of the eligible universe would let `Fund_Z` or `Sent_Z` populate, potentially bringing several of the 12 monitoring-sleeve names (`INTC`, `AMAT`, `AMD`, `MU`, `PANW`, `MRVL` are all in the nominal ≥80th-percentile score band) into investable range on their next run.
