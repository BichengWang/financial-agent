# Evidence and artifact contract

All paths are checkout-local. A canonical run is `docs/research/tickers/TICKER/YYYY-MM-DD/`: `report.md` is the direct reading entry, while `data/evidence.json`, `data/calculations.json`, and `data/audit.json` retain machine artifacts. Imported baselines stay separate in `archive/`. `docs/research/README.md` is authored run guidance; `docs/research/index.md` alone is generated dated ticker navigation, conditional model target tables, coverage and evidence gaps. Shared context, corroboration reviews and verification live in `docs/research/batches/YYYY-MM-DD/` without a comparison README or per-ticker README histories. New dated runs preserve earlier artifacts.

## Evidence envelope

- `schema_version`: integer `1`.
- `ticker`: security identifier matching its directory.
- `as_of`: `YYYY-MM-DD`, the requested research date.
- `currency`: `USD` for this implementation; do not silently convert another currency.
- `quote_time`: timezone-aware ISO datetime of observed quote, no later than as-of and at most seven calendar days old. A missing valid quote is not current evidence.
- `sources`: list of `{id, url, title, publisher, accessed_at, excerpt}`. IDs are unique strings; URLs point to observed documents; accessed_at is ISO date. Retain relevant observed text, including units and periods. A copied URL without a fetched excerpt is not an observation. State the actual publisher, not the hosting mirror.
- `facts`: mapping from fact ID to `{value, unit, period, kind, sources, note}`. `value` is decimal string or null; `unit` is `USD`, `shares`, `USD/share`, or `decimal`; `period` is a nonempty fiscal/date description; `kind` is `reported`, `estimate`, `assumption`, or `unavailable`; `sources` lists source IDs; `note` explains definitions, reconciliation and limitations.
- Required **reported** facts also retain `observations`: list of `{source, value, period}`. Each is a directly observed decimal-string value and period linked to one source ID. At least two distinct publishers must support the canonical value and period. Missing observations => provisional; conflicting canonical value/period => blocked. Normalize millions/splits only with an explicit note and source excerpt showing original units. If primary data settles a disagreement, explain why the incompatible observation is not valid corroboration; never manufacture agreement.

## Required facts

| ID | Unit | Definition |
|---|---|---|
| price | USD/share | actual dated quote, split basis disclosed |
| shares | shares | dated actual shares outstanding across applicable classes; not weighted-average EPS shares |
| market_cap | USD | reported capitalization on comparable security/time basis |
| revenue | USD | consolidated annual or explicitly identified TTM revenue |
| net_income | USD | consolidated GAAP income with attribution basis stated |
| operating_cash_flow | USD | reported operating cash flow, fiscal period identified |
| capital_expenditure | USD | positive capital cash spend, same period as operating cash flow |
| cash | USD | consolidated cash/equivalents, exclusions and restrictions disclosed |
| debt | USD | consolidated debt, lease treatment stated |
| eps | USD/share | GAAP diluted EPS, period and split basis stated |

All ten keys remain present even if unavailable. Null values have kind `unavailable` and a reason. An estimated required fundamental must be labeled, not masquerade as reported, and prevents fully verified status. Fiscal year-end balance-sheet facts need not be called current; share-count date must be made explicit separately from quote date. Short-term investments are not silently included in cash. Non-GAAP metrics use separate IDs and notes; forecast EPS is not reported GAAP EPS.

## Optional valuation configuration

`forward_eps` may be a sourced analyst forecast in USD/share, kind `estimate`, with forecast period, observation date and note. `required_return` is a justified `assumption` in `decimal`; `risk_free_rate` is a contemporary sourced reported/estimated USD rate in `decimal`. Its `period` is the bare ISO observation date `YYYY-MM-DD` (no future date; no older than seven days); record instrument and maturity in `note`. Rates use fractions, not percentage points. Required return exceeds risk-free rate; no hardcoded yields.

When suitable inputs exist, include:

```json
{
  "valuation": {
    "base_eps": "forward_eps",
    "discount_rate": "required_return",
    "risk_free_rate": "risk_free_rate",
    "timing": {
      "kind": "assumption",
      "valuation_date": "2026-10-11",
      "terminal_date": "2031-10-11",
      "eps_basis": "normalized_run_rate",
      "alignment_note": "Assumes the sourced EPS is a current run-rate proxy; five growth periods end at the stated date and the exit multiple uses trailing terminal EPS."
    },
    "scenarios": [
      {"name": "bear", "growth": "0.00", "exit_multiple": "12", "years": 5, "probability": "0.25"},
      {"name": "base", "growth": "0.05", "exit_multiple": "16", "years": 5, "probability": "0.50"},
      {"name": "bull", "growth": "0.10", "exit_multiple": "20", "years": 5, "probability": "0.25"}
    ]
  }
}
```

This configuration example demonstrates syntax, not recommended inputs. Justify every scenario assumption in the report. Exactly three bear/base/bull cases share a positive integer horizon and probabilities sum to one. EPS basis must be positive and sourced or explicitly assumed. If inputs are unavailable or unsuitable, omit valuation entirely and mark provisional—do not substitute the example numbers. Explicit legitimate forecast/model assumptions alone do not imply factual verification or automatically invalidate an otherwise grounded audit; all remain disclosed.

`valuation.timing` explicitly declares a hypothetical calendar mapping, not a future reported fact. Its `valuation_date` must equal `as_of`; `terminal_date` must be the same calendar anniversary after the common scenario `years` (February 29 maps to February 28 in non-leap terminal years). `eps_basis` is `trailing`, `forward` or `normalized_run_rate`. A nonempty `alignment_note` must explain the sourced EPS fiscal period, any current-run-rate normalization and the exit multiple's forward/trailing convention. The example's normalization is an assumption to justify, not a recommendation or an automatic inference.

Missing timing leaves arithmetic available but makes the audit PROVISIONAL: the configured growth/discount periods do not establish a dated holding-period return. Malformed or inconsistent declared timing is BLOCKED. Validation checks declared dates and required disclosure, not the economic truth of a normalization or terminal multiple. Price CAGR is `(terminal_price / reference_price) ** (1 / years) - 1`; EPS CAGR is the separate `growth` input. Neither is an observed YoY return. Discounted present targets must not be substituted for terminal prices in that return formula.

## Report and calculations

Use the graph's exact level-two section headings: Grounding, Business, Moat, Management, Inversion, Industry, Valuation, Decision, Limitations and audit. Cite retained source IDs alongside claims (for example `[issuer-10k]`). All supported arithmetic comes from the native CLI. `data/calculations.json` is engine-generated, not hand-edited: market-cap reconciliation; historical FCF, yield and PE; optional scenario targets, price-only returns, discounted targets and probability-weighted present target. Read its actual keys and values rather than assuming an undocumented shape. Additional financial ratios not implemented by this engine must not be presented as tool-verified.

Engine metric keys are `implied_market_cap`, `market_cap_deviation` (absolute relative deviation), `free_cash_flow`, `free_cash_flow_yield` (FCF divided by reported cap), and `pe`, each a Decimal string or null. Optional `valuation` contains `base_eps_fact`, `discount_rate_fact`, `risk_free_rate_fact`, `scenarios` and `weighted_present_target`. Each scenario retains its input row plus `target_price`, `total_return` (price-only), `annualized_return`, and `present_target`. No independently fetched truth is encoded by these outputs. Required reported observations must match periods and agree within graph relative tolerance; publisher identity is normalized by the engine, but real independence still requires researcher judgment.

Audit recomputation is arithmetic and evidence-contract consistency only. It is not independent web verification or an investment approval. Missing data/source gaps and omitted valuation => PROVISIONAL; malformed inputs, incompatible observations and calculation mismatches => BLOCKED; no implemented findings => PASS. Keep source independence and source-truth judgment explicit outside the machine verdict.
