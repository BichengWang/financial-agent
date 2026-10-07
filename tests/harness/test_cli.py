from __future__ import annotations

import json
from pathlib import Path

import pytest
from conftest import OUTPUT_DIR, REPO, real_data
from test_kernels import RUN

from financial_agent.harness.__main__ import main, tool_names
from financial_agent.harness.skills import SkillRegistry

LATEST = OUTPUT_DIR / "claude-opus-5-2026-09-03"


def test_every_skill_tool_binding_names_a_real_command(tmp_path: Path) -> None:
    registry = SkillRegistry.discover([REPO / "skills"], known_tools=tool_names())
    assert all(r.ok for r in registry.results), [r.errors for r in registry.results]
    bad = tmp_path / "s"
    bad.mkdir()
    (bad / "SKILL.md").write_text(
        '---\nname: s\ndescription: d\nmetadata:\n  fa-tools: "gate place-order"\n'
        "---\nbody\n",
        encoding="utf-8",
    )
    result = SkillRegistry.discover([tmp_path], known_tools=tool_names()).results[0]
    assert any("place-order" in e for e in result.errors)


def test_session_and_reachability(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["session", "2026-06-19"]) == 0
    assert capsys.readouterr().out.startswith("HOLIDAY 2026-06-19 is a market holiday")
    assert main(["reachability"]) == 1
    out = capsys.readouterr().out
    assert out.count("BLOCKER: threshold") == 3 and "GO unreachable" in out
    families = ["--families", "fund_z", "tech_z", "sent_z", "macro_z"]
    assert main(["reachability", *families]) == 1  # fund/sent are still SHADOW


def test_kernel_command(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    request = {
        "closes": [100 + i + (i % 3) for i in range(61)],
        "spy_closes": [400 + 2 * i + (i % 2) for i in range(61)],
    }
    path = tmp_path / "risk.json"
    path.write_text(json.dumps(request), encoding="utf-8")
    assert main(["kernel", "risk", "--input", str(path)]) == 0
    assert "beta_60d_vs_spy" in json.loads(capsys.readouterr().out)
    path.write_text(json.dumps({"closes": [1.0], "spy_closes": [1.0]}))
    assert main(["kernel", "risk", "--input", str(path)]) == 1
    assert "KERNEL ERROR: KernelError: closes: 1 closes" in capsys.readouterr().out
    path.write_text(json.dumps({"run_date": RUN, "model": "m"}))
    assert main(["kernel", "market", "--input", str(path)]) == 1
    assert "KeyError" in capsys.readouterr().out


def test_schema_document(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["schema", "--json-schema"]) == 0
    document = json.loads(capsys.readouterr().out)
    assert document["properties"]["schema_version"] == {"const": 1}


@real_data
def test_schema_reports_a_legacy_ledger(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["schema", str(LATEST)]) == 1
    out = capsys.readouterr().out
    assert "legacy ledger, does not declare schema_version" in out
    assert "v1: predictions[0] VLO: metrics.kelly_025 is not v1" in out


@real_data
def test_gate_json_and_text(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["gate", str(LATEST), "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["pass"] and report["content_hash"].startswith("sha256:")
    assert report["replay"]["session"]["kind"] == "TRADING"
    assert main(["gate", str(LATEST)]) == 0
    out = capsys.readouterr().out
    assert "GO unreachable: threshold 2" in out
    assert "Names rejected per evidence threshold" in out


@real_data
def test_replay_command(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["replay", "--as-of", "2026-09-03"]) == 0
    out = capsys.readouterr().out
    assert "73 of 83 replayed packages agree" in out
    assert "| gpt-5-2026-06-19 | HOLIDAY | REVIEW_ONLY | NO_TRADE |" in out
    assert main(["replay", "--as-of", "2026-09-03", "--strict"]) == 1
    capsys.readouterr()
    assert main(["replay", "--since", "2026-08-27", "--strict"]) == 0
