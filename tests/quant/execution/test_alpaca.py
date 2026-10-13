"""Canned REST v2 responses exercise safety gates and transport recovery."""

from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
import requests  # type: ignore[import-untyped]

from financial_agent.quant.execution import AlpacaBroker, BrokerError, LiveAuthorization
from financial_agent.quant.risk.orders import Order
from financial_agent.quant.execution.alpaca import LIVE_URL, PAPER_URL


class Response:
    def __init__(self, status: int, value: Any) -> None:
        self.status_code = status
        self.value = value

    def json(self) -> Any:
        return self.value


class Transport:
    def __init__(self, *responses: Response | Exception) -> None:
        self.responses = list(responses)
        self.calls: list[tuple[str, str, dict[str, Any]]] = []

    def request(self, method: str, url: str, **kwargs: Any) -> Response:
        self.calls.append((method, url, kwargs))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


@pytest.fixture(autouse=True)
def no_backoff(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "financial_agent.quant.execution.alpaca.time.sleep", lambda _: None
    )


def order_json(status: str = "new") -> dict[str, Any]:
    return dict(
        id="broker-123",
        client_order_id="client-123",
        symbol="SPY",
        side="buy",
        qty="5",
        status=status,
        filled_qty="0",
        filled_avg_price=None,
        submitted_at="2026-10-12T23:00:00Z",
    )


def authorization(*, expired: bool = False) -> LiveAuthorization:
    now = datetime.now(timezone.utc)
    return LiveAuthorization(
        "trend",
        "a" * 64,
        "b" * 64,
        now - timedelta(days=1),
        now + timedelta(days=-0.5 if expired else 1),
    )


def test_live_gate_and_expiry(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("FA_QUANT_ALLOW_LIVE", raising=False)
    for grant in (None, authorization(), authorization(expired=True)):
        with pytest.raises(BrokerError, match="live endpoint"):
            AlpacaBroker("key", "secret", base_url=LIVE_URL, live_authorization=grant)
    monkeypatch.setenv("FA_QUANT_ALLOW_LIVE", "1")
    for grant in (None, authorization(expired=True)):
        with pytest.raises(BrokerError):
            AlpacaBroker("key", "secret", base_url=LIVE_URL, live_authorization=grant)
    transport = Transport(Response(200, {}))
    broker = AlpacaBroker(
        "key",
        "secret",
        base_url=LIVE_URL,
        live_authorization=authorization(),
        session=transport,
    )
    assert broker.is_live
    assert broker.clock() == {}
    assert transport.calls[0][1] == LIVE_URL + "/v2/clock"
    transport.calls.clear()
    monkeypatch.delenv("FA_QUANT_ALLOW_LIVE")
    with pytest.raises(BrokerError):
        broker.clock()
    assert transport.calls == []
    with pytest.raises(BrokerError, match="unsupported"):
        AlpacaBroker("key", "secret", base_url="https://example.com")
    naive = datetime.now()
    assert not LiveAuthorization("s", "a" * 64, "b" * 64, naive, naive).is_valid(naive)


def test_request_and_duplicate_client_lookup() -> None:
    transport = Transport(
        Response(422, {"message": "client_order_id must be unique"}),
        Response(200, order_json()),
    )
    broker = AlpacaBroker("test-key", "test-secret", session=transport)
    ack = broker.submit(Order("SPY", "buy", 5, client_order_id="client-123"))
    assert ack.broker_order_id == "broker-123"
    assert ack.status == "accepted"
    method, url, kwargs = transport.calls[0]
    assert method == "POST" and url == PAPER_URL + "/v2/orders"
    assert kwargs["json"] == dict(
        symbol="SPY",
        side="buy",
        qty="5",
        type="market",
        time_in_force="opg",
        client_order_id="client-123",
    )
    assert kwargs["headers"] == {
        "APCA-API-KEY-ID": "test-key",
        "APCA-API-SECRET-KEY": "test-secret",
    }
    assert kwargs["allow_redirects"] is False
    assert transport.calls[1][1] == PAPER_URL + "/v2/orders:by_client_order_id"
    assert transport.calls[1][2]["params"] == {"client_order_id": "client-123"}
    assert "test-secret" not in repr(broker) + str(broker)


@pytest.mark.parametrize(
    "failure",
    [Response(429, {}), Response(503, {}), requests.ConnectionError("test-secret")],
)
def test_post_recovery_checks_client_id_before_retry(
    failure: Response | Exception,
) -> None:
    transport = Transport(failure, Response(404, {}), Response(200, order_json()))
    broker = AlpacaBroker("key", "test-secret", session=transport)
    assert (
        broker.submit(Order("SPY", "buy", 5, client_order_id="client-123")).status
        == "accepted"
    )
    assert [c[0] for c in transport.calls] == ["POST", "GET", "POST"]
    assert transport.calls[0][2]["json"] == transport.calls[2][2]["json"]


def test_ambiguous_post_found_and_failed_lookup() -> None:
    transport = Transport(
        requests.ConnectionError("test-secret"), Response(200, order_json("filled"))
    )
    broker = AlpacaBroker("key", "test-secret", session=transport)
    assert (
        broker.submit(Order("SPY", "buy", 5, client_order_id="client-123")).status
        == "filled"
    )
    assert len(transport.calls) == 2
    transport = Transport(Response(503, {}), Response(401, {"message": "test-secret"}))
    broker = AlpacaBroker("key", "test-secret", session=transport)
    with pytest.raises(BrokerError) as error:
        broker.submit(Order("SPY", "buy", 5, client_order_id="client-123"))
    assert "test-secret" not in str(error.value)
    assert [c[0] for c in transport.calls] == ["POST", "GET"]


def test_idempotent_retry_budget_and_sanitized_errors() -> None:
    transport = Transport(Response(429, {}), Response(200, {"is_open": False}))
    assert AlpacaBroker("key", "secret", session=transport).clock()["is_open"] is False
    transport = Transport(*[requests.ConnectionError("test-secret") for _ in range(3)])
    broker = AlpacaBroker("key", "test-secret", session=transport, max_retries=2)
    with pytest.raises(BrokerError) as error:
        broker.clock()
    assert len(transport.calls) == 3
    assert "test-secret" not in str(error.value)
    assert error.value.__suppress_context__


def test_account_open_orders_and_multistatus_cancel() -> None:
    partial = order_json("partially_filled")
    partial.update(filled_qty="2", filled_avg_price="101.5")
    transport = Transport(
        Response(200, {"cash": "797", "equity": "1001"}),
        Response(
            200,
            [
                {
                    "symbol": "SPY",
                    "qty": "2",
                    "avg_entry_price": "101.5",
                    "current_price": "102",
                }
            ],
        ),
        Response(200, [partial]),
        Response(207, [{"id": "a", "status": 200}, {"id": "b", "status": 422}]),
    )
    broker = AlpacaBroker("key", "secret", session=transport)
    account = broker.account()
    assert account.cash == 797 and account.equity == 1001
    assert account.positions["SPY"].market_value == 204
    (ack,) = broker.open_orders()
    assert ack.filled_qty == 2 and ack.filled_avg_price == 101.5
    assert broker.cancel_all() == 1
    assert [(c[0], c[1].removeprefix(PAPER_URL)) for c in transport.calls] == [
        ("GET", "/v2/account"),
        ("GET", "/v2/positions"),
        ("GET", "/v2/orders"),
        ("DELETE", "/v2/orders"),
    ]


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("pending_new", "pending"),
        ("new", "accepted"),
        ("filled", "filled"),
        ("partially_filled", "partially_filled"),
        ("expired", "canceled"),
        ("rejected", "rejected"),
    ],
)
def test_status_mapping(raw: str, expected: str) -> None:
    transport = Transport(Response(200, order_json(raw)))
    ack = AlpacaBroker("key", "secret", session=transport).submit(
        Order("SPY", "buy", 5, client_order_id="client-123")
    )
    assert ack.status == expected


def test_from_env_and_nonduplicate_rejection(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("APCA_API_KEY_ID", raising=False)
    monkeypatch.delenv("APCA_API_SECRET_KEY", raising=False)
    with pytest.raises(BrokerError, match="APCA_API_KEY_ID"):
        AlpacaBroker.from_env()
    monkeypatch.setenv("APCA_API_KEY_ID", "key")
    monkeypatch.setenv("APCA_API_SECRET_KEY", "test-secret")
    transport = Transport(
        Response(422, {"message": "test-secret invalid quantity"}), Response(404, {})
    )
    with pytest.raises(BrokerError) as error:
        AlpacaBroker.from_env(session=transport).submit(
            Order("SPY", "buy", 5, client_order_id="client-123")
        )
    assert "test-secret" not in str(error.value)
    assert len(transport.calls) == 2
