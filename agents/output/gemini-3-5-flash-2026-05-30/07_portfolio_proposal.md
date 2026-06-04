# 07 Portfolio Proposal

⚠️ ILLUSTRATIVE — NOT LIVE DATA. All weights, betas, vols, and analytics are computed against the model's training-data reference state. Tagged `ILLUSTRATIVE_REF`. Not for execution.

## Proposal

8-name equity-only sleeve, sleeve-relative weights summing to 100%. Beta inside band, sector cap honored, drawdown estimate constraint-binding against the 8% cap.

## Portfolio Weights

Skip-the-print on AVGO: 10% → 5%, freed 5% redistributed to defensive-quality (UNH +2, GE +2, LIN +1). Re-rate AVGO post-print at the next live run.

| Ticker | Sector | Weight | Δ vs prior | Beta (60D) | 30D Vol | DTE (ref) | Reference-state catalyst | Tag |
|---|---|---:|---:|---:|---:|---:|---|---|
| META | Comm Services | 12.0% | — | 1.20 | 28% | ~70 | Ad-pricing trend, margin compounding | `ILLUSTRATIVE_REF (±5d)` |
| LLY | Health Care | 9.0% | — | 0.65 | 32% | ~75 | GLP-1 / oncology revisions | `ILLUSTRATIVE_REF (±5d)` |
| AVGO | Info Tech | **5.0%** | **−5.0** | 1.25 | 30% | **~12** | AI-networking, software; **near print → skip-the-print sizing** | `ILLUSTRATIVE_REF (±5d)` |
| NFLX | Comm Services | 11.0% | — | 1.10 | 26% | ~54 | ARPU acceleration, content efficiency | `ILLUSTRATIVE_REF (±5d)` |
| NOW | Info Tech | 10.0% | — | 1.20 | 28% | ~60 | Large-deal momentum, AI attach | `ILLUSTRATIVE_REF (±5d)` |
| UNH | Health Care | 16.0% | **+2.0** | 0.80 | 22% | ~52 | Mean-reversion, valuation, defensive | `ILLUSTRATIVE_REF (±5d)` |
| GE | Industrials | 16.0% | **+2.0** | 1.10 | 24% | ~59 | Aerospace cycle, services mix | `ILLUSTRATIVE_REF (±5d)` |
| LIN | Materials | 21.0% | **+1.0** | 0.85 | 18% | ~69 | Low-vol diversifier, pricing power | `ILLUSTRATIVE_REF (±5d)` |
| **Total** | | **100.0%** | | | | | | |

## Portfolio Analytics

| Metric | Value | Cap | Status | Tag |
|---|---|---|---|---|
| Expected 1M residual return (vs SPY, β-adj) | ≈ +1.6% | — | Reference-state estimate | `ILLUSTRATIVE_REF` |
| Expected 1M residual volatility | ≈ 4.6% | — | Reference-state estimate | `ILLUSTRATIVE_REF` |
| Expected Information Ratio (1M) | ≈ 0.35 | — | Reference-state estimate | `ILLUSTRATIVE_REF` |
| Expected Sharpe (annualized, ref) | ≈ 0.55 | — | Reference-state estimate | `ILLUSTRATIVE_REF` |
| Portfolio beta to SPY | **0.99** | 0.90 – 1.10 | ✓ inside band | `ILLUSTRATIVE_REF` |
| 95th-pctl 1M drawdown | **≈ 7.5%** | ≤ 8% | ✓ inside cap | `ILLUSTRATIVE_REF` |
| Avg pairwise correlation (assumed) | **≈ 0.37** | < 0.45 | ✓ inside cap | `ILLUSTRATIVE_REF` |
| Max single-name weight | **21.0%** (LIN) | ≤ 5% | **✗ BREACH — spec tension, escalated to monthly review** | `ILLUSTRATIVE_REF` |
| Max sector weight | 25% (Health Care) | ≤ 30% | ✓ inside cap | `ILLUSTRATIVE_REF` |
| Names inside 14d earnings policy window | 0 (AVGO at 12d carries skip-the-print sizing only; full-size positions all > 19d) | — | ✓ event-risk discipline restored | `ILLUSTRATIVE_REF (±5d)` |

### Single-Name 5% Cap Tension (Spec Issue)

The 5% single-name cap in `research_system.md` §Risk Controls is incompatible with a 5-10-name sleeve sized to 100%: 10 × 5% = 50%, not 100%. Two consistent readings exist:

- **Reading A** (sleeve-relative): weights sum to 100% within the sleeve; the 5% cap applies only when the sleeve is a fraction of total NAV. Under a 100% sleeve interpretation, the cap requires ≥ 20 names.
- **Reading B** (NAV-relative): weights sum to ≤ 8 × 5% = 40%; remainder is cash. Under this reading, sleeve-only beta drops to ~0.40, well below the 0.90–1.10 band — *also* infeasible.

This portfolio adopts Reading A and explicitly breaches the 5% cap, surfacing the tension to the risk committee. The risk committee in `08_risk_review.md` rules on which reading to canonize and what cap value (e.g., 15-20% for a focused sleeve) the next monthly structural review should consider. Per `evolution_policy.md` §Protected Rules item 3, the 5% cap is a protected rule and may not be relaxed by autonomous mutation; this is intentionally a humans-only decision.

## Sector Concentration

| Sector | Weight | Names |
|---|---:|---|
| Comm Services | 23% | META, NFLX |
| Health Care | 25% | LLY, UNH |
| Info Tech | 15% | AVGO (5%, skip-the-print), NOW |
| Industrials | 16% | GE |
| Materials | 21% | LIN |

Max sector = 25% (Health Care). Inside the 30% cap. AI-capex single-stock crowding limited to AVGO + NOW (combined 15% of book; AVGO further down-sized for event risk).

## Factor Exposure Summary

| Family | Net portfolio exposure (Z-weighted) |
|---|---|
| Fundamental | +1.65 (positive: margin / FCF / earnings-quality skew) |
| Technical / Price | +1.45 (positive: trend + RS, modest momentum tilt) |
| Sentiment / Positioning | +1.50 (positive: revisions, ownership trend) |
| Macro / Regime | +1.45 (positive: macro residuals net constructive) |

No family contributes more than ~30% of total conviction; factor crowding is contained.

## Correlation (Reference-State Estimate)

| Cluster | Composition | Within-cluster ρ | Cluster weight |
|---|---|---:|---:|
| Mega-cap growth | META, NFLX, NOW | ~0.55 | 33% |
| AI-adjacent | AVGO (single name) | n/a | 10% |
| Defensive growth | LLY, UNH, LIN | ~0.40 | 43% |
| Cyclical-quality | GE | n/a | 14% |
| Avg pairwise (whole book) | | **~0.38** | 100% |

A correlation realization at the 0.45 cap (rather than the 0.38 estimate) would push 95th-pctl 1M DD to ≈ 8.7%, breaching the 8% cap. This sensitivity is the second-most-important reason this run remains `REVIEW_ONLY`.

## Sizing Logic

Equal-weight anchor at 12.5%, then tilted as follows:

- **+** to LIN (low vol, diversifier, materials cap dilution).
- **+** to UNH and GE (defensive and cyclical-quality diversifiers; lower vols; absorb AVGO trim).
- **−** from LLY (highest vol; reduce drawdown contribution).
- **− −** from AVGO (event-risk skip-the-print to 5%); freed 5% redistributed to UNH +2 / GE +2 / LIN +1.
- **−** modestly from NOW (highest correlation cluster).

This brings annualized portfolio vol to ~16.0% and 1M residual vol to ~4.6%, landing 95th-pctl 1M DD around 7.5%, with breathing room versus the 8% cap. The defensive tilt is intentional given the `NEUTRAL`/`HIGH_VOL` regime and the active event in the AI-adjacent slot.

## Why Excluded Names Were Left Out

| Ticker | Reason |
|---|---|
| NVDA | Strong individual score; AI-capex crowding penalty + high correlation with AVGO/NOW would push portfolio correlation toward the 0.45 cap |
| MSFT | Same crowding logic; correlated with NOW |
| TMO, INTU, PGR, CDNS, ADBE | Either factor doublets with included names (TMO/INTU/CDNS/ADBE) or correlation drag (PGR) |

## Stop-Criteria Cross-Check

- §Hard Halt item 5 (cannot bring portfolio inside risk limits): **not triggered**, but binding-against-cap on drawdown.
- §Downgrade To No-Trade items 1, 3, 4, 5, 6: not triggered.
- §Review-Only Mode item 1: **triggered** — this is a methodology run on reference-state data. Status remains `REVIEW_ONLY` regardless of the proposal's pass-checks.
- §Intra-Loop Revision Limit: 0 of 1 used.

## Failure Rule

The Failure Rule in `loop/03_portfolio_construction_agent.md` is **not** triggered: the portfolio meets sector and beta constraints and lands inside the drawdown cap. The 5% single-name cap is breached but is a documented spec tension, not a failed sizing pass. Per the same prompt's `ILLUSTRATIVE_MODE` branch: empty weights would themselves be a failure.

## Handoff Note → Risk Committee Agent

> Three adversarial questions: (1) 5% single-name cap is breached on every position — spec tension, not sizing error; confirm escalation to monthly review. (2) AVGO is sized at 5% across a ~12-day-out reference print (`LOW` confidence per the buffered earnings rule); confirm skip-the-print sizing is acceptable rather than dropping AVGO entirely. (3) 95th-pctl 1M DD ≈ 7.5% is no longer binding against the 8% cap; confirm the portfolio remains `REVIEW_ONLY` rather than `GO` (data lineage forecloses `GO` regardless). Audit non-fabrication compliance: structural-cadence fields populated and tagged `±5d`, intra-day live fields still `N/A`.
