#!/usr/bin/env python3
"""SHADOW-only Sentiment/Positioning family (Sent_Z) diagnostics from Nasdaq.

Implements Phase 1 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`:
fetch the same free `api.nasdaq.com` endpoints already proven in this repo's
price/earnings-date fetch chains for a shortlist, compute a handful of
sentiment signals with source lineage, and cross-sectionally z-score them.
Output is diagnostic only -- every record is tagged `"gating_status": "SHADOW"`
and this script does not modify `rules.md`'s Evidence Thresholds or the
Sent_Z family-availability gate. A name only counts toward the required
"3 of 4 factor families non-negative" test once a future run explicitly
promotes this family per the plan's governance (HUMAN_REVIEW + one shadow
run logged in `13_evolution_log.md`).

Signals (per rules.md's Sentiment family menu, as many as are derivable from
free, unauthenticated Nasdaq endpoints):
  - analyst_tilt: (buy - sell) / total analyst count from the consensus
    rating breakdown -- a normalized positioning score.
  - target_price_momentum: consensus price-target change from ~3 months ago
    to the latest reading, from the historical consensus series.
  - short_interest_change: percent change between the two most recent
    twice-monthly short-interest settlement readings.

A signal is UNAVAILABLE for a name when Nasdaq has no data for it or a fetch
fails -- never guessed, never interpolated.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
from pathlib import Path
from typing import Any

import factor_scoring

NASDAQ_TARGETPRICE_URL = "https://api.nasdaq.com/api/analyst/{symbol}/targetprice"
NASDAQ_SHORT_INTEREST_URL = (
    "https://api.nasdaq.com/api/quote/{symbol}/short-interest?assetclass=stocks"
)

SIGNAL_NAMES = ("analyst_tilt", "target_price_momentum", "short_interest_change")
_LOWER_IS_BETTER = {"short_interest_change"}

SENT_Z_KEY = "sent_z"
FAMILY_LABEL = "Sent_Z"
PLAN_PATH = "agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md"


def _nasdaq_headers() -> dict[str, str]:
    return {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
        "Origin": "https://www.nasdaq.com",
        "Referer": "https://www.nasdaq.com/",
        "Accept": "application/json",
    }


def fetch_targetprice(symbol: str) -> dict[str, Any]:
    url = NASDAQ_TARGETPRICE_URL.format(symbol=symbol.lower())
    result: dict[str, Any] = factor_scoring.fetch_json(url, _nasdaq_headers())
    return result


def fetch_short_interest(symbol: str) -> dict[str, Any]:
    url = NASDAQ_SHORT_INTEREST_URL.format(symbol=symbol.lower())
    result: dict[str, Any] = factor_scoring.fetch_json(url, _nasdaq_headers())
    return result


def _clean_number(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", "").replace("$", "")
    if not text or text in ("N/A", "NA", "--"):
        return None
    try:
        return float(text)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------


def compute_analyst_signals(targetprice_payload: dict[str, Any]) -> dict[str, Any]:
    values: dict[str, float | None] = {}
    lineage: dict[str, Any] = {}

    data = targetprice_payload.get("data") or {}
    consensus = data.get("consensusOverview") or {}
    buy = _clean_number(consensus.get("buy"))
    hold = _clean_number(consensus.get("hold"))
    sell = _clean_number(consensus.get("sell"))
    if (
        buy is not None
        and hold is not None
        and sell is not None
        and (buy + hold + sell) > 0
    ):
        total = buy + hold + sell
        values["analyst_tilt"] = (buy - sell) / total
        lineage["analyst_tilt"] = {
            "buy": buy,
            "hold": hold,
            "sell": sell,
            "total": total,
        }

    history = data.get("historicalConsensus") or []
    points = [
        (row["x"], row["y"])
        for row in history
        if isinstance(row, dict)
        and row.get("x") is not None
        and row.get("y") is not None
    ]
    points.sort(key=lambda p: p[0])
    if len(points) >= 2:
        latest_ts, latest_target = points[-1]
        # ~3 months back: the closest point at or before latest_ts - 75 days.
        cutoff = latest_ts - 75 * 86400
        prior_candidates = [p for p in points if p[0] <= cutoff]
        if prior_candidates and latest_target and prior_candidates[-1][1]:
            prior_ts, prior_target = prior_candidates[-1]
            values["target_price_momentum"] = latest_target / prior_target - 1
            lineage["target_price_momentum"] = {
                "latest": {"ts": latest_ts, "target": latest_target},
                "prior": {"ts": prior_ts, "target": prior_target},
            }

    return {"values": values, "lineage": lineage}


def compute_short_interest_signal(
    short_interest_payload: dict[str, Any],
) -> dict[str, Any]:
    values: dict[str, float | None] = {}
    lineage: dict[str, Any] = {}

    rows = (short_interest_payload.get("data") or {}).get("shortInterestTable", {}).get(
        "rows"
    ) or []
    parsed = []
    for row in rows:
        interest = _clean_number(row.get("interest"))
        settlement_date = row.get("settlementDate")
        if interest is not None and settlement_date:
            try:
                d = dt.datetime.strptime(settlement_date, "%m/%d/%Y").date()
            except ValueError:
                continue
            parsed.append((d, interest))
    parsed.sort(key=lambda p: p[0], reverse=True)
    if len(parsed) >= 2 and parsed[1][1]:
        latest, prior = parsed[0], parsed[1]
        values["short_interest_change"] = latest[1] / prior[1] - 1
        lineage["short_interest_change"] = {
            "latest": {"date": latest[0].isoformat(), "interest": latest[1]},
            "prior": {"date": prior[0].isoformat(), "interest": prior[1]},
        }

    return {"values": values, "lineage": lineage}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="SHADOW-only Sentiment family (Sent_Z) diagnostics from "
        "free Nasdaq analyst/short-interest endpoints. Phase 1 of the "
        "Fundamental+Sentiment data-source plan; not wired into scoring."
    )
    parser.add_argument("--tickers", nargs="*", default=[])
    parser.add_argument("--tickers-file", type=Path)
    parser.add_argument(
        "--output", type=Path, help="Output JSON path. Defaults to stdout."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tickers = factor_scoring.read_tickers(args.tickers, args.tickers_file)
    if not tickers:
        print("No tickers given (use --tickers or --tickers-file).", file=sys.stderr)
        sys.exit(1)

    per_ticker_values: dict[str, dict[str, float | None]] = {}
    per_ticker_lineage: dict[str, Any] = {}
    fetch_failures: dict[str, str] = {}

    for ticker in tickers:
        values: dict[str, float | None] = {}
        lineage: dict[str, Any] = {}
        failures = []

        try:
            tp_payload = fetch_targetprice(ticker)
            analyst = compute_analyst_signals(tp_payload)
            values.update(analyst["values"])
            lineage.update(analyst["lineage"])
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            failures.append(f"targetprice fetch failed: {exc}")

        try:
            si_payload = fetch_short_interest(ticker)
            short_interest = compute_short_interest_signal(si_payload)
            values.update(short_interest["values"])
            lineage.update(short_interest["lineage"])
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            failures.append(f"short-interest fetch failed: {exc}")

        if failures and not values:
            fetch_failures[ticker] = "; ".join(failures)
            continue

        per_ticker_values[ticker] = {s: values.get(s) for s in SIGNAL_NAMES}
        per_ticker_lineage[ticker] = lineage
        if failures:
            per_ticker_lineage[ticker]["partial_fetch_failures"] = failures
        print(
            f"  {ticker}: {sum(1 for v in values.values() if v is not None)} "
            f"of {len(SIGNAL_NAMES)} signals sourced",
            file=sys.stderr,
        )

    output = factor_scoring.build_shadow_output(
        tickers,
        per_ticker_values,
        per_ticker_lineage,
        fetch_failures,
        SIGNAL_NAMES,
        _LOWER_IS_BETTER,
        SENT_Z_KEY,
        FAMILY_LABEL,
        PLAN_PATH,
    )

    text = json.dumps(output, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n")
        print(f"Wrote sentiment diagnostics to {args.output}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
