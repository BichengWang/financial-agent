# 08 Risk Review — 2026-07-28

**Committee decision: APPROVE publication as NO_TRADE.**

| Review | Finding | Decision |
|---|---|---|
| Price/target lineage | Every published entry passes StockAnalysis + Yahoo/Nasdaq ≤1%; targets/CI recompute from entry, mu, population sigma (L002–L006,L020–L022) | PASS |
| Sigma lineage | REALIZED_VOL_30D uses population stdev (ddof=0) × sqrt(21) (L011) | PASS |
| Score attribution | Every name discloses Fund/Tech/Sent/Macro, DQ, penalties, drivers, and formula (L018,L029–L032) | PASS |
| Metric ledger coverage | Financial/risk/technical metrics map to L010–L032 | PASS |
| Kelly | Beta-adjusted residual edge / tracking-error²; quarter-Kelly capped at 5%; no weights created | PASS |
| Technical interpretation | TD9/RSI/MACD jointly interpreted; technical_indicators.json lineage | PASS |
| Source Ledger | Contiguous L001–L069; no ILLUSTRATIVE claims | PASS |
| GO-blocking discipline | Binding evidence/DQ gates distinguished from Enhancing gaps; pctl80 beta cited only as corroboration | PASS |
| Prediction completeness | 20 EQUITY_ALPHA + 3 MARKET_FORECAST, each settleable; 35 valid current-run settlement candidates retained audit-only because matching keys were already canonical | PASS |
| Macro event calendar | FOMC meeting 2026-07-28–29; statement 2026-07-29 14:00 ET falls inside forecast horizon (L069) | RISK FLAG |
| Sector/event risk | Industrials 35%; MET/PRU/MPC are penalty-window names; SJM/BBY have unpenalized estimate bands overlapping the target (L019) | NO_TRADE supported |

Top concerns: (1) two missing production factor families make threshold #2 unsatisfiable; (2) DQ 80% is below 85%; (3) a hypothetical equal-weight monitor sleeve breaches the Industrials cap; (4) the FOMC decision and five earnings-band risks fall inside the forecast horizon, including three penalty-window names. No revision can turn this run into GO without new upstream evidence, so the final recommendation remains **NO_TRADE**.
