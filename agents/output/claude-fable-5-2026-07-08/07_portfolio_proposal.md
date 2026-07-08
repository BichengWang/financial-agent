# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (Task 0 — before any sizing)

**Investable set is empty** (family-coverage gate: Fund_Z/Sent_Z UNAVAILABLE universe-wide → evidence threshold #2 unsatisfiable; see 04/05). With zero investable names, the minimum-count constraint (≥5) fails before any weight can be drafted → **NO_TRADE** recommended immediately; no weights drafted, no revision pass spent. This is stop criterion #1 (composition), not a process-integrity halt.

## Methodology Demonstration Note (non-binding, no weights)

Had the gate not bound, the feasibility profile of today's top-20 would have been materially better than the June 10 vintage that produced the beta-band NO_TRADE:

- **Sleeve-beta range**: top-20 betas span -0.58 (ABBV, carry) to 1.48 (PANW), with enough mid-beta names (BEN 0.96, CRL 0.96, AMCR 1.00, MAS 1.20) that a 0.90–1.10 portfolio beta is achievable under the 5% single-name cap — unlike 2026-06-10 (all-defensive, sleeve beta -0.14).
- **Sector spread**: healthcare-adjacent weight (DVA, HUM, VRTX, BAX, LLY, ABBV, WST, CRL, MRNA) would bind the 30% GICS cap quickly; financials (BEN, TROW, STT), tech/security (PANW, CRWD, FTNT, DDOG), consumer (MNST, TTWO, LYV, AMCR), industrials (MAS, AXON) provide the offsets.
- **Correlation**: the security-software cluster (PANW/CRWD/FTNT) and the asset-manager pair (BEN/TROW) are the crowding risks; the defensive core (DVA, MNST, LYV, AMCR, LIN) is low-correlation ballast.
- **Event risk**: only 2 of the 23 published names sit inside the 14d earnings window (STT 7d, WST 15d) — below the >2-name NO_TRADE trigger; the heavy event load was pushed out of the sleeve by the penalty machinery upstream, which is the intended behavior.

Per-position Recommendation Metrics: inherited unchanged from 05 (no recomputation performed; ledger rows L060–L197). Portfolio-level Sharpe/Sortino/IR/TE/VaR/CVaR/drawdown, correlation matrix, and sector table: **not computed — no portfolio exists to measure** (computing them for a non-portfolio would manufacture unauditable numbers).

## Excluded-Name Rationale

All exclusions are score- or event-based and documented in 05 §Near-Miss and 02 §5: UNH (earnings 7d penalty → 79.7 pctl; settled HIT — revisit post-print), DAL/UAL (earnings 1d/8d), FFIV (earnings est newly inside window), AIZ (rank 21 vs top-20 cut), DROP-bound names per reflection.

## Recommendation

**NO_TRADE** — publish forecasts (23 MONITOR records + 3 core-ETF MARKET_FORECAST records in 15) and continue the settlement cadence: 17 records due tomorrow 2026-07-09, 20 due 2026-07-12.
