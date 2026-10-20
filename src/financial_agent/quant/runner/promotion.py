"""Live grants require verified research and a clean, dated paper history."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
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


@dataclass(frozen=True)
class FillSlippage:
    """One evidence fill; `slippage` is None when its prices are invalid."""

    session: str
    client_order_id: str | None
    symbol: str | None
    slippage: float | None


@dataclass(frozen=True)
class LiveReadiness:
    """Certificate and paper evidence for one identity; `reasons` lists unmet gates.

    Excludes the environment opt-in and grants nothing; see `authorize_live`.
    """

    evaluated_at: datetime
    certificate_sha256: str | None
    certificate_passed: bool | None
    certificate_identity_match: bool | None
    certificate_age_days: float | None
    certificate_expires_at: datetime | None
    max_certificate_age_days: int
    clean_sessions: int
    min_paper_sessions: int
    window: tuple[str, ...]
    halted_in_window: int
    max_halted_sessions: int
    breaks_in_window: int
    max_reconciliation_breaks: int
    fills: tuple[FillSlippage, ...]
    mean_slippage: float | None
    slippage_allowance: float
    reasons: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.reasons


def live_readiness(
    config: TradingConfig,
    *,
    now: datetime,
    certificate: str | Path | None = None,
    journal: str | Path | Journal | None = None,
) -> LiveReadiness:
    """Read only the certificate and paper journal; never contact a broker.

    Defaults come from the config's `[promotion]` table.
    """
    policy = LivePolicy.load()
    if now.utcoffset() is None:
        raise PromotionError(["now must be timezone-aware"])
    reasons: list[str] = []
    cert_path = certificate or config.certificate_path
    cert = None
    identity_match: bool | None = None
    age: timedelta | None = None
    if cert_path is None:
        reasons.append("promotion.certificate is required")
    else:
        try:
            # Verify integrity independently of verdict/identity/age to list each.
            cert = verify_certificate(
                cert_path, max_age_days=365000, require_passed=False, now=now
            )
        except (CertificateError, OSError):
            reasons.append("certificate verification failed")
        if cert is not None:
            age = now - datetime.fromisoformat(cert.created_at)
            if age > timedelta(days=policy.max_certificate_age_days):
                reasons.append("certificate is older than live policy permits")
            if not cert.passed:
                reasons.append("certificate did not pass validation")
            strategy_match = cert.strategy == config.strategy_name
            if not strategy_match:
                reasons.append("certificate strategy mismatch")
            params_match = _canonical(cert.params) == _canonical(config.strategy_params)
            if not params_match:
                reasons.append("certificate params mismatch")
            identity_match = strategy_match and params_match
    paper = journal or config.paper_journal_path
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
            or payload.get("broker_kind") != config.broker_kind
            or config.broker_kind not in ("alpaca", "ibkr")
            or payload.get("strategy") != config.strategy_name
            or _canonical(payload.get("params")) != identity
        ):
            continue
        day = payload.get("session", "")
        try:
            if date.fromisoformat(day) > now.date():
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
    halted = sum(p["status"] == "HALTED" for p in recent)
    if halted > policy.max_halted_sessions:
        reasons.append("HALTED paper sessions in the last evidence window")
    breaks = sum(int(p.get("reconciliation_breaks", 0)) for p in recent)
    if breaks > policy.max_reconciliation_breaks:
        reasons.append("reconciliation breaks in the last evidence window")
    modeled = (
        config.backtest.costs.half_spread_bps + config.backtest.costs.slippage_bps
    ) / 10000
    allowance = modeled * policy.max_slippage_multiple
    fills = [
        _fill_slippage(e.payload)
        for e in records
        if e.type == "fill"
        and e.payload.get("broker_kind") == config.broker_kind
        and e.payload.get("session", "")[:10] in recent_days
    ]
    mean: float | None = None
    # Evidence without fills cannot establish realized execution quality.
    if not fills:
        reasons.append("paper slippage evidence is missing")
    elif any(f.slippage is None for f in fills):
        reasons.append("paper slippage evidence is invalid")
    else:
        mean = sum(f.slippage or 0.0 for f in fills) / len(fills)
        if mean > allowance + 1e-12:
            reasons.append("realized paper slippage exceeds modeled allowance")
    return LiveReadiness(
        now,
        cert.hash if cert is not None else None,
        cert.passed if cert is not None else None,
        identity_match,
        age / timedelta(days=1) if age is not None else None,
        (
            datetime.fromisoformat(cert.created_at)
            + timedelta(days=policy.max_certificate_age_days)
            if cert is not None
            else None
        ),
        policy.max_certificate_age_days,
        clean,
        policy.min_paper_sessions,
        tuple(recent_days),
        halted,
        policy.max_halted_sessions,
        breaks,
        policy.max_reconciliation_breaks,
        tuple(fills),
        mean,
        allowance,
        tuple(reasons),
    )


def _fill_slippage(payload: Mapping[str, Any]) -> FillSlippage:
    try:
        price, reference = float(payload["price"]), float(payload["reference_price"])
        valid = all(math.isfinite(v) and v > 0 for v in (price, reference))
        slippage = abs(price / reference - 1) if valid else None
    except (KeyError, ValueError, TypeError):
        slippage = None
    return FillSlippage(
        str(payload.get("session", ""))[:10],
        payload.get("client_order_id"),
        payload.get("symbol"),
        slippage,
    )


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
    current = now or datetime.now(timezone.utc)
    if current.utcoffset() is None:
        raise PromotionError(["now must be timezone-aware"])
    reasons: list[str] = []
    if environ.get("FA_QUANT_ALLOW_LIVE") != "1":
        reasons.append("FA_QUANT_ALLOW_LIVE must equal 1")
    readiness = live_readiness(
        config,
        now=current,
        certificate=certificate_path or certificate,
        journal=paper_journal_path or journal,
    )
    reasons.extend(readiness.reasons)
    if reasons:
        raise PromotionError(reasons)
    assert readiness.certificate_sha256 is not None
    return LiveAuthorization(
        config.strategy_name,
        sha256(_canonical(config.strategy_params)).hexdigest(),
        readiness.certificate_sha256,
        current,
        current + timedelta(minutes=LivePolicy.load().authorization_minutes),
    )
