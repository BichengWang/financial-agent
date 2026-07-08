# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (Task 0 — before any sizing)

Input: investable set from 05. **The investable set is EMPTY** (0 names pass evidence threshold #2 with 2/4 families sourceable; threshold requires 3 of 4 non-negative). Stop criterion `NO_TRADE #1` (fewer than 5 investable names) fires immediately — **no weights drafted, no revision pass spent**, per the Track B pre-check rule (2026-06-10, HUMAN_REVIEW).

Recommendation: **NO_TRADE**.

## Feasibility Diagnostics (informational, from already-fetched inputs)

Had the 22-name monitoring sleeve been investable, the achievable envelope from fetched inputs would be: per-name beta range -0.60 (ABBV) to +1.49 (DAL) — cap-weight-mixable inside the 0.90–1.10 band; sector counts below — Health Care at 7/22 (32%) **would breach the 30% sector cap by one name**, so a compliant book would drop the lowest-ranked HC name (ABBV, 81.8 pctl) or downweight the leg; the 5% single-name cap binds every position (all Kelly 0.25 >= 5% NAV):

| Sector (INFERRED) | Names | Share |
|---|---|---|
| Health Care | 7 | 32% of sleeve — cap-binding |
| Information Technology | 5 | 23% of sleeve |
| Industrials | 3 | 14% of sleeve |
| Financials | 2 | 9% of sleeve |
| Communication Services | 2 | 9% of sleeve |
| Consumer Staples | 1 | 5% of sleeve |
| Real Estate | 1 | 5% of sleeve |
| Materials | 1 | 5% of sleeve |

These diagnostics are not a proposal; they document that today's block is the family-coverage gate, not portfolio-constraint infeasibility (the HC overweight is fixable inside one revision by construction).

## Per-Position Recommendation Metrics

Inherited unchanged from 05 (single source; no recomputation) — see the Ranked Candidate Table there, columns Entry through CI bounds, with score traces and ledger rows.

## Excluded Names

DROP names per 02 §5 (MCK, COST, WMT, CVX, XOM, MU, NVDA, GOOGL) excluded regardless of rank; UNH excluded on DOWNGRADE (earnings ~8d, 84.4 pctl post-penalty); 35 earnings-window names penalized -0.10, which pushed yesterday's banks/airlines/industrial entrants (IBKR, WST, DOC, BAC, GE, LUV, UAL, AXP, STT, EW, CFG) below today's top 20; every other eligible name scored below the published ranks.
