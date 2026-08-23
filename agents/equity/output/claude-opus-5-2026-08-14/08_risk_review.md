# 08 — Risk Review · 2026-08-14

## Committee decision: `NO_TRADE`

Nothing was proposed for approval, so this review is an audit of the evidence chain and of the
`NO_TRADE` determination itself.

## Review checklist

| # | Check | Finding | Verdict |
|---|---|---|---|
| 1 | Fabricated or weakly supported inputs | 137/137 price-date checks grounded across 3 independent vendors at 0.000000% max deviation; every score input has a Source Ledger row | **Pass** |
| 2 | Overfitting or unvalidated signal claims | no parameter was fitted this run; the one engine change (`SATS` screener alias) was a correctness fix caught by the reproduction test, not a tuning choice | **Pass** |
| 3 | Excessive event concentration | 0 of 24 published names have earnings inside 14 days; `NO_TRADE` trigger 4 needs > 2 | **Pass** |
| 4 | Correlation or sector crowding | avg pairwise correlation 0.1386 passes, but the naive top-20 is 40.0% Finance — **would breach** the 30% cap, and all names load on one factor family | **Flagged** |
| 5 | Portfolio beta drift outside the band | naive sleeve beta +0.4785 vs the 0.90–1.10 band — **would fail**; the pool is nonetheless feasible ([-0.2791, +1.5397]) | **Flagged** |
| 6 | Thesis quality below stated confidence | all confidence capped `MEDIUM` by the rank-IC binding (-0.0630 over 950); 0 capped `LOW` on earnings proximity | **Pass** |
| 7 | Mismatch between report and shared rules | status, thresholds, mu bands, sigma chain and settlement conventions all trace to `rules.md`; no local reinterpretation | **Pass** |
| 8 | Price/derived-field citation violations | every numeric `entry_price` carries `price_date` 2026-08-14 and `price_tag` `HISTORICAL`; no `target_price`/CI is populated against an unverified entry | **Pass** |
| 9 | Sigma violations | all 24 published names and all 3 core ETFs carry `sigma` with source `REALIZED_VOL_30D`; no blanket `UNAVAILABLE` | **Pass** |
| 10 | Score-attribution violations | all 24 published names have a score trace, family z-scores, DQ, penalties and >=3 positive/negative drivers; `Fund_Z`/`Sent_Z` shown as `UNAVAILABLE`, never as neutral | **Pass** |
| 11 | Source Ledger violations | 122 rows; every price, return, vol, beta, earnings date, target, CI, drawdown, ratio, indicator state and sizing input is ledgered or explicitly `UNAVAILABLE` | **Pass** |
| 12 | Live-sounding or stale-as-current claims | no 'current'/'latest'/'closed at' language without a ledger row; the basis close is described as a dated historical close throughout | **Pass** |
| 13 | Improper `GO`-blocking | all 5 Required inputs grounded and none cited as a blocker; the 6 missing Enhancing inputs are listed as DQ/confidence caps only. `NO_TRADE` rests on evidence thresholds 2/3/4 | **Pass** |
| 14 | Missing prediction records | 24 `EQUITY_ALPHA` records (all with `score_explainability`) + 3 `MARKET_FORECAST` records (SPY/QQQ/SOXX, `benchmark: NONE`, `benchmark_price: null`, `adj_score: null`) + 149 settlements | **Pass** |
| 15 | Technical indicator pack violations | every indicator value cites `L013` (command + formula) and `L002` (price input); TD-9 9s and RSI extremes are treated as exhaustion flags reducing confidence, never as standalone signals; no failure hidden | **Pass** |

## Top three concerns, in severity order

### 1. The ranking model's out-of-sample record argues against its own leaderboard

Rolling rank IC is **-0.0630** over **950** settled `EQUITY_ALPHA` records, and the
MoM window in `02 § 2` is a fresh out-of-sample instance: the 2026-07-24 book returned
-3.87% of alpha with a 11.5% hit rate
while SPY ran +5.06%. Hit rate (40.53%)
is below the 50% healthy floor and mean z (-0.5220) is marginally outside the
-0.5/+0.5 band.

The committee's position: publishing this sleeve is correct — paper forecasts are how the
system earns the evidence to ever publish `GO`, and `rules.md § Settlement Rules` settles
`REVIEW_ONLY`/`NO_TRADE` predictions identically to `GO` ones — but the confidence cap must
bind everywhere, and it does. **No fix is available this run**: every candidate repair is Track
A and Track A is gated at `eff_n = 2 < 3`.

### 2. A `GO` portfolio would have failed two hard caps

The naive top-20 equal-weight sleeve fails the beta band (+0.4785 vs a 0.90
floor) and the sector cap (40.0% Finance vs 30%). This is
independent of the evidence thresholds: even with four families live, this cross-section would
have needed a revision pass. The pool itself is feasible
([-0.2791, +1.5397]), so the problem is the
*selection*, not the opportunity set — a technical-momentum screen in this tape picks
defensives (10 of
24 published names have beta < 0.50).

### 3. Two of four factor families have been unavailable for over a month

`Fund_Z` and `Sent_Z` have been `UNAVAILABLE` universe-wide since before July, making evidence
thresholds 2, 3 and 4 unsatisfiable and guaranteeing `NO_TRADE` regardless of market
conditions. The committee notes this is a **build** blocker, not a research one: Phase 2 of the
plan (bulk `companyfacts.zip` + threaded Nasdaq fetch across all 511 names) has not been
attempted by any run. Until it is, every package will reach this same verdict.

## Specific lineage reviews

| Item | Review |
|---|---|
| **Price / target lineage** | Entry prices are raw basis closes (`L003`) verified against two further independent vendors (`L004`, `L005`) at 0.000000% max deviation. Targets are `entry x (1 + mu)` with `mu` from the calibration band; CI bounds are `entry x (1 + mu ± 1.04 sigma)`. Spot-checked by re-derivation in the verification pass. |
| **Sigma lineage** | `REALIZED_VOL_30D` for every name: population stdev of the trailing 30 daily **adjusted** returns x `sqrt(21)`. No round-number sigma appears without a source. |
| **Score attribution** | Every published `Adj Score` re-derives from its stored `score_explainability` family z-scores within 2e-06. `Fund_Z`/`Sent_Z` are stored `null` and coerced to 0.00 per `rules.md § Family Aggregation`. |
| **Metric ledger coverage** | 122 ledger rows; 4 per published name (price, indicators, derived risk, macro slots) plus 25 infrastructure rows. |
| **Kelly threshold handling** | `0.25 x Kelly` is reported for all 24 names and is positive throughout, so the "<= 0 blocks investable" gate does not bind. It is moot this run — no name is investable on evidence grounds first. |
| **Technical indicator lineage** | All states from `technical_indicators.py` (`L013`) on the adjusted-close tree (`L002`). The helper prefers the `Close` column, so the adjusted tree writes adjusted values into `Close` — the documented way to honour the 2026-07-26 adjusted-basis rule. |
| **Source Ledger completeness** | No downstream artifact introduces a fact absent from `01`. Checked mechanically in the verification pass. |
| **`GO`-blocking discipline** | Verified: no Enhancing input is cited as a blocker anywhere. |
| **Prediction-record completeness** | 24/24 ranked names present in `15`; 3/3 core ETFs present; 149 settlements written; due inventory 0, conflicts 0. |

## A note on the reproduction test

The committee treats `05`'s retrospective same-basis reproduction as **materially
strengthening** this package. It reproduced the 2026-08-07 scored universe, rejection log and
rank order exactly, reproduced entry prices, `dd60`, `sigma`, IR and Sortino exactly, and
`Macro_Z` to 1.9e-06 — and in doing so caught a live engine bug (`SATS` screener alias) before
it reached any published number. The one residual (`vol_conf`, 0.0287) is disclosed with the
variants tested rather than asserted as passed.

## Final publication recommendation

**`NO_TRADE`.** Data integrity is sound and all Required inputs are grounded, so `HALTED` is
not warranted and `REVIEW_ONLY` would misdescribe the cause — the data is neither stale nor
weak, it is a same-session final close verified three ways. The blocker is candidate quality
under `rules.md § Evidence Thresholds`, which is exactly what `NO_TRADE` means.
