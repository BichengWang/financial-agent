# 03 Regime And Data

⚠️ ILLUSTRATIVE — NOT LIVE DATA. All evidence cells are reference-state observations from training data through ~2026-01, tagged `ILLUSTRATIVE_REF`. Calendar fields are projected from today's actual date (2026-05-29) using deterministic cadences and tagged `ILLUSTRATIVE_REF (±Nd)`. Live intra-day fields (today's SPY, today's VIX, today's TLT) remain `N/A`.

## Data State Declaration

Per `loop/01_data_regime_agent.md` §ILLUSTRATIVE_MODE Branch and `eval/research_system.md` §Required Data Discipline: data state is `ILLUSTRATIVE`. Reference vintage disclosed in `00_run_manifest.md` and `01_preflight.md`. The methodology runs end-to-end; the publication status is `REVIEW_ONLY` per `stop_criteria.md` §Review-Only Mode item 1.

## Regime Classification

**Label**: `NEUTRAL` with `HIGH_VOL` tilt. **Confidence**: `MEDIUM` (capped by `ILLUSTRATIVE_MODE`). Unchanged from 2026-05-24.

### Regime Evidence (Reference-State)

| Dimension | Observation | Tag | Implication |
|---|---|---|---|
| Broad-equity trend | Reference-state SPY in a sideways-to-up channel; 50d > 200d MA but with periodic 5-7% pullbacks | `ILLUSTRATIVE_REF` | Trend factor positive but momentum tilt moderated |
| Volatility regime | Reference-state VIX in the upper end of the post-2024 distribution; realized > implied at the index level | `ILLUSTRATIVE_REF` | Defensive-quality tilt favored over high-beta crowding |
| Rates regime | Reference-state curve inverted-but-normalizing; 10y around the cycle midpoint; real yields elevated | `ILLUSTRATIVE_REF` | Long-duration tech remains rate-sensitive; bias toward FCF-rich names |
| Dollar regime | DXY in a neutral band, modest USD strength relative to early-2025 | `ILLUSTRATIVE_REF` | Bias against names with heavy EU/FX revenue translation (note LIN exposure) |
| Credit regime | IG/HY spreads compressed but not euphoric; no acute stress signal | `ILLUSTRATIVE_REF` | No credit-driven risk-off signal; permits standard portfolio beta band |
| Sector rotation | Reference-state leadership: Comm Services, Health Care, Industrials; lag: small-cap, regional banks, low-quality cyclicals | `ILLUSTRATIVE_REF` | Aligns with the carry-forward book composition |
| Calendar | Day 4 of the post-Memorial-Day week; FOMC next meeting reference window ~21-23d out | `ILLUSTRATIVE_REF (±2d)` | No FOMC penalty; short-week effect cleared; standard liquidity expected on a normal Friday |
| Single-name event | AVGO reference Q2 fiscal print at ~7d (inside 19-day buffered window) | `ILLUSTRATIVE_REF (±5d)` | Drives AVGO drop |

### Live Intra-Day Fields (Cannot Be Read Without a Feed)

| Field | Status |
|---|---|
| Today's SPY level / change | `N/A` |
| Today's VIX level | `N/A` |
| Today's TLT level | `N/A` |
| Today's DXY level | `N/A` |
| Today's HYG / LQD spread | `N/A` |
| Today's sector ETF intraday breadth | `N/A` |

These would be required to upgrade the regime label confidence above `MEDIUM`.

## Macro Context Note

Reference-state macro is **constructive but not euphoric**. The dominant idiosyncratic risk is AI-capex concentration in mega-cap tech; the dominant macro risk is real-yield sensitivity in long-duration names. The current book responds to both by (a) keeping AI-adjacent exposure to a single name (NOW, with NVDA held out for crowding), (b) overweighting defensive growth (LLY, UNH, LIN), and (c) carrying a cyclical-quality offset (GE) for sector diversification.

## Universe Filter Application

Universe inclusion / exclusion (per `research_system.md` §Universe Construction) applied to the reference-state U.S. primary-listed equity set. Detail in `04_universe_summary.md`. Headline counts:

| Step | Names |
|---|---|
| Reference-state U.S. primary-listed | ≈ 4,800 |
| After market cap > $2B | ≈ 2,100 |
| After ADV > $20M and price > $5 | ≈ 1,600 |
| After listing-age > 6mo and 80% trading sessions filter | ≈ 1,550 |
| After thin-ADR / halted / spread exclusions | ≈ 1,500 |
| Eligible universe passed to factor scoring | **≈ 1,500** |

Counts are reference-state estimates and tagged `ILLUSTRATIVE_REF`. They are stable across the 05-12, 05-24, and today's runs because the underlying reference state has not shifted within a 30-day cadence.

## Event Concentration Risk

Per `01_data_regime_agent.md` task 6:

| Risk class | Status today |
|---|---|
| Clustered earnings (top-20 candidate window) | One name in the 19-day buffered window: **AVGO ~7d**. Triggers the DROP decision in `02_reflection.md`. |
| FOMC clustering | Next reference FOMC ~21-23d out; outside the buffered window; no penalty applied |
| Quarterly-end portfolio rebalancing | Quarter-end is ~32d out; outside the buffered window |
| Options expiry | Monthly OPEX next week (third Friday 2026-06-19 is the next standard); standard cadence; no signal |
| Index rebalance | Russell rebalance reference window ~late-June; outside today's horizon |

## Recommended Run Posture

| Question | Recommendation |
|---|---|
| Proceed to factor scoring? | Yes. The universe is non-empty; the regime label is supportable on reference state; the only event-window flag (AVGO) is handled by the carry-forward decision. |
| Status target? | `REVIEW_ONLY`. `HALTED` is not warranted (mode is explicitly declared, lineage is clear). `GO` is foreclosed by `ILLUSTRATIVE_MODE`. `NO_TRADE` is foreclosed by ≥ 5 names clearing reference-state thresholds. |
| Confidence cap? | `MEDIUM` for clean names; `LOW` for any name inside the 19-day buffered window. AVGO is moot today (dropped). |

## Handoff Note → Factor Scoring Agent

> Eligible universe ≈ 1,500 reference-state names. `NEUTRAL` / `HIGH_VOL` regime; defensive-quality tilt. Cap confidence at `MEDIUM`. Fixed `0.80` data-quality multiplier. Apply the 14-day earnings policy through the 19-day buffered window using `±5d` cadence drift. Carry-forward decisions from `02_reflection.md` are binding: AVGO is `DROP`-flagged at the scoring stage, not at the portfolio stage. Surface 5-10 investable names; do not return empty tables.
