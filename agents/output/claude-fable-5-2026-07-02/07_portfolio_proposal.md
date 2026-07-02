# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (agents.md §Portfolio Construction task 0)

Investable set from 05: **0 names** (minimum 5). Stop criterion `NO_TRADE #1` fires before sizing; no weights drafted, no revision pass spent.

Supporting evidence (all DERIVED from fetched 60d history; diagnostics only, not a proposal):

- Even ignoring the family gate, the 23-name monitor sleeve cannot reach the protected beta band on NAV: filling 100% of NAV with the 20 highest-beta sleeve names at the 5% cap gives NAV beta = 0.05 x Σβ(top-20) = 0.05 x 13.14 = **0.66** << 0.90. The leadership is structurally low-beta/defensive.
- Equal-weight top-12 sleeve (sleeve-relative weights): beta_sleeve 0.73 (band 0.90-1.10 ✗), avg pairwise corr 0.127 (cap 0.45 ✓, max pair DOC|DVA 0.73), sigma_1m 5.5%, parametric 95th-pctl 1-month drawdown 1.65σ = 9.1% (cap 8% ✗).
- Sector shares under equal weight (INFERRED sectors): Health Care 5/12 = 42% — the 30% cap binds immediately (protected rule #4).

## Decision

**NO_TRADE.** The investable minimum (5 names) is unreachable this run because fundamental and sentiment families have no wired source at index-union scale (Enhancing inputs — they cap confidence and family coverage but never block GO by themselves; what blocks GO here is evidence threshold #2). This is a composition/evidence failure, not a data-integrity failure — HALTED is not warranted (all five Required inputs are grounded, see 00 GO-Gate).

## Per-Position Recommendation Metrics (monitoring sleeve, inherited from 05 — reference only, not sized)

| Ticker | Entry | Date | Tag | Target | TgtDate | mu | sigma | SigSrc | Sharpe | Sortino | IR | Kelly.25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | CI70 | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DVA | 233.71 | 2026-07-02 | DELAYED | 245.40 | 2026-07-30 | +5.0% | 6.9% | REALIZED_VOL_30D | 0.68 | 1.07 | 0.31 | 0.050 | -6.3% | -9.2% | -6.3% | SELL_SETUP_8/SELL_SETUP_4/SELL_SETUP_6 | 84/82/74 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [228.69,262.10] | L076 |
| HUM | 394.07 | 2026-07-02 | DELAYED | 413.77 | 2026-07-30 | +5.0% | 11.6% | REALIZED_VOL_30D | 0.41 | 0.98 | 0.39 | 0.050 | -14.1% | -18.9% | -5.6% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_3 | 70/76/61 | BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | [366.30,461.24] | L082 |
| BAX | 22.55 | 2026-07-02 | DELAYED | 23.90 | 2026-07-30 | +6.0% | 10.6% | REALIZED_VOL_30D | 0.54 | 0.81 | 0.52 | 0.050 | -11.5% | -15.8% | -11.8% | SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2 | 69/60/42 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [21.42,26.38] | L088 |
| BEN | 33.62 | 2026-07-02 | DELAYED | 35.31 | 2026-07-30 | +5.0% | 8.4% | REALIZED_VOL_30D | 0.56 | 0.92 | 0.55 | 0.050 | -8.8% | -12.2% | -6.1% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_7 | 60/75/66 | BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | [32.39,38.23] | L094 |
| URI | 1090.01 | 2026-07-02 | DELAYED | 1155.41 | 2026-07-30 | +6.0% | 9.9% | REALIZED_VOL_30D | 0.58 | 1.63 | 0.36 | 0.050 | -10.3% | -14.4% | -6.2% | BUY_SETUP_2/SELL_SETUP_6/SELL_SETUP_4 | 56/65/65 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [1043.39,1267.42] | L100 |
| MAS | 82.00 | 2026-07-02 | DELAYED | 86.92 | 2026-07-30 | +6.0% | 9.3% | REALIZED_VOL_30D | 0.62 | 0.93 | 0.50 | 0.050 | -9.3% | -13.1% | -14.5% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_4 | 74/66/60 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [79.03,94.81] | L106 |
| PANW | 350.84 | 2026-07-02 | DELAYED | 368.38 | 2026-07-30 | +5.0% | 16.1% | REALIZED_VOL_30D | 0.29 | 0.56 | 0.31 | 0.050 | -21.5% | -28.1% | -13.3% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 80/82/76 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [309.81,426.95] | L112 |
| LII | 563.65 | 2026-07-02 | DELAYED | 597.47 | 2026-07-30 | +6.0% | 10.5% | REALIZED_VOL_30D | 0.54 | 0.81 | 0.53 | 0.050 | -11.2% | -15.5% | -11.2% | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_4 | 61/60/55 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | [536.20,658.74] | L118 |
| DOC | 21.77 | 2026-07-02 | DELAYED | 23.08 | 2026-07-30 | +6.0% | 8.0% | REALIZED_VOL_30D | 0.72 | 1.35 | 0.46 | 0.050 | -7.1% | -10.4% | -7.9% | SELL_SETUP_8/SELL_SETUP_2/SELL_SETUP_4 | 67/67/57 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [21.27,24.88] | L124 |
| HSIC | 85.97 | 2026-07-02 | DELAYED | 91.13 | 2026-07-30 | +6.0% | 5.7% | REALIZED_VOL_30D | 1.00 | 1.33 | 0.85 | 0.050 | -3.4% | -5.7% | -12.8% | SELL_SETUP_7/SELL_SETUP_6/SELL_SETUP_3 | 72/65/60 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [86.04,96.21] | L130 |
| MRNA | 78.66 | 2026-07-02 | DELAYED | 82.59 | 2026-07-30 | +5.0% | 22.1% | REALIZED_VOL_30D | 0.21 | 0.50 | 0.23 | 0.050 | -31.5% | -40.6% | -18.4% | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_8 | 80/77/56 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [64.50,100.68] | L136 |
| MNST | 97.86 | 2026-07-02 | DELAYED | 102.75 | 2026-07-30 | +5.0% | 4.7% | REALIZED_VOL_30D | 1.00 | 1.30 | 0.50 | 0.050 | -2.7% | -4.7% | -3.9% | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_4 | 72/75/73 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | [97.97,107.53] | L142 |

Excluded names: every universe name outside the published 24 — either below the 60th percentile (mu table: do not rank), inside ranks 21-30 without a reflection carry (listed in 05 near-miss), or DROP-bound from 02 (MCK, COST, WMT, CVX, XOM, MU, NVDA, GOOGL) or DOWNGRADE-bound (UNH: earnings window + pctl slide, mu clamp). No name was excluded for missing price/sigma/beta/earnings inputs — Required inputs were grounded for the full shortlist.

Correlation matrix (top-12, 60d daily returns): average 0.127; only DOC|DVA (0.73) and BAX|HSIC (0.55) exceed 0.50; full pairwise values retained in engine output. Portfolio-level Sharpe/Sortino/IR/tracking error are not published because no portfolio is proposed (NO_TRADE); the sleeve diagnostics above cite the same ledger rows as 05.

