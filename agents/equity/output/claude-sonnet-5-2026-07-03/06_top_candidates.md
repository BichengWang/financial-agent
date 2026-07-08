# 06 Top Candidates

Inherited from `05_factor_scores.md` — no new facts introduced. **No name is investable this run** (see `05 § Investable Subset`); the table below is the monitoring/watchlist sleeve, i.e. the 12 names clearing the 60th `SAMPLED_PCTL` ranking floor and therefore carrying a settleable `mu`/`sigma` forecast per `rules.md § Prediction Ledger`.

## Monitoring Sleeve (Rank Order)

| Rank | Ticker | Adj Score | Pctl | Score Trace (compact) | Beta (SPY) | 30d RVol | mu | Confidence | Why it clears the ranking floor | Why it is not Investable |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | --- | --- | --- |
| 1 | `INTC` | 0.375 | 100.0 | Tech_Z +0.82, Macro_Z +1.69 | 3.51 | 26.2% | +6.0% | MEDIUM | Strong 60d momentum (+127.5%) and relative strength (+114.5% vs SPY); high beta captures the `BULL`-regime macro leg. | Fund_Z / Sent_Z `UNAVAILABLE` — fails the ≥3-of-4-family evidence gate regardless of score. |
| 2 | `AMAT` | 0.353 | 96.6 | Tech_Z +0.88, Macro_Z +1.38 | 3.19 | 26.8% | +6.0% | MEDIUM | Bullish daily/weekly/monthly MA alignment, MACD above signal on all three timeframes, strong RS. | Same. |
| 3 | `AMD` | 0.296 | 93.1 | Tech_Z +0.38, Macro_Z +1.87 | 3.98 | 23.4% | +5.0% | MEDIUM | Highest beta in the sample; bullish daily MA alignment. | Same. |
| 4 | `MU` | 0.192 | 89.7 | Tech_Z -0.13, Macro_Z +1.96 | 4.28 | 36.5% | +4.0% | MEDIUM | Very high beta dominates the score despite a slightly negative Tech_Z; daily TD-9 shows exhaustion risk (see `05`). | Same. |
| 5 | `PANW` | 0.179 | 86.2 | Tech_Z +0.85, Macro_Z -0.11 | 1.18 | 16.1% | +4.0% | MEDIUM | Lower beta than the semis cluster but the strongest confirmed bullish technical state in the sleeve (MACD above signal all timeframes); score driven almost entirely by Tech_Z, not macro beta. | Same. |
| 6 | `MRVL` | 0.171 | 82.8 | Tech_Z -0.22, Macro_Z +1.96 | 4.00 | 41.8% | +3.0% | MEDIUM | Very high beta dominates the score despite a negative Tech_Z — the weakest technical confirmation of the top 6. | Same. |
| 7 | `FLEX` | 0.139 | 79.3 | Positive Tech_Z, positive Macro_Z | 3.66 | 22.8% | +2.0% | MEDIUM | Positive momentum/RS, high beta. | Same; also Monitoring-band score (pctl < 80). |
| 8 | `DELL` | 0.087 | 75.9 | Mixed | 2.23 | 35.5% | +2.0% | MEDIUM | Modest positive composite. | Same. |
| 9 | `MRNA` | 0.084 | 72.4 | Mixed | 1.04 | 22.5% | +2.0% | MEDIUM | Modest positive composite. | Same. |
| 10 | `CAT` | 0.080 | 69.0 | Mixed | 2.01 | 15.5% | +1.0% | MEDIUM | Carried forward from `02_reflection.md` (MoM alpha HIT, +8.45%); still clears the ranking floor today. | Same. |
| 11 | `HUM` | 0.077 | 65.5 | Mixed, low beta | 0.15 | 11.4% | +1.0% | MEDIUM | Lowest-beta name in the monitoring sleeve — low regime-macro exposure but still marginally positive composite. | Same. |
| 12 | `DDOG` | 0.051 | 62.1 | Marginal positive composite | 0.43 | 18.4% | +1.0% | LOW | Barely clears the 60th-percentile floor. | Same; also weakest-evidence name in the sleeve. |

## Reader's Guide: Why Nothing Is Investable Despite Positive Scores

Six names (`INTC` through `MRVL`) score in the nominal 80th-percentile-and-above "Investable" score band. None are published as investable because **Fundamental and Sentiment/Positioning are completely unsourced this session** (no cross-sectional feed for either), so at most 2 of the 4 required factor families (Technical/Price, Macro/Regime) are ever available for any name. `rules.md § Evidence Thresholds` requires "at least 3 of 4 factor families are non-negative" for investable status, and `rules.md § Family Aggregation` explicitly excludes `UNAVAILABLE` families from that count. This is a data-completeness gate applied identically to every name in the universe — it is not a judgment that any individual thesis is weak.

See `07_portfolio_proposal.md` for the Portfolio Construction Agent's confirmation and `08_risk_review.md` for the Risk Committee's review of this gate.
