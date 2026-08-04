# 08 — Risk Review — 2026-08-03

## Committee decision: **`NO_TRADE`**

Not `REVISE` — there is no proposal to revise. Not `HALTED` — no fabricated, inconsistent or
contradictory evidence was found. Not `REVIEW_ONLY` — the data is neither stale nor weak: all five
Required inputs are grounded on a completed same-day close.

## Top three concerns, in severity order

**1. The score's rank ordering is anti-correlated with realized alpha, and it stays that way.**
Weighted-mean rank IC **-0.0879** over n=515 settled records, non-positive in **20 of
32** vintages. This run's own settled batch is consistent with it: 19/76 direction hits
(25.00%) with mean z -0.8561. The committee accepts the
`MEDIUM` confidence cap as the correct mechanical response and notes it is a cap, not a cure. The
`Tech_Z` deduplication applied this run is the first structural attempt at the cause; its effect
cannot be judged until `eff_n >= 3`.

**2. `MARKET_FORECAST` mu is a known category error, and it is still being published.**
`mu = beta x SPY_mu` gives SOXX a **+7.06%** four-week call off a
+2.0% SPY prior, trimmable only to +5.56% inside the ±1.5pp band.
Settled hit rate is **22.09%** over n=90. The committee's position: continuing to publish a
forecast known to be mis-specified is defensible **only** because it is labelled, disclosed, and
accumulating the evidence needed to fix it under Track A — and that fix is gated at `eff_n` = 1 < 3.
It would not be defensible if any capital were being allocated against it.

**3. Two of four factor families have no fetch path at all.** This is the root cause of every
non-`GO` run since 2026-07-01 and it is not a market condition. It caps DQ at 0.80, makes three of
five Evidence Thresholds unsatisfiable, and concentrates 66.67% of live conviction in a single
family — itself a threshold-3 violation by construction.

## Required-checks review

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | None. 27/27 published symbols grounded on three independent sources, max deviation 0.0788%. No price failed the Price Sourcing Standard. |
| 2 | Overfitting or unvalidated signal claims | None adopted. The one engine change this run was accepted under Track B on evidence of a mathematical identity, not on performance. No parameter was tuned to recent outcomes; `eff_n` = 1 forbids it. |
| 3 | Excessive event concentration | 153 of 512 scored names print inside 14 days — peak Q2 season. Each carries the -0.10 penalty on a calendar-grounded date. 1 of the published 24 are affected. |
| 4 | Correlation or sector crowding | Diagnostic sleeve average pairwise correlation +0.1482, well inside the 0.45 cap; largest sector 30.0%, inside 30%. |
| 5 | Portfolio beta drift | Not applicable — no portfolio. Feasibility recomputed: attainable [-0.5565, +1.4240], band **feasible**. The naive sleeve's +0.5323 would fail, which is a selection issue, not an infeasibility. |
| 6 | Thesis quality below stated confidence | Every thesis is labelled `INFERRED` and every confidence is `MEDIUM` — no name claims more than its evidence supports. |
| 7 | Report vs shared-rules mismatch | None found. Family weights, protected caps and the mu tables are unmodified. |
| 8 | Price/derived-field citation violations | None. Every numeric `entry_price` carries `price_date` 2026-08-03 and `price_tag` `HISTORICAL`; no target or CI is populated on an unverified price. |
| 9 | Sigma violations | None. All 24 equity records and all 3 ETF records carry `REALIZED_VOL_30D` with a computed value; no blanket `sigma = UNAVAILABLE`, no round sigma. |
| 10 | Score-attribution violations | None. Every ranked name discloses family z-scores, DQ, penalties, top positive and negative drivers and metric ledger rows. Unavailable families are shown as `UNAVAILABLE`, never as neutral. |
| 11 | Source Ledger violations | None. 177 rows in `01` cover every price, return, vol, beta, earnings date, target, CI, drawdown, ratio, indicator state and sizing input used downstream. |
| 12 | Live-sounding or stale-as-current claims | None. All prices are described as the completed 2026-08-03 close and tagged `HISTORICAL`. |
| 13 | Improper GO-blocking | None. The GO-Gate Table in `00` lists only the five Required inputs, all PASS. The six missing Enhancing inputs are recorded as caps, never as blockers. Conversely, no `GO` is claimed with a missing Required input. |
| 14 | Missing prediction records | None. All 24 ranked names appear in `15_predictions.json` with `score_explainability`; the Core ETF block is complete with three `MARKET_FORECAST` records carrying `benchmark: NONE`, `benchmark_price: null`, `adj_score: null`. |
| 15 | Technical indicator pack violations | None. Every indicator cites the `technical_indicators.py` command and its price-input lineage in `01`. TD-9 and RSI are treated as exhaustion flags, MACD as supportive only when aligned with momentum. Monthly gaps on 7 recently-listed names are marked `UNAVAILABLE`, not hidden. |

## Lineage spot-checks performed

| Lineage | Verification |
|---|---|
| Price -> target -> CI | `target = entry x (1 + mu)` and `CI = entry x (1 + mu -/+ 1.04*sigma)` re-derived for all 24 published rows and all 3 ETF rows |
| Sigma | `REALIZED_VOL_30D` = stdev of the last 30 daily adjusted returns x sqrt(21); recomputed independently |
| Score attribution | `Adj Score` re-derived from the stored `score_explainability` z-scores for all 24 rows |
| Settlement timing | All 88 settlements re-validated by `settlement_ledger.py`: 0 conflicts, due inventory 0 |
| Kelly threshold handling | `0.25 x Kelly` computed for every ranked name; 0 names in the pctl>=80 pool have `0.25 x Kelly <= 0` (which would block investable status) |
| Engine reproduction | Prior package reproduced from the same 2026-07-31 basis; found and fixed a drawdown-polarity defect before publication (see `05`, `13`) |

## Final publication recommendation

**`NO_TRADE`.** Inputs are valid and fully grounded; no candidate set meets the quality bar. The
binding constraint is `rules.md § Downgrade to NO_TRADE` #1 — fewer than 5 names pass the investable
threshold (zero do) — and the cause is missing factor-family evidence, not market conditions,
portfolio infeasibility or stale data.
