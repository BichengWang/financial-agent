"""Execution contracts: share quantities, currency prices, and UTC timestamps."""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Protocol
import math

from financial_agent.quant.risk.orders import AccountSnapshot, Order

OrderStatus = Literal[
    "pending", "accepted", "filled", "partially_filled", "canceled", "rejected"
]


class BrokerError(RuntimeError):
    """Execution failed; messages must never contain credentials."""


@dataclass(frozen=True)
class OrderAck:
    client_order_id: str
    broker_order_id: str
    symbol: str
    side: Literal["buy", "sell"]
    qty: float
    status: OrderStatus
    filled_qty: float
    filled_avg_price: float | None
    submitted_at: datetime
    reason: str | None = None


@dataclass(frozen=True)
class Fill:
    client_order_id: str
    symbol: str
    side: Literal["buy", "sell"]
    qty: float
    price: float
    reference_price: float
    commission: float
    session: str


@dataclass(frozen=True)
class LiveAuthorization:
    """Time-bounded runner grant tied to a strategy and its certificate."""

    strategy: str
    params_sha256: str
    certificate_sha256: str
    granted_at: datetime
    expires_at: datetime

    def is_valid(self, now: datetime) -> bool:
        """Require aware times and a nonempty identity, including both hashes."""
        return bool(
            self.strategy
            and all(
                len(h) == 64 and all(c in "0123456789abcdef" for c in h)
                for h in (self.params_sha256, self.certificate_sha256)
            )
            and now.utcoffset() is not None
            and self.granted_at.utcoffset() is not None
            and self.expires_at.utcoffset() is not None
            and self.granted_at <= now < self.expires_at
        )


class Broker(Protocol):
    name: str
    is_live: bool

    def account(self) -> AccountSnapshot: ...

    def submit(self, order: Order) -> OrderAck: ...

    def open_orders(self) -> list[OrderAck]: ...

    def cancel_all(self) -> int: ...


def validate_order(order: Order) -> None:
    """Reject invalid share counts before any broker request or state mutation."""
    if (
        not order.symbol
        or not order.client_order_id
        or order.side not in ("buy", "sell")
        or not math.isfinite(order.qty)
        or order.qty <= 0
        or (
            order.limit_price is not None
            and (not math.isfinite(order.limit_price) or order.limit_price <= 0)
        )
    ):
        raise BrokerError("invalid order identity, side, quantity, or limit price")
