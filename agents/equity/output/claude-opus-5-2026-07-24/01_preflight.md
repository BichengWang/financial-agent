# 01 Preflight — Source Ledger — 2026-07-24

Model `claude-opus-5`. All facts used downstream by `02`–`09` and `15_predictions.json` appear here or are marked `UNAVAILABLE`. Ledger IDs `L001`–`L148`: `L001`–`L029` price rows, `L030`–`L133` per-name derived rows, `L134`–`L148` grouped/methodology rows.

## Fetch Log (what was attempted, what succeeded)

| Source | Purpose | Result |
|---|---|---|
| `query1/query2.finance.yahoo.com/v8/finance/chart` | Primary 5y daily bars | **HTTP 429 on every attempt**, bulk and single-symbol, both hosts. Yahoo came back online for the 2026-07-21 run; today it is blocked again. Treat availability as unstable, not resolved. |
| `api.nasdaq.com/api/quote/{sym}/historical` | Fallback bulk 5y daily bars | **516/521 symbols in 182s** (8 workers). Carries the same-day 2026-07-24 close for every symbol. |
| `api.nasdaq.com/api/quote/{sym}/historical` (`BRK.B`) | BRK-B repair | 1,307 bars. Nasdaq needs dot notation (07-13 precedent). |
| IBKR MCP `get_price_history` conid 4931 | BF-B repair | 1,255 bars. BF-B is unavailable on Nasdaq under any notation (07-13 precedent, reconfirmed). |
| `cdn.cboe.com/.../VIX_History.csv` | VIX | 1,303 bars, last 2026-07-24 = 18.58. |
| `home.treasury.gov/.../daily_treasury_bill_rates` | Risk-free rate | 390 bars, last 2026-07-24 = 3.81% (13-week bank discount). FRED `DTB3` not attempted; the Treasury CSV is the established working path since 2026-07-14. |
| `api.nasdaq.com/api/analyst/{sym}/earnings-date` | Earnings preflight | 76 names across two passes (52 + bounded second pass of 24): 48 CONFIRMED, 28 vendor-empty. |
| `api.nasdaq.com/api/quote/{sym}/summary` | GICS sector / industry | 68/76 names returned a sector. |
| `stockanalysis.com/api/symbol/*/history` | Independent price confirmation #2 | 29/29 exact matches. |
| `quote.cnbc.com/.../restQuote` | Independent price confirmation #3 | 29/29 exact matches (`last` field, gated on `last_time == 2026-07-24`). |

**Per-symbol repairs.** `SATS` → fetched under `ECHO` (EchoStar rename, 07-13 precedent, still not fixed upstream) and saved as `SATS.csv`. `FDXF` returned only 41 bars from 2026-05-27 — a recent spin-off — and is **excluded** (fails the >6-month listing-age filter and the 60-bar minimum). No other symbol required intervention; `L` (Loews), which raced to an empty CSV on 2026-07-21, fetched cleanly this run.

## Price Verification (Price Sourcing Standard)

The Price Sourcing Standard requires a market-data tool **or** two independent web sources agreeing within 1%. All 29 published prices cleared with **three** sources at **0.000%** maximum pairwise difference:

- `api.nasdaq.com` bulk historical (primary),
- `stockanalysis.com` daily history,
- `cnbc.com` quote service (`last`, validated against `last_time == 2026-07-24`).

Full per-symbol detail in `price_verification.json`. A first verification pass wrongly read CNBC's `previous_day_closing` field and produced spurious 0.7–8.1% disagreements; the field was corrected to `last` and every symbol then matched exactly. The largest apparent discrepancy in that bad pass (PKG, 8.06%) was itself the tell — it equals PKG's +8.76% earnings move on 2026-07-24, i.e. the field was returning 2026-07-23.

### Price rows

| Row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 01 | close | TRV | 387.26 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L002 | 01 | close | PAYX | 113.55 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L003 | 01 | close | DGX | 227.86 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L004 | 01 | close | UNP | 307.32 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L005 | 01 | close | PCG | 17.85 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L006 | 01 | close | RTX | 212.79 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L007 | 01 | close | NSC | 350.66 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L008 | 01 | close | GD | 386.75 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L009 | 01 | close | CSX | 53.23 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L010 | 01 | close | CTAS | 205.91 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L011 | 01 | close | PM | 193.0 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L012 | 01 | close | MPC | 309.24 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L013 | 01 | close | LMT | 582.6 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L014 | 01 | close | PKG | 254.39 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L015 | 01 | close | TMO | 568.26 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L016 | 01 | close | SJM | 118.32 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L017 | 01 | close | BNY | 158.91 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L018 | 01 | close | VLO | 302.5 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L019 | 01 | close | MTB | 249.6 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L020 | 01 | close | MET | 94.83 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L021 | 01 | close | HIG | 140.53 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L022 | 01 | close | BAC | 62.05 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L023 | 01 | close | JPM | 353.21 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L024 | 01 | close | AAPL | 333.02 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L025 | 01 | close | UNH | 420.74 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L026 | 01 | close | LLY | 1196.03 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L027 | 01 | close | SPY | 738.93 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L028 | 01 | close | QQQ | 684.23 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |
| L029 | 01 | close | SOXX | 527.01 | USD | 2026-07-24 | api.nasdaq.com bulk historical + stockanalysis.com + cnbc.com (3 sources, max diff 0.0%); retrieved_at 2026-07-25T07:31:36Z | DELAYED | OBSERVED | 02,03,05,06,07,09,15 entry_price/settlement basis |

## Earnings Resolution

`rules.md § Input Classification` #4 requires a confirmed or cadence-estimated next earnings date. 48 of 76 fetched names returned a parseable date. The other 28 returned Nasdaq's vendor-empty response ("hasn't provided us with the upcoming earnings report date"), which is common in late July for names that have just reported. Each was resolved by evidence, not assumption:

| Resolution | Rule applied | Names |
|---|---|---|
| `CONFIRMED` | Vendor date parsed from `data.announcement` / `data.reportText` free text (07-21 schema correction — the response is **not** `data.rows`) | 48 names |
| `ESTIMATED_CADENCE (+91d, ±5d)` | Vendor-empty **and** a print-like signature in the last 12 sessions: a 1-day move ≥3.5% **or** volume ≥1.8× the trailing median. Next report estimated as identified print date + 91d, which lands outside the 14-day penalty window | CSX, CTAS, DGX, FCX, GE, GOOGL, GS, LMT, NSC, PAYX, PCG, PM, RTX, TMO, TRV, UNH, UNP, JPM, BAC, PKG, BNY, MTB |
| `ESTIMATED_PRINT_WEEK (±5d)` | Vendor-empty **and no** clean print signature. Treated conservatively as printing inside the current week → **penalised** on the buffered window | CB, HIG, WRB, EQR, AMP, JNJ |

JPM shows a clean signature (volume ×1.77 with +2.50% on 2026-07-14). BAC's move that day was only +1.88% at volume ×1.47 — below the threshold in isolation — but it sits on the same bank-earnings kickoff date as JPM with elevated volume sustained 07-14 through 07-17, so it is tagged `ESTIMATED_CADENCE` with the inference disclosed as `INFERRED` rather than `OBSERVED`. The six `ESTIMATED_PRINT_WEEK` names are penalised rather than assumed safe; this is the deliberately conservative direction.

**Earnings concentration is extreme this week.** Of the 48 confirmed dates, **29 fall inside 14 calendar days** — late July / early August is the peak of the Q2 reporting cycle. Every one of those names carries the `-0.10` penalty and a `LOW` confidence cap.

## Derived rows

Every derived value cites its formula and inputs. `sigma_30d`, `beta_60d`, `downside_sigma_30d`, and `max_drawdown_60d` are listed per published name below; the technical indicator pack (TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, relative strength on daily/weekly/monthly bars) is carried in `technical_indicators.json` and cited per name in `05_factor_scores.md § Technical Indicator Summary`.

**Sortino lineage note.** `downside_sigma_30d` is the standard deviation of **negative daily returns only** over the last 30 sessions, scaled by `sqrt(21)` — per `rules.md § Ratio Definitions`, and per the bug fixed and logged as Track B in the 2026-07-21 evolution log (the 07-17 and 07-20 runs had reused the total sigma, making Sortino a duplicate of Sharpe). This run computes it correctly; Sortino and Sharpe differ per name, as they should.

| L030 | 01 | sigma_30d (REALIZED_VOL_30D) | TRV | 0.093270 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L031 | 01 | beta_60d vs SPY | TRV | -0.6929 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L032 | 01 | downside_sigma_30d | TRV | 0.033297 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L033 | 01 | max_drawdown_60d | TRV | -0.059564 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L034 | 01 | sigma_30d (REALIZED_VOL_30D) | PAYX | 0.094460 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L035 | 01 | beta_60d vs SPY | PAYX | -0.6376 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L036 | 01 | downside_sigma_30d | PAYX | 0.041574 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L037 | 01 | max_drawdown_60d | PAYX | -0.063549 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L038 | 01 | sigma_30d (REALIZED_VOL_30D) | DGX | 0.096197 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L039 | 01 | beta_60d vs SPY | DGX | -0.5678 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L040 | 01 | downside_sigma_30d | DGX | 0.029867 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L041 | 01 | max_drawdown_60d | DGX | -0.065966 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L042 | 01 | sigma_30d (REALIZED_VOL_30D) | UNP | 0.073164 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L043 | 01 | beta_60d vs SPY | UNP | -0.1635 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L044 | 01 | downside_sigma_30d | UNP | 0.048768 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L045 | 01 | max_drawdown_60d | UNP | -0.080568 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L046 | 01 | sigma_30d (REALIZED_VOL_30D) | PCG | 0.071947 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L047 | 01 | beta_60d vs SPY | PCG | -0.2678 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L048 | 01 | downside_sigma_30d | PCG | 0.043165 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L049 | 01 | max_drawdown_60d | PCG | -0.057109 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L050 | 01 | sigma_30d (REALIZED_VOL_30D) | RTX | 0.097541 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L051 | 01 | beta_60d vs SPY | RTX | -0.0397 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L052 | 01 | downside_sigma_30d | RTX | 0.053633 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L053 | 01 | max_drawdown_60d | RTX | -0.055821 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L054 | 01 | sigma_30d (REALIZED_VOL_30D) | NSC | 0.070538 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L055 | 01 | beta_60d vs SPY | NSC | -0.1069 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L056 | 01 | downside_sigma_30d | NSC | 0.043135 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L057 | 01 | max_drawdown_60d | NSC | -0.078605 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L058 | 01 | sigma_30d (REALIZED_VOL_30D) | GD | 0.075743 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L059 | 01 | beta_60d vs SPY | GD | 0.008 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L060 | 01 | downside_sigma_30d | GD | 0.045626 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L061 | 01 | max_drawdown_60d | GD | -0.056988 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L062 | 01 | sigma_30d (REALIZED_VOL_30D) | CSX | 0.072195 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L063 | 01 | beta_60d vs SPY | CSX | 0.1138 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L064 | 01 | downside_sigma_30d | CSX | 0.034814 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L065 | 01 | max_drawdown_60d | CSX | -0.042043 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L066 | 01 | sigma_30d (REALIZED_VOL_30D) | CTAS | 0.103324 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L067 | 01 | beta_60d vs SPY | CTAS | -0.2875 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L068 | 01 | downside_sigma_30d | CTAS | 0.046787 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L069 | 01 | max_drawdown_60d | CTAS | -0.071916 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L070 | 01 | sigma_30d (REALIZED_VOL_30D) | PM | 0.094303 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L071 | 01 | beta_60d vs SPY | PM | -0.5423 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L072 | 01 | downside_sigma_30d | PM | 0.044282 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L073 | 01 | max_drawdown_60d | PM | -0.100073 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L074 | 01 | sigma_30d (REALIZED_VOL_30D) | MPC | 0.096996 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L075 | 01 | beta_60d vs SPY | MPC | -0.4447 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L076 | 01 | downside_sigma_30d | MPC | 0.054725 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L077 | 01 | max_drawdown_60d | MPC | -0.090940 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L078 | 01 | sigma_30d (REALIZED_VOL_30D) | LMT | 0.128828 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L079 | 01 | beta_60d vs SPY | LMT | -0.4405 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L080 | 01 | downside_sigma_30d | LMT | 0.049716 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L081 | 01 | max_drawdown_60d | LMT | -0.103959 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L082 | 01 | sigma_30d (REALIZED_VOL_30D) | PKG | 0.099611 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L083 | 01 | beta_60d vs SPY | PKG | 0.7941 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L084 | 01 | downside_sigma_30d | PKG | 0.045175 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L085 | 01 | max_drawdown_60d | PKG | -0.104268 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L086 | 01 | sigma_30d (REALIZED_VOL_30D) | TMO | 0.102174 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L087 | 01 | beta_60d vs SPY | TMO | 0.0927 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L088 | 01 | downside_sigma_30d | TMO | 0.02946 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L089 | 01 | max_drawdown_60d | TMO | -0.084809 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L090 | 01 | sigma_30d (REALIZED_VOL_30D) | SJM | 0.094716 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L091 | 01 | beta_60d vs SPY | SJM | -0.7151 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L092 | 01 | downside_sigma_30d | SJM | 0.053172 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L093 | 01 | max_drawdown_60d | SJM | -0.084238 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L094 | 01 | sigma_30d (REALIZED_VOL_30D) | BNY | 0.073849 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L095 | 01 | beta_60d vs SPY | BNY | 0.5846 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L096 | 01 | downside_sigma_30d | BNY | 0.038059 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L097 | 01 | max_drawdown_60d | BNY | -0.033385 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L098 | 01 | sigma_30d (REALIZED_VOL_30D) | VLO | 0.117795 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L099 | 01 | beta_60d vs SPY | VLO | -0.7346 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L100 | 01 | downside_sigma_30d | VLO | 0.050836 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L101 | 01 | max_drawdown_60d | VLO | -0.100221 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L102 | 01 | sigma_30d (REALIZED_VOL_30D) | MTB | 0.063712 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L103 | 01 | beta_60d vs SPY | MTB | 0.2927 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L104 | 01 | downside_sigma_30d | MTB | 0.040463 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L105 | 01 | max_drawdown_60d | MTB | -0.066551 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L106 | 01 | sigma_30d (REALIZED_VOL_30D) | MET | 0.072559 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L107 | 01 | beta_60d vs SPY | MET | 0.0025 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L108 | 01 | downside_sigma_30d | MET | 0.048146 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L109 | 01 | max_drawdown_60d | MET | -0.047726 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L110 | 01 | sigma_30d (REALIZED_VOL_30D) | HIG | 0.062609 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L111 | 01 | beta_60d vs SPY | HIG | -0.5763 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L112 | 01 | downside_sigma_30d | HIG | 0.032329 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L113 | 01 | max_drawdown_60d | HIG | -0.079453 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L114 | 01 | sigma_30d (REALIZED_VOL_30D) | BAC | 0.055711 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L115 | 01 | beta_60d vs SPY | BAC | 0.2741 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L116 | 01 | downside_sigma_30d | BAC | 0.033047 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L117 | 01 | max_drawdown_60d | BAC | -0.071455 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L118 | 01 | sigma_30d (REALIZED_VOL_30D) | JPM | 0.065398 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L119 | 01 | beta_60d vs SPY | JPM | 0.2951 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L120 | 01 | downside_sigma_30d | JPM | 0.039448 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L121 | 01 | max_drawdown_60d | JPM | -0.060972 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L122 | 01 | sigma_30d (REALIZED_VOL_30D) | AAPL | 0.096836 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L123 | 01 | beta_60d vs SPY | AAPL | 0.4985 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L124 | 01 | downside_sigma_30d | AAPL | 0.07062 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L125 | 01 | max_drawdown_60d | AAPL | -0.127062 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L126 | 01 | sigma_30d (REALIZED_VOL_30D) | UNH | 0.072909 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L127 | 01 | beta_60d vs SPY | UNH | -0.0419 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L128 | 01 | downside_sigma_30d | UNH | 0.025006 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L129 | 01 | max_drawdown_60d | UNH | -0.060574 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |
| L130 | 01 | sigma_30d (REALIZED_VOL_30D) | LLY | 0.094858 | decimal (1m) | 2026-07-24 | DERIVED: stdev(last 30 daily returns from L-price history) x sqrt(21) | DELAYED | DERIVED | 05,07,15 sigma/CI/VaR/Kelly |
| L131 | 01 | beta_60d vs SPY | LLY | 0.0704 | ratio | 2026-07-24 | DERIVED: cov(r_i,r_SPY)/var(r_SPY) over trailing 60 aligned sessions | DELAYED | DERIVED | 05,07,09 macro_z/Treynor/IR |
| L132 | 01 | downside_sigma_30d | LLY | 0.039126 | decimal (1m) | 2026-07-24 | DERIVED: stdev(negative daily returns, last 30d) x sqrt(21) per rules.md Ratio Definitions | DELAYED | DERIVED | 05 Sortino |
| L133 | 01 | max_drawdown_60d | LLY | -0.071757 | decimal | 2026-07-24 | DERIVED: min(close/cummax(close)-1) over last 60 bars | DELAYED | DERIVED | 05,07 tail risk |

## Grouped / methodology rows

| Row | artifact | field | entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L134 | 01 | index-union universe | S&P500 ∪ NDX100 | 515 (503 + 101, overlap 89) | count | 2026-06-21 (cache) | `build_index_universe.py` → `universe_summary.json` | HISTORICAL | OBSERVED | 03, 04, 05 percentile base |
| L135 | 01 | technical indicator pack | 518 tickers | 517 OK / 1 UNAVAILABLE | records | 2026-07-24 | `technical_indicators.py --history-dir` over the fetched bars → `technical_indicators.json` | DELAYED | DERIVED | 05, 06, 07, 09 |
| L136 | 01 | risk-free rate (1m) | US 13-week T-bill | 3.81% annual → 0.3175% monthly | percent | 2026-07-24 | home.treasury.gov daily treasury bill rates CSV | DELAYED | OBSERVED | 05 Sharpe/Sortino/Treynor/Calmar |
| L137 | 01 | VIX close | ^VIX | 18.58 (avg20 16.83, avg60 17.36, 3.3% of last 60 sessions > 20) | index | 2026-07-24 | cdn.cboe.com VIX_History.csv | DELAYED | OBSERVED | 03 regime |
| L138 | 01 | TLT close + momentum | TLT | 83.25; 20d −4.69%, 60d −3.61% | USD / percent | 2026-07-24 | Nasdaq bulk historical | DELAYED | OBSERVED / DERIVED | 03 rate-regime evidence |
| L139 | 01 | market breadth | 514 scored names | 54.5% above MA20; 64.6% above MA50; median 20d momentum +1.64%; 58.9% positive | percent | 2026-07-24 | DERIVED from L001-series bars + `technical_indicators.json` | DELAYED | DERIVED | 03 regime |
| L140 | 01 | beta dispersion | 514 scored names | median 60d beta +0.232; **40.9% negative**; p10/p25/p50/p75/p90 = −0.62 / −0.32 / +0.23 / +0.97 / +1.97 | ratio | 2026-07-24 | DERIVED from 60d aligned daily returns vs SPY | DELAYED | DERIVED | 03 regime, 05 macro_z, 07 feasibility |
| L141 | 01 | universe median 30d RVol | 514 scored names | 0.0960 (1-month decimal); 2× penalty threshold 0.1920 | decimal | 2026-07-24 | DERIVED from L-sigma rows | DELAYED | DERIVED | 05 volatility penalty |
| L142 | 01 | canonical settlement ledger | all models, full history | 189 EQUITY_ALPHA + 33 MARKET_FORECAST canonical; due_inventory 0; conflicts 0 | count | 2026-07-24 | `settlement_ledger.py --as-of 2026-07-24` → `settlement_manifest.json` | DELAYED | DERIVED | 02, 13, 14 |
| L143 | 01 | effective independent sample | canonical settlements | MF: 10 vintages / 10 target dates → **1** non-overlapping 28d window. EQ: 12 vintages / 12 target dates → **1** window | count | 2026-07-24 | DERIVED from `settlement_manifest.json` target-date grouping | DELAYED | DERIVED | 13, 14 |
| L144 | 01 | Fund_Z sourceability | eligible universe | `UNAVAILABLE` — SHADOW tooling exists but covers ~4.7% of universe, far below the 70% bar | — | 2026-07-24 | `rules.md § SHADOW Diagnostic Tooling`; no Phase-2 fetch attempted this run | UNAVAILABLE | UNAVAILABLE | 05 evidence threshold #2, 08 |
| L145 | 01 | Sent_Z sourceability | eligible universe | `UNAVAILABLE` — same basis as L144 | — | 2026-07-24 | as L144 | UNAVAILABLE | UNAVAILABLE | 05 evidence threshold #2, 08 |
| L146 | 01 | Enhancing inputs | all | options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow — all `UNAVAILABLE`; no feed wired | — | 2026-07-24 | documented absence, not a fetch failure | UNAVAILABLE | UNAVAILABLE | DQ multiplier 0.80, confidence cap; **never** a GO blocker |
| L147 | 01 | GICS sector | 68 of 76 shortlist names | see `05` sector column | label | 2026-07-24 | `api.nasdaq.com/api/quote/{sym}/summary` | DELAYED | OBSERVED | 05, 07 sector table |
| L148 | 01 | MoM baseline prices | 14 baseline names | entry prices from `gpt-5-2026-06-24/15_predictions.json`; SPY benchmark 733.24 | USD | 2026-06-24 | prior package prediction ledger (immutable) | HISTORICAL | OBSERVED | 02 MoM table |

## Coverage Summary

| claim_type | rows | note |
|---|---|---|
| `OBSERVED` | 36 | 29 verified closes + VIX, rf, TLT, universe counts, sector labels, baseline prices |
| `DERIVED` | 108 | 104 per-name risk metrics + breadth/beta-dispersion/median-sigma/settlement/effective-N aggregates |
| `INFERRED` | 3 | BAC earnings-date inference; the 6 `ESTIMATED_PRINT_WEEK` resolutions; defensive macro polarity (see `05`) |
| `ILLUSTRATIVE` | 0 | this is a live `DELAYED` run, not `ILLUSTRATIVE_MODE` |
| `UNAVAILABLE` | 3 | `Fund_Z`, `Sent_Z`, Enhancing input block |

**Status eligibility:** all five Required inputs grounded → the run is eligible for `GO` on data grounds. It publishes `NO_TRADE` on the evidence threshold, not on a grounding failure.
