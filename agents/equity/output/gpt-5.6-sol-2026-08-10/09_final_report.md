══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-10
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════

## Executive Summary

The full 515-name index union completed with 511 scored equities and all five Required inputs grounded. Twenty Technical/Macro monitors and three core ETFs carry settleable forecasts, while 200 matured predictions were settled and the due queue fell to zero. No equity is investable because only two of four families are available, the maximum family share is 66.67%, and DQ is 0.80. The naive monitor sleeve also breaches the 8% drawdown and 30% sector caps, so the risk committee approved `NO_TRADE`.

## MoM Reflection Summary

The selected `CROSS_MODEL_BASELINE`, `gpt-5-2026-07-13`, produced 50.00% equity direction
hits, 85.00% CI coverage, -1.37% mean alpha and mean z -0.263; its ETF block hit 1/3
directions and 3/3 intervals. Exact-date Claude and Gemini alternatives preserve the
at-or-below-50% hit-rate and negative-alpha conclusion, but the magnitude differs [L018].

## Regime

| Regime | Data Quality | Evidence | Key Macro Risk | Rows |
| --- | --- | --- | --- | --- |
| BULL | 0.80 | SPY above MA20/MA50; +3.18%/+4.40% 20d/60d momentum; VIX 15.46 | FOMC Sep 15-16 inside 42d horizon | L004-L005,L021,L027,L601 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | $773.03 | 2.00% | 3.75% | $788.49 | $758.38–$818.60 | MEDIUM |
| QQQ | $720.87 | 3.42% | 7.23% | $745.52 | $691.34–$799.71 | MEDIUM |
| SOXX | $529.39 | 6.95% | 17.78% | $566.19 | $468.29–$664.10 | MEDIUM |

Target date is September 7; because it is Labor Day, later settlement uses September 4 under
`WEEKEND_TARGET` [L029].

## Ranked Monitoring Candidates

| Ticker | Sector | Rank | Pctl | Adj | Trace | Risk | TD9 D/W/M | MACD D/W/M | mu | sigma | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NTAP | Technology | 1 | 99.80 | 0.4401 | T 1.39; M 0.88; DQ .80 | S 0.44; IR 0.18; DD -15.81% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 12.88% | LOW |
| DXCM | Health Care | 2 | 99.61 | 0.3900 | T 1.34; M 0.58; DQ .80 | S 0.37; IR 0.38; DD -13.86% | SELL_SETUP_1/SELL_SETUP_5/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 15.44% | LOW |
| CRL | Health Care | 3 | 99.41 | 0.3898 | T 1.42; M 0.41; DQ .80 | S 0.41; IR 0.33; DD -6.38% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 13.73% | LOW |
| ABNB | Consumer Discretionary | 4 | 99.22 | 0.3579 | T 1.54; M -0.11; DQ .80 | S 0.34; IR 0.34; DD -7.63% | SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 16.80% | LOW |
| BAX | Health Care | 5 | 99.02 | 0.3549 | T 1.37; M 0.21; DQ .80 | S 0.40; IR 0.38; DD -7.19% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 14.33% | LOW |
| DASH | Consumer Discretionary | 6 | 98.83 | 0.3367 | T 1.12; M 0.56; DQ .80 | S 0.46; IR 0.26; DD -13.26% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 12.42% | LOW |
| REGN | Health Care | 7 | 98.63 | 0.3144 | T 0.87; M 0.88; DQ .80 | S 0.60; IR 0.52; DD -15.61% | SELL_SETUP_9/SELL_SETUP_8/SELL_SETUP_1 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 9.49% | LOW |
| WSM | Consumer Discretionary | 8 | 98.43 | 0.3128 | T 1.19; M 0.23; DQ .80 | S 0.62; IR 0.42; DD -9.79% | SELL_SETUP_6/SELL_SETUP_3/SELL_SETUP_3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 9.11% | LOW |
| VEEV | Technology | 9 | 98.24 | 0.3101 | T 0.98; M 0.63; DQ .80 | S 0.50; IR 0.42; DD -18.82% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 11.37% | LOW |
| COO | Health Care | 10 | 98.04 | 0.3090 | T 0.95; M 0.67; DQ .80 | S 0.68; IR 0.71; DD -7.67% | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 6.00% | 8.42% | LOW |
| J | Industrials | 11 | 97.85 | 0.3073 | T 1.20; M 0.15; DQ .80 | S 0.72; IR 0.60; DD -6.54% | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 7.92% | LOW |
| NTRS | Finance | 12 | 97.65 | 0.3069 | T 0.95; M 0.66; DQ .80 | S 0.90; IR 0.84; DD -7.05% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_9 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 6.31% | LOW |
| TSCO | Consumer Discretionary | 13 | 97.46 | 0.3004 | T 1.02; M 0.46; DQ .80 | S 0.59; IR 0.58; DD -8.99% | SELL_SETUP_6/SELL_SETUP_2/BUY_SETUP_9 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 9.58% | LOW |
| CPAY | Consumer Discretionary | 14 | 97.26 | 0.2973 | T 0.86; M 0.76; DQ .80 | S 0.74; IR 0.61; DD -10.52% | SELL_SETUP_9/SELL_SETUP_5/SELL_SETUP_5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 7.65% | LOW |
| PFE | Health Care | 15 | 97.06 | 0.2951 | T 0.84; M 0.77; DQ .80 | S 1.05; IR 1.04; DD -9.69% | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_1 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 5.41% | LOW |
| TPR | Consumer Discretionary | 16 | 96.87 | 0.2914 | T 1.31; M 0.65; DQ .80 | S 0.66; IR 0.52; DD -10.35% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 8.56% | LOW |
| ZS | Technology | 17 | 96.67 | 0.2867 | T 0.66; M 1.06; DQ .80 | S 0.41; IR 0.17; DD -32.94% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 13.77% | LOW |
| EXPE | Consumer Discretionary | 18 | 96.48 | 0.2833 | T 1.21; M -0.06; DQ .80 | S 0.47; IR 0.44; DD -5.25% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 6.00% | 12.23% | LOW |
| BX | Finance | 19 | 96.28 | 0.2822 | T 0.80; M 0.75; DQ .80 | S 0.56; IR 0.35; DD -11.64% | SELL_SETUP_6/SELL_SETUP_7/SELL_SETUP_3 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 10.11% | LOW |
| WTW | Finance | 20 | 96.09 | 0.2766 | T 1.06; M 0.19; DQ .80 | S 0.59; IR 0.76; DD -4.15% | SELL_SETUP_9/SELL_SETUP_8/SELL_SETUP_2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 6.00% | 9.58% | LOW |

## Portfolio Analytics / No-Trade Rationale

No executable portfolio is proposed. The equal-weight diagnostic has beta 0.534, average
correlation 0.187, sigma 5.59%, and 95th-percentile
drawdown 9.22%; Consumer Discretionary is 35%. Correlation passes, but evidence
breadth, DQ, drawdown and sector constraints fail [L021-L026,L030].

## Assumptions and Limitations

- Completed closes are delayed research inputs, not executable quotes.
- Adjusted histories drive return analytics; raw prices drive entries and settlements.
- Fund_Z, Sent_Z, spread tape, options IV and analyst-revision feeds are unavailable.
- Target/CI calculations assume the rules.md normal approximation and fixed calibration table.
- Weighted rank IC is negative and `eff_n=2`; calibration confidence is capped and changes are deferred.

## Next Scheduled Review

Next daily run after the 2026-08-11 close; re-scan settlements, refresh all market inputs, and
leave parameter weights unchanged until `eff_n>=3` permits Track A validation.
