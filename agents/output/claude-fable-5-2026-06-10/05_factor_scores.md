# 05 Factor Scores

## Methodology (deterministic, reproducible from ledger rows)

Cross-sectional z-scores over the 30-name sampled universe, four families per shared architecture:

- **Technical (0.30):** `T = 0.5·z(YTD%) + 0.3·z(RS1d) + 0.2·z(−HV30)` — all inputs OBSERVED ledger rows. `RS1d` = today's change − SPY's −1.19% (defensive relative strength on an unwind day). The inverse-HV term implements the HIGH_VOL regime preference for low volatility.
- **Fundamental (0.30):** analyst sub-score −2..+2 per name, `INFERRED` (training-reference state ≤ 2026-01, cadence-adjusted), z-scored. Bases in the table below.
- **Sentiment/Positioning (0.25):** `S = 0.6·z(consensus bias, INFERRED — cross-checked against gpt-5-2026-06-09 source-backed consensus notes) + 0.4·(crowding term: −1.5 if HV30 > 60% in unwind tape, else +0.3)`.
- **Macro/Regime (0.15):** regime-fit sub-score −2..+2 (energy/staples/defensive HC positive; crowded AI-beta negative; rates neutral — TLT flat), z-scored.

`Adjusted = 0.30·zF + 0.30·T + 0.25·S + 0.15·zM, × DQ 0.85, − penalties`. DQ 0.85 reflects DELAYED quotes + INFERRED fundamental/sentiment inputs + missing Enhancing feeds. Penalty: MU −0.10 (earnings inside buffered 19d window). Baseline family weights unchanged (no evolution-policy mutation).

## INFERRED Sub-Scores (disclosed; F / Sentiment-analyst / Macro-regime)

| Ticker | F | SA | M | Fundamental basis (reference-state, INFERRED) |
|---|---|---|---|---|
| MCK | +1.5 | +1.0 | +1.5 | Pharma-distribution oligopoly economics; GLP-1 volume tailwind; strong-buy consensus (cross-checked vs 6/9 run) |
| COST | +1.5 | +0.5 | +1.5 | Membership renewal/comp strength; defensive quality |
| WMT | +1.0 | +1.0 | +1.5 | Share gains + e-comm profitability; strong-buy consensus; May earnings drawdown noted as risk |
| CVX | +1.0 | +0.5 | +1.5 | Hess integration FCF; capital discipline |
| UNH | +1.0 | +1.0 | +1.0 | MLR stabilization/margin recovery; upgrade cycle (6/9 run snippets) |
| MU | +2.0 | +0.5 | −1.5 | HBM/memory pricing supercycle — strongest fundamentals in universe, worst regime fit |
| XOM | +1.0 | +0.5 | +1.5 | Upstream cost curve + buybacks |
| LIN | +1.5 | +0.5 | +0.5 | Pricing power, backlog compounding |
| LLY | +1.0 | +0.5 | +0.5 | GLP-1 franchise vs rich valuation |
| NVDA | +1.5 | +0.5 | −1.0 | DC demand intact; crowding dominates near-term |
| GOOGL | +1.0 | +0.5 | 0.0 | Search resilience + Gemini monetization |
| ABBV | +0.5 | +0.5 | +1.0 | Skyrizi/Rinvoq vs Humira erosion |
| (18 rejected names) | … | … | … | Sub-scores recorded in workpaper; all rank < 60th pctl |

## Ranked Candidate Table (12 ranked names; `SAMPLED_PCTL (n=30)`)

| Ticker | Company | Entry | Price Date | Tag | Adj | Pctl | Beta60 | 30d RVol | Days→Earn | mu | sigma(1m) | Sigma Source | Target | Target Date | CI70 Lo | CI70 Hi | Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MCK | McKesson | 790.22 | 2026-06-10 | DELAYED | +0.787 | 100 | −0.17 | 22.5% | ~56 | +6.0% | 6.49% | REALIZED_VOL_30D | 837.63 | 2026-07-08 | 784.30 | 890.97 | 01 rows | MEDIUM | Defensive distribution oligopoly, post-earnings recovery | Policy/drug-pricing headlines |
| COST | Costco | 980.45 | 2026-06-10 | DELAYED | +0.691 | 97 | −0.14 | 26.9% | ~106 | +6.0% | 7.77% | REALIZED_VOL_30D | 1039.28 | 2026-07-08 | 960.05 | 1118.51 | 01 rows | MEDIUM | Membership staple, May earnings reset absorbed | Valuation premium compression |
| WMT | Walmart | 119.83 | 2026-06-10 | DELAYED | +0.624 | 93 | +0.24 | 34.4% | ~70 | +5.0% | 9.94% | REALIZED_VOL_30D | 125.82 | 2026-07-08 | 113.43 | 138.21 | 01 rows | MEDIUM | Defensive retail share-gainer, recovering from May drawdown | Post-earnings momentum still negative |
| CVX | Chevron | 191.01 | 2026-06-10 | DELAYED | +0.550 | 90 | −0.88 | 25.2% | ~51 | +5.0% | 7.28% | REALIZED_VOL_30D | 200.56 | 2026-07-08 | 186.10 | 215.02 | 01 rows | MEDIUM | Energy leadership + geopolitical supply hedge | Crude downside reverses leadership |
| UNH | UnitedHealth | 407.13 | 2026-06-10 | DELAYED | +0.541 | 86 | +0.35 | 28.6% | ~36 | +4.0% | 8.27% | REALIZED_VOL_30D | 423.42 | 2026-07-08 | 388.40 | 458.43 | 01 rows | MEDIUM | Managed-care recovery momentum (+46% off March low) | Jul-16 earnings at horizon edge; MLR surprise |
| MU | Micron | 891.66 | 2026-06-10 | DELAYED | +0.428 | 83 | N/A — no 60d fetch | 101.4% | **~15 ⚠** | +1.0%* | 29.26% | REALIZED_VOL_30D | 900.58 | 2026-07-08 | 629.24 | 1171.91 | 01 rows | LOW | Memory/HBM supercycle | Crowded unwind + earnings ~Jun 25 inside window |
| XOM | Exxon Mobil | 151.35 | 2026-06-10 | DELAYED | +0.522 | 79 | N/A | 30.1% | ~51 | +2.0% | 8.69% | REALIZED_VOL_30D | 154.38 | 2026-07-08 | 140.70 | 168.06 | 01 rows | MEDIUM | Energy momentum/value | Below investable bar (79th pctl) |
| LIN | Linde | 509.20 | 2026-06-10 | DELAYED | +0.510 | 76 | N/A | 21.8% | ~51 | +2.0% | 6.29% | REALIZED_VOL_30D | 519.38 | 2026-07-08 | 486.07 | 552.69 | 01 rows | MEDIUM | Low-vol compounder | Industrial volume softness |
| LLY | Eli Lilly | 1138.16 | 2026-06-10 | DELAYED | +0.247 | 72 | N/A | 38.2% | ~57 | +2.0% | 11.02% | REALIZED_VOL_30D | 1160.92 | 2026-07-08 | 1030.48 | 1291.37 | 01 rows | MEDIUM | GLP-1 defensive growth | Valuation, competitor data |
| NVDA | NVIDIA | 201.65 | 2026-06-10 | DELAYED | +0.175 | 69 | 1.84 | 41.3% | ~77 | +1.0% | 11.91% | REALIZED_VOL_30D | 203.67 | 2026-07-08 | 178.69 | 228.64 | 01 rows | LOW | AI DC leader, −14% off high | Unwind continuation |
| GOOGL | Alphabet | 356.64 | 2026-06-10 | DELAYED | +0.162 | 66 | 1.56 | 36.1% | ~48 | +1.0% | 10.41% | REALIZED_VOL_30D | 360.21 | 2026-07-08 | 321.60 | 398.82 | 01 rows | LOW | Mega-cap relative winner | Beta to further unwind |
| ABBV | AbbVie | 225.82 | 2026-06-10 | DELAYED | +0.134 | 62 | N/A | 29.8% | ~51 | +1.0% | 8.60% | REALIZED_VOL_30D | 228.08 | 2026-07-08 | 207.88 | 248.28 | 01 rows | LOW | Defensive pharma | Humira erosion pace |

\* MU mu = table band +3.0% shaded −2pp for the in-window earnings event (ledger-backed reason; within the ±2pp discretion cap).

Beta60 is reported only where a 60-day fetched return series exists (5 investables + NVDA/GOOGL from reflection fetches); monitor names without a series show `N/A — no 60d fetch` rather than an invented value. Monitor names are not sized, so beta is not a Required input for them.

## Calibration Feedback Binding

`02_reflection.md §0` = `INSUFFICIENT_SETTLED_N` (no prior ledger) → no CI-coverage or rank-IC override active. Confidence is nonetheless capped at MEDIUM universe-wide (first run, INFERRED fundamental/sentiment inputs, missing Enhancing feeds); LOW for crowding-flagged or in-window-earnings names.

## Hallucination Prevention Checklist

- [x] Every numeric `entry_price` has `price_date` + `price_tag` (all DELAYED 2026-06-10)
- [x] Every numeric metric cites Source Ledger rows (column "Ledger")
- [x] `target_price = entry × (1+mu)` — derived, none guessed
- [x] Every sigma has a stated source (REALIZED_VOL_30D; tool HV30 or computed from fetched closes)
- [x] No investable name has `price_tag = UNAVAILABLE`
- [x] mu from Calibration Table band by percentile; one ±2pp adjustment (MU) with ledger-backed reason
- [x] No live-sounding claims without non-illustrative ledger support

Factor families driving the leaderboard: macro/regime (defensive + energy) and the technical low-vol/RS terms dominate; pure momentum (YTD) is heavily diluted by the crowding and regime terms — by construction in a HIGH_VOL unwind.

If fewer than 5 names had passed, recommendation would be NO_TRADE; exactly 5 pass.
