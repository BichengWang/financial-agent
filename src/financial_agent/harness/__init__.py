"""Deterministic harness for LLM-driven financial research runs (spike, v0).

The harness owns everything that must be exact -- arithmetic, provenance,
schemas, gates, and run lifecycle -- so the model only contributes judgment.
Skills (open Agent Skills format, ``SKILL.md`` directories) tell a model
*when and why* to call harness tools; the harness decides *what is allowed*.

Design and spike findings: ``plan/2026-09-28-financial-harness-and-skills.md``.
Standard library only, like the helpers in
``agents/equity/daily_investment_system/``.
"""

from financial_agent.harness.audit import AuditReport, audit_output_dir, audit_record
from financial_agent.harness.gates import StatusDecision, decide_status, investability
from financial_agent.harness.ledger import LedgerRow, SourceLedger
from financial_agent.harness.lifecycle import RunLifecycle, RunState
from financial_agent.harness.policy import Policy, load_policy
from financial_agent.harness.skills import Skill, SkillRegistry, validate_skill_dir

__all__ = [
    "AuditReport",
    "LedgerRow",
    "Policy",
    "RunLifecycle",
    "RunState",
    "Skill",
    "SkillRegistry",
    "SourceLedger",
    "StatusDecision",
    "audit_output_dir",
    "audit_record",
    "decide_status",
    "investability",
    "load_policy",
    "validate_skill_dir",
]
