# 03 Regime and Data

Run `claude-opus-4-8` · 2026-06-30 · Data mode **LIVE**.

## Data Mode Declaration

**LIVE.** A real-time market-data feed (IBKR connected tool) is wired and used for the Core ETF sleeve and a 7-name validation set spanning the full volatility spectrum (SPY, QQQ, SOXX, MU, AMD, UNH, LLY), all cross-checked within 0.30% against the same-session Yahoo feed (01 L001–L007). The broad screening universe uses same-session Yahoo intraday closes validated against the connected tool. All five Required inputs (`rules.md § Input Classification`) are grounded. Unusable-data halt criteria are not triggered.

## Regime Classification — BULL (extended, rotating)

**Label: BULL**, with explicit late-cycle / high-dispersion caveats. Cited evidence (all ledger-backed):

| Signal | Reading | Source |
|---|---|---|
| SPY trend | Daily/weekly/monthly MA alignment all **BULLISH** (close 746.1 > MA20 742.2 > MA50 735.9; weekly/monthly far above) | L303 |
| SPY 60d momentum | +13.8% (3-month advance intact) | L204 |
| SPY 20d momentum | −1.6% (near-term consolidation at highs) | L204 |
| SPY drawdown | only −4.5% from 60d high | L203 |
| SPY realized vol | 30d annualized ~15.4%, **rising** from 11.7% prior 30d | L201 |
| SPY RSI d/w/m | 54.6 / 63.0 / **72.2** (monthly extended/overbought) | L301 |
| SPY MACD d/w/m | **BELOW_SIGNAL** / ABOVE / ABOVE (daily momentum cooling) | L302 |
| Breadth/leadership | Rotation **out of** mega-cap growth (MSFT −18%/MoM, NOW −22%, PLTR −25%, NFLX −15%, META −12%) **into** healthcare/financials/industrials/cyclicals (UNH RS60d +36, CAT +35, GE +19, LLY +15) and semis/memory (SOXX +74 RS, MU +199 RS) | L205 |

**Why BULL, not HIGH_VOL or NEUTRAL:** the index is above all moving averages on every timeframe with a positive multi-month trend and only a shallow drawdown; index-level realized vol (~15%) is not elevated. The volatility is at the *single-stock* level (semis 70–120% annualized), not the index — so the regime is a BULL with extreme internal dispersion, not a HIGH_VOL regime. The defensive caveat (monthly RSI extended, daily MACD below signal, semis at TD9-9 exhaustion) tempers the mu prior to the low end of the BULL band.

**Event-concentration flags:** Q2 earnings season opens inside the 2–6 week horizon. Large-cap banks (JPM ~Jul 14, BAC/GS ~Jul 15) and healthcare (UNH/JNJ ~Jul 15) report ~14–15 days out — inside the buffered 14d+5d earnings window, so those names carry the earnings penalty (05). FOMC: none confirmed inside the immediate 14-day window from sourced calendar (Enhancing input; not separately fetched). Earnings dates are cadence-estimated `ESTIMATED (±5d)`.

## Core ETF Market Forecast Block

Entry = IBKR LIVE (L001–L003). mu derivation per `rules.md § Core ETF Market Forecast`: regime BULL → SPY prior +2.0%, adjusted **−0.5pp to +1.5%** (within ±1.0pp band) for the near-term daily MACD-below-signal / −1.6% 20d consolidation. QQQ/SOXX mu = `beta_to_SPY × SPY_mu`, beta from 60d fetched daily returns (L202, `DERIVED`); SOXX adjusted **−1.5pp** (max band) for weekly+monthly TD9 SELL_SETUP_9 and monthly RSI 88.6 exhaustion. sigma = REALIZED_VOL_30D (L200). target_date = run_date + 28d = 2026-07-28. CI = entry × (1 + mu ± 1.04σ).

| ETF | Entry | Price Date | Tag | Trend 20d/50d | 30d RVol (Δ) | Beta vs SPY | mu | sigma | Sigma Src | Target | Target Date | 70% CI Lo | 70% CI Hi | Conf | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 745.17 | 2026-06-30 | LIVE | BULLISH | 15.4% (rising) | 1.00 | +1.5% | 4.4% | REALIZED_VOL_30D | 756.35 | 2026-07-28 | 721.94 | 790.76 | MEDIUM | L001,L200–L202 |
| QQQ | 734.34 | 2026-06-30 | LIVE | BULLISH | 28.0% (rising) | 1.56 | +2.35% | 8.2% | REALIZED_VOL_30D | 751.60 | 2026-07-28 | 688.90 | 814.30 | MEDIUM | L002,L200–L202 |
| SOXX | 636.03 | 2026-06-30 | LIVE | BULLISH | 69.9% (rising) | 3.17 | +3.26% | 20.5% | REALIZED_VOL_30D | 656.76 | 2026-07-28 | 520.96 | 792.56 | LOW | L003,L200–L202 |

mu(QQQ) = 1.564 × 1.5% = +2.35%. mu(SOXX) = 3.171 × 1.5% = +4.76%, −1.5pp exhaustion = **+3.26%**.

**Relative strength:** QQQ/SPY +0.5% (20d) / +11.8% (60d); SOXX/SPY +12.9% (20d) / +73.6% (60d). Semis are the dominant leadership but the most exhausted (TD9-9 weekly+monthly, RSI 88.6). **Regime-consistency note:** ETF block is internally consistent with the BULL call — all three above rising MAs with positive trend; the LOW confidence on SOXX and MEDIUM elsewhere reflect extended monthly RSI and rising realized vol. Betas are 60d-fetched and **inflated by the parabolic semis advance** (QQQ/SOXX betas should be read as unstable upper bounds).

ETF rows are a **market-forecast sleeve** — never candidates, never universe members, exempt from the single-name filters and the 5–10 investable set.

## Universe Handoff

Eligible universe = 35 equities across all 11 GICS sectors (Sampled Universe Protocol; see 04). Core ETF + eligible-universe ticker list handed to `technical_indicators.py` (executed; `technical_indicators.json` covers all 38 symbols, status OK). Ledger coverage gaps affecting scoring: Fundamental and Sentiment **premium** feeds (analyst revisions, short interest, options IV/skew, institutional flow) are `UNAVAILABLE` → those families are scored on disclosed price-based proxies and the data-quality multiplier is held at 0.80 (04, 05).

## Stop-Rule Check

No `HALTED` condition (data lineage clear, benchmark history present). Not `REVIEW_ONLY`-for-staleness (data is same-session LIVE). Handoff to factor scoring proceeds; the run's status is determined downstream at portfolio construction.
