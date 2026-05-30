"""Minimal Linear GraphQL client used by the Grok automation workflow.

We deliberately avoid pulling in a heavy SDK — Linear's API is a small
GraphQL surface and we only need a handful of operations:

* fetch issues assigned to the agent (or carrying the agent's label),
* read an issue's existing comment thread,
* post a new comment back to the issue,
* optionally move the issue between workflow states.

The client is implemented on top of ``urllib.request`` so the package
keeps zero new runtime dependencies.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

_HttpFn = Callable[[str, dict[str, str], bytes], tuple[int, bytes]]


class LinearAPIError(RuntimeError):
    """Raised when Linear's GraphQL API returns an error."""


@dataclass(frozen=True)
class LinearComment:
    id: str
    body: str
    user_name: str


@dataclass(frozen=True)
class LinearIssue:
    id: str
    identifier: str
    title: str
    description: str
    state_name: str
    url: str
    comments: list[LinearComment] = field(default_factory=list)

    def to_prompt_context(self) -> str:
        """Render the issue as a single text blob for the LLM."""
        lines = [
            f"# {self.identifier} — {self.title}",
            f"State: {self.state_name}",
            f"URL: {self.url}",
            "",
            "## Description",
            self.description.strip() or "(no description)",
        ]
        if self.comments:
            lines.append("")
            lines.append("## Comments")
            for c in self.comments:
                lines.append(f"- **{c.user_name}**: {c.body.strip()}")
        return "\n".join(lines)


_ISSUES_QUERY = """
query GrokAgentIssues($filter: IssueFilter!) {
  issues(filter: $filter, first: 25) {
    nodes {
      id
      identifier
      title
      description
      url
      state { name }
      comments(first: 50) {
        nodes { id body user { name } }
      }
    }
  }
}
""".strip()


_ADD_COMMENT_MUTATION = """
mutation GrokAgentAddComment($issueId: String!, $body: String!) {
  commentCreate(input: { issueId: $issueId, body: $body }) {
    success
    comment { id }
  }
}
""".strip()


_UPDATE_ISSUE_STATE_MUTATION = """
mutation GrokAgentUpdateState($id: String!, $stateId: String!) {
  issueUpdate(id: $id, input: { stateId: $stateId }) {
    success
  }
}
""".strip()


def _default_http(url: str, headers: dict[str, str], body: bytes) -> tuple[int, bytes]:
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


class LinearClient:
    """Tiny GraphQL client for Linear."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.linear.app/graphql",
        http: _HttpFn | None = None,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url
        self._http: _HttpFn = http or _default_http

    def _post(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
        headers = {
            "Authorization": self._api_key,
            "Content-Type": "application/json",
        }
        status, body = self._http(self._base_url, headers, payload)
        if status >= 400:
            raise LinearAPIError(
                f"Linear API HTTP {status}: {body.decode('utf-8', 'replace')}"
            )
        try:
            data = json.loads(body.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise LinearAPIError(f"Invalid JSON from Linear: {body!r}") from exc
        if data.get("errors"):
            raise LinearAPIError(f"Linear API errors: {data['errors']}")
        result = data.get("data") or {}
        if not isinstance(result, dict):
            raise LinearAPIError(f"Unexpected Linear payload: {data}")
        return result

    def fetch_assigned_issues(
        self,
        agent_user_id: str | None = None,
        agent_label: str | None = None,
        exclude_state_names: Iterable[str] = ("Done", "Canceled"),
    ) -> list[LinearIssue]:
        """Fetch issues that the Grok agent should pick up.

        At least one of ``agent_user_id`` or ``agent_label`` must be
        provided. If both are given they are AND-combined.
        """
        if not agent_user_id and not agent_label:
            raise ValueError("agent_user_id or agent_label must be provided")

        filter_: dict[str, Any] = {}
        if agent_user_id:
            filter_["assignee"] = {"id": {"eq": agent_user_id}}
        if agent_label:
            filter_["labels"] = {"name": {"eq": agent_label}}
        excluded = list(exclude_state_names)
        if excluded:
            filter_["state"] = {"name": {"nin": excluded}}

        data = self._post(_ISSUES_QUERY, {"filter": filter_})
        nodes = (data.get("issues") or {}).get("nodes") or []
        return [_parse_issue(n) for n in nodes]

    def add_comment(self, issue_id: str, body: str) -> str:
        """Post a comment on an issue. Returns the new comment ID."""
        data = self._post(_ADD_COMMENT_MUTATION, {"issueId": issue_id, "body": body})
        result = data.get("commentCreate") or {}
        if not result.get("success"):
            raise LinearAPIError(f"commentCreate failed: {data}")
        return ((result.get("comment") or {}).get("id")) or ""

    def update_issue_state(self, issue_id: str, state_id: str) -> None:
        """Move an issue into a different workflow state."""
        data = self._post(
            _UPDATE_ISSUE_STATE_MUTATION,
            {"id": issue_id, "stateId": state_id},
        )
        result = data.get("issueUpdate") or {}
        if not result.get("success"):
            raise LinearAPIError(f"issueUpdate failed: {data}")


def _parse_issue(node: dict[str, Any]) -> LinearIssue:
    comments_node = (node.get("comments") or {}).get("nodes") or []
    comments = [
        LinearComment(
            id=c.get("id", ""),
            body=c.get("body", "") or "",
            user_name=((c.get("user") or {}).get("name") or "unknown"),
        )
        for c in comments_node
    ]
    return LinearIssue(
        id=node.get("id", ""),
        identifier=node.get("identifier", ""),
        title=node.get("title", "") or "",
        description=node.get("description", "") or "",
        state_name=((node.get("state") or {}).get("name") or "Unknown"),
        url=node.get("url", "") or "",
        comments=comments,
    )
