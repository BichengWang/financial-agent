"""Manifest sections generated from the package directory (plan §3.5 step 7).

Three manifests in the history listed artifacts that were never written. The
checklist here is read from disk after the files exist, next to the gate result,
the status replay, and the content hash, so none of it is typed by a model.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from financial_agent.harness.fingerprint import artifact_digests, package_digest
from financial_agent.harness.gates import (
    ALWAYS_ARTIFACTS,
    CHECKPOINT_ARTIFACTS,
    PREDICTIONS_FILE,
    StatusReplay,
    publish_gate,
    replay_status,
)
from financial_agent.harness.policy import Policy


def replay_lines(replay: StatusReplay) -> list[str]:
    """Calendar, structural GO blockers, and per-threshold rejections."""
    lines = []
    if replay.session is not None:
        lines.append(f"Session: {replay.session.describe()}.")
    reach = replay.reachability
    if reach is not None:
        if reach.reachable:
            lines.append(
                f"GO reachable with {', '.join(reach.gating_families)} scoring."
            )
        else:
            lines.append("GO unreachable: " + "; ".join(reach.blockers) + ".")
    if replay.blocking:
        counts = ", ".join(f"{k}: {v}" for k, v in sorted(replay.blocking.items()))
        lines.append(f"Names rejected per evidence threshold: {counts}.")
    return lines


def replay_dict(replay: StatusReplay) -> dict[str, Any]:
    reach = replay.reachability
    return {
        "status": replay.decision.status.value,
        "reasons": list(replay.decision.reasons),
        "published": replay.published,
        "agrees": replay.agrees,
        "investable": replay.investable,
        "session": None if replay.session is None else vars(replay.session),
        "blocking": replay.blocking,
        "go_reachable": None if reach is None else reach.reachable,
        "go_blockers": [] if reach is None else list(reach.blockers),
    }


def gate_report(package_dir: Path, policy: Policy) -> dict[str, Any]:
    """The publish gate, status replay, and content hash as one JSON object."""
    failures = publish_gate(package_dir, policy)
    replay = replay_status(package_dir, policy)
    return {
        "package": package_dir.name,
        "pass": not failures,
        "failures": failures,
        "content_hash": f"sha256:{package_digest(package_dir)}",
        "replay": None if replay is None else replay_dict(replay),
    }


def render_manifest_sections(
    package_dir: Path, policy: Policy
) -> tuple[str, list[str]]:
    """Markdown for the manifest's generated sections, and the gate failures."""
    digests = artifact_digests(package_dir)
    failures = publish_gate(package_dir, policy)
    lines = [
        "## Artifact checklist (generated from the directory)",
        "",
        "| Artifact | Present | sha256 |",
        "|---|---|---|",
    ]
    for name in (*ALWAYS_ARTIFACTS, PREDICTIONS_FILE):
        digest = digests.get(name)
        lines.append(
            f"| `{name}` | {'yes' if digest else '**NO**'} | "
            f"{f'`{digest[:12]}`' if digest else '-'} |"
        )
    for name in CHECKPOINT_ARTIFACTS:
        if name in digests:
            lines.append(f"| `{name}` (checkpoint) | yes | `{digests[name][:12]}` |")
    lines += ["", f"Content hash: `sha256:{package_digest(package_dir)}`", ""]

    replay = replay_status(package_dir, policy)
    lines.append("## Status replay")
    lines.append("")
    if replay is None:
        lines.append(f"No `{PREDICTIONS_FILE}`: nothing to replay.")
    else:
        reasons = "; ".join(replay.decision.reasons)
        lines.append(
            f"Replay: `{replay.decision.status.value}` ({reasons}); "
            f"published: `{replay.published}`; "
            f"{len(replay.investable)} investable. Required inputs assumed grounded."
        )
        lines += ["", *replay_lines(replay)]
    lines += ["", "## Publish gate", ""]
    if failures:
        lines.extend(f"- FAIL: {failure}" for failure in failures)
    else:
        lines.append("PASS")
    return "\n".join(lines), failures
