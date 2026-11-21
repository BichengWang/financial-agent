import pandas as pd

TRAINED_MODEL_DIR = f"trained_models"
DATA_SAVE_DIR = f"datasets"
TENSORBOARD_LOG_DIR = f"tensorboard_log"
RESULTS_DIR = f"results"


## time_fmt = '%Y-%m-%d'
START_DATE = "2000-01-01"
END_DATE = "2025-10-01"
SPLIT_DATE = "2023-10-01"

START_TRADE_DATE = "2019-01-01"

## stockstats technical indicator column names
## check https://pypi.org/project/stockstats/ for different names
TECHNICAL_INDICATORS_LIST = ["macd", "boll_ub", "boll_lb", "rsi_10", "rsi_20", "cci_10", "cci_20", "dx_30", "close_20_sma", "close_60_sma", "close_120_sma", "close_20_ema", "close_60_ema", "close_120_ema"]


## Model Parameters
A2C_PARAMS = {"n_steps": 5, "ent_coef": 0.01, "learning_rate": 0.0007}
PPO_PARAMS = {
    "n_steps": 2048,
    "ent_coef": 0.01,
    "learning_rate": 0.00025,
    "batch_size": 64,
}
DDPG_PARAMS = {"batch_size": 128, "buffer_size": 50000, "learning_rate": 0.001}
TD3_PARAMS = {"batch_size": 100, "buffer_size": 1000000, "learning_rate": 0.001}
SAC_PARAMS = {
    "batch_size": 64,
    "buffer_size": 100000,
    "learning_rate": 0.0001,
    "learning_starts": 100,
    "ent_coef": "auto_0.1",
}

########################################################
############## Stock Ticker Setup starts ##############
def _sanitize_ticker_for_yfinance(ticker):
    """Convert tickers like BRK.B -> BRK-B for yfinance compatibility."""
    if not isinstance(ticker, str):
        return ticker
    return ticker.replace(".", "-").upper()


def get_sp500_constituents_from_wikipedia():
    """Fetch the latest S&P 500 constituents from Wikipedia.

    Returns a list of tickers (strings) sanitized for yfinance.
    """
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    except Exception:
        return []
    if not tables:
        return []
    # The first table usually contains the constituents
    df = tables[0]
    symbol_col = None
    for col in df.columns:
        if str(col).strip().lower() in {"symbol", "ticker symbol", "ticker"}:
            symbol_col = col
            break
    if symbol_col is None:
        # Fallback: try first column
        symbol_col = df.columns[0]
    tickers = [
        _sanitize_ticker_for_yfinance(str(t))
        for t in df[symbol_col].dropna().astype(str).tolist()
    ]
    # Deduplicate while keeping order
    seen = set()
    unique = []
    for t in tickers:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    return unique


def get_sp500_top_n_by_marketcap(n=100):
    """Return top n S&P 500 tickers ranked by market cap using yfinance.

    Falls back to an empty list if retrieval fails.
    """
    try:
        constituents = get_sp500_constituents_from_wikipedia()
        if not constituents:
            return []
        try:
            import yfinance as yf
        except Exception:
            return []

        # Batch query using Tickers to reduce overhead
        market_caps = {}
        batch_size = 50
        for i in range(0, len(constituents), batch_size):
            batch = constituents[i : i + batch_size]
            try:
                tickers_obj = yf.Tickers(" ".join(batch))
            except Exception:
                continue
            # tickers_obj.tickers is a dict of {symbol: Ticker}
            for sym, tk in getattr(tickers_obj, "tickers", {}).items():
                cap = None
                # Prefer fast_info when available
                try:
                    fi = getattr(tk, "fast_info", None)
                    if fi is not None:
                        cap = getattr(fi, "market_cap", None)
                        if cap is None and isinstance(fi, dict):
                            cap = fi.get("market_cap")
                except Exception:
                    cap = None
                if cap is None:
                    # Fallback to info dict (slower)
                    try:
                        info = getattr(tk, "info", {}) or {}
                        cap = info.get("marketCap")
                    except Exception:
                        cap = None
                if isinstance(cap, (int, float)) and cap > 0:
                    market_caps[_sanitize_ticker_for_yfinance(sym)] = cap

        if not market_caps:
            return []

        ranked = sorted(market_caps.items(), key=lambda x: x[1], reverse=True)
        top = [sym for sym, _ in ranked[: max(1, int(n))]]
        return top
    except Exception:
        return []

_SP500_100_TICKER_FALLBACK = [
        # Minimal fallback seed; final list will be computed below if possible
        "AAPL", "MSFT", "NVDA", "GOOG", "AMZN", "META", "LLY", "AVGO", "TSLA", "WMT"
]

# Compute dynamic top-100 (best-effort) unless disabled
_dynamic_enabled = True
_computed_top100 = get_sp500_top_n_by_marketcap(100) if _dynamic_enabled else []

# Assign once to avoid constant redefinition warnings in static checkers
SP500_100_TICKER = _computed_top100 if _computed_top100 else _SP500_100_TICKER_FALLBACK

# Backward-compatible alias: top 20 from the ranked SP500_100_TICKER
SP500_20_TICKER = SP500_100_TICKER[:20] if len(SP500_100_TICKER) >= 20 else SP500_100_TICKER


# check https://wrds-www.wharton.upenn.edu/ for U.S. index constituents
# Dow 30 constituents at 2019/01
DOW_30_TICKER = [
    "AAPL",
    "MSFT",
    "JPM",
    "V",
    "RTX",
    "PG",
    "GS",
    "NKE",
    "DIS",
    "AXP",
    "HD",
    "INTC",
    "WMT",
    "IBM",
    "MRK",
    "UNH",
    "KO",
    "CAT",
    "TRV",
    "JNJ",
    "CVX",
    "MCD",
    "VZ",
    "CSCO",
    "XOM",
    "BA",
    "MMM",
    "PFE",
    "WBA",
    "DD",
]

############## Stock Ticker Setup ends ##############
