from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, REPO, real_data
from test_kernels import RUN

from financial_agent.harness.mcp import HarnessServer, dataclass_schema, serve
from financial_agent.harness.kernels import EquityInputs


def rpc(server: HarnessServer, method: str, params: Any = None, id_: int = 1) -> Any:
    message: dict[str, Any] = {"jsonrpc": "2.0", "id": id_, "method": method}
    if params is not None:
        message["params"] = params
    response = server.handle(message)
    assert response is not None and response["id"] == id_
    return response


def call(server: HarnessServer, name: str, **arguments: Any) -> tuple[bool, str]:
    result = rpc(server, "tools/call", {"name": name, "arguments": arguments})["result"]
    return result["isError"], result["content"][0]["text"]


@pytest.fixture
def server(tmp_path: Path) -> HarnessServer:
    return HarnessServer(tmp_path)


def test_handshake_and_tool_listing(server: HarnessServer) -> None:
    init = rpc(server, "initialize", {"protocolVersion": "2025-03-26"})["result"]
    assert init["protocolVersion"] == "2025-03-26"
    assert init["capabilities"] == {"tools": {"listChanged": False}}
    assert init["serverInfo"]["name"] == "financial-agent-harness"
    unknown = rpc(server, "initialize", {"protocolVersion": "1999-01-01"})
    assert unknown["result"]["protocolVersion"] == "2025-06-18"
    assert (
        server.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}) is None
    )
    assert rpc(server, "ping")["result"] == {}

    tools = {t["name"]: t for t in rpc(server, "tools/list")["result"]["tools"]}
    assert set(tools) == {
        "gate",
        "manifest",
        "schema_check",
        "replay_history",
        "session",
        "reachability",
        "build_equity_records",
        "build_market_forecasts",
        "price_risk",
        "portfolio_feasibility",
        "score_universe",
        "policy",
    }
    assert all(t["annotations"]["readOnlyHint"] for t in tools.values())
    assert tools["gate"]["inputSchema"]["required"] == ["package"]


def test_protocol_errors(server: HarnessServer) -> None:
    assert rpc(server, "resources/list")["error"]["code"] == -32601
    missing = rpc(server, "tools/call", {"name": "place_order", "arguments": {}})
    assert missing["error"]["code"] == -32602
    bad = server.handle_line("{not json")
    assert bad is not None and bad["error"]["code"] == -32700
    listed = server.handle_line(
        '{"jsonrpc": "2.0", "id": 3, "method": "ping", "params": [1]}'
    )
    assert listed is not None and listed["error"]["code"] == -32602
    assert server.handle({"id": 1, "method": "ping"}) == {
        "jsonrpc": "2.0",
        "id": None,
        "error": {"code": -32600, "message": "not a JSON-RPC 2.0 message"},
    }


def test_equity_input_schema_comes_from_the_dataclass() -> None:
    schema = dataclass_schema(EquityInputs)
    assert schema["properties"]["entry_price"] == {"type": "number"}
    assert schema["properties"]["horizon_days"] == {
        "anyOf": [{"type": "integer"}, {"type": "null"}]
    }
    assert schema["properties"]["ledger_rows"]["items"] == {"type": "string"}
    assert "pctl" in schema["required"] and "penalties" not in schema["required"]


def test_compute_tools(server: HarnessServer) -> None:
    is_error, text = call(server, "session", date="2026-07-03")
    assert not is_error and json.loads(text)["kind"] == "HOLIDAY"
    is_error, text = call(server, "reachability")
    assert not is_error and json.loads(text)["reachable"] is False
    is_error, text = call(server, "policy", key="evidence.min_pctl")
    assert (is_error, json.loads(text)) == (False, 80.0)
    is_error, text = call(server, "policy", key="evidence.nope")
    assert is_error and "no policy key" in text

    spy = [400 * 1.001**i for i in range(61)]
    stock = [50 * (1.002**i) * (1.01 if i % 2 else 0.99) for i in range(61)]
    is_error, text = call(server, "price_risk", closes=stock, spy_closes=spy)
    assert not is_error and json.loads(text)["realized_vol_30d"] > 0
    holding = {"ticker": "A", "weight": 0.05, "sector": "Tech", "closes": stock}
    is_error, text = call(
        server, "portfolio_feasibility", holdings=[holding], spy_closes=spy
    )
    assert not is_error and json.loads(text)["avg_pairwise_corr"] is None


def test_kernel_tools_refuse_out_of_policy_inputs(server: HarnessServer) -> None:
    etfs = [
        {
            "ticker": t,
            "entry_price": p,
            "price_tag": "DELAYED",
            "price_date": RUN,
            "sigma": 0.05,
            "sigma_source": "REALIZED_VOL_30D",
            "thesis": "t",
            **({} if t == "SPY" else {"beta_vs_spy": 1.5}),
        }
        for t, p in (("SPY", 773.17), ("QQQ", 717.67), ("SOXX", 502.2))
    ]
    args = {"run_date": RUN, "model": "m", "regime": "BULL", "etfs": etfs}
    is_error, text = call(server, "build_market_forecasts", **args)
    assert not is_error
    assert [r["mu"] for r in json.loads(text)] == [0.02, 0.03, 0.03]
    etfs[1]["mu_adjustment"] = 0.05
    is_error, text = call(server, "build_market_forecasts", **args)
    assert is_error and "exceeds" in text
    is_error, text = call(
        server, "build_equity_records", run_date=RUN, model="m", names=[{"x": 1}]
    )
    assert is_error and "unknown equity input" in text


def test_packages_must_live_directly_under_the_output_dir(tmp_path: Path) -> None:
    (tmp_path / "out").mkdir()
    (tmp_path / "secret").mkdir()
    server = HarnessServer(tmp_path / "out")
    for name in ("../secret", "", ".", "missing-2026-09-03"):
        is_error, text = call(server, "gate", package=name)
        assert is_error and "no package" in text, name


@real_data
def test_gate_and_replay_over_real_packages() -> None:
    server = HarnessServer(OUTPUT_DIR)
    is_error, text = call(server, "gate", package="claude-opus-5-2026-09-03")
    report = json.loads(text)
    assert not is_error and report["pass"] and report["replay"]["agrees"]
    assert report["replay"]["go_reachable"] is False
    is_error, text = call(server, "replay_history", as_of="2026-09-03")
    summary = json.loads(text)
    assert (summary["replayed"], summary["agree"]) == (83, 73)
    is_error, text = call(server, "schema_check", package="claude-opus-5-2026-09-03")
    assert not is_error and any("kelly_025" in f for f in json.loads(text))


def test_stdio_transport(tmp_path: Path) -> None:
    lines = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    ]
    stdin = io.StringIO("\n".join(json.dumps(m) for m in lines) + "\n\n")
    stdout = io.StringIO()
    serve(stdin, stdout, output_dir=tmp_path)
    responses = [json.loads(line) for line in stdout.getvalue().splitlines()]
    assert [r["id"] for r in responses] == [1, 2]


def test_cli_serves_mcp_over_stdio(tmp_path: Path) -> None:
    request = {"jsonrpc": "2.0", "id": 7, "method": "tools/call"}
    request["params"] = {"name": "session", "arguments": {"date": "2026-08-22"}}
    done = subprocess.run(
        [sys.executable, "-m", "financial_agent.harness", "mcp"],
        input=json.dumps(request) + "\n",
        capture_output=True,
        text=True,
        cwd=REPO,
        env={**os.environ, "PYTHONPATH": str(REPO / "src")},
        timeout=60,
        check=True,
    )
    response = json.loads(done.stdout)
    assert response["id"] == 7
    assert json.loads(response["result"]["content"][0]["text"])["kind"] == "WEEKEND"
