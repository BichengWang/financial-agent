"""Close decisions, delayed bar fills and long-only cash-constrained accounting."""

from collections.abc import Iterable
import math
from typing import Any
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from ..data import MarketData
from ..portfolio import rebalance_deltas
from ..strategies.base import Strategy, validate_weights
from .config import BacktestConfig
from .result import BacktestResult

TRADE_COLUMNS = [
    "decision_session",
    "fill_session",
    "symbol",
    "side",
    "shares",
    "reference_price",
    "fill_price",
    "notional",
    "commission",
    "slippage_cost",
]
SKIP_COLUMNS = ["decision_session", "fill_session", "symbol", "reason"]


def _decision_indices(
    data: MarketData, strategy: Strategy, config: BacktestConfig
) -> set[int]:
    sessions = data.sessions
    candidates: Iterable[int]
    if config.rebalance == "daily":
        candidates = range(len(sessions))
    else:
        groups = (
            [(s.isocalendar().year, s.isocalendar().week) for s in sessions]
            if config.rebalance == "weekly"
            else [(s.year, s.month) for s in sessions]
        )
        candidates = [
            i
            for i in range(len(sessions))
            if i == len(sessions) - 1 or groups[i] != groups[i + 1]
        ]
    return {
        i
        for i in candidates
        if i + 1 >= strategy.warmup
        and (config.start is None or sessions[i] >= config.start)
    }


def run_backtest(
    strategy: Strategy, data: MarketData, config: BacktestConfig
) -> BacktestResult:
    """Run next-bar execution; positions/cash persist and cash earns zero.

    Strategies receive independent inclusive history copies. Pending sells are
    capped at actual holdings. Missing reference prices are recorded and skipped.
    Closing marks carry only previously observed valid closes forward.
    """
    if (
        not isinstance(strategy.warmup, int)
        or isinstance(strategy.warmup, bool)
        or strategy.warmup < 1
    ):
        raise ValueError("strategy warmup must be a positive integer")
    sessions = data.sessions
    symbols = data.symbols
    decisions = _decision_indices(data, strategy, config)
    closes = data.close.to_numpy(dtype=float)
    references = (
        data.open if config.execution == "next_open" else data.close
    ).to_numpy(dtype=float)
    positions = np.zeros(len(symbols))
    marks = np.zeros(len(symbols))
    cash = config.initial_cash
    navs = np.zeros(len(sessions))
    daily_costs = np.zeros(len(sessions))
    turnovers = np.zeros(len(sessions))
    weight_rows = np.zeros((len(sessions), len(symbols)))
    pending: dict[int, tuple[pd.Timestamp, dict[str, float]]] = {}
    trades: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    lookup = {s: i for i, s in enumerate(symbols)}
    for i, session in enumerate(sessions):
        traded = 0.0
        if i in pending:
            decision, deltas = pending.pop(i)
            buys: list[tuple[str, float, float, float]] = []
            for symbol, delta in sorted(
                deltas.items(), key=lambda item: (item[1] > 0, item[0])
            ):
                j = lookup[symbol]
                reference = references[i, j]
                if not np.isfinite(reference) or reference <= 0:
                    skipped.append(
                        dict(
                            decision_session=decision,
                            fill_session=session,
                            symbol=symbol,
                            reason="missing_or_invalid_reference_price",
                        )
                    )
                    continue
                side = "buy" if delta > 0 else "sell"
                price = config.costs.fill_price(side, reference)
                if delta > 0:
                    buys.append((symbol, delta, reference, price))
                    continue
                shares = min(-delta, positions[j])
                commission = config.costs.commission(shares, price)
                if shares == 0 or shares * price - commission < -cash:
                    continue
                cash += shares * price - commission
                positions[j] -= shares
                slip = shares * abs(price - reference)
                daily_costs[i] += commission + slip
                traded += shares * price
                trades.append(
                    dict(
                        decision_session=decision,
                        fill_session=session,
                        symbol=symbol,
                        side=side,
                        shares=shares,
                        reference_price=reference,
                        fill_price=price,
                        notional=shares * price,
                        commission=commission,
                        slippage_cost=slip,
                    )
                )

            def quantities(factor: float) -> list[float]:
                return [
                    (
                        qty * factor
                        if config.fractional_shares
                        else float(math.floor(qty * factor))
                    )
                    for _, qty, _, _ in buys
                ]

            def required(qtys: list[float]) -> float:
                return sum(
                    qty * price + config.costs.commission(qty, price)
                    for qty, (_, _, _, price) in zip(qtys, buys)
                )

            qtys = quantities(1.0)
            if required(qtys) > cash:
                low, high = 0.0, 1.0
                for _ in range(60):
                    mid = (low + high) / 2
                    if required(quantities(mid)) <= cash:
                        low = mid
                    else:
                        high = mid
                qtys = quantities(low)
            for shares, (symbol, _, reference, price) in zip(qtys, buys):
                if shares == 0:
                    continue
                # Guard sequential float subtraction as well as aggregate affordability.
                while (
                    shares > 0
                    and shares * price + config.costs.commission(shares, price) > cash
                ):
                    shares = (
                        math.nextafter(shares, 0.0)
                        if config.fractional_shares
                        else shares - 1
                    )
                if shares <= 0:
                    continue
                commission = config.costs.commission(shares, price)
                cash -= shares * price + commission
                positions[lookup[symbol]] += shares
                slip = shares * abs(price - reference)
                daily_costs[i] += commission + slip
                traded += shares * price
                trades.append(
                    dict(
                        decision_session=decision,
                        fill_session=session,
                        symbol=symbol,
                        side="buy",
                        shares=shares,
                        reference_price=reference,
                        fill_price=price,
                        notional=shares * price,
                        commission=commission,
                        slippage_cost=slip,
                    )
                )
        valid = np.isfinite(closes[i]) & (closes[i] > 0)
        marks[valid] = closes[i, valid]
        nav = cash + float(positions @ marks)
        if nav <= 0:
            raise ValueError(f"nonpositive portfolio NAV on {session}")
        navs[i] = nav
        weight_rows[i] = positions * marks / nav
        turnovers[i] = traded / nav
        if i in decisions:
            history = data.upto(session)
            targets = validate_weights(
                strategy, history, strategy.target_weights(history)
            )
            deltas = rebalance_deltas(
                targets.to_dict(),
                dict(zip(symbols, positions)),
                dict(zip(symbols, closes[i])),
                nav,
                drift_threshold=config.drift_threshold,
                fractional=config.fractional_shares,
                min_trade_notional=config.min_trade_notional,
            )
            fill = i + 1 + config.extra_delay
            if fill < len(sessions):
                pending[fill] = (session, deltas)
    equity = pd.Series(navs, index=sessions, name="equity")
    returns = equity.pct_change(fill_method=None)
    if len(returns):
        returns.iloc[0] = equity.iloc[0] / config.initial_cash - 1
    return BacktestResult(
        equity=equity,
        returns=returns.rename("returns"),
        weights=pd.DataFrame(weight_rows, index=sessions, columns=symbols),
        trades=pd.DataFrame(trades, columns=TRADE_COLUMNS),
        costs=pd.Series(daily_costs, index=sessions, name="costs"),
        turnover=pd.Series(turnovers, index=sessions, name="turnover"),
        strategy_name=strategy.name,
        params=strategy.params(),
        data_fingerprint=data.fingerprint(),
        config=config,
        skipped_trades=pd.DataFrame(skipped, columns=SKIP_COLUMNS),
    )
