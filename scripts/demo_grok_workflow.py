"""Local end-to-end demo of the Grok ↔ Linear workflow.

This script does NOT call the real Linear or xAI APIs. It plugs fake
HTTP transports into both clients and prints the JSON traffic that
would have been sent over the wire, plus the final processed-issue
summary.

Run with::

    PYTHONPATH=src python scripts/demo_grok_workflow.py
"""

from __future__ import annotations

import json
from dataclasses import replace

from financial_agent.agents.grok.config import GrokWorkflowConfig
from financial_agent.agents.grok.grok_client import GrokClient
from financial_agent.agents.grok.linear_client import LinearClient
from financial_agent.agents.grok.workflow import GrokWorkflow

_FAKE_GROK_REPLY = """\
**TL;DR** — Wire up a polling loop that turns Linear issue assignments \
into Grok chat-completions calls and posts the result back as a comment.

## Plan
- Add a Linear GraphQL client under `src/financial_agent/agents/grok/`.
- Add a Grok (xAI) chat client (OpenAI-compatible) in the same package.
- Implement an idempotent workflow that polls, prompts, and replies.
- Expose a CLI entry: `python -m financial_agent.agents.grok run-once`.
- Cover the round-trip with mock-based tests under `tests/agents/grok/`.

## Next actions
- Provision a Linear API key + agent user and an xAI API key.
- Decide on cron vs. long-running watcher for deployment.
"""


class _FakeLinearHttp:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict]] = []

    def __call__(self, url, headers, body):
        payload = json.loads(body.decode("utf-8"))
        self.calls.append((url, payload))
        query = payload["query"]
        if "issues(filter:" in query:
            data = {
                "data": {
                    "issues": {
                        "nodes": [
                            {
                                "id": "iss-bip-234",
                                "identifier": "BIP-234",
                                "title": "connect grok for ai workflow",
                                "description": (
                                    "@cursor can you figure out a plan for "
                                    "grok connection and automation? linear "
                                    "assign task, grok finish it."
                                ),
                                "url": ("https://linear.app/x/issue/BIP-234"),
                                "state": {"name": "Backlog"},
                                "comments": {"nodes": []},
                            }
                        ]
                    }
                }
            }
        elif "commentCreate" in query:
            data = {
                "data": {
                    "commentCreate": {
                        "success": True,
                        "comment": {"id": "cmt-demo-1"},
                    }
                }
            }
        else:
            data = {"data": {}}
        return 200, json.dumps(data).encode("utf-8")


class _FakeGrokHttp:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict]] = []

    def __call__(self, url, headers, body):
        payload = json.loads(body.decode("utf-8"))
        self.calls.append((url, payload))
        resp = {
            "id": "chatcmpl-demo",
            "model": payload.get("model"),
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": _FAKE_GROK_REPLY,
                    },
                    "finish_reason": "stop",
                }
            ],
        }
        return 200, json.dumps(resp).encode("utf-8")


def main() -> None:
    base = GrokWorkflowConfig(
        linear_api_key="lin_api_demo",
        xai_api_key="xai_demo",
        agent_user_id="demo-agent",
    )
    config = replace(base, dry_run=False)

    linear_http = _FakeLinearHttp()
    grok_http = _FakeGrokHttp()

    linear = LinearClient(config.linear_api_key, http=linear_http)
    grok = GrokClient(config.xai_api_key, model=config.grok_model, http=grok_http)
    workflow = GrokWorkflow(config, linear=linear, grok=grok)

    results = workflow.run_once()

    print("=== Linear traffic ===")
    for i, (url, payload) in enumerate(linear_http.calls, start=1):
        print(f"[{i}] POST {url}")
        op = payload["query"].splitlines()[0]
        print(f"    op:        {op}")
        print(f"    variables: {payload['variables']}")

    print()
    print("=== Grok traffic ===")
    for i, (url, payload) in enumerate(grok_http.calls, start=1):
        print(f"[{i}] POST {url}")
        print(f"    model:     {payload['model']}")
        print(
            "    messages:  "
            + ", ".join(
                f"{m['role']}({len(m['content'])} chars)" for m in payload["messages"]
            )
        )

    print()
    print("=== Workflow results ===")
    for r in results:
        print(
            f"{r.issue.identifier} → comment={r.posted_comment_id} "
            f"skipped={r.skipped_reason} response_chars={len(r.response)}"
        )

    print()
    print("=== Posted comment body (preview) ===")
    if linear_http.calls:
        for _, payload in linear_http.calls:
            if "commentCreate" in payload["query"]:
                body = payload["variables"]["body"]
                print(body[:600] + ("…" if len(body) > 600 else ""))
                break


if __name__ == "__main__":
    main()
