# 04 Universe Summary — 2026-07-20 (claude-fable-5)

## Construction

S&P 500 ∪ Nasdaq-100 via `build_index_universe.py` (universe_summary.json, L003): **503 + 101, overlap 89 → union 515**; caches fetched 2026-06-21 (stale-cache rule: used as-is, `fetched_at` logged). Core ETFs (SPY/QQQ/SOXX) analyzed separately — never universe members. Normal index-union path succeeded; the 30-name sampled fallback was not used. All ranks labeled `INDEX_UNION_PCTL (n=514)`.

## Inclusion / Exclusion Log

| Filter | Threshold | Result |
|---|---|---|
| Price | > $5 | 515/515 pass |
| ADV20 dollar | > $20M | 515/515 pass (min observed well above; L004) |
| History | ≥ 60 trading days (GO minimum) | 514/515 — **FDXF excluded** (FedEx Freight spinoff, 36 bars; indicator status UNAVAILABLE) |
| Market cap | > $2B | Not independently sourced; index membership used as proxy (disclosed; Enhancing-class gap) |
| Listing age / spread / session-coverage | per rules | No exclusions triggered from fetched data; spread tape not wired (Enhancing) |

Eligible universe: **514 names**.

## Metric Coverage Summary (rules.md §Financial Metrics)

| Metric Group | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Price history / momentum / MA / volume | 514/514 | — | Tech_Z inputs, full coverage |
| Beta / TE / rvol30 / maxDD60 / VaR / CVaR | 514/514 (DERIVED from fetched bars) | — | Macro_Z inputs + risk pack |
| RSI/MACD/TD9 daily+weekly | 514/514 | — | Tech pack (≥70% bar met) |
| Monthly RSI / MACD / MA | 511–503/514 | 3–11 short-history names | Diagnostics unaffected; none published |
| Fundamental family (rev/EPS revisions, margins, FCF) | 0 | 514 | **Family UNAVAILABLE** → 0.00 contribution, DQ 0.80 |
| Sentiment family (revisions breadth, short interest, IV) | 0 | 514 | **Family UNAVAILABLE** → 0.00 contribution |
| Earnings dates | 34 checked (2-pass preflight) | rest NOT_FETCHED | Required-input satisfied for every published name |
| Risk-free rate | treasury.gov 13w 3.71% (L009) | — | Ratios are excess-return, not RAW_DIAGNOSTIC |

Missing Fund/Sent inputs affect **data quality and the evidence-threshold count**, not GO-gate input grounding (Enhancing-class treatment per rules.md §Input Classification; the structural gate consequence is documented in 07/08).

## Technical Indicator Coverage (daily / weekly / monthly)

TD-9 514/514/514 · RSI(14) 514/514/511 · MACD 514/514/507 · MA alignment 514/514/499 · momentum 514/514/~505 · volume ratio 514/514/511 · rel-strength vs SPY 514/514/511 (technical_indicators.json `generated_at 2026-07-20T16:27:43Z`; monthly gaps are short-history names, none in the published sleeve).

## Publication-Boundary Disclosure

After earnings penalties re-ranked the cross-section, final ranks #19–20 belong to HUM and DVA, which were not part of either bounded earnings-preflight pass. Per the one-revision discipline they are **excluded from the published sleeve and prediction ledger** (unfetched earnings = unpublishable), disclosed here rather than silently included; they are not investable regardless (structural gate). AAPL (pctl 81.3) and WST (pctl 80.3) took −0.10 in-window penalties in the second pass and publish at their post-penalty ranks. ABBV fell below the 60th-percentile rank floor after its penalty → rejection log (05).
