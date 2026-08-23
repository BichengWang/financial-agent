# 07 — Portfolio Proposal · 2026-08-14

## Outcome: `NO_TRADE` — no weights drafted

`agents.md § Portfolio Construction Agent` Task 0 requires a constraint feasibility pre-check
**before any sizing**. That pre-check ran, and the run terminated at the evidence-threshold
gate rather than the feasibility gate. No weights were drafted, so the single revision pass
between portfolio construction and the risk committee is untouched.

## Task 0 — constraint feasibility pre-check

The pre-check asks a narrow question: *ignoring score quality, could any weighting of the
eligible pool satisfy the hard caps?*

| Constraint | Requirement | Attainable from the pctl>=80 pool (n=103) | Feasible |
|---|---|---|---|
| Sleeve beta | 0.90 – 1.10 | **[-0.2791, +1.5397]** | **Yes** |
| Single-name weight | <= 5% | implies >= 20 names | Yes |
| Sector concentration | <= 30% | pool spans 7 sectors | Yes |

**The beta band is feasible this run** — the fifth consecutive run for which it is. The
"provably infeasible" narrative from 2026-07-27 (when the maximum attainable sleeve beta was
+0.8519, below the 0.90 floor) does **not** apply and was recomputed rather than reused. The
maximum attainable beta is the mean of the 20 highest betas in the >=80th-percentile pool under
the 5% single-name cap.

## Why there is still no portfolio

Feasibility is necessary, not sufficient. The blocking constraint is
`rules.md § Evidence Thresholds`:

| Threshold | Requirement | This run | Pass |
|---|---|---|---|
| 1. Percentile | >= 80th | up to 100.00 | Yes |
| 2. Families non-negative | >= 3 of 4 | **2 of 4** | **No** |
| 3. Family conviction share | <= 50% | **66.7%** Technical | **No** |
| 4. Data completeness | >= 85% | **80%** | **No** |
| 5. Hard stops | none | none | Yes |

With zero names investable, the minimum investable count of 5 cannot be met, which is
`rules.md § Downgrade to NO_TRADE` trigger 1. `agents.md` is explicit: *never force a
portfolio*.

## Naive top-20 equal-weight sleeve — diagnostic only

This is **not a proposal**. It is computed so the risk numbers a `GO` portfolio would have had
to clear are on the record, from the same 60-day fetched adjusted returns
(`rules.md § Computed Risk Analytics`).

| Analytic | Value | Cap | Status |
|---|---|---|---|
| Portfolio beta to SPY | **+0.4785** | 0.90 – 1.10 | **FAIL** (too defensive) |
| Average pairwise correlation | 0.1386 | < 0.45 | PASS |
| Portfolio sigma (1-month) | 4.02% | — | — |
| 95th-pctl 1-month drawdown | 6.64% | <= 8% | PASS |
| Tracking error (1-month) | 3.54% | — | — |
| Max sector weight | 40.0% (Finance) | <= 30% | **FAIL** |

Method: 95th-percentile drawdown is the parametric estimate `1.65 x portfolio_sigma_1m`
(normality assumed and stated); portfolio sigma is `sqrt(w' Σ w)` from the fetched 60-day
covariance matrix scaled by `sqrt(21)`; tracking error is the standard deviation of
beta-adjusted residual returns versus SPY over the same window, scaled to one month.

**Two independent failures.** Even setting the evidence thresholds aside, the naive sleeve
would have needed a revision pass: its beta of +0.4785 sits far below the
0.90 floor, and Finance at 40.0% breaches the 30% sector cap. The
beta failure is the mechanical consequence of a technical-momentum screen in this tape
selecting defensives — 10 of
the 24 published names carry a beta below 0.50.

### Sector concentration (equal weight, top 20)

| Sector | Equal weight | vs 30% cap |
|---|---|---|
| Finance | 40.0% | **BREACH** |
| Health Care | 30.0% | OK |
| Consumer Discretionary | 15.0% | OK |
| Industrials | 10.0% | OK |
| Technology | 5.0% | OK |

### Correlation structure

Average pairwise correlation across the top-20 60-day return series is
**0.1386**, well inside the 0.45 cap — unsurprising for a book
spanning 5 sectors with low average beta. Factor crowding is
nonetheless real in a sense the correlation number does not capture: every name was selected by
the same two families, so the book loads on one factor family by construction. That is flagged
per `rules.md § Risk Controls` ("flag factor crowding if more than half the portfolio loads on
one factor family").

## Per-position Recommendation Metrics Table

Inherited from `05` with no recomputation.

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NTAP | 207.08 | 2026-08-14 | `HISTORICAL` | 219.50 | 2026-09-11 | +6.00% | 12.73% | `REALIZED_VOL_30D` | 0.447 | 0.673 | 0.175 | 0.926 | -15.00% | -20.22% | -15.81% | SELL9 / SELL6 / SELL5 | 77 / 80 / 75 | A / A / A | 192.09 | 246.92 | (0.30x0.00 UNAVL + 0.30x+1.311 + 0.25x0.00 UNAVL + 0.15x+0.914) x 0.80 - 0.00 = +0.4243 | `L101`, `L201`, `L301`, `L401` |
| CRL | 280.05 | 2026-08-14 | `HISTORICAL` | 296.85 | 2026-09-11 | +6.00% | 13.51% | `REALIZED_VOL_30D` | 0.421 | 1.711 | 0.361 | 0.821 | -16.30% | -21.84% | -6.38% | SELL8 / SELL9 / SELL3 | 76 / 75 / 65 | A / A / A | 257.49 | 336.21 | (0.30x0.00 UNAVL + 0.30x+1.338 + 0.25x0.00 UNAVL + 0.15x+0.246) x 0.80 - 0.00 = +0.3507 | `L102`, `L202`, `L302`, `L402` |
| MDT | 91.27 | 2026-08-14 | `HISTORICAL` | 96.75 | 2026-09-11 | +6.00% | 7.65% | `REALIZED_VOL_30D` | 0.744 | 0.919 | 0.721 | 2.564 | -6.62% | -9.76% | -6.17% | SELL8 / SELL9 / SELL1 | 71 / 61 / 53 | A / A / b | 89.49 | 104.01 | (0.30x0.00 UNAVL + 0.30x+0.992 + 0.25x0.00 UNAVL + 0.15x+0.723) x 0.80 - 0.00 = +0.3247 | `L103`, `L203`, `L303`, `L403` |
| AME | 254.79 | 2026-08-14 | `HISTORICAL` | 270.08 | 2026-09-11 | +6.00% | 5.94% | `REALIZED_VOL_30D` | 0.959 | 1.644 | 0.764 | 4.257 | -3.79% | -6.23% | -4.38% | SELL4 / SELL4 / SELL9 | 63 / 73 / 70 | A / A / A | 254.35 | 285.81 | (0.30x0.00 UNAVL + 0.30x+1.105 + 0.25x0.00 UNAVL + 0.15x+0.470) x 0.80 - 0.00 = +0.3216 | `L104`, `L204`, `L304`, `L404` |
| KKR | 114.01 | 2026-08-14 | `HISTORICAL` | 120.85 | 2026-09-11 | +6.00% | 11.31% | `REALIZED_VOL_30D` | 0.503 | 1.072 | 0.395 | 1.174 | -12.65% | -17.29% | -10.13% | SELL4 / SELL7 / SELL3 | 69 / 62 / 52 | A / A / b | 107.45 | 134.26 | (0.30x0.00 UNAVL + 0.30x+1.059 + 0.25x0.00 UNAVL + 0.15x+0.404) x 0.80 - 0.00 = +0.3026 | `L105`, `L205`, `L305`, `L405` |
| DXCM | 89.75 | 2026-08-14 | `HISTORICAL` | 95.14 | 2026-09-11 | +6.00% | 14.94% | `REALIZED_VOL_30D` | 0.381 | 0.931 | 0.366 | 0.672 | -18.65% | -24.77% | -13.86% | SELL5 / SELL5 / SELL2 | 67 / 70 / 54 | A / A / A | 81.19 | 109.08 | (0.30x0.00 UNAVL + 0.30x+0.985 + 0.25x0.00 UNAVL + 0.15x+0.435) x 0.80 - 0.00 = +0.2886 | `L106`, `L206`, `L306`, `L406` |
| ABNB | 184.06 | 2026-08-14 | `HISTORICAL` | 195.10 | 2026-09-11 | +6.00% | 16.82% | `REALIZED_VOL_30D` | 0.338 | 1.208 | 0.340 | 0.530 | -21.75% | -28.64% | -7.63% | BUY1 / SELL3 / SELL9 | 75 / 77 / 67 | A / A / A | 162.91 | 227.29 | (0.30x0.00 UNAVL + 0.30x+1.298 + 0.25x0.00 UNAVL + 0.15x-0.207) x 0.80 - 0.00 = +0.2866 | `L107`, `L207`, `L307`, `L407` |
| WTW | 331.59 | 2026-08-14 | `HISTORICAL` | 351.49 | 2026-09-11 | +6.00% | 8.64% | `REALIZED_VOL_30D` | 0.659 | 1.945 | 0.796 | 2.009 | -8.26% | -11.80% | -4.15% | BUY2 / SELL8 / SELL2 | 63 / 63 / 59 | b / A / b | 321.69 | 381.28 | (0.30x0.00 UNAVL + 0.30x+1.006 + 0.25x0.00 UNAVL + 0.15x+0.358) x 0.80 - 0.00 = +0.2845 | `L108`, `L208`, `L308`, `L408` |
| EXPE | 332.69 | 2026-08-14 | `HISTORICAL` | 352.65 | 2026-09-11 | +6.00% | 11.56% | `REALIZED_VOL_30D` | 0.492 | 0.934 | 0.438 | 1.123 | -13.07% | -17.81% | -5.25% | SELL9 / SELL3 / SELL3 | 74 / 72 / 71 | A / A / A | 312.66 | 392.65 | (0.30x0.00 UNAVL + 0.30x+1.233 + 0.25x0.00 UNAVL + 0.15x-0.112) x 0.80 - 0.00 = +0.2826 | `L109`, `L209`, `L309`, `L409` |
| JCI | 153.64 | 2026-08-14 | `HISTORICAL` | 162.86 | 2026-09-11 | +6.00% | 7.14% | `REALIZED_VOL_30D` | 0.798 | 2.238 | 0.407 | 2.946 | -5.77% | -8.70% | -6.62% | SELL1 / SELL4 / SELL9 | 61 / 66 / 73 | A / B+ / A | 151.46 | 174.26 | (0.30x0.00 UNAVL + 0.30x+0.664 + 0.25x0.00 UNAVL + 0.15x+0.978) x 0.80 - 0.00 = +0.2767 | `L110`, `L210`, `L310`, `L410` |
| BAC | 64.49 | 2026-08-14 | `HISTORICAL` | 68.36 | 2026-09-11 | +6.00% | 5.12% | `REALIZED_VOL_30D` | 1.111 | 1.393 | 1.045 | 5.721 | -2.45% | -4.55% | -2.74% | SELL9 / SELL9 / SELL3 | 68 / 75 / 74 | A / A / A | 64.93 | 71.79 | (0.30x0.00 UNAVL + 0.30x+0.851 + 0.25x0.00 UNAVL + 0.15x+0.592) x 0.80 - 0.00 = +0.2753 | `L111`, `L211`, `L311`, `L411` |
| MRK | 135.84 | 2026-08-14 | `HISTORICAL` | 143.99 | 2026-09-11 | +6.00% | 6.91% | `REALIZED_VOL_30D` | 0.823 | 1.400 | 0.804 | 3.137 | -5.41% | -8.24% | -6.78% | SELL6 / SELL8 / SELL9 | 69 / 67 / 70 | A / A / A | 134.22 | 153.76 | (0.30x0.00 UNAVL + 0.30x+0.817 + 0.25x0.00 UNAVL + 0.15x+0.633) x 0.80 - 0.00 = +0.2720 | `L112`, `L212`, `L312`, `L412` |
| SOLV | 88.59 | 2026-08-14 | `HISTORICAL` | 93.91 | 2026-09-11 | +6.00% | 10.94% | `REALIZED_VOL_30D` | 0.520 | 1.037 | 0.598 | 1.253 | -12.05% | -16.54% | -10.79% | SELL3 / SELL3 / SELL3 | 63 / 63 / 61 | B+ / A / `UNAVL` | 83.83 | 103.98 | (0.30x0.00 UNAVL + 0.30x+1.055 + 0.25x0.00 UNAVL + 0.15x+0.042) x 0.80 - 0.00 = +0.2582 | `L113`, `L213`, `L313`, `L413` |
| BX | 143.93 | 2026-08-14 | `HISTORICAL` | 152.57 | 2026-09-11 | +6.00% | 10.86% | `REALIZED_VOL_30D` | 0.524 | 1.233 | 0.360 | 1.271 | -11.92% | -16.38% | -11.64% | SELL9 / SELL7 / SELL3 | 64 / 64 / 55 | A / A / b | 136.31 | 168.83 | (0.30x0.00 UNAVL + 0.30x+0.720 + 0.25x0.00 UNAVL + 0.15x+0.672) x 0.80 - 0.00 = +0.2535 | `L114`, `L214`, `L314`, `L414` |
| URI | 1,153.83 | 2026-08-14 | `HISTORICAL` | 1,223.06 | 2026-09-11 | +6.00% | 12.35% | `REALIZED_VOL_30D` | 0.461 | 1.210 | 0.432 | 0.983 | -14.38% | -19.45% | -11.13% | SELL1 / SELL2 / SELL5 | 59 / 64 / 68 | A / A / A | 1,074.81 | 1,371.31 | (0.30x0.00 UNAVL + 0.30x+0.971 + 0.25x0.00 UNAVL + 0.15x+0.161) x 0.80 - 0.00 = +0.2523 | `L115`, `L215`, `L315`, `L415` |
| SCHW | 111.09 | 2026-08-14 | `HISTORICAL` | 117.76 | 2026-09-11 | +6.00% | 5.52% | `REALIZED_VOL_30D` | 1.030 | 1.671 | 0.908 | 4.914 | -3.12% | -5.38% | -7.04% | SELL3 / SELL9 / SELL2 | 76 / 72 / 68 | A / A / B+ | 111.37 | 124.14 | (0.30x0.00 UNAVL + 0.30x+0.676 + 0.25x0.00 UNAVL + 0.15x+0.740) x 0.80 - 0.00 = +0.2510 | `L116`, `L216`, `L316`, `L416` |
| STT | 191.74 | 2026-08-14 | `HISTORICAL` | 203.24 | 2026-09-11 | +6.00% | 7.00% | `REALIZED_VOL_30D` | 0.813 | 1.347 | 0.734 | 3.062 | -5.55% | -8.42% | -5.65% | SELL9 / SELL9 / SELL9 | 67 / 88 / 89 | B+ / A / A | 189.29 | 217.20 | (0.30x0.00 UNAVL + 0.30x+0.676 + 0.25x0.00 UNAVL + 0.15x+0.737) x 0.80 - 0.00 = +0.2506 | `L117`, `L217`, `L317`, `L417` |
| AMGN | 415.21 | 2026-08-14 | `HISTORICAL` | 440.12 | 2026-09-11 | +6.00% | 7.78% | `REALIZED_VOL_30D` | 0.732 | 2.094 | 0.770 | 2.479 | -6.83% | -10.02% | -5.05% | BUY1 / SELL8 / SELL2 | 70 / 71 / 69 | A / A / A | 406.54 | 473.71 | (0.30x0.00 UNAVL + 0.30x+0.884 + 0.25x0.00 UNAVL + 0.15x+0.306) x 0.80 - 0.00 = +0.2490 | `L118`, `L218`, `L318`, `L418` |
| FITB | 58.06 | 2026-08-14 | `HISTORICAL` | 61.54 | 2026-09-11 | +6.00% | 5.73% | `REALIZED_VOL_30D` | 0.993 | 1.151 | 0.788 | 4.564 | -3.46% | -5.81% | -4.83% | SELL3 / SELL2 / SELL9 | 59 / 66 / 71 | b / A / A | 58.08 | 65.01 | (0.30x0.00 UNAVL + 0.30x+0.618 + 0.25x0.00 UNAVL + 0.15x+0.785) x 0.80 - 0.00 = +0.2425 | `L119`, `L219`, `L319`, `L419` |
| BNY | 163.24 | 2026-08-14 | `HISTORICAL` | 173.03 | 2026-09-11 | +6.00% | 6.98% | `REALIZED_VOL_30D` | 0.815 | 1.585 | 0.802 | 3.074 | -5.53% | -8.39% | -5.69% | SELL9 / SELL9 / SELL9 | 67 / 83 / 91 | A / A / A | 161.18 | 184.89 | (0.30x0.00 UNAVL + 0.30x+0.686 + 0.25x0.00 UNAVL + 0.15x+0.625) x 0.80 - 0.00 = +0.2396 | `L120`, `L220`, `L320`, `L420` |
| IVZ | 32.55 | 2026-08-14 | `HISTORICAL` | 34.50 | 2026-09-11 | +6.00% | 11.19% | `REALIZED_VOL_30D` | 0.508 | 1.137 | 0.306 | 1.197 | -12.47% | -17.06% | -11.40% | SELL2 / SELL6 / SELL9 | 67 / 71 / 72 | A / A / A | 30.71 | 38.29 | (0.30x0.00 UNAVL + 0.30x+0.855 + 0.25x0.00 UNAVL + 0.15x+0.282) x 0.80 - 0.00 = +0.2390 | `L121`, `L221`, `L321`, `L421` |
| DASH | 217.02 | 2026-08-14 | `HISTORICAL` | 230.04 | 2026-09-11 | +6.00% | 12.32% | `REALIZED_VOL_30D` | 0.462 | 0.803 | 0.272 | 0.988 | -14.33% | -19.39% | -13.26% | SELL1 / SELL3 / SELL3 | 68 / 62 / 57 | A / A / b | 202.23 | 257.86 | (0.30x0.00 UNAVL + 0.30x+0.846 + 0.25x0.00 UNAVL + 0.15x+0.274) x 0.80 - 0.00 = +0.2359 | `L122`, `L222`, `L322`, `L422` |
| TECH | 72.40 | 2026-08-14 | `HISTORICAL` | 76.74 | 2026-09-11 | +6.00% | 1.31% | `REALIZED_VOL_30D` | 4.356 | 6.765 | 0.326 | 87.887 | +3.84% | +3.31% | -4.02% | SELL1 / SELL9 / SELL3 | 72 / 66 / 55 | b / A / A | 75.76 | 77.73 | (0.30x0.00 UNAVL + 0.30x+0.495 + 0.25x0.00 UNAVL + 0.15x+0.951) x 0.80 - 0.00 = +0.2329 | `L123`, `L223`, `L323`, `L423` |
| REGN | 803.48 | 2026-08-14 | `HISTORICAL` | 851.69 | 2026-09-11 | +6.00% | 8.92% | `REALIZED_VOL_30D` | 0.638 | 1.308 | 0.653 | 1.884 | -8.72% | -12.38% | -7.56% | BUY1 / SELL8 / SELL1 | 77 / 65 / 55 | A / A / A | 777.13 | 926.24 | (0.30x0.00 UNAVL + 0.30x+0.731 + 0.25x0.00 UNAVL + 0.15x+0.474) x 0.80 - 0.00 = +0.2323 | `L124`, `L224`, `L324`, `L424` |

## Excluded names

No name was excluded by portfolio construction, because no portfolio was constructed. The
4 names excluded at the universe stage are logged in `04` with reasons.
Names ranked 25 and below are outside the publication cut, not rejected — they
remain in the scored universe and in the percentile denominator.
