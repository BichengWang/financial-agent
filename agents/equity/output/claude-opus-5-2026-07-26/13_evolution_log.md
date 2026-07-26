# 13 Evolution Log — 2026-07-26

## Run Context

| Field | Value |
|---|---|
| Run date / model | 2026-07-26 (Sunday) / `claude-opus-5` |
| Final status | `NO_TRADE` (11th consecutive) |
| Regime | `NEUTRAL` (L139) |
| Evaluation window | All dated packages 2026-07-19 → 2026-07-26, all models |
| Ledger status | EQ raw `n` = **203**, `eff_n` = **1**; MF raw `n` = **36**, `eff_n` = **1**; `due_inventory: 0`, `conflicts: 0` (L138) |
| Baseline flag | `CROSS_MODEL_BASELINE` (`gpt-5-2026-06-28`, exact 0-day hit, age 28d) |
| Track A eligibility | **Blocked** — `INSUFFICIENT_EFFECTIVE_N` on both record types |

## Review Window — Packages Examined

| Package | Status | Relevance |
|---|---|---|
| `gpt-5-2026-07-20` | NO_TRADE | MF calibration diagnosis; bounded second-pass convention |
| `claude-fable-5-2026-07-20`, `-07-21` | NO_TRADE | Sortino downside-deviation fix; Yahoo availability |
| `gpt-5-2026-07-21` | NO_TRADE | — |
| `claude-sonnet-5-2026-07-22`, `gpt-5-2026-07-22` | NO_TRADE | Settlement-timing `TARGET_DATE_CLOSE` mechanism; first rank-inversion observation |
| `gpt-5-2026-07-24` | NO_TRADE | Concurrent Friday package |
| `claude-opus-5-2026-07-24` | NO_TRADE | **Direct predecessor** — same 07-24 price basis; `eff_n` gate accepted; MF root cause diagnosed |
| **`claude-opus-5-2026-07-26`** (this run) | NO_TRADE | 17 settlements; return-basis correction |

**Cross-model divergence:** none material this window. Every model, on every day, reached `NO_TRADE` for the same root cause. That unanimity is itself the diagnostic finding — see `§ Escalation`.

## What Worked

1. **The `eff_n` gate accepted on 2026-07-24 did exactly its job on its first live test.** This run added 17 settlements — raw `n` 189→203, a 7% increase — and `eff_n` stayed at **1**, because the new target date sits 18 days after the earliest settled target date, inside the same 28-day window. Under the old raw-`n`-only rule, a 14-name batch with a dramatic −0.59 rank IC would have been formally eligible to license a Track A parameter change. It is not, and should not be.
2. **Settling under `WEEKEND_TARGET` worked cleanly at scale.** 17 keys with a Sunday `target_date`, all resolved to the 2026-07-24 close, `due_inventory: 0`, `conflicts: 0` on the verification pass. The 2026-07-24 manifest predicted this maturity precisely and it landed as predicted.
3. **Three-source price verification held at 0.0000%** across 17 symbols. On a weekend the `cnbc_last_time` field is what proves the value is Friday's close rather than a stale or after-hours tape — worth keeping as standard practice for non-session runs.
4. **Programmatic table generation caught a real error.** The carry-forward ranks in `02 § 5` were initially hand-written and **every one of the 14 was wrong**; verification against `run_computed_manifest.json` caught it and the table was regenerated from the manifest. Two decisions changed as a result (CVX and GS moved from `DOWNGRADE` to `DROP` on the 60th-percentile floor). This is the 2026-07-15 lesson holding up under pressure.

## What Failed

1. **The composite score's rank ordering is anti-predictive, and the evidence strengthened.** Vintage `gpt-5:2026-06-28` settled at rank IC **−0.5912 (p=0.026, n=14)** — the second significant inversion after 2026-07-22's −0.712. The pooled weighted mean deteriorated from −0.0939 to **−0.1282** across 14 vintages (n=203). Top-7 by score averaged −2.56% alpha; bottom-7 averaged +3.35%.
2. **`MARKET_FORECAST` calibration remains broken.** 22.22% hit rate, mean z −0.7047 across n=36. QQQ and SOXX both missed again today, exactly as the 2026-07-24 root-cause diagnosis predicts.
3. **A data-preparation defect was found in the prior package** — the subject of this run's change, below.
4. **The vendor-empty earnings signature rule fired on weak evidence** for 4 of 24 published names — recorded as an observation, not this run's change.

## Primary Diagnosis

**Category: data quality** — specifically, corporate-action handling in the return series.

Not "factor calibration", despite the rank-inversion finding being the more dramatic result. The reason is the Track A gate: at `eff_n = 1` no calibration change can be validated, so diagnosing calibration would produce a `DEFER` and no improvement. The data-quality defect is (a) real, (b) demonstrably corrupting published numbers, and (c) fixable under Track B with no statistical evidence requirement. It is the highest-value change actually available this run.

## Proposed Change — Track B

> **Compute all return-derived metrics and the technical-indicator pack from adjusted closes (splits, spin-offs, dividends); retain unadjusted closes for `entry_price`, `target_price` and CI bounds.**

### Problem statement (with the artifact that exposed it)

Prior runs computed returns from raw vendor closes. Vendor raw-close series are **not** consistently corporate-action-adjusted, and the two vendors this system uses disagree about *which* events they adjust. Verified bar-for-bar this run (L143, `01 § Corporate-Action Basis`):

| Name | Event | stockanalysis raw `c` | Nasdaq | stockanalysis adjusted `a` |
|---|---|---|---|---|
| HON | distribution ~2026-06-29 | 243.53 → 227.80 (**adjusted**) | 464.42 → 227.80 (**unadjusted**) | 243.53 → 227.80 |
| FDX | FDXF spin-off 2026-06-01 | 411.75 → 338.49 (**unadjusted**) | 325.01 → 338.49 (**adjusted**) | 330.32 → 337.22 |
| SPGI | distribution 2026-07-01 | 407.26 → 414.97 | 399.58 → 414.97 | 385.21 → 414.97 |

Neither raw series is internally consistent — each vendor adjusts one event and not the other. Only the adjusted series is consistent across all three.

**The artifact that exposed it:** `claude-opus-5-2026-07-24/run_computed_manifest.json`, which on *this exact price basis* recorded **HON `sigma_30d` = 0.4428 and `mom60` = −42.90%**. Both are artifacts of an unadjusted distribution, not market moves. On the adjusted basis HON is **0.1147 and +9.49%** — the published sigma was inflated **4.6×**. FDX (`mom60` +2.26% → −19.28% on raw stockanalysis data) and SPGI were affected in the opposite direction.

A 4.6×-wrong sigma is not cosmetic: sigma drives CI bounds, VaR95/CVaR95, Sharpe, Sortino, Kelly and the 30d-realized-vol penalty. A name carrying it would have had a wildly wrong 70% interval and would have been unsettleable in any meaningful sense.

### Hypothesis

Computing returns from adjusted closes removes mechanical corporate-action gaps from every return-derived metric, making momentum, volatility, beta, tracking error and drawdown measure market moves rather than distribution mechanics. Keeping unadjusted closes for entry/target/CI preserves execution realism, since a trader transacts at the unadjusted price.

### Validation (Track B standard — three conditions)

1. **Explicit problem statement citing the artifact that exposed it.** ✅ Above: `claude-opus-5-2026-07-24/run_computed_manifest.json`, HON sigma 0.4428 vs a true 0.1147, with a bar-level three-vendor comparison (L143).
2. **Cannot weaken a protected rule or any grounding gate.** ✅ Touches no factor weight, no mu table, no forecast prior, no risk limit, and no confidence mapping. Grounding is *strengthened*: entry prices remain the 3-source-verified unadjusted closes, and one more ledger row (L143) documents the basis. This is data preparation, not scoring math.
3. **Logged with a `HUMAN_REVIEW` flag, effective next run unless reverted.** ✅ **`HUMAN_REVIEW`** — see below.

**Scope measured, not assumed.** Two distinct comparisons, and they answer different questions — both are reported because quoting only the first would understate the change:

*(a) Against the previously published 2026-07-24 package (also a raw-close basis).* **3 of 514 names differ materially** — HON, FDX, SPGI — all three traceable to corporate actions. This is the "what was wrong before" number.

*(b) Raw basis vs adjusted basis, recomputing all 514 names this run.* The corporate-action correction is large but narrow; the **dividend** component of the adjustment is small but broad, because momentum and relative strength become total-return rather than price-return measures for every dividend payer:

| Change magnitude | Names affected |
|---|---|
| >5% relative sigma **or** >2pp 60d momentum | **9** (CAG, DOC, FDX, FRT, HST, KHC, PFE, SPGI, HON) |
| >2% relative sigma **or** >0.5pp 60d momentum | 207 |
| >1% relative sigma **or** >0.25pp 60d momentum | 313 |

Distribution of the shift: 60d momentum absolute difference **median 0.375pp, p90 1.04pp, max 19.89pp**; sigma relative difference **median 0.0000%, p90 0.946%, max 17.95%**. In other words the typical name moves by roughly its quarterly dividend yield, exactly as expected, while the tail is corporate actions.

**Ranking impact.** Median rank move across all 514 names is **2 places** (p90 9, max 84). The top-30 retains **28 of 30** members: `ACGL` and `ADM` drop out, `FRT` and `KIM` enter. The largest rank move among retained top-30 names is **10 places** (WRB 29→19). TRV remains #1 on both bases.

**Honest characterization:** this is *not* a cosmetic change that leaves the leaderboard untouched. It corrects three genuinely wrong names and shifts most of the book slightly toward total-return momentum. The committee accepted it on correctness grounds — a 4.6×-wrong sigma is indefensible, and a total-return basis applied uniformly is the standard treatment — not on the grounds that it changes nothing.

**Regression evidence.** This run recomputed the entire 2026-07-24 basis through an independent code path: **all 514 closes reproduced exactly** (`last_price` match 514/514), and against the prior package the only material derived-metric differences were the three corporate-action names. That is a clean regression test of the pipeline as well as of this change.

### Decision

**`ACCEPT`** — Track B, flagged **`HUMAN_REVIEW`**, effective this run and forward.

**Effective next step:** future runs should fetch and persist both series — adjusted for all return/indicator math, unadjusted for execution prices — and record the basis in the Source Ledger as this run does (L003 / L002). The 2026-07-24 package's HON, FDX and SPGI figures should be treated as **known-bad on this defect** rather than silently superseded; they are not retro-corrected, because prior packages are immutable.

**Track B budget:** 1 of 1 used.

## Observations Recorded Without a Change

### 1. Rank-order inversion — `DEFER` (Track A blocked at `eff_n = 1`)

**Finding.** Rank IC by vintage is now negative in 10 of 14 vintages, with two significant inversions (−0.712 on 2026-07-22, **−0.5912 p=0.026** today). Pooled weighted mean −0.1282 over n=203.

**Why no proposal.** Two independent reasons, and both matter:

- **Gating:** a Track A calibration proposal requires `eff_n ≥ 3`. `eff_n = 1`. Per `rules.md § Rolling Calibration Metrics` the correct disposition is `DEFER`, not `REJECT`.
- **Diagnostic:** the standing mu-shrink proposal (carried since 2026-07-20) **cannot address this even in principle**. A uniform mu shrink or sigma widening is a monotonic transform of the score; it cannot reorder a ranking. Magnitude miscalibration and rank-order inversion are distinct failure modes and need distinct fixes. The pooled evidence says magnitude is *fine* (mean z −0.2001, CI coverage 75.37%, both inside healthy bands) while ordering is broken. Continuing to propose a magnitude fix for an ordering problem is the error this entry exists to stop.

**What a real fix would need to test,** once `eff_n ≥ 3` (earliest ~2026-09-18): whether the sign of one or more family polarities is wrong in this regime. The disclosed defensive Macro polarity (L140) is the obvious candidate — it is applied as a judgment each run and has never been tested against settled outcomes. That is a falsifiable, ordering-level hypothesis, unlike a mu shrink.

### 2. Vendor-empty earnings signature rule is too permissive — logged for a future Track B

**Finding.** The rule accepted 2026-07-24 classifies a vendor-empty name as post-print if, in the last 12 sessions, there was a 1-day move ≥3.5% **OR** volume ≥1.8× trailing median. The unconditional `OR` on volume fires on non-earnings events. This run:

| Name | Trigger | 1-day move | Verdict |
|---|---|---|---|
| EQR | volume 1.97× | **0.01%** | A flat tape is not an earnings print |
| PKG | volume 2.13× | **0.01%** | Same |
| WRB | volume 2.00× | 2.45% | Weak |
| CB | volume 1.96× | 2.46% | Weak |

All four were routed to the *unpenalized* `ESTIMATED_CADENCE +91d` branch — the less conservative outcome — on that evidence. 4 of 24 published names are affected.

**Why not this run's change:** one Track B per run, and the corporate-action fix corrects larger, demonstrated numerical errors. **Suggested direction for a future run:** require the price-move condition, or require volume **and** a non-trivial (say ≥1.5%) move, rather than an unconditional `OR`. Disclosed in `01 § Known Limitations` #4 and `08 § Additional Findings` #2.

### 3. `MARKET_FORECAST` — no new proposal

Root cause was diagnosed on 2026-07-24 (`mu = beta × SPY_mu` treats beta as a direction predictor) and both candidate fixes were tested and rejected. Today's data is consistent with that diagnosis: SOXX's beta of 3.64 forces a positive mu even after the full −1.5pp adjustment, producing a `FLAT_CALL` on a name that is −19.54% from its 60-day high. Any repair is Track A and gated at `eff_n = 1`. Disclosed in `03` rather than engineered around.

## Escalation — Eleven Consecutive `NO_TRADE` Runs

Not a `§ Freeze Criteria` breach: freeze requires *three consecutive cycles rejecting all changes for lack of evidence*, and changes have been accepted (2026-07-21 Sortino fix, 2026-07-22 settlement timing, 2026-07-24 `eff_n` gate, today's return basis). The loop is improving; it simply cannot trade.

But the record should be plain: **every model, every day, for eleven runs, has reached `NO_TRADE` for the same reason** — `Fund_Z` and `Sent_Z` are unavailable universe-wide, making evidence threshold #2 unreachable by construction and threshold #4 unreachable by arithmetic. No amount of prompt evolution changes this. It is an **engineering unblock**, not a research problem: Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk SEC `companyfacts.zip` + threaded Nasdaq sentiment fetch to ≥70% universe coverage), which has not been attempted.

Recommended as the top priority for the 2026-07-31 monthly structural review, ahead of any further calibration work — which is gated at `eff_n = 1` regardless.

## Mutation Log

| Field | Value |
|---|---|
| **Current problem** | Return-derived metrics computed from raw vendor closes contained mechanical corporate-action gaps; the two vendors adjust different events, so neither raw series is internally consistent |
| **Proposed change** | Adjusted closes for all return/indicator math; unadjusted closes retained for entry/target/CI prices |
| **Validation method** | Bar-level three-vendor comparison across three known events (L143); full 514-name recompute on both bases; independent-code-path regression of the 2026-07-24 basis |
| **Result** | HON sigma 0.4428 → 0.1147 (prior value inflated 4.6×), mom60 −42.90% → +9.49%. 511 of 514 names numerically unchanged. Top-30 leaderboard membership unchanged. All 514 closes reproduced exactly |
| **Decision** | **`ACCEPT`** (Track B, `HUMAN_REVIEW`) |
| **Effective date** | 2026-07-26, this run and forward |

**Deferred this run:** rank-order inversion (Track A, `INSUFFICIENT_EFFECTIVE_N`); `MARKET_FORECAST` mu derivation (Track A, `INSUFFICIENT_EFFECTIVE_N`); earnings-signature tightening (Track B, budget exhausted).
