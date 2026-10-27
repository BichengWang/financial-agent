"""Argparse operator CLI; research tools share the existing quant engines."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from datetime import date, datetime
import json
from pathlib import Path
import sys
import tempfile
from typing import Any, NoReturn

from financial_agent.harness.market_calendar import session
from .backtest import BacktestConfig, run_backtest
from .data import MarketData, check_quality, synthetic_market
from .data.providers import write_csv
from .runner import (
    ConfigError,
    TradingConfig,
    render_markdown,
    render_status,
    run_session,
    status_summary,
)
from .runner.report import json_value
from .runner.session import EXCHANGE_TZ, session_lock
from .execution import Journal
from .risk import KillSwitch
from .strategies import build_strategy
from .validation import PromotionPolicy, evaluate_promotion, write_certificate

ETF_UNIVERSE = (
    "SPY",
    "QQQ",
    "IWM",
    "EFA",
    "EEM",
    "TLT",
    "IEF",
    "LQD",
    "GLD",
    "DBC",
    "VNQ",
)


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> NoReturn:
        """Usage errors return 1, reserving 2 for a halted trading session."""
        raise ConfigError(message)


def build_parser() -> argparse.ArgumentParser:
    """Expose research, explicit operator controls, and paper-only MCP."""
    parser = Parser(prog="fa-quant")
    sub = parser.add_subparsers(dest="command", required=True)
    data = sub.add_parser(
        "data", help="Fetch or check adjusted market data"
    ).add_subparsers(dest="action", required=True)
    for action in ("fetch", "check"):
        item = data.add_parser(
            action,
            help={
                "fetch": "Fetch and optionally export bars",
                "check": "Check bar quality and freshness",
            }[action],
        )
        item.add_argument(
            "--config",
            type=Path,
            required=True,
            help="Trading TOML; relative paths resolve from its directory",
        )
        item.add_argument(
            "--end",
            type=date.fromisoformat,
            default=date.today(),
            help="Inclusive final data session (YYYY-MM-DD)",
        )
        item.add_argument(
            "--expected-last-session",
            type=date.fromisoformat,
            help="Required last close for freshness (YYYY-MM-DD)",
        )
        item.add_argument(
            "--output-dir", type=Path, help="Export per-symbol CSV bars here"
        )
        item.add_argument(
            "--json", action="store_true", help="Emit machine-readable JSON"
        )
    for command in ("backtest", "validate", "certify"):
        item = sub.add_parser(
            command,
            help={
                "backtest": "Simulate net portfolio returns",
                "validate": "Evaluate statistical promotion gates",
                "certify": "Save a hashed validation certificate",
                "kill": "Engage the persistent trading stop",
                "unkill": "Release a stop with operator justification",
            }[command],
        )
        item.add_argument(
            "--config",
            type=Path,
            help="Trading TOML; relative paths resolve from its directory",
        )
        item.add_argument(
            "--strategy",
            default="trend_vol_target",
            help="Registered strategy name (without --config)",
        )
        item.add_argument("--params", default="{}", help="JSON parameter object")
        item.add_argument(
            "--universe",
            nargs="+",
            default=list(ETF_UNIVERSE),
            help="Ordered ETF symbols (without --config)",
        )
        item.add_argument(
            "--provider",
            choices=("csv", "yahoo"),
            default="yahoo",
            help="Market data source (without --config)",
        )
        item.add_argument(
            "--csv-dir", type=Path, help="Directory containing one SYMBOL.csv per asset"
        )
        item.add_argument(
            "--cache-dir",
            type=Path,
            default=Path(".quant-cache"),
            help="Local adjusted-bar cache (without --config)",
        )
        item.add_argument(
            "--start",
            type=date.fromisoformat,
            default=date(2006, 3, 1),
            help="Inclusive first data session (YYYY-MM-DD)",
        )
        item.add_argument(
            "--end",
            type=date.fromisoformat,
            default=date.today(),
            help="Inclusive final data session (YYYY-MM-DD)",
        )
        item.add_argument(
            "--json", action="store_true", help="Emit machine-readable JSON"
        )
        if command != "backtest":
            item.add_argument("--grid", help="JSON array of parameter objects")
            item.add_argument(
                "--policy",
                type=Path,
                help="TOML promotion policy; defaults to packaged thresholds",
            )
        if command == "certify":
            item.add_argument(
                "--output",
                type=Path,
                required=True,
                help="Certificate JSON destination (also saves failed verdicts)",
            )
    run = sub.add_parser("run", help="Run one fail-closed trading session")
    run.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Trading TOML; relative paths resolve from its directory",
    )
    run.add_argument(
        "--today",
        type=date.fromisoformat,
        default=datetime.now(EXCHANGE_TZ).date(),
        help="Trading session date (YYYY-MM-DD; default: current New York date)",
    )
    run.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview orders without submission; still journals observations",
    )
    run.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    status = sub.add_parser("status", help="Read persisted account and journal status")
    status.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Trading TOML; relative paths resolve from its directory",
    )
    status.add_argument(
        "--json", action="store_true", help="Emit machine-readable JSON"
    )
    for command in ("kill", "unkill"):
        item = sub.add_parser(
            command,
            help={
                "backtest": "Simulate net portfolio returns",
                "validate": "Evaluate statistical promotion gates",
                "certify": "Save a hashed validation certificate",
                "kill": "Engage the persistent trading stop",
                "unkill": "Release a stop with operator justification",
            }[command],
        )
        item.add_argument(
            "--config",
            type=Path,
            required=True,
            help="Trading TOML; relative paths resolve from its directory",
        )
        item.add_argument(
            "--reason", required=True, help="Nonempty operator justification"
        )
        if command == "unkill":
            item.add_argument(
                "--operator",
                required=True,
                help="Operator identity recorded with stop release",
            )
    sub.add_parser("mcp", help="Serve research and paper previews over stdio")
    demo = sub.add_parser(
        "demo", help="Run the offline synthetic research-to-paper demo"
    )
    demo.add_argument(
        "--sessions",
        type=int,
        default=25,
        help="Synthetic paper sessions, 1 through 252 (default: 25)",
    )
    demo.add_argument(
        "--state-dir",
        type=Path,
        help="Fresh directory for demo data, journal and reports",
    )
    return parser


def research_inputs(
    args: argparse.Namespace,
) -> tuple[str, dict[str, Any], MarketData, BacktestConfig]:
    """Load one dataset, once; benchmarks may use explicit backtest-only options."""
    if args.config:
        config = TradingConfig.load(args.config)
        return (
            config.strategy_name,
            config.strategy_params,
            config.provider().fetch(config.symbols, config.data_start, args.end),
            config.backtest,
        )
    params = json.loads(args.params)
    if not isinstance(params, dict):
        raise ConfigError("params: expected JSON object")
    from .data import CachedProvider, CsvProvider, YahooProvider

    if args.provider == "csv" and args.csv_dir is None:
        raise ConfigError("csv-dir: required for csv provider")
    provider = CsvProvider(args.csv_dir) if args.provider == "csv" else YahooProvider()
    data = CachedProvider(provider, args.cache_dir).fetch(
        args.universe, args.start, args.end
    )
    return args.strategy, params, data, BacktestConfig()


def parameter_grid(
    value: str | None, config: TradingConfig | None, params: dict[str, Any]
) -> list[dict[str, Any]]:
    """A grid is explicit parameter variants, not a Cartesian-product shorthand."""
    grid = (
        json.loads(value)
        if value is not None
        else (list(config.grid) if config and config.grid else [params])
    )
    if (
        not isinstance(grid, list)
        or not grid
        or any(not isinstance(p, dict) for p in grid)
    ):
        raise ConfigError("grid: expected nonempty JSON array of parameter objects")
    return grid


def _print(value: Any) -> None:
    print(json.dumps(json_value(value), indent=2, allow_nan=False))


def strategy_toml(name: str, params: dict[str, Any]) -> str:
    """Copyable strategy identity; reject parameter types TOML cannot represent."""

    def value(item: Any) -> str:
        if isinstance(item, bool):
            return "true" if item else "false"
        if isinstance(item, (str, int, float)):
            return json.dumps(item, ensure_ascii=False, allow_nan=False)
        if isinstance(item, (list, tuple)):
            return "[" + ", ".join(value(v) for v in item) + "]"
        if isinstance(item, dict):
            return (
                "{ "
                + ", ".join(
                    f"{json.dumps(str(k))} = {value(v)}" for k, v in item.items()
                )
                + " }"
            )
        raise ConfigError(
            "strategy.params: selected value is not representable in TOML"
        )

    lines = ["[strategy]", f"name = {value(name)}", "", "[strategy.params]"]
    lines.extend(f"{json.dumps(key)} = {value(item)}" for key, item in params.items())
    return "\n".join(lines)


SYNTHETIC_NOTICE = (
    "SYNTHETIC DATA with a planted trend: these numbers demonstrate the pipeline, "
    "not market performance."
)


def _demo(state_dir: Path | None, count: int) -> int:
    """Generate offline evidence under the real policy; never fabricate a pass."""
    if count < 1 or count > 252:
        raise ConfigError("sessions: must be between 1 and 252")
    root = (state_dir or Path(tempfile.mkdtemp(prefix="fa-quant-demo-"))).resolve()
    root.mkdir(parents=True, exist_ok=True)
    if (root / "journal.jsonl").exists():
        raise ConfigError("state-dir: demo requires a fresh directory")
    print(SYNTHETIC_NOTICE, flush=True)
    # A mild planted edge illustrates the gate under the production paper settings.
    data = synthetic_market(
        ETF_UNIVERSE,
        4500 + count,
        seed=1,
        annual_drift=0.12,
        annual_vol=0.18,
        correlation=0.1,
    )
    trading = [s for s in data.sessions if session(s.date()).trading_day]
    data = MarketData(
        **{
            name: getattr(data, name).loc[trading]
            for name in ("open", "high", "low", "close", "volume")
        },
        adjusted=True,
        source="synthetic",
    )
    write_csv(data, root / "csv")
    config_path = root / "demo.toml"
    config_path.write_text(
        'mode = "paper"\nstate_dir = "."\n'
        '[strategy]\nname = "trend_vol_target"\n'
        "[universe]\nsymbols = " + json.dumps(ETF_UNIVERSE) + "\n"
        '[data]\nprovider = "csv"\ncsv_dir = "csv"\n'
        'cache_dir = "cache"\nstart = "2005-01-03"\n'
        "[backtest]\ninitial_cash = 100000.0\ncash_buffer = 0.02\n"
        'rebalance = "weekly"\ndrift_threshold = 0.02\n'
        '[broker]\nkind = "paper"\ninitial_cash = 100000.0\n'
    )
    config = TradingConfig.load(config_path)
    history = data.upto(data.sessions[-count - 1])
    strategy = build_strategy(config.strategy_name, config.strategy_params)
    result = run_backtest(strategy, history, config.backtest)
    print("Offline backtest:")
    _print(result.summary())
    promotion = evaluate_promotion(
        strategy.name,
        [{**strategy.params(), "target_vol": v} for v in (0.08, 0.12)],
        history,
        config.backtest,
        PromotionPolicy.load(),
    )
    cert_path = write_certificate(promotion, root / "certificate.json")
    print(f"Validation passed: {promotion.passed}; certificate: {cert_path}")
    for check in promotion.checks:
        print(check.detail)
    for stamp in data.sessions[-count:]:
        report = run_session(config, today=stamp.date())
        print(
            f"{report.session}: {report.status}; orders={len(report.orders)}; "
            f"fills={len(report.fills)}"
        )
        if report.status == "HALTED":
            print("; ".join(report.reasons))
            print(SYNTHETIC_NOTICE)
            return 2
    print(f"Config: {config_path}")
    print(render_status(status_summary(config)))
    print(SYNTHETIC_NOTICE)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """0 success, 2 halted/failed safety check, 1 usage or configuration errors."""
    try:
        args = build_parser().parse_args(argv)
        if args.command == "mcp":
            from .mcp import serve

            serve(sys.stdin, sys.stdout)
            return 0
        if args.command == "demo":
            return _demo(args.state_dir, args.sessions)
        if args.command in ("backtest", "validate", "certify"):
            name, params, data, backtest = research_inputs(args)
            quality = check_quality(data)
            if not quality.ok:
                _print(quality)
                return 2
            if args.command == "backtest":
                backtest_summary = run_backtest(
                    build_strategy(name, params), data, backtest
                ).summary()
                if args.json:
                    _print(backtest_summary)
                else:
                    print("\n".join(f"{k}: {v}" for k, v in backtest_summary.items()))
                return 0
            config = TradingConfig.load(args.config) if args.config else None
            report = evaluate_promotion(
                name,
                parameter_grid(args.grid, config, params),
                data,
                backtest,
                PromotionPolicy.load(args.policy),
            )
            if args.command == "certify":
                write_certificate(report, args.output)
            if args.json:
                _print(report)
            else:
                print(f"Passed: {report.passed}")
                print("\n".join(c.detail for c in report.checks))
                diagnostics = json_value(report.diagnostics)
                if len(report.grid) == 1:
                    for key in ("pbo", "degradation_slope"):
                        diagnostics[key] = "n/a: single pre-registered variant"
                print(f"Diagnostics: {diagnostics}")
                if args.command == "certify":
                    print("Selected strategy parameters (copy into your config):")
                    print(strategy_toml(report.strategy, report.selected_params))
            return 0 if report.passed else 2
        config = TradingConfig.load(args.config)
        if args.command == "data":
            data = config.provider().fetch(config.symbols, config.data_start, args.end)
            quality = check_quality(
                data, expected_last_session=args.expected_last_session
            )
            if args.action == "fetch" and args.output_dir:
                write_csv(data, args.output_dir)
            _print(
                {
                    "symbols": data.symbols,
                    "sessions": len(data.sessions),
                    "fingerprint": data.fingerprint(),
                    "quality": json_value(quality),
                }
            )
            return 0 if quality.ok else 2
        if args.command == "run":
            session_report = run_session(config, today=args.today, dry_run=args.dry_run)
            if args.json:
                _print(session_report.to_dict())
            else:
                print(render_markdown(session_report))
            return 2 if session_report.status == "HALTED" else 0
        if args.command == "status":
            summary = status_summary(config)
            if args.json:
                _print(summary)
            else:
                print(render_status(summary))
            return 0 if summary["journal"]["ok"] else 2
        if args.command in ("kill", "unkill"):
            with session_lock(config.state_dir):
                journal = Journal(config.state_dir / "journal.jsonl")
                kill = KillSwitch(config.state_dir)
                if args.command == "kill":
                    kill.engage(args.reason, source="operator")
                    if not journal.verify().ok:
                        print(
                            "Stop engaged; journal verification failed", file=sys.stderr
                        )
                        return 2
                    journal.append("kill", {"reason": args.reason})
                else:
                    if not journal.verify().ok:
                        raise ConfigError("journal: verification failed")
                    # The justification must be durable before the stop is removed.
                    if not args.reason.strip() or not args.operator.strip():
                        raise ConfigError("reason and operator: must be nonempty")
                    journal.append(
                        "unkill_intent",
                        {"reason": args.reason, "operator": args.operator},
                    )
                    journal.append(
                        "unkill", kill.release(args.reason, operator=args.operator)
                    )
            return 0
        raise ConfigError("unknown command")
    except (ValueError, TypeError, KeyError, OSError, RuntimeError) as exc:
        # Do not expose raw transport/provider exceptions or secret values.
        message = str(exc) if isinstance(exc, ConfigError) else type(exc).__name__
        print(f"error: {message}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
