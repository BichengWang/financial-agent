"""Guard against two sources of truth while rules.md prose is still canonical.

Until Phase 3 generates the rules.md tables from equity_policy.toml, this test
fails whenever one side changes without the other.
"""

from __future__ import annotations

import re

import pytest
from conftest import OUTPUT_DIR, REPO, real_data

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
        (
            r"more than (\d+) names with earnings inside",
            "evidence.max_earnings_names",
            1,
        ),
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


def test_shadow_families(policy: Policy) -> None:
    match = re.search(r"must not fold `(\w+)`/`(\w+)` into `Adj Score`", RULES)
    assert match
    assert policy.shadow_families == match.groups()


@pytest.mark.parametrize("label", ["HIGH", "MEDIUM"])
def test_confidence_labels(policy: Policy, label: str) -> None:
    match = re.search(
        rf"`{label}`: (\d) of 4 (?:factor )?families supportive, "
        r"percentile >= (\d+), data quality >= ([\d.]+)",
        RULES,
    )
    assert match
    level = label.lower()
    assert [float(g) for g in match.groups()] == [
        policy.num(f"confidence.{level}_min_families"),
        policy.num(f"confidence.{level}_min_pctl"),
        policy.num(f"confidence.{level}_min_data_quality"),
    ]


def test_holiday_status_matches_the_runbook(policy: Policy) -> None:
    runbook = (REPO / "agents/equity/daily_investment_system/runbook.md").read_text(
        encoding="utf-8"
    )
    match = re.search(r"U\.S\. market holidays still publish an `\w+` `(\w+)`", runbook)
    assert match
    assert policy.get("calendar.holiday_status") == match.group(1)


def test_family_slot_minimum_and_coverage(policy: Policy) -> None:
    assert "If fewer than two sourceable metrics support a family" in RULES
    assert policy.num("score.min_family_slots") == 2
    coverage = scalar(r"sourceable for at least (\d+)% of the eligible universe")
    assert coverage / 100 == policy.num("score.min_slot_coverage")


@real_data
def test_slots_match_the_normative_metric_definition_table(policy: Policy) -> None:
    text = (OUTPUT_DIR / "claude-opus-5-2026-09-03" / "05_factor_scores.md").read_text(
        encoding="utf-8"
    )
    families = {"Technical": "tech_z", "Macro": "macro_z"}
    rows = re.findall(r"^\| `(\w+)` \| (Technical|Macro) \|", text, re.MULTILINE)
    table: dict[str, list[str]] = {}
    for slot, family in rows[:10]:  # the Metric Definition Table comes first
        table.setdefault(families[family], []).append(slot)
    assert table == {k: list(v) for k, v in policy.get("score.slots").items()}
