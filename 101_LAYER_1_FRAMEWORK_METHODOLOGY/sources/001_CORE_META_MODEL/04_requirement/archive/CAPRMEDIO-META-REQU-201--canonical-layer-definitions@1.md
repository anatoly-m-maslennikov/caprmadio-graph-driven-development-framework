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
      - CAPRMEDIO-GOV-METH-039--place-executable-methodology-by-role
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-200--meta-eligibility-rule
---

# Requirement — Define the canonical layers

CAPRMEDIO uses the ordered flow `META → GOV → TOOL → SKILL → IMPL → OPS`.

| Layer | Canonical responsibility |
|---|---|
| META | Meanings, routing axes, universal invariants, layer topology, and inter-layer semantics |
| GOV | Governed carriers, identity, settings, provenance, lifecycle, applicability, scope, and conflict governance |
| TOOL | Executable CAPRMEDIO capabilities, validation, resolution, diagnostics, generation, and repository mechanics |
| SKILL | Thin provider-neutral orchestration, entry gates, workflow chaining, and session continuity |
| IMPL | Development environments, implementation profiles, code, automated Test implementations, Evaluation implementations, and code-quality gates |
| OPS | Post-implementation delivery, release, publication, runtime supportability, investigation, containment, recovery, and hosted evidence |

Each responsibility has one canonical owner. Later layers may realize or refine
earlier truth but cannot redefine an earlier layer's responsibility.

## Primary claim

CAPRMEDIO uses the ordered layers META, GOV, TOOL, SKILL, IMPL, and OPS, with one canonical non-overlapping responsibility assigned to each layer.

## Rationale

Stable layer definitions make ownership and dependency direction understandable without relying on directory names or current implementation details.


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
