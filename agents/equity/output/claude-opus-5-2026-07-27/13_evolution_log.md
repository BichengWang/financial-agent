# 13 Evolution Log — 2026-07-27

## Run Context

| Field | Value |
|---|---|
| Run date | 2026-07-27 (Monday, intraday fire ~09:55 ET) |
| Model | `claude-opus-5` |
| Final status | `NO_TRADE` |
| Regime | `NEUTRAL` |
| Evaluation window | 2026-07-20 → 2026-07-27, all models |
| Ledger status | `EQUITY_ALPHA` n=231, `eff_n`=1 · `MARKET_FORECAST` n=42, `eff_n`=1 |
| Track A eligibility | **blocked** — `INSUFFICIENT_EFFECTIVE_N` for both record types |
| Baseline flag | `CROSS_MODEL_BASELINE` (`gpt-5-2026-06-29`) |
| Settlements this run | 0 (due inventory 0; the concurrent `gpt-5-2026-07-27` pre-open run settled all 34 matured keys) |

## Review Window

All dated packages from 2026-07-20 through 2026-07-27, every model: `gpt-5` (07-20, 07-21, 07-22, 07-24,
07-27), `claude-fable-5` (07-22), `claude-sonnet-5` (07-22), `claude-opus-5` (07-24, 07-26, and this
run). **Every package in the window published `NO_TRADE`.** Cross-model divergence is immaterial to
the root blocker — all models are stopped by the same missing factor families, which is itself the
most important cross-model finding available: the blocker is infrastructural, not a difference of
judgement.

## What Worked

1. **Independent reproduction of a prior package's scoring layer.** This run's engine was written from
   `rules.md` plus the `claude-opus-5-2026-07-26` methodology disclosure and reproduces that package
   exactly on the shared 2026-07-24 basis — TRV `Adj Score` +0.3705, `Tech_Z`
   +1.1240, `Macro_Z` +0.8397, beta
   -0.7014, sigma 0.0933, universe median sigma
   0.0961. A methodology disclosure detailed enough to be reproduced from is
   worth more than the numbers themselves, and this is the first run to demonstrate it end-to-end.
2. **The intraday CNBC field inversion was anticipated and handled.** The 2026-07-24 package logged
   that `previous_day_closing` manufactures fake divergences on a post-close run. On an *intraday*
   fire that inverts: `previous_day_closing` is precisely the last completed close. Both fields were
   captured and used for their own purpose; 27
   of 28 symbols agreed
   to the cent.
3. **Three independent price sources on a session where two bulk feeds were down.** Yahoo was
   429-blocked (8th of the last 14 sessions) and Nasdaq's bulk-historical endpoint returned a
   bot-challenge page, yet the Price Sourcing Standard was met twice over: stockanalysis.com + CNBC
   for all published names, plus IBKR brokerage confirmation to the cent on all three core ETFs.
4. **The Task-0 feasibility pre-check again saved a revision pass**, and this run strengthened it by
   measuring the beta ceiling over the entire 103-name ≥80th-percentile pool
   (+0.8519) rather than only the published
   sleeve — making the infeasibility claim robust to the composition of the publication cut.

## What Failed

1. **A transient earnings-fetch failure silently produced penalty-free published forecasts.** Detailed
   below; this is the accepted change.
2. **`eff_n` did not move, again.** 34 settlements landed today and `EQUITY_ALPHA`
   `eff_n` stayed at 1. Every Track A lever remains gated.
3. **The ETF `mu` rule emitted forecasts it is expected to miss.** Today's baseline settled QQQ and
   SOXX as MISS against a SPY HIT, exactly the failure mode diagnosed on 2026-07-24, and the rolling
   `MARKET_FORECAST` hit rate is 23.81% over n=42.

## Primary Diagnosis

**Source grounding.** Not factor calibration: magnitude calibration is healthy (CI coverage
74.03%, mean z -0.1792) and the rank-order inversion, while real,
cannot be addressed under the current `eff_n`. The actionable defect this run exposed is a grounding
gate that can be silently bypassed by a network error.

## Proposed Change — Track B

> **Earnings Preflight Resolution and Convergence Rule.** Add to `rules.md § Input Classification`
> item 4 (next earnings date):
>
> **(a) A fetch failure is never a resolution.** A name whose earnings fetch returns a transport
> error must be re-fetched until it resolves to `CONFIRMED`, `ESTIMATED_CADENCE`, or
> `ESTIMATED_PRINT_WEEK`. A name with an unresolved earnings fetch may not be published in either
> sleeve — next earnings date is a **Required** input, so an unresolved fetch is a missing Required
> input, not a zero penalty.
>
> **(b) The bounded passes iterate to convergence.** Repeat the shortlist → penalty → re-rank cycle
> until every name in the intended published set has a grounded earnings date, to a stated cap of 4
> passes or 60 names, whichever binds first. Names entering the disclosure window only after
> convergence are excluded from publication with disclosure, never scored penalty-free.

### Problem evidence

`earnings_calendar_manifest.json` records **6 transport failures across 57 names** (CB, DGX, EG on
pass 1; HST, MRK, PKG on pass 3). Each returned no date, and in this run's scoring path a name with no
earnings record receives **no earnings penalty** — indistinguishable from a name verified to be clear
of its print. Three of the six landed inside the intended published set:

| Name | State on fetch failure | After retry | Effect of the retry |
|---|---|---|---|
| HST | rank ~19, penalty 0.00, publishable | `CONFIRMED` 2026-08-05 — **9 days out** | penalised −0.10, falls to rank 159 (pctl 69.2), **removed from the published set** |
| MRK | rank ~20, penalty 0.00, publishable | `CONFIRMED` 2026-08-04 — **8 days out** | penalised −0.10, falls to rank 163 (pctl 68.42), **removed from the published set** |
| PKG | rank ~18, penalty 0.00, publishable | `ESTIMATED_CADENCE` 2026-10-23 (88d) | correctly unpenalised; remains published at rank 18 |

Without the retry pass, **HST and MRK would have been published as monitoring forecasts carrying
`mu` +1.0% and no earnings penalty while reporting in
9 and 8 days** — a `LOW`-confidence, penalised profile
published as an unpenalised one. The failure is silent by construction: nothing in the current spec
distinguishes "verified clear of earnings" from "we could not ask".

The procedural half is equally evidenced. The standing precedent is a "bounded **second** pass", but
this run needed **three** shortlist passes plus two retry rounds before the post-penalty top-20
stabilised, because each penalty round promotes new names into the set. The 2026-07-26 package stopped at two passes and excluded 6 names;
this run converged and excluded 8. Same intent, different
stopping point, no rule to appeal to. Under `rules.md § Two-Track Change Classification`, a spec
ambiguity that has now surfaced in the 07-20 (HUM/DVA), 07-26 (six exclusions) and 2026-07-27 logs is
**mandatory Track B work**, not optional.

### Validation

Track B changes have no scoring math to validate statistically; the standard is the three-condition
test below. The behavioural test is nonetheless concrete and was executed: re-fetching the 6 failed
names changed 2 of the 3 in-set outcomes and in both cases **removed** a name from publication —
i.e. the change is strictly conservative in direction. No name gained publication or lost a penalty.
Replaying the convergence loop over this run's data terminated after 3 shortlist passes and 2 retry
rounds covering 57 distinct names — inside the proposed 4-pass / 60-name cap.

### Track B acceptance standard

1. **Explicit problem statement citing the artifact that exposed it** — satisfied:
   `earnings_calendar_manifest.json` (6 `FETCH_ERROR` entries) plus the HST/MRK/PKG counterfactual
   table above.
2. **Cannot weaken a protected rule or any grounding gate** — satisfied, and it *strengthens* one: it
   converts a silent missing-Required-input path into an explicit exclusion. No factor weight, mu or
   sigma rule, confidence mapping, or portfolio limit is touched.
3. **Logged with `HUMAN_REVIEW`, effective next run unless reverted** — satisfied.

### Decision

**`ACCEPT` — Track B, `HUMAN_REVIEW`, effective 2026-07-28.**

This run already applied both halves to itself (all 6 failures were retried to resolution, and the
passes were iterated to convergence), so this package's output is unaffected — the change codifies
what was done here so the next run is not free to skip it.

**Relationship to the concurrent `gpt-5-2026-07-27` Track B.** That package accepted a different
change on the same day: loosening the vendor-empty print signature to `move ≥3.5%` **or**
(`volume ≥1.8×` **and** `move ≥1.5%`), also effective 2026-07-28. The two are complementary, not
competing — theirs changes how a vendor-empty *response* is classified, mine changes what happens when
there is *no response at all*, and neither touches the other's logic. Both are one Track B change in
their own package, so the one-per-run limit holds for each. This run applied the stricter
price-move-required branch for classification (pre-dating their effective date) and disclosed in `05`
that the difference changes nothing in this package: the three affected names (CB, MTB, PFG) all rank
outside the published set, and the one published `ESTIMATED_PRINT_WEEK` name (HIG) resolves
identically under both rules.

## Track A Observations — Deferred

Each is a real finding recorded as an observation, and each is `DEFER`red rather than `REJECT`ed,
because `eff_n = 1` for `EQUITY_ALPHA` and 1 for `MARKET_FORECAST` fails the
`eff_n ≥ 3` gate that `rules.md` requires for any Track A calibration proposal.

| Observation | Evidence | Disposition |
|---|---|---|
| Rank-order inversion persists | weighted-mean rank IC -0.1843 over 231 pairs; today's 2026-06-29 vintage -0.5912 | `DEFER`. Needs an ordering-level test. The mu-shrink/sigma-widen proposal stays **retired** — a monotonic transform cannot reorder a ranking. |
| ETF `mu = beta × SPY_mu` is a category error | `MARKET_FORECAST` hit rate 23.81%, n=42, mean z -0.6640; QQQ and SOXX settled MISS today against a SPY HIT | `DEFER`. Diagnosed 2026-07-24; two candidate fixes were already tested and rejected. Only the evolution agent may change that table and Track A is gated. |
| Magnitude calibration is healthy — do not touch sigma | CI coverage 74.03% (inside 55–85%), mean z -0.1792 (inside ±0.5) | **No change indicated.** Explicitly recorded so a future run does not "fix" a working component. |
| `eff_n` may be structurally stuck | 34 settlements added today; `eff_n` unchanged at 1. Vintages cluster into a single 28-day resolution window | `DEFER`, and flag for the 2026-07-31 structural review: if `eff_n` cannot rise under the current cadence, Track A is permanently unreachable and the gate itself needs review, not the parameters. |

## Freeze Check

No freeze criterion fires. (1) Recent cycles have **accepted** Track B changes rather than rejecting
everything for lack of evidence — 07-26, 07-27 (gpt-5), and this run. (2) There are not two accepted
performance changes in a row worsening out-of-sample results; no Track A change has been accepted at
all under the `eff_n` gate. (3) Weights and thresholds are not oscillating — they have not moved.
Track A remains evidence-gated, which is the designed state and not a freeze.

## Mutation Log

| Field | Value |
|---|---|
| Current problem | A transient earnings-fetch failure yields no date and therefore no earnings penalty, which is indistinguishable from a name verified clear of its print; and "bounded second pass" does not say when to stop iterating |
| Proposed change | (a) a fetch failure is never a resolution — retry to resolution or exclude from publication; (b) iterate the shortlist/penalty/re-rank cycle to convergence, capped at 4 passes / 60 names, excluding later entrants with disclosure |
| Validation method | Re-fetch the 6 failed names in this run and compare published-set membership and penalties before vs after; replay the convergence loop to termination |
| Result | 2 of 3 in-set names changed, both **removed** from publication (HST 9d, MRK 8d); PKG correctly unpenalised; loop converged after 3 shortlist passes + 2 retry rounds, 57 distinct names, inside the cap |
| Decision | **`ACCEPT`**, Track B, `HUMAN_REVIEW` |
| Effective | next run, 2026-07-28 |
