# Security policy

## Supported versions

Security fixes go into the latest release on [PyPI](https://pypi.org/project/fa-quant/)
and `main`. Older releases are not patched.

## Reporting a vulnerability

Please don't open a public issue. Report it privately through
[GitHub private vulnerability reporting](https://github.com/BichengWang/financial-agent/security/advisories/new)
with the affected version, steps to reproduce and the impact you expect.

You should get a reply within 7 days. Once a fix is released, the advisory is
published with credit to the reporter unless you'd rather stay anonymous.

Issues of particular interest:

- Ways to submit orders without the live gate (certificate, paper evidence and
  `FA_QUANT_ALLOW_LIVE=1`), or through the MCP server.
- Ways to loosen runtime risk limits from a config, or to bypass the kill switch.
- Leaks of broker credentials into logs, journals or committed files.
- TLS verification being disabled for a non-loopback IBKR gateway.

## Using the software safely

Keep broker keys in the process environment, never in TOML, git or shell
history. Start with paper accounts, and read the [safety guide](docs/quant/safety.md)
before enabling live trading. The software is provided as is, without warranty;
it is not investment advice.
