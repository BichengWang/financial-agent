"""Shared fixtures for the harness spike tests.

Run with: uv run pytest tests/harness  (or PYTHONPATH=src python3 -m pytest)
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))

from financial_agent.harness.policy import Policy, load_policy  # noqa: E402

OUTPUT_DIR = REPO / "agents" / "equity" / "output"
real_data = pytest.mark.skipif(
    not OUTPUT_DIR.exists(), reason="agents/equity/output data not present"
)


@pytest.fixture(scope="session")
def policy() -> Policy:
    return load_policy()


@pytest.fixture
def vlo_record() -> dict[str, Any]:
    """VLO as published in claude-opus-5-2026-09-03/15_predictions.json."""
    return {
        "run_date": "2026-09-03",
        "model": "claude-opus-5",
        "ticker": "VLO",
        "type": "EQUITY_ALPHA",
        "entry_price": 370.69,
        "price_tag": "DELAYED",
        "price_date": "2026-09-03",
        "mu": 0.06,
        "sigma": 0.084355,
        "sigma_source": "REALIZED_VOL_30D",
        "ci70_lo": 360.411,
        "ci70_hi": 425.4518,
        "target_date": "2026-10-01",
        "benchmark": "SPY",
        "benchmark_price": 773.17,
        "adj_score": 0.372719,
        "confidence": "MEDIUM",
        "status": "OPEN",
        "sleeve": "MONITORING",
        "pctl": 100.0,
        "thesis": "Technical/Macro-only composite; monitoring sleeve only.",
        "score_explainability": {
            "fund_z": None,
            "tech_z": 1.41521,
            "sent_z": None,
            "macro_z": 0.275568,
            "composite_z": 0.465898,
            "data_quality_multiplier": 0.8,
            "penalties": 0.0,
            "metrics": {
                "kelly_raw": 8.431961,
                "kelly_025": 2.10799,
                "var95": -0.079186,
                "cvar95": -0.113771,
            },
        },
    }


def market_forecast(ticker: str, entry: float) -> dict[str, Any]:
    mu, sigma = 0.02, 0.033
    return {
        "run_date": "2026-09-03",
        "model": "claude-opus-5",
        "ticker": ticker,
        "type": "MARKET_FORECAST",
        "entry_price": entry,
        "price_tag": "DELAYED",
        "price_date": "2026-09-03",
        "mu": mu,
        "sigma": sigma,
        "sigma_source": "REALIZED_VOL_30D",
        "ci70_lo": entry * (1 + mu - 1.04 * sigma),
        "ci70_hi": entry * (1 + mu + 1.04 * sigma),
        "target_date": "2026-10-01",
        "benchmark": "NONE",
        "benchmark_price": None,
        "adj_score": None,
        "confidence": "MEDIUM",
        "status": "OPEN",
        "thesis": "regime prior",
    }
