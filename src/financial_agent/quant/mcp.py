"""Research and read-only paper previews over the harness JSON-RPC plumbing."""

from collections.abc import Mapping
from functools import partial
from datetime import date, datetime, timedelta, timezone
import json
from importlib.metadata import version
from pathlib import Path
from typing import IO, Any

import pandas as pd  # type: ignore[import-untyped]

from financial_agent.harness.mcp import HarnessServer, Tool, ToolError
from financial_agent.harness.market_calendar import session
from .backtest import run_backtest
from .data import check_quality
from .execution import Journal, reconcile
from .risk import (
    AccountSnapshot,
    KillSwitch,
    Position,
    RiskState,
    check_orders,
    plan_orders,
    update_risk_state,
)
from .runner import TradingConfig, status_summary
from .runner.report import json_value
from .runner.session import _expected
from .strategies import build_strategy
from .validation import PromotionPolicy, evaluate_promotion


class QuantServer(HarnessServer):
    """Inherit framing and MCP protocol only; every capability is an allowlist."""

    def __init__(self) -> None:
        self.tools = {tool.name: tool for tool in self._tools()}

    def handle(self, message: Any) -> dict[str, Any] | None:
        response = super().handle(message)
        if (
            isinstance(message, dict)
            and message.get("method") == "initialize"
            and response
            and "result" in response
        ):
            response["result"]["serverInfo"] = {
                "name": "financial-agent-quant",
                "version": version("fa-quant"),
            }
            response["result"]["instructions"] = (
                "Research and paper previews only. No submission, cancellation, "
                "kill-switch mutation, or live-mode access exists."
            )
        return response

    def _tools(self) -> list[Tool]:
        tools = []
        for name, description in (
            ("quant_backtest", "Backtest configured strategy with modeled costs."),
            ("quant_validate", "Evaluate the packaged statistical promotion policy."),
            ("quant_data_check", "Check data quality through a specified close."),
            (
                "quant_status",
                "Read persisted paper positions, NAV and journal validity.",
            ),
            ("quant_preview_orders", "Plan paper orders and check risk; never submit."),
        ):
            properties: dict[str, Any] = {"config": {"type": "string"}}
            if name != "quant_status":
                properties["today"] = {"type": "string", "format": "date"}
            if name == "quant_validate":
                properties["grid"] = {"type": "array", "items": {"type": "object"}}
            schema = {
                "type": "object",
                "properties": properties,
                "required": ["config"],
                "additionalProperties": False,
            }
            tools.append(
                Tool(
                    name,
                    description,
                    schema,
                    partial(self._execute, name),
                )
            )
        return tools

    def _execute(self, name: str, args: Mapping[str, Any]) -> Any:
        allowed = self.tools[name].input_schema["properties"]
        if args.keys() - allowed.keys():
            raise ToolError("unknown input keys")
        try:
            config = TradingConfig.load(Path(args["config"]))
            if config.mode != "paper":
                raise ToolError("MCP only accepts paper configurations")
            if name == "quant_status":
                return status_summary(config)
            today = date.fromisoformat(args.get("today", date.today().isoformat()))
            decision = date.fromisoformat(session(today - timedelta(days=1)).basis_date)
            data = config.provider().fetch(config.symbols, config.data_start, decision)
            quality = check_quality(data, expected_last_session=decision)
            if name == "quant_data_check":
                return {"ok": quality.ok, "issues": json_value(quality.issues)}
            if not quality.ok:
                raise ToolError("market data quality gate failed")
            strategy = build_strategy(config.strategy_name, config.strategy_params)
            if name == "quant_backtest":
                return json_value(
                    run_backtest(strategy, data, config.backtest).summary()
                )
            if name == "quant_validate":
                grid = args.get("grid", list(config.grid) or [config.strategy_params])
                if (
                    not isinstance(grid, list)
                    or not grid
                    or any(not isinstance(p, dict) for p in grid)
                ):
                    raise ToolError("grid must be nonempty parameter objects")
                return json_value(
                    evaluate_promotion(
                        strategy.name,
                        grid,
                        data,
                        config.backtest,
                        PromotionPolicy.load(),
                    )
                )
            summary = status_summary(config)
            if not summary["journal"]["ok"]:
                raise ToolError("journal verification failed")
            if not session(today).trading_day:
                return {"status": "NO_SESSION", "orders": []}
            if len(data.sessions) < strategy.warmup:
                raise ToolError("insufficient strategy warmup")
            value = summary["account"] or {
                "cash": config.initial_cash,
                "equity": config.initial_cash,
                "positions": {},
            }
            account = AccountSnapshot(
                value["cash"],
                value["equity"],
                {s: Position(**p) for s, p in value["positions"].items()},
                datetime.now(timezone.utc),
            )
            journal = Journal(config.state_dir / "journal.jsonl")
            breaks = reconcile(_expected(journal), account)
            state = (
                RiskState.load(config.state_dir / "risk_state.json")
                if (config.state_dir / "risk_state.json").exists()
                else RiskState(
                    config.initial_cash, config.initial_cash, today.isoformat()
                )
            )
            _, reasons = update_risk_state(
                state, account, config.risk, session=today.isoformat()
            )
            if breaks:
                reasons.append("reconciliation break")
            # Preview does not settle pending paper orders or mutate broker state.
            paper_path = config.state_dir / "paper.json"
            if paper_path.exists():
                paper = json.loads(paper_path.read_text())
                if any(o["status"] == "pending" for o in paper["orders"].values()):
                    reasons.append("unsettled paper orders remain")
            targets = strategy.target_weights(data.upto(pd.Timestamp(decision)))
            orders = plan_orders(
                targets,
                account,
                data.close.iloc[-1],
                session=today.isoformat(),
                strategy=strategy.name,
                config=config.backtest,
            )
            checked = check_orders(
                orders,
                account,
                data.close.iloc[-1],
                config.risk,
                kill_switch=KillSwitch(config.state_dir),
            )
            return {
                "status": "HALTED" if checked.halt or reasons else "NO_CHANGE",
                "orders": json_value(orders),
                "targets": dict(targets),
                "risk": json_value(checked),
                "reasons": reasons,
            }
        except ToolError:
            raise
        except Exception:
            # A custom source error must never expose credentials over stdio.
            raise ToolError(
                "quant computation failed; check configuration and state"
            ) from None


def serve(instream: IO[str], outstream: IO[str]) -> None:
    """Answer newline-delimited JSON-RPC until stdin closes."""
    server = QuantServer()
    for line in instream:
        if not line.strip():
            continue
        response = server.handle_line(line)
        if response is not None:
            outstream.write(json.dumps(response, allow_nan=False, default=str) + "\n")
            outstream.flush()
