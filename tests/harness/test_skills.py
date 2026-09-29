from __future__ import annotations

from pathlib import Path

import pytest
from conftest import REPO

from financial_agent.harness.lifecycle import RunState
from financial_agent.harness.skills import (
    FrontmatterError,
    SkillRegistry,
    parse_frontmatter,
    validate_skill_dir,
)

STAGES = [s.value for s in RunState]


def write_skill(
    root: Path, dirname: str, frontmatter: str, body: str = "# Do it\n"
) -> Path:
    skill_dir = root / dirname
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        f"---\n{frontmatter}\n---\n{body}", encoding="utf-8"
    )
    return skill_dir


def test_minimal_skill_is_valid(tmp_path: Path) -> None:
    result = validate_skill_dir(
        write_skill(
            tmp_path,
            "pdf-processing",
            "name: pdf-processing\ndescription: Use for PDFs.",
        )
    )
    assert result.ok, result.errors
    assert result.skill is not None and result.skill.name == "pdf-processing"


@pytest.mark.parametrize(
    "name", ["PDF-Processing", "-pdf", "pdf-", "pdf--processing", "a" * 65]
)
def test_spec_invalid_names_are_rejected(tmp_path: Path, name: str) -> None:
    result = validate_skill_dir(
        write_skill(tmp_path, name, f"name: {name}\ndescription: d")
    )
    assert not result.ok
    assert any("name" in error for error in result.errors)


def test_name_must_match_directory(tmp_path: Path) -> None:
    result = validate_skill_dir(
        write_skill(tmp_path, "other-dir", "name: my-skill\ndescription: d")
    )
    assert any("must match its directory" in error for error in result.errors)


def test_description_limit_is_1024_chars(tmp_path: Path) -> None:
    result = validate_skill_dir(
        write_skill(tmp_path, "s", f"name: s\ndescription: {'x' * 1025}")
    )
    assert any("max 1024" in error for error in result.errors)


def test_unquoted_numeric_metadata_is_flagged(tmp_path: Path) -> None:
    fm = (
        "name: s\ndescription: d\nmetadata:\n  version: 1.0\n  author: me\n"
        "  reviewed: 2026-09-28"
    )
    result = validate_skill_dir(write_skill(tmp_path, "s", fm))
    assert any("metadata.version" in error for error in result.errors)
    assert any("metadata.reviewed" in error for error in result.errors)
    fm = fm.replace("2026-09-28", '"2026-09-28"')
    quoted = validate_skill_dir(
        write_skill(tmp_path / "q", "s", fm.replace("1.0", '"1.0"'))
    )
    assert quoted.ok, quoted.errors
    assert quoted.skill is not None and quoted.skill.metadata["version"] == "1.0"


def test_block_and_continuation_scalars() -> None:
    folded = parse_frontmatter("---\nname: s\ndescription: >-\n  one\n  two\n---\nbody")
    assert folded.fields["description"] == "one two"
    plain = parse_frontmatter("---\nname: s\ndescription: one\n  two\n---\nbody")
    assert plain.fields["description"] == "one two"
    assert plain.body == "body"


@pytest.mark.parametrize(
    "line",
    ["name: [a, b]", "name: &anchor x", "description: foo: bar", "- item"],
)
def test_out_of_subset_yaml_is_an_error(line: str) -> None:
    with pytest.raises(FrontmatterError):
        parse_frontmatter(f"---\n{line}\n---\n")


def test_runtime_specific_fields_warn_but_parse(tmp_path: Path) -> None:
    fm = (
        "name: s\ndescription: d\ndisable-model-invocation: true\n"
        "hooks:\n  PreToolUse:\n    - matcher: Bash"
    )
    result = validate_skill_dir(write_skill(tmp_path, "s", fm))
    assert result.ok, result.errors
    assert any("disable-model-invocation" in w for w in result.warnings)
    assert any("'hooks'" in w for w in result.warnings)


def test_harness_stage_binding_is_checked(tmp_path: Path) -> None:
    fm = 'name: s\ndescription: d\nmetadata:\n  fa-stages: "SCORED BOGUS"'
    result = validate_skill_dir(write_skill(tmp_path, "s", fm), known_stages=STAGES)
    assert any("BOGUS" in error for error in result.errors)


def test_progressive_disclosure_levels(tmp_path: Path) -> None:
    skill_dir = write_skill(
        tmp_path,
        "s",
        "name: s\ndescription: Short.",
        body="See [ref](references/REF.md).\n",
    )
    (skill_dir / "references").mkdir()
    (skill_dir / "references" / "REF.md").write_text("deep detail", encoding="utf-8")
    (tmp_path / "secret.txt").write_text("outside", encoding="utf-8")

    registry = SkillRegistry.discover([tmp_path])
    skill = registry.get("s")
    catalog = registry.catalog_xml()
    assert "Short." in catalog and "See [ref]" not in catalog  # level 1: metadata only
    assert "See [ref]" in skill.body()  # level 2 on activation
    assert skill.resource("references/REF.md") == "deep detail"  # level 3
    with pytest.raises(PermissionError):
        skill.resource("../secret.txt")


def test_broken_link_is_an_error(tmp_path: Path) -> None:
    skill_dir = write_skill(
        tmp_path, "s", "name: s\ndescription: d", body="[x](references/nope.md)"
    )
    assert any("missing file" in e for e in validate_skill_dir(skill_dir).errors)


def test_duplicate_names_keep_the_first(tmp_path: Path) -> None:
    write_skill(tmp_path / "a", "dup", "name: dup\ndescription: first")
    write_skill(tmp_path / "b", "dup", "name: dup\ndescription: second")
    registry = SkillRegistry.discover([tmp_path / "a", tmp_path / "b"])
    assert registry.get("dup").description == "first"
    assert any("duplicate" in e for r in registry.results for e in r.errors)


def test_repository_skills_validate_and_route() -> None:
    registry = SkillRegistry.discover(
        [REPO / "skills", REPO / "agents" / "equity" / "turtle-trader"],
        known_stages=STAGES,
    )
    assert all(result.ok for result in registry.results), [
        (r.path, r.errors) for r in registry.results
    ]
    assert {"equity-publish-gate", "turtle-trader"} <= set(registry.skills)
    gate = registry.get("equity-publish-gate")
    assert gate.stages == ("RISK_REVIEW", "PUBLISHED")
    assert gate.tools == ("gate", "audit")
    assert [s.name for s in registry.for_stage("PUBLISHED")] == ["equity-publish-gate"]
    turtle = next(r for r in registry.results if r.path.name == "turtle-trader")
    assert any("leaves the skill root" in w for w in turtle.warnings)
