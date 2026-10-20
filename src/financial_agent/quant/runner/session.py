"""Exclusive, fail-closed sessions; durable intents precede all submissions."""

from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager
from dataclasses import replace
from datetime import date, datetime, time, timedelta, timezone
import fcntl
from functools import cache
import json
import os
from pathlib import Path
import tomllib
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd  # type: ignore[import-untyped]

from financial_agent.harness.market_calendar import session as calendar_session
from ..data import BarProvider, MarketData, check_quality
from ..execution import (
    AlpacaBroker,
    Broker,
    BrokerError,
    Fill,
    IBKRBroker,
    Journal,
    PaperBroker,
)
from ..execution.alpaca import LIVE_URL
from ..risk import (
    AccountSnapshot,
    KillSwitch,
    Order,
    RiskState,
    check_orders,
    plan_orders,
    update_risk_state,
)
from ..strategies import build_strategy
from .config import TradingConfig
from .promotion import authorize_live
from .report import SessionReport, Status, json_value, write_report

EXCHANGE_TZ = ZoneInfo("America/New_York")


class SessionLocked(RuntimeError):
    """Another process holds the state-directory lock."""


@contextmanager
def session_lock(state_dir: Path) -> Iterator[bool]:
    """Kernel lock is authoritative; stale PID metadata is detected and replaced.

    Never unlink the inode: concurrent processes must lock the same file.
    """
    state_dir.mkdir(parents=True, exist_ok=True)
    with (state_dir / "session.lock").open("a+") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SessionLocked("state_dir: another session is running") from None
        handle.seek(0)
        previous = handle.read().strip()
        stale = bool(previous)
        handle.seek(0)
        handle.truncate()
        handle.write(str(os.getpid()))
        handle.flush()
        os.fsync(handle.fileno())
        try:
            yield stale
        finally:
            handle.seek(0)
            handle.truncate()
            handle.flush()
            fcntl.flock(handle, fcntl.LOCK_UN)


def configured_broker(
    config: TradingConfig, environ: Mapping[str, str], *, authorization: Any = None
) -> Broker:
    """Credentials are read only from the caller's environment."""
    if config.broker_kind == "paper":
        return PaperBroker(
            config.state_dir / "paper.json",
            costs=config.backtest.costs,
            initial_cash=config.initial_cash,
        )
    if config.broker_kind == "ibkr":
        assert config.account_id is not None
        return IBKRBroker(
            config.account_id,
            base_url=config.base_url,
            verify=config.verify,
            conids=config.conids,
            confirm_message_ids=config.confirm_message_ids,
            live_authorization=authorization,
        )
    return AlpacaBroker(
        environ.get("APCA_API_KEY_ID", ""),
        environ.get("APCA_API_SECRET_KEY", ""),
        base_url=LIVE_URL if config.mode == "live" else None,
        live_authorization=authorization,
    )


@cache
def _opening_auction_cutoff() -> time:
    """Packaged policy only: a run configuration cannot move the cutoff."""
    path = Path(__file__).parents[1] / "quant_policy.toml"
    policy = tomllib.loads(path.read_text())["execution"]
    return time.fromisoformat(policy["opening_auction_cutoff"])


def _submission_closed(
    broker: Broker, today: date, now: Callable[[], datetime]
) -> list[str]:
    """Broker-backed opening-auction orders go out only before today's cutoff."""
    if isinstance(broker, PaperBroker):
        return []
    observed = now()
    if observed.tzinfo is None:
        raise ValueError("now: clock must return timezone-aware datetimes")
    local = observed.astimezone(EXCHANGE_TZ)
    cutoff = _opening_auction_cutoff()
    if local.date() == today and local.time() < cutoff:
        return []
    return [
        f"submission window closed: observed {local:%Y-%m-%d %H:%M:%S} "
        f"America/New_York; orders for {today} must be submitted that day "
        f"before {cutoff:%H:%M}"
    ]


def _recover_prior_intents(broker: Broker, journal: Journal, today: date) -> None:
    """Observe earlier intents without placing stale orders at a later auction."""
    resolved = {
        e.payload["client_order_id"]
        for e in journal.events(["submitted", "submission_abandoned"])
    }
    for event in journal.events(["submission_intent"]):
        intent = event.payload
        client_id = intent["order"]["client_order_id"]
        if client_id in resolved or intent["session"] >= today.isoformat():
            continue
        ack = broker.lookup(client_id)
        if ack is None:
            journal.append(
                "submission_abandoned",
                {
                    "client_order_id": client_id,
                    "session": intent["session"],
                    "reason": "broker never observed this earlier-session intent",
                },
            )
        else:
            journal.append("submitted", json_value(ack))
        resolved.add(client_id)


def _sync(broker: Broker, data: MarketData, journal: Journal) -> list[Fill]:
    """Recover fills only for recorded intents, including interrupted settlement."""
    submitted = {e.payload["client_order_id"] for e in journal.events(["submitted"])}
    intents = {
        e.payload["order"]["client_order_id"]: e.payload
        for e in journal.events(["submission_intent"])
        if e.payload["order"]["client_order_id"] in submitted
    }
    known: dict[str, float] = {}
    for event in journal.events(["fill"]):
        client = event.payload["client_order_id"]
        known[client] = known.get(client, 0) + float(event.payload["qty"])
    observed: list[Fill] = []
    final: dict[str, str] = {}
    if isinstance(broker, PaperBroker):
        broker.settle(data)
        # Persisted fills also recover a crash between settlement and journaling.
        state = json.loads(broker.state_path.read_text())
        observed = [
            Fill(**f) for f in state["fills"] if f["client_order_id"] in intents
        ]
    else:
        terminal = {
            e.payload["client_order_id"]: e.payload
            for e in journal.events(["order_observed"])
        }
        finalized = {
            e.payload["client_order_id"] for e in journal.events(["order_final"])
        }
        for client_id, intent in intents.items():
            if client_id in finalized:
                continue
            auction_complete = pd.Timestamp(intent["session"]) in data.sessions
            if auction_complete:
                final[client_id] = (
                    "opening auction complete; unfilled remainder canceled"
                )
            previous = terminal.get(client_id, {})
            recovered = known.get(client_id, 0)
            if recovered >= intent["order"]["qty"] or (
                previous.get("status") in ("filled", "canceled", "rejected")
                and recovered >= previous.get("filled_qty", 0)
            ):
                continue
            ack = broker.lookup(client_id)
            if ack is None:
                if auction_complete:
                    final[client_id] = (
                        "not reported by broker after the opening auction"
                    )
                    continue
                raise BrokerError("recorded order is missing at broker")
            journal.append("order_observed", json_value(ack))
            if ack.filled_qty <= known.get(client_id, 0):
                continue
            order = intent["order"]
            if ack.filled_avg_price is None:
                raise BrokerError("filled order has no execution price")
            opening = pd.Timestamp(intent["session"])
            if opening not in data.sessions:
                raise BrokerError("execution reference session is unavailable")
            # Compare with the auction reference, not the previous close's gap.
            reference = float(data.open.loc[opening, order["symbol"]])
            prior_notional = sum(
                e.payload["qty"] * e.payload["price"]
                for e in journal.events(["fill"])
                if e.payload["client_order_id"] == client_id
            )
            delta = ack.filled_qty - known.get(client_id, 0)
            incremental_price = (
                ack.filled_qty * ack.filled_avg_price - prior_notional
            ) / delta
            observed.append(
                Fill(
                    client_id,
                    order["symbol"],
                    order["side"],
                    ack.filled_qty,
                    incremental_price,
                    reference,
                    0.0,
                    intent["session"],
                )
            )
    new: list[Fill] = []
    for fill in observed:
        intended = intents[fill.client_order_id]["order"]
        if (
            fill.symbol != intended["symbol"]
            or fill.side != intended["side"]
            or fill.qty > intended["qty"]
        ):
            raise BrokerError("fill disagrees with recorded order intent")
        delta = fill.qty - known.get(fill.client_order_id, 0)
        if delta <= 0:
            continue
        # Journal incremental quantities; reconstruct cumulative fills on replay.
        incremental = replace(fill, qty=delta)
        journal.append("fill", {**json_value(incremental), "broker_kind": broker.name})
        known[fill.client_order_id] = fill.qty
        new.append(incremental)
    # Persist finality only after incremental fills, so restart recovery cannot
    # skip executions that were observed but not yet journaled.
    for client_id, reason in final.items():
        qty = known.get(client_id, 0)
        filled = qty >= intents[client_id]["order"]["qty"]
        journal.append(
            "order_final",
            {
                "client_order_id": client_id,
                "filled_qty": qty,
                "status": "filled" if filled else "canceled",
                "reason": "opening auction filled" if filled else reason,
            },
        )
    return new


def _expected(journal: Journal) -> dict[str, float]:
    positions: dict[str, float] = {}
    for event in journal.events(["fill"]):
        f = event.payload
        positions[f["symbol"]] = positions.get(f["symbol"], 0) + (
            f["qty"] if f["side"] == "buy" else -f["qty"]
        )
    return positions


def run_session(
    config: TradingConfig,
    *,
    today: date,
    dry_run: bool = False,
    now: Callable[[], datetime] | None = None,
    provider: BarProvider | None = None,
    broker: Broker | None = None,
    environ: Mapping[str, str] = os.environ,
) -> SessionReport:
    """Previous-close decisions; no duplicate session submissions, even on retry.

    `now` is the submission clock (default: system time); it must return aware
    datetimes. Only broker-backed adapters are bound to the opening-auction window.
    """
    clock = now or (lambda: datetime.now(timezone.utc))
    try:
        with session_lock(config.state_dir) as stale:
            return _run_locked(
                config, today, dry_run, provider, broker, environ, stale, clock
            )
    except SessionLocked:
        return SessionReport(
            "HALTED",
            today.isoformat(),
            ["state_dir: another session is running"],
            [],
            [],
            None,
            {},
        )
    except Exception as exc:
        # A filesystem failure may prevent journaling/reporting; still fail closed.
        return SessionReport(
            "HALTED",
            today.isoformat(),
            [f"session failed ({type(exc).__name__})"],
            [],
            [],
            None,
            {},
            dry_run=dry_run,
        )


def _run_locked(
    config: TradingConfig,
    today: date,
    dry_run: bool,
    provider: BarProvider | None,
    broker: Broker | None,
    environ: Mapping[str, str],
    stale: bool,
    now: Callable[[], datetime],
) -> SessionReport:
    journal = Journal(config.state_dir / "journal.jsonl")
    account: AccountSnapshot | None = None
    fills: list[Fill] = []
    orders: list[Order] = []
    risk: dict[str, Any] = {}
    targets: dict[str, float] = {}
    decision: str | None = None
    breaks_count = 0
    verified = journal.verify().ok

    def finish(status: Status, reasons: list[str]) -> SessionReport:
        report = SessionReport(
            status,
            today.isoformat(),
            reasons,
            orders,
            fills,
            account,
            risk,
            decision,
            targets,
            dry_run,
        )
        if verified:
            payload = report.to_dict()
            payload.update(
                mode=config.mode,
                strategy=config.strategy_name,
                params=config.strategy_params,
                reconciliation_breaks=breaks_count,
                broker_kind=broker.name if broker is not None else config.broker_kind,
            )
            journal.append("session_outcome", payload)
        write_report(report, config.state_dir)
        return report

    if not verified:
        return finish("HALTED", ["journal verification failed"])
    kill = KillSwitch(config.state_dir)
    journal.append(
        "session_start",
        {"session": today.isoformat(), "dry_run": dry_run, "stale_lock": stale},
    )
    if kill.engaged():
        return finish("HALTED", ["kill switch engaged"])
    try:
        calendar = calendar_session(today)
        journal.append("calendar", json_value(calendar))
        if not calendar.trading_day:
            return finish("NO_SESSION", [calendar.describe()])
        decision = calendar_session(today - timedelta(days=1)).basis_date
        data = config.provider(provider).fetch(
            config.symbols, config.data_start, date.fromisoformat(decision)
        )
        data = data.upto(pd.Timestamp(decision))
        quality = check_quality(
            data, expected_last_session=date.fromisoformat(decision)
        )
        journal.append(
            "data_quality",
            {
                "session": today.isoformat(),
                "ok": quality.ok,
                "issues": json_value(quality.issues),
            },
        )
        if not quality.ok:
            return finish(
                "HALTED",
                [
                    f"data: {i.code} {i.symbol}"
                    for i in quality.issues
                    if i.severity == "error"
                ],
            )
        authorization = None
        if config.mode == "live":
            # Required before constructing a live broker or making any live call.
            authorization = authorize_live(config, environ=environ)
            journal.append("live_authorized", json_value(authorization))
        if broker is None:
            broker = configured_broker(config, environ, authorization=authorization)
        if broker.is_live != (config.mode == "live"):
            return finish("HALTED", ["broker mode does not match config.mode"])
        _recover_prior_intents(broker, journal, today)
        fills.extend(_sync(broker, data, journal))
        account = broker.account()
        from ..execution import reconcile

        breaks = reconcile(_expected(journal), account)
        breaks_count = len(breaks)
        journal.append(
            "reconcile",
            {
                "session": today.isoformat(),
                "breaks": json_value(breaks),
                "account": json_value(account),
            },
        )
        if breaks:
            return finish("HALTED", ["reconciliation break"])
        state_path = config.state_dir / "risk_state.json"
        recorded_risk = journal.events(["risk_state"])
        journal_state = (
            RiskState(**recorded_risk[-1].payload) if recorded_risk else None
        )
        state = RiskState.load(state_path) if state_path.exists() else journal_state
        if journal_state is not None and state != journal_state:
            return finish("HALTED", ["risk state disagrees with journal"])
        if state is None:
            state = RiskState(account.equity, account.equity, today.isoformat())
        state, reasons = update_risk_state(
            state, account, config.risk, session=today.isoformat()
        )
        state.save(state_path)
        dd = 1 - account.equity / state.high_water_mark
        daily = 1 - account.equity / state.day_start_equity
        risk.update(
            high_water_mark=state.high_water_mark,
            drawdown=dd,
            daily_loss=daily,
            drawdown_utilization=(
                dd / config.risk.max_drawdown_pct
                if config.risk.max_drawdown_pct
                else None
            ),
            daily_loss_utilization=(
                daily / config.risk.max_daily_loss_pct
                if config.risk.max_daily_loss_pct
                else None
            ),
        )
        journal.append("risk_state", json_value(state))
        if reasons:
            kill.engage("; ".join(reasons), source="runner")
            return finish("HALTED", reasons)
        # Daily account safety runs above; hypothetical off-cadence plans cannot halt.
        due = config.backtest.rebalance == "daily"
        if config.backtest.rebalance == "weekly":
            due = (
                pd.Timestamp(decision).isocalendar()[:2]
                != pd.Timestamp(today).isocalendar()[:2]
            )
        elif config.backtest.rebalance == "monthly":
            due = decision[:7] != today.isoformat()[:7]
        if (
            config.backtest.start is not None
            and pd.Timestamp(decision) < config.backtest.start
        ):
            due = False
        risk["rebalance_due"] = due
        if not due and not dry_run:
            previous_plans = [
                e.payload
                for e in journal.events(["plan"])
                if not e.payload.get("dry_run") and e.payload.get("rebalance_due", True)
            ]
            if previous_plans:
                targets.update(previous_plans[-1]["targets"])
            return finish("NO_CHANGE", ["outside rebalance calendar"])
        intents = journal.events(["submission_intent"])
        same = [e for e in intents if e.payload["session"] == today.isoformat()]
        submitted = {
            e.payload["client_order_id"] for e in journal.events(["submitted"])
        }
        abandoned = {
            e.payload["client_order_id"]
            for e in journal.events(["submission_abandoned"])
        }
        declined = [
            e.payload
            for e in journal.events(["broker_question"])
            if e.payload["session"] == today.isoformat()
        ]
        if declined:
            return finish("HALTED", [declined[-1]["detail"]])
        missing = [
            e
            for e in same
            if e.payload["order"]["client_order_id"] not in submitted | abandoned
        ]
        if missing:
            # Include already pending orders in the risk plan: their cash is unspent.
            recovery_plan = [Order(**e.payload["order"]) for e in same]
            checked = check_orders(
                recovery_plan,
                account,
                data.close.iloc[-1],
                config.risk,
                kill_switch=kill,
            )
            orders.extend(Order(**e.payload["order"]) for e in missing)
            journal.append(
                "submission_recovery",
                {
                    "session": today.isoformat(),
                    "orders": json_value(recovery_plan),
                    "halt": checked.halt,
                    "reasons": checked.reasons,
                    "dry_run": dry_run,
                },
            )
            if checked.halt and due:
                return finish("HALTED", checked.reasons)
            if dry_run:
                return finish(
                    "NO_CHANGE",
                    [
                        "dry run: interrupted submission preview",
                        *(["outside rebalance calendar"] if not due else []),
                        *checked.reasons,
                    ],
                )
            for order in orders:
                closed = _submission_closed(broker, today, now)
                if closed:
                    return finish("HALTED", closed)
                ack = broker.submit(order)
                journal.append("submitted", json_value(ack))
                if ack.status == "rejected":
                    return finish("HALTED", ["broker rejected order"])
            return finish("TRADED", ["recovered interrupted submission"])
        if same:
            previous_plans = [
                e.payload
                for e in journal.events(["plan"])
                if e.payload["session"] == today.isoformat()
            ]
            if previous_plans:
                targets.update(previous_plans[-1]["targets"])
            return finish("NO_CHANGE", ["session already submitted"])
        if broker.open_orders():
            return finish("HALTED", ["unsettled orders remain"])
        strategy = build_strategy(config.strategy_name, config.strategy_params)
        if len(data.sessions) < strategy.warmup:
            return finish("HALTED", ["data: insufficient strategy warmup"])
        raw_targets = strategy.target_weights(data.upto(pd.Timestamp(decision)))
        targets.update(config.backtest.buffered_targets(dict(raw_targets)))
        orders.extend(
            plan_orders(
                raw_targets,
                account,
                data.close.iloc[-1],
                session=today.isoformat(),
                strategy=strategy.name,
                config=config.backtest,
            )
        )
        checked = check_orders(
            orders, account, data.close.iloc[-1], config.risk, kill_switch=kill
        )
        turnover = sum(o.qty * float(data.close.iloc[-1][o.symbol]) for o in orders)
        projected = dict(account.weights())
        for order in orders:
            projected[order.symbol] = projected.get(order.symbol, 0) + (
                (1 if order.side == "buy" else -1)
                * order.qty
                * float(data.close.iloc[-1][order.symbol])
                / account.equity
            )
        risk.update(
            turnover_utilization=(
                turnover / account.equity / config.risk.max_turnover_pct
                if config.risk.max_turnover_pct
                else None
            ),
            max_weight_utilization=(
                max(projected.values(), default=0) / config.risk.max_weight
                if config.risk.max_weight
                else None
            ),
            cash_fraction=1 - sum(projected.values()),
            gross_utilization=(
                sum(abs(w) for w in projected.values()) / config.risk.max_gross
                if config.risk.max_gross
                else None
            ),
            order_count_utilization=(
                len(orders) / config.risk.max_orders if config.risk.max_orders else None
            ),
            max_order_notional_utilization=(
                max(
                    (
                        o.qty * float(data.close.iloc[-1][o.symbol]) / account.equity
                        for o in orders
                    ),
                    default=0,
                )
                / config.risk.max_order_notional_pct
                if config.risk.max_order_notional_pct
                else None
            ),
        )
        journal.append(
            "plan",
            {
                "session": today.isoformat(),
                "targets": targets,
                "orders": json_value(orders),
                "halt": checked.halt,
                "reasons": checked.reasons,
                "dry_run": dry_run,
                "rebalance_due": due,
            },
        )
        if not due:
            return finish(
                "NO_CHANGE",
                [
                    "outside rebalance calendar",
                    "dry run: preview only, not due",
                    *checked.reasons,
                ],
            )
        if checked.halt:
            return finish("HALTED", checked.reasons)
        if not orders:
            return finish("NO_CHANGE", [])
        if dry_run:
            return finish("NO_CHANGE", ["dry run: planned orders, no submission"])
        closed = _submission_closed(broker, today, now)
        if closed:
            return finish("HALTED", closed)
        for order in orders:
            journal.append(
                "submission_intent",
                {
                    "session": today.isoformat(),
                    "order": json_value(order),
                    "reference_price": float(data.close.iloc[-1][order.symbol]),
                },
            )
        for order in checked.approved:
            closed = _submission_closed(broker, today, now)
            if closed:
                return finish("HALTED", closed)
            ack = broker.submit(order)
            journal.append("submitted", json_value(ack))
            if ack.status == "rejected":
                return finish("HALTED", ["broker rejected order"])
        return finish("TRADED", [])
    except Exception as exc:
        # Providers/transports may embed credentials in errors: expose type only.
        from .promotion import PromotionError

        from ..execution.ibkr import IBKRQuestion

        if isinstance(exc, IBKRQuestion):
            journal.append(
                "broker_question", {"session": today.isoformat(), "detail": exc.detail}
            )
        reasons = (
            [exc.detail]
            if isinstance(exc, IBKRQuestion)
            else (
                exc.reasons
                if isinstance(exc, PromotionError)
                else [f"session failed ({type(exc).__name__})"]
            )
        )
        return finish("HALTED", reasons)
