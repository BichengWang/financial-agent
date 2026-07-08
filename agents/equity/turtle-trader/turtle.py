#!/usr/bin/env python3
"""Turtle Trading System for US equities & ETFs.

A deterministic implementation of the classic Dennis/Eckhardt Turtle rules, adapted to
stocks/ETFs (dollars-per-point = 1). One script, two modes:

  * ``--mode scan``     — stateless "what would I do today" over a universe of tickers:
                          N (20-day Wilder ATR), 20/55-day Donchian breakout signals, unit
                          sizing, 2N stops, +1/2 N pyramiding adds, and 10/20-day exits.
  * ``--mode backtest`` — per-ticker historical simulation of the full system with stats.

Universe: defaults to the S&P 500 union Nasdaq-100 constituents, read from Wikipedia and
cached locally; ``--tickers`` / ``--tickers-file`` override. Price history comes from
``yfinance`` (bulk threaded download) with a local cache, or from ``--history-dir`` OHLC
CSVs for fully offline / deterministic runs.

Non-fabrication discipline: every value comes from a fetch this run (yfinance or CSV) or is
reported ``UNAVAILABLE``. Nothing is invented.

Heavy third-party imports (pandas, yfinance) are loaded lazily, so the compute core and the
offline CSV path run on the standard library alone.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import ssl
import sys
import time
import urllib.error
import urllib.request
from io import StringIO
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

# --------------------------------------------------------------------------------------
# Classic Turtle defaults
# --------------------------------------------------------------------------------------

N_PERIOD = 20            # Wilder ATR lookback for N (volatility unit)
RISK_PCT = 0.01          # 1% of equity risked per N of price movement (one Unit)
STOP_MULT = 2.0          # initial stop distance in units of N
ADD_SPACING = 0.5        # add one Unit every +1/2 N favorable move
MAX_UNITS = 4            # max Units per market

SYSTEM1 = {"entry": 20, "exit": 10}   # short-term breakout system (with last-trade filter)
SYSTEM2 = {"entry": 55, "exit": 20}   # long-term breakout system (always taken)
FAILSAFE_PERIOD = 55                  # System 1 skipped signals are rescued at the 55-day breakout

WIKI_SP500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
WIKI_NDX = "https://en.wikipedia.org/wiki/Nasdaq-100"
USER_AGENT = "turtle-trader/1.0 (+https://en.wikipedia.org)"


# --------------------------------------------------------------------------------------
# Small utilities
# --------------------------------------------------------------------------------------

def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today_str() -> str:
    return dt.date.today().isoformat()


def yahoo_symbol(symbol: str) -> str:
    """Normalize a ticker to the Yahoo convention (BRK.B -> BRK-B)."""
    return symbol.strip().upper().replace(".", "-")


def round_or_none(value: float | None, digits: int = 4) -> float | None:
    if value is None or (isinstance(value, float) and (math.isnan(value) or math.isinf(value))):
        return None
    return round(value, digits)


def chunked(items: Sequence[str], size: int) -> Iterable[list[str]]:
    for index in range(0, len(items), size):
        yield list(items[index:index + size])


_SSL_CONTEXT: ssl.SSLContext | None = None


def https_context() -> ssl.SSLContext:
    """Opportunistic certifi CA bundle (python.org macOS builds ship without one)."""
    global _SSL_CONTEXT
    if _SSL_CONTEXT is None:
        try:
            import certifi

            _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
        except Exception:
            _SSL_CONTEXT = ssl.create_default_context()
    return _SSL_CONTEXT


def http_get(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout, context=https_context()) as response:
        return response.read().decode("utf-8")


# --------------------------------------------------------------------------------------
# Universe layer — index constituents (Wikipedia), cached locally
# --------------------------------------------------------------------------------------

def _read_html_tables(url: str):
    """Fetch a page with a browser-like UA and parse its tables with pandas."""
    try:
        import pandas as pd  # noqa: F401  (lazy: only needed for universe refresh)
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "pandas is required to refresh the index universe (pip install pandas lxml)."
        ) from exc
    html = http_get(url)
    return pd.read_html(StringIO(html))


def fetch_sp500_constituents() -> list[str]:
    tables = _read_html_tables(WIKI_SP500)
    df = tables[0]
    column = "Symbol" if "Symbol" in df.columns else df.columns[0]
    return [yahoo_symbol(str(s)) for s in df[column].tolist()]


def fetch_nasdaq100_constituents() -> list[str]:
    tables = _read_html_tables(WIKI_NDX)
    for df in tables:
        columns = [str(c) for c in df.columns]
        for key in ("Ticker", "Symbol"):
            if key in columns:
                return [yahoo_symbol(str(s)) for s in df[key].tolist()]
    raise RuntimeError("Could not locate the Nasdaq-100 constituents table on Wikipedia.")


INDEX_FETCHERS: dict[str, Callable[[], list[str]]] = {
    "sp500": fetch_sp500_constituents,
    "nasdaq100": fetch_nasdaq100_constituents,
}


def load_index(index: str, cache_dir: Path, refresh: bool) -> list[str]:
    path = cache_dir / f"{index}.json"
    if refresh or not path.exists():
        tickers = INDEX_FETCHERS[index]()
        cache_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps({"index": index, "fetched_at": utc_now_iso(), "tickers": tickers}, indent=2),
            encoding="utf-8",
        )
        return tickers
    return list(json.loads(path.read_text(encoding="utf-8"))["tickers"])


def resolve_universe(args: argparse.Namespace, cache_dir: Path) -> list[str]:
    """Build the ticker list: explicit override wins, else the requested index union."""
    explicit: list[str] = []
    for chunk in args.tickers or []:
        explicit.extend(chunk.replace(",", " ").split())
    if args.tickers_file:
        explicit.extend(Path(args.tickers_file).read_text(encoding="utf-8").replace(",", " ").split())
    if explicit:
        return dedup([yahoo_symbol(t) for t in explicit])

    indexes = {"sp500": ["sp500"], "nasdaq100": ["nasdaq100"], "both": ["sp500", "nasdaq100"]}[args.universe]
    tickers: list[str] = []
    for index in indexes:
        tickers.extend(load_index(index, cache_dir, args.refresh_universe))
    return dedup(tickers)


def dedup(tickers: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for ticker in tickers:
        if ticker and ticker not in seen:
            seen.add(ticker)
            out.append(ticker)
    return out


# --------------------------------------------------------------------------------------
# Data layer — price history (yfinance bulk download, CSV offline, local cache)
# --------------------------------------------------------------------------------------

Bar = dict[str, Any]


def load_csv_history(symbol: str, history_dir: Path) -> list[Bar] | None:
    """Read an OHLC(V) CSV named TICKER.csv (case-insensitive headers). Offline path."""
    candidates = [history_dir / f"{symbol}.csv", history_dir / f"{symbol.lower()}.csv"]
    path = next((candidate for candidate in candidates if candidate.exists()), None)
    if path is None:
        return None
    bars: list[Bar] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        lower = {name.lower(): name for name in (reader.fieldnames or [])}

        def pick(row: dict[str, str], *names: str) -> str | None:
            for name in names:
                key = lower.get(name)
                if key and row.get(key) not in (None, ""):
                    return row[key]
            return None

        for row in reader:
            date_value = pick(row, "date")
            close_value = pick(row, "close", "adj close", "adjclose", "adj_close")
            if not date_value or close_value is None:
                continue
            bars.append(
                {
                    "date": date_value[:10],
                    "open": _to_float(pick(row, "open")),
                    "high": _to_float(pick(row, "high")),
                    "low": _to_float(pick(row, "low")),
                    "close": float(close_value),
                    "volume": _to_int(pick(row, "volume")),
                }
            )
    bars.sort(key=lambda bar: bar["date"])
    return bars


def _to_float(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    try:
        result = float(value)
    except ValueError:
        return None
    return None if math.isnan(result) else result


def _to_int(value: str | None) -> int | None:
    parsed = _to_float(value)
    return int(parsed) if parsed is not None else None


def _bars_from_frame(frame: Any) -> list[Bar]:
    import pandas as pd

    bars: list[Bar] = []
    for index, row in frame.iterrows():
        close = row.get("Close")
        if close is None or pd.isna(close):
            continue
        timestamp = index.date().isoformat() if hasattr(index, "date") else str(index)[:10]
        bars.append(
            {
                "date": timestamp,
                "open": _cell(row.get("Open")),
                "high": _cell(row.get("High")),
                "low": _cell(row.get("Low")),
                "close": float(close),
                "volume": _cell_int(row.get("Volume")),
            }
        )
    return bars


def _cell(value: Any) -> float | None:
    import pandas as pd

    if value is None or pd.isna(value):
        return None
    return float(value)


def _cell_int(value: Any) -> int | None:
    cell = _cell(value)
    return int(cell) if cell is not None else None


def fetch_yfinance(tickers: list[str], period: str, interval: str, chunk_size: int, pause: float) -> dict[str, list[Bar]]:
    try:
        import yfinance as yf
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("yfinance is required to fetch prices (pip install yfinance).") from exc

    histories: dict[str, list[Bar]] = {}
    batches = list(chunked(tickers, chunk_size))
    for position, batch in enumerate(batches):
        data = yf.download(
            batch,
            period=period,
            interval=interval,
            auto_adjust=True,
            group_by="ticker",
            threads=True,
            progress=False,
        )
        for ticker in batch:
            frame = _select_ticker_frame(data, ticker, len(batch))
            histories[ticker] = _bars_from_frame(frame.dropna(how="all")) if frame is not None else []
        if pause and position < len(batches) - 1:
            time.sleep(pause)
    return histories


def _select_ticker_frame(data: Any, ticker: str, batch_size: int):
    if batch_size == 1:
        return data
    try:
        if ticker in data.columns.get_level_values(0):
            return data[ticker]
    except (AttributeError, KeyError):
        return None
    return None


def _cache_path(cache_dir: Path, ticker: str, period: str, interval: str) -> Path:
    return cache_dir / f"{ticker}__{period}__{interval}.json"


def read_price_cache(cache_dir: Path, ticker: str, period: str, interval: str) -> list[Bar] | None:
    path = _cache_path(cache_dir, ticker, period, interval)
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("fetched_date") != today_str():
        return None
    return payload.get("bars")


def write_price_cache(cache_dir: Path, ticker: str, period: str, interval: str, bars: list[Bar]) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = _cache_path(cache_dir, ticker, period, interval)
    path.write_text(
        json.dumps({"ticker": ticker, "fetched_date": today_str(), "bars": bars}),
        encoding="utf-8",
    )


def get_histories(
    tickers: list[str],
    period: str,
    interval: str,
    cache_dir: Path,
    use_cache: bool,
    history_dir: Path | None,
    chunk_size: int,
    pause: float,
) -> dict[str, list[Bar] | None]:
    """Return ticker -> bars (or None when no data could be sourced)."""
    histories: dict[str, list[Bar] | None] = {}

    if history_dir is not None:  # fully offline, deterministic
        for ticker in tickers:
            histories[ticker] = load_csv_history(ticker, history_dir)
        return histories

    to_fetch: list[str] = []
    for ticker in tickers:
        cached = read_price_cache(cache_dir, ticker, period, interval) if use_cache else None
        if cached is not None:
            histories[ticker] = cached
        else:
            to_fetch.append(ticker)

    if to_fetch:
        fetched = fetch_yfinance(to_fetch, period, interval, chunk_size, pause)
        for ticker in to_fetch:
            bars = fetched.get(ticker) or []
            histories[ticker] = bars if bars else None
            if use_cache and bars:
                write_price_cache(cache_dir, ticker, period, interval, bars)

    return histories


# --------------------------------------------------------------------------------------
# Compute core — deterministic, standard library only
# --------------------------------------------------------------------------------------

def true_ranges(bars: list[Bar]) -> list[float | None]:
    """True Range per bar; index 0 is None (needs a prior close)."""
    trs: list[float | None] = [None]
    for index in range(1, len(bars)):
        high, low = bars[index]["high"], bars[index]["low"]
        prev_close = bars[index - 1]["close"]
        if high is None or low is None or prev_close is None:
            trs.append(None)
            continue
        trs.append(max(high - low, abs(high - prev_close), abs(low - prev_close)))
    return trs


def wilder_n(bars: list[Bar], period: int = N_PERIOD) -> list[float | None]:
    """N = Wilder-smoothed ATR: N = (19*prevN + TR)/20, seeded by the first 20 TR average."""
    trs = true_ranges(bars)
    n_series: list[float | None] = [None] * len(bars)
    valid = [(index, tr) for index, tr in enumerate(trs) if tr is not None]
    if len(valid) < period:
        return n_series

    seed_index = valid[period - 1][0]
    current = sum(tr for _, tr in valid[:period]) / period
    n_series[seed_index] = current
    for index in range(seed_index + 1, len(bars)):
        tr = trs[index]
        if tr is None:
            n_series[index] = current  # carry forward across a gap
            continue
        current = (current * (period - 1) + tr) / period
        n_series[index] = current
    return n_series


def rolling_extreme(bars: list[Bar], key: str, period: int, idx: int, want_max: bool) -> float | None:
    """Highest high / lowest low over the `period` bars BEFORE idx (excludes idx)."""
    if idx < period:
        return None
    window = [bars[j][key] for j in range(idx - period, idx) if bars[j][key] is not None]
    if len(window) < period:
        return None
    return max(window) if want_max else min(window)


def unit_size(account: float, n: float, risk_pct: float, dollars_per_point: float = 1.0) -> int:
    """Shares per Unit so a 1 N move equals risk_pct of the account."""
    if n <= 0 or account <= 0:
        return 0
    return int((risk_pct * account) / (n * dollars_per_point))


# --------------------------------------------------------------------------------------
# Single-instrument simulator (shared by the backtest and the System 1 last-trade filter)
# --------------------------------------------------------------------------------------

class Trade:
    __slots__ = (
        "direction", "entry_date", "exit_date", "units", "entry_avg",
        "exit_price", "shares_per_unit", "pnl", "result",
    )

    def __init__(self, direction: str, entry_date: str, shares_per_unit: int) -> None:
        self.direction = direction
        self.entry_date = entry_date
        self.exit_date: str | None = None
        self.units = 0
        self.entry_avg = 0.0
        self.exit_price = 0.0
        self.shares_per_unit = shares_per_unit
        self.pnl = 0.0
        self.result = "OPEN"

    def to_dict(self) -> dict[str, Any]:
        return {
            "direction": self.direction,
            "entry_date": self.entry_date,
            "exit_date": self.exit_date,
            "units": self.units,
            "shares_per_unit": self.shares_per_unit,
            "entry_avg": round_or_none(self.entry_avg, 4),
            "exit_price": round_or_none(self.exit_price, 4),
            "pnl": round_or_none(self.pnl, 2),
            "result": self.result,
        }


def simulate(
    bars: list[Bar],
    entry_period: int,
    exit_period: int,
    *,
    n_period: int = N_PERIOD,
    stop_mult: float = STOP_MULT,
    add_spacing: float = ADD_SPACING,
    max_units: int = MAX_UNITS,
    account: float = 100_000.0,
    risk_pct: float = RISK_PCT,
    allow_short: bool = True,
    apply_s1_filter: bool = False,
    failsafe_period: int = FAILSAFE_PERIOD,
    compound: bool = True,
    drawdown_throttle: bool = False,
) -> dict[str, Any]:
    """Run the Turtle rules on one instrument. Returns closed trades + an equity curve.

    Fills are modeled on daily bars: breakouts fill at the breakout level (or the open on a
    gap through it); stops and trailing exits fill at their level (or the open on a gap).
    Within a bar, protective exits are checked before pyramiding adds.
    """
    n_series = wilder_n(bars, n_period)
    start = max(entry_period, exit_period, n_period, failsafe_period if apply_s1_filter else 0) + 1

    cash = account
    peak_equity = account
    equity_curve: list[tuple[str, float]] = []
    trades: list[Trade] = []

    position: dict[str, Any] | None = None
    last_breakout_won: bool | None = None  # tracks prior single-direction breakout outcome (S1 filter)

    for i in range(start, len(bars)):
        bar = bars[i]
        n = n_series[i - 1]
        if n is None or n <= 0:
            equity_curve.append((bar["date"], cash + _open_mtm(position, bar)))
            continue

        closed_this_bar = False

        if position is not None:
            closed_this_bar = _manage_open_position(position, bar, bars, i, exit_period, stop_mult, add_spacing, max_units)
            if closed_this_bar:
                trade: Trade = position["trade"]
                cash += trade.pnl
                trades.append(trade)
                if apply_s1_filter:
                    last_breakout_won = trade.pnl > 0
                position = None

        if position is None and not closed_this_bar:
            signal, level = _entry_signal(bars, i, entry_period, allow_short)
            if signal is not None:
                take = True
                if apply_s1_filter and last_breakout_won:
                    # Skip a breakout that follows a winner — unless the failsafe breakout also fires.
                    fh = rolling_extreme(bars, "high", failsafe_period, i, want_max=True)
                    fl = rolling_extreme(bars, "low", failsafe_period, i, want_max=False)
                    failsafe = (signal == "LONG" and fh is not None and bar["high"] > fh) or (
                        signal == "SHORT" and fl is not None and bar["low"] < fl
                    )
                    take = failsafe
                if take:
                    equity_for_size = (cash + _open_mtm(position, bar)) if compound else account
                    if drawdown_throttle:
                        equity_for_size *= _throttle_multiplier(cash + _open_mtm(position, bar), peak_equity)
                    shares = unit_size(equity_for_size, n, risk_pct)
                    if shares > 0:
                        position = _open_position(signal, level, bar, n, shares, stop_mult)

        equity = cash + _open_mtm(position, bar)
        peak_equity = max(peak_equity, equity)
        equity_curve.append((bar["date"], equity))

    # Close any still-open position at the last bar's close for accounting.
    if position is not None:
        trade = position["trade"]
        last_close = bars[-1]["close"]
        _close_position(position, last_close, bars[-1]["date"])
        cash += trade.pnl
        trades.append(trade)

    return _summarize_backtest(bars, trades, equity_curve, account)


def _open_position(signal: str, level: float, bar: Bar, n: float, shares: int, stop_mult: float) -> dict[str, Any]:
    entry = bar["open"] if (bar["open"] is not None and (
        (signal == "LONG" and bar["open"] > level) or (signal == "SHORT" and bar["open"] < level)
    )) else level
    trade = Trade(signal, bar["date"], shares)
    trade.units = 1
    trade.entry_avg = entry
    sign = 1.0 if signal == "LONG" else -1.0
    return {
        "trade": trade,
        "direction": signal,
        "sign": sign,
        "n": n,
        "shares": shares,
        "entries": [entry],
        "last_add": entry,
        "stop": entry - sign * stop_mult * n,
    }


def _manage_open_position(
    position: dict[str, Any], bar: Bar, bars: list[Bar], i: int,
    exit_period: int, stop_mult: float, add_spacing: float, max_units: int,
) -> bool:
    sign = position["sign"]
    n = position["n"]

    # 1) Protective stop.
    stop = position["stop"]
    if (sign > 0 and bar["low"] is not None and bar["low"] <= stop) or (
        sign < 0 and bar["high"] is not None and bar["high"] >= stop
    ):
        fill = bar["open"] if (bar["open"] is not None and (
            (sign > 0 and bar["open"] < stop) or (sign < 0 and bar["open"] > stop)
        )) else stop
        _close_position(position, fill, bar["date"])
        return True

    # 2) Trailing channel exit (10/20-day opposite extreme).
    exit_level = rolling_extreme(bars, "low" if sign > 0 else "high", exit_period, i, want_max=sign < 0)
    if exit_level is not None:
        if (sign > 0 and bar["low"] is not None and bar["low"] < exit_level) or (
            sign < 0 and bar["high"] is not None and bar["high"] > exit_level
        ):
            fill = bar["open"] if (bar["open"] is not None and (
                (sign > 0 and bar["open"] < exit_level) or (sign < 0 and bar["open"] > exit_level)
            )) else exit_level
            _close_position(position, fill, bar["date"])
            return True

    # 3) Pyramiding adds at every +1/2 N favorable move (stop ratchets to the latest unit).
    trade: Trade = position["trade"]
    while trade.units < max_units:
        next_add = position["last_add"] + sign * add_spacing * n
        reached = (sign > 0 and bar["high"] is not None and bar["high"] >= next_add) or (
            sign < 0 and bar["low"] is not None and bar["low"] <= next_add
        )
        if not reached:
            break
        position["entries"].append(next_add)
        position["last_add"] = next_add
        trade.units += 1
        trade.entry_avg = sum(position["entries"]) / len(position["entries"])
        position["stop"] = next_add - sign * stop_mult * n
    return False


def _close_position(position: dict[str, Any], price: float, date: str) -> None:
    trade: Trade = position["trade"]
    sign = position["sign"]
    shares = position["shares"]
    pnl = sum((price - entry) * sign * shares for entry in position["entries"])
    trade.exit_price = price
    trade.exit_date = date
    trade.pnl = pnl
    trade.result = "WIN" if pnl > 0 else ("LOSS" if pnl < 0 else "SCRATCH")


def _open_mtm(position: dict[str, Any] | None, bar: Bar) -> float:
    if position is None or bar["close"] is None:
        return 0.0
    sign = position["sign"]
    shares = position["shares"]
    return sum((bar["close"] - entry) * sign * shares for entry in position["entries"])


def _throttle_multiplier(equity: float, peak: float) -> float:
    if peak <= 0 or equity >= peak:
        return 1.0
    drawdown = (peak - equity) / peak
    buckets = int(drawdown / 0.10)
    return 0.8 ** buckets


def _entry_signal(bars: list[Bar], i: int, entry_period: int, allow_short: bool) -> tuple[str | None, float]:
    bar = bars[i]
    high_break = rolling_extreme(bars, "high", entry_period, i, want_max=True)
    low_break = rolling_extreme(bars, "low", entry_period, i, want_max=False)
    if high_break is not None and bar["high"] is not None and bar["high"] > high_break:
        return "LONG", high_break
    if allow_short and low_break is not None and bar["low"] is not None and bar["low"] < low_break:
        return "SHORT", low_break
    return None, 0.0


# --------------------------------------------------------------------------------------
# Backtest summary statistics
# --------------------------------------------------------------------------------------

def _summarize_backtest(bars: list[Bar], trades: list[Trade], equity_curve: list[tuple[str, float]], account: float) -> dict[str, Any]:
    final_equity = equity_curve[-1][1] if equity_curve else account
    wins = [t.pnl for t in trades if t.pnl > 0]
    losses = [t.pnl for t in trades if t.pnl < 0]
    gross_win = sum(wins)
    gross_loss = abs(sum(losses))

    max_dd = 0.0
    peak = account
    for _, equity in equity_curve:
        peak = max(peak, equity)
        if peak > 0:
            max_dd = max(max_dd, (peak - equity) / peak)

    years = _span_years(bars)
    cagr = ((final_equity / account) ** (1 / years) - 1) if years > 0 and final_equity > 0 else None

    return {
        "bars": len(bars),
        "start": bars[0]["date"] if bars else None,
        "end": bars[-1]["date"] if bars else None,
        "initial_account": round_or_none(account, 2),
        "final_equity": round_or_none(final_equity, 2),
        "total_return_pct": round_or_none((final_equity / account - 1) * 100, 2),
        "cagr_pct": round_or_none(cagr * 100, 2) if cagr is not None else None,
        "max_drawdown_pct": round_or_none(max_dd * 100, 2),
        "num_trades": len(trades),
        "win_rate_pct": round_or_none(100 * len(wins) / len(trades), 2) if trades else None,
        "avg_win": round_or_none(gross_win / len(wins), 2) if wins else None,
        "avg_loss": round_or_none(sum(losses) / len(losses), 2) if losses else None,
        "profit_factor": round_or_none(gross_win / gross_loss, 2) if gross_loss > 0 else None,
        "expectancy": round_or_none(sum(t.pnl for t in trades) / len(trades), 2) if trades else None,
        "_trades": trades,
    }


def _span_years(bars: list[Bar]) -> float:
    if len(bars) < 2:
        return 0.0
    start = dt.date.fromisoformat(bars[0]["date"])
    end = dt.date.fromisoformat(bars[-1]["date"])
    return max((end - start).days / 365.25, 0.0)


# --------------------------------------------------------------------------------------
# Scan mode — stateless "what would I do today" per ticker
# --------------------------------------------------------------------------------------

def last_trade_filter_state(bars: list[Bar], signal_direction: str, args: argparse.Namespace) -> str:
    """System 1 filter: skip a breakout if the previous breakout trade was a winner.

    Computed deterministically by replaying single-unit System 1 trades (no filter) and
    inspecting the most recent closed trade.
    """
    result = simulate(
        bars, SYSTEM1["entry"], SYSTEM1["exit"],
        n_period=args.n_period, stop_mult=args.stop_mult, add_spacing=args.add_spacing,
        max_units=1, account=args.account, risk_pct=args.risk_pct,
        allow_short=not args.long_only, apply_s1_filter=False, compound=False,
    )
    closed = result["_trades"]
    if not closed:
        return "TAKE"
    return "SKIP_LAST_WAS_WINNER" if closed[-1].pnl > 0 else "TAKE"


def scan_system_block(bars: list[Bar], i: int, entry_period: int, exit_period: int, allow_short: bool) -> dict[str, Any]:
    bar = bars[i]
    high_break = rolling_extreme(bars, "high", entry_period, i, want_max=True)
    low_break = rolling_extreme(bars, "low", entry_period, i, want_max=False)
    signal, _ = _entry_signal(bars, i, entry_period, allow_short)
    return {
        "entry_period": entry_period,
        "exit_period": exit_period,
        "breakout_high": round_or_none(high_break, 4),
        "breakout_low": round_or_none(low_break, 4),
        "signal": f"{signal}_ENTRY" if signal else "NONE",
        "exit_for_long": round_or_none(rolling_extreme(bars, "low", exit_period, i + 1, want_max=False), 4),
        "exit_for_short": round_or_none(rolling_extreme(bars, "high", exit_period, i + 1, want_max=True), 4),
    }


def build_entry_plan(direction: str, level: float, n: float, shares: int, exit_level: float | None,
                     system: int, args: argparse.Namespace) -> dict[str, Any]:
    sign = 1.0 if direction == "LONG" else -1.0
    adds = []
    stops_after_add = []
    price = level
    for unit in range(1, args.max_units):
        price = price + sign * args.add_spacing * n
        adds.append(round_or_none(price, 4))
        stops_after_add.append(round_or_none(price - sign * args.stop_mult * n, 4))
    return {
        "system": system,
        "direction": direction,
        "entry_price": round_or_none(level, 4),
        "unit_shares": shares,
        "initial_stop": round_or_none(level - sign * args.stop_mult * n, 4),
        "add_levels": adds,
        "stop_after_each_add": stops_after_add,
        "exit_level": round_or_none(exit_level, 4),
        "max_units": args.max_units,
    }


def scan_ticker(ticker: str, bars: list[Bar] | None, args: argparse.Namespace) -> dict[str, Any]:
    if not bars or len(bars) < max(SYSTEM2["entry"], args.n_period) + 2:
        return {"ticker": ticker, "status": "UNAVAILABLE",
                "error": "insufficient price history" if bars else "no price data"}

    n_series = wilder_n(bars, args.n_period)
    i = len(bars) - 1
    n = n_series[i]
    if n is None or n <= 0:
        return {"ticker": ticker, "status": "UNAVAILABLE", "error": "N (ATR) unavailable"}

    allow_short = not args.long_only
    shares = unit_size(args.account, n, args.risk_pct)
    close = bars[i]["close"]

    system1 = scan_system_block(bars, i, SYSTEM1["entry"], SYSTEM1["exit"], allow_short)
    system2 = scan_system_block(bars, i, SYSTEM2["entry"], SYSTEM2["exit"], allow_short)

    # System 1 last-trade filter + 55-day failsafe, evaluated for the signalled direction.
    s1_actionable = False
    if system1["signal"] != "NONE":
        direction = system1["signal"].split("_")[0]
        state = last_trade_filter_state(bars, direction, args)
        failsafe = False
        if state == "SKIP_LAST_WAS_WINNER":
            fh = rolling_extreme(bars, "high", FAILSAFE_PERIOD, i, want_max=True)
            fl = rolling_extreme(bars, "low", FAILSAFE_PERIOD, i, want_max=False)
            failsafe = (direction == "LONG" and fh is not None and bars[i]["high"] > fh) or (
                direction == "SHORT" and fl is not None and bars[i]["low"] < fl
            )
        system1["last_trade_filter"] = state
        system1["failsafe_55d"] = failsafe
        s1_actionable = (state == "TAKE") or failsafe
    else:
        system1["last_trade_filter"] = "N/A"
        system1["failsafe_55d"] = False

    record: dict[str, Any] = {
        "ticker": ticker,
        "status": "OK",
        "as_of": bars[i]["date"],
        "bars": len(bars),
        "close": round_or_none(close, 4),
        "n_atr20": round_or_none(n, 4),
        "unit_shares": shares,
        "unit_dollar_exposure": round_or_none(shares * close, 2) if close is not None else None,
        "dollar_volatility": round_or_none(shares * n, 2),
        "account": args.account,
        "risk_pct": args.risk_pct,
        "system1": system1,
        "system2": system2,
    }

    # Build a concrete entry plan if anything actionable fires today (System 1 preferred).
    plan = None
    if s1_actionable:
        direction = system1["signal"].split("_")[0]
        level = system1["breakout_high"] if direction == "LONG" else system1["breakout_low"]
        exit_level = system1["exit_for_long"] if direction == "LONG" else system1["exit_for_short"]
        plan = build_entry_plan(direction, level, n, shares, exit_level, 1, args)
    elif system2["signal"] != "NONE":
        direction = system2["signal"].split("_")[0]
        level = system2["breakout_high"] if direction == "LONG" else system2["breakout_low"]
        exit_level = system2["exit_for_long"] if direction == "LONG" else system2["exit_for_short"]
        plan = build_entry_plan(direction, level, n, shares, exit_level, 2, args)
    if plan is not None:
        record["entry_plan"] = plan
        record["actionable"] = True
    else:
        record["actionable"] = False

    return record


def apply_unit_caps(records: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    """Portfolio-level Turtle unit caps across the actionable set."""
    actionable = [r for r in records if r.get("actionable")]
    longs = sum(1 for r in actionable if r["entry_plan"]["direction"] == "LONG")
    shorts = sum(1 for r in actionable if r["entry_plan"]["direction"] == "SHORT")
    return {
        "actionable_count": len(actionable),
        "long_signals": longs,
        "short_signals": shorts,
        "unit_caps": {
            "max_units_per_market": args.max_units,
            "max_units_per_direction": 12,
            "max_units_correlated": 6,
            "max_units_loosely_correlated": 10,
        },
        "note": (
            "Direction signal counts are 1 Unit each at first entry; respect the 12-units-per-"
            "direction cap and the 6/10 correlated-market caps when allocating across names."
        ),
    }


def run_scan(args: argparse.Namespace, paths: dict[str, Path]) -> dict[str, Any]:
    universe = resolve_universe(args, paths["universe"])
    histories = get_histories(
        universe, args.range, args.interval, paths["cache"],
        use_cache=not args.no_cache, history_dir=_history_dir(args),
        chunk_size=args.chunk_size, pause=args.pause,
    )
    records = [scan_ticker(ticker, histories.get(ticker), args) for ticker in universe]
    ok = [r for r in records if r["status"] == "OK"]

    if args.signals_only:
        emitted = [r for r in ok if r.get("actionable")]
    else:
        emitted = records

    return {
        "mode": "scan",
        "generated_at": utc_now_iso(),
        "universe": args.universe if not (args.tickers or args.tickers_file) else "custom",
        "universe_size": len(universe),
        "scanned_ok": len(ok),
        "params": _params(args),
        "portfolio": apply_unit_caps(records, args),
        "results": emitted,
    }


# --------------------------------------------------------------------------------------
# Backtest mode
# --------------------------------------------------------------------------------------

def backtest_ticker(ticker: str, bars: list[Bar] | None, system: dict[str, int], args: argparse.Namespace) -> dict[str, Any]:
    if not bars or len(bars) < system["entry"] + args.n_period + 5:
        return {"ticker": ticker, "system": _system_label(system), "status": "UNAVAILABLE",
                "error": "insufficient price history" if bars else "no price data"}
    result = simulate(
        bars, system["entry"], system["exit"],
        n_period=args.n_period, stop_mult=args.stop_mult, add_spacing=args.add_spacing,
        max_units=args.max_units, account=args.account, risk_pct=args.risk_pct,
        allow_short=not args.long_only, compound=not args.no_compound,
        drawdown_throttle=args.drawdown_throttle,
    )
    trades = result.pop("_trades")
    result.update({"ticker": ticker, "system": _system_label(system), "status": "OK"})
    if args.include_trades:
        result["trades"] = [t.to_dict() for t in trades]
    return result


def run_backtest(args: argparse.Namespace, paths: dict[str, Path]) -> dict[str, Any]:
    universe = resolve_universe(args, paths["universe"])
    histories = get_histories(
        universe, args.range, args.interval, paths["cache"],
        use_cache=not args.no_cache, history_dir=_history_dir(args),
        chunk_size=args.chunk_size, pause=args.pause,
    )
    systems = {"1": [SYSTEM1], "2": [SYSTEM2], "both": [SYSTEM1, SYSTEM2]}[args.system]

    results: list[dict[str, Any]] = []
    for ticker in universe:
        for system in systems:
            results.append(backtest_ticker(ticker, histories.get(ticker), system, args))

    ok = [r for r in results if r["status"] == "OK"]
    return {
        "mode": "backtest",
        "generated_at": utc_now_iso(),
        "universe_size": len(universe),
        "system": args.system,
        "params": _params(args),
        "aggregate": _aggregate_backtest(ok),
        "results": results,
    }


def _aggregate_backtest(ok: list[dict[str, Any]]) -> dict[str, Any]:
    if not ok:
        return {"runs": 0}
    trades = sum(r["num_trades"] for r in ok)
    weighted_win = [r["win_rate_pct"] for r in ok if r.get("win_rate_pct") is not None]
    return {
        "runs": len(ok),
        "total_trades": trades,
        "avg_total_return_pct": round_or_none(sum(r["total_return_pct"] for r in ok) / len(ok), 2),
        "avg_cagr_pct": round_or_none(
            sum(r["cagr_pct"] for r in ok if r.get("cagr_pct") is not None) / max(1, sum(1 for r in ok if r.get("cagr_pct") is not None)), 2),
        "avg_max_drawdown_pct": round_or_none(sum(r["max_drawdown_pct"] for r in ok) / len(ok), 2),
        "avg_win_rate_pct": round_or_none(sum(weighted_win) / len(weighted_win), 2) if weighted_win else None,
        "note": "Per-instrument runs are independent; cross-market correlation/unit caps are not modeled here.",
    }


# --------------------------------------------------------------------------------------
# CLI plumbing
# --------------------------------------------------------------------------------------

def _system_label(system: dict[str, int]) -> str:
    return "system1" if system["entry"] == SYSTEM1["entry"] else "system2"


def _history_dir(args: argparse.Namespace) -> Path | None:
    return Path(args.history_dir) if args.history_dir else None


def _params(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "n_period": args.n_period,
        "risk_pct": args.risk_pct,
        "stop_mult": args.stop_mult,
        "add_spacing": args.add_spacing,
        "max_units": args.max_units,
        "account": args.account,
        "long_only": args.long_only,
        "range": args.range,
        "interval": args.interval,
        "system1": SYSTEM1,
        "system2": SYSTEM2,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Turtle Trading System scanner + backtester (US equities/ETFs).")
    parser.add_argument("--mode", choices=["scan", "backtest"], default="scan")
    parser.add_argument("--universe", choices=["sp500", "nasdaq100", "both"], default="both",
                        help="Index universe when --tickers is not given. Default: both.")
    parser.add_argument("--tickers", nargs="*", help="Explicit tickers (space/comma separated); overrides --universe.")
    parser.add_argument("--tickers-file", help="File of tickers (space/comma/newline separated); overrides --universe.")
    parser.add_argument("--refresh-universe", action="store_true", help="Re-fetch index constituents from Wikipedia.")

    parser.add_argument("--account", type=float, default=100_000.0, help="Account equity for sizing. Default: 100000.")
    parser.add_argument("--risk-pct", type=float, default=RISK_PCT, dest="risk_pct")
    parser.add_argument("--n-period", type=int, default=N_PERIOD, dest="n_period")
    parser.add_argument("--stop-mult", type=float, default=STOP_MULT, dest="stop_mult")
    parser.add_argument("--add-spacing", type=float, default=ADD_SPACING, dest="add_spacing")
    parser.add_argument("--max-units", type=int, default=MAX_UNITS, dest="max_units")
    parser.add_argument("--allow-short", action="store_true", dest="allow_short",
                        help="Enable short breakouts. Default is long-only (equities rarely reward short breakouts).")

    parser.add_argument("--system", choices=["1", "2", "both"], default="both", help="Backtest which system(s).")
    parser.add_argument("--no-compound", action="store_true", help="Size off the initial account, not current equity.")
    parser.add_argument("--drawdown-throttle", action="store_true", help="Cut size 20%% per 10%% equity drawdown.")
    parser.add_argument("--include-trades", action="store_true", help="Include per-trade detail in backtest output.")

    parser.add_argument("--range", default=None, help="yfinance period (e.g. 1y, 2y, 5y, max). Default: 2y scan / max backtest.")
    parser.add_argument("--interval", default="1d")
    parser.add_argument("--history-dir", help="Directory of TICKER.csv OHLC files for offline/deterministic runs.")
    parser.add_argument("--no-cache", action="store_true", help="Bypass the local price cache.")
    parser.add_argument("--chunk-size", type=int, default=100, help="Tickers per yfinance bulk download. Default: 100.")
    parser.add_argument("--pause", type=float, default=1.0, help="Seconds between download chunks. Default: 1.0.")

    parser.add_argument("--signals-only", action="store_true", help="Scan: emit only names with an actionable entry today.")
    parser.add_argument("--output", help="Write JSON here instead of stdout.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    parser.add_argument("--data-dir", default=None, help="Base dir for universe/ and cache/. Default: alongside this script.")

    args = parser.parse_args(argv)
    if args.range is None:
        args.range = "max" if args.mode == "backtest" else "2y"
    args.long_only = not args.allow_short  # long-only is the default for equities
    return args


def print_backtest_summary(payload: dict[str, Any]) -> None:
    rows = [r for r in payload["results"] if r["status"] == "OK"]
    if not rows:
        print("No backtestable tickers.", file=sys.stderr)
        return
    header = f"{'TICKER':<8}{'SYS':<9}{'RET%':>9}{'CAGR%':>8}{'MAXDD%':>8}{'TRADES':>8}{'WIN%':>7}"
    print(header, file=sys.stderr)
    print("-" * len(header), file=sys.stderr)
    for r in rows:
        print(
            f"{r['ticker']:<8}{r['system']:<9}{_fmt(r['total_return_pct']):>9}{_fmt(r['cagr_pct']):>8}"
            f"{_fmt(r['max_drawdown_pct']):>8}{r['num_trades']:>8}{_fmt(r['win_rate_pct']):>7}",
            file=sys.stderr,
        )


def _fmt(value: float | None) -> str:
    return "—" if value is None else f"{value:.1f}"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    base = Path(args.data_dir) if args.data_dir else Path(__file__).resolve().parent
    paths = {"universe": base / "universe", "cache": base / "cache"}

    if args.refresh_universe and not (args.tickers or args.tickers_file):
        # Maintenance action: rebuild the constituent lists and exit. A subsequent scan/
        # backtest reuses the same-day cache, so no double fetch.
        try:
            for index in (["sp500", "nasdaq100"] if args.universe == "both" else [args.universe]):
                count = len(load_index(index, paths["universe"], refresh=True))
                print(f"{index}: {count} constituents cached", file=sys.stderr)
        except (RuntimeError, OSError, urllib.error.URLError) as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        return 0

    try:
        payload = run_scan(args, paths) if args.mode == "scan" else run_backtest(args, paths)
    except (RuntimeError, OSError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.mode == "backtest":
        print_backtest_summary(payload)

    text = json.dumps(payload, indent=2 if args.pretty else None, default=str)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
        print(f"wrote {out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
