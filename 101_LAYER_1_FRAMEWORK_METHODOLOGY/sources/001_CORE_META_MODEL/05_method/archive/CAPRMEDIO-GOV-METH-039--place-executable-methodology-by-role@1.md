---
artifact_subtype: implementation_decision
subject_scopes:
  - methodology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-038--install-executable-methodology
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-METH-032--separate-methodology-from-applied-project-artifacts
---

# Decision — Place executable methodology by semantic role

DSET uses the ordered flow `META → GOV → TOOL → SKILL → IMPL → OPS`.

TOOL owns the DSET executable product contract: CLI behavior, schemas,
templates, fixtures, validation and diagnostics, traceability, lifecycle
mechanics, and self-hosting behavior.

SKILL owns agent-facing orchestration over those executable contracts.

IMPL owns development realization: environment and dependency setup,
production code, automated Test code, Evaluation implementations, code-focused
quality gates, and concrete implementation profiles. Installed methodology
therefore materializes the repository Python package under IMPL `100_python`,
the deterministic Test package under IMPL `110_tests`, and reusable Evaluation
prompts under IMPL `120_evaluations`.

OPS owns what follows implementation: CI delivery, release and publication,
runtime operation and investigation, containment, recovery, escalation, and
hosted evidence. An operational deficiency creates or updates upstream
authority for a later implementation; OPS does not directly rewrite IMPL.

Applied QA definitions, plans, evidence, and Verification remain with their
project or layer owners. Installed reusable implementations do not become
project results or evaluation.

This Decision completely replaces `CAPRMEDIO-GOV-METH-038--install-executable-methodology`. The prior atom
remains immutable history; current evergreen truth compiles this separation.

## Primary claim

Installed methodology separates the DSET executable contract in TOOL from development environments and implementations in IMPL, while OPS owns only post-implementation operation and delivery.

## Rationale

Executable behavior, implementation technique, and post-implementation operation are different owners; separating them removes backward OPS-to-IMPL authority and makes recursive self-hosting inspectable.
