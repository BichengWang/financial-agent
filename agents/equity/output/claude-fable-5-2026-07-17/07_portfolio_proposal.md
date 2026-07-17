# 07 Portfolio Proposal — 2026-07-17

**No proposal — NO_TRADE.** The investable set is empty before sizing begins: evidence threshold #2 (≥3 of 4 factor families non-negative) is unsatisfiable with Fund_Z and Sent_Z `UNAVAILABLE` universe-wide (05; 14th consecutive run). Per the Failure Rule, no portfolio is forced.

## §0 Constraint Feasibility Pre-Check (recorded for the audit trail)

Run on the would-be top-20 from already-fetched inputs (L036-L196), per the Track B pre-check (2026-06-10, HUMAN_REVIEW):

- **Sleeve beta range:** the rank leaders are defensives with near-zero or negative 60d betas — DOC 0.53, MNST 0.37, TRV −0.76, DVA ~0.5-class, UNH −0.19, ABBV −0.68, MPC −0.65 — while only CRWD/DDOG/PANW/GE carry betas near or above 1. An equal-weight top-10 sleeve computes well below the 0.90 floor; reaching 0.90–1.10 would require concentrating into the handful of high-beta names, colliding with the 5% single-name cap and the correlation cap inside the security complex (CRWD/PANW/DDOG pairwise). Conclusion: even absent the family gate, this cross-section is the 06-10 infeasibility shape again — `NO_TRADE` on feasibility, without spending the revision pass.
- **Event risk:** 27 shortlist names inside the buffered 14d earnings window (03) — downgrade trigger #4 would bind on any GO attempt.
- **Sector concentration:** the leadership is health-care- and financials-heavy (DVA/UNH/LLY/ABBV + USB/STT/PRU/MET/TRV); a rank-faithful sleeve would test the 30% sector cap in financials.

## Per-Position Recommendation Metrics

Not drafted (no sizing). The full per-name Recommendation Metrics Blocks — entry, target, mu, sigma, CI, Sharpe/Sortino/IR, Kelly, VaR/CVaR, DD, TD9/RSI/MACD, score traces, ledger rows — are published for all 23 monitoring names in 05 and `15_predictions.json`; nothing here recomputes or extends them.

## Excluded Names

Near-miss ranks 21–30 and the reasoning: 05 §Near-Miss Rejection List. LIN/ANET dropped by reflection decision (02 §5); the eight June DROPs remain excluded sub-60.
