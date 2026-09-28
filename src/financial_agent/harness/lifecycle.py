"""Run lifecycle: the ``main.md`` state machine enforced in code.

``main.md`` says "a run is a state machine, not an essay". Today the model
narrates the transitions; here the harness owns them, so a skipped stage, an
extra revision pass, or publishing without a passing gate is an exception,
not a sentence in a manifest.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from enum import Enum


class RunState(str, Enum):
    PRECHECK = "PRECHECK"
    REFLECTION = "REFLECTION"
    DATA_OK = "DATA_OK"
    TECHNICALS_OK = "TECHNICALS_OK"
    SCORED = "SCORED"
    PORTFOLIO_DRAFT = "PORTFOLIO_DRAFT"
    RISK_REVIEW = "RISK_REVIEW"
    PUBLISHED = "PUBLISHED"
    CLOSE_LOGGED = "CLOSE_LOGGED"
    EVOLUTION_REVIEW = "EVOLUTION_REVIEW"
    HALTED = "HALTED"


class RunStatus(str, Enum):
    GO = "GO"
    NO_TRADE = "NO_TRADE"
    REVIEW_ONLY = "REVIEW_ONLY"
    HALTED = "HALTED"


_FORWARD: dict[RunState, frozenset[RunState]] = {
    RunState.PRECHECK: frozenset({RunState.REFLECTION}),
    RunState.REFLECTION: frozenset({RunState.DATA_OK}),
    RunState.DATA_OK: frozenset({RunState.TECHNICALS_OK}),
    RunState.TECHNICALS_OK: frozenset({RunState.SCORED}),
    RunState.SCORED: frozenset({RunState.PORTFOLIO_DRAFT}),
    RunState.PORTFOLIO_DRAFT: frozenset({RunState.RISK_REVIEW}),
    RunState.RISK_REVIEW: frozenset({RunState.PUBLISHED}),
    RunState.PUBLISHED: frozenset({RunState.CLOSE_LOGGED, RunState.EVOLUTION_REVIEW}),
    RunState.CLOSE_LOGGED: frozenset({RunState.EVOLUTION_REVIEW}),
    RunState.EVOLUTION_REVIEW: frozenset(),
    RunState.HALTED: frozenset(),
}
# rules.md § Intra-Loop Revision Limit: one portfolio<->risk revision pass and
# one clarification back to factor scoring.
_REVISIONS: dict[tuple[RunState, RunState], str] = {
    (RunState.RISK_REVIEW, RunState.PORTFOLIO_DRAFT): "risk_revision",
    (RunState.PORTFOLIO_DRAFT, RunState.SCORED): "scoring_clarification",
    (RunState.RISK_REVIEW, RunState.SCORED): "scoring_clarification",
}
REVISION_BUDGET = {"risk_revision": 1, "scoring_clarification": 1}


class LifecycleError(RuntimeError):
    """An illegal transition, an exhausted revision budget, or a failed gate."""


@dataclass(frozen=True)
class Transition:
    source: RunState
    target: RunState
    at: str
    note: str


@dataclass
class RunLifecycle:
    run_id: str
    state: RunState = RunState.PRECHECK
    status: RunStatus | None = None
    log: list[Transition] = field(default_factory=list)
    revisions_used: dict[str, int] = field(default_factory=dict)

    def advance(
        self, target: RunState, note: str = "", *, at: str | None = None
    ) -> None:
        if target is RunState.PUBLISHED:
            raise LifecycleError("use publish(): PUBLISHED requires a status and gate")
        self._move(target, note, at)

    def halt(self, reason: str, *, at: str | None = None) -> None:
        if self.state in {RunState.HALTED, RunState.EVOLUTION_REVIEW}:
            raise LifecycleError(f"cannot halt from terminal state {self.state.value}")
        self.status = RunStatus.HALTED
        self._record(RunState.HALTED, reason, at)

    def publish(
        self, status: RunStatus, gate_failures: list[str], *, at: str | None = None
    ) -> None:
        """Publish only when every publish-gate check passed."""
        if gate_failures:
            raise LifecycleError("publish gate failed: " + "; ".join(gate_failures))
        if status is RunStatus.HALTED:
            raise LifecycleError("use halt(): HALTED is not a publication status")
        self._move(RunState.PUBLISHED, f"status={status.value}", at)
        self.status = status

    def _move(self, target: RunState, note: str, at: str | None) -> None:
        budget_key = _REVISIONS.get((self.state, target))
        if budget_key is not None:
            used = self.revisions_used.get(budget_key, 0)
            if used >= REVISION_BUDGET[budget_key]:
                raise LifecycleError(
                    f"{budget_key} budget exhausted ({used}); publish NO_TRADE or halt"
                )
            self.revisions_used[budget_key] = used + 1
        elif target not in _FORWARD[self.state]:
            raise LifecycleError(
                f"illegal transition {self.state.value} -> {target.value}"
            )
        self._record(target, note, at)

    def _record(self, target: RunState, note: str, at: str | None) -> None:
        stamp = at or dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        self.log.append(Transition(self.state, target, stamp, note))
        self.state = target

    def transcript(self) -> str:
        """The manifest's state-transition line, generated rather than typed."""
        states = [RunState.PRECHECK.value] + [t.target.value for t in self.log]
        return " -> ".join(states)
