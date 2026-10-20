"""The scheduler wrapper alerts on non-zero exits without leaking credentials."""

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

from financial_agent.quant.risk import KillSwitch

SCRIPT = Path(__file__).parents[3] / "deploy/quant/run-session.py"
SECRET = "paper-secret-0123456789"
WEBHOOK = "https://hooks.example.test/services/T000/B000/webhook-token"
SESSION_DAY = "2020-06-08"
SATURDAY = "2020-06-06"


@pytest.fixture(scope="module")
def wrapper() -> ModuleType:
    spec = importlib.util.spec_from_file_location("run_session_wrapper", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def alerts(wrapper: ModuleType, monkeypatch: pytest.MonkeyPatch) -> list[Any]:
    """Capture alerts; the real urllib post is never reachable from tests."""
    calls: list[Any] = []
    monkeypatch.setattr(
        wrapper, "post_alert", lambda url, payload: calls.append((url, payload))
    )
    return calls


@pytest.fixture
def clean_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("FA_QUANT_ALERT_WEBHOOK", "APCA_API_SECRET_KEY"):
        monkeypatch.delenv(name, raising=False)


def write_env(tmp_path: Path, mode: int = 0o600, webhook: bool = True) -> Path:
    path = tmp_path / "quant-paper.env"
    lines = [f"APCA_API_SECRET_KEY={SECRET}"]
    if webhook:
        lines.append(f"FA_QUANT_ALERT_WEBHOOK={WEBHOOK}")
    path.write_text("\n".join(lines) + "\n")
    path.chmod(mode)
    return path


def run(wrapper: ModuleType, env_file: Path, config: Path | str, *extra: str) -> int:
    code = wrapper.main(["--env-file", str(env_file), "--config", str(config), *extra])
    assert isinstance(code, int)
    return code


def stub_child(
    wrapper: ModuleType, monkeypatch: pytest.MonkeyPatch, script: str
) -> None:
    command = [sys.executable, "-c", script]
    monkeypatch.setattr(wrapper, "build_command", lambda config, extra: command)


@pytest.mark.usefixtures("clean_environment")
def test_halted_session_posts_one_alert_without_secrets(
    wrapper: ModuleType,
    alerts: list[Any],
    config_path: Path,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    KillSwitch(tmp_path / "state").engage("operator stop", source="operator")
    code = run(wrapper, write_env(tmp_path), config_path, "--today", SESSION_DAY)
    assert code == 2
    assert json.loads(capsys.readouterr().out)["status"] == "HALTED"
    assert len(alerts) == 1
    url, payload = alerts[0]
    assert url == WEBHOOK
    assert payload == {
        "text": f"fa-quant HALTED {SESSION_DAY} (exit 2): kill switch engaged",
        "status": "HALTED",
        "session": SESSION_DAY,
        "exit_code": 2,
        "reasons": ["kill switch engaged"],
    }
    encoded = json.dumps(payload)
    assert SECRET not in encoded and WEBHOOK not in encoded


@pytest.mark.usefixtures("clean_environment")
def test_successful_session_passes_through_and_posts_nothing(
    wrapper: ModuleType,
    alerts: list[Any],
    config_path: Path,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert run(wrapper, write_env(tmp_path), config_path, "--today", SATURDAY) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "NO_SESSION"
    assert alerts == []


@pytest.mark.usefixtures("clean_environment")
def test_alert_requires_webhook(
    wrapper: ModuleType, alerts: list[Any], config_path: Path, tmp_path: Path
) -> None:
    KillSwitch(tmp_path / "state").engage("operator stop", source="operator")
    env_file = write_env(tmp_path, webhook=False)
    assert run(wrapper, env_file, config_path, "--today", SESSION_DAY) == 2
    assert alerts == []


@pytest.mark.parametrize("mode", [0o640, 0o604])
@pytest.mark.usefixtures("clean_environment")
def test_accessible_env_file_is_refused(
    wrapper: ModuleType,
    alerts: list[Any],
    monkeypatch: pytest.MonkeyPatch,
    config_path: Path,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    mode: int,
) -> None:
    def forbidden(config: str, extra: list[str]) -> list[str]:
        raise AssertionError("child must not start")

    monkeypatch.setattr(wrapper, "build_command", forbidden)
    env_file = write_env(tmp_path, mode=mode)
    assert run(wrapper, env_file, config_path) == 1
    captured = capsys.readouterr()
    assert str(env_file) in captured.err
    assert SECRET not in captured.err + captured.out
    assert alerts == []


@pytest.mark.usefixtures("clean_environment")
def test_config_error_posts_redacted_error_alert(
    wrapper: ModuleType,
    alerts: list[Any],
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    script = (
        "import sys\n"
        "print('not a report')\n"
        "print('earlier noise', file=sys.stderr)\n"
        f"print('error: bad key {SECRET} at {WEBHOOK}', file=sys.stderr)\n"
        "print('', file=sys.stderr)\n"
        "sys.exit(1)\n"
    )
    stub_child(wrapper, monkeypatch, script)
    assert run(wrapper, write_env(tmp_path), "ignored.toml") == 1
    streams = capsys.readouterr()
    assert streams.out == "not a report\n"  # child output passes through unchanged
    assert len(alerts) == 1
    payload = alerts[0][1]
    assert payload["status"] == "ERROR"
    assert payload["session"] is None
    assert payload["exit_code"] == 1
    assert payload["reasons"] == ["error: bad key [redacted] at [redacted]"]
    assert payload["text"] == (
        "fa-quant ERROR unknown (exit 1): error: bad key [redacted] at [redacted]"
    )
    assert SECRET not in json.dumps(payload) and WEBHOOK not in json.dumps(payload)


@pytest.mark.usefixtures("clean_environment")
def test_reasons_are_capped(
    wrapper: ModuleType,
    alerts: list[Any],
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    report = {"status": "HALTED", "session": SESSION_DAY, "reasons": ["x" * 900] * 12}
    stub_child(
        wrapper,
        monkeypatch,
        f"import sys, json; print(json.dumps({report!r})); sys.exit(2)",
    )
    assert run(wrapper, write_env(tmp_path), "ignored.toml") == 2
    reasons = alerts[0][1]["reasons"]
    assert len(reasons) == 10 and all(len(r) == 500 for r in reasons)


@pytest.mark.usefixtures("clean_environment")
def test_delivery_failure_keeps_exit_code_and_hides_url(
    wrapper: ModuleType,
    monkeypatch: pytest.MonkeyPatch,
    config_path: Path,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    attempts: list[str] = []

    def failing(url: str, payload: dict[str, Any]) -> None:
        attempts.append(url)
        raise RuntimeError(f"cannot reach {url}")

    monkeypatch.setattr(wrapper, "post_alert", failing)
    KillSwitch(tmp_path / "state").engage("operator stop", source="operator")
    code = run(wrapper, write_env(tmp_path), config_path, "--today", SESSION_DAY)
    assert code == 2
    assert attempts == [WEBHOOK]
    err = capsys.readouterr().err
    assert "alert: delivery failed (RuntimeError)" in err
    assert WEBHOOK not in err and "webhook-token" not in err


@pytest.mark.usefixtures("clean_environment")
def test_inherited_webhook_is_used_and_redacted(
    wrapper: ModuleType,
    alerts: list[Any],
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setenv("FA_QUANT_ALERT_WEBHOOK", WEBHOOK)
    stub_child(
        wrapper,
        monkeypatch,
        f"import sys; print('error: {WEBHOOK}', file=sys.stderr); sys.exit(1)",
    )
    assert run(wrapper, write_env(tmp_path, webhook=False), "ignored.toml") == 1
    assert alerts[0][0] == WEBHOOK
    assert alerts[0][1]["reasons"] == ["error: [redacted]"]


def test_env_file_values_override_the_inherited_environment(
    wrapper: ModuleType,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("FA_TEST_VALUE", "inherited")
    monkeypatch.delenv("FA_QUANT_ALERT_WEBHOOK", raising=False)
    path = tmp_path / "quant-paper.env"
    path.write_text("FA_TEST_VALUE=from-file\n")
    path.chmod(0o400)
    stub_child(wrapper, monkeypatch, "import os; print(os.environ['FA_TEST_VALUE'])")
    assert run(wrapper, path, "ignored.toml") == 0
    assert capsys.readouterr().out == "from-file\n"


def test_env_file_syntax(wrapper: ModuleType, tmp_path: Path) -> None:
    path = tmp_path / "quant-paper.env"
    path.write_text(
        "# comment\n"
        "\n"
        "PLAIN=value with spaces  \n"
        "export EXPORTED=1\n"
        'DOUBLE="quoted # not a comment"\n'
        "SINGLE='$HOME stays literal'\n"
        "EMPTY=\n"
    )
    path.chmod(0o600)
    assert wrapper.parse_env_file(path) == {
        "PLAIN": "value with spaces",
        "EXPORTED": "1",
        "DOUBLE": "quoted # not a comment",
        "SINGLE": "$HOME stays literal",
        "EMPTY": "",
    }


@pytest.mark.parametrize("bad", ["not an assignment", "1BAD=x", "KEY='unterminated"])
def test_malformed_env_line_reports_only_its_number(
    wrapper: ModuleType, tmp_path: Path, bad: str
) -> None:
    path = tmp_path / "quant-paper.env"
    path.write_text(f"OK={SECRET}\n{bad}\n")
    path.chmod(0o600)
    with pytest.raises(wrapper.WrapperError) as caught:
        wrapper.parse_env_file(path)
    message = str(caught.value)
    assert "line 2" in message
    assert SECRET not in message and bad not in message
