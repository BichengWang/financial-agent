# 08 — Risk Review · 2026-08-22

**Committee decision: `APPROVE` the publication as `NO_TRADE`.**

There is no portfolio to challenge. The committee's job this run is to verify that the `NO_TRADE`
conclusion is correctly grounded, that nothing in the published monitoring sleeve overstates its
evidence, and that no `GO` blocker was mis-assigned.

## Top three concerns, in severity order

**1. A universe constituent stopped trading and two OPEN predictions reference it.** `EQR` no longer
quotes under its own symbol (renamed into / absorbed by `VMRK`), and two predictions —
`claude-opus-5-2026-07-26` (target 2026-08-23) and `gpt-5-2026-07-27` (target 2026-08-24) — come due
within two days with no settleable price. The system has a rule for what to do with an unsettleable
key (`rules.md § Canonical Settlement Ledger` item 5: report it due, do not loosen the validator) but
**no rule for detecting or surfacing the cause**, so the next run would meet this as a silent
anomaly. Severity: high, because it corrupts due inventory — the measure that gates `eff_n` and
therefore all Track A evolution. Routed to `13` as this run's Track B proposal.

**2. The published sleeve reproduces a book that just lost
2.59pp of alpha.** `Tech_Z` is
trend-persistence by construction and carries 66.7% of live conviction. The committee
accepts publication because the sleeve is explicitly non-investable and every name's forecast is
recorded for settlement — that is how the system earns calibration evidence — but requires that
`05`, `06`, and `09` state the evidence against the leaderboard **alongside** it rather than after
it. Verified: they do.

**3. `MARKET_FORECAST` CI coverage is 90.23%, above the 85% ceiling.** By
`rules.md § Rolling Calibration Metrics` these intervals are uninformatively wide and should be
tightened. The fix is a Track A change to sigma sourcing and is gated at `eff_n = 2 < 3`,
so it must be `DEFER`, not `REJECT`. The committee confirms the run did not quietly tighten sigma
anyway: all three ETF sigmas are unmodified `REALIZED_VOL_30D` (L003b, L004b, L005b).

## Review checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **Clean.** 27/27 published prices agree across 3 independent sources at 0.000000% max deviation. Three names that could not be grounded (`EQR`, `AVB`, `EA`) were excluded, not estimated (L025). |
| 2 | Overfitting or unvalidated signal claims | **Clean.** No parameter was fitted this run. The one accepted change is Track B (process), and both Track A candidates are `DEFER` on the `eff_n` gate. |
| 3 | Excessive event concentration | **Clean.** Complete forward sweep, 26/26 business days, zero transport failures. 0 of 24 published names print inside 14 days. |
| 4 | Correlation or sector crowding | **Sector crowding confirmed** — Health Care 45.0% vs the 30% cap. Correlation is fine at 0.1045 vs the 0.45 cap. Contributes to `NO_TRADE`. |
| 5 | Portfolio beta drift outside the band | **Infeasible, not drifted** — max attainable 0.4841 vs the 0.90 floor. Recomputed this run rather than inherited. |
| 6 | Thesis quality below stated confidence | **Clean.** All 24 names carry `MEDIUM`, capped by the rank-IC binding. No `HIGH` label anywhere in the package. |
| 7 | Report/rules mismatch | **Clean.** Universe, percentile label, mu bands, sigma chain, CI factor 1.04, and the 28-day target all follow `rules.md`. |
| 8 | Price/derived-field citation violations | **Clean.** Every numeric `entry_price` carries `price_date = 2026-08-21` and `price_tag = DELAYED`; no target or CI is populated against an unverified price. |
| 9 | Sigma violations | **Clean.** All 24 equity records and all 3 ETF records carry a numeric sigma with `sigma_source = REALIZED_VOL_30D`. No blanket `UNAVAILABLE`, no round unsourced sigma. |
| 10 | Score-attribution violations | **Clean.** All 24 published names have a full trace in `05` with family z-scores, DQ, penalties, three positive and three negative drivers, and metric ledger rows. `Fund_Z`/`Sent_Z` are shown `UNAVAILABLE`, never neutral or supportive. |
| 11 | Source Ledger violations | **Clean.** 171 ledger rows in `01`; every price, return, vol, beta, earnings date, target, CI, drawdown, ratio, indicator state, and sizing input used downstream has a row or is explicitly `UNAVAILABLE`. |
| 12 | Live-sounding or stale-as-current claims | **Clean.** The package says “the 2026-08-21 close” throughout and declares the Saturday fire window and closed-market vendor field rules in `01`/`03`. No use of “current” or “latest” without a ledger row. |
| 13 | Improper GO-blocking | **Clean.** All five Required inputs are grounded and none is cited as a blocker. The missing **Enhancing** inputs (options IV/skew, short interest, bid-ask tape, analyst revisions, ownership flow) are recorded as a DQ reduction to 0.80 and a `MEDIUM` confidence cap, never as `GO` blockers. `NO_TRADE` is driven by evidence thresholds 2/3/4 and by computed portfolio infeasibility — both legitimate. |
| 14 | Missing prediction records | **Clean.** `15_predictions.json` carries 24 `EQUITY_ALPHA` records (each with `score_explainability` and a numeric `benchmark_price`) plus 3 `MARKET_FORECAST` records for SPY/QQQ/SOXX with `benchmark: NONE`, `benchmark_price: null`, `adj_score: null`, and a `settlements` block of 227 rows. |
| 15 | Technical indicator pack violations | **Clean.** `01` L013 carries the full `technical_indicators.py` command plus price-input lineage; the adjusted-close tree is disclosed (L002a). TD-9 `9` and RSI extremes are handled as exhaustion flags, not trade signals. Indicator failures are marked `UNAVAILABLE` (`Q` was rejected outright as `INDICATOR_INCOMPLETE`). |

## Specific lineage verifications

- **Price/target lineage.** `target_price = entry_price x (1 + mu)` and
  `CI = entry_price x (1 + mu ± 1.04·sigma)` re-derived for all 24 published names and all 3
  ETFs; see the verification pass in `00`.
- **Sigma lineage.** Every sigma is `pstdev(30 daily adjusted returns) x sqrt(21)` from L002, tagged
  `REALIZED_VOL_30D`. The Sigma Fallback Chain never had to descend past step 2.
- **Score attribution.** `Adj Score` re-derived from the stored `score_explainability` z-scores for
  all 24 names within 2e-6.
- **Kelly threshold handling.** `0.25 x Kelly` is positive for every published name, so no name is
  blocked on the `<= 0` rule; the `< 2% NAV` penalty rule is moot because no position is sized.
- **Metric ledger coverage.** Every metric contributing to a family z-score has a ledger row
  (L300/L400 series per name).
- **Prediction-record completeness.** 24 of 24 published names appear in `15`; 3 of 3
  core ETFs appear as `MARKET_FORECAST`.
- **Settlement discipline.** All 227 due keys settled at their own
  target-date close under `ORDINARY` timing, and the post-write ledger re-run reports
  `due_inventory: 0` / `conflicts: 0`.

## Final publication recommendation

**`NO_TRADE`**, on five independent grounds — any one of which is sufficient:

| # | Ground | Evidence |
|---|---|---|
| 1 | Evidence threshold 2 | only 2 of 4 factor families are available (Fund_Z / Sent_Z UNAVAILABLE universe-wide) |
| 2 | Evidence threshold 3 | Technical carries 66.7% of live conviction, above the 50% cap |
| 3 | Evidence threshold 4 | data completeness 80% < 85% |
| 4 | Stop criteria NO_TRADE #6 | beta band structurally infeasible — max attainable sleeve beta 0.4841 < the 0.90 floor under the 5% single-name cap |
| 5 | Stop criteria NO_TRADE #6 | sector concentration — Health Care 45.0% on the naive top-20 EW sleeve, above the 30% cap |

`HALTED` was considered and rejected. `rules.md § Hard Halt Criteria` #5 reserves `HALTED` for
cap failures whose cause is process or data integrity; here the cause is **composition of the
investable set**, which `§ Downgrade to NO_TRADE` #6 assigns to `NO_TRADE`. Data integrity this run
is strong: five of five Required inputs grounded, triple-sourced prices at 0.0000% deviation, and a
complete earnings sweep.

`REVIEW_ONLY` was also considered and rejected: it is reserved for stale or weak data, and a Friday
close read on the following Saturday with all Required inputs grounded is neither.
