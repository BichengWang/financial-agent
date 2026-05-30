"""Orchestration for the Linear → Grok → Linear automation loop.

High-level flow per polling iteration:

1. Query Linear for issues assigned to the Grok agent (or carrying the
   configured trigger label) that are not yet ``Done``/``Canceled``.
2. Skip any issue whose latest comment was already posted by the agent
   (so we don't double-respond on the same input).
3. For each remaining issue, build a prompt, call Grok, and post the
   response back as a Linear comment, optionally moving the issue
   between workflow states.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Callable, Iterator

from .config import GrokWorkflowConfig
from .grok_client import GrokClient, GrokMessage
from .linear_client import LinearClient, LinearIssue
from .playbook import AGENT_COMMENT_MARKER as _AGENT_COMMENT_MARKER
from .prompts import SYSTEM_PROMPT, build_user_message

_LOG = logging.getLogger("financial_agent.agents.grok")


@dataclass(frozen=True)
class ProcessedIssue:
    """Outcome of processing a single Linear issue."""

    issue: LinearIssue
    response: str
    posted_comment_id: str
    skipped_reason: str | None = None


def _already_responded(issue: LinearIssue) -> bool:
    for comment in reversed(issue.comments):
        if _AGENT_COMMENT_MARKER in comment.body:
            return True
    return False


def _format_response_comment(response: str) -> str:
    return f"{_AGENT_COMMENT_MARKER}\n{response.strip()}\n"


class GrokWorkflow:
    """Glue between :class:`LinearClient` and :class:`GrokClient`."""

    def __init__(
        self,
        config: GrokWorkflowConfig,
        linear: LinearClient | None = None,
        grok: GrokClient | None = None,
    ) -> None:
        self._config = config
        self._linear = linear or LinearClient(
            api_key=config.linear_api_key, base_url=config.linear_base_url
        )
        self._grok = grok or GrokClient(
            api_key=config.xai_api_key,
            model=config.grok_model,
            base_url=config.grok_base_url,
        )

    def process_issue(self, issue: LinearIssue) -> ProcessedIssue:
        """Run the LLM and post a response on a single issue."""
        if _already_responded(issue):
            _LOG.info("Skipping %s: agent has already responded", issue.identifier)
            return ProcessedIssue(
                issue=issue,
                response="",
                posted_comment_id="",
                skipped_reason="already_responded",
            )

        if self._config.dry_run:
            _LOG.info("[dry-run] Would call Grok for %s", issue.identifier)
            return ProcessedIssue(
                issue=issue,
                response="",
                posted_comment_id="",
                skipped_reason="dry_run",
            )

        if self._config.in_progress_state_id:
            try:
                self._linear.update_issue_state(
                    issue.id, self._config.in_progress_state_id
                )
            except Exception:  # pragma: no cover - logged + non-fatal
                _LOG.exception(
                    "Could not transition %s to in-progress state",
                    issue.identifier,
                )

        messages = [
            GrokMessage(role="system", content=SYSTEM_PROMPT),
            GrokMessage(
                role="user",
                content=build_user_message(issue.to_prompt_context()),
            ),
        ]
        response = self._grok.chat_completion(messages)
        comment_id = self._linear.add_comment(
            issue.id, _format_response_comment(response)
        )

        if self._config.done_state_id:
            try:
                self._linear.update_issue_state(issue.id, self._config.done_state_id)
            except Exception:  # pragma: no cover - logged + non-fatal
                _LOG.exception(
                    "Could not transition %s to done state", issue.identifier
                )

        return ProcessedIssue(
            issue=issue, response=response, posted_comment_id=comment_id
        )

    def run_once(self) -> list[ProcessedIssue]:
        """Run a single poll → process pass and return all outcomes."""
        issues = self._linear.fetch_assigned_issues(
            agent_user_id=self._config.agent_user_id,
            agent_label=self._config.agent_label,
        )
        _LOG.info("Fetched %d issue(s) for the Grok agent", len(issues))
        results: list[ProcessedIssue] = []
        for issue in issues:
            try:
                results.append(self.process_issue(issue))
            except Exception:
                _LOG.exception("Failed to process %s", issue.identifier)
        return results

    def run_forever(
        self,
        sleep: Callable[[float], None] | None = None,
    ) -> Iterator[list[ProcessedIssue]]:
        """Yield results from successive ``run_once`` calls.

        Stops after ``config.max_iterations`` iterations, or runs forever
        when that is ``0``.
        """
        sleep_fn = sleep or time.sleep
        i = 0
        while True:
            yield self.run_once()
            i += 1
            if self._config.max_iterations and i >= self._config.max_iterations:
                return
            sleep_fn(self._config.poll_interval_seconds)
