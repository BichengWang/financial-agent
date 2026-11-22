import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TICKERS = ["AAPL", "MSFT", "NVDA", "GOOG", "AMZN", "META", "LLY", "AVGO", "TSLA", "WMT"]

# Run in a fresh interpreter, so config is first imported after the network is cut.
IMPORT_WITHOUT_NETWORK = """
import json
import socket

import curl_cffi.curl
import pandas

attempts = []


def refuse(name):
    def call(*args, **kwargs):
        attempts.append(name)
        raise OSError(f"network access attempted: {name}")

    return call


socket.socket.connect = refuse("socket.socket.connect")
socket.create_connection = refuse("socket.create_connection")
pandas.read_html = refuse("pandas.read_html")
# yfinance talks to Yahoo through libcurl, which the socket patches cannot see.
curl_cffi.curl.Curl.perform = refuse("curl_cffi")

from financial_agent.trading.config import config

print(
    json.dumps(
        {
            "attempts": attempts,
            "SP500_100_TICKER": config.SP500_100_TICKER,
            "SP500_20_TICKER": config.SP500_20_TICKER,
        }
    )
)
"""


def test_importing_config_makes_no_network_call() -> None:
    done = subprocess.run(
        [sys.executable, "-c", IMPORT_WITHOUT_NETWORK],
        capture_output=True,
        text=True,
        cwd=REPO,
        env={**os.environ, "PYTHONPATH": str(REPO / "src")},
        timeout=60,
    )
    assert done.returncode == 0, done.stderr
    result = json.loads(done.stdout)
    assert result["attempts"] == []
    assert result["SP500_100_TICKER"] == TICKERS
    assert result["SP500_20_TICKER"] == TICKERS
