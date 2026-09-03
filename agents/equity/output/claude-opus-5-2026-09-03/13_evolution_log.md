# 13 — Evolution Log · 2026-09-03

## Run context

| Field | Value |
|---|---|
| Run date / model | 2026-09-03 · `claude-opus-5` · post-close fire 18:11 ET |
| Status | `NO_TRADE` |
| Regime | `BULL` (SPY prior +2.00%) |
| Evaluation window | all packages dated 2026-08-27 .. 2026-09-03, all models |
| Ledger status — EQUITY_ALPHA | raw n 1451, **eff_n 3**, hit 38.11%, CI 71.74%, mean z -0.5517 |
| Ledger status — MARKET_FORECAST | raw n 216, eff_n 2, hit 43.75%, CI 91.20%, mean z -0.1868 |
| Track A gate | EQUITY_ALPHA **True** (n >= 20 and eff_n >= 3 both satisfied); MARKET_FORECAST False |
| Baseline flag | `OK` — `claude-opus-5-2026-08-06` at delta 0d |

## Review window census

| Package | Status | Note |
|---|---|---|
| `claude-opus-5-2026-08-27` | see its own `09` | in the trailing-7-day window |
| `claude-opus-5-2026-08-28` | see its own `09` | in the trailing-7-day window |
| `claude-opus-5-2026-09-03` | see its own `09` | in the trailing-7-day window |
| `gpt-5.6-sol-2026-08-28` | see its own `09` | in the trailing-7-day window |

## What worked

1. **The `eff_n` projection was falsifiable and it held.** The 2026-07-28 package predicted
   `EQUITY_ALPHA` `eff_n` would increment on **2026-09-03** with 24 pending predictions. It did:
   settling this run's 96 equity keys opened the third non-overlapping 28-day window
   (2026-07-08, 2026-08-05, 2026-09-03) and `eff_n` moved
   2 -> **3**. The 2026-07-27
   escalation — "if `eff_n` can never rise under this cadence, the gate itself needs review" — is
   now definitively answered: it was a startup transient, the gate is sound, and it has opened on
   schedule.
2. **The two-reference liveness screen prevented a large silent universe cut.** 22 names
   tripped the last-bar test and *all 22* were alive on both independent references.
   Requiring two references, rather than treating a stale primary bar as decisive, is what kept
   them in the universe.
3. **The symbol-reuse price gate earned its keep on its first live run.** `EQR` returned a
   basis-date CNBC quote of 0.355
   under the name 'EQ Resources Ltd' on the ASX. A date-only gate accepts that row; the venue and
   volume conditions added on 2026-08-28 reject it (L026).
4. **Settlement was clean at scale:** 111 rows across
   5 vintages and three timing conventions, 0
   conflicts, `rejected_rows` unchanged at 87.

## What failed

1. **The fire window was too early.** The 18:11 ET bulk fetch returned 518/519
   symbols in 15.5s but carried a 2026-09-03 bar for only
   **494** of them. Of the 25 without one,
   2 had genuinely stopped trading
   (AVB, EA), 1 was a dead-ticker fetch failure
   (EQR), and **22** were live,
   screener-listed large-caps with a CNBC basis-date close already available
   (AIG, AWK, BA, BEN, BG, CNP, ELV, FDS, FOX, MTB, OMC, RJF, RL, SBAC, STE, STZ, SW, TFC, VRSK, VTRS, WEC, WST). The run recovered by re-fetching to convergence, but a run that had taken
   the first fetch as final would have dropped 22 live names
   from a 508-name universe and mislabelled them as corporate actions.
   One further published name carried a *preliminary* primary close at that hour (`GILD` 151.19 against 151.22 at both secondary vendors) - the bar existed but was not final.
2. **Rank ordering is still inverted in aggregate.** Mean vintage rank IC is
   -0.0659 over 73 vintages with
   54.79% at or below zero, even though this run's
   own baseline vintage came in at +0.2739.
3. **Hit rate is unchanged at 38.11%**, below the >50% healthy range, for the
   same structural reason as every run since July: the composite is a pure trend-persistence
   ranking.

## Primary diagnosis

**Source grounding** — specifically, the interaction between *when* the run fires and *which
vendor state* the liveness screen sees. The calibration defect (rank-order inversion) is better
evidenced and more consequential, but it is not what this run has a bounded, testable fix for; the
fire-window/vendor-lag interaction is, and it caused a near-miss today.

## Proposed change (exactly one) — Track B

**Problem statement.** `rules.md § Universe Construction` and the 2026-08-22 corporate-action
Track B both key on "last bar predates the basis" as the trigger for a liveness classification.
That condition conflates two different states: a security that has stopped trading, and a vendor
that has not finished publishing. At the 2026-09-03 18:11 ET fire the second state applied to
**22 of 508** scored names. The artifact that exposed it is this package's
own `04 § Corporate-action and liveness screen`, where a class named `VENDOR_BAR_LAG` had to be
invented mid-run to describe names that failed the trigger while passing both confirmations.

The same root cause produced a *second*, subtler symptom in the same fetch. `GILD`'s basis close
read 151.19 at the primary vendor while CNBC and Nasdaq **both** read 151.22 — the
two secondary vendors agreeing with each other against the primary. That is the signature the
2026-08-27 second fire recorded for `TECH` at 19:09 ET, and it was left as an observation there
because that day's Track B slot was spent.

**This one did not resolve.** `TECH`'s disagreement converged by 22:03 ET; `GILD`'s survived the
19:27 ET convergence and was still present on the 19:28 ET
re-fetch (L027). So the second symptom is not merely a slower version of the first: a basis bar can
be *present, converged, and still wrong*, and only cross-vendor majority detects it. Both symptoms
share one defect — **the primary bulk vendor's basis bar is not final when the run assumes it is** —
but they need different tests, which is why the rule below has two clauses.

The published `GILD` entry price keeps the primary value 151.19. The deviation is
0.0198%, far inside the 1% grounding gate, and the majority rule
proposed here is effective **next** run — applying it to today's own package would be exactly the
early application of a future-effective change that `13`'s own comparability rationale forbids.

**Proposed change — primary-vendor finality protocol.** One rule, answering one question: *when
may a post-close run treat the primary vendor's basis bar as final?* It has two clauses because
the bar can be non-final in two ways, and a rule covering only one of them leaves the other
undetected.

1. **Liveness clause.** A symbol whose primary-vendor last bar predates the basis is
   `PENDING_LIVENESS`, not a corporate action, until both independent references have been
   consulted. `PENDING_LIVENESS` + Nasdaq screener row present + CNBC quote passing the
   2026-08-28 symbol-reuse gate => **`VENDOR_BAR_LAG`**: the name stays in the universe and the
   run re-fetches the primary vendor until the basis bar appears. Either reference failing routes
   to the existing `CORPORATE_ACTION_*` / `SYMBOL_REUSE_FOREIGN_LISTING` /
   `TRANSIENT_FETCH_FAILURE` branches, unchanged.
2. **Finality clause.** A basis bar that exists is still not final while the two secondary vendors
   agree with each other to the cent *against* the primary. On that signature the run re-fetches
   the primary; if the disagreement survives convergence — as `GILD`'s did today — the
   **two-vendor majority value** is the entry price and the discarded primary value is recorded in
   `price_verification.json`. A tie-break is required precisely because re-fetching is not always
   enough.
3. **Timing.** A post-close run must not treat a bulk fetch as final while any `VENDOR_BAR_LAG`
   name or any unresolved finality-clause disagreement is outstanding. Recommended earliest
   post-close bulk fetch: **20:00 ET or later**, on the evidence below. This run polled the
   lagging set every ~7 minutes and watched it drain — 18:29 ET: 19 -> 18:44 ET: 16 -> 18:58 ET: 13 -> 19:12 ET: 5 -> 19:27 ET: 0 — reaching zero at
   **19:27 ET**, 207 minutes after the
   16:00 close. Absent bars fall with fire hour across the four observed post-close runs; the
   preliminary-close count is too small a sample to call a trend and is reported as a count.

| Fire time (ET) | Run | Absent basis bars | Preliminary closes |
|---|---|---|---|
| 18:11 | 2026-09-03 (this run) | 22 | 1 |
| 19:09 | 2026-08-27 | 0 | 1 (`TECH`, converged by 22:03) |
| 20:08 | 2026-08-03 | 0 | 0 |
| 22:02 | 2026-08-07 | 0 | 0 |

**Why this is one change and not two.** `rules.md § Required Evolution Workflow` forbids bundling
*unrelated* changes. These clauses share a single diagnosis (non-final primary tape), a single
trigger (an early post-close fire), and a single remedy (re-fetch to convergence, with a defined
tie-break). Splitting them would ship a rule that detects a missing bar but silently accepts a
wrong one.

**Classification: Track B** (process change — a missing-fetch procedure fix and a spec-consistency
fix). It changes no scoring formula, factor weight, forecast prior, or protected risk limit, and
it cannot weaken a grounding gate: clause 1 makes the liveness screen *more* demanding by requiring
both references before a name may be excluded, and clause 2 adds a check where none existed.

**Hypothesis (falsifiable).** If the rule is correct, then on any future post-close run fired at
or after 20:00 ET the `VENDOR_BAR_LAG` count at first bulk fetch will be materially lower than the
22 observed at 18:11 ET, no run applying the two-reference confirmation will exclude a
name that a later fetch shows to be trading normally, and a primary-vendor value that the two
secondary vendors jointly contradict will, on re-fetch, converge to the secondary value rather
than the other way round. Three ways to falsify it: a run firing after 20:00 ET that still finds a
double-digit lag count; a name excluded as a corporate action that is later found trading; or a
finality-clause disagreement that resolves in the *primary* vendor's favour on re-fetch.

**Validation (Track B three-condition standard).**

| Condition | Evidence |
|---|---|
| 1. Explicit problem statement citing the artifact that exposed it | `04 § Corporate-action and liveness screen`: 22 names classified `VENDOR_BAR_LAG`, a class with no prior definition in `rules.md`; and `01 § L011`/`price_verification.json`, where 1 published name(s) show the two secondary vendors agreeing against the primary |
| 2. Cannot weaken a protected rule or any grounding gate | the change adds a required confirmation before exclusion and adds a reporting obligation; it removes no check. Protected rules (5% single name, 30% sector, 0.90-1.10 beta, 0.45 correlation, 8% drawdown, no fabrication, NO_TRADE on weak evidence) are untouched |
| 3. Logged with a `HUMAN_REVIEW` flag, effective next run unless reverted | flagged below |

**Measured scope — this was not a cosmetic near-miss.** The counterfactual was computed, not
asserted: the engine was re-run with the 22 lagging names excluded, exactly as a
one-reference reading of the first fetch would have had it.

| Quantity | One-reference reading (18:11 ET) | Published run (post-convergence) |
|---|---|---|
| Scored universe | 486 | 508 |
| Published book overlap | 21/24 with the published book | — |
| Names that would have been missing | ELV, RJF, SCHW (of which ELV, RJF were the lagging names themselves; the third enters because dropping 22 names shifts every winsorized cross-sectional z-score) | — |
| Names that would have been published instead | MDT, DGX, BMY | — |
| Top-10 overlap | 10/10 | — |
| Median rank move, top 24 | 0.0 places | — |

So **3 of 24 published forecasts** would have been different names, each carrying a real `mu`,
`sigma`, CI and settlement obligation. The leaderboard's top 10 is unchanged, so this is not a
ranking-quality problem — it is a *coverage* problem that silently substitutes forecasts.
3 names are genuine
corporate actions and are unaffected by the rule.

**Decision: `ACCEPT`. `HUMAN_REVIEW`. Effective
2026-09-04.**

## Track A: eligible for the first time, and deliberately deferred

`rules.md § Evolution Policy` requires raw `n >= 20` **and** `eff_n >= 3` for a Track A
calibration proposal. As of this run's post-write manifest, `EQUITY_ALPHA` satisfies both
(n 1451, eff_n 3) — the first time since the gate was built on 2026-07-24.

The obvious candidate is the rank-order inversion: mean vintage rank IC -0.0659
over 73 vintages. It is **not** proposed, for a reason that is now well-evidenced rather
than cautious:

| Previously tested Track A remedy | Run | Result | Why it could not have worked |
|---|---|---|---|
| mu shrink / sigma widen | 2026-07-20, re-examined 07-22 and 07-26 | REJECTED | a monotonic transform of every mu cannot change a rank ordering |
| beta damping at 5 lambdas | 2026-07-24 | REJECTED | hit rate stayed at exactly 21.2% at every lambda |
| own-trend / RS20 amplification at 5 thetas | 2026-07-24 | REJECTED | same — the miss was a reversal no trend term anticipates |

Every remedy tried so far operates on magnitude. The defect is ordinal. The correct Track A
proposal would change *which* signals enter `Tech_Z` or how they are combined — but with two of
four families dark, `Tech_Z` carries 66.7% of conviction and any reweighting inside
it is a rearrangement of six trend measures, which is precisely the anti-overfitting case
`rules.md § Anti-Overfitting Rules` warns against ("do not increase complexity unless the simpler
version measurably fails" — it does fail, but the simpler *alternative* does not exist while the
other two families are unsourceable).

**Recorded as an observation, `DEFER`red as a proposal.** The blocking dependency is not evidence
any more — it is the Phase 2 fundamental/sentiment fetch work in
`agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`. Until a third family is live, a
Track A change to a two-family composite would be tuning the only thing that moves.

## Observations carried forward (not proposed — one change per run)

1. **`MARKET_FORECAST` Track A is still gated** (eff_n 2, projected 3 on
   2026-09-07). The `mu = beta x SPY_mu` category error for
   QQQ/SOXX is the standing candidate the moment that gate opens: this run again produced
   SOXX mu +4.98% — the **highest** of the three ETFs — on the ETF with the
   **worst** relative strength (RS60 -15.79%).
2. **CI coverage on `MARKET_FORECAST` is 91.20%**, above the 85% ceiling,
   meaning core-ETF intervals are uninformatively wide. `rules.md` says to tighten. Same gate.
3. **Dead tickers permanently leak evidence.** 2 key(s) can never settle.
   The constituent caches are
   74
   days stale, which is the upstream cause; a cache refresh is maintenance work, not an evolution
   proposal.

## Mutation log

| Field | Value |
|---|---|
| Current problem | the liveness screen's trigger condition conflates a security that stopped trading with a vendor that has not finished publishing |
| Proposed change | primary-vendor finality protocol: (1) `PENDING_LIVENESS` -> `VENDOR_BAR_LAG` with mandatory two-reference confirmation and re-fetch to convergence; (2) a basis bar the two secondary vendors jointly contradict is not final, and the two-vendor majority wins if the disagreement survives; (3) earliest post-close bulk fetch >= 20:00 ET |
| Validation method | Track B three-condition standard; scope measured against this run's own 508-name cross-section |
| Result | 22 names would have been wrongly excluded under a one-reference reading, changing 3 of the 24 published forecasts (21/24 overlap, top-10 unchanged); 1 published entry price sat on a preliminary primary value at that hour |
| Decision | **ACCEPT** (`HUMAN_REVIEW`) |
| Effective date | 2026-09-04 |

Track A this run: **`DEFER`** — eligible on evidence for the first time, declined on the merits.
