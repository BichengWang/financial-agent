import json

import pytest

from financial_agent.agents.grok.grok_client import (
    GrokAPIError,
    GrokClient,
    GrokMessage,
)


class _FakeHttp:
    def __init__(self, responses: list[tuple[int, dict]]):
        self.responses = list(responses)
        self.calls: list[tuple[str, dict[str, str], dict]] = []

    def __call__(
        self, url: str, headers: dict[str, str], body: bytes
    ) -> tuple[int, bytes]:
        payload = json.loads(body.decode("utf-8"))
        self.calls.append((url, headers, payload))
        status, resp = self.responses.pop(0)
        return status, json.dumps(resp).encode("utf-8")


def test_chat_completion_happy_path() -> None:
    http = _FakeHttp(
        [
            (
                200,
                {"choices": [{"message": {"role": "assistant", "content": "hi!"}}]},
            )
        ]
    )
    client = GrokClient("xai-key", model="grok-test", http=http)
    text = client.chat_completion(
        [GrokMessage("system", "be nice"), GrokMessage("user", "hello")]
    )
    assert text == "hi!"

    url, headers, payload = http.calls[0]
    assert url == "https://api.x.ai/v1/chat/completions"
    assert headers["Authorization"] == "Bearer xai-key"
    assert payload["model"] == "grok-test"
    assert payload["messages"] == [
        {"role": "system", "content": "be nice"},
        {"role": "user", "content": "hello"},
    ]
    assert payload["stream"] is False


def test_chat_completion_http_error() -> None:
    http = _FakeHttp([(401, {"error": "nope"})])
    client = GrokClient("xai-key", http=http)
    with pytest.raises(GrokAPIError, match="HTTP 401"):
        client.chat_completion([GrokMessage("user", "hi")])


def test_chat_completion_no_choices() -> None:
    http = _FakeHttp([(200, {"choices": []})])
    client = GrokClient("xai-key", http=http)
    with pytest.raises(GrokAPIError, match="no choices"):
        client.chat_completion([GrokMessage("user", "hi")])


def test_chat_completion_no_text() -> None:
    http = _FakeHttp([(200, {"choices": [{"message": {"content": None}}]})])
    client = GrokClient("xai-key", http=http)
    with pytest.raises(GrokAPIError, match="no text content"):
        client.chat_completion([GrokMessage("user", "hi")])
