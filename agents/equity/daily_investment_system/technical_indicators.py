#!/usr/bin/env python3
"""Compute deterministic technical indicators for the daily investment system.

The script uses the Python standard library for compute and I/O. If the local
Python install has no working system CA bundle, an installed certifi package is
used opportunistically for HTTPS certificate verification.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


YAHOO_CHART_URL = "https://query2.finance.yahoo.com/v8/finance/chart/{symbol}"
SSL_CONTEXT: ssl.SSLContext | None = None


def https_context() -> ssl.SSLContext | None:
    global SSL_CONTEXT
    if SSL_CONTEXT is not None:
        return SSL_CONTEXT
    try:
        import certifi  # type: ignore

        SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
    except Exception:
        SSL_CONTEXT = ssl.create_default_context()
    return SSL_CONTEXT


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute TD-9, RSI, MACD, MA, momentum, and relative-strength indicators."
    )
    parser.add_argument(
        "--tickers",
        nargs="*",
        default=[],
        help="Tickers to compute. Accepts space-separated values and comma-separated chunks.",
    )
    parser.add_argument(
        "--tickers-file",
        type=Path,
        help="Optional newline/comma/space separated ticker file.",
    )
    parser.add_argument(
        "--benchmark",
        default="SPY",
        help="Benchmark ticker for relative strength calculations. Default: SPY.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSON path. Defaults to stdout.",
    )
    parser.add_argument(
        "--history-dir",
        type=Path,
        help="Optional directory of ticker CSV files. Files named TICKER.csv are used before web fetch.",
    )
    parser.add_argument(
        "--range",
        default="5y",
        help="Yahoo Finance chart range when fetching. Default: 5y, so monthly RSI/MACD have enough bars.",
    )
    parser.add_argument(
        "--interval",
        default="1d",
        help="Yahoo Finance chart interval when fetching. Default: 1d.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON.",
    )
    return parser.parse_args()


def normalize_tickers(chunks: list[str]) -> list[str]:
    seen: set[str] = set()
    tickers: list[str] = []
    for chunk in chunks:
        for raw in chunk.replace(",", " ").split():
            ticker = raw.strip().upper()
            if ticker and ticker not in seen:
                seen.add(ticker)
                tickers.append(ticker)
    return tickers


def load_tickers(args: argparse.Namespace) -> list[str]:
    chunks = list(args.tickers)
    if args.tickers_file:
        chunks.append(args.tickers_file.read_text(encoding="utf-8"))
    tickers = normalize_tickers(chunks)
    benchmark = args.benchmark.upper()
    if benchmark not in tickers:
        tickers.insert(0, benchmark)
    return tickers


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def to_date(timestamp: int) -> str:
    return dt.datetime.fromtimestamp(timestamp, dt.timezone.utc).date().isoformat()


def yahoo_symbol(symbol: str) -> str:
    return symbol.replace(".", "-")


def fetch_yahoo_history(symbol: str, chart_range: str, interval: str) -> tuple[list[dict[str, Any]], str]:
    params = urllib.parse.urlencode(
        {
            "range": chart_range,
            "interval": interval,
            "events": "history",
            "includeAdjustedClose": "true",
        }
    )
    url = f"{YAHOO_CHART_URL.format(symbol=urllib.parse.quote(yahoo_symbol(symbol)))}?{params}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "daily-investment-system/technical-indicators"},
    )
    with urllib.request.urlopen(request, timeout=20, context=https_context()) as response:
        payload = json.loads(response.read().decode("utf-8"))

    chart = payload.get("chart", {})
    if chart.get("error"):
        raise RuntimeError(f"Yahoo chart error for {symbol}: {chart['error']}")
    results = chart.get("result") or []
    if not results:
        raise RuntimeError(f"Yahoo chart returned no result for {symbol}")

    result = results[0]
    timestamps = result.get("timestamp") or []
    indicators = result.get("indicators", {})
    quote = (indicators.get("quote") or [{}])[0]
    adjclose = (indicators.get("adjclose") or [{}])[0].get("adjclose") or []
    closes = quote.get("close") or []
    volumes = quote.get("volume") or []

    bars: list[dict[str, Any]] = []
    for index, timestamp in enumerate(timestamps):
        close = closes[index] if index < len(closes) else None
        if close is None and index < len(adjclose):
            close = adjclose[index]
        if close is None:
            continue
        volume = volumes[index] if index < len(volumes) else None
        bars.append(
            {
                "date": to_date(int(timestamp)),
                "close": float(close),
                "volume": int(volume) if volume is not None else None,
            }
        )
    return bars, url


def load_csv_history(symbol: str, history_dir: Path) -> tuple[list[dict[str, Any]], str] | None:
    path = history_dir / f"{symbol.upper()}.csv"
    if not path.exists():
        return None
    with path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        bars: list[dict[str, Any]] = []
        for row in reader:
            date_value = row.get("date") or row.get("Date")
            close_value = (
                row.get("close")
                or row.get("Close")
                or row.get("adj_close")
                or row.get("Adj Close")
                or row.get("AdjClose")
            )
            if not date_value or close_value in (None, ""):
                continue
            volume_value = row.get("volume") or row.get("Volume")
            bars.append(
                {
                    "date": date_value,
                    "close": float(close_value),
                    "volume": int(float(volume_value)) if volume_value not in (None, "") else None,
                }
            )
    bars.sort(key=lambda item: item["date"])
    return bars, str(path)


def load_history(
    symbol: str,
    history_dir: Path | None,
    chart_range: str,
    interval: str,
) -> tuple[list[dict[str, Any]], str, str]:
    if history_dir:
        csv_result = load_csv_history(symbol, history_dir)
        if csv_result:
            bars, source = csv_result
            return bars, source, "CSV"
    bars, source = fetch_yahoo_history(symbol, chart_range, interval)
    return bars, source, "YAHOO_CHART"


def closes(bars: list[dict[str, Any]]) -> list[float]:
    return [float(bar["close"]) for bar in bars if bar.get("close") is not None]


def volumes(bars: list[dict[str, Any]]) -> list[int | None]:
    return [bar.get("volume") for bar in bars]


def round_or_none(value: float | None, digits: int = 2) -> float | None:
    if value is None or math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def simple_ma(values: list[float], period: int) -> float | None:
    if len(values) < period:
        return None
    return sum(values[-period:]) / period


def momentum_pct(values: list[float], periods: int) -> float | None:
    if len(values) <= periods:
        return None
    base = values[-periods - 1]
    if base == 0:
        return None
    return (values[-1] / base - 1.0) * 100.0


def ema_series(values: list[float | None], period: int) -> list[float | None]:
    alpha = 2.0 / (period + 1.0)
    ema: float | None = None
    output: list[float | None] = []
    for value in values:
        if value is None:
            output.append(None)
            continue
        ema = value if ema is None else alpha * value + (1.0 - alpha) * ema
        output.append(ema)
    return output


def macd(values: list[float], fast: int = 12, slow: int = 26, signal: int = 9) -> dict[str, Any]:
    if len(values) < slow + signal:
        return {
            "macd_line": None,
            "macd_signal": None,
            "macd_histogram": None,
            "macd_state": "UNAVAILABLE",
        }
    fast_ema = ema_series([float(value) for value in values], fast)
    slow_ema = ema_series([float(value) for value in values], slow)
    line = [
        None if fast_value is None or slow_value is None else fast_value - slow_value
        for fast_value, slow_value in zip(fast_ema, slow_ema)
    ]
    signal_line = ema_series(line, signal)
    histogram = [
        None if line_value is None or signal_value is None else line_value - signal_value
        for line_value, signal_value in zip(line, signal_line)
    ]
    last_line = line[-1]
    last_signal = signal_line[-1]
    last_hist = histogram[-1]
    prev_hist = next((value for value in reversed(histogram[:-1]) if value is not None), None)
    state = "UNAVAILABLE"
    if last_hist is not None:
        if prev_hist is not None and prev_hist <= 0 < last_hist:
            state = "BULLISH_CROSS"
        elif prev_hist is not None and prev_hist >= 0 > last_hist:
            state = "BEARISH_CROSS"
        elif last_hist > 0:
            state = "ABOVE_SIGNAL"
        elif last_hist < 0:
            state = "BELOW_SIGNAL"
        else:
            state = "ON_SIGNAL"
    return {
        "macd_line": round_or_none(last_line, 4),
        "macd_signal": round_or_none(last_signal, 4),
        "macd_histogram": round_or_none(last_hist, 4),
        "macd_state": state,
    }


def rsi_wilder(values: list[float], period: int = 14) -> float | None:
    if len(values) < period + 1:
        return None
    deltas = [values[index] - values[index - 1] for index in range(1, len(values))]
    gains = [max(delta, 0.0) for delta in deltas[:period]]
    losses = [max(-delta, 0.0) for delta in deltas[:period]]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    for delta in deltas[period:]:
        gain = max(delta, 0.0)
        loss = max(-delta, 0.0)
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

    if avg_loss == 0:
        return 100.0
    if avg_gain == 0:
        return 0.0
    relative_strength = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + relative_strength))


def td9_setup(values: list[float]) -> str:
    if len(values) < 5:
        return "UNAVAILABLE"
    direction: str | None = None
    count = 0
    for index in range(4, len(values)):
        if values[index] > values[index - 4]:
            next_direction = "SELL"
        elif values[index] < values[index - 4]:
            next_direction = "BUY"
        else:
            direction = None
            count = 0
            continue
        if next_direction == direction:
            count = min(count + 1, 9)
        else:
            direction = next_direction
            count = 1
    if direction is None or count == 0:
        return "NONE"
    return f"{direction}_SETUP_{count}"


def weekly_bars(daily_bars: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: list[dict[str, Any]] = []
    active_key: tuple[int, int] | None = None
    for bar in daily_bars:
        date_value = dt.date.fromisoformat(bar["date"])
        iso_year, iso_week, _ = date_value.isocalendar()
        key = (iso_year, iso_week)
        if key != active_key:
            grouped.append({"date": bar["date"], "close": bar["close"], "volume": bar.get("volume") or 0})
            active_key = key
        else:
            grouped[-1]["date"] = bar["date"]
            grouped[-1]["close"] = bar["close"]
            grouped[-1]["volume"] += bar.get("volume") or 0
    return grouped


def monthly_bars(daily_bars: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: list[dict[str, Any]] = []
    active_key: tuple[int, int] | None = None
    for bar in daily_bars:
        date_value = dt.date.fromisoformat(bar["date"])
        key = (date_value.year, date_value.month)
        if key != active_key:
            grouped.append({"date": bar["date"], "close": bar["close"], "volume": bar.get("volume") or 0})
            active_key = key
        else:
            grouped[-1]["date"] = bar["date"]
            grouped[-1]["close"] = bar["close"]
            grouped[-1]["volume"] += bar.get("volume") or 0
    return grouped


def volume_ratio(values: list[int | None], period: int = 20) -> float | None:
    clean = [value for value in values if value is not None]
    if len(clean) < period or clean[-1] is None:
        return None
    avg_volume = sum(clean[-period:]) / period
    if avg_volume == 0:
        return None
    return clean[-1] / avg_volume


def ma_alignment(last_close: float | None, ma20: float | None, ma50: float | None) -> str:
    if last_close is None or ma20 is None or ma50 is None:
        return "UNAVAILABLE"
    if last_close > ma20 > ma50:
        return "BULLISH"
    if last_close < ma20 < ma50:
        return "BEARISH"
    return "MIXED"


def summarize_timeframe(bars: list[dict[str, Any]], suffix: str) -> dict[str, Any]:
    values = closes(bars)
    if not values:
        return {"status": "UNAVAILABLE"}
    ma20 = simple_ma(values, 20)
    ma50 = simple_ma(values, 50)
    last_close = values[-1]
    summary: dict[str, Any] = {
        "as_of": bars[-1]["date"],
        "bars": len(values),
        "close": round_or_none(last_close, 4),
        "td9": td9_setup(values),
        "rsi_14": round_or_none(rsi_wilder(values, 14), 2),
        "ma20": round_or_none(ma20, 4),
        "ma50": round_or_none(ma50, 4),
        "ma_alignment": ma_alignment(last_close, ma20, ma50),
        f"momentum_20{suffix}_pct": round_or_none(momentum_pct(values, 20), 2),
        f"momentum_60{suffix}_pct": round_or_none(momentum_pct(values, 60), 2),
    }
    summary.update(macd(values))
    if bars and any(bar.get("volume") is not None for bar in bars):
        summary[f"volume_ratio_20{suffix}"] = round_or_none(volume_ratio(volumes(bars), 20), 2)
    else:
        summary[f"volume_ratio_20{suffix}"] = None
    return summary


def add_relative_strength(results: list[dict[str, Any]], benchmark: str) -> None:
    benchmark_record = next((item for item in results if item["ticker"] == benchmark), None)
    if not benchmark_record or benchmark_record.get("status") != "OK":
        return
    timeframe_suffixes = {
        "daily": "d",
        "weekly": "w",
        "monthly": "m",
    }
    for record in results:
        if record.get("status") != "OK":
            continue
        for timeframe, suffix in timeframe_suffixes.items():
            benchmark_frame = benchmark_record.get(timeframe, {})
            frame = record.get(timeframe, {})
            benchmark_m20 = benchmark_frame.get(f"momentum_20{suffix}_pct")
            benchmark_m60 = benchmark_frame.get(f"momentum_60{suffix}_pct")
            m20 = frame.get(f"momentum_20{suffix}_pct")
            m60 = frame.get(f"momentum_60{suffix}_pct")
            frame[f"relative_strength_20{suffix}_vs_benchmark_pct"] = (
                round_or_none(m20 - benchmark_m20, 2)
                if m20 is not None and benchmark_m20 is not None
                else None
            )
            frame[f"relative_strength_60{suffix}_vs_benchmark_pct"] = (
                round_or_none(m60 - benchmark_m60, 2)
                if m60 is not None and benchmark_m60 is not None
                else None
            )


def build_record(
    ticker: str,
    history_dir: Path | None,
    chart_range: str,
    interval: str,
    retrieved_at: str,
) -> dict[str, Any]:
    bars, source, source_type = load_history(ticker, history_dir, chart_range, interval)
    if len(bars) < 60:
        raise RuntimeError(f"{ticker} has {len(bars)} bars; need at least 60 for GO-grade indicators")
    weekly = weekly_bars(bars)
    monthly = monthly_bars(bars)
    return {
        "ticker": ticker,
        "status": "OK",
        "source_type": source_type,
        "source": source,
        "retrieved_at": retrieved_at,
        "daily": summarize_timeframe(bars, "d"),
        "weekly": summarize_timeframe(weekly, "w"),
        "monthly": summarize_timeframe(monthly, "m"),
    }


def main() -> int:
    args = parse_args()
    tickers = load_tickers(args)
    if not tickers:
        print("No tickers supplied", file=sys.stderr)
        return 2

    retrieved_at = utc_now_iso()
    results: list[dict[str, Any]] = []
    for ticker in tickers:
        try:
            results.append(
                build_record(
                    ticker=ticker,
                    history_dir=args.history_dir,
                    chart_range=args.range,
                    interval=args.interval,
                    retrieved_at=retrieved_at,
                )
            )
        except (RuntimeError, OSError, urllib.error.URLError, ValueError) as exc:
            results.append(
                {
                    "ticker": ticker,
                    "status": "UNAVAILABLE",
                    "retrieved_at": retrieved_at,
                    "error": str(exc),
                }
            )

    benchmark = args.benchmark.upper()
    add_relative_strength(results, benchmark)

    payload = {
        "format_version": "1.0",
        "generated_at": retrieved_at,
        "benchmark": benchmark,
        "definitions": {
            "td9": "TD Sequential setup count only: close greater/less than close four bars earlier, capped at 9.",
            "rsi_14": "Wilder RSI over 14 bars.",
            "macd": "EMA(12) - EMA(26), signal EMA(9), histogram MACD minus signal.",
            "relative_strength": "Ticker momentum percentage minus benchmark momentum percentage over the same lookback.",
            "timeframes": "daily, weekly, and monthly bars; momentum keys use d/w/m suffixes.",
        },
        "indicators": results,
    }

    output = json.dumps(payload, indent=2 if args.pretty else None, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)

    ok_count = sum(1 for result in results if result.get("status") == "OK")
    return 0 if ok_count > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
