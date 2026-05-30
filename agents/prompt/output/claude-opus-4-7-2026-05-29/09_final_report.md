# Quantitative Equity Selection Report — 2026-05-29

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-05-29
Run Status: REVIEW_ONLY
Data Status: ILLUSTRATIVE — NOT LIVE DATA
Reference Vintage: training-data state through ~2026-01
Model: claude-opus-4-7
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The pipeline executed end-to-end against the model's training-data reference state, following the v3.0 prompt system plus the 2026-05-24 `ILLUSTRATIVE_MODE` operating-procedure fix. Family scoring ran with ~95% structural-cadence completeness and the fixed `0.80` data-quality multiplier. **Seven** reference-state names cleared the investability gate (down from 8 on 05-24); AVGO was dropped at the carry-forward stage because its reference Q2 fiscal print is now ~7 days out — deeper inside the 19-day buffered earnings window than the 05-24 skip-the-print sizing can survive. The 5% of book that AVGO carried on 05-24 is redistributed pro-rata across the seven remaining names, leaving the book slightly more defensive (β 0.97 vs 0.99, 95th-pctl DD ~7.3% vs ~7.5%, avg pairwise correlation ~0.36 vs ~0.37). The 5% single-name cap is breached on every position (documented spec tension, escalated to the next monthly structural review — *not* relaxed). Risk committee approves for `REVIEW_ONLY`. `GO` is foreclosed by `ILLUSTRATIVE_MODE`. Next live attempt is Monday 2026-06-01 contingent on a wired data feed.

## MoM Reflection (Standalone Detail In `02_reflection.md`)

| Field | Value |
|---|---|
| Primary baseline | `prompt/output/claude-opus-4-7-2026-05-12/` (17 days prior; closest same-model run to the ~30-day target) |
| Cross-check baseline | `prompt/output/claude-opus-4-7-2026-05-24/` (5 days prior; first post-`ILLUSTRATIVE_MODE`-fix run) |
| Price-level MoM | `UNAVAILABLE` — no live feed; the 05-12 baseline also lacked real candidates, so this is structural |
| Theme-level MoM | All four 05-24 themes validated on reference state (mega-cap growth, defensive growth, cyclical quality, AI-adjacent) — the last marked partially validated and paused via AVGO drop |
| Carry-forward | 7 × `CARRY` (META, LLY, NFLX, NOW, UNH, GE, LIN); 1 × `DROP` (AVGO, event-window); 0 × `PROMOTE` |
| Regime | `NEUTRAL` with `HIGH_VOL` tilt; unchanged from 05-24 |

## Market Regime Assessment

| Metric | Observation | Tag | Implication |
|---|---|---|---|
| Regime | `NEUTRAL` with `HIGH_VOL` tilt (reference-state) | `ILLUSTRATIVE_REF` | Favors quality / margin / FCF over high-beta crowding. Confidence `MEDIUM`. |
| Data quality | `ILLUSTRATIVE` (training-data state through ~2026-01) | — | Sizing is reference-state only; not for live execution. |
| Key macro risk | AI-capex concentration; long-duration sensitivity to real yields | `ILLUSTRATIVE_REF` | Bias the book toward diversifiable quality and away from single-stock AI crowding. |
| Calendar | Day 4 of post-Memorial-Day week; FOMC reference window ~21-23d out | `ILLUSTRATIVE_REF (±2d)` | No FOMC penalty; standard Friday-liquidity expectation. |

## Top Candidates

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Numeric fields tagged `ILLUSTRATIVE_REF`. Structural cadence (`Days→Earnings`) populated from reference quarterly cadence with `±5d` drift band. Intra-day live fields (today's spot, today's bid-ask, today's IV30) remain `N/A`. Confidence capped at `MEDIUM`.

| Rank | Ticker | Company | Sector | 1M Expected α | IR (1M, ref) | β (60D) | Adj. Score | Weight | 30D Vol | Days→Earnings | Confidence |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | META | Meta Platforms | Comm Services | +2.0% ± 4.0% | 0.50 | 1.20 | +1.48 | 12.5% | 28% | ~70 | MEDIUM |
| 2 | LLY | Eli Lilly | Health Care | +2.5% ± 5.0% | 0.50 | 0.65 | +1.42 | 9.5% | 32% | ~70 | MEDIUM |
| 3 | NFLX | Netflix | Comm Services | +1.8% ± 4.0% | 0.45 | 1.10 | +1.32 | 11.5% | 26% | ~49 | MEDIUM |
| 4 | NOW | ServiceNow | Info Tech | +1.6% ± 4.5% | 0.36 | 1.20 | +1.24 | 10.5% | 28% | ~55 | MEDIUM |
| 5 | UNH | UnitedHealth | Health Care | +1.5% ± 3.5% | 0.43 | 0.80 | +1.18 | 17.0% | 22% | ~47 | MEDIUM |
| 6 | GE | GE Aerospace | Industrials | +1.5% ± 4.0% | 0.38 | 1.10 | +1.14 | 17.0% | 24% | ~54 | MEDIUM |
| 7 | LIN | Linde | Materials | +1.2% ± 3.0% | 0.40 | 0.85 | +1.10 | 22.0% | 18% | ~64 | MEDIUM |

**Dropped vs 05-24**: AVGO (was 5% at skip-the-print sizing; reference Q2 print now ~7d out — inside the 19-day buffered window, dropped per `02_reflection.md` §5).

## Thesis Summary (Per Approved Name)

- **META** — Reels and ad-pricing trend driving margin expansion; FCF yield compelling; capex headline largely priced. Risks: ad-cycle, regulatory, AI-narrative reversal.
- **LLY** — GLP-1 / oncology revisions; capacity expansion; defensive-growth in a `HIGH_VOL` tilt. Risks: pipeline reads, payer pushback, real-yield sensitivity.
- **NFLX** — Ad-tier scaling and ARPU acceleration; content-cost efficiency; FCF tailwind. Risks: streaming competition, content re-acceleration, FX.
- **NOW** — Large-deal momentum + AI attach; workflow consolidation; margin leadership. Risks: enterprise-IT spending slowdown, valuation re-rating in a rate shock.
- **UNH** — Mean-reversion candidate; Optum diversification; defensive in `HIGH_VOL`. Risks: medical-cost ratio, regulatory headlines, reform overhang.
- **GE** — Aerospace mid-cycle with services-mix tailwind; cyclical-quality diversifier. Risks: airline capex, supply-chain, geopolitical.
- **LIN** — Defensive-growth in Materials; pricing power and contract durations; portfolio-vol diversifier. Risks: industrial-production cycle, FX, real-yield sensitivity.

## Portfolio Analytics

| Metric | Value | Cap | Status |
|---|---|---|---|
| Expected Sharpe (annualized, ref) | ≈ 0.55 | — | reference-state estimate |
| Expected IR (1M, ref) | ≈ 0.35 | — | reference-state estimate |
| Portfolio β | 0.97 | 0.90 – 1.10 | ✓ |
| 95th-pctl 1M drawdown | ≈ 7.3% | ≤ 8% | ✓ (was ~7.5% on 05-24; AVGO drop eased it slightly) |
| Avg pairwise correlation (assumed) | ≈ 0.36 | < 0.45 | ✓ |
| Max single-name weight | 22.0% (LIN) | ≤ 5% | ✗ spec tension — escalated, not relaxed (was 21.0% on 05-24; +1pp from AVGO redistribution) |
| Max sector weight | 26.5% (Health Care) | ≤ 30% | ✓ |
| Names full-size inside 14d earnings window | 0 (AVGO removed) | — | ✓ event-risk discipline restored |

## Sector Concentration

| Sector | Weight | Names |
|---|---:|---|
| Comm Services | 24.0% | META, NFLX |
| Health Care | 26.5% | LLY, UNH |
| Info Tech | 10.5% | NOW (AVGO removed) |
| Industrials | 17.0% | GE |
| Materials | 22.0% | LIN |

## Assumptions And Limitations

- All numeric values are reference-state estimates from training data through ~2026-01. Structural-cadence fields (`Days→Earnings`, FOMC date) are populated from quarterly-reporting / public cadence and tagged `ILLUSTRATIVE_REF (±Nd)`. Intra-day live fields (today's spot, today's bid-ask, today's IV30) are tagged `N/A`.
- Confidence is capped at `MEDIUM`; no `HIGH` confidence is allowed in `ILLUSTRATIVE_MODE`.
- The 5% single-name cap is breached on every position. This is a spec tension surfaced by a 7-name 100%-sleeve construction, not a discretionary override; escalated to the next monthly structural review per `evolution_policy.md` §Protected Rules.
- The 8% 95th-percentile 1M drawdown estimate is constraint-binding under a correlation realization at the 0.45 cap (vs the 0.36 estimate). A live correlation matrix is required before any `GO` publication.
- Markets are open today (Friday 2026-05-29); the next eligible publish slot is Monday 2026-06-01 07:27 ET.
- Methodology is unchanged from prompt-system v3.0 + 2026-05-24 `ILLUSTRATIVE_MODE` OP fix. Today's run records a documentation tension between `main.md` (14-file layout, standalone `02_reflection.md`) and `daily_output_spec.md` (13-file layout) — escalated to monthly review.

## Run-Status Rationale

Per `eval/research_system.md` §ILLUSTRATIVE_MODE Operating Procedure item 5, runs in `ILLUSTRATIVE_MODE` publish `REVIEW_ONLY` rather than `GO`, even when the portfolio passes constraints. `NO_TRADE` is reserved for live-mode runs that fail to produce ≥ 5 investable names; that condition is not met today (7 ≥ 5).

## Compliance Attestation

| Item | Status |
|---|---|
| No fabricated live prices, IVs, or today-as-of earnings dates | Honored |
| `ILLUSTRATIVE_MODE` declared on every artifact | Honored |
| All numeric fields tagged `ILLUSTRATIVE_REF` or `N/A` per the structural-cadence vs intra-day-live split | Honored |
| Confidence capped at `MEDIUM` | Honored |
| Protected rules in `evolution_policy.md` untouched by autonomous mutation | Honored |
| 5% single-name cap tension escalated, not relaxed | Honored |
| 14-day earnings policy wired through 19-day buffered window; AVGO dropped at ~7d to print | Honored |
| Single explicit run status emitted | Honored (`REVIEW_ONLY`) |
| No Slack / external messaging triggered (cron prompt item 7) | Honored |

## Next Review

- 12:15 ET — `10_midday_monitor.md` exception review (suppressed-but-present today; no live feed).
- 15:45 ET — `11_preclose_check.md` (suppressed-but-present).
- 16:20 ET — `12_close_log.md` (suppressed-but-present).
- 17:00 ET — daily evolution review folded into `13_evolution_log.md` (already published in this pre-open run).
- 17:15 ET (Friday cadence) — weekly parameter review documented in `13_evolution_log.md` Addendum; **not** emitted as standalone `13_weekly_review.md` because the threshold-mutation precondition (≥ 1 live run + ≥ 20 closed observations) is not met.
- Next live attempt: Mon 2026-06-01 07:27 ET pre-open publish slot, contingent on a wired data feed.
- Re-rate AVGO post-print at the first publish slot on or after 2026-06-08.
