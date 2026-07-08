# 05 Top Candidates

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Numeric fields tagged `ILLUSTRATIVE_REF`. Structural-cadence fields (`days_to_earnings`) populated from reference cadence with `±5d` drift band per `eval/research_system.md` §ILLUSTRATIVE_MODE OP item 3. Intra-day live fields (today's spot, today's bid-ask) remain `N/A`. Confidence capped at `MEDIUM` for clean names; `LOW` if inside the 19-day buffered earnings window.

## Investable Subset

| Rank | Ticker | Company | Sector | Composite Z | Adj. Score | Pctl | Expected α (1M, ref) | Beta (60D, ref) | 30D Vol (ref) | Days→Earnings | Confidence | Tag |
|---:|---|---|---|---:|---:|---:|---|---:|---:|---:|---|---|
| 1 | META | Meta Platforms | Comm Services | +1.85 | +1.48 | 99 | +2.0% ± 4.0% | 1.20 | 28% | ~70 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 2 | LLY | Eli Lilly | Health Care | +1.78 | +1.42 | 98 | +2.5% ± 5.0% | 0.65 | 32% | ~75 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 3 | NFLX | Netflix | Comm Services | +1.65 | +1.32 | 97 | +1.8% ± 4.0% | 1.10 | 26% | ~54 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 4 | NOW | ServiceNow | Info Tech | +1.55 | +1.24 | 96 | +1.6% ± 4.5% | 1.20 | 28% | ~60 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 5 | UNH | UnitedHealth | Health Care | +1.48 | +1.18 | 95 | +1.5% ± 3.5% | 0.80 | 22% | ~52 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 6 | AVGO | Broadcom | Info Tech | +1.72 | +1.28 | 94 | +2.2% ± 4.5% | 1.25 | 30% | **~12** | **LOW (near print)** | `ILLUSTRATIVE_REF (±5d)` |
| 7 | GE | GE Aerospace | Industrials | +1.42 | +1.14 | 93 | +1.5% ± 4.0% | 1.10 | 24% | ~59 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |
| 8 | LIN | Linde | Materials | +1.38 | +1.10 | 92 | +1.2% ± 3.0% | 0.85 | 18% | ~69 | MEDIUM | `ILLUSTRATIVE_REF (±5d)` |

Reference cadence used: META Q2 ≈ late-Jul; LLY Q2 ≈ early-Aug; NFLX Q2 ≈ mid-Jul; NOW Q2 ≈ late-Jul; UNH Q2 ≈ mid-Jul; **AVGO fiscal Q2 ≈ early-Jun** (Apr-end fiscal year); GE Q2 ≈ late-Jul; LIN Q2 ≈ early-Aug. Today = 2026-05-24. Drift band ±5d covers the typical announce-date variance for these issuers. AVGO is the only name inside the buffered 19-day window.

## Thesis Summary

### META — Meta Platforms (Comm Services)

- Reels and ad-load monetization continue to compound; ad-pricing trend is the dominant tailwind in reference-state revisions.
- Operating margin expansion has been the cleanest in mega-cap; FCF yield is competitive.
- Reality Labs spend is bounded by management commitment; capex headline risk is largely priced.

Risks: ad-cycle sensitivity, regulatory (EU/US), AI-capex narrative reversal.

### LLY — Eli Lilly (Health Care)

- GLP-1 franchise and oncology pipeline continue to lift earnings revisions.
- Manufacturing capacity expansion eases supply concerns and supports volumes.
- Defensive in a `HIGH_VOL` tilt while still offering growth.

Risks: pipeline read disappointments, payer pushback on pricing, real-yield sensitivity in long-duration health care.

### AVGO — Broadcom (Info Tech) — ⚠ near print

- AI-networking design wins differentiate it from pure-GPU exposure; software (VMware) provides margin diversification.
- Dividend profile and FCF yield are atypical for the AI-capex cohort.
- Customer concentration risk is real but priced; semis cycle is supportive.

**Event-risk note:** Reference Q2 print at ~12 days. Inside the 19-day buffered earnings window (14d policy + 5d drift). Confidence capped at `LOW`. Portfolio agent must default to skip-the-print sizing or drop AVGO.

Risks: AI-capex narrative reversal, hyperscaler concentration, China, **single-print binary risk in next two weeks**.

### NFLX — Netflix (Comm Services)

- Ad-supported tier scaling; password-sharing crackdown still tailwind on ARPU.
- Content efficiency reflected in operating-margin trend.
- Lower content-spend cadence supports FCF.

Risks: streaming competition, content-cost re-acceleration, FX.

### NOW — ServiceNow (Info Tech)

- Large-deal momentum and AI-product attach drive earnings quality.
- Workflow consolidation thesis still intact at large enterprises.
- Margin profile leads software peer set.

Risks: enterprise-IT spending slowdown, valuation re-rating risk in a rate shock.

### UNH — UnitedHealth (Health Care)

- Mean-reversion candidate after sector-specific drawdown; valuation has compressed.
- Optum diversification supports earnings stability.
- Defensive in a `HIGH_VOL` tilt.

Risks: medical-cost ratio surprises, regulatory headlines, reform overhang.

### GE — GE Aerospace (Industrials)

- Aerospace cycle is mid-cycle; aftermarket-services mix expansion supports margins.
- Earnings revisions positive across cycle visibility.
- Industrials diversifier with higher quality than the GICS L1 average.

Risks: airline capex sensitivity, supply-chain frictions, geopolitical.

### LIN — Linde (Materials)

- Defensive growth profile within Materials; pricing power and structural contract durations.
- Lower 30D vol than peer set; portfolio-volatility diversifier.
- Hydrogen / electrification thematic optionality with bounded downside.

Risks: industrial-production cyclicality, FX (large EU exposure), real-yield sensitivity.

## Near-Miss List

| Ticker | Reason kept out of subset |
|---|---|
| NVDA | Strong score but AI-capex / mega-cap crowding penalty plus single-name and IT-sector cap interaction makes it a weaker portfolio addition |
| MSFT | Same as NVDA; correlation with NOW and AVGO is high |
| TMO | Slightly lower percentile; partly redundant with LLY/UNH for HC exposure |
| INTU | Software factor doublet with NOW |
| PGR | Insurance-cycle setup is good but adds Financials at the cost of correlation with the existing book |
| CDNS / ADBE | Software/IT crowding; compositionally redundant |

## Cross-Reference

- Drivers and family breakdown: `04_factor_scores.md`.
- Regime context: `02_regime_and_data.md`.
- Portfolio construction: `06_portfolio_proposal.md`.

## Handoff Note → Portfolio Construction Agent

> Eight investable names with one event-risk flag. Build inside all hard caps. Suggested anchoring: roughly equal-weight with tilts toward lower-vol diversifiers (LIN, UNH, GE) to keep portfolio beta in the 0.95-1.05 band. **For AVGO, default to skip-the-print:** carry token weight (~5%) through the print or drop entirely; do not size at the previous 10% across an event window.
