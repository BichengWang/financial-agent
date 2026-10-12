#!/usr/bin/env python3
"""Offline evidence arithmetic and structural audit.

This is not source-truth certification.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import tomllib
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from typing import Any, Never
from urllib.parse import quote

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
RESEARCH_ROOT = REPO_ROOT / "docs" / "research"
ARTIFACT_ROOT = RESEARCH_ROOT / "tickers"
REQUIRED = (
    "price",
    "shares",
    "market_cap",
    "revenue",
    "net_income",
    "operating_cash_flow",
    "capital_expenditure",
    "cash",
    "debt",
    "eps",
)
UNITS = {key: "USD" for key in REQUIRED} | {
    "price": "USD/share",
    "shares": "shares",
    "eps": "USD/share",
    "forward_eps": "USD/share",
    "required_return": "decimal",
    "risk_free_rate": "decimal",
}


class InvalidDocument(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidDocument(message)


def decimal(value: Any, label: str) -> Decimal:
    require(isinstance(value, str), f"{label}: expected decimal string")
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise InvalidDocument(f"{label}: invalid decimal") from exc
    require(result.is_finite(), f"{label}: nonfinite number")
    return result


def iso_date(value: Any, label: str) -> date:
    require(
        isinstance(value, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)),
        f"{label}: expected YYYY-MM-DD",
    )
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise InvalidDocument(f"{label}: invalid date") from exc


def text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InvalidDocument(f"{label}: expected nonempty text")
    return value


def confined(path: str | Path, root: Path) -> Path:
    result = Path(path).resolve()
    require(result.is_relative_to(root.resolve()), f"path outside {root}: {path}")
    return result


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise InvalidDocument(f"{path.name}: invalid JSON") from exc


def graph() -> dict[str, Any]:
    try:
        data = tomllib.loads((SKILL_ROOT / "graph.toml").read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise InvalidDocument("graph: invalid TOML") from exc
    require(data.get("version") == 1, "graph: version must be 1")
    policy = data.get("policy")
    if not isinstance(policy, dict):
        raise InvalidDocument("graph: missing policy")
    require(
        policy.get("required_facts") == list(REQUIRED),
        "graph: required_facts must match contract",
    )
    require(
        type(policy.get("max_quote_age_days")) is int
        and policy["max_quote_age_days"] >= 0,
        "graph: invalid quote age",
    )
    require(
        Decimal(0)
        <= decimal(policy.get("market_cap_tolerance"), "graph tolerance")
        < 1,
        "graph: invalid tolerance",
    )
    nodes = data.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        raise InvalidDocument("graph: missing nodes")
    by_id: dict[str, dict[str, Any]] = {}
    for node in nodes:
        require(isinstance(node, dict), "graph: node must be object")
        name = text(node.get("id"), "node id")
        require(name not in by_id, f"graph: duplicate node {name}")
        dependencies = node.get("requires")
        require(
            isinstance(dependencies, list)
            and all(isinstance(item, str) for item in dependencies)
            and len(set(dependencies)) == len(dependencies),
            f"graph: invalid dependencies for {name}",
        )
        instruction = text(node.get("instructions"), f"{name} instructions")
        target = confined(SKILL_ROOT / instruction, SKILL_ROOT)
        require(target.is_file(), f"graph: missing instructions {instruction}")
        text(node.get("section"), f"{name} section")
        by_id[name] = node
    require(
        set(by_id)
        == {
            "grounding",
            "business",
            "moat",
            "management",
            "inversion",
            "industry",
            "valuation",
            "synthesis",
            "audit",
        },
        "graph: unexpected node IDs",
    )
    ordered: list[dict[str, Any]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> None:
        require(name in by_id, f"graph: unknown dependency {name}")
        require(name not in visiting, f"graph: cycle at {name}")
        if name in visited:
            return
        visiting.add(name)
        for dependency in by_id[name]["requires"]:
            visit(dependency)
        visiting.remove(name)
        visited.add(name)
        ordered.append(by_id[name])

    for name in by_id:
        visit(name)
    require(
        len({node["section"] for node in ordered}) == len(ordered),
        "graph: duplicate report sections",
    )
    expected = {
        "grounding": ([], "Grounding"),
        "business": (["grounding"], "Business"),
        "moat": (["business"], "Moat"),
        "management": (["business"], "Management"),
        "inversion": (["moat", "management"], "Inversion"),
        "industry": (["grounding"], "Industry"),
        "valuation": (["grounding", "inversion", "industry"], "Valuation"),
        "synthesis": (["valuation"], "Decision"),
        "audit": (["synthesis"], "Limitations and audit"),
    }
    for name, (dependencies, section) in expected.items():
        require(
            set(by_id[name]["requires"]) == set(dependencies)
            and by_id[name]["section"] == section,
            f"graph: {name} differs from dependency/section contract",
        )
    extensions = data.get("extensions", [])
    require(isinstance(extensions, list), "graph: extensions must be a list")
    extension_ids: set[str] = set()
    reserved = {
        "report.md",
        "data/evidence.json",
        "data/calculations.json",
        "data/audit.json",
    }
    for extension in extensions:
        require(isinstance(extension, dict), "graph: extension must be object")
        name = text(extension.get("id"), "extension id")
        require(
            bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)),
            "graph: invalid extension id",
        )
        require(name not in extension_ids, f"graph: duplicate extension {name}")
        extension_ids.add(name)
        node = extension.get("node")
        require(
            isinstance(node, str) and node in by_id,
            f"graph: unknown node for {name}",
        )
        instruction = text(extension.get("instructions"), f"{name} instructions")
        require(
            instruction == f"skills/{name}/SKILL.md",
            f"graph: {name} must use its project-local skill entrypoint",
        )
        target = confined(REPO_ROOT / instruction, REPO_ROOT)
        require(target.is_file(), f"graph: missing skill instructions {instruction}")
        artifacts = extension.get("artifacts")
        require(
            isinstance(artifacts, list)
            and bool(artifacts)
            and all(isinstance(item, str) and item for item in artifacts),
            f"graph: invalid artifacts for {name}",
        )
        require(
            len(set(artifacts)) == len(artifacts),
            f"graph: duplicate artifacts for {name}",
        )
        for artifact in artifacts:
            path = Path(artifact)
            require(
                not path.is_absolute()
                and ".." not in path.parts
                and path.as_posix() not in reserved
                and path.as_posix() != ".",
                f"graph: {name} artifact escapes or overwrites core research",
            )
    return {
        "version": 1,
        "policy": policy,
        "nodes": ordered,
        "extensions": extensions,
    }


def validate_evidence(evidence: Any, policy: dict[str, Any]) -> list[dict[str, str]]:
    require(isinstance(evidence, dict), "evidence: expected object")
    require(
        type(evidence.get("schema_version")) is int and evidence["schema_version"] == 1,
        "evidence: schema_version must be integer 1",
    )
    require(
        isinstance(evidence.get("ticker"), str)
        and bool(re.fullmatch(r"[A-Z][A-Z0-9.-]*", evidence["ticker"])),
        "evidence: invalid ticker",
    )
    as_of = iso_date(evidence.get("as_of"), "as_of")
    require(evidence.get("currency") == "USD", "currency must be USD")
    quote = text(evidence.get("quote_time"), "quote_time")
    try:
        quote_time = datetime.fromisoformat(quote)
    except ValueError as exc:
        raise InvalidDocument("quote_time: invalid ISO datetime") from exc
    require(
        quote_time.tzinfo is not None and quote_time.utcoffset() is not None,
        "quote_time: timezone required",
    )
    require(quote_time.date() <= as_of, "quote_time is after as_of")
    findings: list[dict[str, str]] = []

    def warn(message: str) -> None:
        findings.append({"severity": "warning", "message": message})

    if (as_of - quote_time.date()).days > policy["max_quote_age_days"]:
        warn("quote is stale")
    source_rows = evidence.get("sources")
    require(isinstance(source_rows, list), "sources must be a list")
    sources: dict[str, dict[str, Any]] = {}
    for source in source_rows:
        require(isinstance(source, dict), "source must be object")
        source_id = text(source.get("id"), "source id")
        require(source_id not in sources, f"duplicate source {source_id}")
        for key in ("url", "title", "publisher", "excerpt"):
            text(source.get(key), f"source {source_id} {key}")
        require(
            bool(re.match(r"https?://[^/\s]+", source["url"])),
            f"source {source_id}: invalid URL",
        )
        require(
            iso_date(source.get("accessed_at"), f"source {source_id} accessed_at")
            <= as_of,
            f"source {source_id}: future access",
        )
        sources[source_id] = source
    facts = evidence.get("facts")
    require(isinstance(facts, dict), "facts must be object")
    tolerance = decimal(policy["market_cap_tolerance"], "tolerance")
    for name, fact in facts.items():
        require(isinstance(fact, dict), f"fact {name}: expected object")
        value = fact.get("value")
        require("value" in fact, f"fact {name}: missing value field")
        numeric = None if value is None else decimal(value, f"fact {name}")
        unit = fact.get("unit")
        require(
            isinstance(unit, str) and unit in {"USD", "shares", "USD/share", "decimal"},
            f"fact {name}: invalid unit",
        )
        if name in UNITS:
            require(fact["unit"] == UNITS[name], f"fact {name}: unit mismatch")
        period = text(fact.get("period"), f"fact {name} period")
        kind = fact.get("kind")
        require(
            isinstance(kind, str)
            and kind in {"reported", "estimate", "assumption", "unavailable"},
            f"fact {name}: invalid kind",
        )
        require(isinstance(fact.get("note"), str), f"fact {name}: note must be text")
        require(
            (numeric is None) == (kind == "unavailable"),
            f"fact {name}: null requires unavailable kind and vice versa",
        )
        if kind == "reported":
            for period_date in re.findall(r"\d{4}-\d{2}-\d{2}", period):
                require(
                    iso_date(period_date, f"fact {name} period") <= as_of,
                    f"fact {name}: future period cannot be reported",
                )
        references = fact.get("sources")
        require(
            isinstance(references, list)
            and all(isinstance(item, str) for item in references)
            and len(references) == len(set(references)),
            f"fact {name}: invalid sources",
        )
        require(
            all(item in sources for item in references), f"fact {name}: unknown source"
        )
        if numeric is None:
            warn(f"fact {name}: unavailable")
        elif kind in {"reported", "estimate"} and not references:
            warn(f"fact {name}: missing source citations")
        if kind in {"estimate", "assumption", "unavailable"}:
            require(
                bool(fact["note"].strip()),
                f"fact {name}: estimates/assumptions/unavailable values "
                "need explanation",
            )
            if name in REQUIRED:
                warn(f"required fact {name}: {kind}, not verified reported data")
        if name == "forward_eps":
            require(
                kind != "reported",
                "forward_eps: forecast cannot be labeled reported GAAP",
            )
        observations = fact.get("observations", [])
        require(
            isinstance(observations, list), f"fact {name}: observations must be list"
        )
        publishers: set[str] = set()
        for observation in observations:
            require(
                isinstance(observation, dict),
                f"fact {name}: observation must be object",
            )
            source_id = observation.get("source")
            require(
                isinstance(source_id, str) and source_id in references,
                f"fact {name}: observation source must be cited",
            )
            observed = decimal(observation.get("value"), f"fact {name} observation")
            require(
                observation.get("period") == period,
                f"fact {name}: observation period disagreement",
            )
            require(
                numeric is not None
                and abs(observed - numeric) <= abs(numeric) * tolerance,
                f"fact {name}: observation value disagreement",
            )
            publishers.add(" ".join(sources[source_id]["publisher"].casefold().split()))
        if name in REQUIRED and kind == "reported" and len(publishers) < 2:
            warn(f"fact {name}: needs observations from two distinct publishers")
        if name in {"price", "shares", "market_cap"} and numeric is not None:
            require(numeric > 0, f"fact {name}: must be positive")
        if name in {"capital_expenditure", "cash", "debt"} and numeric is not None:
            require(numeric >= 0, f"fact {name}: must be nonnegative")
    for name in REQUIRED:
        if name not in facts:
            warn(f"missing required fact {name}")
    if "operating_cash_flow" in facts and "capital_expenditure" in facts:
        require(
            facts["operating_cash_flow"]["period"]
            == facts["capital_expenditure"]["period"],
            "cash flow and capex periods are incompatible",
        )
    valuation = evidence.get("valuation")
    if valuation is None:
        warn("valuation omitted; no valuation decision can be verified")
        return findings
    require(isinstance(valuation, dict), "valuation must be object")
    require(
        valuation.get("discount_rate") == "required_return"
        and valuation.get("risk_free_rate") == "risk_free_rate",
        "valuation: named rate facts required",
    )
    base_id = text(valuation.get("base_eps"), "valuation base_eps")
    for name in (base_id, "required_return", "risk_free_rate"):
        require(
            name in facts and facts[name]["value"] is not None,
            f"valuation: missing usable {name}",
        )
    base = facts[base_id]
    require(
        base["unit"] == "USD/share" and decimal(base["value"], base_id) > 0,
        "valuation: positive EPS required",
    )
    require(
        bool(base["sources"]) or base["kind"] == "assumption",
        "valuation: EPS must be sourced or explicit assumption",
    )
    rate = facts["risk_free_rate"]
    require(
        rate["kind"] in {"reported", "estimate"} and bool(rate["sources"]),
        "risk_free_rate: contemporary cited market observation required",
    )
    rate_date = iso_date(rate["period"], "risk_free_rate period")
    require(
        0 <= (as_of - rate_date).days <= policy["max_quote_age_days"],
        "risk_free_rate: stale or future market rate",
    )
    risk_free = decimal(rate["value"], "risk_free_rate")
    required = facts["required_return"]
    require(
        required["kind"] == "assumption" and bool(required["note"].strip()),
        "required_return: justified assumption required",
    )
    discount = decimal(required["value"], "required_return")
    require(
        0 <= risk_free < discount,
        "required_return must exceed nonnegative risk_free_rate",
    )
    rows = valuation.get("scenarios")
    require(
        isinstance(rows, list)
        and len(rows) == 3
        and all(isinstance(row, dict) for row in rows),
        "valuation: three scenario objects required",
    )
    require(
        [row.get("name") for row in rows] == ["bear", "base", "bull"],
        "valuation: ordered bear/base/bull required",
    )
    years: set[int] = set()
    probability = Decimal(0)
    for row in rows:
        require(
            type(row.get("years")) is int and row["years"] > 0,
            "scenario: positive integer years required",
        )
        years.add(row["years"])
        require(
            decimal(row.get("growth"), "growth") > -1, "scenario growth must exceed -1"
        )
        require(
            decimal(row.get("exit_multiple"), "exit_multiple") > 0,
            "scenario multiple must be positive",
        )
        weight = decimal(row.get("probability"), "probability")
        require(0 <= weight <= 1, "scenario probability out of range")
        probability += weight
    require(
        len(years) == 1 and probability == 1,
        "scenarios need same horizon and probability sum 1",
    )
    timing = valuation.get("timing")
    if timing is None:
        warn(
            "valuation timing unverified: no explicit valuation/terminal dates "
            "and EPS alignment basis; returns are conditional period CAGR, "
            "not verified dated or YoY returns"
        )
    else:
        require(isinstance(timing, dict), "valuation timing must be object")
        require(
            timing.get("kind") == "assumption",
            "valuation timing must be an explicit assumption, not a future fact",
        )
        start = iso_date(timing.get("valuation_date"), "timing valuation_date")
        end = iso_date(timing.get("terminal_date"), "timing terminal_date")
        require(start == as_of, "timing valuation_date must match as_of")
        terminal_year = start.year + next(iter(years))
        require(terminal_year <= 9999, "timing horizon exceeds calendar range")
        try:
            anniversary = start.replace(year=terminal_year)
        except ValueError:
            anniversary = start.replace(year=terminal_year, day=28)
        require(
            end == anniversary,
            "timing terminal_date must match the scenario calendar-year horizon",
        )
        require(
            timing.get("eps_basis") in ("trailing", "forward", "normalized_run_rate"),
            "timing eps_basis must identify trailing, forward or normalized_run_rate",
        )
        text(timing.get("alignment_note"), "timing EPS alignment_note")
    return findings


def calculate(evidence: dict[str, Any]) -> dict[str, Any]:
    facts = evidence["facts"]

    def value(name: str) -> Decimal | None:
        raw = facts.get(name, {}).get("value")
        return None if raw is None else decimal(raw, name)

    def string(number: Decimal | None) -> str | None:
        return None if number is None else str(number)

    with localcontext() as context:
        context.prec = 40
        price, shares, cap = value("price"), value("shares"), value("market_cap")
        ocf, capex, eps = (
            value("operating_cash_flow"),
            value("capital_expenditure"),
            value("eps"),
        )
        implied = None if price is None or shares is None else price * shares
        fcf = None if ocf is None or capex is None else ocf - capex
        metrics = {
            "implied_market_cap": implied,
            "market_cap_deviation": (
                None if implied is None or cap is None else abs(implied - cap) / cap
            ),
            "free_cash_flow": fcf,
            "free_cash_flow_yield": None if fcf is None or cap is None else fcf / cap,
            "pe": None if price is None or eps is None or eps <= 0 else price / eps,
        }
        valuation_result = None
        model = evidence.get("valuation")
        if model is not None:
            if price is None:
                raise InvalidDocument("valuation requires price")
            base = value(model["base_eps"])
            discount = value(model["discount_rate"])
            if base is None or discount is None:
                raise InvalidDocument("valuation requires EPS and discount rate")
            rows = []
            weighted = Decimal(0)
            for row in model["scenarios"]:
                target = (
                    base
                    * (1 + decimal(row["growth"], "growth")) ** row["years"]
                    * decimal(row["exit_multiple"], "multiple")
                )
                present = target / (1 + discount) ** row["years"]
                annual = context.power(target / price, Decimal(1) / row["years"]) - 1
                weighted += present * decimal(row["probability"], "probability")
                rows.append(
                    row
                    | {
                        "target_price": str(target),
                        "total_return": str(target / price - 1),
                        "annualized_return": str(annual),
                        "present_target": str(present),
                    }
                )
            valuation_result = {
                "base_eps_fact": model["base_eps"],
                "discount_rate_fact": model["discount_rate"],
                "risk_free_rate_fact": model["risk_free_rate"],
                "scenarios": rows,
                "weighted_present_target": str(weighted),
            }
        return {
            "schema_version": 1,
            "ticker": evidence["ticker"],
            "as_of": evidence["as_of"],
            "currency": evidence["currency"],
            "metrics": {key: string(number) for key, number in metrics.items()},
            "valuation": valuation_result,
        }


def artifact_path(path: str | Path) -> Path:
    resolved = index_path(Path(path))
    require(
        resolved.is_relative_to(ARTIFACT_ROOT.resolve()),
        "artifact path outside native tickers root",
    )
    relative = resolved.relative_to(ARTIFACT_ROOT.resolve())
    require(
        len(relative.parts) == 2
        or (
            len(relative.parts) == 4
            and relative.parts[2] == "data"
            and relative.parts[3]
            in {"evidence.json", "calculations.json", "audit.json"}
        ),
        "artifact path requires ticker/date or ticker/date/data native JSON",
    )
    require(
        bool(re.fullmatch(r"[A-Z][A-Z0-9.-]*", relative.parts[0])),
        "artifact ticker directory invalid",
    )
    iso_date(relative.parts[1], "artifact date directory")
    return resolved


def check_identity(evidence: dict[str, Any], directory: Path) -> None:
    require(
        directory.resolve()
        == ARTIFACT_ROOT.resolve() / evidence["ticker"] / evidence["as_of"],
        "evidence ticker/date must match artifact directory",
    )


def audit(directory: Path, specification: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    try:
        directory = artifact_path(directory)
        require(
            len(directory.relative_to(ARTIFACT_ROOT.resolve()).parts) == 2,
            "audit: expected ticker/date run directory",
        )
        evidence_path = index_path(directory / "data" / "evidence.json")
        calculation_path = index_path(directory / "data" / "calculations.json")
        report_path = index_path(directory / "report.md")
        if not evidence_path.is_file():
            findings.append({"severity": "warning", "message": "missing evidence.json"})
        else:
            evidence = load_json(evidence_path)
            findings.extend(validate_evidence(evidence, specification["policy"]))
            check_identity(evidence, directory)
            expected = calculate(evidence)
            if not calculation_path.is_file():
                findings.append(
                    {"severity": "warning", "message": "missing calculations.json"}
                )
            else:
                require(
                    load_json(calculation_path) == expected,
                    "calculations.json does not match deterministic recomputation",
                )
            deviation = expected["metrics"]["market_cap_deviation"]
            if deviation is not None and decimal(deviation, "deviation") > decimal(
                specification["policy"]["market_cap_tolerance"], "tolerance"
            ):
                findings.append(
                    {
                        "severity": "warning",
                        "message": (
                            "price times shares disagrees with reported market cap "
                            "beyond tolerance"
                        ),
                    }
                )
        if not report_path.is_file():
            findings.append({"severity": "warning", "message": "missing report.md"})
        else:
            report = report_path.read_text(encoding="utf-8")
            headings, populated = report_sections(report)
            required = [node["section"] for node in specification["nodes"]]
            require(
                headings == required,
                "report sections must match ordered graph sections",
            )
            for section in required:
                if section not in populated:
                    findings.append(
                        {
                            "severity": "warning",
                            "message": f"missing/empty section: {section}",
                        }
                    )
            if evidence_path.is_file():
                for source in evidence["sources"]:
                    if not re.search(
                        r"(?<![\w-])" + re.escape(source["id"]) + r"(?![\w-])", report
                    ):
                        findings.append(
                            {
                                "severity": "warning",
                                "message": (
                                    "report missing source citation " f"{source['id']}"
                                ),
                            }
                        )
    except (InvalidDocument, OSError, UnicodeError) as exc:
        findings.append({"severity": "error", "message": str(exc)})
    status = (
        "BLOCKED"
        if any(item["severity"] == "error" for item in findings)
        else "PROVISIONAL" if findings else "PASS"
    )
    return {
        "schema_version": 1,
        "status": status,
        "findings": findings,
        "scope": (
            "Offline structural, citation-presence and arithmetic consistency "
            "audit only; not independent verification of source truth, "
            "investment advice, or authorization to trade."
        ),
    }


def persist(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


NATIVE_ARTIFACTS = {
    "evidence.json": "data/evidence.json",
    "calculations.json": "data/calculations.json",
    "report.md": "report.md",
    "audit.json": "data/audit.json",
}


def index_path(path: Path) -> Path:
    """Reject aliases and escapes for both existing inputs and generated outputs."""
    root = RESEARCH_ROOT.absolute()
    require(not root.is_symlink(), "index: symlink root refused")
    canonical_root = root.resolve()
    candidate = path.absolute()
    if candidate.is_relative_to(root):
        candidate = canonical_root / candidate.relative_to(root)
    require(candidate.is_relative_to(canonical_root), "index: path outside research")
    for component in candidate.relative_to(canonical_root).parents:
        require(
            not (canonical_root / component).is_symlink(),
            "index: symlink directory refused",
        )
    require(not candidate.is_symlink(), "index: symlink file/directory refused")
    return confined(candidate, canonical_root)


def report_sections(report: str) -> tuple[list[str], set[str]]:
    """Only actual, non-fenced level-two headings count as graph sections."""
    headings: list[str] = []
    populated: set[str] = set()
    current: str | None = None
    fence: str | None = None
    for line in report.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        heading = re.fullmatch(r"##\s+(.+?)\s*", line)
        if heading:
            current = heading[1]
            headings.append(current)
        elif current is not None and line.strip():
            populated.add(current)
    return headings, populated


def index_run(directory: Path, specification: dict[str, Any]) -> dict[str, Any]:
    directory = artifact_path(index_path(directory))
    require(
        len(directory.relative_to(ARTIFACT_ROOT.resolve()).parts) == 2,
        "index: expected ticker/date run directory",
    )
    paths = {
        name: index_path(directory / relative)
        for name, relative in NATIVE_ARTIFACTS.items()
    }
    legacy = index_path(directory / "archive" / "claude-trial.md")
    require(
        not legacy.exists() or legacy.is_file(),
        "index: expected file archive/claude-trial.md",
    )
    for path in paths.values():
        require(
            not path.exists() or path.is_file(), f"index: expected file {path.name}"
        )
    present = {name: path for name, path in paths.items() if path.is_file()}
    missing = [f"missing {name}" for name in NATIVE_ARTIFACTS if name not in present]
    evidence = None
    gaps = list(missing)
    evidence_provisional = False
    if "evidence.json" in present:
        evidence = load_json(present["evidence.json"])
        try:
            findings = validate_evidence(evidence, specification["policy"])
        except (KeyError, TypeError) as exc:
            raise InvalidDocument("index: malformed evidence structure") from exc
        check_identity(evidence, directory)
        gaps.extend(item["message"] for item in findings)
        evidence_provisional = bool(findings)
    calculations = None
    if "calculations.json" in present:
        calculations = load_json(present["calculations.json"])
        require(isinstance(calculations, dict), "index: calculations must be object")
        require(
            type(calculations.get("schema_version")) is int
            and calculations["schema_version"] == 1,
            "index: calculations schema",
        )
        require(
            calculations.get("ticker") == directory.parent.name
            and calculations.get("as_of") == directory.name,
            "index: calculations identity differs from ticker/date directory",
        )
        check_identity(
            {"ticker": calculations.get("ticker"), "as_of": calculations.get("as_of")},
            directory,
        )
        require(calculations.get("currency") == "USD", "index: calculations currency")
        metrics = calculations.get("metrics")
        require(isinstance(metrics, dict), "index: calculations metrics")
        for key in (
            "implied_market_cap",
            "market_cap_deviation",
            "free_cash_flow",
            "free_cash_flow_yield",
            "pe",
        ):
            require(key in metrics, f"index: missing calculation metric {key}")
            if metrics[key] is not None:
                decimal(metrics[key], f"index: metric {key}")
        require("valuation" in calculations, "index: missing calculation valuation")
        model = calculations.get("valuation")
        require(
            model is None or isinstance(model, dict), "index: calculation valuation"
        )
        if model is not None:
            decimal(model.get("weighted_present_target"), "index: weighted benchmark")
        if evidence is not None:
            require(
                calculations == calculate(evidence),
                "index: calculations.json does not match deterministic recomputation",
            )
    saved_audit = None
    if "audit.json" in present:
        saved_audit = load_json(present["audit.json"])
        require(isinstance(saved_audit, dict), "index: audit must be object")
        require(
            type(saved_audit.get("schema_version")) is int
            and saved_audit["schema_version"] == 1,
            "index: audit schema",
        )
        require(
            text(saved_audit.get("status"), "index: audit status")
            in {"PASS", "PROVISIONAL", "BLOCKED"},
            "index: invalid saved audit status",
        )
        findings = saved_audit.get("findings")
        require(isinstance(findings, list), "index: audit findings must be list")
        for finding in findings:
            require(isinstance(finding, dict), "index: audit finding must be object")
            require(
                text(finding.get("severity"), "index: audit finding severity")
                in {"warning", "error"},
                "index: audit finding severity",
            )
            gaps.append(text(finding.get("message"), "index: audit finding message"))
        expected_status = (
            "BLOCKED"
            if any(item["severity"] == "error" for item in findings)
            else "PROVISIONAL" if findings else "PASS"
        )
        require(
            saved_audit["status"] == expected_status,
            "index: saved audit status disagrees with its findings",
        )
    headings, populated = (
        report_sections(present["report.md"].read_text(encoding="utf-8"))
        if "report.md" in present
        else ([], set())
    )
    required = [node["section"] for node in specification["nodes"]]
    covered = {section for section in required if section in populated}
    gaps.extend(
        f"missing/empty section: {section}"
        for section in required
        if section not in covered
    )
    if "report.md" in present and headings != required:
        gaps.append("report section order/headings differ from graph")
    complete = not missing and covered == set(required) and headings == required
    status = "UNRUN" if saved_audit is None else f"saved {saved_audit['status']}"
    if evidence_provisional:
        status += "; evidence PROVISIONAL"
    if not complete:
        status += "; INCOMPLETE native artifacts/sections"
    return {
        "directory": directory,
        "ticker": directory.parent.name,
        "date": directory.name,
        "present": present,
        "legacy": legacy if legacy.is_file() else None,
        "evidence": evidence,
        "calculations": calculations,
        "audit": saved_audit,
        "headings": headings,
        "covered": covered,
        "complete": complete,
        "status": status,
        "gaps": list(dict.fromkeys(gaps)),
    }


def index(specification: dict[str, Any]) -> dict[str, int]:
    """Render one index from saved artifacts, preserving authored run guidance."""
    root = index_path(RESEARCH_ROOT)
    artifacts = index_path(ARTIFACT_ROOT)
    output = index_path(root / "index.md")
    require(not output.exists() or output.is_file(), "index: output must be file")
    guidance = index_path(root / "README.md")
    require(guidance.is_file(), "index: missing authored README.md run guidance")
    records: list[dict[str, Any]] = []
    batches: set[str] = set()

    def date_directories(parent: Path) -> list[Path]:
        if not parent.exists():
            return []
        require(parent.is_dir(), f"index: expected directory {parent.name}")
        found = []
        for candidate in sorted(parent.iterdir(), reverse=True):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", candidate.name):
                continue
            iso_date(candidate.name, "index: date directory")
            candidate = index_path(candidate)
            require(candidate.is_dir(), "index: date entry must be directory")
            found.append(candidate)
        return found

    require(root.is_dir(), "index: research root must be directory")
    if artifacts.exists():
        require(artifacts.is_dir(), "index: tickers root must be directory")
        for ticker in sorted(artifacts.iterdir()):
            if not re.fullmatch(r"[A-Z][A-Z0-9.-]*", ticker.name):
                continue
            ticker = index_path(ticker)
            if not ticker.is_dir():
                continue
            for directory in date_directories(ticker):
                records.append(index_run(directory, specification))
                batches.add(directory.name)
    shared = index_path(root / "batches")
    batches.update(directory.name for directory in date_directories(shared))

    def cell(value: Any) -> str:
        result = str(value).replace("\\", "\\\\")
        for character in ("|", "[", "]", "`"):
            result = result.replace(character, "\\" + character)
        return (
            result.replace("\n", " ")
            .replace("\r", " ")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    def link(target: Path, label: str) -> str:
        relative = target.relative_to(root).as_posix()
        return f"[{cell(label)}]({quote(relative, safe='/')})"

    def report_link(record: dict[str, Any], label: str) -> str:
        report = record["present"].get("report.md")
        return (
            link(report, label)
            if report is not None
            else f"{cell(label)} (MISSING report)"
        )

    def data_links(record: dict[str, Any]) -> str:
        return " · ".join(
            (
                link(record["present"][name], name.removesuffix(".json"))
                if name in record["present"]
                else f"MISSING {name}"
            )
            for name in ("evidence.json", "calculations.json", "audit.json")
        )

    def latest_report(ticker: str) -> dict[str, Any]:
        history = [record for record in records if record["ticker"] == ticker]
        reports = [record for record in history if "report.md" in record["present"]]
        return max(reports or history, key=lambda record: record["date"])

    sections = len(specification["nodes"])
    lines = [
        "# Research index",
        "",
        link(guidance, "Run guidance"),
        "",
        "Saved audits describe historical offline structure/arithmetic, not source "
        "truth or investment approval; coverage counts nonempty graph sections, "
        "not verification. Conditional model targets are earnings-multiple "
        "USD/share outputs, not DCFs, fair values or guaranteed outcomes; display "
        "rounding does not change full precision, source periods or timestamps "
        "retained in the data and reports.",
        "",
        "Targets are probability-weighted discounted present values, not future "
        "trading prices. The model horizon is an assumption in years, used for "
        "EPS growth, discounting and conditional price CAGR. Model EPS anchor "
        "periods and reported/estimated/assumed kinds are shown below: alignment "
        "with a future price exit requires an explicit convention. Price CAGR "
        "is not EPS growth or observed YoY performance; missing alignment "
        "keeps audits PROVISIONAL.",
        "",
        "Dates: "
        + " · ".join(f"[{batch}](#{batch})" for batch in sorted(batches, reverse=True)),
        "",
        "Latest reports: "
        + " · ".join(
            report_link(latest_report(ticker), ticker)
            for ticker in sorted({record["ticker"] for record in records})
        ),
    ]

    for batch in sorted(batches, reverse=True):
        selected = sorted(
            (record for record in records if record["date"] == batch),
            key=lambda record: record["ticker"],
        )
        lines.extend(
            [
                "",
                f"## {batch}",
                "",
                f"Research reference date: **{batch}**. Present-value targets "
                "use the configured discount periods; terminal timing must be "
                "declared separately and remains conditional.",
                "",
                "| Ticker / report | USD price | Actual quote date "
                "| Present-value target USD/share | EPS anchor period / kind "
                "| Assumed model horizon | Saved audit | Sections | Data artifacts |",
                "|---|---|---|---|---|---|---|---|---|",
            ]
        )
        for record in selected:
            evidence = record["evidence"]
            price = None if evidence is None else evidence["facts"].get("price")
            quote_date = (
                "unavailable" if evidence is None else evidence["quote_time"][:10]
            )
            if price is None or price["value"] is None:
                price_display = "unavailable"
            else:
                price_display = cell(f"{price['value']} ({price['kind']})")
                if price["period"] != evidence["quote_time"][:10]:
                    quote_date += f"; price period {price['period']}"
            calculations = record["calculations"]
            model = None if calculations is None else calculations.get("valuation")
            model_horizon = "not specified"
            source_model = None if evidence is None else evidence.get("valuation")
            eps_period = "not modeled"
            if source_model is not None:
                years = source_model["scenarios"][0]["years"]
                base_fact = evidence["facts"][source_model["base_eps"]]
                eps_period = cell(f"{base_fact['period']} ({base_fact['kind']})")
                timing = source_model.get("timing")
                model_horizon = (
                    f"{years} years assumed; EPS/exit alignment unresolved"
                    if timing is None
                    else f"{years} years → {timing['terminal_date']} (assumed)"
                )
            model_target = "not modeled"
            if model is not None:
                value = decimal(
                    model["weighted_present_target"], "weighted model target"
                )
                model_target = f"{value:.2f}"
            lines.append(
                f"| {report_link(record, record['ticker'])} | "
                f"{price_display} | {cell(quote_date)} | {model_target} "
                f"| {eps_period} | {model_horizon} | "
                f"{cell(record['status'])} | {len(record['covered'])}/{sections} | "
                f"{data_links(record)} |"
            )
        if not selected:
            lines.append("")
            lines.append("No native ticker runs saved for this date.")

        lines.extend(["", "### Evidence gaps", ""])
        grouped_gaps: dict[str, list[str]] = {}
        for record in selected:
            for gap in record["gaps"]:
                grouped_gaps.setdefault(gap, []).append(record["ticker"])
        lines.extend(
            f"- {', '.join(tickers_with_gap)}: {cell(gap)}"
            for gap, tickers_with_gap in grouped_gaps.items()
        )
        if not grouped_gaps:
            lines.append(
                "No recorded structural/evidence-contract gaps."
                if selected
                else "No native runs to assess."
            )

        baselines = [record for record in selected if record["legacy"] is not None]
        if baselines:
            lines.extend(["", "### Imported baseline archives", ""])
            lines.extend(
                "- "
                + link(
                    record["legacy"],
                    f"{record['ticker']} / {record['legacy'].name}",
                )
                + " — historical imported material, not native coverage or audit."
                for record in baselines
            )

        lines.extend(["", "### Shared materials", ""])
        batch_directory = index_path(shared / batch)
        require(
            not batch_directory.exists() or batch_directory.is_dir(),
            "index: batch entry must be directory",
        )
        candidates = (
            sorted(batch_directory.iterdir()) if batch_directory.exists() else []
        )
        shared_names = set()
        for candidate in candidates:
            if candidate.name == "README.md" or not candidate.is_file():
                continue
            target = index_path(candidate)
            name = target.name
            shared_names.add(name)
            if target.suffix == ".json":
                require(
                    isinstance(load_json(target), dict),
                    f"index: {name} must be object",
                )
            lines.append("- " + link(target, name))
        if selected:
            for name in (
                "market-context.json",
                "verification.json",
                "corroboration-review.md",
            ):
                if name not in shared_names:
                    lines.append(f"- {name}: MISSING")

        archive = index_path(batch_directory / "archive")
        if archive.exists():
            require(archive.is_dir(), "index: batch archive must be directory")
            historical = []
            for candidate in sorted(archive.iterdir()):
                candidate = index_path(candidate)
                if candidate.is_file():
                    historical.append(candidate)
            if historical:
                lines.extend(["", "### Historical materials", ""])
                lines.extend(
                    "- "
                    + link(target, target.name)
                    + " — archived, not current verification."
                    for target in historical
                )

    # Every input and the sole destination are validated before any write.
    descriptor, temporary_name = tempfile.mkstemp(
        dir=root, prefix=".index-", suffix=".tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write("\n".join([*lines, ""]))
        index_path(output)
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    return {
        "generated_files": 1,
        "research_runs": len(records),
        "date_batches": len(batches),
    }


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> Never:
        print(json.dumps({"status": "BLOCKED", "error": message}))
        raise SystemExit(2)


def main(argv: list[str] | None = None) -> int:
    parser = JsonArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("graph")
    commands.add_parser("index")
    plan = commands.add_parser("plan")
    plan.add_argument("--tickers", nargs="+", required=True)
    plan.add_argument("--as-of", required=True)
    plan.add_argument("--skills", nargs="+", default=[])
    calc = commands.add_parser("calculate")
    calc.add_argument("evidence")
    calc.add_argument("--output", required=True)
    gate = commands.add_parser("audit")
    gate.add_argument("directory")
    gate.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        specification = graph()
        if args.command == "graph":
            result = specification
        elif args.command == "index":
            result = index(specification)
        elif args.command == "plan":
            iso_date(args.as_of, "as_of")
            require(
                all(
                    bool(re.fullmatch(r"[A-Z][A-Z0-9.-]*", ticker))
                    for ticker in args.tickers
                ),
                "plan: invalid ticker",
            )
            require(
                len(set(args.tickers)) == len(args.tickers), "plan: duplicate tickers"
            )
            selected = set(args.skills)
            available = {row["id"] for row in specification["extensions"]}
            require(
                selected <= available,
                f"plan: unknown research skills {sorted(selected - available)}",
            )
            require(
                len(selected) == len(args.skills), "plan: duplicate research skills"
            )
            selected_extensions = [
                {**extension, "requires": node["requires"]}
                for node in specification["nodes"]
                for extension in specification["extensions"]
                if extension["node"] == node["id"] and extension["id"] in selected
            ]
            result = {
                "graph": specification,
                "artifacts": [
                    {
                        "ticker": ticker,
                        "directory": f"docs/research/tickers/{ticker}/{args.as_of}",
                        "skills": [
                            {
                                **extension,
                                "artifacts": [
                                    f"docs/research/tickers/{ticker}/"
                                    f"{args.as_of}/{name}"
                                    for name in extension["artifacts"]
                                ],
                            }
                            for extension in selected_extensions
                        ],
                    }
                    for ticker in args.tickers
                ],
            }
        elif args.command == "calculate":
            source, output = artifact_path(args.evidence), artifact_path(args.output)
            require(
                source.name == "evidence.json"
                and output.name == "calculations.json"
                and source.parent == output.parent
                and source.parent.name == "data",
                "calculate: expected ticker/date/data/evidence.json and "
                "its data/calculations.json",
            )
            evidence = load_json(source)
            validate_evidence(evidence, specification["policy"])
            check_identity(evidence, source.parent.parent)
            result = calculate(evidence)
            persist(output, result)
        else:
            directory, output = artifact_path(args.directory), artifact_path(
                args.output
            )
            require(
                len(directory.relative_to(ARTIFACT_ROOT.resolve()).parts) == 2
                and output == directory / "data" / "audit.json",
                "audit: expected ticker/date run directory and its data/audit.json",
            )
            require(directory.is_dir(), "audit: run directory does not exist")
            result = audit(directory, specification)
            persist(output, result)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if args.command != "audit" or result["status"] == "PASS" else 1
    except (InvalidDocument, OSError, UnicodeError, InvalidOperation) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
