# 03 Regime and Data — 2026-07-29

## Data Mode Declaration

**`DELAYED`** (`rules.md § Data Mode Taxonomy`). Quotes were fetched this run with <= 1-day lag: the
basis is the 2026-07-28 close, retrieved pre-open on 2026-07-29. All five Required inputs are grounded, so this
mode is `GO`-eligible at reduced exposure — it is **not** `DELAYED_PARTIAL`, and the `NO_TRADE` outcome
has nothing to do with data mode.

`ILLUSTRATIVE_MODE` is **not** in force. No field in this package is `ILLUSTRATIVE_REF`.

## Data Integrity

| Check | Result |
|---|---|
| History fetch | 519/519 symbols, zero failures (L003) |
| Last bar on every symbol | 2026-07-28 — uniform, no straggler (L003) |
| Entry-price cross-verification | 28/28 exact to the cent (L011) |
| Benchmark (SPY) history | 1255 bars — far above the 60-day minimum (L004) |
| Corporate-action scan | 1 of 519 symbols ex-dividend on the basis bar (WST), resolved per the 2026-07-26 rule (L003) |
| Earnings-date grounding | 514/514 of the scored universe (L022) |

No contradictory or missing critical field. No `HALTED` condition.

## Regime Classification — **`NEUTRAL`** (L042)

| Evidence | Value | Reading |
|---|---|---|
| SPY close vs MA20 | 740.86 vs 746.65 | **below** |
| SPY close vs MA50 | 740.86 vs 743.99 | **below** |
| SPY 20d / 60d momentum | -0.02% / +3.35% | flat near-term, mildly positive medium-term |
| SPY RSI(14) daily | 47.36 | neutral (30–70) |
| SPY MACD daily | BELOW_SIGNAL | negative |
| SPY TD-9 daily | BUY_SETUP_9 | exhaustion flag on the **buy** side — not a trade signal alone |
| VIX close | 18.21 | below the 28 `HIGH_VOL` trigger |
| SOXX from 60d high | -24.97% | deep semis drawdown |
| TLT 20d momentum | -3.31% | long duration selling off |
| Universe at negative beta | 42.02% | unusually broad defensive dispersion |

`BULL` is excluded — SPY sits below both moving averages with a negative MACD. `BEAR` is excluded —
60-day momentum is still +3.35%, above the −5% trigger. `HIGH_VOL` is excluded —
VIX 18.21. `RATE_SHOCK` is not supported: TLT is weak (-3.31% over 20d)
but there is no disorderly move. **`NEUTRAL`** is the defensible label.

**Consistency note.** A flat index masking a 25.0% semis drawdown and
42.0% of names at negative beta is a *rotation*, not a broad drawdown — the
index level is being held up by exactly the defensive cohort that dominates the leaderboard in `05`.

## Core ETF Market Forecast Block

Per `rules.md § Core ETF Market Forecast`. These are a **market-forecast sleeve** — never candidates,
never universe members, exempt from the single-name filters, and they count toward no portfolio cap.

mu derivation, never free-handed: regime `NEUTRAL` → **SPY prior +0.50%**;
QQQ and SOXX take `beta_to_SPY x SPY mu` with beta from 60 days of fetched daily returns.
**No adjustment was applied to any of the three** (the rule permits ±1.0pp on SPY and ±1.5pp on
QQQ/SOXX with a ledger-backed reason; none is claimed).

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 740.86 | 2026-07-28 | HISTORICAL | -0.02% / +3.35% | 3.68% | +1.0000 | +0.5000% | 3.6764% | REALIZED_VOL_30D | 744.56 | 2026-08-26 | 716.24 | 772.89 | MEDIUM | L004-L006, L043, L044 |
| QQQ | 675.49 | 2026-07-28 | HISTORICAL | -6.71% / +1.27% | 7.39% | +1.7309 | +0.8654% | 7.3946% | REALIZED_VOL_30D | 681.34 | 2026-08-26 | 629.39 | 733.28 | MEDIUM | L004-L006, L043, L044 |
| SOXX | 491.46 | 2026-07-28 | HISTORICAL | -20.00% / +6.56% | 19.18% | +3.6481 | +1.8241% | 19.1803% | REALIZED_VOL_30D | 500.42 | 2026-08-26 | 402.39 | 598.46 | MEDIUM | L004-L006, L043, L044 |

### Analysis minimum (per ETF)

| Metric | SPY | QQQ | SOXX |
|---|---|---|---|
| Close vs MA20 | 740.86 vs 746.65 | 675.49 vs 708.06 | 491.46 vs 555.62 |
| Close vs MA50 | 740.86 vs 743.99 | 675.49 vs 716.37 | 491.46 vs 568.10 |
| 30d realized vol | 3.68% | 7.39% | 19.18% |
| Prior 30d realized vol | 3.93% | 6.91% | 17.99% |
| Vol direction | **FALLING** | **RISING** | **RISING** |
| Drawdown from 60d high | -2.21% | -9.37% | -24.97% |

### Relative strength

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | -6.69pp | -2.08pp |
| SOXX / SPY | -19.98pp | +3.20pp |

**Regime-consistency check.** The block is internally consistent with `NEUTRAL` — SPY vol is
falling and its drawdown shallow (-2.21%),
while QQQ and SOXX both show **rising** vol and far deeper drawdowns. It is *not* consistent with the
mu column, and that must be stated plainly rather than presented as a view: the rule mechanically
assigns SOXX the **largest positive** mu (+1.8241%, from beta
+3.6481) precisely because it is the most volatile and most beaten-down name
in the sleeve. That is the documented `mu_ETF = beta x SPY_mu` category error (see `02 § 0`), it has
produced a 18.52% direction rate over n=54, and correcting it is a Track A change
gated at `eff_n = 1` until 2026-08-09. The rule is applied
as written and the defect is disclosed rather than silently hand-corrected.

## Event Concentration

| Flag | Count | Note |
|---|---|---|
| Universe names with earnings inside 14 calendar days | **272** of 514 | peak Q2 season (L022, L024) |
| Names reporting **today** (2026-07-29) | **56** | includes 6 that the retired heuristic had scored penalty-free |
| Published-set names with earnings inside 14 days | **1** of 24 | ADP only — penalised −0.10, confidence `LOW` |
| FOMC inside horizon | not sourced | no calendar feed wired; `UNAVAILABLE`, Enhancing only |

`rules.md § Downgrade to NO_TRADE` #4 (more than 2 names with earnings inside 14 days) applies to the
*investable* set. That set is empty, so the trigger is moot — but note the published monitoring sleeve
carries only 1 such name, so it would not have fired regardless.

## Universe Handoff

514 scored names from the 515-name index union (see `04`), plus core ETFs SPY, QQQ, SOXX
and TLT handed to `technical_indicators.py` for the daily/weekly/monthly pack (L021).

## Stop-Rule Assessment

No `HALTED` condition: lineage is complete, the benchmark series is present, and no core field is
missing or contradictory. No `REVIEW_ONLY` condition: the data is a same-day-fresh completed close, not
stale. Recommendation to the orchestrator: **proceed to scoring**; status is a composition question.
