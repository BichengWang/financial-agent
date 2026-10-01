from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, market_forecast, real_data
from test_gates_and_lifecycle import build_package

from financial_agent.harness.__main__ import main
from financial_agent.harness.manifest import render_manifest_sections
from financial_agent.harness.policy import Policy


def package_with_etfs(tmp_path: Path) -> Path:
    etfs = [market_forecast(t, 100.0) for t in ("SPY", "QQQ", "SOXX")]
    return build_package(tmp_path, etfs)


def test_checklist_is_read_from_disk(tmp_path: Path, policy: Policy) -> None:
    package = package_with_etfs(tmp_path)
    text, failures = render_manifest_sections(package, policy)
    assert failures == [] and "## Publish gate\n\nPASS" in text
    assert "| `15_predictions.json` | yes |" in text
    assert "Content hash: `sha256:" in text
    assert "Replay: `NO_TRADE`" in text

    (package / "08_risk_review.md").unlink()
    text, failures = render_manifest_sections(package, policy)
    assert "| `08_risk_review.md` | **NO** | - |" in text
    assert "- FAIL: missing required artifact 08_risk_review.md" in text
    assert failures


def test_checkpoint_artifacts_listed_only_when_present(
    tmp_path: Path, policy: Policy
) -> None:
    package = package_with_etfs(tmp_path)
    assert "checkpoint" not in render_manifest_sections(package, policy)[0]
    (package / "12_close_log.md").write_text("# close\n", encoding="utf-8")
    assert "`12_close_log.md` (checkpoint) | yes" in (
        render_manifest_sections(package, policy)[0]
    )


def test_no_ledger_means_nothing_to_replay(tmp_path: Path, policy: Policy) -> None:
    package = package_with_etfs(tmp_path)
    (package / "15_predictions.json").unlink()
    text, failures = render_manifest_sections(package, policy)
    assert "nothing to replay" in text and failures


@real_data
def test_cli_matches_the_gate_on_a_real_package(
    capsys: pytest.CaptureFixture[str],
) -> None:
    package = OUTPUT_DIR / "claude-opus-5-2026-09-03"
    assert main(["manifest", str(package)]) == 0
    out = capsys.readouterr().out
    assert "Replay: `NO_TRADE`" in out and out.rstrip().endswith("PASS")
    assert main(["gate", str(package)]) == 0
    gate_out: Any = capsys.readouterr().out
    assert "status replay: NO_TRADE" in gate_out
