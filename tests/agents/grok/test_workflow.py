from dataclasses import replace

from financial_agent.agents.grok.config import GrokWorkflowConfig
from financial_agent.agents.grok.linear_client import (
    LinearComment,
    LinearIssue,
)
from financial_agent.agents.grok.workflow import (
    GrokWorkflow,
    _AGENT_COMMENT_MARKER,
)


class _FakeLinear:
    def __init__(self, issues: list[LinearIssue]):
        self.issues = list(issues)
        self.added_comments: list[tuple[str, str]] = []
        self.state_updates: list[tuple[str, str]] = []

    def fetch_assigned_issues(
        self, agent_user_id=None, agent_label=None
    ) -> list[LinearIssue]:
        return list(self.issues)

    def add_comment(self, issue_id: str, body: str) -> str:
        self.added_comments.append((issue_id, body))
        return f"comment-{len(self.added_comments)}"

    def update_issue_state(self, issue_id: str, state_id: str) -> None:
        self.state_updates.append((issue_id, state_id))


class _FakeGrok:
    def __init__(self, response: str = "Grok says hi"):
        self.response = response
        self.calls: list[list] = []

    def chat_completion(self, messages, temperature: float = 0.2) -> str:
        self.calls.append([m.to_dict() for m in messages])
        return self.response


def _config(**kwargs) -> GrokWorkflowConfig:
    base = GrokWorkflowConfig(
        linear_api_key="L",
        xai_api_key="X",
        agent_user_id="u",
    )
    return replace(base, **kwargs)


def _issue(comments: list[LinearComment] | None = None) -> LinearIssue:
    return LinearIssue(
        id="iss-1",
        identifier="BIP-7",
        title="Add foo",
        description="Please add foo to the trading env.",
        state_name="Backlog",
        url="https://linear.app/x/issue/BIP-7",
        comments=comments or [],
    )


def test_run_once_calls_grok_and_posts_comment() -> None:
    issue = _issue()
    fake_linear = _FakeLinear([issue])
    fake_grok = _FakeGrok(response="OK plan here")
    workflow = GrokWorkflow(_config(), linear=fake_linear, grok=fake_grok)

    results = workflow.run_once()

    assert len(results) == 1
    res = results[0]
    assert res.skipped_reason is None
    assert res.posted_comment_id == "comment-1"
    assert res.response == "OK plan here"

    assert len(fake_grok.calls) == 1
    msgs = fake_grok.calls[0]
    assert msgs[0]["role"] == "system"
    assert "BIP-7" in msgs[1]["content"]

    assert len(fake_linear.added_comments) == 1
    issue_id, body = fake_linear.added_comments[0]
    assert issue_id == "iss-1"
    assert _AGENT_COMMENT_MARKER in body
    assert "OK plan here" in body


def test_run_once_skips_already_responded_issues() -> None:
    prior = LinearComment(
        id="c1",
        body=f"{_AGENT_COMMENT_MARKER}\nold reply",
        user_name="grok-bot",
    )
    issue = _issue(comments=[prior])
    fake_linear = _FakeLinear([issue])
    fake_grok = _FakeGrok()
    workflow = GrokWorkflow(_config(), linear=fake_linear, grok=fake_grok)

    results = workflow.run_once()

    assert results[0].skipped_reason == "already_responded"
    assert fake_grok.calls == []
    assert fake_linear.added_comments == []


def test_dry_run_skips_writes() -> None:
    fake_linear = _FakeLinear([_issue()])
    fake_grok = _FakeGrok()
    workflow = GrokWorkflow(_config(dry_run=True), linear=fake_linear, grok=fake_grok)

    results = workflow.run_once()

    assert results[0].skipped_reason == "dry_run"
    assert fake_grok.calls == []
    assert fake_linear.added_comments == []


def test_state_transitions_when_configured() -> None:
    fake_linear = _FakeLinear([_issue()])
    fake_grok = _FakeGrok()
    workflow = GrokWorkflow(
        _config(in_progress_state_id="s-prog", done_state_id="s-done"),
        linear=fake_linear,
        grok=fake_grok,
    )

    workflow.run_once()

    assert fake_linear.state_updates == [
        ("iss-1", "s-prog"),
        ("iss-1", "s-done"),
    ]


def test_run_forever_respects_max_iterations() -> None:
    fake_linear = _FakeLinear([])
    fake_grok = _FakeGrok()
    cfg = _config(max_iterations=3, poll_interval_seconds=0.0)
    workflow = GrokWorkflow(cfg, linear=fake_linear, grok=fake_grok)

    sleeps: list[float] = []

    batches = list(workflow.run_forever(sleep=sleeps.append))

    assert len(batches) == 3
    assert sleeps == [0.0, 0.0]


def test_one_failing_issue_does_not_block_others() -> None:
    issues = [_issue(), _issue()]
    issues[1] = LinearIssue(
        id="iss-2",
        identifier="BIP-8",
        title="Other",
        description="Other desc",
        state_name="Backlog",
        url="https://linear.app/x/issue/BIP-8",
    )
    fake_linear = _FakeLinear(issues)

    class _Boom:
        def __init__(self) -> None:
            self.calls = 0

        def chat_completion(self, messages, temperature: float = 0.2) -> str:
            self.calls += 1
            if self.calls == 1:
                raise RuntimeError("first one always fails")
            return "second works"

    fake_grok = _Boom()
    workflow = GrokWorkflow(_config(), linear=fake_linear, grok=fake_grok)

    results = workflow.run_once()

    assert len(results) == 1
    assert results[0].response == "second works"
    assert fake_linear.added_comments[0][0] == "iss-2"
