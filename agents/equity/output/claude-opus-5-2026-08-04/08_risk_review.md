# 08 — Risk Review — 2026-08-04

## Committee decision: **APPROVE PUBLICATION AS `NO_TRADE`**

There is no portfolio to approve or reject. The committee's job here is to confirm that the
`NO_TRADE` conclusion is correctly reasoned, that nothing fabricated propagated, and that the
monitoring sleeve is auditable enough to settle later.

## Review checklist (`agents.md § Risk Committee`)

| Check | Result | Evidence |
|---|---|---|
| 1. Fabricated or weakly supported inputs | **PASS** | every downstream fact has a Source Ledger row in `01`; 28/28 verified prices agree across 3 independent sources to the cent |
| 2. Overfitting / unvalidated signal claims | **PASS** | no Track A change proposed; `eff_n`=1 < 3 so calibration proposals are `DEFER`red by rule, not adopted |
| 3. Excessive event concentration | **PASS (disclosed)** | 142 of 512 scored names print within 14 days (peak Q2 season); 1 inside the published 24, each penalised `-0.10` and capped `LOW` |
| 4. Correlation / sector crowding | **PASS** | naive sleeve average pairwise correlation 0.1482 < 0.45; max sector 30.0% ≤ 30% |
| 5. Portfolio beta drift outside the band | **N/A — no portfolio** | diagnostic sleeve beta +0.5323 would breach the 0.90 floor; recorded as an independent `NO_TRADE` trigger, not a published position |
| 6. Thesis quality below stated confidence | **PASS** | all confidence is capped `MEDIUM` by the rank-IC binding (-0.0879); theses are labelled `INFERRED` |
| 7. Report/rules mismatch | **PASS** | artifact set matches `runbook.md`; 11/12 omitted because those checkpoints did not run (rule 4) |
| 8. Price/derived-field citation violations | **PASS** | every `entry_price` carries `price_date` 2026-08-03 + `price_tag` `HISTORICAL`; no target/CI is populated on an ungrounded price |
| 9. Sigma violations | **PASS** | all 205 ranked names carry `mu` from the calibration band and `sigma` from `REALIZED_VOL_30D`; no blanket `UNAVAILABLE` |
| 10. Score-attribution violations | **PASS** | every ranked name discloses family z-scores, DQ, penalties, positive/negative drivers and metric ledger rows; `Fund_Z`/`Sent_Z` are `UNAVAILABLE`, never neutral |
| 11. Source Ledger violations | **PASS** | no price, return, vol, beta, earnings date, target, CI, drawdown, indicator state or sizing input is used without a ledger row |
| 12. Live-sounding / stale-as-current claims | **PASS** | the basis is described as the 2026-08-03 completed close throughout; the intraday tape appears only in `10`, explicitly labelled live and observation-only |
| 13. Improper `GO`-blocking | **PASS** | no Enhancing input blocks `GO`; all five Required inputs are grounded and `NO_TRADE` is driven by the Evidence Thresholds |
| 14. Missing prediction records | **PASS** | 24 `EQUITY_ALPHA` records with `score_explainability` + 3 `MARKET_FORECAST` records (`benchmark: NONE`, `benchmark_price: null`, `adj_score: null`) + 48 settlements |
| 15. Technical indicator pack violations | **PASS** | every indicator value cites `technical_indicators.py` command/formula lineage plus `L-HIST-001`; TD-9 and RSI are treated as exhaustion flags, never standalone signals |

## Top three concerns, in severity order

**1. The score is not rank-predictive, and this run publishes 24 records anyway.**
Weighted-mean rank IC is -0.0879 over n=515, non-positive in
20 of 32 vintages. Publishing forecasts
from a score with inverted rank ordering is defensible **only** because these are paper records that
generate the settlement evidence needed to fix it — and because confidence is capped `MEDIUM`
everywhere. It would not be defensible at `GO`. The committee accepts it on that basis and notes the
live intraday corroboration in `10`.

**2. `Macro_Z` is not reproducible from the prior disclosure — one slot remains unpinned.**
`rate_sens` reproduces only to 0.1951 against the prior package's
published drivers, versus ≤0.0060 for
every other slot. This run publishes a normative Metric Definition Table that fixes the convention
going forward, but the committee records that **prior packages' `Macro_Z` values cannot be exactly
reconstructed**, which limits cross-run comparability of `Macro_Z` (not of `Tech_Z`, which now
reproduces to 0.0001).

**3. The published sleeve is structurally defensive and would fail two hard caps if traded.**
Beta +0.5323 against a 0.90 floor and a 8.50%
95th-percentile drawdown against an 8% cap. The attainable beta range
[-0.5413, +1.3472] comfortably contains the
band, so this is a **selection** problem, not a feasibility problem — the ranking systematically
prefers low-beta names. Recorded as evidence for the rank-inversion diagnosis.

## Specific lineage reviews required by the checklist

| Lineage item | Finding |
|---|---|
| Price / target lineage | `entry_price` = raw close 2026-08-03 (`L-PX-*`); `target_price = entry x (1 + mu)`; CI = `entry x (1 + mu ± 1.04*sigma)`. Re-derived for all 24 in the verification pass. |
| Sigma lineage | `REALIZED_VOL_30D` = population stdev of the trailing 30 adjusted daily returns x sqrt(21) (`L-RM-*`). Chain step 1 (`IV30`) unavailable — no options feed, documented. |
| Score attribution | full trace per name; `Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties` with actual values. |
| Metric ledger coverage | 512/512 scored names carry `L-TI-*` and `L-RM-*` equivalents; the published 24 carry explicit rows in `01`. |
| Kelly threshold handling | `0.25 x Kelly` computed for every ranked name; 0 names in the pctl≥80 pool fall below the 2% NAV threshold. No name is marked investable, so no Kelly gate is load-bearing this run. |
| Technical indicator lineage | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adjusted CSVs>`; states interpreted per `rules.md § Technical Indicator Pack Definition`. |
| Source Ledger completeness | no downstream fact lacks a row; `Fund_Z`/`Sent_Z` correctly carry no rows and are `UNAVAILABLE`. |
| `GO`-blocking discipline | only Required inputs were considered as blockers; all five are grounded. |
| Prediction-record completeness | 24 + 3 records; no `HIGH` confidence; no zero sigma; every `EQUITY_ALPHA` carries a numeric `benchmark_price` (757.67). |

## Final publication recommendation

**`NO_TRADE`** — inputs are valid and fully grounded; no candidate set meets the quality bar.
Not `REVIEW_ONLY`: the data is neither stale nor weak (a 2026-08-03 close verified to the cent on three
sources is the freshest completed close available). Not `HALTED`: no integrity failure. Not `GO`:
zero names clear the Evidence Thresholds.
