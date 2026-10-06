---
subject_scope: artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-270--use-change-plans-and-implementation-record-projections
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections
      - CAPRMEDIO-GOV-REQU-472--register-development-backlog-projection
      - CAPRMEDIO-GOV-REQU-320--explicit-root-to-installed-methodology-sync-script
---

# Requirement — Register Change Plan and Implementation Record Projections

GOV registers two internal Projection Types with the Implementation Content role:

| Projection Type | Prefix | Contribution | Update rule |
|---|---|---|---|
| `change_plan` | `CPLN` | Accepted operative plan for changing the distributed specification and resulting implementation | Updated directly through governed planning while operative |
| `implementation_record` | `IREC` | Current view of realized specification, implementation bindings, native targets, commits, coverage, and gaps | Rebuilt from its declared source frontier |

A Change Plan lists governed artifacts to add, revise, replace, archive, or review; identifies resulting code, configuration, documentation, evaluation, and delivery changes; and records ordering, dependencies, completion conditions, and applicable scope. It coordinates the whole accepted change rather than only code implementation. It may cite Analysis Atoms, but neither the plan nor its acceptance promotes recommendations into normative truth. Each normative specification change remains an independently admitted Requirement, Method, Evaluation, or Delivery Atom.

An Implementation Record declares the exact normative-Atom, Implementation-Journal, native-target, and available Git frontier it represents. It reports the effective current state without creating implementation bindings or claiming evaluation, delivery success, or observed runtime behavior. Regeneration replaces its rendered content without converting it into an Atom.

Both carriers use Markdown with YAML frontmatter unless a registered generated representation requires another native carrier. Their filenames and IDs use their registered four-character prefixes and applicable scope path. They live in the applicable Implementation role location; the project-specific flat `400_LAYER_4_IMPLEMENTATION` exception remains governed separately.

The legacy `plan:implementation_plan` classification does not govern this model. Migration of executable catalogs and older carriers is downstream implementation work and does not alter the admitted meaning of these Projection Types.

## Primary claim

`change_plan` and `implementation_record` are the two registered internal Implementation-role Projection Types for operative whole-change planning and derived realization reporting.

## Rationale

Separate planning and reporting projections let Implementation coordinate future work and expose current realization without overloading Analysis, code-writing Method Atoms, immutable Implementation Atoms, or the canonical Implementation Journal.
