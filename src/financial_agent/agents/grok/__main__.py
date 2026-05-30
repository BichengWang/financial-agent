"""Allow ``python -m financial_agent.agents.grok`` to invoke the CLI."""

from .cli import cli

if __name__ == "__main__":
    cli()
