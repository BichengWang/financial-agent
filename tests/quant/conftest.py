"""Spies on how state writers replace a file and fsync its directory."""

import errno
import os
from collections.abc import Callable
from pathlib import Path
import stat
from typing import Any

import pytest


@pytest.fixture
def fsync_log(monkeypatch: pytest.MonkeyPatch) -> list[tuple[str, object]]:
    """Replaced paths and fsynced directories' (st_dev, st_ino), in call order."""
    events: list[tuple[str, object]] = []
    replace, fsync = os.replace, os.fsync

    def logged_replace(source: Any, target: Any) -> None:
        replace(source, target)
        events.append(("replace", Path(target)))

    def logged_fsync(descriptor: int) -> None:
        info = os.fstat(descriptor)
        if stat.S_ISDIR(info.st_mode):
            events.append(("fsync", (info.st_dev, info.st_ino)))
        fsync(descriptor)

    monkeypatch.setattr(os, "replace", logged_replace)
    monkeypatch.setattr(os, "fsync", logged_fsync)
    return events


@pytest.fixture(params=["unopenable", "EINVAL"])
def directory_fsync_fails(
    request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Directories cannot be opened, or the filesystem refuses to fsync them."""
    open_, fsync = os.open, os.fsync

    def refused_open(path: Any, flags: int, *args: Any, **kwargs: Any) -> int:
        if os.path.isdir(path):
            raise PermissionError(errno.EACCES, os.strerror(errno.EACCES), path)
        return open_(path, flags, *args, **kwargs)

    def refused_fsync(descriptor: int) -> None:
        if stat.S_ISDIR(os.fstat(descriptor).st_mode):
            raise OSError(errno.EINVAL, os.strerror(errno.EINVAL))
        fsync(descriptor)

    if request.param == "unopenable":
        monkeypatch.setattr(os, "open", refused_open)
    else:
        monkeypatch.setattr(os, "fsync", refused_fsync)


@pytest.fixture
def open_descriptors() -> Callable[[], int]:
    """How many file descriptors this process has open."""
    return lambda: len(os.listdir("/dev/fd"))
