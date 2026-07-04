# 08 Risk Review

Risk committee review of `00`–`07` per `agents.md § Risk Committee Agent Prompt`. Decision recorded below; this is a first-pass review (no revision cycle was needed — see Decision).

## Review Checklist

1. **Fabricated or weakly supported inputs**: None found. Every numeric price, indicator, and derived ratio traces to a Source Ledger row (`01_preflight.md`, `L001`–`L146`) with a real IBKR retrieval timestamp. The one place a fallback failed (Yahoo, 515-name universe) is disclosed as a failure, not silently patched — see `03_regime_and_data.md` and `04_universe_summary.md`.
2. **Overfitting or unvalidated signal claims**: None found. `Adj Score` explicitly shows `Fund_Z`/`Sent_Z` as `0.00 (UNAVAILABLE)`, not backfilled with a plausible-looking number. No claim of investability is made anywhere in `06`/`07`.
3. **Excessive event concentration**: Earnings-date data is entirely absent (`Days to Earnings` = `UNAVAILABLE` for all 30 names) — flagged in `03_regime_and_data.md` and `05_factor_scores.md` as an independent block on confidence and GO-eligibility, not glossed over.
4. **Correlation or sector crowding**: Moot — no portfolio was constructed (`07_portfolio_proposal.md`). Noted for the record: 3 of the top-5 monitoring names (`MU`, `AMD`, plus `AVGO` at rank 28) share a single AI/semiconductor theme with extreme beta (3.9–4.2) — this would have been a binding sector/theme-crowding constraint had a portfolio been drafted.
5. **Portfolio beta drift outside the band**: Moot — no portfolio.
6. **Thesis quality below stated confidence**: All 12 monitoring names are capped `LOW`, matching the actual evidence quality (2 of 4 families, no earnings confirmation). No name overstates its confidence.
7. **Mismatch between report and shared rules**: One judgment call flagged for transparency, not corrected as an error: the Data Quality Multiplier is set to `0.70` (the floor for "materially incomplete evidence") rather than treating 2-of-4-families-missing as disqualifying the multiplier below the floor entirely. `rules.md` states "if the multiplier would fall below 0.70, do not rank the candidate as investable" — it does not say a 2-family gap must fall below 0.70. Given that 2 of 4 families (50% of the architecture) are entirely absent, `0.70` is the most conservative defensible value at the floor, not an inflated one; the committee accepts this as consistent with the letter of the rule, while noting the spirit of the rule is already honored by the harder, independent 3-of-4-families Evidence Threshold gate, which blocks GO regardless of the DQ value chosen.
8. **Price/derived-field citation violations**: None found. Every `entry_price` in the monitoring sleeve has `price_date` + `price_tag` (`01_preflight.md`); no `target_price`/CI populated where `entry_price` is unverified (all 30 names have grounded IBKR prices).
9. **Sigma violations**: None found. All 12 monitoring names carry `sigma_source = REALIZED_VOL_30D`, computed from the same fetched 60-trading-day+ history used for beta/drawdown, not a round/assumed number.
10. **Score-attribution violations**: None found. Every ranked name (all 30) has a score trace with family z-scores (including explicit `UNAVAILABLE` markers), DQ, penalties, and — for the top 12 — top drivers and metric ledger rows.
11. **Source Ledger violations**: None found (146 rows, cross-checked programmatically for claim-type/freshness-tag counts — see `01_preflight.md`).
12. **Live-sounding or stale-as-current claims**: One caveat surfaced and disclosed, not hidden: `PG` and `MCK` entry-price snapshots are tagged `DELAYED` (stale/closed ticks, one from 07:26Z pre-market and one from a closed-quote response) rather than `LIVE`, and this is called out explicitly in `06_top_candidates.md`'s Key Risk column for both names.
13. **Improper GO-blocking**: This is the central finding, and the committee affirms it is *proper*, not improper, GO-blocking. Fundamental and Sentiment are **not** Enhancing inputs under `rules.md § Input Classification` — they are entire factor families whose absence trips the independent Evidence Threshold ("3 of 4 factor families non-negative"), a rule distinct from the five-item Required-inputs list. Blocking on this threshold is correct; it would be improper GO-blocking only if the run were citing a missing *Enhancing* input (e.g., options IV/skew, short interest) as the reason — it is not. Separately, the earnings-date gap **is** listed as a Required input in `rules.md § Input Classification` #4 ("Next earnings date — confirmed, or cadence-estimated"), and it is entirely `UNAVAILABLE` with no cadence estimate attempted (no prior-quarter reference date was available without a fundamentals/filings feed). This is a second, independent, and *proper* GO block.
14. **Missing prediction records**: Checked against `15_predictions.json` (see that file) — all 12 monitoring names plus the 3 core-ETF `MARKET_FORECAST` records are present, each `EQUITY_ALPHA` record carries `score_explainability`. No gaps.
15. **Technical indicator pack violations**: None found. Every TD-9/RSI/MACD/MA/momentum/volume/RS value cited in `03`/`05`/`06` traces to `technical_indicators.json` (generated 2026-07-02T12:09Z, 33/33 `OK`) and a Source Ledger row. TD-9 and RSI extremes are treated as exhaustion/risk flags in the driver commentary (e.g. `MU`, `CAT`, `UNH` weekly/monthly TD-9 `SELL_SETUP_9` calls), never as standalone buy/sell triggers.

## GO-Blocking Discipline (explicit reconciliation)

Two independent, Required-input-level blocks on `GO` this run:

1. **Factor-family Evidence Threshold** (`rules.md § Evidence Thresholds` #2): max 2 of 4 families sourceable → 0 investable names.
2. **Earnings-date Required input** (`rules.md § Input Classification` #4): `UNAVAILABLE` for all 30 names, no cadence estimate possible.

Both are genuine, disclosed, Required-input-level gaps — not Enhancing inputs being misapplied as blockers. Per `rules.md`: *"A run with all Required inputs grounded and several Enhancing inputs missing is a valid GO candidate at reduced confidence... not an automatic REVIEW_ONLY."* That escape hatch does **not** apply here, because Required inputs (earnings date) and a separate Evidence Threshold (factor-family count) are the actual failure points, not merely Enhancing gaps.

## Prediction-Record Completeness

Verified against `15_predictions.json`: 12 `EQUITY_ALPHA` records (monitoring sleeve) + 3 `MARKET_FORECAST` records (SPY, QQQ, SOXX) = 15 total records, `settlements: []` with the `NO_PREDICTION_LEDGER`-equivalent note explained in `02_reflection.md § 0` (0 predictions due for settlement, earliest open target_date across all prior ledgers is 2026-07-08). Complete.

## Decision

**`APPROVE`** — the package is publishable as-is. No revision is requested because the analysis is internally consistent, every gap is disclosed rather than papered over, and the recommended final status (`NO_TRADE`) is the correct, rules-compliant conclusion given the evidence — not a defect to fix.

## Top Three Concerns (severity order)

1. **Structural data-source gap (highest severity, environmental not process)**: this environment has no fundamentals, positioning, or earnings-calendar feed connected, and general web fetch failed for Yahoo with a policy-level block. Every future run in this environment will hit the same 2-of-4-families ceiling unless a fundamentals/positioning/earnings-calendar MCP tool or an approved web-fetch path is added. This is an infrastructure finding, logged for the evolution agent (`13_evolution_log.md`), not a fixable-this-run process error.
2. **Universe-breadth gap**: only 30 of 515 index-union names were actually scored this run (Sampled Universe Protocol fallback), due to the same Yahoo block plus IBKR per-name fetch budget constraints. A materially larger true-signal name could exist outside the sampled 30 and never surface. Disclosed in `03`/`04`; not correctable within this session's tool budget.
3. **Concentration risk in the monitoring sleeve, not actionable this run**: 3 of the top-5 monitored names share a single AI/semiconductor theme with extreme beta — a real crowding signal for whichever future run first clears the Evidence Threshold and attempts to size a live portfolio from a similar candidate mix. Flagged for `07_portfolio_proposal.md`'s "why excluded" section and for future portfolio-construction discipline.

## Required Fixes

None — see Decision above.

## Final Publication Recommendation

**`NO_TRADE`**
