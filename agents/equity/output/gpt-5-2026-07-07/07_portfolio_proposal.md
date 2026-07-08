# 07 Portfolio Proposal

## Decision

No live portfolio is proposed. The run is `REVIEW_ONLY` because a Required earnings-date feed and sourceable non-price factor families are unavailable.

## Paper Monitoring Diagnostics

The equal-weight top-10 monitoring basket is shown only to keep the process auditable; it is not an executable allocation.

| Metric | Value | Status |
| --- | ---: | --- |
| Equal-weight paper basket expected mu | 6.00% | Diagnostic |
| Realized covariance sigma, 1m | 8.29% | Diagnostic |
| Beta to SPY | 1.10 | Diagnostic |
| Average pairwise correlation | 0.15 | Diagnostic |
| Parametric 95% drawdown proxy | 13.68% | Above 8% target |

## Per-Position Recommendation Metrics

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRWD | 196.94 | 2026-07-07 | DELAYED | 208.76 | 2026-08-04 | 6.00% | 15.98% | REALIZED_VOL_30D | 0.38 | 0.80 | 0.39 | 5.00% | -20.37% | -26.92% | -17.55% | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_3 | 71.29/74.93/73.30 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 176.02 | 241.49 | Tech_Z 4.01; DQ 0.78; penalties 0.07 | L015,L016 |
| PANW | 345.76 | 2026-07-07 | DELAYED | 366.50 | 2026-08-04 | 6.00% | 16.54% | REALIZED_VOL_30D | 0.36 | 0.74 | 0.38 | 5.00% | -21.28% | -28.06% | -13.30% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_3 | 72.19/81.17/75.40 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 307.04 | 425.96 | Tech_Z 3.94; DQ 0.78; penalties 0.06 | L017,L018 |
| MRNA | 79.14 | 2026-07-07 | DELAYED | 83.89 | 2026-08-04 | 6.00% | 22.51% | REALIZED_VOL_30D | 0.27 | 0.64 | 0.27 | 5.00% | -31.14% | -40.37% | -18.40% | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_8 | 75.66/76.12/56.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 65.36 | 102.41 | Tech_Z 3.76; DQ 0.78; penalties 0.07 | L019,L020 |
| HOOD | 114.79 | 2026-07-07 | DELAYED | 121.68 | 2026-08-04 | 6.00% | 23.18% | REALIZED_VOL_30D | 0.26 | 0.50 | 0.24 | 5.00% | -32.25% | -41.76% | -21.99% | SELL_SETUP_5/SELL_SETUP_7/SELL_SETUP_2 | 66.33/60.41/63.50 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 94.00 | 149.36 | Tech_Z 3.78; DQ 0.78; penalties 0.08 | L021,L022 |
| DDOG | 263.50 | 2026-07-07 | DELAYED | 279.31 | 2026-08-04 | 6.00% | 18.49% | REALIZED_VOL_30D | 0.32 | 0.92 | 0.24 | 5.00% | -24.51% | -32.09% | -20.51% | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_3 | 67.72/74.44/74.53 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 228.63 | 329.99 | Tech_Z 3.72; DQ 0.78; penalties 0.07 | L023,L024 |
| DVA | 236.90 | 2026-07-07 | DELAYED | 251.11 | 2026-08-04 | 6.00% | 6.97% | REALIZED_VOL_30D | 0.86 | 1.34 | 0.38 | 5.00% | -5.51% | -8.37% | -6.31% | SELL_SETUP_9/SELL_SETUP_5/SELL_SETUP_6 | 85.19/82.68/74.11 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 233.93 | 268.30 | Tech_Z 3.65; DQ 0.78; penalties 0.06 | L025,L026 |
| WST | 353.65 | 2026-07-07 | DELAYED | 374.87 | 2026-08-04 | 6.00% | 7.02% | REALIZED_VOL_30D | 0.85 | 1.38 | 0.56 | 5.00% | -5.58% | -8.46% | -7.89% | BUY_SETUP_1/SELL_SETUP_5/SELL_SETUP_4 | 64.24/67.17/60.64 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 349.05 | 400.70 | Tech_Z 3.51; DQ 0.78; penalties 0.06 | L027,L028 |
| UAL | 129.12 | 2026-07-07 | DELAYED | 136.87 | 2026-08-04 | 6.00% | 15.75% | REALIZED_VOL_30D | 0.38 | 0.86 | 0.36 | 5.00% | -19.98% | -26.44% | -12.95% | BUY_SETUP_3/SELL_SETUP_8/SELL_SETUP_3 | 61.57/62.20/65.24 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 115.72 | 158.01 | Tech_Z 3.50; DQ 0.78; penalties 0.06 | L029,L030 |
| BEN | 34.67 | 2026-07-07 | DELAYED | 36.76 | 2026-08-04 | 6.00% | 8.12% | REALIZED_VOL_30D | 0.74 | 1.15 | 0.69 | 5.00% | -7.40% | -10.73% | -6.12% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_7 | 68.43/77.23/67.41 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 33.83 | 39.68 | Tech_Z 3.47; DQ 0.78; penalties 0.06 | L031,L032 |
| FTNT | 160.23 | 2026-07-07 | DELAYED | 169.84 | 2026-08-04 | 6.00% | 12.75% | REALIZED_VOL_30D | 0.47 | 0.88 | 0.35 | 5.00% | -15.03% | -20.26% | -7.54% | SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_5 | 68.08/84.56/78.00 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 148.60 | 191.09 | Tech_Z 3.45; DQ 0.78; penalties 0.06 | L033,L034 |

## Sector Table

| Sector | Top-10 Count | Paper Weight |
| --- | --- | --- |
| Financials | 2 | 20.0% |
| Health Care | 3 | 30.0% |
| Industrials | 1 | 10.0% |
| Information Technology | 4 | 40.0% |

## Excluded-Name Rationale

All names are excluded from a live portfolio because the GO gate fails on earnings-date refresh and non-price factor support. The paper basket also breaches the 8% drawdown target, so it would not be promoted even if the feed blocker were resolved without further construction work.
