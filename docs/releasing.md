# Releasing

## Names

| What | Name |
|---|---|
| PyPI distribution | `fa-quant` |
| Import package | `financial_agent` (declared as PEP 794 `import-names`) |
| Command | `fa-quant` |

`financial-agent` on PyPI is an unrelated project that also ships a
`financial_agent` module. Never document `pip install financial-agent`.

## Cutting a release

1. The release PR bumps `[project] version` in `pyproject.toml`, runs `uv lock`,
   moves the `CHANGELOG.md` `[Unreleased]` entries under `## [X.Y.Z] - DATE`, and
   updates the link references. The version line in
   [safety.md](quant/safety.md) changes with it.
2. After the squash merge, tag the merge commit and push the tag:

   ```sh
   git tag -a vX.Y.Z -m vX.Y.Z <merge-sha>
   git push origin vX.Y.Z
   ```

3. The [Release workflow](../.github/workflows/release.yml) reruns the full
   checks. It confirms the tag matches the version and that a CHANGELOG section
   exists. It builds the sdist and builds the wheel from that sdist, runs
   `twine check --strict`, and smoke-tests the installed wheel. Then it uploads to
   PyPI (once enabled) and creates the GitHub release with the CHANGELOG notes.
   If the PyPI upload fails, no GitHub release is created. Rerun the failed jobs
   after fixing the cause.

The sdist contains only what building the wheel needs: `src/financial_agent`,
the two harness helpers the wheel copies from `agents/`, the README, LICENSE and
CHANGELOG. The PyPI description is the README with the Mermaid diagram removed
and repository links pointed at the release tag.

## PyPI trusted publishing (one-time owner setup)

The workflow publishes with PyPI trusted publishing (OIDC), so no API token is
stored. Configure it once:

1. On [TestPyPI](https://test.pypi.org/manage/account/publishing/) and on
   [PyPI](https://pypi.org/manage/account/publishing/), add a pending publisher:
   project `fa-quant`, owner `BichengWang`, repository `financial-agent`, workflow
   `release.yml`, environment `testpypi` and `pypi` respectively.
2. Optional: in GitHub Settings → Environments, give `pypi` a required reviewer,
   so every upload waits for approval.
3. Rehearse: Actions → Release → Run workflow on `main`. The `testpypi` job
   uploads the current version; a rerun of a version already uploaded is skipped.
   Check the project page, then install it:

   ```sh
   pip install --index-url https://test.pypi.org/simple/ \
     --extra-index-url https://pypi.org/simple/ fa-quant
   fa-quant demo --sessions 3 --state-dir /tmp/fa-quant-testpypi
   ```

4. Enable: in Settings → Secrets and variables → Actions → Variables, set
   `PYPI_PUBLISH` to `true`. From then on every `v*` tag uploads to PyPI.

PyPI never accepts the same version twice, even after deletion. Releases up to
v1.2.0 are tagged already, so the first PyPI upload is the next version tag.
