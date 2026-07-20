# 02 Reflection — 2026-07-20

## 0. Prediction Settlement

The canonical normalizer scanned 54 dated ledgers. This run settled **68/68 due keys**: 51 weekend targets use the final close on or before target, while 17 target-equals-run-date keys use the latest completed close under `TARGET_EQ_RUN_DATE`. Final due inventory is **0** with **0 conflicts** (L250).

| Ticker | Model / Vintage | Target | Entry | Settle 07-17 | mu | Return | SPY Return | Alpha | Direction | CI | z | Timing | Ledger |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---:|---|---|
| AVGO | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 411.3500 | 370.8300 | +1.0% | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.581 | WEEKEND_TARGET | L182 |
| BAC | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 56.2000 | 61.2700 | +3.0% | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.968 | WEEKEND_TARGET | L183 |
| CAT | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 985.8200 | 880.2800 | +6.0% | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.365 | WEEKEND_TARGET | L184 |
| CVX | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 173.6300 | 187.3800 | +2.0% | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.789 | WEEKEND_TARGET | L185 |
| EQIX | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 1092.1900 | 1020.0000 | +2.0% | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.535 | WEEKEND_TARGET | L186 |
| ETN | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 421.7700 | 399.9900 | +1.0% | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.446 | WEEKEND_TARGET | L187 |
| FCX | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 68.6800 | 58.3800 | +4.0% | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.210 | WEEKEND_TARGET | L188 |
| GE | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 357.6400 | 348.8300 | +5.0% | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.743 | WEEKEND_TARGET | L189 |
| GOOGL | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 368.0300 | 346.7700 | +6.0% | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.419 | WEEKEND_TARGET | L190 |
| GS | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 1096.5600 | 1065.2200 | +5.0% | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.783 | WEEKEND_TARGET | L191 |
| JPM | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 325.2200 | 341.1000 | +2.0% | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.390 | WEEKEND_TARGET | L192 |
| LIN | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 512.1500 | 513.2200 | +1.0% | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.144 | WEEKEND_TARGET | L193 |
| LLY | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 1098.5700 | 1179.1100 | +4.0% | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.368 | WEEKEND_TARGET | L194 |
| QQQ | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 740.6200 | 695.3300 | +2.9% | -6.12% | N/A | N/A | MISS | OUT_CI_LOW | -1.178 | WEEKEND_TARGET | L195 |
| SOXX | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 639.4500 | 521.8100 | +5.6% | -18.40% | N/A | N/A | MISS | OUT_CI_LOW | -1.241 | WEEKEND_TARGET | L196 |
| SPY | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 746.7400 | 743.2900 | +2.0% | -0.46% | N/A | N/A | MISS | IN_CI | -0.585 | WEEKEND_TARGET | L197 |
| UNH | gemini-3.5-flash / 2026-06-21 | 2026-07-19 | 400.9600 | 426.0900 | +2.0% | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.563 | WEEKEND_TARGET | L198 |
| AVGO | gpt-5 / 2026-06-20 | 2026-07-18 | 411.3500 | 370.8300 | +1.0% | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.581 | WEEKEND_TARGET | L199 |
| BAC | gpt-5 / 2026-06-20 | 2026-07-18 | 56.2000 | 61.2700 | +3.0% | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.968 | WEEKEND_TARGET | L200 |
| CAT | gpt-5 / 2026-06-20 | 2026-07-18 | 985.8200 | 880.2800 | +6.0% | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.365 | WEEKEND_TARGET | L201 |
| CVX | gpt-5 / 2026-06-20 | 2026-07-18 | 173.6300 | 187.3800 | +2.0% | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.789 | WEEKEND_TARGET | L202 |
| EQIX | gpt-5 / 2026-06-20 | 2026-07-18 | 1092.1900 | 1020.0000 | +2.0% | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.535 | WEEKEND_TARGET | L203 |
| ETN | gpt-5 / 2026-06-20 | 2026-07-18 | 421.7700 | 399.9900 | +1.0% | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.446 | WEEKEND_TARGET | L204 |
| FCX | gpt-5 / 2026-06-20 | 2026-07-18 | 68.6800 | 58.3800 | +4.0% | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.210 | WEEKEND_TARGET | L205 |
| GE | gpt-5 / 2026-06-20 | 2026-07-18 | 357.6400 | 348.8300 | +5.0% | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.743 | WEEKEND_TARGET | L206 |
| GOOGL | gpt-5 / 2026-06-20 | 2026-07-18 | 368.0300 | 346.7700 | +6.0% | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.419 | WEEKEND_TARGET | L207 |
| GS | gpt-5 / 2026-06-20 | 2026-07-18 | 1096.5600 | 1065.2200 | +5.0% | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.783 | WEEKEND_TARGET | L208 |
| JPM | gpt-5 / 2026-06-20 | 2026-07-18 | 325.2200 | 341.1000 | +2.0% | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.390 | WEEKEND_TARGET | L209 |
| LIN | gpt-5 / 2026-06-20 | 2026-07-18 | 512.1500 | 513.2200 | +1.0% | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.144 | WEEKEND_TARGET | L210 |
| LLY | gpt-5 / 2026-06-20 | 2026-07-18 | 1098.5700 | 1179.1100 | +4.0% | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.368 | WEEKEND_TARGET | L211 |
| QQQ | gpt-5 / 2026-06-20 | 2026-07-18 | 740.6200 | 695.3300 | +2.9% | -6.12% | N/A | N/A | MISS | OUT_CI_LOW | -1.178 | WEEKEND_TARGET | L212 |
| SOXX | gpt-5 / 2026-06-20 | 2026-07-18 | 639.4500 | 521.8100 | +5.6% | -18.40% | N/A | N/A | MISS | OUT_CI_LOW | -1.241 | WEEKEND_TARGET | L213 |
| SPY | gpt-5 / 2026-06-20 | 2026-07-18 | 746.7400 | 743.2900 | +2.0% | -0.46% | N/A | N/A | MISS | IN_CI | -0.585 | WEEKEND_TARGET | L214 |
| UNH | gpt-5 / 2026-06-20 | 2026-07-18 | 400.9600 | 426.0900 | +2.0% | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.563 | WEEKEND_TARGET | L215 |
| AVGO | gpt-5 / 2026-06-21 | 2026-07-19 | 411.3500 | 370.8300 | +1.0% | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.581 | WEEKEND_TARGET | L216 |
| BAC | gpt-5 / 2026-06-21 | 2026-07-19 | 56.2000 | 61.2700 | +3.0% | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.968 | WEEKEND_TARGET | L217 |
| CAT | gpt-5 / 2026-06-21 | 2026-07-19 | 985.8200 | 880.2800 | +6.0% | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.365 | WEEKEND_TARGET | L218 |
| CVX | gpt-5 / 2026-06-21 | 2026-07-19 | 173.6300 | 187.3800 | +2.0% | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.789 | WEEKEND_TARGET | L219 |
| EQIX | gpt-5 / 2026-06-21 | 2026-07-19 | 1092.1900 | 1020.0000 | +2.0% | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.535 | WEEKEND_TARGET | L220 |
| ETN | gpt-5 / 2026-06-21 | 2026-07-19 | 421.7700 | 399.9900 | +1.0% | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.446 | WEEKEND_TARGET | L221 |
| FCX | gpt-5 / 2026-06-21 | 2026-07-19 | 68.6800 | 58.3800 | +4.0% | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.210 | WEEKEND_TARGET | L222 |
| GE | gpt-5 / 2026-06-21 | 2026-07-19 | 357.6400 | 348.8300 | +5.0% | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.743 | WEEKEND_TARGET | L223 |
| GOOGL | gpt-5 / 2026-06-21 | 2026-07-19 | 368.0300 | 346.7700 | +6.0% | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.419 | WEEKEND_TARGET | L224 |
| GS | gpt-5 / 2026-06-21 | 2026-07-19 | 1096.5600 | 1065.2200 | +5.0% | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.783 | WEEKEND_TARGET | L225 |
| JPM | gpt-5 / 2026-06-21 | 2026-07-19 | 325.2200 | 341.1000 | +2.0% | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.390 | WEEKEND_TARGET | L226 |
| LIN | gpt-5 / 2026-06-21 | 2026-07-19 | 512.1500 | 513.2200 | +1.0% | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.144 | WEEKEND_TARGET | L227 |
| LLY | gpt-5 / 2026-06-21 | 2026-07-19 | 1098.5700 | 1179.1100 | +4.0% | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.368 | WEEKEND_TARGET | L228 |
| QQQ | gpt-5 / 2026-06-21 | 2026-07-19 | 740.6200 | 695.3300 | +2.9% | -6.12% | N/A | N/A | MISS | OUT_CI_LOW | -1.178 | WEEKEND_TARGET | L229 |
| SOXX | gpt-5 / 2026-06-21 | 2026-07-19 | 639.4500 | 521.8100 | +5.6% | -18.40% | N/A | N/A | MISS | OUT_CI_LOW | -1.241 | WEEKEND_TARGET | L230 |
| SPY | gpt-5 / 2026-06-21 | 2026-07-19 | 746.7400 | 743.2900 | +2.0% | -0.46% | N/A | N/A | MISS | IN_CI | -0.585 | WEEKEND_TARGET | L231 |
| UNH | gpt-5 / 2026-06-21 | 2026-07-19 | 400.9600 | 426.0900 | +2.0% | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.563 | WEEKEND_TARGET | L232 |
| AVGO | gpt-5 / 2026-06-22 | 2026-07-20 | 411.3500 | 370.8300 | +1.0% | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.581 | TARGET_EQ_RUN_DATE | L233 |
| BAC | gpt-5 / 2026-06-22 | 2026-07-20 | 56.2000 | 61.2700 | +3.0% | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.968 | TARGET_EQ_RUN_DATE | L234 |
| CAT | gpt-5 / 2026-06-22 | 2026-07-20 | 985.8200 | 880.2800 | +6.0% | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.365 | TARGET_EQ_RUN_DATE | L235 |
| CVX | gpt-5 / 2026-06-22 | 2026-07-20 | 173.6300 | 187.3800 | +2.0% | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.789 | TARGET_EQ_RUN_DATE | L236 |
| EQIX | gpt-5 / 2026-06-22 | 2026-07-20 | 1092.1900 | 1020.0000 | +2.0% | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.535 | TARGET_EQ_RUN_DATE | L237 |
| ETN | gpt-5 / 2026-06-22 | 2026-07-20 | 421.7700 | 399.9900 | +1.0% | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.446 | TARGET_EQ_RUN_DATE | L238 |
| FCX | gpt-5 / 2026-06-22 | 2026-07-20 | 68.6800 | 58.3800 | +4.0% | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.210 | TARGET_EQ_RUN_DATE | L239 |
| GE | gpt-5 / 2026-06-22 | 2026-07-20 | 357.6400 | 348.8300 | +5.0% | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.743 | TARGET_EQ_RUN_DATE | L240 |
| GOOGL | gpt-5 / 2026-06-22 | 2026-07-20 | 368.0300 | 346.7700 | +6.0% | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.419 | TARGET_EQ_RUN_DATE | L241 |
| GS | gpt-5 / 2026-06-22 | 2026-07-20 | 1096.5600 | 1065.2200 | +5.0% | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.783 | TARGET_EQ_RUN_DATE | L242 |
| JPM | gpt-5 / 2026-06-22 | 2026-07-20 | 325.2200 | 341.1000 | +2.0% | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.390 | TARGET_EQ_RUN_DATE | L243 |
| LIN | gpt-5 / 2026-06-22 | 2026-07-20 | 512.1500 | 513.2200 | +1.0% | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.144 | TARGET_EQ_RUN_DATE | L244 |
| LLY | gpt-5 / 2026-06-22 | 2026-07-20 | 1098.5700 | 1179.1100 | +4.0% | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.368 | TARGET_EQ_RUN_DATE | L245 |
| QQQ | gpt-5 / 2026-06-22 | 2026-07-20 | 740.6200 | 695.3300 | +2.9% | -6.12% | N/A | N/A | MISS | OUT_CI_LOW | -1.178 | TARGET_EQ_RUN_DATE | L246 |
| SOXX | gpt-5 / 2026-06-22 | 2026-07-20 | 639.4500 | 521.8100 | +5.6% | -18.40% | N/A | N/A | MISS | OUT_CI_LOW | -1.241 | TARGET_EQ_RUN_DATE | L247 |
| SPY | gpt-5 / 2026-06-22 | 2026-07-20 | 746.7400 | 743.2900 | +2.0% | -0.46% | N/A | N/A | MISS | IN_CI | -0.585 | TARGET_EQ_RUN_DATE | L248 |
| UNH | gpt-5 / 2026-06-22 | 2026-07-20 | 400.9600 | 426.0900 | +2.0% | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.563 | TARGET_EQ_RUN_DATE | L249 |

### Rolling calibration

| Sleeve | n | Hit rate | CI coverage | Mean z | Rank IC |
|---|---:|---:|---:|---:|---:|
| EQUITY_ALPHA | 175 | 51.43% | 77.14% | -0.2363 | -0.048856 weighted vintage mean |
| MARKET_FORECAST | 30 | 20.00% | 60.00% | -0.7723 | N/A |

Equity CI coverage remains inside the healthy 55–85% range. Weighted rank IC remains non-positive, so confidence stays capped at MEDIUM; every published equity is LOW because only two families are sourceable.

## 1. Prior Run Summary

Baseline: `agents/equity/output/gpt-5-2026-06-22`, the exact same-model 28-day match. All defined exception flags are false: `NO_PRIOR_BASELINE=false`, `CROSS_MODEL_BASELINE=false`, `BASELINE_WINDOW_GAP=false`, `NO_VALID_MOM_BASELINE=false`. Source: `agents/equity/output/gpt-5-2026-06-22/15_predictions.json`. It was NO_TRADE and recorded 14 equity-alpha forecasts plus SPY/QQQ/SOXX. Its top five scores were CAT, GOOGL, GS, GE, and LLY. The older package used sampled-universe-era score semantics, so this reflection evaluates its recorded predictions without treating its percentile scale as current evidence.

## 2. MoM Price and Return Table

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI | Ledger / Notes |
|---|---|---:|---|---:|---:|---:|---:|---|---|---|
| AVGO | 2026-06-18 | 411.3500 | 2026-07-17 | 370.8300 | -9.85% | -0.46% | -9.39% | MISS | IN_CI | L233; immutable baseline prediction |
| BAC | 2026-06-18 | 56.2000 | 2026-07-17 | 61.2700 | +9.02% | -0.46% | +9.48% | HIT | IN_CI | L234; immutable baseline prediction |
| CAT | 2026-06-18 | 985.8200 | 2026-07-17 | 880.2800 | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | L235; immutable baseline prediction |
| CVX | 2026-06-18 | 173.6300 | 2026-07-17 | 187.3800 | +7.92% | -0.46% | +8.38% | HIT | IN_CI | L236; immutable baseline prediction |
| EQIX | 2026-06-18 | 1092.1900 | 2026-07-17 | 1020.0000 | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | L237; immutable baseline prediction |
| ETN | 2026-06-18 | 421.7700 | 2026-07-17 | 399.9900 | -5.16% | -0.46% | -4.70% | MISS | IN_CI | L238; immutable baseline prediction |
| FCX | 2026-06-18 | 68.6800 | 2026-07-17 | 58.3800 | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | L239; immutable baseline prediction |
| GE | 2026-06-18 | 357.6400 | 2026-07-17 | 348.8300 | -2.46% | -0.46% | -2.00% | MISS | IN_CI | L240; immutable baseline prediction |
| GOOGL | 2026-06-18 | 368.0300 | 2026-07-17 | 346.7700 | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | L241; immutable baseline prediction |
| GS | 2026-06-18 | 1096.5600 | 2026-07-17 | 1065.2200 | -2.86% | -0.46% | -2.40% | MISS | IN_CI | L242; immutable baseline prediction |
| JPM | 2026-06-18 | 325.2200 | 2026-07-17 | 341.1000 | +4.88% | -0.46% | +5.34% | HIT | IN_CI | L243; immutable baseline prediction |
| LIN | 2026-06-18 | 512.1500 | 2026-07-17 | 513.2200 | +0.21% | -0.46% | +0.67% | HIT | IN_CI | L244; immutable baseline prediction |
| LLY | 2026-06-18 | 1098.5700 | 2026-07-17 | 1179.1100 | +7.33% | -0.46% | +7.79% | HIT | IN_CI | L245; immutable baseline prediction |
| UNH | 2026-06-18 | 400.9600 | 2026-07-17 | 426.0900 | +6.27% | -0.46% | +6.73% | HIT | IN_CI | L249; immutable baseline prediction |

## 3. Theme-Level Performance

**INFERRED from L233,L234,L235,L236,L237,L238,L239,L240,L241,L242,L243,L244,L245,L249:** the June 22 cyclical/AI-infrastructure cohort was mixed. BAC, UNH, LLY, JPM, CVX, and LIN beat SPY; CAT, GOOGL, GS, GE, FCX, EQIX, ETN, and AVGO did not. The top-ranked CAT/GOOGL misses and lower-ranked financial/health wins are consistent with weak score ordering rather than a clean theme validation.

## 4. Regime Shift Assessment

**INFERRED (L008)**: the June 22 BULL posture has cooled to **NEUTRAL**. SPY ended at 743.29, versus MA20 745.02 and MA50 744.38; QQQ and SOXX show negative 20-day SPY-relative strength (L009,L010,L011,L013,L014,L015,L017,L018,L019). The July 28–29 FOMC meeting sits inside the horizon (L005). No factor weights change.

## 5. Carry-Forward Decisions

| Ticker | Prior Score | Prior Thesis | MoM Return | Current Pctl | Decision | Rationale | Ledger / Notes |
|---|---:|---|---:|---:|---|---|---|
| AVGO | 64.7 | AI networking/custom silicon strength balanced by high beta. | -9.85% | 5.9 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L233,L251; baseline `15_predictions.json` |
| BAC | 82.4 | Rate/credit-sensitive financial rebound with low realized sigma. | +9.02% | 95.1 | CARRY | Positive alpha and current monitor-band rank; included in today's sleeve. | L234,L251; baseline `15_predictions.json` |
| CAT | 100.0 | Cyclical machinery quality with strong trend and operating leverage. | -10.71% | 21.9 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L235,L251; baseline `15_predictions.json` |
| CVX | 73.5 | Energy major quality but negative market beta in the sampled window. | +7.92% | 18.4 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L236,L251; baseline `15_predictions.json` |
| EQIX | 70.6 | Data-center REIT demand with rate sensitivity. | -6.61% | 15.8 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L237,L251; baseline `15_predictions.json` |
| ETN | 67.6 | Electrification exposure with high beta and cyclical sensitivity. | -5.16% | 17.0 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L238,L251; baseline `15_predictions.json` |
| FCX | 85.3 | Copper beta and cyclical leverage in a pro-risk tape. | -15.00% | 2.1 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L239,L251; baseline `15_predictions.json` |
| GE | 91.2 | Aerospace quality and strong earnings surprise history. | -2.46% | 81.2 | DOWNGRADE | Current evidence does not support carry; omitted unless independently top-20. | L240,L251; baseline `15_predictions.json` |
| GOOGL | 97.1 | Search/cloud AI monetization with positive earnings evidence. | -5.78% | 14.3 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L241,L251; baseline `15_predictions.json` |
| GS | 94.1 | Capital-markets leverage and positive momentum. | -2.86% | 61.9 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L242,L251; baseline `15_predictions.json` |
| JPM | 76.5 | Large-bank quality with balanced credit and capital-markets exposure. | +4.88% | 75.8 | CARRY | Positive alpha and current monitor-band rank; included in today's sleeve. | L243,L251; baseline `15_predictions.json` |
| LIN | 61.8 | Industrial-gas quality with lower beta. | +0.21% | 38.9 | DROP | Current evidence does not support carry; omitted unless independently top-20. | L244,L251; baseline `15_predictions.json` |
| LLY | 88.2 | GLP-1/obesity leadership with resilient relative strength. | +7.33% | 90.8 | CARRY | Positive alpha and current monitor-band rank; included in today's sleeve. | L245,L251; baseline `15_predictions.json` |
| UNH | 79.4 | Managed-care rebound with defensive beta. | +6.27% | 98.0 | PROMOTE | Positive alpha and current monitor-band rank; included in today's sleeve. | L249,L251; baseline `15_predictions.json` |

## 6. Sign-Off

All current and settlement prices are completed 2026-07-17 closes fetched this run and cross-checked within 1% (L006). Reflection confidence is HIGH for settlement arithmetic and MEDIUM for regime interpretation. Structural calibration uncertainty remains because rank IC is -0.048856.
