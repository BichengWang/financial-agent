import json

from click.testing import CliRunner

from financial_agent.agents.grok import cli as cli_module
from financial_agent.agents.grok.cli import cli
from financial_agent.agents.grok.linear_client import LinearIssue
from financial_agent.agents.grok.workflow import ProcessedIssue


def _full_env() -> dict[str, str]:
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

    runner = CliRunner(env=_full_env())
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


def test_print_playbook_works_without_api_keys() -> None:
    runner = CliRunner(env={"GROK_AGENT_USER_ID": "user-mcp"})
    result = runner.invoke(cli, ["print-playbook"])

    assert result.exit_code == 0, result.output
    assert "user-mcp" in result.output
    assert "<!-- grok-agent-response -->" in result.output


def test_print_playbook_still_needs_trigger() -> None:
    runner = CliRunner(env={})
    result = runner.invoke(cli, ["print-playbook"])
    assert result.exit_code == 2
    assert "GROK_AGENT_USER_ID" in result.output


def test_print_issue_uses_linear_only(monkeypatch) -> None:
    issue = LinearIssue(
        id="iss-1",
        identifier="BIP-9",
        title="Add lunar widget",
        description="please add it",
        state_name="Backlog",
        url="https://linear.app/x/issue/BIP-9",
    )

    class _FakeLinear:
        def __init__(self, api_key, base_url):
            self.api_key = api_key
            self.base_url = base_url

        def fetch_assigned_issues(self, agent_user_id=None, agent_label=None):
            return [issue]

    monkeypatch.setattr(cli_module, "LinearClient", _FakeLinear)

    runner = CliRunner(
        env={
            "LINEAR_API_KEY": "lin_api_test",
            "GROK_AGENT_USER_ID": "user-123",
        }
    )
    result = runner.invoke(cli, ["print-issue", "BIP-9"])

    assert result.exit_code == 0, result.output
    assert "BIP-9 — Add lunar widget" in result.output


def test_print_issue_unknown_id_exits_nonzero(monkeypatch) -> None:
    class _FakeLinear:
        def __init__(self, api_key, base_url):
            pass

        def fetch_assigned_issues(self, agent_user_id=None, agent_label=None):
            return []

    monkeypatch.setattr(cli_module, "LinearClient", _FakeLinear)

    runner = CliRunner(
        env={
            "LINEAR_API_KEY": "lin_api_test",
            "GROK_AGENT_USER_ID": "user-123",
        }
    )
    result = runner.invoke(cli, ["print-issue", "BIP-404"])

    assert result.exit_code == 1
    assert "BIP-404" in result.output
