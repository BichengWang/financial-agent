from __future__ import annotations

from pathlib import Path

from conftest import OUTPUT_DIR, real_data

from financial_agent.harness.fingerprint import (
    artifact_digests,
    find_clones,
    package_digest,
)


def _package(root: Path, name: str, files: dict[str, str]) -> Path:
    package = root / name
    package.mkdir()
    for file_name, text in files.items():
        (package / file_name).write_text(text, encoding="utf-8")
    return package


def test_digest_tracks_content_and_names_only(tmp_path: Path) -> None:
    a = _package(tmp_path, "m-2026-09-01", {"01.md": "x", "15.json": "{}"})
    b = _package(tmp_path, "n-2026-09-02", {"15.json": "{}", "01.md": "x"})
    c = _package(tmp_path, "o-2026-09-03", {"01.md": "y", "15.json": "{}"})
    (a / "scratch.txt").write_text("ignored", encoding="utf-8")
    assert package_digest(a) == package_digest(b)
    assert package_digest(a) != package_digest(c)
    assert set(artifact_digests(a)) == {"01.md", "15.json"}


def test_find_clones_reports_shared_artifacts(tmp_path: Path) -> None:
    _package(tmp_path, "m-2026-06-20", {"06.md": "same", "05.md": "a", "e.md": ""})
    _package(tmp_path, "n-2026-09-02", {"06.md": "same", "05.md": "b", "e.md": ""})
    _package(tmp_path, "o-2026-09-03", {"06.md": "same", "05.md": "c", "e.md": ""})
    (tmp_path / "not-a-package").mkdir()

    everything = find_clones(tmp_path)
    assert [(name, pkgs) for (name, _), pkgs in everything.items()] == [
        ("06.md", ["m-2026-06-20", "n-2026-09-02", "o-2026-09-03"])
    ]
    recent = find_clones(tmp_path, since="2026-07-31")
    assert [pkgs for pkgs in recent.values()] == [["n-2026-09-02", "o-2026-09-03"]]


@real_data
def test_contract_era_packages_have_no_cloned_artifacts() -> None:
    assert find_clones(OUTPUT_DIR, since="2026-07-31") == {}
