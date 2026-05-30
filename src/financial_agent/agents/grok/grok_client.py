"""Thin client for the xAI Grok chat-completions API.

The xAI API is OpenAI-compatible; we expose just the slice we need
(``chat_completion``) and inject a custom HTTP function so it is easy
to mock in tests.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable

_HttpFn = Callable[[str, dict[str, str], bytes], tuple[int, bytes]]


class GrokAPIError(RuntimeError):
    """Raised when the xAI Grok API returns an error."""


@dataclass(frozen=True)
class GrokMessage:
    role: str
    content: str

    def to_dict(self) -> dict[str, str]:
        return {"role": self.role, "content": self.content}


def _default_http(url: str, headers: dict[str, str], body: bytes) -> tuple[int, bytes]:
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


class GrokClient:
    """Minimal Grok / xAI chat client."""

    def __init__(
        self,
        api_key: str,
        model: str = "grok-4-latest",
        base_url: str = "https://api.x.ai/v1",
        http: _HttpFn | None = None,
    ) -> None:
        self._api_key = api_key
        self._model = model
        self._base_url = base_url.rstrip("/")
        self._http: _HttpFn = http or _default_http

    def chat_completion(
        self,
        messages: list[GrokMessage],
        temperature: float = 0.2,
    ) -> str:
        """Send a chat-completion request and return the assistant text.

        Raises :class:`GrokAPIError` on non-2xx responses or malformed
        payloads.
        """
        url = f"{self._base_url}/chat/completions"
        body = json.dumps(
            {
                "model": self._model,
                "messages": [m.to_dict() for m in messages],
                "temperature": temperature,
                "stream": False,
            }
        ).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        status, raw = self._http(url, headers, body)
        if status >= 400:
            raise GrokAPIError(
                f"Grok API HTTP {status}: {raw.decode('utf-8', 'replace')}"
            )
        try:
            data: dict[str, Any] = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise GrokAPIError(f"Invalid JSON from Grok: {raw!r}") from exc

        choices = data.get("choices") or []
        if not choices:
            raise GrokAPIError(f"Grok response had no choices: {data}")
        message = (choices[0] or {}).get("message") or {}
        content = message.get("content")
        if not isinstance(content, str):
            raise GrokAPIError(f"Grok response had no text content: {data}")
        return content
