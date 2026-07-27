# 08 Risk Review — 2026-07-27

Adversarial review of the package before publication. Reviewed against the 15-point checklist in
`agents.md § Risk Committee`.

## Decision: `APPROVE` the `NO_TRADE` publication

There is no portfolio to approve or reject. What is reviewed is whether the `NO_TRADE` conclusion is
correctly derived and whether the published monitoring forecasts are honestly grounded. Both hold.

## Checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **Clean.** All 55 ledger rows carry a source; the 28 published/ETF prices pass the two-source 1% gate (27 exact to the cent, max divergence 0.396451%) and the three ETFs are brokerage-confirmed to the cent (L005–L007). Four `UNAVAILABLE` rows are disclosed, not imputed. |
| 2 | Overfitting / unvalidated signal claims | **Clean.** No parameter was fitted this run. `mu` is the unmodified table value for every name (L027); no per-name adjustment was used. Track A changes are `DEFER`red at `eff_n = 1` rather than taken. |
| 3 | Excessive event concentration | **Disclosed.** 40 of 514 universe names sit inside the buffered 14-day earnings window and 7 of 24 published names are affected, each penalised −0.10 and capped `LOW`. `NO_TRADE` #4 is not the operative trigger because the investable set is already empty. |
| 4 | Correlation / sector crowding | **Flagged, and it is a real finding.** Average pairwise correlation 0.2784 passes the 0.45 cap, but UNP/NSC at 0.9454 is effectively one position, and Industrials is 60% of the top 10 against a 30% cap. Both are recorded in `07`. |
| 5 | Portfolio beta drift outside the band | **The binding blocker.** Max attainable beta across the entire ≥80th-percentile pool is +0.8519 vs a 0.90 floor (L049). Correctly routed to `NO_TRADE` #6 (set composition), **not** `HALTED` #5 (process integrity). |
| 6 | Thesis quality below stated confidence | **Clean.** No name carries `HIGH`. Rank IC -0.1843 over ≥20 settled predictions triggers the `MEDIUM` cap, and the 7 names with earnings inside the window are further capped `LOW`. Every thesis is explicitly labelled monitoring-only. |
| 7 | Report / shared-rules mismatch | **Clean.** Exactly one status is published (`NO_TRADE`) and it is consistent across `00`, `05`, `06`, `07`, `09`, and `15`. |
| 8 | Price / derived-field citation violations | **Clean.** Every numeric `entry_price` carries `price_date` 2026-07-24 and `price_tag HISTORICAL`. No name has a populated `target_price` or CI bound without a grounded entry price. Zero `UNAVAILABLE` entry prices in either sleeve. |
| 9 | Sigma violations | **Clean.** All 24 published names and all 3 ETFs carry `sigma_source = REALIZED_VOL_30D` (L013). No round-number sigma, no blanket `sigma = UNAVAILABLE`, and no `mu = N/A` — so every published forecast is settleable at 2026-08-24. |
| 10 | Score-attribution violations | **Clean.** Every published row shows the full trace `(0.30·Fund_Z + 0.30·Tech_Z + 0.25·Sent_Z + 0.15·Macro_Z) × DQ − Penalties` with actual values, family z-scores, DQ, penalties, and metric drivers. `Fund_Z`/`Sent_Z` appear as `UNAVAILABLE` and contribute `0.00 (UNAVAILABLE)` — **never** as neutral or supportive. |
| 11 | Source Ledger violations | **Clean.** Every price, return, vol, beta, earnings date, target, CI, drawdown, ratio, indicator state and sizing input used downstream has a row in `01`. Spot-checked against `05`'s widest rows. |
| 12 | Live-sounding or stale-as-current claims | **Clean, and this run had a specific exposure here.** The 2026-07-27 session was open during execution, so a live tape existed. It is confined to `10_midday_monitor.md`, tagged `LIVE` (L050, L051), and labelled observation-only. Every forecast price is tagged `HISTORICAL` at 2026-07-24. No artifact says "closed at" or "current" about a 2026-07-27 price. |
| 13 | Improper GO-blocking | **Clean.** All five Required inputs are grounded and the `00` GO-Gate Table says so explicitly. The six missing Enhancing inputs are listed separately as confidence/exposure caps and are **not** cited as `GO` blockers anywhere. `NO_TRADE` rests on the Evidence Thresholds and the beta-band infeasibility, both legitimate. |
| 14 | Missing prediction records | **Clean.** `15_predictions.json` carries 24 `EQUITY_ALPHA` records — one per published name — each with `score_explainability`, plus all three `MARKET_FORECAST` records (SPY, QQQ, SOXX) with `benchmark: NONE`, `benchmark_price: null`, `adj_score: null`. `benchmark_price` = 738.93 is present on every equity record so alpha is computable at settlement. `settlements: []` is correct and carries the `NO_DUE_PREDICTIONS` note (due inventory 0, L054). |
| 15 | Technical indicator pack violations | **Clean.** Every TD-9, RSI, MACD, MA, momentum, volume and relative-strength value traces to `technical_indicators.json` (L019–L021) computed from adjusted closes. No script failure is hidden — 519/519 symbols returned `status: OK`. TD-9 `9` and RSI ≥ 70 are used only as exhaustion flags feeding penalties/confidence, never as standalone signals. |

## Top Three Concerns, in Severity Order

1. **The `NO_TRADE` streak is structural, and the system should stop treating it as a market call.**
   Two of four factor families have had no universe-scale fetch path for weeks, which makes Evidence
   Thresholds #2, #3 and #4 unpassable *by construction* — no market condition can clear them. Every
   run in the trailing window has published `NO_TRADE` and will keep doing so until Phase 2 of the
   Fund/Sent plan lands. This is the single highest-value fix in the system and it is an engineering
   task, not a calibration one.
2. **A known-defective forecast rule is being applied to the ETF sleeve.** `mu = beta × SPY_mu` was
   diagnosed as a category error on 2026-07-24; the settled evidence agrees
   (23.81% hit rate, n=42), and today's baseline again settled QQQ and
   SOXX MISS against a SPY HIT. The committee accepts applying it unmodified — only the evolution
   agent may change that table, and `eff_n = 1` gates Track A — but notes that the
   system is knowingly emitting forecasts it expects to be wrong, and that `eff_n` may never reach 3
   if vintages keep clustering.
3. **Bulk price history is now a single point of failure.** Yahoo is 429-blocked (8th of the last 14
   sessions) and Nasdaq's bulk-historical endpoint returned a bot-challenge page this session. Only
   stockanalysis.com served bulk history. Verification held up (CNBC + IBKR), but a stockanalysis
   outage would leave no bulk path at all.

## Required Fixes

**None blocking.** No revision pass was needed; the factor-scoring and portfolio stages were not sent
back. One integrity gap found during execution is logged as an accepted Track B change in `13`
(transient earnings-fetch failures could publish a name penalty-free) — it was caught and corrected
*within* this run, so it does not affect this package's output.

## Final Publication Recommendation

**`NO_TRADE`.** Inputs are valid and fully grounded; no candidate set meets the quality bar, and the
beta band is structurally unreachable. `HALTED` is not warranted — no fabricated or contradictory
evidence propagated. `REVIEW_ONLY` is not warranted either: the data is neither stale nor weak, it is
a fully-grounded last-completed-close basis independently verified across three sources. Per
`rules.md`, `NO_TRADE` is the accurate label when inputs are valid but candidate quality fails.
