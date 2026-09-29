"""Guard against two sources of truth while rules.md prose is still canonical.

Until Phase 3 generates the rules.md tables from equity_policy.toml, this test
fails whenever one side changes without the other.
"""

from __future__ import annotations

import re

import pytest
from conftest import REPO

from financial_agent.harness.policy import Policy

RULES = (REPO / "agents/equity/daily_investment_system/rules.md").read_text(
    encoding="utf-8"
)


def table_after(header: str) -> list[list[str]]:
    lines = RULES[RULES.index(header) :].splitlines()[2:]  # skip header + divider
    rows = []
    for line in lines:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def pct(text: str) -> float:
    return round(float(text.rstrip("%")) / 100, 6)


def scalar(pattern: str) -> float:
    match = re.search(pattern, RULES)
    assert match, pattern
    return float(match.group(1))


def test_mu_calibration_table(policy: Policy) -> None:
    rows = table_after("| Adjusted-score percentile | Prior mu (4-week) |")
    bands = [
        (float(re.findall(r"\d+", band)[0]), pct(mu), sleeve.split()[0].upper())
        for band, mu, sleeve in rows
        if not band.startswith("<")
    ]
    assert bands == [(b.min_pctl, b.mu, b.sleeve) for b in policy.mu_bands]


def test_family_weights(policy: Policy) -> None:
    keys = {"Fundamental": "fund_z", "Technical": "tech_z"}
    keys |= {"Sentiment": "sent_z", "Macro": "macro_z"}
    rows = table_after("| Family | Weight |")
    weights = {keys[name.split()[0]]: float(w) for name, w in rows}
    assert weights == policy.family_weights


def test_core_etf_regime_priors(policy: Policy) -> None:
    rows = table_after("| Declared regime | SPY prior mu (4-week) |")
    assert {regime: pct(mu) for regime, mu in rows} == {
        k: float(v) for k, v in policy.get("market_forecast.spy_regime_prior").items()
    }


@pytest.mark.parametrize(
    ("pattern", "key", "scale"),
    [
        (r"Maximum single-name weight of `(\d+)%`", "risk.max_single_name_weight", 100),
        (r"Maximum `(\d+)%` in one GICS sector", "risk.max_sector_weight", 100),
        (
            r"correlation of selected names must remain below `([\d.]+)`",
            "risk.max_avg_pairwise_corr",
            1,
        ),
        (r"drawdown target must remain at or below `(\d+)%`", "risk.max_dd95_1m", 100),
        (r"`var95 = mu - ([\d.]+)\*sigma`", "forecast.var95_z", 1),
        (r"`cvar95 = mu - ([\d.]+)\*sigma`", "forecast.cvar95_z", 1),
        (r"\(1 \+ mu - ([\d.]+)sigma\)", "forecast.ci70_z", 1),
        (r"at most ±(\d+) percentage points", "forecast.mu_adjustment_max", 100),
        (r"at or above the (\d+)th percentile", "evidence.min_pctl", 1),
        (
            r"At least (\d) of 4 factor families",
            "evidence.min_non_negative_families",
            1,
        ),
        (
            r"contributes more than (\d+)% of the total",
            "evidence.max_family_conviction_share",
            100,
        ),
        (
            r"Data completeness is at least (\d+)%",
            "evidence.min_data_completeness",
            100,
        ),
        (
            r"would fall below `([\d.]+)`, do not rank",
            "evidence.min_data_quality_multiplier",
            1,
        ),
        (r"Fewer than (\d+) names pass", "evidence.min_investable_names", 1),
        (r"`0.25 x Kelly < (\d+)% NAV`", "kelly.penalty_below", 100),
        (
            r"change limit of `\+/- ([\d.]+)` per family",
            "evolution.max_family_weight_step",
            1,
        ),
    ],
)
def test_scalar_rules(policy: Policy, pattern: str, key: str, scale: int) -> None:
    assert scalar(pattern) / scale == pytest.approx(policy.num(key))


def test_beta_band(policy: Policy) -> None:
    match = re.search(r"between `([\d.]+)` and `([\d.]+)`", RULES)
    assert match
    assert [float(match.group(1)), float(match.group(2))] == policy.get(
        "risk.beta_band"
    )
