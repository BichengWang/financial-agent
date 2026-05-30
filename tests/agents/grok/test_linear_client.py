import json

import pytest

from financial_agent.agents.grok.linear_client import (
    LinearAPIError,
    LinearClient,
)


class _FakeHttp:
    def __init__(self, responses: list[tuple[int, dict]]):
        self.responses = list(responses)
        self.calls: list[tuple[str, dict[str, str], dict]] = []

    def __call__(
        self, url: str, headers: dict[str, str], body: bytes
    ) -> tuple[int, bytes]:
        payload = json.loads(body.decode("utf-8"))
        self.calls.append((url, headers, payload))
        status, resp = self.responses.pop(0)
        return status, json.dumps(resp).encode("utf-8")


def _issue_node(
    iid: str = "iss-1",
    identifier: str = "BIP-1",
    title: str = "Demo",
    description: str = "Demo desc",
    state: str = "Backlog",
    comments: list[dict] | None = None,
) -> dict:
    return {
        "id": iid,
        "identifier": identifier,
        "title": title,
        "description": description,
        "url": f"https://linear.app/x/issue/{identifier}",
        "state": {"name": state},
        "comments": {"nodes": comments or []},
    }


def test_fetch_assigned_issues_by_user_id() -> None:
    http = _FakeHttp(
        [
            (
                200,
                {
                    "data": {
                        "issues": {
                            "nodes": [
                                _issue_node(
                                    comments=[
                                        {
                                            "id": "c1",
                                            "body": "first",
                                            "user": {"name": "alice"},
                                        }
                                    ]
                                )
                            ]
                        }
                    }
                },
            )
        ]
    )
    client = LinearClient("key", http=http)
    issues = client.fetch_assigned_issues(agent_user_id="user-9")
    assert len(issues) == 1
    issue = issues[0]
    assert issue.identifier == "BIP-1"
    assert issue.comments[0].user_name == "alice"

    url, headers, payload = http.calls[0]
    assert headers["Authorization"] == "key"
    assert payload["variables"]["filter"] == {
        "assignee": {"id": {"eq": "user-9"}},
        "state": {"name": {"nin": ["Done", "Canceled"]}},
    }


def test_fetch_assigned_issues_requires_filter() -> None:
    client = LinearClient("key", http=_FakeHttp([]))
    with pytest.raises(ValueError):
        client.fetch_assigned_issues()


def test_fetch_assigned_issues_combines_user_and_label() -> None:
    http = _FakeHttp([(200, {"data": {"issues": {"nodes": []}}})])
    client = LinearClient("key", http=http)
    client.fetch_assigned_issues(agent_user_id="u1", agent_label="grok")
    payload = http.calls[0][2]
    assert payload["variables"]["filter"]["assignee"] == {"id": {"eq": "u1"}}
    assert payload["variables"]["filter"]["labels"] == {"name": {"eq": "grok"}}


def test_add_comment_returns_id() -> None:
    http = _FakeHttp(
        [
            (
                200,
                {
                    "data": {
                        "commentCreate": {
                            "success": True,
                            "comment": {"id": "c-99"},
                        }
                    }
                },
            )
        ]
    )
    client = LinearClient("key", http=http)
    cid = client.add_comment("iss-1", "hello")
    assert cid == "c-99"
    payload = http.calls[0][2]
    assert payload["variables"] == {"issueId": "iss-1", "body": "hello"}


def test_add_comment_failure_raises() -> None:
    http = _FakeHttp([(200, {"data": {"commentCreate": {"success": False}}})])
    client = LinearClient("key", http=http)
    with pytest.raises(LinearAPIError):
        client.add_comment("iss-1", "hello")


def test_http_error_status_raises() -> None:
    http = _FakeHttp([(500, {"errors": "boom"})])
    client = LinearClient("key", http=http)
    with pytest.raises(LinearAPIError, match="HTTP 500"):
        client.fetch_assigned_issues(agent_user_id="u")


def test_graphql_errors_field_raises() -> None:
    http = _FakeHttp([(200, {"errors": [{"message": "bad"}], "data": None})])
    client = LinearClient("key", http=http)
    with pytest.raises(LinearAPIError, match="errors"):
        client.fetch_assigned_issues(agent_user_id="u")


def test_update_issue_state_ok() -> None:
    http = _FakeHttp([(200, {"data": {"issueUpdate": {"success": True}}})])
    client = LinearClient("key", http=http)
    client.update_issue_state("iss-1", "state-1")
    payload = http.calls[0][2]
    assert payload["variables"] == {"id": "iss-1", "stateId": "state-1"}
