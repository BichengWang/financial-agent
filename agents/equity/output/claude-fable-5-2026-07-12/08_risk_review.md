# 08 Risk Committee Review

**Decision: APPROVE — publish as REVIEW_ONLY.** (Weekend session; monitoring-sleeve forecasts only; no trade recommendation to challenge.)

## Checklist Findings (rules.md §Risk Committee items 1–15)

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated/weak inputs | None found. Every price is a 2026-07-10 official close fetched this run, Yahoo + Nasdaq two-source verified at 0.0000% divergence on all 27 checked symbols (01 header) |
| 2 | Overfitting/unvalidated signals | Score methodology unchanged from 07-05..07-09; now backed by settled evidence (weighted rank IC +0.200, n=46) rather than assumption |
| 3 | Event concentration | Zero top-10 names inside the 14d confirmed-earnings window; 28 shortlist names penalized out on **confirmed** dates (upgrade from estimates) |
| 4 | Correlation/sector crowding | Top-10 avg pairwise corr 0.134; security-software cluster (0.66–0.79) flagged in 07; IT 8/24 of the published list — cap enforceable |
| 5 | Beta drift | No portfolio drafted; equal-weight sketch beta 0.835 below band — disclosed in 07, consistent with the standing structural tension |
| 6 | Thesis vs confidence | All names LOW confidence; thesis text labeled INFERRED; no name claims more than its 2/4-family evidence |
| 7 | Report vs shared rules | 05/06/07 inherit without recomputation; percentiles labeled INDEX_UNION_PCTL (n=513) |
| 8 | Price/derived-field citations | Every entry has price_date + price_tag; every target/CI derives from tagged entries (spot-checked DVA, FFIV, DOC, ANET, LLY against 01 rows L109–L252) |
| 9 | Sigma violations | None: every ranked name carries sigma = REALIZED_VOL_30D with formula lineage; no blanket UNAVAILABLE |
| 10 | Score-attribution | Full traces in 05 (family z, DQ 0.80, penalties, drivers, ledger rows); missing families shown as 0.00 (UNAVAILABLE), never neutral-positive |
| 11 | Source Ledger | 252 rows; OBSERVED 118 / DERIVED 133 / INFERRED 1; zero UNAVAILABLE-critical rows; settlements cite entry + settlement close rows |
| 12 | Live-sounding claims | None: weekend run consistently states "official 2026-07-10 close"; IBKR closed-market lag behavior explicitly labeled a prior-record consistency check |
| 13 | GO-blocking discipline | Correct: missing Fund/Sent treated as Enhancing caps (DQ 0.80, LOW, 50% gross cap noted); REVIEW_ONLY on the weekend rule, not on Enhancing inputs |
| 14 | Prediction records | 27 records (24 EQUITY_ALPHA with score_explainability + SPY/QQQ/SOXX MARKET_FORECAST with mu_derivation) + 20 settlements — publishing gate satisfied |
| 15 | Technical indicator lineage | All TD9/RSI/MACD/MA/momentum/VR/RS values cite technical_indicators.json (2026-07-12T12:30:39Z) + price rows; no standalone-signal use; SATS/FDXF failures surfaced as exclusions |

## Settlement-Specific Review (this run's judgment call)

The **WEEKEND_TARGET** treatment (settling the 20 due 2026-07-12-target records at the 2026-07-10 close) was reviewed against the alternative (deferring to Monday 2026-07-13): the rules.md contract "settle every OPEN prediction whose target_date <= run_date" binds today, no tradable price can print between the Friday close and the Sunday target, and the vintage itself entered at a Sunday run-date on Friday-close prices — the treatment is symmetric and economically exact. The judgment is disclosed in 02 §0, 01 header, and on every settlement record. **Accepted.**

## Top Three Concerns (severity order)

1. **REIT sigma calibration** — both REIT settlements today broke low (AMT, PLD OUT_CI_LOW, ~2.4x sigma downside) while DOC ranks 9 in today's sleeve. Not actionable at n=2; logged as a 13 watch item. Mitigant: DOC's block carries the explicit caution note.
2. **Chronic family gap** (10th consecutive run) — with Fund/Sent unwired the system can never publish GO regardless of data quality; the standing Track B escalation continues (13).
3. **Leaderboard event turnover** — 28 confirmed prints inside 14d mean this sleeve's composition will churn through 07-17; forecasts remain settleable regardless (that is the ledger's purpose), but readers should not treat rank stability as signal this week.

## Publication Recommendation

**REVIEW_ONLY** — artifacts complete, grounding gates passed, predictions ledger written. No revision required.
