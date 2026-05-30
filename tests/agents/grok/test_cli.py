import json

from click.testing import CliRunner

from financial_agent.agents.grok import cli as cli_module
from financial_agent.agents.grok.cli import cli
from financial_agent.agents.grok.linear_client import LinearIssue
from financial_agent.agents.grok.workflow import ProcessedIssue


def _env() -> dict[str, str]:
    return {
        "LINEAR_API_KEY": "lin_api_test",
        "XAI_API_KEY": "xai_test",
        "GROK_AGENT_USER_ID": "user-123",
    }


def test_run_once_command(monkeypatch) -> None:
    issue = LinearIssue(
        id="iss-1",
        identifier="BIP-1",
        title="t",
        description="d",
        state_name="Backlog",
        url="u",
    )
    fake_results = [
        ProcessedIssue(
            issue=issue,
            response="hello",
            posted_comment_id="c-1",
        )
    ]

    class _FakeWorkflow:
        def __init__(self, config):
            self.config = config

        def run_once(self):
            return fake_results

    monkeypatch.setattr(cli_module, "GrokWorkflow", _FakeWorkflow)

    runner = CliRunner(env=_env())
    result = runner.invoke(cli, ["run-once"])

    assert result.exit_code == 0, result.output
    parsed = json.loads(result.output)
    assert parsed[0]["issue"] == "BIP-1"
    assert parsed[0]["comment_id"] == "c-1"
    assert parsed[0]["response_chars"] == 5


def test_missing_config_exits_nonzero() -> None:
    runner = CliRunner(env={})
    result = runner.invoke(cli, ["run-once"])
    assert result.exit_code == 2
    assert "Configuration error" in result.output
