import pytest

from financial_agent.agents.grok.playbook import (
    AGENT_COMMENT_MARKER,
    render_playbook,
)


def test_render_playbook_with_user_id() -> None:
    text = render_playbook(agent_user_id="user-42")

    assert "user-42" in text
    assert AGENT_COMMENT_MARKER in text
    assert "## Per-issue procedure" in text
    assert "## Trigger filter" in text


def test_render_playbook_with_label() -> None:
    text = render_playbook(agent_label="grok")

    assert "label named `grok`" in text
    assert "AND" not in text.splitlines()[0]


def test_render_playbook_with_both_uses_and() -> None:
    text = render_playbook(agent_user_id="u-1", agent_label="grok")

    assert "u-1" in text
    assert "label named `grok`" in text
    assert "AND" in text


def test_render_playbook_requires_a_trigger() -> None:
    with pytest.raises(ValueError):
        render_playbook()


def test_render_playbook_mentions_repo_conventions() -> None:
    text = render_playbook(agent_user_id="u")
    assert "numpy<2.0" in text
    assert "pandas<2.0" in text
    assert "Python ≥3.12" in text
