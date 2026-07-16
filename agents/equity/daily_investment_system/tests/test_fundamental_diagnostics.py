"""Regression tests for fundamental_diagnostics.py.

All tests exercise the pure parsing/computation functions against
hand-built companyfacts fixtures -- no network access. The fixture shape
(units/start/end/val for duration tags, end-only for instant tags) matches
what SEC EDGAR's real `companyfacts` endpoint returns (verified by hand
against `data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json` -- Apple --
while building this module). The staleness-fallback fixtures below use the
*actual* real-world numbers found live on 2026-07-16 (see git history):
CVS's RevenueFromContractWithCustomerExcludingAssessedTax tag has no rows
after 2019-09-30 even though the company obviously still reports revenue
(under `Revenues`, current through 2026-03-31); FFIV's `Liabilities` tag
has exactly two rows, both from 2019.
"""

from __future__ import annotations

import datetime as dt
import json
import sys
import urllib.error
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fundamental_diagnostics as fd  # type: ignore[import-not-found]  # noqa: E402

# Reference "today" for every fixture below: the fixtures' newest quarter is
# 2025-06-30, so this sits ~1 month after quarter-end (a realistic filing
# lag) and well inside the staleness window -- deterministic regardless of
# the real wall-clock date the test suite happens to run on.
_AS_OF = dt.date(2025, 8, 1)


def _duration_rows(pairs: list[tuple[str, str, float]]) -> list[dict[str, Any]]:
    return [
        {"start": s, "end": e, "val": v, "form": "10-Q", "fy": 2025}
        for s, e, v in pairs
    ]


def _instant_rows(pairs: list[tuple[str, float]]) -> list[dict[str, Any]]:
    return [{"end": e, "val": v, "form": "10-Q", "fy": 2025} for e, v in pairs]


# Six clean fiscal quarters, newest first in intent (dates ascending here,
# code sorts descending itself). idx position (0=newest .. 5=oldest) after
# sorting: revenue = [110, 105, 102, 100, 100, 100].
_REVENUE_DATES = [
    ("2024-01-01", "2024-03-31"),  # oldest (idx5)
    ("2024-04-01", "2024-06-30"),  # idx4 (year-ago of idx0)
    ("2024-07-01", "2024-09-30"),  # idx3
    ("2024-10-01", "2024-12-31"),  # idx2
    ("2025-01-01", "2025-03-31"),  # idx1
    ("2025-04-01", "2025-06-30"),  # idx0 (newest)
]
_REVENUE_VALS = [100.0, 100.0, 100.0, 102.0, 105.0, 110.0]
_GP_VALS = [38.0, 40.0, 45.0, 48.0, 50.0, 55.0]
_OI_VALS = [14.0, 15.0, 18.0, 19.0, 20.0, 22.0]
_NI_VALS = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
_OCF_VALS = [13.0, 14.0, 15.0, 16.0, 17.0, 18.0]


def _companyfacts_fixture() -> dict[str, Any]:
    def series(vals: list[float]) -> list[dict[str, Any]]:
        return _duration_rows([(s, e, v) for (s, e), v in zip(_REVENUE_DATES, vals)])

    return {
        "facts": {
            "us-gaap": {
                "RevenueFromContractWithCustomerExcludingAssessedTax": {
                    "units": {"USD": series(_REVENUE_VALS)}
                },
                "GrossProfit": {"units": {"USD": series(_GP_VALS)}},
                "OperatingIncomeLoss": {"units": {"USD": series(_OI_VALS)}},
                "NetIncomeLoss": {"units": {"USD": series(_NI_VALS)}},
                "NetCashProvidedByUsedInOperatingActivities": {
                    "units": {"USD": series(_OCF_VALS)}
                },
                "Assets": {"units": {"USD": _instant_rows([("2025-06-30", 1000.0)])}},
                "Liabilities": {
                    "units": {"USD": _instant_rows([("2025-06-30", 500.0)])}
                },
                "StockholdersEquity": {
                    "units": {
                        "USD": _instant_rows(
                            [
                                ("2024-06-30", 180.0),  # idx4
                                ("2024-09-30", 185.0),  # idx3
                                ("2024-12-31", 190.0),  # idx2
                                ("2025-03-31", 195.0),  # idx1
                                ("2025-06-30", 200.0),  # idx0
                            ]
                        )
                    }
                },
            }
        }
    }


def test_quarterly_series_filters_to_80_100_day_durations_and_sorts_newest_first() -> (
    None
):
    facts = _companyfacts_fixture()
    tag, rows = fd._quarterly_series(
        facts, ("RevenueFromContractWithCustomerExcludingAssessedTax",), _AS_OF
    )
    assert tag == "RevenueFromContractWithCustomerExcludingAssessedTax"
    assert [r["val"] for r in rows] == list(reversed(_REVENUE_VALS))


def test_quarterly_series_excludes_year_to_date_cumulative_rows() -> None:
    facts = {
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {
                        "USD": [
                            {"start": "2025-01-01", "end": "2025-03-31", "val": 100.0},
                            # 9-month YTD row (real SEC data mixes these in) --
                            # duration ~270 days, must be excluded.
                            {"start": "2024-09-29", "end": "2025-06-28", "val": 900.0},
                        ]
                    }
                }
            }
        }
    }
    _, rows = fd._quarterly_series(facts, ("Revenues",), dt.date(2025, 4, 1))
    assert len(rows) == 1
    assert rows[0]["val"] == 100.0


def test_quarterly_series_falls_back_through_tag_synonyms() -> None:
    facts = {
        "facts": {
            "us-gaap": {
                "SalesRevenueNet": {
                    "units": {
                        "USD": [
                            {"start": "2025-01-01", "end": "2025-03-31", "val": 50.0}
                        ]
                    }
                }
            }
        }
    }
    tag, rows = fd._quarterly_series(
        facts,
        (
            "RevenueFromContractWithCustomerExcludingAssessedTax",
            "Revenues",
            "SalesRevenueNet",
        ),
        dt.date(2025, 4, 1),
    )
    assert tag == "SalesRevenueNet"
    assert rows[0]["val"] == 50.0


def test_quarterly_series_missing_tag_returns_empty() -> None:
    tag, rows = fd._quarterly_series({"facts": {"us-gaap": {}}}, ("Revenues",), _AS_OF)
    assert tag == ""
    assert rows == []


def test_quarterly_series_skips_a_stale_tag_and_falls_through_to_the_next() -> None:
    # The real CVS pattern found live 2026-07-16: the first-priority tag has
    # real quarterly rows, but the newest one is years old (CVS stopped
    # filing under it after 2019-09-30) -- must not be trusted, must fall
    # through to the second tag, which is current.
    facts = {
        "facts": {
            "us-gaap": {
                "RevenueFromContractWithCustomerExcludingAssessedTax": {
                    "units": {
                        "USD": [
                            {
                                "start": "2019-07-01",
                                "end": "2019-09-30",
                                "val": 64547000000,
                            }
                        ]
                    }
                },
                "Revenues": {
                    "units": {
                        "USD": [
                            {
                                "start": "2026-01-01",
                                "end": "2026-03-31",
                                "val": 95000000000,
                            }
                        ]
                    }
                },
            }
        }
    }
    tag, rows = fd._quarterly_series(
        facts,
        ("RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"),
        dt.date(2026, 7, 16),
    )
    assert tag == "Revenues"
    assert rows[0]["val"] == 95000000000


def test_quarterly_series_returns_empty_when_every_tag_is_stale() -> None:
    facts = {
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {
                        "USD": [
                            {"start": "2019-07-01", "end": "2019-09-30", "val": 100.0}
                        ]
                    }
                }
            }
        }
    }
    tag, rows = fd._quarterly_series(facts, ("Revenues",), dt.date(2026, 7, 16))
    assert tag == ""
    assert rows == []


def test_instant_series_excludes_duration_rows_and_sorts_newest_first() -> None:
    facts = {
        "facts": {
            "us-gaap": {
                "Assets": {
                    "units": {
                        "USD": [
                            {"end": "2025-03-31", "val": 900.0},
                            {"end": "2025-06-30", "val": 1000.0},
                            {
                                "start": "2025-01-01",
                                "end": "2025-06-30",
                                "val": 12345.0,
                            },
                        ]
                    }
                }
            }
        }
    }
    _, rows = fd._instant_series(facts, ("Assets",), _AS_OF)
    assert [r["val"] for r in rows] == [1000.0, 900.0]


def test_instant_series_rejects_a_stale_reading() -> None:
    facts = {
        "facts": {
            "us-gaap": {
                "Liabilities": {
                    "units": {"USD": [{"end": "2019-09-30", "val": 1000.0}]}
                }
            }
        }
    }
    tag, rows = fd._instant_series(facts, ("Liabilities",), dt.date(2026, 7, 16))
    assert tag == ""
    assert rows == []


def test_derive_liabilities_prefers_the_raw_tag_when_fresh() -> None:
    facts = _companyfacts_fixture()
    tag, rows = fd._derive_liabilities(facts, _AS_OF)
    assert tag == "Liabilities"
    assert rows[0]["val"] == 500.0


def test_derive_liabilities_falls_back_to_assets_minus_equity_when_stale() -> None:
    # The real FFIV pattern found live 2026-07-16: Liabilities has exactly
    # two rows, both from 2019 -- must derive from the accounting identity
    # instead, using whatever fresh Assets/Equity readings share an end date.
    facts = {
        "facts": {
            "us-gaap": {
                "Liabilities": {
                    "units": {
                        "USD": [
                            {"end": "2019-06-30", "val": 1.0},
                            {"end": "2019-09-30", "val": 2.0},
                        ]
                    }
                },
                "Assets": {"units": {"USD": [{"end": "2026-03-31", "val": 1000.0}]}},
                "StockholdersEquity": {
                    "units": {"USD": [{"end": "2026-03-31", "val": 350.0}]}
                },
            }
        }
    }
    tag, rows = fd._derive_liabilities(facts, dt.date(2026, 7, 16))
    assert tag == "derived:Assets-StockholdersEquity"
    assert rows[0]["end"] == "2026-03-31"
    assert rows[0]["val"] == pytest.approx(650.0)


def test_derive_liabilities_empty_when_neither_path_available() -> None:
    facts: dict[str, Any] = {"facts": {"us-gaap": {}}}
    tag, rows = fd._derive_liabilities(facts, _AS_OF)
    assert tag == ""
    assert rows == []


def test_compute_fundamental_signals_matches_hand_computed_values() -> None:
    result = fd.compute_fundamental_signals(_companyfacts_fixture(), as_of=_AS_OF)
    values = result["values"]

    assert values["revenue_yoy_growth"] == pytest.approx(110.0 / 100.0 - 1)  # 0.10
    assert values["revenue_accel"] == pytest.approx(0.05)  # 0.10 - 0.05
    assert values["gross_margin_trend"] == pytest.approx(
        55.0 / 110.0 - 40.0 / 100.0
    )  # 0.10
    assert values["operating_margin_trend"] == pytest.approx(
        22.0 / 110.0 - 15.0 / 100.0
    )  # 0.05
    assert values["roe"] == pytest.approx(
        54.0 / 190.0
    )  # TTM NI 15+14+13+12, avg equity (200+180)/2
    assert values["leverage"] == pytest.approx(500.0 / 200.0)  # 2.5
    assert values["accrual_ratio"] == pytest.approx(
        (54.0 - 66.0) / 1000.0
    )  # TTM NI - TTM OCF, /assets
    # Absent (not None-valued), matching every other unsourced signal, since
    # no --prices-json price was given for this ticker.
    assert "fcf_yield" not in values

    for signal in values:
        assert signal in result["lineage"] or values[signal] is None


def test_compute_fundamental_signals_defaults_as_of_to_today() -> None:
    # No as_of given -> defaults to real today, so a fixture dated "now"
    # must not be rejected as stale.
    today = dt.date.today()
    facts = {
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {
                        "USD": [
                            {
                                "start": (today - dt.timedelta(days=30)).isoformat(),
                                "end": today.isoformat(),
                                "val": 100.0,
                            }
                        ]
                    }
                }
            }
        }
    }
    result = fd.compute_fundamental_signals(facts)
    # Not enough history for any signal, but the tag itself must be accepted
    # as fresh (not silently dropped for staleness).
    assert result["values"] == {}


def test_compute_fundamental_signals_falls_back_around_a_stale_revenue_tag() -> None:
    # End-to-end version of the CVS bug: the module must not report
    # revenue_yoy_growth from a 2019 filing when a fresher tag exists.
    facts = _companyfacts_fixture()
    stale = facts["facts"]["us-gaap"].pop(
        "RevenueFromContractWithCustomerExcludingAssessedTax"
    )
    # Re-date every row of the *first-priority* tag to 2019 (stale) and add
    # a *second-priority* "Revenues" tag with the real, current data.
    for row in stale["units"]["USD"]:
        row["start"] = "2019-04-01"
        row["end"] = "2019-06-30"
    facts["facts"]["us-gaap"][
        "RevenueFromContractWithCustomerExcludingAssessedTax"
    ] = stale
    facts["facts"]["us-gaap"]["Revenues"] = {
        "units": {
            "USD": [
                {"start": s, "end": e, "val": v}
                for (s, e), v in zip(_REVENUE_DATES, _REVENUE_VALS)
            ]
        }
    }
    result = fd.compute_fundamental_signals(facts, as_of=_AS_OF)
    assert result["values"]["revenue_yoy_growth"] == pytest.approx(110.0 / 100.0 - 1)
    assert result["lineage"]["revenue_yoy_growth"]["tag"] == "Revenues"


def test_compute_fundamental_signals_reports_unavailable_below_minimum_history() -> (
    None
):
    facts = {
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {
                        "USD": [
                            {"start": "2025-01-01", "end": "2025-03-31", "val": 100.0},
                            {"start": "2025-04-01", "end": "2025-06-30", "val": 110.0},
                        ]
                    }
                }
            }
        }
    }
    result = fd.compute_fundamental_signals(facts, as_of=_AS_OF)
    assert result["values"].get("revenue_yoy_growth") is None
    assert result["values"].get("revenue_accel") is None
    assert result["values"].get("roe") is None


def test_compute_fundamental_signals_computes_fcf_yield_when_price_given() -> None:
    facts = _companyfacts_fixture()
    facts["facts"]["dei"] = {
        "EntityCommonStockSharesOutstanding": {
            "units": {"shares": [{"end": "2025-06-30", "val": 10.0}]}
        }
    }
    result = fd.compute_fundamental_signals(facts, price=100.0, as_of=_AS_OF)
    ttm_ocf = sum(_OCF_VALS[2:])  # newest 4 of the 6-value list (oldest-first) = last 4
    market_cap = 100.0 * 10.0
    ev = market_cap + 500.0
    assert result["values"]["fcf_yield"] == pytest.approx(ttm_ocf / ev)


def test_fcf_yield_does_not_require_equity_data() -> None:
    # EV = price*shares + total liabilities never reads StockholdersEquity;
    # requiring it as a guard would wrongly withhold a computable signal.
    facts = _companyfacts_fixture()
    del facts["facts"]["us-gaap"]["StockholdersEquity"]
    facts["facts"]["dei"] = {
        "EntityCommonStockSharesOutstanding": {
            "units": {"shares": [{"end": "2025-06-30", "val": 10.0}]}
        }
    }
    result = fd.compute_fundamental_signals(facts, price=100.0, as_of=_AS_OF)
    assert result["values"].get("fcf_yield") is not None
    assert result["values"].get("leverage") is None  # leverage still needs equity


def test_main_reports_all_tickers_failed_when_cik_map_fetch_fails(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    def _raise() -> dict[str, int]:
        raise urllib.error.URLError("mock network failure")

    monkeypatch.setattr(fd, "fetch_ticker_cik_map", _raise)
    out_path = tmp_path / "out.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "fundamental_diagnostics.py",
            "--tickers",
            "AAPL",
            "MSFT",
            "--output",
            str(out_path),
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        fd.main()
    assert exc_info.value.code == 1

    output = json.loads(out_path.read_text())
    assert output["gating_status"] == "SHADOW"
    assert set(output["fetch_failures"]) == {"AAPL", "MSFT"}
    assert output["records"] == {}
    assert output["universe_sourceable_pct"] == 0.0
