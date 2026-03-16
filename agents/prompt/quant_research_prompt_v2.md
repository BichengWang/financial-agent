# Quantitative Equity Selection System Prompt — v2.0 Legacy Note

This monolithic file has been superseded by the modular v3 prompt system rooted at `main.md`.

Use this directory as follows:

- `main.md`: master entrypoint and execution order
- `eval/`: shared research rules, stop criteria, and evolution governance
- `loop/`: executable prompts for the orchestrator and specialist agents
- `output/`: daily schedule, artifact layout, and report templates

The v3 version adds:

1. A multi-agent execution loop instead of one prompt.
2. A bounded self-evolution cycle.
3. Explicit stop criteria.
4. A concrete weekday schedule.
5. A dated output package specification under `output/<YYYY-MM-DD>/`.

Treat this file as a legacy pointer, not the active prompt entrypoint.
