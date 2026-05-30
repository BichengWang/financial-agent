# 04 Universe Summary

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Counts are reference-state estimates of the U.S. primary-listed equity set; tagged `ILLUSTRATIVE_REF`. Detailed name-level exclusion only includes representatives from the reference-state universe; today's intra-day liquidity / spread fields are `N/A`.

## Universe Funnel

| Step | Rule (per `research_system.md` §Universe Construction) | Approx. count | Notes |
|---|---|---|---|
| 0 | Reference-state U.S. primary-listed | ≈ 4,800 | Reference vintage ~2026-01 |
| 1 | Market cap > $2B | ≈ 2,100 | Eliminates micro / small-cap tail |
| 2 | 20D ADV > $20M | ≈ 1,600 | Eliminates thinly traded names |
| 3 | Price > $5 | ≈ 1,590 | Eliminates penny / sub-$5 |
| 4 | Listing age > 6 months | ≈ 1,560 | Eliminates recent IPOs / SPAC unwinds |
| 5 | Traded 80% of sessions in trailing 60D | ≈ 1,555 | Eliminates intermittent listings |
| 6 | Exclude bid-ask > 50 bps | ≈ 1,520 | Approximate; live spread `N/A` so step is by reference-state heuristic |
| 7 | Exclude halted / pending delisting | ≈ 1,510 | Reference-state |
| 8 | Exclude unresolved corp-action ambiguity | ≈ 1,500 | Reference-state |
| → | **Eligible universe** | **≈ 1,500** | Passed to factor scoring |

## Rejection Log (Representative)

Only categories are listed; individual reference-state rejections are not enumerated because today's run is concerned with the investable subset, not a full audit of the rejected tail.

| Category | Approx. count | Example reference-state names | Rejection reason |
|---|---|---|---|
| Thin ADRs | ~50 | (Various) | ADR liquidity below the 80% session filter or spread > 50bps |
| Pending delisting / restructuring | ~10 | (Various) | Corp-action ambiguity |
| Sub-$2B mid-caps | (large) | (Various) | Below the market-cap floor |
| Halted | 0 today (reference) | none | n/a |
| Recent IPO < 6mo | ~25 | (Various) | Listing-age floor |

## Sector Distribution Of Eligible Universe (Reference-State, GICS L1)

| Sector | Eligible count | Share |
|---|---:|---:|
| Information Technology | 230 | 15.3% |
| Health Care | 200 | 13.3% |
| Financials | 245 | 16.3% |
| Industrials | 215 | 14.3% |
| Consumer Discretionary | 175 | 11.7% |
| Communication Services | 70 | 4.7% |
| Consumer Staples | 80 | 5.3% |
| Energy | 80 | 5.3% |
| Materials | 80 | 5.3% |
| Utilities | 65 | 4.3% |
| Real Estate | 60 | 4.0% |
| **Total** | **1,500** | **100%** |

Shares are stable across the 05-12, 05-24, and today's runs.

## Event-Calendar Concentration In The Eligible Universe

Per the 19-day buffered earnings window (14d policy + 5d cadence drift):

| Sector | Names with reference Q2 print inside 19d window | Notes |
|---|---|---|
| Info Tech | ≈ 8 — includes AVGO (~7d), CRM (~10d), HPE (~15d) | AVGO is the only one carried into today's candidate set; the others were excluded earlier on score / crowding |
| Industrials | ≈ 4 | None carried into today's set |
| Financials | ≈ 1 | None carried |
| Other | ≈ 6 | None carried |
| **Total inside window** | ≈ 19 of 1,500 (~1.3%) | Standard pre-summer dispersion |

Event-concentration risk at the universe level is **not elevated**.

## Universe Quality Stance

| Question | Answer |
|---|---|
| Is the eligible universe large enough to produce a credible top-N? | Yes. 1,500 is comfortably above the operational threshold; thin-universe `HALTED` (per `stop_criteria.md` §Hard Halt item 4) is not triggered. |
| Did the rejection logic systematically eliminate the upside? | No. Reference-state coverage of mega/large-cap growth and defensive-quality is preserved. |
| Is event concentration manageable? | Yes. The only carried name inside the buffered window (AVGO) is being dropped at the carry-forward stage, not the portfolio stage. |

## Handoff Note → Factor Scoring Agent

> 1,500-name reference-state universe; sector distribution stable; event concentration not elevated. AVGO arrives at scoring with the carry-forward `DROP` flag already applied (see `02_reflection.md` §5). Score the remaining universe per the four-family baseline, surface the top 20 by adjusted score, recommend an investable subset of 5-10 names, and tag every numeric per the §ILLUSTRATIVE_MODE OP item 3 split.
