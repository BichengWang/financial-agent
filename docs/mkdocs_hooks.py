"""MkDocs hooks: publish repository Markdown at its repository path.

The site serves README.md as the home page, plus CHANGELOG.md, the Markdown
under docs/ (except archive/ folders) and reports/quant/, keeping each file's
repository-relative path so the relative links written for GitHub resolve
unchanged. Links to anything else in the repository (source, configs, data,
directories) point to GitHub instead.
"""

import posixpath
import re
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page

ROOT = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/BichengWang/financial-agent"
SITE_GLOBS = ("CHANGELOG.md", "docs/**/*.md", "reports/quant/*.md")
LINK = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
FENCE = re.compile(r"^\s*(```|~~~)")


def on_files(files: Files, config: MkDocsConfig) -> Files:
    site, use_dirs = config.site_dir, config.use_directory_urls
    pages = [File("README.md", str(ROOT), site, use_dirs, dest_uri="index.html")]
    for pattern in SITE_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            uri = path.relative_to(ROOT).as_posix()
            if "/archive/" in uri:
                continue  # Superseded baselines; their links predate later moves.
            dest = None
            if path.name == "README.md":
                # README.md would claim its directory's index, as index.md does.
                stem = uri.removesuffix(".md")
                dest = f"{stem}/index.html" if use_dirs else f"{stem}.html"
            pages.append(File(uri, str(ROOT), site, use_dirs, dest_uri=dest))
    # Keep theme assets only: data, PDFs and this file under docs/ stay on GitHub.
    docs_dir = Path(config.docs_dir).resolve()
    theme = [
        f
        for f in files
        if f.abs_src_path is None
        or not Path(f.abs_src_path).resolve().is_relative_to(docs_dir)
    ]
    return Files(pages + theme)


def on_page_markdown(
    markdown: str, page: Page, config: MkDocsConfig, files: Files
) -> str:
    base = posixpath.dirname(page.file.src_uri)

    def rewrite(match: re.Match[str]) -> str:
        target = match.group(2)
        path, _, fragment = target.partition("#")
        if not path or re.match(r"^[a-z][a-z0-9+.-]*:", path) or path.startswith("/"):
            return match.group(0)
        resolved = posixpath.normpath(posixpath.join(base, path))
        if files.get_file_from_path(resolved) is not None:
            return match.group(0)
        local = ROOT / resolved
        if resolved.startswith("..") or not local.exists():
            return match.group(0)  # Left for MkDocs to report as broken.
        kind = "tree" if local.is_dir() else "blob"
        url = f"{GITHUB}/{kind}/main/{resolved}" + (f"#{fragment}" if fragment else "")
        return f"{match.group(1)}{url}{match.group(3)}"

    out, fenced = [], False
    for line in markdown.splitlines(keepends=True):
        if FENCE.match(line):
            fenced = not fenced
        out.append(line if fenced else LINK.sub(rewrite, line))
    return "".join(out)
