from __future__ import annotations

import copy
import json
import statistics
from pathlib import Path
from typing import Any

import pytest
from conftest import OUTPUT_DIR, real_data
from test_kernels import MODEL, RUN, vlo_inputs

from financial_agent.harness.__main__ import main
from financial_agent.harness.helpers import load_helper
from financial_agent.harness.kernels import KernelError, PriceRisk, equity_record
from financial_agent.harness.policy import Policy
from financial_agent.harness.scoring import (
    NameInputs,
    raw_slots,
    score_request,
    score_universe,
)

LATEST = OUTPUT_DIR / f"{MODEL}-{RUN}" / "15_predictions.json"
TECH = ("mom20", "mom60", "ma_align", "macd", "vol_conf", "dd60")
MACRO = ("beta", "sector_lead", "rate_sens", "vol_stability")


def indicators(
    mom20: float, mom60: float, vol: float, ma: str = "BULLISH", macd: str = "ON_SIGNAL"
) -> dict[str, Any]:
    return {
        "status": "OK",
        "daily": {
            "momentum_20d_pct": mom20,
            "momentum_60d_pct": mom60,
            "volume_ratio_20d": vol,
            "ma_alignment": ma,
            "macd_state": macd,
        },
        "weekly": {"ma_alignment": ma, "macd_state": macd},
    }


def risk(beta: float, dd: float, tlt: float = 0.2, vol30: float = 0.08) -> PriceRisk:
    return PriceRisk(
        beta_60d_vs_spy=beta,
        realized_vol_30d=vol30,
        prior_vol_30d=0.09,
        vol_60d=0.085,
        downside_vol_30d=0.04,
        tracking_error_1m=0.07,
        max_drawdown_60d=dd,
        beta_60d_vs_tlt=tlt,
    )


def universe(n: int = 40) -> list[NameInputs]:
    """Deterministic names spread across two sectors."""
    names = []
    for i in range(n):
        names.append(
            NameInputs(
                f"T{i:02d}",
                "Energy" if i % 2 else "Tech",
                indicators(
                    i * 0.5 - 5,
                    (i * 7) % 23 - 8.0,
                    0.6 + (i % 5) * 0.2,
                    ("BULLISH", "MIXED", "BEARISH")[i % 3],
                    ("BULLISH_CROSS", "ABOVE_SIGNAL", "BELOW_SIGNAL")[i % 3 - 1],
                ),
                risk(
                    0.4 + (i % 9) * 0.15,
                    -0.02 - (i % 7) * 0.01,
                    tlt=(i % 4) * 0.2,
                    vol30=0.05 + (i % 6) * 0.01,
                ),
            )
        )
    return names


def test_slot_z_are_population_z_of_the_clipped_cross_section(
    policy: Policy,
) -> None:
    names = universe()
    names[0] = NameInputs("T00", "Tech", indicators(-500.0, 1.0, 1.0), risk(1, -0.05))
    board = score_universe(names, policy, data_quality=0.8)
    for slot in TECH + MACRO:
        z = [n.slot_z[slot] for n in board.names]
        assert None not in z, slot
        stats = next(s for s in board.slots if s.slot == slot)
        assert stats.scored and stats.n == 40 and stats.coverage == 1.0
        # Winsorizing first means z is not exactly mean 0 / stdev 1 over the
        # raw values, but it is over the clipped ones.
        assert statistics.fmean(z) == pytest.approx(0.0, abs=1e-12), slot
        assert statistics.pstdev(z) == pytest.approx(1.0), slot
    # The -500% outlier is clipped to the 5th-percentile value, not scored raw.
    mom20 = {n.ticker: n.slot_z["mom20"] for n in board.names}
    third_lowest = sorted(mom20.values())[2]
    assert mom20["T00"] == pytest.approx(third_lowest)


def test_families_sector_lead_and_coverage(policy: Policy) -> None:
    names = universe()
    board = score_universe(names, policy, data_quality=0.8)
    vlo = board.names[0]
    assert vlo.family_z["tech_z"] == pytest.approx(
        statistics.fmean(vlo.slot_z[s] for s in TECH)  # type: ignore[misc]
    )
    assert vlo.family_z["fund_z"] is None and vlo.family_z["sent_z"] is None
    energy = [n for n in names if n.sector == "Energy"]
    median = statistics.median(
        n.indicators["daily"]["momentum_60d_pct"] for n in energy
    )
    assert {board.get(n.ticker).raw["sector_lead"] for n in energy} == {median}

    # Price risk for only half the names: risk slots fall below 70% coverage
    # and score for nobody, leaving Macro_Z on one slot, so UNAVAILABLE.
    half = [
        n if i % 2 else NameInputs(n.ticker, n.sector, n.indicators)
        for i, n in enumerate(names)
    ]
    board = score_universe(half, policy, data_quality=0.8)
    skipped = {s.slot for s in board.slots if not s.scored}
    assert skipped == {"dd60", "beta", "rate_sens", "vol_stability"}
    assert all(n.family_z["macro_z"] is None for n in board.names)
    assert all(n.family_z["tech_z"] is not None for n in board.names)
    assert "| `dd60` | tech_z | 20 | 50% | not scored |" in board.slot_table()


def test_rank_percentile_and_trace(policy: Policy) -> None:
    board = score_universe(
        universe(), policy, data_quality={f"T{i:02d}": 0.8 for i in range(40)}
    )
    assert [n.rank for n in board.names] == list(range(1, 41))
    assert (board.names[0].pctl, board.names[-1].pctl) == (100.0, 0.0)
    assert board.names[1].pctl == pytest.approx(100 * 38 / 39)
    for name in board.names:
        assert name.composite_z == pytest.approx(policy.composite_z(name.family_z))
        assert name.adj_score == pytest.approx(name.composite_z * 0.8)
    # Ties share the better rank.
    same = [
        NameInputs(f"S{i}", "X", indicators(1, 1, 1), risk(1, -0.05)) for i in range(3)
    ]
    tied = score_universe(same, policy, data_quality=0.9)
    assert [n.rank for n in tied.names] == [1, 1, 1]


def test_scored_fields_feed_the_record_kernel(policy: Policy) -> None:
    board = score_universe(universe(), policy, data_quality=0.8)
    top = board.names[0]
    record = equity_record(
        RUN, MODEL, vlo_inputs(**top.equity_fields(), ticker=top.ticker), policy
    )
    assert record["pctl"] == 100.0
    assert record["adj_score"] == pytest.approx(top.adj_score, abs=1e-6)


def test_scoring_refusals(policy: Policy) -> None:
    names = universe()
    with pytest.raises(KernelError, match="no names"):
        score_universe([], policy, data_quality=0.8)
    with pytest.raises(KernelError, match="duplicate"):
        score_universe(names + names[:1], policy, data_quality=0.8)
    with pytest.raises(KernelError, match="data_quality missing for T00"):
        score_universe(names, policy, data_quality={"T01": 0.8})
    with pytest.raises(KernelError, match="outside"):
        score_universe(names, policy, data_quality=1.2)
    data = copy.deepcopy(dict(policy.data))
    data["score"]["slots"]["fund_z"] = ["mom20", "mom60"]
    with pytest.raises(KernelError, match="fund_z is SHADOW"):
        score_universe(names, Policy(data), data_quality=0.8)
    data = copy.deepcopy(dict(policy.data))
    data["score"]["slots"]["tech_z"] = ["mom20", "rsi_vibes"]
    with pytest.raises(KernelError, match="unknown slots"):
        score_universe(names, Policy(data), data_quality=0.8)


def published() -> list[dict[str, Any]]:
    payload = json.loads(LATEST.read_text(encoding="utf-8"))
    return [p for p in payload["predictions"] if p["type"] == "EQUITY_ALPHA"]


def inputs_from_record(record: dict[str, Any]) -> NameInputs:
    m = record["score_explainability"]["metrics"]
    indicator = indicators(
        m["momentum_20d_pct"],
        m["momentum_60d_pct"],
        m["volume_ratio_20d"],
        m["ma_alignment_daily"],
        m["macd_state_daily"],
    )
    indicator["weekly"] = {
        "ma_alignment": m["ma_alignment_weekly"],
        "macd_state": m["macd_state_weekly"],
    }
    price = risk(
        m["beta_60d_vs_spy"], m["max_drawdown_60d"], vol30=m["realized_vol_30d"]
    )
    return NameInputs(record["ticker"], record.get("sector"), indicator, price)


@real_data
def test_transforms_match_the_published_engine() -> None:
    """Within the clip bounds a slot's z is affine in its raw value, so the
    published 2026-09-03 z-scores pin each transform and its polarity (the
    08-03 drawdown sign flip would show up as a negative slope)."""
    records = published()
    raw = {r["ticker"]: raw_slots(inputs_from_record(r)) for r in records}
    for slot in ("mom20", "mom60", "vol_conf", "dd60", "beta"):
        points = [
            (raw[r["ticker"]][slot], r["score_explainability"]["slot_z"][slot])
            for r in records
        ]
        top = max(z for _, z in points)
        inner = [(x, z) for x, z in points if z < top - 1e-9]  # drop clipped names
        assert len(inner) >= 15, slot
        (x0, z0), (x1, z1) = min(inner), max(inner)
        slope = (z1 - z0) / (x1 - x0)
        assert slope > 0, slot
        for x, z in inner:
            assert z0 + slope * (x - x0) == pytest.approx(z, abs=2e-5), (slot, x)
    for slot in ("ma_align", "macd"):
        by_raw: dict[float | None, set[float]] = {}
        for r in records:
            z = r["score_explainability"]["slot_z"][slot]
            by_raw.setdefault(raw[r["ticker"]][slot], set()).add(z)
        assert all(len(zs) == 1 for zs in by_raw.values()), slot


@real_data
def test_family_aggregation_and_percentile_match_the_published_engine() -> None:
    scoring = load_helper("factor_scoring")
    for record in published():
        explain = record["score_explainability"]
        slot_z = explain["slot_z"]
        for family, slots in (("tech_z", TECH), ("macro_z", MACRO)):
            value, _ = scoring.composite_z({s: slot_z[s] for s in slots})
            assert value == pytest.approx(explain[family], abs=2e-6), record["ticker"]
        # INDEX_UNION_PCTL (n=508): 100 * (n - rank) / (n - 1), stored to 2 dp.
        assert record["pctl"] == pytest.approx(
            100 * (508 - record["rank"]) / 507, abs=5e-3
        )


@real_data
def test_scores_a_real_indicator_universe(policy: Policy) -> None:
    package = OUTPUT_DIR / "gpt-5-2026-07-30"
    payload = json.loads((package / "technical_indicators.json").read_text())
    sectors = {
        r["ticker"]: r["gics_sector"]
        for r in json.loads((package / "sector_manifest.json").read_text())["records"]
    }
    indicator_tickers = {r["ticker"] for r in payload["indicators"]}
    result = score_request(
        {
            "indicators": payload,
            "sectors": sectors,
            "universe": sorted(set(sectors) & indicator_tickers),
            "data_quality": 0.8,
        },
        policy,
    )
    names = result["names"]
    assert len(names) == 500
    scored = {s["slot"]: s["scored"] for s in result["slots"]}
    # Indicator slots score; price-risk slots need closes this file lacks.
    assert [s for s in TECH + MACRO if scored[s]] == [
        "mom20",
        "mom60",
        "ma_align",
        "macd",
        "vol_conf",
        "sector_lead",
    ]
    assert all(n["family_z"]["tech_z"] is not None for n in names)
    assert all(n["family_z"]["macro_z"] is None for n in names)
    assert names[0]["pctl"] == 100.0 and names[-1]["pctl"] == 0.0


def test_cli_scores_from_closes(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    spy = [400 * (1 + 0.003 * ((i % 5) - 2)) ** 0.5 + i for i in range(61)]
    records, closes = [], {}
    for k in range(4):
        ticker = f"N{k}"
        records.append({"ticker": ticker, **indicators(k, 2 * k, 1 + k / 10)})
        closes[ticker] = [50 + k + i * (0.1 + k / 20) + (i % 3) for i in range(61)]
    records.append({"ticker": "SPY", **indicators(1, 1, 1)})
    request = {
        "indicators": records,
        "sectors": {"N0": "A", "N1": "A", "N2": "B", "N3": "B"},
        "closes": closes,
        "spy_closes": spy,
        "tlt_closes": [100 - i / 10 + (i % 4) for i in range(61)],
        "data_quality": 0.9,
        "penalties": {"N3": 0.1},
    }
    path = tmp_path / "score.json"
    path.write_text(json.dumps(request), encoding="utf-8")
    assert main(["kernel", "score", "--input", str(path)]) == 0
    result = json.loads(capsys.readouterr().out)
    # The core ETF never counts toward the universe percentile.
    assert sorted(n["ticker"] for n in result["names"]) == ["N0", "N1", "N2", "N3"]
    assert all(s["scored"] for s in result["slots"])
    n3 = next(n for n in result["names"] if n["ticker"] == "N3")
    assert n3["adj_score"] == pytest.approx(n3["composite_z"] * 0.9 - 0.1)
