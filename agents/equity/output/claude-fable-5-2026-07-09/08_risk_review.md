# 08 Risk Review

Committee decision: **APPROVE** — publish as **NO_TRADE** with the 23-name monitoring sleeve, the Core ETF forecast block, and 17 settlements. One prior-cycle-style revision was NOT needed this run.

## Checks (rules.md §Risk Committee checklist)

1. **Fabrication / weak inputs** — every entry, settlement, and macro price is tool-fetched this run with retrieval timestamps, two-source verified (max div 0.121%), ETFs triple-checked vs IBKR MCP (0.008%). The 10:47 ET fetch that drifted intraday was caught by the cross-check and superseded by the 14:36 ET refetch — both logged in L002; no stale price reached a published table. PASS.
2. **Overfitting / unvalidated signals** — no parameter changed this run; the rank-IC evidence went to evolution (13) and was rejected for action, not acted on. PASS.
3. **Event concentration** — 2 of 23 published names inside the buffered window (DAL 0d — reported pre-market, print embedded in the live bar; FFIV 18d), both penalized -0.10. Banks cluster 07-14..17 held out by penalties. PASS.
4. **Correlation / sector crowding** — moot at NO_TRADE; noted for the record: IT 7 / HC 6 / Fin 4 in the sleeve (07 pre-check). N/A.
5. **Beta drift** — moot; pre-check shows ~0.75 equal-weight sleeve beta, below band — reconfirms NO_TRADE rather than contradicting it. N/A.
6. **Thesis quality vs confidence** — all names LOW; theses are momentum/RS-grounded with INFERRED tags on judgment claims. PASS.
7. **Report-vs-rules mismatches** — status semantics (NO_TRADE on live data failing thresholds, not REVIEW_ONLY) consistent with rules.md §Run Status. PASS.
8. **Price/derived-field citations** — every numeric entry has price_date + LIVE tag + ledger row; targets/CI computed only from tagged entries. PASS.
9. **Sigma violations** — REALIZED_VOL_30D stated per name and ETF; no round sigmas; no mu/sigma-free ranked names (all 23 + 3 ETFs settleable). PASS.
10. **Score attribution** — 05 carries the full trace per name (family z-scores, DQ 0.80, penalties, drivers, ledger rows); missing families shown as 0.00 (UNAVAILABLE), never neutral-positive. PASS.
11. **Source Ledger completeness** — 207 rows; all downstream tables cite rows; settlement calcs cite vintage entries + today's prints. PASS.
12. **Live-sounding claims** — "settled/validated" statements cite settlement rows; intraday language cites the refetch timestamps. PASS.
13. **GO-blocking discipline** — GO is blocked by evidence threshold #2 (investable count), NOT by missing Enhancing inputs; the GO-Gate Table (00) grounds all five Required inputs. The family-coverage gate itself remains the standing Track B question pending HUMAN_REVIEW (13). PASS.
14. **Prediction records** — 15_predictions.json: 23 EQUITY_ALPHA (all with score_explainability + benchmark_price 751.17) + 3 MARKET_FORECAST + 17 settlements. Publishing gate satisfied. PASS.
15. **Technical indicator lineage** — every displayed TD9/RSI/MACD/momentum state cites technical_indicators.json (L003) + underlying price rows; no indicator treated as a standalone signal (exhaustion flags only modify penalties/mu). PASS.

## Top Three Concerns (severity order)

1. **The two-family scoring gate is now double-edged** (9th consecutive NO_TRADE): the settled evidence cuts both ways — the claude 06-10 vintage ordered alpha inversely (IC -0.51) which argues for keeping the gate closed, while the gpt-5 06-11 vintage ordered it correctly (IC +0.348) and the pooled hit rate is 51.7%. The standing Track B proposal and today's rank-IC trigger both land in the same human review — that review is now the binding constraint on the system, not data quality.
2. **Earnings-window shortcut**: estimates cover the ~76-name shortlist, not all 513 (AXP example in 04). Conservative for published names, but a full-universe cadence pass should be automated before earnings season peaks next week.
3. **Intraday vol regime on the growth complex**: SOXX 30d rvol 74.7% (1.7x prior window) with a LOW-confidence ETF forecast; the monitoring sleeve's IT concentration (7/23) inherits this tail.

Final publication recommendation: **NO_TRADE** (analysis + monitoring sleeve + market-forecast sleeve published; no execution).
