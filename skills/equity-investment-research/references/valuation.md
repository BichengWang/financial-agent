# Valuation

**Inputs:** Grounding evidence, Inversion risk register and Industry driver bounds; native calculation tool.

**Steps:**
1. Run `calculate` on saved evidence. Report computed market-cap reconciliation, historical FCF (operating cash flow minus positive capex), FCF yield and PE when positive EPS permits it. Explain that historical FCF is not owner earnings and a low multiple is not intrinsic value.
2. Choose a positive EPS basis with a source or explicit assumption. GAAP trailing earnings, adjusted earnings and analyst forecasts must not be blended; identify date, horizon and adjustments. Negative/absent earnings can make this EPS model unsuitable.
3. Source a contemporary USD risk-free rate with maturity and observation date; justify a separate required-return assumption above it. No default market yield. Exactly bear/base/bull scenarios use a common horizon, justified growth, exit multiples and probabilities totaling one. Ground growth and reinvestment limits in Industry and place modeled business risks from Inversion in scenarios, not covert rate penalties. Declare `valuation.timing` per the evidence contract: valuation and terminal dates, EPS basis and fiscal/run-rate/exit-multiple alignment. Do not infer dated returns solely from `years`; omitted timing remains PROVISIONAL.
4. Use CLI outputs for terminal price, price-only annualized return and present target discounted at required return. Price CAGR uses terminal price, not present target; it is not EPS growth or observed YoY performance. Multiplying a forward fiscal EPS anchor by five growth steps need not mean a five-year holding period unless the forward/trailing terminal multiple and timeline are aligned. Explicitly exclude dividends, interim cash flows and dilution unless the EPS assumptions already incorporate dilution. These are not full DCFs, total-return forecasts or guaranteed IRRs.
5. Explain terminal-multiple economics, maturity, capital intensity and competition; peer multiples are context, not proof. Discuss what current pricing would require qualitatively; the CLI does not solve reverse DCF or perpetuity ROIC models. Do not publish unsupported perpetual-value calculations as native tool results.
6. Assess sensitivity through separately retained evidence/calculation variants within the ticker directory when justified: explain assumptions and whether the conclusion reverses. Do not overwrite the canonical audit inputs with an optimistic variant.
7. When selected in the plan, load `skills/dcf-model/SKILL.md` and/or `skills/comps-analysis/SKILL.md` after these prerequisites. Preserve their separate narratives and live-formula workbooks. Explain differing methods and dates rather than averaging incomparable outputs or replacing the native EPS model. The core audit does not validate those workbooks; actual recalculation and method-specific checks are mandatory before relying on them.

**Output:** `## Valuation`, tool-derived metric/scenario table, model assumptions, conditional safety-margin assessment and unmodeled tails.

**Failure path:** absent current inputs/rate/positive supported EPS => omit valuation configuration and price target, preserve null metrics and mark provisional. Failed cap reconciliation must be investigated, never passed by dropping its inputs.

**Question:** Does a modest change in growth, exit economics or required return reverse the conclusion—and what business evidence justifies the price?
