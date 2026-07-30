# 02 — Reflection — 2026-07-30

## 0. Prediction Settlement

All **58** due predictions were settled this run (49 `EQUITY_ALPHA`,
9 `MARKET_FORECAST`). Every due key carried `target_date == 2026-07-30` — equal to the
run date — and this run fires at 2026-07-30T10:06:00-04:00, **before** the 2026-07-30 close. `rules.md § Settlement
Rules` therefore mandates the `TARGET_EQ_RUN_DATE` exception: settle at the latest completed
close, **2026-07-29**. No intraday print was used, and no key was held open past its target date.

Ledger files scanned: every `15_predictions.json` under `agents/equity/output/` (all models,
69 packages). Normalization, timing validation and precedence
are `settlement_ledger.py`'s output, not hand-derived.

Verification: re-running `settlement_ledger.py --as-of 2026-07-30` after writing this run's
settlements returns **`due_inventory: 0`, `conflicts: 0`** — every settlement was accepted by
the validator.

### Settled — `EQUITY_ALPHA`

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| BAX | claude-fable-5:2026-07-02 | 22.55 | 2026-07-30 | +6.00% | +9.84% | -1.64% | +11.48% | HIT | IN_CI | +0.36 |
| CCEP | claude-fable-5:2026-07-02 | 106.37 | 2026-07-30 | +6.00% | +4.45% | -1.64% | +6.08% | HIT | IN_CI | -0.21 |
| DOC | claude-fable-5:2026-07-02 | 21.77 | 2026-07-30 | +6.00% | +3.26% | -1.64% | +4.90% | HIT | IN_CI | -0.34 |
| DVA | claude-fable-5:2026-07-02 | 233.71 | 2026-07-30 | +5.00% | +3.10% | -1.64% | +4.74% | HIT | IN_CI | -0.28 |
| SWK | claude-fable-5:2026-07-02 | 90.89 | 2026-07-30 | +6.00% | +2.38% | -1.64% | +4.01% | HIT | IN_CI | -0.31 |
| ABBV | claude-fable-5:2026-07-02 | 260.96 | 2026-07-30 | +3.00% | +0.90% | -1.64% | +2.53% | HIT | IN_CI | -0.22 |
| LLY | claude-fable-5:2026-07-02 | 1211.90 | 2026-07-30 | +4.00% | -0.16% | -1.64% | +1.48% | HIT | IN_CI | -0.42 |
| HSIC | claude-fable-5:2026-07-02 | 85.97 | 2026-07-30 | +6.00% | -0.16% | -1.64% | +1.47% | HIT | OUT_CI_LOW | -1.08 |
| LYV | claude-fable-5:2026-07-02 | 185.09 | 2026-07-30 | +6.00% | -0.36% | -1.64% | +1.28% | HIT | IN_CI | -0.99 |
| MNST | claude-fable-5:2026-07-02 | 97.86 | 2026-07-30 | +5.00% | -0.64% | -1.64% | +0.99% | HIT | OUT_CI_LOW | -1.20 |
| GPC | claude-fable-5:2026-07-02 | 131.88 | 2026-07-30 | +5.00% | -1.44% | -1.64% | +0.20% | HIT | IN_CI | -0.52 |
| FTNT | claude-fable-5:2026-07-02 | 157.64 | 2026-07-30 | +5.00% | -2.80% | -1.64% | -1.17% | MISS | IN_CI | -0.63 |
| URI | claude-fable-5:2026-07-02 | 1090.01 | 2026-07-30 | +6.00% | -3.20% | -1.64% | -1.56% | MISS | IN_CI | -0.93 |
| BEN | claude-fable-5:2026-07-02 | 33.62 | 2026-07-30 | +5.00% | -3.66% | -1.64% | -2.02% | MISS | IN_CI | -1.04 |
| FFIV | claude-fable-5:2026-07-02 | 406.05 | 2026-07-30 | +6.00% | -4.70% | -1.64% | -3.07% | MISS | OUT_CI_LOW | -1.22 |
| KDP | claude-fable-5:2026-07-02 | 33.15 | 2026-07-30 | +6.00% | -5.13% | -1.64% | -3.49% | MISS | OUT_CI_LOW | -1.64 |
| LIN | claude-fable-5:2026-07-02 | 544.77 | 2026-07-30 | +3.00% | -6.17% | -1.64% | -4.53% | MISS | OUT_CI_LOW | -1.56 |
| HUM | claude-fable-5:2026-07-02 | 394.07 | 2026-07-30 | +5.00% | -7.27% | -1.64% | -5.64% | MISS | OUT_CI_LOW | -1.06 |
| WST | claude-fable-5:2026-07-02 | 366.19 | 2026-07-30 | +5.00% | -7.85% | -1.64% | -6.21% | MISS | OUT_CI_LOW | -1.85 |
| PANW | claude-fable-5:2026-07-02 | 350.84 | 2026-07-30 | +5.00% | -10.46% | -1.64% | -8.82% | MISS | IN_CI | -0.96 |
| MAS | claude-fable-5:2026-07-02 | 82.00 | 2026-07-30 | +6.00% | -11.51% | -1.64% | -9.88% | MISS | OUT_CI_LOW | -1.89 |
| LII | claude-fable-5:2026-07-02 | 563.65 | 2026-07-30 | +6.00% | -23.71% | -1.64% | -22.07% | MISS | OUT_CI_LOW | -2.84 |
| MRNA | claude-fable-5:2026-07-02 | 78.66 | 2026-07-30 | +5.00% | -30.73% | -1.64% | -29.09% | MISS | OUT_CI_LOW | -1.62 |
| MCK | claude-sonnet-5:2026-07-02 | 768.06 | 2026-07-30 | +2.00% | +15.69% | -2.27% | +17.96% | HIT | OUT_CI_HIGH | +2.01 |
| AAPL | claude-sonnet-5:2026-07-02 | 294.02 | 2026-07-30 | +2.00% | +15.02% | -2.27% | +17.29% | HIT | OUT_CI_HIGH | +1.48 |
| MSFT | claude-sonnet-5:2026-07-02 | 382.92 | 2026-07-30 | +3.00% | +1.99% | -2.27% | +4.26% | HIT | IN_CI | -0.09 |
| PG | claude-sonnet-5:2026-07-02 | 147.66 | 2026-07-30 | +2.00% | -1.06% | -2.27% | +1.21% | HIT | IN_CI | -0.44 |
| UNH | claude-sonnet-5:2026-07-02 | 426.05 | 2026-07-30 | +1.00% | -1.29% | -2.27% | +0.98% | HIT | IN_CI | -0.29 |
| META | claude-sonnet-5:2026-07-02 | 604.30 | 2026-07-30 | +6.00% | -3.09% | -2.27% | -0.82% | MISS | IN_CI | -0.67 |
| PLTR | claude-sonnet-5:2026-07-02 | 128.13 | 2026-07-30 | +4.00% | -4.00% | -2.27% | -1.73% | MISS | IN_CI | -0.42 |
| GOOGL | claude-sonnet-5:2026-07-02 | 357.20 | 2026-07-30 | +1.00% | -5.74% | -2.27% | -3.47% | MISS | IN_CI | -0.71 |
| AMZN | claude-sonnet-5:2026-07-02 | 241.00 | 2026-07-30 | +1.00% | -5.95% | -2.27% | -3.68% | MISS | IN_CI | -0.68 |
| AMD | claude-sonnet-5:2026-07-02 | 546.50 | 2026-07-30 | +5.00% | -21.40% | -2.27% | -19.13% | MISS | OUT_CI_LOW | -1.14 |
| CAT | claude-sonnet-5:2026-07-02 | 998.00 | 2026-07-30 | +4.00% | -21.57% | -2.27% | -19.30% | MISS | OUT_CI_LOW | -1.68 |
| MU | claude-sonnet-5:2026-07-02 | 1054.15 | 2026-07-30 | +6.00% | -29.90% | -2.27% | -27.63% | MISS | IN_CI | -1.00 |
| DDOG | gpt-5:2026-07-02 | 259.90 | 2026-07-30 | +6.00% | +1.66% | -2.01% | +3.66% | HIT | IN_CI | -0.24 |
| DELL | gpt-5:2026-07-02 | 393.69 | 2026-07-30 | +6.00% | -6.11% | -2.01% | -4.10% | MISS | IN_CI | -0.34 |
| HUM | gpt-5:2026-07-02 | 402.05 | 2026-07-30 | +6.00% | -9.11% | -2.01% | -7.10% | MISS | OUT_CI_LOW | -1.36 |
| CNC | gpt-5:2026-07-02 | 68.19 | 2026-07-30 | +6.00% | -9.33% | -2.01% | -7.33% | MISS | OUT_CI_LOW | -1.24 |
| PANW | gpt-5:2026-07-02 | 350.10 | 2026-07-30 | +6.00% | -10.27% | -2.01% | -8.26% | MISS | IN_CI | -1.01 |
| AMD | gpt-5:2026-07-02 | 519.41 | 2026-07-30 | +6.00% | -17.30% | -2.01% | -15.29% | MISS | IN_CI | -1.00 |
| MU | gpt-5:2026-07-02 | 986.00 | 2026-07-30 | +6.00% | -25.05% | -2.01% | -23.04% | MISS | IN_CI | -0.85 |
| FLEX | gpt-5:2026-07-02 | 140.62 | 2026-07-30 | +6.00% | -26.74% | -2.01% | -24.73% | MISS | OUT_CI_LOW | -1.49 |
| AMAT | gpt-5:2026-07-02 | 599.07 | 2026-07-30 | +6.00% | -27.15% | -2.01% | -25.14% | MISS | OUT_CI_LOW | -1.23 |
| ARM | gpt-5:2026-07-02 | 319.58 | 2026-07-30 | +6.00% | -29.63% | -2.01% | -27.62% | MISS | IN_CI | -0.99 |
| MRNA | gpt-5:2026-07-02 | 78.67 | 2026-07-30 | +6.00% | -30.73% | -2.01% | -28.72% | MISS | OUT_CI_LOW | -1.66 |
| INTC | gpt-5:2026-07-02 | 121.95 | 2026-07-30 | +6.00% | -32.86% | -2.01% | -30.85% | MISS | OUT_CI_LOW | -1.49 |
| MRVL | gpt-5:2026-07-02 | 249.32 | 2026-07-30 | +6.00% | -34.46% | -2.01% | -32.45% | MISS | IN_CI | -0.97 |
| SNDK | gpt-5:2026-07-02 | 1808.04 | 2026-07-30 | +6.00% | -43.81% | -2.01% | -41.80% | MISS | OUT_CI_LOW | -1.31 |

### Settled — `MARKET_FORECAST` (raw-return scoring, no alpha)

| Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | claude-fable-5:2026-07-02 | 708.64 | 2026-07-30 | +0.30% | -6.62% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.81 |
| SOXX | claude-fable-5:2026-07-02 | 556.60 | 2026-07-30 | +0.16% | -16.46% | N/A | N/A | N/A - FLAT_CALL | IN_CI | -0.74 |
| SPY | claude-fable-5:2026-07-02 | 741.60 | 2026-07-30 | +0.50% | -1.64% | N/A | N/A | MISS | IN_CI | -0.48 |
| QQQ | claude-sonnet-5:2026-07-02 | 725.59 | 2026-07-30 | +2.37% | -8.80% | N/A | N/A | MISS | OUT_CI_LOW | -1.34 |
| SOXX | claude-sonnet-5:2026-07-02 | 599.50 | 2026-07-30 | +3.35% | -22.44% | N/A | N/A | MISS | OUT_CI_LOW | -1.21 |
| SPY | claude-sonnet-5:2026-07-02 | 746.40 | 2026-07-30 | +1.50% | -2.27% | N/A | N/A | MISS | IN_CI | -0.85 |
| QQQ | gpt-5:2026-07-02 | 715.13 | 2026-07-30 | +0.79% | -7.47% | N/A | N/A | MISS | IN_CI | -0.98 |
| SOXX | gpt-5:2026-07-02 | 573.10 | 2026-07-30 | +2.00% | -18.86% | N/A | N/A | MISS | IN_CI | -0.96 |
| SPY | gpt-5:2026-07-02 | 744.41 | 2026-07-30 | +0.50% | -2.01% | N/A | N/A | MISS | IN_CI | -0.57 |

### This batch

| Metric | `EQUITY_ALPHA` (n=49) | `MARKET_FORECAST` (n=9) |
|---|---|---|
| Direction | 34.7% HIT | 0/7 HIT (2 `FLAT_CALL`) |
| CI coverage | 57.1% | 77.8% |
| Mean z | -0.8424 | -0.8812 |
| Mean realized return | -9.35% | -9.62% |

The batch is poor and the reason is a single factor event, not 49 independent errors:
between **2026-07-02** and **2026-07-29** semiconductors and
AI hardware collapsed while SPY fell only -2.06% (SOXX -17.89%, QQQ -7.14%). The
11 semi/AI names in this batch averaged **-29.36%**.

Worst: SNDK -43.81%, MRVL -34.46%, INTC -32.86%, MRNA -30.73%, MRNA -30.73%, MU -29.90%, ARM -29.63%, AMAT -27.15%.
Best: MCK +15.69%, AAPL +15.02%, BAX +9.84%, CCEP +4.45%, DOC +3.26%.

### Rolling calibration metrics (canonical, post-settlement)

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy range |
|---|---|---|---|
| Raw `n` | 347 | 63 | ≥ 20 for Track A |
| 28-day `eff_n` | **1** | **1** | ≥ 3 for Track A |
| Hit rate | 47.84% | 16.39% | > 50% |
| CI coverage | 72.05% | 73.02% | 55–85% |
| Mean z | -0.3419 | -0.7156 | −0.5 to +0.5 |
| Rank IC (weighted mean by vintage) | **-0.1975** | n/a | > 0 |
| Track A calibration eligible | `INSUFFICIENT_EFFECTIVE_N` | `INSUFFICIENT_EFFECTIVE_N` | needs both gates |

Reading these correctly matters, because they fail in *different* ways:

- **Magnitude calibration is acceptable.** CI coverage 72.05% sits inside
  the 55–85% band and mean z -0.3419 inside ±0.5. No sigma-widening or mu-shrink is
  indicated — and per the 2026-07-26 finding, a monotonic mu/sigma transform **cannot** fix the
  problem that follows.
- **Rank ordering is inverted.** Weighted-mean rank IC is -0.1975, and
  19
  of 23 vintages are ≤ 0. The composite score is
  not merely mis-scaled; it ranks the wrong names first.

Per `rules.md`, rank IC ≤ 0 over ≥ 20 settled predictions **caps all confidence at `MEDIUM`**
for this run's scoring — applied in `05`. A Track A corrective is **DEFERRED**, not rejected:
`eff_n` = 1 < 3.

## 1. Prior Run Summary — and the baseline tie

The MoM window (2026-06-15 → 2026-07-09, target 2026-07-02) contains
**38** packages but **no `claude-opus-5` package**, so the baseline is
`CROSS_MODEL_BASELINE`. Three folders tie at **delta 0d** from target:

| Tied candidate | Predictions | Settled here | Hit rate | Mean alpha | Mean z |
|---|---|---|---|---|---|
| `claude-fable-5-2026-07-02` ← **selected** | 26 | 23 | 47.8% | -2.54% | -0.9764 |
| `claude-sonnet-5-2026-07-02` | 15 | 12 | 41.7% | -2.84% | -0.3034 |
| `gpt-5-2026-07-02` | 17 | 14 | 7.1% | -19.48% | -1.0843 |

**The tie is decision-relevant and the conclusion is NOT invariant.** Hit rates span
7.1% to 47.8% —
a **40.7pp** spread —
and mean alpha spans -19.48% to
-2.54%. The cause is composition, not luck: the books
barely overlap (claude-fable-5 ∩ gpt-5 = 3 names; claude-fable-5 ∩ claude-sonnet-5 = 0), and
gpt-5's was semiconductor-heavy into the exact window semis collapsed.

`agents.md § Orchestrator Step 2` still has **no tie-break rule**. This is the third
consecutive evolution log to flag it (2026-07-28, 2026-07-29, today) and it is carried as this
run's Track B change in `13_evolution_log.md`. Selection applied here: same model family →
usable `15_predictions.json` → lexicographic ⇒ **`claude-fable-5-2026-07-02`**. All tied
candidates are reported above, as the rule requires.

Prior run (`claude-fable-5-2026-07-02`): status per that package's own manifest; its
23 settled predictions returned -4.17% on average
against SPY -2.06%.

## 2. MoM Price & Return Table

Alpha-based Hit/Miss per `rules.md § Settlement Rules`; every price is the 2026-07-29 close from
`01` ledger rows (`L-PX-*`), verified across two independent vendors.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SNDK | 2026-07-02 | 1808.04 | 2026-07-29 | 1015.89 | -43.81% | -2.01% | -41.80% | MISS | OUT_CI_LOW |
| MRVL | 2026-07-02 | 249.32 | 2026-07-29 | 163.40 | -34.46% | -2.01% | -32.45% | MISS | IN_CI |
| INTC | 2026-07-02 | 121.95 | 2026-07-29 | 81.88 | -32.86% | -2.01% | -30.85% | MISS | OUT_CI_LOW |
| MRNA | 2026-07-02 | 78.67 | 2026-07-29 | 54.49 | -30.73% | -2.01% | -28.72% | MISS | OUT_CI_LOW |
| MRNA | 2026-07-02 | 78.66 | 2026-07-29 | 54.49 | -30.73% | -1.64% | -29.09% | MISS | OUT_CI_LOW |
| MU | 2026-07-02 | 1054.15 | 2026-07-29 | 739.00 | -29.90% | -2.27% | -27.63% | MISS | IN_CI |
| ARM | 2026-07-02 | 319.58 | 2026-07-29 | 224.89 | -29.63% | -2.01% | -27.62% | MISS | IN_CI |
| AMAT | 2026-07-02 | 599.07 | 2026-07-29 | 436.45 | -27.15% | -2.01% | -25.14% | MISS | OUT_CI_LOW |
| FLEX | 2026-07-02 | 140.62 | 2026-07-29 | 103.02 | -26.74% | -2.01% | -24.73% | MISS | OUT_CI_LOW |
| MU | 2026-07-02 | 986.00 | 2026-07-29 | 739.00 | -25.05% | -2.01% | -23.04% | MISS | IN_CI |
| LII | 2026-07-02 | 563.65 | 2026-07-29 | 430.02 | -23.71% | -1.64% | -22.07% | MISS | OUT_CI_LOW |
| CAT | 2026-07-02 | 998.00 | 2026-07-29 | 782.71 | -21.57% | -2.27% | -19.30% | MISS | OUT_CI_LOW |
| AMD | 2026-07-02 | 546.50 | 2026-07-29 | 429.56 | -21.40% | -2.27% | -19.13% | MISS | OUT_CI_LOW |
| AMD | 2026-07-02 | 519.41 | 2026-07-29 | 429.56 | -17.30% | -2.01% | -15.29% | MISS | IN_CI |
| MAS | 2026-07-02 | 82.00 | 2026-07-29 | 72.56 | -11.51% | -1.64% | -9.88% | MISS | OUT_CI_LOW |
| PANW | 2026-07-02 | 350.84 | 2026-07-29 | 314.15 | -10.46% | -1.64% | -8.82% | MISS | IN_CI |
| PANW | 2026-07-02 | 350.10 | 2026-07-29 | 314.15 | -10.27% | -2.01% | -8.26% | MISS | IN_CI |
| CNC | 2026-07-02 | 68.19 | 2026-07-29 | 61.82 | -9.33% | -2.01% | -7.33% | MISS | OUT_CI_LOW |
| HUM | 2026-07-02 | 402.05 | 2026-07-29 | 365.41 | -9.11% | -2.01% | -7.10% | MISS | OUT_CI_LOW |
| WST | 2026-07-02 | 366.19 | 2026-07-29 | 337.46 | -7.85% | -1.64% | -6.21% | MISS | OUT_CI_LOW |
| HUM | 2026-07-02 | 394.07 | 2026-07-29 | 365.41 | -7.27% | -1.64% | -5.64% | MISS | OUT_CI_LOW |
| LIN | 2026-07-02 | 544.77 | 2026-07-29 | 511.17 | -6.17% | -1.64% | -4.53% | MISS | OUT_CI_LOW |
| DELL | 2026-07-02 | 393.69 | 2026-07-29 | 369.64 | -6.11% | -2.01% | -4.10% | MISS | IN_CI |
| AMZN | 2026-07-02 | 241.00 | 2026-07-29 | 226.65 | -5.95% | -2.27% | -3.68% | MISS | IN_CI |
| GOOGL | 2026-07-02 | 357.20 | 2026-07-29 | 336.71 | -5.74% | -2.27% | -3.47% | MISS | IN_CI |
| KDP | 2026-07-02 | 33.15 | 2026-07-29 | 31.45 | -5.13% | -1.64% | -3.49% | MISS | OUT_CI_LOW |
| FFIV | 2026-07-02 | 406.05 | 2026-07-29 | 386.95 | -4.70% | -1.64% | -3.07% | MISS | OUT_CI_LOW |
| PLTR | 2026-07-02 | 128.13 | 2026-07-29 | 123.00 | -4.00% | -2.27% | -1.73% | MISS | IN_CI |
| BEN | 2026-07-02 | 33.62 | 2026-07-29 | 32.39 | -3.66% | -1.64% | -2.02% | MISS | IN_CI |
| URI | 2026-07-02 | 1090.01 | 2026-07-29 | 1055.11 | -3.20% | -1.64% | -1.56% | MISS | IN_CI |
| META | 2026-07-02 | 604.30 | 2026-07-29 | 585.61 | -3.09% | -2.27% | -0.82% | MISS | IN_CI |
| FTNT | 2026-07-02 | 157.64 | 2026-07-29 | 153.22 | -2.80% | -1.64% | -1.17% | MISS | IN_CI |
| GPC | 2026-07-02 | 131.88 | 2026-07-29 | 129.98 | -1.44% | -1.64% | +0.20% | HIT | IN_CI |
| UNH | 2026-07-02 | 426.05 | 2026-07-29 | 420.57 | -1.29% | -2.27% | +0.98% | HIT | IN_CI |
| PG | 2026-07-02 | 147.66 | 2026-07-29 | 146.10 | -1.06% | -2.27% | +1.21% | HIT | IN_CI |
| MNST | 2026-07-02 | 97.86 | 2026-07-29 | 97.23 | -0.64% | -1.64% | +0.99% | HIT | OUT_CI_LOW |
| LYV | 2026-07-02 | 185.09 | 2026-07-29 | 184.43 | -0.36% | -1.64% | +1.28% | HIT | IN_CI |
| HSIC | 2026-07-02 | 85.97 | 2026-07-29 | 85.83 | -0.16% | -1.64% | +1.47% | HIT | OUT_CI_LOW |
| LLY | 2026-07-02 | 1211.90 | 2026-07-29 | 1210.02 | -0.16% | -1.64% | +1.48% | HIT | IN_CI |
| ABBV | 2026-07-02 | 260.96 | 2026-07-29 | 263.30 | +0.90% | -1.64% | +2.53% | HIT | IN_CI |
| DDOG | 2026-07-02 | 259.90 | 2026-07-29 | 264.20 | +1.66% | -2.01% | +3.66% | HIT | IN_CI |
| MSFT | 2026-07-02 | 382.92 | 2026-07-29 | 390.54 | +1.99% | -2.27% | +4.26% | HIT | IN_CI |
| SWK | 2026-07-02 | 90.89 | 2026-07-29 | 93.05 | +2.38% | -1.64% | +4.01% | HIT | IN_CI |
| DVA | 2026-07-02 | 233.71 | 2026-07-29 | 240.96 | +3.10% | -1.64% | +4.74% | HIT | IN_CI |
| DOC | 2026-07-02 | 21.77 | 2026-07-29 | 22.48 | +3.26% | -1.64% | +4.90% | HIT | IN_CI |
| CCEP | 2026-07-02 | 106.37 | 2026-07-29 | 111.10 | +4.45% | -1.64% | +6.08% | HIT | IN_CI |
| BAX | 2026-07-02 | 22.55 | 2026-07-29 | 24.77 | +9.84% | -1.64% | +11.48% | HIT | IN_CI |
| AAPL | 2026-07-02 | 294.02 | 2026-07-29 | 338.19 | +15.02% | -2.27% | +17.29% | HIT | OUT_CI_HIGH |
| MCK | 2026-07-02 | 768.06 | 2026-07-29 | 888.56 | +15.69% | -2.27% | +17.96% | HIT | OUT_CI_HIGH |

## 3. Theme-Level Performance

| Theme | Verdict | Evidence |
|---|---|---|
| Semiconductor / AI hardware long | **FAILED** | 11 names averaged -29.36% over the window; SOXX itself returned -17.89% |
| Defensive healthcare / staples | **PARTIAL** | best names in the batch (MCK, AAPL, BAX) but the cohort still averaged negative |
| Broad-market beta (SPY prior) | **FAILED** | all three SPY forecasts settled `MISS`; SPY realized -2.06% over the window vs priors of +0.50% to +1.50% |

## 4. Regime Shift Assessment

| | Prior vintage (2026-07-02) | Current (2026-07-29) |
|---|---|---|
| SPY vs MA20 / MA50 | above / above | **below / below** |
| VIX | ~17 (20d mean 17.17) | **20.66** (prior close 18.21) |
| SPY 30d realized vol | — | 3.57%, falling vs prior 30d 4.17% |
| Declared regime | BULL-leaning | **`NEUTRAL`** |

Factor-weight implication: the tape has moved from trend-persistent to rotational. That does
**not** license a weight change here — family weights are protected and any change needs Track A
evidence this run cannot supply (`eff_n`=1).

## 5. Carry-Forward Decisions

Ranks below are read programmatically out of `run_computed_manifest.json` — never transcribed.

| Ticker/Theme | Prior Model | MoM Return | MoM Alpha | Decision | Rationale |
|---|---|---|---|---|---|
| MCK | claude-sonnet-5 | +15.69% | +17.96% | DOWNGRADE | fell to 66.7 pctl — monitoring only, below the 80th-pctl investable bar |
| AAPL | claude-sonnet-5 | +15.02% | +17.29% | DOWNGRADE | fell to 68.4 pctl — monitoring only, below the 80th-pctl investable bar |
| BAX | claude-fable-5 | +9.84% | +11.48% | CARRY | still top-quintile today (93.2 pctl); re-scored on current evidence |
| CCEP | claude-fable-5 | +4.45% | +6.08% | CARRY | still top-quintile today (89.7 pctl); re-scored on current evidence |
| DOC | claude-fable-5 | +3.26% | +4.90% | CARRY | still top-quintile today (84.2 pctl); re-scored on current evidence |
| DVA | claude-fable-5 | +3.10% | +4.74% | CARRY | still top-quintile today (95.5 pctl); re-scored on current evidence |
| SWK | claude-fable-5 | +2.38% | +4.01% | CARRY | still top-quintile today (87.5 pctl); re-scored on current evidence |
| MSFT | claude-sonnet-5 | +1.99% | +4.26% | DROP | fell to 35.3 pctl, below the 60th-pctl ranking floor |
| DDOG | gpt-5 | +1.66% | +3.66% | DOWNGRADE | fell to 71.2 pctl — monitoring only, below the 80th-pctl investable bar |
| ABBV | claude-fable-5 | +0.90% | +2.53% | CARRY | still top-quintile today (81.7 pctl); re-scored on current evidence |
| LLY | claude-fable-5 | -0.16% | +1.48% | DOWNGRADE | fell to 71.0 pctl — monitoring only, below the 80th-pctl investable bar |
| HSIC | claude-fable-5 | -0.16% | +1.47% | DOWNGRADE | fell to 71.3 pctl — monitoring only, below the 80th-pctl investable bar |
| LYV | claude-fable-5 | -0.36% | +1.28% | DOWNGRADE | fell to 67.8 pctl — monitoring only, below the 80th-pctl investable bar |
| MNST | claude-fable-5 | -0.64% | +0.99% | DOWNGRADE | fell to 77.4 pctl — monitoring only, below the 80th-pctl investable bar |
| PG | claude-sonnet-5 | -1.06% | +1.21% | DROP | fell to 54.0 pctl, below the 60th-pctl ranking floor |
| UNH | claude-sonnet-5 | -1.29% | +0.98% | CARRY | still top-quintile today (80.7 pctl); re-scored on current evidence |
| GPC | claude-fable-5 | -1.44% | +0.20% | DROP | fell to 55.4 pctl, below the 60th-pctl ranking floor |
| FTNT | claude-fable-5 | -2.80% | -1.17% | CARRY | still top-quintile today (97.1 pctl); re-scored on current evidence |
| META | claude-sonnet-5 | -3.09% | -0.82% | DROP | fell to 32.7 pctl, below the 60th-pctl ranking floor |
| URI | claude-fable-5 | -3.20% | -1.56% | DROP | fell to 44.8 pctl, below the 60th-pctl ranking floor |
| BEN | claude-fable-5 | -3.66% | -2.02% | DROP | fell to 51.9 pctl, below the 60th-pctl ranking floor |
| PLTR | claude-sonnet-5 | -4.00% | -1.73% | DROP | fell to 6.0 pctl, below the 60th-pctl ranking floor |
| FFIV | claude-fable-5 | -4.70% | -3.07% | DROP | fell to 57.1 pctl, below the 60th-pctl ranking floor |
| KDP | claude-fable-5 | -5.13% | -3.49% | DROP | fell to 35.7 pctl, below the 60th-pctl ranking floor |
| GOOGL | claude-sonnet-5 | -5.74% | -3.47% | DROP | fell to 11.5 pctl, below the 60th-pctl ranking floor |
| AMZN | claude-sonnet-5 | -5.95% | -3.68% | DROP | fell to 7.6 pctl, below the 60th-pctl ranking floor |
| DELL | gpt-5 | -6.11% | -4.10% | DROP | fell to 58.3 pctl, below the 60th-pctl ranking floor |
| LIN | claude-fable-5 | -6.17% | -4.53% | DROP | fell to 25.5 pctl, below the 60th-pctl ranking floor |
| HUM | claude-fable-5 | -7.27% | -5.64% | CARRY | still top-quintile today (97.7 pctl); re-scored on current evidence |
| WST | claude-fable-5 | -7.85% | -6.21% | DOWNGRADE | fell to 67.6 pctl — monitoring only, below the 80th-pctl investable bar |
| HUM | gpt-5 | -9.11% | -7.10% | CARRY | still top-quintile today (97.7 pctl); re-scored on current evidence |
| CNC | gpt-5 | -9.33% | -7.33% | CARRY | still top-quintile today (86.9 pctl); re-scored on current evidence |
| PANW | gpt-5 | -10.27% | -8.26% | DOWNGRADE | fell to 65.7 pctl — monitoring only, below the 80th-pctl investable bar |
| PANW | claude-fable-5 | -10.46% | -8.82% | DOWNGRADE | fell to 65.7 pctl — monitoring only, below the 80th-pctl investable bar |
| MAS | claude-fable-5 | -11.51% | -9.88% | DROP | fell to 36.1 pctl, below the 60th-pctl ranking floor |
| AMD | gpt-5 | -17.30% | -15.29% | DROP | fell to 12.5 pctl, below the 60th-pctl ranking floor |
| AMD | claude-sonnet-5 | -21.40% | -19.13% | DROP | fell to 12.5 pctl, below the 60th-pctl ranking floor |
| CAT | claude-sonnet-5 | -21.57% | -19.30% | DROP | fell to 4.1 pctl, below the 60th-pctl ranking floor |
| LII | claude-fable-5 | -23.71% | -22.07% | DROP | fell to 2.1 pctl, below the 60th-pctl ranking floor |
| MU | gpt-5 | -25.05% | -23.04% | DROP | fell to 15.0 pctl, below the 60th-pctl ranking floor |
| FLEX | gpt-5 | -26.74% | -24.73% | DROP | fell to 22.8 pctl, below the 60th-pctl ranking floor |
| AMAT | gpt-5 | -27.15% | -25.14% | DROP | fell to 1.9 pctl, below the 60th-pctl ranking floor |
| ARM | gpt-5 | -29.63% | -27.62% | DROP | fell to 15.4 pctl, below the 60th-pctl ranking floor |
| MU | claude-sonnet-5 | -29.90% | -27.63% | DROP | fell to 15.0 pctl, below the 60th-pctl ranking floor |
| MRNA | claude-fable-5 | -30.73% | -29.09% | DROP | fell to 3.3 pctl, below the 60th-pctl ranking floor |
| MRNA | gpt-5 | -30.73% | -28.72% | DROP | fell to 3.3 pctl, below the 60th-pctl ranking floor |
| INTC | gpt-5 | -32.86% | -30.85% | DROP | fell to 2.9 pctl, below the 60th-pctl ranking floor |
| MRVL | gpt-5 | -34.46% | -32.45% | DROP | fell to 8.2 pctl, below the 60th-pctl ranking floor |
| SNDK | gpt-5 | -43.81% | -41.80% | DROP | fell to 0.2 pctl, below the 60th-pctl ranking floor |

`DROP` names stay out of today's scored set absent new ledger evidence; `CARRY` names are
re-scored from scratch on today's evidence and hold no score advantage from their prior rank.

## 6. Sign-Off

| Item | Value |
|---|---|
| Freshness tag on every price used | `HISTORICAL` (2026-07-29 close), two-source verified |
| Settlement timing | `TARGET_EQ_RUN_DATE` — validator-accepted, `due_inventory: 0` |
| Reflection confidence | **MEDIUM** |
| Structural issues found | (1) `agents.md` MoM tie-break gap — third consecutive flag, Track B this run; (2) rank-order inversion, Track A DEFERRED on `eff_n`; (3) `MARKET_FORECAST` mu category error, unfixed and Track-A-gated |

Confidence is MEDIUM, not HIGH: the settlement and price layers are fully grounded and
validator-checked, but the baseline had to be chosen cross-model from a three-way tie whose
members disagree by 40.7pp,
so the MoM comparison itself carries selection risk that no amount of price grounding removes.
