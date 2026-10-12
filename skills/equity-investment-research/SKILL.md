---
name: equity-investment-research
description: Evidence-first, Berkshire-inspired equity research using Buffett, Munger, Duan Yongping, and Li Lu analytical lenses. Use for company deep dives, comparable stock research, valuation scenarios, or auditing an investment thesis with current sourced financial facts. Produces checkout-local research artifacts and explicit provisional or blocked findings; never submits orders.
license: MIT
compatibility: Python 3.12+ standard library for numeric tools; network access for source collection. Run commands from the repository root.
---

# Equity investment research

This is a repository-native research skill, not a daily-run stage or execution system.
Use the four investors as analytical lenses, not simulated quotations or endorsements.
All materials and outputs stay in this checkout. No global skill installation or external checkout is required.

## Activate progressively

1. Read [graph.toml](graph.toml) and [the evidence contract](references/evidence-contract.md).
2. Run `uv run --python 3.12 python skills/equity-investment-research/scripts/research.py graph` to validate references and get dependency order. Plan the requested names with `plan --tickers CRM MSFT --as-of YYYY-MM-DD`.
3. Load only the instruction file of a ready node, after completing its prerequisites. The graph names the exact report section for each node. Missing evidence is an output, not permission to invent facts.
4. Keep each company's direct-entry `report.md` in `docs/research/tickers/TICKER/YYYY-MM-DD/`, with `data/evidence.json`, `data/calculations.json`, and `data/audit.json`. Preserve imported baselines separately in `archive/`. Keep companies separate; shared market inputs and batch verification belong in `docs/research/batches/YYYY-MM-DD/`.
5. Use the native numeric CLI, not mental arithmetic, for supported calculations. Finalize the report, then audit the exact saved artifacts. A nonzero audit remains provisional or blocked; never weaken policy, delete inconvenient facts, or relabel assumptions to make it pass.
6. Run `uv run --python 3.12 python skills/equity-investment-research/scripts/research.py index` after saving audited artifacts. It refreshes only `docs/research/index.md`, with dated ticker navigation, conditional model target tables, coverage and evidence gaps. `docs/research/README.md` is authored run guidance and is never generated. Dated reports are direct entries, without ticker/batch README wrappers. New research dates get new directories; prior history stays intact. Generated navigation is not independent source verification.

## Optional financial-analysis extensions

The graph also declares project-local `earnings-analysis`, `dcf-model` and `comps-analysis` skills. Select only requested methods with `plan --tickers INTC --as-of YYYY-MM-DD --skills earnings-analysis dcf-model comps-analysis`. The plan names each skill's entrypoint, existing graph prerequisites and ticker/date output paths; it does not execute research.

Load earnings analysis with the Business node after Grounding. Load DCF and comps with Valuation after Grounding, Inversion and Industry. Read each selected skill's native `SKILL.md` under `skills/`; retained upstream material is progressively loaded from that skill's references. Omp, Claude Code and Codex discovery links resolve to the same tracked canonical files.

Extension outputs are separate `earnings.md`, `dcf.md` and `comps.md` files beside the main report, with inputs/workbooks in `data/`. Never replace core evidence, calculations or audits with extension results. The core audit does not verify extension calculations or workbook formulas. Full cash-flow DCF and peer valuation stay separate from the index's discounted EPS/exit-multiple targets.

Use `uv sync --python 3.12 --locked --extra research` for the locked openpyxl workbook dependency. Excel or LibreOffice must actually recalculate a workbook before its cached values are quoted. Installation and instruction activation are not proof of executed financial analysis; missing inputs, consensus access or recalculation must remain explicit.

## Nonnegotiable boundaries

- Every numerical claim has a period, unit, kind, and source trail. Retain observed source excerpts; a URL alone is not evidence.
- Required reported facts need observations from two distinct publishers. Reprints, issuer mirrors, and two pages from one publisher are not independent corroboration.
- Distinguish reported GAAP, adjusted non-GAAP, forecasts, and assumptions. Null is honest when current facts cannot be sourced.
- Do not use a stale quote as current, mix split bases, or mix consolidated and parent-only liquidity. Do not hardcode a market yield.
- Separate research confidence from business certainty. Rich public coverage can amplify consensus and anchoring; sparse coverage does not establish a bad business.
- Valuation scenarios are conditional models, not guaranteed outcomes. No orders, brokerage actions, or portfolio execution.

## Resources

[Grounding](references/grounding.md) · [Business](references/business.md) · [Moat](references/moat.md) · [Management](references/management.md) · [Inversion](references/inversion.md) · [Industry](references/industry.md) · [Valuation](references/valuation.md) · [Decision](references/synthesis.md) · [Audit](references/audit.md).

See [README](README.md) for the graph and CLI, and [upstream MIT license](LICENSE.upstream) for attribution. Adapted from https://github.com/xbtlin/ai-berkshire.
