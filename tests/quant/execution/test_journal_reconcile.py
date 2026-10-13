"""Audit corruption detection and position union reconciliation."""

from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import json

import pytest

from financial_agent.quant.execution import BrokerError, Journal, reconcile
from financial_agent.quant.risk.orders import AccountSnapshot, Position


def test_chain_restart_filter_and_tampering(tmp_path: Path) -> None:
    path = tmp_path / "journal.jsonl"
    journal = Journal(path)
    one = journal.append("fill", {"qty": 2})
    two = Journal(path).append("account", {"cash": 800})
    assert two.seq == 2 and two.prev_hash == one.hash
    assert Journal(path).verify().ok
    assert journal.events(["fill"]) == [one]
    lines = path.read_text().splitlines()
    edited = json.loads(lines[0])
    edited["payload"]["qty"] = 3
    lines[0] = json.dumps(edited)
    path.write_text("\n".join(lines) + "\n")
    check = journal.verify()
    assert not check.ok and check.first_bad_seq == 1
    with pytest.raises(BrokerError):
        journal.append("fill", {})
    with pytest.raises(BrokerError):
        journal.events()


@pytest.mark.parametrize(
    "key", ["secret", "PASSWORD", "access_token", "api_key", "key_id"]
)
def test_nested_secret_keys_rejected(tmp_path: Path, key: str) -> None:
    journal = Journal(tmp_path / "journal")
    with pytest.raises(ValueError, match="secret-like"):
        journal.append("bad", {"nested": [{key: "value"}]})
    assert journal.verify().events == 0


@pytest.mark.parametrize("mutation", [b" ", b"\r", b"\xff"])
def test_byte_encoding_edits_are_detected(tmp_path: Path, mutation: bytes) -> None:
    journal = Journal(tmp_path / "journal")
    journal.append("a", {})
    journal.append("b", {})
    raw = journal.path.read_bytes()
    split = raw.index(b"\n", raw.index(b"\n") + 1)
    journal.path.write_bytes(raw[:split] + mutation + raw[split:])
    assert journal.verify().first_bad_seq == 2
    with pytest.raises(BrokerError):
        journal.append("c", {})


def test_hash_and_genesis(tmp_path: Path) -> None:
    journal = Journal(tmp_path / "journal")
    assert journal.events() == [] and journal.verify().ok
    event = journal.append("a", {"x": [1, 2]})
    from hashlib import sha256

    fields = asdict(event)
    fields.pop("hash")
    assert (
        event.hash
        == sha256(
            json.dumps(fields, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
    )
    assert event.prev_hash == ""


def test_reconcile_union_tolerance_and_nonfinite() -> None:
    account = AccountSnapshot(
        0,
        100,
        {
            "extra": Position("extra", 3, 1, 1),
            "mismatch": Position("mismatch", 4, 1, 1),
            "same": Position("same", 1.0000001, 1, 1),
        },
        datetime.now(timezone.utc),
    )
    breaks = reconcile({"missing": 2, "mismatch": 5, "same": 1}, account)
    assert [(b.symbol, b.expected_qty, b.actual_qty) for b in breaks] == [
        ("extra", 0, 3),
        ("mismatch", 5, 4),
        ("missing", 2, 0),
    ]
    assert reconcile({"bad": float("nan")}, AccountSnapshot(0, 0, {}, account.as_of))
    with pytest.raises(ValueError):
        reconcile({}, account, tolerance=-1)
