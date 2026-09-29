"""Conformance audit of ``15_predictions.json`` ledgers against the policy.

Every prediction record carries its own inputs (entry, mu, sigma, z-scores),
so the formula fields can be recomputed and compared. The spike runs this
over every historical package to measure how often model-authored ledgers
drift from ``rules.md`` -- the evidence behind "code computes, the model
cites". The same function is the per-record check inside the publish gate.

Severities:
* ``error`` -- violates an unambiguous rule (enum, formula, required field).
* ``drift`` -- a unit or meaning the rules leave implicit, used inconsistently
  across runs (e.g. percent vs decimal VaR, capped vs uncapped Kelly).
"""

from __future__ import annotations

import datetime as dt
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from financial_agent.harness.policy import FAMILIES, Policy

REQUIRED_FIELDS = (
    "run_date",
    "model",
    "ticker",
    "entry_price",
    "price_tag",
    "price_date",
    "mu",
    "sigma",
    "sigma_source",
    "ci70_lo",
    "ci70_hi",
    "target_date",
    "benchmark",
    "benchmark_price",
    "adj_score",
    "confidence",
    "status",
    "thesis",
)
ENUMS: dict[str, frozenset[str]] = {
    "type": frozenset({"EQUITY_ALPHA", "MARKET_FORECAST"}),
    "price_tag": frozenset(
        {"LIVE", "DELAYED", "OFFICIAL_FILING", "HISTORICAL", "ILLUSTRATIVE_REF"}
    ),
    "sigma_source": frozenset(
        {"REALIZED_VOL_30D", "IV30", "SECTOR_MEDIAN", "SECTOR_MEDIAN_ILLUS"}
    ),
    "confidence": frozenset({"HIGH", "MEDIUM", "LOW"}),
}
# settlement_ledger.py: first name canonical, the rest legacy spellings.
SETTLEMENT_LEGACY_KEYS = {
    "settlement_price": "settle_price",
    "current_price": "settle_price",
    "settlement_date": "settle_price_date",
    "current_price_date": "settle_price_date",
    "settle_date": "settle_price_date",
    "current_price_tag": "settlement_price_tag",
    "settlement_timing_flag": "timing_flag",
    "settled_on": "settled_at",
}
CORE_ETF_RULE_EFFECTIVE = "2026-06-11"  # rules.md § Core ETF Market Forecast
REL_TOL = 2e-3  # prices and CI bounds are stored rounded
ABS_TOL = 5e-3  # z-scores and scores are stored rounded to 2-4 places


@dataclass(frozen=True)
class Finding:
    check: str
    severity: str
    package: str
    ticker: str
    detail: str


def _num(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _close(actual: float, expected: float, *, rel: float = REL_TOL) -> bool:
    return abs(actual - expected) <= rel * max(abs(expected), 1e-9)


_KELLY_UNITS = (
    (1.0, 1.0, "DECIMAL"),
    (100.0, 100.0, "PERCENT"),
    (1.0, 100.0, "MIXED_UNITS"),  # raw as a decimal, kelly_025 as percent
)


def kelly_convention(raw: float, stored: float, cap: float) -> str:
    """Which of the conventions seen in history a stored ``kelly_025`` follows."""
    for raw_scale, k_scale, unit in _KELLY_UNITS:
        r, k = raw / raw_scale, stored / k_scale
        if abs(k - 0.25 * r) <= 1e-3 * max(1.0, abs(r)):
            return f"UNCAPPED_{unit}"
        if abs(k - min(0.25 * r, cap)) <= 1e-3:
            return f"CAPPED_{unit}"
    return "UNRECOGNIZED"


@dataclass
class RecordAudit:
    checks: list[str] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    kelly_convention: str | None = None


def audit_record(
    record: Mapping[str, Any], policy: Policy, *, package: str = ""
) -> RecordAudit:
    """Recompute one prediction record's formula fields and check its schema."""
    ticker = str(record.get("ticker", "?"))
    result = RecordAudit()
    checks, findings = result.checks, result.findings

    def check(name: str, ok: bool, detail: str, severity: str = "error") -> None:
        checks.append(name)
        if not ok:
            findings.append(Finding(name, severity, package, ticker, detail))

    missing = [f for f in REQUIRED_FIELDS if f not in record]
    check("schema.required_fields", not missing, f"missing {missing}")
    bad_enums = [
        f"{key}={record.get(key)!r}"
        for key, allowed in ENUMS.items()
        if key in record and record.get(key) not in allowed
    ]
    check("schema.enums", not bad_enums, ", ".join(bad_enums))

    kind = str(record.get("type", "EQUITY_ALPHA"))
    entry, mu, sigma = (_num(record.get(k)) for k in ("entry_price", "mu", "sigma"))
    if mu is not None and sigma is not None:
        check(
            "units.mu_sigma_decimal",
            abs(mu) < 0.5 and 0 < sigma < 1,
            f"mu={mu} sigma={sigma}",
            "drift",
        )
    lo, hi = _num(record.get("ci70_lo")), _num(record.get("ci70_hi"))
    if (
        entry is not None
        and mu is not None
        and sigma is not None
        and lo is not None
        and hi is not None
    ):
        exp_lo, exp_hi = policy.ci70(entry, mu, sigma)
        check(
            "formula.ci70",
            _close(lo, exp_lo) and _close(hi, exp_hi),
            f"ci70=[{lo}, {hi}] expected [{exp_lo:.4f}, {exp_hi:.4f}]",
        )
    target = _num(record.get("target_price"))
    if target is not None and entry is not None and mu is not None:
        expected = policy.target_price(entry, mu)
        check(
            "formula.target_price",
            _close(target, expected),
            f"target={target} expected {expected:.4f}",
        )
    try:
        offset = (
            dt.date.fromisoformat(str(record.get("target_date")))
            - dt.date.fromisoformat(str(record.get("run_date")))
        ).days
        horizons = list(policy.get("forecast.allowed_horizon_days"))
        check("horizon.target_offset", offset in horizons, f"offset {offset}d")
    except ValueError:
        check("horizon.target_offset", False, "unparseable run_date/target_date")

    if kind == "MARKET_FORECAST":
        check(
            "market_forecast.shape",
            record.get("benchmark") == "NONE"
            and record.get("benchmark_price") is None
            and record.get("adj_score") is None,
            "benchmark must be NONE with null benchmark_price and adj_score",
        )
        return result

    check(
        "equity.benchmark_price",
        _num(record.get("benchmark_price")) is not None,
        "EQUITY_ALPHA needs benchmark_price to settle alpha",
    )
    pctl = _num(record.get("pctl", record.get("percentile")))
    if pctl is not None and mu is not None:
        band = policy.mu_prior(pctl)
        if band is None:
            check("formula.mu_band", False, f"ranked at pctl {pctl} below every band")
        else:
            limit = policy.num("forecast.mu_adjustment_max")
            check(
                "formula.mu_band",
                abs(mu - band.mu) <= limit + 1e-9,
                f"mu {mu:+.3f} vs prior {band.mu:+.3f} at pctl {pctl} (max ±{limit})",
            )

    explain = record.get("score_explainability")
    if not isinstance(explain, Mapping):
        return result
    composite = _num(explain.get("composite_z"))
    if composite is not None:
        expected = policy.composite_z({f: _num(explain.get(f)) for f in FAMILIES})
        check(
            "formula.composite_z",
            abs(composite - expected) <= ABS_TOL,
            f"composite_z {composite} expected {expected:.4f}",
        )
        dq, adj = _num(explain.get("data_quality_multiplier")), _num(
            record.get("adj_score")
        )
        if dq is not None and adj is not None:
            penalties = _num(explain.get("penalties")) or 0.0
            expected = policy.adj_score(composite, dq, penalties)
            if abs(adj) > 5:
                hint = "; value looks like a 0-100 percentile rank, not a score"
            elif abs(adj - (composite - penalties)) <= ABS_TOL:
                hint = "; DQ multiplier not applied"
            else:
                hint = ""
            check(
                "formula.adj_score",
                abs(adj - expected) <= ABS_TOL,
                f"adj_score {adj} expected {expected:.4f} "
                f"(= {composite} x DQ {dq} - {penalties}){hint}",
            )
    metrics = explain.get("metrics")
    if not isinstance(metrics, Mapping) or mu is None or sigma is None:
        return result
    for name, fn in (("var95", policy.var95), ("cvar95", policy.cvar95)):
        stored = _num(metrics.get(name))
        if stored is None:
            continue
        percent = abs(stored) >= 1
        check(f"units.{name}_decimal", not percent, f"{name}={stored}", "drift")
        value = stored / 100 if percent else stored
        check(
            f"formula.{name}",
            abs(value - fn(mu, sigma)) <= ABS_TOL,
            f"{name} {value:.4f} expected {fn(mu, sigma):.4f}",
        )
    raw, stored_k = _num(metrics.get("kelly_raw")), _num(metrics.get("kelly_025"))
    if raw is not None and stored_k is not None and sigma > 0:
        convention = kelly_convention(
            raw, stored_k, policy.num("risk.max_single_name_weight")
        )
        result.kelly_convention = convention
        check(
            "semantics.kelly_025",
            convention != "UNRECOGNIZED",
            f"kelly_025={stored_k} kelly_raw={raw}",
        )
        check(
            "units.kelly_decimal",
            convention.endswith("_DECIMAL"),
            f"kelly convention {convention}",
            "drift",
        )
        # rules.md prefers a beta-adjusted edge over tracking-error variance and
        # falls back to mu/sigma^2, but no record says which it used: a value
        # that is not the fallback cannot be verified from the record.
        scale = 100.0 if convention.endswith("_PERCENT") else 1.0
        check(
            "lineage.kelly_raw_method",
            _close(raw / scale, mu / sigma**2, rel=0.01),
            f"kelly_raw {raw / scale:.4f} is not the mu/sigma^2 fallback "
            f"{mu / sigma**2:.4f} and the method is unrecorded",
            "drift",
        )
    return result


@dataclass
class AuditReport:
    packages: int = 0
    records: int = 0
    checked: Counter[str] = field(default_factory=Counter)
    findings: list[Finding] = field(default_factory=list)
    kelly_by_model: dict[str, Counter[str]] = field(
        default_factory=lambda: defaultdict(Counter)
    )
    settlement_rows: int = 0
    settlement_keysets: set[tuple[str, ...]] = field(default_factory=set)
    settlement_legacy_keys: Counter[str] = field(default_factory=Counter)
    packages_without_ledger: list[str] = field(default_factory=list)

    def failed(self, check: str) -> list[Finding]:
        return [f for f in self.findings if f.check == check]

    def to_markdown(self) -> str:
        lines = [
            f"Packages audited: {self.packages} "
            f"({len(self.packages_without_ledger)} without 15_predictions.json); "
            f"prediction records: {self.records}; settlement rows: "
            f"{self.settlement_rows}.",
            "",
            "| check | severity | checked | failed | fail % | packages | models |",
            "|---|---|---|---|---|---|---|",
        ]
        for name in sorted(self.checked):
            fails = self.failed(name)
            severity = fails[0].severity if fails else "-"
            packages = {f.package for f in fails}
            models = {f.package.rsplit("-", 3)[0] for f in fails}
            pct = 100 * len(fails) / self.checked[name]
            lines.append(
                f"| {name} | {severity} | {self.checked[name]} | {len(fails)} | "
                f"{pct:.1f} | {len(packages)} | {', '.join(sorted(models)) or '-'} |"
            )
        lines += ["", "`kelly_025` convention by model:", ""]
        for model in sorted(self.kelly_by_model):
            counts = ", ".join(
                f"{k} {v}" for k, v in sorted(self.kelly_by_model[model].items())
            )
            lines.append(f"- {model}: {counts}")
        lines += [
            "",
            f"Settlement rows use {len(self.settlement_keysets)} distinct key-sets; "
            "legacy (non-canonical) field names in use:",
            "",
        ]
        for key, count in self.settlement_legacy_keys.most_common():
            lines.append(
                f"- `{key}` (canonical `{SETTLEMENT_LEGACY_KEYS[key]}`): {count}"
            )
        return "\n".join(lines)


def audit_output_dir(
    output_dir: Path, policy: Policy, *, as_of: str | None = None
) -> AuditReport:
    """Audit every ``{model}-{YYYY-MM-DD}`` package, optionally up to ``as_of``."""
    report = AuditReport()
    for package_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        run_date = package_dir.name[-10:]
        try:
            dt.date.fromisoformat(run_date)
        except ValueError:
            continue
        if as_of is not None and run_date > as_of:
            continue
        report.packages += 1
        path = package_dir / "15_predictions.json"
        if not path.exists():
            report.packages_without_ledger.append(package_dir.name)
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        predictions = payload.get("predictions") or []
        model = package_dir.name[: -len(run_date) - 1]
        for record in predictions:
            report.records += 1
            result = audit_record(record, policy, package=package_dir.name)
            report.checked.update(result.checks)
            report.findings.extend(result.findings)
            if result.kelly_convention is not None:
                report.kelly_by_model[model][result.kelly_convention] += 1
        ranked = any(
            p.get("type", "EQUITY_ALPHA") == "EQUITY_ALPHA" for p in predictions
        )
        if ranked and run_date >= CORE_ETF_RULE_EFFECTIVE:
            etfs = {
                p.get("ticker")
                for p in predictions
                if p.get("type") == "MARKET_FORECAST"
            }
            missing = sorted(set(policy.get("market_forecast.tickers")) - etfs)
            report.checked["package.core_etf_forecasts"] += 1
            if missing:
                report.findings.append(
                    Finding(
                        "package.core_etf_forecasts",
                        "error",
                        package_dir.name,
                        "-",
                        f"ranked names without MARKET_FORECAST for {missing}",
                    )
                )
        for row in payload.get("settlements") or []:
            report.settlement_rows += 1
            report.settlement_keysets.add(tuple(sorted(row)))
            for key in row:
                if key in SETTLEMENT_LEGACY_KEYS:
                    report.settlement_legacy_keys[key] += 1
    return report
