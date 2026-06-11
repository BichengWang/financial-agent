# 03 Regime and Data

## Data Mode

Declared data mode: `DELAYED`. Nasdaq quote/history and Yahoo spark endpoints were fetched during this run and logged in `01_preflight.md`. Required inputs are grounded; enhancing inputs are missing and used only as confidence/exposure caps.

## Regime Classification

| Label | Evidence | Implication |
|---|---|---|
| HIGH_VOL | VIX 19.78, 21-day VIX move 10.69% | Penalize crowded momentum; cap confidence without options/short-interest feeds. |
| RATE_SHOCK overlay | `^TNX` 4.467, 60-day move 6.31% | Avoid relying solely on long-duration growth; require cross-family support. |
| Not BEAR | SPY 60-day return 9.62% remains positive | Long-only research can proceed, but portfolio beta cap still binds. |

## Sector Tape

| Sector | ETF | 21D Return | 60D Return |
|---|---|---:|---:|
| Communication Services | XLC | -3.29% | -2.88% |
| Consumer Discretionary | XLY | -2.47% | 1.93% |
| Consumer Staples | XLP | 1.55% | 1.23% |
| Energy | XLE | 0.42% | -1.20% |
| Financials | XLF | 2.04% | 6.19% |
| Health Care | XLV | 6.05% | 3.36% |
| Industrials | XLI | 0.18% | 4.91% |
| Information Technology | XLK | 3.56% | 30.03% |
| Materials | XLB | -2.21% | 2.97% |
| Real Estate | XLRE | 1.20% | 5.61% |
| Utilities | XLU | -1.80% | -5.85% |

## Coverage Gaps

- Options IV/skew, short interest, borrow, institutional flow, and full analyst-revision tape are not wired.
- These are enhancing inputs under `rules.md`; they cap confidence and gross exposure but are not cited as GO blockers.
- Full-universe screening is not wired; the run uses the sampled universe protocol with `SAMPLED_PCTL (n=42)`.

## Handoff

Proceed to factor scoring with health care, financials, selected high-quality energy, and individual tech names ranked by fetched price history, EPS surprise, beta, and sector-relative momentum. No empty universe condition exists.
