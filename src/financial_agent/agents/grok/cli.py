"""Command-line entry point for the Grok ↔ Linear workflow.

Usage::

    # MCP mode (no API keys needed) — print the playbook for the Grok app:
    python -m financial_agent.agents.grok print-playbook

    # Linear-only mode (LINEAR_API_KEY only) — fetch one issue's context:
    python -m financial_agent.agents.grok print-issue BIP-234

    # API mode (LINEAR_API_KEY + XAI_API_KEY) — automated loop:
    python -m financial_agent.agents.grok run-once
    python -m financial_agent.agents.grok watch --interval 60
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Callable

import click

from .config import ConfigError, GrokWorkflowConfig
from .linear_client import LinearClient
from .playbook import render_playbook
from .workflow import GrokWorkflow, ProcessedIssue

_LoadConfig = Callable[..., GrokWorkflowConfig]


def _format_summary(results: list[ProcessedIssue]) -> str:
    summary = []
    for r in results:
        line = {
            "issue": r.issue.identifier,
            "title": r.issue.title,
            "skipped": r.skipped_reason,
            "comment_id": r.posted_comment_id,
            "response_chars": len(r.response),
        }
        summary.append(line)
    return json.dumps(summary, indent=2)


def _exit_on_config_error(load: Callable[[], GrokWorkflowConfig]) -> GrokWorkflowConfig:
    try:
        return load()
    except ConfigError as exc:
        click.echo(f"Configuration error: {exc}", err=True)
        sys.exit(2)


@click.group(help="Linear ↔ Grok automation for the financial-agent repo.")
@click.option("-v", "--verbose", is_flag=True, help="Enable debug logging.")
@click.pass_context
def cli(ctx: click.Context, verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    def _load(
        require_linear: bool = True, require_xai: bool = True
    ) -> GrokWorkflowConfig:
        return _exit_on_config_error(
            lambda: GrokWorkflowConfig.from_env(
                require_linear=require_linear, require_xai=require_xai
            )
        )

    ctx.obj = _load


@cli.command(
    "print-playbook",
    help=(
        "Print the Grok-app playbook prompt to paste into Grok's iOS app. "
        "Use this when you don't have an XAI_API_KEY but have connected the "
        "Grok app to Linear via MCP. Needs only GROK_AGENT_USER_ID or "
        "GROK_AGENT_LABEL — no API keys required."
    ),
)
@click.pass_obj
def print_playbook(load_config: _LoadConfig) -> None:
    config = load_config(require_linear=False, require_xai=False)
    click.echo(
        render_playbook(
            agent_user_id=config.agent_user_id,
            agent_label=config.agent_label,
        )
    )


@cli.command(
    "print-issue",
    help=(
        "Fetch one Linear issue and print its rendered context (handy to "
        "paste into Grok manually). Needs LINEAR_API_KEY but no XAI key."
    ),
)
@click.argument("issue_identifier")
@click.pass_obj
def print_issue(load_config: _LoadConfig, issue_identifier: str) -> None:
    config = load_config(require_linear=True, require_xai=False)
    client = LinearClient(
        api_key=config.linear_api_key, base_url=config.linear_base_url
    )
    issues = client.fetch_assigned_issues(
        agent_user_id=config.agent_user_id,
        agent_label=config.agent_label,
    )
    matches = [i for i in issues if i.identifier == issue_identifier]
    if not matches:
        click.echo(
            f"No issue matching {issue_identifier!r} is currently assigned to "
            "the Grok agent.",
            err=True,
        )
        sys.exit(1)
    click.echo(matches[0].to_prompt_context())


@cli.command(
    "run-once", help="Process one batch of assigned issues and exit (API mode)."
)
@click.pass_obj
def run_once(load_config: _LoadConfig) -> None:
    config = load_config()
    workflow = GrokWorkflow(config)
    results = workflow.run_once()
    click.echo(_format_summary(results))


@cli.command(
    "watch",
    help="Continuously poll Linear and process issues (API mode).",
)
@click.option(
    "--interval",
    type=float,
    default=None,
    help="Override poll interval in seconds.",
)
@click.option(
    "--max-iterations",
    type=int,
    default=None,
    help="Stop after this many polling iterations (0 = forever).",
)
@click.pass_obj
def watch(
    load_config: _LoadConfig,
    interval: float | None,
    max_iterations: int | None,
) -> None:
    config = load_config()
    if interval is not None or max_iterations is not None:
        from dataclasses import replace

        config = replace(
            config,
            poll_interval_seconds=(
                interval if interval is not None else config.poll_interval_seconds
            ),
            max_iterations=(
                max_iterations if max_iterations is not None else config.max_iterations
            ),
        )
    workflow = GrokWorkflow(config)
    for batch in workflow.run_forever():
        click.echo(_format_summary(batch))


if __name__ == "__main__":  # pragma: no cover
    cli()
