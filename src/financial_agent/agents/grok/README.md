# Grok ↔ Linear automation

This package implements the **"Linear assigns a task, Grok finishes it"**
workflow that BIP-234 (and its parent BIP-41) calls for.

Two modes are supported, picked by which credentials you have:

| Mode | Trigger | Where Grok runs | What this package gives you |
| --- | --- | --- | --- |
| **MCP mode** *(recommended for users without an xAI API key)* | You ask Grok in the iOS app to "check Linear" | Inside the Grok iOS app, using its built-in **Linear MCP connector** | A version-controlled **playbook prompt** to paste into Grok, plus a CLI to print it |
| **API mode** | A scheduled poll (cron / GitHub Actions / container) | This repo, calling the xAI chat-completions API | A full Linear ↔ Grok orchestration loop with idempotency |

```
                      ┌──────────────┐
       (no API key)   │  Grok iOS    │  MCP   ┌────────┐
       ───────────▶   │  app +       │ ─────▶ │ Linear │   MCP mode
                      │  playbook    │ ◀───── │  API   │
                      └──────────────┘        └────────┘

       (XAI_API_KEY)  ┌──────────────┐ GraphQL┌────────┐
       ───────────▶   │ GrokWorkflow │ ─────▶ │ Linear │   API mode
                      │ (this repo)  │ ◀───── │  API   │
                      │              │  REST  ┌────────┐
                      │              │ ─────▶ │  xAI   │
                      └──────────────┘ ◀───── │  Grok  │
                                              └────────┘
```

Both modes use the same idempotency convention: every reply Grok posts
back to Linear is prefixed with the hidden HTML marker
`<!-- grok-agent-response -->`. Re-runs (yours or another agent's)
detect that marker and skip the issue.

---

## MCP mode (no xAI API key needed)

You already have this set up if you have:

1. A Linear API key configured inside an MCP server (Linear ships an
   official MCP, e.g. `https://mcp.linear.app/sse`, and there are
   community servers as well).
2. That MCP server registered inside the Grok iOS app's connector
   settings.

### One-time setup

Set just enough config so the playbook knows which issues are yours:

```shell
export GROK_AGENT_USER_ID="…linear-user-id…"   # OR
export GROK_AGENT_LABEL="grok"
```

Then print the playbook prompt and paste it into Grok in the iOS app.
You can save it as a custom persona / system prompt, or just paste it
at the top of a chat session:

```shell
python -m financial_agent.agents.grok print-playbook
```

The output is a Markdown prompt that tells Grok exactly how to:

* filter Linear issues by your agent user ID / label,
* skip anything already containing the idempotency marker,
* compose a structured Markdown reply (`TL;DR` / `Plan` /
  `Next actions`) that respects this repo's conventions,
* post the reply via the Linear MCP `create_comment` tool.

### Day-to-day use

Once the playbook is loaded, simply tell Grok in the app:

> Check Linear.

Grok then uses its Linear MCP connector to list your eligible issues,
process each one, and reply in the chat with a summary of what it did.

If you want to nudge Grok about a specific issue without round-tripping
through MCP, you can copy a single issue's context from the CLI (this
needs `LINEAR_API_KEY` but **not** an xAI key):

```shell
export LINEAR_API_KEY=lin_api_…
python -m financial_agent.agents.grok print-issue BIP-234
```

…and paste the output into Grok directly.

---

## API mode (when you do have an xAI API key)

This is the fully-automated loop; no human needs to be in the chat.

### Configuration

Required:

| Variable | Purpose |
| --- | --- |
| `LINEAR_API_KEY` | Linear personal API key (`lin_api_…`). |
| `XAI_API_KEY` | xAI API key for Grok. |
| `GROK_AGENT_USER_ID` *or* `GROK_AGENT_LABEL` | Picks which issues to claim. |

Optional (with defaults):

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

### Run

```shell
# Cron / Lambda style:
python -m financial_agent.agents.grok run-once

# Long-running watcher:
python -m financial_agent.agents.grok watch --interval 60
```

Or from Python:

```python
from financial_agent.agents.grok import GrokWorkflow, GrokWorkflowConfig

config = GrokWorkflowConfig.from_env()
workflow = GrokWorkflow(config)
results = workflow.run_once()
```

---

## Module map

| Module | Purpose |
| --- | --- |
| `playbook.py` | MCP-mode prompt rendered with your trigger filter. |
| `prompts.py` | API-mode system prompt sent on every Grok call. |
| `config.py` | Env-driven config; API keys are individually optional. |
| `linear_client.py` | Minimal Linear GraphQL client (stdlib only). |
| `grok_client.py` | Minimal xAI chat-completions client (stdlib only). |
| `workflow.py` | API-mode orchestrator (`run_once`, `run_forever`). |
| `cli.py`, `__main__.py` | `python -m financial_agent.agents.grok …` entry. |

## Testing

Both clients accept a pluggable `http` callable returning
`(status_code, raw_bytes)`, so the entire workflow is unit-testable
without network access. See [`tests/agents/grok/`](../../../../tests/agents/grok)
for the included tests; see also
[`scripts/demo_grok_workflow.py`](../../../../scripts/demo_grok_workflow.py)
for an end-to-end mocked roundtrip.

## Plan / next actions

* **MCP mode** is ready for you to use today: just print the playbook
  and paste it into Grok in the iOS app.
* If/when an xAI API key becomes available, the same module switches
  to **API mode** with no code changes — just set `XAI_API_KEY` and
  schedule `run-once`.
* Future extensions (out of scope for the initial PR): a Linear
  webhook receiver, repo-write capability for issues tagged
  `grok-can-code`, and task-specific prompt templates wired into
  `financial_agent.trading.*`.
