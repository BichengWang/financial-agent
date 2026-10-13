# Grounding

**Inputs:** ticker, requested as-of date, graph policy, evidence contract, observed source documents.

**Steps:**
1. Confirm security, exchange, currency, share classes and any ADR ratio. Rate information richness A (abundant), B (moderate), or C (sparse); identify consensus, missing-data, and selection biases. Separate knowledge limits from investment risk.
2. Prefer issuer filings/SEC for statements and exchange or reliable quote publishers for prices. Independently observe a second publisher for every required reported fact; preserve both observations and excerpts. Syndicated copies do not add independence.
3. Collect required facts and, where available, five-year revenue, margins, cash flow, segment and quarterly trends. Record fiscal versus calendar dates. Label omitted history explicitly rather than extrapolating it.
4. Align current actual price, outstanding shares (not weighted-average diluted EPS denominator), and market cap snapshot; state share-count date, classes and split adjustments. Align EPS and price split basis. Keep GAAP diluted EPS distinct from adjusted or forward EPS.
5. Define consolidated cash (cash and equivalents), short-term investments separately, and total debt with lease inclusion disclosed. Do not equate restricted or overseas cash with freely distributable liquidity. Use same-period operating cash flow and positive capital spending. Explain acquisitions, leases, stock compensation and working-capital effects.
6. Reconcile observations before calculating. Differences above 1% require explanation and primary-document review; unresolved discrepancies block reliance. Store nulls and reasons for missing facts.

**Output:** `## Grounding`, dated source/fact table with source IDs, accounting definitions, richness rating and AI limitation statement; `data/evidence.json` using the contract.

**Failure path:** missing/stale facts or source gaps => provisional; malformed units, future dates or unresolved incompatible observations => blocked. Never replace unavailable current prices with historical values labeled current.

**Question:** Is apparent certainty coming from business economics or merely abundant published commentary?
