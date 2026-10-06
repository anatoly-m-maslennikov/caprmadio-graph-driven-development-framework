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
      - CAPRMEDIO-GOV-METH-043--use-route-derived-identity-kinds
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-211--type-derived-artifact-routes
      - CAPRMEDIO-GOV-REQU-427--expandable-scope-path-identities
---

# Implementation Decision — Derive identity kind from the registered route

Each governed artifact declares one enabled canonical artifact type and, when
the catalog permits it, one direct subtype. That classification resolves to
exactly one semantic route and one visible identity kind.

Artifact IDs and filenames use the catalog's identity kind for the canonical
type, or the enabled subtype identity kind when project settings explicitly
select subtype-bearing names. No parallel parent-family hierarchy or hardcoded
type table determines identity.

A vocabulary change is a governed whole-graph migration: identifiers,
filenames, headings, and stored references change together, and superseded
aliases cease to be valid after cutover.

## Primary claim

Artifact identity kinds are derived from the single registered route
classification rather than a parallel or hardcoded type hierarchy.

## Rationale

The successor retains direct, readable identities without freezing exploratory
type names into implementation authority.
