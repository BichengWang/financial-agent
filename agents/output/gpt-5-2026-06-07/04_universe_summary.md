# Universe Summary

**Date:** 2026-06-07  
**Universe mode:** Sampled liquid U.S. equity universe, not full universe  
**Publication constraint:** `REVIEW_ONLY`

## Universe Construction

The sampled screen included 60 liquid U.S.-listed equities across technology, communication services, industrials, energy, healthcare, financials, staples, discretionary, defense, and AI-infrastructure themes. Thirteen ETFs/index products were used for regime and sector context, not candidate selection.

Inclusion filters applied by construction:

| Filter | Result |
| --- | --- |
| U.S. primary listing | Pass for scored equities |
| Price > $5 | Pass |
| Large/mid-cap liquidity | Pass by sampling design and delayed volume checks |
| Listing age > 6 months | Pass for established names; `CRWV` treated as watch-only due newer listing/crowding risk |
| Market cap > $2B | Pass by sampling design, not independently revalidated for every name |

## Sector Context

| Group | Representative Inputs | June 5 Read |
| --- | --- | --- |
| Technology / semis | `XLK`, `SMH`, `NVDA`, `AVGO`, `AMD`, `MU` | Weak; crowded growth de-risked. |
| Financials | `XLF`, `JPM`, `GS`, `BAC`, `C` | Strong relative group as yields rose. |
| Energy | `XLE`, `XOM`, `CVX`, `COP`, `EOG` | Strongest regime hedge in the sample. |
| Healthcare | `UNH`, `MCK`, `ABBV`, `LLY`, `HCA` | Defensive leadership in several names. |
| Staples | `WMT`, `PG`, `COST`, `KO`, `PEP` | Lower-beta protection; mixed but positive leaders. |
| Industrials | `CAT`, `GE`, `HWM`, `ETN`, `PWR`, `EME` | Selectively resilient; power/aerospace/capex cyclicals remain relevant. |

## Rejection Log

| Ticker | Reason |
| --- | --- |
| `ORCL` | Confirmed June 10 earnings inside 14-day event window. |
| `AVGO` | Post-earnings drawdown and AI guidance disappointment made it unsuitable for top sleeve despite strong AI revenue. |
| `PLTR` | High-beta momentum drawdown; -13.17% versus prior package price. |
| `COIN`, `HOOD`, `APP`, `CRWV` | High beta / drawdown profile too aggressive in `HIGH_VOL / RATE_SHOCK` regime. |
| `NVDA`, `AMD`, `MU`, `DELL` | AI/semiconductor crowding and drawdown risk; keep as structural watch, not current top sleeve. |
| `MSFT`, `GOOGL`, `AMZN`, `META` | Platform AI fundamentals remain strong, but June 5 price action and rate sensitivity cap near-term rank. |
| `HON` | Large weekly drawdown in sample; insufficient current technical confirmation. |
| `NOC`, `LMT` | Defense theme plausible but no current price leadership in sample. |
| `PEP`, `HCA`, `V`, `MA`, `HD` | Lower relative rank versus better defensive or financial alternatives. |

## Handoff To Factor Scoring

Score the following leadership candidates first: `AZO`, `UNH`, `MCK`, `JPM`, `XOM`, `CAT`, `WMT`, `ABBV`, `GS`, `PG`, with near-miss monitoring for `GE`, `CVX`, `BAC`, `C`, `COST`, `ORLY`, `EOG`, `RTX`, `LLY`, and `AMAT`.
