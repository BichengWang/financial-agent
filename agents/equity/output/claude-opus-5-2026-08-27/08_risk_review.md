# 08 — Risk Review · 2026-08-27

Skeptical committee review of the run before publication. Decision first, then the checklist.

## Committee decision

**Decision: `APPROVE` for publication at `NO_TRADE`.**

There is no portfolio to approve or reject — `07`'s Task-0 pre-check proved the beta band unreachable
before any sizing, and `05` shows zero names clearing the evidence thresholds. What the committee is
approving is the *package*: the grounding, the lineage, and the honesty of the no-trade rationale.

## Top three concerns, in severity order

**1. The score is structurally anti-predictive and the run says so plainly.** Aggregate rank IC is
-0.0840 across 60 vintages, and this run's own settlement batch returned
54 hits from
202 `EQUITY_ALPHA` settlements
(26.73%).
The committee accepts publication because the run publishes **paper forecasts under `NO_TRADE`**,
which `rules.md § Settlement Rules` explicitly requires — settled paper forecasts are how the system
earns the evidence to ever publish `GO`. The corrective is Track A and gated at `eff_n >= 3`
(currently 2); acting early would be exactly the
overfitting the gate exists to prevent.

**2. A dead ticker resolves to a different, foreign security at one price vendor.** `EQR` returns
"EQ Resources Ltd" on the ASX at 0.41 from CNBC, with `last_time` on the basis date (L026). Nothing in
this package used that value — `EQR` has no fetched history, was rejected before scoring, and its two
open prediction keys were left due rather than settled. But the *gate* that protects the price path
(`last_time` date == basis) accepts that row on its own, so the protection here came from the fetch
failing, not from the gate. That is a latent hazard and it is this run's Track B proposal in `13`.

**3. Mean z has drifted outside the healthy band.** `EQUITY_ALPHA` mean z is
-0.5553 against a -0.5…+0.5 band — realized returns
run roughly half a sigma below `mu`. Sigma is not the problem (CI coverage
71.88%, inside band); the `mu` prior is too
high for this regime. Track A, deferred.

## Review checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | None. Every numeric in the package is generated from a computed manifest; every metric carries a ledger row (177 rows in `01`). |
| 2 | Overfitting or unvalidated signal claims | None. No parameter was changed this run; the one accepted change is Track B (process), and both Track A findings are `DEFER`red on `eff_n`. |
| 3 | Excessive event concentration | No. 0 of 24 published names print inside 14 days; the complete sweep (L010) grounds the entire universe. |
| 4 | Correlation or sector crowding | Correlation passes (0.1416 < 0.45). **Sector crowding fails** — Health Care 41.67% vs the 30% cap — and is one of the NO_TRADE causes. |
| 5 | Portfolio beta drift outside the band | **Fails, and provably**: max attainable +0.2919 vs the 0.90 floor (L016). Recomputed this run, not inherited. |
| 6 | Thesis quality below stated confidence | Confidence is uniformly `MEDIUM`, capped mechanically by the rank-IC binding rather than asserted per name. No name claims a catalyst it cannot cite. |
| 7 | Report / shared-rules mismatch | None found. Statuses, tags and enumerations all use the values `rules.md` defines. |
| 8 | Price / derived-field citation violations | None. All 24 published entry prices carry `price_date` + `price_tag` and a ledger row; no target or CI is populated on an ungrounded price. |
| 9 | Sigma violations | None. Every ranked name and all three core ETFs carry `sigma` from `REALIZED_VOL_30D` with a stated source; no blanket `sigma = UNAVAILABLE` anywhere. |
| 10 | Score-attribution violations | None. All 24 published names — not just the top 20 — have family z-scores, DQ, penalties, drivers and metric ledger rows in `05`. |
| 11 | Source Ledger violations | None. Prices, vols, betas, drawdowns, earnings statuses, technical states, correlations and feasibility inputs all have rows. |
| 12 | Live-sounding or stale-as-current claims | None. The package says `DELAYED` throughout; no 'validated', 'latest' or 'reported today' claim appears without a ledger row. |
| 13 | Improper GO-blocking | None. The `01` GO-Gate Table blocks only on Required inputs, and all five are grounded; the Enhancing gaps are listed as caps. `GO` is refused on evidence thresholds and feasibility, which is correct. |
| 14 | Missing prediction records | None. `15_predictions.json` carries 24 `EQUITY_ALPHA` records with `score_explainability` plus the three `MARKET_FORECAST` records (SPY/QQQ/SOXX) with `benchmark: NONE`, `benchmark_price: null`, `adj_score: null`. |
| 15 | Technical indicator pack violations | None. Every displayed indicator cites `technical_indicators.py` command lineage (L013) and the price-history row (L002); TD-9 `9` and RSI extremes are read as exhaustion flags only. |

## Settlement and ledger review

| Item | Finding |
|---|---|
| Due inventory cleared | 229 of 231 due keys settled; the 2 left due are the `EQR` corporate-action keys, correctly reported rather than force-settled |
| Timing conventions | `WEEKEND_TARGET` (26), `ORDINARY` (153), `TARGET_DATE_CLOSE` (50) — each matches the rule its target date requires |
| Post-write verification | `settlement_ledger.py` re-run after writing `15`: due 2, conflicts 0, rejected rows 87 (unchanged from pre-write, so this run added zero validator rejections) |
| Canonical absorption | `EQUITY_ALPHA` 1153 -> 1355; `MARKET_FORECAST` 174 -> 201 |
| `eff_n` movement | unchanged at 2 for both types — the projection to 3 on 2026-09-03 (EQ) and 2026-09-07 (MF) still holds and remains falsifiable |

## Price grounding review

| Item | Finding |
|---|---|
| Symbols verified | 27 (24 published + SPY/QQQ/SOXX) |
| Independent sources | 3 — stockanalysis 5Y history (L002), CNBC (L011), Nasdaq quote-info (L012) |
| Grounded | 27/27; max deviation 0.095123%, far inside the 1% Price Sourcing Standard |
| Confirmation re-reads needed | 0 |
| Observed artifact | CNBC matched stockanalysis **to the cent on all 27**; Nasdaq `secondaryData.lastSalePrice` differed by <= 0.095% on 16 of 27 — the consolidated-tape-vs-primary-close artifact documented on 2026-07-17. Disclosed, not smoothed over. |
| Brokerage cross-check | IBKR MCP not attempted (connector invalidated since 2026-08-04, L017); logged as an absence of evidence |

## Final publication recommendation

**`NO_TRADE`.** Two independent causes, either sufficient on its own:

1. **Evidence thresholds** — 0 names clear thresholds 2, 3 and 4, because `Fund_Z` and `Sent_Z` are
   `UNAVAILABLE` universe-wide (`rules.md § Downgrade to NO_TRADE` #1).
2. **Structural infeasibility** — the published sleeve's maximum attainable beta
   (+0.2919) is below the 0.90 floor and Health Care is
   41.67% against a 30% cap (`§ Downgrade to NO_TRADE` #6).

`REVIEW_ONLY` would be the wrong label: it is reserved for stale or weak data, and all five Required
inputs are grounded at zero lag to a completed regular session. `HALTED` would also be wrong: nothing
about process integrity failed, and `§ Hard Halt Criteria` #5 routes composition-driven cap failures
to `NO_TRADE`.
