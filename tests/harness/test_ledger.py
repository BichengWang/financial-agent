from __future__ import annotations

import pytest

from financial_agent.harness.ledger import (
    LedgerError,
    Quote,
    SourceLedger,
    lint_literal_numbers,
)

T = "2026-09-03T16:28:43-04:00"


def spy_close(ledger: SourceLedger, tag: str = "DELAYED") -> str:
    return ledger.observe(
        "close",
        "SPY",
        773.17,
        unit="USD",
        observation_date="2026-09-03",
        source="https://stockanalysis.com/api/symbol/e/SPY/history",
        freshness_tag=tag,
        retrieved_at=T,
    )


def test_observed_rows_need_provenance() -> None:
    ledger = SourceLedger("claude-opus-5-2026-09-03")
    with pytest.raises(LedgerError):
        ledger.observe(
            "close",
            "SPY",
            1.0,
            unit="USD",
            observation_date="2026-09-03",
            source="x",
            freshness_tag="DELAYED",
            retrieved_at="",
        )
    with pytest.raises(LedgerError):
        ledger.observe(
            "close",
            "SPY",
            1.0,
            unit="USD",
            observation_date="09/03/2026",
            source="x",
            freshness_tag="DELAYED",
            retrieved_at=T,
        )


def test_derived_rows_inherit_unavailable() -> None:
    ledger = SourceLedger("run")
    close = spy_close(ledger)
    missing = ledger.unavailable("close", "SPY@2026-08-06", "no grounded prior price")
    row_id = ledger.derive(
        "mom_return",
        "SPY",
        formula="p1/p0 - 1",
        inputs=[close, missing],
        compute=lambda p1, p0: p1 / p0 - 1,
        unit="decimal",
    )
    row = ledger.row(row_id)
    assert row.value is None and row.claim_type == "UNAVAILABLE"
    assert missing in row.source


def test_derived_rows_take_the_weakest_freshness() -> None:
    ledger = SourceLedger("run")
    live = spy_close(ledger, "LIVE")
    old = ledger.observe(
        "close",
        "SPY",
        700.0,
        unit="USD",
        observation_date="2026-08-06",
        source="https://example.com/spy",
        freshness_tag="HISTORICAL",
        retrieved_at=T,
    )
    row = ledger.row(
        ledger.derive(
            "mom_return",
            "SPY",
            formula="p1/p0 - 1",
            inputs=[live, old],
            compute=lambda p1, p0: p1 / p0 - 1,
            unit="decimal",
        )
    )
    assert row.freshness_tag == "HISTORICAL" and row.claim_type == "DERIVED"
    assert row.value == pytest.approx(773.17 / 700 - 1)
    assert row.observation_date == "2026-09-03"


def test_price_sourcing_standard() -> None:
    ledger = SourceLedger("run")
    agree = [
        Quote("https://a.example/SPY", 100.0, T),
        Quote("https://b.example/SPY", 100.5, T),
    ]
    same_host = [
        Quote("https://a.example/1", 100.0, T),
        Quote("https://www.a.example/2", 100.0, T),
    ]
    disagree = [
        Quote("https://a.example/SPY", 100.0, T),
        Quote("https://b.example/SPY", 102.0, T),
    ]
    tool = [Quote("ibkr:get_price_snapshot", 100.0, T, from_market_data_tool=True)]

    def claim(quotes: list[Quote]) -> str:
        row_id = ledger.observe_price(
            "SPY", quotes, observation_date="2026-09-03", freshness_tag="DELAYED"
        )
        return ledger.row(row_id).claim_type

    assert claim(agree) == "OBSERVED"
    assert claim(same_host) == "UNAVAILABLE"  # one independent source
    assert claim(disagree) == "UNAVAILABLE"  # 2% apart
    assert claim(tool) == "OBSERVED"


def test_render_fills_citations_and_tracks_use() -> None:
    ledger = SourceLedger("run")
    close = spy_close(ledger)
    vol = ledger.derive(
        "rvol_30d",
        "SPY",
        formula="pstdev x sqrt(21)",
        inputs=[close],
        compute=lambda _: 0.032999,
        unit="decimal",
    )
    text = ledger.render(
        f"SPY closed at {{{{{close}}}}}, 1m vol {{{{{vol}|pct}}}}.", "09"
    )
    assert text == f"SPY closed at 773.17 ({close}), 1m vol +3.30% ({vol})."
    assert ledger.row(close).used_by == ("09",)
    with pytest.raises(LedgerError):
        ledger.render("{{L999}}", "09")


def test_literal_number_lint() -> None:
    text = (
        "SPY closed at 773.17, up 2.5%, 27/27 checks on 2026-09-03; "
        "3 of 4 families; {{L001}}"
    )
    findings = lint_literal_numbers(text)
    assert [f.split("'")[1] for f in findings] == ["773.17", "2.5%", "27/27"]
    assert len(lint_literal_numbers(text, allow=["27/27"])) == 2


def test_markdown_ledger_uses_the_runbook_schema() -> None:
    ledger = SourceLedger("run")
    spy_close(ledger)
    ledger.unavailable("iv30", "SPY", "no options feed wired")
    table = ledger.to_markdown().splitlines()
    assert table[0].startswith("| artifact | field | ticker/entity | value | unit |")
    assert table[2].startswith("| L001 | close | SPY | 773.17 | USD | 2026-09-03 |")
    assert "| L002 | iv30 | SPY | UNAVAILABLE |" in table[3]
