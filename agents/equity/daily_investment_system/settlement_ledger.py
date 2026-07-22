#!/usr/bin/env python3
"""Canonical settlement ledger for the daily investment system.

Prediction source ledgers (`15_predictions.json`) are immutable and retain
`status: OPEN` forever; every model's daily run independently re-scans prior
packages and appends its own `settlements` rows for whatever it believes is
due. Because many runs settle the same logical prediction, the same
canonical settlement accumulates duplicate rows across packages -- often
with conflicting settlement-timing conventions (see `rules.md` Settlement
Rules) and with key names that drifted across sessions (`settle_price` /
`settlement_price` / `current_price`, `settle_date` / `settlement_date` /
`current_price_date`, etc.).

This module is the single normalizer, timing validator, and precedence
resolver for that data. It only reads `agents/equity/output/*/15_predictions.json`
files and produces a derived, machine-readable manifest -- it never edits a
source file. See `plan/2026-07-15-canonical-settlement-ledger.md` for the
design this implements.

Canonical key: (model, vintage, ticker, type, target_date), where `vintage`
is the run_date of the *original* prediction and `type` defaults to
"EQUITY_ALPHA" when absent, per rules.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

CanonicalKey = tuple[str, str, str, str, str]


# ---------------------------------------------------------------------------
# Trading calendar (weekends + computed NYSE holiday rules; no hardcoded
# per-year table so this keeps working past 2026 without maintenance).
# ---------------------------------------------------------------------------


def _nth_weekday(year: int, month: int, weekday: int, n: int) -> dt.date:
    """The n-th (1-indexed) occurrence of `weekday` (Mon=0) in year/month."""
    first = dt.date(year, month, 1)
    offset = (weekday - first.weekday()) % 7
    return first + dt.timedelta(days=offset + 7 * (n - 1))


def _last_weekday(year: int, month: int, weekday: int) -> dt.date:
    if month == 12:
        last_of_month = dt.date(year + 1, 1, 1) - dt.timedelta(days=1)
    else:
        last_of_month = dt.date(year, month + 1, 1) - dt.timedelta(days=1)
    offset = (last_of_month.weekday() - weekday) % 7
    return last_of_month - dt.timedelta(days=offset)


def _easter_sunday(year: int) -> dt.date:
    """Anonymous Gregorian algorithm for the date of Easter Sunday."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    ll = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * ll) // 451
    month = (h + ll - 7 * m + 114) // 31
    day = ((h + ll - 7 * m + 114) % 31) + 1
    return dt.date(year, month, day)


def _observed(holiday: dt.date) -> dt.date:
    """NYSE fixed-date holidays: Sat -> preceding Fri, Sun -> following Mon."""
    if holiday.weekday() == 5:
        return holiday - dt.timedelta(days=1)
    if holiday.weekday() == 6:
        return holiday + dt.timedelta(days=1)
    return holiday


def us_market_holidays(year: int) -> set[dt.date]:
    """Approximate NYSE holiday calendar for `year`."""
    holidays = {
        _observed(dt.date(year, 1, 1)),  # New Year's Day
        _nth_weekday(year, 1, 0, 3),  # MLK Day
        _nth_weekday(year, 2, 0, 3),  # Washington's Birthday
        _easter_sunday(year) - dt.timedelta(days=2),  # Good Friday
        _last_weekday(year, 5, 0),  # Memorial Day
        _observed(dt.date(year, 6, 19)),  # Juneteenth
        _observed(dt.date(year, 7, 4)),  # Independence Day
        _nth_weekday(year, 9, 0, 1),  # Labor Day
        _nth_weekday(year, 11, 3, 4),  # Thanksgiving
        _observed(dt.date(year, 12, 25)),  # Christmas
    }
    # New Year's Day observance is the only holiday whose Sat/Sun shift can
    # cross a calendar-year boundary (Jan 1 on a Saturday -> observed the
    # prior Dec 31, e.g. 2022-01-01 -> 2021-12-31). is_trading_day() looks
    # holidays up by the *queried* date's own year, so that shifted date
    # must also be included in the set for the year it actually falls in.
    next_new_year_observed = _observed(dt.date(year + 1, 1, 1))
    if next_new_year_observed.year == year:
        holidays.add(next_new_year_observed)
    return holidays


_HOLIDAY_CACHE: dict[int, set[dt.date]] = {}


def is_trading_day(day: dt.date) -> bool:
    if day.weekday() >= 5:
        return False
    if day.year not in _HOLIDAY_CACHE:
        _HOLIDAY_CACHE[day.year] = us_market_holidays(day.year)
    return day not in _HOLIDAY_CACHE[day.year]


def prior_trading_day(day: dt.date) -> dt.date:
    """The most recent trading day strictly before `day`."""
    cur = day - dt.timedelta(days=1)
    while not is_trading_day(cur):
        cur -= dt.timedelta(days=1)
    return cur


def most_recent_trading_day_at_or_before(day: dt.date) -> dt.date:
    cur = day
    while not is_trading_day(cur):
        cur -= dt.timedelta(days=1)
    return cur


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Prediction:
    model: str
    vintage: str
    ticker: str
    type: str
    target_date: str
    adj_score: float | None
    mu: float | None
    sigma: float | None
    entry_price: float | None
    source_file: str

    def key(self) -> CanonicalKey:
        return (self.model, self.vintage, self.ticker, self.type, self.target_date)


@dataclass
class SettlementCandidate:
    model: str
    vintage: str
    ticker: str
    type: str
    target_date: str

    source_file: str
    settlement_run_date: str
    settled_at: str

    price: float | None
    price_date: str | None
    price_tag: str | None
    declared_timing_flag: str | None

    entry_price: float | None
    mu: float | None
    sigma: float | None
    realized_return: float | None
    benchmark_return: float | None
    realized_alpha: float | None
    direction: str | None
    ci_result: str | None
    z: float | None
    note: str | None

    settlement_convention: str = "UNVALIDATED"
    is_timing_valid: bool = False
    rejection_reason: str = ""

    def key(self) -> CanonicalKey:
        return (self.model, self.vintage, self.ticker, self.type, self.target_date)

    @property
    def is_complete(self) -> bool:
        return (
            self.price is not None
            and self.price_date is not None
            and self.direction is not None
            and self.ci_result is not None
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "vintage": self.vintage,
            "ticker": self.ticker,
            "type": self.type,
            "target_date": self.target_date,
            "source_file": self.source_file,
            "settlement_run_date": self.settlement_run_date,
            "settled_at": self.settled_at,
            "price": self.price,
            "price_date": self.price_date,
            "price_tag": self.price_tag,
            "declared_timing_flag": self.declared_timing_flag,
            "settlement_convention": self.settlement_convention,
            "is_timing_valid": self.is_timing_valid,
            "rejection_reason": self.rejection_reason,
            "entry_price": self.entry_price,
            "mu": self.mu,
            "sigma": self.sigma,
            "realized_return": self.realized_return,
            "benchmark_return": self.benchmark_return,
            "realized_alpha": self.realized_alpha,
            "direction": self.direction,
            "ci_result": self.ci_result,
            "z": self.z,
            "note": self.note,
        }


@dataclass
class ConflictRecord:
    key: CanonicalKey
    reason: str
    candidates: list[SettlementCandidate]

    def to_dict(self) -> dict[str, Any]:
        model, vintage, ticker, type_, target_date = self.key
        return {
            "model": model,
            "vintage": vintage,
            "ticker": ticker,
            "type": type_,
            "target_date": target_date,
            "reason": self.reason,
            "candidate_source_files": [c.source_file for c in self.candidates],
        }


# ---------------------------------------------------------------------------
# Loading + normalization
# ---------------------------------------------------------------------------

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_SOURCE_LEDGER_DATE_RE = re.compile(r"-(\d{4}-\d{2}-\d{2})/")

# The first entry in each tuple is the canonical field name new settlement
# rows should use (see rules.md's Canonical Settlement Ledger contract);
# every other entry is a legacy variant kept only to reconcile packages that
# already exist.
_PRICE_KEYS = ("settle_price", "settlement_price", "current_price")
_PRICE_DATE_KEYS = (
    "settle_price_date",
    "settlement_date",
    "current_price_date",
    "settle_date",
)
# Every schema variant observed in the repo pairs its price key with exactly
# one of these date keys (verified against all settlement rows). Prefer a
# same-convention pair over independently picking the first-present price
# and first-present date, so a row that mixes a live field from one
# convention with a stale leftover field from another can never silently
# pair an unrelated date with a price.
_PRICE_SCHEMA_PAIRS: tuple[tuple[str, str], ...] = (
    ("settle_price", "settle_price_date"),
    ("settle_price", "settle_date"),
    ("settlement_price", "settlement_date"),
    ("current_price", "current_price_date"),
)
_PRICE_TAG_KEYS = ("settlement_price_tag", "current_price_tag")
_TIMING_FLAG_KEYS = ("timing_flag", "settlement_timing_flag")
_SETTLED_AT_KEYS = ("settled_at", "settled_on")


def _looks_like_date(value: Any) -> bool:
    return isinstance(value, str) and bool(_DATE_RE.match(value))


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _first_present(raw: dict[str, Any], keys: tuple[str, ...]) -> Any:
    for k in keys:
        if raw.get(k) is not None:
            return raw[k]
    return None


def _resolve_price_and_date(raw: dict[str, Any]) -> tuple[Any, Any]:
    for price_key, date_key in _PRICE_SCHEMA_PAIRS:
        if raw.get(price_key) is not None and raw.get(date_key) is not None:
            return raw[price_key], raw[date_key]
    # No single schema variant supplied both fields together -- fall back to
    # independent resolution so a row with a genuinely partial schema still
    # yields whatever it has (timing validation will reject it if the two
    # values turn out not to describe the same observation).
    return _first_present(raw, _PRICE_KEYS), _first_present(raw, _PRICE_DATE_KEYS)


def _strip_model_prefix(vintage: Any, model: str | None) -> str | None:
    """Some settlement rows store vintage as "{model}-{date}" instead of
    just "{date}" (observed e.g. vintage="gpt-5-2026-06-11" alongside
    model="gpt-5"). Strip the bug when it is safely detectable.
    """
    if not isinstance(vintage, str):
        return None
    if model and vintage.startswith(model + "-"):
        prefix_len = len(model) + 1
        candidate = vintage[prefix_len:]
        if _looks_like_date(candidate):
            return candidate
    return vintage if _looks_like_date(vintage) else None


def _vintage_from_source_ledger(source_ledger: Any) -> str | None:
    if not isinstance(source_ledger, str):
        return None
    m = _SOURCE_LEDGER_DATE_RE.search(source_ledger)
    return m.group(1) if m else None


def _read_json(path: Path) -> dict[str, Any]:
    with path.open() as fh:
        result: dict[str, Any] = json.load(fh)
    return result


def load_packages(output_dir: Path) -> list[dict[str, Any]]:
    """Load every dated `15_predictions.json` package, tagging each with its
    source folder name."""
    packages = []
    for path in sorted(output_dir.glob("*/15_predictions.json")):
        data = _read_json(path)
        data["_source_file"] = path.parent.name
        packages.append(data)
    return packages


def extract_predictions(packages: Iterable[dict[str, Any]]) -> list[Prediction]:
    out = []
    for pkg in packages:
        for p in pkg.get("predictions", []):
            ticker = p.get("ticker")
            target_date = p.get("target_date")
            run_date = p.get("run_date") or pkg.get("run_date")
            model = p.get("model") or pkg.get("model")
            if not (ticker and target_date and run_date and model):
                continue
            out.append(
                Prediction(
                    model=model,
                    vintage=run_date,
                    ticker=ticker,
                    type=p.get("type") or "EQUITY_ALPHA",
                    target_date=target_date,
                    adj_score=_as_float(p.get("adj_score")),
                    mu=_as_float(p.get("mu")),
                    sigma=_as_float(p.get("sigma")),
                    entry_price=_as_float(p.get("entry_price")),
                    source_file=pkg.get("_source_file", ""),
                )
            )
    return out


def normalize_settlement_candidate(
    raw: dict[str, Any],
    container_run_date: str,
    container_model: str,
    source_file: str,
    lookup_by_no_vintage: dict[tuple[str, str, str, str], list[Prediction]],
) -> SettlementCandidate | None:
    """Normalize one raw settlement row from any observed schema variant.

    Returns None only when the row is too malformed to key at all (missing
    ticker/target_date, or no vintage can be determined by any fallback).
    """
    ticker = raw.get("ticker")
    target_date = raw.get("target_date")
    if not ticker or not target_date:
        return None

    model = raw.get("model") or container_model
    ptype = raw.get("type") or "EQUITY_ALPHA"

    vintage = _strip_model_prefix(raw.get("vintage"), model)
    if not vintage and _looks_like_date(raw.get("vintage_run_date")):
        vintage = raw["vintage_run_date"]
    if not vintage:
        vintage = _vintage_from_source_ledger(raw.get("source_ledger"))
    if not vintage and _looks_like_date(raw.get("entry_date")):
        vintage = raw["entry_date"]
    if not vintage:
        # Prefer a validated match against the real prediction ledger over
        # blindly trusting an ambiguous key (below) -- only fires when
        # exactly one prediction matches on every other key field.
        matches = lookup_by_no_vintage.get((model, ticker, ptype, target_date), [])
        if len(matches) == 1:
            vintage = matches[0].vintage
    if not vintage and _looks_like_date(raw.get("run_date")):
        # Last resort: some rows reuse "run_date" for the *prediction's*
        # vintage. This key is never the settlement computation date --
        # that always comes from the containing package's own top-level
        # run_date -- and is unvalidated against the prediction ledger, so
        # every safer fallback above is tried first.
        vintage = raw["run_date"]

    if not vintage:
        return None

    ci_result = raw.get("ci_result") or raw.get("ci")
    benchmark_return = raw.get("benchmark_return")
    if benchmark_return is None:
        benchmark_return = raw.get("spy_return")
    price, price_date = _resolve_price_and_date(raw)

    return SettlementCandidate(
        model=model,
        vintage=vintage,
        ticker=ticker,
        type=ptype,
        target_date=target_date,
        source_file=source_file,
        settlement_run_date=container_run_date,
        settled_at=str(_first_present(raw, _SETTLED_AT_KEYS) or container_run_date),
        price=_as_float(price),
        price_date=price_date,
        price_tag=_first_present(raw, _PRICE_TAG_KEYS),
        declared_timing_flag=_first_present(raw, _TIMING_FLAG_KEYS),
        entry_price=_as_float(raw.get("entry_price")),
        mu=_as_float(raw.get("mu")),
        sigma=_as_float(raw.get("sigma")),
        realized_return=_as_float(raw.get("realized_return")),
        benchmark_return=_as_float(benchmark_return),
        realized_alpha=_as_float(raw.get("realized_alpha")),
        direction=raw.get("direction"),
        ci_result=ci_result,
        z=_as_float(raw.get("z")),
        note=raw.get("note") or raw.get("settlement_note"),
    )


def extract_settlement_candidates(
    packages: Iterable[dict[str, Any]],
    lookup_by_no_vintage: dict[tuple[str, str, str, str], list[Prediction]],
) -> list[SettlementCandidate]:
    out = []
    for pkg in packages:
        container_run_date = pkg.get("run_date", "")
        container_model = pkg.get("model", "")
        source_file = pkg.get("_source_file", "")
        for raw in pkg.get("settlements", []):
            cand = normalize_settlement_candidate(
                raw,
                container_run_date,
                container_model,
                source_file,
                lookup_by_no_vintage,
            )
            if cand is not None:
                out.append(cand)
    return out


# ---------------------------------------------------------------------------
# Timing validation
# ---------------------------------------------------------------------------


def validate_timing(
    target_date_s: str,
    settlement_run_date_s: str,
    price_date_s: str | None,
    declared_timing_flag: str | None = None,
    settled_at_s: str | None = None,
) -> tuple[str, bool, str]:
    """Returns (settlement_convention, is_valid, rejection_reason).

    Per rules.md Settlement Rules, the settlement price must be the close of
    `target_date` itself, with exactly two exceptions:

    - WEEKEND_TARGET: target_date is not a trading session -> settle at the
      last completed trading close at or before target_date.
    - TARGET_EQ_RUN_DATE: target_date is a trading session but equals the
      settlement's own run date and the run occurs before the close exists ->
      settle at the prior completed session.

    A run after the target session closes may use that same-day close only
    when the row explicitly declares ``TARGET_DATE_CLOSE`` and its
    timezone-aware ``settled_at`` timestamp is at or after 16:00 ET. This
    preserves rejection of unlabeled or pre-close same-day prints while
    allowing the ordinary target-close rule to operate after the close.

    Any other target-date/price-date combination is timing-invalid.
    """
    try:
        target_date = dt.date.fromisoformat(target_date_s)
        settlement_run_date = dt.date.fromisoformat(settlement_run_date_s)
    except (TypeError, ValueError):
        return (
            "MALFORMED",
            False,
            "target_date or settlement_run_date is not a valid date",
        )

    if settlement_run_date < target_date:
        return (
            "PREMATURE",
            False,
            f"settled on {settlement_run_date_s}, before target_date "
            f"{target_date_s} was reached",
        )

    if not price_date_s:
        return ("UNKNOWN", False, "candidate has no price_date")
    try:
        price_date = dt.date.fromisoformat(price_date_s)
    except ValueError:
        return ("MALFORMED", False, f"price_date {price_date_s!r} is not a valid date")

    if not is_trading_day(target_date):
        expected = most_recent_trading_day_at_or_before(target_date)
        if price_date == expected:
            return ("WEEKEND_TARGET", True, "")
        return (
            "WEEKEND_TARGET",
            False,
            f"target_date {target_date_s} is not a trading day: expected the "
            f"last completed close at or before it ({expected.isoformat()}), "
            f"got price_date {price_date_s}",
        )

    if settlement_run_date == target_date:
        expected = prior_trading_day(target_date)
        if price_date == expected:
            return ("TARGET_EQ_RUN_DATE", True, "")
        if price_date == target_date and declared_timing_flag == "TARGET_DATE_CLOSE":
            try:
                settled_at = dt.datetime.fromisoformat(
                    (settled_at_s or "").replace("Z", "+00:00")
                )
                if settled_at.tzinfo is None:
                    raise ValueError("settled_at must include a timezone")
                settled_at_et = settled_at.astimezone(ZoneInfo("America/New_York"))
            except (TypeError, ValueError):
                settled_at_et = None
            if (
                settled_at_et is not None
                and settled_at_et.date() == target_date
                and settled_at_et.time() >= dt.time(16, 0)
            ):
                return ("TARGET_DATE_CLOSE", True, "")
            return (
                "TARGET_DATE_CLOSE",
                False,
                "TARGET_DATE_CLOSE requires a timezone-aware settled_at timestamp "
                "on target_date at or after 16:00 America/New_York",
            )
        return (
            "TARGET_EQ_RUN_DATE",
            False,
            f"target_date {target_date_s} equals the settlement run date: "
            f"expected the prior completed close ({expected.isoformat()}), "
            f"got price_date {price_date_s}; same-day/intraday values require an "
            "explicit TARGET_DATE_CLOSE flag after the session closes",
        )

    # Ordinary case: settlement_run_date > target_date, target_date is a
    # trading day -- the completed target-date close must exist and be used.
    if price_date == target_date:
        return ("ORDINARY", True, "")
    return (
        "ORDINARY",
        False,
        f"ordinary target {target_date_s}: expected the completed "
        f"target-date close, got price_date {price_date_s}",
    )


# ---------------------------------------------------------------------------
# Precedence resolution
# ---------------------------------------------------------------------------


def _prices_agree(a: float | None, b: float | None) -> bool:
    if a is None or b is None:
        return a is None and b is None
    return abs(a - b) <= max(0.01, 0.0005 * max(abs(a), abs(b)))


def build_canonical_ledger(
    candidates: list[SettlementCandidate],
) -> tuple[
    dict[CanonicalKey, SettlementCandidate],
    list[ConflictRecord],
    list[SettlementCandidate],
    list[SettlementCandidate],
    list[SettlementCandidate],
]:
    """Resolve one canonical settlement per key.

    Precedence: among timing-valid, complete candidates for a key, the
    earliest `settlement_run_date` wins (ties broken deterministically by
    source_file name) -- this naturally prefers a candidate settled exactly
    on the due date over any later, lower-priority re-settlement. Candidates
    tied for earliest that materially disagree on price or direction make
    the key an unresolved conflict instead of a silent pick; lower-priority
    post-target observations never override a valid target-date settlement.

    Returns (canonical, conflicts, rejected, audit_only, conflicted). Every
    input candidate lands in exactly one of {canonical (as the chosen value),
    rejected, audit_only, conflicted}:
      - rejected: timing-invalid or incomplete rows.
      - audit_only: valid rows that were NOT selected as canonical, either
        because they agree with the chosen candidate (same-tier duplicate)
        or because they are a later, lower-priority valid re-settlement of
        an already-resolved key. Kept for lineage, never scored.
      - conflicted: valid rows tied for earliest that materially disagree.
        The key itself is excluded from `canonical` (see `conflicts`).
    """
    by_key: dict[CanonicalKey, list[SettlementCandidate]] = defaultdict(list)
    for c in candidates:
        by_key[c.key()].append(c)

    canonical: dict[CanonicalKey, SettlementCandidate] = {}
    conflicts: list[ConflictRecord] = []
    rejected: list[SettlementCandidate] = []
    audit_only: list[SettlementCandidate] = []
    conflicted: list[SettlementCandidate] = []

    for key, rows in by_key.items():
        valid = [c for c in rows if c.is_timing_valid and c.is_complete]
        rejected.extend(c for c in rows if not (c.is_timing_valid and c.is_complete))

        if not valid:
            continue

        ordered = sorted(valid, key=lambda c: (c.settlement_run_date, c.source_file))
        earliest_run_date = ordered[0].settlement_run_date
        earliest_batch = [
            c for c in ordered if c.settlement_run_date == earliest_run_date
        ]
        later_valid = [c for c in ordered if c.settlement_run_date != earliest_run_date]

        if len(earliest_batch) > 1:
            first = earliest_batch[0]
            disagree = any(
                not _prices_agree(first.price, c.price)
                or first.direction != c.direction
                for c in earliest_batch[1:]
            )
            if disagree:
                conflicts.append(
                    ConflictRecord(
                        key=key,
                        reason="same-precedence-tier candidates disagree on "
                        "normalized price or direction",
                        candidates=earliest_batch,
                    )
                )
                conflicted.extend(earliest_batch)
                audit_only.extend(later_valid)
                continue
            audit_only.extend(earliest_batch[1:])

        canonical[key] = earliest_batch[0]
        audit_only.extend(later_valid)

    return canonical, conflicts, rejected, audit_only, conflicted


def compute_due_inventory(
    predictions: list[Prediction],
    canonical: dict[CanonicalKey, SettlementCandidate],
    conflicted_keys: set[CanonicalKey],
    as_of: str,
) -> set[CanonicalKey]:
    """Prediction keys that are due (target_date <= as_of), have no canonical
    settlement, and are not already flagged as an unresolved conflict --
    derived from source prediction keys, never from the source's mutable
    (and never-updated) `status` field. A conflicted key needs manual
    reconciliation, not another automated settlement attempt, so it is
    reported separately (see `conflicts` in the manifest) rather than folded
    into due inventory where it would look like an ordinary open prediction.
    """
    return {
        p.key()
        for p in predictions
        if p.target_date <= as_of
        and p.key() not in canonical
        and p.key() not in conflicted_keys
    }


# ---------------------------------------------------------------------------
# Rolling calibration metrics (computed only from canonical keys)
# ---------------------------------------------------------------------------


def _ranks(values: list[float]) -> list[float]:
    """Average ranks (1-indexed, ties averaged), ascending."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg_rank = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = avg_rank
        i = j + 1
    return ranks


def spearman_rank_ic(pairs: list[tuple[float, float]]) -> float | None:
    n = len(pairs)
    if n < 2:
        return None
    xs = _ranks([p[0] for p in pairs])
    ys = _ranks([p[1] for p in pairs])
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    cov = sum((a - mean_x) * (b - mean_y) for a, b in zip(xs, ys))
    var_x = sum((a - mean_x) ** 2 for a in xs)
    var_y = sum((b - mean_y) ** 2 for b in ys)
    if var_x == 0 or var_y == 0:
        return None
    return cov / math.sqrt(var_x * var_y)


def compute_rolling_metrics(
    canonical: dict[CanonicalKey, SettlementCandidate],
    predictions_index: dict[CanonicalKey, Prediction],
) -> dict[str, Any]:
    """Hit rate, CI coverage, mean z, and per-vintage rank IC, per
    rules.md § Rolling Calibration Metrics -- EQUITY_ALPHA and
    MARKET_FORECAST reported separately, never pooled.
    """

    def _hit_rate(records: list[SettlementCandidate]) -> float | None:
        scored = [c for c in records if c.direction in ("HIT", "MISS")]
        return (
            (sum(1 for c in scored if c.direction == "HIT") / len(scored))
            if scored
            else None
        )

    def _ci_coverage(records: list[SettlementCandidate]) -> float | None:
        scored = [c for c in records if c.ci_result is not None]
        return (
            (sum(1 for c in scored if c.ci_result == "IN_CI") / len(scored))
            if scored
            else None
        )

    def _mean_z(records: list[SettlementCandidate]) -> float | None:
        zs = [c.z for c in records if c.z is not None]
        return (sum(zs) / len(zs)) if zs else None

    def _block(records: list[SettlementCandidate]) -> dict[str, Any]:
        return {
            "n": len(records),
            "status": "OK" if len(records) >= 10 else "INSUFFICIENT_SETTLED_N",
            "hit_rate": _hit_rate(records),
            "ci_coverage": _ci_coverage(records),
            "mean_z": _mean_z(records),
        }

    eq = [c for c in canonical.values() if c.type == "EQUITY_ALPHA"]
    mf = [c for c in canonical.values() if c.type == "MARKET_FORECAST"]

    by_vintage: dict[tuple[str, str], list[SettlementCandidate]] = defaultdict(list)
    for c in eq:
        by_vintage[(c.model, c.vintage)].append(c)

    per_vintage_ic: dict[str, dict[str, Any]] = {}
    weighted_sum = 0.0
    weighted_n = 0
    for (model, vintage), records in sorted(by_vintage.items()):
        pairs = []
        for c in records:
            pred = predictions_index.get(c.key())
            score = pred.adj_score if pred else None
            if score is not None and c.realized_alpha is not None:
                pairs.append((score, c.realized_alpha))
        ic = spearman_rank_ic(pairs)
        per_vintage_ic[f"{model}:{vintage}"] = {"n": len(pairs), "rank_ic": ic}
        if ic is not None and len(pairs) >= 2:
            weighted_sum += ic * len(pairs)
            weighted_n += len(pairs)

    return {
        "equity_alpha": _block(eq),
        "market_forecast": _block(mf),
        "rank_ic_by_vintage": per_vintage_ic,
        "rank_ic_weighted_mean": (weighted_sum / weighted_n) if weighted_n else None,
    }


# ---------------------------------------------------------------------------
# Manifest assembly
# ---------------------------------------------------------------------------


def build_manifest(
    packages: list[dict[str, Any]], as_of: str | None = None
) -> dict[str, Any]:
    if as_of is None:
        run_dates = [p.get("run_date", "") for p in packages if p.get("run_date")]
        as_of = max(run_dates) if run_dates else ""

    predictions = extract_predictions(packages)
    predictions_index: dict[CanonicalKey, Prediction] = {
        p.key(): p for p in predictions
    }
    lookup_by_no_vintage: dict[tuple[str, str, str, str], list[Prediction]] = (
        defaultdict(list)
    )
    for p in predictions:
        lookup_by_no_vintage[(p.model, p.ticker, p.type, p.target_date)].append(p)

    candidates = extract_settlement_candidates(packages, lookup_by_no_vintage)
    for c in candidates:
        convention, valid, reason = validate_timing(
            c.target_date,
            c.settlement_run_date,
            c.price_date,
            c.declared_timing_flag,
            c.settled_at,
        )
        c.settlement_convention = convention
        c.is_timing_valid = valid
        c.rejection_reason = reason

    canonical, conflicts, rejected, audit_only, conflicted = build_canonical_ledger(
        candidates
    )
    conflicted_keys = {c.key for c in conflicts}
    due = compute_due_inventory(predictions, canonical, conflicted_keys, as_of)
    metrics = compute_rolling_metrics(canonical, predictions_index)

    eq_n = sum(1 for c in canonical.values() if c.type == "EQUITY_ALPHA")
    mf_n = sum(1 for c in canonical.values() if c.type == "MARKET_FORECAST")

    return {
        "as_of": as_of,
        "generated_from_packages": [p.get("_source_file", "") for p in packages],
        "summary": {
            "canonical_equity_alpha_settlements": eq_n,
            "canonical_market_forecast_settlements": mf_n,
            "conflicts": len(conflicts),
            "due_inventory": len(due),
            "total_candidate_rows": len(candidates),
            "rejected_rows": len(rejected),
            "audit_only_rows": len(audit_only),
            "conflicted_rows": len(conflicted),
        },
        "canonical_settlements": [c.to_dict() for _, c in sorted(canonical.items())],
        "conflicts": [c.to_dict() for c in conflicts],
        "rejected_candidates": [c.to_dict() for c in rejected],
        "audit_only_candidates": [c.to_dict() for c in audit_only],
        "conflicted_candidates": [c.to_dict() for c in conflicted],
        "due_inventory": [
            {
                "model": k[0],
                "vintage": k[1],
                "ticker": k[2],
                "type": k[3],
                "target_date": k[4],
            }
            for k in sorted(due)
        ],
        "rolling_metrics": metrics,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the canonical settlement ledger from all dated "
        "15_predictions.json packages."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("agents/equity/output"),
        help="Directory containing {model}-{date}/15_predictions.json packages.",
    )
    parser.add_argument(
        "--as-of",
        type=str,
        default=None,
        help="Only consider packages with run_date <= this date (YYYY-MM-DD). "
        "Default: no bound (use every package found).",
    )
    parser.add_argument(
        "--manifest-out",
        type=Path,
        default=None,
        help="Write the full JSON manifest here. Defaults to stdout.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    packages = load_packages(args.output_dir)
    if args.as_of:
        packages = [p for p in packages if p.get("run_date", "") <= args.as_of]

    manifest = build_manifest(packages, as_of=args.as_of)
    text = json.dumps(manifest, indent=2, sort_keys=True)

    if args.manifest_out:
        args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
        args.manifest_out.write_text(text + "\n")
        print(
            f"Wrote canonical settlement manifest to {args.manifest_out}",
            file=sys.stderr,
        )
        print(json.dumps(manifest["summary"], indent=2, sort_keys=True))
    else:
        print(text)


if __name__ == "__main__":
    main()
