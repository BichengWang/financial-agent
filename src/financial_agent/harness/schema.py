"""Prediction ledger schema v1 for ``15_predictions.json`` (plan Phase 1).

The spike's audit found the ledger drifting in names, units, and meaning:
``adj_score`` stored as a percentile, VaR in percent, one ``kelly_025`` field
with four conventions, three names for the run status, 35 settlement key-sets.
v1 fixes one shape, following the proposals in plan §6 (1-3):

* one status key (``run_status``) and a required ``data_mode`` and ``regime``;
* ``pctl`` is its own required field and ``adj_score`` is always the score;
* every return and risk field is a decimal;
* Kelly is split into ``kelly_fractional`` (uncapped, the gate input) and
  ``position_weight`` (capped, the sizing input), with ``kelly_method``;
* settlement rows use the canonical ``settlement_ledger.py`` names only.

v1 is opt-in: a payload that declares ``"schema_version": 1`` is validated in
full by the publish gate; older payloads are immutable history and are only
audited. The specs below are the single source for both the validator and the
JSON Schema document other runtimes can consume (``harness schema --json-schema``).
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from typing import Any, Mapping, TypeGuard

from financial_agent.harness.audit import SETTLEMENT_LEGACY_KEYS
from financial_agent.harness.gates import (
    CONFIDENCE_ORDER,
    confidence_ceiling,
    earnings_in_window,
    investability,
)
from financial_agent.harness.lifecycle import RunStatus
from financial_agent.harness.policy import FAMILIES, Policy

SCHEMA_VERSION = 1
DATA_MODES = ("LIVE", "DELAYED", "DELAYED_PARTIAL", "ILLUSTRATIVE")
PRICE_TAGS = ("LIVE", "DELAYED", "OFFICIAL_FILING", "HISTORICAL", "ILLUSTRATIVE_REF")
SIGMA_SOURCES = ("REALIZED_VOL_30D", "IV30", "SECTOR_MEDIAN", "SECTOR_MEDIAN_ILLUS")
CONFIDENCE = ("HIGH", "MEDIUM", "LOW")
SLEEVES = ("INVESTABLE", "MONITORING")
KELLY_METHODS = ("BETA_ADJ_TE", "MU_OVER_SIGMA2")
KELLY_GATES = ("BLOCKED", "PENALTY", "OK", "CAP_BINDING")
RATIO_BASES = ("EXCESS_RETURN", "RAW_DIAGNOSTIC")
TIMING_FLAGS = ("ORDINARY", "WEEKEND_TARGET", "TARGET_EQ_RUN_DATE", "TARGET_DATE_CLOSE")
DIRECTIONS = ("HIT", "MISS", "N/A - FLAT_CALL")
CI_RESULTS = ("IN_CI", "OUT_CI_LOW", "OUT_CI_HIGH")
SETTLEMENT_PRICE_TAGS = ("LIVE", "DELAYED", "HISTORICAL")
FORMULA = (
    "Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) "
    "* DQ - Penalties"
)
TOL = 1e-6


@dataclass(frozen=True)
class Spec:
    """One field: ``kind`` is string, number, integer, date, datetime, enum,
    object, or array."""

    kind: str
    required: bool = True
    nullable: bool = False
    enum: tuple[str, ...] = ()


def _s(kind: str, *enum: str, required: bool = True, nullable: bool = False) -> Spec:
    return Spec(kind, required, nullable, tuple(enum))


def _common_record() -> dict[str, Spec]:
    return {
        "run_date": _s("date"),
        "model": _s("string"),
        "ticker": _s("string"),
        "entry_price": _s("number"),
        "price_tag": _s("enum", *PRICE_TAGS),
        "price_date": _s("date"),
        "mu": _s("number"),
        "mu_prior": _s("number"),
        "mu_adjustment": _s("number"),
        "mu_adjustment_reason": _s("string", required=False),
        "sigma": _s("number"),
        "sigma_source": _s("enum", *SIGMA_SOURCES),
        "target_price": _s("number"),
        "ci70_lo": _s("number"),
        "ci70_hi": _s("number"),
        "target_date": _s("date"),
        "confidence": _s("enum", *CONFIDENCE),
        "status": _s("enum", "OPEN"),
        "thesis": _s("string"),
    }


def specs(policy: Policy) -> dict[str, dict[str, Spec]]:
    """Every v1 object's fields; enums that live in the policy come from it."""
    regimes = tuple(policy.get("market_forecast.spy_regime_prior"))
    return {
        "payload": {
            "schema_version": _s("integer"),
            "run_date": _s("date"),
            "model": _s("string"),
            "run_status": _s("enum", *(s.value for s in RunStatus)),
            "data_mode": _s("enum", *DATA_MODES),
            "regime": _s("enum", *regimes),
            "predictions": _s("array"),
            "settlements": _s("array"),
        },
        "equity_alpha": {
            **_common_record(),
            "type": _s("enum", "EQUITY_ALPHA"),
            "benchmark": _s("enum", "SPY"),
            "benchmark_price": _s("number"),
            "pctl": _s("number"),
            "adj_score": _s("number"),
            "sleeve": _s("enum", *SLEEVES),
            "score_explainability": _s("object"),
        },
        "market_forecast": {
            **_common_record(),
            "type": _s("enum", "MARKET_FORECAST"),
            "ticker": _s("enum", *policy.get("market_forecast.tickers")),
            "benchmark": _s("enum", "NONE"),
            "benchmark_price": _s("number", nullable=True),
            "adj_score": _s("number", nullable=True),
            "beta_vs_spy": _s("number", nullable=True),
            "mu_derivation": _s("string"),
        },
        "score_explainability": {
            **{f: _s("number", nullable=True) for f in FAMILIES},
            "composite_z": _s("number"),
            "data_quality_multiplier": _s("number"),
            "penalties": _s("number"),
            "formula": _s("string"),
            "metrics": _s("object"),
            "ledger_rows": _s("array", required=False),
        },
        "metrics": {
            "kelly_raw": _s("number"),
            "kelly_method": _s("enum", *KELLY_METHODS),
            "kelly_fractional": _s("number"),
            "position_weight": _s("number"),
            "kelly_gate": _s("enum", *KELLY_GATES),
            "var95": _s("number"),
            "cvar95": _s("number"),
            "ratio_basis": _s("enum", *RATIO_BASES, required=False),
        },
        "settlement": {
            "model": _s("string"),
            "vintage": _s("date"),
            "ticker": _s("string"),
            "type": _s("enum", "EQUITY_ALPHA", "MARKET_FORECAST"),
            "target_date": _s("date"),
            "settle_price": _s("number"),
            "settle_price_date": _s("date"),
            "settlement_price_tag": _s("enum", *SETTLEMENT_PRICE_TAGS),
            "timing_flag": _s("enum", *TIMING_FLAGS),
            "settled_at": _s("datetime"),
            "realized_return": _s("number"),
            "direction": _s("enum", *DIRECTIONS),
            "ci_result": _s("enum", *CI_RESULTS),
        },
    }


# Keys v1 replaces, and what replaces them.
FORBIDDEN: dict[str, dict[str, str]] = {
    "payload": {"final_status": "run_status", "status": "run_status"},
    "equity_alpha": {"percentile": "pctl"},
    "market_forecast": {"percentile": "pctl"},
    "metrics": {"kelly_025": "kelly_fractional and position_weight"},
    "settlement": dict(SETTLEMENT_LEGACY_KEYS),
}


def _is_number(value: Any) -> TypeGuard[float]:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _type_ok(spec: Spec, value: Any) -> bool:
    if spec.kind == "number":
        return _is_number(value)
    if spec.kind == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if spec.kind == "enum":
        return value in spec.enum
    if spec.kind == "object":
        return isinstance(value, Mapping)
    if spec.kind == "array":
        return isinstance(value, list)
    if not isinstance(value, str):
        return False
    if spec.kind == "date":
        try:
            dt.date.fromisoformat(value)
        except ValueError:
            return False
        return len(value) == 10
    if spec.kind == "datetime":
        try:
            stamp = dt.datetime.fromisoformat(value)
        except ValueError:
            return False
        return stamp.tzinfo is not None
    return bool(value.strip())


def check_fields(obj: Mapping[str, Any], kind: str, policy: Policy) -> list[str]:
    """Shape findings for one object against ``specs(policy)[kind]``."""
    findings: list[str] = []
    for name, spec in specs(policy)[kind].items():
        if name not in obj:
            if spec.required:
                findings.append(f"missing {name}")
            continue
        value = obj[name]
        if value is None:
            if not spec.nullable:
                findings.append(f"{name} is null")
        elif not _type_ok(spec, value):
            expected = f"one of {list(spec.enum)}" if spec.enum else spec.kind
            findings.append(f"{name}={value!r} is not {expected}")
    for name, replacement in FORBIDDEN.get(kind, {}).items():
        if name in obj:
            findings.append(f"{name} is not v1; use {replacement}")
    return findings


def _close(a: Any, b: float, rel: float = TOL) -> bool:
    return _is_number(a) and abs(a - b) <= rel * max(1.0, abs(b))


def _check_mu(record: Mapping[str, Any], prior: float, limit: float) -> list[str]:
    findings: list[str] = []
    adjustment = record.get("mu_adjustment")
    if not _close(record.get("mu_prior"), prior, rel=1e-5):
        findings.append(f"mu_prior {record.get('mu_prior')} != {prior:.6f}")
    if _is_number(adjustment):
        if abs(adjustment) > limit + TOL:
            findings.append(f"mu_adjustment {adjustment:+.4f} exceeds ±{limit}")
        if adjustment and not str(record.get("mu_adjustment_reason", "")).strip():
            findings.append("mu_adjustment needs a mu_adjustment_reason")
        if not _close(record.get("mu"), prior + adjustment, rel=1e-5):
            findings.append(f"mu {record.get('mu')} != mu_prior + mu_adjustment")
    return findings


def _check_equity(record: Mapping[str, Any], policy: Policy) -> list[str]:
    findings = check_fields(record, "equity_alpha", policy)
    explain = record.get("score_explainability")
    if not isinstance(explain, Mapping):
        return findings
    findings += [
        f"score_explainability.{f}"
        for f in check_fields(explain, "score_explainability", policy)
    ]
    for family in policy.shadow_families:
        if explain.get(family) is not None:
            findings.append(
                f"score_explainability.{family} is SHADOW and must be null "
                "(rules.md § SHADOW Diagnostic Tooling)"
            )
    pctl = record.get("pctl")
    band = policy.mu_prior(pctl) if _is_number(pctl) else None
    if _is_number(pctl) and band is None:
        findings.append(f"pctl {pctl} is below every mu band: do not rank")
    if band is not None:
        findings += _check_mu(record, band.mu, policy.num("forecast.mu_adjustment_max"))
    if record.get("sleeve") == "INVESTABLE":
        for failure in investability(record, policy):
            findings.append(f"sleeve INVESTABLE but {failure}")
    ceiling, reasons = confidence_ceiling(
        record, policy, earnings_within_window=earnings_in_window(record, policy)
    )
    confidence = record.get("confidence")
    if confidence in CONFIDENCE_ORDER and CONFIDENCE_ORDER.index(
        confidence
    ) > CONFIDENCE_ORDER.index(ceiling):
        findings.append(
            f"confidence {confidence} exceeds ceiling {ceiling} ({'; '.join(reasons)})"
        )

    metrics = explain.get("metrics")
    if not isinstance(metrics, Mapping):
        return findings
    findings += [f"metrics.{f}" for f in check_fields(metrics, "metrics", policy)]
    raw, mu, sigma = metrics.get("kelly_raw"), record.get("mu"), record.get("sigma")
    if not (_is_number(raw) and _is_number(mu) and _is_number(sigma)) or sigma <= 0:
        return findings
    for name in ("var95", "cvar95"):
        value = metrics.get(name)
        if _is_number(value) and abs(value) >= 1:
            findings.append(f"metrics.{name}={value} must be a decimal")
    if metrics.get("kelly_method") == "MU_OVER_SIGMA2" and not _close(
        raw, mu / sigma**2, rel=1e-3
    ):
        findings.append(f"metrics.kelly_raw {raw} != mu/sigma^2 {mu / sigma**2:.6f}")
    sizing = policy.kelly_sizing(raw)
    for name, expected in (
        ("kelly_fractional", sizing.fractional),
        ("position_weight", sizing.weight),
    ):
        if not _close(metrics.get(name), expected, rel=1e-5):
            findings.append(f"metrics.{name} {metrics.get(name)} != {expected:.6f}")
    if metrics.get("kelly_gate") != sizing.gate:
        findings.append(
            f"metrics.kelly_gate {metrics.get('kelly_gate')} != {sizing.gate}"
        )
    return findings


def _check_market(
    record: Mapping[str, Any], policy: Policy, regime: Any, spy_mu: Any
) -> list[str]:
    findings = check_fields(record, "market_forecast", policy)
    for name in ("benchmark_price", "adj_score", "score_explainability"):
        if record.get(name) is not None:
            findings.append(f"{name} must be null on MARKET_FORECAST")
    ticker = record.get("ticker")
    if ticker == "SPY":
        regimes = policy.get("market_forecast.spy_regime_prior")
        if regime in regimes:
            limit = policy.num("market_forecast.spy_adjustment_max")
            findings += _check_mu(record, policy.spy_mu_prior(regime), limit)
    else:
        beta = record.get("beta_vs_spy")
        if not _is_number(beta):
            findings.append(f"{ticker} needs beta_vs_spy: mu = beta x SPY mu")
        elif _is_number(spy_mu):
            limit = policy.num("market_forecast.beta_scaled_adjustment_max")
            findings += _check_mu(record, beta * spy_mu, limit)
    return findings


def validate_payload(payload: Any, policy: Policy) -> list[str]:
    """Every v1 finding for a ``15_predictions.json`` payload; empty means valid."""
    if not isinstance(payload, Mapping):
        return ["payload is not a JSON object"]
    findings = check_fields(payload, "payload", policy)
    if payload.get("schema_version") != SCHEMA_VERSION:
        findings.append(f"schema_version must be {SCHEMA_VERSION}")
    predictions = payload.get("predictions")
    predictions = predictions if isinstance(predictions, list) else []
    spy_mu = next(
        (
            p.get("mu")
            for p in predictions
            if isinstance(p, Mapping)
            and p.get("type") == "MARKET_FORECAST"
            and p.get("ticker") == "SPY"
        ),
        None,
    )
    for index, record in enumerate(predictions):
        if not isinstance(record, Mapping):
            findings.append(f"predictions[{index}] is not an object")
            continue
        where = f"predictions[{index}] {record.get('ticker', '?')}"
        for key in ("run_date", "model"):
            if record.get(key) != payload.get(key):
                findings.append(f"{where}: {key} differs from the payload's")
        kind = record.get("type")
        if kind == "EQUITY_ALPHA":
            found = _check_equity(record, policy)
        elif kind == "MARKET_FORECAST":
            found = _check_market(record, policy, payload.get("regime"), spy_mu)
        else:
            found = [f"type={kind!r} is not EQUITY_ALPHA or MARKET_FORECAST"]
        findings += [f"{where}: {f}" for f in found]
    settlements = payload.get("settlements")
    for index, row in enumerate(settlements if isinstance(settlements, list) else []):
        if not isinstance(row, Mapping):
            findings.append(f"settlements[{index}] is not an object")
            continue
        where = f"settlements[{index}] {row.get('ticker', '?')}"
        findings += [f"{where}: {f}" for f in check_fields(row, "settlement", policy)]
    return findings


def _json_type(spec: Spec) -> dict[str, Any]:
    if spec.kind == "enum":
        return {"enum": [*spec.enum, None] if spec.nullable else list(spec.enum)}
    kinds: dict[str, dict[str, Any]] = {
        "number": {"type": "number"},
        "integer": {"type": "integer"},
        "object": {"type": "object"},
        "array": {"type": "array"},
        "date": {"type": "string", "format": "date"},
        "datetime": {"type": "string", "format": "date-time"},
        "string": {"type": "string", "minLength": 1},
    }
    node = kinds[spec.kind]
    if spec.nullable:
        return {"anyOf": [node, {"type": "null"}]}
    return node


def _object_schema(kind: str, policy: Policy) -> dict[str, Any]:
    fields = specs(policy)[kind]
    properties: dict[str, Any] = {name: _json_type(s) for name, s in fields.items()}
    properties.update({name: False for name in FORBIDDEN.get(kind, {})})
    return {
        "type": "object",
        "required": [name for name, s in fields.items() if s.required],
        "properties": properties,
    }


def json_schema(policy: Policy) -> dict[str, Any]:
    """The v1 shape as a JSON Schema (draft 2020-12) document.

    Shape only: cross-field rules (Kelly split, mu bands, confidence ceiling,
    SHADOW families) need the policy and are checked by ``validate_payload``.
    """
    defs = {
        kind: _object_schema(kind, policy)
        for kind in (
            "equity_alpha",
            "market_forecast",
            "score_explainability",
            "metrics",
            "settlement",
        )
    }
    defs["equity_alpha"]["properties"]["score_explainability"] = {
        "$ref": "#/$defs/score_explainability"
    }
    defs["score_explainability"]["properties"]["metrics"] = {"$ref": "#/$defs/metrics"}
    document = _object_schema("payload", policy)
    document["properties"]["schema_version"] = {"const": SCHEMA_VERSION}
    document["properties"]["predictions"] = {
        "type": "array",
        "items": {
            "oneOf": [
                {"$ref": "#/$defs/equity_alpha"},
                {"$ref": "#/$defs/market_forecast"},
            ]
        },
    }
    document["properties"]["settlements"] = {
        "type": "array",
        "items": {"$ref": "#/$defs/settlement"},
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "financial-agent/15_predictions.v1.schema.json",
        "title": "15_predictions.json (prediction ledger) v1",
        **document,
        "$defs": defs,
    }
