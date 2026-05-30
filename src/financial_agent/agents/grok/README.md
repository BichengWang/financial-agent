# Grok ↔ Linear automation

This package implements the **"Linear assigns a task, Grok finishes it"**
workflow that BIP-234 (and its parent BIP-41) calls for.

```
┌──────────┐    assign     ┌──────────────────┐    GraphQL    ┌────────┐
│  Linear  │  ───────────▶ │ GrokWorkflow     │  ──────────▶  │ Linear │
│  Issue   │               │ (this package)   │               │  API   │
└──────────┘               │                  │  ──────────▶  └────────┘
                           │  build prompt    │   chat        ┌────────┐
                           │  call Grok       │  ──────────▶  │  xAI   │
                           │  post comment    │  ◀──────────  │ Grok   │
                           └──────────────────┘               └────────┘
```

## How it works

1. **Trigger.** A human assigns a Linear issue to the dedicated *Grok
   agent* user (or applies the configured trigger label such as
   `grok`). The workflow polls Linear on an interval; no inbound
   webhook is required.
2. **Fetch.** `LinearClient.fetch_assigned_issues` runs a single
   GraphQL query that filters by `assignee.id` and/or `labels.name` and
   excludes already-`Done`/`Canceled` issues. It also pulls the
   existing comment thread.
3. **Idempotency.** Each agent reply is wrapped in a hidden HTML
   marker (`<!-- grok-agent-response -->`). Before responding, the
   workflow scans the comment thread for that marker and skips the
   issue if it already replied — so re-runs and overlapping pollers
   don't double-post.
4. **(Optional) state transition.** If `GROK_IN_PROGRESS_STATE_ID` is
   set the issue is moved into "In Progress" before the LLM call, and
   into `GROK_DONE_STATE_ID` afterwards.
5. **LLM call.** `GrokClient` calls
   `POST {GROK_BASE_URL}/chat/completions` against the OpenAI-compatible
   xAI API (default model `grok-4-latest`) with the system prompt in
   [`prompts.py`](./prompts.py) and the issue context as the user
   message.
6. **Reply.** The model's text is posted back as a comment on the
   issue via `commentCreate`.

## Configuration

All configuration is read from environment variables. The minimum
required set is:

| Variable | Purpose |
| --- | --- |
| `LINEAR_API_KEY` | Linear personal API key (`lin_api_…`). |
| `XAI_API_KEY` | xAI API key for Grok. |
| `GROK_AGENT_USER_ID` *or* `GROK_AGENT_LABEL` | Picks which issues to claim. |

Optional knobs (with defaults):

| Variable | Default | Notes |
| --- | --- | --- |
| `GROK_MODEL` | `grok-4-latest` | xAI model name. |
| `GROK_BASE_URL` | `https://api.x.ai/v1` | xAI base URL. |
| `LINEAR_BASE_URL` | `https://api.linear.app/graphql` | Linear endpoint. |
| `GROK_POLL_INTERVAL_SECONDS` | `60` | Seconds between polls in `watch` mode. |
| `GROK_MAX_ITERATIONS` | `0` (forever) | Stop after N polls. |
| `GROK_IN_PROGRESS_STATE_ID` | unset | If set, move issue here on start. |
| `GROK_DONE_STATE_ID` | unset | If set, move issue here on finish. |
| `GROK_DRY_RUN` | unset | When truthy, skip Grok + Linear writes. |

## Usage

```shell
# Run a single batch and exit (good for cron / Lambda):
uv run python -m financial_agent.agents.grok run-once

# Long-running watcher:
uv run python -m financial_agent.agents.grok watch --interval 60
```

You can also drive it from Python:

```python
from financial_agent.agents.grok import GrokWorkflow, GrokWorkflowConfig

config = GrokWorkflowConfig.from_env()
workflow = GrokWorkflow(config)
results = workflow.run_once()
```

## Deployment options

The workflow is designed so the same code can run in any of these
shapes:

* **GitHub Actions cron** — schedule `python -m financial_agent.agents.grok run-once`
  every few minutes; idempotency comes from the comment marker, so a
  missed or duplicate run is harmless.
* **Long-running container** — `watch` mode for low-latency response.
* **Local dev** — set the env vars in a `.env` and run `run-once` to
  smoke test end-to-end.

## Testing

Both clients accept a pluggable `http` callable that returns
`(status_code, raw_bytes)`, so the entire workflow is unit-testable
without network access. See [`tests/agents/grok/`](../../../../tests/agents/grok)
for the included tests, which fake both APIs and assert the round-trip
behavior (issue fetched → Grok called → comment posted).

## Plan / next actions

This module covers the connection plumbing requested in BIP-234. Likely
follow-ups:

* Hook the workflow into the existing trading code paths so Grok can
  call into `financial_agent.trading.*` for repo-aware research tasks.
* Add a webhook receiver as a faster alternative to polling.
* Extend `prompts.py` with task-specific templates (e.g. backtest
  request, dataset request).
* Wire repo-write capability (PR creation) for issues tagged
  `grok-can-code`.
