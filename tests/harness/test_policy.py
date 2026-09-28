from __future__ import annotations

import copy
from typing import Any

import pytest

from financial_agent.harness.policy import (
    MutationEvidence,
    Policy,
    check_mutation,
)


def bumped(policy: Policy, **changes: Any) -> Policy:
    """A copy of ``policy`` with dotted-key changes and a new version/date."""
    data = copy.deepcopy(dict(policy.data))
    data["policy_version"] = "3.4"
    data["effective_date"] = "2026-10-01"
    for dotted, value in changes.items():
        node = data
        *parents, leaf = dotted.split("__")
        for part in parents:
            node = node[part]
        node[leaf] = value
    return Policy(data)


def test_policy_mirrors_rules_md_tables(policy: Policy) -> None:
    assert sum(policy.family_weights.values()) == pytest.approx(1.0)
    top = policy.mu_prior(100)
    assert top is not None and (top.mu, top.sleeve) == (0.06, "INVESTABLE")
    edge = policy.mu_prior(80)
    assert edge is not None and (edge.mu, edge.sleeve) == (0.03, "INVESTABLE")
    below = policy.mu_prior(79.9)
    assert below is not None and (below.mu, below.sleeve) == (0.02, "MONITORING")
    assert policy.mu_prior(59.9) is None  # "do not rank"
    assert policy.spy_mu_prior("BULL") == 0.02


def test_formulas_reproduce_a_published_record(policy: Policy) -> None:
    # VLO, claude-opus-5-2026-09-03/15_predictions.json
    entry, mu, sigma = 370.69, 0.06, 0.084355
    lo, hi = policy.ci70(entry, mu, sigma)
    assert (lo, hi) == (
        pytest.approx(360.411, abs=1e-3),
        pytest.approx(425.4518, abs=1e-3),
    )
    assert policy.var95(mu, sigma) == pytest.approx(-0.079186, abs=1e-6)
    assert policy.cvar95(mu, sigma) == pytest.approx(-0.113771, abs=1e-6)
    composite = policy.composite_z(
        {"fund_z": None, "tech_z": 1.41521, "sent_z": None, "macro_z": 0.275568}
    )
    assert composite == pytest.approx(0.465898, abs=1e-6)
    assert policy.adj_score(composite, 0.8, 0.0) == pytest.approx(0.372719, abs=1e-6)
    kelly = policy.kelly(mu, sigma)
    # The run computed from unrounded sigma; the ledger stores it to 6 places.
    assert kelly.raw == pytest.approx(8.431961, rel=1e-5)
    assert kelly.fractional == pytest.approx(2.10799, rel=1e-5)
    assert (kelly.weight, kelly.gate) == (0.05, "CAP_BINDING")


@pytest.mark.parametrize(
    ("mu", "sigma", "gate"),
    [(-0.01, 0.1, "BLOCKED"), (0.0005, 0.1, "PENALTY"), (0.001, 0.1, "OK")],
)
def test_kelly_gates(policy: Policy, mu: float, sigma: float, gate: str) -> None:
    assert policy.kelly(mu, sigma).gate == gate


def test_unchanged_policy_is_no_change(policy: Policy) -> None:
    assert check_mutation(policy, policy, MutationEvidence()).decision == "NO_CHANGE"


def test_protected_rule_needs_human_approval(policy: Policy) -> None:
    proposal = bumped(policy, risk__max_single_name_weight=0.06)
    verdict = check_mutation(policy, proposal, MutationEvidence(settled_n=99, eff_n=9))
    assert verdict.decision == "REJECT"
    assert "risk.max_single_name_weight" in verdict.changed
    approved = MutationEvidence(settled_n=99, eff_n=9, human_approved=True)
    assert check_mutation(policy, proposal, approved).decision == "ACCEPTABLE"


def test_family_weight_step_limit_and_evidence_gate(policy: Policy) -> None:
    too_far = bumped(
        policy,
        score__family_weights={
            "fund_z": 0.20,
            "tech_z": 0.40,
            "sent_z": 0.25,
            "macro_z": 0.15,
        },
    )
    assert check_mutation(policy, too_far, MutationEvidence(20, 3)).decision == "REJECT"

    one_step = bumped(
        policy,
        score__family_weights={
            "fund_z": 0.25,
            "tech_z": 0.35,
            "sent_z": 0.25,
            "macro_z": 0.15,
        },
    )
    thin = check_mutation(policy, one_step, MutationEvidence(settled_n=1451, eff_n=2))
    assert thin.decision == "DEFER" and "eff_n>=3" in thin.reasons[0]
    assert (
        check_mutation(policy, one_step, MutationEvidence(1451, 3)).decision
        == "ACCEPTABLE"
    )


def test_a_proposal_cannot_relax_its_own_limits(policy: Policy) -> None:
    proposal = bumped(policy, evolution__max_family_weight_step=0.5)
    verdict = check_mutation(policy, proposal, MutationEvidence(1451, 3))
    assert verdict.decision == "REJECT"


def test_version_and_date_must_move(policy: Policy) -> None:
    data = copy.deepcopy(dict(policy.data))
    data["forecast"]["mu_bands"][0]["mu"] = 0.055
    verdict = check_mutation(policy, Policy(data), MutationEvidence(1451, 3))
    assert verdict.decision == "REJECT"
    assert "forecast.mu_bands[0].mu" in verdict.changed
