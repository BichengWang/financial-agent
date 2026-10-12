"""Deterministic offline behavioral regressions.

Run with python3.12 -m unittest discover -s this directory.
"""

from __future__ import annotations

import copy
import importlib.util
import io
import json
import re
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from typing import cast
from unittest.mock import patch
from urllib.parse import unquote

SPEC = importlib.util.spec_from_file_location(
    "equity_research", Path(__file__).with_name("research.py")
)
assert SPEC is not None and SPEC.loader is not None
research = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(research)

POLICY = {
    "required_facts": list(research.REQUIRED),
    "max_quote_age_days": 7,
    "market_cap_tolerance": "0.01",
}
SECTIONS = [
    "Grounding",
    "Business",
    "Moat",
    "Management",
    "Inversion",
    "Industry",
    "Valuation",
    "Decision",
    "Limitations and audit",
]
GRAPH = {"policy": POLICY, "nodes": [{"section": section} for section in SECTIONS]}


def fixture() -> dict:
    sources = [
        {
            "id": source_id,
            "url": f"https://{source_id}.example/filing",
            "title": "Observed filing and quote",
            "publisher": publisher,
            "accessed_at": "2026-10-11",
            "excerpt": (
                "Price 100; shares 1000; market cap 100000; revenue 80000; "
                "net income 10000; operating cash flow 12000; "
                "capital expenditure 2000; cash 5000; debt 3000; EPS 10."
            ),
        }
        for source_id, publisher in [
            ("filing", "Company IR"),
            ("provider", "Independent Data Publisher"),
        ]
    ]
    values = {
        "price": "100",
        "shares": "1000",
        "market_cap": "100000",
        "revenue": "80000",
        "net_income": "10000",
        "operating_cash_flow": "12000",
        "capital_expenditure": "2000",
        "cash": "5000",
        "debt": "3000",
        "eps": "10",
    }
    facts = {}
    for name, value in values.items():
        period = "2026-10-11" if name in {"price", "shares", "market_cap"} else "FY2025"
        facts[name] = {
            "value": value,
            "unit": research.UNITS[name],
            "period": period,
            "kind": "reported",
            "sources": ["filing", "provider"],
            "note": "Observed in retained source excerpts.",
            "observations": [
                {"source": source_id, "value": value, "period": period}
                for source_id in ("filing", "provider")
            ],
        }
    sources.append(
        {
            "id": "treasury",
            "url": "https://treasury.example/yields",
            "title": "Contemporary Treasury yield",
            "publisher": "Treasury",
            "accessed_at": "2026-10-11",
            "excerpt": "Observed 10-year Treasury yield 4 percent on 2026-10-09.",
        }
    )
    facts["risk_free_rate"] = {
        "value": "0.04",
        "unit": "decimal",
        "period": "2026-10-09",
        "kind": "reported",
        "sources": ["treasury"],
        "note": "Contemporary observed 10-year yield.",
    }
    facts["required_return"] = {
        "value": "0.10",
        "unit": "decimal",
        "period": "5-year model",
        "kind": "assumption",
        "sources": [],
        "note": (
            "Six percentage point premium over observed Treasury yield "
            "for equity risk."
        ),
    }
    return {
        "schema_version": 1,
        "ticker": "TEST",
        "as_of": "2026-10-11",
        "currency": "USD",
        "quote_time": "2026-10-11T12:00:00+00:00",
        "sources": sources,
        "facts": facts,
        "valuation": {
            "base_eps": "eps",
            "discount_rate": "required_return",
            "risk_free_rate": "risk_free_rate",
            "timing": {
                "kind": "assumption",
                "valuation_date": "2026-10-11",
                "terminal_date": "2031-10-11",
                "eps_basis": "normalized_run_rate",
                "alignment_note": "FY2025 EPS is an assumed current run-rate proxy; "
                "terminal EPS and trailing exit P/E use five calendar years.",
            },
            "scenarios": [
                {
                    "name": name,
                    "growth": growth,
                    "exit_multiple": multiple,
                    "years": 5,
                    "probability": weight,
                }
                for name, growth, multiple, weight in [
                    ("bear", "0", "8", "0.25"),
                    ("base", "0.05", "10", "0.50"),
                    ("bull", "0.10", "12", "0.25"),
                ]
            ],
        },
    }


class ResearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.artifact_root = self.root / "tickers"
        self.directory = self.artifact_root / "TEST" / "2026-10-11"
        self.directory.mkdir(parents=True)
        self.data = self.directory / "data"
        self.guidance = self.root / "README.md"
        self.guidance.write_bytes(
            b"# Author-written guidance\nKeep these instructions.\n"
        )
        self.guidance_before = self.guidance.read_bytes()
        self.root_patch = patch.object(research, "RESEARCH_ROOT", self.root)
        self.artifact_patch = patch.object(
            research, "ARTIFACT_ROOT", self.artifact_root
        )
        self.root_patch.start()
        self.artifact_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.addCleanup(self.artifact_patch.stop)
        self.addCleanup(self.temp.cleanup)
        self.evidence = fixture()

    def save(self, evidence: dict | None = None) -> None:
        evidence = self.evidence if evidence is None else evidence
        research.persist(self.data / "evidence.json", evidence)
        research.persist(self.data / "calculations.json", research.calculate(evidence))
        (self.directory / "report.md").write_text(
            "\n".join(
                f"## {section}\nAnalysis [filing] [provider] [treasury].\n"
                for section in SECTIONS
            ),
            encoding="utf-8",
        )

    def status(self) -> str:
        return cast(str, research.audit(self.directory, GRAPH)["status"])

    def test_grounded_fixture_and_calculation(self) -> None:
        self.assertEqual(research.validate_evidence(self.evidence, POLICY), [])
        self.save()
        self.assertEqual(self.status(), "PASS")
        calculations = research.calculate(self.evidence)
        self.assertEqual(calculations["metrics"]["implied_market_cap"], "100000")
        self.assertEqual(calculations["metrics"]["free_cash_flow"], "10000")
        self.assertEqual(calculations["metrics"]["pe"], "10")
        self.assertEqual(
            calculations["valuation"]["scenarios"][0]["target_price"], "80"
        )

    def test_empty_sections_are_provisional_and_fenced_headings_are_not_sections(
        self,
    ) -> None:
        self.save()
        report = self.directory / "report.md"
        body = report.read_text()
        report.write_text(body + "\n```text\n## Quoted source heading\n```\n")
        self.assertEqual(self.status(), "PASS")
        report.write_text("\n".join(f"## {section}\n" for section in SECTIONS))
        self.assertEqual(self.status(), "PROVISIONAL")

    def test_malformed_fact_unit_and_kind_are_validation_errors(self) -> None:
        for field in ("unit", "kind"):
            with self.subTest(field=field):
                evidence = fixture()
                evidence["facts"]["price"][field] = []
                with self.assertRaises(research.InvalidDocument):
                    research.validate_evidence(evidence, POLICY)

    def test_invalid_scenario_boundaries_are_blocked(self) -> None:
        for field, value in (
            ("probability", "-0.1"),
            ("probability", "0.3"),
            ("growth", "-1"),
            ("exit_multiple", "0"),
            ("years", 0),
            ("years", 4),
            ("years", True),
            ("name", "base"),
        ):
            with self.subTest(field=field, value=value):
                evidence = fixture()
                evidence["valuation"]["scenarios"][0][field] = value
                with self.assertRaises(research.InvalidDocument):
                    research.validate_evidence(evidence, POLICY)
        evidence = fixture()
        evidence["valuation"]["scenarios"].pop()
        with self.assertRaises(research.InvalidDocument):
            research.validate_evidence(evidence, POLICY)

    def test_missing_run_audit_does_not_create_phantom_coverage(self) -> None:
        missing = self.artifact_root / "MISSING" / "2026-10-11"
        with patch.object(research, "graph", return_value=GRAPH):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(
                    research.main(
                        [
                            "audit",
                            str(missing),
                            "--output",
                            str(missing / "data/audit.json"),
                        ]
                    ),
                    1,
                )
        self.assertFalse(missing.exists())

    def test_stale_calculations_cannot_replace_the_existing_index(self) -> None:
        self.save()
        research.persist(
            self.data / "audit.json", research.audit(self.directory, GRAPH)
        )
        sentinel = self.root / "index.md"
        sentinel.write_text("Previous navigation.")
        calculations = research.calculate(self.evidence)
        calculations["valuation"]["weighted_present_target"] = "999999"
        research.persist(self.data / "calculations.json", calculations)
        with self.assertRaises(research.InvalidDocument):
            research.index(GRAPH)
        self.assertEqual(sentinel.read_text(), "Previous navigation.")
        self.assertFalse((self.artifact_root / "TEST" / "README.md").exists())

    def test_missing_timing_cannot_verify_dated_returns(self) -> None:
        del self.evidence["valuation"]["timing"]
        self.save()
        result = research.audit(self.directory, GRAPH)
        self.assertEqual(result["status"], "PROVISIONAL")

    def test_inconsistent_or_undefined_timing_is_blocked(self) -> None:
        for field, value in [
            ("valuation_date", "2026-10-09"),
            ("terminal_date", "2032-10-11"),
            ("terminal_date", "not-a-date"),
            ("eps_basis", "unspecified"),
            ("eps_basis", []),
            ("alignment_note", " "),
            ("kind", "reported"),
        ]:
            with self.subTest(field=field, value=value):
                evidence = fixture()
                evidence["valuation"]["timing"][field] = value
                self.save(evidence)
                self.assertEqual(self.status(), "BLOCKED")

    def test_price_cagr_uses_terminal_price_not_discounted_target(self) -> None:
        self.evidence["valuation"]["scenarios"][1].update(
            growth="0", exit_multiple="20"
        )
        base = research.calculate(self.evidence)["valuation"]["scenarios"][1]
        self.assertEqual(base["target_price"], "200")
        self.assertEqual(base["total_return"], "1")
        self.assertAlmostEqual(
            float(base["annualized_return"]), 2 ** (1 / 5) - 1, places=12
        )
        self.assertAlmostEqual(float(base["present_target"]), 200 / 1.1**5, places=12)

    def test_leap_day_terminal_anniversary(self) -> None:
        self.evidence["as_of"] = "2028-02-29"
        self.evidence["quote_time"] = "2028-02-29T12:00:00+00:00"
        self.evidence["facts"]["risk_free_rate"]["period"] = "2028-02-28"
        for source in self.evidence["sources"]:
            source["accessed_at"] = "2028-02-29"
        for name in ("price", "shares", "market_cap"):
            fact = self.evidence["facts"][name]
            fact["period"] = "2028-02-29"
            for observation in fact["observations"]:
                observation["period"] = "2028-02-29"
        self.evidence["valuation"]["timing"].update(
            valuation_date="2028-02-29", terminal_date="2033-02-28"
        )
        self.assertEqual(research.validate_evidence(self.evidence, POLICY), [])
        self.evidence["valuation"]["timing"]["terminal_date"] = "2033-03-01"
        with self.assertRaises(research.InvalidDocument):
            research.validate_evidence(self.evidence, POLICY)

    def test_stale_quote(self) -> None:
        self.evidence["quote_time"] = "2026-09-30T12:00:00+00:00"
        self.save()
        self.assertEqual(self.status(), "PROVISIONAL")
        record = research.index_run(self.directory, GRAPH)
        self.assertIn("PROVISIONAL", record["status"])

    def test_missing_evidence(self) -> None:
        self.assertEqual(self.status(), "PROVISIONAL")

    def test_units_and_incompatible_cashflow_periods(self) -> None:
        for key, field, value in [
            ("shares", "unit", "USD"),
            ("capital_expenditure", "period", "FY2024"),
        ]:
            with self.subTest(key=key):
                evidence = fixture()
                evidence["facts"][key][field] = value
                self.save(evidence)
                self.assertEqual(self.status(), "BLOCKED")

    def test_same_publisher_not_independent(self) -> None:
        self.evidence["sources"][1]["publisher"] = "  COMPANY   IR "
        self.save()
        self.assertEqual(self.status(), "PROVISIONAL")

    def test_missing_observations_not_verified(self) -> None:
        del self.evidence["facts"]["revenue"]["observations"]
        self.save()
        self.assertEqual(self.status(), "PROVISIONAL")

    def test_rounding_tolerance_and_disagreement(self) -> None:
        self.evidence["facts"]["revenue"]["observations"][1]["value"] = "80001"
        self.assertEqual(research.validate_evidence(self.evidence, POLICY), [])
        self.evidence["facts"]["revenue"]["observations"][1]["value"] = "90000"
        self.save()
        self.assertEqual(self.status(), "BLOCKED")

    def test_arithmetic_tampering(self) -> None:
        self.save()
        result = research.calculate(self.evidence)
        result["metrics"]["free_cash_flow"] = "99999"
        research.persist(self.data / "calculations.json", result)
        self.assertEqual(self.status(), "BLOCKED")

    def test_null_required_fact(self) -> None:
        self.evidence["facts"]["revenue"].update(
            value=None, kind="unavailable", observations=[]
        )
        self.save()
        self.assertEqual(self.status(), "PROVISIONAL")

    def test_rate_omission_and_staleness(self) -> None:
        for mutation in ("omitted", "unsourced", "stale", "insufficient_return"):
            with self.subTest(mutation=mutation):
                evidence = fixture()
                if mutation == "omitted":
                    del evidence["facts"]["risk_free_rate"]
                elif mutation == "unsourced":
                    evidence["facts"]["risk_free_rate"]["sources"] = []
                elif mutation == "stale":
                    evidence["facts"]["risk_free_rate"]["period"] = "2026-09-01"
                else:
                    evidence["facts"]["required_return"]["value"] = "0.03"
                self.save(evidence)
                self.assertEqual(self.status(), "BLOCKED")

    def test_malformed_and_omitted_valuation(self) -> None:
        self.save()
        (self.data / "evidence.json").write_text('{"facts":', encoding="utf-8")
        self.assertEqual(self.status(), "BLOCKED")
        del self.evidence["valuation"]
        self.save()
        self.assertEqual(self.status(), "PROVISIONAL")

    def test_forecast_estimate_is_not_gaap(self) -> None:
        self.evidence["facts"]["forward_eps"] = {
            "value": "12",
            "unit": "USD/share",
            "period": "FY2027 consensus as of 2026-10-11",
            "kind": "estimate",
            "sources": ["provider"],
            "note": "Contemporary analyst consensus; not reported GAAP.",
        }
        self.evidence["valuation"]["base_eps"] = "forward_eps"
        self.save()
        self.assertEqual(self.status(), "PASS")
        self.evidence["facts"]["forward_eps"]["kind"] = "reported"
        self.save()
        self.assertEqual(self.status(), "BLOCKED")

    def test_structural_errors(self) -> None:
        for key, value in [("sources", {}), ("facts", []), ("currency", "EUR")]:
            with self.subTest(key=key):
                evidence = copy.deepcopy(self.evidence)
                evidence[key] = value
                research.persist(self.data / "evidence.json", evidence)
                self.assertEqual(self.status(), "BLOCKED")

    def test_cli_calculation_and_gate(self) -> None:
        self.save()
        with patch.object(research, "graph", return_value=GRAPH):
            self.assertEqual(
                research.main(
                    [
                        "calculate",
                        str(self.data / "evidence.json"),
                        "--output",
                        str(self.data / "calculations.json"),
                    ]
                ),
                0,
            )
            self.assertEqual(
                research.main(
                    [
                        "audit",
                        str(self.directory),
                        "--output",
                        str(self.data / "audit.json"),
                    ]
                ),
                0,
            )
        self.assertEqual(
            json.loads((self.data / "audit.json").read_text())["status"], "PASS"
        )

    def test_cli_rejects_old_and_arbitrary_artifact_locations(self) -> None:
        self.save()
        with patch.object(research, "graph", return_value=GRAPH):
            for source, output in (
                (
                    self.root / "TEST" / "2026-10-11" / "data" / "evidence.json",
                    self.root / "TEST" / "2026-10-11" / "data" / "calculations.json",
                ),
                (
                    self.directory / "evidence.json",
                    self.directory / "calculations.json",
                ),
                (
                    self.directory / "other" / "evidence.json",
                    self.directory / "other" / "calculations.json",
                ),
                (
                    self.data / "nested" / "evidence.json",
                    self.data / "nested" / "calculations.json",
                ),
                (self.data / "evidence.json", self.directory / "calculations.json"),
            ):
                with self.subTest(source=source, output=output):
                    captured = io.StringIO()
                    with redirect_stdout(captured):
                        self.assertEqual(
                            research.main(
                                ["calculate", str(source), "--output", str(output)]
                            ),
                            1,
                        )
                    self.assertEqual(
                        json.loads(captured.getvalue())["status"], "BLOCKED"
                    )
            for directory, output in (
                (
                    self.root / "TEST" / "2026-10-11",
                    self.root / "TEST" / "2026-10-11" / "data" / "audit.json",
                ),
                (self.directory, self.directory / "audit.json"),
                (self.data, self.data / "audit.json"),
                (
                    self.directory,
                    self.artifact_root / "OTHER" / "2026-10-11" / "data" / "audit.json",
                ),
            ):
                with self.subTest(directory=directory, output=output):
                    captured = io.StringIO()
                    with redirect_stdout(captured):
                        self.assertEqual(
                            research.main(
                                ["audit", str(directory), "--output", str(output)]
                            ),
                            1,
                        )
                    self.assertEqual(
                        json.loads(captured.getvalue())["status"], "BLOCKED"
                    )
        self.assertFalse((self.data / "audit.json").exists())

    def test_data_sibling_symlink_is_refused_before_calculation_write(self) -> None:
        self.save()
        sibling = self.directory / "archive" / "evidence.json"
        research.persist(sibling, self.evidence)
        source = self.data / "evidence.json"
        source.unlink()
        source.symlink_to(sibling)
        output = self.data / "calculations.json"
        before = output.read_bytes()
        with patch.object(research, "graph", return_value=GRAPH):
            self.assertEqual(
                research.main(["calculate", str(source), "--output", str(output)]),
                1,
            )
        self.assertEqual(output.read_bytes(), before)
        self.assertEqual(self.status(), "BLOCKED")

    def test_paths_outside_artifact_root_rejected(self) -> None:
        with self.assertRaises(research.InvalidDocument):
            research.artifact_path(self.root.parent / "outside.json")

    def test_audit_rejects_artifact_symlink_outside_ticker_directory(self) -> None:
        self.save()
        external = self.root / "external.json"
        research.persist(external, self.evidence)
        evidence_path = self.data / "evidence.json"
        evidence_path.unlink()
        evidence_path.symlink_to(external)
        self.assertEqual(self.status(), "BLOCKED")

    def test_graph_cycle(self) -> None:
        skill = self.root / "skill"
        skill.mkdir()
        (skill / "instruction.txt").write_text("Read evidence.")
        names = [
            "grounding",
            "business",
            "moat",
            "management",
            "inversion",
            "industry",
            "valuation",
            "synthesis",
            "audit",
        ]
        graph = (
            "version = 1\n[policy]\nrequired_facts = "
            + json.dumps(list(research.REQUIRED))
            + '\nmax_quote_age_days = 7\nmarket_cap_tolerance = "0.01"\n'
        )
        for index, name in enumerate(names):
            dependency = names[(index + 1) % len(names)]
            graph += (
                f'\n[[nodes]]\nid = "{name}"\nrequires = ["{dependency}"]\n'
                'instructions = "instruction.txt"\n'
                f'section = "{SECTIONS[index]}"\n'
            )
        (skill / "graph.toml").write_text(graph)
        with (
            patch.object(research, "SKILL_ROOT", skill),
            self.assertRaisesRegex(research.InvalidDocument, "cycle"),
        ):
            research.graph()

    def test_extension_cannot_overwrite_core_calculations(self) -> None:
        specification = research.graph()
        specification["extensions"] = [
            {
                "id": "dcf-model",
                "node": "valuation",
                "instructions": "skills/dcf-model/SKILL.md",
                "artifacts": ["data/calculations.json"],
            }
        ]
        with (
            patch.object(research.tomllib, "loads", return_value=specification),
            self.assertRaisesRegex(research.InvalidDocument, "overwrites core"),
        ):
            research.graph()

    def test_extension_entrypoint_symlink_cannot_escape_checkout(self) -> None:
        specification = research.graph()
        specification["extensions"] = [
            {
                "id": "dcf-model",
                "node": "valuation",
                "instructions": "skills/dcf-model/SKILL.md",
                "artifacts": ["dcf.md"],
            }
        ]
        skill_parent = self.root / "skills"
        skill_parent.mkdir(parents=True)
        with tempfile.TemporaryDirectory() as outside:
            (Path(outside) / "SKILL.md").write_text("External instructions.")
            (skill_parent / "dcf-model").symlink_to(outside, target_is_directory=True)
            with (
                patch.object(research, "REPO_ROOT", self.root),
                patch.object(research.tomllib, "loads", return_value=specification),
                self.assertRaisesRegex(research.InvalidDocument, "path outside"),
            ):
                research.graph()

    def test_future_reported_period_is_blocked(self) -> None:
        self.evidence["facts"]["eps"]["period"] = "FY2027 ended 2027-01-31"
        for observation in self.evidence["facts"]["eps"]["observations"]:
            observation["period"] = "FY2027 ended 2027-01-31"
        self.save()
        self.assertEqual(self.status(), "BLOCKED")

    def test_future_fiscal_label_with_completed_period_is_valid(self) -> None:
        period = "FY2027 Q2 ended 2026-07-31"
        self.evidence["facts"]["eps"]["period"] = period
        for observation in self.evidence["facts"]["eps"]["observations"]:
            observation["period"] = period
        self.save()
        self.assertEqual(self.status(), "PASS")

    def test_index_saved_pass_cannot_cover_missing_report_section(self) -> None:
        self.save()
        research.persist(
            self.data / "audit.json", research.audit(self.directory, GRAPH)
        )
        report = self.directory / "report.md"
        report.write_text(
            "\n".join(
                f"## {section}\nAnalysis [filing] [provider] [treasury].\n"
                for section in SECTIONS
                if section != "Moat"
            ),
            encoding="utf-8",
        )
        record = research.index_run(self.directory, GRAPH)
        self.assertEqual(record["audit"]["status"], "PASS")
        self.assertFalse(record["complete"])
        self.assertNotIn("Moat", record["covered"])
        self.assertTrue(any("Moat" in gap for gap in record["gaps"]))

    def test_index_saved_pass_cannot_cover_missing_artifact(self) -> None:
        self.save()
        research.persist(
            self.data / "audit.json", research.audit(self.directory, GRAPH)
        )
        (self.data / "calculations.json").unlink()
        record = research.index_run(self.directory, GRAPH)
        self.assertFalse(record["complete"])
        self.assertIn("missing calculations.json", record["gaps"])

    def test_index_legacy_report_is_not_native_coverage(self) -> None:
        archive = self.directory / "archive"
        archive.mkdir()
        legacy = archive / "claude-trial.md"
        legacy.write_text(
            "\n".join(f"## {section}\nImported analysis." for section in SECTIONS)
        )
        record = research.index_run(self.directory, GRAPH)
        self.assertIsNone(record["audit"])
        self.assertEqual(record["covered"], set())
        self.assertFalse(record["complete"])
        self.assertEqual(record["legacy"], legacy.resolve())
        self.assertNotIn("claude-trial.md", record["present"])

    def test_index_refuses_output_symlink_before_overwriting_any_page(self) -> None:
        self.save()
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.md"
            target.write_text("Do not overwrite.", encoding="utf-8")
            (self.root / "index.md").symlink_to(target)
            with self.assertRaises(research.InvalidDocument):
                research.index(GRAPH)
            self.assertEqual(target.read_text(), "Do not overwrite.")
            self.assertEqual(self.guidance.read_bytes(), self.guidance_before)
            self.assertFalse((self.artifact_root / "TEST" / "README.md").exists())
            self.assertFalse(
                (self.root / "batches" / "2026-10-11" / "README.md").exists()
            )

    def test_index_refuses_malformed_or_misgrouped_runs_without_writes(self) -> None:
        self.save()
        sentinel = self.root / "index.md"
        sentinel.write_text("Previous navigation.", encoding="utf-8")
        invalid_date = self.artifact_root / "TEST" / "2026-13-11"
        invalid_date.mkdir()
        with self.assertRaises(research.InvalidDocument):
            research.index(GRAPH)
        invalid_date.rmdir()
        self.evidence["ticker"] = "OTHER"
        research.persist(self.data / "evidence.json", self.evidence)
        with self.assertRaises(research.InvalidDocument):
            research.index(GRAPH)
        (self.data / "evidence.json").write_text("{bad JSON", encoding="utf-8")
        with self.assertRaises(research.InvalidDocument):
            research.index(GRAPH)
        self.assertEqual(sentinel.read_text(), "Previous navigation.")
        self.assertEqual(self.guidance.read_bytes(), self.guidance_before)
        self.assertFalse((self.artifact_root / "TEST" / "README.md").exists())

    def test_index_discovers_new_dates_and_resolving_links(self) -> None:
        self.save()
        research.persist(
            self.data / "audit.json", research.audit(self.directory, GRAPH)
        )
        next_directory = self.artifact_root / "TEST" / "2026-10-12"
        next_directory.mkdir()
        next_evidence = copy.deepcopy(self.evidence)
        next_evidence["as_of"] = "2026-10-12"
        next_evidence["valuation"]["timing"].update(
            valuation_date="2026-10-12", terminal_date="2031-10-12"
        )
        research.persist(next_directory / "data" / "evidence.json", next_evidence)
        new_ticker_directory = self.artifact_root / "ADDED" / "2026-10-12"
        new_ticker_directory.mkdir(parents=True)
        (new_ticker_directory / "report.md").write_text(
            "## Grounding\nRetained analysis.", encoding="utf-8"
        )
        baseline = self.directory / "archive" / "claude-trial.md"
        baseline.parent.mkdir()
        baseline.write_text("Imported analysis.", encoding="utf-8")
        archive = self.root / "batches" / "2026-10-11" / "archive"
        archive.mkdir(parents=True)
        receipt = archive / "verification (historical) #1.json"
        receipt.write_text('{"historical": true}', encoding="utf-8")
        shared_date = self.root / "batches" / "2026-10-13"
        shared_date.mkdir()
        context = shared_date / "market-context.json"
        context.write_text('{"retained": true}', encoding="utf-8")
        ignored = self.root / "notes" / "2026-10-11"
        ignored.mkdir(parents=True)
        (ignored / "evidence.json").write_text("{not research}", encoding="utf-8")
        retained_paths = [
            *self.directory.rglob("*"),
            *next_directory.rglob("*"),
            *new_ticker_directory.rglob("*"),
            receipt,
            context,
        ]
        retained_bytes = {
            path: path.read_bytes() for path in retained_paths if path.is_file()
        }
        result = research.index(GRAPH)
        self.assertEqual(result["research_runs"], 3)
        self.assertEqual(result["date_batches"], 3)
        self.assertEqual(result["generated_files"], 1)
        self.assertEqual(self.guidance.read_bytes(), self.guidance_before)
        page = self.root / "index.md"
        self.assertTrue(page.is_file())
        self.assertFalse((self.root / "coverage.md").exists())
        self.assertEqual(set(self.artifact_root.rglob("README.md")), set())
        self.assertEqual(set((self.root / "batches").rglob("README.md")), set())
        content = page.read_text()
        headings, _ = research.report_sections(content)
        self.assertEqual(headings, ["2026-10-13", "2026-10-12", "2026-10-11"])
        target = research.calculate(self.evidence)["valuation"][
            "weighted_present_target"
        ]
        row = next(
            line
            for line in content.splitlines()
            if line.startswith("| [TEST](tickers/TEST/2026-10-11/report.md)")
        )
        columns = [column.strip() for column in row.split("|")]
        self.assertEqual(
            columns[2].split()[0], self.evidence["facts"]["price"]["value"]
        )
        self.assertEqual(columns[3], self.evidence["quote_time"][:10])
        self.assertEqual(columns[4], f"{research.decimal(target, 'target'):.2f}")
        later_rows = [
            line
            for line in content.splitlines()
            if line.startswith("|") and "2026-10-12" in line
        ]
        self.assertTrue(later_rows[0].startswith("| [ADDED]("))
        self.assertIn("TEST", later_rows[1])
        self.assertIn("UNRUN", content)
        self.assertIn("saved PASS", content)
        self.assertIn("INCOMPLETE", content)
        self.assertIn("1/9", content)
        self.assertIn("9/9", content)
        self.assertNotIn("tickers/TEST/2026-10-12/report.md", content)
        linked_targets = set()
        linked_anchors = set()
        for target in re.findall(r"\]\(([^)]+)\)", content):
            relative, _, anchor = target.partition("#")
            destination = (
                (page.parent / unquote(relative)).resolve()
                if relative
                else page.resolve()
            )
            linked_targets.add(destination)
            self.assertTrue(destination.is_relative_to(self.root.resolve()))
            self.assertTrue(destination.is_file(), str(destination))
            if anchor:
                destination_headings, _ = research.report_sections(
                    destination.read_text()
                )
                anchors = {
                    re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
                    for heading in destination_headings
                }
                self.assertIn(anchor, anchors)
                linked_anchors.add(anchor)
        self.assertEqual(linked_anchors, {"2026-10-11", "2026-10-12", "2026-10-13"})
        self.assertTrue(
            {
                self.guidance.resolve(),
                (self.directory / "report.md").resolve(),
                (self.data / "evidence.json").resolve(),
                (self.data / "calculations.json").resolve(),
                (self.data / "audit.json").resolve(),
                (next_directory / "data" / "evidence.json").resolve(),
                (new_ticker_directory / "report.md").resolve(),
                baseline.resolve(),
                receipt.resolve(),
                context.resolve(),
            }.issubset(linked_targets)
        )
        research.index(GRAPH)
        self.assertEqual(self.guidance.read_bytes(), self.guidance_before)
        for path, before in retained_bytes.items():
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
