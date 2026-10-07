from __future__ import annotations

import json
import math
import random
from pathlib import Path
from typing import Any

import pytest
from test_kernels import compound

from financial_agent.harness.__main__ import main
from financial_agent.harness.gates import decide_status
from financial_agent.harness.kernels import (
    Holding,
    KernelError,
    portfolio_feasibility,
)
from financial_agent.harness.lifecycle import RunStatus
from financial_agent.harness.policy import Policy

SPY_R = [0.01 if i % 2 else -0.01 for i in range(60)]
SPY = compound(400.0, SPY_R)
REQUIRED = {
    "grounded_entry_price": True,
    "price_history_60d": True,
    "sigma_fallback_chain": True,
    "next_earnings_date": True,
    "index_union_universe": True,
}


def wobble(seed: int) -> list[float]:
    """Deterministic idiosyncratic returns: about 0.3 correlation at beta 1."""
    rng = random.Random(seed)
    return [rng.gauss(0.0, 0.015) for _ in range(60)]


def name(ticker: str, beta: float, seed: int, sector: str, **kw: Any) -> Holding:
    returns = [beta * s + e for s, e in zip(SPY_R, wobble(seed))]
    return Holding(
        ticker, kw.pop("weight", 0.05), sector, compound(50.0, returns), **kw
    )


def with_basis(policy: Policy, basis: str) -> Policy:
    data = json.loads(json.dumps(policy.data))
    data["risk"]["exposure_basis"] = basis
    return Policy(data)


def test_levered_copies_of_spy_are_perfectly_correlated(policy: Policy) -> None:
    book = [
        Holding(t, 0.05, s, compound(50.0, [b * r for r in SPY_R]))
        for t, b, s in (("A", 2.0, "Tech"), ("B", 1.0, "Energy"))
    ]
    risk = portfolio_feasibility(book, SPY, policy)
    assert risk.gross == pytest.approx(0.10)
    assert risk.beta_vs_spy == pytest.approx(0.15)
    assert risk.invested_beta == pytest.approx(1.5)
    assert risk.avg_pairwise_corr == pytest.approx(1.0)
    # sigma is sum(w * beta) * spy sigma for a book of SPY copies.
    assert risk.sigma_1m == pytest.approx(0.15 * 0.01 * math.sqrt(21))
    assert risk.dd95_1m == pytest.approx(1.65 * risk.sigma_1m)
    assert risk.sector_weights == {"Energy": 0.05, "Tech": 0.05}
    assert risk.sector_shares == pytest.approx({"Energy": 0.5, "Tech": 0.5})
    assert risk.breaches == (
        "NAV beta 0.15 outside 0.90-1.10 (invested-book beta 1.50 at gross 10%)",
        "avg pairwise corr 1.00 >= 0.45",
    )


def test_a_diversified_full_book_passes(policy: Policy) -> None:
    sectors = ["Tech", "Energy", "Health", "Financials", "Industrials"]
    book = [name(f"N{i}", 1.0, i, sectors[i % 5], weight=0.05) for i in range(1, 21)]
    risk = portfolio_feasibility(book, SPY, policy)
    assert risk.gross == pytest.approx(1.0)
    assert risk.beta_vs_spy == pytest.approx(1.0, abs=0.1)
    assert risk.avg_pairwise_corr is not None and risk.avg_pairwise_corr < 0.45
    assert risk.breaches == ()
    decision = decide_status(
        data_mode="LIVE",
        required_inputs=REQUIRED,
        investable_count=len(book),
        policy=policy,
        risk_breaches=risk.breaches,
    )
    assert decision.status is RunStatus.GO


def test_exposure_basis_decides_beta_and_sector(policy: Policy) -> None:
    book = [
        name("A", 1.0, 1, "Tech"),
        name("B", 1.0, 2, "Tech"),
        name("C", 1.0, 3, "Health"),
    ]
    nav = portfolio_feasibility(book, SPY, policy)
    assert nav.basis == "NAV"
    assert any(b.startswith("NAV beta") for b in nav.breaches)
    assert not any("sector cap" in b for b in nav.breaches)  # 10% of NAV
    invested = portfolio_feasibility(book, SPY, with_basis(policy, "INVESTED"))
    assert invested.basis == "INVESTED"
    assert not any("beta" in b for b in invested.breaches)
    assert "Tech 66.67% of INVESTED > 30% sector cap" in invested.breaches
    # A NAV breach becomes NO_TRADE (Downgrade to NO_TRADE #6).
    decision = decide_status(
        data_mode="LIVE",
        required_inputs=REQUIRED,
        investable_count=5,
        policy=policy,
        risk_breaches=nav.breaches,
    )
    assert decision.status is RunStatus.NO_TRADE


def test_single_name_cap_drawdown_and_event_risk(policy: Policy) -> None:
    book = [
        name("A", 3.0, 1, "Tech", weight=0.30, earnings_within_window=True),
        name("B", 3.0, 2, "Energy", weight=0.30, earnings_within_window=True),
        name("C", 3.0, 3, "Health", weight=0.30, earnings_within_window=True),
    ]
    risk = portfolio_feasibility(book, SPY, with_basis(policy, "INVESTED"))
    assert risk.max_name_weight == pytest.approx(0.30)
    assert risk.earnings_names == ("A", "B", "C")
    text = "\n".join(risk.breaches)
    assert "A weight 30.00% > 5% single-name cap" in text
    assert "Tech 33.33% of INVESTED > 30% sector cap" in text
    assert f"INVESTED beta {risk.invested_beta:.2f} outside 0.90-1.10" in text
    assert f"dd95 1m {risk.dd95_1m:.2%} > 8%" in text
    assert "3 names with earnings inside the window (> 2): A, B, C" in text


@pytest.mark.parametrize(
    ("book", "match"),
    [
        ([], "at least one name"),
        ([("A", 0.05), ("A", 0.05)], "duplicate"),
        ([("A", 0.0)], "must be positive"),
        ([("A", 0.6), ("B", 0.6)], "exceeds NAV"),
    ],
)
def test_refuses_malformed_books(
    policy: Policy, book: list[tuple[str, float]], match: str
) -> None:
    holdings = [name(t, 1.0, i, "Tech", weight=w) for i, (t, w) in enumerate(book)]
    with pytest.raises(KernelError, match=match):
        portfolio_feasibility(holdings, SPY, policy)


def test_refuses_bad_series_and_fields(policy: Policy) -> None:
    flat = Holding("F", 0.05, "Tech", [100.0] * 61)
    with pytest.raises(KernelError, match="zero return variance"):
        portfolio_feasibility([flat], SPY, policy)
    with pytest.raises(KernelError, match="need 61"):
        portfolio_feasibility([name("A", 1.0, 1, "Tech")], SPY[:30], policy)
    with pytest.raises(KernelError, match="GICS sector"):
        portfolio_feasibility([name("A", 1.0, 1, " ")], SPY, policy)
    with pytest.raises(KernelError, match="unknown holding"):
        Holding.from_mapping({"ticker": "A", "beta": 1.0})
    with pytest.raises(KernelError, match="exposure_basis"):
        portfolio_feasibility(
            [name("A", 1.0, 1, "Tech")], SPY, with_basis(policy, "GROSS")
        )


def test_portfolio_kernel_command(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    holdings = [
        {"ticker": h.ticker, "weight": h.weight, "sector": h.sector, "closes": h.closes}
        for h in (name("A", 1.0, 1, "Tech"), name("B", 1.2, 2, "Energy"))
    ]
    path = tmp_path / "book.json"
    path.write_text(json.dumps({"holdings": holdings, "spy_closes": SPY}))
    assert main(["kernel", "portfolio", "--input", str(path)]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["basis"] == "NAV" and out["names"] == 2
    assert any(b.startswith("NAV beta") for b in out["breaches"])
