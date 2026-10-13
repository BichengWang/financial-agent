"""Operator smoke tests and MCP's capability boundary remain network-free."""

from io import StringIO
import json
from pathlib import Path
from typing import Any

import pytest

from financial_agent.quant.__main__ import main
from financial_agent.quant.mcp import QuantServer, serve
from financial_agent.quant.risk import KillSwitch
from financial_agent.quant.runner import TradingConfig

# Share real CSV fixtures across CLI and runner tests.
from .runner import conftest as runner_fixtures

config_path = runner_fixtures.config_path


def test_cli_run_status_preview_and_controls(config_path: Path, capsys: Any) -> None:
    config = TradingConfig.load(config_path)
    prefix = ["--config", str(config_path)]
    assert main(["run", *prefix, "--today", "2020-06-08", "--dry-run", "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["orders"]
    assert main(["run", *prefix, "--today", "2020-06-08", "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "TRADED"
    assert main(["run", *prefix, "--today", "2020-06-09", "--json"]) == 0
    capsys.readouterr()
    assert main(["status", *prefix, "--json"]) == 0
    summary = json.loads(capsys.readouterr().out)
    assert summary["nav"] > 0 and summary["account"]["positions"]
    assert main(["kill", *prefix, "--reason", "review requested"]) == 0
    assert main(["run", *prefix, "--today", "2020-06-10"]) == 2
    capsys.readouterr()
    assert (
        main(["unkill", *prefix, "--reason", "review complete", "--operator", "owner"])
        == 0
    )
    assert not KillSwitch(config.state_dir).engaged()
    assert main(["run", *prefix, "--today", "2020-06-10", "--dry-run"]) == 0


def test_cli_research_data_and_failed_certificate(
    config_path: Path, tmp_path: Path, capsys: Any
) -> None:
    prefix = ["--config", str(config_path), "--end", "2020-06-05"]
    assert (
        main(["data", "check", *prefix, "--expected-last-session", "2020-06-05"]) == 0
    )
    assert json.loads(capsys.readouterr().out)["quality"]["issues"] == []
    assert main(["backtest", *prefix, "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["total_return"] > 0
    cert = tmp_path / "cert.json"
    assert (
        main(
            [
                "certify",
                *prefix,
                "--grid",
                '[{"lookbacks":[3,10],"cov_lookback":10}]',
                "--output",
                str(cert),
                "--json",
            ]
        )
        == 2
    )
    assert not json.loads(cert.read_text())["passed"]
    assert not json.loads(capsys.readouterr().out)["passed"]


@pytest.mark.parametrize(
    "args", [[], ["run"], ["run", "--today", "oops"], ["demo", "--sessions", "0"]]
)
def test_usage_errors_return_one(args: list[str], capsys: Any) -> None:
    assert main(args) == 1
    assert "error:" in capsys.readouterr().err


def call(server: QuantServer, name: str, args: dict[str, Any]) -> dict[str, Any]:
    response = server.handle(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": name, "arguments": args},
        }
    )
    assert response is not None
    return response


def test_mcp_tools_cannot_submit_cancel_or_access_live(config_path: Path) -> None:
    server = QuantServer()
    assert set(server.tools) == {
        "quant_backtest",
        "quant_validate",
        "quant_data_check",
        "quant_status",
        "quant_preview_orders",
    }
    result = call(
        server,
        "quant_preview_orders",
        {"config": str(config_path), "today": "2020-06-08"},
    )
    assert not result["result"]["isError"]
    value = json.loads(result["result"]["content"][0]["text"])
    assert value["orders"] and not value["risk"]["halt"]
    config = TradingConfig.load(config_path)
    assert not (config.state_dir / "paper.json").exists()
    assert not (config.state_dir / "journal.jsonl").exists()
    assert not (config.state_dir / "risk_state.json").exists()
    result = call(server, "submit", {"config": str(config_path)})
    assert "error" in result
    config_path.write_text(
        config_path.read_text()
        .replace('mode = "paper"', 'mode = "live"')
        .replace('kind = "paper"', 'kind = "alpaca"')
    )
    result = call(server, "quant_status", {"config": str(config_path)})
    assert result["result"]["isError"]
    assert "paper configurations" in result["result"]["content"][0]["text"]


def test_mcp_reuses_protocol_and_suppresses_notifications() -> None:
    requests = [
        "{",
        json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}),
        json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "initialize",
                "params": {"protocolVersion": "2025-03-26"},
            }
        ),
        json.dumps({"jsonrpc": "2.0", "id": 4, "method": "tools/list"}),
    ]
    output = StringIO()
    serve(StringIO("\n".join(requests)), output)
    responses = [json.loads(line) for line in output.getvalue().splitlines()]
    assert len(responses) == 3
    assert responses[0]["error"]["code"] == -32700
    assert responses[1]["result"]["serverInfo"]["name"] == "financial-agent-quant"
    from importlib.metadata import version

    assert responses[1]["result"]["serverInfo"]["version"] == version("financial-agent")
    assert responses[1]["result"]["protocolVersion"] == "2025-03-26"
    assert len(responses[2]["result"]["tools"]) == 5


def test_emergency_stop_survives_broken_journal(config_path: Path) -> None:
    config = TradingConfig.load(config_path)
    config.state_dir.mkdir()
    (config.state_dir / "journal.jsonl").write_text("{}\n")
    assert main(["kill", "--config", str(config_path), "--reason", "emergency"]) == 2
    assert KillSwitch(config.state_dir).engaged()
    assert (
        main(
            [
                "unkill",
                "--config",
                str(config_path),
                "--reason",
                "review",
                "--operator",
                "owner",
            ]
        )
        == 1
    )
    assert KillSwitch(config.state_dir).engaged()


def test_certify_prints_selected_parameters_as_copyable_toml(
    config_path: Path, tmp_path: Path, capsys: Any
) -> None:
    import tomllib

    policy = tmp_path / "policy.toml"
    policy.write_text(
        "[promotion]\ntrain_sessions = 126\ntest_sessions = 63\n"
        "min_oos_sessions = 100\nembargo_sessions = 0\npbo_splits = 4\n"
    )
    cert = tmp_path / "certificate.json"
    result = main(
        [
            "certify",
            "--config",
            str(config_path),
            "--end",
            "2020-06-05",
            "--policy",
            str(policy),
            "--grid",
            '[{"lookbacks":[3,10],"cov_lookback":10,"max_weight":0.25},'
            '{"lookbacks":[3,12],"cov_lookback":10,"max_weight":0.25}]',
            "--output",
            str(cert),
        ]
    )
    assert result in (0, 2)
    output = capsys.readouterr().out
    selected_toml = output.split(
        "Selected strategy parameters (copy into your config):\n"
    )[1]
    strategy = tomllib.loads(selected_toml)["strategy"]
    certificate = json.loads(cert.read_text())
    assert strategy["name"] == certificate["strategy"]
    assert strategy["params"] == certificate["params"]
    assert strategy["params"]["lookbacks"] in ([3, 10], [3, 12])
