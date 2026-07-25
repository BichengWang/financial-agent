# 08 Risk Review — 2026-07-24

Adversarial review of the package before publication.

## Decision: `APPROVE` for publication as `NO_TRADE`

No portfolio is proposed, so there is no sizing to challenge. The review therefore targets what could still be wrong: grounding, lineage, calibration discipline, and whether `NO_TRADE` is genuine rather than a hedge.

## Top Three Concerns (severity order)

### 1. `Tech_Z` is flattered by post-earnings gaps — the leaderboard may be one week stale

9 of the top 15 names printed earnings within the last 7 sessions, several with very large single-day moves: LMT +10.54%, TRV +9.22%, TMO +8.71%, PKG +8.76%, DGX +8.61%, RTX +7.33%, CSX +5.77%, NSC +5.32%, UNP +4.02%. Momentum, relative strength and MA-alignment inputs all mechanically reward a gap that has already happened, and `rules.md § Research Horizon Alignment` warns against letting short-lived signals dominate a 2–6 week horizon.

**Assessment:** real, disclosed, and correctly handled. `05 § What Drives the Leaderboard` and `06 § Named Risks` both flag it explicitly as signal decay. No name is being *recommended*, only forecast, and each carries a settleable `mu`/`sigma` so the decay hypothesis will be scored at the 2026-08-21 target. **No revision required** — but this is the concern most likely to show up as negative alpha at settlement, and the evolution agent should watch it.

### 2. `Tech_Z` and `Macro_Z` are not independent this run — conviction may be single-factor

In a rotation, the names with the strongest relative strength are largely the same names with the lowest beta. The two available families therefore co-move, and evidence threshold #3 ("no single factor family contributes more than 50% of total conviction") passes arithmetically (0.30 vs 0.15 weights) while being questionable in substance.

**Assessment:** the concern is legitimate and `05` states it plainly rather than hiding it. It is **moot for publication** because no name is investable, but it would be a blocking concern in any `GO` run built on this leaderboard. Recorded for the evolution agent. **No revision required.**

### 3. Six earnings dates rest on an inference, not a vendor date

CB, HIG, WRB, EQR, AMP and JNJ returned vendor-empty with no clean print signature and were assigned `ESTIMATED_PRINT_WEEK (±5d)`. BAC's `ESTIMATED_CADENCE` tag rests on a volume ratio of 1.47 — below the 1.8 threshold used elsewhere — supported by the shared bank-earnings date with JPM.

**Assessment:** the inferences are **conservative in the right direction** — the six print-week names are *penalised*, not assumed safe, which costs them rank rather than flattering them. BAC's is the one inference that removes a penalty; it is labelled `INFERRED` rather than `OBSERVED` and the weak volume evidence is disclosed in `01`. Of the six, only HIG reaches the published set, where it is penalised anyway. **No revision required**, but this is the weakest link in the Required-input chain and should not be relied on more heavily in a future `GO` run.

## Review Checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **Clean.** Every published price verified by 3 independent sources at 0.000% difference. No price, vol, beta, target, CI or indicator value lacks a ledger row. Yahoo's 429 blockade is disclosed rather than papered over. |
| 2 | Overfitting or unvalidated signal claims | **Clean, and actively enforced.** Two candidate Track A calibration changes were tested and **rejected** for failing the acceptance standard (`13`). The run does not claim its defensive tilt is validated — it labels the Macro polarity `INFERRED` and regime-conditional. |
| 3 | Excessive event concentration | **Confirmed and disclosed.** 7 of 26 published names report inside 14 days; `NO_TRADE` condition #4 is met and recorded in `07`. |
| 4 | Correlation / sector crowding | **Confirmed.** Average pairwise correlation 0.261 passes, but Industrials is 60% of the top 10 and the whole sleeve is one defensive factor. Reported in `07`, not minimised. |
| 5 | Portfolio beta drift outside the band | **Confirmed infeasible** — max attainable beta ≈ +0.114 against a 0.90 floor. This is the strongest single finding in the package and is computed, not asserted. |
| 6 | Thesis quality below stated confidence | **Clean.** All 26 names are `LOW` confidence; no thesis claims more than the evidence supports. |
| 7 | Report/rules mismatch | **Clean.** Status is exactly one of the four allowed values; family weights unchanged; no protected rule touched. |
| 8 | Price/derived-field citation violations | **Clean.** Every numeric `entry_price` carries `price_date` 2026-07-24 and `price_tag` `DELAYED`. No target price or CI bound is populated on an unverified entry. |
| 9 | Sigma violations | **Clean.** All 26 names and all 3 ETFs carry `REALIZED_VOL_30D` from fetched bars with the source stated. No blanket `sigma = UNAVAILABLE`, no round unsourced sigma. The Sigma Fallback Chain terminated at step 2 universe-wide; step 1 (`IV30`) is documented unavailable. |
| 10 | Score-attribution violations | **Clean.** Every ranked name shows family z-scores, DQ, penalties, the full trace, and positive/negative drivers. Both `UNAVAILABLE` families are shown as `UNAVAILABLE` — never as 0-and-neutral or as supportive. |
| 11 | Source Ledger violations | **Clean.** 148 ledger rows covering prices, sigma, beta, downside sigma, drawdown, indicator lineage, rates, breadth, settlement state and the two unavailable families. |
| 12 | Live-sounding or stale-as-current claims | **Clean.** The run genuinely holds the 2026-07-24 official close for every name, fetched this run and triple-verified, so "close"/"today" language is ledger-backed. No claim is dressed up beyond `DELAYED`. |
| 13 | Improper GO-blocking | **Clean — and specifically checked.** `NO_TRADE` rests on evidence thresholds #2/#4 and on portfolio infeasibility, never on missing Enhancing inputs. The GO-Gate Table shows all 5 Required inputs grounded, and the manifest states the run was `GO`-eligible on data grounds. The inverse violation (a `GO` with a missing Required input) does not arise. |
| 14 | Missing prediction records | **Clean.** 26 `EQUITY_ALPHA` records (every ranked/monitored name) each with `score_explainability`, plus 3 `MARKET_FORECAST` records for SPY/QQQ/SOXX. `settlements: []` carries an explanatory note and is verified by `settlement_ledger.py --as-of 2026-07-24` (`due_inventory 0`). |
| 15 | Technical indicator pack violations | **Clean.** All TD-9/RSI/MACD/MA/momentum/volume/RS values trace to `technical_indicators.json` (L135). `FDXF` is marked `UNAVAILABLE` rather than hidden. TD-9 and RSI are treated as exhaustion flags feeding penalties and confidence, never as standalone signals. |

## Specific Challenges Raised and Resolved

**"Is `due_inventory: 0` a missed scan?"** No. Independently confirmed: the last matured target date across all packages is 2026-07-22 (settled by the 07-22 runs), no prediction anywhere carries a 2026-07-23 or 2026-07-24 target, and the next 17 keys are dated 2026-07-26 — beyond today's run date, so correctly left `OPEN`. The `--as-of` flag was passed explicitly, avoiding the 2026-07-20 default-`as_of` trap.

**"Is the SPY forecast of exactly 0.00% an evasion of scoring?"** Partly, and it is disclosed as such. `|mu| < 0.5%` means SPY settles as `N/A - FLAT_CALL` with no direction score. The mitigating facts: the 0.00% follows a stated ±1.0pp adjustment from the `NEUTRAL` prior with four cited technical reasons; QQQ and SOXX both carry scoreable directional calls; and `03` states the consequence rather than letting it pass silently. **Accepted, with the observation that a rule permitting a forecast to opt out of direction scoring is itself worth evolution attention.**

**"Does the degenerate beta multiplier invalidate the ETF block?"** No, but it is the block's weakest point and `03` says so outright: with SPY mu at exactly 0.00%, `beta × SPY_mu` is 0.00% for both QQQ and SOXX, so their forecasts come entirely from the adjustment band. The values remain inside the permitted bands with ledger-backed reasons, so the block is publishable — and the underlying structural flaw is escalated to `13`.

**"Is `NO_TRADE` being used to avoid a hard call?"** No. The run publishes 26 forecasts with full `mu`/`sigma`/CI that will be scored on 2026-08-21, plus three ETF forecasts. It takes real, falsifiable positions; it declines only to size them. That is the distinction `rules.md` draws between run status and evaluation.

## Prediction-Record Completeness Verification

| Requirement | Status |
|---|---|
| One record per ranked/monitored name | 26 / 26 |
| `score_explainability` on every new `EQUITY_ALPHA` record | 26 / 26 |
| `benchmark_price` (SPY at same `price_date`) on every equity record | 26 / 26 at 738.93 |
| Core ETF `MARKET_FORECAST` records | 3 / 3 (SPY, QQQ, SOXX) with `benchmark: NONE`, `benchmark_price: null`, `adj_score: null` |
| `settlements` block present | Yes — `[]` with note |
| Valid JSON, no markdown wrapper | Yes |

## Final Publication Recommendation

**`NO_TRADE`.** The package is internally consistent, fully grounded, and honest about the two structural reasons it cannot publish a portfolio. No revision pass required; the revision budget is unspent.
