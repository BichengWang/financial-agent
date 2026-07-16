#!/usr/bin/env python3
"""Shared helpers for the SHADOW diagnostic scripts.

Used by `fundamental_diagnostics.py` and `sentiment_diagnostics.py`: fetch
plumbing (SSL context, JSON fetch, ticker-list parsing) and the
cross-sectional factor-scoring pipeline that turns per-name raw signals into
a family z-score, per rules.md's Family Aggregation rule -- convert
sourceable metrics into cross-sectional z-scores after winsorizing extreme
observations at the 5th and 95th percentiles, then equal-weight the
available signal z-scores.
"""

from __future__ import annotations

import datetime as dt
import json
import ssl
import urllib.request
from pathlib import Path
from typing import Any

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


def fetch_json(url: str, headers: dict[str, str], timeout: int = 20) -> Any:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout, context=https_context()) as resp:
        result: Any = json.loads(resp.read())
    return result


def read_tickers(tickers: list[str], tickers_file: Path | None) -> list[str]:
    """Merge --tickers and --tickers-file into one de-duplicated, order-
    preserving, upper-cased ticker list."""
    out_tickers = list(tickers)
    if tickers_file:
        text = tickers_file.read_text()
        out_tickers.extend(
            t.strip().upper() for t in text.replace(",", "\n").splitlines() if t.strip()
        )
    seen = set()
    deduped = []
    for t in out_tickers:
        if t not in seen:
            seen.add(t)
            deduped.append(t)
    return deduped


# ---------------------------------------------------------------------------
# Cross-sectional z-scoring
# ---------------------------------------------------------------------------


def winsorize(
    values: list[float], lo_pct: float = 0.05, hi_pct: float = 0.95
) -> list[float]:
    if len(values) < 2:
        return values
    ordered = sorted(values)
    lo = ordered[max(0, int(len(ordered) * lo_pct))]
    hi = ordered[min(len(ordered) - 1, int(len(ordered) * hi_pct))]
    return [min(max(v, lo), hi) for v in values]


def zscore_cross_sectionally(
    per_ticker_values: dict[str, dict[str, float | None]],
    signal_names: tuple[str, ...],
    lower_is_better: set[str],
) -> dict[str, dict[str, float | None]]:
    """z-scores each named signal across the tickers that carry it; polarity
    is normalized per `lower_is_better` so every returned z-score is
    "higher is better", regardless of the raw signal's own polarity.
    """
    z: dict[str, dict[str, float | None]] = {t: {} for t in per_ticker_values}
    for signal in signal_names:
        tickers = [t for t, v in per_ticker_values.items() if v.get(signal) is not None]
        if len(tickers) < 2:
            for t in per_ticker_values:
                z[t][signal] = None
            continue
        raw = [per_ticker_values[t][signal] for t in tickers]  # type: ignore[misc]
        winsorized = winsorize(raw)  # type: ignore[arg-type]
        mean = sum(winsorized) / len(winsorized)
        variance = sum((v - mean) ** 2 for v in winsorized) / len(winsorized)
        stdev = variance**0.5
        for t in per_ticker_values:
            if t not in tickers:
                z[t][signal] = None
                continue
            raw_v: float = per_ticker_values[t][signal]  # type: ignore[assignment]
            wv = min(max(raw_v, min(winsorized)), max(winsorized))
            score = 0.0 if stdev == 0 else (wv - mean) / stdev
            z[t][signal] = -score if signal in lower_is_better else score
    return z


def composite_z(
    z_signals: dict[str, float | None], min_signals: int = 2
) -> tuple[float | None, int]:
    """Equal-weight average of available signal z-scores, per rules.md's
    "equal-weight available sourceable metric z-scores" rule. `composite` is
    None when fewer than `min_signals` are available (mirrors rules.md's
    "fewer than two sourceable metrics" -> family UNAVAILABLE rule)."""
    available = [v for v in z_signals.values() if v is not None]
    if len(available) < min_signals:
        return None, len(available)
    return sum(available) / len(available), len(available)


# ---------------------------------------------------------------------------
# SHADOW output envelope (shared shape between both diagnostic scripts)
# ---------------------------------------------------------------------------


def build_shadow_output(
    tickers: list[str],
    per_ticker_values: dict[str, dict[str, float | None]],
    per_ticker_lineage: dict[str, Any],
    fetch_failures: dict[str, str],
    signal_names: tuple[str, ...],
    lower_is_better: set[str],
    composite_key: str,
    family_label: str,
    plan_path: str,
) -> dict[str, Any]:
    """Assemble the standard SHADOW diagnostic manifest: z-score every
    signal, compute the family composite under `composite_key`, and wrap it
    all in the disclosure envelope both scripts publish. Every record and
    the envelope itself carry `"gating_status": "SHADOW"` -- this output is
    never wired into rules.md's Evidence Thresholds or Adj Score.
    """
    z_scores = zscore_cross_sectionally(
        per_ticker_values, signal_names, lower_is_better
    )

    records = {}
    for ticker in per_ticker_values:
        composite, n_available = composite_z(z_scores[ticker])
        records[ticker] = {
            "gating_status": "SHADOW",
            "raw_signals": per_ticker_values[ticker],
            "z_signals": z_scores[ticker],
            composite_key: composite,
            "n_signals_available": n_available,
            "sourceable": n_available >= 2,
            "lineage": per_ticker_lineage[ticker],
        }

    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "gating_status": "SHADOW",
        "note": f"Diagnostic only per {plan_path} Phase 1 -- {family_label} is NOT "
        "wired into the 3-of-4 evidence-threshold gate or Adj Score until a "
        "future run explicitly promotes it per the Evolution Policy "
        "(HUMAN_REVIEW + logged shadow run).",
        "universe_sourceable_pct": (
            round(100 * len(per_ticker_values) / len(tickers), 1) if tickers else 0.0
        ),
        "fetch_failures": fetch_failures,
        "records": records,
    }
