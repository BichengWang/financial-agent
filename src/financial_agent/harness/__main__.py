"""Harness CLI: the tool surface any agent runtime can call from a shell.

    python -m financial_agent.harness skills validate
    python -m financial_agent.harness skills catalog
    python -m financial_agent.harness audit --output-dir agents/equity/output
    python -m financial_agent.harness gate agents/equity/output/<model>-<date> [--json]
    python -m financial_agent.harness replay --since 2026-07-31
    python -m financial_agent.harness schema [<package>] [--json-schema]
    python -m financial_agent.harness session <YYYY-MM-DD>
    python -m financial_agent.harness reachability [--families tech_z macro_z]
    python -m financial_agent.harness kernel {equity,market,risk} --input FILE
    python -m financial_agent.harness run --model <id> --date <YYYY-MM-DD>
    python -m financial_agent.harness manifest agents/equity/output/<model>-<date>
    python -m financial_agent.harness hash agents/equity/output/<model>-<date>
    python -m financial_agent.harness clones --since 2026-07-31
    python -m financial_agent.harness policy-check OLD.toml NEW.toml --settled-n 20
    python -m financial_agent.harness mcp

Exit status is non-zero when a check fails, so a skill, a CI job, or a
PreToolUse hook can use the command as a gate.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from financial_agent.harness.audit import audit_output_dir
from financial_agent.harness.fingerprint import (
    artifact_digests,
    find_clones,
    package_digest,
)
from financial_agent.harness.gates import (
    PREDICTIONS_FILE,
    go_reachability,
    publish_gate,
    replay_history,
    replay_status,
)
from financial_agent.harness.kernels import (
    EquityInputs,
    KernelError,
    MarketInputs,
    equity_record,
    market_forecast_records,
    price_risk,
)
from financial_agent.harness.lifecycle import RunState
from financial_agent.harness.manifest import (
    gate_report,
    render_manifest_sections,
    replay_lines,
)
from financial_agent.harness.market_calendar import session
from financial_agent.harness.policy import (
    FAMILIES,
    MutationEvidence,
    check_mutation,
    load_policy,
)
from financial_agent.harness.runner import RunLocked, default_handlers, run
from financial_agent.harness.schema import json_schema, validate_payload
from financial_agent.harness.skills import CHARS_PER_TOKEN, SkillRegistry

DEFAULT_SKILL_ROOTS = (
    Path("skills"),
    Path(".claude/skills"),
    Path("agents/equity/turtle-trader"),
)


def _registry(roots: list[Path] | None) -> SkillRegistry:
    candidates = roots or [r for r in DEFAULT_SKILL_ROOTS if r.exists()]
    return SkillRegistry.discover(
        candidates,
        known_stages=[s.value for s in RunState],
        known_tools=tool_names(),
    )


def tool_names() -> list[str]:
    """CLI subcommands: the names a skill's ``fa-tools`` may bind to."""
    sub = next(
        a for a in build_parser()._actions if isinstance(a, argparse._SubParsersAction)
    )
    return sorted(sub.choices)


def _print_json(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=False, default=str))


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
    if args.json:
        report = gate_report(args.package, policy)
        _print_json(report)
        return 0 if report["pass"] else 1
    failures = publish_gate(args.package, policy)
    replay = replay_status(args.package, policy)
    if replay is not None:
        print(f"investable (recomputed): {len(replay.investable)} {replay.investable}")
        print(
            f"status replay: {replay.decision.status.value} "
            f"({'; '.join(replay.decision.reasons)}); "
            f"published: {replay.published}; Required inputs assumed grounded"
        )
        for line in replay_lines(replay):
            print(line)
    print(f"content hash: sha256:{package_digest(args.package)}")
    for failure in failures:
        print(f"GATE FAIL: {failure}")
    print("publish gate:", "FAIL" if failures else "PASS")
    return 1 if failures else 0


def cmd_replay(args: argparse.Namespace) -> int:
    replays = replay_history(
        args.output_dir, load_policy(args.policy), since=args.since, as_of=args.as_of
    )
    agree = [name for name, replay in replays if replay.agrees]
    print("| package | session | replay | published | reasons |")
    print("|---|---|---|---|---|")
    for name, replay in replays:
        if replay.agrees and not args.all:
            continue
        kind = replay.session.kind if replay.session else "-"
        reasons = "; ".join(replay.decision.reasons).replace("|", "\\|")
        print(
            f"| {name} | {kind} | {replay.decision.status.value} | "
            f"{replay.published} | {reasons} |"
        )
    print()
    print(
        f"{len(agree)} of {len(replays)} replayed packages agree with their "
        "published status (Required inputs assumed grounded)."
    )
    return 1 if args.strict and len(agree) < len(replays) else 0


def cmd_schema(args: argparse.Namespace) -> int:
    policy = load_policy(args.policy)
    if args.json_schema or args.package is None:
        _print_json(json_schema(policy))
        return 0
    path = args.package / PREDICTIONS_FILE
    if not path.exists():
        print(f"{path}: not found")
        return 1
    payload = json.loads(path.read_text(encoding="utf-8"))
    declared = isinstance(payload, dict) and "schema_version" in payload
    findings = validate_payload(payload, policy)
    for finding in findings:
        print(f"v1: {finding}")
    label = "declares" if declared else "legacy ledger, does not declare"
    print(f"{path}: {label} schema_version; {len(findings)} v1 finding(s)")
    return 1 if findings else 0


def cmd_session(args: argparse.Namespace) -> int:
    day = session(args.date)
    print(f"{day.kind} {day.describe()}")
    return 0


def cmd_reachability(args: argparse.Namespace) -> int:
    reach = go_reachability(
        load_policy(args.policy),
        available_families=args.families,
        ranked_names=args.ranked_names,
    )
    print(f"gating families: {', '.join(reach.gating_families) or 'none'}")
    for blocker in reach.blockers:
        print(f"BLOCKER: {blocker}")
    print("GO", "reachable" if reach.reachable else "unreachable")
    return 0 if reach.reachable else 1


def run_kernel(kind: str, request: dict[str, Any], policy: Any) -> Any:
    """Shared by the CLI and the MCP server; raises ``KernelError``."""
    if kind == "equity":
        return [
            equity_record(
                request["run_date"],
                request["model"],
                EquityInputs.from_mapping(item),
                policy,
            )
            for item in request["names"]
        ]
    if kind == "market":
        return market_forecast_records(
            request["run_date"],
            request["model"],
            request["regime"],
            [MarketInputs.from_mapping(item) for item in request["etfs"]],
            policy,
        )
    if kind == "risk":
        return vars(
            price_risk(
                request["closes"],
                request["spy_closes"],
                tlt_closes=request.get("tlt_closes"),
            )
        )
    raise KernelError(f"unknown kernel {kind!r}")


def cmd_kernel(args: argparse.Namespace) -> int:
    text = sys.stdin.read() if str(args.input) == "-" else args.input.read_text()
    try:
        _print_json(run_kernel(args.kind, json.loads(text), load_policy(args.policy)))
    except (KernelError, KeyError, TypeError, ValueError) as exc:
        print(f"KERNEL ERROR: {type(exc).__name__}: {exc}")
        return 1
    return 0


def cmd_mcp(args: argparse.Namespace) -> int:
    from financial_agent.harness.mcp import serve

    serve(sys.stdin, sys.stdout, output_dir=args.output_dir)
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    try:
        report = run(args.model, args.date, args.output_dir, default_handlers())
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
    gate.add_argument("--json", action="store_true", help="machine-readable report")
    gate.set_defaults(func=cmd_gate)

    replay = sub.add_parser("replay", help="status replay across the run history")
    replay.add_argument("--output-dir", type=Path, default=Path("agents/equity/output"))
    replay.add_argument("--since", help="only packages dated on or after YYYY-MM-DD")
    replay.add_argument("--as-of", help="only packages dated on or before YYYY-MM-DD")
    replay.add_argument("--all", action="store_true", help="list agreeing rows too")
    replay.add_argument("--policy", type=Path)
    replay.add_argument("--strict", action="store_true", help="exit 1 on a mismatch")
    replay.set_defaults(func=cmd_replay)

    schema = sub.add_parser("schema", help="validate a ledger against schema v1")
    schema.add_argument("package", type=Path, nargs="?")
    schema.add_argument("--json-schema", action="store_true", help="print the schema")
    schema.add_argument("--policy", type=Path)
    schema.set_defaults(func=cmd_schema)

    day = sub.add_parser("session", help="NYSE session type for a run date")
    day.add_argument("date", help="YYYY-MM-DD")
    day.set_defaults(func=cmd_session)

    reach = sub.add_parser("reachability", help="structural GO blockers")
    reach.add_argument("--families", nargs="*", choices=FAMILIES)
    reach.add_argument("--ranked-names", type=int)
    reach.add_argument("--policy", type=Path)
    reach.set_defaults(func=cmd_reachability)

    kernel = sub.add_parser("kernel", help="compute records or risk from JSON input")
    kernel.add_argument("kind", choices=["equity", "market", "risk"])
    kernel.add_argument("--input", type=Path, required=True, help="JSON file or -")
    kernel.add_argument("--policy", type=Path)
    kernel.set_defaults(func=cmd_kernel)

    mcp = sub.add_parser("mcp", help="serve the read-only tools over MCP (stdio)")
    mcp.add_argument("--output-dir", type=Path, default=Path("agents/equity/output"))
    mcp.set_defaults(func=cmd_mcp)

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
