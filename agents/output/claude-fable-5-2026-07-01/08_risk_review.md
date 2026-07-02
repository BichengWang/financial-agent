# 08 Risk Review — Committee Decision

Adversarial review of the 2026-07-01 package (24 monitoring forecasts + 3 core ETF forecasts, proposed status NO_TRADE).

## Checklist Findings

1. **Fabricated/weak inputs** — none found. Every price is tagged DELAYED with observation date 2026-07-01 and two-source verification (Yahoo + Nasdaq, max divergence 0.845%; IBKR MCP corroboration for 7 names). No bare numeric prices.
2. **Overfitting/unvalidated signals** — scores are momentum/risk-only (2 of 4 families); this is disclosed in every score trace rather than dressed up as full-factor conviction. Acceptable for a monitor-only publication.
3. **Event concentration** — only UNH inside the 14d earnings window among published names (penalized −0.10, LOW confidence, mu shaded −2pp). NO_TRADE trigger #4 not activated. FOMC lands on the 2026-07-29 target date — noted in 03; acceptable for forecasts, would be a sizing concern for a GO book.
4. **Correlation/sector crowding** — Health Care is 10/24 of the published names (INFERRED sectors). Flagged: any future GO portfolio from this leaderboard binds the 30% sector cap immediately (07). Pairwise correlations are low (avg 0.092; max 0.64).
5. **Beta drift** — no portfolio exists; the pre-check exhibit (max achievable NAV beta 0.60 at the 5% cap) is arithmetic from ledger-backed betas, correctly labeled diagnostic.
6. **Thesis quality vs confidence** — all equity confidence set to LOW, consistent with 2/4 family coverage; theses are labeled INFERRED reference-state color, excluded from scores. Consistent.
7. **Rules mismatches** — none found in cross-reading 03/04/05/06/07 against rules.md; percentiles carry INDEX_UNION_PCTL (n=513) labels throughout.
8. **Price/derived-field citations** — every entry_price has price_date + price_tag; no target/CI populated off an unverified price.
9. **Sigma** — every sigma states REALIZED_VOL_30D; no blanket UNAVAILABLE; every ranked name carries mu and sigma (settleable).
10. **Score attribution** — every ranked name shows the full trace `(0.30*Fund + 0.30*Tech + 0.25*Sent + 0.15*Macro)*DQ − Pen` with actual values, drivers, and ledger rows; UNAVAILABLE families shown as 0.00 (UNAVAILABLE), never as neutral support.
11. **Source Ledger** — 214 rows cover every price, vol, beta, dd, indicator state, earnings estimate, score, and forecast used downstream; derived rows cite formulas and input rows.
12. **Live-sounding claims** — none; DELAYED/HISTORICAL tags used consistently; "today's session" claims cite same-day close rows.
13. **GO-blocking discipline** — correct: manifest GO-Gate passes all 5 Required inputs; Enhancing gaps applied as DQ/confidence caps. The NO_TRADE stems from evidence-threshold arithmetic, explicitly not from Enhancing-input absence as a gate. (The committee notes this arithmetic makes GO unreachable while fund/sent feeds are absent — escalated to Evolution, see 13.)
14. **Prediction records** — all 24 ranked names + 3 core ETF MARKET_FORECAST records present in 15_predictions.json with score_explainability (fund_z/sent_z null with formula note — matches UNAVAILABLE family declaration); benchmark_price present on every EQUITY_ALPHA record. Complete.
15. **Technical indicator lineage** — all TD9/RSI/MACD/MA/momentum/RS/VR values cite technical_indicators.json (517/518 OK); TD9-9/RSI≥75 used only as penalty flags and mu shades, never standalone signals; script failures (FDXF) surfaced as exclusions, not hidden.

## Top Three Concerns (severity order)

1. **Two-family scoring.** The leaderboard is a momentum/low-vol screen, not a full multi-factor ranking. Mitigation in place (DQ 0.80, LOW confidence, NO_TRADE, monitor-only) is adequate; publishing settleable forecasts is the right way to accumulate calibration evidence. Watch for systematic momentum-chase bias when settlements arrive.
2. **Exhaustion cluster in a breaking tape.** 9 of 24 names carry RSI≥75/TD9-9 flags on the day the momentum complex cracked (SOXX −6.41%). A defensive-momentum book is exposed to a snap-back rotation; −1pp mu shades are applied but the vintage's CI calibration will be informative.
3. **Interim-alpha carry decisions.** CARRY/PROMOTE/DROP decisions rest on 21-day interim alpha (predictions settle 2026-07-08), documented as such. UNH carried with earnings inside 14d is properly penalized (LOW, −0.10, mu +1%).

## Decision

**APPROVE** publication as **NO_TRADE**. No revision required. Data integrity is clean; the no-trade outcome follows from disclosed evidence arithmetic, not from data failure (HALTED unwarranted). Publication recommendation: NO_TRADE.
