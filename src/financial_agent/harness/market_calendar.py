"""The exchange calendar for run dates: one rule set for every model.

The same market holiday has been labelled three ways in the run history, and
weekend runs publish ``REVIEW_ONLY`` under one model and ``NO_TRADE`` under
another. A session is computed here from the NYSE calendar that
``settlement_ledger.py`` already uses for settlement timing, so status replay,
the run driver, and settlement agree on what a trading day is.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass

from financial_agent.harness.helpers import load_helper

TRADING = "TRADING"
WEEKEND = "WEEKEND"
HOLIDAY = "HOLIDAY"


@dataclass(frozen=True)
class Session:
    date: str
    kind: str  # TRADING | WEEKEND | HOLIDAY
    basis_date: str  # the most recent trading day at or before ``date``

    @property
    def trading_day(self) -> bool:
        return self.kind == TRADING

    def describe(self) -> str:
        if self.trading_day:
            return f"{self.date} is a trading day"
        what = "a weekend" if self.kind == WEEKEND else "a market holiday"
        return f"{self.date} is {what}; last close {self.basis_date}"


def session(day: str | dt.date) -> Session:
    """Classify ``day`` (``YYYY-MM-DD``) against the NYSE calendar."""
    date = dt.date.fromisoformat(day) if isinstance(day, str) else day
    ledger = load_helper("settlement_ledger")
    if ledger.is_trading_day(date):
        kind = TRADING
    elif date.weekday() >= 5:
        kind = WEEKEND
    else:
        kind = HOLIDAY
    basis = ledger.most_recent_trading_day_at_or_before(date)
    return Session(date.isoformat(), kind, basis.isoformat())
