"""Fail-closed whole-plan checks at reference prices, before any submission."""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import math
import pandas as pd  # type: ignore[import-untyped]

from .killswitch import KillSwitch
from .limits import RiskLimits
from .orders import AccountSnapshot, Order


@dataclass(frozen=True)
class RiskDecision:
    """A rejected plan always halts with no approved orders."""

    approved: list[Order]
    rejected: list[tuple[Order, str]]
    halt: bool
    reasons: list[str]


def _over(value: float, threshold: float) -> bool:
    return value > threshold and not math.isclose(
        value, threshold, rel_tol=1e-12, abs_tol=1e-12
    )


def check_orders(
    orders: Sequence[Order],
    account: AccountSnapshot,
    prices: Mapping[str, float] | pd.Series,
    limits: RiskLimits,
    *,
    kill_switch: KillSwitch,
) -> RiskDecision:
    """Check currency notionals and equity fractions; never partially execute."""
    orders = list(orders)
    prices = dict(prices)
    reasons: list[str] = []
    per_order: dict[int, list[str]] = {}

    def reject(
        name: str, value: object, threshold: object, index: int | None = None
    ) -> None:
        reason = f"{name} value={value} threshold={threshold}"
        if reason not in reasons:
            reasons.append(reason)
        if index is not None:
            per_order.setdefault(index, []).append(reason)

    if kill_switch.engaged():
        reject("kill_switch", f"engaged ({kill_switch.reason()})", "released")
    if len(orders) > limits.max_orders:
        reject("max_orders", len(orders), limits.max_orders)
    valid_account = math.isfinite(account.equity) and account.equity > 0
    if not valid_account:
        reject("equity", account.equity, ">0 finite")
    if not math.isfinite(account.cash):
        reject("cash", account.cash, "finite")
        valid_account = False
    holdings = {s: p.qty for s, p in account.positions.items()}
    for symbol, held_position in account.positions.items():
        if not math.isfinite(held_position.qty):
            reject("position_qty", f"{symbol}:{held_position.qty}", "finite")
            valid_account = False
    cash = account.cash
    turnover = 0.0
    sold: dict[str, float] = {}
    for index, order in enumerate(orders):
        if limits.allowed_symbols and order.symbol not in limits.allowed_symbols:
            reject("allowed_symbols", order.symbol, limits.allowed_symbols, index)
        if order.side not in ("buy", "sell"):
            reject("side", order.side, "buy or sell", index)
            continue
        if not math.isfinite(order.qty) or order.qty <= 0:
            reject("qty", order.qty, ">0 finite", index)
            continue
        price = prices.get(order.symbol, float("nan"))
        if not math.isfinite(price) or price <= 0:
            reject("reference_price", f"{order.symbol}:{price}", ">0 finite", index)
            continue
        notional = order.qty * price
        if not math.isfinite(notional):
            reject("order_notional", notional, "finite", index)
            continue
        if valid_account and _over(
            notional, limits.max_order_notional_pct * account.equity
        ):
            reject(
                "max_order_notional_pct",
                notional / account.equity,
                limits.max_order_notional_pct,
                index,
            )
        if order.side == "sell":
            sold[order.symbol] = sold.get(order.symbol, 0.0) + order.qty
            held = account.positions.get(order.symbol)
            held_qty = held.qty if held else 0.0
            if not limits.allow_short and _over(sold[order.symbol], held_qty):
                reject(
                    "allow_short",
                    f"{order.symbol}:sell_qty={sold[order.symbol]}",
                    f"False; held_qty={held_qty}",
                    index,
                )
        sign = 1 if order.side == "buy" else -1
        holdings[order.symbol] = holdings.get(order.symbol, 0.0) + sign * order.qty
        cash -= sign * notional
        turnover += notional

    gross = 0.0
    for symbol, qty in holdings.items():
        price = prices.get(symbol, float("nan"))
        if not math.isfinite(price) or price <= 0:
            reject("reference_price", f"{symbol}:{price}", ">0 finite")
            continue
        position = account.positions.get(symbol)
        if position is not None and position.qty != 0:
            if not math.isfinite(position.market_price) or position.market_price <= 0:
                reject(
                    "price_band_pct",
                    f"{symbol}:market_price={position.market_price}",
                    ">0 finite",
                )
            else:
                band = abs(price / position.market_price - 1)
                if _over(band, limits.price_band_pct):
                    reject("price_band_pct", f"{symbol}:{band}", limits.price_band_pct)
        if valid_account:
            weight = qty * price / account.equity
            gross += abs(weight)
            if not math.isfinite(weight) or _over(abs(weight), limits.max_weight):
                reject("max_weight", f"{symbol}:{weight}", limits.max_weight)
            if not limits.allow_short and weight < 0:
                reject("allow_short", f"{symbol}:weight={weight}", "False; weight>=0")
    if valid_account:
        if _over(gross, limits.max_gross):
            reject("max_gross", gross, limits.max_gross)
        cash_fraction = cash / account.equity
        if not math.isfinite(cash_fraction) or _over(
            limits.min_cash_pct, cash_fraction
        ):
            reject("min_cash_pct", cash_fraction, limits.min_cash_pct)
        if not math.isfinite(turnover) or _over(
            turnover / account.equity, limits.max_turnover_pct
        ):
            reject(
                "max_turnover_pct", turnover / account.equity, limits.max_turnover_pct
            )
    if reasons:
        rejected = [
            (order, "; ".join(per_order.get(i, reasons)))
            for i, order in enumerate(orders)
        ]
        return RiskDecision([], rejected, True, reasons)
    return RiskDecision(orders, [], False, [])
