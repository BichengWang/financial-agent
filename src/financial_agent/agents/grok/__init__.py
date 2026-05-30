"""Grok ↔ Linear automation for the financial-agent repo.

This package wires Linear (issue tracker) up to xAI Grok so a human can
assign an issue to the Grok agent in Linear and have Grok respond
automatically.

The public entry points are:

* :class:`GrokWorkflowConfig` — env-driven config.
* :class:`LinearClient` — minimal Linear GraphQL client.
* :class:`GrokClient` — minimal xAI chat-completions client.
* :class:`GrokWorkflow` — orchestration.

See ``README.md`` in this directory for the integration plan.
"""

from .config import ConfigError, GrokWorkflowConfig
from .grok_client import GrokClient, GrokMessage, GrokAPIError
from .linear_client import (
    LinearAPIError,
    LinearClient,
    LinearComment,
    LinearIssue,
)
from .workflow import GrokWorkflow, ProcessedIssue

__all__ = [
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
]
