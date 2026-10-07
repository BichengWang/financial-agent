from __future__ import annotations

import dataclasses
import json
import math
from typing import Any

import pytest
from conftest import OUTPUT_DIR, real_data

from financial_agent.harness.kernels import (
    EquityInputs,
    KernelError,
    MarketInputs,
    PriceRisk,
    equity_record,
    forecast_ratios,
    market_forecast_records,
    price_risk,
)
from financial_agent.harness.policy import Policy

RUN, MODEL = "2026-09-03", "claude-opus-5"
RF_1M = 0.0375 / 12  # claude-opus-5-2026-09-03 L008: 3.75% annual 3m T-bill


def compound(start: float, returns: list[float]) -> list[float]:
    closes = [start]
    for r in returns:
        closes.append(closes[-1] * (1 + r))
    return closes


def test_price_risk_on_a_levered_copy_of_spy() -> None:
    spy_r = [0.01 if i % 2 else -0.01 for i in range(60)]
    stock = compound(50.0, [2 * r for r in spy_r])
    risk = price_risk(stock, compound(400.0, spy_r))
    assert risk.beta_60d_vs_spy == pytest.approx(2.0)
    assert risk.tracking_error_1m == pytest.approx(0.0, abs=1e-12)
    assert risk.realized_vol_30d == pytest.approx(0.02 * math.sqrt(21))
    assert risk.vol_60d == pytest.approx(risk.prior_vol_30d)
    assert risk.downside_vol_30d == pytest.approx(0.0)  # every down day is -2%
    # Each -2%/+2% pair loses 0.04%, so the first close stays the peak.
    assert risk.max_drawdown_60d == pytest.approx(min(stock) / stock[0] - 1)


def test_price_risk_windows_and_drawdown() -> None:
    spy = compound(400.0, [0.01 if i % 3 else -0.005 for i in range(80)])
    # 20 extra old closes are ignored: only the latest 61 count.
    stock = [1.0] * 20 + [100.0 + i for i in range(30)] + [129.0 - i for i in range(31)]
    risk = price_risk(stock, spy, tlt_closes=spy)
    assert risk.max_drawdown_60d == pytest.approx(99.0 / 129.0 - 1)
    assert risk.beta_60d_vs_tlt == pytest.approx(risk.beta_60d_vs_spy)
    rising = price_risk([100.0 + i for i in range(61)], spy)
    assert rising.downside_vol_30d is None  # fewer than two down days
    assert rising.max_drawdown_60d == 0.0


def test_price_risk_refuses_short_or_bad_history() -> None:
    with pytest.raises(KernelError, match="need 61"):
        price_risk([1.0] * 60, [1.0] * 61)
    with pytest.raises(KernelError, match="positive"):
        price_risk([1.0] * 60 + [0.0], [1.0 + i for i in range(61)])
    with pytest.raises(KernelError, match="zero variance"):
        price_risk([1.0 + i for i in range(61)], [5.0] * 61)


def test_ratios_reproduce_vlo() -> None:
    ratios = forecast_ratios(
        0.06,
        0.084355,
        rf_1m=RF_1M,
        downside_vol=0.02566,
        beta=-0.380435,
        tracking_error=0.100104,
        max_drawdown=-0.086481,
        spy_mu=0.02,
    )
    assert ratios.sharpe == pytest.approx(0.674233, rel=1e-5)
    assert ratios.sortino == pytest.approx(2.216456, rel=5e-4)
    assert ratios.information_ratio == pytest.approx(0.675387, rel=1e-5)
    assert ratios.treynor == pytest.approx(-0.1495, rel=1e-4)
    assert ratios.basis == "EXCESS_RETURN"
    raw = forecast_ratios(0.06, 0.1)
    assert (raw.basis, raw.sortino, raw.treynor, raw.sharpe) == (
        "RAW_DIAGNOSTIC",
        None,
        None,
        pytest.approx(0.6),
    )


@real_data
def test_ratios_reproduce_every_published_name_on_2026_09_03() -> None:
    """The kernel and the run's own engine agree on all 24 names, so a
    Sortino-equals-Sharpe bug (fable 07-21) cannot recur unnoticed."""
    path = OUTPUT_DIR / f"{MODEL}-{RUN}" / "15_predictions.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    equities = [p for p in payload["predictions"] if p["type"] == "EQUITY_ALPHA"]
    assert len(equities) == 24
    for record in equities:
        m = record["score_explainability"]["metrics"]
        ratios = forecast_ratios(
            record["mu"],
            record["sigma"],
            rf_1m=RF_1M,
            downside_vol=m["downside_vol_30d"],
            beta=m["beta_60d_vs_spy"],
            tracking_error=m["tracking_error_1m"],
            spy_mu=0.02,
        )
        for name in ("sharpe", "sortino", "information_ratio", "treynor"):
            assert getattr(ratios, name) == pytest.approx(m[name], rel=5e-4), (
                record["ticker"],
                name,
            )


def vlo_inputs(**changes: Any) -> EquityInputs:
    """VLO's grounded inputs from claude-opus-5-2026-09-03 (L200, L500, L008)."""
    values: dict[str, Any] = {
        "ticker": "VLO",
        "entry_price": 370.69,
        "price_tag": "DELAYED",
        "price_date": RUN,
        "benchmark_price": 773.17,
        "sigma": 0.084355,
        "sigma_source": "REALIZED_VOL_30D",
        "pctl": 100.0,
        "family_z": {
            "fund_z": None,
            "tech_z": 1.41521,
            "sent_z": None,
            "macro_z": 0.275568,
        },
        "data_quality_multiplier": 0.8,
        "confidence": "LOW",
        "thesis": "Technical/Macro-only composite; monitoring sleeve only.",
        "rf_1m": RF_1M,
        "spy_mu": 0.02,
        "risk": PriceRisk(
            beta_60d_vs_spy=-0.380435,
            realized_vol_30d=0.084355,
            prior_vol_30d=0.09,
            vol_60d=0.09,
            downside_vol_30d=0.02566,
            tracking_error_1m=0.100104,
            max_drawdown_60d=-0.086481,
        ),
        "ledger_rows": ("L200", "L500"),
        "extra": {"sector": "Energy"},
    }
    values.update(changes)
    return EquityInputs(**values)


def test_equity_record_reproduces_the_published_vlo_numbers(policy: Policy) -> None:
    record = equity_record(RUN, MODEL, vlo_inputs(), policy)
    # The run's engine used unrounded sigma; the ledger stores 6 places.
    assert (record["ci70_lo"], record["ci70_hi"]) == (
        pytest.approx(360.411, abs=2e-4),
        pytest.approx(425.4518, abs=2e-4),
    )
    assert (record["target_date"], record["target_price"]) == ("2026-10-01", 392.9314)
    assert record["adj_score"] == pytest.approx(0.372719, abs=1e-6)
    explain = record["score_explainability"]
    assert explain["composite_z"] == pytest.approx(0.465898, abs=1e-6)
    m = explain["metrics"]
    assert (m["var95"], m["cvar95"]) == (-0.079186, -0.113771)
    assert m["kelly_raw"] == pytest.approx(8.431961, rel=1e-5)
    assert m["kelly_fractional"] == pytest.approx(2.10799, rel=1e-5)
    assert (m["position_weight"], m["kelly_gate"]) == (0.05, "CAP_BINDING")
    assert m["kelly_method"] == "MU_OVER_SIGMA2" and "kelly_025" not in m
    assert m["sharpe"] == pytest.approx(0.674233, rel=1e-5)
    # Pctl 100 sits in an investable band, but 2 of 4 families cannot pass.
    assert (record["mu"], record["sleeve"], record["sector"]) == (
        0.06,
        "MONITORING",
        "Energy",
    )


def test_confidence_can_be_lowered_never_raised(policy: Policy) -> None:
    # The run published VLO at MEDIUM; rules.md § Confidence Labels needs
    # 3 of 4 supportive families for MEDIUM.
    with pytest.raises(KernelError, match="exceeds the ceiling LOW"):
        equity_record(RUN, MODEL, vlo_inputs(confidence="MEDIUM"), policy)


def test_full_evidence_record_is_investable_once_promoted(
    policy: Policy, promoted_policy: Policy
) -> None:
    families = {"fund_z": 0.6, "tech_z": 0.9, "sent_z": 0.5, "macro_z": 0.4}
    inputs = vlo_inputs(
        family_z=families,
        pctl=92.0,
        sigma=0.08,
        data_quality_multiplier=0.9,
        confidence="HIGH",
        mu_adjustment=-0.01,
        mu_adjustment_reason="L512 sector breadth fading",
    )
    record = equity_record(RUN, MODEL, inputs, promoted_policy)
    assert (record["sleeve"], record["mu"], record["mu_prior"]) == (
        "INVESTABLE",
        0.04,
        0.05,
    )
    assert record["mu_adjustment_reason"] == "L512 sector breadth fading"
    with pytest.raises(KernelError, match="fund_z is SHADOW"):
        equity_record(RUN, MODEL, inputs, policy)
    # Earnings inside 14 days caps LOW, from the flag or the record's own field.
    for soon in (
        {"earnings_within_window": True},
        {"extra": {"days_to_earnings": 6}},
    ):
        with pytest.raises(KernelError, match="earnings inside the window"):
            equity_record(
                RUN, MODEL, dataclasses.replace(inputs, **soon), promoted_policy
            )


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"pctl": 59.9}, "do not rank"),
        ({"mu_adjustment": 0.025, "mu_adjustment_reason": "x"}, "exceeds"),
        ({"mu_adjustment": 0.01}, "needs a stated"),
        ({"horizon_days": 30}, "horizon 30d"),
        ({"price_tag": "FRESH"}, "price_tag"),
        ({"sigma": 8.4}, "out of range"),
        ({"family_z": {"value_z": 1.0}}, "unknown families"),
        ({"extra": {"mu": 0.09}}, "may not override"),
    ],
)
def test_equity_record_refuses_inputs_outside_the_policy(
    policy: Policy, changes: dict[str, Any], message: str
) -> None:
    with pytest.raises(KernelError, match=message):
        equity_record(RUN, MODEL, vlo_inputs(**changes), policy)


def test_inputs_from_json_reject_unknown_keys() -> None:
    data = {
        "ticker": "VLO",
        "entry_price": 1.0,
        "price_tag": "DELAYED",
        "price_date": RUN,
        "benchmark_price": 1.0,
        "sigma": 0.1,
        "sigma_source": "IV30",
        "pctl": 90.0,
        "family_z": {},
        "data_quality_multiplier": 1.0,
        "confidence": "LOW",
        "thesis": "t",
    }
    assert EquityInputs.from_mapping(data).ticker == "VLO"
    with pytest.raises(KernelError, match="unknown equity input"):
        EquityInputs.from_mapping(dict(data, adj_score=0.5))
    with pytest.raises(KernelError, match="missing"):
        EquityInputs.from_mapping({"ticker": "VLO"})


def etf_inputs() -> list[MarketInputs]:
    """claude-opus-5-2026-09-03 core ETF inputs (L002-L005b)."""
    reason = "both RS20 and RS60 negative vs SPY"
    return [
        MarketInputs("SPY", 773.17, "DELAYED", RUN, 0.032999, "REALIZED_VOL_30D", "t"),
        MarketInputs(
            "QQQ",
            717.67,
            "DELAYED",
            RUN,
            0.057128,
            "REALIZED_VOL_30D",
            "t",
            beta_vs_spy=1.700616,
            mu_adjustment=-0.015,
            mu_adjustment_reason=reason,
        ),
        MarketInputs(
            "SOXX",
            502.2,
            "DELAYED",
            RUN,
            0.138752,
            "REALIZED_VOL_30D",
            "t",
            beta_vs_spy=3.240214,
            mu_adjustment=-0.015,
            mu_adjustment_reason=reason,
        ),
    ]


def test_market_forecasts_reproduce_the_published_core_etfs(policy: Policy) -> None:
    records = market_forecast_records(RUN, MODEL, "BULL", etf_inputs(), policy)
    published = {
        "SPY": (0.02, 762.0991, 815.1677),
        "QQQ": (0.019012, 688.6754, 773.9537),
        "SOXX": (0.049804, 454.7431, 599.6803),
    }
    for record in records:
        mu, lo, hi = published[record["ticker"]]
        assert record["mu"] == mu
        assert record["ci70_lo"] == pytest.approx(lo, abs=5e-4)
        assert record["ci70_hi"] == pytest.approx(hi, abs=5e-4)
    spy, qqq, _ = records
    assert spy["mu_derivation"] == "regime prior for BULL; no adjustment applied"
    assert qqq["mu_derivation"].startswith("beta 1.7006 x SPY mu +2.0000% = +3.4012%")
    assert all(r["benchmark"] == "NONE" and r["adj_score"] is None for r in (spy, qqq))


def test_market_forecasts_refuse_inputs_outside_the_policy(policy: Policy) -> None:
    spy, qqq, soxx = etf_inputs()
    with pytest.raises(KernelError, match="must be exactly"):
        market_forecast_records(RUN, MODEL, "BULL", [spy, qqq], policy)
    with pytest.raises(KernelError, match="regime"):
        market_forecast_records(RUN, MODEL, "EUPHORIA", [spy, qqq, soxx], policy)
    too_far = MarketInputs(**{**qqq.__dict__, "mu_adjustment": -0.02})
    with pytest.raises(KernelError, match="exceeds"):
        market_forecast_records(RUN, MODEL, "BULL", [spy, too_far, soxx], policy)
    no_beta = MarketInputs(**{**soxx.__dict__, "beta_vs_spy": None})
    with pytest.raises(KernelError, match="needs beta_vs_spy"):
        market_forecast_records(RUN, MODEL, "BULL", [spy, qqq, no_beta], policy)
