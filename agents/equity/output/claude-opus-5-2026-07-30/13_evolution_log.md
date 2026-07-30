# 13 — Evolution Log — 2026-07-30

## Run context

| Field | Value |
|---|---|
| Run | `claude-opus-5-2026-07-30` · fired 10:06 ET (intraday) |
| Status | `NO_TRADE` |
| Regime | `NEUTRAL` (VIX 20.66) |
| Evaluation window | trailing 7 calendar days, all models: 2026-07-30 back to 2026-07-23 |
| Ledger status | `EQUITY_ALPHA` n=347, eff_n=1 · `MARKET_FORECAST` n=63, eff_n=1 |
| Settled this run | 58 (49 EQ, 9 MF), `due_inventory: 0`, `conflicts: 0` |
| Baseline flag | `CROSS_MODEL_BASELINE` → `claude-fable-5-2026-07-02` |

## What worked

1. **Full-universe earnings grounding held up under cross-validation.** The forward calendar
   sweep (27/27 business days, complete)
   grounded **262 CONFIRMED_CALENDAR +
   251 NO_PRINT_IN_WINDOW = all 513** scored names,
   with **zero** ungrounded. Cross-validated against the per-name endpoint on 25 top-ranked
   names: **7 agree, 0 disagree**,
   18 vendor-empty. That vendor-empty count is itself the finding — 18 of
   25 top names would have been unresolvable under the retired per-name heuristic, in the exact
   post-print window where that heuristic produced six false "clear of earnings" calls on
   2026-07-29. Ranks stayed contiguous 1–24.
2. **Intraday fire cost nothing on price grounding.** stockanalysis's bulk history had not yet
   published a partial 2026-07-30 bar, so all 519 fetched symbols returned 2026-07-29 as the last bar —
   one consistent basis. CNBC's field inversion behaved as the 2026-07-27 note predicts: under
   `REG_MKT`, `previous_day_closing` is the completed close and `last` is the live tape. All
   74 distinct cross-verified names (30 published + 47 settlement)
   agreed within 0.1% with no confirmation pass needed; IBKR matched the three core ETFs to the cent via `last − change`
   (`prior-close` empty during RTH, confirmed again).
3. **Feasibility was re-verified rather than inherited.** Max attainable sleeve beta came back
   **+1.1258** — *feasible* — where 2026-07-27 computed +0.8519 and
   proved infeasibility. Reusing that narrative would have been wrong, exactly as the
   2026-07-29 package warned.

## What failed

1. **Rank ordering, again and measurably.** Weighted-mean rank IC **-0.1975** across
   n=347; **19 of 23** vintages ≤ 0. Magnitude calibration is *fine*
   (CI coverage 72.05%, mean z -0.3419) — the score is not
   mis-scaled, it orders the wrong names first.
2. **`MARKET_FORECAST` went 0-for-7** this batch
   (rolling 16.4%, n=63). Unchanged root cause from 2026-07-24.
3. **The tied baseline problem recurred and was decision-relevant.** Three folders tied at
   delta 0d; their settled hit rates were
   claude-fable-5 47.8%, claude-sonnet-5 41.7%, gpt-5 7.1% — a **40.7pp** spread with
   mean alpha from -19.48% to
   -2.54%.

## Primary diagnosis

**Factor calibration** — specifically rank-order inversion, not magnitude drift.

The mechanism is visible in this run's own data. `Tech_Z` carries
66.7% of the live conviction weight (the only other live family is `Macro_Z`
at 0.15), and it is built from 20d/60d momentum and relative strength. That is a
trend-persistence construction: it *necessarily* ranks the trailing 60 days' winners first.
Over the settled window those winners were defensives, because semis collapsed
(9
semi names in the batch, SOXX itself -17.89%). So the leaderboard this run produced is
maximally defensive — 12 of 24 published names
carry negative 60-day beta.

An unusually clean out-of-sample test then arrived unbidden. Ranks were computed from 2026-07-29
data with no knowledge of the 2026-07-30 tape; within an hour of the run firing
(snapshot 2026-07-30T10:26:18-04:00), **21 of 24** published names were down, averaging
**-3.47%**, against SPY +1.17% and SOXX
**+8.67%** — a 4.64pp adverse
same-session move, with the rotation running precisely opposite to the one the ranking encodes.

This is one session and is treated as **illustrative, not evidentiary**.

## Proposed change

### Track A candidate (priority override) — **DEFERRED**

`rules.md § Evolution Policy` fires the priority override: rank IC -0.1975 ≤ 0 over
≥20 settled predictions means the change *must* address calibration before anything else. The
correct proposal is a **regime-conditional or reversal-aware `Tech_Z`** — a momentum family
that does not load maximally into leadership immediately before it rotates.

It is **`DEFERRED`, not `REJECT`**, exactly as the policy directs: a Track A calibration
proposal requires raw `n >= 20` **and** `eff_n >= 3`. Here n=347 passes but
**eff_n=1** fails. Per the 2026-07-28 finding this is a startup transient, not a
design flaw, and it is falsifiably projected to reach 2 on
**2026-08-05**
(43 pending), so Track A eligibility
remains ~early September. Adopting a momentum redesign on a single overlapping cohort is
precisely the overfitting the policy exists to prevent — and the 2026-07-24 and 2026-07-26 logs
already record two rejected attempts to fix this class of miss with parameter tweaks.

Also recorded for the 2026-07-31 structural review: a monotonic mu-shrink or sigma-widen
**cannot** repair a rank inversion (retired as a standing proposal on 2026-07-26), and the
`MARKET_FORECAST` `mu = beta x SPY_mu` category error is Track-A-gated on
eff_n=1 < 3 (rises 2026-08-09).

### Accepted change this run — **Track B**

**Problem.** `agents.md § Orchestrator Step 2` specifies the MoM baseline algorithm but has
**no tie-break** when several folders sit at the same distance from target. Step 4 says
"closest in-window cross-model folder" and stops. This was flagged in the `13_evolution_log.md`
of **2026-07-28** and **2026-07-29**; `rules.md § Two-Track Change Classification` states that a
spec inconsistency flagged in two consecutive evolution logs is **mandatory Track B work, not
optional**. Today is the third consecutive occurrence, and the first where the executing model
had *no* same-model folder in window at all — so the tie was resolved entirely by cross-model
choice.

**The artifact that exposed it.** `02_reflection.md § 1` of this run: `claude-fable-5-2026-07-02`,
`claude-sonnet-5-2026-07-02` and `gpt-5-2026-07-02` all tie at delta 0d. Their settled outcomes,
computed from this run's own 49 settlements:

| Tied folder | n settled | Hit rate | Mean alpha |
|---|---|---|---|
| `claude-fable-5-2026-07-02` | 23 | 47.8% | -2.54% |
| `claude-sonnet-5-2026-07-02` | 12 | 41.7% | -2.84% |
| `gpt-5-2026-07-02` | 14 | 7.1% | -19.48% |

A **40.7pp** hit-rate spread. The conclusion is **not invariant**, and the cause is
composition rather than luck: the books are near-disjoint (claude-fable-5 ∩ claude-sonnet-5 = 0
shared names; claude-fable-5 ∩ gpt-5 = 3), and gpt-5's was semiconductor-weighted into the exact
window semis collapsed. Whichever folder the orchestrator happened to pick would have set the
MoM narrative.

**Change.** Add rule 8 to `agents.md § Orchestrator Step 2`: on a tie in
`|folder_date − target|`, resolve by (a) same model family, (b) usable `15_predictions.json`,
(c) lexicographic folder name — **and report every tied candidate** in `02_reflection.md § 1`
with its own hit rate, mean alpha and mean z, stating explicitly whether the MoM conclusion is
invariant across them.

**Hypothesis (falsifiable).** Baseline selection is currently non-deterministic across
implementations and silently selects the MoM narrative whenever tied books disagree. Making the
order explicit removes the non-determinism; making disclosure mandatory removes the silence.
Falsifier: a future run finds tied candidates whose reported outcomes are materially different
*and* the reflection still presents a single baseline without the comparison — that would mean
the rule was written but is not binding, and it should be moved into a validator rather than
left as prose.

**Validation — Track B three-condition standard.**

1. *Explicit problem statement citing the artifact that exposed it* — yes: `02 § 1` of this run,
   plus the 2026-07-28 and 2026-07-29 evolution logs.
2. *Cannot weaken a protected rule or grounding gate* — confirmed. This touches only which prior
   folder is compared against and what must be disclosed. It changes no scoring formula, factor
   weight, forecast prior, risk limit, or price-grounding requirement. It strictly **adds** a
   disclosure obligation.
3. *Logged with a `HUMAN_REVIEW` flag, effective next run unless reverted* — yes (below).

Track B changes do not require a statistical holdout, and none is claimed. The supporting
numbers above are the problem statement, not a performance test.

**Decision: `ACCEPT`.** 🚩 `HUMAN_REVIEW`

Applied to `agents/equity/daily_investment_system/agents.md § Orchestrator Step 2` as rule 8,
in this run's commit. Effective the next run that selects a MoM baseline, unless reverted.
This run already applied the rule to itself: selection order was documented and all three tied
candidates are reported in `02 § 1`.

**Limit check:** exactly one Track B change this run.

## Cross-model observations (trailing 7 days)

- **The tied-baseline spread is a repeat, not a one-off.** 2026-07-29 measured a 48pp spread
  between tied books; today measures 40.7pp. Both trace to the same structural fact —
  models running the same date produce near-disjoint books with very different factor tilts —
  which makes cross-model divergence genuinely diagnostic rather than noise.
- **A concurrent `gpt-5-2026-07-30` run is in flight** in a separate worktree. Per the standing
  rebase discipline, `main` was re-checked after this package was staged; any competing
  2026-07-30 package that lands afterwards is a known race and does not invalidate this one.
- **`eff_n` projections remain unfalsified.** `EQUITY_ALPHA` → 2 on
  2026-08-05, `MARKET_FORECAST` → 2 on
  2026-08-09. Both are still in the future, so today's
  eff_n=1 is the expected reading and not evidence against the 2026-07-28 change.

## Effective next step

1. **Next run:** apply `agents.md` Step 2 rule 8 (tie-break + mandatory reporting of all tied
   candidates).
2. **2026-07-31 (Friday, last trading day of July):** weekly parameter review **and** month-end
   structural review. Carry forward the rank-inversion diagnosis, the `MARKET_FORECAST` mu
   category error, and `Fund_Z`/`Sent_Z` Phase 2 — the last being the only one of the three that
   would let any run reach `GO`.
3. **~2026-08-05 onward:** re-test Track A eligibility as
   `eff_n` rises; do not attempt a momentum-family redesign before both gates open.
