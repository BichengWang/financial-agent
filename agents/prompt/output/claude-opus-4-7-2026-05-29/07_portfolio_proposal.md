# 07 Portfolio Proposal

⚠️ ILLUSTRATIVE — NOT LIVE DATA. All weights, betas, vols, and analytics are computed against the model's training-data reference state. Tagged `ILLUSTRATIVE_REF`. Not for execution.

## Proposal

7-name equity-only sleeve, sleeve-relative weights summing to 100%. **Δ vs 05-24 baseline**: AVGO removed (5% → 0%); freed 5% redistributed pro-rata across the remaining seven. Beta inside band, sector cap honored, drawdown estimate inside the 8% cap. The 5% single-name cap is breached on every position — documented spec tension, escalated to monthly review.

## Portfolio Weights

| Ticker | Sector | Weight | Δ vs 05-24 | β (60D, ref) | 30D Vol (ref) | DTE (ref) | Reference-state catalyst | Tag |
|---|---|---:|---:|---:|---:|---:|---|---|
| META | Comm Services | 12.5% | +0.5 | 1.20 | 28% | ~70 | Ad-pricing trend, margin compounding | `ILLUSTRATIVE_REF (±5d)` |
| LLY | Health Care | 9.5% | +0.5 | 0.65 | 32% | ~70 | GLP-1 / oncology revisions | `ILLUSTRATIVE_REF (±5d)` |
| NFLX | Comm Services | 11.5% | +0.5 | 1.10 | 26% | ~49 | ARPU acceleration, content efficiency | `ILLUSTRATIVE_REF (±5d)` |
| NOW | Info Tech | 10.5% | +0.5 | 1.20 | 28% | ~55 | Large-deal momentum, AI attach | `ILLUSTRATIVE_REF (±5d)` |
| UNH | Health Care | 17.0% | +1.0 | 0.80 | 22% | ~47 | Mean-reversion, valuation, defensive | `ILLUSTRATIVE_REF (±5d)` |
| GE | Industrials | 17.0% | +1.0 | 1.10 | 24% | ~54 | Aerospace cycle, services mix | `ILLUSTRATIVE_REF (±5d)` |
| LIN | Materials | 22.0% | +1.0 | 0.85 | 18% | ~64 | Low-vol diversifier, pricing power | `ILLUSTRATIVE_REF (±5d)` |
| **AVGO (removed)** | Info Tech | **0.0%** | **−5.0** | — | — | **~7** | **Reference Q2 print inside 19-day buffered window — DROP per `02_reflection.md`** | — |
| **Total** | | **100.0%** | | | | | | |

## Portfolio Analytics

| Metric | Value | Cap | Status | Tag |
|---|---|---|---|---|
| Expected 1M residual return (vs SPY, β-adj) | ≈ +1.55% | — | Reference-state estimate (slight reduction from ≈ +1.6% on 05-24 due to AVGO drop) | `ILLUSTRATIVE_REF` |
| Expected 1M residual volatility | ≈ 4.4% | — | Reference-state estimate | `ILLUSTRATIVE_REF` |
| Expected Information Ratio (1M) | ≈ 0.35 | — | Reference-state estimate (essentially unchanged) | `ILLUSTRATIVE_REF` |
| Expected Sharpe (annualized, ref) | ≈ 0.55 | — | Reference-state estimate | `ILLUSTRATIVE_REF` |
| **Portfolio β to SPY** | **0.97** | 0.90 – 1.10 | ✓ inside band (was 0.99 on 05-24; AVGO drop reduced β by ~0.02 net of pro-rata redistribution) | `ILLUSTRATIVE_REF` |
| **95th-pctl 1M drawdown** | **≈ 7.3%** | ≤ 8% | ✓ inside cap (was ~7.5% on 05-24; lower vol from AVGO removal) | `ILLUSTRATIVE_REF` |
| **Avg pairwise correlation (assumed)** | **≈ 0.36** | < 0.45 | ✓ inside cap (was ~0.37 on 05-24; AVGO removal slightly reduces IT crowding) | `ILLUSTRATIVE_REF` |
| Max single-name weight | **22.0%** (LIN) | ≤ 5% | **✗ BREACH — spec tension, escalated to monthly review (was 21% on 05-24; +1pp from AVGO redistribution)** | `ILLUSTRATIVE_REF` |
| Max sector weight | 26.5% (Health Care) | ≤ 30% | ✓ inside cap (was 25% on 05-24; +1.5pp from UNH redistribution) | `ILLUSTRATIVE_REF` |
| Names inside 14d earnings policy window | **0** | — | ✓ event-risk discipline honored (AVGO removed) | `ILLUSTRATIVE_REF (±5d)` |

### Single-Name 5% Cap Tension (Spec Issue, Unchanged from 05-24)

The 5% single-name cap in `research_system.md` §Risk Controls is geometrically incompatible with a 5-10-name sleeve sized to 100% of NAV: 10 × 5% = 50%, not 100%. Two consistent readings exist (sleeve-relative vs NAV-relative); both are infeasible against the rest of the constraint set as currently written. The 05-24 escalation stands; the recommended structural-review options (Option A: raise cap to 15-20% for focused sleeves; Option B: canonize NAV-relative with cash overlay) remain on the next monthly structural-review agenda. Per `evolution_policy.md` §Protected Rules item 3, this is a humans-only decision; today's run does not relax the cap.

## Sector Concentration

| Sector | Weight | Names |
|---|---:|---|
| Comm Services | 24.0% | META (12.5%), NFLX (11.5%) |
| Health Care | 26.5% | LLY (9.5%), UNH (17.0%) |
| Info Tech | 10.5% | NOW (10.5%) — AVGO removed |
| Industrials | 17.0% | GE (17.0%) |
| Materials | 22.0% | LIN (22.0%) |

Max sector = 26.5% (Health Care). Inside the 30% cap. AI-capex single-stock crowding reduced from 15% (AVGO + NOW on 05-24) to 10.5% (NOW only) — favorable side-effect of the AVGO drop.

## Factor Exposure Summary

| Family | Net portfolio exposure (Z-weighted) | Δ vs 05-24 |
|---|---|---|
| Fundamental | +1.62 | -0.03 (AVGO contribution removed; partially offset by redistribution) |
| Technical / Price | +1.42 | -0.03 |
| Sentiment / Positioning | +1.48 | -0.02 |
| Macro / Regime | +1.43 | -0.02 |

No family contributes more than ~30% of total conviction; factor crowding remains contained.

## Correlation Structure (Reference-State Estimate)

| Cluster | Composition | Within-cluster ρ | Cluster weight | Δ vs 05-24 |
|---|---|---:|---:|---:|
| Mega-cap growth | META, NFLX, NOW | ~0.55 | 34.5% | +1.5 |
| AI-adjacent | (none — AVGO removed) | — | 0% | -10 |
| Defensive growth | LLY, UNH, LIN | ~0.40 | 48.5% | +5.5 |
| Cyclical-quality | GE | n/a | 17.0% | +1.0 |
| **Avg pairwise (whole book)** | | **~0.36** | 100% | -0.01 |

The book is now structurally tilted further toward the **defensive-growth cluster (48.5% of weights)**. This is intentional given the AVGO drop and the `HIGH_VOL` regime tilt.

### Sensitivity Check

A correlation realization at the 0.45 cap (vs the 0.36 estimate) would push 95th-pctl 1M DD to ≈ 8.5%, just above the 8% cap. This sensitivity (unchanged from 05-24) is the second-most-important reason this run remains `REVIEW_ONLY` rather than `GO`; the first is the `ILLUSTRATIVE_MODE` data-lineage status.

## Sizing Logic

Equal-weight anchor at 14.3% (1/7), then tilted as follows:

- **+** to LIN (low vol, materials diversifier, absorbs largest pro-rata share).
- **+** to UNH and GE (defensive and cyclical-quality diversifiers; lower vols).
- **−** modestly from LLY (highest vol in the book at 32%; reduce drawdown contribution).
- **−** modestly from NOW (highest-correlation cluster; AI-adjacent residual exposure).
- META, NFLX, NOW each absorb the smaller pro-rata share (+0.5pp) to keep mega-cap growth cluster from re-expanding.

This brings annualized portfolio vol to ~15.5% (was ~16.0%) and 1M residual vol to ~4.4%, landing 95th-pctl 1M DD around 7.3%, with marginally improved breathing room versus the 8% cap. The defensive tilt is intentional given the `NEUTRAL` / `HIGH_VOL` regime and the AVGO event-window discipline.

## Why Excluded Names Were Left Out

| Ticker | Reason |
|---|---|
| AVGO | Carry-forward `DROP`; reference Q2 print ~7d inside the 19-day buffered window |
| NVDA | Post-print eligibility but AI-capex crowding with NOW — would push avg pairwise correlation toward the 0.45 cap |
| MSFT | Same crowding logic; correlated with NOW |
| TMO, INTU, PGR, CDNS, ADBE, GOOGL, AMZN, COST | Factor doublets, correlation drag, or out-of-thesis cluster (see `06_top_candidates.md` rejection notes) |

## Stop-Criteria Cross-Check

- §Hard Halt item 5 (cannot bring portfolio inside risk limits): **not triggered**; β / DD / corr / sector all inside their caps.
- §Downgrade To No-Trade items 1-6: **not triggered** (7 names ≥ 5; ≥ 80th pctl; corr 0.36 < 0.45; 0 names in 14d window; DD inside cap; no single-sector overconcentration).
- §Review-Only Mode item 1: **triggered** — methodology run on reference-state data. Status remains `REVIEW_ONLY` regardless of the proposal's pass-checks.
- §Intra-Loop Revision Limit: 0 of 1 used.

## Failure Rule

The Failure Rule in `loop/03_portfolio_construction_agent.md` is **not** triggered: 7 names pass, the portfolio is inside all hard caps except the documented 5% spec tension, drawdown is inside the 8% cap with breathing room. Per the `ILLUSTRATIVE_MODE` branch of the prompt, empty weights would themselves be a failure.

## Handoff Note → Risk Committee Agent

> Three adversarial questions for the committee: (1) AVGO drop at ~7d to print — confirm event-risk discipline supersedes the 05-24 skip-the-print sizing now that proximity has compressed; (2) Pro-rata redistribution of AVGO's 5% across the existing book — confirm this is preferable to either (a) adding a new name like NVDA at 5% (post-print eligibility) or (b) holding 5% cash equivalent; (3) 5% single-name cap remains breached on every position (max 22% LIN, up from 21% on 05-24) — confirm the spec tension escalation is the correct disposition and the cap is not relaxed. Audit non-fabrication compliance: structural-cadence fields populated and tagged `±5d`, intra-day live fields still `N/A`, no live prices invented.
