# Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-17
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The run completed on 515 index-union names with `DELAYED` two-source quotes and 513 scoreable technical records. The monitor sleeve is led by CRWD, PANW, DDOG, MNST, BBY, but Technical is the only supportive scoring family and data completeness is 77.78%. All five Required inputs pass; missing Enhancing feeds are confidence caps, not blockers. The regime is `NEUTRAL`, with weakening 20d growth/semiconductor breadth and rising realized volatility. Final status is `NO_TRADE`; 20 equity and three ETF forecasts are published only for calibration.

## MoM Reflection Summary

The exact baseline is `gpt-5-2026-06-19`. All 63 due keys were settled, leaving zero canonical due inventory. Rolling equity metrics are 119 records, 55.46% hit rate, 79.83% CI coverage, mean z `-0.174`, and weighted rank IC `-0.0088` (L336,L337,L338); the non-positive IC triggers calibration priority and a MEDIUM confidence cap.

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| NEUTRAL | DELAYED; DQ 0.78 | FOMC July 28–29; short-horizon QQQ/SOXX weakness | L155,L006 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | CI70 | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 743.625 | +0.50% | 4.50% | 747.343 | 712.546–782.140 | MEDIUM |
| QQQ | 696.750 | +0.86% | 8.80% | 702.718 | 638.945–766.491 | MEDIUM |
| SOXX | 522.950 | +1.84% | 22.09% | 532.550 | 412.422–652.679 | MEDIUM |

## Ranked Monitoring Candidates

| Universe Rank | Ticker | Entry | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe RAW | IR | Kelly 0.25 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | Class | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CRWD | 203.945 | 0.363 | (0.30*0_UNAV+0.30*1.551+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 100.0 | 1.48 | 17.1% | 0.35 | 0.35 | 5.00% | SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_3 | 63.73/74.07/74.32 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L156,L157,L158,L159,L160,L161,L162,L163,L164 |
| 3 | PANW | 356.790 | 0.295 | (0.30*0_UNAV+0.30*1.515+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.06 | 99.6 | 1.59 | 16.4% | 0.37 | 0.36 | 5.00% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_3 | 67.05/77.19/76.3 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L165,L166,L167,L168,L169,L170,L171,L172,L173 |
| 4 | DDOG | 258.290 | 0.281 | (0.30*0_UNAV+0.30*1.202+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 99.4 | 0.43 | 14.0% | 0.43 | 0.24 | 5.00% | BUY_SETUP_1/SELL_SETUP_3/SELL_SETUP_3 | 57.63/72.94/73.67 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L174,L175,L176,L177,L178,L179,L180,L181,L182 |
| 6 | MNST | 97.310 | 0.274 | (0.30*0_UNAV+0.30*1.255+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.02 | 99.0 | 0.36 | 4.9% | 1.21 | 0.61 | 5.00% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_4 | 57.68/73.64/72.68 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L183,L184,L185,L186,L187,L188,L189,L190,L191 |
| 8 | BBY | 84.950 | 0.247 | (0.30*0_UNAV+0.30*1.055+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 98.6 | 0.61 | 8.5% | 0.70 | 0.43 | 5.00% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3 | 69.85/64.12/55.74 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L192,L193,L194,L195,L196,L197,L198,L199,L200 |
| 10 | BAC | 61.175 | 0.236 | (0.30*0_UNAV+0.30*1.009+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 98.2 | 0.22 | 5.9% | 1.02 | 1.00 | 5.00% | SELL_SETUP_4/SELL_SETUP_7/SELL_SETUP_2 | 69.47/69.21/69.39 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L201,L202,L203,L204,L205,L206,L207,L208,L209 |
| 14 | MPC | 311.415 | 0.215 | (0.30*0_UNAV+0.30*1.560+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.15 | 97.5 | -0.53 | 10.1% | 0.59 | 0.62 | 5.00% | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_6 | 77.43/74.41/80.34 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L210,L211,L212,L213,L214,L215,L216,L217,L218 |
| 15 | PSX | 206.370 | 0.207 | (0.30*0_UNAV+0.30*1.439+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.13 | 97.3 | -0.65 | 9.8% | 0.61 | 0.68 | 5.00% | SELL_SETUP_9/SELL_SETUP_2/SELL_SETUP_7 | 72.46/69.05/72.5 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | LOW / MONITOR | L219,L220,L221,L222,L223,L224,L225,L226,L227 |
| 16 | GEN | 26.745 | 0.203 | (0.30*0_UNAV+0.30*0.869+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 97.1 | 0.62 | 10.7% | 0.56 | 0.43 | 5.00% | SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_3 | 61.94/59.58/53.67 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW / MONITOR | L228,L229,L230,L231,L232,L233,L234,L235,L236 |
| 17 | UNP | 299.880 | 0.201 | (0.30*0_UNAV+0.30*1.415+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.13 | 96.9 | -0.14 | 7.1% | 0.84 | 0.71 | 5.00% | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_6 | 76.39/70.33/65.67 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L237,L238,L239,L240,L241,L242,L243,L244,L245 |
| 19 | INCY | 117.175 | 0.194 | (0.30*0_UNAV+0.30*1.258+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.10 | 96.5 | -0.51 | 12.0% | 0.50 | 0.64 | 5.00% | SELL_SETUP_1/SELL_SETUP_7/SELL_SETUP_2 | 63.9/65.17/73.21 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L246,L247,L248,L249,L250,L251,L252,L253,L254 |
| 20 | NTAP | 163.550 | 0.191 | (0.30*0_UNAV+0.30*0.818+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 96.3 | 1.30 | 14.0% | 0.43 | 0.29 | 5.00% | BUY_SETUP_3/SELL_SETUP_2/SELL_SETUP_4 | 53.52/67.57/66.91 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L255,L256,L257,L258,L259,L260,L261,L262,L263 |
| 21 | AAPL | 334.190 | 0.185 | (0.30*0_UNAV+0.30*1.348+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.13 | 96.1 | 0.51 | 9.9% | 0.60 | 0.71 | 5.00% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3 | 70.26/69.05/70.01 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L264,L265,L266,L267,L268,L269,L270,L271,L272 |
| 23 | DOC | 22.330 | 0.178 | (0.30*0_UNAV+0.30*1.189+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.10 | 95.7 | 0.64 | 7.5% | 0.80 | 0.46 | 5.00% | SELL_SETUP_3/SELL_SETUP_4/SELL_SETUP_4 | 68.46/68.04/58.53 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L273,L274,L275,L276,L277,L278,L279,L280,L281 |
| 24 | VLO | 306.700 | 0.175 | (0.30*0_UNAV+0.30*1.474+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.17 | 95.5 | -0.81 | 11.6% | 0.52 | 0.58 | 5.00% | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_9 | 71.35/74.17/81.43 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L282,L283,L284,L285,L286,L287,L288,L289,L290 |
| 25 | DG | 125.460 | 0.172 | (0.30*0_UNAV+0.30*0.735+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 95.3 | 0.31 | 10.9% | 0.55 | 0.52 | 5.00% | SELL_SETUP_6/SELL_SETUP_6/SELL_SETUP_1 | 62.35/54.0/51.31 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | LOW / MONITOR | L291,L292,L293,L294,L295,L296,L297,L298,L299 |
| 27 | HPQ | 24.975 | 0.167 | (0.30*0_UNAV+0.30*0.715+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 94.9 | 0.40 | 9.7% | 0.52 | 0.29 | 5.00% | SELL_SETUP_1/SELL_SETUP_1/SELL_SETUP_3 | 59.39/56.81/48.26 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | LOW / MONITOR | L300,L301,L302,L303,L304,L305,L306,L307,L308 |
| 28 | CHRW | 207.220 | 0.167 | (0.30*0_UNAV+0.30*1.268+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.13 | 94.7 | 0.56 | 8.9% | 0.56 | 0.46 | 5.00% | SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_2 | 71.01/65.24/74.24 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | LOW / MONITOR | L309,L310,L311,L312,L313,L314,L315,L316,L317 |
| 29 | IQV | 206.645 | 0.157 | (0.30*0_UNAV+0.30*1.099+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.10 | 94.5 | 0.42 | 11.0% | 0.46 | 0.36 | 5.00% | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_2 | 63.24/58.55/52.08 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | LOW / MONITOR | L318,L319,L320,L321,L322,L323,L324,L325,L326 |
| 30 | VEEV | 195.750 | 0.156 | (0.30*0_UNAV+0.30*0.666+0.25*0_SHADOW+0.15*0_UNAV)*0.78-0.00 | 94.3 | 0.18 | 12.8% | 0.39 | 0.35 | 5.00% | BUY_SETUP_1/SELL_SETUP_3/SELL_SETUP_1 | 65.77/53.54/45.03 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | LOW / MONITOR | L327,L328,L329,L330,L331,L332,L333,L334,L335 |

## Portfolio Analytics / No-Trade Rationale

There is no investable subset: every ranked equity fails three-family support, 85% completeness, and the 50% maximum-family-contribution gate. Six monitor names have literal earnings dates inside 14 calendar days; the required +/-5-day estimated-date buffer raises the concentration to nine, above the limit of two (L213,L222,L240,L249,L267,L276,L285,L312,L321). Portfolio weights and aggregate analytics are therefore not applicable; no protected limit was tested with invented weights.

## Assumptions and Limitations

- Public Yahoo/Nasdaq observations are not a brokerage feed; all entry prices are tagged `DELAYED` and dated 2026-07-17.
- Risk histories and settlements use completed closes; intraday technical snapshots are never substituted for settlement closes.
- Fundamental and Sentiment outputs remain SHADOW at 24/515 coverage and are excluded from scoring; per-name Macro_Z and several Enhancing feeds are unavailable.
- The FOMC meeting date comes from the Federal Reserve's official calendar; no unsourced press-conference time is asserted.

## Next Scheduled Review

No durable scheduler is active. The 15:45 ET pre-close, 16:20 close, 17:00 evolution, and Friday 17:15 weekly checkpoints remain manual; this run records their pre-due status in `11`, `12`, and `14`.
