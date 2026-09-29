# Compatibility Entrypoint

This path is kept for automation prompts that still call:

`agents/equity/prompt/main.md`

The canonical entrypoint is:

`agents/equity/daily_investment_system/main.md`

Run the canonical prompt directly. This file intentionally contains no separate rules, scoring logic, or output specification.

Old callers of `investments/equity/prompt/main.md` (or any other `investments/...` path) should switch to the canonical entrypoint above: the `investments/` tree was renamed to `agents/` and no longer exists.
