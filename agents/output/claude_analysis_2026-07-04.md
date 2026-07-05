# Model Comparison & Investment Recommendation — as of 2026-07-04

Prepared from the full `output/` tree (43 run folders, 28 machine-readable `15_predictions.json` ledgers, 517 prediction records across 91 tickers) scored against **real market data** fetched via Yahoo Finance on 2026-07-04/05. Complements the earlier `comprehensive_analysis_2026-07-04.md`.

## 1. Data grounding

- Last real trading session: **Thursday 2026-07-02** (Friday 2026-07-03 was the observed Independence Day holiday; 2026-07-04 is a Saturday). First tradable session: **Monday 2026-07-06**.
- All 91 predicted tickers were re-priced from fresh Yahoo Finance daily closes (2026-05-01 → 2026-07-02). No ticker failed to resolve.
- **Zero predictions have settled yet** — every record is `OPEN`, earliest target dates come due 2026-07-08. "Performance" below therefore means *interim mark-to-market from each model's recorded entry price to the 2026-07-02 close*, and alpha means excess return over SPY across the same window.

## 2. Which model performs better?

### 2a. Data integrity (entry price vs. actual close on the claimed date)

| Model | Median abs error | Max error | Verdict |
|---|---:|---:|---|
| claude-fable-5 | 0.00% | 1.7% | Clean |
| gemini-3.5-flash | 0.00% | 0.16% | Clean |
| gpt-5 | 0.00% | 3.6% | Clean (isolated split/stale artifacts) |
| claude-opus-4-8 | 0.38% | 1.1% | Acceptable |
| **claude-sonnet-5** | **3.39%** | **12.2%** | **Broken** — records entries for a 2026-07-03 session that never traded (market holiday), with prices up to 12% off reality (FLEX 153.53 vs 136.86 actual; MRVL, MRNA, DELL, AMAT all fabricated) |

Claude Sonnet 5's ledger fails basic grounding and should be excluded from any capital decision until its price pipeline is fixed.

### 2b. Interim mark-to-market (stock predictions only; ETF records excluded)

**All records** (includes 1–2 day-old picks):

| Model | N | Avg alpha | Median alpha | Alpha hit rate |
|---|---:|---:|---:|---:|
| claude-fable-5 | 105 | +0.07pp | 0.00pp | 60.0% |
| gpt-5 | 267 | −0.29pp | −0.00pp | 47.2% |
| claude-opus-4-8 | 15 | −0.46pp | +2.00pp | 73.3% |
| gemini-3.5-flash | 28 | −0.92pp | −1.82pp | 39.3% |
| claude-sonnet-5 | 24 | −2.27pp | −2.95pp | 33.3% |

**Aged ≥ 14 days** (the only records with real signal content):

| Model | N | Avg return | Avg alpha | Alpha hit rate |
|---|---:|---:|---:|---:|
| **gpt-5** | **149** | −0.05% | **−0.05pp** | **51.0%** |
| gemini-3.5-flash | 14 | −1.08% | −0.81pp | 42.9% |
| claude-fable-5 | 12 | +0.84% | −2.09pp | 41.7% |

**Distinct picks** (dedup: earliest entry per model–ticker pair):

| Model | Distinct picks | Avg alpha | Alpha hit rate |
|---|---:|---:|---:|
| gemini-3.5-flash | 17 | +0.06pp | 52.9% |
| claude-fable-5 | 44 | −0.27pp | 50.0% |
| claude-opus-4-8 | 15 | −0.46pp | 73.3% |
| gpt-5 | 56 | −0.88pp | 48.2% |
| claude-sonnet-5 | 21 | −2.00pp | 38.1% |

### 2c. Best and worst calls (realized alpha vs SPY, distinct picks)

- **claude-fable-5** (2026-06-10 vintage, 22 days aged): ABBV **+12.7pp**, MU +6.5pp, LIN +4.4pp, LLY +3.7pp — but its investable basket also carried CVX −14.4pp, XOM −12.4pp, WMT −9.6pp. Its health-care thesis was right; its energy/staples legs were wrong.
- **gpt-5**: ABBV +13.8pp, GE +13.6pp, SHW +11.0pp, JNJ +8.6pp, HD +8.3pp vs ORCL **−24.3pp**, AMT −14.1pp, SNDK −13.8pp, COP −11.9pp, FCX −11.5pp. Widest coverage, fat tails both ways, netting to ~benchmark.
- **claude-opus-4-8** (only 2 days aged): 11/15 positive alpha (V +5.9, LIN +5.4, PG +3.9) but averaged down by MU −14.6, AMD −9.9, CAT −9.3 — it bought the semi complex the day before the AI-capex unwind.
- **gemini-3.5-flash**: LLY +10.8, LIN +7.0, UNH +6.3 vs AVGO −12.1, FCX −11.0, EQIX −8.0.
- **ETF calls**: every model that forecast SOXX a month out (µ ≈ +6%) was wrong so far — SOXX realized **−9% to −11%** on the aged calls. Systematic over-optimism on semis is the shared failure mode.

### 2d. Process quality (from the report trees)

- **claude-fable-5** produces the most rigorous package: two-source price verification (0.000% divergence, 26/26 names), explicit settlement calendar, MoM reflection with named DROP/CARRY decisions, risk-gate math (beta/correlation/drawdown caps), and honest no-trade rationale. Its CARRY discipline is verifiably good: LIN/LLY/ABBV carries all have positive interim alpha.
- **gpt-5** has the most consistent daily cadence (18 scored run-days since 06-11) and the largest evidence base, but its 100th-percentile monitor picks are currently the market's worst names (MU, INTC, AMD after an −11.6% two-session SOXX unwind).
- **claude-opus-4-8** and **gemini-3.5-flash** run competent but thinner pipelines; **claude-sonnet-5** fails data grounding outright.

### 2e. Verdict

No model has settled a single forecast yet, so this is interim evidence, but:

1. **Best forecasting evidence so far: gpt-5** — the only model with a large aged sample (149 records ≥14d), and it sits essentially benchmark-neutral (−0.05pp avg alpha, 51% hit rate). Not impressive in absolute terms, but the most statistically defensible.
2. **Best process & best individual calls: claude-fable-5** — cleanest data discipline, the single best pick in the book (ABBV), and its defensive-rotation read of the current tape has been validated by four other models' losers. Its aged average (−2.09pp, n=12) is dragged by one early basket's energy/staples legs, which it has since explicitly dropped.
3. **Too young to judge:** claude-opus-4-8 (2 days). **Middling:** gemini-3.5-flash. **Fail:** claude-sonnet-5 (fabricated holiday-session prices).

Practical read: use **gpt-5 for breadth/screening cadence** and **claude-fable-5 for final selection and risk gating**; their current disagreement (semis vs defensives) is itself informative — see below.

## 3. Which ticker to invest from 2026-07-04

Cross-model consensus among runs since 2026-06-28, fused with real fundamentals (Yahoo Finance, fetched now) and interim performance:

| Ticker | Models picking | 20d mom | Fwd P/E | Rev growth | Notes (real data) |
|---|---|---:|---:|---:|---|
| UNH | **all 5** | +13.5% | 20.3 | +2% | Earnings **7/16** inside window; price above mean analyst target |
| **V** | 4 (fable, opus, gemini, gpt-5) | +15.9% | 24.4 | +17% | **Strong-buy consensus, +10% to mean target ($399), 67% op margin, β 0.75, earnings 7/28** |
| LLY | 4 | +12.5% | 27.3 | +56% | Positive interim alpha in 3 model ledgers; at mean target |
| CAT | 4 | +4.0% | 31.9 | +22% | −9.3pp since Opus entry; earnings 8/4 |
| LIN | 3 | +8.0% | 27.7 | +8% | Fable CARRY +4.4pp alpha; β 0.72; at target |
| ABBV | 2 | +20.2% | 16.1 | +12% | Best realized alpha in the book (+13pp); 2.65% yield, β ≈ −0.4; extended, earnings 7/31 |
| MU | 3 | −9.6% | **6.5** | +346% | GPT-5's #1 monitor; analyst mean target +52%; σ ≈ 36%/mo, β 2.1, earnings 9/23 |
| DVA / HUM / PANW | fable top-3 | +20–24% | 13.7 / 25.2 / 84.5 | — | Momentum leaders but price sits **17–23% above mean analyst targets** — chase risk |

### Recommendation (entries executable Monday 2026-07-06)

**Primary pick: V (Visa) — $362.13.** It is the only name that clears every screen simultaneously: 4-of-5 model consensus, +5.9pp interim alpha since the Opus entry, real fundamentals to back it (17% revenue growth, 67% operating margin, 36% EPS growth), analyst strong-buy with ~10% upside to the mean target — the only consensus name where the Street target is meaningfully *above* price — moderate beta (0.75) suiting the defensive regime, and no earnings until 7/28 (outside the immediate risk window).

**Core defensive pair alongside: LLY ($1,213.91) and LIN ($546.64).** Both are multi-model consensus, both carry verified positive interim alpha in the ledgers (LLY +3.7 to +10.8pp across three models; LIN +4.4 to +7.0pp), both are low-beta fits for the defensive rotation every model's regime read agrees on. They are at analyst mean targets, so treat as carry/compounder positions, not upside bets.

**Income/hedge satellite: ABBV ($261.07).** The single best realized call in the entire prediction book, negative beta, 16× forward earnings, 2.65% yield — but +20% in 20 days and earnings 7/31, so enter half-size or wait for a pullback.

**Avoid despite consensus: UNH** (all 5 models, but earnings 7/16 lands inside the holding window and price is above the mean target — exactly why claude-fable-5 downgraded it) and **CAT** (4 models but −9pp tape damage since entry). **Avoid the momentum chase:** DVA/HUM/PANW trade 17–23% above analyst mean targets.

**High-risk contrarian (only with speculative sizing, ≤2%): MU ($975.56).** GPT-5's top-scored name, 6.5× forward earnings after +346% revenue growth, mean target implies +52% — but it is mid-unwind (−9.6% in 20d, β 2.1, ~36% monthly vol) and every model's SOXX optimism has been wrong for a month. If taken, treat as a 2026-09-23-earnings story, not a July trade.

### Risk calendar
- Mon 7/06: first session after the holiday — weekend gap risk on all 7/02 reference prices.
- Wed 7/08: first prediction settlements (2026-06-10 vintage) — first *real* model accuracy data.
- 7/15–7/16: JNJ, UNH, GE earnings; 7/28–29: **FOMC** + V earnings; 7/31: ABBV, LIN earnings.

### Caveats
All model comparison here is interim mark-to-market with unequal sample sizes and windows; no forecast has reached its target date. Sonnet-5 numbers are unreliable at the source. Analyst targets and fundamentals are point-in-time Yahoo Finance data. Nothing here is a trade instruction; every run in the tree finished `REVIEW_ONLY`/`NO_TRADE`.
