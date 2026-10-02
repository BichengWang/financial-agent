"""Run driver: the skeleton behind ``fa-harness run`` (plan §3.5, Phase 4).

The runner owns the order of a run, the (model, date) lock, and the gated
publish. Everything that does work (adapters, kernels, model calls) plugs in as
a stage handler; a stage without a handler halts the run instead of being
skipped, so a half-built pipeline can never publish.

A handler for state ``S`` runs while the lifecycle is in ``S``; the runner then
advances to the next state. ``RISK_REVIEW`` must return the run status, and the
publish gate runs before the lifecycle moves to ``PUBLISHED``.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Mapping

from financial_agent.harness.gates import publish_gate
from financial_agent.harness.lifecycle import (
    LifecycleError,
    RunLifecycle,
    RunState,
    RunStatus,
)
from financial_agent.harness.policy import Policy, load_policy

# States whose handler runs before the lifecycle advances, in order.
PIPELINE = (
    RunState.PRECHECK,
    RunState.REFLECTION,
    RunState.DATA_OK,
    RunState.TECHNICALS_OK,
    RunState.SCORED,
    RunState.PORTFOLIO_DRAFT,
    RunState.RISK_REVIEW,
)
POST_PUBLISH = RunState.EVOLUTION_REVIEW


class RunLocked(RuntimeError):
    """Another run holds the (model, date) lock, or a crashed one left it."""


@dataclass(frozen=True)
class RunContext:
    model: str
    date: str
    package_dir: Path

    @property
    def run_id(self) -> str:
        return f"{self.model}-{self.date}"


@dataclass(frozen=True)
class StageResult:
    note: str = ""
    status: RunStatus | None = None  # required from the RISK_REVIEW handler
    halt: str | None = None  # a handler's way to stop the run with a reason


Handler = Callable[[RunContext], StageResult]


@dataclass
class RunReport:
    run_id: str
    lifecycle: RunLifecycle
    gate_failures: list[str] = field(default_factory=list)

    @property
    def published(self) -> bool:
        return self.lifecycle.status not in {None, RunStatus.HALTED}

    @property
    def halt_reason(self) -> str | None:
        last = self.lifecycle.log[-1] if self.lifecycle.log else None
        if last is not None and last.target is RunState.HALTED:
            return last.note
        return None


class RunLock:
    """``{output_dir}/.locks/{model}-{date}.lock``, created atomically.

    Not reentrant and never stolen: a crashed run leaves the file, and a person
    removes it after looking at the half-written package.
    """

    def __init__(self, output_dir: Path, run_id: str) -> None:
        self.path = output_dir / ".locks" / f"{run_id}.lock"

    def __enter__(self) -> "RunLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise RunLocked(
                f"{self.path} exists: a run is in progress or crashed; "
                "inspect the package, then remove the lock"
            ) from None
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(f"pid={os.getpid()}\n")
        return self

    def __exit__(self, *exc: object) -> None:
        self.path.unlink(missing_ok=True)


def run(
    model: str,
    date: str,
    output_dir: Path,
    handlers: Mapping[RunState, Handler],
    *,
    policy: Policy | None = None,
) -> RunReport:
    """Drive one run to ``EVOLUTION_REVIEW`` or ``HALTED``; never raises on a halt."""
    context = RunContext(model, date, output_dir / f"{model}-{date}")
    lifecycle = RunLifecycle(context.run_id)
    report = RunReport(context.run_id, lifecycle)
    with RunLock(output_dir, context.run_id):
        status: RunStatus | None = None
        for index, state in enumerate(PIPELINE):
            outcome = _call(handlers, state, context)
            if isinstance(outcome, str):
                lifecycle.halt(outcome)
                return report
            if outcome.halt:
                lifecycle.halt(outcome.halt)
                return report
            if state is RunState.RISK_REVIEW:
                if outcome.status is None or outcome.status is RunStatus.HALTED:
                    lifecycle.halt("RISK_REVIEW handler returned no publishable status")
                    return report
                status = outcome.status
                break
            lifecycle.advance(PIPELINE[index + 1], outcome.note)
        assert status is not None
        report.gate_failures = _gate(context, policy or load_policy())
        try:
            lifecycle.publish(status, report.gate_failures)
        except LifecycleError as exc:
            lifecycle.halt(str(exc))
            return report
        if POST_PUBLISH in handlers:
            outcome = _call(handlers, POST_PUBLISH, context)
            note = outcome if isinstance(outcome, str) else outcome.note
        else:
            note = "skipped: no handler"
        lifecycle.advance(POST_PUBLISH, note)
    return report


def _call(
    handlers: Mapping[RunState, Handler], state: RunState, context: RunContext
) -> StageResult | str:
    """A handler's result, or the halt reason when it is missing or raises."""
    handler = handlers.get(state)
    if handler is None:
        return f"no handler for {state.value}"
    try:
        return handler(context)
    except Exception as exc:  # a failed stage halts the run; it never publishes
        return f"{state.value} handler failed: {type(exc).__name__}: {exc}"


def _gate(context: RunContext, policy: Policy) -> list[str]:
    if not context.package_dir.is_dir():
        return [f"package directory {context.package_dir} was never created"]
    return publish_gate(context.package_dir, policy)


def default_handlers() -> Mapping[RunState, Handler]:
    """Shipped handlers. Stages without one halt the run (plan Phase 2)."""
    from financial_agent.harness.handlers import reflection_handler

    return {RunState.REFLECTION: reflection_handler}
