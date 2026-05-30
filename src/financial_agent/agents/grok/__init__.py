"""Grok ↔ Linear automation for the financial-agent repo.

This package wires Linear (issue tracker) up to Grok in two
interchangeable modes:

* **MCP mode** (preferred when you don't have an xAI API key): drive
  Grok from the iOS app via its Linear MCP connector. This package
  ships the playbook prompt to paste into Grok in
  :func:`render_playbook`.
* **API mode** (when you do have an xAI API key): poll Linear and call
  the xAI chat-completions API directly via :class:`GrokWorkflow`.

The public entry points are:

* :class:`GrokWorkflowConfig` — env-driven config.
* :func:`render_playbook` — render the MCP-mode prompt for the user.
* :class:`LinearClient` — minimal Linear GraphQL client.
* :class:`GrokClient` — minimal xAI chat-completions client.
* :class:`GrokWorkflow` — API-mode orchestration.

See ``README.md`` in this directory for the integration plan.
"""

from .config import ConfigError, GrokWorkflowConfig
from .grok_client import GrokAPIError, GrokClient, GrokMessage
from .linear_client import (
    LinearAPIError,
    LinearClient,
    LinearComment,
    LinearIssue,
)
from .playbook import AGENT_COMMENT_MARKER, render_playbook
from .workflow import GrokWorkflow, ProcessedIssue

__all__ = [
    "AGENT_COMMENT_MARKER",
    "ConfigError",
    "GrokAPIError",
    "GrokClient",
    "GrokMessage",
    "GrokWorkflow",
    "GrokWorkflowConfig",
    "LinearAPIError",
    "LinearClient",
    "LinearComment",
    "LinearIssue",
    "ProcessedIssue",
    "render_playbook",
]
