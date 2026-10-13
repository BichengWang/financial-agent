# Safety and live authorization

Version 1.0.0 is beta. Historical evidence and simulated fills do not establish
live performance. Risk checks bound proposed exposure at reference prices; they
cannot guarantee an execution price or prevent losses during gaps or outages.

## Statistical gate

The packaged [policy](../../src/financial_agent/quant/quant_policy.toml) requires
all eight checks below. Undefined values fail closed.

| Check | Required value |
|---|---:|
| Complete walk-forward OOS sessions | ≥ 2,520 |
| OOS net Sharpe, rf = 0 | ≥ 0.5 |
| Deflated Sharpe Ratio probability | ≥ 0.95 |
| CSCV probability of OOS loss | ≤ 0.10 |
| OOS maximum drawdown | ≤ 25% |
| Net Sharpe at twice modeled costs | ≥ 0.3 |
| Net Sharpe with one extra session of delay | ≥ 0.3 |
| Block-bootstrap Sharpe 5th percentile | > 0 |

PBO is a reported rank-reversal diagnostic, not a ninth gate. A high PBO says
in-sample parameter selection is unreliable even when absolute OOS returns are
positive. The [release evidence](../../reports/quant/2026-10-default-strategy-evidence.md)
shows the unchanged verdicts and grids. `certify` writes failed certificates too;
writing a file does not authorize capital.

## Live gate

The [authorization implementation](../../src/financial_agent/quant/runner/promotion.py)
requires a live Alpaca configuration, `FA_QUANT_ALLOW_LIVE=1`, and:

- A verified, passing certificate no older than 90 days with exactly the same
  normalized strategy name and parameters. Future timestamps fail verification.
- At least 20 distinct successful Alpaca-paper sessions for that identity.
  Local `PaperBroker`, previews and repeated same-day runs do not count.
- Zero halted sessions and zero reconciliation breaks in the most recent
  20-session evidence window; a successful retry cannot erase that day's halt.
- Observed Alpaca-paper fills in that window with valid positive prices and
  mean absolute slippage no greater than twice modeled spread plus slippage.
  References are the adjusted opening prices, not the prior close.

The grant expires after 15 minutes. Authorization runs before constructing the
live broker; its endpoint cannot be selected without a grant. Certificate hashes
include package version and policy/data identifiers for audit, but the verifier
does not independently demand equality to today's installed version, policy or
universe. Review those explicitly before promotion; recreate evidence after a
material change. The paper history is filtered by identity and date, but there
is no separate maximum paper-history age check.

## Runtime gates and limits

The default limits are for diversified ETF portfolios. SPY buy-and-hold and
60/40 exceed the per-name cap; default dual momentum can also exceed it (one
slot is 33.3%, or multiple slots may enter IEF). These are backtest comparisons,
not ready-to-run live configurations. Passing statistics does not override risk.
The trend grid includes a 35% cap variant; any selected identity must still obey
the 30% execution cap. Configuration overrides can tighten limits, never loosen.

| Limit | Default | Meaning |
|---|---:|---|
| Per-symbol absolute weight | 30% | Projected holdings / equity |
| Gross exposure | 100% | Sum of absolute projected weights |
| Shorting | Disabled | No selling more than held or negative projected weights |
| Each order notional | 35% | Quantity × reference price / equity |
| Total turnover per plan | 100% | Sum of absolute order notionals / equity |
| Daily loss | 3% | Loss from recorded day-start equity; breach persists stop |
| Drawdown | 20% | Loss from persisted high-water NAV; breach persists stop |
| Minimum projected cash | 1% | Reference-price cash / equity |
| Price band | 5% | Reference vs broker-mark price for held positions |
| Orders per plan | 50 | Whole-plan count |
| Symbols | Configured universe | Policy/run allowlist may only narrow it |

The runner requires `cash_buffer > min_cash_pct` (examples use 2%), next-open
execution, no extra delay, and whole shares. Cash reserve is calculated at
reference prices; transaction costs and gaps can consume it. Price-band checks
are not broker-enforced protective limit prices, and pending orders/fills can
create exposure before the next observation.

State locking prevents concurrent sessions. Bad/stale data, corrupt journal,
invalid live evidence, broker-mode mismatch, reconciliation breaks, risk-state
mismatch, warmup failure, unresolved open orders on a planning day, rejected
plans and broker errors halt further submission. Exchange non-sessions return
`NO_SESSION`. Hard pre-trade rejection approves no part of a plan; a transport
failure during a submission loop can still leave earlier orders at the broker.
Recover using durable intents and client IDs, then reconcile.

The kill switch is a `KILL` file or persisted breach. Loss/drawdown breaches
engage it automatically; other halts need investigation before a retry. Clearing
it requires an explicit journaled operator identity and reason. **Kill stops new
submissions; it does not cancel open broker orders or liquidate positions.**
Perform those actions directly at the broker when the incident requires them.
The system is a scheduled observer, not an intraday monitor or stop-loss order.

## Secrets and tool boundary

Only process environment supplies `APCA_API_KEY_ID` and `APCA_API_SECRET_KEY`.
Use paper keys in paper mode and separate live credentials after approval.
Never put secrets in TOML, source control, report attachments or shell history.
Provider/transport exceptions are sanitized; protect state and logs nonetheless.

MCP exposes `quant_backtest`, `quant_validate`, `quant_data_check`, `quant_status`
and `quant_preview_orders`. It rejects live configurations and extra input keys.
There is no MCP order-submission, cancellation or stop-mutation tool. Research
agents and the equity harness produce evidence; the operator CLI owns execution.

## Go live step by step

1. Freeze the universe, costs, strategy and grid. Run `validate` and `certify`
   using the [research instructions](strategy-research.md). Inspect every check,
   data provenance and parameter-selection diagnostic.
2. Copy the normalized `[strategy]` and `[strategy.params]` printed by `certify`
   into your paper TOML. Review the selected allocation against runtime caps.
   Revalidate if you change the strategy; do not edit policy to make it pass.
3. Use Alpaca paper keys and collect at least 20 distinct clean sessions with
   fills. Read the journal and broker account daily. Local demo sessions are
   useful for learning but do not establish broker execution quality.
4. Preserve the paper journal and certificate. Create a separate live TOML and
   state directory; set `mode = "live"`, `broker.kind = "alpaca"`, and point
   `[promotion]` at that evidence. Use a clean/dedicated broker account: unexplained
   existing holdings cause reconciliation breaks.
5. Review certificate age, params, universe, policy/version, paper slippage,
   account funding, position caps, cash reserve and the opening-auction schedule.
   Load live keys and explicitly set `FA_QUANT_ALLOW_LIVE=1` in the protected
   operator environment. A dry run still needs authorization and can observe
   existing fills; it suppresses new submissions only.
6. Run the same `fa-quant run --config` command with your live config before the
   OPG cutoff. Monitor acknowledgements, fills and reconciliation directly.
   Follow the [incident runbook](operations.md) if any condition is uncertain.

This release verifies the live path with deterministic fake transports. It does
not include a real Alpaca-paper or live account run; those need owner credentials.
