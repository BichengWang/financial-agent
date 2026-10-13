# Limitations and audit

**Inputs:** final evidence, calculations and complete saved report; graph section requirements.

**Steps:**
1. Write `## Limitations and audit` before invoking audit. List missing facts, nonindependent sources, dated statements/quotes, assumptions, accounting/model exclusions, unmodeled discrete risks and unresolved primary-research questions.
2. Check report citations against retained source excerpts and financial definitions manually. Programmatic source-count checks cannot prove publisher independence, observed truth, quote accuracy or analytical soundness.
3. Run `audit` on the exact ticker/date run directory, saving `data/audit.json`. The engine recomputes arithmetic, compares calculations and checks evidence schema, dates, provenance and required headings. Missing valuation/terminal dates and EPS alignment in `valuation.timing` warn that price CAGR is conditional, not a verified dated or YoY return. Declared timing must match the configured calendar-year horizon; its economic assumptions remain subject to human review. The engine does not fetch independent market evidence or certify investment truth.
4. Record the actual status and findings. PASS means no implemented structural/arithmetic/evidence findings, not a recommendation. PROVISIONAL (nonzero) means missing evidence, required fundamentals labeled estimate/assumption, omitted valuation or unverified valuation timing; BLOCKED (nonzero) means malformed/invalid inputs or contradictions/calculation mismatch. Legitimate sourced forecast EPS and explicitly justified model assumptions remain disclosed and do not alone invalidate a grounded audit. Do not describe an unrun audit as passed.
5. Correct actual errors at their source, regenerate calculations and rerun audit after any changed inputs or report. Preserve explicit gaps; never remove failed inputs to obtain a pass.

**Output:** final limitations section and retained `data/audit.json`, with machine result distinguished from human analytical judgment.

**Failure path:** tool error => retain error and mark unaudited/blocked; unresolved source gaps => provisional. No publication claim of verification beyond performed checks.

**Question:** Can another researcher reconstruct every material claim and every computed result from the retained artifacts?
