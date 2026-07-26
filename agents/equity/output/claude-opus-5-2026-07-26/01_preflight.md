# 01 Preflight — Source Ledger — 2026-07-26

Published **before** reflection, scoring, portfolio construction, and risk review use any fact downstream. Every price, return, volatility, beta, earnings date, target, CI bound, drawdown, ratio, technical indicator state, and sizing input used anywhere in this package appears here or is marked `UNAVAILABLE`.

## Run Context

- Run date **2026-07-26 (Sunday)**; U.S. equity markets closed. Last completed session: **Friday 2026-07-24**.
- Single price basis: the **2026-07-24 official close**.
- **Return basis (changed this run):** all return-derived metrics and the entire technical-indicator pack are computed from **adjusted closes** (splits, spin-offs, dividends). Entry/target/CI prices use the **unadjusted** 2026-07-24 close. Rationale and evidence in `13_evolution_log.md`; scope note in `§ Corporate-Action Basis` below.
- Yahoo Finance `v8/finance/chart` was **HTTP 429 on both `query1` and `query2`** at 2026-07-26T20:41Z — the 7th blocked session in the 13 sessions since 2026-07-13. Availability remains unstable; the Nasdaq/stockanalysis path is treated as primary.

## Endpoints Used

| Endpoint | Used for | Result |
|---|---|---|
| `stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y` | 5y daily bars, raw **and** adjusted close | 518/518 symbols, ~24s at 8 workers |
| `api.nasdaq.com/api/quote/{SYM}/historical` | independent close verification; bulk fallback | 3 names fell back here on the first pass; used for all 17 verification symbols |
| `quote.cnbc.com/.../restQuote/symbolType/symbol` | third independent close + `last_time` stamp | 17/17 symbols |
| `api.nasdaq.com/api/analyst/{sym}/earnings-date` | next earnings date | 56 fetched, 34 `CONFIRMED`, 22 vendor-empty |
| `api.nasdaq.com/api/quote/{sym}/summary` | GICS sector / industry | 24/24 published names returned a sector |
| `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` | VIX level and 30d averages | OK, 9,236 rows |
| `home.treasury.gov/.../daily_treasury_bill_rates` | risk-free rate | OK (FRED `fredgraph.csv?id=DTB3` timed out — connection closed without response) |
| `query1/query2.finance.yahoo.com/v8/finance/chart` | primary bar source (attempted) | **HTTP 429, both hosts** |

## Price Verification (Price Sourcing Standard)

Full detail in `price_verification.json`. All 17 symbols that carry a settlement or a core-ETF forecast were confirmed by **three independent sources**:

| Symbol | stockanalysis | Nasdaq historical | CNBC `last` | CNBC `last_time` | Max pairwise diff |
|---|---|---|---|---|---|
| AAPL | 333.02 | 333.02 | 333.02 | 2026-07-24 | 0.0000% |
| BAC | 62.05 | 62.05 | 62.05 | 2026-07-24 | 0.0000% |
| CAT | 888.73 | 888.73 | 888.73 | 2026-07-24 | 0.0000% |
| CVX | 194.79 | 194.79 | 194.79 | 2026-07-24 | 0.0000% |
| EQIX | 1084.24 | 1084.24 | 1084.24 | 2026-07-24 | 0.0000% |
| FCX | 62.60 | 62.60 | 62.60 | 2026-07-24 | 0.0000% |
| GE | 353.73 | 353.73 | 353.73 | 2026-07-24 | 0.0000% |
| GOOGL | 319.74 | 319.74 | 319.74 | 2026-07-24 | 0.0000% |
| GS | 1061.23 | 1061.23 | 1061.23 | 2026-07-24 | 0.0000% |
| JPM | 353.21 | 353.21 | 353.21 | 2026-07-24 | 0.0000% |
| LLY | 1196.03 | 1196.03 | 1196.03 | 2026-07-24 | 0.0000% |
| SHW | 317.51 | 317.51 | 317.51 | 2026-07-24 | 0.0000% |
| UNH | 420.74 | 420.74 | 420.74 | 2026-07-24 | 0.0000% |
| V | 355.74 | 355.74 | 355.74 | 2026-07-24 | 0.0000% |
| SPY | 738.93 | 738.93 | 738.93 | 2026-07-24 | 0.0000% |
| QQQ | 684.23 | 684.23 | 684.23 | 2026-07-24 | 0.0000% |
| SOXX | 527.01 | 527.01 | 527.01 | 2026-07-24 | 0.0000% |

This exceeds the two-source requirement. The `last_time` stamp matters on a weekend run: it rules out the CNBC field having drifted to an after-hours or Monday-premarket print.

The 24 published monitoring names carry the same 2026-07-24 close from the bulk fetch (`stockanalysis.com`, raw `c` field), cross-checked against the same vendor's adjusted series for internal consistency. They are `HISTORICAL`-tagged and are not executed against, so the three-source standard is applied to the settlement and forecast set rather than to all 514.

## Corporate-Action Basis

Diagnosed this run by comparing two vendors bar-for-bar around three known events:

| Name | Event window | stockanalysis raw `c` | Nasdaq | stockanalysis adjusted `a` |
|---|---|---|---|---|
| HON | 2026-06-26 → 06-29 | 243.53 → 227.80 (**adjusted**) | 464.42 → 227.80 (**unadjusted**) | 243.53 → 227.80 |
| FDX | 2026-05-29 → 06-01 | 411.75 → 338.49 (**unadjusted**) | 325.01 → 338.49 (**adjusted**) | 330.32 → 337.22 |
| SPGI | 2026-06-30 → 07-01 | 407.26 → 414.97 | 399.58 → 414.97 | 385.21 → 414.97 |

Neither vendor's raw close is internally consistent — each adjusts one event and not the other. Only the adjusted `a` series is consistent across all three. Using it removes a spurious −42.90% 60-day momentum and a 4.6×-inflated sigma on HON that the 2026-07-24 package carried on this same basis.

**Scope.** Against the prior package, **3 of 514 names** differ materially (HON, FDX, SPGI). Comparing raw vs adjusted basis directly within this run, the corporate-action correction is large but narrow while the dividend component is small but broad — 9 names move >5% relative sigma or >2pp 60d momentum, 207 move >2%/>0.5pp, with a median 60d-momentum shift of 0.375pp (p90 1.04pp). Median rank move across all 514 is 2 places; the top-30 retains 28 of 30 members. Full detail in `13_evolution_log.md`.

## Source Ledger

| Row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 01 | close (unadjusted) | 17 verified symbols | see `§ Price Verification` | USD | 2026-07-24 | stockanalysis + Nasdaq + CNBC (3-source, 0.0000%) | HISTORICAL | OBSERVED | 02, 03, 05, 15 |
| L002 | 01 | close (unadjusted) | 24 published names | see `05` Entry column | USD | 2026-07-24 | `stockanalysis.com` history `c` field | HISTORICAL | OBSERVED | 05, 06, 15 |
| L003 | 01 | daily bars (adjusted) | 514 union names + SPY/QQQ/SOXX/TLT | 185–1,255 bars each | USD | 2021-07-26 → 2026-07-24 | `stockanalysis.com` history `a` field | HISTORICAL | OBSERVED | 03, 05, technical_indicators.json |
| L004 | 01 | retrieval timestamp | bulk fetch | 2026-07-26T20:4xZ | ISO ts | 2026-07-26 | run log | — | OBSERVED | 01 |
| L005 | 01 | VIX close | ^VIX | 18.58 | index | 2026-07-24 | `cdn.cboe.com` VIX_History.csv | HISTORICAL | OBSERVED | 03 |
| L006 | 01 | VIX 30d avg / prior-30d avg | ^VIX | 17.12 / 17.60 | index | 2026-07-24 | derived from L005 series | HISTORICAL | DERIVED | 03 |
| L007 | 01 | risk-free (13wk bank discount) | US T-bill | 3.81 | % p.a. | 2026-07-24 | `home.treasury.gov` daily_treasury_bill_rates 2026 | HISTORICAL | OBSERVED | 05 ratios |
| L008 | 01 | rf monthly | US T-bill | 0.003175 | decimal | 2026-07-24 | `rf_annual / 12`, input L007 | HISTORICAL | DERIVED | 05 Sharpe/Sortino/Treynor/Calmar |
| L009 | 01 | index-union counts | universe | 503 S&P / 101 NDX / 89 overlap / 515 union | count | cache 2026-06-21T21:05:56Z | `build_index_universe.py`, `universe_summary.json` | HISTORICAL | OBSERVED | 00, 03, 04 |
| L010 | 01 | scored universe | universe | 514 | count | 2026-07-26 | L009 minus FDXF (listing age) | — | DERIVED | 04, 05 |
| L011 | 01 | exclusion | FDXF | 40 bars from 2026-05-28 | count | 2026-07-24 | L003 | HISTORICAL | OBSERVED | 04 |
| L012 | 01 | listing age admit | Q (Qnity Electronics) | first bar 2025-10-28, 185 bars ≈ 8.9 months | count | 2026-07-24 | L003 + `api.nasdaq.com/quote/Q/info` | HISTORICAL | OBSERVED | 04 |
| L013 | 01 | 30d realized vol | 514 names + 3 ETFs | see `05` / `03` | decimal (1m) | 2026-07-24 | `stdev(last 30 daily adj returns) × √21`, input L003 | HISTORICAL | DERIVED | 05, 15 sigma |
| L014 | 01 | prior-30d realized vol | 3 core ETFs | SPY 0.0375 / QQQ 0.0640 / SOXX 0.1692 | decimal (1m) | 2026-07-24 | same formula on bars −60..−30, input L003 | HISTORICAL | DERIVED | 03 vol-direction |
| L015 | 01 | downside sigma 30d | 514 names | see `05` Sortino | decimal (1m) | 2026-07-24 | `stdev(negative daily adj returns, last 30) × √21`, input L003 | HISTORICAL | DERIVED | 05 Sortino |
| L016 | 01 | 60d beta vs SPY | 514 names + QQQ/SOXX/TLT | see `05` / `03` | ratio | 2026-07-24 | OLS slope of 60 daily adj returns vs SPY, inputs L003 | HISTORICAL | DERIVED | 05, 07 feasibility, 03 ETF mu |
| L017 | 01 | tracking error 1m | 514 names | see `05` IR | decimal (1m) | 2026-07-24 | `stdev(r − β·r_SPY over 60d) × √21`, inputs L003, L016 | HISTORICAL | DERIVED | 05 IR |
| L018 | 01 | 60d max drawdown | 514 names + 3 ETFs | see `05` / `03` | decimal | 2026-07-24 | worst peak-to-trough over last 60 adj bars, input L003 | HISTORICAL | DERIVED | 05, 03 |
| L019 | 01 | ADV20 (dollar) | 514 names | all > $20M | USD | 2026-07-24 | `mean(close × volume, 20d)`, input L003 | HISTORICAL | DERIVED | 04 liquidity filter |
| L020 | 01 | universe median sigma30 | universe | 0.096089 | decimal (1m) | 2026-07-24 | median of L013 | — | DERIVED | 05 vol penalty threshold |
| L021 | 01 | GICS sector / industry | 24 published names | see `05` | label | 2026-07-26 | `api.nasdaq.com/api/quote/{sym}/summary` | DELAYED | OBSERVED | 05, 07 sector table |
| L022 | 01 | next earnings date (confirmed) | 34 names | see `05` Days→Earn | date | 2026-07-26 | `api.nasdaq.com/api/analyst/{sym}/earnings-date` | DELAYED | OBSERVED | 05 penalty, 08 |
| L023 | 01 | next earnings (vendor-empty, cadence) | 21 names | `ESTIMATED_CADENCE +91d (±5d)` | date | 2026-07-26 | vendor-empty + print-like signature in last 12 sessions (rule accepted 2026-07-24) | DELAYED | INFERRED | 05 penalty |
| L024 | 01 | next earnings (vendor-empty, print week) | HIG | `ESTIMATED_PRINT_WEEK (±5d)` | date | 2026-07-26 | vendor-empty + no print signature → conservative penalized branch | DELAYED | INFERRED | 05 penalty |
| L025 | 01 | 20d/60d momentum | 514 names + 3 ETFs | see `05` | % | 2026-07-24 | `technical_indicators.json`, inputs L003 | HISTORICAL | DERIVED | 05 Tech_Z |
| L026 | 01 | RS20/RS60 vs SPY | 514 names + QQQ/SOXX | see `05` / `03` | pp | 2026-07-24 | `technical_indicators.json`, inputs L003 | HISTORICAL | DERIVED | 05 Tech_Z, 03 |
| L027 | 01 | 20d volume ratio | 514 names | see `05` | ratio | 2026-07-24 | `technical_indicators.json`, inputs L003 | HISTORICAL | DERIVED | 05 Tech_Z |
| L028 | 01 | core ETF close | SPY / QQQ / SOXX | 738.93 / 684.23 / 527.01 | USD | 2026-07-24 | L001 | HISTORICAL | OBSERVED | 03, 09, 15 |
| L029 | 01 | TLT close + trend | TLT | 83.25; MA20 84.65, MA50 84.79, RSI 33.19 | USD / index | 2026-07-24 | L003 + `technical_indicators.json` | HISTORICAL | DERIVED | 03 regime evidence |
| L030 | 01 | sigma for forecasts | 24 names + 3 ETFs | `REALIZED_VOL_30D` | decimal (1m) | 2026-07-24 | L013; Sigma Fallback Chain step 2 | HISTORICAL | DERIVED | 05, 03, 15 |
| L135 | 01 | technical indicator pack | 518 records | TD-9, RSI(14), MACD(12,26,9), MA align, momentum, volume ratio, RS — daily/weekly/monthly | mixed | 2026-07-24 | `technical_indicators.py` → `technical_indicators.json`; formula lineage in that artifact's `definitions` block; price inputs L003 | HISTORICAL | DERIVED | 05, 06, 09, 15 |
| L136 | 01 | settlement prices | 17 settled keys | see `02 § 0` | USD | 2026-07-24 | L001 (3-source verified) | HISTORICAL | OBSERVED | 02, 15 settlements |
| L137 | 01 | settlement arithmetic | 17 settled keys | realized return, benchmark return, alpha, CI result, z | decimal | 2026-07-26 | `rules.md § Settlement Rules` steps 1–6, inputs L136 + vintage records | — | DERIVED | 02 § 0 |
| L138 | 01 | canonical ledger state | all models | `due_inventory: 0`, `conflicts: 0`, EQ n=203, MF n=36, `eff_n`=1/1 | count | 2026-07-26 | `settlement_ledger.py --as-of 2026-07-26` → `settlement_manifest.json` | — | DERIVED | 00, 02, 13 |
| L139 | 01 | regime classification | market | `NEUTRAL` | label | 2026-07-24 | judgment on L005, L025, L028, L029, L135 | HISTORICAL | INFERRED | 03, 05, 09 |
| L140 | 01 | defensive Macro polarity | universe | lower beta / lower vol / shallower DD score better | polarity | 2026-07-26 | regime-conditional reading of L139 evidence | — | INFERRED | 05 Macro_Z |
| L141 | 01 | portfolio feasibility | top-10 ranked | max attainable beta −0.159 vs 0.90–1.10 band | ratio | 2026-07-26 | `Σ 0.05 × β_i` over the 10 highest betas, input L016 | — | DERIVED | 07, 08 |
| L142 | 01 | universe beta distribution | universe | 212 of 514 negative (41.2%), median +0.228 | count / ratio | 2026-07-24 | L016 | — | DERIVED | 03, 07 |
| L143 | 01 | corporate-action basis check | HON, FDX, SPGI | see `§ Corporate-Action Basis` | USD | 2026-07-24 | bar-for-bar vendor comparison, L003 + Nasdaq historical | HISTORICAL | OBSERVED | 13 |
| L144 | 01 | Fundamental family | 514 names | **UNAVAILABLE** | — | 2026-07-26 | no fetch path wired; SHADOW tooling exists but is not promoted (`rules.md § SHADOW Diagnostic Tooling`) | UNAVAILABLE | UNAVAILABLE | 05 Fund_Z, 08 |
| L145 | 01 | Sentiment family | 514 names | **UNAVAILABLE** | — | 2026-07-26 | as L144 | UNAVAILABLE | UNAVAILABLE | 05 Sent_Z, 08 |
| L146 | 01 | Enhancing input block | universe | **UNAVAILABLE** — options IV/skew, short interest, bid-ask, revisions, institutional flow | — | 2026-07-26 | no feed wired | UNAVAILABLE | UNAVAILABLE | 05 DQ 0.80, 08 |
| L147 | 01 | Yahoo availability | vendor | HTTP 429 on query1 and query2 | status | 2026-07-26 | fetch attempt log | UNAVAILABLE | OBSERVED | 13 |

## Coverage Summary

| claim_type | Rows | Notes |
|---|---|---|
| `OBSERVED` | 12 | prices, VIX, rf, universe counts, sectors, confirmed earnings, vendor comparison, Yahoo status |
| `DERIVED` | 21 | every risk/return/technical metric and all settlement arithmetic; each cites formula + input rows |
| `INFERRED` | 4 | regime, Macro polarity, two vendor-empty earnings branches |
| `UNAVAILABLE` | 3 | `Fund_Z`, `Sent_Z`, Enhancing block |
| **Total** | **40** | |

**Status eligibility from grounding alone: `GO`-eligible.** Every Required input has a row. The `NO_TRADE` outcome is driven by evidence thresholds #2/#4 and the beta-feasibility pre-check, not by any ledger gap.

## Known Limitations Carried Into Scoring

1. `Fund_Z` and `Sent_Z` are `UNAVAILABLE` for all 514 names (L144, L145). They are displayed as `0.00 (UNAVAILABLE)` in the arithmetic and **do not** count toward the 3-of-4 family threshold.
2. Data-quality multiplier fixed at **0.80** for every name (L146) — below the 0.85 completeness bar, so no name can be investable regardless of rank.
3. The "unstable earnings profile" penalty in `rules.md § Risk Controls` cannot be applied — it requires fundamentals (L144). Disclosed as an *unapplied* penalty, not as absent risk.
4. 22 of 56 earnings lookups were vendor-empty and resolved by inference (L023, L024). Two of those resolutions (EQR, PKG) rest on a volume-only signature with a ~0.01% price move, which is weak evidence; flagged in `13`.
5. Adjusted closes include dividend reinvestment, so momentum and relative strength are total-return measures. Across a 60-day window this adds roughly the names' quarterly yield (order 0.5–1pp) versus a price-return measure — small relative to the ±25pp momentum dispersion, and applied uniformly to all 514 names.
