# 03 Regime And Data

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Regime label and evidence are derived from training-data reference state, not from a live tape. Tagged `ILLUSTRATIVE_REF` throughout.

## Declaration

| Field | Value |
|---|---|
| Data state | `ILLUSTRATIVE` |
| Reference vintage | Training data through ~2026-01 |
| Regime label | `NEUTRAL` with a `HIGH_VOL` tilt |
| Confidence | `MEDIUM` (capped per `ILLUSTRATIVE_MODE` rules) |
| Eligible to recommend trades | No — `REVIEW_ONLY` only |

## Regime Reasoning

Reference-state characterization, all `ILLUSTRATIVE_REF`:

- Broad equity trend: SPY trading near multi-quarter highs; 50/200-day MAs both rising. Net trend signal: mildly positive.
- Volatility regime: VIX in the high teens to low 20s, MOVE elevated relative to the 2017-2019 baseline. Net vol signal: cautious — supports a `HIGH_VOL` tilt without committing to it.
- Rates regime: Fed in a measured easing posture from peak rates; long end sticky. Real yields off their highs but still positive.
- Dollar regime: DXY mid-range, FX vol contained.
- Credit regime: HY OAS tight; investment-grade spreads near cycle averages. No obvious credit-market stress.

The composite implication is `NEUTRAL` with a `HIGH_VOL` tilt: trend is supportive, but vol/rate sensitivity argues against high-beta crowding.

## Regime Evidence Table

| Signal | Threshold For Label | Reference-State Reading | Tag |
|---|---|---|---|
| SPY 50/200-day MA cross | Above both → `BULL`; below both → `BEAR` | Above both | `ILLUSTRATIVE_REF` |
| SPY trailing-20d realized vol | >20% annualized → `HIGH_VOL` consideration | Mid-teens; below threshold | `ILLUSTRATIVE_REF` |
| VIX level | >25 → `HIGH_VOL`; >35 → strong bear bias | High-teens to low-20s; near `HIGH_VOL` boundary | `ILLUSTRATIVE_REF` |
| VIX term structure | Backwardation → `HIGH_VOL` consideration | Mild contango; not in stress | `ILLUSTRATIVE_REF` |
| MOVE index | >120 → `RATE_SHOCK` consideration | Elevated but below 120 | `ILLUSTRATIVE_REF` |
| UST 2s10s slope | Sharp re-steepening or deepening inversion → rate stress | Modestly positive, stable | `ILLUSTRATIVE_REF` |
| HY OAS, weekly Δ | Widening >50 bps in 5 sessions → bear bias | Tight; not widening | `ILLUSTRATIVE_REF` |
| DXY, weekly Δ | >2% in 5 sessions → cross-asset stress | Range-bound | `ILLUSTRATIVE_REF` |
| Sector breadth (% of XL\* > 50DMA) | <30% → bear; >70% → bull | ~55-65% | `ILLUSTRATIVE_REF` |
| Cross-sectional dispersion | Top decile > vol-of-vol cohort → factor regime shift | Elevated; rewards stock-picking | `ILLUSTRATIVE_REF` |

## Macro Context

Reference-state characterization. Not a live macro call:

- AI-capex cycle still central to sector leadership; concentration risk remains the dominant headline risk for index beta.
- Fed posture supports duration but introduces convexity risk in long-duration growth.
- Consumer signals are mixed; staples and discretionary are diverging within the same GICS L1.
- Geopolitical/energy risk is non-zero but not pricing as crisis.

## Sector Posture

| Sector | Reference-state posture | Use in scoring |
|---|---|---|
| Information Technology | Leadership (AI-capex), but crowded | Demand factor confirmation; beware concentration |
| Communication Services | Mixed; mega-cap leadership masks dispersion | Stock-picker's tape |
| Health Care | Defensive bid; large-cap pharma re-rating | Eligible for diversification |
| Industrials | Capex beneficiaries (electrification, automation) | Selectively constructive |
| Financials | Range-bound; rate-curve sensitive | Selectively constructive |
| Consumer Discretionary | Bifurcated; quality bias | Quality-only |
| Consumer Staples | Defensive | Diversifier |
| Energy | Range-bound | Avoid unless vol-compression setup |
| Materials | Cycle-late | Constructive for inflation hedges (Linde) |
| Utilities | AI-power-demand re-rating ongoing | Diversifier |
| Real Estate | Rate-sensitive | Avoid |

## Event Concentration Risks

| Risk vector | Status |
|---|---|
| Cluster of mega-cap earnings within 14 calendar days | `ILLUSTRATIVE_REF (±5d)` — derived from stable historical quarterly-reporting cadence relative to today's date. (AVGO near print, NVDA near print) |
| FOMC / payrolls / CPI within 14 calendar days | `N/A` — calendar not wired |
| Quad-witch or quarterly index rebalance | `N/A` — calendar not wired |

Per the corrected `ILLUSTRATIVE_MODE` operating procedure, structural cadence dates are allowed and populated with a `±5d` drift buffer to ensure earnings event penalties can fire correctly, while intra-day live tape metrics remain `N/A`.

## Cross-Reference To Stop Criteria

- §Hard Halt item 1: not triggered — `ILLUSTRATIVE_MODE` is explicit.
- §Hard Halt item 2: not triggered — lineage is "training-data reference state," disclosed.
- §Review-Only Mode item 1: triggered — methodology valid, data is reference-state.

## Handoff Note → Factor Scoring Agent

> Use a `NEUTRAL` regime with a `HIGH_VOL` tilt. Run all four factor families against reference-state inputs. Apply the fixed `0.80` data quality multiplier per `ILLUSTRATIVE_MODE` rules. Cap confidence at `MEDIUM` for every name. Avoid AI-capex single-stock crowding when constructing the investable subset. Ensure structural cadence is used to check for upcoming earnings.
