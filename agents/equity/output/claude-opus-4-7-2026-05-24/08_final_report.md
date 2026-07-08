# Quantitative Equity Selection Report — 2026-05-24

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-05-24
Run Status: REVIEW_ONLY
Data Status: ILLUSTRATIVE — NOT LIVE DATA
Reference Vintage: training-data state through ~2026-01
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The pipeline executed end-to-end against the model's training-data reference state. All four factor families ran with ~90% input completeness and a fixed `0.80` data quality multiplier. Eight reference-state names cleared the investability gate; the 8-name illustrative portfolio is sized inside all hard caps except the 5% single-name cap (documented spec tension, escalated to monthly review). The 14-day earnings penalty — silently disabled in the prior pass when `Days→Earnings` was N/A — is now wired with a 5-day drift buffer on reference cadence; AVGO (~12d to print) is held at skip-the-print sizing (5%), NVDA (~3d) is excluded outright. Risk committee approves for `REVIEW_ONLY` — methodology demonstration, not live execution. Next eligible live attempt is Tuesday 2026-05-26 contingent on a wired data feed.

## Market Regime Assessment

| Metric | Observation | Implication |
|---|---|---|
| Regime | `NEUTRAL` with a `HIGH_VOL` tilt (reference-state) | Favors quality/margin/FCF over high-beta crowding. Confidence MEDIUM. |
| Data quality | `ILLUSTRATIVE` (training-data state through ~2026-01) | Sizing is reference-state only; not for live execution. |
| Key macro risk | AI-capex concentration; long-duration sensitivity to real yields | Bias the book toward diversifiable quality and away from single-stock AI crowding. |

## Top Candidates

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Numeric fields tagged `ILLUSTRATIVE_REF`. Structural cadence (`Days→Earnings`) populated from reference quarterly-reporting cadence with `±5d` drift band. Intra-day live fields (today's spot, bid-ask, IV30) remain `N/A`. Confidence capped at `MEDIUM`; `LOW` if inside the 19-day buffered earnings window.

| Rank | Ticker | Company | Sector | 1M Expected α | IR (1M, ref) | β (60D) | Adj. Score | Weight | 30D Vol | Days→Earnings | Confidence |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | META | Meta Platforms | Comm Services | +2.0% ± 4.0% | 0.50 | 1.20 | +1.48 | 12.0% | 28% | ~70 | MEDIUM |
| 2 | LLY | Eli Lilly | Health Care | +2.5% ± 5.0% | 0.50 | 0.65 | +1.42 | 9.0% | 32% | ~75 | MEDIUM |
| 3 | NFLX | Netflix | Comm Services | +1.8% ± 4.0% | 0.45 | 1.10 | +1.32 | 11.0% | 26% | ~54 | MEDIUM |
| 4 | NOW | ServiceNow | Info Tech | +1.6% ± 4.5% | 0.36 | 1.20 | +1.24 | 10.0% | 28% | ~60 | MEDIUM |
| 5 | UNH | UnitedHealth | Health Care | +1.5% ± 3.5% | 0.43 | 0.80 | +1.18 | 16.0% | 22% | ~52 | MEDIUM |
| 6 | AVGO | Broadcom | Info Tech | +2.2% ± 4.5% | 0.49 | 1.25 | +1.28 | **5.0%** | 30% | **~12** | **LOW** (near print) |
| 7 | GE | GE Aerospace | Industrials | +1.5% ± 4.0% | 0.38 | 1.10 | +1.14 | 16.0% | 24% | ~59 | MEDIUM |
| 8 | LIN | Linde | Materials | +1.2% ± 3.0% | 0.40 | 0.85 | +1.10 | 21.0% | 18% | ~69 | MEDIUM |

Reference cadence: META Q2 ≈ late-Jul; LLY Q2 ≈ early-Aug; NFLX Q2 ≈ mid-Jul; NOW Q2 ≈ late-Jul; UNH Q2 ≈ mid-Jul; AVGO fiscal Q2 ≈ early-Jun (Apr-end fiscal year, the only name inside the 19-day buffered window); GE Q2 ≈ late-Jul; LIN Q2 ≈ early-Aug. Today = 2026-05-24.

## Thesis Summary (Per Approved Name)

- **META** — Reels and ad-pricing trend driving margin expansion; FCF yield compelling; capex headline largely priced. Risks: ad-cycle, regulatory, AI-narrative reversal.
- **LLY** — GLP-1 / oncology revisions; capacity expansion; defensive-growth in a HIGH_VOL tilt. Risks: pipeline reads, payer pushback, real-yield sensitivity.
- **AVGO** — AI-networking design wins, software diversification, dividend profile atypical for AI-capex cohort. **Reference Q2 print ~12d out → skip-the-print sizing at 5%.** Risks: AI-narrative reversal, hyperscaler concentration, China, single-print binary risk inside event window.
- **NFLX** — Ad-tier scaling and ARPU acceleration; content-cost efficiency; FCF tailwind. Risks: streaming competition, content re-acceleration, FX.
- **NOW** — Large-deal momentum + AI attach; workflow consolidation thesis; margin leadership. Risks: enterprise-IT spend slowdown, valuation re-rating in a rate shock.
- **UNH** — Mean-reversion candidate; Optum diversification; defensive in HIGH_VOL. Risks: medical-cost ratio, regulatory headlines, reform overhang.
- **GE** — Aerospace mid-cycle with services-mix tailwind; cyclical-quality diversifier. Risks: airline capex, supply-chain, geopolitical.
- **LIN** — Defensive-growth in Materials; pricing power and contract durations; portfolio-vol diversifier. Risks: industrial-production cycle, FX, real-yield sensitivity.

## Portfolio Analytics

| Metric | Value | Cap | Status |
|---|---|---|---|
| Expected Sharpe (annualized, ref) | ≈ 0.55 | — | reference-state estimate |
| Expected IR (1M, ref) | ≈ 0.35 | — | reference-state estimate |
| Portfolio β | 0.99 | 0.90 – 1.10 | ✓ |
| 95th-pctl 1M drawdown | ≈ 7.5% | ≤ 8% | ✓ (was ~7.9% pre-fix; defensive tilt eased it) |
| Avg pairwise correlation (assumed) | ≈ 0.37 | < 0.45 | ✓ |
| Max single-name weight | 21.0% (LIN) | ≤ 5% | ✗ spec tension — escalated, not relaxed |
| Max sector weight | 25% (Health Care) | ≤ 30% | ✓ |
| Names full-size inside 14d earnings window | 0 (AVGO at 12d held at 5% skip-the-print only) | — | ✓ event-risk discipline restored |

## Sector Concentration

| Sector | Weight | Names |
|---|---:|---|
| Comm Services | 23% | META, NFLX |
| Health Care | 25% | LLY, UNH |
| Info Tech | 15% | AVGO (5%, skip-the-print), NOW |
| Industrials | 16% | GE |
| Materials | 21% | LIN |

## Assumptions And Limitations

- All numeric values are reference-state estimates from training data through ~2026-01. Structural-cadence fields (`Days→Earnings`) are populated from quarterly-reporting cadence and tagged `ILLUSTRATIVE_REF (±5d)`. Intra-day live fields (today's spot, today's bid-ask, today's IV30) are tagged `N/A`.
- Confidence is capped at `MEDIUM`; no `HIGH` confidence is allowed in `ILLUSTRATIVE_MODE`.
- The 5% single-name cap is breached on every position. This is a spec tension surfaced by an 8-name 100%-sleeve construction, not a discretionary override; it is escalated to the next monthly structural review per `evolution_policy.md` §Protected Rules.
- The 8% 95th-percentile 1M drawdown is constraint-binding and sensitive to the assumed correlation. A live correlation matrix is required before any `GO` publication.
- Markets are closed today (Sunday 2026-05-24); the next eligible cash session is Tuesday 2026-05-26 (Memorial Day Monday).
- Methodology is unchanged from prompt-system v3.0 except for the `ILLUSTRATIVE_MODE` operating-procedure addition committed today.

## Run-Status Rationale

Per `eval/research_system.md` §ILLUSTRATIVE_MODE Operating Procedure item 5, runs in `ILLUSTRATIVE_MODE` publish `REVIEW_ONLY` rather than `GO`, even when the portfolio passes constraints. `NO_TRADE` is reserved for live-mode runs that fail to produce ≥ 5 investable names; that condition is not met today.

## Compliance Attestation

| Item | Status |
|---|---|
| No fabricated live prices, IVs, or today-as-of earnings dates | Honored |
| `ILLUSTRATIVE_MODE` declared on every artifact | Honored |
| All numeric fields tagged `ILLUSTRATIVE_REF` or `N/A` | Honored |
| Confidence capped at `MEDIUM` | Honored |
| Protected rules in `evolution_policy.md` untouched by autonomous mutation | Honored |
| 5% single-name cap tension escalated, not relaxed | Honored |
| Single explicit run status emitted | Honored (`REVIEW_ONLY`) |

## Next Review

- The 09:30 → 16:20 ET intraday checkpoints (`09_midday_monitor.md`, `10_preclose_check.md`, `11_close_log.md`) are written as suppressed-but-present (markets closed today).
- Daily evolution review (`12_evolution_log.md`) — loop fix logged; threshold mutation ineligible (<20 closed observations).
- Next live attempt: Tue 2026-05-26 07:30 ET pre-open publish slot, contingent on a wired data feed.
- Friday 2026-05-29 17:15 ET: weekly parameter review (`13_weekly_review.md`) — only if a feed is wired and at least one live run has produced realized data.
