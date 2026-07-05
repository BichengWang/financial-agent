# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (agents.md §Portfolio Construction task 0)

Investable set from 05: **0 names** (minimum 5). On a trading day stop criterion `NO_TRADE #1` would fire before sizing; today the weekend rule sets **REVIEW_ONLY**. No weights drafted, no revision pass spent.

Supporting evidence (all DERIVED from fetched 60d history; diagnostics only, not a proposal):

- Even ignoring the family gate, the 23-name monitor sleeve cannot reach the protected beta band on NAV: filling 100% of NAV with the 20 highest-beta sleeve names at the 5% cap gives NAV beta = 0.05 x Σβ(top-20) = 0.05 x 14.05 = **0.70** << 0.90. The leadership is structurally low-beta/defensive (today's promotions WELL/INCY carry negative betas, replacing the also-low-beta DOC/WST/KDP).
- Equal-weight top-12 sleeve (sleeve-relative weights): beta_sleeve 0.66 (band 0.90-1.10 ✗), avg pairwise corr 0.177 (cap 0.45 ✓, max pair MAS|SWK 0.64), sigma_1m 5.2%, parametric 95th-pctl 1-month drawdown 1.65σ = 8.6% (cap 8% ✗).
- Sector shares under equal weight (INFERRED sectors): Health Care 5/12 = 42% — the 30% cap binds immediately (protected rule #4).

## Decision

**REVIEW_ONLY** (weekend; markets closed — no executable session). The investable minimum (5 names) also remains unreachable because fundamental and sentiment families have no wired source at index-union scale (Enhancing inputs — they cap confidence and family coverage but never block GO by themselves; what blocks GO here is evidence threshold #2). This is a composition/evidence failure, not a data-integrity failure — HALTED is not warranted (all five Required inputs are grounded, see 00 GO-Gate).

## Per-Position Recommendation Metrics (monitoring sleeve top-12, inherited from 05 — reference only, not sized)

| Ticker | Entry | Date | Tag | Target | TgtDate | mu | sigma | SigSrc | Sharpe | Sortino | IR | Kelly.25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | CI70 | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DVA | 234.91 | 2026-07-02 | DELAYED | 246.66 | 2026-08-02 | +5.0% | 7.0% | REALIZED_VOL_30D | 0.67 | 1.07 | 0.31 | 0.050 | -6.5% | -9.4% | -6.3% | SELL_SETUP_8/SELL_SETUP_4/SELL_SETUP_6 | 84/82/74 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [229.58,263.73] | L076 |
| PANW | 348.06 | 2026-07-02 | DELAYED | 365.46 | 2026-08-02 | +5.0% | 16.1% | REALIZED_VOL_30D | 0.29 | 0.57 | 0.31 | 0.050 | -21.6% | -28.2% | -13.3% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 78/82/76 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [307.09,423.83] | L082 |
| BEN | 34.11 | 2026-07-02 | DELAYED | 35.82 | 2026-08-02 | +5.0% | 8.2% | REALIZED_VOL_30D | 0.57 | 0.90 | 0.56 | 0.050 | -8.6% | -12.0% | -6.1% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_7 | 65/76/67 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [32.89,38.74] | L088 |
| HUM | 396.75 | 2026-07-02 | DELAYED | 416.59 | 2026-08-02 | +5.0% | 11.4% | REALIZED_VOL_30D | 0.41 | 1.05 | 0.39 | 0.050 | -13.8% | -18.5% | -5.6% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_3 | 72/76/61 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [369.52,463.65] | L094 |
| MNST | 97.60 | 2026-07-02 | DELAYED | 102.48 | 2026-08-02 | +5.0% | 4.7% | REALIZED_VOL_30D | 1.00 | 1.30 | 0.50 | 0.050 | -2.8% | -4.7% | -3.9% | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_4 | 72/75/73 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [97.71,107.25] | L100 |
| HSIC | 86.43 | 2026-07-02 | DELAYED | 91.62 | 2026-08-02 | +6.0% | 5.8% | REALIZED_VOL_30D | 0.98 | 1.33 | 0.84 | 0.050 | -3.5% | -5.9% | -12.8% | SELL_SETUP_7/SELL_SETUP_6/SELL_SETUP_3 | 73/66/60 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [86.42,96.82] | L106 |
| MAS | 82.77 | 2026-07-02 | DELAYED | 86.91 | 2026-08-02 | +5.0% | 9.3% | REALIZED_VOL_30D | 0.51 | 0.76 | 0.41 | 0.050 | -10.3% | -14.1% | -14.5% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_4 | 75/66/60 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [78.94,94.88] | L112 |
| BAX | 22.65 | 2026-07-02 | DELAYED | 24.01 | 2026-08-02 | +6.0% | 10.7% | REALIZED_VOL_30D | 0.53 | 0.81 | 0.52 | 0.050 | -11.6% | -16.0% | -11.8% | SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2 | 69/61/42 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [21.49,26.53] | L118 |
| VRTX | 528.04 | 2026-07-02 | DELAYED | 554.44 | 2026-08-02 | +5.0% | 8.3% | REALIZED_VOL_30D | 0.56 | 1.20 | 0.66 | 0.050 | -8.7% | -12.2% | -6.2% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_1 | 81/71/62 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | [508.69,600.19] | L124 |
| CCEP | 106.61 | 2026-07-02 | DELAYED | 113.01 | 2026-08-02 | +6.0% | 7.5% | REALIZED_VOL_30D | 0.76 | 1.45 | 0.77 | 0.050 | -6.4% | -9.5% | -9.6% | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_1 | 74/62/64 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | [104.68,121.33] | L130 |
| SWK | 91.90 | 2026-07-02 | DELAYED | 97.41 | 2026-08-02 | +6.0% | 11.6% | REALIZED_VOL_30D | 0.49 | 0.77 | 0.47 | 0.050 | -13.2% | -18.0% | -8.9% | BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_4 | 65/65/54 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [86.28,108.55] | L136 |
| LYV | 186.59 | 2026-07-02 | DELAYED | 197.79 | 2026-08-02 | +6.0% | 6.5% | REALIZED_VOL_30D | 0.88 | 1.01 | 0.67 | 0.050 | -4.6% | -7.3% | -7.9% | SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_6 | 74/69/69 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [185.27,210.31] | L142 |

Excluded names: every universe name outside the published 23 — either below the 60th percentile (mu table: do not rank), inside ranks 21-30 without a reflection carry (listed in 05 near-miss), penalized into the <=19d earnings window (21 shortlist names incl. DOC/WST/KDP, which ranked top-20 yesterday), DROP-bound from 02 (MCK, COST, WMT, CVX, XOM, MU, NVDA, GOOGL), or DOWNGRADE-bound (UNH). No name was excluded for missing price/sigma/beta/earnings inputs — Required inputs were grounded for the full shortlist.

Correlation matrix (top-12, 60d daily returns): average 0.177; pairs above 0.50: MAS|SWK 0.64, HSIC|BAX 0.56, BAX|CCEP 0.52, MAS|BAX 0.50; full pairwise values retained in engine output. Portfolio-level Sharpe/Sortino/IR/tracking error are not published because no portfolio is proposed (family gate → would-be NO_TRADE); the sleeve diagnostics above cite the same ledger rows as 05.
