# 13 Evolution Log — 2026-07-29

## Run Context

| Field | Value |
|---|---|
| Run date / model | 2026-07-29 / `claude-opus-5` (pre-open, 08:05 ET) |
| Final status | `NO_TRADE` |
| Regime | `NEUTRAL` |
| Evaluation window | Trailing 7 calendar days, all models: 2026-07-22 → 2026-07-29 |
| Ledger status | `EQUITY_ALPHA` n=298, `eff_n`=1 · `MARKET_FORECAST` n=54, `eff_n`=1 |
| Track A gate | **INSUFFICIENT_EFFECTIVE_N** — closed for both record types |
| Baseline flag | `CROSS_MODEL_BASELINE` |

## Packages Reviewed (trailing 7 days, all models)

`gpt-5-2026-07-22`, `claude-sonnet-5-2026-07-22`, `gpt-5-2026-07-24`, `claude-opus-5-2026-07-24`,
`claude-opus-5-2026-07-26`, `gpt-5-2026-07-27`, `claude-opus-5-2026-07-27`, `gpt-5-2026-07-28`,
`claude-opus-5-2026-07-28`, plus this run.

## What Worked

- **The pre-open fire window held up again.** 519/519
  symbols in 25.8s with every last bar
  at 2026-07-28, and 28/28 entry prices exact to the cent across three to four independent
  sources. No confirmation pass was needed for the first time in several runs.
- **Settlement mechanics are now boringly reliable.** 44 settled, due inventory 0, conflicts 0,
  all under one timing flag.
- **The `eff_n` projection accepted on 2026-07-28 is tracking exactly as forecast.** Adding 38
  equity settlements moved raw `n` 260 → 298 and left `eff_n` at 1, because the new
  target date falls inside the existing 28-day window. Dates unchanged:
  2026-08-05 and 2026-08-09.
- **Reproducing the prior run's disclosed engine caught nothing wrong with it.** Rebuilding scoring
  from `rules.md` plus the 2026-07-28 `05` methodology section reproduced that leaderboard's defensive
  character on a one-day-later basis.

## What Failed

- **Earnings grounding was silently wrong, and had been for at least three published packages.** See
  the proposed change below.
- **The MoM baseline tie-break gap became material.** Three folders tie at 0 days from target; the two
  with usable ledgers disagree by 48.2pp of hit rate
  (62.5% vs 14.3%) and by
  16.3pp of mean alpha. On 2026-07-28 this gap was judged
  cosmetic because the conclusion was invariant; today it is not.
- **`MARKET_FORECAST` lost 6 for 6 again**, every one `IN_CI` — the same directional
  failure, unchanged since the 2026-07-24 diagnosis, and still gated behind `eff_n`.

## Primary Diagnosis

**Source grounding.** The failure was not in scoring math, regime classification, or portfolio
construction — all of those behaved. It was that a *required* input (next earnings date) was being
produced by an inference chain that could return a confidently wrong answer, and nothing downstream
could tell the difference between "verified clear of earnings" and "guessed clear of earnings".

## Proposed Change (exactly one)

### Replace the vendor-empty earnings print-signature heuristic with a forward calendar sweep

**Track B — process change** (source-grounding / missing-fetch procedure fix). It changes how a
required input is *grounded*. It does not touch a scoring formula, factor weight, mu prior, confidence
mapping, sizing parameter, or any protected risk limit. The `−0.10` earnings penalty and its 14-day
window are unchanged.

**Current problem.** When `api.nasdaq.com/api/analyst/{sym}/earnings-date` returns vendor-empty — 27 of
59 shortlist names this run, routine during peak season — the rule in force (accepted 2026-07-24,
refined by gpt-5 on 2026-07-27) infers the next report date from a *past* price/volume signature:
print-like iff `|1d move| >= 3.5%` **or** (`volume >= 1.8x` trailing median **and** `|1d move| >= 1.5%`),
then assumes `+91d` and applies **no penalty**.

Two independent defects, both observed in this run's data:

1. The price-only branch fires on ordinary volatility. **ADP** moved 3.77% on 0.98× volume on
   2026-07-13 — no volume confirmation at all — and was resolved to "+91d, no penalty". **AON** moved
   3.84% on 1.03× volume. Neither move was an earnings print.
2. More fundamentally, a past move cannot establish a *future* date. The inference assumes the
   detected move **was** the most recent report, which is unverifiable from price data.

Consequence, verified against an independent source: **6 of the names the heuristic cleared —
ADP, AON, AWK, FICO, HUM, VRSK — report on 2026-07-29 itself.** ADP ranked #4 and AON #8 before regrounding.
All six would have published penalty-free at `MEDIUM` confidence while printing that morning, violating
`rules.md § Risk Controls`. A further 3 names (SCHW, ACGL, FE) were penalised by the conservative
branch despite not reporting inside the window. This is the same class the 2026-07-27 change addressed
— a non-resolution reading downstream as penalty-free — arriving by a different route.

**Artifact that exposed it.** This run's `05` preflight: a 27-of-59 vendor-empty rate looked implausible
for late July, and probing `api.nasdaq.com/api/calendar/earnings?date=2026-07-29` returned ADP directly.

**Proposed change.** Ground earnings dates from a **forward sweep of
`api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD`** over every business day from `run_date` through
`run_date + 37d`, then:

- Name appears on a dated page → **`CONFIRMED_CALENDAR`**, that date, band 0.
- Name absent from a **complete** sweep (every business day fetched, zero transport failures) →
  **`NO_PRINT_IN_WINDOW`**: it does not report before the sweep end, so `days_to > 37` and no penalty
  applies. Absence is evidence **only** when the sweep is complete; any unresolved day invalidates it
  and the run must retry or fall back.
- The per-name endpoint is retained as **corroboration**, not as the primary path.

**Hypothesis (falsifiable).** A forward calendar sweep grounds strictly more names, with strictly fewer
false "clear of earnings" calls, than the print-signature heuristic. Falsified if the sweep is
incomplete, if it disagrees with confirmed per-name dates, or if it grounds fewer names.

**Validation.**

| Test | Result |
|---|---|
| Sweep completeness | **28/28 business days, 0 failures** |
| Cross-validation vs per-name `CONFIRMED` dates | **25 agree / 0 disagree / 0 absent** |
| Universe coverage | **514/514** vs 59 shortlist names under the heuristic |
| False "clear of earnings" removed | **6** (ADP, AON, AWK, FICO, HUM, VRSK — all report 2026-07-29) |
| False penalties removed | **3** (SCHW, ACGL, FE) |
| Cost | 28 requests, ~3778 symbols, well under the previous per-name fetch count |

The Track B acceptance standard is met: (1) explicit problem statement citing the artifact that
exposed it; (2) the change **strengthens** a grounding gate — it replaces an inference with a positive
observation and cannot weaken a protected rule; (3) logged here with a `HUMAN_REVIEW` flag.

Note this is deliberately *not* a Track A change: it does not require settled-prediction evidence
because there is no scoring math to validate, which is exactly why the two-track split exists.

**Decision: `ACCEPT`** — `HUMAN_REVIEW`. Effective this run (already applied to the published set) and
standing for subsequent runs.

**Effective next step.** Future runs sweep the calendar before scoring and treat the per-name endpoint
as corroboration. If a sweep cannot be completed, the run must say so and fall back to the per-name
endpoint with the *conservative* branch only — never the "+91d, no penalty" inference.

## Observations Recorded (not proposed — one Track B per run)

1. **MoM baseline tie-break rule — next run's Track B candidate.** `agents.md § Orchestrator Step 2`
   is silent when several folders tie on distance to target. Today that swings the headline reflection
   metric by 48.2pp. A concrete proposal to evaluate next run:
   prefer the tied folder whose model family matches the running model; if still tied, prefer the one
   with a usable `15_predictions.json`; if still tied, order lexicographically by folder name — and
   require the artifact to report every tied candidate's metrics so the choice is always auditable.
   Flagged in two consecutive evolution logs (2026-07-28, 2026-07-29), which makes it **mandatory Track B
   work** under `rules.md § Two-Track Change Classification`.
2. **Three published packages carry an unquantified earnings-penalty error** (2026-07-26, -27, -28),
   since all three relied on the retired heuristic. Not retroactively corrected — prediction ledgers
   are immutable — but noted so their calibration contribution is read with that caveat.
3. **`MARKET_FORECAST` remains broken and remains gated.** 18.52% over n=54. The
   fix is Track A and unavailable until `eff_n >= 3`. The first `eff_n` increment is
   2026-08-09; do not attempt a hand-correction before then.
4. **The defensive Macro polarity now has settled support**, not just contemporaneous technicals:
   16.3pp of realized mean-alpha separation between the
   defensive and semiconductor books over the settlement window. Still `INFERRED`, still not a rule.

## Anti-Overfitting Check

The accepted change is a data-sourcing fix validated against an independent source with a falsifiable
completeness test — not a parameter tuned to recent outcomes. No factor weight, threshold, mu value or
confidence mapping was altered. No change was made on the basis of recent winners. Track A remains
frozen at `eff_n = 1` for both record types, as it has been since 2026-07-24.
