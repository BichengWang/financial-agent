# 08 Risk Review — 2026-07-26

Adversarial committee review of the proposed publication. Reviewing a `NO_TRADE` recommendation with a 24-name monitoring sleeve and 17 settled predictions.

## Decision

**`APPROVE`** — publish as `NO_TRADE`.

The recommendation not to trade is correct and over-determined. The committee's scrutiny therefore falls where it belongs on a `NO_TRADE` run: on whether the **published forecasts and settlements** are honestly grounded, since those are the only things this run actually asserts.

## Top Three Concerns (severity order)

### 1. The score's rank ordering is anti-predictive, and the sleeve is published anyway

`02 § 0` reports rank IC **−0.5912 (p=0.026, n=14)** on the most recent settled vintage and **−0.1282** pooled across 14 vintages (n=203). The 24 names published today are ordered by the same mechanism. Top-7-by-score delivered −2.56% mean alpha last cycle while bottom-7 delivered +3.35%.

**Committee position: publishing is still correct, but the framing must be exact.** These are `LOW`-confidence monitoring forecasts, not recommendations, and `rules.md § Settlement Rules` is explicit that paper forecasts are how the system earns the evidence to ever publish `GO`. Suppressing them would destroy the only data that can diagnose the inversion. **Required and satisfied:** `05` and `06` both state the inversion in-line rather than burying it, and no name carries above `LOW` confidence. **No fix outstanding.**

The committee notes with approval that the run did **not** attempt a Track A correction — `eff_n = 1` gates it, and a monotonic mu/sigma transform cannot repair a rank inversion in any case.

### 2. `Tech_Z` supplies a mean 69.7% of conviction — evidence threshold #3 breached on 22 of 24 published names

With `Fund_Z` and `Sent_Z` unavailable, the composite is effectively a one-and-a-half-factor model, and `Tech_Z` and `Macro_Z` are positively correlated across this leaderboard (in a rotation, the strongest relative performers *are* the lowest-beta names).

**Committee position:** `05` states this explicitly with the computed range (46.9%–96.8%) and counts the breaches rather than asserting a marginal pass. That is the correct treatment. It is a third independent reason no name here is investable. **No fix outstanding.**

### 3. Post-catalyst extension is doing much of the work in `Tech_Z`

Thirteen of 24 published names printed earnings within the last 12 sessions — several on gaps of 4–10% (LMT +10.54%, WAB +10.04%, TMO +8.71%, RTX +7.33%). Their momentum and RS z-scores are substantially earned by a single already-realized move, which is a genuine decay risk over a 2–6 week horizon.

**Committee position:** disclosed in both `05` and `06` as a signal-decay warning. The committee additionally notes the *mechanism* by which this became visible is itself a weakness — see `§ Additional Findings` #2. **No fix outstanding for this run.**

## Review Checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **Clean.** 40 ledger rows; 17 settlement/ETF prices verified across 3 independent sources at 0.0000% max difference. `cnbc_last_time = 2026-07-24` on every symbol rules out a stale or after-hours tape on a weekend run |
| 2 | Overfitting / unvalidated signal claims | **Clean.** No Track A change proposed; `eff_n = 1` gate respected and stated. The defensive Macro polarity is labelled `INFERRED` (L140) and explicitly scoped as regime-conditional, not a weight change |
| 3 | Excessive event concentration | **BREACH, correctly reported.** 5 penalized names against a limit of 2 — an independent `NO_TRADE` trigger, reported as such in `07` |
| 4 | Correlation / sector crowding | **BREACH, correctly reported.** Industrials 41.7% vs the 30% cap. Pairwise correlation 0.275 passes, and `07` correctly warns that low residual correlation does not mean the macro bet is diversified |
| 5 | Portfolio beta drift outside the band | **INFEASIBLE, correctly reported.** Max attainable −0.159 vs 0.90–1.10; Task-0 pre-check stopped before sizing, spending 0 of 1 revision passes |
| 6 | Thesis quality below stated confidence | **Clean.** All 24 at `LOW`. Thesis lines are one-line sector/factor descriptions labelled as monitoring-only, and each states the run is `NO_TRADE` |
| 7 | Report / shared-rules mismatch | **Clean.** Exactly one status published; artifact set complete per `runbook.md` |
| 8 | Price / derived-field citation violations | **Clean.** Every `entry_price` carries `price_date` 2026-07-24 and `price_tag` `HISTORICAL`. No `target_price` or CI bound is populated on an unverified price |
| 9 | Sigma violations | **Clean.** All 24 names + 3 ETFs carry `REALIZED_VOL_30D` from fetched bars. No blanket `sigma = UNAVAILABLE`; no round unsourced sigma. Every monitoring name is settleable |
| 10 | Score-attribution violations | **Clean.** Every ranked name discloses family z-scores, DQ, penalties, drivers and metric ledger rows. `Fund_Z`/`Sent_Z` render as `UNAVAILABLE` on every row — never as neutral or supportive |
| 11 | Source Ledger violations | **Clean.** 40 rows covering price, return, vol, beta, earnings, target, CI, drawdown, ratios, technical states and feasibility inputs |
| 12 | Live-sounding / stale-as-current claims | **Clean.** The package consistently says "the 2026-07-24 close" and never "current", "latest" or "closed at" without a ledger row. The Sunday fire time and the closed market are stated in `00`, `01` and `03` |
| 13 | Improper `GO`-blocking | **Clean.** `00 § GO-Gate Table` lists all 5 Required inputs as GROUNDED and puts the missing Enhancing block in a separate confidence/exposure section. The run is *not* `REVIEW_ONLY` on Enhancing-input grounds |
| 14 | Missing prediction records | **Clean.** All 24 ranked names present in `15_predictions.json` with `score_explainability`; the Core ETF block is complete with 3 `MARKET_FORECAST` records; 17 settlements written; `due_inventory: 0`, `conflicts: 0` |
| 15 | Technical indicator pack violations | **Clean.** All states cite `technical_indicators.json` (L135). TD-9 is setup-count only. TD-9 `9` and RSI ≥ 70 are treated as an exhaustion *conjunction* penalty, never as standalone signals. The 8 genuine gaps (4 monthly MACD, 1 monthly RSI, 3 monthly MA) are `UNAVAILABLE`, not hidden |

## Specific Lineage Reviews

**Price / target lineage.** Entry prices are the unadjusted 2026-07-24 close (L002); target and CI derive from `entry × (1 + mu)` and `entry × (1 + mu ± 1.04σ)`. Spot-checked TRV: entry 387.26, mu +6.00%, sigma 9.327% → target 410.50, CI 372.93–448.06. Arithmetic verified.

**Sigma lineage.** `REALIZED_VOL_30D` = `stdev(last 30 daily adjusted returns) × √21` (L013). Sigma Fallback Chain step 1 (`IV30`) skipped — no options feed wired, documented. Step 2 succeeded universe-wide, so `SECTOR_MEDIAN` was never reached. Committee accepts.

**Score attribution.** The trace `(0.30·Tech_Z + 0.15·Macro_Z) × 0.80 − Penalties` is shown with actual values per name, and the two unavailable families are displayed as `UNAVAILABLE` rather than silently dropped from the formula. Committee accepts.

**Kelly threshold handling.** `0.25 × Kelly` is cap-binding at 5% NAV for all 24. No name has `0.25 × Kelly ≤ 0` and none falls below the 2% threshold. `05` correctly states the Kelly gate is *not* what blocks this book. Committee accepts, with the note that Kelly computed as `mu/σ²` on a monthly sigma produces large nominal values and should not be read as sizing conviction.

**Settlement lineage.** All 17 settled under `WEEKEND_TARGET` at the 2026-07-24 close because `target_date 2026-07-26` is a Sunday. The committee specifically checked that none was settled on an intraday print and that none was held open past its target date — both correct. Row schema uses the canonical `settle_price` / `settle_price_date` / `z` field names, so the manifest's `mean_z` picks them up (the 2026-07-20 `magnitude_z` trap is avoided). `settlement_ledger.py` re-run confirms `due_inventory: 0`, `conflicts: 0`.

**GO-blocking discipline.** Correct in both directions: no Enhancing input is cited as a blocker, and no Required input is missing while `GO` is claimed — `GO` is not claimed at all.

## Additional Findings (not blockers)

1. **The corporate-action return-basis change is material and correctly evidenced.** The committee reviewed the vendor comparison in `01 § Corporate-Action Basis` and agrees the prior unadjusted basis was producing genuinely wrong numbers (HON at 4.6× its true sigma). The change is Track B — it corrects a data-preparation defect and touches no scoring formula, factor weight, forecast prior or protected limit. **Approved.** The committee asks that the 07-24 package's HON figures be treated as known-bad rather than silently superseded; `13` does this.

2. **The vendor-empty earnings signature rule is too loose, and it fired loosely today.** The rule (accepted 2026-07-24) triggers on a 1-day move ≥3.5% **OR** volume ≥1.8× trailing median. This run, **EQR** (1.97× volume, **0.01%** price move) and **PKG** (2.13× volume, **0.01%** move) were classified as having printed earnings on a volume signal alone with an essentially flat tape — which is far more consistent with index rebalancing or an expiry than with a print. Both were consequently treated as *unpenalized*, the less conservative branch. **WRB** (2.00×, 2.45%) and **CB** (1.96×, 2.46%) are weaker versions of the same pattern.

   This is a real, disclosed weakness in Required input #4 for 4 of 24 published names. It is not this run's Track B change (one per run), and the committee agrees the adjusted-close fix is the higher-value correction. **Logged as an observation in `13` for a future run**, and disclosed in `01 § Known Limitations` #4. The committee's suggested direction, for the record: require the price-move condition, or require volume *and* a non-trivial move, rather than an unconditional `OR`.

3. **`eff_n` remains 1 after adding 17 settlements.** Working as designed. The committee notes the practical consequence: no Track A calibration change is possible before roughly 2026-08-21, and the rank-order inversion therefore cannot be acted on for several weeks. That is the correct trade-off — it is precisely the overfitting the gate exists to prevent — but it should be visible to a human reader, and `00 § Outstanding Blockers` makes it so.

4. **Eleven consecutive `NO_TRADE` runs.** Not a stop-criterion breach, and the run is behaving correctly each time. But the committee records that the *same* root cause (`Fund_Z`/`Sent_Z` unavailable) has produced the same outcome eleven times, and that this is an unblocking problem — Phase 2 of the SHADOW plan — not a research problem. `13` escalates it.

## Fabrication / Integrity Check

No fabricated, inconsistent or contradictory evidence found. Nothing propagated across artifacts that lacks a ledger row. **`HALTED` is not warranted.**

One process note in the run's favour: the carry-forward table in `02 § 5` was **caught and regenerated from `run_computed_manifest.json` after hand-written rank figures proved wrong on verification.** That is the 2026-07-15 lesson ("render every numeric table programmatically") being applied. The committee verified the 6 excluded-name rows and 8 rejection-log rows in `05` against the manifest independently — all match.

## Final Publication Recommendation

**`NO_TRADE`** — approved for publication as-is. Zero revision passes used (budget 1). No `HALTED` condition.
