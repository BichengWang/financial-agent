"""Content hashes for run packages, to catch cloned artifacts.

Historical packages show byte-identical analysis files shared across different
models and dates (for example ``gpt-5-2026-06-20`` and ``gemini-3.5-flash-2026-06-21``
have the same ``06_top_candidates.md``). A package digest pins what was
published; ``find_clones`` reports artifacts that another package also contains.
"""

from __future__ import annotations

import datetime as dt
import hashlib
from collections import defaultdict
from pathlib import Path

ARTIFACT_SUFFIXES = {".md", ".json"}


def artifact_digests(package_dir: Path) -> dict[str, str]:
    """SHA-256 of every artifact file in a package, keyed by file name."""
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(package_dir.iterdir())
        if path.is_file() and path.suffix in ARTIFACT_SUFFIXES
    }


def package_digest(package_dir: Path) -> str:
    """One hash over all artifact names and contents; order-independent of disk."""
    lines = "".join(
        f"{name}:{digest}\n" for name, digest in artifact_digests(package_dir).items()
    )
    return hashlib.sha256(lines.encode("utf-8")).hexdigest()


def find_clones(
    output_dir: Path, *, since: str | None = None
) -> dict[tuple[str, str], list[str]]:
    """Packages sharing a byte-identical artifact, keyed by ``(file, sha256)``.

    Only packages named ``{model}-{YYYY-MM-DD}`` dated on or after ``since`` are
    compared. Empty files are ignored: they carry no content to clone.
    """
    seen: dict[tuple[str, str], list[str]] = defaultdict(list)
    for package_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        try:
            dt.date.fromisoformat(package_dir.name[-10:])
        except ValueError:
            continue
        if since is not None and package_dir.name[-10:] < since:
            continue
        for name, digest in artifact_digests(package_dir).items():
            if digest != hashlib.sha256(b"").hexdigest():
                seen[(name, digest)].append(package_dir.name)
    return {key: pkgs for key, pkgs in seen.items() if len(pkgs) > 1}
