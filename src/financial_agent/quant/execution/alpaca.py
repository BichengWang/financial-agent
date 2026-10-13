"""Alpaca REST v2 transport, paper by default, with guarded live execution."""

from datetime import datetime, timezone
from typing import Any, cast
import math
import os
import time

import requests  # type: ignore[import-untyped]

from financial_agent.quant.risk.orders import AccountSnapshot, Order, Position
from .broker import (
    BrokerError,
    LiveAuthorization,
    OrderAck,
    OrderStatus,
    validate_order,
)

PAPER_URL = "https://paper-api.alpaca.markets"
LIVE_URL = "https://api.alpaca.markets"


def _timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.utcoffset() is None:
        raise ValueError("timestamp must have timezone")
    return parsed


def _decimal_string(value: float) -> str:
    """Encode positive values in plain decimal with at most nine decimal places."""
    if float(value).is_integer():
        return str(int(value))
    encoded = f"{value:.9f}".rstrip("0").rstrip(".")
    if encoded == "0":
        raise BrokerError(
            "order quantity or price is below supported decimal precision"
        )
    return encoded


class AlpacaBroker:
    """Credentials stay in memory; transport error messages exclude server text."""

    name = "alpaca"

    def __init__(
        self,
        key_id: str,
        secret_key: str,
        *,
        live_authorization: LiveAuthorization | None = None,
        session: Any = None,
        base_url: str | None = None,
        timeout: float = 10.0,
        max_retries: int = 3,
    ) -> None:
        self.base_url = (base_url or PAPER_URL).rstrip("/")
        if self.base_url not in (PAPER_URL, LIVE_URL):
            raise BrokerError("unsupported broker endpoint")
        self.is_live = self.base_url == LIVE_URL
        self._authorization = live_authorization
        self._guard_live()
        if not key_id or not secret_key:
            raise BrokerError("Alpaca credentials are required")
        if not math.isfinite(timeout) or timeout <= 0 or max_retries < 0:
            raise ValueError("timeout must be positive; max_retries nonnegative")
        self._headers = {"APCA-API-KEY-ID": key_id, "APCA-API-SECRET-KEY": secret_key}
        self._session = session if session is not None else requests.Session()
        self.timeout = timeout
        self.max_retries = max_retries

    @classmethod
    def from_env(
        cls,
        *,
        live_authorization: LiveAuthorization | None = None,
        session: Any = None,
        base_url: str | None = None,
        timeout: float = 10.0,
        max_retries: int = 3,
    ) -> "AlpacaBroker":
        """Require APCA_API_KEY_ID and APCA_API_SECRET_KEY, without echoing values."""
        key = os.environ.get("APCA_API_KEY_ID", "")
        secret = os.environ.get("APCA_API_SECRET_KEY", "")
        if not key or not secret:
            raise BrokerError("set APCA_API_KEY_ID and APCA_API_SECRET_KEY")
        return cls(
            key,
            secret,
            live_authorization=live_authorization,
            session=session,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

    def _guard_live(self) -> None:
        if self.is_live and (
            os.environ.get("FA_QUANT_ALLOW_LIVE") != "1"
            or not isinstance(self._authorization, LiveAuthorization)
            or not self._authorization.is_valid(datetime.now(timezone.utc))
        ):
            raise BrokerError(
                "live endpoint requires a valid authorization and explicit opt-in"
            )

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        """Retry idempotent verbs only; submit owns all POST recovery decisions."""
        retries = 0 if method == "POST" else self.max_retries
        for attempt in range(retries + 1):
            self._guard_live()
            try:
                response = self._session.request(
                    method,
                    self.base_url + path,
                    headers=self._headers,
                    timeout=self.timeout,
                    allow_redirects=False,
                    **kwargs,
                )
            except requests.RequestException:
                if attempt == retries:
                    raise BrokerError("broker connection failed") from None
            else:
                if response.status_code != 429 and response.status_code < 500:
                    return response
                if attempt == retries:
                    return response
            time.sleep(min(0.25 * 2**attempt, 2.0))
        raise BrokerError("broker retry budget exhausted")

    @staticmethod
    def _json(response: Any) -> Any:
        if not 200 <= response.status_code < 300:
            raise BrokerError(f"broker request failed (HTTP {response.status_code})")
        try:
            return response.json()
        except (ValueError, TypeError):
            raise BrokerError("invalid broker JSON response") from None

    @staticmethod
    def _ack(value: Any) -> OrderAck:
        statuses: dict[str, OrderStatus] = {
            "new": "accepted",
            "accepted": "accepted",
            "pending_new": "pending",
            "accepted_for_bidding": "accepted",
            "pending_cancel": "accepted",
            "pending_replace": "accepted",
            "held": "pending",
            "stopped": "accepted",
            "filled": "filled",
            "partially_filled": "partially_filled",
            "canceled": "canceled",
            "expired": "canceled",
            "done_for_day": "canceled",
            "replaced": "canceled",
            "rejected": "rejected",
            "suspended": "pending",
            "calculated": "filled",
        }
        try:
            side = value["side"]
            if side not in ("buy", "sell"):
                raise ValueError("invalid side")
            # Server rejection text can contain submitted credentials; omit it.
            return OrderAck(
                str(value["client_order_id"]),
                str(value["id"]),
                str(value["symbol"]),
                side,
                float(value["qty"]),
                statuses[value["status"]],
                float(value["filled_qty"]),
                (
                    float(value["filled_avg_price"])
                    if value.get("filled_avg_price")
                    else None
                ),
                _timestamp(value["submitted_at"] or value["created_at"]),
                "broker rejected order" if value["status"] == "rejected" else None,
            )
        except (KeyError, TypeError, ValueError):
            raise BrokerError("invalid broker order response") from None

    def _lookup(self, client_order_id: str) -> OrderAck | None:
        response = self._request(
            "GET",
            "/v2/orders:by_client_order_id",
            params={"client_order_id": client_order_id},
        )
        if response.status_code == 404:
            return None
        return self._ack(self._json(response))

    def submit(self, order: Order) -> OrderAck:
        """Every ambiguous POST is followed by a client-ID lookup before retrying."""
        validate_order(order)
        # Alpaca permits fractional qty only for market/day orders, excluding OPG:
        # https://docs.alpaca.markets/us/reference/postorder (qty field).
        if not float(order.qty).is_integer() and (
            order.order_type != "market" or order.time_in_force != "day"
        ):
            raise BrokerError(
                "fractional quantities require market orders with day TIF"
            )
        body = dict(
            symbol=order.symbol,
            qty=_decimal_string(order.qty),
            side=order.side,
            type=order.order_type,
            time_in_force=order.time_in_force,
            client_order_id=order.client_order_id,
        )
        if order.limit_price is not None:
            body["limit_price"] = _decimal_string(order.limit_price)
        for attempt in range(self.max_retries + 1):
            try:
                response = self._request("POST", "/v2/orders", json=body)
            except BrokerError:
                # If lookup fails, stop: it is not safe to blindly place again.
                existing = self._lookup(order.client_order_id)
                if existing is not None:
                    return existing
                if attempt == self.max_retries:
                    raise BrokerError(
                        "order submission failed after client-ID lookup"
                    ) from None
            else:
                if 200 <= response.status_code < 300:
                    return self._ack(self._json(response))
                retryable = response.status_code == 429 or response.status_code >= 500
                if response.status_code in (409, 422) or retryable:
                    existing = self._lookup(order.client_order_id)
                    if existing is not None:
                        return existing
                if not retryable or attempt == self.max_retries:
                    self._json(response)
            time.sleep(min(0.25 * 2**attempt, 2.0))
        raise BrokerError("order retry budget exhausted")

    def account(self) -> AccountSnapshot:
        """Observe broker-reported cash/equity and current per-share position marks."""
        value = self._json(self._request("GET", "/v2/account"))
        records = self._json(self._request("GET", "/v2/positions"))
        try:
            positions = {
                p["symbol"]: Position(
                    p["symbol"],
                    float(p["qty"]),
                    float(p["avg_entry_price"]),
                    float(p["current_price"]),
                )
                for p in records
            }
            return AccountSnapshot(
                float(value["cash"]),
                float(value["equity"]),
                positions,
                datetime.now(timezone.utc),
            )
        except (KeyError, TypeError, ValueError):
            raise BrokerError("invalid broker account response") from None

    def open_orders(self) -> list[OrderAck]:
        """Fetch open orders, requesting Alpaca's maximum page size."""
        records = self._json(
            self._request("GET", "/v2/orders", params={"status": "open", "limit": 500})
        )
        if not isinstance(records, list):
            raise BrokerError("invalid broker orders response")
        if len(records) >= 500:
            raise BrokerError(
                "open orders reach API page limit; observation incomplete"
            )
        return [self._ack(v) for v in records]

    def cancel_all(self) -> int:
        """Count successful per-order cancellations from the multi-status response."""
        records = self._json(self._request("DELETE", "/v2/orders"))
        try:
            return sum(200 <= int(record["status"]) < 300 for record in records)
        except (KeyError, TypeError, ValueError):
            raise BrokerError("invalid broker cancellation response") from None

    def clock(self) -> dict[str, Any]:
        """Return exchange timestamp, is_open, next_open and next_close fields."""
        value = self._json(self._request("GET", "/v2/clock"))
        if not isinstance(value, dict):
            raise BrokerError("invalid broker clock response")
        return cast(dict[str, Any], value)
