"""Provenance by construction: the ``01_preflight.md`` Source Ledger as code.

Today the model hand-writes ~180 ledger rows per run and then re-types their
values into five other artifacts. Here every fact enters through a method
that stamps provenance, derived facts inherit UNAVAILABLE from any missing
input (``rules.md`` § Source Ledger Contract, hard rule 2), the Price
Sourcing Standard is a function rather than a paragraph, and narrative text
cites ``{{L012}}`` placeholders that the renderer fills -- so a transcription
error has nowhere to happen.
"""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field, replace
from typing import Callable, Sequence
from urllib.parse import urlparse

FRESHNESS_TAGS = (
    "LIVE",
    "DELAYED",
    "OFFICIAL_FILING",
    "HISTORICAL",
    "ILLUSTRATIVE_REF",
    "UNAVAILABLE",
)
# Weakest input wins when facts are combined.
_FRESHNESS_RANK = {tag: rank for rank, tag in enumerate(FRESHNESS_TAGS)}
CLAIM_TYPES = ("OBSERVED", "DERIVED", "INFERRED", "ILLUSTRATIVE", "UNAVAILABLE")
PRICE_AGREEMENT = 0.01  # rules.md § Price Sourcing Standard: two sources within 1%

Value = float | str | None
_REF_RE = re.compile(r"\{\{(L\d+[a-z]?)(?:\|(\w+))?\}\}")
# Decimals (optionally %), integer percentages, count ratios like 27/27,
# thousands-grouped integers, and bare integers of three or more digits.
_LITERAL_NUMBER_RE = re.compile(
    r"(?<![\w.{/])(?:[-+]?\d[\d,]*\.\d+%?|[-+]?\d+%|\d+/\d+|\d{1,3}(?:,\d{3})+"
    r"|\d{3,})(?![\w}/])"
)
_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


class LedgerError(ValueError):
    """A fact without provenance, an unknown row, or a malformed citation."""


@dataclass(frozen=True)
class Quote:
    """One observed price from one source, stamped when it was fetched."""

    source: str
    value: float
    retrieved_at: str
    from_market_data_tool: bool = False


@dataclass(frozen=True)
class LedgerRow:
    row_id: str
    field: str
    entity: str
    value: Value
    unit: str
    observation_date: str | None
    source: str
    freshness_tag: str
    claim_type: str
    inputs: tuple[str, ...] = ()
    used_by: tuple[str, ...] = ()

    @property
    def available(self) -> bool:
        return self.claim_type != "UNAVAILABLE"


def _host(source: str) -> str:
    parsed = urlparse(source)
    return (parsed.netloc or source).lower().removeprefix("www.")


@dataclass
class SourceLedger:
    run_id: str
    rows: dict[str, LedgerRow] = field(default_factory=dict)
    _next: int = 1

    # -- writing ---------------------------------------------------------

    def _add(self, row: LedgerRow) -> str:
        if row.freshness_tag not in _FRESHNESS_RANK:
            raise LedgerError(f"freshness_tag {row.freshness_tag!r} not allowed")
        if row.claim_type not in CLAIM_TYPES:
            raise LedgerError(f"claim_type {row.claim_type!r} not allowed")
        self.rows[row.row_id] = row
        return row.row_id

    def _new_id(self) -> str:
        row_id = f"L{self._next:03d}"
        self._next += 1
        return row_id

    def observe(
        self,
        field_name: str,
        entity: str,
        value: float | str,
        *,
        unit: str,
        observation_date: str,
        source: str,
        freshness_tag: str,
        retrieved_at: str,
    ) -> str:
        """A fact read directly from a cited source during this run."""
        if not source or not retrieved_at:
            raise LedgerError("an OBSERVED row needs a source and retrieved_at")
        try:
            dt.date.fromisoformat(observation_date)
        except ValueError:
            raise LedgerError(f"observation_date {observation_date!r}") from None
        return self._add(
            LedgerRow(
                row_id=self._new_id(),
                field=field_name,
                entity=entity,
                value=value,
                unit=unit,
                observation_date=observation_date,
                source=f"{source} retrieved_at {retrieved_at}",
                freshness_tag=freshness_tag,
                claim_type="OBSERVED",
            )
        )

    def unavailable(self, field_name: str, entity: str, reason: str) -> str:
        return self._add(
            LedgerRow(
                row_id=self._new_id(),
                field=field_name,
                entity=entity,
                value=None,
                unit="",
                observation_date=None,
                source=reason,
                freshness_tag="UNAVAILABLE",
                claim_type="UNAVAILABLE",
            )
        )

    def observe_price(
        self,
        entity: str,
        quotes: Sequence[Quote],
        *,
        observation_date: str,
        freshness_tag: str,
        unit: str = "USD",
    ) -> str:
        """Price Sourcing Standard as code: a market-data tool quote, or two
        independent sources agreeing within 1%; anything else is UNAVAILABLE."""
        tool = [q for q in quotes if q.from_market_data_tool]
        if tool:
            q = tool[0]
            return self.observe(
                "close",
                entity,
                q.value,
                unit=unit,
                observation_date=observation_date,
                source=q.source,
                freshness_tag=freshness_tag,
                retrieved_at=q.retrieved_at,
            )
        by_host: dict[str, Quote] = {}
        for q in quotes:
            by_host.setdefault(_host(q.source), q)
        independent = list(by_host.values())
        if len(independent) < 2:
            return self.unavailable(
                "close",
                entity,
                f"price grounding failed: {len(independent)} independent source(s)",
            )
        values = [q.value for q in independent]
        spread = max(values) / min(values) - 1
        if spread > PRICE_AGREEMENT:
            return self.unavailable(
                "close",
                entity,
                f"price grounding failed: sources disagree {spread:.2%}",
            )
        primary = independent[0]
        cross = "; ".join(f"{q.source}={q.value}" for q in independent[1:])
        return self.observe(
            "close",
            entity,
            primary.value,
            unit=unit,
            observation_date=observation_date,
            source=f"{primary.source} (cross-check {cross}, spread {spread:.2%})",
            freshness_tag=freshness_tag,
            retrieved_at=primary.retrieved_at,
        )

    def derive(
        self,
        field_name: str,
        entity: str,
        *,
        formula: str,
        inputs: Sequence[str],
        compute: Callable[..., float],
        unit: str,
    ) -> str:
        """A computed fact; any UNAVAILABLE input makes the result UNAVAILABLE."""
        rows = [self.row(i) for i in inputs]
        if not rows:
            raise LedgerError("a DERIVED row must cite at least one input row")
        if not all(r.available for r in rows):
            missing = ", ".join(r.row_id for r in rows if not r.available)
            return self._add(
                LedgerRow(
                    row_id=self._new_id(),
                    field=field_name,
                    entity=entity,
                    value=None,
                    unit=unit,
                    observation_date=None,
                    source=f"DERIVED: {formula}; input(s) {missing} UNAVAILABLE",
                    freshness_tag="UNAVAILABLE",
                    claim_type="UNAVAILABLE",
                    inputs=tuple(inputs),
                )
            )
        value = compute(*(r.value for r in rows))
        dates = [r.observation_date for r in rows if r.observation_date]
        weakest = max((r.freshness_tag for r in rows), key=_FRESHNESS_RANK.__getitem__)
        return self._add(
            LedgerRow(
                row_id=self._new_id(),
                field=field_name,
                entity=entity,
                value=value,
                unit=unit,
                observation_date=max(dates) if dates else None,
                source=f"DERIVED: {formula}; inputs {', '.join(inputs)}",
                freshness_tag=weakest,
                claim_type="DERIVED",
                inputs=tuple(inputs),
            )
        )

    # -- reading ---------------------------------------------------------

    def row(self, row_id: str) -> LedgerRow:
        try:
            return self.rows[row_id]
        except KeyError:
            raise LedgerError(f"unknown ledger row {row_id}") from None

    def cite(self, row_id: str, artifact: str) -> Value:
        """Read a value *and* record which artifact used it (``used_by``)."""
        row = self.row(row_id)
        if artifact not in row.used_by:
            self.rows[row_id] = replace(row, used_by=row.used_by + (artifact,))
        return row.value

    def render(self, template: str, artifact: str) -> str:
        """Fill ``{{L012}}`` / ``{{L012|pct}}`` citations from the ledger."""

        def fill(match: re.Match[str]) -> str:
            row_id, fmt = match.group(1), match.group(2)
            value = self.cite(row_id, artifact)
            if value is None:
                return f"UNAVAILABLE ({row_id})"
            if fmt == "pct" and isinstance(value, float):
                return f"{value:+.2%} ({row_id})"
            if isinstance(value, float):
                return f"{value:,.2f} ({row_id})"
            return f"{value} ({row_id})"

        return _REF_RE.sub(fill, template)

    def to_markdown(self) -> str:
        """The Source Ledger table in the ``runbook.md § 01`` schema."""
        header = (
            "| artifact | field | ticker/entity | value | unit | observation_date "
            "| source | freshness_tag | claim_type | used_by |\n"
            "|---|---|---|---|---|---|---|---|---|---|"
        )
        lines = [header]
        for row in self.rows.values():
            value = "UNAVAILABLE" if row.value is None else row.value
            cells = [
                row.row_id,
                row.field,
                row.entity,
                str(value),
                row.unit,
                row.observation_date or "UNAVAILABLE",
                row.source.replace("|", "\\|"),
                row.freshness_tag,
                row.claim_type,
                ", ".join(row.used_by),
            ]
            lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines)


def lint_literal_numbers(template: str, allow: Sequence[str] = ()) -> list[str]:
    """Numbers typed into model-authored text instead of cited via ``{{L...}}``.

    ISO dates and one- or two-digit integers ("3 of 4 families") pass;
    decimals, percentages, count ratios (``27/27``), and integers of three or
    more digits must come from the ledger unless listed in ``allow``.
    """
    allowed = set(allow)
    findings: list[str] = []
    for line_no, line in enumerate(template.splitlines(), start=1):
        scrubbed = _DATE_RE.sub("", _REF_RE.sub("", line))
        for match in _LITERAL_NUMBER_RE.finditer(scrubbed):
            if match.group(0) not in allowed:
                findings.append(f"line {line_no}: literal number {match.group(0)!r}")
    return findings
