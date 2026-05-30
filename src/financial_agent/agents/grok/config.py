"""Configuration for the Grok ↔ Linear automation workflow.

All values are loaded from environment variables so credentials and
deployment-specific settings stay out of the source tree.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping

_DEFAULT_GROK_MODEL = "grok-4-latest"
_DEFAULT_GROK_BASE_URL = "https://api.x.ai/v1"
_DEFAULT_LINEAR_BASE_URL = "https://api.linear.app/graphql"


class ConfigError(RuntimeError):
    """Raised when required configuration is missing."""


@dataclass(frozen=True)
class GrokWorkflowConfig:
    """Runtime configuration for the Grok automation loop.

    Attributes:
        linear_api_key: Linear personal API key (``lin_api_…``). Optional;
            only required when actually talking to Linear from this code
            (``run-once`` / ``watch`` / ``print-issue``).
        xai_api_key: xAI API key used to call Grok. Optional; only the
            API-driven path (``run-once`` / ``watch``) needs it. If you
            drive Grok from the iOS app via its Linear MCP connector
            instead, leave this blank and use ``print-playbook``.
        agent_user_id: The Linear user ID that represents the Grok agent.
            Issues assigned to this user are picked up by the workflow.
            If unset, ``agent_label`` is used instead.
        agent_label: A Linear label name (e.g. ``grok``) used as a fallback
            trigger when ``agent_user_id`` is not set.
        in_progress_state_id: Optional workflow-state ID to move issues to
            when the agent starts working on them.
        done_state_id: Optional workflow-state ID to move issues to when
            the agent finishes.
        grok_model: xAI model name. Defaults to ``grok-4-latest``.
        grok_base_url: xAI API base URL.
        linear_base_url: Linear GraphQL endpoint URL.
        poll_interval_seconds: Seconds to wait between polls when running
            in ``--watch`` mode.
        max_iterations: Maximum number of poll iterations in watch mode.
            ``0`` means "run forever".
        dry_run: If True, the workflow logs its planned actions but does
            not call Grok or write back to Linear.
    """

    linear_api_key: str = ""
    xai_api_key: str = ""
    agent_user_id: str | None = None
    agent_label: str | None = None
    in_progress_state_id: str | None = None
    done_state_id: str | None = None
    grok_model: str = _DEFAULT_GROK_MODEL
    grok_base_url: str = _DEFAULT_GROK_BASE_URL
    linear_base_url: str = _DEFAULT_LINEAR_BASE_URL
    poll_interval_seconds: float = 60.0
    max_iterations: int = 0
    dry_run: bool = False

    @classmethod
    def from_env(
        cls,
        env: Mapping[str, str] | None = None,
        *,
        require_linear: bool = True,
        require_xai: bool = True,
    ) -> "GrokWorkflowConfig":
        """Build a config from environment variables.

        At least one of ``GROK_AGENT_USER_ID`` or ``GROK_AGENT_LABEL`` must
        be set so the workflow knows which issues to claim.

        ``require_linear`` and ``require_xai`` control which API keys
        must be present. The MCP-driven path (``print-playbook``) does
        not need either, the linear-only path (``print-issue``) needs
        only Linear, and the API-driven path (``run-once`` / ``watch``)
        needs both.
        """
        source: Mapping[str, str] = env if env is not None else os.environ

        linear_key = source.get("LINEAR_API_KEY", "").strip()
        xai_key = source.get("XAI_API_KEY", "").strip()
        if require_linear and not linear_key:
            raise ConfigError("LINEAR_API_KEY is not set")
        if require_xai and not xai_key:
            raise ConfigError("XAI_API_KEY is not set")

        agent_user_id = source.get("GROK_AGENT_USER_ID", "").strip() or None
        agent_label = source.get("GROK_AGENT_LABEL", "").strip() or None
        if not agent_user_id and not agent_label:
            raise ConfigError(
                "Set either GROK_AGENT_USER_ID or GROK_AGENT_LABEL so the "
                "workflow knows which Linear issues to claim."
            )

        return cls(
            linear_api_key=linear_key,
            xai_api_key=xai_key,
            agent_user_id=agent_user_id,
            agent_label=agent_label,
            in_progress_state_id=source.get("GROK_IN_PROGRESS_STATE_ID") or None,
            done_state_id=source.get("GROK_DONE_STATE_ID") or None,
            grok_model=source.get("GROK_MODEL", _DEFAULT_GROK_MODEL),
            grok_base_url=source.get("GROK_BASE_URL", _DEFAULT_GROK_BASE_URL),
            linear_base_url=source.get("LINEAR_BASE_URL", _DEFAULT_LINEAR_BASE_URL),
            poll_interval_seconds=float(source.get("GROK_POLL_INTERVAL_SECONDS", "60")),
            max_iterations=int(source.get("GROK_MAX_ITERATIONS", "0")),
            dry_run=source.get("GROK_DRY_RUN", "").lower() in {"1", "true", "yes"},
        )
