# 00 Run Manifest

- Date: 2026-05-12
- Timezone: America/New_York
- Run mode: SCHEDULED_DAILY
- Model: claude-opus-4-7
- Data mode: ILLUSTRATIVE
- Top-level status target: REVIEW_ONLY
- State trace: `PRECHECK -> DATA_OK(ILLUSTRATIVE) -> SCORED(ILLUSTRATIVE) -> PORTFOLIO_DRAFT(PAPER) -> RISK_REVIEW -> PUBLISHED(REVIEW_ONLY) -> CLOSE_LOGGED -> EVOLUTION_REVIEW`
- Agents executed:
  1. Orchestrator (00)
  2. Data and Regime Agent (01)
  3. Factor Scoring Agent (02)
  4. Portfolio Construction Agent (03)
  5. Risk Committee Agent (04)
  6. Evolution Agent (05)
- Outstanding blockers:
  - No live market data feed connected in this environment.
  - No verified real-time earnings calendar.
  - No options-positioning / borrow / 13F feed.
  - Macro signal inputs are simulated for process validation only.
- Revision budget used: 0 of 1 (portfolio↔risk), 0 of 1 (clarifications to factor scoring).
- Next scheduled checkpoint: 12:15 ET — `09_midday_monitor.md`.
