"""Trade dated research forecasts as long-only horizon-return Kelly weights."""

from collections import Counter
from dataclasses import dataclass
import datetime as dt
from functools import lru_cache
import math
from pathlib import Path
from typing import Any, cast

import pandas as pd  # type: ignore[import-untyped]

from financial_agent.harness.helpers import load_helper
from financial_agent.harness.policy import load_policy
from ..data import MarketData
from .base import validate_weights


@dataclass(frozen=True)
class _SinglePackage:
    """Restrict the canonical loader to one file to isolate corrupt packages."""

    path: Path

    def glob(self, pattern: str) -> tuple[Path, ...]:
        return (self.path,)


@dataclass(frozen=True)
class _Forecast:
    run_date: dt.date
    target_date: dt.date
    model: str
    ticker: str
    mu: float
    sigma: float
    sleeve: str | None
    type: str


def _number(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("missing_or_invalid_number")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("nonfinite_number")
    return result


def _date(value: Any) -> dt.date:
    if not isinstance(value, str):
        raise ValueError("missing_or_invalid_date")
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("missing_or_invalid_date") from exc


@lru_cache(maxsize=None)
def _load(output_dir: str) -> tuple[tuple[_Forecast, ...], int, dict[str, int]]:
    ledger = load_helper("settlement_ledger")
    forecasts: list[_Forecast] = []
    skipped: Counter[str] = Counter()
    packages = 0
    for path in sorted(Path(output_dir).glob("*/15_predictions.json")):
        try:
            package = ledger.load_packages(_SinglePackage(path))[0]
        except (OSError, ValueError, TypeError, IndexError):
            skipped["malformed_package"] += 1
            continue
        packages += 1
        records = package.get("predictions")
        if not isinstance(records, list):
            skipped["invalid_predictions_list"] += 1
            continue
        for record in records:
            try:
                if not isinstance(record, dict):
                    raise ValueError("invalid_record")
                run = _date(record.get("run_date") or package.get("run_date"))
                if package.get("run_date") is not None:
                    run = max(run, _date(package["run_date"]))
                target = _date(record.get("target_date"))
                if target <= run:
                    raise ValueError("nonpositive_horizon")
                model = record.get("model") or package.get("model")
                ticker = record.get("ticker")
                kind = record.get("type")
                if not all(isinstance(v, str) and v for v in (model, ticker, kind)):
                    raise ValueError("missing_identity_or_type")
                mu, sigma = _number(record.get("mu")), _number(record.get("sigma"))
                if sigma <= 0:
                    raise ValueError("nonpositive_sigma")
                forecasts.append(
                    _Forecast(
                        run,
                        target,
                        cast(str, model),
                        cast(str, ticker),
                        mu,
                        sigma,
                        record.get("sleeve"),
                        cast(str, kind),
                    )
                )
            except ValueError as exc:
                skipped[str(exc)] += 1
    return tuple(forecasts), packages, dict(skipped)


class ResearchForecastStrategy:
    """Use only run_date < decision <= target_date, with horizon decimal returns.

    Most recent active vintage wins; ties average mu and sigma equally across
    models (within-model means).
    Package dates bound row dates from below. Status/confidence are metadata,
    never a hindsight filter; types must be explicit (no legacy type invention).
    The default cap reads equity policy risk.max_single_name_weight. Packages
    are a process-local snapshot cached by resolved output directory; restart
    the process to ingest newly published packages.
    """

    name = "research_forecast"
    warmup = 1

    def __init__(
        self,
        output_dir: str,
        *,
        models: tuple[str, ...] | None = None,
        kelly_fraction: float = 0.25,
        max_weight: float = load_policy().num("risk.max_single_name_weight"),
        min_mu: float = 0.0,
        sleeves: tuple[str, ...] | None = None,
        types: tuple[str, ...] = ("EQUITY_ALPHA",),
    ) -> None:
        if not isinstance(output_dir, str) or not output_dir:
            raise ValueError("output_dir must be a nonempty string")
        kelly_fraction, max_weight, min_mu = map(
            _number, (kelly_fraction, max_weight, min_mu)
        )
        if not 0 <= kelly_fraction <= 1 or not 0 <= max_weight <= 1:
            raise ValueError("kelly_fraction and max_weight must be in [0, 1]")
        for values in (models, sleeves, types):
            if values is not None and (
                not isinstance(values, (tuple, list))
                or any(not isinstance(v, str) or not v for v in values)
            ):
                raise ValueError("filters must contain nonempty strings")
        self.output_dir = output_dir
        self.models = tuple(models) if models is not None else None
        self.sleeves = tuple(sleeves) if sleeves is not None else None
        self.types = tuple(types)
        self.kelly_fraction = kelly_fraction
        self.max_weight = max_weight
        self.min_mu = min_mu
        parsed, self.package_count, reasons = _load(str(Path(output_dir).resolve()))
        self.skipped_reasons = Counter(reasons)
        selected = []
        for forecast in parsed:
            reason = (
                "model_filter"
                if self.models is not None and forecast.model not in self.models
                else (
                    "sleeve_filter"
                    if self.sleeves is not None and forecast.sleeve not in self.sleeves
                    else "type_filter" if forecast.type not in self.types else ""
                )
            )
            if reason:
                self.skipped_reasons[reason] += 1
            else:
                selected.append(forecast)
        self.forecasts = tuple(selected)
        self.forecast_count = len(self.forecasts)

    def params(self) -> dict[str, Any]:
        """Return JSON-compatible constructor parameters, preserving output_dir."""
        return {
            key: getattr(self, key)
            for key in (
                "output_dir",
                "models",
                "kelly_fraction",
                "max_weight",
                "min_mu",
                "sleeves",
                "types",
            )
        }

    def target_weights(self, data: MarketData) -> pd.Series:
        """Clip per-name horizon Kelly, then scale gross exposure to at most one."""
        weights = pd.Series(0.0, index=data.symbols)
        if not len(data.sessions):
            return validate_weights(self, data, weights)
        decision = data.sessions[-1].date()
        active: dict[str, list[_Forecast]] = {}
        for forecast in self.forecasts:
            if forecast.ticker in data.symbols and (
                forecast.run_date < decision <= forecast.target_date
            ):
                prior = active.get(forecast.ticker, [])
                if not prior or forecast.run_date > prior[0].run_date:
                    active[forecast.ticker] = [forecast]
                elif forecast.run_date == prior[0].run_date:
                    prior.append(forecast)
        for ticker, forecasts in active.items():
            by_model: dict[str, list[_Forecast]] = {}
            for forecast in forecasts:
                by_model.setdefault(forecast.model, []).append(forecast)
            mu = sum(
                sum(f.mu / len(rows) for f in rows) / len(by_model)
                for rows in by_model.values()
            )
            sigma = sum(
                sum(f.sigma / len(rows) for f in rows) / len(by_model)
                for rows in by_model.values()
            )
            if mu > self.min_mu:
                # Divide successively to avoid underflow in sigma squared.
                raw = self.kelly_fraction * mu / sigma / sigma
                weights[ticker] = min(self.max_weight, max(0.0, raw))
        if weights.sum() > 1:
            weights /= weights.sum()
        return validate_weights(self, data, weights)
