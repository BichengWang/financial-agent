# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (agents.md §Portfolio Construction task 0)

Investable set from 05: **0 names** (minimum 5). On a trading day stop criterion `NO_TRADE #1` would fire before sizing; today the runbook holiday rule sets **REVIEW_ONLY**. No weights drafted, no revision pass spent.

Supporting evidence (all DERIVED from fetched 60d history; diagnostics only, not a proposal):

- Even ignoring the family gate, the 23-name monitor sleeve cannot reach the protected beta band on NAV: filling 100% of NAV with the 20 highest-beta sleeve names at the 5% cap gives NAV beta = 0.05 x Σβ(top-20) = 0.05 x 14.14 = **0.71** << 0.90. The leadership is structurally low-beta/defensive.
- Equal-weight top-12 sleeve (sleeve-relative weights): beta_sleeve 0.75 (band 0.90-1.10 ✗), avg pairwise corr 0.132 (cap 0.45 ✓, max pair DOC|DVA 0.73), sigma_1m 5.7%, parametric 95th-pctl 1-month drawdown 1.65σ = 9.3% (cap 8% ✗).
- Sector shares under equal weight (INFERRED sectors): Health Care 5/12 = 42% — the 30% cap binds immediately (protected rule #4).

## Decision

**REVIEW_ONLY** (holiday; markets closed — no executable session). The investable minimum (5 names) also remains unreachable because fundamental and sentiment families have no wired source at index-union scale (Enhancing inputs — they cap confidence and family coverage but never block GO by themselves; what blocks GO here is evidence threshold #2). This is a composition/evidence failure, not a data-integrity failure — HALTED is not warranted (all five Required inputs are grounded, see 00 GO-Gate).

## Per-Position Recommendation Metrics (monitoring sleeve, inherited from 05 — reference only, not sized)

| Ticker | Entry | Date | Tag | Target | TgtDate | mu | sigma | SigSrc | Sharpe | Sortino | IR | Kelly.25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | CI70 | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DVA | 234.91 | 2026-07-02 | DELAYED | 246.66 | 2026-07-31 | +5.0% | 7.0% | REALIZED_VOL_30D | 0.67 | 1.07 | 0.31 | 0.050 | -6.5% | -9.4% | -6.3% | SELL_SETUP_8/SELL_SETUP_4/SELL_SETUP_6 | 84/82/74 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [229.58,263.73] | L076 |
| BEN | 34.11 | 2026-07-02 | DELAYED | 35.82 | 2026-07-31 | +5.0% | 8.2% | REALIZED_VOL_30D | 0.57 | 0.90 | 0.56 | 0.050 | -8.6% | -12.0% | -6.1% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_7 | 65/76/67 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [32.89,38.74] | L082 |
| HUM | 396.75 | 2026-07-02 | DELAYED | 416.59 | 2026-07-31 | +5.0% | 11.4% | REALIZED_VOL_30D | 0.41 | 1.05 | 0.39 | 0.050 | -13.8% | -18.5% | -5.6% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_3 | 72/76/61 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [369.52,463.65] | L088 |
| PANW | 348.06 | 2026-07-02 | DELAYED | 365.46 | 2026-07-31 | +5.0% | 16.1% | REALIZED_VOL_30D | 0.29 | 0.57 | 0.31 | 0.050 | -21.6% | -28.2% | -13.3% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 78/82/76 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [307.09,423.83] | L094 |
| LII | 570.03 | 2026-07-02 | DELAYED | 604.23 | 2026-07-31 | +6.0% | 10.4% | REALIZED_VOL_30D | 0.55 | 0.80 | 0.54 | 0.050 | -11.1% | -15.3% | -11.2% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_4 | 64/61/55 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | [542.87,665.59] | L100 |
| DOC | 21.89 | 2026-07-02 | DELAYED | 23.20 | 2026-07-31 | +6.0% | 8.0% | REALIZED_VOL_30D | 0.71 | 1.35 | 0.46 | 0.050 | -7.2% | -10.4% | -7.9% | SELL_SETUP_8/SELL_SETUP_2/SELL_SETUP_4 | 68/67/58 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [21.39,25.02] | L106 |
| BAX | 22.65 | 2026-07-02 | DELAYED | 24.01 | 2026-07-31 | +6.0% | 10.7% | REALIZED_VOL_30D | 0.53 | 0.81 | 0.52 | 0.050 | -11.6% | -16.0% | -11.8% | SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2 | 69/61/42 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [21.49,26.53] | L112 |
| URI | 1098.59 | 2026-07-02 | DELAYED | 1164.51 | 2026-07-31 | +6.0% | 9.8% | REALIZED_VOL_30D | 0.58 | 1.64 | 0.36 | 0.050 | -10.1% | -14.1% | -6.2% | BUY_SETUP_2/SELL_SETUP_6/SELL_SETUP_4 | 58/66/66 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [1053.00,1276.01] | L118 |
| HSIC | 86.43 | 2026-07-02 | DELAYED | 91.62 | 2026-07-31 | +6.0% | 5.8% | REALIZED_VOL_30D | 0.98 | 1.33 | 0.84 | 0.050 | -3.5% | -5.9% | -12.8% | SELL_SETUP_7/SELL_SETUP_6/SELL_SETUP_3 | 73/66/60 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [86.42,96.82] | L124 |
| MNST | 97.60 | 2026-07-02 | DELAYED | 102.48 | 2026-07-31 | +5.0% | 4.7% | REALIZED_VOL_30D | 1.00 | 1.30 | 0.50 | 0.050 | -2.8% | -4.7% | -3.9% | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_4 | 72/75/73 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [97.71,107.25] | L130 |
| MRNA | 79.76 | 2026-07-02 | DELAYED | 83.75 | 2026-07-31 | +5.0% | 22.5% | REALIZED_VOL_30D | 0.21 | 0.50 | 0.23 | 0.050 | -32.1% | -41.3% | -18.4% | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_8 | 81/77/57 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [65.11,102.39] | L136 |
| SWK | 91.90 | 2026-07-02 | DELAYED | 97.41 | 2026-07-31 | +6.0% | 11.6% | REALIZED_VOL_30D | 0.49 | 0.77 | 0.47 | 0.050 | -13.2% | -18.0% | -8.9% | BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_4 | 65/65/54 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [86.28,108.55] | L142 |

Excluded names: every universe name outside the published 24 — either below the 60th percentile (mu table: do not rank), inside ranks 21-30 without a reflection carry (listed in 05 near-miss), or DROP-bound from 02 (MCK, COST, WMT, CVX, XOM, MU, NVDA, GOOGL) or DOWNGRADE-bound (UNH). No name was excluded for missing price/sigma/beta/earnings inputs — Required inputs were grounded for the full shortlist.

Correlation matrix (top-12, 60d daily returns): average 0.132; DOC|DVA (0.73), LII|SWK (0.71) and BAX|HSIC (0.56) exceed 0.50; full pairwise values retained in engine output. Portfolio-level Sharpe/Sortino/IR/tracking error are not published because no portfolio is proposed (NO_TRADE); the sleeve diagnostics above cite the same ledger rows as 05.

