# 05 Factor Scores

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Family-level Z-scores and the composite are computed against the model's training-data reference state. Every numeric field is tagged `ILLUSTRATIVE_REF`. Structural-cadence fields (`days_to_earnings`) are populated from reference quarterly cadence and tagged `ILLUSTRATIVE_REF (±5d)`. Intra-day live fields (today's spot, today's bid-ask, today's IV30, today's volume tape, today's short-interest delta) remain `N/A`.

Family weights are unchanged from the §Factor Architecture baseline:

| Family | Weight |
|---|---|
| Fundamental | 0.30 |
| Technical / Price | 0.30 |
| Sentiment / Positioning | 0.25 |
| Macro / Regime | 0.15 |

Data-quality multiplier: **fixed `0.80`** per `research_system.md` §ILLUSTRATIVE_MODE OP item 4.

## Methodology Notes

1. Family Z-scores are cross-sectional, computed against the ~1,500-name reference-state eligible universe.
2. Composite Z = `0.30·F + 0.30·T + 0.25·S + 0.15·M`.
3. Adjusted score = `Composite Z · 0.80 − Penalties`.
4. Penalties:
   - `−0.10` if `days_to_earnings ≤ 19` (14d policy + 5d cadence drift).
   - `−0.05` if 30D realized vol > 2× sector median (reference-state heuristic).
   - `−0.05` if no plausible 30-day catalyst on the reference-state thesis.
5. Confidence is capped at `MEDIUM` by `ILLUSTRATIVE_MODE`; `LOW` inside the 19-day buffered earnings window.
6. Family-level scores below are net of the data-quality multiplier (applied at the composite level, not double-counted at the family level).

## Carry-Forward Constraint

Per `02_reflection.md` §5: AVGO is `DROP`-flagged on event-risk grounds. AVGO is shown in the leaderboard below for transparency, but the `Investable?` column reflects the carry-forward decision and AVGO sits in the rejection list.

## Top 20 By Adjusted Score (Reference-State)

| Rank | Ticker | Sector | F (0.30) | T (0.30) | S (0.25) | M (0.15) | Composite Z | DQ × | Penalty | Adj. Score | Pctl | DTE (ref) | Investable? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | META | Comm Services | +1.95 | +1.80 | +1.85 | +1.60 | +1.85 | 0.80 | 0.00 | **+1.48** | 99 | ~70 | ✓ |
| 2 | LLY | Health Care | +2.05 | +1.55 | +1.80 | +1.60 | +1.78 | 0.80 | 0.00 | **+1.42** | 98 | ~70 | ✓ |
| 3 | NFLX | Comm Services | +1.65 | +1.75 | +1.65 | +1.50 | +1.65 | 0.80 | 0.00 | **+1.32** | 97 | ~49 | ✓ |
| 4 | AVGO | Info Tech | +1.85 | +1.70 | +1.65 | +1.65 | +1.72 | 0.80 | **−0.10 (DTE)** | **+1.28** | 94 | **~7** | ✗ (carry-fwd DROP) |
| 5 | NOW | Info Tech | +1.55 | +1.55 | +1.55 | +1.55 | +1.55 | 0.80 | 0.00 | **+1.24** | 96 | ~55 | ✓ |
| 6 | UNH | Health Care | +1.65 | +1.30 | +1.50 | +1.50 | +1.48 | 0.80 | 0.00 | **+1.18** | 95 | ~47 | ✓ |
| 7 | MSFT | Info Tech | +1.45 | +1.40 | +1.50 | +1.50 | +1.45 | 0.80 | 0.00 | +1.16 | 93 | ~55 | ✗ (crowding) |
| 8 | NVDA | Info Tech | +1.85 | +1.60 | +1.50 | +1.70 | +1.66 | 0.80 | 0.00* | +1.33 | 92 | ~85 (post Q1) | ✗ (crowding) |
| 9 | GE | Industrials | +1.45 | +1.45 | +1.40 | +1.40 | +1.42 | 0.80 | 0.00 | **+1.14** | 93 | ~54 | ✓ |
| 10 | LIN | Materials | +1.50 | +1.30 | +1.40 | +1.30 | +1.38 | 0.80 | 0.00 | **+1.10** | 92 | ~64 | ✓ |
| 11 | TMO | Health Care | +1.40 | +1.30 | +1.30 | +1.30 | +1.33 | 0.80 | 0.00 | +1.07 | 91 | ~55 | ✗ (HC doublet w/ LLY) |
| 12 | INTU | Info Tech | +1.50 | +1.30 | +1.30 | +1.35 | +1.37 | 0.80 | 0.00 | +1.10 | 91 | ~75 | ✗ (software doublet w/ NOW) |
| 13 | GOOGL | Comm Services | +1.30 | +1.35 | +1.30 | +1.40 | +1.33 | 0.80 | 0.00 | +1.06 | 90 | ~50 | ✗ (Comm Svcs cap; correlated w/ META) |
| 14 | PGR | Financials | +1.45 | +1.30 | +1.20 | +1.10 | +1.30 | 0.80 | 0.00 | +1.04 | 90 | ~45 | ✗ (correlation drag) |
| 15 | ADBE | Info Tech | +1.25 | +1.20 | +1.30 | +1.30 | +1.25 | 0.80 | 0.00 | +1.00 | 89 | ~14 | ✗ (DTE in buffered window) |
| 16 | CDNS | Info Tech | +1.30 | +1.15 | +1.20 | +1.25 | +1.23 | 0.80 | 0.00 | +0.98 | 89 | ~70 | ✗ (software doublet w/ NOW/INTU) |
| 17 | MA | Financials | +1.35 | +1.20 | +1.20 | +1.10 | +1.24 | 0.80 | 0.00 | +0.99 | 88 | ~55 | ✗ (Financials shelf; not a thesis priority) |
| 18 | V | Financials | +1.30 | +1.20 | +1.20 | +1.10 | +1.22 | 0.80 | 0.00 | +0.97 | 87 | ~55 | ✗ (Same) |
| 19 | AMZN | Comm Services* | +1.20 | +1.10 | +1.25 | +1.30 | +1.20 | 0.80 | 0.00 | +0.96 | 87 | ~55 | ✗ (Comm Svcs cap) |
| 20 | COST | Cons Staples | +1.30 | +1.10 | +1.10 | +1.10 | +1.18 | 0.80 | 0.00 | +0.94 | 86 | ~30 | ✗ (Staples not in thesis cluster) |

`*` NVDA reference Q1 print is past on reference cadence as of today (~3-day post-print). The buffered DTE penalty does not apply.

`*` AMZN GICS classification varies (Consumer Discretionary / Comm Services); reference state uses Comm Services for the AI-narrative cluster.

## Investable Subset (7 Names — Carry-Forward Honored)

| Rank | Ticker | Sector | Adj. Score | Pctl | DTE (ref) | Confidence | Tag |
|---:|---|---|---:|---:|---:|---|---|
| 1 | META | Comm Services | +1.48 | 99 | ~70 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 2 | LLY | Health Care | +1.42 | 98 | ~70 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 3 | NFLX | Comm Services | +1.32 | 97 | ~49 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 4 | NOW | Info Tech | +1.24 | 96 | ~55 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 5 | UNH | Health Care | +1.18 | 95 | ~47 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 6 | GE | Industrials | +1.14 | 93 | ~54 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 7 | LIN | Materials | +1.10 | 92 | ~64 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |

All 7 clear the `research_system.md` §Evidence Thresholds:

1. Composite percentile ≥ 80? ✓ (all ≥ 92)
2. ≥ 3 of 4 factor families non-negative? ✓ (all 4 positive)
3. No single family > 50% of total conviction? ✓ (max contribution ≈ 32%)
4. Data completeness ≥ 85%? ✓ on the reference-state structural fields; intra-day live fields tracked separately
5. No `stop_criteria.md` hard stop? ✓

## Rejection Notes (Near-Misses)

| Ticker | Reason kept out of subset |
|---|---|
| AVGO | Carry-forward `DROP`: reference Q2 print ~7d, inside the 19-day buffered window; event-risk discipline supersedes |
| MSFT | High-quality score but adds AI-capex crowding with NOW; correlation with NOW > 0.55 reference-state |
| NVDA | Post-print eligibility restored but AI-capex crowding with NOW; correlation > 0.55 reference-state; held out |
| TMO | HC doublet with LLY/UNH; redundant exposure |
| INTU / CDNS | Software doublet with NOW; redundant factor exposure |
| GOOGL / AMZN | Comm Services cluster; correlated with META and NFLX |
| PGR / MA / V | Financials are not in today's thesis cluster; correlation drag exceeds incremental alpha |
| ADBE | DTE ~14d puts ADBE inside the 19-day buffered window; would carry `LOW` confidence and the same skip-the-print sizing constraint AVGO was dropped under |
| COST | Staples not in thesis cluster; defensive-growth slot already filled by LLY/UNH/LIN |

## Family Driver Summary (Investable Subset)

| Family | Contribution range (Z) | Comment |
|---|---|---|
| Fundamental | +1.45 to +2.05 | Earnings-revision momentum dominant in META and LLY; FCF discipline supports NFLX |
| Technical / Price | +1.30 to +1.80 | Trend strength and RS strongest in META, NFLX, AVGO (now dropped) |
| Sentiment / Positioning | +1.40 to +1.85 | Net analyst revisions and ownership trend favorable across the seven |
| Macro / Regime | +1.30 to +1.65 | Defensive-growth tilt (LLY, UNH, LIN) carries macro family scores |

No single family is contributing more than ~32% to any name's conviction — the §Evidence Threshold cap of 50% is well respected.

## Signal Decay Notes

No name in the investable subset is anchored on a signal with half-life < 5 trading days. The closest is META's ad-pricing trend (≈ 10 trading days half-life on reference state); within tolerance.

## Handoff Note → Portfolio Construction Agent

> 7 investable names; all `MEDIUM` confidence; AVGO already dropped at the scoring stage. Build a portfolio inside all hard caps. Suggested anchoring: redistribute AVGO's 5% from the 05-24 book pro-rata across the remaining 7. Expect portfolio β to drift slightly defensive (~0.97 from 0.99); confirm inside the 0.90-1.10 band. The 5% single-name cap will be breached as usual; surface the tension, do not relax.
