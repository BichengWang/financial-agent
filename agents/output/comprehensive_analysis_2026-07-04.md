# Comprehensive Equity Output Analysis - 2026-07-04

## Scope Read

Reviewed the full output tree under `investments/equity/output`.

- Run folders: 39
- Machine-readable prediction ledgers: 28 `15_predictions.json` files
- Prediction records: 517
- Settlement records: 0
- Unique tickers covered by prediction ledgers: 91
- Latest run date represented: 2026-07-04
- Latest run statuses: `REVIEW_ONLY` or `NO_TRADE`; no run produced an approved live portfolio

The most important limitation is that all prediction records are still `OPEN`. The ledgers themselves state that no target-date settlements are due by 2026-07-04. Therefore, "model performance" cannot yet mean final target-date forecast accuracy. The best available comparison is interim mark-to-market performance from each model's entry prices to the latest available market prices.

## Market Date Clarification

2026-07-04 is a Saturday. U.S. equity markets observe Independence Day on Friday, 2026-07-03, so the last grounded regular-session prices in the strongest July 4 ledgers are 2026-07-02 closes. The first normal trading session after the requested date is Monday, 2026-07-06.

Official and market-data checks used:

- NYSE holiday calendar: Friday, 2026-07-03 is Independence Day observed.
- Nasdaq holiday calendar: Friday, 2026-07-03 is closed for Independence Day observed.
- Current finance snapshots matched the July 4 run prices for the main tickers and ETFs.

## Latest Market Context

The broad tape going into 2026-07-04 is mixed beneath the index level:

| Instrument | Latest Price | Latest Change | Read |
|---|---:|---:|---|
| SPY | 744.78 | -0.11% | Broad market roughly flat |
| QQQ | 712.60 | -1.70% | Growth/mega-cap pressure |
| SOXX | 566.32 | -5.51% | Semiconductor unwind is the dominant near-term risk |
| MU | 975.56 | -5.45% | High score in GPT-5 but large drawdown day |
| AMD | 517.82 | -4.24% | High score in GPT-5 but caught in SOXX weakness |
| INTC | 120.35 | -5.19% | High score in GPT-5 but negative EPS and high volatility |
| DVA | 234.91 | +3.06% | Top Claude Fable score, defensive health-care momentum |
| PANW | 348.06 | -1.20% | Strong momentum but very expensive valuation |
| HUM | 396.75 | -3.17% | Defensive/managed-care signal, but recent price weakness |
| LLY | 1213.91 | +1.69% | Quality health-care carry candidate |
| LIN | 546.64 | +2.44% | Low-beta industrial-gas quality carry |
| ABBV | 261.07 | +3.99% | Strong prior interim alpha, but valuation optics are stretched on GAAP PE |

## Model Performance Method

Because there are no settled predictions yet, I scored interim performance as follows:

1. Treat each `EQUITY_ALPHA` prediction as a positive-return/positive-alpha call.
2. Exclude ETF framing records (`SPY`, `QQQ`, `SOXX`) from stock-model scoring.
3. Use the latest valid market price available through 2026-07-02, because July 3 was a market holiday.
4. Compute realized return: `(latest price / entry price) - 1`.
5. Compute interim alpha versus SPY using each prediction's recorded `benchmark_price`.
6. Use aged windows to avoid giving same-day/newer predictions artificial zero-return marks.

## Interim Performance Summary

### Aged at least 7 calendar days

This is the fairest available window because it removes most same-week noise.

| Model | Scored Names | Avg Return | Median Return | Hit Rate | Avg SPY-Relative Alpha | Median Alpha | Alpha Win Rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5 | 119 | +1.22% | +1.34% | 61.3% | +1.44% | +1.60% | 63.0% |
| gemini-3.5-flash | 12 | +0.81% | +1.29% | 58.3% | +1.07% | +1.55% | 66.7% |

Verdict: `gpt-5` is the best-performing model on the only reasonably sized aged sample. Gemini is competitive on alpha win rate, but its sample is too small to rank above GPT-5.

### Aged at least 3 calendar days

| Model | Scored Names | Avg Return | Median Return | Hit Rate | Avg Alpha | Median Alpha | Alpha Win Rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5 | 148 | +1.15% | +1.24% | 60.8% | +0.97% | +1.35% | 56.8% |
| gemini-3.5-flash | 23 | +0.95% | +0.48% | 60.9% | +0.05% | -0.91% | 47.8% |

Verdict: `gpt-5` again ranks first. Gemini's absolute return is positive, but alpha quality weakens materially in the broader sample.

### Aged at least 1 calendar day

This includes very fresh signals and is less reliable.

| Model | Scored Names | Avg Return | Median Return | Hit Rate | Avg Alpha | Median Alpha | Alpha Win Rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| claude-fable-5 | 18 | +0.53% | +0.34% | 61.1% | +0.66% | +0.47% | 66.7% |
| claude-opus-4-8 | 8 | -2.50% | +0.74% | 62.5% | -2.45% | +0.79% | 62.5% |
| gemini-3.5-flash | 23 | +0.95% | +0.48% | 60.9% | +0.05% | -0.91% | 47.8% |
| gpt-5 | 172 | +0.77% | +0.97% | 59.3% | +0.60% | +0.70% | 55.2% |

Verdict: `claude-fable-5` looks promising in the latest short window and has the best recent risk-control language, but it is too fresh to call the best performer. It should be watched closely after the first formal settlement pass.

## Model Ranking

1. `gpt-5` - Best current performer. It has the largest sample, the strongest aged 7-day average alpha, and a consistently positive median return/median alpha profile. It also captured several strong winners, including ABBV and GE, though it also had repeated FCX misses.
2. `gemini-3.5-flash` - Positive but less convincing. The 7-day alpha win rate is good, but sample size is small and the broader 3-day alpha median is negative.
3. `claude-fable-5` - Best latest process quality, not yet enough aged performance. Its July 4 report is more balanced and risk-aware than GPT-5's semiconductor-heavy output, but performance evidence is still too short.
4. `claude-opus-4-8` - Too little recent evidence and weak aged marks in the available sample.
5. `claude-sonnet-5` - Latest run was useful diagnostically, but not enough valid aged performance through the July 4 decision point.

## Cross-Model Ticker Signals

Recent repeated names since 2026-06-29:

| Ticker | Recent Mentions | Interpretation |
|---|---:|---|
| HUM | 9 | Strong consensus defensive/managed-care signal, but price fell into the holiday |
| PANW | 9 | Strong momentum consensus, but high valuation and overbought risk |
| LLY | 8 | Quality health-care carry with positive prior validation |
| MRNA | 7 | High-beta squeeze candidate, speculative |
| UNH | 6 | Prior health-care validation, but earnings-window risk in latest Claude Fable review |
| LIN | 6 | Low-beta quality carry, lower upside but strong risk profile |
| AMD | 6 | GPT/Sonnet semiconductor signal, but SOXX unwind raises timing risk |
| CAT | 6 | Cyclical signal, mixed recent model performance |
| MU | 6 | Highest GPT-5 score, but very high volatility and semiconductor drawdown |

## Latest Model Recommendations

### GPT-5, 2026-07-04

Top stock scores: `MU`, `INTC`, `AMD`, `DELL`, `WDC`, `MRVL`, `STX`, `SNDK`, `DDOG`, `ARM`.

Strength: strong technical ranking and large sample performance history.

Weakness: current list is concentrated in semiconductors/storage/software right after SOXX dropped 5.51%. All candidates are `LOW` confidence and `REVIEW_ONLY`.

### Claude Fable 5, 2026-07-04

Top stock scores: `DVA`, `PANW`, `DOC`, `BEN`, `HUM`, `HSIC`, `MNST`, `MAS`, `BAX`, `VRTX`, plus carry names `LIN`, `LLY`, `ABBV`.

Strength: better sector balance, explicit no-trade discipline, lower-volatility defensive leadership.

Weakness: all candidates are still `LOW` confidence because fundamental and sentiment factor families are unavailable. Several top names have overbought/exhaustion markers.

## Investability Decision From 2026-07-04

Primary decision: do not treat any single ticker as a fully approved investment from the model system on 2026-07-04.

Reasons:

- Every latest run says `NO_TRADE` or `REVIEW_ONLY`.
- No prediction has settled yet, so true forecast accuracy is unproven.
- Fundamental and sentiment/positioning feeds are unavailable across the system.
- July 4 is not a trading day; July 6 is the first possible regular-session execution date.
- Semiconductor names have the highest GPT-5 scores but are under immediate sector stress.

## If Forced To Pick A Ticker

If a single ticker must be selected from the model outputs for a watchlist or very small starter position after the holiday, the best risk-adjusted candidate is:

### LLY

Rationale:

- Appears repeatedly in recent outputs.
- Positive prior validation in the Claude Fable reflection.
- Current price snapshot: 1213.91, +1.69% latest move.
- Stronger business-quality profile than the most speculative momentum names.
- Less exposed to the immediate SOXX/AI-capex unwind than GPT-5's top semiconductor/storage cluster.
- Fits the health-care defensive leadership theme that has worked better than energy/staples/cyclicals in the interim review.

Main risks:

- Valuation is not cheap; PE is about 43x on the current snapshot.
- GLP-1 expectations are crowded and can re-rate sharply on trial, capacity, pricing, or payer news.
- It is not the top score in the latest Claude Fable run; it is a carry/quality candidate rather than a pure momentum leader.

Position framing if used:

- Treat as a watchlist/starter position, not a full allocation.
- First executable date is Monday, 2026-07-06.
- Avoid chasing a large gap above the 2026-07-02 close.
- Re-check earnings/news/fundamental feed before sizing.

## Alternatives By Risk Profile

| Profile | Ticker | Why | Main Risk |
|---|---|---|---|
| Best single balanced pick | LLY | Quality health-care carry, repeated validation | Valuation/crowding |
| Lowest-beta quality alternative | LIN | Low beta, steady industrial-gas compounder | Lower upside |
| Strongest latest Claude score | DVA | Top July 4 Claude Fable rank; PE about 22x; low beta | RSI/TD9 exhaustion; company-specific health-care risk |
| High-growth momentum | PANW | Strong cyber momentum and repeated model mentions | PE above 300x; overbought |
| Speculative rebound | MU or AMD | Highest GPT-5 technical scores | SOXX drawdown, high volatility, timing risk |

## Final Answer

Best model right now: `gpt-5`.

Best ticker to prioritize from 2026-07-04 outputs if forced to choose one: `LLY`, with the explicit caveat that the system itself says `NO_TRADE` / `REVIEW_ONLY`, so this should be treated as a watchlist or small starter candidate after 2026-07-06 confirmation rather than an unconditional buy signal.
