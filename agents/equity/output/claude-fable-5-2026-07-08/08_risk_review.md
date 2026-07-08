# 08 Risk Review — Committee Decision

## Decision: **APPROVE** — publish as **NO_TRADE**

The run publishes forecasts, not positions; the review below covers the forecast package and the first settlement pass.

## Checklist Findings

1. **Price/target lineage** — PASS. Every entry price LIVE 2026-07-08 with two-source verification (max div 0.28%, all <1%; L001–L005 fetch/cross-check rows); every target = close×(1+mu) with mu from the Calibration Table band; CI bounds from the ±1.04σ formula. No numeric price without tag+date found in 02/03/05/06/09.
2. **Sigma lineage** — PASS. All 23 equity sigmas + 3 ETF sigmas are REALIZED_VOL_30D (stdev of fetched 30d daily returns × √21, DERIVED rows). No round-number sigma without source; no blanket UNAVAILABLE.
3. **Score attribution** — PASS. Every Adj Score carries the full trace with family z-scores, DQ 0.80, penalties, drivers, and ledger rows; missing families displayed as 0.00 (UNAVAILABLE), never neutral/supportive.
4. **Metric ledger coverage** — PASS. 197 ledger rows cover every printed value; universe-scale inputs carried in the fetch manifest + technical_indicators.json support artifacts as documented in the 01 footer.
5. **Kelly thresholds** — PASS. 0.25×Kelly cap-binding at 5% NAV for all names (disclosed TE-denominated fallback); no ≤0 Kelly in the published sleeve.
6. **Technical indicator lineage** — PASS. All TD-9/RSI/MACD/MA/momentum/VR/RS values cite technical_indicators.json (2026-07-08T17:48:58Z, CSV-sourced from the exact fetched bars) + price-history rows; exhaustion flags used as penalties/confidence caps, never standalone signals.
7. **GO-blocking discipline** — PASS. GO-Gate Table shows all 5 Required inputs grounded; NO_TRADE rests on evidence threshold #2 (family coverage), not on missing Enhancing inputs. No Enhancing input cited as a blocker anywhere in the package.
8. **Prediction-record completeness** — PASS. 15_predictions.json: 23 EQUITY_ALPHA records (each with score_explainability, benchmark_price 744.34) + 3 MARKET_FORECAST records (mu_derivation blocks) + **12 settlement records** — the publishing gate is satisfied; every ranked name is settleable.
9. **Settlement integrity (first pass)** — PASS. All 12 due records settled per §Settlement Rules (alpha direction vs recorded SPY 728.31; CI on price bounds; z on mu/sigma); arithmetic spot-checked (ABBV: 253.71/225.82−1 = +12.35%, alpha +10.15% vs +2.20% SPY ✓). Calibration metrics reported with the n=12 caveat and no premature parameter action — correct restraint given the 20-record Track A floor.
10. **Live-sounding language** — PASS with note: 02/05/06 use "settled/realized" only for ledger-backed settlement rows; intraday partial-bar caveat disclosed in 01 and 05.

## Top Three Concerns (severity order)

1. **Rank IC -0.51 on the first vintage** — the composite score ordered realized alpha *inversely* within the June-10 vintage (high-scored retail/energy missed; low-scored healthcare monitors hit). n=12 is below every action threshold, but if this sign persists through the 07-09 and 07-12 settlements (n≈49 cumulative), the evolution agent must prioritize a calibration change over the standing family-coverage proposal per the §Priority Override.
2. **Earnings-estimate load-bearing** — 34 of 80 shortlist penalties rest on cadence-estimated dates (INFERRED ±5d). DAL prints tomorrow; STT/UNH next week. A missed estimate mis-prices the penalty, not the ledger — acceptable, but the ±5d band must stay disclosed everywhere (it is).
3. **Exhaustion breadth** — 15 of 23 names carry exhaustion/high-vol/earnings flags; the sleeve is a stretched-momentum board in a NEUTRAL tape. The -1pp mu shades and penalties price this mechanically; no discretionary override applied (correct), but CI coverage on this cohort will be the real test at the 2026-08-05 settlements.

## Required Fixes

None blocking publication. Standing item (7th→8th escalation): the family-coverage Track B proposal remains DEFER/HUMAN_REVIEW — see 13.

## Final Publication Recommendation

**NO_TRADE** — artifacts complete, grounding gates satisfied, first settlement pass clean.
