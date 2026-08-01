# Quantitative Equity Selection Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-30
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The full index-union run scored 500 equities on the completed 2026-07-30 close. Final status is `NO_TRADE`: Fund_Z and Sent_Z remain unavailable, so no name reaches the three-family evidence threshold. The merged same-day package had already canonicalized all 58 matured forecasts; this run adds zero duplicate settlements and confirms due inventory and conflicts remain zero. The package publishes 20 LOW-confidence monitoring forecasts plus SPY/QQQ/SOXX for later calibration, not execution. [L001,L020,L023,L024,L046-L068]

## MoM Reflection Summary

The exact same-model July 2 cohort materially underperformed SPY through independently verified July 30 closes; reflection decisions are DROP 12, CARRY 2. Three folders tied at the target date, and the conclusion is **not invariant** across their materially different books; the same-model rule selected GPT while all alternatives remain disclosed in `02_reflection.md`. Raw canonical settlement evidence is EQ n=347 and MF n=63, while both effective sample sizes remain one. [L020-L022,L029-L045]

## Regime

| Regime | Data Quality | Key macro risk | Ledger |
| --- | --- | --- | --- |
| NEUTRAL, post-FOMC volatility/dispersion watch | DQ 0.80; Required inputs 100% | Hawkish 9-3 hold, VIX 17.09, growth/semiconductor dispersion | L005,L006,L026 |

## Core ETF Forecasts

| ETF | Entry | Price Date | Price Tag | mu | sigma | Target | Target Date | 70% CI | Confidence | Ledger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 741.69 | 2026-07-30 | DELAYED | 0.50% | 3.78% | 745.40 | 2026-08-27 | 716.28-774.52 | MEDIUM | L066 |
| QQQ | 683.55 | 2026-07-30 | DELAYED | -0.64% | 7.34% | 679.19 | 2026-08-27 | 626.98-731.40 | MEDIUM | L067 |
| SOXX | 504.53 | 2026-07-30 | DELAYED | 1.87% | 19.59% | 513.94 | 2026-08-27 | 411.17-616.72 | MEDIUM | L068 |

## Ranked Monitoring Forecasts

| Ticker | Adj | Pctl | Entry | Price Date | Price Tag | mu | sigma | Target | Target Date | 70% CI | TD9/RSI/MACD daily | Score trace | Ledger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PAYX | 0.373 | 100.00 | 116.33 | 2026-07-30 | DELAYED | 6.00% | 10.66% | 123.31 | 2026-08-27 | 110.41-136.21 | SELL_SETUP_4/62.36/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.203 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.705)×0.80−0.00=+0.373 | L046 |
| TRV | 0.364 | 99.80 | 375.99 | 2026-07-30 | DELAYED | 6.00% | 10.08% | 398.55 | 2026-08-27 | 359.13-437.97 | BUY_SETUP_1/63.4/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.141 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.748)×0.80−0.00=+0.364 | L047 |
| CTAS | 0.357 | 99.60 | 206.79 | 2026-07-30 | DELAYED | 6.00% | 10.68% | 219.20 | 2026-08-27 | 196.23-242.16 | SELL_SETUP_5/63.25/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.208 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.555)×0.80−0.00=+0.357 | L048 |
| WTW | 0.353 | 99.40 | 336.05 | 2026-07-30 | DELAYED | 6.00% | 10.09% | 356.21 | 2026-08-27 | 320.94-391.49 | SELL_SETUP_5/80.24/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.152 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.637)×0.80−0.00=+0.353 | L049 |
| ADP | 0.344 | 99.20 | 263.87 | 2026-07-30 | DELAYED | 6.00% | 10.52% | 279.70 | 2026-08-27 | 250.84-308.56 | SELL_SETUP_4/63.66/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.083 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.697)×0.80−0.00=+0.344 | L050 |
| AON | 0.335 | 99.00 | 366.57 | 2026-07-30 | DELAYED | 6.00% | 9.81% | 388.56 | 2026-08-27 | 351.18-425.95 | SELL_SETUP_4/56.99/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.016 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.761)×0.80−0.00=+0.335 | L051 |
| PCG | 0.325 | 98.80 | 17.78 | 2026-07-30 | DELAYED | 6.00% | 6.84% | 18.85 | 2026-08-27 | 17.58-20.11 | BUY_SETUP_1/57.7/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.914 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.884)×0.80−0.00=+0.325 | L052 |
| LH | 0.306 | 98.60 | 315.53 | 2026-07-30 | DELAYED | 6.00% | 8.03% | 334.46 | 2026-08-27 | 308.11-360.82 | SELL_SETUP_6/74.23/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.934 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.685)×0.80−0.00=+0.306 | L053 |
| BBY | 0.304 | 98.40 | 87.82 | 2026-07-30 | DELAYED | 6.00% | 8.79% | 93.09 | 2026-08-27 | 85.06-101.12 | SELL_SETUP_5/64.65/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.116 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.302)×0.80−0.00=+0.304 | L054 |
| INCY | 0.299 | 98.20 | 122.99 | 2026-07-30 | DELAYED | 6.00% | 11.87% | 130.37 | 2026-08-27 | 115.18-145.56 | SELL_SETUP_5/61.32/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.083 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.324)×0.80−0.00=+0.299 | L055 |
| MRSH | 0.297 | 98.00 | 191.51 | 2026-07-30 | DELAYED | 6.00% | 9.94% | 203.00 | 2026-08-27 | 183.21-222.80 | SELL_SETUP_4/64.6/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.815 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.842)×0.80−0.00=+0.297 | L056 |
| AWK | 0.289 | 97.80 | 136.81 | 2026-07-30 | DELAYED | 6.00% | 7.52% | 145.02 | 2026-08-27 | 134.32-155.72 | SELL_SETUP_5/60.12/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.735 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.940)×0.80−0.00=+0.289 | L057 |
| BXP | 0.284 | 97.60 | 71.67 | 2026-07-30 | DELAYED | 6.00% | 8.53% | 75.97 | 2026-08-27 | 69.61-82.33 | SELL_SETUP_5/63.93/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.895 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.574)×0.80−0.00=+0.284 | L058 |
| BRO | 0.280 | 97.39 | 70.87 | 2026-07-30 | DELAYED | 6.00% | 12.34% | 75.12 | 2026-08-27 | 66.03-84.22 | SELL_SETUP_4/58.37/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.858 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.613)×0.80−0.00=+0.280 | L059 |
| SJM | 0.279 | 97.19 | 122.21 | 2026-07-30 | DELAYED | 6.00% | 10.19% | 129.54 | 2026-08-27 | 116.59-142.50 | SELL_SETUP_9/61.72/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.806 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.714)×0.80−0.00=+0.279 | L060 |
| BAX | 0.279 | 96.99 | 26.75 | 2026-07-30 | DELAYED | 6.00% | 14.01% | 28.36 | 2026-08-27 | 24.46-32.25 | SELL_SETUP_5/75.93/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.205 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×-0.087)×0.80−0.00=+0.279 | L061 |
| AAPL | 0.275 | 96.79 | 333.43 | 2026-07-30 | DELAYED | 6.00% | 9.45% | 353.44 | 2026-08-27 | 320.65-386.22 | SELL_SETUP_5/61.66/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.072 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.148)×0.80−0.00=+0.275 | L062 |
| SYK | 0.270 | 96.59 | 348.04 | 2026-07-30 | DELAYED | 6.00% | 11.93% | 368.92 | 2026-08-27 | 325.74-412.11 | SELL_SETUP_5/62.65/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.919 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.416)×0.80−0.00=+0.270 | L063 |
| PM | 0.267 | 96.39 | 192.00 | 2026-07-30 | DELAYED | 6.00% | 9.67% | 203.52 | 2026-08-27 | 184.21-222.83 | BUY_SETUP_1/54.74/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.823 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.582)×0.80−0.00=+0.267 | L064 |
| RTX | 0.266 | 96.19 | 214.38 | 2026-07-30 | DELAYED | 6.00% | 9.47% | 227.24 | 2026-08-27 | 206.13-248.35 | SELL_SETUP_7/69.69/ABOVE_SIGNAL | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.813 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.587)×0.80−0.00=+0.266 | L065 |

## Portfolio Analytics / No-Trade Rationale

No weights are proposed. Factor convergence fails before construction; the equal-weight diagnostic also has beta -0.389, average correlation 0.305, 95th-pctl drawdown 8.87%, and largest-sector share 25.00%. [L019]

## Assumptions and Limitations

Data mode is `DELAYED`; only completed July 30 bars are used. The run's audit continuation completed on August 1, and all retrieval timestamps are retained rather than backdated. Fundamental, sentiment, options, short-interest, analyst-revision, and ownership feeds are not production-ready. Normal-distribution assumptions underpin parametric VaR/CVaR and CI. The risk-free ratio input is the sourced 3.83% three-month Treasury yield and is aligned exactly across manifests and calculations. [L002,L003,L006,L016,L017,L023-L025]

## Next Scheduled Review

The next scheduled full review is 2026-07-31 at 07:27 ET. This run defers its single Track A factor-weight proposal because eff_n remains below the evidence gate.
