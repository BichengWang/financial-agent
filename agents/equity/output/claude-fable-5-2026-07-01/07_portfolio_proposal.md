# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (agents.md §Portfolio Construction task 0)

Investable set from 05: **0 names** (minimum 5). Stop criterion `NO_TRADE #1` fires before sizing; no weights drafted, no revision pass spent.

Supporting evidence (all DERIVED from fetched 60d history; diagnostics only, not a proposal):

- Even ignoring the family gate, the 24-name monitor sleeve cannot reach the protected beta band on NAV: even filling 100% of NAV with the 20 highest-beta sleeve names at the 5% cap yields NAV beta = 0.05 x Σβ(top-20) = 0.05 x 12.03 = **0.60** << 0.90. The leadership is structurally low-beta/defensive.
- Equal-weight top-12 sleeve (sleeve-relative weights): beta_sleeve 0.55 (band 0.90-1.10 ✗), avg pairwise corr 0.092 (cap 0.45 ✓, max pair URI|WST 0.64), sigma_1m 4.6%, parametric 95th-pctl 1-month drawdown 1.65σ = 7.6% (cap 8% ✓).
- Sector shares under equal weight (INFERRED sectors): Health Care 4/12 = 33% — the 30% cap binds immediately (protected rule #4).

## Decision

**NO_TRADE.** The investable minimum (5 names) is unreachable this run because fundamental and sentiment families have no wired source at index-union scale (Enhancing inputs — they cap confidence and family coverage but never block GO by themselves; what blocks GO here is evidence threshold #2). This is a composition/evidence failure, not a data-integrity failure — HALTED is not warranted (all five Required inputs are grounded, see 00 GO-Gate).

## Per-Position Recommendation Metrics (monitoring sleeve, inherited from 05 — reference only, not sized)

| Ticker | Entry | Date | Tag | Target | TgtDate | mu | sigma | SigSrc | Sharpe | Sortino | IR | Kelly.25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | CI70 | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DVA | 228.03 | 2026-07-01 | DELAYED | 239.43 | 2026-07-29 | +5.0% | 7.1% | REALIZED_VOL_30D | 0.66 | 1.07 | 0.31 | 0.050 | -6.8% | -9.7% | -6.3% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_6 | 81/81/73 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [222.50,256.37] | L076 |
| HUM | 409.42 | 2026-07-01 | DELAYED | 429.89 | 2026-07-29 | +5.0% | 10.9% | REALIZED_VOL_30D | 0.43 | 1.12 | 0.39 | 0.050 | -13.0% | -17.4% | -5.6% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_3 | 83/78/62 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | [383.51,476.27] | L082 |
| FFIV | 424.18 | 2026-07-01 | DELAYED | 449.63 | 2026-07-29 | +6.0% | 7.9% | REALIZED_VOL_30D | 0.72 | 1.21 | 0.62 | 0.050 | -7.1% | -10.3% | -6.2% | SELL_SETUP_5/SELL_SETUP_2/SELL_SETUP_6 | 73/76/76 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | [414.69,484.58] | L088 |
| MAS | 81.64 | 2026-07-01 | DELAYED | 86.54 | 2026-07-29 | +6.0% | 9.5% | REALIZED_VOL_30D | 0.60 | 0.94 | 0.50 | 0.050 | -9.6% | -13.5% | -14.5% | SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_4 | 74/66/59 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [78.49,94.58] | L094 |
| BEN | 34.06 | 2026-07-01 | DELAYED | 35.76 | 2026-07-29 | +5.0% | 8.9% | REALIZED_VOL_30D | 0.53 | 0.90 | 0.56 | 0.050 | -9.7% | -13.4% | -6.1% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_7 | 65/76/67 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | [32.61,38.92] | L100 |
| URI | 1111.76 | 2026-07-01 | DELAYED | 1178.47 | 2026-07-29 | +6.0% | 9.9% | REALIZED_VOL_30D | 0.58 | 1.59 | 0.36 | 0.050 | -10.3% | -14.3% | -6.2% | BUY_SETUP_1/SELL_SETUP_6/SELL_SETUP_4 | 61/68/67 | BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | [1064.55,1292.38] | L106 |
| LII | 571.08 | 2026-07-01 | DELAYED | 605.34 | 2026-07-29 | +6.0% | 10.9% | REALIZED_VOL_30D | 0.52 | 0.81 | 0.54 | 0.050 | -12.1% | -16.6% | -11.2% | SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_4 | 65/61/56 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | [540.32,670.37] | L112 |
| WST | 365.00 | 2026-07-01 | DELAYED | 383.25 | 2026-07-29 | +5.0% | 7.0% | REALIZED_VOL_30D | 0.67 | 1.02 | 0.46 | 0.050 | -6.5% | -9.4% | -7.9% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_4 | 79/72/63 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [356.75,409.75] | L118 |
| PANW | 352.04 | 2026-07-01 | DELAYED | 369.64 | 2026-07-29 | +5.0% | 16.4% | REALIZED_VOL_30D | 0.29 | 0.56 | 0.31 | 0.050 | -22.1% | -28.8% | -13.3% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 81/83/76 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [309.59,429.70] | L124 |
| V | 351.08 | 2026-07-01 | DELAYED | 372.14 | 2026-07-29 | +6.0% | 5.8% | REALIZED_VOL_30D | 0.99 | 2.60 | 0.83 | 0.050 | -3.5% | -5.9% | -6.7% | SELL_SETUP_6/SELL_SETUP_2/SELL_SETUP_3 | 72/63/60 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | [351.11,393.18] | L130 |
| CCEP | 106.10 | 2026-07-01 | DELAYED | 112.47 | 2026-07-29 | +6.0% | 7.6% | REALIZED_VOL_30D | 0.75 | 1.44 | 0.77 | 0.050 | -6.5% | -9.6% | -9.6% | SELL_SETUP_6/SELL_SETUP_5/SELL_SETUP_1 | 74/62/64 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | [104.12,120.82] | L136 |
| CVS | 104.81 | 2026-07-01 | DELAYED | 110.05 | 2026-07-29 | +5.0% | 7.3% | REALIZED_VOL_30D | 0.64 | 1.26 | 0.52 | 0.050 | -7.0% | -10.0% | -8.8% | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_4 | 70/70/68 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [102.11,117.99] | L142 |

Excluded names: every universe name outside the published 24 — either below the 60th percentile (mu table: do not rank), inside ranks 21-30 without a reflection carry (listed in 05 near-miss), or DROP-bound from 02 (MCK, COST, WMT, CVX, XOM, MU, NVDA, GOOGL). No name was excluded for missing price/sigma/beta/earnings inputs — Required inputs were grounded for the full shortlist.

Correlation matrix (top-12, 60d daily returns): average 0.092; only URI|WST (0.64) and CVS|HUM (0.55) exceed 0.50; full pairwise values retained in engine output. Portfolio-level Sharpe/Sortino/IR/tracking error are not published because no portfolio is proposed (NO_TRADE); the sleeve diagnostics above cite the same ledger rows as 05.

