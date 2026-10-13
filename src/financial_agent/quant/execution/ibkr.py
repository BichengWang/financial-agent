"""Client Portal Gateway execution; USD accounts and whole-share opening auctions.

Endpoint schemas verified 2026-10-13 against https://api.ibkr.com/gw/api/v3/api-docs
and https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/ .
Direct IBKR OAuth endpoints are deliberately outside this adapter's scope.
"""

from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from typing import Any, Literal, cast
from urllib.parse import quote, urlsplit
import ipaddress
import math
import os
import re
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

GATEWAY_URL = "https://localhost:5000/v1/api"
# API-pending/cancelled are IB server states also defined in the order guide:
# https://interactivebrokers.github.io/tws-api/order_submission.html
_STATUSES: dict[str, OrderStatus] = {
    "PendingSubmit": "pending",
    "ApiPending": "pending",
    "PreSubmitted": "accepted",
    "Submitted": "accepted",
    "PendingCancel": "accepted",
    "Filled": "filled",
    "Cancelled": "canceled",
    "ApiCancelled": "canceled",
    "Inactive": "rejected",
    "WarnState": "pending",
}


def validate_gateway(base_url: str, verify: bool | str) -> None:
    """Require HTTPS, gateway API paths and verified TLS beyond loopback."""
    parsed = urlsplit(base_url)
    host = parsed.hostname or ""
    if (
        parsed.scheme != "https"
        or not host
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path.rstrip("/") != "/v1/api"
        or host == "ibkr.com"
        or host.endswith(".ibkr.com")
        or host == "interactivebrokers.com"
        or host.endswith(".interactivebrokers.com")
    ):
        raise BrokerError("use a Client Portal Gateway HTTPS endpoint, not OAuth")
    # A gateway may be hosted remotely, but its TLS must then be verified.
    loopback = host in ("localhost", "127.0.0.1", "::1")
    if not isinstance(verify, (bool, str)) or (isinstance(verify, str) and not verify):
        raise BrokerError("TLS verify must be a boolean or CA-bundle path")
    if verify is False and not loopback:
        raise BrokerError("TLS verification may be disabled only on loopback")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        pass
    else:
        if not address.is_private and not address.is_loopback:
            raise BrokerError("use a locally hosted Client Portal Gateway")


class IBKRQuestion(BrokerError):
    """An explicitly declined precaution; safe details may enter session reports."""

    def __init__(
        self, ids: Sequence[str], messages: Sequence[str], account_id: str
    ) -> None:
        # Only the dedicated prompt field is exposed, never arbitrary error bodies.
        text = " ".join(messages)
        text = re.sub(
            r"\b(?:DU|DF|U|D|F)\d+\b",
            lambda m: m[0] if m[0] == account_id else "[account]",
            text,
        )
        text = re.sub(r"[\w.+-]+@[\w.-]+", "[redacted]", text)
        text = re.sub(r"https?://\S+", "[redacted]", text)
        self.detail = f"IBKR question declined; message ids {list(ids)}: {text[:2000]}"
        super().__init__(self.detail)


class IBKRBroker:
    """Never switch accounts, auto-approve unknown questions, or retry order POSTs."""

    name = "ibkr"

    def __init__(
        self,
        account_id: str,
        *,
        base_url: str = GATEWAY_URL,
        verify: bool | str = True,
        session: Any = None,
        live_authorization: LiveAuthorization | None = None,
        conids: Mapping[str, int] | None = None,
        confirm_message_ids: Sequence[str] = (),
        timeout: float = 10.0,
        max_retries: int = 3,
    ) -> None:
        validate_gateway(base_url, verify)
        if not isinstance(account_id, str) or not re.fullmatch(
            r"[A-Z]+\d+", account_id
        ):
            raise BrokerError("IBKR account_id is required and must be an account ID")
        if (
            not math.isfinite(timeout)
            or timeout <= 0
            or type(max_retries) is not int
            or max_retries < 0
        ):
            raise ValueError("timeout must be positive; max_retries nonnegative")
        self.account_id = account_id
        self.is_live = not account_id.startswith("D")
        self._authorization = live_authorization
        self._guard_live()
        self.base_url = base_url.rstrip("/")
        self.verify = verify
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = session if session is not None else requests.Session()
        self._conids = dict(conids or {})
        if any(
            not isinstance(s, str) or not s or type(c) is not int or c <= 0
            for s, c in self._conids.items()
        ) or len(set(self._conids.values())) != len(self._conids):
            raise BrokerError("conids require unique positive integer contract IDs")
        if isinstance(confirm_message_ids, str) or any(
            not isinstance(i, str) or not re.fullmatch(r"[A-Za-z0-9]+", i)
            for i in confirm_message_ids
        ):
            raise BrokerError("confirm_message_ids must contain message identifiers")
        self._confirm = frozenset(confirm_message_ids)
        self._submitted: dict[str, OrderAck] = {}
        self._last_request = 0.0
        self._last_slow: dict[str, float] = {}
        self._authenticated_at: float | None = None
        self._account_validated = False
        self._ready()

    def _guard_live(self) -> None:
        if self.is_live and (
            os.environ.get("FA_QUANT_ALLOW_LIVE") != "1"
            or not isinstance(self._authorization, LiveAuthorization)
            or not self._authorization.is_valid(datetime.now(timezone.utc))
        ):
            raise BrokerError(
                "live IBKR requires valid authorization and explicit opt-in"
            )

    def _pace(self, path: str) -> None:
        """Respect 10 requests/s globally and five seconds between slow reads.

        Pacing: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
        One adapter owns one gateway session; do not share it with other clients.
        """
        slow = path in (
            "/portfolio/accounts",
            "/iserver/account/orders",
            "/iserver/account/trades",
        )
        now = time.monotonic()
        delay = max(0.0, self._last_request + 0.1 - now)
        if slow and path in self._last_slow:
            delay = max(delay, self._last_slow[path] + 5.0 - now)
        if delay:
            time.sleep(delay)
        stamp = time.monotonic()
        self._last_request = stamp
        if slow:
            self._last_slow[path] = stamp

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        """Retry idempotent reads/deletes only; never include server error bodies."""
        retries = self.max_retries if method in ("GET", "DELETE") else 0
        for attempt in range(retries + 1):
            self._guard_live()
            self._pace(path)
            self._guard_live()
            try:
                response = self._session.request(
                    method,
                    self.base_url + path,
                    verify=self.verify,
                    timeout=self.timeout,
                    allow_redirects=False,
                    **kwargs,
                )
            except requests.RequestException:
                if attempt == retries:
                    raise BrokerError("IBKR gateway connection failed") from None
            else:
                if 200 <= response.status_code < 300:
                    try:
                        return response.json()
                    except (ValueError, TypeError):
                        raise BrokerError("invalid IBKR JSON response") from None
                if response.status_code == 401:
                    self._authenticated_at = None
                    if path != "/iserver/auth/status":
                        self._check_auth(force=True)
                if (
                    response.status_code != 429 and response.status_code < 500
                ) or attempt == retries:
                    raise BrokerError(
                        f"IBKR request failed (HTTP {response.status_code})"
                    )
            time.sleep(min(0.25 * 2**attempt, 2.0))
        raise BrokerError("IBKR retry budget exhausted")

    def _check_auth(self, *, force: bool = False) -> None:
        """Check gateway authentication at most once/minute, except after 401."""
        if (
            not force
            and self._authenticated_at is not None
            and time.monotonic() - self._authenticated_at < 60
        ):
            return
        self._authenticated_at = None
        # OpenAPI: auth/status is POST; accounts must precede order queries.
        status = self._request("POST", "/iserver/auth/status")
        if not isinstance(status, dict) or not (
            status.get("authenticated") is True and status.get("connected") is True
        ):
            raise BrokerError("log in to the Client Portal Gateway before trading")
        self._authenticated_at = time.monotonic()

    def _ready(self) -> None:
        """Guard live requests; validate account identity/type/USD once per instance."""
        self._guard_live()
        self._check_auth()
        if self._account_validated:
            return
        accounts = self._request("GET", "/iserver/accounts")
        if (
            not isinstance(accounts, dict)
            or not isinstance(accounts.get("accounts"), list)
            or self.account_id not in accounts["accounts"]
        ):
            raise BrokerError(f"configured account {self.account_id} is not tradable")
        if "isPaper" in accounts and (
            type(accounts["isPaper"]) is not bool or accounts["isPaper"] == self.is_live
        ):
            raise BrokerError("IBKR paper metadata disagrees with account ID")
        # accountAttributes.type describes the environment; acctCustType is unrelated.
        metadata = self._request("GET", "/portfolio/accounts")
        if not isinstance(metadata, list) or any(
            not isinstance(m, dict) for m in metadata
        ):
            raise BrokerError("invalid IBKR account metadata")
        matches = [
            m for m in metadata if m.get("accountId", m.get("id")) == self.account_id
        ]
        if len(matches) != 1:
            raise BrokerError("configured account missing from portfolio metadata")
        record = matches[0]
        kind = record.get("type")
        if kind is not None:
            paper_types = {"DEMO", "DEMO-BROKER", "DEMO-ADVISOR", "PAPER"}
            live_types = {
                "FNF",
                "INDIVIDUAL",
                "COMPANY",
                "STL",
                "UTMA",
                "PRO-ADV",
                "IRA",
                "TRUST",
            }
            if not isinstance(kind, str) or kind not in paper_types | live_types:
                raise BrokerError("unrecognized IBKR account environment")
            paper = kind in paper_types
            if paper == self.is_live:
                raise BrokerError("IBKR account type disagrees with account ID")
        if record.get("currency") != "USD":
            raise BrokerError("IBKR requires USD account base currency")
        self._account_validated = True

    def _conid(self, symbol: str) -> int:
        if symbol not in self._conids:
            value = self._request("GET", "/trsrv/stocks", params={"symbols": symbol})
            try:
                contracts = [
                    c["conid"]
                    for stock in value[symbol]
                    if stock["assetClass"] == "STK"
                    for c in stock["contracts"]
                    if c["isUS"] is True
                ]
                if (
                    len(contracts) != 1
                    or type(contracts[0]) is not int
                    or contracts[0] <= 0
                ):
                    raise ValueError("ambiguous")
                self._conids[symbol] = contracts[0]
            except (KeyError, TypeError, ValueError):
                raise BrokerError(
                    f"require exactly one US stock contract for {symbol}"
                ) from None
        return self._conids[symbol]

    def _symbol(self, value: dict[str, Any]) -> str:
        conid = int(value["conid"])
        symbols = [s for s, c in self._conids.items() if c == conid]
        if symbols:
            return symbols[0]
        symbol = value.get("ticker", value.get("symbol"))
        if not isinstance(symbol, str) or not symbol or self._conid(symbol) != conid:
            raise BrokerError("position/order contract cannot be mapped to a US symbol")
        return symbol

    @staticmethod
    def _number(value: Any) -> float:
        result = float(value)
        if not math.isfinite(result):
            raise ValueError("nonfinite number")
        return result

    def account(self) -> AccountSnapshot:
        """Observe USD cash, net liquidation and every page of equity positions."""
        self._ready()
        summary = self._request("GET", f"/portfolio/{self.account_id}/summary")
        ledger = self._request("GET", f"/portfolio/{self.account_id}/ledger")
        try:
            net = summary["netliquidation"]
            if net["currency"] != "USD" or net.get("isNull"):
                raise BrokerError("IBKR summary must report USD net liquidation")
            cash = self._number(ledger["BASE"]["cashbalance"])
            equity = self._number(net["amount"])
            if ledger["BASE"].get("acctcode", self.account_id) != self.account_id:
                raise BrokerError("IBKR ledger account mismatch")
            positions: dict[str, Position] = {}
            # Positions are paged (100/page); an empty page terminates observation.
            for page in range(1000):
                records = self._request(
                    "GET", f"/portfolio/{self.account_id}/positions/{page}"
                )
                if not isinstance(records, list):
                    raise BrokerError("invalid IBKR positions response")
                if not records:
                    break
                for p in records:
                    if (
                        p["acctId"] != self.account_id
                        or p["assetClass"] != "STK"
                        or p["currency"] != "USD"
                    ):
                        raise BrokerError(
                            "IBKR positions require same-account USD equities"
                        )
                    symbol = self._symbol(p)
                    if symbol in positions:
                        raise BrokerError("duplicate IBKR position across pages")
                    positions[symbol] = Position(
                        symbol,
                        self._number(p["position"]),
                        self._number(p["avgPrice"]),
                        self._number(p["mktPrice"]),
                    )
            else:
                raise BrokerError("IBKR position page budget exhausted")
            return AccountSnapshot(cash, equity, positions, datetime.now(timezone.utc))
        except (KeyError, TypeError, ValueError):
            raise BrokerError("invalid IBKR account response") from None

    def _orders(self) -> list[dict[str, Any]]:
        value = self._request("GET", "/iserver/account/orders")
        if (
            not isinstance(value, dict)
            or not isinstance(value.get("orders"), list)
            or value.get("snapshot") is not True
        ):
            raise BrokerError("IBKR orders observation is incomplete")
        if any(
            not isinstance(o, dict) or not o.get("account", o.get("acct"))
            for o in value["orders"]
        ):
            raise BrokerError("IBKR orders lack account identity")
        return [
            o
            for o in value["orders"]
            if o.get("account", o.get("acct")) == self.account_id
        ]

    def _ack(self, value: dict[str, Any], client_id: str | None = None) -> OrderAck:
        try:
            side = cast(
                Literal["buy", "sell"], {"BUY": "buy", "SELL": "sell"}[value["side"]]
            )
            qty = self._number(value["totalSize"])
            filled = self._number(value["filledQuantity"])
            status = _STATUSES[value["status"]]
            if 0 < filled < qty and status == "accepted":
                status = "partially_filled"
            if (
                qty <= 0
                or filled < 0
                or filled > qty
                or (status == "filled" and filled != qty)
            ):
                raise ValueError("invalid quantities")
            price = self._number(value["avgPrice"]) if filled else None
            if price is not None and price <= 0:
                raise ValueError("invalid fill price")
            return OrderAck(
                client_id
                or str(value.get("local_order_id", value.get("order_ref", ""))),
                str(value["orderId"]),
                self._symbol(value),
                side,
                qty,
                status,
                filled,
                price,
                datetime.now(timezone.utc),
                "IBKR rejected order" if status == "rejected" else None,
            )
        except (KeyError, TypeError, ValueError):
            raise BrokerError("invalid IBKR order response") from None

    # IBKR defines local_order_id = cOID in its submission walkthrough:
    # https://www.interactivebrokers.com/campus/ibkr-quant-news/how-to-code-a-bracket-order-in-the-web-api/
    def lookup(self, client_order_id: str) -> OrderAck | None:
        """Recover cOID from current orders or deduplicated seven-day executions."""
        self._ready()
        for order in self._orders():
            if client_order_id in (order.get("local_order_id"), order.get("order_ref")):
                return self._ack(order, client_order_id)
        trades = self._request("GET", "/iserver/account/trades", params={"days": 7})
        if not isinstance(trades, list) or any(
            not isinstance(t, dict) or not t.get("account") for t in trades
        ):
            raise BrokerError("invalid IBKR trades response")
        matches = [
            t
            for t in trades
            if t.get("account") == self.account_id
            and t.get("order_ref") == client_order_id
        ]
        if not matches:
            return None
        try:
            unique = {t["execution_id"]: t for t in matches}
            first = matches[0]
            if first["side"] not in ("B", "S") or any(
                unique[t["execution_id"]] != t for t in matches
            ):
                raise ValueError("invalid or conflicting execution")
            if any(
                (t["order_id"], t["conid"], t["side"])
                != (first["order_id"], first["conid"], first["side"])
                for t in unique.values()
            ):
                raise ValueError("conflicting execution identity")
            qty = sum(self._number(t["size"]) for t in unique.values())
            if qty <= 0 or any(
                self._number(t["size"]) <= 0 or self._number(t["price"]) <= 0
                for t in unique.values()
            ):
                raise ValueError("invalid executions")
            price = (
                sum(
                    self._number(t["size"]) * self._number(t["price"])
                    for t in unique.values()
                )
                / qty
            )
            known = self._submitted.get(client_order_id)
            if known and qty > known.qty:
                raise ValueError("executions exceed original order quantity")
            # Trade history does not disclose original quantity or terminal status.
            # Do not invent completion when only partial executions are observable.
            return OrderAck(
                client_order_id,
                str(first["order_id"]),
                self._symbol(first),
                "buy" if first["side"] == "B" else "sell",
                known.qty if known else qty,
                "filled" if known and qty == known.qty else "partially_filled",
                qty,
                price,
                datetime.fromtimestamp(
                    self._number(first["trade_time_r"]) / 1000, timezone.utc
                ),
            )
        except (KeyError, TypeError, ValueError):
            raise BrokerError("invalid IBKR executions") from None

    def submit(self, order: Order) -> OrderAck:
        """Lookup before POST and after ambiguity; unknown precautions are declined."""
        validate_order(order)
        if (
            order.order_type != "market"
            or order.time_in_force != "opg"
            or not float(order.qty).is_integer()
            or order.limit_price is not None
            or len(order.client_order_id) > 64
        ):
            raise BrokerError(
                "IBKR requires whole-share market OPG orders and cOID <= 64"
            )
        existing = self.lookup(order.client_order_id)
        if existing is not None:
            return existing
        body = {
            "orders": [
                {
                    "acctId": self.account_id,
                    "conid": self._conid(order.symbol),
                    "orderType": "MKT",
                    "tif": "OPG",
                    "quantity": int(order.qty),
                    "side": order.side.upper(),
                    "cOID": order.client_order_id,
                }
            ]
        }
        try:
            self._ready()
            value = self._request(
                "POST", f"/iserver/account/{self.account_id}/orders", json=body
            )
            for _ in range(10):
                if (
                    not isinstance(value, list)
                    or len(value) != 1
                    or not isinstance(value[0], dict)
                ):
                    raise BrokerError("invalid IBKR submission response")
                item = value[0]
                if "order_id" in item:
                    status = _STATUSES.get(str(item.get("order_status")))
                    if status is None or status in ("filled", "partially_filled"):
                        observed = self.lookup(order.client_order_id)
                        if observed is None:
                            raise BrokerError(
                                "IBKR submission needs an observable order"
                            )
                        return observed
                    ack = OrderAck(
                        order.client_order_id,
                        str(item["order_id"]),
                        order.symbol,
                        order.side,
                        order.qty,
                        status,
                        0,
                        None,
                        datetime.now(timezone.utc),
                    )
                    self._submitted[order.client_order_id] = ack
                    return ack
                if "id" not in item:
                    raise BrokerError("IBKR order submission failed")
                ids, messages = item.get("messageIds", []), item.get("message", [])
                if (
                    not isinstance(ids, list)
                    or not all(
                        isinstance(i, str) and re.fullmatch(r"[A-Za-z0-9]+", i)
                        for i in ids
                    )
                    or not isinstance(messages, list)
                    or not all(isinstance(m, str) for m in messages)
                ):
                    raise BrokerError("invalid IBKR question")
                allowed = bool(ids) and set(ids).issubset(self._confirm)
                if not allowed:
                    try:
                        self._request(
                            "POST",
                            "/iserver/reply/" + quote(str(item["id"]), safe=""),
                            json={"confirmed": False},
                        )
                    finally:
                        raise IBKRQuestion(ids, messages, self.account_id)
                value = self._request(
                    "POST",
                    "/iserver/reply/" + quote(str(item["id"]), safe=""),
                    json={"confirmed": True},
                )
            raise BrokerError("IBKR question loop budget exhausted")
        except IBKRQuestion:
            raise
        except BrokerError:
            existing = self.lookup(order.client_order_id)
            if existing is not None:
                return existing
            # Stop after an uncertain POST; a later runner retry performs lookup first.
            raise BrokerError("IBKR submission failed after cOID lookup") from None

    def open_orders(self) -> list[OrderAck]:
        """Observe working orders only in the configured account."""
        self._ready()
        return [
            ack
            for o in self._orders()
            if (ack := self._ack(o)).status
            in ("pending", "accepted", "partially_filled")
        ]

    def cancel_all(self) -> int:
        """Request cancellation of configured-account working orders only."""
        count = 0
        for order in self.open_orders():
            self._ready()
            value = self._request(
                "DELETE",
                f"/iserver/account/{self.account_id}/order/"
                + quote(order.broker_order_id, safe=""),
            )
            if (
                not isinstance(value, dict)
                or "error" in value
                or "order_id" not in value
            ):
                raise BrokerError("IBKR cancellation failed")
            count += 1
        return count
