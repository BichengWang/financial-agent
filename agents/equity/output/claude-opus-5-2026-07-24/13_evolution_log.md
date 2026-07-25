# 13 Evolution Log — 2026-07-24

## Run Context

| Field | Value |
|---|---|
| Run date | 2026-07-24 (Friday, post-close ~23:17 ET) |
| Model | claude-opus-5 |
| Final status | `NO_TRADE` |
| Regime | `NEUTRAL` (index) with extreme internal dispersion |
| Evaluation window | 2026-07-17 → 2026-07-24, all models (9 packages incl. this run) |
| Ledger status | All 5 Required inputs grounded; `Fund_Z`/`Sent_Z` `UNAVAILABLE`; 148 ledger rows |
| Baseline flag | `CROSS_MODEL_BASELINE` (`gpt-5-2026-06-24`) |
| Settled this run | 0 (`due_inventory 0`, verified) |

## Review Window — Cross-Model Evidence

| Model | Date | Status | Predictions |
|---|---|---|---|
| gpt-5 | 2026-07-17 | `NO_TRADE` | 23 |
| claude-fable-5 | 2026-07-17 | `NO_TRADE` | 26 |
| gpt-5 | 2026-07-20 | `NO_TRADE` | 26 |
| claude-fable-5 | 2026-07-20 | `NO_TRADE` | 36 |
| gpt-5 | 2026-07-21 | `NO_TRADE` | 26 |
| claude-fable-5 | 2026-07-21 | `NO_TRADE` | 23 |
| gpt-5 | 2026-07-22 | `NO_TRADE` | 29 |
| claude-sonnet-5 | 2026-07-22 | `NO_TRADE` | 29 |
| **claude-opus-5** | **2026-07-24** | **`NO_TRADE`** | **29** |

**Nine consecutive `NO_TRADE` packages across three model families.** There is zero cross-model divergence on status, and the stated cause is identical in every one: `Fund_Z`/`Sent_Z` unavailable → evidence threshold #2 unreachable. This unanimity is itself diagnostic — the blocker is structural and tooling-shaped, not a judgment difference between models. **No run in the window attempted Phase 2** of the SHADOW promotion plan, which is the only thing that would change the outcome.

## What Worked

- **Post-close firing gave a single clean price basis.** Firing ~7 hours after the bell let Nasdaq's bulk historical endpoint supply the same-day close for all 520 symbols, eliminating the split technical/entry price basis the 07-17 and 07-22 at-close runs (~16:4x ET fires) had to carry and reconcile. Recommend future at-close runs fire late rather than immediately after the bell.
- **Three-source price verification at zero variance.** Nasdaq + stockanalysis.com + cnbc.com agreed to the cent on all 29 published prices. stockanalysis.com and CNBC are both new to this stack and both worked while Yahoo was 429-blocked; they are materially better fallbacks than the single-vendor cross-checks used since 07-13.
- **Programmatic table generation** (07-15 precedent) again produced zero transcription errors across ~250 numeric cells.
- **The constraint feasibility pre-check earned its keep.** It surfaced a second, fully independent reason for `NO_TRADE` — beta-band infeasibility — that the scoring stage could not have found, and it did so without spending the revision pass.

## What Failed

- **`MARKET_FORECAST` calibration remains broken**: 21.21% hit rate, mean z −0.731 over n=33. Flagged in the 07-20 and 07-22 logs; still unresolved.
- **Rank IC is negative** (−0.0939 weighted). The prior run's #1 name (CAT, adj score 100.0) now ranks 482/514 — the composite's rank ordering is not yet predictive.
- **The SPY forecast opted out of direction scoring.** `mu` landed at exactly 0.00%, so `|mu| < 0.5%` → `N/A - FLAT_CALL`. Legal and disclosed, but a rule that lets a forecast avoid being scored is a calibration leak worth noting.

## Primary Diagnosis: **factor calibration** — specifically, *the evidence base cannot support the calibration changes it keeps inviting*

`rules.md § Evolution Agent § Tasks` #3 imposes a priority override: with rank IC ≤ 0 over ≥20 settled predictions, this run's change **must** address calibration before anything else. Two calibration corrections were designed, tested, and **rejected**; the accepted change addresses the reason they could not be evaluated honestly.

### Root-cause analysis of the `MARKET_FORECAST` failure

Decomposition by ETF (`02 § 0`):

| ETF | approx. beta | mean mu | mean realized | Direction |
|---|---|---|---|---|
| SPY | 1.0 | +1.86% | +0.35% | 6 HIT / 5 MISS |
| QQQ | ~1.7 | +2.99% | −3.65% | 1 HIT / 10 MISS |
| SOXX | ~3.6 | +5.60% | −12.73% | **0 HIT / 11 MISS** |

**SPY's own regime-prior forecast is acceptable.** The failure scales precisely with beta. The mechanism is structural: `rules.md § Core ETF Market Forecast` sets `mu_ETF = beta_to_SPY × SPY_mu`, adjustable ±1.5pp. Because every regime prior except `RATE_SHOCK`/`BEAR` is non-negative, multiplying a positive SPY prior by a beta ≥1 produces a *large positive* forecast on exactly the highest-volatility, most-drawdown-prone assets — and the ±1.5pp band is far too narrow to bring it back to zero. With SPY at the `BULL` prior of +2.0%, SOXX's base mu is +7.2% and the band floor is +5.7%: **a bearish SOXX view is unrepresentable.** 100% of the 33 forecasts carried positive `mu`; 21% of realized returns were positive.

Beta measures co-movement *magnitude*, not expected-return *direction*. Using it as a return multiplier is a category error.

### Track A candidate #1 — damp the beta amplification — **REJECTED**

Counterfactual `mu'(λ) = SPY_mu + λ·(mu_recorded − SPY_mu)`; λ=1 is status quo, λ=0 gives every ETF SPY's mu. Scored on all 33 canonical settlements per `§ Settlement Rules`.

| λ | n directional | Hit rate | CI coverage | Mean z |
|---|---|---|---|---|
| **1.00 (status quo)** | 33 | **21.2%** | 63.6% | −0.731 |
| 0.75 | 33 | 21.2% | 69.7% | −0.702 |
| 0.50 | 33 | 21.2% | 69.7% | −0.673 |
| 0.25 | 33 | 21.2% | 72.7% | −0.644 |
| 0.00 | 33 | **21.2%** | 75.8% | −0.615 |

**Hit rate is unchanged at every λ (+0.0pp).** Damping shrinks magnitude toward a *still-positive* SPY mu, so every direction call keeps its sign and every miss stays a miss. CI coverage and mean z improve, but neither is an acceptance criterion, and CI coverage at 63.6% was already inside the healthy band. Fails the Acceptance Standard (needs ≥+2pp hit rate or ≥+0.05 IR). **This reproduces the 07-20 finding that a −0.5pp mu shrink was rejected for the same reason: magnitude adjustments cannot repair a directional failure.**

### Track A candidate #2 — replace beta with own-trend amplification — **REJECTED**

`mu' = SPY_mu + θ·RS20(ETF vs SPY)`, with RS20 recomputed from bars **at or before each vintage date** (no lookahead). Unlike beta, RS20 can be negative, so this rule *can* express a bearish view.

| Rule | Hit rate | CI coverage | Mean z |
|---|---|---|---|
| CURRENT (beta × SPY_mu) | 21.2% | 63.6% | −0.731 |
| θ = 0.25 | 21.2% | 69.7% | −0.727 |
| θ = 0.50 | 21.2% | 57.6% | −0.839 |
| θ = 1.00 | 21.2% | 54.5% | −1.063 |
| θ = 1.50 | 21.2% | 42.4% | −1.286 |

Leave-one-vintage-out rolling validation at θ=1.0: pooled **7/33 = 21.2%**, no vintage better than 2/3.

**Also +0.0pp, and it degrades CI coverage as θ rises.** The reason is decisive: **mean RS20 at the vintage dates was +19.58% for SOXX and +2.36% for QQQ.** At the moment those forecasts were made, semis had been *outperforming strongly*. A trend rule would have made SOXX's mu *more* positive, not negative. The mid-July drawdown was a **reversal**, and neither beta nor trend — the only two ETF-level signals the spec has — could have anticipated it. Fails the Acceptance Standard. **REJECTED.**

### The finding that both rejections expose

Both tests were run against `n=33` settlements, which nominally clears the Track A bar of "≥20 settled prediction records". That bar is **numerically satisfied and statistically vacuous here**:

| Type | n | Distinct vintages | Vintage span | Target span | Non-overlapping 28d target windows |
|---|---|---|---|---|---|
| `MARKET_FORECAST` | 33 | 10 | 2026-06-14 → 06-24 (10d) | 2026-07-12 → 07-22 | **1** |
| `EQUITY_ALPHA` | 189 | 12 | 2026-06-10 → 06-24 (14d) | 2026-07-08 → 07-22 | **1** |

Every canonical settlement in the system comes from a **single overlapping forecast cohort**: near-identical forecasts issued on consecutive days in mid-June, all resolving into one two-week window in mid-July. The 33 market-forecast "observations" are approximately **one market call** — the mid-July growth/semis reversal — repeated 33 times. Likewise `n=189` for equities.

This explains the whole pattern. It is why both of today's candidates produce *identical* 21.2% hit rates: they are being fitted to one event, and no reparameterisation of a single event can generalise. It is why the 07-20 mu-shrink failed. And it is why `n ≥ 20` has been licensing Track A experiments that the data cannot actually adjudicate — the exact overfitting risk `rules.md § Anti-Overfitting Rules` exists to prevent ("Do not optimize to a single recent regime").

## Proposed Change (ACCEPTED) — Track B

**Report effective independent sample size alongside raw `n`, and gate Track A changes on it.**

1. `settlement_ledger.py`'s `rolling_metrics` block gains an **`eff_n`** field per record type: the count of **non-overlapping target-date windows** of length equal to the forecast horizon (28 days) spanned by that type's canonical settlements.
2. `02_reflection.md § 0` and `00_run_manifest.md` must report `eff_n` next to `n` in the rolling-calibration table.
3. **A Track A change to the mu Calibration Table or the Core ETF mu prior table requires `eff_n ≥ 3`**, in addition to the existing `n ≥ 20`. Below that, calibration findings are logged as observations and the change is `DEFER`, not `REJECT` — the evidence is absent, not contrary.

### Classification and acceptance

**Track B — process change.** It alters reporting, a schema field, and an evidence gate. It changes **no** scoring formula, factor weight, forecast prior, sigma sourcing, or risk limit.

Against `rules.md § Evolution Policy` Track B's three-condition standard:

1. **Explicit problem statement citing the exposing artifact** — `settlement_manifest.json` from this run: 33 and 189 canonical settlements spanning 10 and 12 vintages within 10- and 14-day windows, collapsing to 1 effective window each (ledger row L143).
2. **Cannot weaken a protected rule or grounding gate** — it strictly *raises* the evidence bar for parameter mutation. No protected rule is touched.
3. **Logged with `HUMAN_REVIEW`, effective next run unless reverted** — see below.

**Decision: `ACCEPT`.** Flag: **`HUMAN_REVIEW`**. Effective: next run. One Track B change this run, within the limit.

### Hypothesis (falsifiable)

If calibration statistics are gated on effective independent sample size, then Track A proposals will stop being generated against pseudo-replicated evidence, and the next accepted Track A change will be one whose out-of-sample behaviour actually holds. Falsified if a change accepted under `eff_n ≥ 3` still fails out-of-sample as badly as the λ and θ candidates did today.

### Why this over the direct calibration fix

The priority override demands a calibration change. Two were built and tested; both failed their bars, and the reason they failed is that the evidence base cannot distinguish a good ETF-mu rule from a bad one right now. Accepting a change that "looks better" on this sample would be fitting the mid-July reversal. **The honest calibration action available today is to fix how calibration evidence is counted, so the real fix can be made when the data can support it.** The underlying beta-multiplier flaw is fully diagnosed above and is now queued with a concrete, pre-registered hypothesis rather than being changed blind.

## Not Adopted This Run (recorded, not proposed)

- **Beta-multiplier replacement in `§ Core ETF Market Forecast`.** Diagnosis is complete and compelling; both candidate replacements failed testing. Revisit when `eff_n ≥ 3` — realistically once forecasts from late July and August settle into distinct windows. Queue for the 2026-07-31 structural review.
- **`|mu| < 0.5%` FLAT_CALL escape.** Today's SPY forecast used it legitimately, but a forecast able to opt out of direction scoring weakens the calibration record. Note for structural review; not proposed now (one Track B per run).
- **`Fund_Z`/`Sent_Z` Phase 2 promotion.** Still the only change that would end the `NO_TRADE` streak. Not an evolution-policy change — it is engineering work specified in `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`, untouched for nine consecutive packages across three model families.

## Freeze-Criteria Check

| Criterion | Status |
|---|---|
| Three consecutive cycles rejecting all changes for lack of evidence | **No** — 07-21 accepted the Sortino fix, 07-22 accepted the settlement-timing adoption, this run accepts a Track B change |
| Two accepted changes in a row worsening out-of-sample performance | **No** |
| Weights/thresholds oscillating without stable improvement | **No** — no weight or threshold has been mutated |

**Not frozen.** Parameter mutation remains permitted, now under a stricter evidence gate.

## Mutation Log

| Field | Value |
|---|---|
| **Current problem** | Rolling calibration reports raw `n` (189 equity, 33 market forecast) that overstates independent evidence by ~2 orders of magnitude; all settlements derive from one overlapping forecast cohort resolving in a single window, licensing Track A changes the data cannot adjudicate |
| **Proposed change** | Add `eff_n` (non-overlapping 28-day target windows) to `settlement_ledger.py § rolling_metrics`; report it beside `n` in `02` and `00`; require `eff_n ≥ 3` in addition to `n ≥ 20` before any Track A change to the mu Calibration Table or Core ETF mu prior table |
| **Track** | **B** (process/schema/evidence-gate; no scoring math altered) |
| **Validation method** | Direct measurement on this run's `settlement_manifest.json`; plus two Track A candidates tested against the same data (λ-damping and θ-trend), both returning identical 21.2% hit rates — demonstrating the sample cannot discriminate between rules |
| **Result** | λ-damping: +0.0pp hit rate at every λ → REJECT. θ-trend: +0.0pp hit rate, CI coverage degrades with θ, LOVO pooled 7/33 → REJECT. Effective-N measurement: MF 33→1 window, EQ 189→1 window |
| **Decision** | **ACCEPT** the Track B change; **REJECT** both Track A candidates |
| **Effective date** | Next run (2026-07-27 or earlier), flagged `HUMAN_REVIEW` |
