---
artifact_subtype: implementation_decision
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-018--fpf-aligned-boundaries-for-the-flat-type-model
  - type: resolution_of
    targets:
      - CAPRMEDIO-GOV-CONC-045--requirements-versus-implementation-decisions
---

# Decision — Separate Requirements from Decisions

DSET has five peer semantic Types:

- **Requirement** — required observable results, behavior, capabilities,
  qualities, limits, and obligations;
- **Decision** — a material selected implementation, architecture, governance,
  or operating approach, normally with rationale and alternatives;
- **Question** — unresolved knowledge, interpretation, or choice;
- **Problem** — a currently true insufficiency;
- **QA** — a Test or Evaluation definition.

Constraint, Contract, User Story, Outcome, Scenario, and Invariant are direct
Requirement subtypes. Decision has no subtype. Question, Problem, and QA retain
their current direct subtype sets. No subtype contains another subtype.

Origin does not determine classification. A mandated approach is a Requirement
when the project has no discretion. A project-selected approach is a Decision.
Routine implementation detail remains implementation and does not require an
atom merely because code contains a choice.

This Decision completely replaces `CAPRMEDIO-GOV-METH-018--fpf-aligned-boundaries-for-the-flat-type-model`. The predecessor
remains immutable history and is removed from the active authority set through
its append-only absorption event.

## Primary claim

DSET uses peer Requirement and Decision Types: Requirements state required results or obligations, while Decisions record material selected implementation, architecture, governance, or operating approaches.

## Rationale

The previous Decision-parent model obscures the practical WHAT-versus-selected-HOW boundary. Peer Types preserve both required truth and the rationale for consequential choices without classifying routine code as authority.
