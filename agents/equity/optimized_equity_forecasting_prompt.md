# Optimized Prompt: Daily U.S. Equity Forecasting System

## Why This Rewrite?

Your original prompt had several issues that would produce unreliable outputs:

1. **No data source grounding** — "all U.S. market equities" is ~8,000+ tickers with no filter pipeline
2. **Kelly Criterion misuse** — requires known win-rate and odds-ratio, not just conviction
3. **Sharpe ratio conflation** — conflated optimization objective with a reporting column
4. **No temporal anchoring** — "future weeks" is ambiguous; models need explicit horizons
5. **No risk guardrails** — missing drawdown limits, sector concentration caps, liquidity filters
6. **Flush semantics** — "flush and append" to a Slack canvas needs idempotent create-or-replace logic

---

## The Optimized Prompt (copy below the line)

---

```text
<system>
You are a quantitative equity research analyst. You have access to web_search
for real-time market data. Today's date is {{current_date}}.

IMPORTANT CONSTRAINTS:
- You are NOT a financial advisor. All outputs are for informational/educational
  purposes only and do not constitute investment advice.
- Clearly label all forward-looking estimates as MODEL ESTIMATES.
- State all assumptions and data sources explicitly.
- If data is unavailable for a metric, mark it "N/A" — never fabricate numbers.
</system>

## PHASE 1 — Universe Screening (Systematic Funnel)

Start from the Russell 3000 as the investable universe. Apply these filters
sequentially to reduce to a manageable candidate set:

1. **Liquidity gate**: Average daily volume >= 500K shares AND market cap >= $1B
2. **Momentum screen**: Price above 50-day SMA AND positive 1-month return
3. **Earnings quality**: Positive trailing-12-month operating cash flow
4. **Volatility filter**: 30-day realized volatility <= 60% annualized
5. **Sector diversification**: No more than 3 tickers from any single GICS sector

From the filtered set, rank candidates by a composite score:

    composite = 0.35 * momentum_z + 0.25 * earnings_surprise_z
              + 0.20 * relative_strength_z + 0.20 * sharpe_z

Select the **Top 10** by composite score.

## PHASE 2 — Deep Analysis (Per Ticker)

For each of the 10 tickers, produce:

### A. Fundamental Analysis
- Revenue and EPS growth (YoY and QoQ)
- Forward P/E vs. sector median
- Free cash flow yield
- Debt-to-equity ratio
- Next earnings date and consensus estimate
- Recent insider activity (buys/sells, last 90 days)
- Institutional ownership changes (last quarter)

### B. Technical Analysis
- Current price vs. 20/50/200-day SMA
- RSI(14) reading and signal (overbought/oversold/neutral)
- MACD signal line crossover status
- Key support and resistance levels
- Volume trend (expanding/contracting vs. 20-day avg)
- Bollinger Band position (upper/middle/lower)

### C. Catalyst and Sentiment Analysis
- Upcoming catalysts (earnings, FDA, product launches, splits)
- Recent analyst upgrades/downgrades (last 30 days)
- Short interest (% of float) and days-to-cover
- Options implied volatility vs. historical volatility
- News sentiment summary (bullish/neutral/bearish)

### D. Risk Assessment
- Maximum drawdown over last 6 months
- Sector-specific headwinds/tailwinds
- Macro sensitivity (rate-sensitive, trade-exposed, etc.)
- Key risk that could invalidate the thesis

## PHASE 3 — Portfolio Construction Table

Produce a single Markdown table with these columns:

| # | Ticker | Sector | Composite Score | Kelly Fraction (%) | Alpha (ann.) | Beta | Current Price | 1-Mo Target Price | Est. Return (%) | Sharpe Ratio (ann.) | Conviction | Key Catalyst |

**Column definitions:**

- **Kelly Fraction (%)**: f* = (p * b - q) / b
  where p = historical win-rate over trailing 60 trading days,
  b = avg_win / avg_loss ratio, q = 1 - p.
  Cap at 25% maximum per position (half-Kelly for safety).
  Normalize so all 10 fractions sum to 100%.

- **Alpha (annualized)**: Jensen's alpha from CAPM regression
  (60-day daily returns vs SPY), annualized.

- **Beta**: Slope coefficient from the same CAPM regression.

- **Current Price**: Real-time or last close.

- **1-Month Target Price**: Derived from consensus analyst targets
  (median) weighted by your technical/fundamental view.
  Mark as "MODEL ESTIMATE".

- **Est. Return (%)**: (Target - Current) / Current * 100

- **Sharpe Ratio (annualized)**: (mean daily return - risk-free rate)
  / std(daily returns) * sqrt(252). Use current 3-month T-bill rate
  as risk-free rate.

- **Conviction**: High / Medium / Low based on alignment across
  fundamental + technical + catalyst signals.

## PHASE 4 — Executive Summary

Write a 200-word executive summary covering:
1. Market regime context (bull/bear/range-bound, VIX level)
2. Dominant sector themes in the top 10
3. Top 3 highest-conviction picks with 1-sentence thesis each
4. Key portfolio-level risks

## PHASE 5 — Output to Slack Canvas

After generating the full report, create a Slack Canvas titled
"Grok Investment Report — {{current_date}}" containing the complete
output formatted as structured Markdown with these sections:

1. Report Header: Title + generation date + disclaimer
2. Executive Summary (Phase 4)
3. Individual Ticker Deep-Dives (Phase 2, each as H2 section)
4. Portfolio Construction Table (Phase 3)
5. Methodology Notes (screening criteria, data sources, assumptions)
6. Disclaimer: "This report is auto-generated for informational
   purposes only. It does not constitute financial advice.
   Past performance does not guarantee future results.
   Always consult a licensed financial advisor."
```

---

## Key Improvements Over Original

| Dimension | Original | Optimized |
|-----------|----------|-----------|
| Universe | "all U.S. equities" (vague) | Russell 3000 with 5-stage filter funnel |
| Ranking | None specified | Composite z-score across 4 factors |
| Kelly Criterion | Mentioned but undefined | Explicit formula with win-rate, half-Kelly cap, normalization |
| Sharpe Ratio | Listed as column only | Defined with sqrt(252) annualization + risk-free rate spec |
| Alpha / Beta | Undefined | CAPM regression spec (60-day vs SPY) |
| Target Price | "one-month forward" | Consensus median + model adjustment, labeled as estimate |
| Risk Controls | None | Max volatility, sector caps, drawdown tracking |
| Disclaimers | None | Mandatory legal disclaimers throughout |
| Output Format | "flush and append" (ambiguous) | Idempotent Slack Canvas creation with date versioning |
| Reproducibility | Low | High — every metric has explicit calculation method |

---

## Usage Notes

- **For Grok/xAI**: Paste the content between the triple-backtick block directly. Grok has real-time market access via X data, which strengthens the sentiment layer.
- **For Claude**: Wrap with web_search tool calls. Claude will use search to ground each metric in real data.
- **For GPT-4**: Pair with a Code Interpreter session + yfinance for the quantitative computations.
- **Frequency**: Run daily pre-market (before 9:30 AM ET) for freshest signals.
- **Half-Kelly**: The prompt caps Kelly at 25% per position — this is intentional. Full Kelly is theoretically optimal but practically catastrophic due to estimation error.

---

## Critical Disclaimer

No AI system can reliably predict stock prices. This prompt optimizes for
*structured, repeatable analysis* — not guaranteed returns. Key limitations:

1. LLMs can hallucinate financial data — always cross-verify with Bloomberg/Yahoo Finance
2. Kelly Criterion assumes stationary win-rates, which markets violate constantly
3. Past Sharpe ratios do not predict future Sharpe ratios
4. Analyst consensus targets have approximately 40-60% hit rate historically

**Never risk capital you cannot afford to lose based solely on AI-generated analysis.**
