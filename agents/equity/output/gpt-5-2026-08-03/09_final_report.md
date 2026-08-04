# 09 — Final Report — 2026-08-03

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-03
Run Status: HALTED
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

All 88 due predictions settled with completed closes and current-run two-source checks,
leaving due=0 and conflicts=0. The 515-name index union produced 511 scoreable equities,
and 20 names reached pre-halt ranking before the Required-input breach was recognized.
The six-signal `Tech_Z` deduplication was applied, but 15 of those 20 names lack a confirmed
or cadence-estimated next earnings date. That 75% unresolved-critical-input rate exceeds
Hard Halt Criterion 3's 20% threshold, so the final status is **`HALTED`**. All equity rankings below are pre-halt diagnostics, not valid predictions or trades; the
three independently grounded ETF research forecasts remain ledgered and non-executable.

## MoM reflection summary

Exact-date same-model baseline `gpt-5-2026-07-06` was selected from a two-folder tie; the
alternative `claude-fable-5-2026-07-06` is disclosed in `02`. Selected-book hit rate is
20.00%, mean alpha -11.38%, and mean z
-0.812. The 6.09% hit-rate spread makes the conclusion
**invariant** across the tie.

## Regime

| Field | Value | Ledger |
| --- | --- | --- |
| Regime | BULL | L-TI-SPY, L-MAC-VIX, L-MAC-VIX60 |
| Data mode | DELAYED_PARTIAL; 15/20 pre-halt ranked names lack a confirmed/cadence-estimated next earnings date | L-EA-* |
| Data quality | 0.80; two factor families unavailable | L-UNA-FUND, L-UNA-SENT |
| Key risk | Hard Halt Criterion 3 triggered; weighted rank IC -0.0879 | L-SET-SUM, L-EA-* |

## Core ETF market forecasts

These independently grounded market forecasts remain valid research records, but the
`HALTED` run status makes them non-executable.

| ETF | Entry | Trend 20d/50d | 30d RVol trend | Drawdown from 60d high | Beta | mu | sigma | Target | 70% CI | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | $757.67 | ABOVE/ABOVE | 3.83% vs 4.24%; falling | -4.49% | +1.000 | +2.00% | 3.83% | $772.82 | $742.68–$802.97 | MEDIUM |
| QQQ | $700.07 | ABOVE/BELOW | 7.30% vs 7.63%; falling | -11.22% | +1.706 | +1.91% | 7.30% | $713.46 | $660.30–$766.61 | MEDIUM |
| SOXX | $507.68 | BELOW/BELOW | 18.92% vs 19.31%; falling | -29.01% | +3.530 | +5.56% | 18.92% | $535.91 | $436.03–$635.78 | MEDIUM |

## Pre-halt ranked diagnostics (top 10 of 20)

These rows are retained to audit work completed before the hard stop. They are not valid
current-run predictions, a monitoring sleeve, or trade recommendations.

| Rank | Ticker | Sector | Entry | Adj Score | Pctl | Score trace | Beta | mu | sigma | Target | Technical | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DXCM | Health Care | $87.31 | +0.3970 | 99.90 | Tech +1.37; Macro +0.57 | +0.21 | +6.00% | 15.60% | $92.55 | SELL_SETUP_5; RSI 72.6; ABOVE_SIGNAL | MEDIUM |
| 2 | BEN | Finance | $35.24 | +0.3768 | 99.71 | Tech +1.09; Macro +0.95 | +1.09 | +6.00% | 8.26% | $37.35 | SELL_SETUP_7; RSI 66.1; BULLISH_CROSS | MEDIUM |
| 3 | BMY | Health Care | $65.47 | +0.3593 | 99.51 | Tech +1.31; Macro +0.38 | -0.20 | +6.00% | 8.81% | $69.40 | SELL_SETUP_9; RSI 71.8; ABOVE_SIGNAL | MEDIUM |
| 4 | WTW | Finance | $341.63 | +0.3384 | 99.32 | Tech +1.25; Macro +0.32 | -0.37 | +6.00% | 10.01% | $362.13 | SELL_SETUP_7; RSI 81.6; ABOVE_SIGNAL | MEDIUM |
| 5 | BAX | Health Care | $28.10 | +0.3215 | 99.12 | Tech +1.30; Macro +0.07 | +0.64 | +6.00% | 14.47% | $29.79 | SELL_SETUP_7; RSI 76.4; ABOVE_SIGNAL | MEDIUM |
| 6 | PCAR | Consumer Discretionary | $132.06 | +0.3016 | 98.92 | Tech +0.93; Macro +0.65 | +1.03 | +6.00% | 9.05% | $139.98 | BUY_SETUP_2; RSI 59.7; ABOVE_SIGNAL | MEDIUM |
| 7 | TGT | Consumer Discretionary | $149.35 | +0.2984 | 98.73 | Tech +1.11; Macro +0.27 | -0.16 | +6.00% | 10.20% | $158.31 | SELL_SETUP_6; RSI 69.5; ABOVE_SIGNAL | MEDIUM |
| 8 | ADP | Industrials | $269.78 | +0.2742 | 98.53 | Tech +1.14; Macro +0.01 | -0.74 | +6.00% | 10.53% | $285.97 | SELL_SETUP_6; RSI 66.8; ABOVE_SIGNAL | MEDIUM |
| 9 | KKR | Finance | $106.56 | +0.2711 | 98.34 | Tech +0.85; Macro +0.56 | +1.27 | +6.00% | 10.59% | $112.95 | SELL_SETUP_1; RSI 65.8; ABOVE_SIGNAL | MEDIUM |
| 10 | ROST | Consumer Discretionary | $252.91 | +0.2596 | 98.14 | Tech +0.90; Macro +0.35 | +0.22 | +6.00% | 8.99% | $268.08 | SELL_SETUP_7; RSI 71.0; ABOVE_SIGNAL | MEDIUM |

## Halt rationale

| # | Evidence threshold | Result |
| --- | --- | --- |
| 1 | Adjusted-score percentile ≥80 | PRE-HALT DIAGNOSTIC — 102/511 names |
| 2 | ≥3 of 4 families non-negative | FAIL — only Technical and Macro are available |
| 3 | No family >50% of conviction | FAIL — Technical is 66.7% of available family weight |
| 4 | Data completeness ≥85% | FAIL — DQ multiplier is 0.80 |
| 5 | No hard stop | FAIL — 15/20 pre-halt ranked names have an unresolved Required earnings-date input |

Hard Halt Criterion 3 applies because unresolved critical inputs affect 75% of the pre-halt
set. No equity prediction set or portfolio is valid; retained equity analytics are audit-only
diagnostics, while the three ETF research forecasts remain in `15`.

## Assumptions and limitations

1. Fifteen of 20 pre-halt ranked names lack a confirmed or cadence-estimated next earnings date.
2. Fundamental and Sentiment are unpromoted and `UNAVAILABLE` universe-wide.
3. Rank IC is negative and both record types have `eff_n=1`; no confidence label is actionable.
4. VaR/CVaR and drawdown diagnostics use normal-return approximations where stated.
5. Options IV, positioning, bid-ask, and analyst tape are missing Enhancing inputs.
6. The mandated ETF beta×SPY-mu architecture has a known deferred Track A concern.

## Next manual review

No scheduler is active. The next manual weekday full-run opportunity is 2026-08-04 at 07:27
ET, after confirmed or cadence-estimated earnings dates are supplied for the full ranked
set. Equity `eff_n` is projected to increment on 2026-08-05 but remains below 3.
