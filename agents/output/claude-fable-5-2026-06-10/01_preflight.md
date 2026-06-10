# 01 Preflight — Source Ledger and Data Coverage

- Run: claude-fable-5, 2026-06-10, run timestamps 14:46–15:00 ET (intraday, market open)
- Data mode: **DELAYED** — all prices tool-fetched this run via the Interactive Brokers MCP (`get_price_snapshot`, `get_price_history`), each with retrieval timestamp; quotes are real-time-or-delayed per subscription, treated as DELAYED conservatively. No fabricated values.
- Price Sourcing Standard: satisfied by brokerage-tool fetch (single-tool path). `retrieved_at` for all snapshot rows: 2026-06-10 14:46–15:00 ET; history fetches same window.
- Universe: 30 names per Sampled Universe Protocol (see 04). All percentiles labeled `SAMPLED_PCTL (n=30)`.

## Required-for-GO Input Status (GO-Gate inputs, summarized in 00)

1. Grounded entry prices: **PASS** (30/30 snapshot-fetched)
2. ~60d fetched price history per portfolio name + SPY: **PASS** (11 series x 62 bars)
3. Sigma via fallback chain: **PASS** (REALIZED_VOL_30D for all 12 ranked names; no UNAVAILABLE sigmas)
4. Next earnings date: **PASS** (confirmed-from-tape or cadence-estimated `ESTIMATED (±5d)`; MU flagged inside buffered window)
5. Sampled universe ≥30 grounded: **PASS** (n=30)

Missing **Enhancing** inputs (cap confidence/exposure, never block GO): options IV/skew, short-interest/borrow feed, bid-ask tape, analyst-revision tape, institutional flow, full-universe screen.

## Source Ledger

| row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 01/04/05/06/07 | last_price | AAPL | 293.16 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L002 | 05 | chg_1d_pct | AAPL | 0.9 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L003 | 05 | ytd_pct | AAPL | 7.94 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L004 | 05/07 | hv30_ann_pct | AAPL | 25.42 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L005 | 01/04/05/06/07 | last_price | ABBV | 225.82 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L006 | 05 | chg_1d_pct | ABBV | 0.18 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L007 | 05 | ytd_pct | ABBV | -0.37 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L008 | 05/07 | hv30_ann_pct | ABBV | 29.8 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L009 | 01/04/05/06/07 | last_price | AMD | 452.24 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L010 | 05 | chg_1d_pct | AMD | -4.89 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L011 | 05 | ytd_pct | AMD | 111.17 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L012 | 05/07 | hv30_ann_pct | AMD | 86.48 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L013 | 01/04/05/06/07 | last_price | AMZN | 238.64 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L014 | 05 | chg_1d_pct | AMZN | -2.27 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L015 | 05 | ytd_pct | AMZN | 3.22 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L016 | 05/07 | hv30_ann_pct | AMZN | 33.16 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L017 | 01/04/05/06/07 | last_price | ANET | 151.33 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L018 | 05 | chg_1d_pct | ANET | -0.55 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L019 | 05 | ytd_pct | ANET | 15.49 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L020 | 05/07 | hv30_ann_pct | ANET | 65.69 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L021 | 01/04/05/06/07 | last_price | AVGO | 374.07 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L022 | 05 | chg_1d_pct | AVGO | -4.61 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L023 | 05 | ytd_pct | AVGO | 8.08 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L024 | 05/07 | hv30_ann_pct | AVGO | 70.96 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L025 | 01/04/05/06/07 | last_price | CAT | 857.96 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L026 | 05 | chg_1d_pct | CAT | -6.2 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L027 | 05 | ytd_pct | CAT | 50.12 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L028 | 05/07 | hv30_ann_pct | CAT | 39.5 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L029 | 01/04/05/06/07 | last_price | CEG | 242.72 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L030 | 05 | chg_1d_pct | CEG | -3.55 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L031 | 05 | ytd_pct | CEG | -31.2 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L032 | 05/07 | hv30_ann_pct | CEG | 49.01 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L033 | 01/04/05/06/07 | last_price | COST | 980.45 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L034 | 05 | chg_1d_pct | COST | 1.22 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L035 | 05 | ytd_pct | COST | 13.85 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L036 | 05/07 | hv30_ann_pct | COST | 24.69 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L037 | 01/04/05/06/07 | last_price | CVX | 191.01 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L038 | 05 | chg_1d_pct | CVX | 2.28 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L039 | 05 | ytd_pct | CVX | 26.56 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L040 | 05/07 | hv30_ann_pct | CVX | 27.07 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L041 | 01/04/05/06/07 | last_price | ETN | 377.23 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L042 | 05 | chg_1d_pct | ETN | -6.1 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L043 | 05 | ytd_pct | ETN | 18.8 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L044 | 05/07 | hv30_ann_pct | ETN | 45.45 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L045 | 01/04/05/06/07 | last_price | GE | 321.95 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L046 | 05 | chg_1d_pct | GE | -2.57 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L047 | 05 | ytd_pct | GE | 4.52 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L048 | 05/07 | hv30_ann_pct | GE | 34.02 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L049 | 01/04/05/06/07 | last_price | GOOGL | 356.64 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L050 | 05 | chg_1d_pct | GOOGL | -2.09 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L051 | 05 | ytd_pct | GOOGL | 13.91 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L052 | 05/07 | hv30_ann_pct | GOOGL | 36.07 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L053 | 01/04/05/06/07 | last_price | JPM | 311.55 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L054 | 05 | chg_1d_pct | JPM | -0.37 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L055 | 05 | ytd_pct | JPM | -2.88 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L056 | 05/07 | hv30_ann_pct | JPM | 21.6 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L057 | 01/04/05/06/07 | last_price | LIN | 509.2 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L058 | 05 | chg_1d_pct | LIN | -1.24 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L059 | 05 | ytd_pct | LIN | 19.82 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L060 | 05/07 | hv30_ann_pct | LIN | 21.79 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L061 | 01/04/05/06/07 | last_price | LLY | 1138.16 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L062 | 05 | chg_1d_pct | LLY | -0.57 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L063 | 05 | ytd_pct | LLY | 6.08 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L064 | 05/07 | hv30_ann_pct | LLY | 38.18 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L065 | 01/04/05/06/07 | last_price | MCK | 790.22 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L066 | 05 | chg_1d_pct | MCK | 0.76 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L067 | 05 | ytd_pct | MCK | -3.59 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L068 | 05/07 | hv30_ann_pct | MCK | 32.13 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L069 | 01/04/05/06/07 | last_price | META | 573.36 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L070 | 05 | chg_1d_pct | META | -1.92 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L071 | 05 | ytd_pct | META | -13.25 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L072 | 05/07 | hv30_ann_pct | META | 36.49 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L073 | 01/04/05/06/07 | last_price | MSFT | 400.57 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L074 | 05 | chg_1d_pct | MSFT | -0.7 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L075 | 05 | ytd_pct | MSFT | -17.1 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L076 | 05/07 | hv30_ann_pct | MSFT | 33.33 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L077 | 01/04/05/06/07 | last_price | MU | 891.66 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L078 | 05 | chg_1d_pct | MU | -4.73 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L079 | 05 | ytd_pct | MU | 212.47 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L080 | 05/07 | hv30_ann_pct | MU | 101.35 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L081 | 01/04/05/06/07 | last_price | NVDA | 201.65 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L082 | 05 | chg_1d_pct | NVDA | -3.14 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L083 | 05 | ytd_pct | NVDA | 7.79 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L084 | 05/07 | hv30_ann_pct | NVDA | 41.27 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L085 | 01/04/05/06/07 | last_price | PG | 149.44 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L086 | 05 | chg_1d_pct | PG | 0.52 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L087 | 05 | ytd_pct | PG | 5.01 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L088 | 05/07 | hv30_ann_pct | PG | 22.56 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L089 | 01/04/05/06/07 | last_price | PLD | 146.37 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L090 | 05 | chg_1d_pct | PLD | -0.78 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L091 | 05 | ytd_pct | PLD | 14.66 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L092 | 05/07 | hv30_ann_pct | PLD | 19.12 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L093 | 01/04/05/06/07 | last_price | TSLA | 382.13 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L094 | 05 | chg_1d_pct | TSLA | -3.67 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L095 | 05 | ytd_pct | TSLA | -15.03 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L096 | 05/07 | hv30_ann_pct | TSLA | 44.33 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L097 | 01/04/05/06/07 | last_price | UNH | 407.13 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L098 | 05 | chg_1d_pct | UNH | -1.42 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L099 | 05 | ytd_pct | UNH | 23.33 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L100 | 05/07 | hv30_ann_pct | UNH | 26.42 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L101 | 01/04/05/06/07 | last_price | V | 324.68 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L102 | 05 | chg_1d_pct | V | -0.11 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L103 | 05 | ytd_pct | V | -7.23 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L104 | 05/07 | hv30_ann_pct | V | 33.18 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L105 | 01/04/05/06/07 | last_price | VRT | 277.65 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L106 | 05 | chg_1d_pct | VRT | -4.1 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L107 | 05 | ytd_pct | VRT | 71.38 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L108 | 05/07 | hv30_ann_pct | VRT | 65.54 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L109 | 01/04/05/06/07 | last_price | VST | 138.98 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L110 | 05 | chg_1d_pct | VST | -4.95 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L111 | 05 | ytd_pct | VST | -13.85 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L112 | 05/07 | hv30_ann_pct | VST | 43.96 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L113 | 01/04/05/06/07 | last_price | WMT | 119.83 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L114 | 05 | chg_1d_pct | WMT | 0.8 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L115 | 05 | ytd_pct | WMT | 7.78 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L116 | 05/07 | hv30_ann_pct | WMT | 29.11 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L117 | 01/04/05/06/07 | last_price | XOM | 151.35 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | entry_price, ranking, CI, predictions |
| L118 | 05 | chg_1d_pct | XOM | 1.64 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (change) | DELAYED | OBSERVED | technical RS factor |
| L119 | 05 | ytd_pct | XOM | 26.63 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (year_to_date_change) | DELAYED | OBSERVED | technical momentum factor |
| L120 | 05/07 | hv30_ann_pct | XOM | 30.09 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (historical_vol 30d) | DELAYED | OBSERVED | sigma chain REALIZED_VOL_30D, vol penalty |
| L121 | 03 | last_price | SPY | 728.31 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | benchmark, regime, MoM, predictions benchmark_price |
| L122 | 03 | chg_1d_pct | SPY | -1.19 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | regime, RS baseline |
| L123 | 03 | perf_1m_pct | SPY | 5.02 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | regime |
| L124 | 03 | ytd_pct | SPY | 10.98 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | regime |
| L125 | 03 | hv30_ann_pct | SPY | 12.4 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | beta denominator context |
| L126 | 03 | high_52w | SPY | 760.39 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (misc_statistics) | DELAYED | OBSERVED | regime drawdown-from-high |
| L127 | 03 | last_price | QQQ | 696.61 | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | regime |
| L128 | 03 | chg_1d/1m/ytd | QQQ | -1.59 / +10.56 / +20.36 | % | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | regime growth-vs-broad |
| L129 | 03 | last/chg_1d | VIX | 21.36 / +7.5% | idx | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) (CBOE IND) | DELAYED | OBSERVED | regime vol classification |
| L130 | 03 | prior_close | VIX | 19.87 | idx | 2026-06-09 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | regime vol classification |
| L131 | 03 | last/chg_1d/1m/ytd | TLT | 84.94 / -0.21% / +0.51% / -0.25% | USD | 2026-06-10 | IBKR MCP get_price_snapshot (SMART) | DELAYED | OBSERVED | rates regime (no rate shock) |
| L132 | 01/02/07 | daily_close_series_3m | SPY | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L133 | 01/02/07 | daily_close_series_3m | NVDA | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L134 | 01/02/07 | daily_close_series_3m | MSFT | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L135 | 01/02/07 | daily_close_series_3m | META | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L136 | 01/02/07 | daily_close_series_3m | GOOGL | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L137 | 01/02/07 | daily_close_series_3m | AMZN | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L138 | 01/02/07 | daily_close_series_3m | MCK | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L139 | 01/02/07 | daily_close_series_3m | COST | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L140 | 01/02/07 | daily_close_series_3m | WMT | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L141 | 01/02/07 | daily_close_series_3m | CVX | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L142 | 01/02/07 | daily_close_series_3m | UNH | 62 bars 2026-03-13..2026-06-10 | USD | 2026-06-10 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | DELAYED | OBSERVED | beta60, corr, vol30, MoM prior prices |
| L143 | 02 | close_2026-05-12 | SPY | 738.18 | USD | 2026-05-12 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | HISTORICAL | OBSERVED | MoM baseline price |
| L144 | 02 | close_2026-05-12 | MSFT | 407.77 | USD | 2026-05-12 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | HISTORICAL | OBSERVED | MoM baseline price |
| L145 | 02 | close_2026-05-12 | NVDA | 220.78 | USD | 2026-05-12 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | HISTORICAL | OBSERVED | MoM baseline price |
| L146 | 02 | close_2026-05-12 | META | 603.0 | USD | 2026-05-12 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | HISTORICAL | OBSERVED | MoM baseline price |
| L147 | 02 | close_2026-05-12 | GOOGL | 387.35 | USD | 2026-05-12 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | HISTORICAL | OBSERVED | MoM baseline price |
| L148 | 02 | close_2026-05-12 | AMZN | 265.82 | USD | 2026-05-12 | IBKR MCP get_price_history THREE_MONTHS/ONE_DAY (SMART) | HISTORICAL | OBSERVED | MoM baseline price |
| L149 | 02 | mom_return / alpha_vs_SPY | MSFT | -1.77% / -0.43pp | % | 2026-06-10 | DERIVED: px_now/px_0512-1; alpha=ret-SPY_ret(-1.34%); inputs: close_2026-05-12 + last_price rows | DELAYED | DERIVED | reflection Hit/Miss, carry-forward |
| L150 | 02 | mom_return / alpha_vs_SPY | NVDA | -8.66% / -7.33pp | % | 2026-06-10 | DERIVED: px_now/px_0512-1; alpha=ret-SPY_ret(-1.34%); inputs: close_2026-05-12 + last_price rows | DELAYED | DERIVED | reflection Hit/Miss, carry-forward |
| L151 | 02 | mom_return / alpha_vs_SPY | META | -4.92% / -3.58pp | % | 2026-06-10 | DERIVED: px_now/px_0512-1; alpha=ret-SPY_ret(-1.34%); inputs: close_2026-05-12 + last_price rows | DELAYED | DERIVED | reflection Hit/Miss, carry-forward |
| L152 | 02 | mom_return / alpha_vs_SPY | GOOGL | -7.93% / -6.59pp | % | 2026-06-10 | DERIVED: px_now/px_0512-1; alpha=ret-SPY_ret(-1.34%); inputs: close_2026-05-12 + last_price rows | DELAYED | DERIVED | reflection Hit/Miss, carry-forward |
| L153 | 02 | mom_return / alpha_vs_SPY | AMZN | -10.22% / -8.89pp | % | 2026-06-10 | DERIVED: px_now/px_0512-1; alpha=ret-SPY_ret(-1.34%); inputs: close_2026-05-12 + last_price rows | DELAYED | DERIVED | reflection Hit/Miss, carry-forward |
| L154 | 07 | beta60 | MCK | -0.17 | ratio | 2026-06-10 | DERIVED: cov(r_t,r_SPY)/var(r_SPY), 60d daily, inputs: close series rows | DELAYED | DERIVED | portfolio beta check |
| L155 | 07/15 | sigma_1m | MCK | 6.49 | % | 2026-06-10 | DERIVED: stdev(last 21 daily rets)*sqrt(252)/sqrt(12), inputs: close series | DELAYED | DERIVED | CI bounds, predictions |
| L156 | 07 | beta60 | COST | -0.14 | ratio | 2026-06-10 | DERIVED: cov(r_t,r_SPY)/var(r_SPY), 60d daily, inputs: close series rows | DELAYED | DERIVED | portfolio beta check |
| L157 | 07/15 | sigma_1m | COST | 7.77 | % | 2026-06-10 | DERIVED: stdev(last 21 daily rets)*sqrt(252)/sqrt(12), inputs: close series | DELAYED | DERIVED | CI bounds, predictions |
| L158 | 07 | beta60 | WMT | +0.24 | ratio | 2026-06-10 | DERIVED: cov(r_t,r_SPY)/var(r_SPY), 60d daily, inputs: close series rows | DELAYED | DERIVED | portfolio beta check |
| L159 | 07/15 | sigma_1m | WMT | 9.94 | % | 2026-06-10 | DERIVED: stdev(last 21 daily rets)*sqrt(252)/sqrt(12), inputs: close series | DELAYED | DERIVED | CI bounds, predictions |
| L160 | 07 | beta60 | CVX | -0.88 | ratio | 2026-06-10 | DERIVED: cov(r_t,r_SPY)/var(r_SPY), 60d daily, inputs: close series rows | DELAYED | DERIVED | portfolio beta check |
| L161 | 07/15 | sigma_1m | CVX | 7.28 | % | 2026-06-10 | DERIVED: stdev(last 21 daily rets)*sqrt(252)/sqrt(12), inputs: close series | DELAYED | DERIVED | CI bounds, predictions |
| L162 | 07 | beta60 | UNH | +0.35 | ratio | 2026-06-10 | DERIVED: cov(r_t,r_SPY)/var(r_SPY), 60d daily, inputs: close series rows | DELAYED | DERIVED | portfolio beta check |
| L163 | 07/15 | sigma_1m | UNH | 8.27 | % | 2026-06-10 | DERIVED: stdev(last 21 daily rets)*sqrt(252)/sqrt(12), inputs: close series | DELAYED | DERIVED | CI bounds, predictions |
| L164 | 07 | avg_pairwise_corr60 | portfolio5 | +0.184 | ratio | 2026-06-10 | DERIVED: mean of 10 pairwise 60d return corrs | DELAYED | DERIVED | correlation cap check (<0.45 PASS) |
| L165 | 07 | sleeve_beta | portfolio5 | -0.14 | ratio | 2026-06-10 | DERIVED: sum(w_i*beta_i), normalized sleeve weights | DELAYED | DERIVED | beta band check (0.90-1.10 FAIL) |
| L166 | 07 | sleeve_sigma_1m / dd95_1m | portfolio5 | 4.68% / 7.72% | % | 2026-06-10 | DERIVED: sqrt(w'Cov w) 1m; dd95=1.65*sigma (normality stated) | DELAYED | DERIVED | drawdown cap check (<=8% PASS) |
| L167 | 05 | next_earnings_date | MCK | 2026-08-05 ESTIMATED (+/-5d) | date | 2026-06-10 | prior report 2026-05-06 observed in fetched tape gap | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L168 | 05 | next_earnings_date | COST | 2026-09-24 ESTIMATED (+/-5d) | date | 2026-06-10 | prior report 2026-05-28 observed in tape gap | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L169 | 05 | next_earnings_date | WMT | 2026-08-19 ESTIMATED (+/-5d) | date | 2026-06-10 | prior report 2026-05-20 observed in tape gap | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L170 | 05 | next_earnings_date | CVX | 2026-07-31 ESTIMATED (+/-5d) | date | 2026-06-10 | cadence from reference state | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L171 | 05 | next_earnings_date | UNH | 2026-07-16 ESTIMATED (+/-5d) | date | 2026-06-10 | prior report 2026-04-21 observed in tape gap | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L172 | 05 | next_earnings_date | MU | 2026-06-25 ESTIMATED (+/-5d) | date | 2026-06-10 | fiscal Q3 cadence — INSIDE buffered 19d window, penalty applied | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L173 | 05 | next_earnings_date | XOM | 2026-07-31 ESTIMATED (+/-5d) | date | 2026-06-10 | cadence | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L174 | 05 | next_earnings_date | LIN | 2026-07-31 ESTIMATED (+/-5d) | date | 2026-06-10 | cadence | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L175 | 05 | next_earnings_date | LLY | 2026-08-06 ESTIMATED (+/-5d) | date | 2026-06-10 | cadence | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L176 | 05 | next_earnings_date | NVDA | 2026-08-26 ESTIMATED (+/-5d) | date | 2026-06-10 | fiscal cadence | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L177 | 05 | next_earnings_date | GOOGL | 2026-07-28 ESTIMATED (+/-5d) | date | 2026-06-10 | cadence | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L178 | 05 | next_earnings_date | ABBV | 2026-07-31 ESTIMATED (+/-5d) | date | 2026-06-10 | cadence | HISTORICAL | INFERRED | 14d earnings penalty (buffered <=19d) |
| L179 | 05 | fundamental/sentiment/macro family sub-scores | 30 names | -2..+2 per name, table in 05_factor_scores.md | score | 2026-06-10 | Analyst judgment on training-reference state (vintage <=2026-01), cadence-adjusted; cross-checked vs gpt-5-2026-06-09 consensus notes | HISTORICAL | INFERRED | composite score (DQ multiplier 0.85 + MEDIUM confidence cap applied) |
| L180 | 15 | mu per ranked name | 12 names | mu Calibration Table band by SAMPLED_PCTL(n=30); MU shaded -2pp (earnings window, ledger row above) | % | 2026-06-10 | eval/research_system.md mu table | DELAYED | DERIVED | predictions, target prices |

## Coverage Summary

| Claim type | Rows | Notes |
|---|---:|---|
| OBSERVED | 148 | Tool-fetched prices, vols, returns, macro |
| DERIVED | 19 | Betas, sigmas, correlations, MoM returns, CIs — formulas cited in-row |
| INFERRED | 13 | Earnings cadence estimates + fundamental/sentiment/macro sub-scores (training-reference, disclosed) |
| ILLUSTRATIVE | 0 | None — run is fully fetched |
| UNAVAILABLE | 0 | No required field unavailable; Enhancing inputs listed above are absent but never block GO |

Critical-field status: no Required input failed. The run is eligible for GO/NO_TRADE/REVIEW_ONLY on portfolio-construction merits, not data grounds.
