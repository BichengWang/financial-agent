"""Harness CLI: the tool surface any agent runtime can call from a shell.

    python -m financial_agent.harness skills validate
    python -m financial_agent.harness skills catalog
    python -m financial_agent.harness audit --output-dir agents/equity/output
    python -m financial_agent.harness gate agents/equity/output/<model>-<date>
    python -m financial_agent.harness run --model <id> --date <YYYY-MM-DD>
    python -m financial_agent.harness manifest agents/equity/output/<model>-<date>
    python -m financial_agent.harness hash agents/equity/output/<model>-<date>
    python -m financial_agent.harness clones --since 2026-07-31
    python -m financial_agent.harness policy-check OLD.toml NEW.toml --settled-n 20

Exit status is non-zero when a check fails, so a skill, a CI job, or a
PreToolUse hook can use the command as a gate.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from financial_agent.harness.audit import audit_output_dir
from financial_agent.harness.fingerprint import (
    artifact_digests,
    find_clones,
    package_digest,
)
from financial_agent.harness.gates import publish_gate, replay_status
from financial_agent.harness.lifecycle import RunState
from financial_agent.harness.manifest import render_manifest_sections
from financial_agent.harness.policy import MutationEvidence, check_mutation, load_policy
from financial_agent.harness.runner import DEFAULT_HANDLERS, RunLocked, run
from financial_agent.harness.skills import CHARS_PER_TOKEN, SkillRegistry

DEFAULT_SKILL_ROOTS = (
    Path("skills"),
    Path(".claude/skills"),
    Path("agents/equity/turtle-trader"),
)


def _registry(roots: list[Path] | None) -> SkillRegistry:
    candidates = roots or [r for r in DEFAULT_SKILL_ROOTS if r.exists()]
    return SkillRegistry.discover(candidates, known_stages=[s.value for s in RunState])


def cmd_skills(args: argparse.Namespace) -> int:
    registry = _registry(args.root)
    if args.action == "catalog":
        catalog = registry.catalog_xml()
        print(catalog)
        print(
            f"<!-- {len(registry.skills)} skills, ~{len(catalog) // CHARS_PER_TOKEN} "
            "tokens at level 1 -->"
        )
        return 0
    failed = False
    for result in registry.results:
        status = "OK" if result.ok else "INVALID"
        print(f"{status:8} {result.path}")
        for error in result.errors:
            print(f"  error: {error}")
        for warning in result.warnings:
            print(f"  warn:  {warning}")
        failed = failed or not result.ok
    return 1 if failed else 0


def cmd_audit(args: argparse.Namespace) -> int:
    report = audit_output_dir(
        args.output_dir, load_policy(args.policy), as_of=args.as_of
    )
    print(report.to_markdown())
    errors = [f for f in report.findings if f.severity == "error"]
    return 1 if errors and args.strict else 0


def cmd_gate(args: argparse.Namespace) -> int:
    policy = load_policy(args.policy)
    failures = publish_gate(args.package, policy)
    replay = replay_status(args.package, policy)
    if replay is not None:
        print(f"investable (recomputed): {len(replay.investable)} {replay.investable}")
        print(
            f"status replay: {replay.decision.status.value} "
            f"({'; '.join(replay.decision.reasons)}); "
            f"published: {replay.published}; Required inputs assumed grounded"
        )
    print(f"content hash: sha256:{package_digest(args.package)}")
    for failure in failures:
        print(f"GATE FAIL: {failure}")
    print("publish gate:", "FAIL" if failures else "PASS")
    return 1 if failures else 0


def cmd_run(args: argparse.Namespace) -> int:
    try:
        report = run(args.model, args.date, args.output_dir, DEFAULT_HANDLERS)
    except RunLocked as exc:
        print(f"LOCKED: {exc}")
        return 2
    print(report.lifecycle.transcript())
    for failure in report.gate_failures:
        print(f"GATE FAIL: {failure}")
    if report.published:
        print(f"run {report.run_id}: {report.lifecycle.status}")
        return 0
    print(f"run {report.run_id}: HALTED: {report.halt_reason}")
    return 1


def cmd_manifest(args: argparse.Namespace) -> int:
    text, failures = render_manifest_sections(args.package, load_policy(args.policy))
    print(text)
    return 1 if failures else 0


def cmd_hash(args: argparse.Namespace) -> int:
    for name, digest in artifact_digests(args.package).items():
        print(f"{digest}  {name}")
    print(f"content hash: sha256:{package_digest(args.package)}")
    return 0


def cmd_clones(args: argparse.Namespace) -> int:
    clones = find_clones(args.output_dir, since=args.since)
    for (name, digest), packages in sorted(clones.items()):
        print(f"{name} {digest[:12]}: {', '.join(packages)}")
    print(f"{len(clones)} artifact(s) shared between packages")
    return 1 if clones and args.strict else 0


def cmd_policy_check(args: argparse.Namespace) -> int:
    verdict = check_mutation(
        load_policy(args.old),
        load_policy(args.new),
        MutationEvidence(
            settled_n=args.settled_n,
            eff_n=args.eff_n,
            human_approved=args.human_approved,
        ),
    )
    print(f"decision: {verdict.decision}")
    for key in verdict.changed:
        print(f"  changed: {key}")
    for reason in verdict.reasons:
        print(f"  reason:  {reason}")
    return 0 if verdict.decision in {"NO_CHANGE", "ACCEPTABLE"} else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m financial_agent.harness")
    sub = parser.add_subparsers(dest="command", required=True)

    skills = sub.add_parser("skills", help="validate skills or print the catalog")
    skills.add_argument("action", choices=["validate", "catalog"])
    skills.add_argument("--root", type=Path, action="append")
    skills.set_defaults(func=cmd_skills)

    audit = sub.add_parser("audit", help="conformance audit of prediction ledgers")
    audit.add_argument("--output-dir", type=Path, default=Path("agents/equity/output"))
    audit.add_argument("--as-of", help="only packages dated on or before YYYY-MM-DD")
    audit.add_argument("--policy", type=Path)
    audit.add_argument("--strict", action="store_true", help="exit 1 on any error")
    audit.set_defaults(func=cmd_audit)

    gate = sub.add_parser("gate", help="publish gate + status replay for a package")
    gate.add_argument("package", type=Path)
    gate.add_argument("--policy", type=Path)
    gate.set_defaults(func=cmd_gate)

    run_parser = sub.add_parser("run", help="drive one run through the lifecycle")
    run_parser.add_argument("--model", required=True)
    run_parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    run_parser.add_argument(
        "--output-dir", type=Path, default=Path("agents/equity/output")
    )
    run_parser.set_defaults(func=cmd_run)

    manifest = sub.add_parser("manifest", help="generated manifest sections")
    manifest.add_argument("package", type=Path)
    manifest.add_argument("--policy", type=Path)
    manifest.set_defaults(func=cmd_manifest)

    digest = sub.add_parser("hash", help="per-artifact and package content hashes")
    digest.add_argument("package", type=Path)
    digest.set_defaults(func=cmd_hash)

    clones = sub.add_parser("clones", help="artifacts shared between packages")
    clones.add_argument("--output-dir", type=Path, default=Path("agents/equity/output"))
    clones.add_argument("--since", help="only packages dated on or after YYYY-MM-DD")
    clones.add_argument("--strict", action="store_true", help="exit 1 on any clone")
    clones.set_defaults(func=cmd_clones)

    check = sub.add_parser("policy-check", help="govern a proposed policy change")
    check.add_argument("old", type=Path)
    check.add_argument("new", type=Path)
    check.add_argument("--settled-n", type=int, default=0)
    check.add_argument("--eff-n", type=int, default=0)
    check.add_argument("--human-approved", action="store_true")
    check.set_defaults(func=cmd_policy_check)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result: int = args.func(args)
    return result


if __name__ == "__main__":
    sys.exit(main())
