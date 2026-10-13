"""Validated TOML settings; paths are relative to the configuration file."""

from collections.abc import Mapping
from dataclasses import dataclass, field, fields
from datetime import date
from pathlib import Path
import tomllib
from typing import Any, Literal

from ..backtest import BacktestConfig, CostModel
from ..data import BarProvider, CachedProvider, CsvProvider, YahooProvider
from ..data.providers import validate_request
from ..risk import RiskLimits
from ..strategies import build_strategy


class ConfigError(ValueError):
    """A named configuration key is invalid."""


def _table(raw: Mapping[str, Any], key: str, allowed: set[str]) -> dict[str, Any]:
    value = raw.get(key, {})
    if not isinstance(value, dict):
        raise ConfigError(f"{key}: expected a table")
    unknown = value.keys() - allowed
    if unknown:
        raise ConfigError(f"{key}: unknown keys {sorted(unknown)}")
    return dict(value)


@dataclass(frozen=True)
class TradingConfig:
    """Paper by default; strategy identity is normalized before certification."""

    strategy_name: str
    strategy_params: dict[str, Any]
    symbols: tuple[str, ...]
    data_provider: Literal["yahoo", "csv"]
    data_start: date
    csv_dir: Path | None
    cache_dir: Path
    state_dir: Path
    backtest: BacktestConfig
    broker_kind: Literal["paper", "alpaca"] = "paper"
    initial_cash: float = 100_000.0
    mode: Literal["paper", "live"] = "paper"
    risk: RiskLimits = field(default_factory=RiskLimits.load)
    certificate_path: Path | None = None
    paper_journal_path: Path | None = None
    grid: tuple[dict[str, Any], ...] = ()

    def __post_init__(self) -> None:
        try:
            RiskLimits.load().tighten(
                {f.name: getattr(self.risk, f.name) for f in fields(RiskLimits)}
            )
        except (ValueError, TypeError) as exc:
            raise ConfigError(f"risk: {exc}") from None
        if self.mode not in ("paper", "live"):
            raise ConfigError("mode: expected paper or live")
        if self.broker_kind not in ("paper", "alpaca"):
            raise ConfigError("broker.kind: expected paper or alpaca")
        if self.mode == "live" and self.broker_kind != "alpaca":
            raise ConfigError("broker.kind: live mode requires alpaca")
        if self.data_provider not in ("yahoo", "csv"):
            raise ConfigError("data.provider: expected yahoo or csv")
        if self.data_provider == "csv" and self.csv_dir is None:
            raise ConfigError("data.csv_dir: required for csv provider")
        try:
            validate_request(self.symbols, self.data_start, date.max)
        except ValueError as exc:
            raise ConfigError(f"universe.symbols: {exc}") from None
        if self.backtest.cash_buffer <= self.risk.min_cash_pct:
            raise ConfigError("backtest.cash_buffer: must exceed risk.min_cash_pct")
        if self.backtest.execution != "next_open" or self.backtest.extra_delay:
            raise ConfigError("backtest.execution: runner requires next_open, no delay")
        if self.backtest.fractional_shares:
            raise ConfigError("backtest.fractional_shares: OPG requires whole shares")
        try:
            BacktestConfig(initial_cash=self.initial_cash)
            strategy = build_strategy(self.strategy_name, self.strategy_params)
        except (ValueError, TypeError, KeyError) as exc:
            raise ConfigError(
                f"strategy.params or broker.initial_cash: {exc}"
            ) from None
        object.__setattr__(self, "strategy_params", strategy.params())
        # The configured universe is an implicit allowlist even if policy is empty.
        allowed = self.risk.allowed_symbols or self.symbols
        if not set(allowed).issubset(self.symbols):
            raise ConfigError("risk.allowed_symbols: must be within universe.symbols")
        object.__setattr__(
            self, "risk", self.risk.tighten({"allowed_symbols": allowed})
        )

    @classmethod
    def load(cls, path: str | Path) -> "TradingConfig":
        """Reject unknown keys and risk expansions before touching any broker."""
        source = Path(path).resolve()
        try:
            raw = tomllib.loads(source.read_text())
        except (OSError, ValueError) as exc:
            raise ConfigError(f"config: {exc}") from None
        unknown = raw.keys() - {
            "strategy",
            "universe",
            "data",
            "backtest",
            "broker",
            "mode",
            "state_dir",
            "risk",
            "promotion",
        }
        if unknown:
            raise ConfigError(f"config: unknown keys {sorted(unknown)}")

        def resolve(value: Any, key: str) -> Path:
            if not isinstance(value, str) or not value.strip():
                raise ConfigError(f"{key}: expected a nonempty path")
            return (source.parent / value).resolve()

        strategy = _table(raw, "strategy", {"name", "params"})
        universe = _table(raw, "universe", {"symbols"})
        data = _table(raw, "data", {"provider", "csv_dir", "cache_dir", "start"})
        backtest = _table(raw, "backtest", {f.name for f in fields(BacktestConfig)})
        broker = _table(raw, "broker", {"kind", "initial_cash"})
        promotion = _table(raw, "promotion", {"certificate", "paper_journal", "grid"})
        risk = _table(raw, "risk", {f.name for f in fields(RiskLimits)})
        params = strategy.get("params", {})
        if not isinstance(params, dict):
            raise ConfigError("strategy.params: expected a table")
        symbols = universe.get("symbols", [])
        if not isinstance(symbols, list):
            raise ConfigError("universe.symbols: expected an array")
        grid = promotion.get("grid", [])
        if not isinstance(grid, list) or any(not isinstance(p, dict) for p in grid):
            raise ConfigError("promotion.grid: expected an array of parameter tables")
        if "costs" in backtest:
            costs = _table(backtest, "costs", {f.name for f in fields(CostModel)})
            try:
                backtest["costs"] = CostModel(**costs)
            except (ValueError, TypeError) as exc:
                raise ConfigError(f"backtest.costs: {exc}") from None
        try:
            bt = BacktestConfig(**backtest)
        except (ValueError, TypeError) as exc:
            raise ConfigError(f"backtest: {exc}") from None
        try:
            limits = RiskLimits.load().tighten(risk)
        except (ValueError, TypeError) as exc:
            raise ConfigError(f"risk: {exc}") from None
        try:
            start = date.fromisoformat(str(data.get("start", "2006-03-01")))
        except ValueError:
            raise ConfigError("data.start: expected YYYY-MM-DD") from None
        state = resolve(raw.get("state_dir", "state"), "state_dir")
        return cls(
            strategy.get("name", "trend_vol_target"),
            params,
            tuple(symbols),
            data.get("provider", "yahoo"),
            start,
            resolve(data["csv_dir"], "data.csv_dir") if "csv_dir" in data else None,
            (
                resolve(data["cache_dir"], "data.cache_dir")
                if "cache_dir" in data
                else state / "cache"
            ),
            state,
            bt,
            broker.get("kind", "paper"),
            broker.get("initial_cash", bt.initial_cash),
            raw.get("mode", "paper"),
            limits,
            (
                resolve(promotion["certificate"], "promotion.certificate")
                if "certificate" in promotion
                else None
            ),
            (
                resolve(promotion["paper_journal"], "promotion.paper_journal")
                if "paper_journal" in promotion
                else None
            ),
            tuple(grid),
        )

    def provider(self, inner: BarProvider | None = None) -> CachedProvider:
        """Wrap the configured or injected source in the incremental cache."""
        if inner is None:
            inner = (
                CsvProvider(self.csv_dir)
                if self.data_provider == "csv" and self.csv_dir is not None
                else YahooProvider()
            )
        return CachedProvider(inner, self.cache_dir)
