# Regime And Data

**Date:** 2026-06-07  
**Regime label:** `HIGH_VOL / RATE_SHOCK`  
**Regime confidence:** `MEDIUM`  
**Data state:** `MIXED_DELAYED`

## Regime Evidence

| Input | Latest Value | Tag | Interpretation |
| --- | ---: | --- | --- |
| `SPY` | 737.55, -2.50% from May 29 close | `DELAYED` | Broad market sold off into the weekend. |
| `QQQ` | 705.06, -4.50% from May 29 close | `DELAYED` | Growth / tech underperformed sharply. |
| `SMH` | 569.69, -4.88% from May 29 close | `DELAYED` | Semiconductor weakness confirms AI-crowding unwind. |
| `XLK` | 180.30, -5.61% from May 29 close | `DELAYED` | Technology was the major laggard. |
| `XLE` | 57.67, +2.45% from May 29 close | `DELAYED` | Energy leadership supports inflation hedge rotation. |
| `XLF` | 52.30, +1.40% from May 29 close | `DELAYED` | Banks/financials benefited from rate shift. |
| `XLP` | 83.44, +0.64% from May 29 close | `DELAYED` | Staples acted defensively. |
| `VIX` | 21.51 on 2026-06-05 | `OFFICIAL DELAYED` | Volatility moved above the low-vol comfort zone. |
| 10Y Treasury | 4.55% at 2026-06-05 close | `DELAYED` | Rate pressure is a primary driver. |
| May payrolls | +172,000 | `OFFICIAL` | Strong jobs report reduced rate-cut expectations in market narrative. |
| Next FOMC | 2026-06-16 to 2026-06-17 | `OFFICIAL` | Macro event risk falls inside the 2-6 week horizon. |

## Market Narrative

The June 5 session changed the short-horizon setup. AP reported the S&P 500 fell 2.6%, the Nasdaq fell 4.2%, and the Russell 2000 fell 3.5%. Axios and Kiplinger both attributed the pressure to a technology/semiconductor selloff, stronger payrolls, rising yields, and AI-bubble/capex concerns. The correct regime response is to de-emphasize crowded AI beta and promote names with relative strength in energy, financials, healthcare, staples, and selected industrials.

## Event Risk

| Event | Date | Risk |
| --- | --- | --- |
| U.S. CPI | 2026-06-10 | High macro sensitivity for rates and growth multiples. |
| Oracle Q4 FY26 earnings | 2026-06-10 after close | Excludes `ORCL` from candidate set under 14-day event rule. |
| FOMC meeting | 2026-06-16 to 2026-06-17 | Could extend or reverse the rate-shock rotation. |
| June options expiration | 2026-06-19 | Potential volatility around crowded tech de-risking. |

## Data Handoff

The factor scoring agent should:

1. Penalize high-beta AI momentum after the June 5 selloff.
2. Promote relative strength in `XLE`, `XLF`, `XLP`, healthcare, and selected cyclicals.
3. Exclude `ORCL` due June 10 earnings.
4. Keep all confidence labels capped at `MEDIUM` because the run lacks options, short-interest, and validated risk feeds.
