---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-17 16:30:52
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-001--ordered-realization-topology
    - CAPRMEDIO-REQU-031--model-project-structure-as-numbered-levels
---
# Acyclic layers with Ops feedback

The ordered layer graph is a directed acyclic graph:

- structural authority and refinement follow the cumulative topology defined
  by CAPRMEDIO-REQU-001--ordered-realization-topology;
- a later layer may consume authority from its own or any earlier layer;
- no layer may govern or redefine an earlier layer;
- dependency is distinct from scope specialization and `child_of`; and
- peer scopes interact through explicit Contracts rather than layer precedence.

A project Principle may directly parent a Core Requirement in any Layer. That applicability edge neither creates a Layer dependency nor requires intermediate Layers to restate the Principle.

An Ops fact from a later layer may become input to Exploration Mode. After explicit acceptance, the result enters the normal forward flow at its proper owning layer. This feedback is not a backward authority edge.

If backward coupling cannot be deleted, re-homed, or expressed as feedback, CAPRMEDIO proposes remodeling the coupled owners as horizontal Features. The operator must accept that structural change.
