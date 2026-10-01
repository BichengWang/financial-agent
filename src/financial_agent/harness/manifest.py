"""Manifest sections generated from the package directory (plan §3.5 step 7).

Three manifests in the history listed artifacts that were never written. The
checklist here is read from disk after the files exist, next to the gate result,
the status replay, and the content hash, so none of it is typed by a model.
"""

from __future__ import annotations

from pathlib import Path

from financial_agent.harness.fingerprint import artifact_digests, package_digest
from financial_agent.harness.gates import (
    ALWAYS_ARTIFACTS,
    CHECKPOINT_ARTIFACTS,
    PREDICTIONS_FILE,
    publish_gate,
    replay_status,
)
from financial_agent.harness.policy import Policy


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
    lines += ["", "## Publish gate", ""]
    if failures:
        lines.extend(f"- FAIL: {failure}" for failure in failures)
    else:
        lines.append("PASS")
    return "\n".join(lines), failures
