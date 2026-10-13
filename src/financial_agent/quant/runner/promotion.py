"""Live grants require verified research and a clean, dated paper history."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
import math
from pathlib import Path
import tomllib
from typing import Any

from ..execution import Journal, LiveAuthorization
from ..validation import CertificateError, verify_certificate
from .config import TradingConfig


class PromotionError(ValueError):
    """All independently observable unmet conditions, without credential values."""

    def __init__(self, reasons: list[str]) -> None:
        self.reasons = reasons
        super().__init__("; ".join(reasons))


@dataclass(frozen=True)
class LivePolicy:
    max_certificate_age_days: int
    min_paper_sessions: int
    max_halted_sessions: int
    max_reconciliation_breaks: int
    max_slippage_multiple: float
    authorization_minutes: int

    @classmethod
    def load(cls) -> "LivePolicy":
        """Thresholds are packaged policy data, never per-run overrides."""
        path = Path(__file__).parents[1] / "quant_policy.toml"
        return cls(**tomllib.loads(path.read_text())["live"])


def _canonical(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def authorize_live(
    config: TradingConfig,
    *,
    certificate_path: str | Path | None = None,
    paper_journal_path: str | Path | None = None,
    environ: Mapping[str, str],
    now: datetime | None = None,
    certificate: str | Path | None = None,
    journal: str | Path | Journal | None = None,
) -> LiveAuthorization:
    """Aggregate failures; contract aliases certificate/journal remain accepted."""
    policy = LivePolicy.load()
    current = now or datetime.now(timezone.utc)
    if current.utcoffset() is None:
        raise PromotionError(["now must be timezone-aware"])
    reasons: list[str] = []
    if environ.get("FA_QUANT_ALLOW_LIVE") != "1":
        reasons.append("FA_QUANT_ALLOW_LIVE must equal 1")
    cert_path = certificate_path or certificate or config.certificate_path
    cert = None
    if cert_path is None:
        reasons.append("promotion.certificate is required")
    else:
        try:
            # Verify integrity independently of verdict/identity/age to list each.
            cert = verify_certificate(
                cert_path, max_age_days=365000, require_passed=False, now=current
            )
        except (CertificateError, OSError):
            reasons.append("certificate verification failed")
        if cert is not None:
            age = current - datetime.fromisoformat(cert.created_at)
            if age > timedelta(days=policy.max_certificate_age_days):
                reasons.append("certificate is older than live policy permits")
            if not cert.passed:
                reasons.append("certificate did not pass validation")
            if cert.strategy != config.strategy_name:
                reasons.append("certificate strategy mismatch")
            if _canonical(cert.params) != _canonical(config.strategy_params):
                reasons.append("certificate params mismatch")
    paper = paper_journal_path or journal or config.paper_journal_path
    records = []
    if paper is None:
        reasons.append("promotion.paper_journal is required")
    else:
        try:
            source = paper if isinstance(paper, Journal) else Journal(paper)
            if not source.path.is_file():
                raise ValueError("missing journal")
            records = source.events()
        except (RuntimeError, ValueError, OSError):
            reasons.append("paper journal verification failed")
    # A rerun is not another session, and a dry run supplies no capital evidence.
    sessions: dict[str, dict[str, Any]] = {}
    identity = _canonical(config.strategy_params)
    for event in records:
        payload = event.payload
        if event.type != "session_outcome" or payload.get("dry_run"):
            continue
        if (
            payload.get("mode") != "paper"
            or payload.get("broker_kind") != "alpaca"
            or payload.get("strategy") != config.strategy_name
            or _canonical(payload.get("params")) != identity
        ):
            continue
        day = payload.get("session", "")
        try:
            from datetime import date

            if date.fromisoformat(day) > current.date():
                continue
        except (ValueError, TypeError):
            continue
        if payload.get("status") not in ("TRADED", "NO_CHANGE", "HALTED"):
            continue
        old = sessions.get(day)
        # Never let a successful retry erase a halt on that session.
        if old is None or payload["status"] == "HALTED":
            sessions[day] = payload
    recent_days = sorted(sessions)[-policy.min_paper_sessions :]
    recent = [sessions[s] for s in recent_days]
    clean = sum(p["status"] in ("TRADED", "NO_CHANGE") for p in sessions.values())
    if clean < policy.min_paper_sessions:
        reasons.append(f"paper sessions {clean} < {policy.min_paper_sessions}")
    if sum(p["status"] == "HALTED" for p in recent) > policy.max_halted_sessions:
        reasons.append("HALTED paper sessions in the last evidence window")
    breaks = sum(int(p.get("reconciliation_breaks", 0)) for p in recent)
    if breaks > policy.max_reconciliation_breaks:
        reasons.append("reconciliation breaks in the last evidence window")
    fills = [
        e.payload
        for e in records
        if e.type == "fill"
        and e.payload.get("broker_kind") == "alpaca"
        and e.payload.get("session", "")[:10] in recent_days
    ]
    # Evidence without fills cannot establish realized execution quality.
    if not fills:
        reasons.append("paper slippage evidence is missing")
    else:
        modeled = (
            config.backtest.costs.half_spread_bps + config.backtest.costs.slippage_bps
        ) / 10000
        try:
            slippage = []
            for fill in fills:
                price, reference = float(fill["price"]), float(fill["reference_price"])
                if not all(math.isfinite(v) and v > 0 for v in (price, reference)):
                    raise ValueError("invalid fill price")
                slippage.append(abs(price / reference - 1))
            if sum(slippage) / len(slippage) > (
                modeled * policy.max_slippage_multiple + 1e-12
            ):
                reasons.append("realized paper slippage exceeds modeled allowance")
        except (KeyError, ValueError, TypeError, ZeroDivisionError):
            reasons.append("paper slippage evidence is invalid")
    if reasons:
        raise PromotionError(reasons)
    assert cert is not None
    return LiveAuthorization(
        config.strategy_name,
        sha256(identity).hexdigest(),
        cert.hash,
        current,
        current + timedelta(minutes=policy.authorization_minutes),
    )
