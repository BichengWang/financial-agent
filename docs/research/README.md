# Research run guidance

Browse [the research index](index.md) for dated reports, ticker history, conditional model targets and evidence gaps. This README is author-written operating guidance; the index is generated navigation, not a source-verification service.

## Repository-local layout

```text
docs/research/
  README.md                         # authored run guidance
  index.md                          # generated dates, tickers and target tables
  tickers/TICKER/DATE/
    report.md                       # direct entry; all nine graph sections
    data/{evidence,calculations,audit}.json
    archive/                        # imported baselines/history, when present
  batches/DATE/                     # shared materials, no comparison README
    market-context.json
    verification.json
    corroboration-review.md         # when present
    archive/                        # earlier execution receipts, when present
```

Create a new dated folder for each new research date; preserve earlier reports, evidence, calculations, audits and imported baselines. The folder date is a research date, not necessarily the quote or financial-statement date.

## Run from the repository root

Use Python 3.12 through `uv`; the numeric CLI uses the standard library. Start with the [research skill](../../skills/equity-investment-research/SKILL.md), [graph](../../skills/equity-investment-research/graph.toml) and [evidence contract](../../skills/equity-investment-research/references/evidence-contract.md).

```sh
uv run --python 3.12 python skills/equity-investment-research/scripts/research.py graph
uv run --python 3.12 python skills/equity-investment-research/scripts/research.py plan --tickers AAPL AMZN CRM GOOGL INTC META MSFT NFLX TSLA --as-of 2026-10-11
```

`graph` validates the dependency graph and instruction references. `plan` prints dependency order and destinations; it does not fetch sources, create researched facts or automatically execute the analytical nodes. For a smaller run, use `--tickers CRM MSFT` and the actual research date.

Collect and read sources yourself using the ready nodes' instructions, completing prerequisites in graph order: grounding, business, moat, management, inversion, industry, valuation, decision, and limitations/audit. Retain actual source excerpts and observations in `data/evidence.json` under the evidence contract; write the corresponding nine sections in `report.md`. Two URLs are not two independent publishers. Record unavailable facts honestly rather than inventing inputs. Shared observed market context belongs in the dated batch folder, not duplicated across navigation pages.

After collecting evidence and documenting justified model assumptions, calculate supported numeric results, finalize the report against those saved results, and audit the exact run directory:

```sh
uv run --python 3.12 python skills/equity-investment-research/scripts/research.py calculate docs/research/tickers/CRM/2026-10-11/data/evidence.json --output docs/research/tickers/CRM/2026-10-11/data/calculations.json
uv run --python 3.12 python skills/equity-investment-research/scripts/research.py audit docs/research/tickers/CRM/2026-10-11 --output docs/research/tickers/CRM/2026-10-11/data/audit.json
uv run --python 3.12 python skills/equity-investment-research/scripts/research.py index
```

These are usage recipes, not execution receipts. Substitute your ticker and date consistently. Audit exits **0 for PASS**, **1 for PROVISIONAL or BLOCKED**; retain findings rather than weakening policy to pass. `index` refreshes only `index.md`: it never rewrites this guide, reports or research data and creates no ticker/batch README wrappers. Record actual executions separately in dated batch verification materials.

## Optional earnings, DCF and peer research

The [native graph](../../skills/equity-investment-research/graph.toml) integrates three project-local skills without changing the nine-section core report or existing targets. Read [installation and activation guidance](../../skills/equity-investment-research/README.md#installed-optional-financial-skills).

```sh
uv sync --python 3.12 --locked --extra research
uv run --python 3.12 --extra research python skills/equity-investment-research/scripts/research.py plan --tickers INTC CRM --as-of 2026-10-11 --skills earnings-analysis dcf-model comps-analysis
```

Complete the graph prerequisites, then load only selected skill entrypoints. `plan` is not an automatic executor. Omp resolves them with `omp read skill://earnings-analysis`, `omp read skill://dcf-model` and `omp read skill://comps-analysis`. New earnings, DCF and peer narratives belong beside `report.md`; source inputs and live-formula workbooks belong in that same run's `data/` folder. Preserve core evidence/calculations/audits; use a new dated core run when evidence changes.

Keep cash-flow DCF, comparable-company multiples and EPS/exit-multiple targets separately labeled. Core audits and index targets do not validate extension arithmetic or workbook formulas. Excel/LibreOffice must actually recalculate before spreadsheet values are relied upon. Source/provider gaps and unavailable consensus remain explicit. [Installation verification](batches/2026-10-11/financial-skills-verification.json) concerns skill activation and integration, not completed extension analyses for the 50 tickers.

Canonical instructions and original source materials live under `skills/`; `.agents/skills/` is the common discovery directory and contains symlinks, not extra copies. The [current provenance manifest](../../skills/equity-investment-research/financial-skills-provenance.json) records current paths and adapter hashes. Earlier installation and workspace-review receipts describe the layout at their execution time, not the current layout. The [common discovery verification](batches/2026-10-12/common-agent-discovery-verification.json) records the cutover away from runtime-specific discovery directories.

The [workspace review verification](batches/2026-10-12/workspace-review-verification.json) records structure and validation corrections. Original NVDA/LLY/UNH artifacts are retained in their dated `archive/2026-10-12-review/` folders before correcting copied ticker-specific notes; numeric inputs and saved calculations are unchanged. BABA/JD/PDD initial calculation failures are retained once in `data/native-cli.json`, rather than duplicate failure files. Batch navigation discovers all retained top-level batch files; receipt-only dates do not require market-context files.


## Reading results responsibly

Keep units, currency, quote timestamps, source periods, split basis, accounting basis, consolidation scope and provenance explicit. Calculations retain full-precision Decimal strings; index displays may round. Reconcile reported facts and model inputs before arithmetic, and keep reported GAAP, adjusted results, forecasts and assumptions distinct.

The index's **present-value target (USD/share)** is `weighted_present_target`: a probability-weighted discounted earnings-multiple model, not a future trading price, cash-flow DCF, validated fair value or guaranteed outcome. Model horizons are explicit assumptions in years. The initial nine company models assume five years but leave EPS/exit alignment unresolved; their existing evidence is preserved. The expanded scan's modeled companies declare three-, four- or five-year calendar assumptions and explain their starting earning-capacity normalization and terminal multiple. The index shows each **model EPS anchor period and kind** (reported, estimate or assumption) and any declared **terminal date**. An assumed normalized anchor is not reported earnings; a forward EPS anchor is not automatically today's EPS run rate, and explicit timing is not proof of future earnings. Follow the [evidence contract](../../skills/equity-investment-research/references/evidence-contract.md); source gaps and economic limitations remain visible.

**Price CAGR ≠ EPS CAGR ≠ observed YoY return.** Price CAGR is `(terminal_price / reference_price) ** (1 / years) - 1`; EPS CAGR is the separate scenario growth input. Use future terminal price, not discounted present value. Probability-weighted present targets, CAGR of weighted terminal price and weighted mean scenario CAGR are different quantities. See the [independent nine-ticker return audit](batches/2026-10-11/return-audit.md) and its [full-precision arithmetic evidence](batches/2026-10-11/return-arithmetic-audit.json).

Saved audits are historical offline arithmetic/evidence-contract findings, not independent source truth or proof that files remain unchanged. Missing artifacts or graph sections remain INCOMPLETE even with a saved PASS; empty report sections make a fresh audit PROVISIONAL. Quoted headings inside fenced code are not graph sections. Index generation rejects saved calculations that differ from deterministic recomputation of the retained evidence. Reaudit final artifacts; PROVISIONAL evidence gaps and BLOCKED contradictions must remain visible. See [the dated index and evidence gaps](index.md#2026-10-11) for the retained ticker batch.

## Expanded universe

The [2026-10-11 expanded scan](batches/2026-10-11/expanded-scan.md) covers all 50 unique requested securities: 41 new packages and nine preserved existing packages. INTC and NFLX requests were deduplicated. [Methodology and full requested universe](batches/2026-10-11/expanded-scan-method.md) and [actual integration verification](batches/2026-10-11/expanded-scan-verification.json) are retained in the dated batch.

SPY, QQQ, SOXX, XBI and TLT have fund-specific mandate, NAV, holdings, fees and risk analysis; TLT also has duration/yield analysis. Corporate EPS/FCF facts that do not apply to funds are explicitly N/A. No fund EPS target is invented. Eleven companies also intentionally omit the EPS-growth target where earnings normalization, accounting, currency or market-data reconciliation makes the model unsuitable. Read their Valuation sections; an omitted target is not omitted research.
