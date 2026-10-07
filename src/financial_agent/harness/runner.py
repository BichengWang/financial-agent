"""Run driver: the skeleton behind ``fa-harness run`` (plan §3.5, Phase 4).

The runner owns the order of a run, the (model, date) lock, and the gated
publish. Everything that does work (adapters, kernels, model calls) plugs in as
a stage handler; a stage without a handler halts the run instead of being
skipped, so a half-built pipeline can never publish.

A handler for state ``S`` runs while the lifecycle is in ``S``; the runner then
advances to the next state. ``RISK_REVIEW`` must return the run status, and the
publish gate runs before the lifecycle moves to ``PUBLISHED``. A handler sees
every earlier stage's result (``context.results``), so stages pass data forward
without a side channel.

Every run writes a journal, ``{output_dir}/.runs/{model}-{date}.json``, after each
stage: transitions, per-stage notes, data and timings, gate failures, and the
halt reason. It is the run's heartbeat while it runs and its record after.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Mapping

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
class StageResult:
    note: str = ""
    status: RunStatus | None = None  # required from the RISK_REVIEW handler
    halt: str | None = None  # a handler's way to stop the run with a reason
    data: Mapping[str, Any] = field(default_factory=dict)  # for later stages


@dataclass(frozen=True)
class RunContext:
    model: str
    date: str
    package_dir: Path
    policy: Policy | None = field(default=None, compare=False)
    # Results of the stages that already ran, filled in by ``run``.
    results: dict[RunState, StageResult] = field(default_factory=dict, compare=False)

    @property
    def run_id(self) -> str:
        return f"{self.model}-{self.date}"


Handler = Callable[[RunContext], StageResult]


@dataclass
class RunReport:
    run_id: str
    lifecycle: RunLifecycle
    gate_failures: list[str] = field(default_factory=list)
    stages: dict[str, dict[str, Any]] = field(default_factory=dict)

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


class RunJournal:
    """``{output_dir}/.runs/{run_id}.json``, replaced atomically on every write."""

    def __init__(self, output_dir: Path, run_id: str) -> None:
        self.path = output_dir / ".runs" / f"{run_id}.json"
        self.started_at = _now()

    def write(self, report: RunReport, *, finished: bool = False) -> None:
        lifecycle = report.lifecycle
        body = {
            "run_id": report.run_id,
            "started_at": self.started_at,
            "updated_at": _now(),
            "finished": finished,
            "state": lifecycle.state.value,
            "status": lifecycle.status.value if lifecycle.status else None,
            "transcript": lifecycle.transcript(),
            "transitions": [
                {
                    "source": t.source.value,
                    "target": t.target.value,
                    "at": t.at,
                    "note": t.note,
                }
                for t in lifecycle.log
            ],
            "stages": report.stages,
            "gate_failures": report.gate_failures,
            "halt_reason": report.halt_reason,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        partial = self.path.with_suffix(".json.partial")
        partial.write_text(json.dumps(body, indent=2, default=str), encoding="utf-8")
        partial.replace(self.path)


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def run(
    model: str,
    date: str,
    output_dir: Path,
    handlers: Mapping[RunState, Handler],
    *,
    policy: Policy | None = None,
) -> RunReport:
    """Drive one run to ``EVOLUTION_REVIEW`` or ``HALTED``; never raises on a halt."""
    policy = policy or load_policy()
    context = RunContext(model, date, output_dir / f"{model}-{date}", policy)
    report = RunReport(context.run_id, RunLifecycle(context.run_id))
    with RunLock(output_dir, context.run_id):
        journal = RunJournal(output_dir, context.run_id)
        try:
            _drive(context, report, handlers, policy, journal)
        finally:
            journal.write(report, finished=True)
    return report


def _drive(
    context: RunContext,
    report: RunReport,
    handlers: Mapping[RunState, Handler],
    policy: Policy,
    journal: RunJournal,
) -> None:
    lifecycle = report.lifecycle
    status: RunStatus | None = None
    for index, state in enumerate(PIPELINE):
        outcome = _stage(handlers, state, context, report)
        journal.write(report)
        if isinstance(outcome, str):
            lifecycle.halt(outcome)
            return
        if outcome.halt:
            lifecycle.halt(outcome.halt)
            return
        if state is RunState.RISK_REVIEW:
            if outcome.status is None or outcome.status is RunStatus.HALTED:
                lifecycle.halt("RISK_REVIEW handler returned no publishable status")
                return
            status = outcome.status
            break
        lifecycle.advance(PIPELINE[index + 1], outcome.note)
    assert status is not None
    report.gate_failures = _gate(context, policy)
    try:
        lifecycle.publish(status, report.gate_failures)
    except LifecycleError as exc:
        lifecycle.halt(str(exc))
        return
    journal.write(report)
    if POST_PUBLISH in handlers:
        outcome = _stage(handlers, POST_PUBLISH, context, report)
        note = outcome if isinstance(outcome, str) else outcome.note
    else:
        note = "skipped: no handler"
    lifecycle.advance(POST_PUBLISH, note)


def _stage(
    handlers: Mapping[RunState, Handler],
    state: RunState,
    context: RunContext,
    report: RunReport,
) -> StageResult | str:
    """Run one stage and record it; a string result is the halt reason."""
    started = time.monotonic()
    outcome = _call(handlers, state, context)
    entry: dict[str, Any] = {"seconds": round(time.monotonic() - started, 3)}
    if isinstance(outcome, str):
        entry["halt"] = outcome
    else:
        context.results[state] = outcome
        entry.update(note=outcome.note, data=dict(outcome.data))
        if outcome.halt:
            entry["halt"] = outcome.halt
    report.stages[state.value] = entry
    return outcome


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
    from financial_agent.harness.handlers import precheck_handler, reflection_handler

    return {
        RunState.PRECHECK: precheck_handler,
        RunState.REFLECTION: reflection_handler,
    }
