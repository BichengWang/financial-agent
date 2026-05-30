# 01 Preflight

## Run Identity

| Field | Value |
|---|---|
| Date / Time | 2026-05-29 (Friday) 07:27 ET pre-open publish slot |
| Model | claude-opus-4-7 |
| Run mode | `SCHEDULED_DAILY` (cron `56841f5d`, weekdays 27 7 * * 1-5) |
| Effective data mode | `ILLUSTRATIVE` (reference state through ~2026-01) |
| Target run status | `REVIEW_ONLY` |
| Banner | ⚠️ ILLUSTRATIVE — NOT LIVE DATA |

## Data Coverage Audit

Two field classes are tracked separately per `eval/research_system.md` §ILLUSTRATIVE_MODE OP item 3.

### Structural Cadence (Required, Reference-Derived, Tagged `ILLUSTRATIVE_REF (±Nd)`)

| Field | Coverage | Source / Method | Drift band |
|---|---|---|---|
| Next earnings date (DTE) | 100% of investable set | Reference-state Q2 cadence projected forward from today's actual date | `±5d` |
| Next dividend date | Populated where applicable | Reference-state declaration / record cadence | `±5d` |
| FOMC schedule | 100% | Public FOMC calendar (stable for ~2 years out) | `±2d` |
| Options-expiry calendar | 100% | Standard third-Friday cycle (deterministic) | `±0d` |
| Index-rebalance window | 100% | S&P / Russell published windows | `±5d` |

### Intra-Day Live Tape (N/A in `ILLUSTRATIVE_MODE`)

| Field | Coverage | Why N/A |
|---|---|---|
| Today's spot price | 0% | Requires live feed; not wired |
| Today's bid-ask spread | 0% | Requires live feed |
| Today's IV30 | 0% | Requires live options chain |
| Today's volume | 0% | Requires live tape |
| Today's short-interest reading | 0% | Requires bi-weekly print + delta |
| Today's analyst-revision tape | 0% | Requires revision feed |

### Fundamental / Macro Reference State (Tagged `ILLUSTRATIVE_REF`)

| Family | Reference-state coverage | Notes |
|---|---|---|
| Earnings revision momentum | ~95% | Reference-state estimate vintage ~2026-01 |
| Revenue acceleration | ~95% | Same vintage |
| Margin trajectory | ~95% | Same vintage |
| FCF yield vs EV | ~95% | Same vintage |
| Trend / MA alignment | ~90% | Derived from reference-state price path; no live update |
| 60-day β to SPY | ~90% | Reference-state rolling window |
| 30-day realized vol | ~90% | Reference-state |
| Sector membership (GICS) | 100% | Stable mapping |

## Data-Quality Multiplier

Per §ILLUSTRATIVE_MODE OP item 4, the multiplier is **fixed at `0.80`** regardless of family-level coverage. No name in this run can carry `HIGH` confidence; the cap is `MEDIUM`, downgraded to `LOW` for any name flagged by the buffered 19-day earnings window.

## Lineage Validation

| Check | Result |
|---|---|
| Every structured field tagged `LIVE`, `DELAYED`, `ILLUSTRATIVE` (`_REF` variant), or `N/A` | ✓ |
| `00_run_manifest.md` discloses reference vintage | ✓ (through ~2026-01) |
| Structural-cadence fields populated, intra-day live fields `N/A` | ✓ |
| 14-day earnings penalty wired through 19-day buffered window | ✓ |
| Non-fabrication contract preserved | ✓ |

## Freshness Stance

`ILLUSTRATIVE_MODE` is by definition stale relative to today's tape. Per `stop_criteria.md` §Review-Only Mode item 1, the methodology is valid but the evidence is too stale for live positioning. `REVIEW_ONLY` is the correct status; `HALTED` is suppressed because the mode is explicitly declared and the operating procedure is being followed.

## Stop-Criteria Cross-Check

| §Hard Halt criterion | Triggered? | Note |
|---|---|---|
| 1. Live or delayed benchmark missing AND not in `ILLUSTRATIVE_MODE` | ✗ | Mode is explicitly declared. |
| 2. Data lineage unclear for price / volume / β / earnings date | ✗ | Lineage is `ILLUSTRATIVE_REF` with disclosed vintage and `±5d` drift bands; not unclear. |
| 3. >20% of top candidates with unresolved missing critical inputs | ✗ | All 7 names have full structural-cadence coverage. |
| 4. Universe filter leaves too few names | ✗ | Reference-state universe sized adequately (see `04_universe_summary.md`). |
| 5. Portfolio cannot be brought inside risk limits after one revision | ✗ | Inside all hard caps except the 5% single-name cap tension (escalated, not relaxed). |
| 6. Risk committee identifies fabricated / contradictory evidence | ✗ | See `08_risk_review.md`. |

No `HALTED` trigger.

## Handoff to Data and Regime Agent

> Reference vintage disclosed; structural-cadence fields wired; intra-day-live fields `N/A`. Build the eligible universe against the reference-state listed-equity set. Do not return empty tables. Pass forward to factor scoring with the documented `ILLUSTRATIVE_REF` tagging schema.
