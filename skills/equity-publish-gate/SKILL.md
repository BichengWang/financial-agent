---
name: equity-publish-gate
description: Checks a daily equity research package before it is published - required artifacts on disk, 15_predictions.json schema and units, formula conformance (70% CI, mu calibration band, Adj Score trace, VaR/CVaR), core ETF forecasts, and a replay of the run status from the ledger. Use before moving a daily investment run to PUBLISHED, when a manifest checklist is being written, or when auditing prediction ledgers for drift across runs and models.
compatibility: Requires Python 3.11+ (standard library only), run from the repository root. No network access.
metadata:
  fa-stages: "RISK_REVIEW PUBLISHED"
  fa-tools: "gate audit hash clones manifest"
  fa-writes: "none"
  fa-version: "1"
---

# Equity publish gate

The harness, not this skill, owns the rules: the checks live in
`src/financial_agent/harness/` and the numbers in its `equity_policy.toml`.
This skill tells you when to run them and how to act on the result.

## Before publishing a run

1. Write every artifact first. Never write the manifest's artifact checklist
   before the files exist; the gate reads the directory.
2. Run the gate on the package:

   ```bash
   PYTHONPATH=src python3 -m financial_agent.harness gate agents/equity/output/{model}-{YYYY-MM-DD}
   ```

3. Exit status 0 and `publish gate: PASS` means the package may move to
   `PUBLISHED`. Copy the `status replay` and `content hash` lines into
   `00_run_manifest.md` (the hash pins exactly what was published); if the replay
   disagrees with your status, explain why in `08_risk_review.md` (the replay
   assumes all Required inputs are grounded and knows nothing about market
   holidays or integrity halts).
4. On `GATE FAIL`, fix the cause and regenerate the artifact. Do not edit the
   policy file or loosen a check to get a pass. A failure you cannot fix makes
   the run `HALTED`, not published.

To generate the manifest's artifact checklist, gate result, status replay, and
content hash from the finished directory, run
`PYTHONPATH=src python3 -m financial_agent.harness manifest agents/equity/output/{model}-{YYYY-MM-DD}`
and paste its output into `00_run_manifest.md`. Never type the checklist by hand.

## Reading the output

- `error`: breaks an explicit rule (missing artifact, enum, CI or mu-band
  formula, Adj Score trace). Blocks publication.
- `drift`: a unit or meaning the rules leave implicit (VaR stored as percent,
  `kelly_025` capped in one run and uncapped in the next). Report it in
  `13_evolution_log.md` as a schema-clarity observation. Do not "fix" history.

## Auditing history

`python -m financial_agent.harness clones --since YYYY-MM-DD` lists artifacts
that are byte-identical in more than one package. A clone means an analysis
file was copied instead of produced; explain or regenerate it.

```bash
PYTHONPATH=src python3 -m financial_agent.harness audit --output-dir agents/equity/output
```

Historical packages are immutable: never rewrite a prior `15_predictions.json`.
Use the audit table as evidence for a Track B schema proposal instead.
