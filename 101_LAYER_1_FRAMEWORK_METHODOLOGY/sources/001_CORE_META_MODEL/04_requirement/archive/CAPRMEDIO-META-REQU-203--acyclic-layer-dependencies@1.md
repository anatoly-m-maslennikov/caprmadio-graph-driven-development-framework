---
subject_scope: scope-topology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-403--forward-only-layer-authority
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-201--canonical-layer-definitions
---

# Requirement — Keep layer dependencies acyclic

The ordered layer graph is a directed acyclic graph:

- authority and refinement flow `META → GOV → TOOL → SKILL → IMPL → OPS`;
- a later layer may consume authority from its own or any earlier layer;
- no layer may govern or redefine an earlier layer;
- dependency is distinct from scope specialization and `child_of`;
- peer features interact through explicit Contracts rather than layer
  precedence.

An Observation from a later layer may become input to Exploration Mode. After
explicit acceptance, the result enters the normal forward flow at its proper
owning layer. This feedback is not a backward authority edge.

If backward coupling cannot be deleted, re-homed, or expressed as feedback,
CAPRMEDIO proposes remodeling the coupled owners as horizontal features. The
operator must accept that structural change.

## Primary claim

CAPRMEDIO layer dependencies form an acyclic graph in which authority and refinement flow forward, later layers consume earlier authority, and feedback cannot create backward governance.

## Rationale

Separating authority flow, dependency direction, specialization, and feedback protects stable layers from volatile downstream mechanisms.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "operations"
  applies_unchanged: true
  local_context_required: false
```
