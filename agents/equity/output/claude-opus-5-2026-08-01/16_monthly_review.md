# 16 — Monthly Structural Review — July 2026

**Published late and by a Saturday run.** `runbook.md § Cadence` schedules the structural
review for the last trading day of the month at 17:30 ET — that was Friday **2026-07-31**, and
**no run fired that day**. This is the first run since, so it owes the review. It covers the
full month rather than deferring to August.

## July 2026 census

| Field | Value |
|---|---|
| Dated packages | **54** |
| Distinct run dates | 26 of 23 weekdays |
| Weekdays with no package | 2026-07-23, 2026-07-31 |
| Models active | 6 |
| **Status distribution** | **{'NO_TRADE': 39, 'REVIEW_ONLY': 11, 'HALTED': 1, 'NO_09_ARTIFACT': 3}** |
| **`GO` runs** | **0** |

| Model | Packages | Status distribution |
|---|---|---|
| `claude-fable-5` | 18 | {'NO_TRADE': 13, 'REVIEW_ONLY': 4, 'HALTED': 1} |
| `claude-haiku-4-5` | 1 | {'NO_09_ARTIFACT': 1} |
| `claude-opus-5` | 6 | {'NO_TRADE': 6} |
| `claude-sonnet-5` | 3 | {'NO_TRADE': 3} |
| `gemini-3.5-flash` | 3 | {'NO_09_ARTIFACT': 2, 'NO_TRADE': 1} |
| `gpt-5` | 23 | {'NO_TRADE': 16, 'REVIEW_ONLY': 7} |

## Structural finding 1 — July produced zero tradeable portfolios, and the cause is singular

**54 packages. Six models. Twenty-six run dates. Zero `GO`.**

Every package that reached a status published `NO_TRADE` (39),
`REVIEW_ONLY` (11) or `HALTED` (1). This is not a
market judgement repeated 54 times — it is one blocker observed 54 times. `Fund_Z` and
`Sent_Z` are `UNAVAILABLE` universe-wide, which makes `rules.md § Evidence Thresholds` #2
(≥ 3 of 4 families non-negative), #3 (no family > 50% of conviction) and #4 (data
completeness ≥ 85%) **arithmetically unsatisfiable for every name in every regime**.

The system is behaving *correctly*: it refuses to publish a portfolio it cannot support, and
that discipline is the most valuable property it currently has. But a research loop that
cannot reach `GO` under any market condition is not producing decision-relevant output — it
is producing an audit trail proving it should not. That is worth exactly one month, not two.

**The gap is not a prompt problem and cannot be fixed by prompt mutation.** It needs Phase 2
of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`: bulk SEC EDGAR
`companyfacts.zip` plus a threaded Nasdaq analyst/short-interest fetch across all
513 names, to clear the 70%-of-universe coverage bar that
`rules.md § Financial Metrics and Score Attribution` requires before a metric may contribute
to `Adj Score`. Phase 1 (the SHADOW tooling) has been complete since 2026-07-16 and covers
~4.7% of the universe. **This has been the top open item for 17 days and is unchanged.**

Recommendation for August, in priority order:
1. Implement Phase 2 fundamentals/sentiment at universe scale.
2. Promote `Fund_Z`/`Sent_Z` as a Track B change with `HUMAN_REVIEW` after one full shadow
   run at ≥ 70% coverage.
3. Only then is a `GO` reachable, and only then does the rest of the calibration work
   (rank IC, mu tables) become measurable on a four-family score.

## Structural finding 2 — magnitude calibration is healthy; ordering is not

This separation held all month and is now well-evidenced:

| Dimension | Metric | State |
|---|---|---|
| Magnitude | CI coverage 70.16% (target 70%) | **healthy** |
| Magnitude | Mean z -0.4608 | marginal, slightly optimistic mu |
| Ordering | Rank IC -0.1314, negative in 20/28 vintages | **broken** |
| Ordering | Hit rate 42.37% | below the 50% bar |

The intervals are the right width; the ranking puts the wrong names first. Any proposal that
is a monotonic transform of the score (mu shrink, sigma widen) **cannot** fix the second
problem, and that proposal was retired on 2026-07-26. July's contribution to the ordering
problem is the **`Tech_Z` duplicate-signal defect** found today (`13`): momentum has been
carrying double weight inside the family that itself carries 66.7% of the live
composite. That is a concrete, mechanical contributor to trend over-fitting, and it is the
first structural correction to the ordering problem the loop has produced.

## Structural finding 3 — `eff_n` is a startup transient, and the projection is holding

The question escalated to this review on 2026-07-27 ("if `eff_n` can never rise under this
cadence, the gate itself needs review") was **closed on 2026-07-28** as arithmetic, not
design: all settled target dates spanned fewer than 28 days, so exactly one window fit. The
Track B change accepted that day added an `eff_n_projection` block to `settlement_ledger.py`
with a falsifiable claim.

**Status today:** `EQUITY_ALPHA` `eff_n` = 1, projected to increment on
**2026-08-05** with
43 pending; `MARKET_FORECAST` on
**2026-08-09** with
6 pending. Adding 92
equity settlements today moved raw `n` to 439 and left `eff_n` at 1, with the
target-date span now 24d — still inside one
window. **The projection has not been falsified.** Track A eligibility (`eff_n ≥ 3`) remains
projected for early September. No further review action; the gate is working as designed.

## Structural finding 4 — the MoM tie-break rule was needed and is now proven

Flagged on 07-28 and 07-29, implemented 07-30 as `agents.md § Orchestrator Step 2` rule 8.
It has now fired three times with very different results:

| Date | Tie | Hit-rate spread across tied books | Conclusion invariant? |
|---|---|---|---|
| 2026-07-29 | 3-way | 48pp | **No** — the choice determined the narrative |
| 2026-07-30 | 3-way | 40.7pp | **No** |
| 2026-08-01 | 2-way | 1.7pp | **Yes** |

The rule is doing exactly what it was written for: forcing disclosure so that *whether* the
baseline choice matters is an observable fact rather than an assumption. Today it showed the
conclusion is robust; on the two prior firings it showed it was not. **No change needed.**

## Data-sourcing state at month end

| Source | State |
|---|---|
| stockanalysis.com 5Y bulk | **Primary and healthy** — 519/519 in 31.8s |
| CNBC restQuote | Healthy; field choice depends on market state (`last` when closed, `previous_day_closing` intraday) |
| Nasdaq quote-info | Healthy as a third source |
| Nasdaq calendar/earnings | **Healthy — now the grounding path for 100% of the universe** |
| Nasdaq screener (cap/sector) | Healthy — one call, 7131 rows |
| Nasdaq bulk `historical` | **Dead since 2026-07-27** (bot-challenge HTML) |
| Yahoo v8 chart | Unreliable — 429-blocked most of July |
| FRED `fredgraph.csv` | **Timed out this run**; Treasury CSV fallback worked |
| IBKR MCP | **Unreachable this run** (weekend) |

**Bulk history has no redundancy.** stockanalysis.com is the only working bulk source; Yahoo
is unreliable and Nasdaq's bulk endpoint is dead. This is a single point of failure for the
whole loop and is the second engineering priority after the fundamentals gap.

## Protected rules

No protected rule was modified, weakened, or proposed for modification in July. The one
change accepted today is a within-family metric-count correction that touches no protected
rule. Human approval was neither required nor implied for anything logged this month.

## August priorities

1. **Phase 2 fundamentals + sentiment at universe scale** — the only path out of permanent
   `NO_TRADE`.
2. **A second bulk price-history source** — remove the stockanalysis single point of failure.
3. **Verify the `Tech_Z` deduplication** accepted today against the un-deduplicated baseline
   once `eff_n ≥ 3`.
4. **Revisit the Core ETF mu derivation** the moment `MARKET_FORECAST` `eff_n` reaches 3.
5. **Refresh the constituent caches** (41 days old).
