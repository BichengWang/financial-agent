"""Run one scheduled quant session and alert a webhook when it does not succeed.

Usage (stdlib only; run from the repository root):

    uv run --no-dev python deploy/quant/run-session.py \\
        --env-file /abs/quant-paper.env --config /abs/host.toml [fa-quant run args]

The env file must be a regular file owned by the current user with mode 600/400.
Its ``KEY=VALUE`` pairs override the inherited environment for the child only.
The wrapper exits with the child's exit code. When that code is non-zero and
``FA_QUANT_ALERT_WEBHOOK`` is set, it posts one JSON alert. Credential values and
the webhook URL never reach the alert text or stderr.
"""

import argparse
import json
import os
import re
import stat
import subprocess
import sys
import urllib.request
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

Redact = Callable[[str], str]

WEBHOOK_VARIABLE = "FA_QUANT_ALERT_WEBHOOK"
MIN_SECRET_LENGTH = 8
MAX_REASONS = 10
MAX_REASON_CHARS = 500
POST_TIMEOUT_SECONDS = 10.0
REDACTED = "[redacted]"
_ASSIGNMENT = re.compile(r"(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(.*)")


class WrapperError(Exception):
    """A refusal that is safe to print: it never carries file contents."""


def check_env_file(path: Path) -> None:
    """Require a user-owned regular file without group/other permission bits."""
    try:
        info = path.stat()
    except OSError as exc:
        raise WrapperError(f"env file {path}: {type(exc).__name__}") from None
    if not stat.S_ISREG(info.st_mode):
        raise WrapperError(f"env file {path}: not a regular file")
    if info.st_uid != os.getuid():
        raise WrapperError(f"env file {path}: not owned by the current user")
    if info.st_mode & 0o077:
        raise WrapperError(
            f"env file {path}: permissions must be 600 or 400 "
            f"(found {stat.S_IMODE(info.st_mode):03o})"
        )


def parse_env_file(path: Path) -> dict[str, str]:
    """Parse KEY=VALUE lines; no expansion. Errors name only the line number."""
    check_env_file(path)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise WrapperError(f"env file {path}: {type(exc).__name__}") from None
    values: dict[str, str] = {}
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = _ASSIGNMENT.fullmatch(line)
        if match is None:
            raise WrapperError(f"env file {path}: malformed line {number}")
        key, value = match.group(1), match.group(2).strip()
        if value[:1] in ("'", '"'):
            if len(value) < 2 or value[-1] != value[0]:
                raise WrapperError(f"env file {path}: malformed line {number}")
            value = value[1:-1]
        values[key] = value
    return values


def build_command(config: str, extra: Sequence[str]) -> list[str]:
    return [
        sys.executable,
        "-m",
        "financial_agent.quant",
        "run",
        "--config",
        config,
        "--json",
        *extra,
    ]


def redactor(secrets: Sequence[str]) -> Redact:
    """Return a function replacing every secret (longest first) with a marker."""
    ordered = sorted({s for s in secrets if s}, key=len, reverse=True)

    def redact(text: str) -> str:
        for secret in ordered:
            text = text.replace(secret, REDACTED)
        return text

    return redact


def child_report(stdout: str) -> dict[str, Any] | None:
    """Return the session report if stdout is one, otherwise None."""
    try:
        report = json.loads(stdout)
    except ValueError:
        return None
    if isinstance(report, dict) and isinstance(report.get("status"), str):
        return report
    return None


def build_alert(
    exit_code: int, stdout: str, stderr: str, redact: Redact
) -> dict[str, Any]:
    report = child_report(stdout)
    session: str | None = None
    if report is not None:
        status = str(report["status"])
        if report.get("session") is not None:
            session = str(report["session"])
        raw = report.get("reasons")
        reasons = [str(r) for r in raw] if isinstance(raw, list) else []
    else:
        status = "ERROR"
        lines = [line.strip() for line in stderr.splitlines() if line.strip()]
        reasons = [lines[-1] if lines else "no error output"]
    status = redact(status)
    if session is not None:
        session = redact(session)
    reasons = [redact(r)[:MAX_REASON_CHARS] for r in reasons[:MAX_REASONS]]
    return {
        "text": (
            f"fa-quant {status} {session or 'unknown'} (exit {exit_code}): "
            + "; ".join(reasons)
        ),
        "status": status,
        "session": session,
        "exit_code": exit_code,
        "reasons": reasons,
    }


def post_alert(url: str, payload: dict[str, Any]) -> None:
    """POST the payload once as JSON; raises on any delivery failure."""
    if not url.lower().startswith(("https://", "http://")):
        raise ValueError("webhook must be an http(s) URL")
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=POST_TIMEOUT_SECONDS):
        pass


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0] if __doc__ else None,
        allow_abbrev=False,
    )
    parser.add_argument("--env-file", type=Path, required=True)
    parser.add_argument("--config", required=True)
    args, extra = parser.parse_known_args(argv)
    try:
        file_values = parse_env_file(args.env_file)
    except WrapperError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    environment: Mapping[str, str] = {**os.environ, **file_values}
    webhook = environment.get(WEBHOOK_VARIABLE, "")
    result = subprocess.run(
        build_command(args.config, extra),
        env=dict(environment),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    sys.stdout.write(result.stdout)
    sys.stdout.flush()
    sys.stderr.write(result.stderr)
    sys.stderr.flush()
    if result.returncode != 0 and webhook:
        secrets = [v for v in file_values.values() if len(v) >= MIN_SECRET_LENGTH]
        redact = redactor([*secrets, webhook])
        payload = build_alert(result.returncode, result.stdout, result.stderr, redact)
        try:
            post_alert(webhook, payload)
        except Exception as exc:  # alerting must never mask the exit code
            print(f"alert: delivery failed ({type(exc).__name__})", file=sys.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
