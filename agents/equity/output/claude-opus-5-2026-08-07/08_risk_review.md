# 08 — Risk Committee Review

## Decision: `REJECT` — the set becomes `NO_TRADE`

`REJECT` is the correct verdict here rather than `REVISE`: no single targeted revision can
make any name investable, because two of the four evidence thresholds are arithmetically
unsatisfiable rather than narrowly missed. This is not a failure of the candidate set.

## Review checklist

| # | Check | Finding | Verdict |
|---|---|---|---|
| 1 | Fabricated or weakly supported inputs | 27/27 published prices on 3 independent sources at 0.0000% max deviation; every score input has a ledger row | **PASS** |
| 2 | Overfitting / unvalidated signal claims | no parameter was changed on this run's data; Track A gated at `eff_n = 2 < 3` | **PASS** |
| 3 | Excessive event concentration | 1 of 24 published names have earnings <=14d; `rules.md § Stop Criteria` downgrade #4 fires above 2 | **PASS** |
| 4 | Correlation / sector crowding | avg pairwise 0.1699 (cap 0.45) PASS; Consumer Discretionary at 41.67% (cap 30%) BREACH | **MIXED** |
| 5 | Portfolio beta drift outside the band | attainable -0.3876 … 1.3387 straddles 0.90–1.10 | **PASS** |
| 6 | Thesis quality below stated confidence | no name carries HIGH; rank IC <= 0 caps all confidence at MEDIUM, and the 1 earnings names are capped LOW | **PASS** |
| 7 | Report / shared-rules mismatch | status, thresholds and sleeve isolation all conform | **PASS** |
| 8 | Price / derived-field citation violations | every numeric `entry_price` carries `price_date` + `price_tag`; no target or CI is populated on an unverified price | **PASS** |
| 9 | Sigma violations | all 24 published names + 3 ETFs carry `REALIZED_VOL_30D` with a stated source; no blanket `UNAVAILABLE` | **PASS** |
| 10 | Score-attribution violations | all 24 published names have a full trace, family z-scores, DQ, penalties and drivers in `05` | **PASS** |
| 11 | Source Ledger violations | every price, return, vol, beta, earnings date, target, CI, drawdown, ratio and indicator state used downstream has a row in `01` | **PASS** |
| 12 | Live-sounding or stale-as-current claims | prices are described as the completed 2026-08-07 close, tagged `HISTORICAL`; no 'current'/'latest' language without a ledger row | **PASS** |
| 13 | Improper GO-blocking | all 5 Required inputs grounded; no Enhancing input is cited as a GO blocker; `NO_TRADE` rests on evidence thresholds and two hard caps | **PASS** |
| 14 | Missing prediction records | 24 EQUITY_ALPHA + 3 MARKET_FORECAST records emitted, all with `score_explainability` (null on MF per spec); Core ETF block complete | **PASS** |
| 15 | Technical indicator pack violations | every displayed state cites `L019` (command + formula) and `L002` (price input); TD-9/RSI treated as exhaustion flags only | **PASS** |

## Top three concerns, in severity order

**1. Two factor families are dark, and the run cannot say what it does not know.**
`Fund_Z` and `Sent_Z` are `UNAVAILABLE` across all 511 names (`L022`, `L023`). The committee's
specific concern is *presentation*, not just coverage: a composite that silently treats two
missing families as 0.00 can read like a four-family consensus. `05` states the live score as
`(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` and shows `UNAVAILABLE` rather than `0.00` in the
attribution table. Verified: no artifact in this package describes a missing metric as neutral
or supportive.

**2. The leaderboard is a single-signal ranking with a negative measured rank IC.**
`Tech_Z` carries 66.67% of live conviction and is essentially trend persistence.
Weighted-mean rank IC is -0.0430 over
643 settled records, and the settled hit rate is 39.04% against a >50%
healthy bar. The committee accepts publication of the monitoring sleeve — unsettleable
forecasts are worse than wrong ones — but requires that `06` and `09` not present the ranking
as a multi-factor consensus. Verified in both.

**3. Event concentration exceeds the stop-criteria threshold.**
1 published names carry earnings inside 14 days (TPR),
against `rules.md § Stop Criteria` downgrade #4's threshold of more than 2. Each carries the
-0.10 penalty and a LOW confidence cap. On its own this would force `NO_TRADE`; here it is one
of three independent triggers.

## Specific lineage audits

| Audit | Finding |
|---|---|
| Price / target lineage | every target is `entry x (1 + mu)` and every CI is `entry x (1 + mu +/- 1.04 sigma)` off a grounded raw close (`L003`, `L101`–`L124`); re-derived in the verification pass |
| Sigma lineage | `REALIZED_VOL_30D` = population stdev of 30 daily adjusted returns x sqrt(21) (`L201`–`L224`); no round or sourceless sigma |
| Score attribution | `Adj Score` re-derived from stored `score_explainability` for all 24 records within 2e-6 |
| Metric ledger coverage | all 10 scoring slots are 100% sourceable across the universe; all clear the 70% bar |
| Kelly threshold handling | 0.25 x Kelly spans 0.175–74.344; none <= 0, so none is blocked on Kelly; confidence capped where < 2% NAV |
| Technical indicator lineage | every state cites `L019` (script + formula) and `L002` (adjusted price input); relative strength displayed but excluded from scoring to avoid double-counting momentum |
| Source Ledger completeness | no downstream artifact introduces a fact absent from `01` |
| GO-blocking discipline | no Enhancing input is used as a blocker; the GO-Gate Table lists only Required inputs |
| Prediction-record completeness | 24 + 3 records; every ranked name is present; `benchmark_price` set on all EQUITY_ALPHA and null on all 3 MARKET_FORECAST per spec |
| Settlement handling | the committee specifically reviewed the decision **not** to publish 50 computed settlements. Publishing rows the canonical normalizer rejects would permanently inflate the audit-only pile and misstate due inventory. `rules.md § Canonical Settlement Ledger` item 5 is directly on point. **Endorsed.** |

## Final publication recommendation

**`NO_TRADE`.** Three independent triggers, any one of which is sufficient:

1. Evidence thresholds #2, #3 and #4 fail for every name (structural, unsatisfiable today).
2. 95th-percentile 1-month drawdown 9.15% > 8% cap
   (`rules.md § Stop Criteria` downgrade #5).
3. Consumer Discretionary concentration 41.67% > 30% cap
   (downgrade #6); and event concentration 1 > 2 (downgrade #4).

No `HALTED` condition applies: data lineage is complete, the benchmark is present, and no
fabricated or contradictory evidence was found. The monitoring sleeve and the Core ETF forecast
block publish as normal so they can be settled later.
