"""Command-line entry point for the Grok ↔ Linear workflow.

Usage::

    uv run python -m financial_agent.agents.grok run-once
    uv run python -m financial_agent.agents.grok watch --interval 60
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Callable

import click

from .config import ConfigError, GrokWorkflowConfig
from .workflow import GrokWorkflow, ProcessedIssue


_LoadConfig = Callable[[], GrokWorkflowConfig]


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


@click.group(help="Linear ↔ Grok automation for the financial-agent repo.")
@click.option("-v", "--verbose", is_flag=True, help="Enable debug logging.")
@click.pass_context
def cli(ctx: click.Context, verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    def _load() -> GrokWorkflowConfig:
        try:
            return GrokWorkflowConfig.from_env()
        except ConfigError as exc:
            click.echo(f"Configuration error: {exc}", err=True)
            sys.exit(2)

    ctx.obj = _load


@cli.command("run-once", help="Process one batch of assigned issues and exit.")
@click.pass_obj
def run_once(load_config: _LoadConfig) -> None:
    config = load_config()
    workflow = GrokWorkflow(config)
    results = workflow.run_once()
    click.echo(_format_summary(results))


@cli.command("watch", help="Continuously poll Linear and process issues.")
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
