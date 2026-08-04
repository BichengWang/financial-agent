# 07 — Portfolio Proposal — 2026-08-03

**Final status: `HALTED`; data mode: `DELAYED_PARTIAL`.** No portfolio was approved or
constructed. All values below are provisional pre-halt diagnostics only.

## Pre-halt constraint diagnostics

Hard Halt criterion #3 stops construction because unresolved Required-input earnings dates
and resulting event penalties affect more than 20% of the top-ranked set. No executable
weights exist. Before the halt, the full scoreable universe's 20-name, 5%-cap beta range was
-1.059 to +3.950 and intersected the 0.90–1.10 band; that observation does not cure the
input-integrity failure or authorize a portfolio.

## Equal-weight monitoring diagnostic (not a portfolio)

The equal-weight basket is shown only to preserve computations completed before the halt. It
is not an approved weight vector. Portfolio analytics that require executable weights and a
portfolio expected-return thesis are explicitly `N/A — HALTED`; this does not imply missing
price history and must not be read as a recommendation.

| Metric | Value | Limit / requirement | Result |
| --- | --- | --- | --- |
| Executable weights | N/A — construction stopped at Hard Halt #3 | Required | HALTED |
| Expected beta | +0.223 (equal-weight diagnostic) | 0.90–1.10 | FAIL — diagnostic basket only |
| Average pairwise correlation | 0.174 (60-session equal-weight diagnostic) | <0.45 | PASS — diagnostic only |
| Portfolio sigma, 1 month | 4.70% (equal-weight diagnostic) | Required analytic | PRE-HALT ONLY |
| Expected Sharpe | N/A — no approved weights or portfolio expected return | Required analytic | HALTED |
| Expected Sortino | N/A — no approved weights or portfolio downside-return series | Required analytic | HALTED |
| Expected Information Ratio | N/A — no approved weights or portfolio alpha thesis | Required analytic | HALTED |
| Tracking error / residual sigma | N/A — no approved weights | Required analytic | HALTED |
| Factor exposure summary | N/A — no approved weights; provisional evidence has Technical and Macro only | Required analytic | HALTED |
| VaR95 | N/A — no approved weights or executable portfolio return distribution | Required analytic | HALTED |
| CVaR95 | N/A — no approved weights or executable portfolio return distribution | Required analytic | HALTED |
| 95th-pctl 1-month drawdown | 7.76% (equal-weight diagnostic; `1.65 × 4.70%`, normality assumption) | ≤8% | PASS — diagnostic only |
| Kelly cap binding | 20/20 provisional names: bounded `0.25 × Kelly = 5.00%`; pre-cap range 59.78%–492.22% | ≤5% per name | CAP_BINDING; no weights proposed |

| Sector | Pre-halt equal-weight diagnostic share | 30% cap |
| --- | --- | --- |
| Consumer Discretionary | 25.00% | PASS — diagnostic only |
| Finance | 25.00% | PASS — diagnostic only |
| Health Care | 20.00% | PASS — diagnostic only |
| Industrials | 20.00% | PASS — diagnostic only |
| Energy | 5.00% | PASS — diagnostic only |
| Technology | 5.00% | PASS — diagnostic only |

## Pre-halt per-name diagnostics — withdrawn, not recommendations

| Ticker | Entry | Price date | Tag | Target | Target date | mu | sigma | Sigma source | Sharpe | Sortino | IR | Kelly 0.25 (bounded) | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DXCM | $87.31 | 2026-08-03 | HISTORICAL | $92.55 | 2026-08-31 | +6.00% | 15.60% | REALIZED_VOL_30D | 0.36 | 0.86 | 0.39 | 5.00% (raw .25=68.36%; CAP_BINDING) | -19.73% | -26.13% | -13.86% | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_2 | 72.6/67.8/53.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $78.39 | $106.71 | Tech +1.37; Macro +0.57; DQ .80; pen 0.00 | L-PX-DXCM,L-TI-DXCM,L-RM-DXCM,L-SC-DXCM |
| BEN | $35.24 | 2026-08-03 | HISTORICAL | $37.35 | 2026-08-31 | +6.00% | 8.26% | REALIZED_VOL_30D | 0.69 | 1.05 | 0.55 | 5.00% (raw .25=200.34%; CAP_BINDING) | -7.63% | -11.02% | -6.42% | SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_8 | 66.1/74.3/71.8 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | $34.33 | $40.38 | Tech +1.09; Macro +0.95; DQ .80; pen 0.00 | L-PX-BEN,L-TI-BEN,L-RM-BEN,L-SC-BEN |
| BMY | $65.47 | 2026-08-03 | HISTORICAL | $69.40 | 2026-08-31 | +6.00% | 8.81% | REALIZED_VOL_30D | 0.65 | 1.10 | 0.77 | 5.00% (raw .25=234.32%; CAP_BINDING) | -8.54% | -12.16% | -9.32% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2 | 71.8/68.5/65.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $63.40 | $75.40 | Tech +1.31; Macro +0.38; DQ .80; pen 0.00 | L-PX-BMY,L-TI-BMY,L-RM-BMY,L-SC-BMY |
| WTW | $341.63 | 2026-08-03 | HISTORICAL | $362.13 | 2026-08-31 | +6.00% | 10.01% | REALIZED_VOL_30D | 0.57 | 1.84 | 0.73 | 5.00% (raw .25=198.85%; CAP_BINDING) | -10.52% | -14.63% | -6.18% | SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2 | 81.6/68.4/60.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $326.55 | $397.71 | Tech +1.25; Macro +0.32; DQ .80; pen 0.00 | L-PX-WTW,L-TI-WTW,L-RM-WTW,L-SC-WTW |
| BAX | $28.10 | 2026-08-03 | HISTORICAL | $29.79 | 2026-08-31 | +6.00% | 14.47% | REALIZED_VOL_30D | 0.39 | 0.89 | 0.38 | 5.00% (raw .25=75.28%; CAP_BINDING) | -17.88% | -23.82% | -7.19% | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_3 | 76.4/73.6/51.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $25.56 | $34.02 | Tech +1.30; Macro +0.07; DQ .80; pen 0.00 | L-PX-BAX,L-TI-BAX,L-RM-BAX,L-SC-BAX |
| PCAR | $132.06 | 2026-08-03 | HISTORICAL | $139.98 | 2026-08-31 | +6.00% | 9.05% | REALIZED_VOL_30D | 0.63 | 1.39 | 0.50 | 5.00% (raw .25=157.76%; CAP_BINDING) | -8.93% | -12.64% | -4.76% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 59.7/66.7/66.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $127.55 | $152.41 | Tech +0.93; Macro +0.65; DQ .80; pen 0.00 | L-PX-PCAR,L-TI-PCAR,L-RM-PCAR,L-SC-PCAR |
| TGT | $149.35 | 2026-08-03 | HISTORICAL | $158.31 | 2026-08-31 | +6.00% | 10.20% | REALIZED_VOL_30D | 0.56 | 0.94 | 0.61 | 5.00% (raw .25=147.72%; CAP_BINDING) | -10.83% | -15.01% | -10.69% | SELL_SETUP_6/SELL_SETUP_2/SELL_SETUP_9 | 69.5/68.2/65.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $142.47 | $174.16 | Tech +1.11; Macro +0.27; DQ .80; pen 0.00 | L-PX-TGT,L-TI-TGT,L-RM-TGT,L-SC-TGT |
| ADP | $269.78 | 2026-08-03 | HISTORICAL | $285.97 | 2026-08-31 | +6.00% | 10.53% | REALIZED_VOL_30D | 0.54 | 1.07 | 0.81 | 5.00% (raw .25=219.14%; CAP_BINDING) | -11.38% | -15.70% | -7.49% | SELL_SETUP_6/SELL_SETUP_7/SELL_SETUP_3 | 66.8/66.6/56.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $256.41 | $315.52 | Tech +1.14; Macro +0.01; DQ .80; pen 0.00 | L-PX-ADP,L-TI-ADP,L-RM-ADP,L-SC-ADP |
| KKR | $106.56 | 2026-08-03 | HISTORICAL | $112.95 | 2026-08-31 | +6.00% | 10.59% | REALIZED_VOL_30D | 0.54 | 0.98 | 0.41 | 5.00% (raw .25=118.81%; CAP_BINDING) | -11.48% | -15.82% | -13.08% | SELL_SETUP_1/SELL_SETUP_6/SELL_SETUP_3 | 65.8/55.3/49.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $101.21 | $124.69 | Tech +0.85; Macro +0.56; DQ .80; pen 0.00 | L-PX-KKR,L-TI-KKR,L-RM-KKR,L-SC-KKR |
| ROST | $252.91 | 2026-08-03 | HISTORICAL | $268.08 | 2026-08-31 | +6.00% | 8.99% | REALIZED_VOL_30D | 0.63 | 0.72 | 0.56 | 5.00% (raw .25=140.53%; CAP_BINDING) | -8.84% | -12.53% | -13.03% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_9 | 71.0/69.1/76.4 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | $244.43 | $291.74 | Tech +0.90; Macro +0.35; DQ .80; pen 0.00 | L-PX-ROST,L-TI-ROST,L-RM-ROST,L-SC-ROST |
| MA | $570.97 | 2026-08-03 | HISTORICAL | $605.23 | 2026-08-31 | +6.00% | 6.95% | REALIZED_VOL_30D | 0.82 | 2.09 | 0.93 | 5.00% (raw .25=347.74%; CAP_BINDING) | -5.46% | -8.31% | -6.77% | SELL_SETUP_6/SELL_SETUP_7/SELL_SETUP_2 | 67.8/65.3/60.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $563.98 | $646.48 | Tech +0.82; Macro +0.51; DQ .80; pen 0.00 | L-PX-MA,L-TI-MA,L-RM-MA,L-SC-MA |
| RTX | $216.65 | 2026-08-03 | HISTORICAL | $229.65 | 2026-08-31 | +6.00% | 8.69% | REALIZED_VOL_30D | 0.65 | 1.43 | 0.72 | 5.00% (raw .25=210.79%; CAP_BINDING) | -8.34% | -11.90% | -5.58% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 71.5/68.5/75.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $210.07 | $249.23 | Tech +0.79; Macro +0.51; DQ .80; pen 0.00 | L-PX-RTX,L-TI-RTX,L-RM-RTX,L-SC-RTX |
| GRMN | $304.76 | 2026-08-03 | HISTORICAL | $323.05 | 2026-08-31 | +6.00% | 15.54% | REALIZED_VOL_30D | 0.37 | 1.30 | 0.46 | 5.00% (raw .25=92.67%; CAP_BINDING) | -19.65% | -26.02% | -6.86% | SELL_SETUP_6/SELL_SETUP_6/SELL_SETUP_2 | 79.9/73.1/69.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $273.78 | $372.31 | Tech +1.06; Macro -0.03; DQ .80; pen 0.00 | L-PX-GRMN,L-TI-GRMN,L-RM-GRMN,L-SC-GRMN |
| VLO | $307.54 | 2026-08-03 | HISTORICAL | $325.99 | 2026-08-31 | +6.00% | 11.01% | REALIZED_VOL_30D | 0.52 | 1.44 | 0.65 | 5.00% (raw .25=156.85%; CAP_BINDING) | -12.17% | -16.68% | -9.62% | SELL_SETUP_3/SELL_SETUP_7/SELL_SETUP_9 | 62.0/71.1/81.1 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $290.78 | $361.21 | Tech +0.97; Macro +0.13; DQ .80; pen 0.00 | L-PX-VLO,L-TI-VLO,L-RM-VLO,L-SC-VLO |
| IR | $87.78 | 2026-08-03 | HISTORICAL | $93.05 | 2026-08-31 | +6.00% | 10.76% | REALIZED_VOL_30D | 0.53 | 1.21 | 0.43 | 5.00% (raw .25=115.22%; CAP_BINDING) | -11.76% | -16.17% | -11.54% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 65.3/59.9/54.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $83.22 | $102.87 | Tech +0.79; Macro +0.47; DQ .80; pen 0.00 | L-PX-IR,L-TI-IR,L-RM-IR,L-SC-IR |
| COO | $74.23 | 2026-08-03 | HISTORICAL | $78.68 | 2026-08-31 | +6.00% | 8.90% | REALIZED_VOL_30D | 0.64 | 1.05 | 0.73 | 5.00% (raw .25=197.61%; CAP_BINDING) | -8.69% | -12.34% | -7.67% | SELL_SETUP_5/SELL_SETUP_1/SELL_SETUP_2 | 63.3/55.8/46.2 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | $71.81 | $85.56 | Tech +0.85; Macro +0.35; DQ .80; pen 0.00 | L-PX-COO,L-TI-COO,L-RM-COO,L-SC-COO |
| VEEV | $206.25 | 2026-08-03 | HISTORICAL | $218.62 | 2026-08-31 | +6.00% | 12.98% | REALIZED_VOL_30D | 0.44 | 1.01 | 0.45 | 5.00% (raw .25=83.25%; CAP_BINDING) | -15.42% | -20.74% | -18.82% | SELL_SETUP_6/SELL_SETUP_6/SELL_SETUP_2 | 63.8/56.8/47.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $190.78 | $246.47 | Tech +0.89; Macro +0.25; DQ .80; pen 0.00 | L-PX-VEEV,L-TI-VEEV,L-RM-VEEV,L-SC-VEEV |
| HIG | $142.90 | 2026-08-03 | HISTORICAL | $151.47 | 2026-08-31 | +6.00% | 6.61% | REALIZED_VOL_30D | 0.86 | 1.62 | 1.20 | 5.00% (raw .25=492.22%; CAP_BINDING) | -4.91% | -7.63% | -7.43% | BUY_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 58.6/61.0/65.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $141.64 | $161.30 | Tech +0.78; Macro +0.47; DQ .80; pen 0.00 | L-PX-HIG,L-TI-HIG,L-RM-HIG,L-SC-HIG |
| ULTA | $534.41 | 2026-08-03 | HISTORICAL | $566.47 | 2026-08-31 | +6.00% | 9.57% | REALIZED_VOL_30D | 0.59 | 0.77 | 0.59 | 5.00% (raw .25=156.65%; CAP_BINDING) | -9.80% | -13.72% | -14.39% | SELL_SETUP_5/SELL_SETUP_2/BUY_SETUP_6 | 72.0/53.0/53.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $513.27 | $619.68 | Tech +0.84; Macro +0.35; DQ .80; pen 0.00 | L-PX-ULTA,L-TI-ULTA,L-RM-ULTA,L-SC-ULTA |
| ARES | $138.57 | 2026-08-03 | HISTORICAL | $146.88 | 2026-08-31 | +6.00% | 13.69% | REALIZED_VOL_30D | 0.42 | 0.79 | 0.25 | 5.00% (raw .25=59.78%; CAP_BINDING) | -16.59% | -22.20% | -20.28% | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_3 | 69.3/57.4/51.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $127.16 | $166.61 | Tech +0.87; Macro +0.28; DQ .80; pen 0.00 | L-PX-ARES,L-TI-ARES,L-RM-ARES,L-SC-ARES |

## Correlation matrix — 60-session daily returns

| Ticker | DXCM | BEN | BMY | WTW | BAX | PCAR | TGT | ADP | KKR | ROST | MA | RTX | GRMN | VLO | IR | COO | VEEV | HIG | ULTA | ARES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DXCM | 1.00 | -0.01 | 0.18 | 0.33 | 0.29 | 0.04 | 0.17 | 0.48 | 0.10 | 0.09 | 0.30 | 0.01 | 0.10 | 0.05 | 0.17 | 0.25 | 0.39 | 0.13 | 0.26 | 0.17 |
| BEN | -0.01 | 1.00 | 0.14 | 0.12 | 0.22 | 0.40 | -0.18 | -0.10 | 0.63 | 0.01 | 0.11 | 0.35 | -0.02 | -0.17 | 0.36 | -0.09 | 0.02 | -0.02 | -0.02 | 0.61 |
| BMY | 0.18 | 0.14 | 1.00 | 0.38 | 0.45 | -0.02 | 0.21 | 0.18 | 0.16 | 0.19 | 0.41 | 0.37 | 0.05 | -0.05 | 0.13 | 0.48 | 0.15 | 0.39 | 0.17 | 0.09 |
| WTW | 0.33 | 0.12 | 0.38 | 1.00 | 0.59 | -0.03 | 0.12 | 0.60 | 0.22 | 0.07 | 0.67 | 0.22 | 0.17 | 0.09 | 0.06 | 0.33 | 0.43 | 0.48 | 0.29 | 0.12 |
| BAX | 0.29 | 0.22 | 0.45 | 0.59 | 1.00 | 0.22 | 0.40 | 0.26 | 0.43 | 0.18 | 0.45 | 0.13 | 0.33 | -0.12 | 0.37 | 0.55 | 0.20 | 0.23 | 0.49 | 0.32 |
| PCAR | 0.04 | 0.40 | -0.02 | -0.03 | 0.22 | 1.00 | -0.01 | -0.20 | 0.43 | 0.12 | -0.05 | 0.14 | 0.11 | -0.06 | 0.66 | 0.10 | -0.09 | -0.03 | 0.14 | 0.37 |
| TGT | 0.17 | -0.18 | 0.21 | 0.12 | 0.40 | -0.01 | 1.00 | 0.06 | 0.02 | 0.33 | 0.02 | -0.13 | 0.09 | -0.12 | 0.07 | 0.31 | 0.09 | -0.00 | 0.41 | 0.06 |
| ADP | 0.48 | -0.10 | 0.18 | 0.60 | 0.26 | -0.20 | 0.06 | 1.00 | 0.01 | 0.04 | 0.59 | 0.07 | 0.28 | 0.14 | -0.07 | 0.29 | 0.75 | 0.41 | 0.10 | 0.06 |
| KKR | 0.10 | 0.63 | 0.16 | 0.22 | 0.43 | 0.43 | 0.02 | 0.01 | 1.00 | 0.21 | 0.22 | 0.27 | 0.10 | -0.33 | 0.54 | 0.17 | 0.08 | -0.10 | 0.21 | 0.86 |
| ROST | 0.09 | 0.01 | 0.19 | 0.07 | 0.18 | 0.12 | 0.33 | 0.04 | 0.21 | 1.00 | 0.01 | -0.07 | 0.18 | -0.17 | 0.12 | 0.05 | 0.05 | 0.03 | 0.25 | 0.19 |
| MA | 0.30 | 0.11 | 0.41 | 0.67 | 0.45 | -0.05 | 0.02 | 0.59 | 0.22 | 0.01 | 1.00 | 0.28 | 0.12 | -0.03 | 0.20 | 0.48 | 0.52 | 0.37 | 0.17 | 0.09 |
| RTX | 0.01 | 0.35 | 0.37 | 0.22 | 0.13 | 0.14 | -0.13 | 0.07 | 0.27 | -0.07 | 0.28 | 1.00 | -0.00 | -0.32 | 0.25 | 0.19 | 0.02 | 0.19 | -0.05 | 0.29 |
| GRMN | 0.10 | -0.02 | 0.05 | 0.17 | 0.33 | 0.11 | 0.09 | 0.28 | 0.10 | 0.18 | 0.12 | -0.00 | 1.00 | -0.15 | 0.24 | 0.20 | 0.22 | 0.20 | 0.30 | 0.17 |
| VLO | 0.05 | -0.17 | -0.05 | 0.09 | -0.12 | -0.06 | -0.12 | 0.14 | -0.33 | -0.17 | -0.03 | -0.32 | -0.15 | 1.00 | -0.29 | -0.25 | 0.11 | -0.01 | -0.12 | -0.30 |
| IR | 0.17 | 0.36 | 0.13 | 0.06 | 0.37 | 0.66 | 0.07 | -0.07 | 0.54 | 0.12 | 0.20 | 0.25 | 0.24 | -0.29 | 1.00 | 0.37 | 0.03 | 0.06 | 0.42 | 0.39 |
| COO | 0.25 | -0.09 | 0.48 | 0.33 | 0.55 | 0.10 | 0.31 | 0.29 | 0.17 | 0.05 | 0.48 | 0.19 | 0.20 | -0.25 | 0.37 | 1.00 | 0.18 | 0.43 | 0.36 | 0.08 |
| VEEV | 0.39 | 0.02 | 0.15 | 0.43 | 0.20 | -0.09 | 0.09 | 0.75 | 0.08 | 0.05 | 0.52 | 0.02 | 0.22 | 0.11 | 0.03 | 0.18 | 1.00 | 0.26 | 0.13 | 0.10 |
| HIG | 0.13 | -0.02 | 0.39 | 0.48 | 0.23 | -0.03 | -0.00 | 0.41 | -0.10 | 0.03 | 0.37 | 0.19 | 0.20 | -0.01 | 0.06 | 0.43 | 0.26 | 1.00 | 0.26 | -0.11 |
| ULTA | 0.26 | -0.02 | 0.17 | 0.29 | 0.49 | 0.14 | 0.41 | 0.10 | 0.21 | 0.25 | 0.17 | -0.05 | 0.30 | -0.12 | 0.42 | 0.36 | 0.13 | 0.26 | 1.00 | 0.10 |
| ARES | 0.17 | 0.61 | 0.09 | 0.12 | 0.32 | 0.37 | 0.06 | 0.06 | 0.86 | 0.19 | 0.09 | 0.29 | 0.17 | -0.30 | 0.39 | 0.08 | 0.10 | -0.11 | 0.10 | 1.00 |

## Halt and exclusion rationale

Construction stopped before an executable proposal because unresolved Required-input
earnings dates and event penalties exceed the 20% Hard Halt threshold. Separately, every
provisional name fails the 3-of-4-family, max-family-contribution, and completeness gates.
Geometry cannot cure either defect; no revision pass or weight optimization was authorized.
