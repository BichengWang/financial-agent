"""Gateway-shaped fake transport exercises safety and order recovery offline."""

from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
import requests

from financial_agent.quant.execution import IBKRBroker, BrokerError, LiveAuthorization
from financial_agent.quant.execution.ibkr import IBKRQuestion
from financial_agent.quant.risk import Order


_PACE = IBKRBroker._pace


@pytest.fixture(autouse=True)
def no_transport_pacing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(IBKRBroker, "_pace", lambda self, path: None)


class Response:
    def __init__(self, value: Any, status: int = 200) -> None:
        self.status_code = status
        self.value = value

    def json(self) -> Any:
        return self.value


class Gateway:
    """Minimal documented responses; mutations stay observable to the consumer."""

    def __init__(self, account_id: str = "DU123456") -> None:
        self.account_id = account_id
        self.authenticated = True
        self.connected = True
        self.accounts = [account_id]
        self.is_paper = account_id.startswith("D")
        self.account_type = "DEMO" if self.is_paper else "INDIVIDUAL"
        self.currency = "USD"
        self.cash = 100000.0
        self.orders: list[dict[str, Any]] = []
        self.trades: list[dict[str, Any]] = []
        self.positions: list[dict[str, Any]] = []
        self.calls: list[tuple[str, str, dict[str, Any]]] = []
        self.questions: list[list[str]] = []
        self.pending: dict[str, Any] | None = None
        self.duplicate = False
        self.ambiguous = False
        self.stock_contracts = [{"conid": 123, "exchange": "NYSE", "isUS": True}]

    def request(self, method: str, url: str, **kwargs: Any) -> Response:
        path = url.split("/v1/api")[1]
        self.calls.append((method, path, kwargs))
        if path == "/iserver/auth/status":
            assert method == "POST"
            return Response(
                {"authenticated": self.authenticated, "connected": self.connected}
            )
        if path == "/iserver/accounts":
            return Response({"accounts": self.accounts, "isPaper": self.is_paper})
        if path == "/portfolio/accounts":
            return Response(
                [
                    {
                        "accountId": self.account_id,
                        "type": self.account_type,
                        "currency": self.currency,
                    }
                ]
            )
        if path.endswith("/summary"):
            equity = self.cash + sum(
                p["position"] * p["mktPrice"] for p in self.positions
            )
            return Response(
                {
                    "netliquidation": {
                        "amount": equity,
                        "currency": self.currency,
                        "isNull": False,
                    }
                }
            )
        if path.endswith("/ledger"):
            return Response(
                {
                    "BASE": {
                        "cashbalance": self.cash,
                        "acctcode": self.account_id,
                        "currency": "BASE",
                    }
                }
            )
        if "/positions/" in path:
            page = int(path.rsplit("/", 1)[1])
            return Response(self.positions[page * 100 : (page + 1) * 100])
        if path == "/trsrv/stocks":
            symbol = kwargs["params"]["symbols"]
            return Response(
                {symbol: [{"assetClass": "STK", "contracts": self.stock_contracts}]}
            )
        if path == "/iserver/account/orders":
            return Response({"orders": self.orders.copy(), "snapshot": True})
        if path == "/iserver/account/trades":
            assert kwargs["params"] == {"days": 7}
            return Response(self.trades.copy())
        if path.endswith("/orders") and method == "POST":
            self.pending = kwargs["json"]["orders"][0]
            if self.duplicate:
                self.accept()
                return Response({"error": "duplicate cOID private-account-data"}, 422)
            if self.questions:
                return self.question()
            result = self.accept()
            if self.ambiguous:
                raise requests.ConnectionError("private-account-data")
            return result
        if path.startswith("/iserver/reply/"):
            if not kwargs["json"]["confirmed"]:
                self.pending = None
                return Response({})
            return self.question() if self.questions else self.accept()
        if method == "DELETE":
            order_id = int(path.rsplit("/", 1)[1])
            for order in self.orders:
                if order["orderId"] == order_id:
                    order["status"] = "Cancelled"
            return Response({"order_id": order_id, "msg": "Request was submitted"})
        raise AssertionError((method, path))

    def question(self) -> Response:
        return Response(
            [
                {
                    "id": "reply-1",
                    "messageIds": self.questions.pop(0),
                    "message": ["Order without market data for U999999; continue?"],
                }
            ]
        )

    def accept(self) -> Response:
        assert self.pending is not None
        p = self.pending
        self.orders.append(
            {
                "account": self.account_id,
                "local_order_id": p["cOID"],
                "orderId": len(self.orders) + 1,
                "conid": p["conid"],
                "ticker": "SPY",
                "side": p["side"],
                "totalSize": p["quantity"],
                "filledQuantity": 0,
                "avgPrice": "0",
                "status": "PreSubmitted",
            }
        )
        self.pending = None
        return Response(
            [{"order_id": self.orders[-1]["orderId"], "order_status": "PreSubmitted"}]
        )


def order(qty: float = 10) -> Order:
    return Order("SPY", "buy", qty, client_order_id="client-1")


def grant(expired: bool = False) -> LiveAuthorization:
    now = datetime.now(timezone.utc)
    return LiveAuthorization(
        "trend_vol_target",
        "a" * 64,
        "b" * 64,
        now - timedelta(minutes=30),
        now + timedelta(minutes=-1 if expired else 15),
    )


@pytest.mark.parametrize("account_id", ["DU123456", "DF123456"])
def test_paper_detection_and_auth_checks(account_id: str) -> None:
    transport = Gateway(account_id)
    assert not IBKRBroker(account_id, session=transport).is_live
    transport.authenticated = False
    with pytest.raises(BrokerError, match="log in"):
        IBKRBroker(account_id, session=transport)
    transport.authenticated = True
    transport.connected = False
    with pytest.raises(BrokerError, match="log in"):
        IBKRBroker(account_id, session=transport)


@pytest.mark.parametrize("failure", ["no_grant", "expired", "no_env"])
def test_live_refusal_before_transport(
    failure: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("FA_QUANT_ALLOW_LIVE", "1")
    if failure == "no_env":
        monkeypatch.delenv("FA_QUANT_ALLOW_LIVE")
    transport = Gateway("U123456")
    with pytest.raises(BrokerError, match="authorization"):
        IBKRBroker(
            "U123456",
            session=transport,
            live_authorization=(
                None if failure == "no_grant" else grant(failure == "expired")
            ),
        )
    assert not transport.calls


def test_live_guard_on_every_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FA_QUANT_ALLOW_LIVE", "1")
    transport = Gateway("U123456")
    broker = IBKRBroker("U123456", session=transport, live_authorization=grant())
    assert broker.is_live
    monkeypatch.delenv("FA_QUANT_ALLOW_LIVE")
    before = len(transport.calls)
    with pytest.raises(BrokerError, match="authorization"):
        broker.account()
    assert len(transport.calls) == before


@pytest.mark.parametrize("variation", ["missing", "isPaper", "type", "currency"])
def test_account_validation(variation: str) -> None:
    transport = Gateway()
    if variation == "missing":
        transport.accounts = ["DU999999"]
    elif variation == "isPaper":
        transport.is_paper = False
    elif variation == "type":
        transport.account_type = "INDIVIDUAL"
    else:
        transport.currency = "EUR"
    with pytest.raises(BrokerError):
        IBKRBroker(transport.account_id, session=transport)
    assert not any(p.endswith("/orders") for _, p, _ in transport.calls)


@pytest.mark.parametrize("host", ["localhost", "127.0.0.1", "[::1]"])
def test_loopback_self_signed(host: str) -> None:
    transport = Gateway()
    IBKRBroker(
        "DU123456",
        base_url=f"https://{host}:5001/v1/api",
        verify=False,
        session=transport,
    )
    assert all(
        k["verify"] is False and not k["allow_redirects"] for _, _, k in transport.calls
    )


@pytest.mark.parametrize(
    "url,verify",
    [
        ("https://gateway.internal:5001/v1/api", False),
        ("http://localhost:5000/v1/api", True),
        ("https://api.ibkr.com/v1/api", True),
        ("https://localhost:5000/other", True),
    ],
)
def test_endpoint_refusal(url: str, verify: bool) -> None:
    with pytest.raises(BrokerError):
        IBKRBroker("DU123456", base_url=url, verify=verify, session=Gateway())


def test_verified_remote_gateway() -> None:
    transport = Gateway()
    IBKRBroker(
        "DU123456",
        base_url="https://gateway.internal:5001/v1/api",
        verify="/tmp/ca.pem",
        session=transport,
    )
    assert all(k["verify"] == "/tmp/ca.pem" for _, _, k in transport.calls)


def test_contract_resolution_body_and_idempotency() -> None:
    transport = Gateway()
    broker = IBKRBroker("DU123456", session=transport)
    ack = broker.submit(order())
    assert broker.submit(order()).broker_order_id == ack.broker_order_id
    posts = [
        k["json"]
        for m, p, k in transport.calls
        if m == "POST" and p.endswith("/orders")
    ]
    assert posts == [
        {
            "orders": [
                {
                    "acctId": "DU123456",
                    "conid": 123,
                    "orderType": "MKT",
                    "tif": "OPG",
                    "quantity": 10,
                    "side": "BUY",
                    "cOID": "client-1",
                }
            ]
        }
    ]
    assert type(posts[0]["orders"][0]["quantity"]) is int
    assert sum(p == "/trsrv/stocks" for _, p, _ in transport.calls) == 1
    assert broker.cancel_all() == 1
    assert not broker.open_orders()


def test_ambiguity_override_and_fractional_refusal() -> None:
    transport = Gateway()
    transport.stock_contracts.append({"conid": 456, "exchange": "NASDAQ", "isUS": True})
    broker = IBKRBroker("DU123456", session=transport)
    with pytest.raises(BrokerError, match="SPY"):
        broker.submit(order())
    override = IBKRBroker("DU123456", session=transport, conids={"SPY": 456})
    before = len(transport.calls)
    with pytest.raises(BrokerError, match="whole-share"):
        override.submit(order(1.5))
    assert len(transport.calls) == before
    override.submit(order())
    assert transport.orders[-1]["conid"] == 456


@pytest.mark.parametrize("duplicate", [True, False])
def test_ambiguous_post_recovers_without_repeat(duplicate: bool) -> None:
    transport = Gateway()
    transport.duplicate = duplicate
    transport.ambiguous = not duplicate
    broker = IBKRBroker("DU123456", session=transport)
    assert broker.submit(order()).status == "accepted"
    assert (
        sum(m == "POST" and p.endswith("/orders") for m, p, _ in transport.calls) == 1
    )


def test_reply_chain_and_decline() -> None:
    transport = Gateway()
    transport.questions = [["o354"], ["o163", "o354"]]
    broker = IBKRBroker("DU123456", session=transport, confirm_message_ids=["o354"])
    with pytest.raises(IBKRQuestion, match="o163") as caught:
        broker.submit(order())
    assert "U999999" not in str(caught.value)
    assert "Order without market data" in str(caught.value)
    replies = [
        k["json"] for _, p, k in transport.calls if p.startswith("/iserver/reply/")
    ]
    assert replies == [{"confirmed": True}, {"confirmed": False}]
    assert not transport.orders
    transport.questions = [["o354"], ["o163"]]
    allowed = IBKRBroker(
        "DU123456", session=transport, confirm_message_ids=["o354", "o163"]
    )
    assert allowed.submit(order()).status == "accepted"


def test_reply_loop_bound() -> None:
    transport = Gateway()
    transport.questions = [["o354"]] * 12
    broker = IBKRBroker("DU123456", session=transport, confirm_message_ids=["o354"])
    with pytest.raises(BrokerError):
        broker.submit(order())
    assert sum(p.startswith("/iserver/reply/") for _, p, _ in transport.calls) == 10
    assert not transport.orders


@pytest.mark.parametrize(
    "status,expected",
    [
        ("PendingSubmit", "pending"),
        ("ApiPending", "pending"),
        ("PreSubmitted", "accepted"),
        ("Submitted", "accepted"),
        ("PendingCancel", "accepted"),
        ("Filled", "filled"),
        ("Cancelled", "canceled"),
        ("ApiCancelled", "canceled"),
        ("Inactive", "rejected"),
        ("WarnState", "pending"),
    ],
)
def test_status_mapping(status: str, expected: str) -> None:
    transport = Gateway()
    broker = IBKRBroker("DU123456", session=transport)
    broker.submit(order())
    transport.orders[0].update(
        status=status, filledQuantity=10 if status == "Filled" else 0, avgPrice="100"
    )
    ack = broker.lookup("client-1")
    assert ack is not None and ack.status == expected


def test_lookup_partial_executions_after_session_restart() -> None:
    transport = Gateway()
    broker = IBKRBroker("DU123456", session=transport, conids={"SPY": 123})
    broker.submit(order())
    transport.orders[0].update(status="Submitted", filledQuantity=3, avgPrice="100")
    ack = broker.lookup("client-1")
    assert ack is not None and ack.status == "partially_filled" and ack.filled_qty == 3
    transport.orders = []
    trade = {
        "account": "DU123456",
        "order_ref": "client-1",
        "order_id": 1,
        "execution_id": "a",
        "conid": 123,
        "symbol": "SPY",
        "side": "B",
        "size": 3,
        "price": "100",
        "trade_time_r": 1702317649000,
    }
    transport.trades = [
        trade,
        {**trade, "execution_id": "b", "size": 7, "price": "102"},
        trade,
        {**trade, "account": "DU999999", "execution_id": "c", "size": 900},
    ]
    fresh = IBKRBroker("DU123456", session=transport, conids={"SPY": 123})
    ack = fresh.lookup("client-1")
    assert (
        ack is not None
        and ack.filled_qty == 10
        and ack.filled_avg_price == pytest.approx(101.4)
    )
    assert (
        ack.status == "partially_filled"
    )  # history alone cannot prove terminal status
    assert broker.lookup("client-1").status == "filled"  # type: ignore[union-attr]
    assert fresh.lookup("missing") is None


def test_account_positions_pagination_and_contract_mapping() -> None:
    transport = Gateway()
    conids = {f"S{i}": i + 1 for i in range(101)}
    transport.positions = [
        {
            "acctId": "DU123456",
            "conid": i + 1,
            "position": 2,
            "avgPrice": 90,
            "mktPrice": 100,
            "currency": "USD",
            "assetClass": "STK",
        }
        for i in range(101)
    ]
    broker = IBKRBroker("DU123456", session=transport, conids=conids)
    account = broker.account()
    assert account.cash == 100000 and account.equity == 120200
    assert len(account.positions) == 101 and account.positions["S100"].qty == 2
    assert any(p.endswith("/positions/2") for _, p, _ in transport.calls)
    transport.currency = "EUR"
    with pytest.raises(BrokerError, match="USD"):
        broker.submit(order())


def test_idempotent_backoff_and_sanitized_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class Flaky(Gateway):
        def __init__(self) -> None:
            super().__init__()
            self.failures = 0

        def request(self, method: str, url: str, **kwargs: Any) -> Response:
            if url.endswith("/iserver/accounts") and self.failures < 2:
                self.failures += 1
                return Response({"error": "private-account-data"}, 503)
            return super().request(method, url, **kwargs)

    sleeps: list[float] = []
    monkeypatch.setattr(
        "financial_agent.quant.execution.ibkr.time.sleep", sleeps.append
    )
    transport = Flaky()
    IBKRBroker("DU123456", session=transport, max_retries=2)
    assert sleeps == [0.25, 0.5]
    transport = Flaky()
    with pytest.raises(BrokerError) as caught:
        IBKRBroker("DU123456", session=transport, max_retries=0)
    assert "private-account-data" not in str(caught.value)


@pytest.mark.parametrize("where", ["orders", "trades", "status", "executions"])
def test_incomplete_observation_never_submits(where: str) -> None:
    class Broken(Gateway):
        def request(self, method: str, url: str, **kwargs: Any) -> Response:
            if where == "orders" and url.endswith("/account/orders"):
                return Response({"orders": [], "snapshot": False})
            if where == "trades" and url.endswith("/account/trades"):
                return Response({"error": "private-account-data"})
            return super().request(method, url, **kwargs)

    transport = Broken()
    broker = IBKRBroker("DU123456", session=transport)
    if where in ("status", "executions"):
        broker.submit(order())
        transport.orders[0]["status"] = "Unknown" if where == "status" else "Filled"
    with pytest.raises(BrokerError):
        broker.submit(order())
    assert sum(
        m == "POST" and p.endswith("/orders") for m, p, _ in transport.calls
    ) == (1 if where in ("status", "executions") else 0)


def test_failed_post_is_not_retried_and_body_is_private() -> None:
    class Rejected(Gateway):
        def request(self, method: str, url: str, **kwargs: Any) -> Response:
            if method == "POST" and url.endswith("/orders"):
                self.calls.append((method, url, kwargs))
                return Response({"error": "private-account-data"}, 503)
            return super().request(method, url, **kwargs)

    transport = Rejected()
    broker = IBKRBroker("DU123456", session=transport, max_retries=3)
    with pytest.raises(BrokerError) as caught:
        broker.submit(order())
    assert "private-account-data" not in str(caught.value)
    assert (
        sum(m == "POST" and p.endswith("/orders") for m, p, _ in transport.calls) == 1
    )
    assert sum(p == "/iserver/account/trades" for _, p, _ in transport.calls) == 2


def test_live_metadata_disagreement(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FA_QUANT_ALLOW_LIVE", "1")
    transport = Gateway("U123456")
    transport.account_type = "DEMO"
    with pytest.raises(BrokerError, match="disagrees"):
        IBKRBroker("U123456", session=transport, live_authorization=grant())


def test_empty_reply_ids_are_declined() -> None:
    transport = Gateway()
    transport.questions = [[]]
    broker = IBKRBroker("DU123456", session=transport, confirm_message_ids=["o354"])
    with pytest.raises(IBKRQuestion):
        broker.submit(order())
    assert not transport.orders
    assert [
        k["json"] for _, p, k in transport.calls if p.startswith("/iserver/reply/")
    ] == [{"confirmed": False}]


def test_gateway_pacing(monkeypatch: pytest.MonkeyPatch) -> None:
    now = [10.0]
    sleeps: list[float] = []

    def sleep(delay: float) -> None:
        sleeps.append(delay)
        now[0] += delay

    monkeypatch.setattr(
        "financial_agent.quant.execution.ibkr.time.monotonic", lambda: now[0]
    )
    monkeypatch.setattr("financial_agent.quant.execution.ibkr.time.sleep", sleep)
    broker = IBKRBroker("DU123456", session=Gateway())
    _PACE(broker, "/iserver/account/orders")
    _PACE(broker, "/iserver/auth/status")
    _PACE(broker, "/iserver/account/orders")
    assert sleeps == pytest.approx([0.1, 4.9])
