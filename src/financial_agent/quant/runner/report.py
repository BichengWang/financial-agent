"""Durable session reports; currency values and equity-fraction utilization."""

from collections.abc import Mapping
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
import json
import math
from pathlib import Path
from typing import Any, Literal

from ..execution import Fill, Journal
from ..risk import AccountSnapshot, KillSwitch, Order, RiskState
from ..risk.state import _atomic_json
from .config import TradingConfig

Status = Literal["TRADED", "NO_CHANGE", "NO_SESSION", "HALTED"]


def json_value(value: Any) -> Any:
    """Convert immutable dataclasses and nonfinite research statistics to JSON."""
    if is_dataclass(value) and not isinstance(value, type):
        return {
            f.name: json_value(getattr(value, f.name))
            for f in fields(value)
            if not f.name.startswith("_")
        }
    if isinstance(value, Mapping):
        return {str(k): json_value(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(v) for v in value]
    if isinstance(value, (date, datetime, Path)):
        return str(value)
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


@dataclass(frozen=True)
class SessionReport:
    status: Status
    session: str
    reasons: list[str]
    orders: list[Order]
    fills: list[Fill]
    account: AccountSnapshot | None
    risk: dict[str, Any]
    decision_session: str | None = None
    targets: dict[str, float] | None = None
    dry_run: bool = False

    def to_dict(self) -> dict[str, Any]:
        """JSON-ready report with observed actual weights beside targets."""
        result: dict[str, Any] = json_value(self)
        result["actual_weights"] = (
            self.account.weights() if self.account and self.account.equity > 0 else {}
        )
        return result


def render_markdown(report: SessionReport) -> str:
    """Render planned orders distinctly from submitted orders in previews."""
    account = report.account
    lines = [
        f"# {report.session}: {report.status}",
        "",
        f"Decision close: {report.decision_session or 'unavailable'}",
        f"Dry run: {report.dry_run}",
        f"NAV: {account.equity:.2f}" if account else "NAV: unavailable",
        "",
    ]
    lines.extend(f"- {reason}" for reason in report.reasons)
    lines += ["", "| Symbol | Target (last plan) | Actual |", "|---|---:|---:|"]
    actual = account.weights() if account and account.equity > 0 else {}
    targets = report.targets or {}
    for symbol in sorted(targets.keys() | actual.keys()):
        target_weight = f"{targets[symbol]:.2%}" if symbol in targets else "—"
        lines.append(f"| {symbol} | {target_weight} | {actual.get(symbol, 0):.2%} |")
    lines += ["", "## Planned orders" if report.dry_run else "## Orders", ""]
    lines.extend(
        f"- {o.side} {o.qty:g} {o.symbol} ({o.client_order_id})" for o in report.orders
    )
    lines += ["", "## Fills", ""]
    lines.extend(
        f"- {f.side} {f.qty:g} {f.symbol} at {f.price:.4f}" for f in report.fills
    )
    lines += [
        "",
        "## Risk (fractions of equity / limit)",
        "",
        "```json",
        json.dumps(json_value(report.risk), indent=2),
        "```",
        "",
    ]
    return "\n".join(lines)


def write_report(report: SessionReport, state_dir: Path) -> None:
    """Preserve each attempt; callers serialize writes with the session lock."""
    root = state_dir / "reports"
    root.mkdir(parents=True, exist_ok=True)
    name = report.session + (".preview" if report.dry_run else "")
    base = name
    attempt = 2
    while (root / f"{name}.json").exists() or (root / f"{name}.md").exists():
        name = f"{base}.{attempt}"
        attempt += 1
    _atomic_json(root / f"{name}.json", report.to_dict())
    target = root / f"{name}.md"
    temporary = target.with_suffix(".md.tmp")
    temporary.write_text(render_markdown(report))
    temporary.replace(target)


def status_summary(config: TradingConfig) -> dict[str, Any]:
    """Read persisted observations only; never connect to or initialize a broker."""
    root = config.state_dir
    journal = Journal(root / "journal.jsonl")
    check = journal.verify()
    records = journal.events(["session_outcome"]) if check.ok else []
    last = records[-1].payload if records else {}
    account = last.get("account")
    if config.broker_kind == "paper" and (root / "paper.json").exists():
        state = json.loads((root / "paper.json").read_text())
        positions = state["positions"]
        equity = state["cash"] + sum(
            p["qty"] * p["market_price"] for p in positions.values()
        )
        account = {
            "cash": state["cash"],
            "equity": equity,
            "positions": positions,
            "as_of": state["last_session"],
        }
    risk_path = root / "risk_state.json"
    risk = RiskState.load(risk_path) if risk_path.exists() else None
    nav = account["equity"] if account else None
    drawdown = 1 - nav / risk.high_water_mark if risk and nav is not None else None
    kill = KillSwitch(root)
    return {
        "mode": config.mode,
        "account": account,
        "nav": nav,
        "drawdown": drawdown,
        "risk": json_value(risk),
        "kill_switch": {"engaged": kill.engaged(), "reason": kill.reason()},
        "last_sessions": [e.payload for e in records[-10:]],
        "journal": json_value(check),
    }


def render_status(summary: dict[str, Any]) -> str:
    """A compact operator view with chain validity and observation timestamp."""
    lines = [
        f"NAV: {summary['nav']}",
        f"Drawdown: {summary['drawdown']}",
        f"Kill switch: {summary['kill_switch']['engaged']}",
        f"Journal verified: {summary['journal']['ok']}",
    ]
    account = summary.get("account") or {}
    lines.append(f"Observed at: {account.get('as_of')}")
    lines.extend(
        f"{s}: {p['qty']:g} shares @ {p['market_price']:.4f}"
        for s, p in account.get("positions", {}).items()
    )
    lines.extend(f"{p['session']}: {p['status']}" for p in summary["last_sessions"])
    return "\n".join(lines)
