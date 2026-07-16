#!/usr/bin/env python3
"""SHADOW-only Fundamental family (Fund_Z) diagnostics from SEC EDGAR XBRL.

Implements Phase 1 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`:
fetch `companyfacts` for a shortlist, compute a handful of fundamental
signals with full source-filing lineage, and cross-sectionally z-score them.
Output is diagnostic only -- every record is tagged `"gating_status": "SHADOW"`
and this script does not modify `rules.md`'s Evidence Thresholds or the
Fund_Z family-availability gate. A name only counts toward the required
"3 of 4 factor families non-negative" test once a future run explicitly
promotes this family per the plan's governance (HUMAN_REVIEW + one shadow
run logged in `13_evolution_log.md`).

Signals (per rules.md's Fundamental family menu, as many as are derivable
from free, unauthenticated companyfacts data):
  - revenue_yoy_growth, revenue_accel: quarterly revenue vs 4 quarters ago,
    and whether that growth rate is itself accelerating.
  - gross_margin_trend, operating_margin_trend: margin now vs 4 quarters ago.
  - roe: trailing-twelve-month net income / average stockholders' equity.
  - leverage: total liabilities / stockholders' equity (a leverage proxy;
    used in place of a debt/equity tag because reporting of "debt" alone is
    not consistently tagged across filers, while Liabilities and
    StockholdersEquity are close to universal).
  - accrual_ratio: (net income - operating cash flow) / total assets, lower
    is higher quality (per rules.md's "accrual quality" signal).

FCF yield vs EV is intentionally NOT computed here: it requires a live
market price (shares outstanding x price) that this script does not fetch,
per the Non-Fabrication Contract. Pass `--prices-json` (ticker -> price) to
compute it; otherwise it is reported `UNAVAILABLE` per name. Even when
computed, it is an *approximation*: TTM operating cash flow stands in for
free cash flow (capex is not uniformly tagged across filers) and EV does
not net out cash -- both disclosed in that signal's lineage.

A signal is UNAVAILABLE for a name when SEC has no matching tag or fewer
than 6 quarters of history -- never guessed, never interpolated.
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

SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
SEC_CONTACT_USER_AGENT = "financial-agent-daily-research contact@example.com"

_REVENUE_TAGS = (
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "Revenues",
    "SalesRevenueNet",
)
_GROSS_PROFIT_TAGS = ("GrossProfit",)
_OPERATING_INCOME_TAGS = ("OperatingIncomeLoss",)
_NET_INCOME_TAGS = ("NetIncomeLoss", "ProfitLoss")
_OCF_TAGS = (
    "NetCashProvidedByUsedInOperatingActivities",
    "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
)
_ASSETS_TAGS = ("Assets",)
_LIABILITIES_TAGS = ("Liabilities",)
_EQUITY_TAGS = (
    "StockholdersEquity",
    "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
)
_SHARES_TAGS = ("CommonStockSharesOutstanding",)

SIGNAL_NAMES = (
    "revenue_yoy_growth",
    "revenue_accel",
    "gross_margin_trend",
    "operating_margin_trend",
    "roe",
    "leverage",
    "accrual_ratio",
    "fcf_yield",
)
# Signals where a *lower* value is the positive driver -- everything else is
# "higher is better", per rules.md's Family Aggregation polarity rule.
_LOWER_IS_BETTER = {"leverage", "accrual_ratio"}

FUND_Z_KEY = "fund_z"
FAMILY_LABEL = "Fund_Z"
PLAN_PATH = "agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md"


def _sec_headers() -> dict[str, str]:
    # SEC EDGAR's fair-access policy requires a descriptive contact User-Agent:
    # https://www.sec.gov/os/webmaster-faq#developers
    return {"User-Agent": SEC_CONTACT_USER_AGENT}


def fetch_ticker_cik_map() -> dict[str, int]:
    data = factor_scoring.fetch_json(SEC_TICKERS_URL, _sec_headers(), timeout=30)
    return {v["ticker"]: int(v["cik_str"]) for v in data.values()}


def fetch_companyfacts(cik: int) -> dict[str, Any]:
    url = SEC_FACTS_URL.format(cik=cik)
    result: dict[str, Any] = factor_scoring.fetch_json(url, _sec_headers(), timeout=30)
    return result


# ---------------------------------------------------------------------------
# XBRL extraction
# ---------------------------------------------------------------------------


def _quarterly_series(
    facts: dict[str, Any], tags: tuple[str, ...]
) -> tuple[str, list[dict[str, Any]]]:
    """Duration (flow) rows covering ~one fiscal quarter, newest first.
    Returns (tag_used, rows); tag_used is "" when no tag had any quarterly
    (80-100 day duration) row -- distinguishing "no data" from "only
    year-to-date data available", both of which leave the series empty.
    """
    usgaap = facts.get("facts", {}).get("us-gaap", {})
    for tag in tags:
        entry = usgaap.get(tag)
        if not entry:
            continue
        rows = entry.get("units", {}).get("USD", [])
        quarterly = []
        for r in rows:
            start, end = r.get("start"), r.get("end")
            if not start or not end:
                continue
            days = (dt.date.fromisoformat(end) - dt.date.fromisoformat(start)).days
            if 80 <= days <= 100:
                quarterly.append(r)
        if quarterly:
            quarterly.sort(key=lambda r: r["end"], reverse=True)
            return tag, quarterly
    return "", []


def _instant_series(
    facts: dict[str, Any], tags: tuple[str, ...]
) -> tuple[str, list[dict[str, Any]]]:
    """Point-in-time (balance sheet) rows, newest first."""
    usgaap = facts.get("facts", {}).get("us-gaap", {})
    for tag in tags:
        entry = usgaap.get(tag)
        if not entry:
            continue
        rows = [
            r
            for r in entry.get("units", {}).get("USD", [])
            if r.get("end") and "start" not in r
        ]
        if rows:
            rows.sort(key=lambda r: r["end"], reverse=True)
            return tag, rows
    return "", []


def _align_by_end(series: list[dict[str, Any]]) -> dict[str, float]:
    return {r["end"]: r["val"] for r in series}


def _margin_trend(
    numerator_q: list[dict[str, Any]], revenue_q: list[dict[str, Any]]
) -> float | None:
    """Latest-quarter margin (numerator/revenue) minus the margin 4 quarters
    ago, over whichever quarter-end dates both series share."""
    if not numerator_q or not revenue_q:
        return None
    num_by_end = _align_by_end(numerator_q)
    rev_by_end = _align_by_end(revenue_q)
    ends = sorted(set(num_by_end) & set(rev_by_end), reverse=True)
    if len(ends) < 5:
        return None
    latest_end, year_ago_end = ends[0], ends[4]
    if not rev_by_end[latest_end] or not rev_by_end[year_ago_end]:
        return None
    latest_margin = num_by_end[latest_end] / rev_by_end[latest_end]
    year_ago_margin = num_by_end[year_ago_end] / rev_by_end[year_ago_end]
    return latest_margin - year_ago_margin


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------


def compute_fundamental_signals(
    facts: dict[str, Any], price: float | None = None
) -> dict[str, Any]:
    """Returns {"values": {signal: float|None}, "lineage": {...}}. A signal
    absent from "values" (or None) is UNAVAILABLE -- never guessed.
    """
    rev_tag, revenue_q = _quarterly_series(facts, _REVENUE_TAGS)
    gp_tag, gp_q = _quarterly_series(facts, _GROSS_PROFIT_TAGS)
    oi_tag, oi_q = _quarterly_series(facts, _OPERATING_INCOME_TAGS)
    ni_tag, ni_q = _quarterly_series(facts, _NET_INCOME_TAGS)
    ocf_tag, ocf_q = _quarterly_series(facts, _OCF_TAGS)
    assets_tag, assets_i = _instant_series(facts, _ASSETS_TAGS)
    _, liab_i = _instant_series(facts, _LIABILITIES_TAGS)
    equity_tag, equity_i = _instant_series(facts, _EQUITY_TAGS)

    values: dict[str, float | None] = {}
    lineage: dict[str, Any] = {}

    # -- Revenue YoY growth + acceleration (needs 6 quarters: 0,1 = latest two,
    # 4,5 = the same two quarters a year earlier) --
    if len(revenue_q) >= 6 and revenue_q[4]["val"] and revenue_q[5]["val"]:
        yoy_growth = revenue_q[0]["val"] / revenue_q[4]["val"] - 1
        prior_yoy_growth = revenue_q[1]["val"] / revenue_q[5]["val"] - 1
        values["revenue_yoy_growth"] = yoy_growth
        values["revenue_accel"] = yoy_growth - prior_yoy_growth
        lineage["revenue_yoy_growth"] = {
            "tag": rev_tag,
            "latest": revenue_q[0],
            "year_ago": revenue_q[4],
        }
        lineage["revenue_accel"] = {
            "tag": rev_tag,
            "derived_from": "revenue_yoy_growth",
        }

    gross_margin_trend = _margin_trend(gp_q, revenue_q)
    if gross_margin_trend is not None:
        values["gross_margin_trend"] = gross_margin_trend
        lineage["gross_margin_trend"] = {"tag": gp_tag, "revenue_tag": rev_tag}

    operating_margin_trend = _margin_trend(oi_q, revenue_q)
    if operating_margin_trend is not None:
        values["operating_margin_trend"] = operating_margin_trend
        lineage["operating_margin_trend"] = {"tag": oi_tag, "revenue_tag": rev_tag}

    # -- ROE: trailing-twelve-month net income / average stockholders' equity --
    if len(ni_q) >= 4 and len(equity_i) >= 5:
        ttm_ni = sum(r["val"] for r in ni_q[:4])
        avg_equity = (equity_i[0]["val"] + equity_i[4]["val"]) / 2
        if avg_equity:
            values["roe"] = ttm_ni / avg_equity
            lineage["roe"] = {
                "ni_tag": ni_tag,
                "equity_tag": equity_tag,
                "ttm_quarters": [r["end"] for r in ni_q[:4]],
            }

    # -- Leverage: total liabilities / stockholders' equity --
    if liab_i and equity_i and equity_i[0]["val"]:
        values["leverage"] = liab_i[0]["val"] / equity_i[0]["val"]
        lineage["leverage"] = {"as_of": liab_i[0]["end"]}

    # -- Accrual ratio: (net income - operating cash flow) / total assets --
    if len(ni_q) >= 4 and len(ocf_q) >= 4 and assets_i and assets_i[0]["val"]:
        ttm_ni = sum(r["val"] for r in ni_q[:4])
        ttm_ocf = sum(r["val"] for r in ocf_q[:4])
        values["accrual_ratio"] = (ttm_ni - ttm_ocf) / assets_i[0]["val"]
        lineage["accrual_ratio"] = {
            "ni_tag": ni_tag,
            "ocf_tag": ocf_tag,
            "assets_tag": assets_tag,
        }

    # -- FCF yield vs EV: requires a live price, not fetched by this script --
    if price is not None and len(ocf_q) >= 4 and liab_i:
        ttm_ocf = sum(r["val"] for r in ocf_q[:4])
        shares_tag, shares = _instant_series(facts, _SHARES_TAGS)
        dei_shares = (
            facts.get("facts", {})
            .get("dei", {})
            .get("EntityCommonStockSharesOutstanding", {})
        )
        dei_rows = dei_shares.get("units", {}).get("shares", [])
        share_count = None
        share_source = ""
        if dei_rows:
            share_count = sorted(dei_rows, key=lambda r: r["end"])[-1]["val"]
            share_source = "dei:EntityCommonStockSharesOutstanding"
        elif shares:
            share_count = shares[0]["val"]
            share_source = f"us-gaap:{shares_tag}"
        if share_count:
            market_cap = price * share_count
            ev = market_cap + liab_i[0]["val"]
            if ev:
                values["fcf_yield"] = ttm_ocf / ev
                lineage["fcf_yield"] = {
                    "approximation": "TTM operating cash flow used in place of "
                    "FCF (capex is not uniformly tagged); EV = price*shares + "
                    "total liabilities (cash not separately netted)",
                    "price": price,
                    "share_count": share_count,
                    "share_count_source": share_source,
                }

    return {"values": values, "lineage": lineage}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="SHADOW-only Fundamental family (Fund_Z) diagnostics "
        "from free SEC EDGAR XBRL companyfacts. Phase 1 of the "
        "Fundamental+Sentiment data-source plan; not wired into scoring."
    )
    parser.add_argument("--tickers", nargs="*", default=[])
    parser.add_argument("--tickers-file", type=Path)
    parser.add_argument(
        "--prices-json",
        type=Path,
        help="Optional {ticker: price} JSON for the FCF-yield-vs-EV signal.",
    )
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

    prices: dict[str, float] = {}
    if args.prices_json:
        prices = json.loads(args.prices_json.read_text())

    per_ticker_values: dict[str, dict[str, float | None]] = {}
    per_ticker_lineage: dict[str, Any] = {}
    fetch_failures: dict[str, str] = {}

    print("Fetching SEC ticker->CIK map...", file=sys.stderr)
    try:
        cik_map = fetch_ticker_cik_map()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        # A single shared fetch feeds every ticker below; without this guard
        # its failure would crash the whole run instead of reporting every
        # ticker as UNAVAILABLE with a clear reason.
        reason = f"SEC company_tickers.json fetch failed: {exc}"
        print(reason, file=sys.stderr)
        output = factor_scoring.build_shadow_output(
            tickers,
            {},
            {},
            {t: reason for t in tickers},
            SIGNAL_NAMES,
            _LOWER_IS_BETTER,
            FUND_Z_KEY,
            FAMILY_LABEL,
            PLAN_PATH,
        )
        text = json.dumps(output, indent=2, sort_keys=True)
        if args.output:
            args.output.write_text(text + "\n")
        else:
            print(text)
        sys.exit(1)

    for ticker in tickers:
        cik = cik_map.get(ticker)
        if cik is None:
            fetch_failures[ticker] = "no CIK mapping in SEC company_tickers.json"
            continue
        try:
            facts = fetch_companyfacts(cik)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            fetch_failures[ticker] = f"companyfacts fetch failed: {exc}"
            continue
        result = compute_fundamental_signals(facts, price=prices.get(ticker))
        per_ticker_values[ticker] = {s: result["values"].get(s) for s in SIGNAL_NAMES}
        per_ticker_lineage[ticker] = result["lineage"]
        print(
            f"  {ticker}: {sum(1 for v in result['values'].values() if v is not None)} "
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
        FUND_Z_KEY,
        FAMILY_LABEL,
        PLAN_PATH,
    )

    text = json.dumps(output, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n")
        print(f"Wrote fundamental diagnostics to {args.output}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
