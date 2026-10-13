"""Canonical, self-hashed validation certificates; hashes are not signatures."""

from collections.abc import Mapping
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
import hashlib
from importlib.metadata import PackageNotFoundError, version
import json
import math
from pathlib import Path
from typing import Any

from .gate import Check, PromotionReport


class CertificateError(ValueError):
    """A malformed, changed, stale or incompatible validation certificate."""


@dataclass(frozen=True)
class Certificate:
    schema_version: int
    strategy: str
    params: dict[str, Any]
    grid_size: int
    data_fingerprint: str
    data_start: str
    data_end: str
    policy_sha256: str
    package_version: str
    created_at: str
    passed: bool
    checks: tuple[Check, ...]
    hash: str


def _canonical(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def write_certificate(report: PromotionReport, path: str | Path) -> Path:
    """Write UTF-8 canonical JSON, hashing every field except hash itself.

    Undefined check values are JSON null; failed reports can be saved, but the
    verifier rejects them by default. Policy bytes must match report.policy.
    """
    try:
        package_version = version("financial-agent")
    except PackageNotFoundError:
        package_version = "0+unknown"
    checks = [asdict(check) for check in report.checks]
    for check in checks:
        if not math.isfinite(check["value"]):
            check["value"] = None
    payload = {
        "schema_version": 1,
        "strategy": report.strategy,
        "params": report.selected_params,
        "grid_size": len(report.grid),
        "data_fingerprint": report.data_fingerprint,
        "data_start": report.data_start,
        "data_end": report.data_end,
        "policy_sha256": report.policy.file_sha256(),
        "package_version": package_version,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "passed": report.passed,
        "checks": checks,
    }
    payload["hash"] = hashlib.sha256(_canonical(payload)).hexdigest()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(_canonical(payload))
    return target


def verify_certificate(
    path: str | Path,
    *,
    max_age_days: float = 90,
    now: datetime | None = None,
    expected_strategy: str | None = None,
    expected_params: Mapping[str, Any] | None = None,
    require_passed: bool = True,
) -> Certificate:
    """Verify integrity before age, identity and gate verdict; reject future dates."""
    if not math.isfinite(max_age_days) or max_age_days < 0:
        raise CertificateError("max_age_days must be finite and nonnegative")
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("expected a JSON object")
        claimed = payload.pop("hash", None)
        actual = hashlib.sha256(_canonical(payload)).hexdigest()
    except (OSError, ValueError, TypeError) as exc:
        raise CertificateError(f"malformed certificate: {exc}") from exc
    if claimed != actual:
        raise CertificateError("certificate hash mismatch (tamper)")
    required = set(Certificate.__dataclass_fields__) - {"hash"}
    if (
        payload.keys() != required
        or type(payload["schema_version"]) is not int
        or payload["schema_version"] != 1
    ):
        raise CertificateError("invalid certificate schema (expected schema_version 1)")
    if (
        not isinstance(payload["strategy"], str)
        or not isinstance(payload["params"], dict)
        or type(payload["passed"]) is not bool
        or type(payload["grid_size"]) is not int
        or payload["grid_size"] < 1
        or not isinstance(payload["checks"], list)
    ):
        raise CertificateError("invalid certificate field types")
    checks: list[Check] = []
    try:
        for row in payload["checks"]:
            if (
                not isinstance(row, dict)
                or row.keys() != {"name", "value", "threshold", "passed", "detail"}
                or type(row["passed"]) is not bool
                or not isinstance(row["name"], str)
                or not isinstance(row["detail"], str)
                or not math.isfinite(row["threshold"])
                or (row["value"] is not None and not math.isfinite(row["value"]))
            ):
                raise ValueError("invalid check")
            checks.append(
                Check(
                    **{
                        **row,
                        "value": float("nan") if row["value"] is None else row["value"],
                    }
                )
            )
        if payload["passed"] and (not checks or not all(c.passed for c in checks)):
            raise ValueError("inconsistent gate verdict")
        created = datetime.fromisoformat(payload["created_at"])
        if created.tzinfo is None:
            raise ValueError("created_at must include a timezone")
    except (KeyError, TypeError, ValueError) as exc:
        raise CertificateError(f"invalid certificate fields: {exc}") from exc
    current = datetime.now(timezone.utc) if now is None else now
    if current.tzinfo is None:
        raise CertificateError("now must include a timezone")
    age = current - created
    if age < timedelta(0):
        raise CertificateError("certificate created_at is in the future")
    if age > timedelta(days=max_age_days):
        raise CertificateError(
            f"certificate expired (older than {max_age_days:g} days)"
        )
    if expected_strategy is not None and payload["strategy"] != expected_strategy:
        raise CertificateError("certificate strategy mismatch")
    if expected_params is not None:
        try:
            equal = _canonical(payload["params"]) == _canonical(expected_params)
        except (ValueError, TypeError) as exc:
            raise CertificateError(f"invalid expected_params: {exc}") from exc
        if not equal:
            raise CertificateError("certificate params mismatch")
    if require_passed and not payload["passed"]:
        raise CertificateError("certificate failed promotion gate")
    payload["checks"] = tuple(checks)
    return Certificate(**payload, hash=claimed)
