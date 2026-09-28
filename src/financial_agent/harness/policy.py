"""Rules-as-code: the numeric policy a model must never re-derive by hand.

``equity_policy.toml`` holds the numbers from ``rules.md``; this module turns
them into pure functions (mu prior, CI, VaR/CVaR, Kelly, score trace) and
into a governance check for self-evolution proposals, so "only the evolution
agent may change the mu table, with evidence" becomes a code path.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

DEFAULT_POLICY_PATH = Path(__file__).with_name("equity_policy.toml")
FAMILIES = ("fund_z", "tech_z", "sent_z", "macro_z")
_MISSING = object()


@dataclass(frozen=True)
class MuBand:
    min_pctl: float
    mu: float
    sleeve: str


@dataclass(frozen=True)
class KellySizing:
    raw: float
    fractional: float  # fraction x raw, uncapped: the investability-gate input
    weight: float  # fractional clipped to [0, single-name cap]: the sizing input
    gate: str  # BLOCKED | PENALTY | OK | CAP_BINDING


class Policy:
    """Read-only view over a policy document with typed helpers."""

    def __init__(self, data: Mapping[str, Any], source: str = "<memory>") -> None:
        self.data = data
        self.source = source

    @property
    def version(self) -> str:
        return str(self.data["policy_version"])

    @property
    def effective_date(self) -> str:
        return str(self.data["effective_date"])

    def get(self, dotted: str) -> Any:
        node: Any = self.data
        for part in dotted.split("."):
            node = node[part]
        return node

    def num(self, dotted: str) -> float:
        return float(self.get(dotted))

    @property
    def family_weights(self) -> dict[str, float]:
        return {k: float(v) for k, v in self.get("score.family_weights").items()}

    @property
    def mu_bands(self) -> list[MuBand]:
        bands = [
            MuBand(float(b["min_pctl"]), float(b["mu"]), str(b["sleeve"]))
            for b in self.get("forecast.mu_bands")
        ]
        return sorted(bands, key=lambda b: b.min_pctl, reverse=True)

    def mu_prior(self, pctl: float) -> MuBand | None:
        """Calibration-table band for a percentile; ``None`` means do not rank."""
        return next((b for b in self.mu_bands if pctl >= b.min_pctl), None)

    def spy_mu_prior(self, regime: str) -> float:
        return float(self.get("market_forecast.spy_regime_prior")[regime])

    def target_price(self, entry: float, mu: float) -> float:
        return entry * (1 + mu)

    def ci70(self, entry: float, mu: float, sigma: float) -> tuple[float, float]:
        z = self.num("forecast.ci70_z")
        return entry * (1 + mu - z * sigma), entry * (1 + mu + z * sigma)

    def var95(self, mu: float, sigma: float) -> float:
        """Parametric one-month VaR in return space (decimal, not percent)."""
        return mu - self.num("forecast.var95_z") * sigma

    def cvar95(self, mu: float, sigma: float) -> float:
        return mu - self.num("forecast.cvar95_z") * sigma

    def kelly(self, mu: float, sigma: float) -> KellySizing:
        """``mu / sigma^2`` fallback Kelly, with both the gate and sizing views.

        The two views are separate fields on purpose: historical ledgers store
        one number called ``kelly_025`` that some runs cap at 5% and others do
        not, which makes the ``< 2%`` and cap-binding gates unreproducible.
        """
        raw = mu / sigma**2
        fractional = self.num("kelly.fraction") * raw
        cap = self.num("risk.max_single_name_weight")
        weight = min(max(fractional, 0.0), cap)
        if fractional <= self.num("kelly.block_at_or_below"):
            gate = "BLOCKED"
        elif fractional < self.num("kelly.penalty_below"):
            gate = "PENALTY"
        elif fractional >= cap:
            gate = "CAP_BINDING"
        else:
            gate = "OK"
        return KellySizing(raw=raw, fractional=fractional, weight=weight, gate=gate)

    def composite_z(self, family_z: Mapping[str, float | None]) -> float:
        """Weighted family z; an UNAVAILABLE family contributes the policy default."""
        fallback = self.num("score.unavailable_family_contribution")
        total = 0.0
        for family, weight in self.family_weights.items():
            z = family_z.get(family)
            total += weight * (fallback if z is None else z)
        return total

    def adj_score(self, composite: float, dq: float, penalties: float) -> float:
        return composite * dq - penalties


def load_policy(path: Path | None = None) -> Policy:
    target = path or DEFAULT_POLICY_PATH
    with target.open("rb") as handle:
        return Policy(tomllib.load(handle), source=str(target))


def flatten(data: Mapping[str, Any], prefix: str = "") -> dict[str, Any]:
    """Dotted-key view; lists of tables are indexed (``forecast.mu_bands[0].mu``)."""
    out: dict[str, Any] = {}
    for key, value in data.items():
        dotted = f"{prefix}.{key}" if prefix else key
        if isinstance(value, Mapping):
            out.update(flatten(value, dotted))
        elif (
            isinstance(value, list)
            and value
            and all(isinstance(v, Mapping) for v in value)
        ):
            for index, item in enumerate(value):
                out.update(flatten(item, f"{dotted}[{index}]"))
        else:
            out[dotted] = value
    return out


def _under(key: str, prefixes: list[str]) -> bool:
    return any(
        key == p or key.startswith(p + ".") or key.startswith(p + "[") for p in prefixes
    )


@dataclass(frozen=True)
class MutationEvidence:
    """What a proposal can show: canonical settlement counts + human sign-off."""

    settled_n: int = 0
    eff_n: int = 0
    human_approved: bool = False


@dataclass(frozen=True)
class MutationVerdict:
    decision: str  # NO_CHANGE | ACCEPTABLE | DEFER | REJECT
    changed: tuple[str, ...]
    reasons: tuple[str, ...]


def check_mutation(
    old: Policy, new: Policy, evidence: MutationEvidence
) -> MutationVerdict:
    """Govern a proposed policy diff with the *old* policy's limits.

    ACCEPTABLE means the diff may be proposed for merge; adoption stays a
    reviewed change (the harness never edits its own policy file).
    """
    before, after = flatten(old.data), flatten(new.data)
    bookkeeping = {"policy_version", "effective_date"}
    changed = tuple(
        sorted(
            key
            for key in set(before) | set(after)
            if key not in bookkeeping
            and before.get(key, _MISSING) != after.get(key, _MISSING)
        )
    )
    if not changed:
        return MutationVerdict("NO_CHANGE", (), ())

    rejects: list[str] = []
    defers: list[str] = []
    protected = list(old.get("evolution.protected"))
    track_a = list(old.get("evolution.track_a"))
    for key in changed:
        if _under(key, protected) and not evidence.human_approved:
            rejects.append(f"{key}: protected rule, requires human approval")
    if new.version == old.version:
        rejects.append("policy_version must change with any rule change")
    if new.effective_date <= old.effective_date:
        rejects.append("effective_date must move forward")

    if any(_under(key, ["score.family_weights"]) for key in changed):
        step = old.num("evolution.max_family_weight_step")
        old_w, new_w = old.family_weights, new.family_weights
        if set(old_w) != set(new_w):
            rejects.append("score.family_weights: the family set cannot change")
        else:
            for family in FAMILIES:
                delta = abs(new_w[family] - old_w[family])
                if delta > step + 1e-12:
                    rejects.append(
                        f"score.family_weights.{family}: step {delta:.3f} "
                        f"exceeds {step:.2f}"
                    )
            if abs(sum(new_w.values()) - 1.0) > 1e-9:
                rejects.append("score.family_weights must sum to 1.0")

    if any(_under(key, track_a) for key in changed):
        min_n = int(old.num("evolution.track_a_min_settled_n"))
        min_eff = int(old.num("evolution.track_a_min_eff_n"))
        if evidence.settled_n < min_n or evidence.eff_n < min_eff:
            defers.append(
                f"Track A change needs settled n>={min_n} and eff_n>={min_eff} "
                f"(have n={evidence.settled_n}, eff_n={evidence.eff_n}): "
                "log as an observation and DEFER"
            )

    decision = "REJECT" if rejects else "DEFER" if defers else "ACCEPTABLE"
    return MutationVerdict(decision, changed, tuple(rejects + defers))
