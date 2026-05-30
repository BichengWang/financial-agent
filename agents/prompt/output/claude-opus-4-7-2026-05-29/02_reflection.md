# 02 Reflection — Month-over-Month Comparison

⚠️ ILLUSTRATIVE — NOT LIVE DATA. This reflection runs in `ILLUSTRATIVE_MODE`. Price-level MoM comparisons require a live or delayed feed that is not wired; affected cells are marked `UNAVAILABLE` per the non-fabrication contract in `eval/research_system.md`. Process-level and thesis-level MoM are fully populated.

## 1. Prior Run Summary

### Primary Baseline (closest available to "approximately one month prior")

| Field | Value |
|---|---|
| Path | `/Users/mac/my-code/diary/investments/equity/prompt/output/claude-opus-4-7-2026-05-12/` |
| Date | 2026-05-12 |
| Days prior to today | 17 calendar days (closest same-model run to the ~30-day target; no claude-opus-4-7 run exists at ~30d back) |
| Model | claude-opus-4-7 (match) |
| Final status | `REVIEW_ONLY` |
| Run mode | `ILLUSTRATIVE` |
| Regime classification | `NEUTRAL` (low confidence; placeholder) |
| Prior portfolio | **None** — investable set was empty; the artifact was a schema-demo with placeholder names (MSFT, NVDA, META, GOOGL, AMZN) tagged `LOW` confidence |
| Prior composite top 5 | MSFT (+1.18 / +0.83 / pctl 99) · NVDA (+1.18 / +0.83 / 99) · META (+1.13 / +0.79 / 98) · GOOGL (+1.02 / +0.71 / 97) · AMZN (+0.96 / +0.67 / 96) — all placeholder, not theses |

### Cross-Check Baseline (5 days prior, first post-fix illustrative run)

| Field | Value |
|---|---|
| Path | `/Users/mac/my-code/diary/investments/equity/prompt/output/claude-opus-4-7-2026-05-24/` |
| Date | 2026-05-24 |
| Days prior to today | 5 calendar days |
| Model | claude-opus-4-7 (match) |
| Final status | `REVIEW_ONLY` |
| Run mode | `ILLUSTRATIVE` (first run after `ILLUSTRATIVE_MODE` OP fix) |
| Regime classification | `NEUTRAL` with `HIGH_VOL` tilt (reference-state) |
| Prior portfolio | 8 names: META (12%) · LLY (9%) · NFLX (11%) · NOW (10%) · UNH (16%) · AVGO (5%, skip-the-print) · GE (16%) · LIN (21%) |
| Prior composite top 5 | META (+1.85 / +1.48 / 99) · LLY (+1.78 / +1.42 / 98) · NFLX (+1.65 / +1.32 / 97) · NOW (+1.55 / +1.24 / 96) · UNH (+1.48 / +1.18 / 95) |

The 05-24 baseline is used as the working carry-forward source because the 05-12 baseline contains no investable names. The 05-12 baseline is retained for *process* MoM (loop fix, schema audit) only.

## 2. MoM Price & Return Table

Per `main.md` §Reflection Required Sections item 2. Affected cells are marked `UNAVAILABLE` per the non-fabrication contract; today's spot prices cannot be cited because no live feed is wired.

### Against 05-12 Primary Baseline (17-day window)

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | Hit / Miss | Notes |
|---|---|---|---|---|---|---|---|
| MSFT | 2026-05-12 | `N/A` (placeholder) | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | 05-12 was schema-demo; no position taken; no thesis |
| NVDA | 2026-05-12 | `N/A` (placeholder) | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| META | 2026-05-12 | `N/A` (placeholder) | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| GOOGL | 2026-05-12 | `N/A` (placeholder) | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| AMZN | 2026-05-12 | `N/A` (placeholder) | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |

Process MoM only against the 05-12 baseline; price MoM is structurally `UNAVAILABLE` because the 05-12 run did not produce real candidates.

### Against 05-24 Cross-Check Baseline (5-day window)

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | Hit / Miss | Notes |
|---|---|---|---|---|---|---|---|
| META | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | `REVIEW_ONLY` — no position taken; thesis intact on reference state |
| LLY | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| NFLX | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| NOW | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| UNH | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| AVGO | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | `REVIEW_ONLY` and skip-the-print sizing only; reference Q2 print was ~12d out at 05-24, now ~7d out |
| GE | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |
| LIN | 2026-05-24 | `UNAVAILABLE` | 2026-05-29 | `UNAVAILABLE` | `UNAVAILABLE` | `Neutral` | Same |

Per `main.md` §Reflection Required Sections item 2 final clause, `APPROX` requires a stated source. With no source, the correct tag is `UNAVAILABLE`. Fabricating an "APPROX" price from training-data state would violate the non-fabrication contract.

## 3. Theme-Level Performance Summary

Each cluster carried from the 05-24 cross-check. Validation is **on the reference-state thesis itself**, not on realized 5-day returns (which require a feed).

| Theme | 05-24 Names | Status | Reference-state evidence | Evidence quality |
|---|---|---|---|---|
| Mega-cap growth / margin compounding | META, NFLX, NOW | Validated | Reference-state revisions remain positive; margin trajectory intact; AI-attach narrative still supportive | `ILLUSTRATIVE_REF` — no live update |
| Defensive growth (HC + Materials) | LLY, UNH, LIN | Validated | Reference-state GLP-1 / oncology pipeline and Optum diversification still intact; LIN low-vol diversifier role unchanged | `ILLUSTRATIVE_REF` |
| Cyclical quality (Industrials) | GE | Validated | Aerospace mid-cycle thesis unchanged on reference state | `ILLUSTRATIVE_REF` |
| AI-adjacent single name | AVGO | **Partially validated → event window dominates** | Reference Q2 fiscal print at ~7d; thesis intact but event-risk discipline supersedes for the 2-6 week horizon | `ILLUSTRATIVE_REF (±5d)` |

No theme is marked "failed" today. The AVGO partial-validation maps to a portfolio action (DROP), not a thesis revision.

## 4. Regime Shift Assessment

| Dimension | 05-12 baseline | 05-24 cross-check | Today (2026-05-29) | Change |
|---|---|---|---|---|
| Regime label | `NEUTRAL` (low conf) | `NEUTRAL` with `HIGH_VOL` tilt | `NEUTRAL` with `HIGH_VOL` tilt | No change (reference state) |
| VIX regime | Unmeasured | Reference-state elevated | Reference-state elevated | No change |
| Rates / yield curve | Unmeasured | Reference-state inverted-but-normalizing | Reference-state inverted-but-normalizing | No change |
| Macro risk dominant | Unverifiable | AI-capex concentration | AI-capex concentration | No change |
| Calendar-driven factor | None noted | Memorial Day approach | Post-Memorial-Day, pre-FOMC window | Modest: short-week effect cleared |

**Factor-weighting implication**: No re-weighting today. Family weights remain at the §Factor Architecture baseline (`Fundamental 0.30 / Technical 0.30 / Sentiment 0.25 / Macro 0.15`). The autonomous mutation scope (`±0.05` per family per day) is not used because (a) no realized observations exist to justify it, and (b) the `ILLUSTRATIVE_MODE` posture caps confidence at `MEDIUM` regardless.

## 5. Carry-Forward Decisions (Binding Input to `05_factor_scores.md`)

| Ticker / Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| META | +1.48 (05-24) | Reels / ad-pricing trend, margin compounding | `UNAVAILABLE` | `CARRY` | Thesis intact on reference state; no event inside 19-day buffered window; correlation cluster acceptable |
| LLY | +1.42 (05-24) | GLP-1 / oncology revisions, capacity expansion | `UNAVAILABLE` | `CARRY` | Defensive-growth role intact; DTE ~70d on reference cadence |
| NFLX | +1.32 (05-24) | ARPU acceleration, content efficiency | `UNAVAILABLE` | `CARRY` | Thesis intact; DTE ~49d on reference cadence |
| NOW | +1.24 (05-24) | Large-deal momentum, AI attach | `UNAVAILABLE` | `CARRY` | Thesis intact; DTE ~55d; correlation with mega-cap-growth cluster watched but inside the 0.45 cap |
| UNH | +1.18 (05-24) | Mean-reversion, Optum diversification, defensive | `UNAVAILABLE` | `CARRY` | Defensive role intact; DTE ~47d on reference cadence |
| **AVGO** | **+1.28 (05-24)** | **AI-networking, software diversification** | `UNAVAILABLE` | **`DROP`** | **Reference Q2 fiscal print at ~7d. Inside 14d policy window and 19-day buffered window. Skip-the-print sizing at 5% no longer survives the proximity; event-window discipline supersedes. Re-rate post-print at next live attempt on or after 2026-06-08.** |
| GE | +1.14 (05-24) | Aerospace mid-cycle, services mix | `UNAVAILABLE` | `CARRY` | Thesis intact; DTE ~54d on reference cadence |
| LIN | +1.10 (05-24) | Defensive growth, low-vol diversifier | `UNAVAILABLE` | `CARRY` | Thesis intact; DTE ~64d; portfolio-vol diversifier role unchanged |
| NVDA (near-miss) | n/a | AI-capex / data-center | `UNAVAILABLE` | `HOLD-OUT` (not `PROMOTE`) | NVDA reference Q1 print was ~3d at 05-24, now done on reference cadence (~3 days past). Post-print eligibility restored, but adding NVDA would re-introduce AI-capex correlation crowding with NOW. Logged for re-review at next run if AVGO returns post-print. |
| MSFT / TMO / INTU / PGR / CDNS / ADBE (near-miss) | n/a | Various | `UNAVAILABLE` | `HOLD-OUT` | None cleared the crowding / doublet test relative to the remaining 7-name book. |
| Theme: Mega-cap growth | n/a | Margin / FCF compounding | `UNAVAILABLE` | `CARRY` | Intact on reference state |
| Theme: Defensive growth | n/a | HC + Materials | `UNAVAILABLE` | `CARRY` | Intact on reference state; absorbs the AVGO drop |
| Theme: Cyclical quality | n/a | Aerospace | `UNAVAILABLE` | `CARRY` | Intact on reference state |
| Theme: AI-adjacent | n/a | Networking + software | `UNAVAILABLE` | `PAUSED` | One-name expression (AVGO) is paused until post-print |

**Net effect on today's investable set**: 8 → 7 names (AVGO out, no promotion). Carry-forward decisions are binding inputs to `05_factor_scores.md` and `06_top_candidates.md`. The portfolio agent in `07_portfolio_proposal.md` redistributes AVGO's 5% pro-rata across the remaining 7.

## 6. Reflection Sign-Off

### Data quality note

| Field class | Status |
|---|---|
| Prior 05-12 prices | `UNAVAILABLE` — baseline contained placeholders only |
| Prior 05-24 prices | `UNAVAILABLE` — `ILLUSTRATIVE_MODE` baseline; no live entry prices to cite |
| Today's spot prices | `UNAVAILABLE` — no live feed |
| Reference-state cadence (DTE, FOMC) | `ILLUSTRATIVE_REF (±5d)` — populated, used to wire the 14-day earnings policy |

### Confidence in this reflection

**MEDIUM** (capped by `ILLUSTRATIVE_MODE`). Rationale:

- **Pro**: same-model baseline available; reference-state theses are internally consistent; the AVGO event-window decision is grounded in a deterministic cadence calculation, not a guess.
- **Con**: no realized returns to validate carry-forward decisions against; the 17-day primary-baseline gap and the structurally empty 05-12 candidate set limit MoM signal strength.

### Structural issues discovered

1. **05-12 baseline is structurally pre-fix**, so it cannot serve as a price-MoM source even hypothetically. The next monthly run (e.g., 2026-06-12) will be the first with a same-model baseline that was itself a real `ILLUSTRATIVE_MODE` run.
2. **No claude-opus-4-7 run exists at ~30 days back**. The closest same-model prior is 17 days back. This is a *cadence* gap, not a methodology gap; the system has only existed for two same-model dated runs (05-12 and 05-24) before today.
3. **Output-spec layout tension** between `main.md` (14 files) and `daily_output_spec.md` (13 files) escalated in `00_run_manifest.md` §Spec Tensions and `13_evolution_log.md`. Today follows the `main.md` 14-file layout because the cron prompt is explicit about that.
4. **5% single-name cap geometric infeasibility** restated; today's book breaches the cap on every name (max 22% LIN, single name reduction from 21% as AVGO's 5% redistributes). Escalated to next monthly structural review; not relaxed.

### Handoff Note

> Carry-forward decisions are binding. Factor scoring agent must (a) drop AVGO from the investable subset on event-risk grounds (DTE ~7d on reference cadence), (b) keep the other 7 names at their 05-24 rank ordering modulo today's score recompute, (c) not add a new name without explicit evidence of a regime/factor shift that outweighs the crowding risk, and (d) tag every numeric field per the §ILLUSTRATIVE_MODE OP item 3 split.
