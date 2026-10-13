"""Compare expected and observed share quantities over their symbol union."""

from collections.abc import Mapping
from dataclasses import dataclass
import math

from financial_agent.quant.risk.orders import AccountSnapshot


@dataclass(frozen=True)
class Break:
    symbol: str
    expected_qty: float
    actual_qty: float


def reconcile(
    expected: Mapping[str, float],
    account: AccountSnapshot,
    *,
    tolerance: float = 1e-6,
) -> list[Break]:
    """Absolute share tolerance; nonfinite observations always constitute breaks."""
    if not math.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and nonnegative")
    result = []
    for symbol in sorted(expected.keys() | account.positions.keys()):
        wanted = expected.get(symbol, 0.0)
        actual = account.positions[symbol].qty if symbol in account.positions else 0.0
        if (
            not (math.isfinite(wanted) and math.isfinite(actual))
            or abs(wanted - actual) > tolerance
        ):
            result.append(Break(symbol, wanted, actual))
    return result
