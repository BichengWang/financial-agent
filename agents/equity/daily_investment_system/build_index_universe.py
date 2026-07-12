#!/usr/bin/env python3
"""Build the daily investment system equity universe.

The daily research loop should not silently fall back to a hand-sampled list
when local S&P 500 and Nasdaq-100 constituent caches are available. This helper
materializes the deduped S&P 500 union Nasdaq-100 ticker set so downstream
artifacts can cite the exact universe that was scanned.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_SP500 = Path("agents/equity/turtle-trader/universe/sp500.json")
DEFAULT_NASDAQ100 = Path("agents/equity/turtle-trader/universe/nasdaq100.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write the S&P 500 union Nasdaq-100 ticker universe for a daily investment run."
    )
    parser.add_argument("--sp500-cache", type=Path, default=DEFAULT_SP500)
    parser.add_argument("--nasdaq100-cache", type=Path, default=DEFAULT_NASDAQ100)
    parser.add_argument("--output-tickers", type=Path, required=True)
    parser.add_argument("--output-summary", type=Path, required=True)
    parser.add_argument(
        "--min-count",
        type=int,
        default=450,
        help="Fail if the union has fewer names than this. Default: 450.",
    )
    return parser.parse_args()


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_cache(path: Path, expected_index: str) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"{expected_index} cache not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    tickers = payload.get("tickers")
    if not isinstance(tickers, list) or not tickers:
        raise ValueError(f"{expected_index} cache has no tickers: {path}")
    return payload


def dedup(tickers: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for raw in tickers:
        ticker = str(raw).strip().upper()
        if ticker and ticker not in seen:
            seen.add(ticker)
            output.append(ticker)
    return output


def main() -> int:
    args = parse_args()
    sp500 = load_cache(args.sp500_cache, "sp500")
    nasdaq100 = load_cache(args.nasdaq100_cache, "nasdaq100")

    sp500_tickers = dedup(sp500["tickers"])
    nasdaq100_tickers = dedup(nasdaq100["tickers"])
    union = dedup(sp500_tickers + nasdaq100_tickers)
    overlap = sorted(set(sp500_tickers) & set(nasdaq100_tickers))

    if len(union) < args.min_count:
        raise RuntimeError(
            f"Index-union universe too small: {len(union)} names; expected at least {args.min_count}"
        )

    args.output_tickers.parent.mkdir(parents=True, exist_ok=True)
    args.output_summary.parent.mkdir(parents=True, exist_ok=True)
    args.output_tickers.write_text("\n".join(union) + "\n", encoding="utf-8")
    args.output_summary.write_text(
        json.dumps(
            {
                "generated_at": utc_now_iso(),
                "source": "S&P 500 union Nasdaq-100 constituent caches",
                "sp500_cache": str(args.sp500_cache),
                "sp500_fetched_at": sp500.get("fetched_at"),
                "sp500_count": len(sp500_tickers),
                "nasdaq100_cache": str(args.nasdaq100_cache),
                "nasdaq100_fetched_at": nasdaq100.get("fetched_at"),
                "nasdaq100_count": len(nasdaq100_tickers),
                "overlap_count": len(overlap),
                "union_count": len(union),
                "tickers_file": str(args.output_tickers),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(
        f"wrote {len(union)} tickers "
        f"({len(sp500_tickers)} S&P 500, {len(nasdaq100_tickers)} Nasdaq-100, {len(overlap)} overlap)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
