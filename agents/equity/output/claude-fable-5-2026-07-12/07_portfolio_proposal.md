# 07 Portfolio Proposal — Constraint Feasibility Pre-Check Only (REVIEW_ONLY)

**No weights drafted.** Two independent caps bind before sizing: (1) **weekend rule** — no executable session today (Sunday 2026-07-12); (2) the family-coverage gate leaves the investable set empty (05), which on a trading day would force NO_TRADE. Per the stage-0 feasibility pre-check (Track B, 2026-06-10, HUMAN_REVIEW), the analytics below demonstrate what a sizing pass would face; they inherit 05/01 values with no recomputation.

## Feasibility Sketch (hypothetical top-10 sleeve, from already-fetched inputs)

- **Beta band:** the top-10 betas span 0.17 (HUM) to 1.43 (DAL); an equal-weight invested sleeve carries beta **0.835** — below the 0.90–1.10 band. Reaching the band requires concentrating toward CRWD/DAL/CRL and away from HUM/DVA/DOC; feasible in weights, but it fights the leaderboard's defensive tilt (same structural tension as every run since 07-03).
- **Correlation:** average pairwise correlation of the top-10 is **0.134** — comfortably inside the 0.45 cap. One cluster to manage: the security-software block (CRWD/DDOG/FTNT at 0.66–0.79 pairwise; PANW adjacent) — a Kelly-capped book would hold at most 2 of the 4. One diversification pair to note: DVA/DOC at 0.74.
- **Sector caps:** the published 24 skew Information Technology 8/24 and Health Care 6/24 — a 10-name book drawn top-down hits the 30% sector cap quickly in IT; enforceable by construction.
- **Event risk:** zero of the top-10 carries earnings inside 14 days (confirmed dates) — the penalty already gated those names; the NO_TRADE trigger "more than 2 names with earnings inside 14d" would not fire.
- **Drawdown:** with avg pairwise corr 0.134 and 1m sigmas of 5–19%, a 10-name equal-weight sleeve's parametric 95th-pctl 1-month drawdown sits well inside the 8% NAV cap at any gross ≤ 50% (the Enhancing-inputs exposure cap that would apply on a GO day).

## Correlation Matrix (60d daily returns, hypothetical top-10)

| | DVA | FFIV | CRL | CRWD | HUM | DDOG | FTNT | DAL | DOC | BEN |
|---|---|---|---|---|---|---|---|---|---|---|
| **DVA** | 1.00 | -0.07 | -0.05 | -0.14 | 0.07 | -0.14 | -0.10 | 0.19 | 0.74 | 0.10 |
| **FFIV** | -0.07 | 1.00 | 0.02 | 0.38 | 0.33 | 0.24 | 0.41 | -0.07 | 0.02 | 0.25 |
| **CRL** | -0.05 | 0.02 | 1.00 | 0.13 | 0.09 | 0.03 | 0.04 | 0.38 | -0.03 | -0.03 |
| **CRWD** | -0.14 | 0.38 | 0.13 | 1.00 | 0.11 | 0.66 | 0.75 | 0.12 | -0.21 | 0.05 |
| **HUM** | 0.07 | 0.33 | 0.09 | 0.11 | 1.00 | 0.16 | 0.20 | -0.10 | 0.02 | 0.18 |
| **DDOG** | -0.14 | 0.24 | 0.03 | 0.66 | 0.16 | 1.00 | 0.79 | -0.05 | -0.08 | -0.14 |
| **FTNT** | -0.10 | 0.41 | 0.04 | 0.75 | 0.20 | 0.79 | 1.00 | -0.02 | -0.06 | 0.01 |
| **DAL** | 0.19 | -0.07 | 0.38 | 0.12 | -0.10 | -0.05 | -0.02 | 1.00 | 0.34 | 0.26 |
| **DOC** | 0.74 | 0.02 | -0.03 | -0.21 | 0.02 | -0.08 | -0.06 | 0.34 | 1.00 | 0.23 |
| **BEN** | 0.10 | 0.25 | -0.03 | 0.05 | 0.18 | -0.14 | 0.01 | 0.26 | 0.23 | 1.00 |


## Sector Table (published 24, sleeve composition — weights undrafted)

| Sector | Count | Names |
|---|---|---|
| Information Technology | 8 | FFIV, CRWD, DDOG, FTNT, PANW, CSCO, ZBRA, ANET |
| Health Care | 6 | DVA, CRL, HUM, CVS, LLY, ABBV |
| Financials | 3 | BEN, TROW, AIZ |
| Industrials | 2 | DAL, SWK |
| Consumer Discretionary | 2 | BBY, ABNB |
| Real Estate | 1 | DOC |
| Communication Services | 1 | TTWO |
| Materials | 1 | LIN |

Sector labels are GICS assignments from analyst knowledge (INFERRED — no sector feed wired); used for cap bookkeeping only, never in scores.

## Excluded-Name Rationale

Ranks 21–30 and the event-gated financials: 05 §Near-Miss. UNH and GE (multiple settled HITs each) are excluded solely on their confirmed 07-16 prints — standing re-entry candidates for Tuesday's run onward. The eight DROP names from 02 §5 remain excluded on carried settled-MISS evidence and sub-66 percentiles.

## Per-Position Recommendation Metrics

Fully carried in 05's ranked table (entry, target, mu, sigma, CI70, Sharpe, Sortino, IR, Kelly 0.25 (cap-binding 0.050 for every name), VaR95, CVaR95, MaxDD60, TD9/RSI/MACD d/w/m, ledger rows) — inherited here by reference, no recomputation.
