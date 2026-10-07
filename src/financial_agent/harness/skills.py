"""Agent Skills registry: discovery, validation, and progressive disclosure.

Implements the open Agent Skills format (agentskills.io specification, the
same ``SKILL.md`` layout Claude Code and other agent runtimes load):

* Level 1 -- metadata: ``name`` + ``description`` for every skill, rendered as
  the ``<available_skills>`` catalog a runtime puts in the system prompt.
* Level 2 -- instructions: the ``SKILL.md`` body, read only on activation.
* Level 3 -- resources: files under the skill root, read only when referenced.

Harness binding rides in the spec's ``metadata`` string map under ``fa-`` keys
(``fa-stages``, ``fa-tools``, ``fa-writes``, ``fa-version``), so a skill stays a
valid, portable Agent Skill for any client that ignores those keys.

The frontmatter parser accepts a strict YAML subset (scalars, quoted scalars,
block scalars, one-level mappings) and rejects anything else, keeping the
harness on the standard library. A value another client's YAML parser would
re-type (``version: 1.0`` becomes a float, ``reviewed: 2026-09-28`` a date) is
flagged, because the spec requires ``metadata`` values to be strings.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Union
from xml.sax.saxutils import escape

SKILL_FILE = "SKILL.md"
NAME_MAX = 64
DESCRIPTION_MAX = 1024
COMPATIBILITY_MAX = 500
BODY_MAX_LINES = 500
BODY_TOKEN_BUDGET = 5000
CHARS_PER_TOKEN = 4  # rough estimate, used only for size warnings

SPEC_FIELDS = frozenset(
    {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
)
HARNESS_PREFIX = "fa-"
HARNESS_KEYS = frozenset({"fa-stages", "fa-tools", "fa-writes", "fa-version"})

_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_KEY_RE = re.compile(r"^([A-Za-z0-9_][A-Za-z0-9_.-]*):(?:[ \t]+(.*)|)$")
# Plain scalars YAML 1.1/1.2 loaders turn into numbers, booleans, null, or dates.
_RETYPED_SCALAR_RE = re.compile(
    r"^(?:[-+]?(?:\d[\d_]*)?\.?\d+(?:[eE][-+]?\d+)?|0x[0-9a-fA-F]+|0o[0-7]+"
    r"|\d{4}-\d{2}-\d{2}|true|false|yes|no|on|off|null|~)$",
    re.IGNORECASE,
)
_LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
_ESCAPING_REF_RE = re.compile(r"`(\.\./[^`]*)`")

FrontmatterValue = Union[str, dict[str, str]]


class FrontmatterError(ValueError):
    """Raised when SKILL.md frontmatter is missing or outside the YAML subset."""


@dataclass(frozen=True)
class ParsedFrontmatter:
    fields: dict[str, FrontmatterValue]
    body: str
    # Dotted keys (``metadata.version``) whose plain scalar another YAML parser
    # would load as a number, boolean, or null instead of a string.
    retyped_keys: frozenset[str]


def _unquote(raw: str, line_no: int) -> tuple[str, bool]:
    """Return (value, was_quoted) for a single-line YAML scalar."""
    if raw[:1] in {'"', "'"}:
        quote = raw[0]
        if len(raw) < 2 or not raw.endswith(quote):
            raise FrontmatterError(f"line {line_no}: unterminated quoted scalar")
        inner = raw[1:-1]
        if quote == "'":
            return inner.replace("''", "'"), True
        return inner.replace('\\"', '"').replace("\\\\", "\\"), True
    if raw[:1] in {"[", "{", "&", "*", "!", "|", ">", "%", "@", "`"} or (
        raw == "-" or raw.startswith("- ")
    ):
        # Flow collections, anchors, aliases, tags, sequences: out of subset.
        raise FrontmatterError(f"line {line_no}: unsupported YAML construct {raw!r}")
    comment = re.search(r"\s#", raw)
    value = (raw[: comment.start()] if comment else raw).strip()
    if ": " in value or value.endswith(":"):
        raise FrontmatterError(
            f"line {line_no}: plain scalar contains ': ' which YAML parsers "
            "reject; quote the value"
        )
    return value, False


def _block_scalar(indicator: str, lines: list[str]) -> str:
    folded = indicator.startswith(">")
    strip = indicator.endswith("-")
    stripped = [line.strip() for line in lines]
    if folded:
        text = ""
        for line in stripped:
            if not line:
                text = text.rstrip(" ") + "\n"
            else:
                text += line + " "
        text = text.rstrip(" ")
    else:
        indent = min(
            (len(line) - len(line.lstrip()) for line in lines if line.strip()),
            default=0,
        )
        text = "\n".join(line[indent:] for line in lines)
    text = text.rstrip("\n")
    return text if strip else text + "\n"


def parse_frontmatter(text: str) -> ParsedFrontmatter:
    """Split ``SKILL.md`` text into frontmatter fields and Markdown body."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("SKILL.md must start with '---' YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise FrontmatterError("frontmatter is not closed with '---'") from None
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1 :]).lstrip("\n")

    fields: dict[str, FrontmatterValue] = {}
    retyped: set[str] = set()
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        line_no = i + 2
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line[:1] in {" ", "\t"}:
            raise FrontmatterError(f"line {line_no}: unexpected indentation")
        match = _KEY_RE.match(line.rstrip())
        if not match:
            raise FrontmatterError(f"line {line_no}: expected 'key: value'")
        key, raw = match.group(1), (match.group(2) or "").strip()
        if key in fields:
            raise FrontmatterError(f"line {line_no}: duplicate key {key!r}")
        # Collect the indented continuation block that belongs to this key.
        j = i + 1
        block: list[str] = []
        while j < len(fm_lines) and (
            not fm_lines[j].strip() or fm_lines[j][:1] in {" ", "\t"}
        ):
            block.append(fm_lines[j])
            j += 1
        while block and not block[-1].strip():
            block.pop()
            j -= 1
        if key not in SPEC_FIELDS:
            # Runtime-specific field (e.g. a Claude Code extension): keep the raw
            # text so richer YAML there never breaks portable parsing.
            fields[key] = "\n".join([raw, *block]).strip()
        elif raw in {">", ">-", "|", "|-"}:
            fields[key] = _block_scalar(raw, block)
        elif raw:
            value, quoted = _unquote(raw, line_no)
            if block:
                if quoted:
                    raise FrontmatterError(
                        f"line {line_no}: multi-line quoted scalars are unsupported"
                    )
                value = " ".join([value, *(b.strip() for b in block if b.strip())])
            elif not quoted and _RETYPED_SCALAR_RE.match(value):
                retyped.add(key)
            fields[key] = value
        else:
            mapping: dict[str, str] = {}
            for offset, sub in enumerate(block):
                if not sub.strip() or sub.lstrip().startswith("#"):
                    continue
                sub_no = line_no + 1 + offset
                sub_match = _KEY_RE.match(sub.strip())
                if not sub_match or not sub_match.group(2):
                    raise FrontmatterError(
                        f"line {sub_no}: expected 'subkey: value' under {key!r}"
                    )
                sub_key = sub_match.group(1)
                sub_value, quoted = _unquote(sub_match.group(2).strip(), sub_no)
                if sub_key in mapping:
                    raise FrontmatterError(
                        f"line {sub_no}: duplicate key {key}.{sub_key}"
                    )
                if not quoted and _RETYPED_SCALAR_RE.match(sub_value):
                    retyped.add(f"{key}.{sub_key}")
                mapping[sub_key] = sub_value
            fields[key] = mapping
        i = j
    return ParsedFrontmatter(fields=fields, body=body, retyped_keys=frozenset(retyped))


@dataclass(frozen=True)
class Skill:
    """A validated skill. Only level-1 metadata is held in memory."""

    name: str
    description: str
    root: Path
    metadata: dict[str, str] = field(default_factory=dict)
    license: str | None = None
    compatibility: str | None = None
    allowed_tools: str | None = None
    extra_fields: dict[str, FrontmatterValue] = field(default_factory=dict)

    @property
    def skill_file(self) -> Path:
        return self.root / SKILL_FILE

    @property
    def stages(self) -> tuple[str, ...]:
        return tuple(self.metadata.get("fa-stages", "").split())

    @property
    def tools(self) -> tuple[str, ...]:
        return tuple(self.metadata.get("fa-tools", "").split())

    def body(self) -> str:
        """Level 2: the instructions, read from disk only when activated."""
        return parse_frontmatter(self.skill_file.read_text(encoding="utf-8")).body

    def resource(self, relpath: str) -> str:
        """Level 3: a bundled file, confined to the skill root."""
        target = (self.root / relpath).resolve()
        if Path(relpath).is_absolute() or not target.is_relative_to(
            self.root.resolve()
        ):
            raise PermissionError(f"{relpath!r} escapes skill root {self.root}")
        return target.read_text(encoding="utf-8")


@dataclass
class ValidationResult:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    skill: Skill | None = None

    @property
    def ok(self) -> bool:
        return not self.errors


def _check_str(
    fields: dict[str, FrontmatterValue],
    key: str,
    *,
    required: bool,
    max_len: int | None,
    errors: list[str],
) -> str | None:
    value = fields.get(key)
    if value is None:
        if required:
            errors.append(f"missing required field {key!r}")
        return None
    if not isinstance(value, str):
        errors.append(f"{key!r} must be a string, not a mapping")
        return None
    if not value.strip():
        errors.append(f"{key!r} must be non-empty")
    elif max_len is not None and len(value) > max_len:
        errors.append(f"{key!r} is {len(value)} chars; max {max_len}")
    return value


def validate_skill_dir(
    path: Path, *, known_stages: Iterable[str] = (), known_tools: Iterable[str] = ()
) -> ValidationResult:
    """Validate one skill directory against the open spec plus harness keys."""
    result = ValidationResult(path=path)
    skill_file = path / SKILL_FILE
    if not skill_file.is_file():
        result.errors.append(f"no {SKILL_FILE} in {path}")
        return result
    try:
        parsed = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    except FrontmatterError as exc:
        result.errors.append(str(exc))
        return result
    fields, errors, warnings = parsed.fields, result.errors, result.warnings

    name = _check_str(fields, "name", required=True, max_len=NAME_MAX, errors=errors)
    if name is not None and name.strip():
        if not _NAME_RE.match(name):
            errors.append(
                f"name {name!r} must be lowercase a-z/0-9 and single hyphens, "
                "not starting or ending with a hyphen"
            )
        if name != path.name:
            errors.append(
                f"name {name!r} must match its directory {path.name!r} (open spec)"
            )
    description = _check_str(
        fields, "description", required=True, max_len=DESCRIPTION_MAX, errors=errors
    )
    license_ = _check_str(
        fields, "license", required=False, max_len=None, errors=errors
    )
    compatibility = _check_str(
        fields,
        "compatibility",
        required=False,
        max_len=COMPATIBILITY_MAX,
        errors=errors,
    )
    allowed_tools = _check_str(
        fields, "allowed-tools", required=False, max_len=None, errors=errors
    )

    metadata: dict[str, str] = {}
    raw_metadata = fields.get("metadata")
    if raw_metadata is not None:
        if isinstance(raw_metadata, dict):
            metadata = dict(raw_metadata)
        else:
            errors.append("'metadata' must be a mapping of string keys to strings")
    for key in sorted(parsed.retyped_keys):
        if key.startswith("metadata.") or key in {"name", "description"}:
            errors.append(
                f"{key!r} is an unquoted scalar other YAML parsers load as a "
                "non-string; quote it"
            )

    stages, tools = set(known_stages), set(known_tools)
    for key, value in metadata.items():
        if not key.startswith(HARNESS_PREFIX):
            continue
        if key not in HARNESS_KEYS:
            warnings.append(f"unknown harness metadata key {key!r}")
        if key == "fa-stages" and stages:
            unknown = sorted(set(value.split()) - stages)
            if unknown:
                errors.append(f"fa-stages names unknown run states {unknown}")
        if key == "fa-tools" and tools:
            unknown = sorted(set(value.split()) - tools)
            if unknown:
                errors.append(f"fa-tools names unknown harness tools {unknown}")

    extra = {k: v for k, v in fields.items() if k not in SPEC_FIELDS}
    for key in sorted(extra):
        warnings.append(
            f"field {key!r} is not in the open spec; runtime-specific clients may "
            "honour it, others ignore it"
        )

    body = parsed.body
    body_lines = body.count("\n") + 1 if body else 0
    if not body.strip():
        warnings.append("SKILL.md body is empty")
    if body_lines > BODY_MAX_LINES:
        warnings.append(f"body is {body_lines} lines; keep under {BODY_MAX_LINES}")
    est_tokens = len(body) // CHARS_PER_TOKEN
    if est_tokens > BODY_TOKEN_BUDGET:
        warnings.append(
            f"body is ~{est_tokens} tokens; keep under {BODY_TOKEN_BUDGET} and move "
            "detail into references/"
        )
    for target in _LINK_RE.findall(body):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        rel = target.split("#", 1)[0]
        if rel.startswith("/") or ".." in Path(rel).parts:
            warnings.append(f"link {target!r} leaves the skill root; not portable")
        elif not (path / rel).exists():
            errors.append(f"link {target!r} points to a missing file")
        elif len(Path(rel).parts) > 2:
            warnings.append(f"link {target!r} is nested deeper than one level")
    for target in sorted(set(_ESCAPING_REF_RE.findall(body))):
        warnings.append(f"reference {target!r} leaves the skill root; not portable")

    if not errors and name and description:
        result.skill = Skill(
            name=name,
            description=description,
            root=path,
            metadata=metadata,
            license=license_,
            compatibility=compatibility,
            allowed_tools=allowed_tools,
            extra_fields=extra,
        )
    return result


class SkillRegistry:
    """Validated skills indexed by name, with stage routing and a catalog."""

    def __init__(self, results: Iterable[ValidationResult]) -> None:
        self.results = list(results)
        self.skills: dict[str, Skill] = {}
        for result in self.results:
            skill = result.skill
            if skill is None:
                continue
            if skill.name in self.skills:
                first = self.skills[skill.name].root
                result.errors.append(f"duplicate skill name {skill.name!r} ({first})")
                result.skill = None
                continue
            self.skills[skill.name] = skill

    @classmethod
    def discover(
        cls,
        roots: Iterable[Path],
        *,
        known_stages: Iterable[str] = (),
        known_tools: Iterable[str] = (),
    ) -> SkillRegistry:
        """Validate every skill directory at, or one level under, each root."""
        stages, tools = tuple(known_stages), tuple(known_tools)
        dirs: list[Path] = []
        for root in roots:
            if (root / SKILL_FILE).is_file():
                dirs.append(root)
            elif root.is_dir():
                dirs.extend(
                    sorted(p for p in root.iterdir() if (p / SKILL_FILE).is_file())
                )
        return cls(
            validate_skill_dir(d, known_stages=stages, known_tools=tools) for d in dirs
        )

    def get(self, name: str) -> Skill:
        return self.skills[name]

    def for_stage(self, stage: str) -> list[Skill]:
        return [s for s in self.skills.values() if stage in s.stages]

    def catalog_xml(self) -> str:
        """Level-1 catalog in the ``<available_skills>`` shape used by skills-ref."""
        parts = ["<available_skills>"]
        for skill in sorted(self.skills.values(), key=lambda s: s.name):
            parts.extend(
                [
                    "<skill>",
                    f"<name>\n{escape(skill.name)}\n</name>",
                    f"<description>\n{escape(skill.description)}\n</description>",
                    f"<location>\n{escape(str(skill.skill_file))}\n</location>",
                    "</skill>",
                ]
            )
        parts.append("</available_skills>")
        return "\n".join(parts)
