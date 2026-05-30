import pytest

from financial_agent.agents.grok.config import ConfigError, GrokWorkflowConfig


def _base_env() -> dict[str, str]:
    return {
        "LINEAR_API_KEY": "lin_api_test",
        "XAI_API_KEY": "xai_test",
        "GROK_AGENT_USER_ID": "user-123",
    }


def test_from_env_minimal_ok() -> None:
    cfg = GrokWorkflowConfig.from_env(_base_env())
    assert cfg.linear_api_key == "lin_api_test"
    assert cfg.xai_api_key == "xai_test"
    assert cfg.agent_user_id == "user-123"
    assert cfg.agent_label is None
    assert cfg.grok_model == "grok-4-latest"
    assert cfg.dry_run is False


def test_from_env_label_alone_ok() -> None:
    env = {
        "LINEAR_API_KEY": "lin_api_test",
        "XAI_API_KEY": "xai_test",
        "GROK_AGENT_LABEL": "grok",
    }
    cfg = GrokWorkflowConfig.from_env(env)
    assert cfg.agent_user_id is None
    assert cfg.agent_label == "grok"


def test_from_env_missing_keys() -> None:
    with pytest.raises(ConfigError, match="LINEAR_API_KEY"):
        GrokWorkflowConfig.from_env({"XAI_API_KEY": "x"})
    with pytest.raises(ConfigError, match="XAI_API_KEY"):
        GrokWorkflowConfig.from_env({"LINEAR_API_KEY": "l"})


def test_from_env_requires_user_or_label() -> None:
    env = {"LINEAR_API_KEY": "l", "XAI_API_KEY": "x"}
    with pytest.raises(ConfigError, match="GROK_AGENT_USER_ID"):
        GrokWorkflowConfig.from_env(env)


def test_from_env_optionals_parsed() -> None:
    env = _base_env() | {
        "GROK_MODEL": "grok-test",
        "GROK_POLL_INTERVAL_SECONDS": "5.5",
        "GROK_MAX_ITERATIONS": "3",
        "GROK_DRY_RUN": "true",
    }
    cfg = GrokWorkflowConfig.from_env(env)
    assert cfg.grok_model == "grok-test"
    assert cfg.poll_interval_seconds == 5.5
    assert cfg.max_iterations == 3
    assert cfg.dry_run is True
