# 08 — Risk Review · 2026-09-03

Committee decision: **`APPROVE` for publication as `NO_TRADE`.** No portfolio is proposed, so
there is no sizing to challenge; the review below is of the evidence, the lineage and the
publication decision itself.

## Review checklist

| # | Check | Finding | Verdict |
|---|---|---|---|
| 1 | Fabricated or weakly supported inputs | every price, return, vol, beta, indicator state, target, CI bound and earnings date used downstream has a `01` ledger row; the two dark families are marked `UNAVAILABLE`, never imputed | clean |
| 2 | Overfitting or unvalidated signal claims | no parameter changed this run; `eff_n` reached 3 so Track A is *eligible*, and `13` still declines to spend it on an untested change | clean |
| 3 | Excessive event concentration | 0 of 24 published names print inside 14 days against a limit of 2; the forward sweep is complete (27/27 days, 0 failures) | within limits |
| 4 | Correlation or sector crowding | avg pairwise correlation 0.1227 passes the 0.45 cap, but the naive sleeve's largest sector is 40.00% against a 30% cap, and factor crowding is flagged (Technical carries 66.7% of conviction) | **flagged** — an independent NO_TRADE trigger |
| 5 | Portfolio beta drift outside the band | naive sleeve beta +0.1187 vs the 0.90-1.10 band; the band itself is *attainable* (-0.6671 to +1.4337), so this is a composition failure, not an infeasibility | **flagged** |
| 6 | Thesis quality below stated confidence | every published name is `MEDIUM`, the cap forced by negative aggregate rank IC; no name claims `HIGH` | clean |
| 7 | Mismatch between the report and the shared rules | status, thresholds, mu bands, CI factor 1.04 and the Tech_Z six-slot construction all match `rules.md` | clean |
| 8 | Price / derived-field citation violations | all 24 entry prices carry `price_date` + `price_tag`; no target or CI bound exists beside an `UNAVAILABLE` entry price | clean |
| 9 | Sigma violations | every ranked name and every core ETF carries `REALIZED_VOL_30D`; no blanket `sigma = UNAVAILABLE` anywhere | clean |
| 10 | Score-attribution violations | the `05` attribution table spans all 24 published names with family z-scores, DQ, penalties, drivers and metric ledger rows | clean |
| 11 | Source Ledger violations | no downstream numeric lacks a ledger row | clean |
| 12 | Live-sounding or stale-as-current claims | prices are described as basis-date closes with `DELAYED` tags; no 'current'/'latest' language sits on an unsupported claim | clean |
| 13 | Improper GO-blocking | all five Required inputs are grounded and `01` says so explicitly; the block is the evidence thresholds, and no Enhancing input is cited as a blocker | clean |
| 14 | Missing prediction records | 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` records written, each equity record with `score_explainability`; the Core ETF block is complete in `03` | clean |
| 15 | Technical indicator pack violations | every displayed indicator cites `technical_indicators.py` (L013) and the price-history row (L002); TD-9 `9` and RSI extremes are treated as exhaustion flags, not trade signals | clean |

## Price and sigma lineage

| Item | Finding |
|---|---|
| Primary source | stockanalysis 5Y daily history, raw close `c` for entry/target/CI (L002) |
| Independent check 1 | CNBC `last`, gated on basis-date `last_time` **and** a US venue **and** volume > 0 — the symbol-reuse gate effective 2026-08-28; agreement to the cent on 25/26 (L011) |
| Independent check 2 | Nasdaq `secondaryData.lastSalePrice` gated on the 'Closed at' marker; max deviation 0.3234% (L012) |
| Grounding result | 27/27 grounded, 1 confirmation re-reads (L012a) |
| Sigma lineage | `REALIZED_VOL_30D` = pstdev(30 daily **adjusted** returns) x sqrt(21); IV30 skipped at chain step 1 because no options feed is wired (L500-series) |
| Corporate-action guard | the symbol-reuse gate rejected `EQR` (CNBC returns 'EQ Resources Ltd' on ASX). Under a date-only gate that row would have been accepted at a ~99% price error (L025, L026) |

## Two things the committee wants on the record

**1. The `VENDOR_BAR_LAG` class is a near-miss, not a clean pass.** The 18:11 ET fire found
22 live large-caps with
no basis bar at the primary vendor. The 2026-08-22 liveness screen keys on exactly that condition,
and applying it without the two-reference confirmation it mandates would have dropped those names
from the scored universe with a corporate-action label. The screen behaved correctly *because* it
requires two references; the run's own fire-time choice is what created the exposure. `13` carries
this forward.

**2. Track A is now eligible and was deliberately not spent.** `eff_n` reached
3 for `EQUITY_ALPHA` this run — the first time the gate has opened since it was built
on 2026-07-24. `rules.md § Evolution Policy` permits a calibration proposal; `13` records an
observation and defers instead, because the diagnosed defect is a **rank-order inversion** and the
only tested Track A remedies to date (mu shrink, sigma widen, beta damping, trend amplification)
are monotonic transforms that cannot repair a rank ordering. Eligibility is not a reason to change
something.

## Engine reproduction test

`05 § Reproduction test against the prior package` records a rebuild of the **2026-08-28** package
from this run's normative Metric Definition Table alone. Reproduced
24/24 published names with `Tech_Z` max abs difference
0.0391, `Macro_Z` 0.0012 and `Adj Score`
0.0094, against a one-name difference in the scored cross-section
(509 vs 510). The committee treats this as the strongest available
evidence that the scoring code and the published methodology are the same thing — it is the check
that caught a drawdown-polarity sign error on 2026-08-03 and a window-length convention error on
2026-08-04, and it shows neither signature today.

## Prediction-record completeness

| Requirement | Status |
|---|---|
| one record per ranked/monitored name | 24/24 |
| `score_explainability` on every new equity record | 24/24 |
| three core-ETF `MARKET_FORECAST` records | 3/3 (SPY, QQQ, SOXX) |
| `benchmark_price` present on equity records, `null` on market-forecast records | conforms |
| no `HIGH` confidence | 0 of 27 |
| no zero sigma | 0 of 27 |
| settlements block | 111 rows plus 2 disclosed unsettleable key(s) |

## Decision

**`APPROVE` — publish as `NO_TRADE`.**

Top three concerns, in severity order:

1. **Structural, not fixable in-run:** two of four factor families are `UNAVAILABLE` universe-wide,
   which makes evidence thresholds 2, 3 and 4 unsatisfiable and guarantees an empty investable set
   regardless of market conditions. This is the same blocker every run has reported since July.
2. **Composition:** the rank-ordered sleeve is too defensive and too sector-concentrated to hold
   the beta band, even though the band is attainable from the eligible pool.
3. **Evidence base leakage:** 2 prediction key(s) can never settle
   because the underlying ticker no longer trades, permanently subtracting from the `eff_n` the
   evolution gate depends on.
