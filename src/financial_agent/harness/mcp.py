"""The harness tools over the Model Context Protocol (stdio, plan Phase 4).

Any MCP client (Claude Code, the Agent SDK, Codex, Gemini CLI) can call the
same functions the CLI exposes, with typed inputs and JSON results, instead of
parsing shell output. Standard library only: newline-delimited JSON-RPC 2.0 on
stdin/stdout, implementing ``initialize``, ``ping``, ``tools/list`` and
``tools/call``.

Every tool is read-only or a pure computation. Packages are addressed by name
and must live directly under the output directory; nothing here writes files,
and no order-placement tool exists (plan §3.7).

    python -m financial_agent.harness mcp
"""

from __future__ import annotations

import dataclasses
import json
import types
import typing
from dataclasses import dataclass
from pathlib import Path
from typing import IO, Any, Callable, Mapping

from financial_agent.harness.gates import go_reachability, replay_history
from financial_agent.harness.kernels import (
    EquityInputs,
    KernelError,
    MarketInputs,
    equity_record,
    market_forecast_records,
    price_risk,
)
from financial_agent.harness.manifest import (
    gate_report,
    render_manifest_sections,
    replay_dict,
)
from financial_agent.harness.market_calendar import session
from financial_agent.harness.policy import FAMILIES, Policy, load_policy
from financial_agent.harness.schema import validate_payload

SERVER_INFO = {"name": "financial-agent-harness", "version": "0.1.0"}
PROTOCOL_VERSIONS = ("2025-06-18", "2025-03-26", "2024-11-05")
PARSE_ERROR, INVALID_REQUEST, METHOD_NOT_FOUND, INVALID_PARAMS, INTERNAL_ERROR = (
    -32700,
    -32600,
    -32601,
    -32602,
    -32603,
)
INSTRUCTIONS = (
    "Deterministic tools for the daily equity research run. The model decides; "
    "these tools compute and enforce. Never type a number a tool can compute: "
    "build ledger records with build_equity_records and build_market_forecasts, "
    "and run gate before a package moves to PUBLISHED."
)


class ToolError(ValueError):
    """A tool call the server refuses; reported as an ``isError`` result."""


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: Callable[[Mapping[str, Any]], Any]


def _json_type(annotation: Any) -> dict[str, Any]:
    origin = typing.get_origin(annotation)
    args = [a for a in typing.get_args(annotation) if a is not type(None)]
    if origin in (typing.Union, types.UnionType):
        inner = _json_type(args[0]) if len(args) == 1 else {}
        return {"anyOf": [inner, {"type": "null"}]}
    if annotation is str:
        return {"type": "string"}
    if annotation is bool:
        return {"type": "boolean"}
    if annotation is int:
        return {"type": "integer"}
    if annotation is float:
        return {"type": "number"}
    if origin in (tuple, list):
        return {"type": "array", "items": _json_type(args[0])}
    return {"type": "object"}


def dataclass_schema(cls: type) -> dict[str, Any]:
    """Input schema from a kernel's input dataclass: one source of truth."""
    hints = typing.get_type_hints(cls)
    fields = dataclasses.fields(cls)
    return {
        "type": "object",
        "properties": {f.name: _json_type(hints[f.name]) for f in fields},
        "required": [
            f.name
            for f in fields
            if f.default is dataclasses.MISSING
            and f.default_factory is dataclasses.MISSING
        ],
        "additionalProperties": False,
    }


def _object(
    properties: dict[str, Any], required: tuple[str, ...] = ()
) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": list(required),
        "additionalProperties": False,
    }


DATE = {"type": "string", "format": "date", "description": "YYYY-MM-DD"}
PACKAGE = {
    "type": "string",
    "description": "package directory name, e.g. claude-opus-5-2026-09-03",
}
SERIES = {"type": "array", "items": {"type": "number"}, "minItems": 61}


class HarnessServer:
    def __init__(self, output_dir: Path, policy: Policy | None = None) -> None:
        self.output_dir = output_dir
        self.policy = policy or load_policy()
        self.tools = {tool.name: tool for tool in self._tools()}

    # -- tools -------------------------------------------------------------

    def _package(self, args: Mapping[str, Any]) -> Path:
        name = str(args.get("package", ""))
        root = self.output_dir.resolve()
        target = (root / name).resolve()
        if not name or target.parent != root or not target.is_dir():
            raise ToolError(f"no package {name!r} directly under {self.output_dir}")
        return target

    def _tools(self) -> list[Tool]:
        policy = self.policy
        return [
            Tool(
                "gate",
                "Publish gate, status replay (with trading calendar and GO "
                "reachability), and content hash for one run package. A package "
                "may move to PUBLISHED only when pass is true.",
                _object({"package": PACKAGE}, ("package",)),
                lambda a: gate_report(self._package(a), policy),
            ),
            Tool(
                "manifest",
                "Markdown for the generated sections of 00_run_manifest.md: "
                "artifact checklist read from disk, status replay, publish gate.",
                _object({"package": PACKAGE}, ("package",)),
                lambda a: render_manifest_sections(self._package(a), policy)[0],
            ),
            Tool(
                "schema_check",
                "Findings for a package's 15_predictions.json against ledger "
                "schema v1 (empty means valid).",
                _object({"package": PACKAGE}, ("package",)),
                self._schema_check,
            ),
            Tool(
                "replay_history",
                "Recompute every published run status from its ledger and list "
                "the packages whose published status disagrees.",
                _object({"since": DATE, "as_of": DATE}),
                self._replay_history,
            ),
            Tool(
                "session",
                "Whether a date is an NYSE trading day, weekend, or holiday, and "
                "the most recent close at or before it.",
                _object({"date": DATE}, ("date",)),
                lambda a: vars(session(str(a["date"]))),
            ),
            Tool(
                "reachability",
                "Structural GO blockers: evidence thresholds no name can pass "
                "with the factor families that can score.",
                _object(
                    {
                        "families": {
                            "type": "array",
                            "items": {"enum": list(FAMILIES)},
                        },
                        "ranked_names": {"type": "integer"},
                    }
                ),
                self._reachability,
            ),
            Tool(
                "build_equity_records",
                "Schema-v1 EQUITY_ALPHA ledger records computed from grounded "
                "inputs and judgment (mu adjustment within policy, confidence "
                "no higher than the evidence allows). Refuses out-of-policy input.",
                _object(
                    {
                        "run_date": DATE,
                        "model": {"type": "string"},
                        "names": {
                            "type": "array",
                            "items": dataclass_schema(EquityInputs),
                        },
                    },
                    ("run_date", "model", "names"),
                ),
                lambda a: [
                    equity_record(
                        a["run_date"],
                        a["model"],
                        EquityInputs.from_mapping(item),
                        policy,
                    )
                    for item in a["names"]
                ],
            ),
            Tool(
                "build_market_forecasts",
                "Schema-v1 MARKET_FORECAST records for SPY, QQQ, SOXX: SPY from "
                "the regime prior, the others as beta x SPY mu, within the bands.",
                _object(
                    {
                        "run_date": DATE,
                        "model": {"type": "string"},
                        "regime": {
                            "enum": list(policy.get("market_forecast.spy_regime_prior"))
                        },
                        "etfs": {
                            "type": "array",
                            "items": dataclass_schema(MarketInputs),
                        },
                    },
                    ("run_date", "model", "regime", "etfs"),
                ),
                lambda a: market_forecast_records(
                    a["run_date"],
                    a["model"],
                    a["regime"],
                    [MarketInputs.from_mapping(item) for item in a["etfs"]],
                    policy,
                ),
            ),
            Tool(
                "price_risk",
                "Beta, realized/downside vol, tracking error and 60d drawdown from "
                "date-aligned adjusted closes (oldest first, at least 61).",
                _object(
                    {"closes": SERIES, "spy_closes": SERIES, "tlt_closes": SERIES},
                    ("closes", "spy_closes"),
                ),
                lambda a: vars(
                    price_risk(
                        a["closes"], a["spy_closes"], tlt_closes=a.get("tlt_closes")
                    )
                ),
            ),
            Tool(
                "policy",
                "Read a value from the numeric policy by dotted key (e.g. "
                "evidence.min_pctl), or the whole policy. Cite it; never retype it.",
                _object({"key": {"type": "string"}}),
                self._policy_value,
            ),
        ]

    def _schema_check(self, args: Mapping[str, Any]) -> list[str]:
        path = self._package(args) / "15_predictions.json"
        if not path.exists():
            raise ToolError(f"{path.name} not found in {path.parent.name}")
        return validate_payload(
            json.loads(path.read_text(encoding="utf-8")), self.policy
        )

    def _replay_history(self, args: Mapping[str, Any]) -> dict[str, Any]:
        replays = replay_history(
            self.output_dir,
            self.policy,
            since=args.get("since"),
            as_of=args.get("as_of"),
        )
        return {
            "replayed": len(replays),
            "agree": sum(1 for _, r in replays if r.agrees),
            "disagreements": {
                name: replay_dict(replay)
                for name, replay in replays
                if not replay.agrees
            },
        }

    def _reachability(self, args: Mapping[str, Any]) -> dict[str, Any]:
        reach = go_reachability(
            self.policy,
            available_families=args.get("families"),
            ranked_names=args.get("ranked_names"),
        )
        return {
            "reachable": reach.reachable,
            "gating_families": list(reach.gating_families),
            "blockers": list(reach.blockers),
        }

    def _policy_value(self, args: Mapping[str, Any]) -> Any:
        key = args.get("key")
        if not key:
            return self.policy.data
        try:
            return self.policy.get(str(key))
        except (KeyError, TypeError):
            raise ToolError(f"no policy key {key!r}") from None

    # -- protocol ----------------------------------------------------------

    def handle(self, message: Any) -> dict[str, Any] | None:
        """One JSON-RPC message in, the response out (``None`` for notices)."""
        if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
            return _error(None, INVALID_REQUEST, "not a JSON-RPC 2.0 message")
        if "id" not in message:
            return None  # notifications/initialized, cancelled, ...
        request_id, method = message["id"], message.get("method")
        params = message.get("params") or {}
        if not isinstance(params, dict):
            return _error(request_id, INVALID_PARAMS, "params must be an object")
        if method == "initialize":
            asked = params.get("protocolVersion")
            version = asked if asked in PROTOCOL_VERSIONS else PROTOCOL_VERSIONS[0]
            return _result(
                request_id,
                {
                    "protocolVersion": version,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": SERVER_INFO,
                    "instructions": INSTRUCTIONS,
                },
            )
        if method == "ping":
            return _result(request_id, {})
        if method == "tools/list":
            return _result(
                request_id,
                {
                    "tools": [
                        {
                            "name": t.name,
                            "description": t.description,
                            "inputSchema": t.input_schema,
                            "annotations": {
                                "readOnlyHint": True,
                                "openWorldHint": False,
                            },
                        }
                        for t in self.tools.values()
                    ]
                },
            )
        if method == "tools/call":
            tool = self.tools.get(str(params.get("name")))
            if tool is None:
                return _error(
                    request_id, INVALID_PARAMS, f"unknown tool {params.get('name')!r}"
                )
            return _result(request_id, self._call(tool, params.get("arguments") or {}))
        return _error(request_id, METHOD_NOT_FOUND, f"method {method!r} not found")

    def _call(self, tool: Tool, arguments: Any) -> dict[str, Any]:
        try:
            if not isinstance(arguments, Mapping):
                raise ToolError("arguments must be an object")
            value = tool.handler(arguments)
        except (
            ToolError,
            KernelError,
            KeyError,
            TypeError,
            ValueError,
            OSError,
        ) as exc:
            text = f"{type(exc).__name__}: {exc}"
            return {"content": [{"type": "text", "text": text}], "isError": True}
        text = value if isinstance(value, str) else json.dumps(value, default=str)
        return {"content": [{"type": "text", "text": text}], "isError": False}

    def handle_line(self, line: str) -> dict[str, Any] | None:
        try:
            message = json.loads(line)
        except json.JSONDecodeError as exc:
            return _error(None, PARSE_ERROR, f"parse error: {exc}")
        try:
            return self.handle(message)
        except Exception as exc:  # one bad request never stops the server
            request_id = message.get("id") if isinstance(message, dict) else None
            return _error(request_id, INTERNAL_ERROR, f"{type(exc).__name__}: {exc}")


def _result(request_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def _error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": message},
    }


def serve(instream: IO[str], outstream: IO[str], *, output_dir: Path) -> None:
    """Answer newline-delimited JSON-RPC on ``instream`` until it closes."""
    server = HarnessServer(output_dir)
    for line in instream:
        if not line.strip():
            continue
        response = server.handle_line(line)
        if response is not None:
            outstream.write(json.dumps(response, default=str) + "\n")
            outstream.flush()
