# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

The investable-grade set is CAT, GOOGL, GS, GE, LLY, FCX, BAC. At the protected 5% single-name cap, maximum gross exposure is 35.00% and maximum NAV beta is 0.509, below the required 0.90-1.10 band. The run therefore publishes `NO_TRADE`; no executable weights are approved.

## Max-Cap Diagnostic Basket (Not Approved)

| Ticker | Weight | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 5.00% | 985.82 | 2026-06-18 | DELAYED | 1044.97 | 2026-07-20 | +6.0% | 12.24% | REALIZED_VOL_30D | 0.49 | 0.75 | 0.24 | +5.00% | -14.19% | -19.21% | -8.97% | SELL_SETUP_4/SELL_SETUP_3 | 919.51 | 1170.43 | RawAdjZ=(0.30*0.78+0.30*1.77+0.25*1.74+0.15*1.55)*0.90-0.00=1.29; Adj Score=100.0 sampled pct | L139,L140,L141,L142,L143,L144 |
| GOOGL | 5.00% | 368.03 | 2026-06-18 | DELAYED | 390.11 | 2026-07-20 | +6.0% | 8.30% | REALIZED_VOL_30D | 0.72 | 1.15 | 0.37 | +5.00% | -7.70% | -11.10% | -11.48% | SELL_SETUP_4/BUY_SETUP_4 | 358.34 | 421.89 | RawAdjZ=(0.30*2.80+0.30*-0.08+0.25*1.74+0.15*0.70)*0.90-0.00=1.22; Adj Score=97.1 sampled pct | L043,L044,L045,L046,L047,L048 |
| GS | 5.00% | 1096.56 | 2026-06-18 | DELAYED | 1151.39 | 2026-07-20 | +5.0% | 10.03% | REALIZED_VOL_30D | 0.50 | 0.74 | 0.30 | +5.00% | -11.55% | -15.66% | -8.36% | SELL_SETUP_5/SELL_SETUP_9 | 1037.02 | 1265.76 | RawAdjZ=(0.30*0.06+0.30*1.77+0.25*1.26+0.15*1.53)*0.90-0.00=0.98; Adj Score=94.1 sampled pct | L109,L110,L111,L112,L113,L114 |
| GE | 5.00% | 357.64 | 2026-06-18 | DELAYED | 375.52 | 2026-07-20 | +5.0% | 10.05% | REALIZED_VOL_30D | 0.50 | 1.04 | 0.20 | +5.00% | -11.58% | -15.70% | -13.12% | SELL_SETUP_6/SELL_SETUP_5 | 338.15 | 412.90 | RawAdjZ=(0.30*0.35+0.30*1.73+0.25*0.68+0.15*1.55)*0.90-0.00=0.92; Adj Score=91.2 sampled pct | L145,L146,L147,L148,L149,L150 |
| LLY | 5.00% | 1098.57 | 2026-06-18 | DELAYED | 1142.51 | 2026-07-20 | +4.0% | 9.06% | REALIZED_VOL_30D | 0.44 | 1.06 | 0.26 | +5.00% | -10.94% | -14.66% | -10.89% | BUY_SETUP_5/SELL_SETUP_9 | 1039.03 | 1245.99 | RawAdjZ=(0.30*0.91+0.30*1.16+0.25*1.01+0.15*0.56)*0.90-0.00=0.86; Adj Score=88.2 sampled pct | L121,L122,L123,L124,L125,L126 |
| FCX | 5.00% | 68.68 | 2026-06-18 | DELAYED | 71.43 | 2026-07-20 | +4.0% | 15.70% | REALIZED_VOL_30D | 0.25 | 0.37 | -0.10 | +5.00% | -21.91% | -28.35% | -21.02% | SELL_SETUP_6/SELL_SETUP_5 | 60.21 | 82.64 | RawAdjZ=(0.30*-0.14+0.30*1.45+0.25*1.09+0.15*1.46)*0.90-0.00=0.79; Adj Score=85.3 sampled pct | L169,L170,L171,L172,L173,L174 |
| BAC | 5.00% | 56.20 | 2026-06-18 | DELAYED | 57.89 | 2026-07-20 | +3.0% | 6.22% | REALIZED_VOL_30D | 0.48 | 0.78 | 0.32 | +5.00% | -7.27% | -9.82% | -8.38% | SELL_SETUP_9/SELL_SETUP_3 | 54.25 | 61.52 | RawAdjZ=(0.30*0.61+0.30*1.12+0.25*1.16+0.15*0.52)*0.90-0.03=0.77; Adj Score=82.4 sampled pct | L103,L104,L105,L106,L107,L108 |

## Portfolio Analytics
| Metric | Value | Lineage |
| --- | --- | --- |
| Gross exposure | 35.00% | 5% cap times 7 names |
| Expected NAV return | 1.65% | sum(weight x mu) |
| Expected beta | 0.509 | sum(weight x beta) |
| Average pairwise correlation | 0.431 | 60d fetched daily returns |
| Portfolio sigma | 2.82% | sqrt(w covariance w) scaled to 1m |
| VaR95 | -3.00% | parametric normal return-space estimate |
| CVaR95 | -4.15% | parametric normal return-space estimate |
| 95th-pctl drawdown | 4.65% | 1.65 x portfolio sigma |

## Sector Table
| Sector | Weight | Names |
| --- | --- | --- |
| Communication Services | 5.00% | GOOGL |
| Financials | 10.00% | GS, BAC |
| Health Care | 5.00% | LLY |
| Industrials | 10.00% | CAT, GE |
| Materials | 5.00% | FCX |

## Correlation Matrix
| | CAT | GOOGL | GS | GE | LLY | FCX | BAC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 1.00 | 0.51 | 0.59 | 0.54 | 0.45 | 0.51 | 0.35 |
| GOOGL | 0.51 | 1.00 | 0.45 | 0.48 | 0.52 | 0.30 | 0.35 |
| GS | 0.59 | 0.45 | 1.00 | 0.58 | 0.31 | 0.63 | 0.48 |
| GE | 0.54 | 0.48 | 0.58 | 1.00 | 0.31 | 0.38 | 0.53 |
| LLY | 0.45 | 0.52 | 0.31 | 0.31 | 1.00 | 0.23 | 0.21 |
| FCX | 0.51 | 0.30 | 0.63 | 0.38 | 0.23 | 1.00 | 0.34 |
| BAC | 0.35 | 0.35 | 0.48 | 0.53 | 0.21 | 0.34 | 1.00 |

## Excluded-Name Rationale

Monitoring names are excluded because admitting sub-threshold names to repair beta would violate the factor-scoring threshold. Raising weights above 5% would violate the protected single-name cap.
