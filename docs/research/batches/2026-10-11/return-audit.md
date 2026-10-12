# Independent return and calendar-assumption audit — 2026-10-11

## Bottom line

**Saved financial arithmetic: PASS for all nine tickers. Dated five-year price forecasts: UNVERIFIED. Model economics and EPS/run-rate alignment: conditional ASSUMPTIONS.** These are separate findings, not interchangeable audit grades.

The independent calculation used the retained source-evidence values and Python standard-library `Decimal` at **80-digit precision**, without importing or calling production `calculate()` or `audit()`. It compared **162 saved numeric/null fields**: five historical metrics, four derived outputs in each of 27 scenarios, and nine weighted present targets. It also checked every saved scenario input/reference against retained evidence, rate/probability/growth constraints, units and cash-flow periods. **No saved calculation field failed.** This is not a repeat of the production audit, nor certification of issuer/source truth.

The original reports did contain concrete reporting errors: **AMZN implied capitalization was 1,000× too small in two locations; META implied capitalization was 1,000× too small in one.** Original AAPL/NFLX annualized-return cells were correct decimal fractions but had no explicit decimal unit, making them easy to misread as percentages. The report-owner corrections now restore the capitalization dollars and display CAGR percentages. Current scenario/metric/weighted-PV displays pass independently computed rounding checks. Original tokens, line locations, deltas and before/after report hashes are preserved in the [machine audit](return-arithmetic-audit.json); these were report defects, not evidence/calculations changes.

All nine input packages configure **five EPS growth steps** and use **five price holding/discount years** arithmetically. That does **not** independently establish a five-year calendar forecast: none of their retained `valuation` inputs declares `valuation.timing`, exact exit dates or a complete EPS-to-exit alignment. No EPS rebasing, probabilities, growth rates, hurdles, quotes or scenario horizons were changed for this audit.

## Nine-ticker return summary

USD/share prices are rounded to cents here; return diagnostics are percentages rounded to six decimals. “5 / 5” means **configured growth steps / assumed price holding years**, not a verified calendar. The two weighted CAGR columns are intentionally different metrics; neither is obtained by annualizing weighted-PV upside.

| Ticker | Base EPS period/basis | Growth / holding | Base future terminal price | Base price CAGR | Weighted present-value target | Weighted future terminal price | CAGR of weighted future value | Weighted mean scenario CAGR | Finding |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| [AAPL](../../tickers/AAPL/2026-10-11/report.md#valuation) | FY2027 adjusted, $9.59 | 5 / 5 | $385.50 | 2.747354% | $232.35 | $374.20 | 2.137846% | 1.227812% | Original decimal units clarified; FY2032/run-rate alignment unverified |
| [AMZN](../../tickers/AMZN/2026-10-11/report.md#valuation) | FY2026 adjusted, $8.31 | 5 / 5 | $428.70 | 10.313219% | $271.67 | $457.77 | 11.770467% | 9.254547% | Original cap ×1,000 correction; FY2031/exit convention unverified |
| [CRM](../../tickers/CRM/2026-10-11/report.md#valuation) | FY2028 adjusted, $16.02 | 5 / 5 | $400.16 | 11.796872% | $226.16 | $389.75 | 11.209386% | 8.866874% | FY2033 fiscal-step proxy versus five holding years unresolved |
| [GOOGL](../../tickers/GOOGL/2026-10-11/report.md#valuation) | FY2026 adjusted, $12.11 | 5 / 5 | $489.75 | 6.848754% | $289.29 | $476.59 | 6.268370% | 3.633601% | FY2031 earnings/exit convention unverified |
| [INTC](../../tickers/INTC/2026-10-11/report.md#valuation) | FY2026 adjusted, $1.52 | 5 / 5 | $83.21 | -4.490810% | $47.96 | $84.51 | -4.193324% | -9.643470% | Historical PE correctly null; adjusted FY2031 convention unverified |
| [META](../../tickers/META/2026-10-11/report.md#valuation) | FY2026 adjusted, $30.40 | 5 / 5 | $1,029.03 | 7.443426% | $578.26 | $974.40 | 6.277644% | 4.082862% | Original cap ×1,000 correction; FY2031 alignment unverified |
| [MSFT](../../tickers/MSFT/2026-10-11/report.md#valuation) | FY2027 adjusted, $19.77 | 5 / 5 | $932.78 | 11.756759% | $545.48 | $898.65 | 10.926612% | 9.456731% | FY2032 proxy versus five holding years unresolved |
| [NFLX](../../tickers/NFLX/2026-10-11/report.md#valuation) | FY2027 adjusted, $3.81 | 5 / 5 | $166.92 | 18.880762% | $96.72 | $162.98 | 18.313651% | 16.331844% | Forward FY2032/illustrative Oct2031 potentially coherent; undated |
| [TSLA](../../tickers/TSLA/2026-10-11/report.md#valuation) | FY2025 GAAP, $1.08 | 5 / 5 | $80.62 | -26.765022% | $48.04 | $92.50 | -24.724155% | -29.990423% | FY2030 fiscal-step proxy versus five holding years unresolved |

**Reported metric scope:** the corrected reports show the three **scenario** price CAGRs, scenario terminal prices, discounted scenario present values and weighted present target. The [research index](../../index.md#2026-10-11) lists **weighted present values**, not future exit prices, and no CAGR. The retained `calculations.json` files contain scenario `annualized_return` and `weighted_present_target`, but **no weighted terminal price, CAGR of weighted terminal price or probability-weighted mean scenario CAGR**. The latter two are separately labeled audit diagnostics above and in the JSON; absence is not treated as a fabricated pre-existing report value.

## CAGR is not YoY, EPS growth or present-value upside

For an assumed holding interval of \(h\) years, the numerical price-only annualization is:

\[
\operatorname{CAGR}_{price}=\left(\frac{P_{exit}}{P_{current}}\right)^{1/h}-1,
\qquad P_{exit}=EPS_{base}(1+g_{EPS})^{n_{growth}}M_{exit}.
\]

The present packages set both exponents to five; their equality is a **configuration**, not proof that the EPS period and price interval align on calendar dates. A **YoY** return requires prices one year apart. A five-year endpoint CAGR does not establish any particular intervening one-year result or actual yearly path. Total terminal upside divided by five is not compound annualization. A decimal `0.02747354…` means approximately **2.747354%**, not 0.02747354%.

Concrete example: AAPL assumes **7.5% annual EPS growth**, yet its base-case price-only CAGR is **2.747354%** from $336.64 to $385.495186663671875 over the assumed five holding years. The EPS anchor and exit PE are separate assumptions; EPS growth is not price return. NFLX’s base-case price CAGR is **18.880762%**, while its **CAGR of probability-weighted future price is 18.313651%** and its **probability-weighted mean scenario CAGR is 16.331844%**. Averaging future prices before taking a root is not averaging the scenario roots.

Weighted PV is a present-date hurdle-discounted comparison, not a future sale price. For NFLX, the independent weighted future price is **$162.97823257605540**, discounted at 11% for the assumed five periods to weighted PV **$96.719648566896752…**. Its weighted-PV premium versus $70.30 is not an exit-value CAGR. At a common horizon the audit also checked the financial identity that **weighted future price/current price equals (1 + hurdle)^years × weighted PV/current price**. It passes to audit precision; it does not validate dates, earnings or probabilities.

All modeled returns exclude dividends, interim distributions, taxes and fees. They are **price-only conditional returns**, not total-return IRRs or investment guarantees.

## Confirmed original report errors and their resolution

| Original artifact/field | Observed original display | Independent/saved correct value | Original delta | Current resolution |
|---|---:|---:|---:|---|
| [AMZN Grounding](../../tickers/AMZN/2026-10-11/report.md#grounding), original line 40, implied cap | $2,829,782,690.00 | $2,829,782,690,000.00 | −$2,826,952,907,310.00 | Corrected USD display |
| [AMZN Valuation](../../tickers/AMZN/2026-10-11/report.md#valuation), original line 174, implied cap | $2,829,782,690.00 | $2,829,782,690,000.00 | −$2,826,952,907,310.00 | Corrected USD display |
| [META Valuation](../../tickers/META/2026-10-11/report.md#valuation), original line 183, implied cap | $1,831,171,160.00 | $1,831,171,160,000.00 | −$1,829,339,988,840.00 | Corrected USD display |
| [AAPL Valuation](../../tickers/AAPL/2026-10-11/report.md#valuation), original annualized-return cells | −0.080108750… / 0.027473544… / 0.112869868… | −8.010875…% / 2.747354…% / 11.286987…% | No numerical error when read as decimals | Explicit percentages; original unit ambiguity retained |
| [NFLX Valuation](../../tickers/NFLX/2026-10-11/report.md#valuation), original annualized-return cells | 0.014959242… / 0.188807615… / 0.322134309… | 1.495924…% / 18.880762…% / 32.213431…% | No numerical error when read as decimals | Explicit percentages; original unit ambiguity retained |

Corrected report links above show the current state, not the historical bad text. The machine file preserves captured original displays/hash provenance and separate current checks. No original financial calculation was rewritten to conceal these reporting defects.

## Historical metric arithmetic, units and periods

The independently recomputed price-times-shares market caps below use the retained **dated actual/estimated common-share input**, not diluted weighted-average EPS shares. All absolute relative deviations from retained reported cap are below the existing 1% reconciliation policy; that is not proof of an exact current share register. GOOGL applies the retained Class-A-price × total-common-share convention, not a separately priced A/B/C equity-cap sum.

| Ticker/source facts | Implied market cap, USD | Absolute cap deviation | OCF/capex common period | Recomputed FCF | Historical FCF/current-cap yield | Historical price/EPS |
|---|---:|---:|---|---:|---:|---:|
| [AAPL evidence](../../tickers/AAPL/2026-10-11/data/evidence.json) | $4,912,924,160,000.00 | 0.059555% | FY2025 ended 2025-09-27 | $98.767000B | 2.011548% | 45.13× |
| [AMZN evidence](../../tickers/AMZN/2026-10-11/data/evidence.json) | $2,829,782,690,000.00 | 0.007679% | TTM ended 2026-06-30 | $-11.625000B | -0.410777% | 21.10× |
| [CRM evidence](../../tickers/CRM/2026-10-11/data/evidence.json) | $188,573,990,000.00 | 0.002116% | FY2026 ended 2026-01-31 | $14.402000B | 7.637482% | 29.38× |
| [GOOGL evidence](../../tickers/GOOGL/2026-10-11/data/evidence.json) | $4,300,801,800,000.00 | 0.018647% | FY ended 2025-12-31 | $73.266000B | 1.703860% | 32.53× |
| [INTC evidence](../../tickers/INTC/2026-10-11/data/evidence.json) | $553,455,220,931.40 | 0.000040% | FY2025 ended 2025-12-27 | $-4.949000B | -0.894201% | null (GAAP EPS −$0.06) |
| [META evidence](../../tickers/META/2026-10-11/data/evidence.json) | $1,831,171,160,000.00 | 0.063998% | FY2025 ended 2025-12-31 | $46.109000B | 2.519617% | 30.59× |
| [MSFT evidence](../../tickers/MSFT/2026-10-11/data/evidence.json) | $3,973,964,890,000.00 | 0.099871% | FY2026 ended 2026-06-30 | $66.987000B | 1.687330% | 29.81× |
| [NFLX evidence](../../tickers/NFLX/2026-10-11/data/evidence.json) | $292,729,200,000.00 | 0.003143% | FY2025 ended 2025-12-31 | $9.461053B | 3.232117% | 27.79× |
| [TSLA evidence](../../tickers/TSLA/2026-10-11/data/evidence.json) | $1,511,491,787,683.80 | 0.098794% | FY2025 ended 2025-12-31 | $6.220000B | 0.411921% | 354.35× |

**All cash-flow pairs use matching retained annual/TTM periods and positive cash-capex units**, so FCF is OCF less capex, not OCF plus a normalized positive expense. Dollars/shares and per-share EPS are not confused with millions. Negative AMZN/INTC FCF and yields are retained, not forced positive. **INTC historical GAAP EPS is −$0.06, so historical PE is correctly null**; its $1.52 adjusted FY2026 EPS is a different positive valuation anchor. Every other historical PE uses the retained positive historical EPS, not a silently substituted TTM/adjusted PE.

Historical FCF/current capitalization and historical EPS/current-price ratios deliberately combine labeled periods; they are not forward cash yields or full owner earnings. Cash capex does not settle maintenance-versus-growth reinvestment, noncash leases, SBC, working-capital or acquisition economics. Share dates and these period/scope limits are retained per ticker in the machine audit.

All three scenario probabilities for every ticker lie in [0, 1] and sum exactly to one; all growth inputs exceed −100%, all EPS valuation anchors/exit PEs are positive, all configured periods are positive integers, and all numeric inputs are finite. The annual hurdle and risk-free inputs are **decimal rates**, not percent integers. The retained hurdles exceed the common 0.0524 Treasury reference. These constraint passes do not establish calibrated probabilities, appropriate growth, valid adjusted earnings or a market-determined equity hurdle.

## Fiscal anchors versus price holding periods

The “fiscal-step proxy” below is explicitly an **[INFERENCE]** from the retained fiscal-year label plus five annual EPS increments. It is not an invented terminal fiscal-end date, a rebased EPS estimate or proof that this is the proper earnings window at exit.

| Ticker | Sourced EPS anchor period | Five-step earnings label diagnostic | Exit earnings-multiple convention in retained report |
|---|---|---|---|
| [AAPL](../../tickers/AAPL/2026-10-11/report.md#valuation) | FY2027 adjusted forecast; vendor Sep30 label is not exact Apple fiscal year-end | FY2032 [INFERENCE] | UNKNOWN: report says Exit PE, not forward versus trailing |
| [AMZN](../../tickers/AMZN/2026-10-11/report.md#valuation) | FY2026 adjusted forecast ending 2026-12-31 | FY2031 [INFERENCE] | UNKNOWN: report says Exit PE |
| [CRM](../../tickers/CRM/2026-10-11/report.md#valuation) | FY2028 adjusted forecast ending 2028-01-31 | FY2033 [INFERENCE] | UNKNOWN: adjusted exit PE identifies accounting basis, not earnings timing |
| [GOOGL](../../tickers/GOOGL/2026-10-11/report.md#valuation) | FY2026 adjusted forecast ending 2026-12-31 | FY2031 [INFERENCE] | UNKNOWN: report says Exit PE |
| [INTC](../../tickers/INTC/2026-10-11/report.md#valuation) | FY2026 adjusted forecast; exact forecast fiscal-end day not retained as canonical period | FY2031 [INFERENCE] | UNKNOWN: report says exit multiple |
| [META](../../tickers/META/2026-10-11/report.md#valuation) | FY2026 adjusted forecast ending 2026-12-31 | FY2031 [INFERENCE] | UNKNOWN: report says exit PE |
| [MSFT](../../tickers/MSFT/2026-10-11/report.md#valuation) | FY2027 adjusted forecast ending 2027-06-30 | FY2032 [INFERENCE] | UNKNOWN: FY2032 earnings proxy stated, forward-versus-trailing exit PE not stated |
| [NFLX](../../tickers/NFLX/2026-10-11/report.md#valuation) | FY2027 adjusted forecast ending 2027-12-31 | FY2032 [INFERENCE] | EXPLICIT_FORWARD: report capitalizes FY2032 forward EPS at illustrative October2031 exit |
| [TSLA](../../tickers/TSLA/2026-10-11/report.md#valuation) | FY2025 reported GAAP EPS ended 2025-12-31 | FY2030 [INFERENCE] | UNKNOWN: report says assumed exit PE |

- **AAPL:** the FY2027 source’s September 30 label is a vendor fiscal-month convention, not Apple’s exact last-Saturday fiscal year end. Five growth steps suggest FY2032 only as a label diagnostic. Treating that forward EPS as initial capacity remains a run-rate assumption.
- **AMZN, GOOGL, META, INTC:** the FY2026 anchors suggest FY2031 earnings labels after five fiscal steps. This does not identify whether the price is at an earnings-period end, before it using forward PE, or after it using trailing PE. INTC’s exact forecast fiscal-end day is not supplied by the canonical period; none is invented.
- **CRM:** FY2028 ends January 31, 2028 and is intentionally used as a starting run-rate. Five literal fiscal-year increments suggest FY2033, while five holding years from the 2026 snapshot is a different clock. The original claim that the horizon “runs from the research date in the engine” was not established by saved calendar fields; the corrected report states the unresolved run-rate alignment. This is not automatically a numerical EPS-growth error.
- **MSFT:** FY2027 ends June 30, 2027, and five steps suggest FY2032 EPS. The report previously disclosed five-year decision-date discounting as an approximation and now explicitly marks the alignment unverified. FY2032 EPS might support an earlier price under an explicit forward-PE convention, but that convention is not established for MSFT.
- **NFLX:** the retained report explicitly pairs an **illustrative October 2031 price exit with forward FY2032 EPS**. A forward PE can legitimately capitalize following-year earnings at exit, so “future EPS base is always wrong” would be an invalid universal rule. No exact start/exit day or complete forward earnings window is documented; the dated CAGR remains unverified.
- **TSLA:** historical FY2025 GAAP EPS plus five literal fiscal steps suggests FY2030, not a sourced FY2031 earnings forecast. Using historical $1.08 as current initial earning capacity is a conditional run-rate normalization. No intervening earnings bridge or new EPS is fabricated to make the clocks agree.

Thus, **five configured periods are confirmed; five calendar holding years are not independently validated**. The corrected reports disclose assumptions rather than converting these diagnostics into false certainty.

## What prevents dated CAGR verification

The quote prices are dated October 9, 2026, while the research snapshot is October 11. The retained numeric models do not resolve even that start-date convention into a dated holding schedule. A dated audit needs:

1. **Declared price holding/valuation start**: quote timestamp versus research/decision date, or an explicit undated run-rate-only model classification.
2. **Declared exact exit/settlement date and year-count convention**: annual periods versus elapsed fractional years; no guessed fiscal-end day.
3. **Terminal earnings period and PE timing convention**: trailing fiscal EPS, next fiscal year, rolling next-twelve-month EPS, or a clearly classified run-rate proxy; “adjusted PE” alone identifies accounting basis, not calendar alignment.
4. **Earnings-clock alignment**: the retained historical/forecast EPS period, any justified normalization to starting earning capacity, configured EPS growth intervals and any forecast lead/stub treatment must be distinguished from the price holding clock.

Missing `valuation.timing` is therefore a **native calendar-alignment coverage gap for all nine input packages**, even where old saved audit receipts passed arithmetic/schema checks. Neither this independent arithmetic PASS nor a native audit PASS should certify a dated return forecast or promote a package to investment approval. Adding dates cannot be replaced by retuning the scenario horizon until the output looks plausible.

## Reproducibility and evidence scope

The [machine audit](return-arithmetic-audit.json) retains per-ticker concrete facts/units/periods/source references, all 27 scenario inputs, independently recomputed terminal EPS/prices/upside/CAGR/PV, each saved field/delta/tolerance, weighted diagnostics, constraints, captured original/current report checks, and SHA-256 bindings for the current numeric dataset. The source EPS excerpts are linked back to their retained local evidence; no new quote or web truth certification was used.

- **Saved calculation tolerance:** absolute **1e−28** plus relative **1e−35 × |independent result|**. This accommodates approximately 40-significant-digit stored Decimal roundoff while excluding financial-scale errors.
- **Report/index rounding:** half the last displayed decimal unit after USD/billion/percent conversion, plus the numerical tolerance. Original unlabeled decimal returns pass numerical comparison only, not unambiguous reporting.
- **Hash scope:** `evidence.json` and `calculations.json` bind numeric inputs/saved comparisons. Corrected report hashes bind current displays; original report hashes/tokens retain observed defects. Native `audit.json` and regenerated index audit-status receipts are downstream outputs, not numeric inputs. Captured index checks describe its observed weighted-PV reporting scope, not a promise that receipt bytes will remain unchanged.
- **Independent worker execution scope:** research recomputation and display/period review only. No tests, builds, linters, formatters, production calculate/audit calls, quote fetches, orders or trade execution were run by that worker. The archived INTC trial was not edited or used as independent evidence.

## Final native integration verification

The updated native CLI audited all nine final ticker packages and regenerated the central index. Every saved `data/audit.json` is now **PROVISIONAL**, with the missing-timing warning retained; no package is BLOCKED and no arithmetic error was introduced. GOOGL's earlier PASS is historical, not evidence that its holding dates were verified. The index now shows **five years assumed; EPS/exit alignment unresolved** alongside the sourced **EPS anchor period**, separates research and quote dates, and links this audit instead of asserting a dated five-year forecast.

Final regression run: **31 passed**. Mypy checked both engine/test files with no issues; flake8 and black checks passed. The 18 evidence/calculation files, shared market context and historical INTC trial were preserved byte-for-byte during native integration. Source truth was not re-fetched. Actual commands, findings, input/display hash bindings and local-link checks are recorded in [verification.json](verification.json); the prior receipt is retained in [archive/verification-before-return-audit.json](archive/verification-before-return-audit.json).
